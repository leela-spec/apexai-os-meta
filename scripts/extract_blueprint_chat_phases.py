#!/usr/bin/env python3
"""Extract phase answer chapters from BlueprintProjectMapping chat history.

The extractor copies exact source bytes for detected phase answer chapters.
Missing requested chapters are reported, not synthesized.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = (
    REPO_ROOT
    / "FutureDevelopments&Research"
    / "ProjectMM&Task&KB"
    / "DeepResearch-File&Process"
    / "3rdIteration_ProThinking"
    / "Preps"
    / "BlueprintProjectMapping_ChatHistory_GPT.md"
)
OUTPUT_DIR = REPO_ROOT / "source-knowledge" / "ProjectRepos" / "ProjectMapping&Apex"
REPORT_PATH = OUTPUT_DIR / "blueprint-chat-phase-extraction-report.md"


REQUESTED_PHASES = [
    ("phase-1-authority-extraction.md", "Phase 1 Authority Extraction", br"Phase 1"),
    ("phase-2-source-map.md", "Phase 2 Source Map", br"Phase 2"),
    ("phase-3-file-read-ledger.md", "Phase 3 File Read Ledger", br"Phase 3"),
    ("phase-4-mechanism-ledger.md", "Phase 4 Mechanism Ledger", br"Phase 4"),
    (
        "phase-5-coverage-gate.md",
        "Phase 5 Coverage Gate",
        br"# Phase 5 Complete",
    ),
    (
        "phase-6-pm2-audit.md",
        "Phase 6 PM2 Audit",
        br"# Phase 6 Complete",
    ),
]


@dataclass(frozen=True)
class Extraction:
    filename: str
    chapter: str
    content: bytes
    start: int
    end: int


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def find_line_start(data: bytes, marker: bytes) -> int | None:
    idx = data.find(marker)
    if idx == -1:
        return None
    return data.rfind(b"\n", 0, idx) + 1


def normalize_marker_re(marker: bytes) -> re.Pattern[bytes]:
    parts = marker.split(b" ")
    return re.compile(br"[ \t]+".join(re.escape(part) for part in parts))


def find_heading_start(data: bytes, marker: bytes) -> int | None:
    pattern = normalize_marker_re(marker)
    for match in pattern.finditer(data):
        line_start = data.rfind(b"\n", 0, match.start()) + 1
        line_end = data.find(b"\n", match.end())
        if line_end == -1:
            line_end = len(data)
        line = data[line_start:line_end].strip()
        if line.startswith(b"#"):
            return line_start
    return None


def find_next_phase_answer_start(data: bytes, start: int) -> int:
    next_markers = [
        br"\n# Phase 5 Complete",
        br"\n# Phase 6 Complete",
        br"\nStarting \*\*Phase",
        br"\nAcknowledged ",
    ]
    candidates = [m.start() + 1 for pat in next_markers for m in re.finditer(pat, data[start:])]
    absolute = [start + candidate for candidate in candidates if start + candidate > start]
    return min(absolute) if absolute else len(data)


def parse() -> tuple[list[Extraction], list[str]]:
    data = SOURCE_PATH.read_bytes()
    found: list[Extraction] = []
    missing: list[str] = []

    phase5_start = find_heading_start(data, b"# Phase 5 Complete")
    phase6_start = find_heading_start(data, b"# Phase 6 Complete")

    starts = {
        "Phase 5 Coverage Gate": phase5_start,
        "Phase 6 PM2 Audit": phase6_start,
    }
    ends = {
        "Phase 5 Coverage Gate": phase6_start if phase5_start is not None and phase6_start is not None else None,
        "Phase 6 PM2 Audit": len(data) if phase6_start is not None else None,
    }

    for filename, chapter, marker in REQUESTED_PHASES:
        if chapter in starts:
            start = starts[chapter]
            end = ends[chapter]
            if start is None or end is None:
                missing.append(chapter)
                continue
            content = data[start:end].rstrip(b"\r\n") + b"\n"
            found.append(Extraction(filename, chapter, content, start, end))
            continue

        # Require a completed/output heading for Phase 1-4. Mentions in the prompt,
        # phase split table, or later references are not treated as extractable answers.
        completed = find_heading_start(data, marker + b" Complete")
        if completed is None:
            missing.append(chapter)
            continue
        end = find_next_phase_answer_start(data, completed)
        content = data[completed:end].rstrip(b"\r\n") + b"\n"
        found.append(Extraction(filename, chapter, content, completed, end))

    return found, missing


def render_report(extractions: list[Extraction], missing: list[str]) -> bytes:
    lines = [
        "# Blueprint Chat Phase Extraction Report",
        "",
        f"- source: `{rel(SOURCE_PATH)}`",
        f"- source_sha256: `{sha256_bytes(SOURCE_PATH.read_bytes())}`",
        f"- output_dir: `{rel(OUTPUT_DIR)}`",
        "",
        "## Extracted",
        "",
    ]
    if extractions:
        for item in extractions:
            lines.append(f"- `{item.chapter}` -> `{item.filename}`")
            lines.append(f"  - bytes: `{len(item.content)}`")
            lines.append(f"  - sha256: `{sha256_bytes(item.content)}`")
            lines.append(f"  - source_byte_range: `{item.start}:{item.end}`")
    else:
        lines.append("None.")

    lines.extend(["", "## Missing Requested Chapters", ""])
    if missing:
        for chapter in missing:
            lines.append(
                f"- `{chapter}`: no completed answer chapter with that phase was present in the source file."
            )
    else:
        lines.append("None.")
    lines.append("")
    return "\n".join(lines).encode("utf-8")


def plan_actions(extractions: list[Extraction]) -> list[tuple[Path, bytes, str]]:
    actions = []
    for item in extractions:
        path = OUTPUT_DIR / item.filename
        actions.append((path, item.content, item.chapter))
    return actions


def write_verified(path: Path, content: bytes) -> str:
    expected = sha256_bytes(content)
    if path.exists() and path.read_bytes() != content:
        raise ValueError(f"Existing file differs from extracted source: {rel(path)}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    actual = sha256_bytes(path.read_bytes())
    if actual != expected:
        raise ValueError(f"Verification failed for {rel(path)}: expected {expected}, got {actual}")
    return actual


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="show extraction plan without writing files")
    args = parser.parse_args(argv)

    extractions, missing = parse()
    actions = plan_actions(extractions)
    report = render_report(extractions, missing)

    print(f"source: {rel(SOURCE_PATH)} sha256={sha256_bytes(SOURCE_PATH.read_bytes())}")
    for path, content, chapter in actions:
        state = "exists-same" if path.exists() and path.read_bytes() == content else "write"
        print(f"{state.upper():11} {rel(path)} chapter={chapter!r} bytes={len(content)} sha256={sha256_bytes(content)}")
    for chapter in missing:
        print(f"MISSING     {chapter}")

    if args.dry_run:
        print(f"DRY-RUN     {rel(REPORT_PATH)} bytes={len(report)} sha256={sha256_bytes(report)}")
        return 0

    for path, content, _chapter in actions:
        write_verified(path, content)
    write_verified(REPORT_PATH, report)
    print(f"REPORT      {rel(REPORT_PATH)} bytes={len(report)} sha256={sha256_bytes(report)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
