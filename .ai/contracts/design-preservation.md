# Hazel Workflow Design-Preservation Contract

## Protected by default

- All `:root` CSS custom-property names and values.
- External font imports and every `font-family` declaration.
- Image sources, inline SVG markup, and any element or asset containing `logo` in its path, ID, class, alt text, or accessible label.
- The page shell, title block, metadata panel, legend, header, footer, and responsive breakpoints.
- Existing workflow phases outside the approved manifest.
- Existing decisions, approvals, open questions, owners, identifiers, and status labels outside the approved manifest.

## Allowed only with explicit manifest authorization

- Global CSS or font changes require `permissions.allow_global_styles: true`.
- Logo or brand changes require `permissions.allow_brand_assets: true`.
- Page-shell changes require `permissions.allow_page_shell: true`.
- Deleting or superseding a decision requires its stable ID and replacement evidence.
- Resolving an open question requires evidence of the answer and approval authority.

## Implementation standard

- Prefer text edits within existing components.
- Prefer existing classes and CSS variables.
- Add the fewest new selectors possible.
- Do not rename existing classes unless required by an approved acceptance criterion.
- Do not reformat the entire HTML file.
- Do not introduce unrelated cleanup.

## Verification standard

Source guardrails are mandatory but not sufficient. A reviewer must compare before and after rendering at desktop and mobile widths. Unexpected changes outside approved regions fail verification.
