<!-- GENERATED FILE — DO NOT EDIT.
     Source of truth: 04-ledger/questions/*.json
     Regenerate:      python .ai/checks/build-registries.py
     Records hash:    c280d1e24db22540 -->

# Open Questions

5 outstanding · 0 answered · generated 2026-08-04

## Outstanding

| ID | Question | Owner | Due | Raised | Blocks |
|---|---|---|---|---|---|
| `Q-001` | What form does the Wolfsberg fallback take — dynamic questions, an optional field, or a template upload? | ⚠ unowned | ⚠ no date | 2026-07-27 | `DEC-001` |
| `Q-002` | Must intake process documents be stored in Databricks? | Joel Olivares | ⚠ no date | 2026-07-27 | — |
| `Q-003` | Is GitHub access ready for the build team? | ⚠ unowned | ⚠ no date | 2026-07-27 | — |
| `Q-004` | Which two documents gate due diligence, and where was that requirement decided? | ⚠ unowned | ⚠ no date | 2026-07-27 | — |
| `Q-005` | Does Coverbase accept a fallback answer payload in place of extracted Wolfsberg content? | ⚠ unowned | ⚠ no date | 2026-08-03 | `DEC-001` |

## Detail

### Q-001 — What form does the Wolfsberg fallback take — dynamic questions, an optional field, or a template upload?

When a bank has no Wolfsberg document, is the fallback presented as dynamic in-flow questions, as an optional field offering either upload or answers, as a pop-up or page, or as a downloadable template the bank fills in and uploads? Deferred until the number and type of questions is known.

- **Owner** unknown · no committed date
- **Raised** 2026-07-27 · `01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md` (2026-07-27)
- **Evidence** `t:0:25:34`, `t:0:26:02`
- **Blocks** `DEC-001`
- **Concerns** react-frontend/step-03-documents

### Q-002 — Must intake process documents be stored in Databricks?

Does the intake process have to store the documents it collects into Databricks? Named as an outstanding piece to lock down.

- **Owner** Joel Olivares · no committed date
- **Raised** 2026-07-27 · `01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md` (2026-07-27)
- **Evidence** `t:0:32:17`
- **Concerns** wf-orchestration/data-storage

### Q-003 — Is GitHub access ready for the build team?

What is the status of GitHub readiness and access provisioning for the team? Deferred to a later call.

- **Owner** unknown · no committed date
- **Raised** 2026-07-27 · `01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md` (2026-07-27)
- **Evidence** `t:0:32:17`, `t:0:33:04`
- **Concerns** none/infrastructure

### Q-004 — Which two documents gate due diligence, and where was that requirement decided?

Which two documents must be in place before a member bank can continue to the due diligence part, and in which session was that requirement decided? It is reported here as a change already made, attributed to an earlier call that is not in the ledger, so the requirement has no DEC- id to cite.

- **Owner** unknown · no committed date
- **Raised** 2026-07-27 · `01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md` (2026-07-27)
- **Evidence** `l:49`
- **Concerns** react-frontend/step-03-documents

### Q-005 — Does Coverbase accept a fallback answer payload in place of extracted Wolfsberg content?

DEC-001 requires that answers to the fallback question set are pushed to Coverbase in place of content that would otherwise be extracted from a Wolfsberg CBDDQ. Nothing confirms Coverbase's intake accepts such a payload, or how it maps to the control set. If it does not, DEC-001 is not implementable as recorded.

- **Owner** unknown · no committed date
- **Raised** 2026-08-03 · internal — Shardul Patki
- **Evidence** `s:Requirement: Fallback answers are persisted and pushed to Coverbase`
- **Blocks** `DEC-001`
- **Concerns** integration-wrapper/coverbase
