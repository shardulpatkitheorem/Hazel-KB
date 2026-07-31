#!/usr/bin/env python3
"""Ingest a meeting transcript into the Hazel knowledge base.

Performs the ingestion convention documented in
``01-transcripts/daily-calls/README.md``: preserve the received file in
``raw/``, write a searchable Markdown copy with YAML metadata to ``parsed/``,
and add the meeting to the transcript index.

Extraction is standard-library only for ``.txt`` and ``.docx`` sources. PDF
sources additionally require ``pdfplumber``, or pre-extracted text supplied
via ``--text-file``.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRANSCRIPTS_ROOT = REPO_ROOT / "01-transcripts"

WORD_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

# Link label used in the index for each original source type.
SOURCE_LABELS = {
    ".pdf": "PDF",
    ".txt": "Text",
    ".docx": "Word",
    ".md": "Markdown",
}

VERBATIM_SUFFIXES = {".txt", ".md"}

# Title and tag defaults keyed by a substring of the slug. Presets exist so the
# common case needs no flags; anything unrecognised must be named explicitly
# rather than guessed into a committed file.
PRESETS: tuple[tuple[str, str | None, tuple[str, ...]], ...] = (
    ("standup", "Daily HOP Standup", ("daily-standup", "hop", "project-status")),
    ("kickoff", None, ("onboarding", "kickoff", "requirements")),
)

DATED_NAME_PATTERN = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

INDEX_HEADER = "| Date | Meeting | Searchable transcript | Original source |"
INDEX_DIVIDER = "| --- | --- | --- | --- |"


class IngestError(Exception):
    """A problem the user can act on, reported without a traceback."""


# --- text I/O ---------------------------------------------------------------
#
# The repository is CRLF throughout and carries no .gitattributes, so every
# read and write disables newline translation. Letting Python normalise would
# break byte-identity of parsed bodies and turn a one-row index edit into a
# whole-file diff.


def read_text(path: Path) -> str:
    with path.open(encoding="utf-8", newline="") as handle:
        return handle.read()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def detect_newline(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def apply_newline(text: str, newline: str) -> str:
    """Normalise any mix of line endings in *text* to *newline*."""
    return text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", newline)


# --- extraction -------------------------------------------------------------


def extract_docx(path: Path, newline: str) -> str:
    """Extract paragraph text from a .docx using only the standard library.

    A .docx is a zip of XML. Walking ``w:p`` paragraphs and joining their
    ``w:t`` runs reproduces the Teams meeting-transcript export: ``w:br``
    elements supply the blank line that separates speaker blocks, and ``w:tab``
    is preserved as a tab.
    """
    try:
        with zipfile.ZipFile(path) as archive:
            document = archive.read("word/document.xml")
    except (zipfile.BadZipFile, KeyError) as error:
        raise IngestError(f"{path.name} is not a readable .docx file ({error}).") from error

    root = ET.fromstring(document)
    paragraphs: list[str] = []
    for paragraph in root.iter(f"{WORD_NS}p"):
        runs: list[str] = []
        for node in paragraph.iter():
            if node.tag == f"{WORD_NS}t":
                runs.append(node.text or "")
            elif node.tag == f"{WORD_NS}tab":
                runs.append("\t")
            elif node.tag == f"{WORD_NS}br":
                runs.append("\n")
        paragraphs.append("".join(runs))

    return apply_newline("\n".join(paragraphs), newline)


def extract_pdf(path: Path, newline: str) -> str:
    try:
        import pdfplumber
    except ImportError as error:
        raise IngestError(
            f"Reading {path.name} needs a PDF text extractor, which is not installed.\n"
            "  Either:  pip install pdfplumber\n"
            "  Or:      extract the text yourself and re-run with "
            "--text-file <path>"
        ) from error

    pages: list[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            pages.append(page.extract_text() or "")
    return apply_newline("\n".join(pages), newline)


def extract_body(source: Path, newline: str) -> str:
    """Return the transcript body for *source*.

    Plain-text sources are copied through untouched so that the parsed body is
    byte-identical to the original.
    """
    suffix = source.suffix.lower()
    if suffix in VERBATIM_SUFFIXES:
        return read_text(source)
    if suffix == ".docx":
        return extract_docx(source, newline)
    if suffix == ".pdf":
        return extract_pdf(source, newline)
    raise IngestError(
        f"No extractor for '{suffix}' files. Supply pre-extracted text with --text-file."
    )


# --- parsed document --------------------------------------------------------


def build_document(
    title: str,
    date: str,
    tags: list[str],
    source_name: str,
    body: str,
    newline: str,
) -> str:
    """Assemble the parsed Markdown file.

    The frontmatter is written literally rather than through a YAML serialiser
    so that quoting and indentation match the existing parsed files exactly.
    """
    lines = [
        "---",
        f'title: "{title}"',
        'document_type: "transcript"',
        'source: "meeting"',
        'client: "Hazel"',
        f'date: "{date}"',
        'status: "parsed"',
        'version: "1.0"',
        "tags:",
        *[f'  - "{tag}"' for tag in tags],
        'confidentiality: "client-confidential"',
        f'source_file: "../raw/{source_name}"',
        "---",
        "",
        f"# {title}",
        "",
        "## Transcript",
        "",
    ]
    header = newline.join(lines) + newline
    if not body.endswith(newline):
        body += newline
    return header + body


# --- transcript index -------------------------------------------------------


def build_index_row(date: str, title: str, basename: str, suffix: str) -> str:
    label = SOURCE_LABELS.get(suffix.lower(), suffix.lstrip(".").upper())
    return (
        f"| {date} | {title} "
        f"| [Markdown](parsed/{basename}.md) "
        f"| [{label}](raw/{basename}{suffix}) |"
    )


def row_sort_key(row: str) -> tuple[str, str]:
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    date = cells[0] if cells else ""
    link = re.search(r"\(parsed/(.+?)\.md\)", row)
    return (date, link.group(1) if link else "")


def update_index(readme_text: str, row: str, basename: str) -> str:
    """Insert or replace *row* in the transcript index, keeping date order.

    Replacing by basename rather than appending keeps re-runs idempotent.
    Every byte outside the table is left alone.
    """
    newline = detect_newline(readme_text)
    lines = readme_text.split(newline)

    try:
        header_index = next(
            index for index, line in enumerate(lines) if line.strip() == INDEX_HEADER
        )
    except StopIteration:
        raise IngestError(
            "Could not find the transcript index table header in the README:\n"
            f"  {INDEX_HEADER}"
        ) from None

    start = header_index + 1
    if start < len(lines) and lines[start].strip() == INDEX_DIVIDER:
        start += 1
    end = start
    while end < len(lines) and lines[end].strip().startswith("|"):
        end += 1

    marker = f"(parsed/{basename}.md)"
    rows = [line for line in lines[start:end] if marker not in line]
    rows.append(row)
    rows.sort(key=row_sort_key)

    return newline.join(lines[:start] + rows + lines[end:])


# --- metadata resolution ----------------------------------------------------


def resolve_preset(slug: str) -> tuple[str | None, tuple[str, ...] | None]:
    for keyword, title, tags in PRESETS:
        if keyword in slug:
            return title, tags
    return None, None


def resolve_naming(source: Path, args: argparse.Namespace) -> tuple[str, str]:
    """Return (date, slug), preferring explicit flags over the filename."""
    date, slug = args.date, args.slug
    match = DATED_NAME_PATTERN.match(source.stem)
    if match:
        date = date or match.group(1)
        slug = slug or match.group(2)
    else:
        slug = slug or source.stem

    if not date:
        raise IngestError(
            f"Cannot determine the meeting date: '{source.name}' is not named "
            "YYYY-MM-DD-descriptive-name.ext. Pass --date YYYY-MM-DD."
        )
    if not DATE_PATTERN.match(date):
        raise IngestError(f"--date must be YYYY-MM-DD, got '{date}'.")
    if not SLUG_PATTERN.match(slug):
        raise IngestError(
            f"Slug '{slug}' must be lowercase kebab-case. Pass --slug explicitly."
        )
    return date, slug


def resolve_metadata(slug: str, args: argparse.Namespace) -> tuple[str, list[str]]:
    preset_title, preset_tags = resolve_preset(slug)

    title = args.title or preset_title
    if not title:
        raise IngestError(
            f"No title for '{slug}' and no preset matches it. Pass "
            '--title "Meeting Name".'
        )

    if args.tags:
        tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    elif preset_tags:
        tags = list(preset_tags)
    else:
        raise IngestError(
            f"No tags for '{slug}' and no preset matches it. Pass --tags a,b,c."
        )
    return title, tags


# --- main -------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ingest a meeting transcript into the Hazel knowledge base.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "examples:\n"
            "  ingest-transcript.py ~/Downloads/2026-07-28-daily-hop-standup.txt\n"
            '  ingest-transcript.py notes.pdf --date 2026-07-28 --slug hazel-review \\\n'
            '      --title "Hazel Design Review" --tags design,review\n'
        ),
    )
    parser.add_argument("source", type=Path, help="transcript file to ingest")
    parser.add_argument("--date", help="meeting date (YYYY-MM-DD); inferred from the filename")
    parser.add_argument("--slug", help="kebab-case name; inferred from the filename")
    parser.add_argument("--title", help="meeting title for the frontmatter, heading, and index")
    parser.add_argument("--tags", help="comma-separated frontmatter tags")
    parser.add_argument(
        "--text-file",
        type=Path,
        help="use this pre-extracted text as the body instead of reading the source",
    )
    parser.add_argument(
        "--collection",
        default="daily-calls",
        help="subdirectory of 01-transcripts/ to ingest into (default: daily-calls)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        help="write the parsed file here instead; skips the raw copy and the index update",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would change without writing anything",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite existing raw and parsed files",
    )
    return parser.parse_args(argv)


def ingest(args: argparse.Namespace) -> int:
    source = args.source
    if not source.is_file():
        raise IngestError(f"Source file not found: {source}")

    date, slug = resolve_naming(source, args)
    title, tags = resolve_metadata(slug, args)

    basename = f"{date}-{slug}"
    suffix = source.suffix.lower()
    collection = TRANSCRIPTS_ROOT / args.collection
    raw_path = collection / "raw" / f"{basename}{suffix}"
    standalone = args.out_dir is not None
    parsed_dir = args.out_dir if standalone else collection / "parsed"
    parsed_path = parsed_dir / f"{basename}.md"
    readme_path = collection / "README.md"

    if not standalone and not collection.is_dir():
        raise IngestError(f"No such transcript collection: {collection}")

    # Step 1: preserve the original in raw/ under the conventional name.
    copy_raw = not standalone and source.resolve() != raw_path.resolve()
    if copy_raw and raw_path.exists() and not args.force:
        raise IngestError(f"{raw_path} already exists. Re-run with --force to replace it.")
    if parsed_path.exists() and not args.force:
        raise IngestError(f"{parsed_path} already exists. Re-run with --force to replace it.")

    # Step 2: obtain the transcript body.
    if args.text_file:
        if not args.text_file.is_file():
            raise IngestError(f"--text-file not found: {args.text_file}")
        raw_body = read_text(args.text_file)
    else:
        raw_body = None

    newline = detect_newline(raw_body) if raw_body is not None else "\r\n"
    body = raw_body if raw_body is not None else extract_body(source, newline)
    if raw_body is None and source.suffix.lower() in VERBATIM_SUFFIXES:
        newline = detect_newline(body)

    document = build_document(title, date, tags, f"{basename}{suffix}", body, newline)

    # Step 3: index row.
    row = build_index_row(date, title, basename, suffix)
    updated_readme = None
    if not standalone:
        if not readme_path.is_file():
            raise IngestError(f"No README to index into: {readme_path}")
        readme_text = read_text(readme_path)
        updated_readme = update_index(readme_text, row, basename)
        if updated_readme == readme_text:
            updated_readme = None

    action = "Would write" if args.dry_run else "Wrote"
    if copy_raw:
        print(f"{action.replace('write', 'copy')} {_rel(raw_path)}  <- {source}")
    print(f"{action} {_rel(parsed_path)}  ({len(body.splitlines())} lines of transcript)")
    if updated_readme is not None:
        print(f"{action.replace('write', 'index')} {_rel(readme_path)}")
        print(f"  {row}")
    elif not standalone:
        print(f"Index row in {_rel(readme_path)} already up to date.")

    if args.dry_run:
        return 0

    if copy_raw:
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, raw_path)
    write_text(parsed_path, document)
    if updated_readme is not None:
        write_text(readme_path, updated_readme)
    return 0


def _rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        return ingest(args)
    except IngestError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
