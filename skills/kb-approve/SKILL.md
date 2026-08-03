---
name: kb-approve
description: Walk the librarian through the candidates in a meeting delta and promote the accepted ones to authoritative records. This is the human gate — run it deliberately, never automatically.
disable-model-invocation: true
---

# Librarian review

This is the gate. Everything upstream produces candidates; nothing is
authoritative until it passes through here. One approval does two things at
once: it confirms an item into the ledger, and it authorises its dispatch to a
product repository.

**You are not the reviewer.** The librarian is. Your job is to present each
candidate clearly, capture their judgement exactly, and write the records. You
do not decide, and you do not persuade.

## Constraints

- **Never accept a candidate on your own judgement.** Every outcome comes from
  the librarian, stated explicitly. Silence is not acceptance.
- **Never invent, tidy, or improve a statement.** If the librarian wants
  different wording, they say so and it is recorded as an amendment.
- **Every candidate gets an outcome.** No candidate is silently dropped.
- **Allocate ids only via the script.** Never guess the next number.
- Work on a branch. This writes to the ledger.

## Procedure

### 1. Load

Read the delta at `iterations/<iteration-id>/meeting-delta.json` and hash it:

```
python .ai/checks/hash-source.py iterations/<id>/meeting-delta.json
```

That hash goes in the review record and binds the review to exactly what was on
screen. If the delta is re-extracted afterwards, the review no longer applies.

Read `04-iteration-ledger/decisions.md` too — you need it to spot restatements
and contradictions.

### 2. Orient

Before the first candidate, give the librarian the shape of the review:

```
Delta: 2026-07-30-onboarding-standup
Source: 01-transcripts/2026-07-30-onboarding-standup.md

  2 candidate decisions   (1 high, 1 low confidence)
  1 candidate question
  1 action item
  2 items not promoted

Contradicts an existing record: none
```

### 3. Walk the candidates

One at a time. For each, show:

- **id, title, confidence** — and the confidence note if it is not high
- **the statement, verbatim**
- **every evidence item, verbatim**, with its anchor
- **proposed owner** and **proposed routing**
- whether it contradicts or supersedes anything already in the ledger

Then ask for an outcome. Present the options plainly:

| Outcome | Means |
|---|---|
| **accept** | Promote as written |
| **amend** | Promote with changes — statement, owner, or routing |
| **reject** | Not a decision, or not something we intend to do |
| **defer** | Leave as a candidate; revisit at a later review |

Take low-confidence candidates as slowly as the librarian wants. Those are the
ones the gate exists for. Do not summarise a low-confidence candidate — show
them the evidence and let them read it.

If the librarian rejects, ask for a one-line reason. This is not bureaucracy: a
recorded rejection is what distinguishes a considered decision from an
oversight when someone reads this back in six months.

### 4. Review what was NOT promoted

Do not skip this. Present the extractor's `not_promoted` list with topic,
reason and evidence, and ask whether anything there should have been proposed.

This is the half of the gate that catches extractor misses. A librarian who only
reviews suggestions is reviewing the extractor's output, not the meeting.

If the librarian promotes something from this list, it goes in the review
record's `promoted_from_not_promoted` — those entries are the signal for tuning
the extraction rubric later.

### 5. Write the records

For each accepted or amended candidate:

```
python .ai/checks/next-id.py decision      # or: question
```

Write `04-iteration-ledger/decisions/DEC-nnn.json` against
`.ai/contracts/decision.schema.json`, or
`04-iteration-ledger/questions/Q-nnn.json` against the question contract.

Carry forward unchanged: `statement` (unless amended), `evidence`, `origin`.
Set from the review: `owner`, `routing`, `status: active`,
`decided_on` (the meeting date), `recorded_on` (today),
`approval.approved_by` and `approval.approved_at`.
Set `spec_impact: "pending"` where routing is anything other than `none`.

Where a candidate supersedes an existing record, update **both**: the new
record's `supersedes`, and the old record's `superseded_by` and
`status: superseded`. The validator enforces both halves.

### 6. Write the review record

`iterations/<iteration-id>/review.json`, against
`.ai/contracts/review.schema.json`. One outcome per candidate, no exceptions.

### 7. Verify

```
python .ai/checks/validate.py
python .ai/checks/build-registries.py
```

Both must pass. If validation fails, fix the records — never the validator.

### 8. Report

Tell the librarian what now exists:

```
Written:
  DEC-015  Wolfsberg CBDDQ upload is optional     → react-frontend/step-03-documents
  Q-010    Equivalent question set                → owner Joel Castaneda, no date

Rejected:
  CAND-DEC-002  restates DEC-009

Registries regenerated. 1 decision awaiting dispatch.
```

Then stop. Dispatch is a separate step.

## What this step must not do

- Do not create tickets. That is `/kb-dispatch`.
- Do not edit the transcript or the delta. Both are immutable once written.
- Do not update living documents. That happens when the change lands.
- Do not proceed if the librarian is uncertain. Deferring is a valid outcome
  and costs nothing; a wrongly promoted decision propagates into a spec.
