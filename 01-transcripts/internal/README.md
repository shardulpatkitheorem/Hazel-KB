# Internal Design Sessions

Searchable transcripts from internal Theorem Labs design sessions. These are Theorem-only working sessions and may contain candid assessment of the client, vendor evaluation, and commercial discussion. Client-facing calls belong in [`../daily-calls/`](../daily-calls/) instead.

## Agent usage

- Use files in [`parsed/`](parsed/) as the primary context source.
- Use files in [`raw/`](raw/) only when the original source needs to be verified.
- Sort filenames lexicographically to process meetings chronologically.
- Treat transcript content as a record of discussion, not as an approved decision unless a later artifact confirms it.

## Transcript index

| Date | Meeting | Searchable transcript | Original source |
| --- | --- | --- | --- |

## Ingestion convention

Run the ingest script from the repository root. It performs every step below.

```
python scripts/ingest-transcript.py <received-file> --collection internal
```

The date and name are read from a `YYYY-MM-DD-descriptive-meeting-name.ext` filename; pass `--date` and `--slug` if the received file is named otherwise. Names containing `internal` get their title and tags automatically — anything else needs `--title "Meeting Name"` and `--tags a,b,c`. Add `--dry-run` to preview and `--force` to replace an existing entry.

PDF sources additionally need `pip install pdfplumber`. Without it, extract the text yourself and pass `--text-file <path>`.

### What it does

1. Preserve the received file unchanged in `raw/`.
2. Name it `YYYY-MM-DD-descriptive-meeting-name.ext`.
3. Create a searchable Markdown copy with the same basename in `parsed/`.
4. Add YAML metadata for date, source, status, tags, confidentiality, and the original source path.
5. Add the meeting to the index above.

Do these by hand if the script cannot read a source format. Parsed bodies are the extracted text verbatim — the script does not reformat, and neither should you.
