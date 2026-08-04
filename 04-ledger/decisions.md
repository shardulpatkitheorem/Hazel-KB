<!-- GENERATED FILE — DO NOT EDIT.
     Source of truth: 04-ledger/decisions/*.json
     Regenerate:      python .ai/checks/build-registries.py
     Records hash:    fc5f4f299500bdc5 -->

# Decision Registry

8 active · 0 superseded · generated 2026-08-04

Ordered by decision date. Decision IDs are identifiers, not sequence — never infer chronology from them.

## Active

| ID | Decision | Decided | Owner | Routes to | Spec |
|---|---|---|---|---|---|
| `DEC-001` | The Wolfsberg questionnaire is not mandatory; a fallback question set is asked in Hazel onboarding | 2026-07-27 | Joel Olivares | react-frontend/step-03-documents, wf-orchestration/step-03-documents | change:wolfsberg-optional-fallback |
| `DEC-002` | Signing the NDA in Hazel onboarding satisfies the Vanta trust-center NDA requirement | 2026-07-27 | Shawn | integration-wrapper/vanta, wf-orchestration/step-02-nda | ⚠ pending |
| `DEC-003` | CoverBase risk scoring is internal-only; the member portal shows a general status | 2026-07-27 | unknown | react-frontend/member-portal, wf-orchestration/risk-assessment | ⚠ pending |
| `DEC-004` | The bank confirms, corrects or declines CoverBase-prepared answers, with the source document shown | 2026-07-27 | unknown | react-frontend/step-04-risk-questions, integration-wrapper/coverbase | ⚠ pending |
| `DEC-005` | The NDA is acknowledged electronically, not by DocuSign; one full signature at the end | 2026-08-03 | Joel Olivares | react-frontend/step-02-nda, wf-orchestration/step-02-nda, integration-wrapper/docusign | ⚠ pending |
| `DEC-006` | Authentication and authorization run outside Databricks, on Azure | 2026-08-03 | Shawn Main | wf-orchestration/architecture, react-frontend/authentication | ⚠ pending |
| `DEC-007` | The blank Wolfsberg questionnaire PDF is removed; upload only for banks that hold one | 2026-08-03 | Joel Olivares | react-frontend/step-03-documents | ⚠ pending |
| `DEC-008` | The workflow must not hard-code Vantage's requirements; Vantage is a reference only | 2026-08-03 | Shawn Main | wf-orchestration/architecture, react-frontend/onboarding | ⚠ pending |

## Detail

### DEC-001 — The Wolfsberg questionnaire is not mandatory; a fallback question set is asked in Hazel onboarding

A bank that does not hold a Wolfsberg questionnaire is not blocked. It answers an equivalent set of questions inside the Hazel onboarding flow instead, and that data is pushed to CoverBase. The questions are asked by the Hazel-built onboarding rather than by CoverBase directly. A bank that does hold a Wolfsberg document continues on the existing path.

- **Decided** 2026-07-27 by Joel Olivares · recorded 2026-08-03
- **Source** `01-transcripts/daily-calls/parsed/2026-07-27-daily-hop-standup.md` (2026-07-27)
- **Evidence** `t:0:16:02`, `t:0:27:38`, `t:0:28:04`
- **Routes to** react-frontend/step-03-documents, wf-orchestration/step-03-documents
- **Spec impact** change:wolfsberg-optional-fallback
- **Implemented by** https://github.com/shardulpatkitheorem/hop-frontend-demo/pull/2
- **Approved by** Shardul Patki on 2026-08-03

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
