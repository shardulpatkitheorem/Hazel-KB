# Design and Workflow Assets

Shared Hazel styling, prototype snapshots, and workflow schematics for specification-driven development.

Read [`PROTOTYPE-SPEC.md`](PROTOTYPE-SPEC.md) before creating or modifying a prototype.

## Structure

```text
02-design-and-workflows/
├── PROTOTYPE-SPEC.md
├── mocks/
│   ├── index.html
│   ├── auth.html
│   ├── hub-assets/
│   │   ├── tokens.css
│   │   ├── style.css
│   │   ├── auth.css
│   │   ├── review-shell.css
│   │   └── brand/hazel-network-logo.svg
│   └── versions/
│       └── YYYY-MM-DD/index.html
└── workflow-html/
    └── versioned workflow schematics
```

## Current artifacts

- [Prototype review hub](mocks/index.html)
- [Prototype access page](mocks/auth.html)
- [2026-07-28 member-bank onboarding prototype](mocks/versions/2026-07-28/index.html)
- [Hazel onboarding workflow v1.4](workflow-html/hazel-onboarding-workflow-v1.4.html)
- [Hazel Network logo](mocks/hub-assets/brand/hazel-network-logo.svg)

## Reuse rules

- Use [`tokens.css`](mocks/hub-assets/tokens.css) as the canonical prototype palette and typography source.
- Reuse the SVG logo; do not recreate or approximate it in CSS.
- Treat dated directories in `mocks/versions/` as immutable review snapshots.
- Create a new dated snapshot for material prototype changes.
- Use semantic versions for workflow schematics.
- Link each build or specification to the transcripts, client documents, and decisions that informed it.

## Known runtime dependencies

The supplied hub and access HTML reference `hub-assets/app.js` and `hub-assets/auth.js`, but those runtime files were not included in the provided asset set. Styling, logo, workflow HTML, and the dated prototype are preserved; the review-hub loading/auth behavior requires those scripts or a later replacement.
