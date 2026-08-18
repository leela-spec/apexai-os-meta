#!/usr/bin/env python3
"""Run-level validation, compiled freshness, status and resume state."""
from ttk_wiki import *
def validate_run(run_dir: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        manifest = read_json(run_dir / "manifest.json")
        if manifest.get("schema") != RUN_SCHEMA:
            errors.append(f"manifest schema must be {RUN_SCHEMA}")
        transcript = read_json(run_dir / "source" / "transcript.json")
        if transcript.get("source_sha256") != manifest.get("source_sha256"):
            errors.append("transcript source hash differs from manifest")
        windows = read_json(run_dir / "windows" / "index.json")
        core = [sid for win in windows.get("windows", []) for sid in win.get("core_segment_ids", [])]
        expected = [seg["id"] for seg in transcript.get("segments", [])]
        if core != expected:
            errors.append("processing windows do not provide exact ordered core coverage of transcript")
    except TTKError as exc:
        return {"schema": VALIDATION_SCHEMA, "ok": False, "errors": [str(exc)], "warnings": [], "map": None, "reduce": None, "verify": None}
    map_state = validate_maps(run_dir)
    reduce_state = validate_reduce(run_dir)
    verify_state = validate_verify_results(run_dir)
    if map_state["invalid"]:
        errors.append(f"{map_state['invalid']} map result(s) invalid")
    if reduce_state["status"] == "invalid":
        errors.append("reduce result invalid")
    if verify_state["status"] == "invalid":
        errors.append("verification results invalid")
    if map_state["missing"]:
        warnings.append(f"{map_state['missing']} map result(s) still missing")
    if reduce_state["status"] in {"packet_missing", "result_missing"}:
        warnings.append(f"reduce stage: {reduce_state['status']}")
    if verify_state["status"] in {"queue_missing", "result_missing"}:
        warnings.append(f"verification stage: {verify_state['status']}")
    compiled_path = run_dir / "wiki" / "compiled.json"
    compiled_current = False
    if compiled_path.exists() and reduce_state["status"] == "valid" and verify_state["status"] != "invalid":
        try:
            compiled = read_json(compiled_path)
            reduce_sha = file_hash(run_dir / "work" / "results" / "reduce.json")
            verify_sha = (
                file_hash(run_dir / "work" / "results" / "verify" / "results.json")
                if verify_state["status"] == "valid"
                else None
            )
            compiled_current = (
                compiled.get("reduce_result_sha256") == reduce_sha
                and compiled.get("verify_results_sha256") == verify_sha
            )
            if not compiled_current:
                warnings.append("compiled wiki is stale relative to current semantic/verification results")
        except TTKError as exc:
            errors.append(f"compiled manifest invalid: {exc}")
    elif compiled_path.exists():
        warnings.append("compiled wiki exists but upstream semantic state is not currently valid")

    complete = (
        not errors
        and map_state["missing"] == 0
        and map_state["invalid"] == 0
        and reduce_state["status"] == "valid"
        and compiled_current
    )
    report = {
        "schema": VALIDATION_SCHEMA,
        "ok": not errors,
        "complete": complete,
        "compiled_current": compiled_current,
        "errors": errors,
        "warnings": warnings,
        "map": map_state,
        "reduce": reduce_state,
        "verify": verify_state,
    }
    write_json(run_dir / "validation.json", report)
    return report


def status(run_dir: Path) -> dict[str, Any]:
    manifest = read_json(run_dir / "manifest.json")
    map_state = validate_maps(run_dir)
    reduce_state = validate_reduce(run_dir)
    verify_state = validate_verify_results(run_dir)
    compiled_path = run_dir / "wiki" / "compiled.json"
    compiled = compiled_path.exists()
    compiled_current = False
    if compiled and reduce_state["status"] == "valid" and verify_state["status"] != "invalid":
        try:
            compiled_manifest = read_json(compiled_path)
            reduce_sha = file_hash(run_dir / "work" / "results" / "reduce.json")
            verify_sha = (
                file_hash(run_dir / "work" / "results" / "verify" / "results.json")
                if verify_state["status"] == "valid"
                else None
            )
            compiled_current = (
                compiled_manifest.get("reduce_result_sha256") == reduce_sha
                and compiled_manifest.get("verify_results_sha256") == verify_sha
            )
        except TTKError:
            compiled_current = False
    if map_state["invalid"]:
        stage, action = "map_invalid", "Fix invalid map result JSON before continuing."
    elif map_state["missing"]:
        missing = next(row["window_id"] for row in map_state["windows"] if row["status"] == "missing")
        stage, action = "map", f"Complete semantic map result for {missing}."
    elif reduce_state["status"] == "packet_missing":
        stage, action = "reduce_packet_ready", "Run make-reduce to build the compact evidence ledger and reduce packet."
    elif reduce_state["status"] == "result_missing":
        stage, action = "reduce", "Complete work/results/reduce.json from work/packets/reduce.json."
    elif reduce_state["status"] == "invalid":
        stage, action = "reduce_invalid", "Fix invalid reduce result JSON before continuing."
    elif not (run_dir / "work" / "packets" / "verify-queue.json").exists():
        stage, action = "verify_queue_ready", "Run make-verify to route check-worthy factual claims."
    elif verify_state["status"] == "invalid":
        stage, action = "verify_invalid", "Fix or remove invalid verification results."
    elif compiled_current:
        stage, action = "compiled", "Pipeline artifacts are compiled. Re-run validation after any semantic result change."
    elif compiled:
        stage, action = "compile_stale", "Re-run compile because semantic or verification results changed after the last compile."
    else:
        stage, action = "compile_ready", "Run compile. Verification results are optional; missing results remain UNVERIFIED."
    return {
        "schema": "ttk.status.v2",
        "source_name": manifest.get("source_name"),
        "stage": stage,
        "next_action": action,
        "map": {k: map_state[k] for k in ("total", "valid", "missing", "invalid")},
        "reduce": reduce_state["status"],
        "verify": verify_state["status"],
        "compiled": compiled,
        "compiled_current": compiled_current,
    }


def next_action(run_dir: Path) -> dict[str, Any]:
    state = status(run_dir)
    out = dict(state)
    stage = state["stage"]
    if stage == "map":
        map_state = validate_maps(run_dir)
        missing = next(row["window_id"] for row in map_state["windows"] if row["status"] == "missing")
        packet_path = run_dir / "work" / "packets" / "map" / f"{missing}.json"
        packet = read_json(packet_path)
        out["packet"] = str(packet_path)
        out["result"] = str(run_dir / "work" / "results" / "map" / f"{missing}.json")
        out["packet_sha256"] = packet["packet_sha256"]
        out["semantic_contract"] = "references/semantic-contracts.md#map-result"
    elif stage == "reduce":
        packet_path = run_dir / "work" / "packets" / "reduce.json"
        packet = read_json(packet_path)
        out["packet"] = str(packet_path)
        out["result"] = str(run_dir / "work" / "results" / "reduce.json")
        out["packet_sha256"] = packet["packet_sha256"]
        out["semantic_contract"] = "references/semantic-contracts.md#reduce-result"
    elif stage in {"verify_queue_ready", "compile_ready", "compile_stale"}:
        out["semantic_contract"] = "references/semantic-contracts.md#external-verification"
    return out



__all__ = [name for name in globals() if not name.startswith("__")]
