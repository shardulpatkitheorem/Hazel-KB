<!-- GENERATED FILE — DO NOT EDIT.
     Source of truth: 04-ledger/decisions/*.json
     Regenerate:      python .ai/checks/build-registries.py
     Records hash:    938a0d7f46e9a2b2 -->

# Decision Registry

15 active · 1 superseded

Ordered by decision date. Decision IDs are identifiers, not sequence — never infer chronology from them.

## Active

| ID | Decision | Decided | Owner | Routes to | Spec |
|---|---|---|---|---|---|
| `DEC-002` | Signing the NDA in Hazel onboarding satisfies the Vanta trust-center NDA requirement | 2026-07-27 | Shawn | integration-wrapper/vanta, wf-orchestration/step-02-nda | ⚠ pending |
| `DEC-003` | CoverBase risk scoring is internal-only; the member portal shows a general status | 2026-07-27 | unknown | react-frontend/member-portal, wf-orchestration/risk-assessment | ⚠ pending |
| `DEC-004` | The bank confirms, corrects or declines CoverBase-prepared answers, with the source document shown | 2026-07-27 | unknown | react-frontend/step-04-risk-questions, integration-wrapper/coverbase | ⚠ pending |
| `DEC-014` | The residual risk score and the yes/no result are not automated and require manual oversight | 2026-07-31 | Joel Olivares | wf-orchestration/risk-assessment, integration-wrapper/coverbase | ⚠ pending |
| `DEC-015` | The relaxed front-of-flow document requirements are scoped to FDIC-insured accounts | 2026-07-31 | Joel Olivares | react-frontend/step-03-documents, wf-orchestration/step-03-documents | ⚠ pending |
| `DEC-016` | The signed NDA identifies the partner entity in its relationship header, not only the signer | 2026-07-31 | Joel Olivares | react-frontend/step-02-nda, wf-orchestration/step-02-nda | ⚠ pending |
| `DEC-005` | The NDA is acknowledged electronically, not by DocuSign; one full signature at the end | 2026-08-03 | Joel Olivares | react-frontend/step-02-nda, wf-orchestration/step-02-nda, integration-wrapper/docusign | ⚠ pending |
| `DEC-006` | Authentication and authorization run outside Databricks, on Azure | 2026-08-03 | Shawn Main | wf-orchestration/architecture, react-frontend/authentication | ⚠ pending |
| `DEC-007` | The blank Wolfsberg questionnaire PDF is removed; upload only for banks that hold one | 2026-08-03 | Joel Olivares | react-frontend/step-03-documents | ⚠ pending |
| `DEC-008` | The workflow must not hard-code Vantage's requirements; Vantage is a reference only | 2026-08-03 | Shawn Main | wf-orchestration/architecture, react-frontend/onboarding | ⚠ pending |
| `DEC-009` | No Wolfsberg question set is asked of banks that do not hold the questionnaire | 2026-08-04 | unknown | react-frontend/step-03-documents, wf-orchestration/step-03-documents, integration-wrapper/coverbase | ⚠ pending |
| `DEC-010` | The electronic NDA acknowledgement captures signature, name and date and is retained as a PDF | 2026-08-04 | unknown | react-frontend/step-02-nda, wf-orchestration/step-02-nda | ⚠ pending |
| `DEC-011` | The e-signature is sent only on the final package, after Hazel's internal review loop closes | 2026-08-04 | unknown | wf-orchestration/step-02-nda, react-frontend/onboarding | ⚠ pending |
| `DEC-012` | The NDA appears in the document repository as a completed activity, with a downloadable copy | 2026-08-04 | Aaron McWilliams | react-frontend/document-repository, wf-orchestration/step-02-nda | ⚠ pending |
| `DEC-013` | The Wolfsberg upload is labelled "if applicable"; one other document at that step stays required | 2026-08-04 | Joel Olivares | react-frontend/step-03-documents | ⚠ pending |

## Detail

### DEC-002 — Signing the NDA in Hazel onboarding satisfies the Vanta trust-center NDA requirement

The applicant bank signs one NDA, in the Hazel onboarding flow. That signature satisfies the NDA that Vanta requires before Hazel's due diligence package is released through the Trust Center, so the bank is not asked to execute a second NDA there.

- **Decided** 2026-07-27 by Shawn · recorded 2026-08-03
- **Source** `01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md` (2026-07-27)
- **Evidence** `t:0:20:15`, `t:0:20:21`
- **Routes to** integration-wrapper/vanta, wf-orchestration/step-02-nda
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-03

### DEC-003 — CoverBase risk scoring is internal-only; the member portal shows a general status

The member bank portal never surfaces the CoverBase risk assessment score, risk band or findings. Applicants see only a general application status. The internal Hazel operator opens the CoverBase assessment section to see the score, band and findings, and returns to the HOP portal to request missing information from the bank.

- **Decided** 2026-07-27 by unknown · recorded 2026-08-03
- **Source** `01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md` (2026-07-27)
- **Evidence** `l:49`, `l:49`
- **Routes to** react-frontend/member-portal, wf-orchestration/risk-assessment
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-03

### DEC-004 — The bank confirms, corrects or declines CoverBase-prepared answers, with the source document shown

Risk answers prepared by CoverBase are returned to the member bank for review. For each one the bank may confirm it, correct it, or state "I'm unable to confirm". The portal tells the bank which already-supplied document each prepared answer was drawn from.

- **Decided** 2026-07-27 by unknown · recorded 2026-08-03
- **Source** `01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md` (2026-07-27)
- **Evidence** `l:49`, `l:49`
- **Routes to** react-frontend/step-04-risk-questions, integration-wrapper/coverbase
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-03

### DEC-014 — The residual risk score and the yes/no result are not automated and require manual oversight

The Coverbase side of intake is not fully automated. Running the residual risk, generating the report and averaging it out into the yes/no result given back to the applicant requires manual oversight, and may involve routing the case to Hazel's internal subject-matter experts to review. This is accepted as a bottleneck inside an intake that is otherwise to be as fast as possible.

- **Decided** 2026-07-31 by Joel Olivares · recorded 2026-08-06
- **Source** `01-transcripts/daily-calls/parsed/2026-07-31-daily-hop-standup.md` (2026-07-31)
- **Evidence** `t:0:03:13`, `t:0:03:13`
- **Routes to** wf-orchestration/risk-assessment, integration-wrapper/coverbase
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-06

### DEC-015 — The relaxed front-of-flow document requirements are scoped to FDIC-insured accounts

Making the Wolfsberg questionnaire optional — and the wider removal of the friction points at the front of the flow — is limited to FDIC-insured accounts. Joel Olivares attaches the limit to the relaxation itself, and separately gives FDIC accounts as the reason he expects most residual risk reviews to be straightforward.

- **Decided** 2026-07-31 by Joel Olivares · recorded 2026-08-06
- **Source** `01-transcripts/daily-calls/parsed/2026-07-31-daily-hop-standup.md` (2026-07-31)
- **Evidence** `t:0:11:19`, `t:0:03:13`
- **Routes to** react-frontend/step-03-documents, wf-orchestration/step-03-documents
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-06

### DEC-016 — The signed NDA identifies the partner entity in its relationship header, not only the signer

The NDA that is digitally signed must name the party the agreement is between. Today the signer supplies name, title and date, but the header stating who the relationship is between is not pre-filled, so the executed PDF does not identify the partner that signed it. That counterparty information is to be populated; Coverbase is floated as a possible source but not established.

- **Decided** 2026-07-31 by Joel Olivares · recorded 2026-08-06
- **Source** `01-transcripts/daily-calls/parsed/2026-07-31-daily-hop-standup.md` (2026-07-31)
- **Evidence** `t:0:10:30`, `t:0:10:30`, `t:0:11:18`
- **Routes to** react-frontend/step-02-nda, wf-orchestration/step-02-nda
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-06

### DEC-005 — The NDA is acknowledged electronically, not by DocuSign; one full signature at the end

The applicant bank acknowledges the NDA as an electronic agreement — name, title and date captured, accept and move on — instead of executing it through DocuSign. No e-sign workflow runs at the NDA step. A single full signature is taken at the end of the journey, so the partner is not asked to sign through DocuSign several times.

- **Decided** 2026-08-03 by Joel Olivares · recorded 2026-08-04
- **Source** `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:11:31`, `t:0:12:57`, `t:0:13:10`, `t:0:13:18`
- **Routes to** react-frontend/step-02-nda, wf-orchestration/step-02-nda, integration-wrapper/docusign
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-04

### DEC-006 — Authentication and authorization run outside Databricks, on Azure

User authentication and authorization — including the authorization API and Azure External ID — sit outside the Databricks deployment, in Azure, because there is no advantage to placing them inside Databricks. This is the named exception to running everything in Databricks. The public application UI is likewise a separate deployment outside the Databricks deployment.

- **Decided** 2026-08-03 by Shawn Main · recorded 2026-08-04
- **Source** `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:09:27`, `t:0:09:34`, `t:0:05:41`
- **Routes to** wf-orchestration/architecture, react-frontend/authentication
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-04

### DEC-007 — The blank Wolfsberg questionnaire PDF is removed; upload only for banks that hold one

The onboarding flow no longer offers a blank Wolfsberg questionnaire PDF. A potential partner that already holds a completed questionnaire is given the option to upload it; a partner that does not have one is not blocked and continues. This came out of the user-experience session with Norma Saenz and Mary Campos.

- **Decided** 2026-08-03 by Joel Olivares · recorded 2026-08-04
- **Source** `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:10:23`, `t:0:10:23`
- **Routes to** react-frontend/step-03-documents
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-04

### DEC-008 — The workflow must not hard-code Vantage's requirements; Vantage is a reference only

The workflow is built so that it is not Vantage-specific. Vantage is used as a reference for what onboarding looks like, but its requirements are not the fixed shape of the product: another bank onboarding into Hazel may want a different settlement bank, and that settlement bank may impose its own requirements which must be supportable.

- **Decided** 2026-08-03 by Shawn Main · recorded 2026-08-04
- **Source** `01-transcripts/daily-calls/parsed/2026-08-03-daily-hop-standup.md` (2026-08-03)
- **Evidence** `t:0:13:18`, `t:0:13:18`, `t:0:15:05`
- **Routes to** wf-orchestration/architecture, react-frontend/onboarding
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-04

### DEC-009 — No Wolfsberg question set is asked of banks that do not hold the questionnaire

The questions contained in the Wolfsberg correspondent bank due diligence questionnaire are not asked anywhere in Hazel onboarding. A bank that holds a completed questionnaire may upload it, and that data is run against the CoverBase controls to produce a residual risk score. A bank that does not hold one is asked nothing in its place — it proceeds through the standard due diligence and risk questions, which every applicant answers regardless. A weaker residual risk score is accepted as the consequence.

- **Decided** 2026-08-04 by unknown · recorded 2026-08-05
- **Source** `01-transcripts/daily-calls/parsed/2026-08-04-daily-hop-standup.md` (2026-08-04)
- **Evidence** `t:0:19:51`, `t:0:20:06`, `t:0:20:06`, `t:0:21:37`
- **Routes to** react-frontend/step-03-documents, wf-orchestration/step-03-documents, integration-wrapper/coverbase
- **Spec impact** pending
- **Supersedes** `DEC-001`
- **Approved by** Shardul Patki on 2026-08-05

### DEC-010 — The electronic NDA acknowledgement captures signature, name and date and is retained as a PDF

The electronic acknowledgement that replaces the DocuSign NDA must capture three things: the signature, the name and the date. The mock-up form is the name of the user, their title, the date, and their electronic acknowledgement of what they are doing. The completed acknowledgement is rendered to a PDF and kept for record keeping.

- **Decided** 2026-08-04 by unknown · recorded 2026-08-05
- **Source** `01-transcripts/daily-calls/parsed/2026-08-04-daily-hop-standup.md` (2026-08-04)
- **Evidence** `t:0:05:06`, `t:0:05:21`, `t:0:05:27`
- **Routes to** react-frontend/step-02-nda, wf-orchestration/step-02-nda
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-05

### DEC-011 — The e-signature is sent only on the final package, after Hazel's internal review loop closes

The end-of-journey signature is not triggered when the applicant submits. The sequence is: the bank submits, Hazel reviews internally, the internal review may raise questions and there is back-and-forth with the bank, and only once everything is final does the document go out for e-signature. The version sent for signature is therefore the final document.

- **Decided** 2026-08-04 by unknown · recorded 2026-08-05
- **Source** `01-transcripts/daily-calls/parsed/2026-08-04-daily-hop-standup.md` (2026-08-04)
- **Evidence** `t:0:02:38`, `t:0:03:14`
- **Routes to** wf-orchestration/step-02-nda, react-frontend/onboarding
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-05

### DEC-012 — The NDA appears in the document repository as a completed activity, with a downloadable copy

The mutual NDA is surfaced to the applicant bank in the document repository as an activity record showing that it has been completed, rather than only inside the NDA step. The bank is additionally given the option to download the document, because a bank may want a PDF copy for its own records.

- **Decided** 2026-08-04 by Aaron McWilliams · recorded 2026-08-05
- **Source** `01-transcripts/daily-calls/parsed/2026-08-04-daily-hop-standup.md` (2026-08-04)
- **Evidence** `t:0:16:43`, `t:0:17:27`, `t:0:17:33`, `t:0:17:39`, `t:0:17:52`
- **Routes to** react-frontend/document-repository, wf-orchestration/step-02-nda
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-05

### DEC-013 — The Wolfsberg upload is labelled "if applicable"; one other document at that step stays required

The documents step no longer presents the Wolfsberg upload as something the bank must provide. It is relabelled to read as "if applicable, completed Wolfsberg correspondent bank due diligence questionnaire", because the current wording still implies an upload is needed. One other document at that step is explicitly not made optional and remains required.

- **Decided** 2026-08-04 by Joel Olivares · recorded 2026-08-05
- **Source** `01-transcripts/daily-calls/parsed/2026-08-04-daily-hop-standup.md` (2026-08-04)
- **Evidence** `t:0:15:56`, `t:0:16:25`, `t:0:23:58`
- **Routes to** react-frontend/step-03-documents
- **Spec impact** pending
- **Approved by** Shardul Patki on 2026-08-05

## Superseded

| ID | Decision | Decided | Superseded by |
|---|---|---|---|
| `DEC-001` | The Wolfsberg questionnaire is not mandatory; a fallback question set is asked in Hazel onboarding | 2026-07-27 | `DEC-009` |
