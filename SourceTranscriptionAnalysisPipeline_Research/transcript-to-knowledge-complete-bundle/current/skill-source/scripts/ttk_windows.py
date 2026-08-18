#!/usr/bin/env python3
"""Transcript diagnostics and deterministic processing-window planning."""
from ttk_base import *
def transcript_markdown(segments: list[Segment], source_sha: str) -> str:
    lines = ["# Normalized Transcript", "", f"Source SHA-256: `{source_sha}`", ""]
    for seg in segments:
        if seg.start is None:
            timing = "timing unavailable"
        elif seg.end is None:
            timing = format_timestamp(seg.start) or "timing unavailable"
        else:
            timing = f"{format_timestamp(seg.start)} -> {format_timestamp(seg.end)}"
        speaker = f" · {seg.speaker}" if seg.speaker else ""
        lines.extend([
            f"<a id=\"{seg.id}\"></a>",
            f"**[{seg.id}] {timing}{speaker}**", "", seg.text, "",
        ])
    return "\n".join(lines)


def build_diagnostics(segments: list[Segment]) -> dict[str, Any]:
    issues: list[dict[str, Any]] = []
    missing_start = 0
    missing_end = 0
    missing_speaker = 0
    low_conf_words = 0
    word_probs = 0
    gaps: list[float] = []
    previous: Segment | None = None
    for seg in segments:
        if seg.start is None:
            missing_start += 1
        if seg.end is None:
            missing_end += 1
        if seg.speaker is None:
            missing_speaker += 1
        for word in seg.words:
            if word.probability is not None:
                word_probs += 1
                if word.probability < 0.5:
                    low_conf_words += 1
        if previous is not None:
            if seg.start is not None and previous.start is not None and seg.start < previous.start:
                issues.append({"type": "non_monotonic_start", "segments": [previous.id, seg.id]})
            if seg.start is not None and previous.end is not None:
                gap = seg.start - previous.end
                if gap >= 0:
                    gaps.append(gap)
                    if gap > 15:
                        issues.append({"type": "large_gap", "seconds": round(gap, 3), "segments": [previous.id, seg.id]})
                elif gap < -2:
                    issues.append({"type": "timestamp_overlap", "seconds": round(-gap, 3), "segments": [previous.id, seg.id]})
            if norm_text(seg.text) == norm_text(previous.text) and norm_text(seg.text):
                issues.append({"type": "consecutive_duplicate_text", "segments": [previous.id, seg.id]})
        previous = seg
    total_words = sum(seg.word_count for seg in segments)
    return {
        "schema": "ttk.source-diagnostics.v2",
        "segment_count": len(segments),
        "word_count": total_words,
        "timestamp_quality": timestamp_quality(segments),
        "missing_start_segments": missing_start,
        "missing_end_segments": missing_end,
        "missing_speaker_segments": missing_speaker,
        "word_probability_count": word_probs,
        "low_confidence_word_count": low_conf_words,
        "median_inter_segment_gap_seconds": round(statistics.median(gaps), 3) if gaps else None,
        "issue_count": len(issues),
        "issues": issues,
    }


def _idf(segments: list[Segment]) -> dict[str, float]:
    doc_count = max(1, len(segments))
    df: dict[str, int] = {}
    for seg in segments:
        for token in set(tokens(seg.text)):
            df[token] = df.get(token, 0) + 1
    return {term: math.log((doc_count + 1) / (count + 1)) + 1.0 for term, count in df.items()}


def _weighted_counts(segments: list[Segment], idf: dict[str, float]) -> dict[str, float]:
    counts: dict[str, float] = {}
    for seg in segments:
        for token in tokens(seg.text):
            counts[token] = counts.get(token, 0.0) + idf.get(token, 1.0)
    return counts


def _cosine(left: dict[str, float], right: dict[str, float]) -> float:
    if not left or not right:
        return 0.0
    common = set(left).intersection(right)
    dot = sum(left[k] * right[k] for k in common)
    lnorm = math.sqrt(sum(v * v for v in left.values()))
    rnorm = math.sqrt(sum(v * v for v in right.values()))
    if not lnorm or not rnorm:
        return 0.0
    return max(0.0, min(1.0, dot / (lnorm * rnorm)))


def boundary_scores(segments: list[Segment], block_segments: int = 4, pause_weight: float = 0.15) -> list[dict[str, Any]]:
    if block_segments <= 0:
        raise TTKError("block_segments must be > 0")
    if not 0.0 <= pause_weight <= 1.0:
        raise TTKError("pause_weight must be between 0 and 1")
    idf = _idf(segments)
    positive_gaps = [
        max(0.0, segments[i].start - segments[i - 1].end)
        for i in range(1, len(segments))
        if segments[i].start is not None and segments[i - 1].end is not None and segments[i].start >= segments[i - 1].end
    ]
    typical_gap = statistics.median([g for g in positive_gaps if g > 0]) if any(g > 0 for g in positive_gaps) else 1.0
    out: list[dict[str, Any]] = []
    for gap_index in range(1, len(segments)):
        left = segments[max(0, gap_index - block_segments):gap_index]
        right = segments[gap_index:min(len(segments), gap_index + block_segments)]
        lexical = 1.0 - _cosine(_weighted_counts(left, idf), _weighted_counts(right, idf))
        pause = 0.0
        prev, cur = segments[gap_index - 1], segments[gap_index]
        raw_gap: float | None = None
        if prev.end is not None and cur.start is not None:
            raw_gap = max(0.0, cur.start - prev.end)
            pause = min(1.0, raw_gap / max(0.001, typical_gap * 4))
        score = (1.0 - pause_weight) * lexical + pause_weight * pause
        out.append({
            "after_segment": prev.id,
            "before_segment": cur.id,
            "gap_index": gap_index,
            "lexical_dissimilarity": round(lexical, 6),
            "pause_score": round(pause, 6),
            "pause_seconds": round(raw_gap, 3) if raw_gap is not None else None,
            "boundary_score": round(score, 6),
        })
    return out


def plan_windows(segments: list[Segment], target_words: int = 1100, min_words: int = 700,
                 max_words: int = 1500, block_segments: int = 4, pause_weight: float = 0.15,
                 context_segments: int = 1) -> dict[str, Any]:
    if not (0 < min_words <= target_words <= max_words):
        raise TTKError("require 0 < min_words <= target_words <= max_words")
    if context_segments < 0:
        raise TTKError("context_segments must be >= 0")
    scores = boundary_scores(segments, block_segments, pause_weight)
    by_gap = {row["gap_index"]: row for row in scores}
    windows: list[dict[str, Any]] = []
    start = 0
    while start < len(segments):
        cumulative = 0
        candidates: list[tuple[float, int, int]] = []
        end = start
        while end < len(segments):
            cumulative += segments[end].word_count
            gap = end + 1
            if gap < len(segments) and cumulative >= min_words:
                boundary = by_gap.get(gap, {"boundary_score": 0.0})["boundary_score"]
                span = max(1, max_words - min_words)
                closeness = max(0.0, 1.0 - abs(cumulative - target_words) / span)
                selection = float(boundary) + 0.12 * closeness
                candidates.append((selection, gap, cumulative))
            if cumulative >= max_words or end == len(segments) - 1:
                break
            end += 1
        if end == len(segments) - 1:
            chosen_end = len(segments)
            chosen_words = sum(s.word_count for s in segments[start:chosen_end])
            chosen_boundary = None
        elif candidates:
            valid = [c for c in candidates if c[2] <= max_words]
            pool = valid or candidates
            _, chosen_end, chosen_words = max(pool, key=lambda item: (item[0], -abs(item[2] - target_words), -item[1]))
            chosen_boundary = by_gap.get(chosen_end)
        else:
            chosen_end = min(len(segments), end + 1)
            chosen_words = sum(s.word_count for s in segments[start:chosen_end])
            chosen_boundary = by_gap.get(chosen_end)
        core = segments[start:chosen_end]
        context_start = max(0, start - context_segments)
        context_end = min(len(segments), chosen_end + context_segments)
        full = segments[context_start:context_end]
        windows.append({
            "id": f"window-{len(windows) + 1:04d}",
            "core_start_segment": core[0].id,
            "core_end_segment": core[-1].id,
            "core_segment_ids": [s.id for s in core],
            "context_before_segment_ids": [s.id for s in segments[context_start:start]],
            "context_after_segment_ids": [s.id for s in segments[chosen_end:context_end]],
            "packet_segment_ids": [s.id for s in full],
            "word_count": chosen_words,
            "start": core[0].start,
            "end": core[-1].end,
            "start_hms": format_timestamp(core[0].start),
            "end_hms": format_timestamp(core[-1].end),
            "selected_boundary": chosen_boundary,
        })
        start = chosen_end
    all_core = [sid for win in windows for sid in win["core_segment_ids"]]
    expected = [s.id for s in segments]
    if all_core != expected:
        raise TTKError("internal window coverage error")
    return {
        "schema": WINDOW_SCHEMA,
        "algorithm": {
            "name": "lexical-cohesion-plus-pause",
            "target_words": target_words,
            "min_words": min_words,
            "max_words": max_words,
            "block_segments": block_segments,
            "pause_weight": pause_weight,
            "context_segments": context_segments,
            "note": "Processing windows are transport boundaries, not final semantic chapters.",
        },
        "boundary_scores": scores,
        "windows": windows,
    }



__all__ = [name for name in globals() if not name.startswith("__")]
