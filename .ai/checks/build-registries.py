#!/usr/bin/env python3
"""
Generate the markdown registries from the JSON records.

04-ledger/decisions.md and open-questions.md describe themselves as
derived indexes. Nothing generated them, so they were a hand-maintained second
source of truth that drifted from the records. This makes the claim true.

The generated files carry a DO NOT EDIT banner and a content hash. Editing one
by hand and re-running restores it; --check fails if a registry is out of date,
so CI catches drift.

Usage:
    python .ai/checks/build-registries.py            # write the registries
    python .ai/checks/build-registries.py --check    # fail if out of date
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LEDGER = REPO / "04-ledger"

BANNER = (
    "<!-- GENERATED FILE — DO NOT EDIT.\n"
    "     Source of truth: {source}\n"
    "     Regenerate:      python .ai/checks/build-registries.py\n"
    "     Records hash:    {digest} -->\n"
)


def load_records(directory: Path) -> list[dict]:
    if not directory.is_dir():
        return []
    out = []
    for path in sorted(directory.glob("*.json")):
        try:
            out.append(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError) as exc:
            sys.stderr.write(f"error: cannot read {path}: {exc}\n")
            raise SystemExit(2)
    return out


def records_digest(records: list[dict]) -> str:
    blob = json.dumps(records, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode()).hexdigest()[:16]


def by_decided(rec: dict) -> tuple:
    """Order by date, never by id."""
    return (rec.get("decided_on") or rec.get("raised_on") or "", rec.get("id", ""))


def origin_line(rec: dict) -> str:
    o = rec.get("origin", {})
    kind = o.get("kind")
    if kind == "meeting":
        return f"`{o.get('transcript_path','?')}` ({o.get('meeting_date','?')})"
    if kind == "document":
        return f"`{o.get('document_path','?')}`"
    if kind == "internal":
        return f"internal — {o.get('decided_by') or o.get('raised_by','?')}"
    return "unknown"


def evidence_line(rec: dict) -> str:
    ev = rec.get("evidence", [])
    if not ev:
        return "—"
    return ", ".join(f"`{e['location']}`" for e in ev)


def routing_line(rec: dict) -> str:
    routes = rec.get("routing") or []
    if not routes:
        return "—"
    return ", ".join(f"{r['repo']}/{r['area']}" for r in routes)


# ---------------------------------------------------------------------------


def build_decisions(records: list[dict]) -> str:
    active = sorted([r for r in records if r.get("status") == "active"], key=by_decided)
    superseded = sorted([r for r in records if r.get("status") == "superseded"], key=by_decided)

    lines = [
        BANNER.format(source="04-ledger/decisions/*.json",
                      digest=records_digest(records)),
        "# Decision Registry",
        "",
        f"{len(active)} active · {len(superseded)} superseded · "
        f"generated {date.today().isoformat()}",
        "",
        "Ordered by decision date. Decision IDs are identifiers, not sequence — "
        "never infer chronology from them.",
        "",
    ]

    if not records:
        lines += ["_No decisions recorded._", ""]
        return "\n".join(lines)

    lines += ["## Active", ""]
    if active:
        lines += [
            "| ID | Decision | Decided | Owner | Routes to | Spec |",
            "|---|---|---|---|---|---|",
        ]
        for r in active:
            impact = r.get("spec_impact", "—")
            flag = "⚠ pending" if impact == "pending" else impact
            lines.append(
                f"| `{r['id']}` | {r['title']} | {r.get('decided_on','—')} | "
                f"{r.get('owner','—')} | {routing_line(r)} | {flag} |"
            )
        lines.append("")
    else:
        lines += ["_None._", ""]

    lines += ["## Detail", ""]
    for r in active:
        lines += [
            f"### {r['id']} — {r['title']}",
            "",
            r.get("statement", ""),
            "",
            f"- **Decided** {r.get('decided_on','—')} by {r.get('owner','—')}"
            + (f" · recorded {r['recorded_on']}"
               if r.get("recorded_on") != r.get("decided_on") else ""),
            f"- **Source** {origin_line(r)}",
            f"- **Evidence** {evidence_line(r)}",
            f"- **Routes to** {routing_line(r)}",
            f"- **Spec impact** {r.get('spec_impact','—')}",
        ]
        if r.get("implemented_by"):
            lines.append("- **Implemented by** "
                         + ", ".join(r["implemented_by"]))
        if r.get("supersedes"):
            lines.append(f"- **Supersedes** `{r['supersedes']}`")
        appr = r.get("approval", {})
        if appr:
            lines.append(f"- **Approved by** {appr.get('approved_by','—')} "
                         f"on {appr.get('approved_at','—')[:10]}")
        lines.append("")

    if superseded:
        lines += ["## Superseded", "",
                  "| ID | Decision | Decided | Superseded by |",
                  "|---|---|---|---|"]
        for r in superseded:
            lines.append(
                f"| `{r['id']}` | {r['title']} | {r.get('decided_on','—')} | "
                f"`{r.get('superseded_by','—')}` |"
            )
        lines.append("")

    return "\n".join(lines)


def build_questions(records: list[dict]) -> str:
    order = {"blocked": 0, "open": 1, "answered": 2}
    live = sorted([r for r in records if r.get("status") in ("open", "blocked")],
                  key=lambda r: (order.get(r.get("status"), 9), by_decided(r)))
    answered = sorted([r for r in records if r.get("status") == "answered"],
                      key=by_decided)

    lines = [
        BANNER.format(source="04-ledger/questions/*.json",
                      digest=records_digest(records)),
        "# Open Questions",
        "",
        f"{len(live)} outstanding · {len(answered)} answered · "
        f"generated {date.today().isoformat()}",
        "",
    ]

    if not records:
        lines += ["_No questions recorded._", ""]
        return "\n".join(lines)

    lines += ["## Outstanding", ""]
    if live:
        lines += [
            "| ID | Question | Owner | Due | Raised | Blocks |",
            "|---|---|---|---|---|---|",
        ]
        for r in live:
            due = r.get("due_date", "—")
            if due == "unknown":
                due = "⚠ no date"
            blocks = ", ".join(f"`{b}`" for b in r.get("blocking", [])) or "—"
            owner = r.get("owner", "—")
            if owner == "unknown":
                owner = "⚠ unowned"
            lines.append(
                f"| `{r['id']}` | {r['title']} | {owner} | {due} | "
                f"{r.get('raised_on','—')} | {blocks} |"
            )
        lines.append("")
    else:
        lines += ["_None._", ""]

    lines += ["## Detail", ""]
    for r in live:
        lines += [
            f"### {r['id']} — {r['title']}",
            "",
            r.get("question", ""),
            "",
            f"- **Owner** {r.get('owner','—')}"
            + (f" · due {r['due_date']}"
               if r.get("due_date") and r["due_date"] != "unknown"
               else " · no committed date"),
            f"- **Raised** {r.get('raised_on','—')} · {origin_line(r)}",
            f"- **Evidence** {evidence_line(r)}",
        ]
        if r.get("blocking"):
            lines.append("- **Blocks** "
                         + ", ".join(f"`{b}`" for b in r["blocking"]))
        if r.get("routing"):
            lines.append(f"- **Concerns** {routing_line(r)}")
        lines.append("")

    if answered:
        lines += ["## Answered", "",
                  "| ID | Question | Answered | Resolved by |",
                  "|---|---|---|---|"]
        for r in answered:
            a = r.get("answer") or {}
            lines.append(
                f"| `{r['id']}` | {r['title']} | {a.get('answered_on','—')} | "
                f"`{a.get('resolved_by','—')}` |"
            )
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="fail if a registry is out of date; write nothing")
    args = ap.parse_args()

    targets = [
        (LEDGER / "decisions.md", build_decisions(load_records(LEDGER / "decisions"))),
        (LEDGER / "open-questions.md", build_questions(load_records(LEDGER / "questions"))),
    ]

    stale, wrote = [], []
    for path, content in targets:
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current == content:
            continue
        if args.check:
            stale.append(path)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            wrote.append(path)

    if args.check:
        if stale:
            for p in stale:
                print(f"STALE  {p.relative_to(REPO)}")
            print("\nFAIL   registries are out of date")
            print("       run: python .ai/checks/build-registries.py")
            return 1
        print("PASS   registries are up to date")
        return 0

    if wrote:
        for p in wrote:
            print(f"WROTE  {p.relative_to(REPO)}")
    else:
        print("OK     registries already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
