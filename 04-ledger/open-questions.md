<!-- GENERATED FILE — DO NOT EDIT.
     Source of truth: 04-ledger/questions/*.json
     Regenerate:      python .ai/checks/build-registries.py
     Records hash:    2aebea3bd32f77f7 -->

# Open Questions

13 outstanding · 0 answered

## Outstanding

| ID | Question | Owner | Due | Raised | Blocks |
|---|---|---|---|---|---|
| `Q-001` | What form does the Wolfsberg fallback take — dynamic questions, an optional field, or a template upload? | ⚠ unowned | ⚠ no date | 2026-07-27 | `DEC-001` |
| `Q-002` | Must intake process documents be stored in Databricks? | Joel Olivares | ⚠ no date | 2026-07-27 | — |
| `Q-003` | Is GitHub access ready for the build team? | ⚠ unowned | ⚠ no date | 2026-07-27 | — |
| `Q-004` | Which two documents gate due diligence, and where was that requirement decided? | ⚠ unowned | ⚠ no date | 2026-07-27 | — |
| `Q-005` | Does Coverbase accept a fallback answer payload in place of extracted Wolfsberg content? | ⚠ unowned | ⚠ no date | 2026-08-03 | `DEC-001` |
| `Q-006` | Has Jonathan confirmed that an electronic NDA acknowledgement is acceptable? | ⚠ unowned | ⚠ no date | 2026-08-03 | `DEC-005` |
| `Q-007` | Which Databricks components are used, and is data in a database or lakehouse tables? | Shantanu Wadodkar | 2026-08-03 | 2026-08-03 | — |
| `Q-008` | What data is shared with a prospective partner before an NDA is in place? | ⚠ unowned | ⚠ no date | 2026-08-03 | — |
| `Q-009` | What are the membership stages, what qualifies a bank for each, and what limits apply? | ⚠ unowned | ⚠ no date | 2026-08-03 | — |
| `Q-010` | How are duties split between the infrastructure team and the build team? | Shawn Main | 2026-08-03 | 2026-08-03 | — |
| `Q-011` | Has Tate signed off on the electronic NDA acknowledgement mock-up? | ⚠ unowned | ⚠ no date | 2026-08-04 | `DEC-005`, `DEC-010` |
| `Q-012` | Which document at the documents step remains mandatory? | ⚠ unowned | ⚠ no date | 2026-08-04 | `DEC-013` |
| `Q-013` | Can the Vanta trust-center NDA step be removed, and how is a requester verified without it? | Joel Olivares | ⚠ no date | 2026-08-04 | `DEC-002` |

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

### Q-006 — Has Jonathan confirmed that an electronic NDA acknowledgement is acceptable?

Is capturing the customer's name, title and date as an electronic agreement acceptable as acknowledgement of the NDA, instead of executing it through DocuSign? Norma Saenz sent the proposal to the team for review and is waiting to hear back from Jonathan.

- **Owner** unknown · no committed date
- **Raised** 2026-08-03 · `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:11:31`, `t:0:13:18`
- **Blocks** `DEC-005`
- **Concerns** wf-orchestration/step-02-nda

### Q-007 — Which Databricks components are used, and is data in a database or lakehouse tables?

Which Databricks components will the end-to-end workflow leverage, which of them are serverless, and is application data stored in a database or as lakehouse tables? Raised as an open design item with the conclusion targeted for the same day.

- **Owner** Shantanu Wadodkar · due 2026-08-03
- **Raised** 2026-08-03 · `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:05:41`
- **Concerns** wf-orchestration/architecture

### Q-008 — What data is shared with a prospective partner before an NDA is in place?

Between a partner's initial login and account creation and Hazel approving them, what information could be shared while no NDA has been executed? Joel Olivares raised the exposure created by deferring the full signature to the end of the journey and left it as something for the team to think about.

- **Owner** unknown · no committed date
- **Raised** 2026-08-03 · `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:12:06`, `t:0:12:52`
- **Concerns** wf-orchestration/step-02-nda, react-frontend/onboarding

### Q-009 — What are the membership stages, what qualifies a bank for each, and what limits apply?

How many onboarding stages are there, what does a bank get at each one, what risk criteria qualify it, and what transaction limits and permitted use cases attach to each stage? Chris Colson proposed a three-stage model taken from The Clearing House's RTP onboarding; Shawn Main accepted the risk-adjusted direction but said the requirements still have to be worked out.

- **Owner** unknown · no committed date
- **Raised** 2026-08-03 · `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:18:20`, `t:0:19:46`
- **Concerns** wf-orchestration/onboarding

### Q-010 — How are duties split between the infrastructure team and the build team?

What are the respective duties and responsibilities of David Gonzalez and Zeb on infrastructure versus Shantanu Wadodkar's build team on development? Deferred to a 1 o'clock call on the day of the meeting.

- **Owner** Shawn Main · due 2026-08-03
- **Raised** 2026-08-03 · `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:15:18`, `t:0:15:41`
- **Concerns** none/infrastructure

### Q-011 — Has Tate signed off on the electronic NDA acknowledgement mock-up?

Is the mock-up — name of the user, their title, the date, and their electronic acknowledgement, rendered to a PDF — acceptable as the NDA acknowledgement? Norma Saenz sent it and has had no reply. Aaron McWilliams spoke to Tate separately and relayed that signature, name and date are still required, then closed the topic with "we'll verify that".

- **Owner** unknown · no committed date
- **Raised** 2026-08-04 · `01-transcripts/daily-calls/parsed/2026-08-04-daily-hop-standup.md` (2026-08-04)
- **Evidence** `t:0:05:27`, `t:0:05:27`, `t:0:05:59`
- **Blocks** `DEC-005`, `DEC-010`
- **Concerns** react-frontend/step-02-nda, wf-orchestration/step-02-nda

### Q-012 — Which document at the documents step remains mandatory?

Joel Olivares ruled that one document at the documents step cannot be made optional and must stay required, while the Wolfsberg upload becomes "if applicable". The transcript refers to it only as "that one" and "this one" against a screen share, so which document it is cannot be recovered from the source.

- **Owner** unknown · no committed date
- **Raised** 2026-08-04 · `01-transcripts/daily-calls/parsed/2026-08-04-daily-hop-standup.md` (2026-08-04)
- **Evidence** `t:0:15:56`, `t:0:16:25`
- **Blocks** `DEC-013`
- **Concerns** react-frontend/step-03-documents

### Q-013 — Can the Vanta trust-center NDA step be removed, and how is a requester verified without it?

Vanta presents the NDA a second time when a partner requests Hazel's security data through the Trust Center. Can that step be removed, given Vanta exists to evidence Hazel's security procedures for SOC certification? If it is removed, how does Hazel establish that a party asking for the data is a real bank already in the onboarding flow rather than a random requester?

- **Owner** Joel Olivares · no committed date
- **Raised** 2026-08-04 · `01-transcripts/daily-calls/parsed/2026-08-04-daily-hop-standup.md` (2026-08-04)
- **Evidence** `t:0:05:59`, `t:0:06:58`, `t:0:08:07`, `t:0:08:17`
- **Blocks** `DEC-002`
- **Concerns** integration-wrapper/vanta, wf-orchestration/step-02-nda
