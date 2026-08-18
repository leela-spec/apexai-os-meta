#!/usr/bin/env python3
"""Deterministically normalize and chunk timestamped transcripts."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

CONTRACT_VERSION = "apex.transcript.v1"
_TS = re.compile(r"^(?:(\d{1,3}):)?(\d{1,2}):(\d{2})(?:[,.](\d{1,3}))?$")
_CUE = re.compile(r"(\S+)\s+-->\s+(\S+)")
_BRACKET = re.compile(r"^\[(\d{1,3}:\d{2}(?::\d{2})?(?:[,.]\d{1,3})?)\]\s*(.+)$")
_SPEAKER = re.compile(r"^(?:\[([^\]]+)\]|([A-Za-z][^:]{0,60}):)\s*(.+)$")
_VOICE = re.compile(r"^<v(?:\.[^ >]+)?(?:\s+([^>]+))?>(.*)$", re.I)

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
    def word_count(self): return len(self.text.split())

class TranscriptError(ValueError): pass

def clean(v: Any) -> str: return re.sub(r"\s+", " ", str(v or "")).strip()
def sha256(p: Path) -> str: return hashlib.sha256(p.read_bytes()).hexdigest()

def parse_timestamp(v: str) -> float:
    m = _TS.match(v.strip().replace(",", "."))
    if not m: raise TranscriptError(f"invalid timestamp: {v!r}")
    h, minute, sec, ms = int(m[1] or 0), int(m[2]), int(m[3]), int((m[4] or "0").ljust(3, "0"))
    if minute >= 60 or sec >= 60: raise TranscriptError(f"invalid timestamp: {v!r}")
    return h * 3600 + minute * 60 + sec + ms / 1000

def fnum(v: Any) -> float | None:
    if v is None or v == "": return None
    try: out = float(v)
    except (TypeError, ValueError): out = parse_timestamp(str(v))
    if out < 0: raise TranscriptError(f"negative timestamp: {v!r}")
    return out

def format_timestamp(v: float | None) -> str | None:
    if v is None: return None
    ms = max(0, round(v * 1000)); h, r = divmod(ms, 3600000); m, r = divmod(r, 60000); s, x = divmod(r, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{x:03d}"

def speaker_text(text: str) -> tuple[str | None, str]:
    v = _VOICE.match(text)
    if v: return clean(v[1]) or None, clean(v[2])
    m = _SPEAKER.match(text)
    if not m: return None, clean(text)
    candidate = clean(m[1] or m[2]).rstrip(":")
    if _TS.match(candidate.replace(",", ".")): return None, clean(text)
    return candidate or None, clean(m[3])

def segment(i: int, text: str, start=None, end=None, speaker=None, words=(), pointer="") -> Segment:
    text = clean(text)
    if not text: raise TranscriptError(f"empty segment at {pointer}")
    if start is not None and end is not None and end < start: raise TranscriptError(f"segment end before start at {pointer}")
    return Segment(f"seg-{i:06d}", text, start, end, clean(speaker) or None, tuple(words), pointer)

def word_json(x: Any) -> Word | None:
    if not isinstance(x, dict) or not clean(x.get("word", x.get("text"))): return None
    p = x.get("probability", x.get("score"))
    try: p = float(p) if p is not None else None
    except (TypeError, ValueError): p = None
    return Word(clean(x.get("word", x.get("text"))), fnum(x.get("start")), fnum(x.get("end")), p)

def parse_json(path: Path) -> list[Segment]:
    raw = path.read_text(encoding="utf-8-sig")
    data = [json.loads(x) for x in raw.splitlines() if x.strip()] if path.suffix.lower() == ".jsonl" else json.loads(raw)
    rows = data.get("segments", [data] if isinstance(data, dict) else data) if isinstance(data, (dict, list)) else None
    if not isinstance(rows, list): raise TranscriptError("JSON transcript must contain segments or text")
    out = []
    for n, x in enumerate(rows, 1):
        if not isinstance(x, dict) or not clean(x.get("text", x.get("transcript"))): continue
        words = tuple(w for r in (x.get("words") or []) if (w := word_json(r)))
        sp = x.get("speaker", x.get("speaker_id", x.get("speaker_label")))
        out.append(segment(len(out)+1, x.get("text", x.get("transcript")), fnum(x.get("start")), fnum(x.get("end")), sp, words, f"json:segments:{n}"))
    if not out: raise TranscriptError("JSON transcript contains no non-empty segments")
    return out

def blocks(text: str) -> list[list[str]]:
    out, cur = [], []
    for line in text.replace("\r", "").split("\n"):
        if line.strip(): cur.append(line.strip())
        elif cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out

def parse_subtitles(path: Path) -> list[Segment]:
    out = []
    for b, lines in enumerate(blocks(path.read_text(encoding="utf-8-sig")), 1):
        lines = [x for x in lines if not x.startswith("WEBVTT") and not x.startswith("NOTE")]
        cue_i = next((i for i, x in enumerate(lines) if _CUE.search(x)), None)
        if cue_i is None: continue
        m = _CUE.search(lines[cue_i]); text = clean(" ".join(lines[cue_i+1:]));
        if not text: continue
        sp, text = speaker_text(text)
        out.append(segment(len(out)+1, text, parse_timestamp(m[1]), parse_timestamp(m[2]), sp, pointer=f"subtitle:block:{b}"))
    if not out: raise TranscriptError("subtitle transcript contains no cues")
    return out

def parse_text(path: Path) -> list[Segment]:
    out = []
    for n, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip(): continue
        start = None; text = line.strip(); m = _BRACKET.match(text)
        if m: start, text = parse_timestamp(m[1]), m[2]
        sp, text = speaker_text(text)
        out.append(segment(len(out)+1, text, start, None, sp, pointer=f"line:{n}"))
    if not out: raise TranscriptError("text transcript is empty")
    return out

def load_transcript(path: Path) -> tuple[list[Segment], str]:
    s = path.suffix.lower()
    if s in {".json", ".jsonl", ".ndjson"}: return parse_json(path), "json"
    if s in {".srt", ".vtt"}: return parse_subtitles(path), s[1:]
    if s in {".txt", ".md", ".markdown"}: return parse_text(path), "text"
    raise TranscriptError(f"unsupported transcript format: {s or '<none>'}")

def timestamp_quality(segs: list[Segment]) -> str:
    if any(s.words and any(w.start is not None or w.end is not None for w in s.words) for s in segs): return "word"
    timed = sum(s.start is not None or s.end is not None for s in segs)
    return "segment" if timed == len(segs) else "partial_segment" if timed else "none"

def build_chunks(segs: list[Segment], chunk_words=1200, overlap_words=120) -> list[dict[str, Any]]:
    if chunk_words <= 0 or overlap_words < 0 or overlap_words >= chunk_words: raise TranscriptError("require 0 <= overlap_words < chunk_words")
    if not segs: return []
    chunks, start = [], 0
    while start < len(segs):
        total, end = 0, start
        while end < len(segs) and (total < chunk_words or end == start): total += max(1, segs[end].word_count); end += 1
        chosen = segs[start:end]
        chunks.append({"id": f"chunk-{len(chunks)+1:04d}", "start_segment": chosen[0].id, "end_segment": chosen[-1].id,
                       "segment_ids": [s.id for s in chosen], "word_count": sum(s.word_count for s in chosen),
                       "start": chosen[0].start, "end": chosen[-1].end,
                       "start_hms": format_timestamp(chosen[0].start), "end_hms": format_timestamp(chosen[-1].end)})
        if end >= len(segs): break
        overlap, next_start = 0, end
        while next_start > start and overlap < overlap_words: next_start -= 1; overlap += max(1, segs[next_start].word_count)
        start = max(start + 1, next_start)
    return chunks

def seg_dict(s: Segment) -> dict[str, Any]:
    d = asdict(s); d["start_hms"] = format_timestamp(s.start); d["end_hms"] = format_timestamp(s.end)
    d["words"] = [{**asdict(w), "start_hms": format_timestamp(w.start), "end_hms": format_timestamp(w.end)} for w in s.words]
    return d

def markdown(segs: list[Segment], source_hash: str) -> str:
    lines = ["# Normalized Transcript", "", f"Source SHA-256: `{source_hash}`", ""]
    for s in segs:
        timing = f"{format_timestamp(s.start)} -> {format_timestamp(s.end)}" if s.start is not None else "timing unavailable"
        who = f" · {s.speaker}" if s.speaker else ""
        lines += [f"<a id=\"{s.id}\"></a>", f"**[{s.id}] {timing}{who}**", "", s.text, ""]
    return "\n".join(lines)

def task_plan(chunks: list[dict[str, Any]]) -> dict[str, Any]:
    return {"schema": "apex.transcript.task-plan.v1", "order": ["meso_map", "micro_claims", "macro_reduce", "external_verification"],
            "tasks": {"meso_map": [{"chunk_id": c["id"], "source": f"chunks/{c['id']}.md"} for c in chunks],
                      "micro_claims": [{"chunk_id": c["id"], "source": f"chunks/{c['id']}.md", "default_status": "[UNVERIFIED]"} for c in chunks],
                      "macro_reduce": {"inputs": "validated meso outputs", "raw_source_reopen": "only for gaps/contradictions/quote checks"},
                      "external_verification": {"inputs": "testable micro claims only", "allowed": ["[CONFIRMED]", "[CONTRADICTED]", "[MIXED]", "[UNVERIFIED]", "[OPINION]"]}}}

def prepare(input_path: Path, output_dir: Path, chunk_words=1200, overlap_words=120) -> dict[str, Any]:
    input_path = input_path.resolve(); output_dir.mkdir(parents=True, exist_ok=True); (output_dir / "chunks").mkdir(exist_ok=True)
    segs, fmt = load_transcript(input_path); source_hash = sha256(input_path); chunks = build_chunks(segs, chunk_words, overlap_words)
    (output_dir/"transcript.json").write_text(json.dumps({"schema": CONTRACT_VERSION, "source_sha256": source_hash, "segments": [seg_dict(s) for s in segs]}, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    (output_dir/"transcript.md").write_text(markdown(segs, source_hash), encoding="utf-8")
    (output_dir/"chunk-index.json").write_text(json.dumps({"schema": "apex.transcript.chunk-index.v1", "chunks": chunks}, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    by_id = {s.id: s for s in segs}
    for c in chunks:
        body = [f"# {c['id']}", "", f"Source SHA-256: `{source_hash}`", ""]
        for sid in c["segment_ids"]:
            s = by_id[sid]; body += [f"**[{sid}] {format_timestamp(s.start) or 'timing unavailable'}{(' · '+s.speaker) if s.speaker else ''}**", "", s.text, ""]
        (output_dir/"chunks"/f"{c['id']}.md").write_text("\n".join(body), encoding="utf-8")
    (output_dir/"task-plan.json").write_text(json.dumps(task_plan(chunks), indent=2, sort_keys=True)+"\n", encoding="utf-8")
    manifest = {"schema": "apex.transcript.manifest.v1", "source": {"name": input_path.name, "sha256": source_hash, "format": fmt}, "normalizer": CONTRACT_VERSION,
                "segment_count": len(segs), "word_count": sum(s.word_count for s in segs), "speaker_labels": sorted({s.speaker for s in segs if s.speaker}),
                "timestamp_quality": timestamp_quality(segs), "chunking": {"chunk_words": chunk_words, "overlap_words": overlap_words, "chunk_count": len(chunks)},
                "artifacts": {"transcript_markdown":"transcript.md", "transcript_json":"transcript.json", "chunk_index":"chunk-index.json", "task_plan":"task-plan.json", "chunks_dir":"chunks/"},
                "semantic_boundary": {"deterministic":["source hashing","format parsing","anchor preservation","chunk planning"], "semantic":["macro synthesis","meso themes","micro claim extraction","external verification"]}}
    (output_dir/"manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    return manifest

def main(argv=None) -> int:
    p = argparse.ArgumentParser(); sp = p.add_subparsers(dest="command", required=True); q = sp.add_parser("prepare")
    q.add_argument("input", type=Path); q.add_argument("--output", type=Path, required=True); q.add_argument("--chunk-words", type=int, default=1200); q.add_argument("--overlap-words", type=int, default=120)
    a = p.parse_args(argv)
    try: print(json.dumps(prepare(a.input, a.output, a.chunk_words, a.overlap_words), indent=2, sort_keys=True)); return 0
    except (OSError, json.JSONDecodeError, TranscriptError) as e: print(f"error: {e}", file=sys.stderr); return 2
if __name__ == "__main__": raise SystemExit(main())
