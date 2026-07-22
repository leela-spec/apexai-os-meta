# Apex KB Phase 2 target-oriented exact patch pack

Status: operator review required before deterministic application.

Scope: `apex-meta/apex-kb-cli` only. This pack creates no branch, worktree, stash, commit, or push. Unrelated repository files are out of scope.

## Intended result

- Add `apex-kb drive --run-root <path>` as the autonomous deterministic outer loop.
- Treat independent semantic acceptance as opt-in compatibility behavior; validated Phase 2 pages are accepted by default.
- Turn an invalid semantic result into a bounded next attempt (`a02`, `a03`) instead of leaving the run stuck on the invalid packet.
- Generate the source atlas deterministically from the accepted Phase 1 source ledger.
- Validate Phase 1 answer pointers against that same ledger before import.
- Strengthen each Phase 2 dossier with purpose, ranked sources, question routes, source boundaries, unresolved questions, and raw-source reopen triggers.
- Preserve `continue` as the one-action command.

## Block 1 — CLI imports the lifecycle driver

<file>apex-meta/apex-kb-cli/src/apex_kb/cli.py</file>
<old>
from .lifecycle import (
    continue_once,
    create_manifest,
</old>
<new>
from .lifecycle import (
    continue_once,
    create_manifest,
    drive_until_boundary,
</new>

## Block 2 — Public `drive` command

<file>apex-meta/apex-kb-cli/src/apex_kb/cli.py</file>
<old>
@cli.command()
@click.option("--run-root", type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option("--query", "query_text", required=True)
</old>
<new>
@cli.command()
@click.option("--run-root", type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option("--semantic-acceptance", is_flag=True, help="Enable the legacy independent semantic-acceptance pass.")
@click.option("--max-actions", type=click.IntRange(1, 1000), default=200, show_default=True)
@click.option("--json-output", is_flag=True)
def drive(run_root: Path, semantic_acceptance: bool, max_actions: int, json_output: bool) -> None:
    """Run deterministic actions until semantic work or terminal completion."""
    root = run_root.resolve()
    try:
        result = drive_until_boundary(root, semantic_acceptance=semantic_acceptance, max_actions=max_actions)
        emit("drive", "ok", result, json_output=json_output)
    except ApexKBError as exc:
        abort("drive", exc, json_output)


@cli.command()
@click.option("--run-root", type=click.Path(path_type=Path, exists=True, file_okay=False), required=True)
@click.option("--query", "query_text", required=True)
</new>

## Block 3 — Acceptance defaults to disabled

<file>apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py</file>
<old>
            "acceptance": {"status": "not_required" if output == "analysis_only" else "pending", "attempt": 0, "verdict": None, "artifacts": {}, "evaluator_context_id": None},
</old>
<new>
            "acceptance": {"status": "not_required", "attempt": 0, "verdict": None, "artifacts": {}, "evaluator_context_id": None},
</new>

## Block 4 — Topic eligibility and compatibility-mode state

<file>apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py</file>
<old>
def _mark_pages_accepted(run_root: Path, manifest: dict[str, Any], topic_id: str) -> None:
</old>
<new>
def _acceptance_enabled(state: dict[str, Any]) -> bool:
    return any(item["acceptance"]["status"] != "not_required" for item in state["topics"].values())


def _accepted_topic_ids(state: dict[str, Any]) -> list[str]:
    if _acceptance_enabled(state):
        return [topic_id for topic_id, item in state["topics"].items() if item["acceptance"].get("verdict") == "semantic_pass"]
    return [topic_id for topic_id, item in state["topics"].items() if item["phase2"]["status"] in {"completed", "reused"}]


def configure_semantic_acceptance(run_root: Path, state: dict[str, Any], enabled: bool) -> None:
    changed = False
    for item in state["topics"].values():
        acceptance = item["acceptance"]
        if acceptance["status"] in {"completed", "failed", "reused"}:
            continue
        target = "pending" if enabled and item["phase2"]["status"] != "not_required" else "not_required"
        if acceptance["status"] != target:
            acceptance["status"] = target
            changed = True
    if changed:
        save_state(run_root, state, "semantic_acceptance_mode_configured", {"enabled": enabled})


def _mark_pages_accepted(run_root: Path, manifest: dict[str, Any], topic_id: str) -> None:
</new>

## Block 5 — Directly accept validated Phase 2 pages when compatibility acceptance is disabled

<file>apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py</file>
<old>
    elif active["task_kind"] == "phase2":
        result = import_phase2_result(run_root, manifest, active)
        topic_state["phase2"].update({"status": "completed", "artifacts": result, "worker_context_id": result["worker_context_id"]})
        event = "phase2_imported"
</old>
<new>
    elif active["task_kind"] == "phase2":
        result = import_phase2_result(run_root, manifest, active)
        topic_state["phase2"].update({"status": "completed", "artifacts": result, "worker_context_id": result["worker_context_id"]})
        if topic_state["acceptance"]["status"] == "not_required":
            _mark_pages_accepted(run_root, manifest, topic_id)
        event = "phase2_imported"
</new>

## Block 6 — Bounded repair progression

<file>apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py</file>
<old>
    if action["kind"] == "semantic_import":
        return {"stage": f"{action['task_kind']}_import", "result": _import_active_task(run_root, manifest, state)}
</old>
<new>
    if action["kind"] == "semantic_import":
        try:
            return {"stage": f"{action['task_kind']}_import", "result": _import_active_task(run_root, manifest, state)}
        except ApexKBError as exc:
            if exc.code != "semantic_result_invalid":
                raise
            active = state["active_task"]
            slot = state["topics"][active["topic_id"]][active["task_kind"]]
            max_repairs = manifest["run_options"]["max_semantic_repairs"]
            if slot["attempt"] >= max_repairs + 1:
                state["lifecycle_status"] = "blocked"
                state["blockers"].append({"code": "semantic_repairs_exhausted", "task_id": active["task_id"], "details": exc.details})
            else:
                slot["status"] = "needs_repair"
                slot["repair_context"] = {"failed_task_id": active["task_id"], "error": exc.details}
            state["active_task"] = None
            state["current_stage"] = f"{active['task_kind']}_repair_required"
            save_state(run_root, state, "semantic_repair_requested", {"task_id": active["task_id"], "details": exc.details})
            return {"stage": "semantic_repair", "failed_task_id": active["task_id"], "repair": exc.details}
</new>

## Block 7 — Postflight does not demand disabled acceptance

<file>apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py</file>
<old>
        "all_semantic_acceptance_pass": output == "analysis_only" or (all(value == "semantic_pass" for value in acceptance.values()) and len(acceptance) == len(state["topics"])),
</old>
<new>
        "all_semantic_acceptance_pass": output == "analysis_only" or not _acceptance_enabled(state) or (all(value == "semantic_pass" for value in acceptance.values()) and len(acceptance) == len(state["topics"])),
</new>

## Block 8 — Completion and retrieval use validated Phase 2 topics by default

<file>apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py</file>
<old>
    accepted_topics = [
        topic_id for topic_id, item in state["topics"].items()
        if item["acceptance"].get("verdict") == "semantic_pass"
    ]
</old>
<new>
    accepted_topics = _accepted_topic_ids(state)
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py</file>
<old>
        accepted = [topic_id for topic_id, item in state["topics"].items() if item["acceptance"].get("verdict") == "semantic_pass"]
        result = build_retrieval(run_root, manifest, accepted)
</old>
<new>
        accepted = _accepted_topic_ids(state)
        result = build_retrieval(run_root, manifest, accepted)
</new>

## Block 9 — Autonomous deterministic outer loop

<file>apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py</file>
<old>
def status_snapshot(run_root: Path) -> dict[str, Any]:
</old>
<new>
def drive_until_boundary(run_root: Path, semantic_acceptance: bool = False, max_actions: int = 200) -> dict[str, Any]:
    manifest, state = load_run(run_root)
    configure_semantic_acceptance(run_root, state, semantic_acceptance)
    executed = []
    for _ in range(max_actions):
        snapshot = status_snapshot(run_root)
        action = snapshot["next_action"]
        if action["kind"] in {"completed", "blocked", "semantic_wait"}:
            return {"executed": executed, "status": snapshot}
        executed.append(continue_once(run_root))
    raise ApexKBError("drive_action_limit", "Drive reached its deterministic action limit", {"max_actions": max_actions})


def status_snapshot(run_root: Path) -> dict[str, Any]:
</new>

## Block 10 — Validate Phase 1 answer citations before accepting the evidence ledger

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
        expected_queries = {item["query_id"] for item in packet_task["target_queries"]}
        actual_queries = [item["query_id"] for item in value["topic_analysis"]["target_answers"]]
        if set(actual_queries) != expected_queries or len(actual_queries) != len(set(actual_queries)):
            raise ApexKBError("target_answer_set_incomplete", "Phase 1 must address every locked target query exactly once", {"expected": sorted(expected_queries), "actual": actual_queries})
</old>
<new>
        expected_queries = {item["query_id"] for item in packet_task["target_queries"]}
        actual_queries = [item["query_id"] for item in value["topic_analysis"]["target_answers"]]
        if set(actual_queries) != expected_queries or len(actual_queries) != len(set(actual_queries)):
            raise ApexKBError("target_answer_set_incomplete", "Phase 1 must address every locked target query exactly once", {"expected": sorted(expected_queries), "actual": actual_queries})
        review_by_id = {item["source_id"]: item for item in value["source_reviews"]}
        for answer in value["topic_analysis"]["target_answers"]:
            citations = []
            for citation in answer["citations"]:
                source_id, separator, pointer = citation.partition(":")
                if not separator or not pointer:
                    raise ApexKBError("phase1_citation_invalid", f"Phase 1 answer {answer['query_id']} has an invalid citation: {citation}")
                citations.append({"source_id": source_id, "pointer": pointer})
            _validate_citations(citations, review_by_id, f"Phase 1 answer {answer['query_id']}")
</new>

## Block 11 — Phase 2 packet declares target-oriented value contracts

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
        "source_capsule_paths": sorted(capsule_paths),
        "required_routes": topic["expected_routes"],
</old>
<new>
        "source_capsule_paths": sorted(capsule_paths),
        "context_contract": "Read only this topic's Phase 1 analysis and the source capsules listed by this packet; do not read another topic's Phase 1 analysis.",
        "page_value_contract": {
            "macro": "Why this topic matters for the operator's stated outcome.",
            "meso": "What the models, patterns, distinctions, and relationships are.",
            "micro": "How to recognize, choose, and apply the practices safely.",
            "required_sections": ["page_purpose", "adaptive_ranked_sources", "route_by_question", "source_boundaries", "open_questions", "raw_source_reopen_triggers"],
        },
        "atlas_contract": "The application generates the complete source atlas deterministically from Phase 1; the semantic worker must not reproduce it.",
        "required_routes": topic["expected_routes"],
</new>

## Block 12 — Deterministic atlas construction

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
def _citation_text(citations: list[dict[str, str]]) -> str:
</old>
<new>
def _deterministic_atlas(task: dict[str, Any], phase1: dict[str, Any]) -> dict[str, Any]:
    return {
        "route": task["required_routes"]["source_atlas"],
        "title": f"{task['topic']['name']} — Source Atlas",
        "entries": [
            {
                "source_id": review["source_id"],
                "repository_path": review["repository_path"],
                "disposition": review["disposition"],
                "read_status": review["read_status"],
                "content_snapshot": review["summary"],
                "individual_value": review["individual_value"],
                "authority": review["authority"],
                "freshness": review["freshness"],
                "duplicate_or_supersession": review["duplicate_or_supersession"],
                "pointers": review["pointers"],
                "questions_supported": review["questions_supported"],
            }
            for review in phase1["source_reviews"]
        ],
    }


def _citation_text(citations: list[dict[str, str]]) -> str:
</new>

## Block 13 — Render the stronger dossier contract

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
        "## Executive summary",
        "",
        dossier["executive_summary"],
        "",
</old>
<new>
        "## Page purpose",
        "",
        dossier["page_purpose"],
        "",
        "## Executive summary",
        "",
        dossier["executive_summary"],
        "",
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
    lines.extend(["## Key claims", ""])
</old>
<new>
    lines.extend(["## Adaptive ranked source set", ""])
    for source in dossier["adaptive_ranked_sources"]:
        lines.append(f"{source['rank']}. `{source['source_id']}` — {source['value']} — {_citation_text(source['citations'])}")
    lines.extend(["", "## Routes by question", ""])
    for route in dossier["route_by_question"]:
        lines.append(f"- `{route['query_id']}` — {route['route']}")
    lines.extend(["", "## Source boundaries", ""])
    lines.extend(f"- {item}" for item in dossier["source_boundaries"])
    lines.extend(["", "## Key claims", ""])
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
    lines.extend(["", "## Uncertainty", ""])
    lines.extend(f"- {item}" for item in dossier["uncertainties"] or ["None recorded."])
    lines.extend(["", "## Routes", "", f"- Source atlas: `{value['atlas']['route']}`"])
</old>
<new>
    lines.extend(["", "## Uncertainty and open questions", ""])
    lines.extend(f"- {item}" for item in dossier["uncertainties"] + dossier["open_questions"] or ["None recorded."])
    lines.extend(["", "## Raw-source reopen triggers", ""])
    lines.extend(f"- {item}" for item in dossier["raw_source_reopen_triggers"] or ["None recorded."])
    lines.extend(["", "## Routes", "", f"- Source atlas: `{value['atlas']['route']}`"])
</new>

## Block 14 — Ignore semantic atlas copies and render the deterministic atlas

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
        expected_candidates = set(task["candidate_source_ids"])
        atlas_ids = [item["source_id"] for item in value["atlas"]["entries"]]
        if set(atlas_ids) != expected_candidates or len(atlas_ids) != len(set(atlas_ids)):
            raise ApexKBError("source_atlas_incomplete", "Source atlas must preserve every Phase 0 candidate exactly once", {"missing": sorted(expected_candidates - set(atlas_ids)), "unexpected": sorted(set(atlas_ids) - expected_candidates)})
        phase1 = load_json(Path(task["phase1_analysis_path"]))
        review_by_id = {item["source_id"]: item for item in phase1["source_reviews"]}
</old>
<new>
        phase1 = load_json(Path(task["phase1_analysis_path"]))
        review_by_id = {item["source_id"]: item for item in phase1["source_reviews"]}
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
        for entry in value["atlas"]["entries"]:
            review = review_by_id[entry["source_id"]]
            for field in (
                "repository_path", "disposition", "read_status", "individual_value", "authority", "freshness",
                "duplicate_or_supersession", "pointers", "questions_supported",
            ):
                if entry[field] != review[field]:
                    raise ApexKBError("source_atlas_identity_mismatch", f"Atlas {field} differs from Phase 1 for {entry['source_id']}")
            if entry["content_snapshot"] != review["summary"]:
                raise ApexKBError("source_atlas_identity_mismatch", f"Atlas content_snapshot differs from the Phase 1 summary for {entry['source_id']}")
        if value["dossier"]["route"] != task["required_routes"]["dossier"] or value["atlas"]["route"] != task["required_routes"]["source_atlas"]:
            raise ApexKBError("page_route_mismatch", "Phase 2 result does not use the required dossier and atlas routes")
</old>
<new>
        if value["dossier"]["route"] != task["required_routes"]["dossier"]:
            raise ApexKBError("page_route_mismatch", "Phase 2 result does not use the required dossier route")
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py</file>
<old>
    dossier_path = run_root / value["dossier"]["route"]
    atlas_path = run_root / value["atlas"]["route"]
    atomic_text(dossier_path, _render_dossier(value))
    atomic_text(atlas_path, _render_atlas(value))
</old>
<new>
    rendered_value = {**value, "atlas": _deterministic_atlas(task, phase1)}
    dossier_path = run_root / value["dossier"]["route"]
    atlas_path = run_root / rendered_value["atlas"]["route"]
    atomic_text(dossier_path, _render_dossier(rendered_value))
    atomic_text(atlas_path, _render_atlas(rendered_value))
</new>

## Block 15 — Phase 2 schema makes atlas application-owned and requires value-bearing sections

<file>apex-meta/apex-kb-cli/src/apex_kb/schemas/phase2-result.schema.json</file>
<old>
  "required": ["schema", "run_id", "config_hash", "task_id", "phase", "topic_id", "worker_context_id", "dossier", "atlas"],
</old>
<new>
  "required": ["schema", "run_id", "config_hash", "task_id", "phase", "topic_id", "worker_context_id", "dossier"],
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/schemas/phase2-result.schema.json</file>
<old>
      "required": ["route", "title", "executive_summary", "macro", "meso", "micro", "target_answers", "key_claims", "evolution", "contradictions", "uncertainties"],
</old>
<new>
      "required": ["route", "title", "page_purpose", "executive_summary", "macro", "meso", "micro", "adaptive_ranked_sources", "route_by_question", "source_boundaries", "target_answers", "key_claims", "evolution", "contradictions", "uncertainties", "open_questions", "raw_source_reopen_triggers"],
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/schemas/phase2-result.schema.json</file>
<old>
        "route": {"type": "string", "minLength": 1}, "title": {"type": "string", "minLength": 1}, "executive_summary": {"type": "string", "minLength": 1}, "macro": {"type": "string", "minLength": 1}, "meso": {"type": "string", "minLength": 1}, "micro": {"type": "string", "minLength": 1},
</old>
<new>
        "route": {"type": "string", "minLength": 1}, "title": {"type": "string", "minLength": 1}, "page_purpose": {"type": "string", "minLength": 1}, "executive_summary": {"type": "string", "minLength": 1}, "macro": {"type": "string", "minLength": 1}, "meso": {"type": "string", "minLength": 1}, "micro": {"type": "string", "minLength": 1},
        "adaptive_ranked_sources": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["rank", "source_id", "value", "citations"], "properties": {"rank": {"type": "integer", "minimum": 1}, "source_id": {"type": "string", "minLength": 1}, "value": {"type": "string", "minLength": 1}, "citations": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/citation"}}}}},
        "route_by_question": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["query_id", "route"], "properties": {"query_id": {"type": "string", "minLength": 1}, "route": {"type": "string", "minLength": 1}}}},
        "source_boundaries": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 1}},
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/schemas/phase2-result.schema.json</file>
<old>
        "evolution": {"type": "array", "items": {"type": "string"}}, "contradictions": {"type": "array", "items": {"type": "string"}}, "uncertainties": {"type": "array", "items": {"type": "string"}}
</old>
<new>
        "evolution": {"type": "array", "items": {"type": "string"}}, "contradictions": {"type": "array", "items": {"type": "string"}}, "uncertainties": {"type": "array", "items": {"type": "string"}},
        "open_questions": {"type": "array", "items": {"type": "string", "minLength": 1}}, "raw_source_reopen_triggers": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 1}}
</new>

## Block 16 — Phase 2 task explicitly supports one-go iterative execution

<file>apex-meta/apex-kb-cli/src/apex_kb/templates/phase2-task.md</file>
<old>
Compile an answer-bearing Macro/Meso/Micro dossier at `{dossier}` and a complete source atlas at `{atlas}`. Macro, Meso, Micro, every locked answer, every material key claim, and every citation must be non-empty. Preserve every locked query ID and question verbatim. Cite only topic candidates reviewed in Phase 1, using source IDs and exact pointers preserved by that review. Use only validated Phase 1 analysis and reusable source capsules. Preserve present, proposed, historical, open, and contradicted states. The atlas must contain every deterministic candidate exactly once, including incidental, duplicate, historical, generated, blocked, and irrelevant-after-review dispositions.

Return structured JSON; the application renders the Markdown pages deterministically. Write only to:
</old>
<new>
Compile an answer-bearing Macro/Meso/Micro dossier at `{dossier}`. Macro explains why the topic matters for the operator's outcome; Meso explains what the relevant models, patterns, distinctions, and relationships are; Micro explains how to recognize, choose, and apply practices safely. Every locked answer, material key claim, and citation must be non-empty. Preserve every locked query ID and question verbatim. Cite only topic candidates reviewed in Phase 1, using source IDs and exact pointers preserved by that review. Use only this topic's validated Phase 1 analysis and the source capsules listed in this packet. Do not read another topic's Phase 1 analysis. Preserve only evidence states actually supported by the sources; do not manufacture enum coverage.

Include page purpose, an adaptive ranked source set, routes by locked question, source boundaries, contradictions or tensions, uncertainty and open questions, raw-source reopen triggers, and material evolution. The application creates `{atlas}` deterministically from Phase 1; do not submit or copy the atlas.

Return readable, indented structured JSON; the application renders the Markdown pages deterministically. Write only to:
</new>

<file>apex-meta/apex-kb-cli/src/apex_kb/templates/phase2-task.md</file>
<old>
Do not mutate manifests, run state, indexes, retrieval, or sources. Do not select the next lifecycle stage.
</old>
<new>
Do not mutate manifests, run state, indexes, retrieval, or sources. After writing this result, the outer executor must run `apex-kb drive` again, report concise progress, and continue to the next topic without asking for approval. The application remains the sole authority that selects the next lifecycle stage.
</new>

## Required verification after application

```powershell
python -m pytest apex-meta/apex-kb-cli/tests -q
apex-kb --help
apex-kb drive --run-root "C:\GitDev\apexai-os-meta\apex-meta\kb\therapy-narm-personal-development" --json-output
```

The test patch will update helper-generated Phase 2 fixtures to the strengthened schema, assert deterministic atlas generation, assert default acceptance bypass, assert opt-in compatibility acceptance, assert `a02` repair progression, and assert `drive` stops only at semantic or terminal boundaries.
