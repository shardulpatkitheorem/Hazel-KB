# Run the Hazel meeting-to-workflow loop

Use this prompt from the repository root:

```text
Run the Hazel meeting-to-workflow loop for:
TRANSCRIPT: <repository-relative transcript path>
WORKFLOW: <repository-relative workflow HTML path>
ITERATION_ID: <YYYY-MM-DD-meeting-slug>

Follow .ai/AGENTS.md and run each role from .ai/agents/ in order.

Phase 1:
- Produce and schema-validate the meeting delta.
- Produce the concise summary with no additional notes.
- If no repository change is warranted, create the no-change iteration record and stop.

Phase 2:
- Produce and schema-validate a minimal proposed change manifest.
- Show the exact scope, protected elements, acceptance criteria, evidence, and required reviewers.
- Stop for human scope approval. Do not edit implementation files.

Phase 3 (only after explicit approval):
- Confirm the base commit is current.
- Apply the smallest permitted patch on a feature branch.
- Do not regenerate the entire workflow.
- Run repository guardrails.

Phase 4:
- Independently verify evidence, scope, acceptance criteria, protected elements, retained questions/approvals, and visual stability.
- Produce the schema-valid verification report.
- Create or update a draft PR only when required checks pass.
- Append the ledger after merge; promote only durable behavioral rules to lessons.md.
```
