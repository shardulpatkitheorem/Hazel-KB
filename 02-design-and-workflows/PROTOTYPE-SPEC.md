---
title: "Hazel Prototype Development Specification"
document_type: "design"
source: "generated"
client: "Hazel"
date: "2026-07-28"
status: "draft"
version: "1.0"
tags:
  - "prototype"
  - "design-system"
  - "spec-driven-development"
confidentiality: "client-confidential"
---

# Hazel Prototype Development Specification

This specification defines how Hazel prototypes are sourced, styled, versioned, and reviewed. It is the default contract for future prototype work unless a more specific approved specification overrides it.

## 1. Evidence before implementation

Every material prototype change must identify:

- the user or operator problem being explored;
- the actors and permissions involved;
- the transcript, client document, decision, or requirement that motivated the change;
- assumptions that are not yet confirmed;
- the states and edge cases the prototype demonstrates;
- what is explicitly out of scope.

Client documents and meeting transcripts are evidence. They do not become approved requirements merely because they are represented in a prototype.

## 2. Required build specification

Before implementation, create or update a versioned specification containing:

1. objective and success criteria;
2. source references using repository-relative paths;
3. actors and role boundaries;
4. happy path, alternate paths, and failure states;
5. data collected, displayed, retained, or handed off;
6. integration assumptions and simulated behavior;
7. acceptance criteria that can be checked in the prototype;
8. unresolved questions and the owner of each decision.

## 3. Canonical visual system

Use [`mocks/hub-assets/tokens.css`](mocks/hub-assets/tokens.css) as the source of truth for new shared styling.

| Token | Value | Intended use |
| --- | --- | --- |
| `--hz-plum` | `#3a1c32` | Primary brand text, navigation, dark surfaces |
| `--hz-ink` | `#140a14` | Body text |
| `--hz-red` | `#eb001f` | Primary actions, active states, required emphasis |
| `--hz-red-hover` | `#c9001b` | Primary-action hover state |
| `--hz-orange` | `#ff6e46` | Review accents and secondary emphasis |
| `--hz-muted` | `#645573` | Secondary text |
| `--hz-mint-50` | `#f8fef9` | Primary light background |
| `--hz-mint-200` | `#dfe9e1` | Subtle borders and supporting surfaces |
| `--hz-white` | `#ffffff` | Cards and inverse text |
| `--hz-line` | `rgba(58, 28, 50, 0.24)` | Borders and separators |
| `--hz-focus` | `rgba(235, 0, 31, 0.28)` | Keyboard focus treatment |

Typography:

- Use `--hz-font-sans` for controls, navigation, labels, and body copy.
- Use `--hz-font-editorial` for major headings and editorial emphasis.
- Preserve the defined system fallbacks when licensed brand fonts are unavailable.

Brand:

- Use [`hazel-network-logo.svg`](mocks/hub-assets/brand/hazel-network-logo.svg).
- Do not redraw the logo, substitute a CSS mark, alter its colors, or distort its aspect ratio.

## 4. Interaction and content rules

- A prototype must clearly identify simulated behavior and must not imply a live production integration.
- Never embed real credentials, secrets, regulated customer information, or unnecessary personal data.
- Prefer explicit status labels over color-only communication.
- Include keyboard focus states, semantic labels, and reduced-motion behavior.
- Model loading, empty, validation, permission, unavailable, and recovery states where relevant.
- Keep internal-only information out of member-facing views.
- Use external-safe language for messages shown to member banks.

## 5. Versioning

- Store reviewable prototype snapshots at `mocks/versions/YYYY-MM-DD/index.html`.
- Once shared for review, do not silently overwrite a dated snapshot.
- Create another dated snapshot for material changes; add a suffix only when multiple independently reviewed builds occur on the same date.
- Name workflow schematics `descriptive-name-vMAJOR.MINOR.html`.
- Use semantic version changes:
  - patch: wording or visual correction with no workflow change;
  - minor: additive or revised workflow behavior;
  - major: incompatible workflow, role, or information-architecture change.

## 6. Review checklist

A build is ready to share when:

- source references and assumptions are documented;
- acceptance criteria are demonstrable;
- the Hazel logo and visual tokens are used consistently;
- member and operator boundaries are clear;
- simulated integrations are labeled;
- common responsive widths and keyboard navigation have been checked;
- no secrets or sensitive real-person data are present;
- the snapshot opens using repository-relative assets;
- known gaps are recorded in the associated specification.
