# Daily Call Transcripts

Searchable transcripts from Hazel and Theorem Labs working sessions.

## Agent usage

- Use files in [`parsed/`](parsed/) as the primary context source.
- Use files in [`raw/`](raw/) only when the original source needs to be verified.
- Sort filenames lexicographically to process meetings chronologically.
- Treat transcript content as a record of discussion, not as an approved decision unless a later artifact confirms it.

## Transcript index

| Date | Meeting | Searchable transcript | Original source |
| --- | --- | --- | --- |
| 2026-07-16 | Hazel Onboarding Kick-Off — Part 1 | [Markdown](parsed/2026-07-16-hazel-onboarding-kickoff-part-1.md) | [PDF](raw/2026-07-16-hazel-onboarding-kickoff-part-1.pdf) |
| 2026-07-16 | Hazel Onboarding Kick-Off — Part 2 | [Markdown](parsed/2026-07-16-hazel-onboarding-kickoff-part-2.md) | [PDF](raw/2026-07-16-hazel-onboarding-kickoff-part-2.pdf) |
| 2026-07-21 | Daily HOP Standup | [Markdown](parsed/2026-07-21-daily-hop-standup.md) | [Text](raw/2026-07-21-daily-hop-standup.txt) |
| 2026-07-22 | Daily HOP Standup | [Markdown](parsed/2026-07-22-daily-hop-standup.md) | [Text](raw/2026-07-22-daily-hop-standup.txt) |
| 2026-07-23 | Daily HOP Standup | [Markdown](parsed/2026-07-23-daily-hop-standup.md) | [Word](raw/2026-07-23-daily-hop-standup.docx) |
| 2026-07-24 | Daily HOP Standup | [Markdown](parsed/2026-07-24-daily-hop-standup.md) | [Text](raw/2026-07-24-daily-hop-standup.txt) |
| 2026-07-27 | Daily HOP Standup | [Markdown](parsed/2026-07-27-daily-hop-standup.md) | [Text](raw/2026-07-27-daily-hop-standup.txt) |

## Ingestion convention

1. Preserve the received file unchanged in `raw/`.
2. Name it `YYYY-MM-DD-descriptive-meeting-name.ext`.
3. Create a searchable Markdown copy with the same basename in `parsed/`.
4. Add YAML metadata for date, source, status, tags, confidentiality, and the original source path.
5. Add the meeting to the index above.
