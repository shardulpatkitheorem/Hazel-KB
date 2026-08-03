#!/usr/bin/env python3
"""
Content hashing for knowledge base sources.

Shared by ingest-transcript.py, hash-source.py and validate.py so all three
compute the same digest. Import it; do not reimplement.

WHY BODY-ONLY
-------------
A parsed transcript is YAML frontmatter followed by the transcript body. If the
digest covered the whole file, correcting a title or adding a tag would change
it, and every decision record citing that transcript would fail validation for
a cosmetic edit.

So the digest covers the body only — everything after the closing `---` of the
frontmatter. Metadata corrections are free; altering a word of transcript is
not. The body is also exactly the region evidence anchors point into.

NORMALISATION
-------------
Line endings are normalised to LF and trailing whitespace is stripped before
hashing. This repository is CRLF on disk with no .gitattributes, so a file
checked out on a Linux CI runner would otherwise hash differently from the same
file on a Windows machine. The digest must not depend on who checked it out.

Files with no frontmatter are hashed whole, with the same normalisation.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

FRONTMATTER_FENCE = "---"
TEXT_SUFFIXES = {".md", ".markdown", ".txt"}


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter, body). Frontmatter is None when absent.

    Recognises a leading `---` fence, tolerating a UTF-8 BOM and CRLF.
    """
    stripped = text.lstrip("\ufeff")
    normalised = stripped.replace("\r\n", "\n").replace("\r", "\n")

    if not normalised.startswith(FRONTMATTER_FENCE + "\n"):
        return None, normalised

    end = normalised.find("\n" + FRONTMATTER_FENCE, len(FRONTMATTER_FENCE))
    if end == -1:
        # Opening fence with no close — treat the whole file as body.
        return None, normalised

    body_start = normalised.find("\n", end + 1 + len(FRONTMATTER_FENCE))
    if body_start == -1:
        return normalised[:end], ""

    return normalised[:end], normalised[body_start + 1:]


def normalise(text: str) -> str:
    """LF line endings, no trailing whitespace per line, single trailing LF."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    return "\n".join(line.rstrip() for line in lines).rstrip("\n") + "\n"


def hash_text(body: str) -> str:
    return hashlib.sha256(normalise(body).encode("utf-8")).hexdigest()


def hash_body(path: Path) -> str:
    """Digest of a source file's body, excluding YAML frontmatter.

    Binary and unrecognised text formats are hashed over their raw bytes, since
    they have no frontmatter to exclude and no line endings to normalise.
    """
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    with path.open(encoding="utf-8", newline="") as fh:
        text = fh.read()
    _, body = split_frontmatter(text)
    return hash_text(body)


def hash_bytes(path: Path) -> str:
    """Digest over raw bytes. For comparison and for non-text sources."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
