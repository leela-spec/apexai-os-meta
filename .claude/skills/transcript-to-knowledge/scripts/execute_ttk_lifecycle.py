#!/usr/bin/env python3
"""
execute_ttk_lifecycle.py
Production TTK lifecycle runner.
Drives Map -> Reduce -> Verification -> Compile -> Validate with 100% evidence custody.
Uses SemanticCLIWorker for real strong-CLI semantic reasoning and fails closed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any

# Add scripts directory and V2 harness to sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(REPO_ROOT / "scripts" / "transcript_pipeline_v2"))

import ttk
from adapters.semantic_cli import SemanticCLIWorker, ProviderUnavailableError, SemanticExecutionError
from receipt import ExecutionReceipt, write_atomic_receipt, utc_now_iso


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def execute_full_ttk_run(
    source_path: Path,
    output_dir: Path,
    provider: str = "claude",
    min_checkworthiness: str = "medium",
    force: bool = False
) -> dict[str, Any]:
    """Execute complete resumable TTK lifecycle with strong-CLI semantic worker."""
    output_dir = Path(output_dir).resolve()
    source_path = Path(source_path).resolve()
    print(f"=== Starting TTK Full Lifecycle for '{source_path.name}' ===")

    # 1. Initialize run if not already initialized
    manifest_path = output_dir / "manifest.json"
    if not manifest_path.exists() or force:
        print("1. Initializing run ledger...")
        manifest = ttk.init_run(
            source_path,
            output_dir,
            target_words=1100,
            min_words=700,
            max_words=1500,
            block_segments=4,
            pause_weight=0.15,
            context_segments=1
        )
    else:
        manifest = ttk.read_json(manifest_path)
        print(f"1. Resuming existing run ledger ({manifest['window_count']} windows)...")

    # Segment lookup table
    lookup = ttk._segment_lookup(output_dir)
    receipts_dir = output_dir / "work" / "receipts"
    receipts_dir.mkdir(parents=True, exist_ok=True)

    # 2. Process all Map packets
    packet_dir = output_dir / "work" / "packets" / "map"
    result_map_dir = output_dir / "work" / "results" / "map"
    result_map_dir.mkdir(parents=True, exist_ok=True)

    packets = sorted(packet_dir.glob("window-*.json"))
    print(f"2. Processing {len(packets)} Map packets with semantic worker ({provider})...")

    worker = SemanticCLIWorker(provider=provider)

    for ppath in packets:
        rpath = result_map_dir / ppath.name
        packet = ttk.read_json(ppath)
        receipt_path = receipts_dir / f"map_{ppath.stem}.json"

        # Check if current result is valid and fresh
        if rpath.exists() and not force:
            try:
                res = ttk.read_json(rpath)
                errors = ttk.validate_map_result(packet, res, lookup)
                if not errors:
                    # Valid existing result, skip invocation
                    continue
            except Exception:
                pass

        print(f"   Invoking Map worker on {ppath.name}...")
        result = worker.execute_map(packet, lookup, receipt_path=receipt_path)
        write_json(rpath, result)

    # 3. Validate Map stage
    print("3. Validating Map stage...")
    map_validation = ttk.validate_maps(output_dir)
    if map_validation["invalid"] > 0 or map_validation["missing"] > 0:
        raise SemanticExecutionError(f"Map stage incomplete: {map_validation}")
    print(f"   All {map_validation['valid']} Map results VALID.")

    # 4. Create Reduce packet
    print("4. Creating Reduce packet...")
    reduce_packet = ttk.make_reduce_packet(output_dir)
    reduce_packet_path = output_dir / "work" / "packets" / "reduce.json"

    # 5. Generate Reduce result
    reduce_result_path = output_dir / "work" / "results" / "reduce.json"
    reduce_receipt_path = receipts_dir / "reduce.json"

    need_reduce = True
    if reduce_result_path.exists() and not force:
        try:
            curr_reduce = ttk.read_json(reduce_result_path)
            errors = ttk.validate_reduce_result(reduce_packet, curr_reduce, lookup)
            if not errors:
                need_reduce = False
                print("   Existing Reduce result VALID and fresh, skipping invocation.")
        except Exception:
            pass

    if need_reduce:
        print("5. Generating full-coverage Reduce result...")
        reduce_result = worker.execute_reduce(reduce_packet, lookup, receipt_path=reduce_receipt_path)
        write_json(reduce_result_path, reduce_result)

    # 6. Validate Reduce result
    print("6. Validating Reduce result...")
    reduce_validation = ttk.validate_reduce(output_dir)
    if reduce_validation["status"] != "valid":
        raise SemanticExecutionError(f"Reduce result invalid: {reduce_validation['errors']}")
    print("   Reduce result VALID.")

    # 7. Route verification queue
    print("7. Routing verification queue...")
    verify_queue = ttk.make_verify_queue(output_dir, min_checkworthiness)
    print(f"   Verification queue generated ({len(verify_queue['items'])} checkworthy claims).")

    # 8. Compile Obsidian Wiki
    print("8. Compiling Obsidian Wiki...")
    compile_result = ttk.compile_wiki(output_dir, strict=False)
    print(f"   Compiled {compile_result['claim_count']} claims into wiki at {output_dir / 'wiki'}.")

    # 9. Final Complete Validation
    print("9. Running final complete validation receipt...")
    final_validation = ttk.validate_run(output_dir)
    if not final_validation.get("ok"):
        raise SemanticExecutionError(f"Final validation failed: {final_validation}")

    print("=== TTK Full Lifecycle Completed Successfully (100% Validated) ===")
    return {
        "status": "PASS",
        "output_dir": str(output_dir),
        "windows_count": len(packets),
        "claims_compiled": compile_result["claim_count"],
        "validation": final_validation
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Execute complete TTK lifecycle")
    parser.add_argument("source", type=Path, help="Path to transcript file")
    parser.add_argument("output", type=Path, help="Output directory for TTK run")
    parser.add_argument("--provider", default="claude", help="Semantic CLI provider")
    parser.add_argument("--force", action="store_true", help="Force reprocessing of all stages")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    try:
        execute_full_ttk_run(args.source, args.output, provider=args.provider, force=args.force)
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
