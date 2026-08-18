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
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(REPO_ROOT / ".claude" / "skills" / "transcript-to-knowledge" / "scripts"))

from receipt import ExecutionReceipt, write_atomic_receipt, utc_now_iso
from adapters.semantic_cli import SemanticCLIWorker, ProviderUnavailableError, SemanticExecutionError


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
    # Look for transcript.json in sibling/parent directories
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
    # Fall back to segments embedded in packet if present
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
