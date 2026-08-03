# Meeting-to-Workflow Agent Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Add a documented, contract-driven, verifiable AI loop for converting meeting transcripts into controlled Hazel workflow updates.

**Architecture:** Four isolated agent roles exchange schema-validated artifacts through two human approval gates. A dependency-free verifier enforces file scope and protects global visual identity, while an append-only ledger preserves every iteration and durable lesson.

**Tech Stack:** Markdown, JSON Schema Draft 2020-12, Python 3 standard library, GitHub pull requests.

## Global Constraints

- No agent writes directly to `main`.
- Every material claim cites transcript evidence.
- Implementation is limited to an approved manifest.
- Logos, global CSS tokens, fonts, and page shell are protected by default.
- Iteration history is append-only.
- Meeting-specific facts never become global lessons.

---

### Task 1: Documentation and operating model

**Files:**
- Create: `docs/AI-MEETING-TO-WORKFLOW-LOOP.md`
- Create: `.ai/AGENTS.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: approved design.
- Produces: human-readable workflow and repository-wide agent routing.

- [x] Write the manager-facing flow, roles, gates, ledger, and file tree.
- [x] Write repository agent routing and non-negotiable rules.
- [x] Link the workflow from the root README.
- [x] Verify links and placeholder-free prose.

### Task 2: Agent role specifications

**Files:**
- Create: `.ai/agents/evidence-extractor.md`
- Create: `.ai/agents/change-planner.md`
- Create: `.ai/agents/workflow-implementer.md`
- Create: `.ai/agents/independent-verifier.md`
- Create: `.ai/prompts/run-meeting-loop.md`

**Interfaces:**
- Consumes: artifact contracts from Task 3.
- Produces: bounded prompts with explicit inputs, outputs, stop conditions, and prohibitions.

- [x] Define evidence extraction and no-inference rules.
- [x] Define minimal-scope planning and human approval gate.
- [x] Define implementation constraints and retry behavior.
- [x] Define independent verification and failure reporting.
- [x] Define the end-to-end invocation prompt.
- [x] Verify every role names its contract and stop conditions.

### Task 3: Machine-readable contracts and templates

**Files:**
- Create: `.ai/contracts/meeting-delta.schema.json`
- Create: `.ai/contracts/change-manifest.schema.json`
- Create: `.ai/contracts/verification-report.schema.json`
- Create: `.ai/contracts/design-preservation.md`
- Create: `.ai/templates/meeting-delta.json`
- Create: `.ai/templates/change-manifest.json`
- Create: `.ai/templates/verification-report.json`

**Interfaces:**
- Produces: JSON Schema Draft 2020-12 contracts and valid starter instances.

- [x] Define required identifiers, evidence, status enums, and approval fields.
- [x] Define allowed scope and protected-element fields.
- [x] Define verification checks and final disposition.
- [x] Create valid templates containing neutral example values.
- [x] Parse all JSON and validate templates against schemas.

### Task 4: Deterministic repository guardrails

**Files:**
- Create: `.ai/checks/protected-workflow-elements.json`
- Create: `.ai/checks/verify-workflow-guardrails.py`
- Create: `.ai/checks/fixtures/base.html`
- Create: `.ai/checks/fixtures/pass.html`
- Create: `.ai/checks/fixtures/fail-logo.html`
- Create: `.ai/checks/fixtures/fail-css.html`
- Create: `.ai/checks/fixtures/manifest.json`

**Interfaces:**
- Command: `python3 .ai/checks/verify-workflow-guardrails.py --base BASE --candidate CANDIDATE --manifest MANIFEST --changed-file PATH`
- Exit `0`: protected elements and scope pass.
- Exit `1`: one or more guardrail failures, emitted as JSON.

- [x] Write fixtures that represent allowed copy change and prohibited logo/CSS changes.
- [x] Run the verifier before implementation and confirm the expected failure.
- [x] Implement file allowlist, `:root`, font, and logo comparison.
- [x] Run passing and failing fixtures and confirm exit codes.

### Task 5: Append-only ledger

**Files:**
- Create: `04-ledger/README.md`
- Create: `04-ledger/decisions.md`
- Create: `04-ledger/open-questions.md`
- Create: `04-ledger/lessons.md`
- Create: `04-ledger/meetings/.gitkeep`

**Interfaces:**
- Consumes: approved deltas, manifests, reports, PR links.
- Produces: immutable iteration history plus derived decision/question/lesson registries.

- [x] Document iteration creation and immutability rules.
- [x] Add registry formats with provenance requirements.
- [x] Add the durable-lesson admission test.
- [x] Verify no meeting-specific placeholder claims exist.

### Task 6: Repository verification and publication

**Files:**
- Modify: plan checkboxes after execution.

**Interfaces:**
- Produces: reviewed Git branch and draft pull request.

- [x] Parse every JSON file.
- [x] Validate all templates against their schemas.
- [x] Run positive and negative guardrail fixtures.
- [x] Scan for unresolved `TBD` or `TODO`.
- [x] Review `git diff --check`, file tree, and scoped diff.
- [x] Commit, push, and open a draft pull request against `main`.
