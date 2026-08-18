#!/usr/bin/env python3
"""Content-bound Map packet construction and run initialization."""
from ttk_windows import *
def _packet_payload(packet: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in packet.items() if k != "packet_sha256"}


def _attach_packet_hash(packet: dict[str, Any]) -> dict[str, Any]:
    out = dict(packet)
    out["packet_sha256"] = obj_hash(_packet_payload(out))
    return out


def _packet_hash_valid(packet: dict[str, Any]) -> bool:
    return packet.get("packet_sha256") == obj_hash(_packet_payload(packet))


def build_map_packet(window: dict[str, Any], segment_lookup: dict[str, dict[str, Any]], source_sha: str) -> dict[str, Any]:
    packet_segments = []
    core = set(window["core_segment_ids"])
    for sid in window["packet_segment_ids"]:
        seg = segment_lookup[sid]
        packet_segments.append({
            "id": sid,
            "role": "core" if sid in core else "context_only",
            "start_hms": seg.get("start_hms"),
            "end_hms": seg.get("end_hms"),
            "speaker": seg.get("speaker"),
            "text": seg["text"],
        })
    return _attach_packet_hash({
        "schema": MAP_PACKET_SCHEMA,
        "contract_version": CONTRACT_VERSION,
        "packet_id": f"map-{window['id']}",
        "window_id": window["id"],
        "source_sha256": source_sha,
        "core_segment_ids": window["core_segment_ids"],
        "context_only_segment_ids": window["context_before_segment_ids"] + window["context_after_segment_ids"],
        "source_segments": packet_segments,
        "result_path": f"work/results/map/{window['id']}.json",
        "rules": [
            "Extract evidence only from core segments; context_only segments are orientation only.",
            "Every candidate claim requires at least one verbatim quote from its cited core segment.",
            "Do not force content into categories; empty arrays are valid.",
            "Separate factual assertions from opinion, prediction, recommendation, decision, anecdote, definition, mechanism, estimate, and hypothesis.",
            "Preserve disagreement and uncertainty rather than reconciling it.",
        ],
    })


def _existing_run_ok(output_dir: Path, source_sha: str, config: dict[str, Any]) -> bool:
    manifest_path = output_dir / "manifest.json"
    if not manifest_path.exists():
        return False
    manifest = read_json(manifest_path)
    return manifest.get("schema") == RUN_SCHEMA and manifest.get("source_sha256") == source_sha and manifest.get("config") == config


def init_run(input_path: Path, output_dir: Path, target_words: int, min_words: int,
             max_words: int, block_segments: int, pause_weight: float, context_segments: int) -> dict[str, Any]:
    input_path = input_path.resolve()
    if not input_path.is_file():
        raise TTKError(f"input transcript not found: {input_path}")
    source_sha = file_hash(input_path)
    config = {
        "target_words": target_words,
        "min_words": min_words,
        "max_words": max_words,
        "block_segments": block_segments,
        "pause_weight": pause_weight,
        "context_segments": context_segments,
    }
    if output_dir.exists() and any(output_dir.iterdir()):
        if _existing_run_ok(output_dir, source_sha, config):
            return read_json(output_dir / "manifest.json")
        raise TTKError(f"output directory is non-empty and is not the same initialized run: {output_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    segments, source_format = load_transcript(input_path)
    transcript = {
        "schema": TRANSCRIPT_SCHEMA,
        "source_sha256": source_sha,
        "source_name": input_path.name,
        "segments": [segment_dict(seg) for seg in segments],
    }
    diagnostics = build_diagnostics(segments)
    windows = plan_windows(segments, target_words, min_words, max_words, block_segments, pause_weight, context_segments)
    manifest = {
        "schema": RUN_SCHEMA,
        "contract_version": CONTRACT_VERSION,
        "source_name": input_path.name,
        "source_format": source_format,
        "source_sha256": source_sha,
        "segment_count": len(segments),
        "word_count": sum(seg.word_count for seg in segments),
        "timestamp_quality": diagnostics["timestamp_quality"],
        "window_count": len(windows["windows"]),
        "config": config,
    }
    write_json(output_dir / "manifest.json", manifest)
    write_json(output_dir / "source" / "transcript.json", transcript)
    (output_dir / "source" / "transcript.md").write_text(transcript_markdown(segments, source_sha), encoding="utf-8")
    write_json(output_dir / "source" / "diagnostics.json", diagnostics)
    write_json(output_dir / "windows" / "index.json", windows)
    segment_lookup = {seg["id"]: seg for seg in transcript["segments"]}
    for win in windows["windows"]:
        packet = build_map_packet(win, segment_lookup, source_sha)
        write_json(output_dir / "work" / "packets" / "map" / f"{win['id']}.json", packet)
    (output_dir / "work" / "results" / "map").mkdir(parents=True, exist_ok=True)
    (output_dir / "work" / "results" / "verify").mkdir(parents=True, exist_ok=True)
    return manifest



__all__ = [name for name in globals() if not name.startswith("__")]
