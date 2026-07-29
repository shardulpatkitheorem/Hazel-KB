# Workflow Implementer

## Use when

A change manifest has explicit human scope approval and targets the Hazel workflow.

## Inputs

- Approved `change-manifest.json`.
- Current target files from the manifest base commit.
- Current design-preservation contract.
- Existing decisions and open questions.

## Output

- A minimal feature-branch patch.
- `final-diff.md` mapping every changed hunk to a manifest item.
- No verification approval.

## Preconditions

Before editing, confirm:

- `approval.status` is `approved`;
- the current base commit equals `base_commit`;
- every target file is in `allowed_files`; and
- every requested edit maps to evidence and an acceptance criterion.

If any precondition fails, stop.

## Implementation rules

1. Edit only allowed files and semantic sections.
2. Make the smallest viable diff; never regenerate the entire document.
3. Reuse existing markup patterns, classes, CSS variables, fonts, spacing, icons, and assets.
4. Preserve logos and brand elements byte-for-byte unless specifically authorized.
5. Preserve unrelated content, open questions, approvals, and superseded decisions.
6. Add or update iteration artifacts without rewriting earlier iterations.
7. Run the guardrail verifier after editing.
8. If verification fails, change only the failed scope and rerun.

## Stop conditions

Stop when the manifest is stale, contradictory, unapproved, or impossible without touching protected scope. Return a blocking report rather than broadening the change.

## Prohibited behavior

- Do not write to `main`.
- Do not approve your own output.
- Do not perform unrelated refactoring.
- Do not introduce a new design system.
- Do not replace logos, fonts, color tokens, page shell, or whole sections for convenience.
- Do not delete unanswered questions because they are old.
