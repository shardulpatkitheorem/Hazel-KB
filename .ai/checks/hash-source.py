#!/usr/bin/env python3
"""
Compute the content_sha256 for a source file.

The digest is taken over the raw bytes of the file as committed. Use the value
this prints in a record's origin.content_sha256; validate.py re-computes it and
fails if the source has changed since the record was written.

Usage:
    python .ai/checks/hash-source.py 01-transcripts/2026-07-30-standup.md
    python .ai/checks/hash-source.py --json 01-transcripts/*.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="source file(s) to hash")
    ap.add_argument("--json", action="store_true")
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
        try:
            rel = str(path.relative_to(REPO))
        except ValueError:
            rel = str(path)
        results.append({"path": rel, "content_sha256": digest(path),
                        "bytes": path.stat().st_size})

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"{r['content_sha256']}  {r['path']}  ({r['bytes']} bytes)")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
