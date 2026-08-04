<!-- GENERATED FILE — DO NOT EDIT.
     Source of truth: 04-ledger/decisions/*.json
     Regenerate:      python .ai/checks/build-registries.py
     Records hash:    9e4f16605b76d7f1 -->

# Decision Registry

4 active · 0 superseded · generated 2026-08-03

Ordered by decision date. Decision IDs are identifiers, not sequence — never infer chronology from them.

## Active

| ID | Decision | Decided | Owner | Routes to | Spec |
|---|---|---|---|---|---|
| `DEC-001` | The Wolfsberg questionnaire is not mandatory; a fallback question set is asked in Hazel onboarding | 2026-07-27 | Joel Olivares | react-frontend/step-03-documents, wf-orchestration/step-03-documents | change:wolfsberg-optional-fallback |
| `DEC-002` | Signing the NDA in Hazel onboarding satisfies the Vanta trust-center NDA requirement | 2026-07-27 | Shawn | integration-wrapper/vanta, wf-orchestration/step-02-nda | ⚠ pending |
| `DEC-003` | CoverBase risk scoring is internal-only; the member portal shows a general status | 2026-07-27 | unknown | react-frontend/member-portal, wf-orchestration/risk-assessment | ⚠ pending |
| `DEC-004` | The bank confirms, corrects or declines CoverBase-prepared answers, with the source document shown | 2026-07-27 | unknown | react-frontend/step-04-risk-questions, integration-wrapper/coverbase | ⚠ pending |

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
