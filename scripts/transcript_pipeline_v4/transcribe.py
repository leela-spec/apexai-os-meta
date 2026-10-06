"""Transcribe local media into source-order TXT and timestamped SRT files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable, Protocol


class Segment(Protocol):
    start: float
    end: float
    text: str


def format_srt_timestamp(seconds: float) -> str:
    total_milliseconds = round(seconds * 1000)
    hours, remainder = divmod(total_milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    whole_seconds, milliseconds = divmod(remainder, 1_000)
    return f"{hours:02d}:{minutes:02d}:{whole_seconds:02d},{milliseconds:03d}"


def write_outputs(
    segments: Iterable[Segment],
    text_path: Path,
    srt_path: Path,
    segments_json_path: Path | None = None,
) -> None:
    transcript_lines: list[str] = []
    srt_entries: list[str] = []
    segment_records: list[dict[str, object]] = []

    for index, segment in enumerate(segments, start=1):
        text = segment.text.strip()
        transcript_lines.append(text)
        srt_entries.append(
            f"{index}\n"
            f"{format_srt_timestamp(segment.start)} --> {format_srt_timestamp(segment.end)}\n"
            f"{text}"
        )
        record: dict[str, object] = {
            "ordinal": index,
            "start": segment.start,
            "end": segment.end,
            "text": text,
        }
        for field in ("avg_logprob", "compression_ratio", "no_speech_prob", "temperature"):
            value = getattr(segment, field, None)
            if value is not None:
                record[field] = value
        segment_records.append(record)

    text_path.parent.mkdir(parents=True, exist_ok=True)
    srt_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.write_text("\n".join(transcript_lines) + ("\n" if transcript_lines else ""), encoding="utf-8")
    srt_path.write_text("\n\n".join(srt_entries) + ("\n" if srt_entries else ""), encoding="utf-8")
    if segments_json_path is not None:
        segments_json_path.parent.mkdir(parents=True, exist_ok=True)
        segments_json_path.write_text(
            json.dumps(
                {"schema_version": "1.0", "segments": segment_records},
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Local media file to transcribe.")
    parser.add_argument("--text-out", required=True, type=Path, help="Destination UTF-8 transcript TXT file.")
    parser.add_argument("--srt-out", required=True, type=Path, help="Destination UTF-8 SRT subtitle file.")
    parser.add_argument(
        "--segments-json-out",
        type=Path,
        help="Optional destination for source-order segments and available Whisper decoder metadata.",
    )
    parser.add_argument("--language", choices=("en", "de"), help="Optional source language hint.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    from faster_whisper import WhisperModel

    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
    segments, _info = model.transcribe(
        str(args.input),
        task="transcribe",
        language=args.language,
        vad_filter=True,
        word_timestamps=False,
    )
    write_outputs(segments, args.text_out, args.srt_out, args.segments_json_out)


if __name__ == "__main__":
    main()
