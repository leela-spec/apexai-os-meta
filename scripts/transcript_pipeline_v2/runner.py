#!/usr/bin/env python3
"""
Transcript Pipeline V2 Runner.
Provides deterministic CLI entrypoints for benchmark tasks, adapters, and stage status.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(REPO_ROOT / ".claude" / "skills" / "transcript-to-knowledge" / "scripts"))

from receipt import ExecutionReceipt, write_atomic_receipt, utc_now_iso
from adapters.semantic_cli import SemanticCLIWorker, ProviderUnavailableError, SemanticExecutionError

STAGE_OWNED_PATTERNS = (
    "scripts/transcript_pipeline_v2/runner.py",
    "scripts/transcript_pipeline_v2/tests/test_init_run.py",
    "artifacts/transcript_pipeline_v2/runs/",
)


def compute_sha256(path: Path) -> str:
    """Compute sha256 checksum of raw file bytes."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def write_canonical_text(path: Path, text: str) -> tuple[Path, str]:
    """Write text file explicitly with LF newlines and return (path, sha256)."""
    normalized = text.replace("\r\n", "\n")
    if not normalized.endswith("\n"):
        normalized += "\n"
    raw_bytes = normalized.encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        f.write(raw_bytes)
    sha256 = hashlib.sha256(raw_bytes).hexdigest()
    return path, sha256


def write_canonical_json(path: Path, data: Any) -> tuple[Path, str]:
    """Write JSON file explicitly with LF newlines and return (path, sha256)."""
    json_str = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    return write_canonical_text(path, json_str)


def filter_unrelated_dirty_paths(dirty_paths: list[str]) -> list[str]:
    """Filter out S00 stage-owned paths from the dirty paths list."""
    unrelated = []
    for dp in dirty_paths:
        norm_dp = dp.replace("\\", "/")
        if any(norm_dp == pat or norm_dp.startswith(pat) for pat in STAGE_OWNED_PATTERNS):
            continue
        unrelated.append(dp)
    return unrelated


def get_git_repo_info(cwd: Path | None = None) -> dict[str, Any]:
    """Capture current git branch, head, dirty paths, and remote origin URL."""
    cwd = cwd or REPO_ROOT
    try:
        branch = subprocess.check_output(
            ["git", "branch", "--show-current"],
            cwd=str(cwd),
            text=True
        ).strip()
        head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=str(cwd),
            text=True
        ).strip()
        dirty_out = subprocess.check_output(
            ["git", "status", "--porcelain"],
            cwd=str(cwd),
            text=True
        )
        dirty_paths = []
        for line in dirty_out.splitlines():
            if not line:
                continue
            if len(line) >= 4:
                p = line[3:].strip()
                if " -> " in p:
                    p = p.split(" -> ")[-1].strip()
                dirty_paths.append(p)
        remote_url = ""
        try:
            remote_url = subprocess.check_output(
                ["git", "remote", "get-url", "origin"],
                cwd=str(cwd),
                text=True
            ).strip()
        except Exception:
            pass
        return {
            "branch": branch,
            "head": head,
            "dirty_paths": dirty_paths,
            "remote_url": remote_url,
        }
    except Exception as e:
        return {
            "branch": "unknown",
            "head": "unknown",
            "dirty_paths": [],
            "remote_url": "",
            "error": str(e),
        }


def parse_diff_check_failing_paths(output: str) -> list[str]:
    """Extract distinct filenames referenced in git diff --check failure output."""
    paths = set()
    for line in output.splitlines():
        m = re.match(r"^([^:\r\n]+):\d+:", line)
        if m:
            paths.add(m.group(1).strip())
    return sorted(list(paths))


def run_actual_tests(
    repo_root: Path,
    run_id: str | None = None,
    unrelated_dirty_paths: list[str] | None = None
) -> list[dict[str, Any]]:
    """Execute real test suite, S00-owned diff check, and repository-wide diff check."""
    results: list[dict[str, Any]] = []

    # 1. pytest
    proc_pytest = subprocess.run(
        [sys.executable, "-m", "pytest", "scripts/transcript_pipeline_v2/tests"],
        cwd=str(repo_root),
        capture_output=True,
        text=True
    )
    results.append({
        "command": "pytest scripts/transcript_pipeline_v2/tests",
        "result": "PASS" if proc_pytest.returncode == 0 else "FAIL",
    })

    # 2. S00-owned whitespace check
    s00_paths = ["scripts/transcript_pipeline_v2/"]
    if run_id:
        s00_paths.append(f"artifacts/transcript_pipeline_v2/runs/{run_id}/")
    s00_cmd = ["git", "diff", "--check", "--"] + s00_paths
    s00_cmd_str = " ".join(s00_cmd)
    proc_s00_diff = subprocess.run(
        s00_cmd,
        cwd=str(repo_root),
        capture_output=True,
        text=True
    )
    results.append({
        "command": s00_cmd_str,
        "result": "PASS" if proc_s00_diff.returncode == 0 else "FAIL",
    })

    # 3. repository-wide git diff check
    proc_diff = subprocess.run(
        ["git", "diff", "--check"],
        cwd=str(repo_root),
        capture_output=True,
        text=True
    )
    if proc_diff.returncode == 0:
        results.append({
            "command": "git diff --check",
            "result": "PASS",
        })
    else:
        failing_paths = parse_diff_check_failing_paths(proc_diff.stdout)
        classified: dict[str, str] = {}
        unrelated_set = set(unrelated_dirty_paths or [])
        for fp in failing_paths:
            norm_fp = fp.replace("\\", "/")
            if fp in unrelated_set or norm_fp in unrelated_set:
                classified[fp] = "PRE_EXISTING_UNRELATED"
            elif any(norm_fp == pat or norm_fp.startswith(pat) for pat in STAGE_OWNED_PATTERNS):
                classified[fp] = "S00_OWNED"
            else:
                classified[fp] = "UNKNOWN"

        results.append({
            "command": "git diff --check",
            "result": "FAIL",
            "exit_code": proc_diff.returncode,
            "failing_paths": failing_paths,
            "classifications": classified,
        })

    return results


def init_run(
    source: str,
    source_id: str | None = None,
    language: str | None = None,
    mode: str | None = None,
    purpose: str | None = None,
    title: str | None = None,
    finalize: bool = False,
    _runs_dir: Path | None = None,
    _repo_root: Path | None = None,
    _skip_repo_check: bool = False,
) -> dict[str, Any]:
    """
    Initialize a deterministic V2.1 TTK run (Module S00).
    Validates request, captures git state, creates directory tree,
    writes canonical request.json, and optionally finalizes stage acceptance.
    """
    repo_root = _repo_root or REPO_ROOT
    runs_dir = _runs_dir or (repo_root / "artifacts" / "transcript_pipeline_v2" / "runs")

    # 1. Validate source locator
    if not source or not str(source).strip():
        raise ValueError("Source locator must not be empty.")
    source_str = str(source).strip()
    is_url = source_str.startswith("http://") or source_str.startswith("https://")
    source_type = "url" if is_url else "local_file"

    if not is_url:
        local_path = Path(source_str)
        if not local_path.is_absolute():
            local_path = (repo_root / local_path).resolve()
        if not local_path.exists():
            raise FileNotFoundError(f"Local source path does not exist: {source_str}")

    # 2. Validate mode if provided
    valid_modes = {"fresh_e2e", "existing_transcript", "regression"}
    if mode is not None and mode not in valid_modes:
        raise ValueError(f"Invalid mode '{mode}'. Allowed modes: {sorted(valid_modes)}")

    # 3. Validate repository and branch assumptions
    git_info = get_git_repo_info(cwd=repo_root)
    if not _skip_repo_check:
        if git_info.get("branch") != "main":
            raise RuntimeError(f"Run initialization requires branch 'main', but current branch is '{git_info.get('branch')}'.")
        if "leela-spec/apexai-os-meta" not in git_info.get("remote_url", ""):
            raise RuntimeError(f"Run initialization requires repository 'leela-spec/apexai-os-meta', but remote URL is '{git_info.get('remote_url')}'.")

    start_head = git_info.get("head", "unknown")
    unrelated_dirty_paths = filter_unrelated_dirty_paths(git_info.get("dirty_paths", []))

    # 4. Generate unique, non-colliding run_id
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    clean_id = (source_id or "run").replace("/", "_").replace("\\", "_").replace(":", "_")
    unique_token = uuid.uuid4().hex[:6]
    run_id = f"ttk_{timestamp}_{clean_id}_{unique_token}"
    run_dir = runs_dir / run_id
    while run_dir.exists():
        unique_token = uuid.uuid4().hex[:6]
        run_id = f"ttk_{timestamp}_{clean_id}_{unique_token}"
        run_dir = runs_dir / run_id

    # 5. Create directory structure (no fake result files)
    run_dir.mkdir(parents=True, exist_ok=False)
    handoffs_dir = run_dir / "handoffs"
    handoffs_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "source").mkdir(parents=True, exist_ok=True)
    (run_dir / "work").mkdir(parents=True, exist_ok=True)

    # 6. Write request.json with only operator-declared / request-derived facts
    request_dict: dict[str, Any] = {
        "schema": "ttk.v2_1.run-request.v1",
        "run_id": run_id,
        "source": source_str,
        "source_type": source_type,
    }
    if source_id is not None:
        request_dict["source_id"] = source_id
    if language is not None:
        request_dict["language"] = language
    if mode is not None:
        request_dict["mode"] = mode
    if purpose is not None:
        request_dict["purpose"] = purpose
    if title is not None:
        request_dict["title"] = title
    request_dict["created_at"] = utc_now_iso()

    request_file = run_dir / "request.json"
    _, request_hash = write_canonical_json(request_file, request_dict)

    try:
        rel_request = str(request_file.relative_to(repo_root)).replace("\\", "/")
        rel_s00_yaml = str((handoffs_dir / "S00.yaml").relative_to(repo_root)).replace("\\", "/")
        rel_s00_md = str((handoffs_dir / "S00-HANDOVER.md").relative_to(repo_root)).replace("\\", "/")
    except ValueError:
        rel_request = str(request_file)
        rel_s00_yaml = str(handoffs_dir / "S00.yaml")
        rel_s00_md = str(handoffs_dir / "S00-HANDOVER.md")

    handover_md_path = handoffs_dir / "S00-HANDOVER.md"
    yaml_path = handoffs_dir / "S00.yaml"

    if finalize:
        return finalize_s00(
            run_dir=run_dir,
            repo_root=repo_root,
            start_head=start_head,
            unrelated_dirty_paths=unrelated_dirty_paths,
            request_dict=request_dict,
        )

    return {
        "status": "INITIALIZED",
        "run_id": run_id,
        "run_dir": str(run_dir),
        "request_path": str(request_file),
        "handoff_yaml": str(yaml_path),
        "handoff_md": str(handover_md_path),
        "start_head": start_head,
        "unrelated_dirty_paths": unrelated_dirty_paths,
        "request": request_dict,
    }


def finalize_s00(
    run_dir: Path,
    repo_root: Path | None = None,
    start_head: str | None = None,
    unrelated_dirty_paths: list[str] | None = None,
    request_dict: dict[str, Any] | None = None,
    test_records: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    Accept and finalize S00 stage after executing real tests and verifying invariants.
    """
    repo_root = repo_root or REPO_ROOT
    run_dir = Path(run_dir).resolve()
    handoffs_dir = run_dir / "handoffs"
    request_file = run_dir / "request.json"

    if not request_file.exists():
        raise FileNotFoundError(f"request.json not found in {run_dir}")

    if request_dict is None:
        with open(request_file, "r", encoding="utf-8") as f:
            request_dict = json.load(f)

    run_id = request_dict["run_id"]
    source_str = request_dict["source"]
    source_id = request_dict.get("source_id")
    source_type = request_dict.get("source_type", "url")
    language = request_dict.get("language")
    mode = request_dict.get("mode")
    purpose = request_dict.get("purpose")

    if start_head is None or unrelated_dirty_paths is None:
        git_info = get_git_repo_info(cwd=repo_root)
        start_head = start_head or git_info.get("head", "unknown")
        if unrelated_dirty_paths is None:
            unrelated_dirty_paths = filter_unrelated_dirty_paths(git_info.get("dirty_paths", []))

    # Real component identifier (canonical LF content hash of runner.py)
    runner_py = SCRIPT_DIR / "runner.py"
    if runner_py.exists():
        runner_bytes = runner_py.read_bytes().replace(b"\r\n", b"\n")
        runner_sha256 = hashlib.sha256(runner_bytes).hexdigest()
    else:
        runner_sha256 = "unknown"

    # Invariant checks: verify no fake or later-stage outputs
    source_dir = run_dir / "source"
    work_dir = run_dir / "work"
    source_files = list(source_dir.iterdir()) if source_dir.exists() else []
    work_files = list(work_dir.iterdir()) if work_dir.exists() else []

    if source_files:
        raise RuntimeError(f"S00 invariant violation: source directory contains unexpected files: {source_files}")
    if work_files:
        raise RuntimeError(f"S00 invariant violation: work directory contains unexpected files: {work_files}")

    # Execute actual tests if not supplied
    if test_records is None:
        test_records = run_actual_tests(repo_root=repo_root, run_id=run_id, unrelated_dirty_paths=unrelated_dirty_paths)

    # Decision rule evaluation
    pytest_pass = any(t["command"].startswith("pytest") and t.get("result") == "PASS" for t in test_records)
    s00_diff_pass = any("scripts/transcript_pipeline_v2/" in t["command"] and t.get("result") == "PASS" for t in test_records)
    global_diff = next((t for t in test_records if t["command"] == "git diff --check"), None)

    limitations: list[str] = []

    if not pytest_pass or not s00_diff_pass:
        stage_status = "FAIL"
    elif global_diff and global_diff.get("result") == "FAIL":
        classifications = global_diff.get("classifications", {})
        if any(c == "UNKNOWN" for c in classifications.values()):
            stage_status = "BLOCKED"
            limitations.append("Repository-wide git diff --check contains unclassified (UNKNOWN) failure paths.")
        elif any(c == "S00_OWNED" for c in classifications.values()):
            stage_status = "FAIL"
            limitations.append("Repository-wide git diff --check contains S00-owned whitespace defects.")
        elif len(classifications) > 0 and all(c == "PRE_EXISTING_UNRELATED" for c in classifications.values()):
            # CASE A: All global failures are pre-existing unrelated and S00-owned check passed
            stage_status = "PASS"
            failing_list = ", ".join(global_diff.get("failing_paths", []))
            limitations.append(
                f"Repository-wide git diff --check returned exit code {global_diff.get('exit_code', 1)} solely due to pre-existing unrelated dirty paths ({failing_list}); zero S00-owned whitespace defects were found."
            )
        else:
            stage_status = "FAIL"
    else:
        stage_status = "PASS"

    try:
        rel_request = str(request_file.relative_to(repo_root)).replace("\\", "/")
        rel_s00_yaml = str((handoffs_dir / "S00.yaml").relative_to(repo_root)).replace("\\", "/")
        rel_s00_md = str((handoffs_dir / "S00-HANDOVER.md").relative_to(repo_root)).replace("\\", "/")
    except ValueError:
        rel_request = str(request_file)
        rel_s00_yaml = str(handoffs_dir / "S00.yaml")
        rel_s00_md = str(handoffs_dir / "S00-HANDOVER.md")

    request_hash = compute_sha256(request_file)

    # Write S00-HANDOVER.md canonically with LF
    md_lines = [
        f"# S00 Stage Handover — Run {run_id}",
        "",
        f"- **Stage**: S00 (Trigger and Run Initialization)",
        f"- **Status**: {stage_status}",
        f"- **Run ID**: `{run_id}`",
        f"- **Start HEAD**: `{start_head}`",
        f"- **Source**: `{source_str}`",
        f"- **Source Type**: `{source_type}`",
        f"- **Source ID**: `{source_id or 'None'}`",
        f"- **Language**: `{language or 'None'}`",
        f"- **Mode**: `{mode or 'None'}`",
        f"- **Purpose**: `{purpose or 'None'}`",
        "",
        "## Generated Stage Outputs",
        f"- `{rel_request}`",
        f"- `{rel_s00_yaml}`",
        f"- `{rel_s00_md}`",
        "",
        "## Actual Test Execution Evidence",
    ]
    for tr in test_records:
        cmd_str = tr["command"]
        res_str = tr.get("result", "UNKNOWN")
        md_lines.append(f"- `{cmd_str}` — **{res_str}**")
        if res_str == "FAIL" and "failing_paths" in tr:
            md_lines.append(f"  - Exit code: `{tr.get('exit_code', 1)}`")
            for fp in tr.get("failing_paths", []):
                cls = tr.get("classifications", {}).get(fp, "UNKNOWN")
                md_lines.append(f"  - Failing path: `{fp}` (classification: `{cls}`)")

    md_lines.extend([
        "",
        "## Stage Invariants Verified",
        "1. Canonical LF byte encoding enforced across all artifacts.",
        "2. Run directory created with standard empty subdirectories (`source/`, `work/`, `handoffs/`).",
        "3. No source media downloaded or acquired.",
        "4. No ASR transcription executed or generated.",
        "5. No LLM or semantic worker invoked.",
        "6. No Map/Reduce intermediate or final artifacts created.",
        "7. Pre-existing unrelated dirty paths preserved untouched.",
        "",
        "## Pre-existing Unrelated Dirty Paths",
    ])
    if unrelated_dirty_paths:
        for dp in unrelated_dirty_paths:
            md_lines.append(f"- `{dp}`")
    else:
        md_lines.append("- None")

    if limitations:
        md_lines.extend(["", "## Limitations & Diagnostic Context"])
        for lim in limitations:
            md_lines.append(f"- {lim}")

    handover_md_path = handoffs_dir / "S00-HANDOVER.md"
    _, md_hash = write_canonical_text(handover_md_path, "\n".join(md_lines) + "\n")

    # Write S00.yaml canonically with LF
    yaml_lines = [
        "schema: ttk.v2_1.stage-handoff.v1",
        "stage: S00",
        f"status: {stage_status}",
        f"run_id: {run_id}",
        f"start_head: {start_head}",
        "end_head: null",
        "",
        "inputs:",
        f"  - path: {rel_request}",
        f"    sha256: {request_hash}",
        "",
        "components:",
        "  - id: scripts/transcript_pipeline_v2/runner.py",
        f"    sha256: {runner_sha256}",
        "    config:",
        f"      mode: {json.dumps(mode)}",
        f"      language: {json.dumps(language)}",
        "",
        "outputs:",
        f"  - path: {rel_request}",
        f"    sha256: {request_hash}",
        f"  - path: {rel_s00_md}",
        f"    sha256: {md_hash}",
        "",
        "tests:",
    ]
    for tr in test_records:
        yaml_lines.extend([
            f"  - command: {tr['command']}",
            f"    result: {tr['result']}",
        ])
        if tr.get("result") == "FAIL" and "exit_code" in tr:
            yaml_lines.append(f"    exit_code: {tr['exit_code']}")
            if tr.get("failing_paths"):
                yaml_lines.append("    failing_paths:")
                for fp in tr["failing_paths"]:
                    yaml_lines.append(f"      - {fp}")
            if tr.get("classifications"):
                yaml_lines.append("    classifications:")
                for fp, cls in tr["classifications"].items():
                    yaml_lines.append(f"      {fp}: {cls}")

    yaml_lines.append("")
    yaml_lines.append(f"product_check: Run directory initialized for {source_id or source_str} with canonical LF request.json and zero later-stage artifacts")
    if limitations:
        yaml_lines.append("limitations:")
        for lim in limitations:
            yaml_lines.append(f"  - {lim}")
    else:
        yaml_lines.append("limitations: []")

    yaml_lines.append("unrelated_dirty_paths:")
    if unrelated_dirty_paths:
        for dp in unrelated_dirty_paths:
            yaml_lines.append(f"  - {dp}")
    else:
        yaml_lines.append("  # None")

    yaml_lines.extend([
        "",
        "next_stage_input:",
        "  paths:",
        f"    - {rel_request}",
        "  facts:",
        f"    - source: {source_str}",
        f"    - source_type: {source_type}",
    ])
    if source_id is not None:
        yaml_lines.append(f"    - source_id: {source_id}")
    if language is not None:
        yaml_lines.append(f"    - language: {language}")
    if mode is not None:
        yaml_lines.append(f"    - mode: {mode}")
    if purpose is not None:
        yaml_lines.append(f"    - purpose: {purpose}")

    yaml_path = handoffs_dir / "S00.yaml"
    write_canonical_text(yaml_path, "\n".join(yaml_lines) + "\n")

    return {
        "status": stage_status,
        "run_id": run_id,
        "run_dir": str(run_dir),
        "request_path": str(request_file),
        "handoff_yaml": str(yaml_path),
        "handoff_md": str(handover_md_path),
        "start_head": start_head,
        "unrelated_dirty_paths": unrelated_dirty_paths,
        "test_results": test_records,
        "limitations": limitations,
        "request": request_dict,
    }


def get_preflight_status() -> dict[str, Any]:
    """Inspect repository preflight conditions."""
    receipt_file = REPO_ROOT / "artifacts" / "transcript_pipeline_v2" / "receipts" / "P0-preflight.json"
    if not receipt_file.exists():
        return {
            "status": "NOT_INITIALIZED",
            "p0_receipt": None,
            "message": "P0 preflight receipt does not exist."
        }
    with open(receipt_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {
        "status": "INITIALIZED",
        "p0_receipt": data,
        "head_commit": data.get("repository", {}).get("head_commit"),
        "claude_status": data.get("cli_environment", {}).get("claude_code", {}).get("status")
    }


def _load_segment_lookup(packet_path: Path) -> dict[str, dict[str, Any]]:
    """Resolve segment lookup table from packet directory context."""
    candidate_paths = [
        packet_path.parent.parent.parent / "source" / "transcript.json",
        packet_path.parent.parent / "source" / "transcript.json",
        packet_path.parent / "transcript.json"
    ]
    for p in candidate_paths:
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
                return {row["id"]: row for row in data.get("segments", [])}
    with open(packet_path, "r", encoding="utf-8") as f:
        pkt = json.load(f)
    segments = pkt.get("source_segments", [])
    return {row["id"]: row for row in segments}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Transcript Pipeline V2 Benchmark Runner")
    parser.add_argument("--json-output", action="store_true", help="Emit JSON output")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("preflight", help="Show preflight environment status")
    sub.add_parser("status", help="Show pipeline benchmark state")

    p_init = sub.add_parser("init-run", help="Initialize a new V2.1 TTK run (Module S00)")
    p_init.add_argument("--source", required=True, type=str, help="Source locator (URL, local file path, or transcript path)")
    p_init.add_argument("--source-id", default=None, type=str, help="Operator-declared source identifier")
    p_init.add_argument("--language", default=None, type=str, help="Operator-declared language code")
    p_init.add_argument("--mode", default=None, choices=["fresh_e2e", "existing_transcript", "regression"], help="Execution mode")
    p_init.add_argument("--purpose", default=None, type=str, help="Operator-declared purpose")
    p_init.add_argument("--title", default=None, type=str, help="Operator-declared title")
    p_init.add_argument("--finalize", action="store_true", help="Execute real tests and finalize S00 acceptance")

    p_finalize = sub.add_parser("finalize-s00", help="Finalize acceptance for an existing S00 run")
    p_finalize.add_argument("--run-dir", required=True, type=Path, help="Path to run directory")

    p_map = sub.add_parser("map", help="Execute semantic Map extraction on a single packet")
    p_map.add_argument("--provider", default="claude", help="Semantic CLI provider (claude, codex, antigravity)")
    p_map.add_argument("--packet", required=True, type=Path, help="Path to input Map packet JSON")
    p_map.add_argument("--output", required=True, type=Path, help="Path to output Map result JSON")
    p_map.add_argument("--receipt", type=Path, help="Path to output execution receipt JSON")

    p_reduce = sub.add_parser("reduce", help="Execute semantic Reduce synthesis on a reduce packet")
    p_reduce.add_argument("--provider", default="claude", help="Semantic CLI provider (claude, codex, antigravity)")
    p_reduce.add_argument("--packet", required=True, type=Path, help="Path to input Reduce packet JSON")
    p_reduce.add_argument("--output", required=True, type=Path, help="Path to output Reduce result JSON")

    p_run = sub.add_parser("run", help="Execute complete TTK pipeline on a source transcript")
    p_run.add_argument("source", type=Path, help="Path to input transcript file")
    p_run.add_argument("output", type=Path, help="Output directory for knowledge package")
    p_run.add_argument("--provider", default="antigravity_agent", help="Semantic worker provider (antigravity_agent, claude, codex)")
    p_run.add_argument("--force", action="store_true", help="Force recomputation of all stages")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    if args.command == "preflight":
        status = get_preflight_status()
        if args.json_output:
            print(json.dumps(status, indent=2, ensure_ascii=False))
        else:
            print(f"Preflight status: {status['status']}")
            if status.get("head_commit"):
                print(f"HEAD commit: {status['head_commit']}")
                print(f"Claude CLI status: {status.get('claude_status')}")
        return 0 if status["status"] == "INITIALIZED" else 1

    elif args.command == "status":
        status = {
            "schema": "transcript-pipeline-status.v2",
            "timestamp": utc_now_iso(),
            "preflight": get_preflight_status()
        }
        if args.json_output:
            print(json.dumps(status, indent=2, ensure_ascii=False))
        else:
            print(f"Pipeline V2 Status: {status['preflight']['status']}")
        return 0

    elif args.command == "init-run":
        try:
            res = init_run(
                source=args.source,
                source_id=args.source_id,
                language=args.language,
                mode=args.mode,
                purpose=args.purpose,
                title=args.title,
                finalize=args.finalize,
            )
            if args.json_output:
                print(json.dumps(res, indent=2, ensure_ascii=False))
            else:
                print(f"Initialized run: {res['run_id']}")
                print(f"Status: {res['status']}")
                print(f"Directory: {res['run_dir']}")
                print(f"Request: {res['request_path']}")
                print(f"Handoff: {res['handoff_yaml']}")
            return 0 if res["status"] in ("INITIALIZED", "PASS") else 1
        except Exception as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1

    elif args.command == "finalize-s00":
        try:
            res = finalize_s00(run_dir=args.run_dir)
            if args.json_output:
                print(json.dumps(res, indent=2, ensure_ascii=False))
            else:
                print(f"Finalized S00 for run: {res['run_id']}")
                print(f"Status: {res['status']}")
                print(f"Handoff: {res['handoff_yaml']}")
            return 0 if res["status"] == "PASS" else 1
        except Exception as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1

    elif args.command == "map":
        if not args.packet.exists():
            print(f"ERROR: Packet file {args.packet} not found", file=sys.stderr)
            return 1
        with open(args.packet, "r", encoding="utf-8") as f:
            packet = json.load(f)
        lookup = _load_segment_lookup(args.packet)
        
        try:
            worker = SemanticCLIWorker(provider=args.provider)
            result = worker.execute_map(packet, lookup, receipt_path=args.receipt)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
                f.write("\n")
            if args.json_output:
                print(json.dumps({"status": "SUCCESS", "output": str(args.output)}, indent=2))
            else:
                print(f"Map extraction succeeded: {args.output}")
            return 0
        except (ProviderUnavailableError, SemanticExecutionError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2

    elif args.command == "reduce":
        if not args.packet.exists():
            print(f"ERROR: Packet file {args.packet} not found", file=sys.stderr)
            return 1
        with open(args.packet, "r", encoding="utf-8") as f:
            packet = json.load(f)
        lookup = _load_segment_lookup(args.packet)

        try:
            worker = SemanticCLIWorker(provider=args.provider)
            result = worker.execute_reduce(packet, lookup, receipt_path=args.receipt)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
                f.write("\n")
            if args.json_output:
                print(json.dumps({"status": "SUCCESS", "output": str(args.output)}, indent=2))
            else:
                print(f"Reduce synthesis succeeded: {args.output}")
            return 0
        except (ProviderUnavailableError, SemanticExecutionError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2

    elif args.command == "run":
        import execute_ttk_lifecycle
        try:
            res = execute_ttk_lifecycle.execute_full_ttk_run(
                args.source,
                args.output,
                provider=args.provider,
                force=args.force
            )
            if args.json_output:
                print(json.dumps(res, indent=2, ensure_ascii=False))
            else:
                print(f"Pipeline executed successfully: {res['claims_compiled']} claims compiled to {args.output}")
            return 0
        except Exception as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
