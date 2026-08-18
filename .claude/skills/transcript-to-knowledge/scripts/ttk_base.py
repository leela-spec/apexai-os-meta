#!/usr/bin/env python3
"""Standalone transcript-to-knowledge evidence pipeline.

The CLI is intentionally model-agnostic. It never calls an LLM or the network.
It prepares deterministic work packets, validates semantic results written by an
agent, builds a compact evidence ledger, routes only check-worthy factual claims
for optional verification, and compiles source-grounded Markdown wiki pages.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import statistics
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

RUN_SCHEMA = "ttk.run.v2"
TRANSCRIPT_SCHEMA = "ttk.transcript.v2"
WINDOW_SCHEMA = "ttk.windows.v2"
MAP_PACKET_SCHEMA = "ttk.map-packet.v2"
MAP_RESULT_SCHEMA = "ttk.map-result.v2"
EVIDENCE_SCHEMA = "ttk.evidence-ledger.v2"
REDUCE_PACKET_SCHEMA = "ttk.reduce-packet.v2"
REDUCE_RESULT_SCHEMA = "ttk.reduce-result.v2"
VERIFY_QUEUE_SCHEMA = "ttk.verify-queue.v2"
VERIFY_RESULT_SCHEMA = "ttk.verify-results.v2"
VALIDATION_SCHEMA = "ttk.validation.v2"
CONTRACT_VERSION = "ttk.semantic-contract.v2"

CLAIM_KINDS = {
    "fact", "opinion", "prediction", "recommendation", "decision", "anecdote",
    "definition", "mechanism", "estimate", "hypothesis",
}
CHECKWORTHINESS = {"high", "medium", "low", "none"}
SOURCE_SUPPORT = {"SUPPORTED", "PARTIAL", "AMBIGUOUS", "UNSUPPORTED"}
EXTERNAL_STATUS = {"CONFIRMED", "CONTRADICTED", "MIXED", "UNVERIFIED"}
EVIDENCE_STANCE = {"supports", "contradicts", "context"}

_TS = re.compile(r"^(?:(\d{1,3}):)?(\d{1,2}):(\d{2})(?:[,.](\d{1,3}))?$")
_CUE = re.compile(r"(\S+)\s+-->\s+(\S+)")
_BRACKET = re.compile(r"^\[(\d{1,3}:\d{2}(?::\d{2})?(?:[,.]\d{1,3})?)\]\s*(.+)$")
_SPEAKER = re.compile(r"^(?:\[([^\]]+)\]|([A-Za-z][^:]{0,60}):)\s*(.+)$")
_VOICE = re.compile(r"^<v(?:\.[^ >]+)?(?:\s+([^>]+))?>(.*)$", re.I)
_TOKEN = re.compile(r"[^\W_]+(?:['’-][^\W_]+)?", re.UNICODE)
_SAFE_SLUG = re.compile(r"[^a-z0-9]+")


class TTKError(ValueError):
    pass


@dataclass(frozen=True)
class Word:
    text: str
    start: float | None = None
    end: float | None = None
    probability: float | None = None


@dataclass(frozen=True)
class Segment:
    id: str
    text: str
    start: float | None
    end: float | None
    speaker: str | None
    words: tuple[Word, ...]
    source_pointer: str

    @property
    def word_count(self) -> int:
        return max(1, len(tokens(self.text)))


def clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def tokens(text: str) -> list[str]:
    return [m.group(0).casefold() for m in _TOKEN.finditer(text)]


def norm_text(text: str) -> str:
    return " ".join(tokens(text))


def stable_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def obj_hash(value: Any) -> str:
    return hashlib.sha256(stable_json(value).encode("utf-8")).hexdigest()


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise TTKError(f"missing file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise TTKError(f"invalid JSON in {path}: {exc}") from exc


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def parse_timestamp(value: str) -> float:
    m = _TS.match(value.strip().replace(",", "."))
    if not m:
        raise TTKError(f"invalid timestamp: {value!r}")
    h = int(m[1] or 0)
    minute = int(m[2])
    sec = int(m[3])
    ms = int((m[4] or "0").ljust(3, "0"))
    if minute >= 60 or sec >= 60:
        raise TTKError(f"invalid timestamp: {value!r}")
    return h * 3600 + minute * 60 + sec + ms / 1000


def fnum(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        out = float(value)
    except (TypeError, ValueError):
        out = parse_timestamp(str(value))
    if out < 0:
        raise TTKError(f"negative timestamp: {value!r}")
    return out


def format_timestamp(value: float | None) -> str | None:
    if value is None:
        return None
    ms = max(0, round(value * 1000))
    h, rem = divmod(ms, 3_600_000)
    minute, rem = divmod(rem, 60_000)
    sec, millis = divmod(rem, 1000)
    return f"{h:02d}:{minute:02d}:{sec:02d}.{millis:03d}"


def speaker_text(text: str) -> tuple[str | None, str]:
    voice = _VOICE.match(text)
    if voice:
        return clean(voice[1]) or None, clean(voice[2])
    match = _SPEAKER.match(text)
    if not match:
        return None, clean(text)
    candidate = clean(match[1] or match[2]).rstrip(":")
    if _TS.match(candidate.replace(",", ".")):
        return None, clean(text)
    return candidate or None, clean(match[3])


def make_segment(index: int, text: str, start: Any = None, end: Any = None,
                 speaker: Any = None, words: Iterable[Word] = (), pointer: str = "") -> Segment:
    text = clean(text)
    if not text:
        raise TTKError(f"empty segment at {pointer}")
    start_f, end_f = fnum(start), fnum(end)
    if start_f is not None and end_f is not None and end_f < start_f:
        raise TTKError(f"segment end before start at {pointer}")
    return Segment(
        id=f"seg-{index:06d}", text=text, start=start_f, end=end_f,
        speaker=clean(speaker) or None, words=tuple(words), source_pointer=pointer,
    )


def parse_word(value: Any) -> Word | None:
    if not isinstance(value, dict):
        return None
    text = clean(value.get("word", value.get("text")))
    if not text:
        return None
    prob = value.get("probability", value.get("score"))
    try:
        probability = float(prob) if prob is not None else None
    except (TypeError, ValueError):
        probability = None
    return Word(text=text, start=fnum(value.get("start")), end=fnum(value.get("end")), probability=probability)


def parse_json_transcript(path: Path) -> list[Segment]:
    raw = path.read_text(encoding="utf-8-sig")
    if path.suffix.lower() in {".jsonl", ".ndjson"}:
        data: Any = [json.loads(line) for line in raw.splitlines() if line.strip()]
    else:
        data = json.loads(raw)
    if isinstance(data, dict):
        if isinstance(data.get("segments"), list):
            rows = data["segments"]
        elif clean(data.get("text", data.get("transcript"))):
            rows = [data]
        else:
            raise TTKError("JSON transcript must contain a segments array or transcript text")
    elif isinstance(data, list):
        rows = data
    else:
        raise TTKError("JSON transcript root must be an object or list")
    out: list[Segment] = []
    for row_index, item in enumerate(rows, 1):
        if not isinstance(item, dict):
            continue
        text = clean(item.get("text", item.get("transcript")))
        if not text:
            continue
        words = [w for raw_word in (item.get("words") or []) if (w := parse_word(raw_word))]
        speaker = item.get("speaker", item.get("speaker_id", item.get("speaker_label")))
        out.append(make_segment(
            len(out) + 1, text, item.get("start"), item.get("end"), speaker,
            words, f"json:segments:{row_index}",
        ))
    if not out:
        raise TTKError("JSON transcript contains no non-empty segments")
    return out


def text_blocks(text: str) -> list[list[str]]:
    out: list[list[str]] = []
    cur: list[str] = []
    for line in text.replace("\r", "").split("\n"):
        if line.strip():
            cur.append(line.strip())
        elif cur:
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def parse_subtitles(path: Path) -> list[Segment]:
    out: list[Segment] = []
    for block_index, lines in enumerate(text_blocks(path.read_text(encoding="utf-8-sig")), 1):
        lines = [line for line in lines if not line.startswith("WEBVTT") and not line.startswith("NOTE")]
        cue_index = next((i for i, line in enumerate(lines) if _CUE.search(line)), None)
        if cue_index is None:
            continue
        cue = _CUE.search(lines[cue_index])
        assert cue is not None
        text = clean(" ".join(lines[cue_index + 1:]))
        if not text:
            continue
        speaker, text = speaker_text(text)
        out.append(make_segment(
            len(out) + 1, text, parse_timestamp(cue[1]), parse_timestamp(cue[2]),
            speaker, pointer=f"subtitle:block:{block_index}",
        ))
    if not out:
        raise TTKError("subtitle transcript contains no cues")
    return out


def parse_text_transcript(path: Path) -> list[Segment]:
    out: list[Segment] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        start: float | None = None
        text = line.strip()
        match = _BRACKET.match(text)
        if match:
            start = parse_timestamp(match[1])
            text = match[2]
        speaker, text = speaker_text(text)
        out.append(make_segment(len(out) + 1, text, start, None, speaker, pointer=f"line:{line_no}"))
    if not out:
        raise TTKError("text transcript is empty")
    return out


def load_transcript(path: Path) -> tuple[list[Segment], str]:
    suffix = path.suffix.lower()
    if suffix in {".json", ".jsonl", ".ndjson"}:
        return parse_json_transcript(path), "json"
    if suffix in {".srt", ".vtt"}:
        return parse_subtitles(path), suffix[1:]
    if suffix in {".txt", ".md", ".markdown"}:
        return parse_text_transcript(path), "text"
    raise TTKError(f"unsupported transcript format: {suffix or '<none>'}")


def timestamp_quality(segments: list[Segment]) -> str:
    if any(seg.words and any(w.start is not None or w.end is not None for w in seg.words) for seg in segments):
        return "word"
    timed = sum(seg.start is not None or seg.end is not None for seg in segments)
    if timed == len(segments):
        return "segment"
    if timed:
        return "partial_segment"
    return "none"


def segment_dict(seg: Segment) -> dict[str, Any]:
    value = asdict(seg)
    value["start_hms"] = format_timestamp(seg.start)
    value["end_hms"] = format_timestamp(seg.end)
    value["word_count"] = seg.word_count
    value["words"] = [
        {**asdict(word), "start_hms": format_timestamp(word.start), "end_hms": format_timestamp(word.end)}
        for word in seg.words
    ]
    return value



__all__ = [name for name in globals() if not name.startswith("__")]
