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
from dataclasses import dataclass

# [00:13:59] or [13:59]
BRACKETED = re.compile(r"\[(\d{1,2}):(\d{2})(?::(\d{2}))?\]")
# "Joel Olivares 9:02" at the end of a line
TRAILING = re.compile(r"^\s*\S.*?\s(\d{1,2}):(\d{2})(?::(\d{2}))?\s*$", re.MULTILINE)

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


def parse_anchor(anchor: str) -> dict | None:
    """Return a dict describing the anchor, or None if malformed."""
    m = ANCHOR.match(anchor)
    if not m:
        return None
    if m.group("h") is not None:
        h, mi, s = m.group("h"), m.group("m"), m.group("s")
        if s is None:                       # t:MM:SS
            seconds = int(h) * 60 + int(mi)
            precision = "ms"
        else:                               # t:HH:MM:SS
            seconds = int(h) * 3600 + int(mi) * 60 + int(s)
            precision = "hms"
        return {"kind": "time", "seconds": seconds, "precision": precision}
    if m.group("section") is not None:
        return {"kind": "section", "heading": m.group("section").strip()}
    return {
        "kind": "line",
        "start": int(m.group("line")),
        "end": int(m.group("line_end")) if m.group("line_end") else int(m.group("line")),
    }


def timestamp_markers(body: str) -> list[Marker]:
    """Every timestamp in the body, with its character offset, in order."""
    markers: list[Marker] = []

    for m in BRACKETED.finditer(body):
        a, b, c = m.group(1), m.group(2), m.group(3)
        seconds = (int(a) * 3600 + int(b) * 60 + int(c)) if c \
            else (int(a) * 60 + int(b))
        markers.append(Marker(seconds, m.start(), m.group(0)))

    if not markers:
        for m in TRAILING.finditer(body):
            a, b, c = m.group(1), m.group(2), m.group(3)
            seconds = (int(a) * 3600 + int(b) * 60 + int(c)) if c \
                else (int(a) * 60 + int(b))
            markers.append(Marker(seconds, m.start(), m.group(0).strip()))

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
    body: str, anchor: str, excerpt: str, tolerance_seconds: int = 120
) -> tuple[bool, str, str]:
    """Verify one evidence item.

    Returns (ok, level, message). level is "error" or "warning"; message is
    empty when ok and there is nothing to note.
    """
    parsed = parse_anchor(anchor)
    if parsed is None:
        return False, "error", f"anchor {anchor!r} is not a recognised form"

    folded_body = fold(body)
    folded_excerpt = fold(excerpt)

    if not folded_excerpt:
        return False, "error", "excerpt is empty"

    # --- line anchors: check the range exists, then the excerpt within it ----
    if parsed["kind"] == "line":
        lines = body.splitlines()
        if parsed["end"] > len(lines):
            return False, "error", (
                f"anchor {anchor} points past the end of the source "
                f"({len(lines)} lines)"
            )
        region = fold("\n".join(lines[parsed["start"] - 1:parsed["end"]]))
        if folded_excerpt not in region:
            if folded_excerpt in folded_body:
                return False, "error", (
                    f"excerpt does not appear at {anchor}, though it appears "
                    f"elsewhere in the source"
                )
            return False, "error", "excerpt does not appear in the source"
        return True, "", ""

    # --- section anchors ----------------------------------------------------
    if parsed["kind"] == "section":
        wanted = fold(parsed["heading"]).lower()
        headings = [(m.start(), fold(m.group(2)).lower()) for m in HEADING.finditer(body)]
        if not any(wanted == h or wanted in h for _, h in headings):
            return False, "error", f"no heading matching {parsed['heading']!r}"
        if folded_excerpt not in folded_body:
            return False, "error", "excerpt does not appear in the source"
        return True, "", ""

    # --- timestamp anchors --------------------------------------------------
    position = folded_body.find(folded_excerpt)
    if position == -1:
        head = folded_excerpt[:60]
        return False, "error", (
            f"excerpt does not appear in the source: {head!r}…"
        )

    if folded_body.count(folded_excerpt) > 1:
        return True, "warning", (
            f"excerpt appears more than once in the source; the anchor cannot "
            f"identify which occurrence"
        )

    markers = timestamp_markers(folded_body)
    if not markers:
        return True, "warning", (
            "source has no timestamps, so the anchor cannot be verified"
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
            f"under {marker.raw} ({format_seconds(marker.seconds)}), "
            f"{format_seconds(drift)} away"
        )
    if drift > 0:
        return True, "warning", (
            f"anchor {anchor} is {drift}s from the timestamp governing this "
            f"excerpt ({marker.raw}); use the source's own timestamp"
        )

    return True, "", ""
