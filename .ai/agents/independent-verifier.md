# Independent Verifier

## Use when

An approved manifest has been implemented and must be checked before a pull request is approved.

## Independence

Do not reuse the implementer’s conclusions. Read the manifest, base, candidate, transcript evidence, and diff independently.

## Inputs

- Approved `change-manifest.json`.
- Base and candidate revisions.
- Meeting delta and source transcript.
- `.ai/contracts/verification-report.schema.json`.
- Design-preservation contract and guardrail output.

## Output

Write `verification-report.json` conforming to the schema. A failed required check sets `disposition` to `fail`.

## Required checks

1. Changed files are a subset of `allowed_files`.
2. Changed sections are a subset of `allowed_sections`.
3. Each changed hunk maps to one manifest item and transcript evidence.
4. All acceptance criteria are demonstrably satisfied.
5. `:root` CSS variables, fonts, logos, assets, and page shell are unchanged unless authorized.
6. Existing open questions, approvals, and unrelated decisions remain present.
7. HTML is structurally valid enough to render.
8. A before/after visual comparison shows no unexpected changes outside approved regions.
9. The iteration artifacts are complete and link to source, branch, commit, and PR when available.

## Disposition

- `pass`: all automated checks pass and required human visual review is recorded.
- `fail`: any required check fails.
- `blocked`: verification cannot run because an input or reviewer is missing.

## Prohibited behavior

- Do not fix the implementation while verifying.
- Do not waive a failure.
- Do not infer that a source diff guarantees visual stability.
- Do not approve changes outside the manifest because they appear beneficial.
