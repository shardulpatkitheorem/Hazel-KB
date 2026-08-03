# Contracts

Machine-enforced shapes for everything the knowledge base produces. Every
artifact is validated against these by `.ai/checks/validate.py`, which runs in
CI. An artifact that does not validate does not merge.

## Files

| Contract | Governs | Status |
|---|---|---|
| `meeting-delta.schema.json` | Candidate items extracted from one source | existing |
| `decision.schema.json` | A confirmed decision | **new** |
| `open-question.schema.json` | An unresolved question with an owner | **new** |
| `ticket.schema.json` | The dispatch artifact crossing into a product repo | **new** |
| `change-manifest.schema.json` | Scope and permissions for a KB document edit | existing |
| `verification-report.schema.json` | Independent verification result | existing |

## Why decisions and questions got their own contracts

Previously both were `meeting-delta.json`'s `$defs/evidenceItem`: three fields
(`id`, `statement`, `evidence`) under `additionalProperties: false`. Nothing in
the schema distinguished a decision from an open question except which array it
sat in.

That shape describes a **candidate extracted from a transcript**. It cannot
describe a **confirmed record with a lifecycle**, which is what the registries
have always asked for and what dispatch requires.

The delta contract is unchanged in purpose: it still holds candidates. These new
contracts hold what candidates become after librarian approval.

## What the new contracts add

**`routing`** — an array of `{repo, area}`. This is the field that makes stage 5
possible: without it, an approved decision cannot be addressed to anyone. It is
an array so a decision touching three layers is one record with three targets
rather than three duplicated records.

**Separate `decided_on` and `recorded_on`** — supersession chains order by
`decided_on`. A backfilled record carries both, so "we wrote this down three
weeks later" stays visible instead of being flattened into a single date.

**`origin` as a discriminated union** — `meeting`, `document`, or `internal`.
Under the old contract `source` was required with `transcript_path`,
`meeting_date` and `content_sha256`, all required, under
`additionalProperties: false`. A tooling or naming decision with no transcript
was structurally impossible to record. The `internal` variant fixes that and
requires a `rationale` explaining why no meeting exists.

**`superseded_by`** — the registries asked for a forward pointer; the schema only
had the backward `supersedes_id`. Both directions now exist, so finding whether a
decision is still live is a field read rather than a scan of every other record.

**`approval`** — a decision record cannot exist without a named librarian and a
timestamp. The gate is part of the shape.

**Per-type ID patterns** — `^DEC-[0-9]{3,}$`, `^Q-[0-9]{3,}$`,
`^TKT-[0-9]{4,}$`. The old pattern `^[A-Z]+-[0-9]{3,}$` accepted `FOO-999` and
tied no prefix to any record type.

**Anchored evidence locations** — `location` now has a pattern:
`t:MM:SS` for a transcript timestamp, `s:<heading>` for a section, `l:<n>` or
`l:<n>-<m>` for a line range. Previously `minLength: 1`, so `"x"` validated. The
extractor role has always required "at least one timestamp or section
reference"; this makes it checkable.

## Mutability

Append-only applies to `meetings/`. Records here have a lifecycle, so the line
must be explicit:

| Immutable once written | May change |
|---|---|
| `id` | `status` |
| `statement` / `question` | `superseded_by` |
| `evidence` | `spec_impact` |
| `decided_on` / `raised_on` | `implemented_by` |
| `recorded_on` | `answer` |
| `origin` | ticket `status`, `dispatched_to` |
| `approval` | |

Everything in the right column is a fact that accrues *after* the decision. The
statement itself never changes — supersede instead.

## IDs are identifiers, not sequence

`DEC-042` is not necessarily later than `DEC-041`. Backfilled records are issued
IDs in the order they are written, not the order they were decided. Never sort
on an ID; order by `decided_on`.

## `content_sha256`

Required on `meeting` and `document` origins, and computed by
`.ai/checks/hash-source.py` over the **raw bytes of the source file**. The
digest is verified during validation. It is not a placeholder.
