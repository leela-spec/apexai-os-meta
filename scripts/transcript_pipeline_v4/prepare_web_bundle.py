"""Create a deterministic, manifest-backed bundle for long transcript processing."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "1.0"
DEFAULT_MAX_UTF8_BYTES = 200_000
DEFAULT_MAX_CUES = 1_000
DEFAULT_MAX_DURATION_SECONDS = 1_800
SRT_TIMESTAMP = re.compile(
    r"^(?P<sh>\d{2,}):(?P<sm>\d{2}):(?P<ss>\d{2}),(?P<sms>\d{3})"
    r"\s+-->\s+"
    r"(?P<eh>\d{2,}):(?P<em>\d{2}):(?P<es>\d{2}),(?P<ems>\d{3})$"
)


@dataclass(frozen=True)
class Unit:
    ordinal: int
    raw: str
    text: str
    start_ms: int | None = None
    end_ms: int | None = None
    source_counter: int | None = None
    asr: dict[str, float] | None = None

    @property
    def byte_count(self) -> int:
        return len(self.raw.encode("utf-8"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def reason(code: str, affected_range: str, evidence: str, remediation: str) -> dict[str, object]:
    return {
        "code": code,
        "affected_ranges": [affected_range],
        "evidence": evidence,
        "remediation": remediation,
    }


def timestamp_ms(match: re.Match[str], prefix: str) -> int:
    return (
        int(match[f"{prefix}h"]) * 3_600_000
        + int(match[f"{prefix}m"]) * 60_000
        + int(match[f"{prefix}s"]) * 1_000
        + int(match[f"{prefix}ms"])
    )


def parse_srt(text: str) -> tuple[list[Unit], list[dict[str, object]]]:
    tokens = re.split(r"(\r?\n[ \t]*\r?\n)", text) if text else []
    blocks: list[tuple[str, str]] = []
    for index in range(0, len(tokens), 2):
        content = tokens[index]
        separator = tokens[index + 1] if index + 1 < len(tokens) else ""
        if content or separator:
            blocks.append((content, content + separator))
    units: list[Unit] = []
    reasons: list[dict[str, object]] = []
    previous_start = -1
    seen_counters: set[int] = set()

    for block_ordinal, (content, raw_block) in enumerate(blocks, start=1):
        lines = content.rstrip("\r\n").splitlines()
        affected = f"cue-block {block_ordinal}"
        if len(lines) < 3 or not lines[0].strip().isdigit():
            reasons.append(reason("PARSE_FAILED", affected, "Cue block lacks a numeric counter or text.", "Repair or regenerate the SRT cue block."))
            continue
        counter = int(lines[0].strip())
        if counter in seen_counters:
            reasons.append(reason("PARSE_FAILED", f"cue {counter}", f"Duplicate SRT cue counter: {counter}", "Renumber cues so every source counter is unique."))
            continue
        seen_counters.add(counter)
        match = SRT_TIMESTAMP.fullmatch(lines[1].strip())
        if not match:
            reasons.append(reason("PARSE_FAILED", f"cue {counter}", f"Unparseable SRT timestamp line: {lines[1].strip()!r}", "Repair or regenerate the timestamp line."))
            continue
        start_ms = timestamp_ms(match, "s")
        end_ms = timestamp_ms(match, "e")
        invalid = end_ms <= start_ms or start_ms < previous_start
        if invalid:
            reasons.append(reason("INVALID_TIMESTAMPS", f"cue {counter}", f"start_ms={start_ms}, end_ms={end_ms}, previous_start_ms={previous_start}", "Repair or regenerate the affected cue timestamps."))
            continue
        previous_start = start_ms
        units.append(
            Unit(
                ordinal=len(units) + 1,
                raw=raw_block,
                text="\n".join(lines[2:]),
                start_ms=start_ms,
                end_ms=end_ms,
                source_counter=counter,
            )
        )
    return units, reasons


def parse_text(text: str) -> tuple[list[Unit], list[dict[str, object]]]:
    if not text:
        return [], [reason("SOURCE_UNREADABLE", "entire source", "The text source is empty.", "Provide a non-empty UTF-8 transcript.")]
    lines = text.splitlines(keepends=True)
    if lines and not lines[-1].endswith(("\n", "\r")):
        pass
    units = [Unit(ordinal=index, raw=line, text=line.rstrip("\r\n")) for index, line in enumerate(lines, start=1)]
    return units, []


def numeric(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def parse_whisper_json(text: str) -> tuple[list[Unit], list[dict[str, object]]]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        return [], [reason("PARSE_FAILED", f"line {exc.lineno}", str(exc), "Provide valid Whisper segment JSON.")]
    segments = payload.get("segments") if isinstance(payload, dict) else None
    if not isinstance(segments, list):
        return [], [reason("PARSE_FAILED", "entire source", "Expected a top-level 'segments' array.", "Export Whisper segment JSON or provide SRT/TXT instead.")]

    units: list[Unit] = []
    reasons: list[dict[str, object]] = []
    previous_start = -1
    for index, segment in enumerate(segments, start=1):
        affected = f"segment {index}"
        if not isinstance(segment, dict):
            reasons.append(reason("PARSE_FAILED", affected, "Segment is not an object.", "Regenerate the segment JSON."))
            continue
        start = numeric(segment.get("start"))
        end = numeric(segment.get("end"))
        segment_text = segment.get("text")
        if start is None or end is None or not isinstance(segment_text, str):
            reasons.append(reason("PARSE_FAILED", affected, "Segment requires numeric start/end and string text.", "Regenerate the segment JSON."))
            continue
        start_ms = round(start * 1_000)
        end_ms = round(end * 1_000)
        if end_ms <= start_ms or start_ms < previous_start:
            reasons.append(reason("INVALID_TIMESTAMPS", affected, f"start_ms={start_ms}, end_ms={end_ms}, previous_start_ms={previous_start}", "Repair or regenerate the affected segment timestamps."))
            continue
        previous_start = start_ms
        metrics: dict[str, float] = {}
        for field in ("avg_logprob", "compression_ratio", "no_speech_prob", "temperature"):
            value = numeric(segment.get(field))
            if value is not None:
                metrics[field] = value
        raw = segment_text
        units.append(Unit(index, raw, segment_text.strip(), start_ms, end_ms, index, metrics or None))
    return units, reasons


def load_asr_metadata(path: Path | None) -> dict[int, dict[str, float]]:
    if path is None:
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    segments = payload.get("segments") if isinstance(payload, dict) else None
    if not isinstance(segments, list):
        raise ValueError("ASR metadata must contain a top-level 'segments' array.")
    by_ordinal: dict[int, dict[str, float]] = {}
    for fallback, segment in enumerate(segments, start=1):
        if not isinstance(segment, dict):
            continue
        ordinal_value = segment.get("ordinal", fallback)
        if not isinstance(ordinal_value, int):
            continue
        metrics: dict[str, float] = {}
        for field in ("avg_logprob", "compression_ratio", "no_speech_prob", "temperature"):
            value = numeric(segment.get(field))
            if value is not None:
                metrics[field] = value
        if metrics:
            by_ordinal[ordinal_value] = metrics
    return by_ordinal


def apply_asr_metadata(units: list[Unit], by_ordinal: dict[int, dict[str, float]]) -> list[Unit]:
    if not by_ordinal:
        return units
    return [
        Unit(unit.ordinal, unit.raw, unit.text, unit.start_ms, unit.end_ms, unit.source_counter, by_ordinal.get(unit.ordinal, unit.asr))
        for unit in units
    ]


def split_units(units: list[Unit], max_bytes: int, max_cues: int, max_duration_ms: int) -> list[list[Unit]]:
    parts: list[list[Unit]] = []
    current: list[Unit] = []
    current_bytes = 0

    for unit in units:
        proposed_duration = 0
        if current and current[0].start_ms is not None and unit.end_ms is not None:
            proposed_duration = unit.end_ms - current[0].start_ms
        exceeds = bool(current) and (
            len(current) + 1 > max_cues
            or current_bytes + unit.byte_count > max_bytes
            or proposed_duration > max_duration_ms
        )
        if exceeds:
            parts.append(current)
            current = []
            current_bytes = 0
        current.append(unit)
        current_bytes += unit.byte_count
    if current:
        parts.append(current)
    return parts


def unit_record(source_id: str, unit: Unit) -> dict[str, object]:
    record: dict[str, object] = {
        "unit_id": f"{source_id}:unit-{unit.ordinal:08d}",
        "ordinal": unit.ordinal,
        "raw": unit.raw,
        "text": unit.text,
        "text_sha256": sha256_bytes(unit.text.encode("utf-8")),
    }
    if unit.source_counter is not None:
        record["source_counter"] = unit.source_counter
    if unit.start_ms is not None and unit.end_ms is not None:
        record["start_ms"] = unit.start_ms
        record["end_ms"] = unit.end_ms
    if unit.asr:
        record["asr"] = unit.asr
    return record


def build_bundle(args: argparse.Namespace) -> int:
    source: Path = args.input.resolve()
    output: Path = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    parts_dir = output / "parts"
    parts_dir.mkdir(parents=True, exist_ok=True)
    for stale in parts_dir.glob("part-*.json"):
        stale.unlink()

    raw = source.read_bytes()
    source_hash = sha256_bytes(raw)
    source_id = f"src-{source_hash[:16]}"
    reasons: list[dict[str, object]] = []
    warnings: list[dict[str, object]] = []

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        text = ""
        reasons.append(reason("SOURCE_UNREADABLE", f"bytes {exc.start}-{exc.end}", str(exc), "Convert the source losslessly to UTF-8 and retry."))

    extension = source.suffix.lower()
    units: list[Unit] = []
    parser_name = "unknown"
    if not reasons:
        if extension == ".srt":
            parser_name = "srt-strict-v1"
            units, parse_reasons = parse_srt(text)
        elif extension in {".txt", ".md"}:
            parser_name = "text-lines-v1"
            units, parse_reasons = parse_text(text)
        elif extension == ".json":
            parser_name = "whisper-segments-v1"
            units, parse_reasons = parse_whisper_json(text)
        else:
            parse_reasons = [reason("PARSE_FAILED", "entire source", f"Unsupported extension: {extension or '<none>'}", "Provide SRT, TXT, MD, or Whisper segment JSON.")]
        reasons.extend(parse_reasons)

    if args.asr_json and not reasons:
        try:
            units = apply_asr_metadata(units, load_asr_metadata(args.asr_json.resolve()))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            reasons.append(reason("PARSE_FAILED", "ASR metadata", str(exc), "Repair or omit the optional ASR metadata file."))

    if not units and not reasons:
        reasons.append(reason("SOURCE_UNREADABLE", "entire source", "No source units were parsed.", "Provide a non-empty supported transcript."))

    has_asr = any(unit.asr for unit in units)
    risky_units = [
        unit.ordinal
        for unit in units
        if unit.asr
        and (
            unit.asr.get("compression_ratio", float("-inf")) > 2.4
            or unit.asr.get("avg_logprob", float("inf")) < -1.0
        )
    ]
    if risky_units:
        warnings.append({
            "code": "ASR_RISKY_SEGMENTS",
            "affected_ranges": [f"units {','.join(map(str, risky_units))}"],
            "evidence": "Whisper decoder fallback thresholds were exceeded.",
            "remediation": "Review these segments before using them as evidence for central claims.",
        })
    if units and not has_asr:
        warnings.append({
            "code": "ASR_METADATA_MISSING",
            "affected_ranges": ["entire source"],
            "evidence": "No original Whisper decoder metadata is present.",
            "remediation": "Continue with structural checks only, or provide transcript.segments.json.",
        })

    copied_source = output / "source" / f"original{extension or '.txt'}"
    copied_source.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, copied_source)

    part_entries: list[dict[str, object]] = []
    if not reasons:
        parts = split_units(units, args.max_utf8_bytes, args.max_cues, args.max_duration_seconds * 1_000)
        for part_ordinal, part_units in enumerate(parts, start=1):
            payload = {
                "schema_version": SCHEMA_VERSION,
                "source_id": source_id,
                "source_sha256": source_hash,
                "part_ordinal": part_ordinal,
                "range": {
                    "first_unit": part_units[0].ordinal,
                    "last_unit": part_units[-1].ordinal,
                    "start_ms": part_units[0].start_ms,
                    "end_ms": part_units[-1].end_ms,
                },
                "units": [unit_record(source_id, unit) for unit in part_units],
            }
            part_hash = sha256_bytes(canonical_json_bytes(payload))
            part_id = f"part-{part_ordinal:04d}-{part_hash[:12]}"
            payload["part_id"] = part_id
            relative_path = f"parts/part-{part_ordinal:04d}.json"
            write_json(output / relative_path, payload)
            part_entries.append({
                "ordinal": part_ordinal,
                "part_id": part_id,
                "path": relative_path,
                "sha256": sha256_bytes((output / relative_path).read_bytes()),
                "first_unit": part_units[0].ordinal,
                "last_unit": part_units[-1].ordinal,
                "start_ms": part_units[0].start_ms,
                "end_ms": part_units[-1].end_ms,
                "unit_count": len(part_units),
                "utf8_text_bytes": sum(unit.byte_count for unit in part_units),
            })

    status = "NEEDS_PREPROCESSING" if reasons else ("PASS_WITH_WARNINGS" if warnings else "PASS")
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "bundle_type": "deterministic-transcript-parts",
        "source": {
            "source_id": source_id,
            "filename": source.name,
            "format": extension.lstrip(".") or "text",
            "encoding": "UTF-8" if not any(item["code"] == "SOURCE_UNREADABLE" for item in reasons) else "unreadable",
            "sha256": source_hash,
            "byte_count": len(raw),
            "unit_count": len(units),
            "start_ms": units[0].start_ms if units else None,
            "end_ms": units[-1].end_ms if units else None,
            "copied_path": copied_source.relative_to(output).as_posix(),
        },
        "parser": {"name": parser_name, "version": SCHEMA_VERSION, "text_normalization": "none"},
        "preflight": {
            "status": status,
            "accuracy_assessed": "asr_proxy_only" if has_asr else False,
            "reasons": reasons,
            "warnings": warnings,
        },
        "chunking": {
            "algorithm": "source-unit-greedy-v1",
            "max_utf8_bytes": args.max_utf8_bytes,
            "max_cues": args.max_cues,
            "max_duration_seconds": args.max_duration_seconds,
            "overlap_units": 0,
        },
        "parts": part_entries,
        "integrity": {
            "parts_count": len(part_entries),
            "units_across_parts": sum(entry["unit_count"] for entry in part_entries),
            "source_units": len(units),
            "coverage_status": "blocked" if reasons else "complete",
        },
    }
    write_json(output / "manifest.json", manifest)
    print(output / "manifest.json")
    return 2 if reasons else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="SRT, TXT, MD, or Whisper segment JSON source.")
    parser.add_argument("--output", required=True, type=Path, help="Destination bundle directory.")
    parser.add_argument("--asr-json", type=Path, help="Optional Whisper segment metadata for an SRT/TXT source.")
    parser.add_argument("--max-utf8-bytes", type=int, default=DEFAULT_MAX_UTF8_BYTES)
    parser.add_argument("--max-cues", type=int, default=DEFAULT_MAX_CUES)
    parser.add_argument("--max-duration-seconds", type=int, default=DEFAULT_MAX_DURATION_SECONDS)
    args = parser.parse_args()
    for field in ("max_utf8_bytes", "max_cues", "max_duration_seconds"):
        if getattr(args, field) <= 0:
            parser.error(f"--{field.replace('_', '-')} must be greater than zero")
    return args


def main() -> None:
    try:
        raise SystemExit(build_bundle(parse_args()))
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
