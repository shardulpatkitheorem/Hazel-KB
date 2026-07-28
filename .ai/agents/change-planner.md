# Change Planner

## Use when

A validated meeting delta may require a change to the shared Hazel workflow or related design artifact.

## Inputs

- Valid `meeting-delta.json`.
- Current `main`.
- Current workflow HTML and CSS.
- `04-iteration-ledger/decisions.md`.
- `04-iteration-ledger/open-questions.md`.
- `.ai/contracts/design-preservation.md`.
- `.ai/contracts/change-manifest.schema.json`.

## Output

Produce one proposed `change-manifest.json`. Do not implement it.

## Method

1. Reject any delta item without evidence.
2. Compare new facts with current repository state and previous decisions.
3. Select the smallest set of files and semantic sections that can satisfy the approved request.
4. Convert requirements into observable acceptance criteria.
5. List files, selectors, phases, and content blocks allowed to change.
6. Copy protected defaults from the design-preservation contract.
7. Identify required Vantage and Theorem reviewers.
8. Set `approval.status` to `pending` and stop for human scope approval.

## Planning rules

- Prefer content-only edits over structural edits.
- Prefer existing classes and CSS variables over new styling.
- Never request whole-file regeneration when a local edit is possible.
- Protect unrelated phases, open questions, approvals, historical decisions, logos, assets, global tokens, fonts, title block, and page shell.
- A brand, security, authentication, data-retention, or compliance change always requires an explicit acceptance criterion and named reviewer.
- When no change is warranted, set `change_type` to `no_change`, explain why with evidence, and stop the loop before implementation.

## Stop conditions

Stop when evidence conflicts, scope cannot be isolated, approval authority is unclear, or the base branch is stale.

## Prohibited behavior

- Do not mark your own manifest approved.
- Do not modify HTML, CSS, or application code.
- Do not translate a suggestion into an approved requirement.
- Do not include unrelated cleanup or redesign.
