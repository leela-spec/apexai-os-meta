"""
Run real subscription-CLI smoke test for Checkpoint B.
Executes Claude Code CLI on a representative TTK Map packet with sanitized environment,
performs TTK validation, captures raw output and execution receipt,
and probes Codex and Antigravity availability honestly.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts" / "transcript_pipeline_v2"))
sys.path.insert(0, str(REPO_ROOT / ".claude" / "skills" / "transcript-to-knowledge" / "scripts"))

import ttk
import ttk_map
from adapters.semantic_cli import SemanticCLIWorker, get_sanitized_env
from receipt import ExecutionReceipt, write_atomic_receipt, utc_now_iso


def run_cli_smoke():
    corrective_root = REPO_ROOT / "artifacts" / "transcript_pipeline_v2" / "corrective-run"
    raw_smoke_dir = corrective_root / "raw" / "cli-smoke"
    smoke_receipts_dir = corrective_root / "receipts" / "smoke"
    raw_smoke_dir.mkdir(parents=True, exist_ok=True)
    smoke_receipts_dir.mkdir(parents=True, exist_ok=True)

    print("=== Checkpoint B: Proving Real Subscription CLI Execution ===")

    # 1. Probe Codex and Antigravity honestly
    for provider, cmd_name in [("codex", "codex"), ("antigravity", "agy")]:
        receipt_path = smoke_receipts_dir / f"{provider}.json"
        which_path = shutil.which(cmd_name)
        if not which_path:
            write_atomic_receipt(receipt_path, {
                "schema": "ttk.receipt.v2",
                "component_id": provider,
                "provider": provider,
                "command": cmd_name,
                "installed": False,
                "status": "BLOCKED_FOR_TRIAL1",
                "reason": f"{cmd_name} CLI executable not found in PATH",
                "evaluated_at": utc_now_iso()
            })
            print(f"[{provider.upper()}] Status: BLOCKED_FOR_TRIAL1 ({cmd_name} not on PATH)")
        else:
            print(f"[{provider.upper()}] Found executable at {which_path}")

    # 2. Verify Claude Code CLI
    claude_which = shutil.which("claude")
    if not claude_which:
        print("[FAIL] claude CLI executable not found on PATH!")
        sys.exit(1)
    print(f"[CLAUDE] Found executable at: {claude_which}")

    # Verify environment sanitization
    env = get_sanitized_env()
    for forbidden_key in ["ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "OPENAI_API_KEY", "GEMINI_API_KEY"]:
        if forbidden_key in env:
            print(f"[FAIL] Child environment leaked {forbidden_key}!")
            sys.exit(1)
    print("[CLAUDE] Child process environment sanitization verified: 0 API keys in child environment.")

    # 3. Create a representative TTK packet from CygwqaNg2PY transcript
    transcript_path = REPO_ROOT / ".claude" / "skills" / "SourceTranscriptionAnalysisPipeline" / "artifacts" / "transcripts" / "CygwqaNg2PY" / "CygwqaNg2PY.srt"
    
    with tempfile.TemporaryDirectory(prefix="ttk_smoke_") as tmpdir:
        tmp_path = Path(tmpdir)
        manifest = ttk.init_run(
            transcript_path,
            tmp_path,
            target_words=1100,
            min_words=700,
            max_words=1500,
            block_segments=4,
            pause_weight=0.15,
            context_segments=1
        )
        packet_path = tmp_path / "work" / "packets" / "map" / "window-0001.json"
        packet = ttk.read_json(packet_path)
        lookup = ttk._segment_lookup(tmp_path)

        # 4. Invoke Claude worker on window-0001
        print("[CLAUDE] Invoking real Claude Code CLI on CygwqaNg2PY window-0001...")
        worker = SemanticCLIWorker(provider="claude", timeout_seconds=120)
        
        receipt_path = smoke_receipts_dir / "claude.json"
        result = worker.execute_map(packet, lookup, receipt_path=receipt_path)

        # 5. Verify result and save raw artifact
        raw_output_path = raw_smoke_dir / "claude_map_smoke.json"
        with open(raw_output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        val_errors = ttk_map.validate_map_result(packet, result, lookup)
        if val_errors:
            print(f"[FAIL] TTK validation failed for smoke Map result: {val_errors}")
            sys.exit(1)

        print(f"[PASS] Claude Map smoke output is valid. Result saved to: {raw_output_path}")
        print(f"[PASS] Receipt saved to: {receipt_path}")


if __name__ == "__main__":
    run_cli_smoke()
