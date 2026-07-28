# Hazel Knowledge Base

A structured knowledge repository for client context, meeting transcripts, design artifacts, workflows, prompts, and intermediate AI outputs.

## Knowledge pipeline

```text
Sources                 Repository engine                 AI consumers
Transcripts   ─┐
Client docs   ─┼─> Markdown + YAML front matter ───────> Cursor / Copilot / IDE
Internal PPTs ─┤                │                       RAG / vector store
Mocks & HTML  ─┤                ├─> auto-index          Custom LLM workflows
AI outputs    ─┘                └─> GitHub Actions / LFS
```

## Repository structure

- `00-context/`: client-provided source material and architecture context
- `01-transcripts/`: offsite and dated daily-call transcripts
- `02-design-and-workflows/`: workflow prototypes, mocks, and design specifications
- `03-intermediate-ai-outputs/`: reusable prompts and proof-of-concept outputs
- `04-iteration-ledger/`: append-only meeting deltas, decisions, open questions, and durable lessons
- `.ai/`: agent roles, artifact contracts, prompts, templates, and deterministic guardrails

## Meeting-to-workflow AI loop

See [Hazel Meeting-to-Workflow AI Loop](docs/AI-MEETING-TO-WORKFLOW-LOOP.md) for the team-facing flowchart, agent responsibilities, approval gates, file structure, and definition of done.

## Suggested document metadata

Add YAML front matter to parsed Markdown documents:

```yaml
---
title: "Document title"
document_type: "transcript | client-doc | architecture | design | prompt | poc"
source: "client | internal | meeting | generated"
client: "Hazel"
date: "YYYY-MM-DD"
status: "raw | parsed | reviewed | approved | superseded"
version: "1.0"
owners:
  - "GitHub username or team"
tags:
  - "topic"
confidentiality: "internal | client-confidential"
source_file: "relative/path/to/original"
---
```

## Working conventions

1. Keep original client files unchanged under a `raw/` directory.
2. Store searchable Markdown conversions beside them under `parsed/`.
3. Name daily transcripts `YYYY-MM-DD.md`.
4. Version architecture and design decisions explicitly.
5. Do not commit secrets, credentials, personal data, or restricted client material without authorization.
6. Use Git LFS for large binary documents when repository policy is configured.
