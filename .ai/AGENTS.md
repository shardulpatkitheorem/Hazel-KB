# Hazel Knowledge Base Agent Rules

## Required loop

For work originating from a meeting transcript, run these roles in order:

1. `.ai/agents/evidence-extractor.md`
2. `.ai/agents/change-planner.md`
3. Human scope approval
4. `.ai/agents/workflow-implementer.md`
5. `.ai/agents/independent-verifier.md`
6. Human pull-request approval

Do not skip a role or combine implementation with verification.

## Non-negotiable rules

- Never write directly to `main`.
- Treat client content as confidential.
- Cite transcript evidence for every decision, request, action, and question.
- Do not infer decisions, owners, deadlines, or approvals.
- Make the smallest change that satisfies an approved manifest.
- Protect logos, assets, global CSS tokens, fonts, page shell, and unrelated workflow sections.
- Preserve open questions, approvals, and superseded decisions.
- Append an iteration record even when no repository change is warranted.
- Put meeting facts in their iteration. Put only reusable behavior rules in `04-iteration-ledger/lessons.md`.
- Stop and request human resolution when evidence conflicts or scope is ambiguous.

## Artifact validation

Artifacts must conform to the schemas in `.ai/contracts/`. Run the guardrail verifier before requesting review:

```bash
python3 .ai/checks/verify-workflow-guardrails.py \
  --base path/to/base.html \
  --candidate path/to/candidate.html \
  --manifest path/to/change-manifest.json \
  --changed-file "02-design-and-workflows/workflow-html/<file>.html"
```

An iteration cannot pass when the verifier returns a non-zero exit code.
