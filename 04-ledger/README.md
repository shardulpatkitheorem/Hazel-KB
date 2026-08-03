# Hazel Ledger

This directory is the audit trail for meeting-driven changes shared by Vantage and Theorem.

## One folder per meeting

Create:

```text
meetings/YYYY-MM-DD-meeting-slug/
├── meeting-delta.json
├── summary.md
├── change-manifest.json
├── verification-report.json
└── final-diff.md
```

Use the templates under `.ai/templates/`. Validate artifacts against `.ai/contracts/`.

## Lifecycle

1. Add the evidence-backed meeting delta and concise summary.
2. Add the proposed change manifest.
3. Record human scope approval in the manifest.
4. Add the implementation diff and independent verification report.
5. Add branch, commit, and pull-request references.
6. After merge, update the derived decisions and open-question registries.
7. Promote a lesson only when it passes the lesson admission test.

## Append-only rule

An iteration becomes immutable when its pull request merges. Correct an error through a new iteration that links to the original; do not silently rewrite history. Superseded decisions remain visible.

## No-change meetings

Create an iteration even when no implementation is warranted. Set the delta status to `no_change`, explain the evidence-backed reason, and leave implementation artifacts in their documented blocked/no-change state.

## Review requirement

Vantage and Theorem must approve scope before implementation and approve the pull request before merge.
