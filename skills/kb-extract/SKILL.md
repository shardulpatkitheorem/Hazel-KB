---
name: kb-extract
description: Extract candidate decisions, open questions and action items from a meeting transcript or document into a meeting delta for librarian review. Use when a new transcript, PDF or document has landed in the knowledge base and needs processing. Produces candidates only — never authoritative records.
---

# Extract candidates from a source

You are reading one source document and proposing what it might contain. You
are **not** deciding anything. Everything you produce is a candidate that a
human librarian will accept, correct, or reject.

The single most important property of your output is that it is **honest about
what the source does and does not establish**. An extractor that promotes
discussion to decision is worse than no extractor, because it launders
uncertainty into the authoritative record.

## Constraints

- **Read-only.** Do not modify the source. Do not write to
  `04-iteration-ledger/decisions/`, `questions/`, or any registry.
- **One output file:** `iterations/<iteration-id>/meeting-delta.json`.
- **Never invent an owner or a date.** If the source does not name one, write
  `"unknown"`. This is a correct answer, not a failure.
- **Every claim needs an anchor that resolves.** At least one evidence item
  whose `excerpt` is copied **verbatim** from the source and whose `location`
  is the source's **own timestamp, copied exactly**. A transcript reading
  `[00:13:59]` gives the anchor `t:0:13:59`. Do not round, estimate, or reuse
  one timestamp for several excerpts from different moments.

  Validation now resolves every anchor: it finds the excerpt in the source and
  checks which timestamp governs it. An excerpt that does not appear, or an
  anchor more than two minutes from where it actually appears, is an error.
- Validate before finishing: `python .ai/checks/validate.py`.

## Procedure

1. **Hash the source by running the script.** Do not compute a digest
   yourself — the digest covers the transcript body only, excluding
   frontmatter, and a hash computed any other way will fail validation.

   ```
   python .ai/checks/hash-source.py <path>
   ```

   Paste its output verbatim into `source.content_sha256`.
2. **Read the whole source before extracting anything.** A statement at 3:00 is
   frequently reversed by 6:00. Extracting linearly produces records that the
   same meeting already overturned.
3. **Read the existing registry** at `04-iteration-ledger/decisions.md`. You
   need it to spot restatements and reversals.
4. **Classify** every substantive exchange using the rubric below.
5. **Write the delta**, including `not_promoted`.
6. **Validate.** `python .ai/checks/validate.py` must pass with no errors. If
   an anchor fails to resolve, fix the anchor or the excerpt — never loosen
   the check.
7. Stop. Report what you found and hand off to the librarian.

## The rubric

### A decision

Promote to `decisions` only when **both** hold:

- The source records **agreement, or a named authority making a call**, and
- The outcome is stated as **settled**, not proposed.

A useful test: could a spec requirement be written from this sentence? "The
system MUST…" — if the source does not support that sentence, it is not a
decision.

Signals that it is: "here's the call", "let's do X", "that's decided",
"agreed", followed by others accepting. A person with authority over that area
stating an outcome and nobody dissenting.

Signals that it is **not**: "we could", "what if", "I'd suggest", "maybe we",
"let's think about", "one option is". A question left hanging. A statement
followed by an objection that is not resolved.

### An open question

Promote to `open_questions` when the source records something **explicitly
unresolved**, or resolution deferred to a named person. Capture the question as
posed. If nobody committed a date, `due_date` is `"unknown"` — do not compute
one from "next week" unless a specific date was said aloud.

### An action item

A task someone will do. Distinguish from a decision: an action item changes
somebody's week; a decision changes what the system does.

### A superseded decision

When a candidate reverses something already in the registry, set
`supersedes_id` to that record's real `DEC-` id. Do not edit the existing
record — approval handles that.

If the source clearly reverses an earlier decision but **no `DEC-` record
exists yet**, you cannot cite one. Say so plainly in your report: name the
meeting that established the earlier position and state that it needs
backfilling before this candidate can be approved. Do not silently promote a
reversal as though it were a fresh decision — the supersession would be lost.

## What must NOT be promoted

Record these in `not_promoted` with a reason. This array is how the librarian
sees your judgement, so populate it properly.

| Situation | Reason code |
|---|---|
| Someone floats an idea and then retracts it | `withdrawn_by_speaker` |
| Deliberately deferred — "let's not solve that today" | `explicitly_parked` |
| Proposed, objected to, never resolved | `no_agreement_reached` |
| Already in the registry, said again | `restates_existing_record` |
| "We might eventually…" with no commitment | `speculation_without_commitment` |
| Not about this project | `out_of_scope` |

**A withdrawn idea is not a decision.** If someone proposes X, is argued out of
it, and says "withdrawn", the meeting did not decide "not X" — it declined to
decide. The exception is when a named authority explicitly rules it out with a
reason and the group accepts; that *is* a negative decision, and it belongs in
`decisions` with `confidence: low` and a note explaining the judgement call.

When genuinely torn between promoting and not, **promote with
`confidence: low`** and say why in `confidence_note`. A candidate the librarian
rejects costs thirty seconds. A missed decision costs a wrong build.

## Confidence

| Level | Use when |
|---|---|
| `high` | Explicit agreement or a named authority deciding. Owner and substance both unambiguous. |
| `medium` | The substance is clear but an attribute is not — no named owner, or scope uncertain. |
| `low` | Arguably a decision, arguably not. The librarian should look closely. |

`confidence_note` is required for `medium` and `low`. Say what is uncertain, not
that you are uncertain.

## Routing

Propose `routing` for every candidate decision — which repository and area it
affects. The librarian confirms or corrects it, but proposing it is your job:
without it the decision cannot be dispatched.

| Repo | Covers |
|---|---|
| `react-frontend` | Applicant and ops portal UI, screens, forms, client validation |
| `wf-orchestration` | Back-end APIs, workflow logic, state, server-side rules |
| `integration-wrapper` | Third-party provider APIs and the abstraction over them |
| `hazel-kb` | Living current-state documents only |
| `none` | Process or policy decisions that change no software |

`area` convention: onboarding step slug (`step-03-documents`), module name, or
living document name. A decision touching two layers gets two routing entries,
not two candidates.

## Terminology

Sources are frequently speech-to-text and corrupt exactly the terms that matter.
Normalise vendor and product names in `statement` and `title`; leave `excerpt`
**verbatim**, including errors, because it must match the source for verification.

Common corruptions: "cover base"/"Coverabase" → Coverbase · "Infinite" →
Infinant · "advantage" → Vantage (context-dependent; "advantage" is also an
ordinary word) · "Woodesburgh"/"Wolfsburg" → Wolfsberg · "open spec kit" →
OpenSpec · "BSL" → BSA · "hop" → HOP (context-dependent).

## Report

After writing and validating, tell the librarian:

- Counts: decisions, questions, action items, not-promoted
- Every `low` confidence candidate, and why
- Anything that contradicts an existing record
- Anything in the source you could not classify

Do not summarise the meeting. The librarian reviews candidates, not minutes.
