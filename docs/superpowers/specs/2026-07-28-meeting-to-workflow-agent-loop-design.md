# Meeting-to-Workflow Agent Loop Design

## Objective

Create a reliable, reviewable pipeline that converts Hazel meeting transcripts into minimal changes to the shared onboarding workflow while preserving visual design, branding, provenance, approvals, and iteration history.

## Constraints

- Transcript output contains final takeaways and structured decisions, actions, approvals, and open questions—no free-form extra notes.
- Discussion cannot be classified as a decision without explicit transcript evidence.
- Agents never write directly to `main`.
- Implementation changes only approved files and sections.
- Existing CSS, typography, layout, assets, and logos are preserved unless the change manifest explicitly authorizes them.
- The shared workflow retains unresolved questions, approvals, ownership, and superseded history.
- Every iteration produces an append-only delta, including iterations with no code change.
- Durable agent-behavior lessons are separated from meeting-specific facts.

## Architecture

The loop uses four isolated roles connected by versioned JSON artifacts:

1. Evidence Extractor: transcript to meeting delta.
2. Change Planner: delta plus repository state to proposed change manifest.
3. Workflow Implementer: approved manifest to minimal patch.
4. Independent Verifier: patch plus manifest to verification report.

Human scope approval separates planning from implementation. Human PR approval separates verified output from `main`.

## Artifact contracts

`meeting-delta.json` records source metadata and evidence-linked decisions, changes, actions, questions, supersessions, and takeaways.

`change-manifest.json` records approval state, authorized file/section scope, protected elements, acceptance criteria, evidence references, and reviewers.

`verification-report.json` records every automated and human-required check, failures, changed files/sections, and final disposition.

All artifacts include `schema_version`, `iteration_id`, and stable item IDs. IDs are never reused.

## Design preservation

The current workflow establishes its visual language in `:root` CSS variables, font imports/families, reusable classes, page shell, and any image/SVG/logo elements. These are protected by default.

The automated verifier compares a base and candidate file. Unless globally authorized, it rejects changes to:

- `:root` variable declarations;
- font imports and `font-family` declarations;
- image elements, inline SVG elements, and references containing `logo`;
- files outside the manifest allowlist.

Rendered screenshot comparison remains a required human/visual check because source-level checks cannot detect every layout regression.

## Iteration ledger

Each iteration directory is immutable after merge except for corrections made through a new linked iteration. Global decisions and open questions are derived registries; they link back to the originating iteration. `lessons.md` accepts only reusable rules with evidence, trigger, required behavior, and date adopted.

## Failure handling

- Missing or ambiguous evidence: extractor records `unknown` and blocks promotion to a decision.
- Conflicting decisions: planner records the conflict and requires human resolution.
- Unauthorized scope: verifier fails the patch.
- Guardrail failure: implementer receives the report and retries only the failed scope.
- No warranted change: the iteration records `no_change` with evidence and stops before implementation.
- Stale base: implementation is regenerated against the latest `main` before review.

## Acceptance criteria

- Manager-facing workflow documentation is readable without repository context.
- Each agent has a bounded prompt with inputs, outputs, stop conditions, and prohibited behavior.
- JSON schemas validate the three machine-readable artifacts.
- A dependency-free guardrail script detects unauthorized file, CSS-token, font, and logo changes.
- Templates make the next meeting iteration executable without inventing structure.
- Repository documentation explains invocation, approval, verification, and ledger promotion.
