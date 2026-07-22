from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path
from typing import Any

from .config import normalize_config, preview_config
from .corpus import build_corpus_intelligence, check_source_drift
from .errors import ApexKBError
from .io import (
    atomic_json,
    atomic_text,
    atomic_yaml,
    canonical_hash,
    load_json,
    load_yaml,
    utc_now,
    utc_stamp,
    validate_schema,
)
from .retrieval import build_retrieval, retrieval_health
from .semantic import (
    create_acceptance_packet,
    create_phase1_packet,
    create_phase2_packet,
    import_acceptance_result,
    import_phase1_result,
    import_phase2_result,
)

MANIFEST_SCHEMA = "apex.kb.run-manifest.v2"
STATE_SCHEMA = "apex.kb.run-state.v2"


def _artifact_layout(run_id: str) -> dict[str, str]:
    return {
        "run_dir": f"runs/{run_id}",
        "stage_results": f"runs/{run_id}/stage-results",
        "semantic_tasks": f"runs/{run_id}/semantic-tasks",
        "incoming": f"runs/{run_id}/incoming",
        "semantic_results": f"runs/{run_id}/semantic-results",
        "logs": f"runs/{run_id}/logs",
    }


def create_manifest(config: dict[str, Any], run_root: Path, preview: dict[str, Any], run_kind: str = "new", previous_run: dict[str, Any] | None = None) -> dict[str, Any]:
    config_hash = canonical_hash(config)
    run_id = f"run-{utc_stamp()}-{config_hash[:10]}"
    if previous_run:
        run_id += f"-u{str(previous_run['run_id'])[-6:]}"
    manifest = {
        "schema": MANIFEST_SCHEMA,
        "schema_version": 2,
        "run_id": run_id,
        "run_kind": run_kind,
        "config_hash": config_hash,
        "created_at": utc_now(),
        "source": preview["source"],
        "destination": preview["destination"],
        "exclusions": config["exclusions"],
        "lifecycle_hint_rules": config["lifecycle_hint_rules"],
        "authority_hint_rules": config["authority_hint_rules"],
        "corpus_scope": {
            "source_roots": [item["configured"] for item in preview["source"]["resolved_folders"]],
            "exclusions": config["exclusions"],
            "output_root_exclusion": preview["destination"]["resolved_run_root"],
            "source_handling": config["run_options"]["source_handling"],
            "non_text_policy": config["run_options"]["non_text"],
            "lifecycle_hint_rules": config["lifecycle_hint_rules"],
            "authority_hint_rules": config["authority_hint_rules"],
        },
        "topics": config["topics"],
        "run_options": config["run_options"],
        "artifact_layout": _artifact_layout(run_id),
        "previous_run": previous_run,
    }
    validate_schema(manifest, "run-manifest.schema.json")
    return manifest


def initial_state(manifest: dict[str, Any]) -> dict[str, Any]:
    output = manifest["run_options"]["output"]
    topics = {}
    for topic in manifest["topics"]:
        topics[topic["topic_id"]] = {
            "topic_id": topic["topic_id"],
            "affected": True,
            "phase1": {"status": "pending", "attempt": 0, "artifacts": {}, "worker_context_id": None},
            "phase2": {"status": "not_required" if output == "analysis_only" else "pending", "attempt": 0, "artifacts": {}, "worker_context_id": None},
            "acceptance": {"status": "not_required" if output == "analysis_only" else "pending", "attempt": 0, "verdict": None, "artifacts": {}, "evaluator_context_id": None},
        }
    state = {
        "schema": STATE_SCHEMA,
        "schema_version": 2,
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "run_kind": manifest["run_kind"],
        "lifecycle_status": "running",
        "current_stage": "setup_confirmed",
        "completed_stages": ["setup_confirmed"],
        "corpus_intelligence": {"status": "pending", "artifacts": {}},
        "topics": topics,
        "active_task": None,
        "retrieval": {"status": "not_required" if output != "query_ready" else "pending", "artifacts": {}},
        "postflight": {"status": "pending", "artifacts": {}},
        "completion": {"status": "pending", "artifacts": {}},
        "blockers": [],
        "history": [{"at": utc_now(), "event": "setup_confirmed"}],
        "updated_at": utc_now(),
    }
    validate_schema(state, "run-state.schema.json")
    return state


def write_new_run(run_root: Path, config: dict[str, Any], manifest: dict[str, Any], state: dict[str, Any]) -> None:
    if (run_root / "run-manifest.json").exists() or (run_root / "run-state.json").exists():
        raise ApexKBError("run_exists", f"A controlled run already exists at {run_root}")
    run_root.mkdir(parents=True, exist_ok=True)
    for path in (
        "manifests/phase0/topic-maps", "ingest-analysis/sources", "ingest-analysis/topics", "wiki/concepts",
        "wiki/summaries", "audit/semantic-acceptance", "derived/search", "outputs/queries", "maintenance",
        manifest["artifact_layout"]["stage_results"], manifest["artifact_layout"]["semantic_tasks"],
        manifest["artifact_layout"]["incoming"], manifest["artifact_layout"]["semantic_results"],
    ):
        (run_root / path).mkdir(parents=True, exist_ok=True)
    atomic_yaml(run_root / "run-config.yaml", config)
    atomic_json(run_root / "run-manifest.json", manifest)
    atomic_json(run_root / "run-state.json", state)


def save_state(run_root: Path, state: dict[str, Any], event: str | None = None, details: dict[str, Any] | None = None) -> None:
    if event:
        state["history"].append({"at": utc_now(), "event": event, "details": details or {}})
    state["updated_at"] = utc_now()
    validate_schema(state, "run-state.schema.json")
    atomic_json(run_root / "run-state.json", state)


def _validate_run_identity(manifest: dict[str, Any], state: dict[str, Any]) -> None:
    if manifest.get("run_id") != state.get("run_id") or manifest.get("config_hash") != state.get("config_hash"):
        raise ApexKBError("run_identity_mismatch", "Manifest and state do not describe the same run")


def inspect_run_schema(run_root: Path) -> str:
    manifest = load_json(run_root / "run-manifest.json")
    return str(manifest.get("schema") or "unknown")


def load_run(run_root: Path, allow_legacy: bool = False) -> tuple[dict[str, Any], dict[str, Any]]:
    manifest = load_json(run_root / "run-manifest.json")
    state = load_json(run_root / "run-state.json")
    if manifest.get("schema") != MANIFEST_SCHEMA or state.get("schema") != STATE_SCHEMA:
        if allow_legacy:
            return manifest, state
        raise ApexKBError("migration_required", "Run uses a legacy schema; run `apex-kb continue` or `apex-kb update` to migrate safely", {"manifest_schema": manifest.get("schema"), "state_schema": state.get("schema")})
    validate_schema(manifest, "run-manifest.schema.json")
    validate_schema(state, "run-state.schema.json")
    _validate_run_identity(manifest, state)
    config = normalize_config(load_yaml(run_root / "run-config.yaml"))
    if canonical_hash(config) != manifest["config_hash"]:
        raise ApexKBError("config_drift", "run-config.yaml no longer matches the frozen manifest", {"expected": manifest["config_hash"], "actual": canonical_hash(config)})
    return manifest, state


def migrate_legacy_run(run_root: Path) -> dict[str, Any]:
    old_manifest, old_state = load_run(run_root, allow_legacy=True)
    if old_manifest.get("schema") == MANIFEST_SCHEMA and old_state.get("schema") == STATE_SCHEMA:
        return {"migrated": False}
    migration_root = run_root / "log" / "migrations" / utc_stamp()
    migration_root.mkdir(parents=True, exist_ok=True)
    for name in ("run-config.yaml", "run-manifest.json", "run-state.json"):
        source = run_root / name
        if source.is_file():
            shutil.copy2(source, migration_root / name)
    config = normalize_config(load_yaml(run_root / "run-config.yaml"))
    resolved_root, _, preview = preview_config(config)
    if resolved_root != run_root.resolve():
        raise ApexKBError("legacy_destination_mismatch", "Normalized legacy destination does not resolve to the existing run root", {"expected": str(run_root.resolve()), "actual": str(resolved_root)})
    manifest = create_manifest(config, run_root, preview, run_kind="migration")
    state = initial_state(manifest)
    state["history"].append({"at": utc_now(), "event": "migrated_from_legacy", "details": {"old_manifest_schema": old_manifest.get("schema"), "old_state_schema": old_state.get("schema")}})
    atomic_yaml(run_root / "run-config.yaml", config)
    atomic_json(run_root / "run-manifest.json", manifest)
    atomic_json(run_root / "run-state.json", state)
    atomic_json(migration_root / "migration-result.json", {"schema": "apex.kb.migration-result.v2", "migrated_at": utc_now(), "new_run_id": manifest["run_id"], "new_config_hash": manifest["config_hash"]})
    return {"migrated": True, "backup_path": str(migration_root), "run_id": manifest["run_id"]}


def derive_next_action(manifest: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    if state["lifecycle_status"] in {"query_ready", "compiled_accepted", "analysis_complete", "blocked"}:
        return {"kind": "completed" if state["lifecycle_status"] != "blocked" else "blocked", "status": state["lifecycle_status"]}
    active = state.get("active_task")
    if active:
        if active["task_kind"] == "phase1" and active.get("transport") == "direct_main":
            return {
                "kind": "semantic_reconcile",
                "task_kind": active["task_kind"],
                "topic_id": active["topic_id"],
                "task_id": active["task_id"],
                "packet_dir": active["packet_dir"],
                "prompt_path": active["prompt_path"],
                "base_commit": active["base_commit"],
                "expected_output_paths": active["expected_output_paths"],
            }
        incoming_exists = Path(active["incoming_path"]).is_file()
        return {
            "kind": "semantic_import" if incoming_exists else "semantic_wait",
            "task_kind": active["task_kind"],
            "topic_id": active["topic_id"],
            "task_id": active["task_id"],
            "packet_dir": active["packet_dir"],
            "incoming_path": active["incoming_path"],
        }
    if state["corpus_intelligence"]["status"] != "completed":
        return {"kind": "deterministic", "stage": "corpus_intelligence"}
    for topic in manifest["topics"]:
        topic_state = state["topics"][topic["topic_id"]]
        if topic_state["phase1"]["status"] in {"pending", "needs_repair"}:
            return {"kind": "semantic_packet", "task_kind": "phase1", "topic_id": topic["topic_id"]}
    if manifest["run_options"]["output"] != "analysis_only":
        for topic in manifest["topics"]:
            topic_state = state["topics"][topic["topic_id"]]
            if topic_state["phase2"]["status"] in {"pending", "needs_repair"}:
                return {"kind": "semantic_packet", "task_kind": "phase2", "topic_id": topic["topic_id"]}
        for topic in manifest["topics"]:
            topic_state = state["topics"][topic["topic_id"]]
            if topic_state["acceptance"]["status"] in {"pending", "needs_repair"}:
                return {"kind": "semantic_packet", "task_kind": "acceptance", "topic_id": topic["topic_id"]}
    # Postflight proves source freshness and semantic completion before any
    # query-ready retrieval index is built.
    if state["postflight"]["status"] != "completed":
        return {"kind": "deterministic", "stage": "postflight"}
    if manifest["run_options"]["output"] == "query_ready" and state["retrieval"]["status"] != "completed":
        return {"kind": "deterministic", "stage": "retrieval"}
    if state["completion"]["status"] != "completed":
        return {"kind": "deterministic", "stage": "completion"}
    raise ApexKBError("state_completion_mismatch", "Run has completed all stages but lifecycle_status is not terminal")

def next_action_text(run_root: Path, action: dict[str, Any]) -> str:
    if action["kind"] == "semantic_reconcile":
        return (
            f'Execute the complete Phase 2A browser prompt at "{action["prompt_path"]}". '
            f'After the browser worker commits and pushes the declared outputs directly to destination main, '
            f'run apex-kb continue --run-root "{run_root}"'
        )
    if action["kind"] == "semantic_wait":
        return (
            f'Execute the bounded {action["task_kind"]} packet at "{action["packet_dir"]}", '
            f'write the result to "{action["incoming_path"]}", then run '
            f'apex-kb continue --run-root "{run_root}"'
        )
    if action["kind"] in {"semantic_import", "semantic_packet", "deterministic"}:
        return f'apex-kb continue --run-root "{run_root}"'
    if action["kind"] == "blocked":
        return "Resolve the recorded blocker, then use apex-kb status or apex-kb update as appropriate."
    return "No further lifecycle action."


def _activate_packet(run_root: Path, manifest: dict[str, Any], state: dict[str, Any], task_kind: str, topic_id: str) -> dict[str, Any]:
    topic_state = state["topics"][topic_id]
    if task_kind == "phase1":
        slot = topic_state["phase1"]
        slot["attempt"] += 1
        packet = create_phase1_packet(run_root, manifest, topic_id, slot["attempt"], slot.pop("repair_context", None))
    elif task_kind == "phase2":
        slot = topic_state["phase2"]
        slot["attempt"] += 1
        packet = create_phase2_packet(run_root, manifest, topic_id, slot["attempt"], slot.pop("repair_context", None))
    elif task_kind == "acceptance":
        slot = topic_state["acceptance"]
        slot["attempt"] += 1
        drafting_context = topic_state["phase2"]["worker_context_id"]
        if not drafting_context:
            raise ApexKBError("phase2_context_missing", f"Cannot create acceptance task without Phase 2 drafting context for {topic_id}")
        packet = create_acceptance_packet(run_root, manifest, topic_id, drafting_context, slot["attempt"])
    else:
        raise ApexKBError("task_kind_unknown", f"Unknown semantic task kind: {task_kind}")
    slot["status"] = "awaiting_result"
    state["active_task"] = packet
    state["current_stage"] = f"awaiting_{task_kind}_{topic_id}"
    save_state(run_root, state, "semantic_packet_created", packet)
    return packet


def _mark_pages_accepted(run_root: Path, manifest: dict[str, Any], topic_id: str) -> None:
    topic = next(item for item in manifest["topics"] if item["topic_id"] == topic_id)
    for route in topic["expected_routes"].values():
        path = run_root / route
        if not path.is_file():
            raise ApexKBError("accepted_page_missing", f"Cannot mark missing page accepted: {path}")
        text = path.read_text(encoding="utf-8")
        if "status: accepted_pending_evaluation" not in text:
            raise ApexKBError("page_acceptance_marker_missing", f"Page does not contain the expected pending-acceptance marker: {path}")
        atomic_text(path, text.replace("status: accepted_pending_evaluation", "status: accepted", 1))


def _semantic_stage_result(run_root: Path, manifest: dict[str, Any], active: dict[str, Any], result: dict[str, Any]) -> None:
    stage = f"{active['task_kind']}:{active['topic_id']}"
    artifacts: list[str] = []
    for key, value in result.items():
        if not (key.endswith("path") or key.endswith("paths") or key.endswith("markdown") or key == "imported_result"):
            continue
        if isinstance(value, str):
            artifacts.append(value)
        elif isinstance(value, list):
            artifacts.extend(str(item) for item in value if isinstance(item, str))
    stage_result = {
        "schema": "apex.kb.stage-result.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "stage": stage,
        "status": "completed",
        "started_at": utc_now(),
        "completed_at": utc_now(),
        "artifacts": artifacts,
        "reason_code": None,
        "message": f"Validated completed {active['task_kind']} result for {active['topic_id']}.",
        "metrics": {"task_id": active["task_id"], "topic_id": active["topic_id"]},
    }
    validate_schema(stage_result, "stage-result.schema.json")
    atomic_json(run_root / manifest["artifact_layout"]["stage_results"] / f"{active['task_id']}.json", stage_result)


def _import_active_task(run_root: Path, manifest: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    active = state["active_task"]
    if not active:
        raise ApexKBError("active_task_missing", "No active semantic task is recorded")
    topic_id = active["topic_id"]
    topic_state = state["topics"][topic_id]
    if active["task_kind"] == "phase1":
        result = import_phase1_result(run_root, manifest, active)
        topic_state["phase1"].update({"status": "completed", "artifacts": result, "worker_context_id": result["worker_context_id"]})
        event = "phase1_imported"
    elif active["task_kind"] == "phase2":
        result = import_phase2_result(run_root, manifest, active)
        topic_state["phase2"].update({"status": "completed", "artifacts": result, "worker_context_id": result["worker_context_id"]})
        event = "phase2_imported"
    elif active["task_kind"] == "acceptance":
        result = import_acceptance_result(run_root, manifest, active)
        verdict = result["verdict"]
        topic_state["acceptance"].update({"status": "completed" if verdict == "semantic_pass" else "failed", "verdict": verdict, "artifacts": result, "evaluator_context_id": result["evaluator_context_id"]})
        if verdict == "semantic_pass":
            _mark_pages_accepted(run_root, manifest, topic_id)
        if verdict != "semantic_pass":
            max_repairs = manifest["run_options"]["max_semantic_repairs"]
            if topic_state["phase2"]["attempt"] >= max_repairs + 1:
                state["lifecycle_status"] = "blocked"
                state["blockers"].append({"code": "semantic_acceptance_failed", "topic_id": topic_id, "verdict": verdict, "failed_items": result["failed_items"]})
            else:
                topic_state["phase2"]["status"] = "needs_repair"
                topic_state["phase2"]["repair_context"] = {"acceptance_verdict": verdict, "failed_items": result["failed_items"]}
                topic_state["acceptance"]["status"] = "pending"
        event = "acceptance_imported"
    else:
        raise ApexKBError("task_kind_unknown", f"Unknown active task kind: {active['task_kind']}")
    _semantic_stage_result(run_root, manifest, active, result)
    state["active_task"] = None
    state["current_stage"] = event
    completed_key = f"{active['task_kind']}:{topic_id}"
    if completed_key not in state["completed_stages"]:
        state["completed_stages"].append(completed_key)
    save_state(run_root, state, event, result)
    return result


def _apply_update_impact(run_root: Path, manifest: dict[str, Any], state: dict[str, Any], impact: dict[str, Any] | None) -> None:
    if not impact or not manifest.get("previous_run"):
        return
    previous_state_path = Path(manifest["previous_run"]["state_path"])
    previous_manifest_path = Path(manifest["previous_run"].get("manifest_path", ""))
    if not previous_state_path.is_file() or not previous_manifest_path.is_file():
        return
    previous_state = load_json(previous_state_path)
    previous_manifest = load_json(previous_manifest_path)
    semantic_depth_changed = previous_manifest.get("run_options", {}).get("semantic_depth") != manifest["run_options"]["semantic_depth"]
    previous_output = previous_manifest.get("run_options", {}).get("output")
    new_output = manifest["run_options"]["output"]
    for topic_id, topic_impact in impact["affected_topics"].items():
        topic_state = state["topics"][topic_id]
        source_or_contract_affected = bool(topic_impact["affected"] or semantic_depth_changed)
        topic_state["affected"] = source_or_contract_affected
        old = previous_state.get("topics", {}).get(topic_id)
        if not old:
            continue
        if source_or_contract_affected:
            continue
        # Unchanged Phase 1 understanding is content-hash reusable regardless of a later output-tier upgrade.
        if old.get("phase1", {}).get("status") in {"completed", "reused"}:
            topic_state["phase1"] = copy.deepcopy(old["phase1"])
            topic_state["phase1"]["status"] = "reused"
        if new_output == "analysis_only":
            continue
        # A prior analysis-only run has no compiled pages or independent acceptance to reuse.
        if previous_output == "analysis_only":
            continue
        if old.get("phase2", {}).get("status") in {"completed", "reused"}:
            topic_state["phase2"] = copy.deepcopy(old["phase2"])
            topic_state["phase2"]["status"] = "reused"
        if old.get("acceptance", {}).get("status") in {"completed", "reused"} and old.get("acceptance", {}).get("verdict") == "semantic_pass":
            topic_state["acceptance"] = copy.deepcopy(old["acceptance"])
            topic_state["acceptance"]["status"] = "reused"


def _complete_run(run_root: Path, manifest: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    output = manifest["run_options"]["output"]
    if state["postflight"]["status"] != "completed":
        raise ApexKBError("completion_before_postflight", "Completion requires a passing deterministic postflight")
    source_integrity = check_source_drift(run_root, manifest)
    if not source_integrity["fresh"]:
        raise ApexKBError(
            "completion_source_drift",
            "Source integrity changed after deterministic postflight; completion cannot be certified",
            source_integrity,
        )
    retrieval = retrieval_health(run_root) if output == "query_ready" else {"not_required": True}
    if output == "query_ready" and not (state["retrieval"]["status"] == "completed" and retrieval.get("fresh") and retrieval.get("integrity_ok")):
        raise ApexKBError("completion_before_retrieval", "Query-ready completion requires a fresh, healthy derived retrieval index", retrieval)
    accepted_topics = [
        topic_id for topic_id, item in state["topics"].items()
        if item["acceptance"].get("verdict") == "semantic_pass"
    ]
    completion_time = utc_now()
    certificate = {
        "schema": "apex.kb.completion.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "run_kind": manifest["run_kind"],
        "output": output,
        "completed_at": completion_time,
        "lifecycle_status": {"analysis_only": "analysis_complete", "compiled_kb": "compiled_accepted", "query_ready": "query_ready"}[output],
        "accepted_topics": accepted_topics,
        "postflight": state["postflight"]["artifacts"],
        "retrieval": state["retrieval"]["artifacts"],
        "blockers": list(state["blockers"]),
        "canonical_artifacts": {
            "run_config": "run-config.yaml",
            "run_manifest": "run-manifest.json",
            "run_state": "run-state.json",
            "source_inventory": "manifests/source-inventory.ndjson",
            "navigation_report": "manifests/phase0/phase0-navigation-report.md",
            "wiki_index": "wiki/index.md" if output == "query_ready" else None,
        },
        "source_integrity": source_integrity,
        "source_repository_mutated": not source_integrity["fresh"],
    }
    if certificate["blockers"]:
        raise ApexKBError("completion_with_blockers", "Completion certificate cannot be issued while blockers remain", certificate["blockers"])
    root_path = run_root / "completion.json"
    audit_path = run_root / "audit" / "completion" / f"{manifest['run_id']}.json"
    atomic_json(root_path, certificate)
    atomic_json(audit_path, certificate)
    stage_result = {
        "schema": "apex.kb.stage-result.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "stage": "completion",
        "status": "completed",
        "started_at": completion_time,
        "completed_at": completion_time,
        "artifacts": ["completion.json", str(audit_path.relative_to(run_root))],
        "reason_code": None,
        "message": f"Apex KB reached {certificate['lifecycle_status']} with durable completion evidence.",
        "metrics": {"accepted_topic_count": len(accepted_topics), "output": output},
    }
    validate_schema(stage_result, "stage-result.schema.json")
    atomic_json(run_root / manifest["artifact_layout"]["stage_results"] / "completion.json", stage_result)
    state["completion"].update({"status": "completed", "artifacts": {"certificate": "completion.json", "audit": str(audit_path.relative_to(run_root))}})
    state["lifecycle_status"] = certificate["lifecycle_status"]
    state["current_stage"] = "completion_complete"
    if "completion" not in state["completed_stages"]:
        state["completed_stages"].append("completion")
    return {"certificate": certificate, "result": stage_result}


def _postflight(run_root: Path, manifest: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    source = check_source_drift(run_root, manifest)
    output = manifest["run_options"]["output"]
    acceptance = {
        topic_id: topic_state["acceptance"].get("verdict")
        for topic_id, topic_state in state["topics"].items()
        if topic_state["acceptance"]["status"] != "not_required"
    }
    checks = {
        "source_fresh": source["fresh"],
        "all_phase1_complete": all(item["phase1"]["status"] in {"completed", "reused"} for item in state["topics"].values()),
        "all_phase2_complete": output == "analysis_only" or all(item["phase2"]["status"] in {"completed", "reused"} for item in state["topics"].values()),
        "all_semantic_acceptance_pass": output == "analysis_only" or (all(value == "semantic_pass" for value in acceptance.values()) and len(acceptance) == len(state["topics"])),
        "retrieval_deferred_until_postflight": output != "query_ready" or state["retrieval"]["status"] == "pending",
    }
    passed = all(checks.values())
    completion_time = utc_now()
    report = {
        "schema": "apex.kb.postflight.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "completed_at": completion_time,
        "output": output,
        "passed": passed,
        "checks": checks,
        "source_drift": source,
        "acceptance_verdicts": acceptance,
    }
    path = run_root / "audit" / "postflight" / f"{manifest['run_id']}.json"
    atomic_json(path, report)
    result = {
        "schema": "apex.kb.stage-result.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "stage": "postflight",
        "status": "completed" if passed else "blocked",
        "started_at": report["completed_at"],
        "completed_at": report["completed_at"],
        "artifacts": [str(path.relative_to(run_root))],
        "reason_code": None if passed else "postflight_failed",
        "message": "Source freshness and semantic completion passed before retrieval." if passed else "Apex KB lifecycle did not pass deterministic postflight.",
        "metrics": checks,
    }
    validate_schema(result, "stage-result.schema.json")
    atomic_json(run_root / manifest["artifact_layout"]["stage_results"] / "postflight.json", result)
    state["postflight"].update({"status": "completed" if passed else "blocked", "artifacts": {"report": str(path.relative_to(run_root))}})
    if not passed:
        state["lifecycle_status"] = "blocked"
        state["blockers"].append({"code": "postflight_failed", "checks": checks})
        state["current_stage"] = "postflight_blocked"
    else:
        state["current_stage"] = "postflight_complete"
        if "postflight" not in state["completed_stages"]:
            state["completed_stages"].append("postflight")
        if output != "query_ready":
            _complete_run(run_root, manifest, state)
    save_state(run_root, state, "postflight_completed" if passed else "postflight_blocked", report)
    return {"report": report, "result": result}

def continue_once(run_root: Path) -> dict[str, Any]:
    if inspect_run_schema(run_root) != MANIFEST_SCHEMA:
        migration = migrate_legacy_run(run_root)
        return {"stage": "migration", "migration": migration}
    manifest, state = load_run(run_root)
    action = derive_next_action(manifest, state)
    if action["kind"] == "completed":
        return {"stage": "completed", "status": state["lifecycle_status"]}
    if action["kind"] == "blocked":
        raise ApexKBError("run_blocked", "Run is blocked", state["blockers"])
    if action["kind"] == "semantic_reconcile":
        return {"stage": f"{action['task_kind']}_import", "result": _import_active_task(run_root, manifest, state)}
    if action["kind"] == "semantic_wait":
        raise ApexKBError("semantic_result_pending", "A bounded semantic task is awaiting its declared result", action)
    if action["kind"] == "semantic_import":
        return {"stage": f"{action['task_kind']}_import", "result": _import_active_task(run_root, manifest, state)}
    if action["kind"] == "semantic_packet":
        packet = _activate_packet(run_root, manifest, state, action["task_kind"], action["topic_id"])
        return {"stage": f"{action['task_kind']}_packet", "packet": packet}
    stage = action["stage"]
    if stage == "corpus_intelligence":
        previous = manifest.get("previous_run")
        result = build_corpus_intelligence(run_root, manifest, previous)
        state["corpus_intelligence"].update({"status": "completed", "artifacts": result["summary"]})
        _apply_update_impact(run_root, manifest, state, result["summary"].get("impact_report"))
        state["current_stage"] = "corpus_intelligence_complete"
        state["completed_stages"].append("corpus_intelligence")
        save_state(run_root, state, "corpus_intelligence_completed", result["summary"])
        return {"stage": stage, "result": result["summary"]}
    if stage == "retrieval":
        if state["postflight"]["status"] != "completed":
            raise ApexKBError("retrieval_before_postflight", "Retrieval cannot run before deterministic postflight passes")
        accepted = [topic_id for topic_id, item in state["topics"].items() if item["acceptance"].get("verdict") == "semantic_pass"]
        result = build_retrieval(run_root, manifest, accepted)
        state["retrieval"].update({"status": "completed", "artifacts": result["manifest"]})
        state["current_stage"] = "retrieval_complete"
        if "retrieval" not in state["completed_stages"]:
            state["completed_stages"].append("retrieval")
        completion = _complete_run(run_root, manifest, state)
        save_state(run_root, state, "retrieval_completed", {"health": result["health"], "completion": completion["certificate"]})
        return {"stage": stage, "result": result, "completion": completion}
    if stage == "postflight":
        return {"stage": stage, "result": _postflight(run_root, manifest, state)}
    if stage == "completion":
        completion = _complete_run(run_root, manifest, state)
        save_state(run_root, state, "completion_completed", completion["certificate"])
        return {"stage": stage, "result": completion}
    raise ApexKBError("illegal_next_stage", f"Unsupported deterministic stage: {stage}")


def status_snapshot(run_root: Path) -> dict[str, Any]:
    schema_name = inspect_run_schema(run_root)
    if schema_name != MANIFEST_SCHEMA:
        manifest, state = load_run(run_root, allow_legacy=True)
        return {
            "schema": "apex.kb.status.v2",
            "run_root": str(run_root),
            "migration_required": True,
            "manifest_schema": manifest.get("schema"),
            "state_schema": state.get("schema"),
            "exact_next_action": f"apex-kb continue --run-root \"{run_root}\"",
        }
    manifest, state = load_run(run_root)
    action = derive_next_action(manifest, state)
    return {
        "schema": "apex.kb.status.v2",
        "run_root": str(run_root),
        "run_id": manifest["run_id"],
        "run_kind": manifest["run_kind"],
        "config_hash": manifest["config_hash"],
        "lifecycle_status": state["lifecycle_status"],
        "current_stage": state["current_stage"],
        "completed_stages": state["completed_stages"],
        "topics": state["topics"],
        "active_task": state["active_task"],
        "retrieval": state["retrieval"],
        "postflight": state["postflight"],
        "completion": state["completion"],
        "blockers": state["blockers"],
        "next_action": action,
        "exact_next_action": next_action_text(run_root, action),
    }


def archive_current_run(run_root: Path, manifest: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    archive = run_root / "log" / "control-archive" / manifest["run_id"]
    archive.mkdir(parents=True, exist_ok=True)
    for name in ("run-config.yaml", "run-manifest.json", "run-state.json"):
        source = run_root / name
        if source.is_file():
            shutil.copy2(source, archive / name)
    for relative in ("wiki", "manifests"):
        source = run_root / relative
        if source.is_dir():
            target = archive / relative
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(source, target)
    topic_paths = {
        topic["topic_id"]: str(archive / "manifests" / "phase0" / "topic-maps" / f"{topic['topic_id']}.json")
        for topic in manifest["topics"]
    }
    return {
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "archive_root": str(archive),
        "state_path": str(archive / "run-state.json"),
        "manifest_path": str(archive / "run-manifest.json"),
        "config_path": str(archive / "run-config.yaml"),
        "inventory_path": str(archive / "manifests" / "source-inventory.ndjson"),
        "topic_map_paths": topic_paths,
    }


def initialize_update(run_root: Path, config_override: dict[str, Any] | None = None) -> dict[str, Any]:
    raw_manifest, raw_state = load_run(run_root, allow_legacy=True)
    migration = None
    if raw_manifest.get("schema") != MANIFEST_SCHEMA or raw_state.get("schema") != STATE_SCHEMA:
        migration = migrate_legacy_run(run_root)
    manifest, state = load_run(run_root)
    if migration is None and state["lifecycle_status"] not in {"query_ready", "compiled_accepted", "analysis_complete", "blocked"}:
        raise ApexKBError("update_requires_stable_run", "Update requires a completed or explicitly blocked prior run", {"status": state["lifecycle_status"]})
    old_config = normalize_config(load_yaml(run_root / "run-config.yaml"))
    config = normalize_config(config_override) if config_override is not None else old_config
    resolved_root, _, preview = preview_config(config)
    if resolved_root != run_root.resolve():
        raise ApexKBError("update_destination_changed", "Update cannot silently move an existing KB root", {"expected": str(run_root.resolve()), "actual": str(resolved_root)})
    previous = archive_current_run(run_root, manifest, state)
    new_manifest = create_manifest(config, run_root, preview, run_kind="update", previous_run=previous)
    new_state = initial_state(new_manifest)
    atomic_yaml(run_root / "run-config.yaml", config)
    atomic_json(run_root / "run-manifest.json", new_manifest)
    atomic_json(run_root / "run-state.json", new_state)
    return {
        "run_id": new_manifest["run_id"],
        "previous_run_id": manifest["run_id"],
        "archive_root": previous["archive_root"],
        "migration": migration,
    }
