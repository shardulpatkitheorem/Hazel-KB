#!/usr/bin/env python3
"""
Evidence anchor resolution.

An evidence item claims two things: that a quoted excerpt appears in a source,
and that it appears at a particular place. Neither was checked anywhere, which
meant an anchor could point at the wrong moment in a meeting — or at nothing —
and still validate.

The whole value of the ledger is that you can click an anchor and read the
sentence. An anchor that lands near the right place is a broken promise. This
module makes both claims checkable.

Supported anchor forms:

    t:MM:SS      t:HH:MM:SS      a timestamp in a transcript
    s:<heading>  a section heading
    l:<n>        l:<n>-<m>       a line or line range

Supported transcript timestamp conventions, both present in this repository:

    [00:13:59] Joel Olivares:        bracketed, HH:MM:SS
    Joel Olivares 9:02               trailing, MM:SS or HH:MM:SS
"""

from __future__ import annotations

import re
import unicodedata
from bisect import bisect_right
from dataclasses import dataclass

# [00:13:59] or [13:59]
BRACKETED = re.compile(r"\[(\d{1,2}):(\d{2})(?::(\d{2}))?\]")
# A whole line that is a speaker followed by a timestamp: "Joel Olivares 9:02"
TRAILING_LINE = re.compile(r"^\S.*?\s(\d{1,2}):(\d{2})(?::(\d{2}))?$")

ANCHOR = re.compile(
    r"^(?:"
    r"t:(?P<h>\d{1,2}):(?P<m>\d{2})(?::(?P<s>\d{2}))?"
    r"|s:(?P<section>.+)"
    r"|l:(?P<line>\d+)(?:-(?P<line_end>\d+))?"
    r")$"
)

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*$", re.MULTILINE)

# Characters that differ between a transcript and a hand-copied excerpt without
# any difference in meaning.
PUNCT_FOLD = {
    "\u2018": "'", "\u2019": "'", "\u201a": "'", "\u201b": "'",
    "\u201c": '"', "\u201d": '"', "\u201e": '"', "\u201f": '"',
    "\u2010": "-", "\u2011": "-", "\u2012": "-", "\u2013": "-",
    "\u2014": "-", "\u2015": "-", "\u2212": "-",
    "\u00a0": " ", "\u2007": " ", "\u202f": " ", "\u2009": " ",
    "\u2026": "...",
}


def fold(text: str) -> str:
    """Normalise for comparison: NFKC, fold punctuation, collapse whitespace."""
    text = unicodedata.normalize("NFKC", text)
    text = "".join(PUNCT_FOLD.get(ch, ch) for ch in text)
    return " ".join(text.split())


@dataclass
class Marker:
    seconds: int
    offset: int          # character offset in the folded body
    raw: str


@dataclass
class FoldedSource:
    """A source folded for comparison, with line structure retained.

    fold() collapses newlines along with all other whitespace, which is right
    for matching an excerpt that wraps across lines. But timestamp markers in
    the trailing convention ("Joel Olivares 9:02") are identified by being a
    whole line, so they cannot be found once newlines are gone.

    This keeps both: each line folded individually, the offset of each line
    within the joined body recorded, so a marker found on a line can be located
    in the folded body.
    """
    body: str                    # folded, newlines replaced by single spaces
    lines: list[str]             # folded, one per original line
    offsets: list[int]           # start offset of each line within body


def fold_source(raw: str) -> FoldedSource:
    lines = [fold(line) for line in raw.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    offsets, cursor = [], 0
    for line in lines:
        offsets.append(cursor)
        cursor += len(line) + 1          # +1 for the joining space
    return FoldedSource(" ".join(lines), lines, offsets)


def parse_anchor(anchor: str) -> dict | None:
    """Return a dict describing the anchor, or None if malformed."""
    m = ANCHOR.match(anchor)
    if not m:
        return None
    if m.group("h") is not None:
        h, mi, sec = m.group("h"), m.group("m"), m.group("s")
        if sec is None:                     # t:MM:SS
            return {"kind": "time", "seconds": int(h) * 60 + int(mi),
                    "precision": "ms"}
        return {"kind": "time",
                "seconds": int(h) * 3600 + int(mi) * 60 + int(sec),
                "precision": "hms"}
    if m.group("section") is not None:
        return {"kind": "section", "heading": m.group("section").strip()}
    return {
        "kind": "line",
        "start": int(m.group("line")),
        "end": int(m.group("line_end")) if m.group("line_end") else int(m.group("line")),
    }


def _seconds(a: str, b: str, c: str | None) -> int:
    return (int(a) * 3600 + int(b) * 60 + int(c)) if c else (int(a) * 60 + int(b))


def timestamp_markers(src: FoldedSource) -> list[Marker]:
    """Every timestamp in the source, with its offset in the folded body.

    Tries the bracketed convention first, then the trailing convention. A
    transcript uses one or the other, not both.
    """
    markers: list[Marker] = []

    for m in BRACKETED.finditer(src.body):
        markers.append(Marker(_seconds(m.group(1), m.group(2), m.group(3)),
                              m.start(), m.group(0)))
    if markers:
        markers.sort(key=lambda x: x.offset)
        return markers

    for index, line in enumerate(src.lines):
        m = TRAILING_LINE.match(line)
        if m:
            markers.append(Marker(_seconds(m.group(1), m.group(2), m.group(3)),
                                  src.offsets[index], line))
    markers.sort(key=lambda x: x.offset)
    return markers


def governing_marker(markers: list[Marker], offset: int) -> Marker | None:
    """The last timestamp at or before *offset* — whose block this text is in."""
    found = None
    for marker in markers:
        if marker.offset <= offset:
            found = marker
        else:
            break
    return found


def format_seconds(total: int) -> str:
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def check_evidence(
    body: str,
    anchor: str,
    excerpt: str,
    tolerance_seconds: int = 120,
    block_char_warning: int = 2500,
) -> tuple[bool, str, str]:
    """Verify one evidence item.

    Returns (ok, level, message). level is "error" or "warning"; message is
    empty when ok and there is nothing to note.
    """
    parsed = parse_anchor(anchor)
    if parsed is None:
        return False, "error", f"anchor {anchor!r} is not a recognised form"

    src = fold_source(body)
    folded_excerpt = fold(excerpt)

    if not folded_excerpt:
        return False, "error", "excerpt is empty"

    # --- line anchors -------------------------------------------------------
    if parsed["kind"] == "line":
        raw_lines = body.splitlines()
        if parsed["end"] > len(raw_lines):
            return False, "error", (
                f"anchor {anchor} points past the end of the source "
                f"({len(raw_lines)} lines)"
            )
        region = fold("\n".join(raw_lines[parsed["start"] - 1:parsed["end"]]))
        if folded_excerpt not in region:
            if folded_excerpt in src.body:
                return False, "error", (
                    "excerpt does not appear at this anchor, though it appears "
                    "elsewhere in the source"
                )
            return False, "error", "excerpt does not appear in the source"
        return True, "", ""

    # --- section anchors ----------------------------------------------------
    if parsed["kind"] == "section":
        wanted = fold(parsed["heading"]).lower()
        headings = [fold(m.group(2)).lower() for m in HEADING.finditer(body)]
        if not any(wanted == h or wanted in h for h in headings):
            return False, "error", f"no heading matching {parsed['heading']!r}"
        if folded_excerpt not in src.body:
            return False, "error", "excerpt does not appear in the source"
        return True, "", ""

    # --- timestamp anchors --------------------------------------------------
    position = src.body.find(folded_excerpt)
    if position == -1:
        return False, "error", (
            f"excerpt does not appear in the source: "
            f"{folded_excerpt[:60]!r}…"
        )

    occurrences = src.body.count(folded_excerpt)
    markers = timestamp_markers(src)
    if not markers:
        return True, "warning", (
            "source has no recognisable timestamps, so the anchor cannot be "
            "verified"
        )

    marker = governing_marker(markers, position)
    if marker is None:
        return False, "error", (
            f"excerpt appears before the first timestamp in the source, so "
            f"anchor {anchor} cannot be right"
        )

    drift = abs(marker.seconds - parsed["seconds"])
    if drift > tolerance_seconds:
        return False, "error", (
            f"anchor {anchor} does not match where the excerpt appears — it is "
            f"under {marker.raw.strip()} ({format_seconds(marker.seconds)}), "
            f"{format_seconds(drift)} away"
        )

    if occurrences > 1:
        return True, "warning", (
            "excerpt appears more than once in the source; the anchor cannot "
            "identify which occurrence"
        )

    # The anchor is correct but may point into a very long speaker block, in
    # which case it does not locate the quote in any useful sense.
    distance = position - marker.offset
    if distance > block_char_warning:
        # A long block usually means the source attributes many speakers to one
        # microphone, so there is no nearer timestamp to use. A line anchor is
        # the only way to be precise about such a source.
        # The folded body was built from the lines, so the offset of the
        # excerpt maps directly back to a line number. Searching for the text
        # would fail whenever a quote wraps across lines.
        index = bisect_right(src.offsets, position) - 1
        line_hint = f" Use l:{index + 1} instead." if index >= 0 else ""
        return True, "warning", (
            f"anchor {anchor} is correct but imprecise — the excerpt is "
            f"{distance:,} characters into that block, which has no nearer "
            f"timestamp.{line_hint}"
        )

    if drift > 0:
        return True, "warning", (
            f"anchor {anchor} is {drift}s from the timestamp governing this "
            f"excerpt ({marker.raw.strip()}); use the source's own timestamp"
        )

    return True, "", ""
