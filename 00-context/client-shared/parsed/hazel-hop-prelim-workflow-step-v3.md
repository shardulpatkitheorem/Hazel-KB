---
title: "Hazel HOP + Prelim Workflow Step"
document_type: "workflow"
source: "client"
client: "Hazel"
date: "2026-07-21"
status: "parsed"
version: "3"
tags:
  - "hop"
  - "prelim"
  - "account-opening"
  - "document-generation"
confidentiality: "client-confidential"
source_file: "../raw/hazel-hop-prelim-workflow-step-v3.docx"
---

# Hazel HOP + Prelim Workflow Step

## Source Text

Hazel HOP + Prelim Workflow Step
Version 3 — updated from Norma field email and Daily HOP Standup transcript | July 21, 2026
Decision direction from the transcript: For MVP, keep Prelim as a sub-workflow inside the broader HOP onboarding process rather than rebuilding all Prelim/DocuSign/account-opening logic natively. HOP should trigger or hand off to Prelim, monitor Prelim state, and then continue the next Hazel workflow step after the Prelim package is complete.

1. Scope of This Document
This document is only about the Prelim document-generation, signature, and account-opening workflow step inside HOP.
It intentionally excludes unrelated Daily HOP topics such as infrastructure access, Teams access, broader prospecting design, and data-team setup unless they directly affect the Prelim workflow step.
HOP remains the overarching workflow and user-facing onboarding experience; Prelim is a sub-workflow/platform dependency for the account-opening/document package portion.
2. Updated Field List for the Prelim Package
Use this as the working minimum data set for the Prelim signature-card/document package. HOP may already know some fields from earlier steps and can send them to Prelim; other fields may be collected directly in the Prelim flow if that preserves Prelim branching logic.
Area
Field / Element
Why it matters for Prelim
Status / Source Note
Business
Business Name / Legal Bank Name
Needed for signature card, onboarding record, and Prelim package.
HOP likely already captures earlier; send to Prelim.
Business
EIN
Business identifier for document package.
From Norma email.
Business
Physical Address
Business address field.
From Norma email; HOP may already capture.
Business
Mailing Address, if applicable
Additional business address field.
Added from Norma email.
Business
State/Country and Date of Organization
Organization jurisdiction and date.
Added/expanded from Norma email.
Business
Nature of Business
Signature-card business field.
From Norma email; may be new for Prelim.
Business
Business Email Address
Business contact field.
Added from Norma email.
Business
Business Phone Number
Business contact field.
Added from Norma email.
Signer
Signer Name
Required signer field.
From Norma email.
Signer
Relationship (Signer)
Signer role/relationship.
Added from Norma email.
Signer
Physical Address
Signer address.
From Norma email.
Signer
ID Information
Signer identification details.
From Norma email; avoid unnecessary Databricks storage.
Signer
Signer Email Address
Signer contact field.
Added from Norma email.
Signer
Mobile Number
Signer contact field.
Added from Norma email.
Signer
Date of Birth
Likely required because signers are physical people and still need KYC.
Clarified in Daily HOP transcript.
Signer
SSN, optional for business account signers
Norma said optional; Daily HOP clarified signers likely still require SSN/KYC handling.
Confirm policy and downstream storage.
Signer / BSA / Archive
Pseudo TIN if SSN is not provided
Norma said Vantage creates pseudo TIN for BSA/archive if no SSN is provided.
Confirm if Infinant/HOP need similar handling.
Account
Infinite Account Number
Must be the account number on signature card/resolution if those forms include an account number.
Daily HOP clarified this should be Infinite, not Fiserv.
Authorization
Signer authority / ability to transact
Resolution identifies authorized transactors; signature card contains signer info/signatures.
From Prelim call and Daily HOP.
3. Prelim Document Package and Signature Treatment
Document
Treatment / note
Signature card
Signature required. Includes signer information/signatures and has a spot for the account number.
Resolution / RESO
Signature required. Shows authorized signers and transact authority; has a spot for account number.
Wire agreement / wire form
Signature required. Included in the package and expected to draw from entity information where applicable.
E-Docs disclosure
Disclosure/acknowledgement, not one of the signature-required documents discussed as top three.
All-in-one terms and conditions
Disclosure/acknowledgement.
Hazel Membership Agreement
Signature required. Hazel-specific agreement added to the package.
Hazel Security Procedures
Signature required. Hazel-specific procedures added to the package.
4. MVP Workflow for the Prelim Step
Step
Prelim workflow stage
Updated working rule
1
HOP reaches the account-opening/document-package stage
Earlier HOP steps handle invite/initiation, eligibility, NDA, due diligence, and approval logic. Prelim is not the entire HOP flow.
2
Trigger or hand off to Prelim
MVP direction is to use Prelim as the account-opening/document sub-workflow. HOP should either trigger Prelim through API or use a practical manual handoff until integration exists.
3
Prelim collects or receives the required fields
HOP can pass known fields such as legal bank name/address. Prelim may collect additional signer/account data directly to preserve its branching logic.
4
Prelim uses existing/customized business account-opening logic
Copy the existing business account-opening/in-branch flow, simplify for Hazel, remove unnecessary pieces, and add Hazel-specific documents.
5
Reserve or generate Infinite account number before signatures
Daily HOP clarified the forms should use the Infinite account number. Open action is to ask Infinite whether it can reserve an account number like Fiserv does before final account opening.
6
Prelim routes documents for signature/acknowledgement
Prelim is expected to use DocuSign or a DocuSign-like signing flow for the package.
7
HOP validates Prelim state and moves forward
Theorem should evaluate whether Prelim APIs can trigger the workflow/signing ceremony and validate completion state so HOP knows when to proceed.
8
Completed package links to Infinite and Databricks record
Final records should tie back to the underlying bank/customer/account record. Sensitive PII should be retained in Infinite where appropriate; Databricks/HOP should keep reference IDs/links rather than unnecessary DOB/SSN/ID data.
5. Prelim Build / Configuration Requirements
Use Prelim for MVP, but keep optionality: MVP preference is to leverage Prelim because branch/back-office workflows, DocuSign, KYB/KYC, and account-opening logic already exist. If the rebuild is heavier than expected, reassess whether to build natively.
Copy and simplify existing business account opening: Norma indicated Prelim could copy the current workflow and adjust it for Hazel; prior estimate was about six weeks once work starts.
Remove non-Hazel requirements: Remove beneficial ownership for member banks and remove unrelated due-diligence/risk pieces that are handled by Coverbase/HOP.
Keep signer KYC-related data: Even though beneficial ownership is not needed for banks, signers are physical people and likely still require DOB, ID, SSN, and related KYC handling.
Add Hazel-specific documents: Add Hazel Membership Agreement and Hazel Security Procedures to the package.
Handle account number from Infinite: Remove/replace core/Fiserv account-number integration. Add path for Infinite account number, ideally reserve-before-signature if Infinite supports it.
API integration topic: Confirm whether Prelim APIs can trigger the workflow/signing ceremony and report completion/state back to HOP.
State validation: HOP should know when Prelim is complete so the broader HOP flow can advance to the next step.
Data minimization: Avoid storing sensitive signer PII in Databricks/HOP when Infinite can hold it; keep links/reference IDs where possible.
Architecture posture: Build HOP as technology-agnostic where possible; accept stronger Prelim coupling for MVP only if it meaningfully accelerates delivery.
6. Open Questions / Actions from the Transcript
Infinite account-number reservation: Ask Infinite whether it can reserve an account number without fully activating/opening the account, similar to the Fiserv pattern described by Shawn.
Infinite tenant/account API recipe: Clarify the API path for setting up a member-bank tenant and initial accounts, including whether account-number generation can happen early enough for Prelim documents.
Prelim API capability: Confirm whether Prelim can be triggered by API, whether it can initiate the signing ceremony, and how HOP can validate status/completion.
Prelim vs. native decision gate: If Prelim customization is too heavy, reassess whether to build the workflow natively in HOP.
Signer KYC fields: Confirm the exact signer requirements: DOB, ID, SSN, address, and how optional SSN/pseudo-TIN should flow through Infinant/Infinite and document storage.
Final storage/linking model: Confirm what goes to Infinite, what stays in Prelim, what is retained in HOP/Databricks, and what should only be referenced by ID.
Manual MVP fallback: Define who manually kicks off Prelim, keys fields if needed, and retrieves/links final signed documents before API integration exists.
7. Clean Summary for Prelim / Theorem Follow-Up
Prelim is a step inside HOP, not the full HOP onboarding platform.
For MVP, the preferred approach is to leverage Prelim as a sub-workflow because it already has account-opening workflow, branching logic, DocuSign integration, and back-office familiarity.
HOP should remain the system of experience/orchestration; Prelim can remain the document/account-opening sub-workflow; Infinite should be the downstream banking/account system for sensitive account and signer data where appropriate.
The highest-priority technical questions are Prelim API trigger/status capability and Infinite account-number reservation/provisional-account capability.
If Prelim requires too much custom rebuild, then the team should compare it against building the document/signature flow natively in HOP.
Source Notes
Primary source: Daily HOP Standup.docx, meeting recording transcript dated July 21, 2026, 4:00 PM UTC, 1h 13m 26s.
Additional source: Business Information Capture email from Norma Saenz for business/signature-card field list and pseudo-TIN note.
Additional source: Prelim options with Onboarding Hazel banks meeting transcript for the original Prelim workflow concept and Norma discussion.
This version intentionally filters out non-Prelim topics from the Daily HOP Standup transcript.
