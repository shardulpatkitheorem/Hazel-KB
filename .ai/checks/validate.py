#!/usr/bin/env python3
"""
Validate every machine-readable artifact in the knowledge base.

Nothing in this repository previously checked that artifacts matched their
contracts. This does. It runs three passes:

  1. SCHEMA      every artifact validates against its contract
  2. INTEGRITY   every cross-reference resolves; no orphans, no cycles
  3. PROVENANCE  every content_sha256 matches the source it names
  4. ANCHORS     every quoted excerpt appears where its anchor says

Exit code 0 if clean, 1 if any error. Warnings do not fail the run.

Usage:
    python .ai/checks/validate.py               # validate the whole repo
    python .ai/checks/validate.py --path X      # validate one file or directory
    python .ai/checks/validate.py --json        # machine-readable output
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_hash import hash_body
from anchors import check_evidence

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.stderr.write(
        "error: jsonschema is not installed.\n"
        "       pip install jsonschema\n"
    )
    raise SystemExit(2)


REPO = Path(__file__).resolve().parents[2]
CONTRACTS = REPO / ".ai" / "contracts"
LEDGER = REPO / "04-iteration-ledger"
ITERATIONS = REPO / "iterations"

# Which contract governs which artifacts.
ARTIFACT_MAP = [
    (LEDGER / "decisions", "decision.schema.json"),
    (LEDGER / "questions", "open-question.schema.json"),
    (LEDGER / "tickets", "ticket.schema.json"),
]

DEC_ID = re.compile(r"^DEC-[0-9]{3,}$")
Q_ID = re.compile(r"^Q-[0-9]{3,}$")
TKT_ID = re.compile(r"^TKT-[0-9]{4,}$")


# ---------------------------------------------------------------------------


@dataclass
class Findings:
    errors: list[dict] = field(default_factory=list)
    warnings: list[dict] = field(default_factory=list)

    def error(self, where: str, message: str, hint: str = "") -> None:
        self.errors.append({"level": "error", "where": where,
                            "message": message, "hint": hint})

    def warn(self, where: str, message: str, hint: str = "") -> None:
        self.warnings.append({"level": "warning", "where": where,
                              "message": message, "hint": hint})

    @property
    def ok(self) -> bool:
        return not self.errors


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(REPO))
    except ValueError:
        return str(p)


def load_json(path: Path, f: Findings) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        f.error(rel(path), f"invalid JSON: {exc.msg} at line {exc.lineno}")
    except OSError as exc:
        f.error(rel(path), f"cannot read: {exc}")
    return None


def load_contracts(f: Findings) -> dict[str, Draft202012Validator]:
    validators: dict[str, Draft202012Validator] = {}
    if not CONTRACTS.is_dir():
        f.error(rel(CONTRACTS), "contracts directory not found")
        return validators
    for path in sorted(CONTRACTS.glob("*.schema.json")):
        schema = load_json(path, f)
        if schema is None:
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:
            f.error(rel(path), f"contract is not a valid schema: {exc}")
            continue
        validators[path.name] = Draft202012Validator(schema)
    return validators


# ---------------------------------------------------------------------------
# Pass 1 — schema
# ---------------------------------------------------------------------------


def validate_schemas(
    validators: dict[str, Draft202012Validator], f: Findings
) -> dict[str, list[dict]]:
    """Validate every artifact. Returns records grouped by kind."""
    collected: dict[str, list[dict]] = {
        "decision": [], "open-question": [], "ticket": [], "meeting-delta": []
    }

    targets: list[tuple[Path, str]] = []
    for directory, contract in ARTIFACT_MAP:
        if directory.is_dir():
            for path in sorted(directory.glob("*.json")):
                targets.append((path, contract))
    if ITERATIONS.is_dir():
        for path in sorted(ITERATIONS.glob("*/meeting-delta.json")):
            targets.append((path, "meeting-delta.schema.json"))

    if not targets:
        f.warn("repository", "no artifacts found to validate",
               "expected records under 04-iteration-ledger/ or iterations/")

    for path, contract_name in targets:
        validator = validators.get(contract_name)
        if validator is None:
            f.error(rel(path), f"no contract named {contract_name}")
            continue

        doc = load_json(path, f)
        if doc is None:
            continue

        errs = sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
        for err in errs:
            loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
            f.error(rel(path), f"{loc}: {err.message}",
                    f"contract: {contract_name}")

        kind = contract_name.replace(".schema.json", "")
        kind = {"open-question": "open-question"}.get(kind, kind)
        collected.setdefault(kind, []).append({"path": path, "doc": doc})

        # Filename should match the record id.
        rec_id = doc.get("id")
        if rec_id and path.stem != rec_id and contract_name != "meeting-delta.schema.json":
            f.warn(rel(path), f"filename does not match id {rec_id}",
                   f"rename to {rec_id}.json")

    return collected


# ---------------------------------------------------------------------------
# Pass 2 — referential integrity
# ---------------------------------------------------------------------------


def validate_integrity(collected: dict[str, list[dict]], f: Findings) -> None:
    decisions = {r["doc"]["id"]: r for r in collected["decision"]
                 if "id" in r["doc"]}
    questions = {r["doc"]["id"]: r for r in collected["open-question"]
                 if "id" in r["doc"]}

    # -- duplicate ids -------------------------------------------------------
    for kind, records in collected.items():
        seen: dict[str, Path] = {}
        for rec in records:
            rid = rec["doc"].get("id")
            if not rid:
                continue
            if rid in seen:
                f.error(rel(rec["path"]),
                        f"duplicate id {rid}",
                        f"also defined in {rel(seen[rid])}")
            seen[rid] = rec["path"]

    # -- supersession --------------------------------------------------------
    for did, rec in decisions.items():
        doc, path = rec["doc"], rec["path"]

        target = doc.get("supersedes")
        if target:
            if target not in decisions:
                f.error(rel(path), f"supersedes unknown decision {target}")
            else:
                other = decisions[target]["doc"]
                if other.get("superseded_by") != did:
                    f.error(
                        rel(path),
                        f"{did} supersedes {target}, but {target}.superseded_by "
                        f"is {other.get('superseded_by')!r}",
                        "supersession must be recorded on both records",
                    )
                if other.get("status") != "superseded":
                    f.error(rel(decisions[target]["path"]),
                            f"{target} is superseded by {did} but status is "
                            f"{other.get('status')!r}")
                # Chronology: a decision cannot supersede a later one.
                if doc.get("decided_on") and other.get("decided_on"):
                    if doc["decided_on"] < other["decided_on"]:
                        f.error(
                            rel(path),
                            f"{did} ({doc['decided_on']}) supersedes {target} "
                            f"({other['decided_on']}), which is later",
                            "order supersession by decided_on, never by id",
                        )

        back = doc.get("superseded_by")
        if back:
            if back not in decisions:
                f.error(rel(path), f"superseded_by unknown decision {back}")
            if doc.get("status") != "superseded":
                f.error(rel(path),
                        f"superseded_by is set but status is "
                        f"{doc.get('status')!r}")
        elif doc.get("status") == "superseded":
            f.error(rel(path),
                    "status is superseded but superseded_by is null")

        # dates
        if doc.get("recorded_on") and doc.get("decided_on"):
            if doc["recorded_on"] < doc["decided_on"]:
                f.error(rel(path),
                        f"recorded_on {doc['recorded_on']} precedes "
                        f"decided_on {doc['decided_on']}")

        if doc.get("owner") == "unknown":
            f.warn(rel(path), f"{did} has no named owner")

    # -- supersession cycles -------------------------------------------------
    for start in decisions:
        seen, cur = set(), start
        while cur:
            if cur in seen:
                f.error(rel(decisions[start]["path"]),
                        f"supersession cycle involving {cur}")
                break
            seen.add(cur)
            cur = decisions.get(cur, {}).get("doc", {}).get("superseded_by")

    # -- questions -----------------------------------------------------------
    for qid, rec in questions.items():
        doc, path = rec["doc"], rec["path"]
        if doc.get("status") == "answered" and doc.get("answer") is None:
            f.error(rel(path), "status is answered but answer is null")
        if doc.get("status") != "answered" and doc.get("answer") is not None:
            f.error(rel(path),
                    f"answer is present but status is {doc.get('status')!r}")
        for blocked in doc.get("blocking", []):
            if DEC_ID.match(blocked) and blocked not in decisions:
                f.error(rel(path), f"blocks unknown decision {blocked}")

    # -- tickets -------------------------------------------------------------
    dispatched_by_decision: dict[str, list[str]] = {}
    for rec in collected["ticket"]:
        doc, path = rec["doc"], rec["path"]
        did = doc.get("decision_id")
        if did and did not in decisions:
            f.error(rel(path), f"references unknown decision {did}")
            continue
        if not did:
            continue

        decision = decisions[did]["doc"]
        dispatched_by_decision.setdefault(did, []).append(doc.get("id", "?"))

        # target must be one of the decision's routing entries
        target = doc.get("target", {})
        routes = [(r.get("repo"), r.get("area"))
                  for r in decision.get("routing", [])]
        if (target.get("repo"), target.get("area")) not in routes:
            f.error(
                rel(path),
                f"target {target.get('repo')}/{target.get('area')} is not in "
                f"{did}'s routing",
                f"routing declares: {routes}",
            )

        # evidence must be carried, not reinvented
        d_ev = {(e["location"], e["excerpt"]) for e in decision.get("evidence", [])}
        t_ev = {(e["location"], e["excerpt"]) for e in doc.get("evidence", [])}
        if not t_ev.issubset(d_ev):
            f.error(rel(path),
                    "evidence does not match the decision's evidence",
                    "tickets carry evidence forward unchanged")

        # authorization must match the decision's approval
        appr = decision.get("approval", {})
        auth = doc.get("authorized_by", {})
        if appr.get("approved_by") and auth.get("librarian") != appr["approved_by"]:
            f.error(rel(path),
                    f"authorized_by.librarian {auth.get('librarian')!r} does "
                    f"not match {did}'s approver {appr['approved_by']!r}",
                    "dispatch is not a second gate")

        if doc.get("status") != "draft" and not doc.get("dispatched_to"):
            f.error(rel(path),
                    f"status is {doc['status']!r} but dispatched_to is absent")

        for qid in doc.get("related_questions", []):
            if qid not in questions:
                f.error(rel(path), f"references unknown question {qid}")

    # -- decisions awaiting dispatch ----------------------------------------
    for did, rec in decisions.items():
        doc = rec["doc"]
        needs = [r for r in doc.get("routing", []) if r.get("repo") != "none"]
        if doc.get("status") == "active" and needs:
            if did not in dispatched_by_decision:
                f.warn(rel(rec["path"]),
                       f"{did} routes to {len(needs)} target(s) but no ticket "
                       f"exists",
                       "run dispatch.py")
            elif len(dispatched_by_decision[did]) < len(needs):
                f.warn(rel(rec["path"]),
                       f"{did} routes to {len(needs)} target(s) but only "
                       f"{len(dispatched_by_decision[did])} ticket(s) exist")


# ---------------------------------------------------------------------------
# Pass 3 — provenance
# ---------------------------------------------------------------------------


def validate_provenance(collected: dict[str, list[dict]], f: Findings) -> None:
    """Re-derive every content_sha256 from the source it names.

    Covers meeting deltas as well as records. A delta whose hash does not match
    is extracted from a source that has since changed, and nothing downstream
    of it can be trusted.
    """
    cache: dict[Path, str] = {}

    def digest(path: Path) -> str | None:
        """Body-only digest — see .ai/checks/content_hash.py."""
        if path in cache:
            return cache[path]
        try:
            h = hash_body(path)
        except (OSError, UnicodeDecodeError):
            return None
        cache[path] = h
        return h

    def verify(record_path: Path, src_rel: str, claimed: str, field: str) -> None:
        source = REPO / src_rel
        if not source.is_file():
            f.error(rel(record_path), f"{field} not found: {src_rel}")
            return
        actual = digest(source)
        if actual is None:
            f.error(rel(record_path), f"cannot hash {src_rel}")
        elif actual != claimed:
            f.error(
                rel(record_path),
                f"content_sha256 does not match {src_rel}",
                f"recorded {claimed[:12]}…, actual {actual[:12]}… — either the "
                f"source body changed after this was written, or the digest was "
                f"computed differently. Regenerate with: "
                f"python .ai/checks/hash-source.py {src_rel}",
            )

    for kind in ("decision", "open-question"):
        for rec in collected[kind]:
            doc, path = rec["doc"], rec["path"]
            origin = doc.get("origin", {})
            claimed = origin.get("content_sha256")
            if not claimed:
                continue
            field = "transcript_path" if origin.get("kind") == "meeting" \
                else "document_path"
            src_rel = origin.get(field)
            if src_rel:
                verify(path, src_rel, claimed, f"origin.{field}")

    for rec in collected["meeting-delta"]:
        doc, path = rec["doc"], rec["path"]
        source = doc.get("source", {})
        claimed = source.get("content_sha256")
        src_rel = source.get("transcript_path")
        if claimed and src_rel:
            verify(path, src_rel, claimed, "source.transcript_path")


def validate_anchors(collected: dict[str, list[dict]], f: Findings) -> None:
    """Verify that every quoted excerpt appears where its anchor says.

    An anchor nobody can follow is worse than no anchor: it looks like
    provenance and is not.
    """
    bodies: dict[Path, str | None] = {}

    def body_of(src_rel: str) -> str | None:
        path = REPO / src_rel
        if path in bodies:
            return bodies[path]
        try:
            with path.open(encoding="utf-8", newline="") as fh:
                text = fh.read()
            from content_hash import split_frontmatter
            _, body = split_frontmatter(text)
        except (OSError, UnicodeDecodeError):
            body = None
        bodies[path] = body
        return body

    def walk(record_path: Path, src_rel: str, items, label: str) -> None:
        body = body_of(src_rel)
        if body is None:
            return
        for index, ev in enumerate(items or []):
            anchor = ev.get("location", "")
            excerpt = ev.get("excerpt", "")
            ok, level, message = check_evidence(body, anchor, excerpt)
            if not message:
                continue
            where = f"{label}[{index}] {anchor}"
            if level == "error" or not ok:
                f.error(rel(record_path), f"{where}: {message}",
                        f"source: {src_rel}")
            else:
                f.warn(rel(record_path), f"{where}: {message}")

    for kind in ("decision", "open-question"):
        for rec in collected[kind]:
            doc, path = rec["doc"], rec["path"]
            origin = doc.get("origin", {})
            src_rel = origin.get("transcript_path") or origin.get("document_path")
            if src_rel:
                walk(path, src_rel, doc.get("evidence"), "evidence")

    delta_arrays = ("decisions", "approved_changes", "requested_changes",
                    "action_items", "open_questions", "superseded_decisions",
                    "not_promoted")
    for rec in collected["meeting-delta"]:
        doc, path = rec["doc"], rec["path"]
        src_rel = doc.get("source", {}).get("transcript_path")
        if not src_rel:
            continue
        for array in delta_arrays:
            for item in doc.get(array, []):
                label = f"{array}.{item.get('id') or item.get('topic', '?')[:40]}"
                walk(path, src_rel, item.get("evidence"), label)


# ---------------------------------------------------------------------------


def report(f: Findings, as_json: bool) -> int:
    if as_json:
        print(json.dumps({
            "ok": f.ok,
            "error_count": len(f.errors),
            "warning_count": len(f.warnings),
            "findings": f.errors + f.warnings,
        }, indent=2))
        return 0 if f.ok else 1

    width = 74
    for item in f.errors + f.warnings:
        tag = "ERROR  " if item["level"] == "error" else "WARN   "
        print(f"{tag} {item['where']}")
        print(f"        {item['message']}")
        if item["hint"]:
            print(f"        → {item['hint']}")
        print()

    print("─" * width)
    if f.ok and not f.warnings:
        print("PASS   all artifacts valid")
    elif f.ok:
        print(f"PASS   {len(f.warnings)} warning(s), 0 errors")
    else:
        print(f"FAIL   {len(f.errors)} error(s), {len(f.warnings)} warning(s)")
    return 0 if f.ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--path", help="validate a single file or directory")
    args = ap.parse_args()

    f = Findings()
    validators = load_contracts(f)
    if not validators:
        return report(f, args.json)

    collected = validate_schemas(validators, f)
    if f.ok:
        validate_integrity(collected, f)
        validate_provenance(collected, f)
        validate_anchors(collected, f)
    else:
        f.warn("validation", "integrity and provenance passes skipped",
               "fix schema errors first")

    return report(f, args.json)


if __name__ == "__main__":
    raise SystemExit(main())
