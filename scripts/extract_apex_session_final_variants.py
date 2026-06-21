#!/usr/bin/env python3
"""Extract final apex-session variant files from the v2 full-answer source.

The extractor copies file-body bytes exactly from fenced markdown blocks. It
does not normalize line endings, repair Markdown, or modify canonical package
files.
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
    / "ProFinal_apex-session_skillpack_fullanswer_v2.md"
)
PACKAGE_ROOT = REPO_ROOT / ".claude" / "skills" / "apex-session"
REPORT_PATH = PACKAGE_ROOT / "apex-session-final-extraction-report.md"
EXPECTED_BLOCK_COUNT = 10
PLACEHOLDER = b"<complete final file content>"


@dataclass(frozen=True)
class Block:
    target_path: Path
    output_path: Path
    content: bytes
    source_start: int
    source_end: int


@dataclass(frozen=True)
class Action:
    kind: str
    path: Path
    content: bytes | None
    source_hash: str
    note: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def repo_relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def resolve_target(raw_target: bytes) -> Path:
    target_text = raw_target.decode("utf-8")
    if "\\" in target_text:
        raise ValueError(f"Backslash is not allowed in target path: {target_text}")
    target = (REPO_ROOT / target_text).resolve()
    if not target.is_relative_to(PACKAGE_ROOT):
        raise ValueError(f"Target is outside apex-session package: {target_text}")
    if target.suffix != ".md":
        raise ValueError(f"Target must be a Markdown file: {target_text}")
    return target


def final_variant_path(target_path: Path) -> Path:
    return target_path.with_name(f"{target_path.stem}.final{target_path.suffix}")


def find_outer_fenced_content(data: bytes, search_from: int) -> tuple[int, int, int]:
    opener = re.search(br"```(?:markdown)?[ \t]*\r?\n", data[search_from:])
    if not opener:
        raise ValueError("Missing opening fenced markdown block")

    content_start = search_from + opener.end()
    line_start = content_start

    while line_start < len(data):
        line_end = data.find(b"\n", line_start)
        if line_end == -1:
            line_end = len(data)
            next_line_start = len(data)
        else:
            next_line_start = line_end + 1

        line = data[line_start:line_end]
        line_without_cr = line[:-1] if line.endswith(b"\r") else line
        if line_without_cr.strip() == b"```":
            content_end = line_start
            if content_end > content_start and data[content_end - 1 : content_end] == b"\n":
                content_end -= 1
                if content_end > content_start and data[content_end - 1 : content_end] == b"\r":
                    content_end -= 1
            return content_start, content_end, next_line_start

        line_start = next_line_start

    raise ValueError("Missing closing fenced markdown block")


def parse_blocks() -> list[Block]:
    data = SOURCE_PATH.read_bytes()
    heading_re = re.compile(
        br"(?m)^#{2,4}[ \t]+(?:\d+(?:\.\d+)?[ \t]+)?"
        br"`(?P<target>\.claude/skills/apex-session/[^`]+)`[ \t]*\r?\n[ \t]*\r?\n"
    )
    blocks: list[Block] = []

    for match in heading_re.finditer(data):
        target_path = resolve_target(match.group("target"))
        content_start, content_end, _ = find_outer_fenced_content(data, match.end())
        content = data[content_start:content_end]
        blocks.append(
            Block(
                target_path=target_path,
                output_path=final_variant_path(target_path),
                content=content,
                source_start=content_start,
                source_end=content_end,
            )
        )

    return blocks


def validate_blocks(blocks: list[Block]) -> None:
    if len(blocks) != EXPECTED_BLOCK_COUNT:
        raise ValueError(f"Detected {len(blocks)} blocks; expected {EXPECTED_BLOCK_COUNT}")

    targets = [block.target_path for block in blocks]
    duplicates = sorted({target for target in targets if targets.count(target) > 1})
    if duplicates:
        rendered = ", ".join(repo_relative(path) for path in duplicates)
        raise ValueError(f"Duplicate target paths detected: {rendered}")

    for block in blocks:
        if block.content.strip() == PLACEHOLDER:
            raise ValueError(f"Placeholder block detected: {repo_relative(block.target_path)}")
        if not block.content.strip():
            raise ValueError(f"Empty block detected: {repo_relative(block.target_path)}")


def plan_actions(blocks: list[Block]) -> list[Action]:
    actions: list[Action] = []
    for block in blocks:
        content_hash = sha256_bytes(block.content)
        if block.output_path.exists():
            existing = block.output_path.read_bytes()
            if existing != block.content:
                raise ValueError(
                    f"Existing final variant differs from extracted source: "
                    f"{repo_relative(block.output_path)}"
                )
            actions.append(
                Action(
                    kind="exists-same",
                    path=block.output_path,
                    content=None,
                    source_hash=content_hash,
                    note=f"matches extracted source for {repo_relative(block.target_path)}",
                )
            )
        else:
            actions.append(
                Action(
                    kind="write",
                    path=block.output_path,
                    content=block.content,
                    source_hash=content_hash,
                    note=f"write final variant for {repo_relative(block.target_path)}",
                )
            )
    return actions


def apply_actions(actions: list[Action]) -> None:
    for action in actions:
        if action.kind != "write":
            continue
        if action.content is None:
            raise ValueError(f"Write action missing content: {repo_relative(action.path)}")
        action.path.parent.mkdir(parents=True, exist_ok=True)
        action.path.write_bytes(action.content)
        written_hash = sha256_bytes(action.path.read_bytes())
        if written_hash != action.source_hash:
            raise ValueError(
                f"Verification failed for {repo_relative(action.path)}: "
                f"expected {action.source_hash}, got {written_hash}"
            )


def render_report(blocks: list[Block], actions: list[Action]) -> bytes:
    action_by_path = {action.path: action for action in actions}
    lines = [
        "# apex-session Final Variant Extraction Report",
        "",
        "Generated by `scripts/extract_apex_session_final_variants.py`.",
        "",
        "## Source",
        "",
        f"- path: `{repo_relative(SOURCE_PATH)}`",
        f"- sha256: `{sha256_bytes(SOURCE_PATH.read_bytes())}`",
        f"- extracted_blocks: `{len(blocks)}`",
        "",
        "## Extracted Files",
        "",
    ]

    for block in blocks:
        action = action_by_path[block.output_path]
        lines.append(f"- `{repo_relative(block.output_path)}`")
        lines.append(f"  - target_path: `{repo_relative(block.target_path)}`")
        lines.append(f"  - action: `{action.kind}`")
        lines.append(f"  - bytes: `{len(block.content)}`")
        lines.append(f"  - sha256: `{sha256_bytes(block.content)}`")
        lines.append(f"  - source_byte_range: `{block.source_start}:{block.source_end}`")

    lines.extend(["", "## Conflicts", "", "None.", ""])
    return "\n".join(lines).encode("utf-8")


def write_report(report: bytes) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_bytes(report)
    written_hash = sha256_bytes(REPORT_PATH.read_bytes())
    expected_hash = sha256_bytes(report)
    if written_hash != expected_hash:
        raise ValueError(
            f"Verification failed for {repo_relative(REPORT_PATH)}: "
            f"expected {expected_hash}, got {written_hash}"
        )


def print_plan(blocks: list[Block], actions: list[Action], report: bytes) -> None:
    print(f"source: {repo_relative(SOURCE_PATH)} sha256={sha256_bytes(SOURCE_PATH.read_bytes())}")
    print(f"blocks: {len(blocks)}")
    for action in actions:
        block = next(block for block in blocks if block.output_path == action.path)
        print(
            f"{action.kind.upper():11} {repo_relative(action.path)} "
            f"target={repo_relative(block.target_path)} "
            f"bytes={len(block.content)} sha256={sha256_bytes(block.content)}"
        )
    print(f"REPORT      {repo_relative(REPORT_PATH)} bytes={len(report)} sha256={sha256_bytes(report)}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="show planned actions without writing files")
    args = parser.parse_args(argv)

    blocks = parse_blocks()
    validate_blocks(blocks)
    actions = plan_actions(blocks)
    report = render_report(blocks, actions)
    print_plan(blocks, actions, report)

    if not args.dry_run:
        apply_actions(actions)
        write_report(report)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
