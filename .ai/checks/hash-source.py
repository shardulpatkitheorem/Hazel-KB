#!/usr/bin/env python3
"""
Compute the content_sha256 for a knowledge base source.

For parsed transcripts and other markdown, the digest covers the BODY ONLY —
everything after the YAML frontmatter — with line endings normalised. This
means correcting a title or adding a tag does not invalidate decision records
citing that transcript, while altering the transcript itself does.

See .ai/checks/content_hash.py for the full rationale.

Usage:
    python .ai/checks/hash-source.py 01-transcripts/daily-calls/parsed/x.md
    python .ai/checks/hash-source.py --json 01-transcripts/daily-calls/parsed/*.md
    python .ai/checks/hash-source.py --show-scope x.md    # what is being hashed
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_hash import hash_body, hash_bytes, split_frontmatter, TEXT_SUFFIXES

REPO = Path(__file__).resolve().parents[2]


def relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO)).replace("\\", "/")
    except ValueError:
        return str(path)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--show-scope", action="store_true",
                    help="report which region of the file is hashed")
    args = ap.parse_args()

    results, failed = [], False
    for raw in args.paths:
        path = Path(raw)
        if not path.is_absolute():
            path = (REPO / raw) if (REPO / raw).exists() else path.resolve()
        if not path.is_file():
            sys.stderr.write(f"error: not a file: {raw}\n")
            failed = True
            continue

        is_text = path.suffix.lower() in TEXT_SUFFIXES
        has_fm = False
        body_lines = None
        if is_text:
            with path.open(encoding="utf-8", newline="") as fh:
                text = fh.read()
            fm, body = split_frontmatter(text)
            has_fm = fm is not None
            body_lines = len(body.splitlines())

        results.append({
            "path": relative(path),
            "content_sha256": hash_body(path),
            "scope": ("body after frontmatter" if has_fm
                      else "whole file" if is_text else "raw bytes"),
            "body_lines": body_lines,
            "bytes": path.stat().st_size,
            "whole_file_sha256": hash_bytes(path) if args.show_scope else None,
        })

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"{r['content_sha256']}  {r['path']}")
            if args.show_scope:
                detail = f"  scope: {r['scope']}"
                if r["body_lines"] is not None:
                    detail += f" ({r['body_lines']} lines)"
                print(detail)
                print(f"  whole file: {r['whole_file_sha256']}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
