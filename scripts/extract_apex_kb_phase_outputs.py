#!/usr/bin/env python3
"""
Extract Apex KB artifact files from malformed ChatGPT Markdown outputs.

Purpose
-------
This script reads the two raw chat-output Markdown files that contain Apex KB
Phase 1 ingest-analysis artifacts and Phase 2 minimal summary/wiki artifacts,
extracts each embedded target file, and writes it to the path declared inside
the chat output.

It is intentionally deterministic and stdlib-only. It does not perform semantic
analysis. It only parses explicit path markers and file-content sections.

Expected inputs by default, relative to --input-dir:
  - Phase1_IngestAnalysis.md
  - Phase2_MinimalSummaryLayer.md

Usage examples
--------------
Preview only:
  python extract_apex_kb_phase_outputs.py --repo-root . --input-dir .

Actually write files:
  python extract_apex_kb_phase_outputs.py --repo-root . --input-dir . --allow-write

With explicit paths:
  python extract_apex_kb_phase_outputs.py \
    --repo-root C:\\GitDev\\apexai-os-meta \
    --phase1 "C:\\path\\to\\Phase1_IngestAnalysis.md" \
    --phase2 "C:\\path\\to\\Phase2_MinimalSummaryLayer.md" \
    --allow-write
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path, PurePosixPath
from typing import Iterable, List, Optional, Sequence, Tuple

DEFAULT_PHASE1 = "Phase1_IngestAnalysis.md"
DEFAULT_PHASE2 = "Phase2_MinimalSummaryLayer.md"

# Only repo-relative paths under this prefix are expected for this task.
ALLOWED_TARGET_PREFIX = PurePosixPath("apex-meta/kb/lika-verein-taxes-accounting")


@dataclass(frozen=True)
class ExtractedArtifact:
    source_file: str
    source_kind: str
    target_path: str
    content: str
    start_line: int
    end_line: int
    sha256: str
    bytes_utf8: int


@dataclass(frozen=True)
class WriteResult:
    target_path: str
    status: str
    bytes_utf8: int
    sha256: str
    message: str


class ExtractionError(RuntimeError):
    pass


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def normalize_target_path(raw: str) -> str:
    """Normalize a declared target path to a safe repo-relative POSIX path."""
    candidate = raw.strip().strip("` ").replace("\\", "/")
    while candidate.startswith("./"):
        candidate = candidate[2:]
    parts = []
    for part in PurePosixPath(candidate).parts:
        if part in ("", "."):
            continue
        if part == "..":
            raise ExtractionError(f"Unsafe target path escapes repo root: {raw!r}")
        parts.append(part)
    if not parts:
        raise ExtractionError(f"Empty target path parsed from: {raw!r}")
    normalized = str(PurePosixPath(*parts))
    if PurePosixPath(normalized).is_absolute():
        raise ExtractionError(f"Absolute target paths are not allowed: {raw!r}")
    return normalized


def ensure_allowed_target(target_path: str, allow_any_kb: bool = False) -> None:
    pure = PurePosixPath(target_path)
    if pure.is_absolute() or ".." in pure.parts:
        raise ExtractionError(f"Unsafe target path: {target_path}")
    if allow_any_kb:
        if len(pure.parts) < 3 or pure.parts[0:3] != ("apex-meta", "kb", pure.parts[2]):
            raise ExtractionError(f"Target path is not under apex-meta/kb/<kb-slug>/: {target_path}")
        return
    allowed = ALLOWED_TARGET_PREFIX
    if not (pure == allowed or str(pure).startswith(str(allowed) + "/")):
        raise ExtractionError(
            f"Target path outside expected KB root {allowed}: {target_path}"
        )


def content_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def line_no_at_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, max(0, offset)) + 1


def strip_outer_noise(content: str) -> str:
    """Remove trailing wrapper separators/fences without touching embedded fences.

    ChatGPT outputs often close a wrapper code fence and then add a horizontal
    rule before the next FILE/Path marker. Those wrapper lines are not part of
    the intended target files. Internal fenced blocks are preserved because only
    terminal wrapper lines are removed.
    """
    content = content.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    # Remove wrapper tail blocks like:
    #   ```
    #   ---
    #   # Phase 2 stop/gate status
    # These are chat-output separators, not target-file content. Use the last
    # occurrence so normal frontmatter at the top is unaffected.
    wrapper_tail = list(re.finditer(r"(?m)^`{3,}\s*\n\s*---\s*\n", content))
    if wrapper_tail:
        content = content[: wrapper_tail[-1].start()].rstrip("\n")
    lines = content.split("\n")

    changed = True
    while changed:
        changed = False
        while lines and lines[-1].strip() == "":
            lines.pop()
            changed = True
        if lines and re.fullmatch(r"`{3,}\s*", lines[-1].strip()):
            # Remove a terminal code fence only when it appears to be an
            # unmatched wrapper close. If fence-line count is even, the final
            # fence probably closes a real code block inside the target file.
            fence_count = sum(1 for line in lines if re.fullmatch(r"`{3,}.*", line.strip()))
            if fence_count % 2 == 1:
                lines.pop()
                changed = True
                continue
        if lines and re.fullmatch(r"-{3,}\s*", lines[-1].strip()):
            lines.pop()
            changed = True
            continue
        if lines and re.fullmatch(r"#{1,6}\s+Ingest-analysis artifact\s+\d+\s*", lines[-1].strip(), flags=re.IGNORECASE):
            lines.pop()
            changed = True
            continue

    return "\n".join(lines).rstrip() + "\n"


def find_code_start_after(text: str, offset: int) -> Tuple[int, int]:
    """Return (content_start_offset, fence_line_number) after a markdown fence."""
    m = re.search(r"(?m)^`{3,}markdown\s*$", text[offset:])
    if not m:
        raise ExtractionError("Could not find markdown content fence after target path marker")
    fence_start = offset + m.start()
    fence_end = offset + m.end()
    # Start after the newline following the fence line.
    nl = text.find("\n", fence_end)
    if nl == -1:
        raise ExtractionError("Markdown fence found but no content follows it")
    return nl + 1, line_no_at_offset(text, fence_start)


def parse_phase1(path: Path, allow_any_kb: bool = False) -> List[ExtractedArtifact]:
    """Parse Phase1_IngestAnalysis.md using explicit Path: blocks.

    The source is known to contain malformed/nested code fences, so extraction
    is section-based: Path block -> next markdown fence -> next artifact header.
    """
    text = read_text(path).replace("\r\n", "\n").replace("\r", "\n")
    artifacts: List[ExtractedArtifact] = []

    # Path:\n\n```text\n<target>\n```
    path_re = re.compile(
        r"(?ms)^Path:\s*\n\s*```text\s*\n(?P<target>[^\n]+?)\s*\n```"
    )
    matches = list(path_re.finditer(text))
    if not matches:
        raise ExtractionError(f"No Phase 1 Path blocks found in {path}")

    for idx, match in enumerate(matches):
        target = normalize_target_path(match.group("target"))
        ensure_allowed_target(target, allow_any_kb=allow_any_kb)
        content_start, fence_line = find_code_start_after(text, match.end())
        next_match_start = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        # Trim the following section header if present before the next Path block.
        content_end = next_match_start
        # If the next Path block is preceded by a new artifact heading, cut at
        # that heading rather than at the Path line. This avoids leaking the
        # next section header into the previous target file.
        heading_re = re.compile(r"(?im)^#{1,6}\s+Ingest-analysis artifact\s+\d+\s*$")
        trailing = list(heading_re.finditer(text, content_start, next_match_start))
        if trailing:
            content_end = trailing[-1].start()
        raw_content = text[content_start:content_end]
        content = strip_outer_noise(raw_content)
        artifacts.append(
            ExtractedArtifact(
                source_file=str(path),
                source_kind="phase1_ingest_analysis",
                target_path=target,
                content=content,
                start_line=fence_line + 1,
                end_line=line_no_at_offset(text, next_match_start),
                sha256=content_hash(content),
                bytes_utf8=len(content.encode("utf-8")),
            )
        )
    return artifacts


def parse_phase2(path: Path, allow_any_kb: bool = False) -> List[ExtractedArtifact]:
    """Parse Phase2_MinimalSummaryLayer.md using '# FILE: `path`' markers."""
    text = read_text(path).replace("\r\n", "\n").replace("\r", "\n")
    artifacts: List[ExtractedArtifact] = []

    file_re = re.compile(r"(?m)^# FILE:\s*`(?P<target>[^`]+)`\s*$")
    matches = list(file_re.finditer(text))
    if not matches:
        raise ExtractionError(f"No Phase 2 '# FILE:' blocks found in {path}")

    for idx, match in enumerate(matches):
        target = normalize_target_path(match.group("target"))
        ensure_allowed_target(target, allow_any_kb=allow_any_kb)
        content_start, fence_line = find_code_start_after(text, match.end())
        content_end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        raw_content = text[content_start:content_end]
        content = strip_outer_noise(raw_content)
        artifacts.append(
            ExtractedArtifact(
                source_file=str(path),
                source_kind="phase2_wiki_compile",
                target_path=target,
                content=content,
                start_line=fence_line + 1,
                end_line=line_no_at_offset(text, content_end),
                sha256=content_hash(content),
                bytes_utf8=len(content.encode("utf-8")),
            )
        )
    return artifacts


def resolve_repo_path(repo_root: Path, target_path: str) -> Path:
    root = repo_root.resolve()
    final = (root / Path(*PurePosixPath(target_path).parts)).resolve()
    try:
        final.relative_to(root)
    except ValueError as exc:
        raise ExtractionError(f"Resolved path escapes repo root: {final}") from exc
    return final


def write_artifacts(
    artifacts: Sequence[ExtractedArtifact],
    repo_root: Path,
    allow_write: bool,
    overwrite: bool,
) -> List[WriteResult]:
    results: List[WriteResult] = []
    for artifact in artifacts:
        final = resolve_repo_path(repo_root, artifact.target_path)
        exists = final.exists()
        if not allow_write:
            status = "dry_run_create" if not exists else "dry_run_overwrite" if overwrite else "dry_run_skip_exists"
            results.append(
                WriteResult(
                    target_path=artifact.target_path,
                    status=status,
                    bytes_utf8=artifact.bytes_utf8,
                    sha256=artifact.sha256,
                    message=str(final),
                )
            )
            continue
        if exists and not overwrite:
            existing_hash = hashlib.sha256(final.read_bytes()).hexdigest()
            if existing_hash == artifact.sha256:
                status = "unchanged"
                message = "existing file has identical SHA-256"
            else:
                status = "skipped_exists"
                message = "target exists and --overwrite was not supplied"
            results.append(
                WriteResult(
                    target_path=artifact.target_path,
                    status=status,
                    bytes_utf8=artifact.bytes_utf8,
                    sha256=artifact.sha256,
                    message=message,
                )
            )
            continue
        final.parent.mkdir(parents=True, exist_ok=True)
        final.write_text(artifact.content, encoding="utf-8", newline="\n")
        results.append(
            WriteResult(
                target_path=artifact.target_path,
                status="written_overwrite" if exists else "written_create",
                bytes_utf8=artifact.bytes_utf8,
                sha256=artifact.sha256,
                message=str(final),
            )
        )
    return results


def build_report(artifacts: Sequence[ExtractedArtifact], results: Sequence[WriteResult]) -> str:
    lines = [
        "# Apex KB Phase Output Extraction Report",
        "",
        "## Summary",
        "",
        f"- Extracted artifacts: {len(artifacts)}",
        f"- Total UTF-8 bytes: {sum(a.bytes_utf8 for a in artifacts)}",
        "",
        "## Files",
        "",
        "| Status | Target | Bytes | SHA-256 |",
        "|---|---|---:|---|",
    ]
    by_target = {r.target_path: r for r in results}
    for artifact in artifacts:
        result = by_target.get(artifact.target_path)
        status = result.status if result else "not_processed"
        lines.append(
            f"| {status} | `{artifact.target_path}` | {artifact.bytes_utf8} | `{artifact.sha256}` |"
        )
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract Apex KB Phase 1/2 artifact files from raw chat-output Markdown."
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root where target files should be created. Default: current directory.",
    )
    parser.add_argument(
        "--input-dir",
        default=".",
        help="Directory containing Phase1_IngestAnalysis.md and Phase2_MinimalSummaryLayer.md. Default: current directory.",
    )
    parser.add_argument("--phase1", default=None, help="Explicit path to Phase1_IngestAnalysis.md")
    parser.add_argument("--phase2", default=None, help="Explicit path to Phase2_MinimalSummaryLayer.md")
    parser.add_argument(
        "--allow-write",
        action="store_true",
        help="Actually create/update files. Without this flag the script is dry-run only.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files when --allow-write is supplied.",
    )
    parser.add_argument(
        "--allow-any-kb",
        action="store_true",
        help="Allow any target under apex-meta/kb/<kb-slug>/ instead of only the expected Lika KB root.",
    )
    parser.add_argument(
        "--report",
        default="apex-meta/kb/lika-verein-taxes-accounting/log/extract-phase-outputs-report.md",
        help="Repo-relative report path. Written only with --allow-write unless --report - is used.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON summary instead of human-readable text.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    repo_root = Path(args.repo_root)
    input_dir = Path(args.input_dir)
    phase1 = Path(args.phase1) if args.phase1 else input_dir / DEFAULT_PHASE1
    phase2 = Path(args.phase2) if args.phase2 else input_dir / DEFAULT_PHASE2

    for required in (phase1, phase2):
        if not required.exists():
            raise ExtractionError(f"Input file not found: {required}")

    artifacts: List[ExtractedArtifact] = []
    artifacts.extend(parse_phase1(phase1, allow_any_kb=args.allow_any_kb))
    artifacts.extend(parse_phase2(phase2, allow_any_kb=args.allow_any_kb))

    # Catch accidental duplicate targets with different content.
    seen = {}
    for artifact in artifacts:
        old = seen.get(artifact.target_path)
        if old and old != artifact.sha256:
            raise ExtractionError(f"Duplicate target with different content: {artifact.target_path}")
        seen[artifact.target_path] = artifact.sha256

    results = write_artifacts(
        artifacts=artifacts,
        repo_root=repo_root,
        allow_write=args.allow_write,
        overwrite=args.overwrite,
    )

    report_text = build_report(artifacts, results)
    if args.report != "-":
        report_path = resolve_repo_path(repo_root, normalize_target_path(args.report))
        if args.allow_write:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(report_text, encoding="utf-8", newline="\n")

    payload = {
        "ok": True,
        "mode": "write" if args.allow_write else "dry_run",
        "repo_root": str(repo_root),
        "phase1": str(phase1),
        "phase2": str(phase2),
        "artifact_count": len(artifacts),
        "artifacts": [asdict(a) for a in artifacts],
        "results": [asdict(r) for r in results],
        "report_path": args.report,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Extracted {len(artifacts)} artifacts from Phase 1 and Phase 2 outputs.")
        print(f"Mode: {'WRITE' if args.allow_write else 'DRY RUN'}")
        print("")
        for result in results:
            print(f"{result.status:20} {result.target_path} ({result.bytes_utf8} bytes)")
        if args.report != "-":
            if args.allow_write:
                print(f"\nReport written to: {args.report}")
            else:
                print(f"\nReport path reserved: {args.report} (not written in dry-run)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ExtractionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
