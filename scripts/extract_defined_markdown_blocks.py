#!/usr/bin/env python3
"""Extract defined markdown file blocks from Apex research outputs.

This script intentionally treats source block bodies as bytes. It copies the
bytes between the outer fenced block markers without normalizing line endings,
encoding, spacing, or Markdown content.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = (
    REPO_ROOT
    / "FutureDevelopments&Research"
    / "ProjectMM&Task&KB"
    / "DeepResearch-File&Process"
    / "3rdIteration_ProThinking"
)

SOURCES = {
    "dr": SOURCE_DIR / "DR_Apex_Plan.md",
    "pro": SOURCE_DIR / "Prothinking_Apex_Plan.md",
}

EXPECTED_TARGET_COUNT = 7
REPORT_PATH = REPO_ROOT / ".claude" / "skills" / "apex-plan" / "extraction-report.md"
PACKAGE_ROOT = REPO_ROOT / ".claude" / "skills" / "apex-plan"


@dataclass(frozen=True)
class Block:
    variant: str
    source_path: Path
    target_path: Path
    content: bytes
    source_block_start: int
    source_block_end: int


@dataclass(frozen=True)
class Action:
    kind: str
    path: Path
    content: bytes | None
    source_hash: str | None
    note: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def repo_relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def output_variant_path(target_path: Path, variant: str) -> Path:
    if target_path.suffix != ".md":
        raise ValueError(f"Target is not a Markdown file: {repo_relative(target_path)}")
    return target_path.with_name(f"{target_path.stem}.{variant}{target_path.suffix}")


def resolve_target(raw_target: bytes) -> Path:
    target_text = raw_target.decode("utf-8")
    if "\\" in target_text:
        raise ValueError(f"Backslash is not allowed in target path: {target_text}")
    candidate = (REPO_ROOT / target_text).resolve()
    if not candidate.is_relative_to(REPO_ROOT):
        raise ValueError(f"Target escapes repository root: {target_text}")
    if candidate.suffix != ".md":
        raise ValueError(f"Target must end in .md: {target_text}")
    return candidate


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
        if line.endswith(b"\r"):
            line_without_cr = line[:-1]
        else:
            line_without_cr = line

        if line_without_cr.strip() == b"```":
            content_end = line_start
            if content_end > content_start and data[content_end - 1 : content_end] == b"\n":
                content_end -= 1
                if content_end > content_start and data[content_end - 1 : content_end] == b"\r":
                    content_end -= 1
            return content_start, content_end, next_line_start

        line_start = next_line_start

    raise ValueError("Missing closing fenced markdown block")


def parse_dr(source_path: Path) -> list[Block]:
    data = source_path.read_bytes()
    heading_re = re.compile(br"\*\*File\s+[^`\r\n]+`(?P<target>[^`]+)`\*\*")
    blocks: list[Block] = []

    for match in heading_re.finditer(data):
        target_path = resolve_target(match.group("target"))
        content_start, content_end, _ = find_outer_fenced_content(data, match.end())
        blocks.append(
            Block(
                variant="dr",
                source_path=source_path,
                target_path=target_path,
                content=data[content_start:content_end],
                source_block_start=content_start,
                source_block_end=content_end,
            )
        )

    return blocks


def parse_pro(source_path: Path) -> list[Block]:
    data = source_path.read_bytes()
    target_re = re.compile(
        br"(?im)^##[ \t]*(?:\d+\.[ \t]*)?Target path[ \t]*\r?\n"
        br"[ \t]*\r?\n"
        br"`(?P<target>[^`]+)`[ \t]*\r?\n"
        br"[ \t]*\r?\n"
        br"##[ \t]*Complete file content[ \t]*\r?\n"
        br"[ \t]*\r?\n"
    )
    blocks: list[Block] = []

    for match in target_re.finditer(data):
        target_path = resolve_target(match.group("target"))
        content_start, content_end, _ = find_outer_fenced_content(data, match.end())
        blocks.append(
            Block(
                variant="pro",
                source_path=source_path,
                target_path=target_path,
                content=data[content_start:content_end],
                source_block_start=content_start,
                source_block_end=content_end,
            )
        )

    return blocks


def validate_blocks(blocks_by_variant: dict[str, list[Block]]) -> None:
    expected_targets: set[Path] | None = None
    for variant, blocks in blocks_by_variant.items():
        if len(blocks) != EXPECTED_TARGET_COUNT:
            raise ValueError(
                f"{variant} source yielded {len(blocks)} blocks; "
                f"expected {EXPECTED_TARGET_COUNT}"
            )
        targets = [block.target_path for block in blocks]
        duplicate_targets = sorted({target for target in targets if targets.count(target) > 1})
        if duplicate_targets:
            rendered = ", ".join(repo_relative(path) for path in duplicate_targets)
            raise ValueError(f"{variant} source contains duplicate target paths: {rendered}")
        target_set = set(targets)
        if expected_targets is None:
            expected_targets = target_set
        elif target_set != expected_targets:
            missing = sorted(expected_targets - target_set)
            extra = sorted(target_set - expected_targets)
            raise ValueError(
                f"{variant} target set differs; "
                f"missing={[repo_relative(path) for path in missing]}, "
                f"extra={[repo_relative(path) for path in extra]}"
            )


def plan_actions(blocks_by_variant: dict[str, list[Block]]) -> list[Action]:
    actions: list[Action] = []

    existing_markdown = sorted(PACKAGE_ROOT.rglob("*.md"), key=lambda path: repo_relative(path).lower())
    for existing_path in existing_markdown:
        if existing_path == REPORT_PATH:
            continue
        if existing_path.stem.endswith((".v1", ".dr", ".pro")):
            continue
        v1_path = output_variant_path(existing_path, "v1")
        canonical_bytes = existing_path.read_bytes()
        canonical_hash = sha256_bytes(canonical_bytes)
        if v1_path.exists():
            existing = v1_path.read_bytes()
            if existing != canonical_bytes:
                raise ValueError(f"Existing v1 differs from source file: {repo_relative(v1_path)}")
            actions.append(
                Action(
                    kind="skip",
                    path=v1_path,
                    content=None,
                    source_hash=canonical_hash,
                    note=f"v1 already matches existing file {repo_relative(existing_path)}",
                )
            )
        else:
            actions.append(
                Action(
                    kind="write",
                    path=v1_path,
                    content=canonical_bytes,
                    source_hash=canonical_hash,
                    note=f"copy existing file {repo_relative(existing_path)}",
                )
            )

    for variant in ("dr", "pro"):
        for block in blocks_by_variant[variant]:
            out_path = output_variant_path(block.target_path, variant)
            block_hash = sha256_bytes(block.content)
            if out_path.exists():
                existing = out_path.read_bytes()
                if existing != block.content:
                    raise ValueError(
                        f"Existing variant differs from extracted source: {repo_relative(out_path)}"
                    )
                actions.append(
                    Action(
                        kind="skip",
                        path=out_path,
                        content=None,
                        source_hash=block_hash,
                        note=f"{variant} variant already matches extracted block",
                    )
                )
            else:
                actions.append(
                    Action(
                        kind="write",
                        path=out_path,
                        content=block.content,
                        source_hash=block_hash,
                        note=f"write {variant} extracted block",
                    )
                )

    return actions


def apply_actions(actions: list[Action]) -> None:
    for action in actions:
        if action.kind != "write":
            continue
        if action.content is None or action.source_hash is None:
            raise ValueError(f"Write action has no content: {repo_relative(action.path)}")
        action.path.parent.mkdir(parents=True, exist_ok=True)
        action.path.write_bytes(action.content)
        written = action.path.read_bytes()
        written_hash = sha256_bytes(written)
        if written_hash != action.source_hash:
            raise ValueError(
                f"Verification failed for {repo_relative(action.path)}: "
                f"expected {action.source_hash}, got {written_hash}"
            )


def render_report(blocks_by_variant: dict[str, list[Block]], actions: list[Action]) -> bytes:
    lines: list[str] = [
        "# apex-plan Extraction Report",
        "",
        "Generated by `scripts/extract_defined_markdown_blocks.py`.",
        "",
        "## Sources",
        "",
    ]

    for variant in ("dr", "pro"):
        source = SOURCES[variant]
        lines.append(f"- `{variant}`: `{repo_relative(source)}`")
        lines.append(f"  - source_sha256: `{sha256_bytes(source.read_bytes())}`")
        lines.append(f"  - extracted_blocks: `{len(blocks_by_variant[variant])}`")

    lines.extend(["", "## Extracted Blocks", ""])
    for variant in ("dr", "pro"):
        for block in blocks_by_variant[variant]:
            lines.append(f"- `{variant}` -> `{repo_relative(output_variant_path(block.target_path, variant))}`")
            lines.append(f"  - logical_target: `{repo_relative(block.target_path)}`")
            lines.append(f"  - bytes: `{len(block.content)}`")
            lines.append(f"  - sha256: `{sha256_bytes(block.content)}`")

    lines.extend(["", "## Actions", ""])
    for action in actions:
        lines.append(f"- `{action.kind}` `{repo_relative(action.path)}`")
        lines.append(f"  - sha256: `{action.source_hash or 'n/a'}`")
        lines.append(f"  - note: {action.note}")

    lines.extend(["", "## Conflicts", "", "None.", ""])
    return ("\n".join(lines)).encode("utf-8")


def print_dry_run(blocks_by_variant: dict[str, list[Block]], actions: list[Action]) -> None:
    for variant in ("dr", "pro"):
        print(f"{variant}: {SOURCES[variant]}")
        for block in blocks_by_variant[variant]:
            out_path = output_variant_path(block.target_path, variant)
            print(
                f"  {repo_relative(block.target_path)} -> {repo_relative(out_path)} "
                f"bytes={len(block.content)} sha256={sha256_bytes(block.content)}"
            )
    print("actions:")
    for action in actions:
        print(
            f"  {action.kind.upper():5} {repo_relative(action.path)} "
            f"sha256={action.source_hash or 'n/a'} note={action.note}"
        )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="print actions without writing files")
    args = parser.parse_args(argv)

    blocks_by_variant = {
        "dr": parse_dr(SOURCES["dr"]),
        "pro": parse_pro(SOURCES["pro"]),
    }
    validate_blocks(blocks_by_variant)
    actions = plan_actions(blocks_by_variant)

    if args.dry_run:
        print_dry_run(blocks_by_variant, actions)
        return 0

    apply_actions(actions)
    report_bytes = render_report(blocks_by_variant, actions)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_bytes(report_bytes)
    written_report = REPORT_PATH.read_bytes()
    if sha256_bytes(written_report) != sha256_bytes(report_bytes):
        raise ValueError(f"Verification failed for report: {repo_relative(REPORT_PATH)}")
    print_dry_run(blocks_by_variant, actions)
    print(f"report: {repo_relative(REPORT_PATH)} sha256={sha256_bytes(report_bytes)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
