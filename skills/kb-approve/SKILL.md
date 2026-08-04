---
name: kb-approve
description: Review all candidates in a meeting delta at once, promote the accepted ones to authoritative records, and land them on the working branch. This is the human gate — run it deliberately, never automatically.
disable-model-invocation: true
---

# Librarian review

This is the gate. Everything upstream produces candidates; nothing is
authoritative until it passes through here. One approval does two things at
once: it confirms an item into the ledger, and it authorises its dispatch to a
product repository.

**You are not the reviewer.** The librarian is. Your job is to present the
candidates clearly, capture their judgement exactly, write the records, and land
them. You do not decide, and you do not persuade.

## Constraints

- **Never accept a candidate on your own judgement.** Every outcome comes from
  the librarian, stated explicitly. Silence is not acceptance.
- **Never invent, tidy, or improve a statement.** If the librarian wants
  different wording, they say so and it is recorded as an amendment.
- **Every candidate gets an outcome.** No candidate is silently dropped.
- **Allocate ids only via the script.** Never guess the next number.
- **Ask for confirmation exactly once**, at step 6, before anything is written.
  Never ask again after that; never ask before.

## Procedure

### 1. Set up

Read the delta at `meetings/<meeting-id>/meeting-delta.json` and hash it:

```
python .ai/checks/hash-source.py meetings/<meeting-id>/meeting-delta.json
```

That hash goes in the review record and binds the review to exactly what was on
screen. If the delta is re-extracted afterwards, the review no longer applies.

Note the current branch. If it is `main`, create `review/<meeting-id>` and
switch to it. Otherwise stay where you are — the librarian has chosen a branch.

Read `04-ledger/decisions.md` to spot restatements and contradictions.

### 2. Present everything at once

Do **not** walk candidates one at a time. Show all of them in two tables, then
ask for a single disposition.

```
Delta: 2026-07-27-daily-hop-standup
Source: 01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md
Branch: review/2026-07-27-daily-hop-standup

DECISIONS
 #  id             Conf   Owner           Routes to                        Title
 1  CAND-DEC-001   med    Joel Olivares   hop-frontend-demo/step-03-docs   Wolfsberg not mandatory…
 2  CAND-DEC-002   low    Shawn           integration-wrapper/vanta        NDA satisfies Vanta…

QUESTIONS
 #  id             Conf   Owner           Due        Title
 7  CAND-Q-001     high   unowned         —          What form the fallback takes…

NOT PROMOTED (4)
 a  withdrawn_by_speaker      Collecting fallback questions in Coverbase
 b  explicitly_parked         How the fallback is presented

Contradicts an existing record: none
```

Then, unprompted, expand **only** the low-confidence candidates — full statement
and every evidence excerpt verbatim. Those are what the gate exists for; the
librarian should not have to ask to see them.

### 3. Take the disposition

Ask once:

> Give me your disposition. Anything you don't mention, I'll ask about.

Accept freeform input in any shape, for example:

```
accept 1, 4, 6, 7
defer 2, 3 — needs a real conversation first
reject 5 — restates DEC-004
amend 8: owner should be unknown, Robert never confirmed
```

Rules for reading it:

- Numbers, ids, and ranges (`1-4`) all resolve. Ask if anything is ambiguous.
- `reject` and `defer` need a reason. If one is missing, ask for that reason and
  nothing else.
- `amend` needs the field and the new value.
- If any candidate is unaccounted for after parsing, list only those and ask.
  Do not re-ask about ones already dispositioned.

### 4. Ask what is missing entirely

`not_promoted` shows what the extractor considered and declined. It cannot show
what the extractor never saw.

Decisions stated **descriptively** are the common miss: nobody says "let's
require this", they discuss an existing requirement as settled fact. The
extractor looks for decision moments, finds none, and the requirement is never
proposed — and never appears in `not_promoted` either.

Ask directly, once: **is anything settled in this source that no candidate
covers?**

If the librarian names something, find it, quote it verbatim, anchor it (a line
anchor if the block is long), and record it in the review's
`added_by_librarian` with a `reason_missed`.

### 5. Draft the records

Allocate ids:

```
python .ai/checks/next-id.py decision --count <n>
python .ai/checks/next-id.py question --count <n>
```

Build each record against its contract. Carry forward unchanged: `statement`,
`evidence`, `origin`. Set from the review: `owner`, `routing`, `status`,
`decided_on` (the meeting date), `recorded_on` (today), and `approval`.
Set `spec_impact: "pending"` where routing is anything other than `none`.

**Owner rule.** An owner is recorded only where the source shows that person
*accepting* it. Named-at but silent is `unknown`. Someone whose position was
relayed by another speaker is `unknown`. This is not a judgement call — apply it
uniformly and say so if it changes what the candidate proposed.

Where a candidate supersedes an existing record, update **both**: the new
record's `supersedes`, and the old record's `superseded_by` and
`status: superseded`.

Do not write anything to disk yet.

### 6. ══ CONFIRM ══ once

Show the finished records as a compact table — id, title, owner, routing, and
for questions the due date. Flag anything the owner rule changed.

```
About to write 2 decisions, 1 question, and the review record:

  DEC-001  Wolfsberg not mandatory…            Joel Olivares   hop-frontend-demo/step-03-documents
  DEC-002  NDA satisfies Vanta…                unknown ←       integration-wrapper/vanta
  Q-001    What form the fallback takes…       unowned         —

  ← owner weakened by the owner rule

Then commit, merge to <branch>, and push. Proceed?
```

Wait for a yes.

**This is the only confirmation.** The librarian's disposition in step 3 is the
gate; this is a transcription check — confirming the records say what they said,
not re-deciding whether to approve. Do not ask again at any later step.

### 7. Write

On a yes, write everything:

- `04-ledger/decisions/DEC-nnn.json`
- `04-ledger/questions/Q-nnn.json`
- `meetings/<meeting-id>/review.json` — one outcome per candidate, no
  exceptions, plus `promoted_from_not_promoted` and `added_by_librarian` where
  they apply

Then:

```
python .ai/checks/validate.py
python .ai/checks/build-registries.py
```

Both must pass. If validation fails, fix the records — never the validator, and
never by loosening a check. Report the failure and stop; do not commit a failing
ledger.

### 8. Land it

With validation green, commit and merge without asking again:

```
git add -A
git commit -m "feat(ledger): approve records from <meeting-id>"
git checkout <the branch you came from>
git merge review/<meeting-id>
git branch -d review/<meeting-id>
git push
```

If you were already on a working branch at step 1 rather than creating one,
commit and push there — there is nothing to merge.

If the merge conflicts, stop and report it. Do not resolve a ledger conflict
yourself.

### 9. Report

```
Written and merged.

  DEC-001  Wolfsberg not mandatory…       → hop-frontend-demo/step-03-documents
  Q-001    What form the fallback takes…  → unowned, no date

  Deferred 3 · Rejected 1
  Registries regenerated. 1 decision awaiting dispatch.

Next: python .ai/checks/dispatch.py DEC-001 --dry-run
```

Then stop. Dispatch is a separate step.

## What this step must not do

- Do not create tickets or open issues. That is dispatch.
- Do not edit the transcript or the delta. Both are immutable once written.
- Do not update living documents. That happens when the change lands.
- Do not proceed if the librarian is uncertain about a candidate. Deferring is
  a valid outcome and costs nothing; a wrongly promoted decision propagates
  into a spec.
