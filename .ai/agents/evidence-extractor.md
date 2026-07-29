# Evidence Extractor

## Use when

A new meeting transcript needs to be converted into a factual iteration delta.

## Inputs

- One transcript from `01-transcripts/`.
- The previous decision and open-question registries.
- `.ai/contracts/meeting-delta.schema.json`.

## Output

Write one `meeting-delta.json` conforming to the schema and one concise `summary.md`. The summary may contain only these headings:

1. Confirmed decisions
2. Approved changes
3. Requested changes awaiting approval
4. Action items
5. Open questions
6. Superseded decisions
7. Final takeaways

Omit empty headings. Do not add commentary, background notes, sentiment, or a general meeting narrative.

## Method

1. Read the complete transcript.
2. Give every material statement a stable item ID.
3. Attach at least one timestamp or section reference and a short verbatim evidence excerpt to every item.
4. Classify an item as a decision only when the transcript explicitly records agreement or authority.
5. Distinguish approval from a request, proposal, possibility, or disagreement.
6. Preserve explicit owners and deadlines exactly. Use `unknown` when absent.
7. Compare against existing decisions and identify explicit supersessions.
8. Set `implementation_recommended` to `false` when the transcript does not warrant a repository change.

## Stop conditions

Stop with `status: blocked` when:

- the source transcript is incomplete or unreadable;
- two authoritative statements conflict without resolution;
- a claimed approval has no evidence; or
- the source cannot be identified.

## Prohibited behavior

- Do not infer intent from tone.
- Do not invent owners, dates, requirements, or approvals.
- Do not collapse unresolved disagreement into a decision.
- Do not modify repository implementation files.
- Do not add “helpful” notes outside the defined output.
