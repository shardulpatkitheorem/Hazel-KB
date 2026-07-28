# Hazel Knowledge Base Agent Instructions

This repository contains client-confidential Hazel and Vantage context.

## Evidence and provenance

- Prefer repository evidence over assumptions.
- Use `parsed/` material for retrieval and `raw/` material for source verification.
- Cite repository-relative source paths in specifications, summaries, and implementation notes.
- Do not treat meeting discussion, client source material, or prototypes as approved requirements without an explicit decision artifact.
- Preserve raw files unchanged and keep generated or transformed material separate.

## Specification-driven development

- Read `02-design-and-workflows/PROTOTYPE-SPEC.md` before prototype work.
- Define the objective, actors, role boundaries, source references, states, assumptions, acceptance criteria, and open questions before implementation.
- Clearly label simulated integrations and unverified behavior.
- Store material prototype revisions as new dated snapshots under `02-design-and-workflows/mocks/versions/`.

## Design consistency

- Reuse `02-design-and-workflows/mocks/hub-assets/tokens.css`.
- Reuse `02-design-and-workflows/mocks/hub-assets/brand/hazel-network-logo.svg`.
- Do not redraw or alter the logo.
- Preserve accessible focus, semantic labels, reduced-motion support, and responsive behavior.

## Safety

- Do not add secrets, credentials, unnecessary personal information, or real regulated-customer data.
- Treat all content as client-confidential unless explicitly marked otherwise.
- Clearly label generated content, assumptions, open questions, and unverified claims.
