#!/usr/bin/env python3
"""
Dispatch an approved decision to the repository that must act on it.

Reads a decision record, creates one ticket per routing entry, and opens a
GitHub issue for each. The ticket carries the decision's statement, reasoning
and evidence forward unchanged, so the receiving engineer needs nothing else.

Dispatch is NOT a second gate. Authorisation comes from the librarian approval
already on the decision; this only delivers it. A decision without an approval
block cannot be dispatched.

Usage:
    python .ai/checks/dispatch.py DEC-001 --dry-run
    python .ai/checks/dispatch.py DEC-001
    python .ai/checks/dispatch.py --pending          # list what is undispatched
    python .ai/checks/dispatch.py DEC-001 --no-github  # write tickets only
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LEDGER = REPO / "04-ledger"
DECISIONS = LEDGER / "decisions"
QUESTIONS = LEDGER / "questions"
TICKETS = LEDGER / "tickets"
TARGETS = REPO / ".ai" / "contracts" / "repo-targets.json"


def regenerate_registries() -> bool:
    """Regenerate the markdown registries after writing to the ledger.

    Any script that changes a record leaves decisions.md and open-questions.md
    stale, and CI rejects a stale registry. Doing it here rather than printing a
    reminder removes a step nobody remembers.
    """
    script = Path(__file__).resolve().parent / "build-registries.py"
    if not script.is_file():
        sys.stderr.write(f"warning: {script.name} not found; registries not "
                         f"regenerated\n")
        return False
    result = subprocess.run([sys.executable, str(script)],
                            capture_output=True, text=True, cwd=REPO)
    if result.returncode != 0:
        sys.stderr.write("warning: build-registries.py failed:\n"
                         + result.stderr.strip() + "\n")
        return False
    for line in result.stdout.splitlines():
        if line.startswith("WROTE"):
            print(line)
    return True


def die(message: str, hint: str = "") -> None:
    sys.stderr.write(f"error: {message}\n")
    if hint:
        sys.stderr.write(f"       {hint}\n")
    raise SystemExit(1)


def load(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        die(f"not found: {path.relative_to(REPO)}")
    except json.JSONDecodeError as exc:
        die(f"invalid JSON in {path.relative_to(REPO)}: {exc.msg}")


def next_ticket_id() -> int:
    highest = 0
    if TICKETS.is_dir():
        for path in TICKETS.glob("TKT-*.json"):
            try:
                highest = max(highest, int(path.stem.split("-")[1]))
            except (IndexError, ValueError):
                continue
    return highest + 1


def existing_tickets_for(decision_id: str) -> list[dict]:
    out = []
    if TICKETS.is_dir():
        for path in sorted(TICKETS.glob("TKT-*.json")):
            doc = load(path)
            if doc.get("decision_id") == decision_id:
                out.append(doc)
    return out


def related_questions(decision_id: str) -> list[str]:
    out = []
    if QUESTIONS.is_dir():
        for path in sorted(QUESTIONS.glob("Q-*.json")):
            doc = load(path)
            if decision_id in doc.get("blocking", []) and doc.get("status") != "answered":
                out.append(doc["id"])
    return out


def question_detail(qid: str) -> dict | None:
    path = QUESTIONS / f"{qid}.json"
    return load(path) if path.is_file() else None


# ---------------------------------------------------------------------------


def acceptance_criteria(decision: dict, route: dict) -> list[str]:
    """A starting checklist. The receiving engineer refines it in the spec."""
    return [
        f"A spec change exists in {route['repo']} covering the behaviour in "
        f"{decision['id']}, in the {route['area']} area.",
        f"Every requirement added or modified by that change cites "
        f"[{decision['id']}] in its requirement text.",
        "Each new or modified requirement has at least one scenario.",
        "The implementation satisfies the changed spec, and the PR references "
        "this issue.",
    ]


def build_ticket(decision: dict, route: dict, ticket_id: str,
                 questions: list[str]) -> dict:
    approval = decision.get("approval") or {}
    return {
        "schema_version": "1.0",
        "id": ticket_id,
        "decision_id": decision["id"],
        "title": decision["title"],
        "target": {"repo": route["repo"], "area": route["area"]},
        "direction": decision["statement"],
        "reasoning": (
            f"Recorded as {decision['id']} from the "
            f"{decision['origin'].get('meeting_date', 'unknown')} meeting"
            + (f", decided by {decision['owner']}."
               if decision.get("owner") and decision["owner"] != "unknown"
               else ". No individual is recorded as the deciding authority.")
        ),
        "acceptance_criteria": acceptance_criteria(decision, route),
        "evidence": decision["evidence"],
        "authorized_by": {
            "librarian": approval.get("approved_by", "unknown"),
            "authorized_at": approval.get("approved_at"),
        },
        "status": "draft",
        **({"related_questions": questions} if questions else {}),
    }


def issue_body(ticket: dict, decision: dict) -> str:
    lines: list[str] = []

    lines.append(f"**Decision:** `{ticket['decision_id']}` · "
                 f"**Ticket:** `{ticket['id']}` · "
                 f"**Area:** `{ticket['target']['area']}`")
    lines.append("")
    lines.append("## What must change")
    lines.append("")
    lines.append(ticket["direction"])
    lines.append("")
    lines.append("## Why")
    lines.append("")
    lines.append(ticket["reasoning"])
    lines.append("")

    lines.append("## Evidence")
    lines.append("")
    lines.append("Verbatim from the meeting transcript. Anchors resolve against "
                 f"`{decision['origin']['transcript_path']}`.")
    lines.append("")
    for item in ticket["evidence"]:
        lines.append(f"- `{item['location']}` — \u201c{item['excerpt']}\u201d")
    lines.append("")

    lines.append("## Done when")
    lines.append("")
    for criterion in ticket["acceptance_criteria"]:
        lines.append(f"- [ ] {criterion}")
    lines.append("")

    if ticket.get("related_questions"):
        lines.append("## Open questions affecting this")
        lines.append("")
        lines.append("These are unresolved. They do not block starting, but the "
                     "spec should record what is still undecided rather than "
                     "assuming an answer.")
        lines.append("")
        for qid in ticket["related_questions"]:
            q = question_detail(qid)
            if q:
                owner = q.get("owner", "unknown")
                owner = "unowned" if owner == "unknown" else owner
                lines.append(f"- **{qid}** — {q['title']} _(owner: {owner})_")
            else:
                lines.append(f"- **{qid}**")
        lines.append("")

    auth = ticket["authorized_by"]
    lines.append("---")
    lines.append("")
    lines.append(
        f"Approved by {auth['librarian']} on "
        f"{(auth.get('authorized_at') or '')[:10]}. "
        f"Generated from the Hazel-KB ledger — do not edit this description by "
        f"hand; correct the decision record and re-dispatch."
    )
    return "\n".join(lines)


def create_issue(github_repo: str, ticket: dict, decision: dict,
                 labels: list[str], dry: bool) -> str | None:
    body = issue_body(ticket, decision)
    title = f"[{ticket['decision_id']}] {ticket['title']}"

    if dry:
        print("\n" + "─" * 74)
        print(f"WOULD CREATE ISSUE on {github_repo}")
        print("─" * 74)
        print(f"title: {title}")
        if labels:
            print(f"labels: {', '.join(labels)}")
        print("─" * 74)
        print(body)
        print("─" * 74 + "\n")
        return None

    if not shutil.which("gh"):
        die("gh is not installed or not on PATH",
            "install the GitHub CLI, or re-run with --no-github")

    cmd = ["gh", "issue", "create", "--repo", github_repo,
           "--title", title, "--body", body]
    for label in labels:
        cmd += ["--label", label]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = result.stderr.strip()
        hint = ""
        if "could not add label" in stderr.lower() or "not found" in stderr.lower():
            hint = ("the label may not exist on the target repo — create it, or "
                    "clear labels.default in .ai/contracts/repo-targets.json")
        elif "authentication" in stderr.lower() or "auth" in stderr.lower():
            hint = "run: gh auth status"
        die(f"gh issue create failed: {stderr}", hint)

    return result.stdout.strip().splitlines()[-1]


# ---------------------------------------------------------------------------


def list_pending() -> int:
    if not DECISIONS.is_dir():
        print("No decisions recorded.")
        return 0

    rows = []
    for path in sorted(DECISIONS.glob("DEC-*.json")):
        doc = load(path)
        if doc.get("status") != "active":
            continue
        routes = [r for r in doc.get("routing", []) if r["repo"] != "none"]
        if not routes:
            continue
        dispatched = {(t["target"]["repo"], t["target"]["area"])
                      for t in existing_tickets_for(doc["id"])}
        outstanding = [r for r in routes
                       if (r["repo"], r["area"]) not in dispatched]
        if outstanding:
            rows.append((doc["id"], doc["title"], outstanding))

    if not rows:
        print("Nothing pending — every active decision has been dispatched.")
        return 0

    print(f"{len(rows)} decision(s) awaiting dispatch:\n")
    for did, title, routes in rows:
        print(f"  {did}  {title[:60]}")
        for r in routes:
            print(f"          -> {r['repo']}/{r['area']}")
    print(f"\nDispatch one with: python .ai/checks/dispatch.py <DEC-id>")
    return 0


def dispatch(decision_id: str, dry: bool, use_github: bool,
             only_repo: str | None) -> int:
    decision = load(DECISIONS / f"{decision_id}.json")
    targets = load(TARGETS)

    if decision.get("status") != "active":
        die(f"{decision_id} has status {decision.get('status')!r}",
            "only an active decision can be dispatched")

    approval = decision.get("approval") or {}
    if not approval.get("approved_by"):
        die(f"{decision_id} has no librarian approval",
            "dispatch carries the approval forward; it cannot create one")

    routes = [r for r in decision.get("routing", []) if r["repo"] != "none"]
    if only_repo:
        routes = [r for r in routes if r["repo"] == only_repo]
    if not routes:
        die(f"{decision_id} has no dispatchable routing"
            + (f" for {only_repo}" if only_repo else ""),
            "routing to 'none' means no software change is required")

    already = {(t["target"]["repo"], t["target"]["area"]): t["id"]
               for t in existing_tickets_for(decision_id)}

    questions = related_questions(decision_id)
    next_num = next_ticket_id()
    created: list[tuple[dict, str | None]] = []

    print(f"\n{decision_id}  {decision['title']}")
    print(f"  approved by {approval['approved_by']}")
    if questions:
        print(f"  {len(questions)} open question(s) affecting this: "
              f"{', '.join(questions)}")
    print()

    for route in routes:
        key = (route["repo"], route["area"])
        if key in already:
            print(f"SKIP     {route['repo']}/{route['area']} — already "
                  f"dispatched as {already[key]}")
            continue

        target = targets["repos"].get(route["repo"])
        if target is None:
            die(f"no target configured for repo {route['repo']!r}",
                "add it to .ai/contracts/repo-targets.json")
        if not target.get("dispatch"):
            print(f"HOLD     {route['repo']}/{route['area']} — "
                  f"{target['description']}")
            continue

        ticket_id = f"TKT-{next_num:04d}"
        next_num += 1
        ticket = build_ticket(decision, route, ticket_id, questions)

        labels = list(targets.get("labels", {}).get("default", []))
        labels += targets.get("labels", {}).get("by_repo", {}).get(route["repo"], [])

        url = None
        if use_github:
            url = create_issue(target["github"], ticket, decision, labels, dry)
            if url:
                ticket["status"] = "dispatched"
                ticket["dispatched_to"] = url

        if not use_github and not dry:
            ticket["status"] = "dispatched"
            ticket["dispatched_to"] = (
                f"{route['repo']}:{route['area']} (no issue created)")

        created.append((ticket, url))

        if dry:
            print(f"WOULD    write 04-ledger/tickets/{ticket_id}.json")
        else:
            TICKETS.mkdir(parents=True, exist_ok=True)
            (TICKETS / f"{ticket_id}.json").write_text(
                json.dumps(ticket, indent=2) + "\n", encoding="utf-8")
            print(f"WROTE    04-ledger/tickets/{ticket_id}.json")
            if url:
                print(f"ISSUE    {url}")

    if not created:
        print("\nNothing to do.")
        return 0

    if dry:
        print("\nDry run — nothing written. Re-run without --dry-run.")
        return 0

    # spec_impact stays "pending" until a spec change lands. Record the link.
    print()
    print(f"DONE     {len(created)} ticket(s) created for {decision_id}")
    regenerate_registries()
    print()
    print("Next:")
    print("  python .ai/checks/validate.py")
    print(f"  git add -A && git commit -m "
          f"\"feat(ledger): dispatch {decision_id}\"")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("decision_id", nargs="?", help="e.g. DEC-001")
    ap.add_argument("--pending", action="store_true",
                    help="list decisions awaiting dispatch")
    ap.add_argument("--dry-run", action="store_true",
                    help="show the issue that would be created; write nothing")
    ap.add_argument("--no-github", action="store_true",
                    help="write the ticket record but do not open an issue")
    ap.add_argument("--repo", help="dispatch only to this repo")
    args = ap.parse_args()

    if args.pending or not args.decision_id:
        return list_pending()

    return dispatch(args.decision_id, args.dry_run,
                    not args.no_github, args.repo)


if __name__ == "__main__":
    raise SystemExit(main())
