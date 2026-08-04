#!/usr/bin/env python3
"""
Link merged pull requests back to the decisions they implement.

Closes the loop. Dispatch sends a decision out to a repository; this brings the
result back, so a decision record answers "was this built, and where" rather
than sitting at spec_impact: pending forever.

Scans merged PRs in every dispatchable repo, finds decision ids in the branch
name, title or body, and updates the matching record's `implemented_by` and
`spec_impact`. Both fields are in the mutable set, so this is an edit, not a
supersession.

A PR is matched to a decision when a DEC- id appears in:
  - the branch name       dec-001-wolfsberg-optional-fallback
  - the title             [DEC-001] Wolfsberg CBDDQ is not mandatory
  - the body              Closes #1 · implements DEC-001

Usage:
    python .ai/checks/link-implementation.py --dry-run
    python .ai/checks/link-implementation.py
    python .ai/checks/link-implementation.py --since 2026-07-01
    python .ai/checks/link-implementation.py DEC-001
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LEDGER = REPO / "04-ledger"
DECISIONS = LEDGER / "decisions"
TARGETS = REPO / ".ai" / "contracts" / "repo-targets.json"

DEC_REF = re.compile(r"\bDEC-([0-9]{3,})\b", re.IGNORECASE)
CHANGE_REF = re.compile(r"openspec/changes/([a-z0-9][a-z0-9-]*)", re.IGNORECASE)


def die(message: str, hint: str = "") -> None:
    sys.stderr.write(f"error: {message}\n")
    if hint:
        sys.stderr.write(f"       {hint}\n")
    raise SystemExit(1)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def merged_prs(github_repo: str, since: str | None) -> list[dict]:
    """Merged PRs for a repo, newest first."""
    cmd = [
        "gh", "pr", "list", "--repo", github_repo, "--state", "merged",
        "--limit", "100",
        "--json", "number,title,body,headRefName,url,mergedAt,files",
    ]
    if since:
        cmd += ["--search", f"merged:>={since}"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        stderr = result.stderr.strip()
        if "could not resolve" in stderr.lower():
            sys.stderr.write(f"warning: cannot reach {github_repo} — skipped\n")
            return []
        die(f"gh pr list failed for {github_repo}: {stderr}",
            "run: gh auth status")

    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        die(f"unexpected output from gh for {github_repo}")
        return []


def decisions_in(pr: dict) -> set[str]:
    """Decision ids referenced anywhere in a PR."""
    haystack = " ".join([
        pr.get("headRefName", ""),
        pr.get("title", ""),
        pr.get("body") or "",
    ])
    return {f"DEC-{m.group(1)}" for m in DEC_REF.finditer(haystack)}


def change_id_in(pr: dict) -> str | None:
    """The OpenSpec change a PR touches, from its changed file paths."""
    for entry in pr.get("files") or []:
        m = CHANGE_REF.search(entry.get("path", ""))
        if m:
            return m.group(1)
    body_match = CHANGE_REF.search(pr.get("body") or "")
    return body_match.group(1) if body_match else None


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("decision_id", nargs="?", help="link only this decision")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--since", help="only PRs merged on or after YYYY-MM-DD")
    args = ap.parse_args()

    if not shutil.which("gh"):
        die("gh is not installed or not on PATH")
    if not DECISIONS.is_dir():
        die("no decisions recorded")

    targets = load(TARGETS)
    repos = {name: cfg["github"] for name, cfg in targets["repos"].items()
             if cfg.get("dispatch") and cfg.get("github")}
    if not repos:
        die("no dispatchable repos configured",
            "set dispatch: true and a github target in "
            ".ai/contracts/repo-targets.json")

    # Gather PRs once per distinct GitHub repo — several layer names may point
    # at the same repository.
    seen: dict[str, list[dict]] = {}
    for github_repo in set(repos.values()):
        print(f"Scanning {github_repo}…")
        seen[github_repo] = merged_prs(github_repo, args.since)

    # decision id -> list of (url, change_id)
    found: dict[str, list[tuple[str, str | None]]] = {}
    for prs in seen.values():
        for pr in prs:
            for did in decisions_in(pr):
                found.setdefault(did, []).append((pr["url"], change_id_in(pr)))

    if not found:
        print("\nNo merged PR references any decision id.")
        print("Reference a decision in the branch name, title or body, e.g.")
        print("  dec-001-wolfsberg-optional-fallback")
        return 0

    updated, unchanged, unknown = [], [], []

    for did, hits in sorted(found.items()):
        if args.decision_id and did != args.decision_id:
            continue

        path = DECISIONS / f"{did}.json"
        if not path.is_file():
            unknown.append((did, hits))
            continue

        record = load(path)
        before = json.dumps(record, sort_keys=True)

        urls = sorted({url for url, _ in hits})
        existing = record.get("implemented_by", [])
        merged_urls = sorted(set(existing) | set(urls))
        record["implemented_by"] = merged_urls

        # spec_impact points at the OpenSpec change, when a PR reveals one.
        change_ids = sorted({c for _, c in hits if c})
        if change_ids and record.get("spec_impact") == "pending":
            record["spec_impact"] = f"change:{change_ids[0]}"
            if len(change_ids) > 1:
                sys.stderr.write(
                    f"warning: {did} touches several changes "
                    f"({', '.join(change_ids)}); recorded the first\n")

        if json.dumps(record, sort_keys=True) == before:
            unchanged.append(did)
            continue

        added = [u for u in merged_urls if u not in existing]
        print(f"\n{did}  {record['title'][:58]}")
        for url in added:
            print(f"  + implemented_by  {url}")
        if record.get("spec_impact", "").startswith("change:"):
            print(f"  · spec_impact     {record['spec_impact']}")

        if not args.dry_run:
            path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        updated.append(did)

    print()
    if unknown:
        for did, hits in unknown:
            sys.stderr.write(
                f"warning: {hits[0][0]} references {did}, which has no record\n")

    if not updated:
        print(f"OK       nothing to link"
              + (f" — {len(unchanged)} already current" if unchanged else ""))
        return 0

    if args.dry_run:
        print(f"DRY RUN  {len(updated)} decision(s) would be updated")
        return 0

    print(f"DONE     {len(updated)} decision(s) linked")
    print()
    print("Next:")
    print("  python .ai/checks/validate.py")
    print("  python .ai/checks/build-registries.py")
    print("  git add -A && git commit -m \"feat(ledger): link decisions to "
          "their implementing PRs\"")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
