# Client-Shared Context

Source material provided by Vantage for Hazel discovery, configuration, risk, vendor, and workflow work.

## Agent usage

- Use [`parsed/`](parsed/) for searchable context and structured data.
- Use [`raw/`](raw/) to verify the original source, formatting, formulas, or workbook behavior.
- Treat these files as client-provided context, not automatically as approved product requirements.
- Preserve source traceability when deriving specifications, decisions, or implementation tasks.

## Document catalog

| Document | Purpose | Agent-readable form | Original |
| --- | --- | --- | --- |
| Consolidated Vendor Report | Vendor and service inventory exported from Coverbase | [CSV sheets](parsed/consolidated-vendor-report/) | [XLSX](raw/consolidated-vendor-report.xlsx) |
| CoverBaseSS | Coverbase reference material | Image-based PDF; consult original | [PDF](raw/coverbase-ss.pdf) |
| Hazel Configuration Workbook — TransPecos | Compliance, tenant, product, limit, fee, operating-account, and card configuration | [CSV sheets](parsed/hazel-configuration-workbook-transpecos/) | [XLSX](raw/hazel-configuration-workbook-transpecos.xlsx) |
| Hazel Inherent Risk Questionnaire Template | Risk-question structure, options, mappings, guidance, and sections | [Questions CSV](parsed/hazel-inherent-risk-questionnaire-template/questions.csv) | [XLSX](raw/hazel-inherent-risk-questionnaire-template.xlsx) |
| Hazel HOP + Prelim Workflow Step v3 | Working workflow direction for the Prelim sub-workflow inside HOP | [Markdown](parsed/hazel-hop-prelim-workflow-step-v3.md) | [DOCX](raw/hazel-hop-prelim-workflow-step-v3.docx) |

## Storage convention

1. Keep received files unchanged in `raw/` with lowercase kebab-case filenames.
2. Store searchable or machine-readable conversions in `parsed/`.
3. Record source references in every derived specification.
4. Put approved requirements and decisions in a separate versioned specification rather than modifying client source files.
5. Do not place secrets, live credentials, or unnecessary sensitive personal information in derived artifacts.

## Conversion notes

- Spreadsheet tabs are exported individually as UTF-8 CSV while the original workbooks retain formulas, styling, and external-link metadata.
- `CoverBaseSS` is an image-based PDF and does not currently have a reliable text extraction.
- The Prelim workflow Markdown preserves the source wording and adds repository metadata; it is not an approval record.
