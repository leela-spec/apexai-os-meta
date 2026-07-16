#!/usr/bin/env python3
"""Split a ChatGPT/Codex Markdown export into timestamped message files.

The export format handled here places a display timestamp on the line directly
after the message it belongs to. The script never invents missing timestamps or
silently discards trailing UI fragments.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo


TIMESTAMP_RE = re.compile(
    r"^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) "
    r"(\d{1,2}):(\d{2}) (AM|PM)$"
)
ASSISTANT_START_RE = re.compile(
    r"^(Worked for\b|I(?:’|')ll\b|I(?:’|')m\b|The skill(?:’|')s router\b|"
    r"The checked-out KB\b|Remote main\b|Deterministic Apex KB lifecycle\b|"
    r"Reached the mandatory wait point\b)",
    re.IGNORECASE,
)
USER_INTERRUPT_RE = re.compile(
    r"^(yes but push afterwords\b|yes, implement this plan$)", re.IGNORECASE
)
UI_TAIL_MARKERS = {
    "Show in text field",
    "Environment",
    "Changes",
    "Local",
    "Commit or push",
    "Compare branch",
    "Plan",
    "Browser",
    "Sources",
    "View all",
}


@dataclass
class Message:
    sequence: int
    start_line: int
    end_line: int
    content: str
    display_timestamp: str
    iso_timestamp: str | None
    timestamp_relation: str
    role: str
    role_confidence: str
    truncated: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Markdown chat-history file")
    parser.add_argument("output", type=Path, help="Directory for extracted files")
    parser.add_argument(
        "--conversation-date",
        help="Known display date in YYYY-MM-DD form; omit if unknown",
    )
    parser.add_argument(
        "--timezone",
        default="Europe/Berlin",
        help="IANA timezone for normalized timestamps (default: Europe/Berlin)",
    )
    parser.add_argument(
        "--utc-offset",
        help="Fixed UTC offset fallback such as +02:00 when IANA timezone data is unavailable",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Replace only the generated messages/fragments directories and indexes",
    )
    return parser.parse_args()


def normalize_timestamp(
    display: str,
    conversation_date: str | None,
    timezone_name: str,
    utc_offset: str | None,
) -> str | None:
    if conversation_date is None:
        return None
    match = TIMESTAMP_RE.fullmatch(display)
    if not match:
        return None
    hour = int(match.group(2))
    minute = int(match.group(3))
    meridiem = match.group(4)
    if meridiem == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12
    date = datetime.strptime(conversation_date, "%Y-%m-%d").date()
    try:
        tzinfo = ZoneInfo(timezone_name)
    except Exception:
        if not utc_offset or not re.fullmatch(r"[+-]\d{2}:\d{2}", utc_offset):
            raise RuntimeError(
                f"Timezone data for {timezone_name!r} is unavailable; supply --utc-offset"
            )
        sign = 1 if utc_offset[0] == "+" else -1
        offset_hours, offset_minutes = map(int, utc_offset[1:].split(":"))
        tzinfo = timezone(sign * timedelta(hours=offset_hours, minutes=offset_minutes))
    value = datetime(date.year, date.month, date.day, hour, minute, tzinfo=tzinfo)
    expected_weekday = match.group(1)
    if value.strftime("%A") != expected_weekday:
        raise ValueError(
            f"{conversation_date} is {value.strftime('%A')}, but the export says "
            f"{expected_weekday}"
        )
    return value.isoformat()


def trim_message_lines(lines: list[str], start: int, end: int) -> tuple[int, int, list[str]]:
    while start <= end and not lines[start - 1].strip():
        start += 1
    while end >= start and not lines[end - 1].strip():
        end -= 1
    return start, end, lines[start - 1 : end]


def infer_role(content: str, sequence: int) -> tuple[str, str]:
    first = next((line.strip() for line in content.splitlines() if line.strip()), "")
    if ASSISTANT_START_RE.search(first):
        return "assistant", "high"
    if sequence == 1:
        return "user", "high"
    return "user", "medium"


def slug(text: str, limit: int = 56) -> str:
    first = next((line.strip() for line in text.splitlines() if line.strip()), "message")
    value = re.sub(r"[^a-z0-9]+", "-", first.lower()).strip("-")
    return (value[:limit].rstrip("-") or "message")


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def parse_messages(
    text: str,
    conversation_date: str | None,
    timezone_name: str,
    utc_offset: str | None,
) -> tuple[list[Message], tuple[int, int, str] | None]:
    lines = text.splitlines()
    messages: list[Message] = []
    previous_boundary = 0

    def add_message(
        start: int,
        end: int,
        body_lines: list[str],
        display: str,
        exact_timestamp: bool,
    ) -> None:
        content = "\n".join(body_lines)
        if not content:
            return
        sequence = len(messages) + 1
        role, confidence = infer_role(content, sequence)
        messages.append(
            Message(
                sequence=sequence,
                start_line=start,
                end_line=end,
                content=content,
                display_timestamp=(display if exact_timestamp else f"before {display}; exact time absent"),
                iso_timestamp=(
                    normalize_timestamp(display, conversation_date, timezone_name, utc_offset)
                    if exact_timestamp
                    else None
                ),
                timestamp_relation="exact" if exact_timestamp else "upper_bound_only",
                role=role,
                role_confidence=confidence,
                truncated=any(marker in content for marker in ("Show more", "â€¦", "…")),
            )
        )

    for timestamp_line, line in enumerate(lines, start=1):
        display = line.strip()
        if not TIMESTAMP_RE.fullmatch(display):
            continue
        start, end, body_lines = trim_message_lines(lines, previous_boundary + 1, timestamp_line - 1)
        content = "\n".join(body_lines)
        if content:
            initial_role, _ = infer_role(content, len(messages) + 1)
            interrupt_index = next(
                (
                    index
                    for index, body_line in enumerate(body_lines)
                    if USER_INTERRUPT_RE.match(body_line.strip())
                ),
                None,
            )
            if initial_role == "assistant" and interrupt_index not in (None, 0):
                first_lines = body_lines[:interrupt_index]
                while first_lines and not first_lines[-1].strip():
                    first_lines.pop()
                second_lines = body_lines[interrupt_index:]
                while second_lines and not second_lines[0].strip():
                    second_lines.pop(0)
                first_end = start + interrupt_index - 1
                second_start = start + interrupt_index
                add_message(start, first_end, first_lines, display, exact_timestamp=False)
                add_message(second_start, end, second_lines, display, exact_timestamp=True)
            else:
                add_message(start, end, body_lines, display, exact_timestamp=True)
        previous_boundary = timestamp_line

    tail_start, tail_end, tail_lines = trim_message_lines(lines, previous_boundary + 1, len(lines))
    tail_content = "\n".join(tail_lines)
    tail = (tail_start, tail_end, tail_content) if tail_content else None
    return messages, tail


def frontmatter(message: Message, source: Path) -> str:
    digest = hashlib.sha256(message.content.encode("utf-8")).hexdigest()
    kind = "question_or_instruction" if message.role == "user" else "answer_or_execution_report"
    iso = yaml_string(message.iso_timestamp) if message.iso_timestamp else "null"
    return "\n".join(
        [
            "---",
            f"message_id: chat-{message.sequence:03d}",
            f"sequence: {message.sequence}",
            f"role: {message.role}",
            f"role_confidence: {message.role_confidence}",
            f"message_kind: {kind}",
            f"display_timestamp: {yaml_string(message.display_timestamp)}",
            f"timestamp: {iso}",
            f"timestamp_relation: {message.timestamp_relation}",
            f"timestamp_source: {'export_plus_supplied_date' if message.iso_timestamp else 'not_present_for_message'}",
            f"source_file: {yaml_string(str(source.resolve()))}",
            f"source_lines: {yaml_string(f'{message.start_line}-{message.end_line}')}",
            f"content_sha256: {digest}",
            f"export_truncation_marker_present: {str(message.truncated).lower()}",
            "---",
        ]
    )


def safe_clean(output: Path) -> None:
    for name in ("messages", "fragments"):
        target = output / name
        if target.exists():
            shutil.rmtree(target)
    for name in ("INDEX.md", "extraction-report.json", "transcript-quality-report.md"):
        target = output / name
        if target.exists():
            target.unlink()


def write_outputs(
    source: Path,
    output: Path,
    messages: Iterable[Message],
    tail: tuple[int, int, str] | None,
    clean: bool,
) -> None:
    messages = list(messages)
    output.mkdir(parents=True, exist_ok=True)
    if clean:
        safe_clean(output)
    message_dir = output / "messages"
    fragment_dir = output / "fragments"
    message_dir.mkdir(exist_ok=True)
    fragment_dir.mkdir(exist_ok=True)

    index_rows = []
    report_messages = []
    for message in messages:
        stamp = (
            message.iso_timestamp[:16].replace(":", "-").replace("T", "_")
            if message.iso_timestamp
            else re.sub(r"[^A-Za-z0-9]+", "-", message.display_timestamp)
        )
        filename = f"{message.sequence:03d}-{stamp}-{message.role}-{slug(message.content)}.md"
        path = message_dir / filename
        path.write_text(frontmatter(message, source) + "\n\n" + message.content + "\n", encoding="utf-8")
        index_rows.append(
            f"| {message.sequence:03d} | {message.display_timestamp} | {message.role} | "
            f"{message.role_confidence} | {'yes' if message.truncated else 'no'} | "
            f"[{filename}](messages/{filename}) |"
        )
        report_messages.append(
            {
                "message_id": f"chat-{message.sequence:03d}",
                "role": message.role,
                "role_confidence": message.role_confidence,
                "display_timestamp": message.display_timestamp,
                "timestamp": message.iso_timestamp,
                "timestamp_relation": message.timestamp_relation,
                "source_lines": [message.start_line, message.end_line],
                "truncated": message.truncated,
                "file": f"messages/{filename}",
            }
        )

    fragment_record = None
    if tail:
        start, end, content = tail
        fragment_path = fragment_dir / "001-untimestamped-trailing-fragment.md"
        fragment_path.write_text(
            "---\n"
            "fragment_id: trailing-001\n"
            "role: unknown\n"
            "timestamp: null\n"
            "timestamp_source: missing\n"
            f"source_file: {yaml_string(str(source.resolve()))}\n"
            f"source_lines: {yaml_string(f'{start}-{end}')}\n"
            "classification: unclosed_export_or_ui_fragment\n"
            "---\n\n"
            + content
            + "\n",
            encoding="utf-8",
        )
        fragment_record = {
            "source_lines": [start, end],
            "file": "fragments/001-untimestamped-trailing-fragment.md",
            "ui_markers_detected": sorted({line.strip() for line in content.splitlines()} & UI_TAIL_MARKERS),
        }

    index = "\n".join(
        [
            "# Timestamped Chat Message Index",
            "",
            f"Source: `{source.resolve()}`",
            "",
            "Exact timestamps are taken from the timestamp displayed after a message in the export.",
            "When a user interrupted assistant commentary before the next timestamp, the commentary keeps only an upper-bound time.",
            "Role confidence is explicit because the source export contains no machine-readable speaker labels.",
            "",
            "## How to use this index",
            "",
            "1. Read `HANDOVER.md` and `transcript-quality-report.md` first.",
            "2. Open only the message files relevant to the incident under investigation.",
            "3. Use `source_lines` and `content_sha256` to preserve evidence traceability.",
            "4. Verify repository, commit, and push claims independently before classifying them as confirmed.",
            "",
            "Generated supporting artifacts:",
            "",
            "- `extraction-report.json`: machine-readable message inventory.",
            "- `transcript-quality-report.md`: truncation and timestamp limitations.",
            "- `fragments/`: material that could not be classified as a complete timestamped message.",
            "",
            "## Timestamped messages",
            "",
            "| # | Display timestamp | Role | Role confidence | Truncated | File |",
            "|---:|---|---|---|---|---|",
            *index_rows,
            "",
            "## Unclosed fragments",
            "",
            "- [Untimestamped trailing fragment](fragments/001-untimestamped-trailing-fragment.md)"
            if tail
            else "- None",
            "",
        ]
    )
    (output / "INDEX.md").write_text(index, encoding="utf-8")

    report = {
        "source": str(source.resolve()),
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "message_count": len(messages),
        "messages": report_messages,
        "trailing_fragment": fragment_record,
    }
    (output / "extraction-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    truncated_ids = [f"chat-{m.sequence:03d}" for m in messages if m.truncated]
    quality = "\n".join(
        [
            "# Transcript Quality Report",
            "",
            f"- Timestamped messages extracted: {len(messages)}",
            f"- Messages containing export truncation markers: {len(truncated_ids)}",
            f"- Truncated message IDs: {', '.join(truncated_ids) if truncated_ids else 'None'}",
            f"- Untimestamped trailing fragment present: {'yes' if tail else 'no'}",
            "- Speaker labels were inferred because the export does not encode roles.",
            "- Existing mojibake in the source was preserved; the extractor does not rewrite quoted evidence.",
            "- A `Show more` marker means the source export may omit content. Extracted files must not be treated as complete evidence for those messages.",
            "",
        ]
    )
    (output / "transcript-quality-report.md").write_text(quality, encoding="utf-8")


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    output = args.output.resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    text = source.read_text(encoding="utf-8-sig")
    messages, tail = parse_messages(
        text, args.conversation_date, args.timezone, args.utc_offset
    )
    if not messages:
        raise RuntimeError("No timestamped messages were detected")
    write_outputs(source, output, messages, tail, args.clean)
    print(f"Extracted {len(messages)} timestamped messages into {output}")
    if tail:
        print("Preserved one untimestamped trailing fragment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
