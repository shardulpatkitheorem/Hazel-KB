#!/usr/bin/env python3
"""
Allocate the next record id.

ID allocation must be deterministic. A model asked to "pick the next number"
will occasionally reuse one, and a duplicate id in the ledger is a silent
corruption that only surfaces later. This scans what exists and answers.

IDs are identifiers, not sequence. The next id is max+1 over what is present,
which says nothing about chronology — order by decided_on, never by id.

Usage:
    python .ai/checks/next-id.py decision              -> DEC-015
    python .ai/checks/next-id.py question --count 3    -> Q-010 Q-011 Q-012
    python .ai/checks/next-id.py ticket --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LEDGER = REPO / "04-iteration-ledger"

KINDS = {
    "decision": {"dir": LEDGER / "decisions", "prefix": "DEC", "width": 3},
    "question": {"dir": LEDGER / "questions", "prefix": "Q", "width": 3},
    "ticket": {"dir": LEDGER / "tickets", "prefix": "TKT", "width": 4},
}


def scan(kind: str) -> tuple[int, list[str]]:
    """Return (highest number seen, all ids found)."""
    spec = KINDS[kind]
    pattern = re.compile(rf"^{spec['prefix']}-([0-9]+)$")
    highest = 0
    found: list[str] = []

    if not spec["dir"].is_dir():
        return highest, found

    for path in sorted(spec["dir"].glob("*.json")):
        # Prefer the id inside the file; fall back to the filename.
        rec_id = None
        try:
            rec_id = json.loads(path.read_text(encoding="utf-8")).get("id")
        except (json.JSONDecodeError, OSError):
            pass
        candidate = rec_id or path.stem

        m = pattern.match(candidate)
        if not m:
            sys.stderr.write(
                f"warning: {path.name} has id {candidate!r}, which does not "
                f"match {spec['prefix']}-<digits>\n"
            )
            continue
        found.append(candidate)
        highest = max(highest, int(m.group(1)))

    dupes = {i for i in found if found.count(i) > 1}
    if dupes:
        sys.stderr.write(f"error: duplicate ids in {spec['dir'].name}: "
                         f"{', '.join(sorted(dupes))}\n")
        raise SystemExit(1)

    return highest, found


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("kind", choices=sorted(KINDS))
    ap.add_argument("--count", type=int, default=1,
                    help="allocate several consecutive ids")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.count < 1:
        sys.stderr.write("error: --count must be at least 1\n")
        return 2

    spec = KINDS[args.kind]
    highest, existing = scan(args.kind)

    ids = [
        f"{spec['prefix']}-{n:0{spec['width']}d}"
        for n in range(highest + 1, highest + 1 + args.count)
    ]

    if args.json:
        print(json.dumps({
            "kind": args.kind,
            "next": ids,
            "existing_count": len(existing),
            "highest_existing": (
                f"{spec['prefix']}-{highest:0{spec['width']}d}" if highest else None
            ),
            "directory": str(spec["dir"].relative_to(REPO)),
        }, indent=2))
    else:
        print(" ".join(ids))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
