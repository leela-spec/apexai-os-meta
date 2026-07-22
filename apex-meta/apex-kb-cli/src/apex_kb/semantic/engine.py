from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..corpus import load_topic_map
from ..errors import ApexKBError
from ..io import atomic_json, atomic_text, load_json, schema, template, utc_now, validate_schema

MATERIAL_DISPOSITIONS = {
    "core_current", "supporting_current", "implementation", "prototype", "historical", "contextual", "superseded",
    # Legacy v1/v2 aliases remain importable so existing KBs can migrate without rewriting evidence.
    "core", "contradictory", "duplicate_material",
}
BLOCKED_DISPOSITIONS = {"blocked_unreadable", "blocked_unsupported"}
VALID_DISPOSITIONS = MATERIAL_DISPOSITIONS | BLOCKED_DISPOSITIONS | {
    "incidental", "duplicate", "irrelevant_after_review",
    # Legacy aliases.
    "duplicate_nonmaterial", "generated_noise",
}
VALID_READ_STATUS = {"full", "targeted", "capsule_reused", "blocked"}


def _topic(manifest: dict[str, Any], topic_id: str) -> dict[str, Any]:
    for topic in manifest["topics"]:
        if topic["topic_id"] == topic_id:
            return topic
    raise ApexKBError("topic_unknown", f"Topic is not present in the manifest: {topic_id}")


def _task_id(kind: str, topic_id: str, attempt: int) -> str:
    return f"{kind}-{topic_id}-a{attempt:02d}"


def _packet_dir(run_root: Path, manifest: dict[str, Any], task_id: str) -> Path:
    return run_root / manifest["artifact_layout"]["semantic_tasks"] / task_id


def _incoming_path(run_root: Path, manifest: dict[str, Any], task_id: str) -> Path:
    return run_root / manifest["artifact_layout"]["incoming"] / f"{task_id}.json"


def _write_packet(packet_dir: Path, task: dict[str, Any], allowlist: dict[str, Any], schema_name: str, task_md: str, incoming: Path) -> dict[str, Any]:
    packet_dir.mkdir(parents=True, exist_ok=True)
    atomic_json(packet_dir / "task.json", task)
    atomic_json(packet_dir / "source-allowlist.json", allowlist)
    atomic_json(packet_dir / "output.schema.json", schema(schema_name))
    atomic_text(packet_dir / "expected-output-path.txt", str(incoming) + "\n")
    atomic_text(packet_dir / "TASK.md", task_md)
    return {
        "task_id": task["task_id"],
        "task_kind": task["task_kind"],
        "topic_id": task["topic_id"],
        "packet_dir": str(packet_dir),
        "incoming_path": str(incoming),
    }


def _evidence_entry(run_root: Path, candidate: dict[str, Any]) -> dict[str, Any]:
    capsule = run_root / "ingest-analysis" / "sources" / f"{candidate['content_hash']}.analysis.json"
    evidence_path = candidate.get("derived_text_path")
    if evidence_path:
        evidence_path = str(run_root / evidence_path)
    elif candidate.get("custody_path"):
        evidence_path = str(run_root / candidate["custody_path"])
    else:
        evidence_path = candidate["absolute_path"]
    record = {
        "source_id": candidate["source_id"],
        "repository_path": candidate["repository_path"],
        "absolute_path": candidate["absolute_path"],
        "evidence_path": evidence_path,
        "derived_text_path": candidate.get("derived_text_path"),
        "custody_path": candidate.get("custody_path"),
        "content_hash": candidate["content_hash"],
        "candidate_class": candidate["candidate_class"],
        "extraction_status": candidate["extraction_status"],
        "match_reasons": candidate["match_reasons"],
        "duplicate_relationships": candidate["duplicate_relationships"],
        "lifecycle_hints": candidate["lifecycle_hints"],
        "reusable_capsule_path": str(capsule) if capsule.is_file() else None,
    }
    return record


def create_phase1_packet(run_root: Path, manifest: dict[str, Any], topic_id: str, attempt: int = 1, repair_context: dict[str, Any] | None = None) -> dict[str, Any]:
    topic = _topic(manifest, topic_id)
    topic_map = load_topic_map(run_root, topic_id)
    task_id = _task_id("phase1", topic_id, attempt)
    packet_dir = _packet_dir(run_root, manifest, task_id)
    incoming = _incoming_path(run_root, manifest, task_id)
    sources = [_evidence_entry(run_root, candidate) for candidate in topic_map["candidates"]]
    task = {
        "schema": "apex.kb.semantic-task.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "task_id": task_id,
        "task_kind": "phase1",
        "topic_id": topic_id,
        "attempt": attempt,
        "semantic_depth": manifest["run_options"]["semantic_depth"],
        "topic": topic,
        "target_queries": topic["target_queries"],
        "topic_map_path": str(run_root / "manifests" / "phase0" / "topic-maps" / f"{topic_id}.json"),
        "candidate_count": topic_map["candidate_count"],
        "candidate_source_ids": [item["source_id"] for item in sources],
        "allowed_dispositions": sorted(VALID_DISPOSITIONS),
        "disposition_contract": "Every candidate exactly once; preserve current, implementation, prototype, historical, duplicate, superseded, incidental, irrelevant, and blocked distinctions.",
        "source_allowlist_path": "source-allowlist.json",
        "required_output_schema": "phase1-result.schema.json",
        "allowed_output_paths": [str(incoming)],
        "forbidden_writes": ["run-config.yaml", "run-manifest.json", "run-state.json", "manifests/**", "wiki/**", "derived/**", "source repository paths"],
        "repair_context": repair_context,
        "created_at": utc_now(),
    }
    validate_schema(task, "semantic-task.schema.json")
    body = template("phase1-task.md").format(
        run_id=manifest["run_id"],
        config_hash=manifest["config_hash"],
        task_id=task_id,
        topic_id=topic_id,
        topic_name=topic["name"],
        candidate_count=topic_map["candidate_count"],
        questions="\n".join(f"- `{item['query_id']}` [{item['priority']}]: {item['question']}" for item in topic["target_queries"]),
        incoming=str(incoming),
    )
    return _write_packet(packet_dir, task, {"schema": "apex.kb.source-allowlist.v2", "sources": sources}, "phase1-result.schema.json", body, incoming)


def _validate_identity(value: dict[str, Any], manifest: dict[str, Any], task: dict[str, Any], phase: str) -> None:
    expected = {
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "task_id": task["task_id"],
        "topic_id": task["topic_id"],
        "phase": phase,
    }
    for key, expected_value in expected.items():
        if value.get(key) != expected_value:
            raise ApexKBError("semantic_result_identity_mismatch", f"{key} does not match the task", {"expected": expected_value, "actual": value.get(key)})


def _validate_citations(citations: list[dict[str, str]], reviews: dict[str, dict[str, Any]], label: str) -> None:
    for citation in citations:
        source_id = citation["source_id"]
        review = reviews.get(source_id)
        if review is None:
            raise ApexKBError("citation_source_invalid", f"{label} cites a source outside the topic candidate set: {source_id}")
        if review["read_status"] == "blocked":
            raise ApexKBError("citation_source_unreadable", f"{label} cites blocked evidence: {source_id}")
        if citation["pointer"] not in review["pointers"]:
            raise ApexKBError(
                "citation_pointer_invalid",
                f"{label} cites a pointer that was not preserved by Phase 1 for {source_id}",
                {"pointer": citation["pointer"], "allowed": review["pointers"]},
            )


def _validate_scoped_pointers(pointers: list[str], allowed_paths: list[str], label: str) -> None:
    invalid = [
        pointer for pointer in pointers
        if not any(pointer == path or pointer.startswith(path + "#") for path in allowed_paths)
    ]
    if invalid:
        raise ApexKBError(
            "semantic_pointer_outside_packet",
            f"{label} contains pointers outside the task packet",
            {"invalid": invalid, "allowed_paths": allowed_paths},
        )


def _repair_file(incoming: Path, task: dict[str, Any], error: ApexKBError) -> Path:
    path = incoming.with_suffix(".repair.json")
    atomic_json(
        path,
        {
            "schema": "apex.kb.semantic-repair.v2",
            "task_id": task["task_id"],
            "topic_id": task["topic_id"],
            "reason_code": error.code,
            "message": "Repair only the declared result file. Do not edit configuration, manifests, state, stage results, wiki pages, retrieval files, or sources.",
            "validation_errors": error.details or [error.message],
            "expected_path": str(incoming),
        },
    )
    return path


def _capsule_markdown(capsule: dict[str, Any]) -> str:
    lines = [
        f"# Source capsule — {capsule['title']}",
        "",
        f"- Source ID: `{capsule['source_id']}`",
        f"- Content hash: `{capsule['content_hash']}`",
        f"- Source path: `{capsule['repository_path']}`",
        f"- Authority: `{capsule['authority']}`",
        f"- Freshness: `{capsule['freshness']}`",
        "",
        "## Summary",
        "",
        capsule["summary"],
        "",
        "## Key claims",
        "",
    ]
    lines.extend(f"- {item}" for item in capsule["key_claims"] or ["None recorded."])
    lines.extend(["", "## Contributions", ""])
    lines.extend(f"- {item}" for item in capsule["contributions"] or ["None recorded."])
    lines.extend(["", "## Contradictions", ""])
    lines.extend(f"- {item}" for item in capsule["contradictions"] or ["None recorded."])
    lines.extend(["", "## Uncertainties", ""])
    lines.extend(f"- {item}" for item in capsule["uncertainties"] or ["None recorded."])
    lines.extend(["", "## Pointers", ""])
    lines.extend(f"- `{item}`" for item in capsule["pointers"] or ["No stable pointer recorded."])
    return "\n".join(lines) + "\n"


def _phase1_markdown(value: dict[str, Any]) -> str:
    analysis = value["topic_analysis"]
    lines = [
        f"# Phase 1 topic analysis — {value['topic_name']}",
        "",
        f"- Topic ID: `{value['topic_id']}`",
        f"- Worker context: `{value['worker_context_id']}`",
        f"- Candidate dispositions: **{len(value['source_reviews'])}**",
        "",
        "## Macro",
        "",
        analysis["macro"],
        "",
        "## Meso",
        "",
        analysis["meso"],
        "",
        "## Micro",
        "",
        analysis["micro"],
        "",
        "## Target answers",
        "",
    ]
    for answer in analysis["target_answers"]:
        lines.extend([f"### {answer['query_id']}", "", answer["answer"], "", "Citations: " + ", ".join(f"`{item}`" for item in answer["citations"]), ""])
    lines.extend(["## Candidate dispositions", ""])
    for review in value["source_reviews"]:
        lines.append(f"- `{review['source_id']}` `{review['repository_path']}` — `{review['disposition']}` / `{review['read_status']}` — {review['summary']}")
    lines.extend(["", "## Contradictions", ""])
    lines.extend(f"- {item}" for item in analysis["contradictions"] or ["None recorded."])
    lines.extend(["", "## Uncertainties", ""])
    lines.extend(f"- {item}" for item in analysis["uncertainties"] or ["None recorded."])
    return "\n".join(lines) + "\n"


def import_phase1_result(run_root: Path, manifest: dict[str, Any], active_task: dict[str, Any]) -> dict[str, Any]:
    incoming = Path(active_task["incoming_path"])
    packet_task = load_json(Path(active_task["packet_dir"]) / "task.json")
    if not incoming.is_file():
        raise ApexKBError("semantic_result_missing", f"Phase 1 result is not present: {incoming}", {"expected_path": str(incoming)})
    try:
        value = load_json(incoming)
        validate_schema(value, "phase1-result.schema.json")
        _validate_identity(value, manifest, packet_task, "phase1")
        expected_ids = set(packet_task["candidate_source_ids"])
        actual_ids = [item["source_id"] for item in value["source_reviews"]]
        if set(actual_ids) != expected_ids or len(actual_ids) != len(set(actual_ids)):
            raise ApexKBError("candidate_disposition_incomplete", "Phase 1 must disposition every candidate exactly once", {"missing": sorted(expected_ids - set(actual_ids)), "unexpected": sorted(set(actual_ids) - expected_ids), "duplicates": sorted({item for item in actual_ids if actual_ids.count(item) > 1})})
        candidates = {item["source_id"]: item for item in load_topic_map(run_root, packet_task["topic_id"])["candidates"]}
        for review in value["source_reviews"]:
            if review["disposition"] not in VALID_DISPOSITIONS:
                raise ApexKBError("source_disposition_invalid", f"Invalid disposition for {review['source_id']}: {review['disposition']}")
            if review["read_status"] not in VALID_READ_STATUS:
                raise ApexKBError("read_status_invalid", f"Invalid read status for {review['source_id']}: {review['read_status']}")
            if review["content_hash"] != candidates[review["source_id"]]["content_hash"] or review["repository_path"] != candidates[review["source_id"]]["repository_path"]:
                raise ApexKBError("source_review_identity_mismatch", f"Source identity mismatch for {review['source_id']}")
            if review["read_status"] == "blocked" and review["disposition"] not in BLOCKED_DISPOSITIONS:
                raise ApexKBError("blocked_source_disposition_invalid", f"Blocked source {review['source_id']} must use a blocked disposition")
            if review["read_status"] != "blocked" and review["disposition"] in BLOCKED_DISPOSITIONS:
                raise ApexKBError("blocked_source_read_status_invalid", f"Blocked disposition for {review['source_id']} requires read_status=blocked")
            if review["read_status"] == "capsule_reused":
                capsule_path = run_root / "ingest-analysis" / "sources" / f"{review['content_hash']}.analysis.json"
                if not capsule_path.is_file():
                    raise ApexKBError("reused_capsule_missing", f"Declared reusable capsule is missing for {review['source_id']}: {capsule_path}")
        material_hashes = {item["content_hash"] for item in value["source_reviews"] if item["disposition"] in MATERIAL_DISPOSITIONS and item["read_status"] != "capsule_reused"}
        review_by_hash = {item["content_hash"]: item for item in value["source_reviews"]}
        capsule_hashes = [item["content_hash"] for item in value["source_capsules"]]
        unexpected_capsules = sorted(set(capsule_hashes) - set(review_by_hash))
        if not material_hashes.issubset(set(capsule_hashes)) or len(capsule_hashes) != len(set(capsule_hashes)) or unexpected_capsules:
            raise ApexKBError("source_capsules_incomplete", "Every newly read material content hash requires exactly one source capsule and no unrelated capsule is allowed", {"missing": sorted(material_hashes - set(capsule_hashes)), "unexpected": unexpected_capsules})
        for capsule in value["source_capsules"]:
            review = review_by_hash[capsule["content_hash"]]
            if capsule["source_id"] not in {item["source_id"] for item in value["source_reviews"] if item["content_hash"] == capsule["content_hash"]}:
                raise ApexKBError("capsule_source_identity_mismatch", f"Capsule source ID is not a reviewed source for hash {capsule['content_hash']}")
            candidate = candidates[capsule["source_id"]]
            if capsule["repository_path"] != candidate["repository_path"]:
                raise ApexKBError("capsule_source_identity_mismatch", f"Capsule path mismatch for {capsule['source_id']}")
        expected_queries = {item["query_id"] for item in packet_task["target_queries"]}
        actual_queries = [item["query_id"] for item in value["topic_analysis"]["target_answers"]]
        if set(actual_queries) != expected_queries or len(actual_queries) != len(set(actual_queries)):
            raise ApexKBError("target_answer_set_incomplete", "Phase 1 must address every locked target query exactly once", {"expected": sorted(expected_queries), "actual": actual_queries})
    except ApexKBError as exc:
        repair = _repair_file(incoming, packet_task, exc)
        raise ApexKBError("semantic_result_invalid", exc.message, {"repair_instruction": str(repair), "validation": exc.details}) from exc
    source_root = run_root / "ingest-analysis" / "sources"
    source_root.mkdir(parents=True, exist_ok=True)
    capsule_paths = []
    for capsule in value["source_capsules"]:
        json_path = source_root / f"{capsule['content_hash']}.analysis.json"
        markdown_path = source_root / f"{capsule['content_hash']}.analysis.md"
        if json_path.is_file():
            existing = load_json(json_path)
            if existing["content_hash"] != capsule["content_hash"]:
                raise ApexKBError("capsule_hash_collision", f"Existing capsule identity mismatch: {json_path}")
        else:
            atomic_json(json_path, capsule)
            atomic_text(markdown_path, _capsule_markdown(capsule))
        capsule_paths.extend([str(json_path.relative_to(run_root)), str(markdown_path.relative_to(run_root))])
    topic_root = run_root / "ingest-analysis" / "topics"
    json_path = topic_root / f"{packet_task['topic_id']}.analysis.json"
    markdown_path = topic_root / f"{packet_task['topic_id']}.analysis.md"
    atomic_json(json_path, value)
    atomic_text(markdown_path, _phase1_markdown(value))
    imported = run_root / manifest["artifact_layout"]["semantic_results"] / incoming.name
    imported.parent.mkdir(parents=True, exist_ok=True)
    atomic_json(imported, value)
    return {
        "topic_id": packet_task["topic_id"],
        "topic_analysis_path": str(json_path.relative_to(run_root)),
        "topic_analysis_markdown": str(markdown_path.relative_to(run_root)),
        "capsule_paths": capsule_paths,
        "worker_context_id": value["worker_context_id"],
        "imported_result": str(imported.relative_to(run_root)),
    }


def create_phase2_packet(run_root: Path, manifest: dict[str, Any], topic_id: str, attempt: int = 1, repair_context: dict[str, Any] | None = None) -> dict[str, Any]:
    topic = _topic(manifest, topic_id)
    topic_map = load_topic_map(run_root, topic_id)
    analysis_path = run_root / "ingest-analysis" / "topics" / f"{topic_id}.analysis.json"
    analysis = load_json(analysis_path)
    task_id = _task_id("phase2", topic_id, attempt)
    packet_dir = _packet_dir(run_root, manifest, task_id)
    incoming = _incoming_path(run_root, manifest, task_id)
    capsule_paths = []
    for review in analysis["source_reviews"]:
        path = run_root / "ingest-analysis" / "sources" / f"{review['content_hash']}.analysis.json"
        if path.is_file():
            capsule_paths.append(str(path))
    task = {
        "schema": "apex.kb.semantic-task.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "task_id": task_id,
        "task_kind": "phase2",
        "topic_id": topic_id,
        "attempt": attempt,
        "semantic_depth": manifest["run_options"]["semantic_depth"],
        "topic": topic,
        "target_queries": topic["target_queries"],
        "candidate_count": topic_map["candidate_count"],
        "candidate_source_ids": [item["source_id"] for item in topic_map["candidates"]],
        "phase1_analysis_path": str(analysis_path),
        "source_capsule_paths": sorted(capsule_paths),
        "required_routes": topic["expected_routes"],
        "required_output_schema": "phase2-result.schema.json",
        "allowed_output_paths": [str(incoming)],
        "forbidden_writes": ["run-config.yaml", "run-manifest.json", "run-state.json", "manifests/**", "derived/**", "source repository paths"],
        "repair_context": repair_context,
        "created_at": utc_now(),
    }
    validate_schema(task, "semantic-task.schema.json")
    body = template("phase2-task.md").format(
        run_id=manifest["run_id"], config_hash=manifest["config_hash"], task_id=task_id, topic_id=topic_id,
        topic_name=topic["name"], candidate_count=topic_map["candidate_count"],
        dossier=topic["expected_routes"]["dossier"], atlas=topic["expected_routes"]["source_atlas"], incoming=str(incoming),
    )
    return _write_packet(packet_dir, task, {"schema": "apex.kb.phase2-inputs.v2", "phase1_analysis": str(analysis_path), "source_capsules": sorted(capsule_paths)}, "phase2-result.schema.json", body, incoming)


def _citation_text(citations: list[dict[str, str]]) -> str:
    return "; ".join(f"`{item['source_id']}` {item['pointer']}" for item in citations) or "No citation recorded"


def _render_dossier(value: dict[str, Any]) -> str:
    dossier = value["dossier"]
    lines = [
        "---",
        f"title: {json.dumps(dossier['title'], ensure_ascii=False)}",
        f"topic_id: {json.dumps(value['topic_id'])}",
        "page_type: concept_dossier",
        "status: accepted_pending_evaluation",
        f"run_id: {json.dumps(value['run_id'])}",
        "---",
        "",
        f"# {dossier['title']}",
        "",
        "## Executive summary",
        "",
        dossier["executive_summary"],
        "",
        "## Macro — Why it matters",
        "",
        dossier["macro"],
        "",
        "## Meso — What it is",
        "",
        dossier["meso"],
        "",
        "## Micro — How it works",
        "",
        dossier["micro"],
        "",
        "## Direct answers",
        "",
    ]
    for answer in dossier["target_answers"]:
        lines.extend([f"### {answer['query_id']}: {answer['question']}", "", answer["answer"], "", f"Evidence: {_citation_text(answer['citations'])}", ""])
    lines.extend(["## Key claims", ""])
    for claim in dossier["key_claims"]:
        lines.append(f"- **{claim['state']}** — {claim['claim']} — {_citation_text(claim['citations'])}")
    lines.extend(["", "## Evolution and versions", ""])
    lines.extend(f"- {item}" for item in dossier["evolution"] or ["No material evolution recorded."])
    lines.extend(["", "## Contradictions", ""])
    lines.extend(f"- {item}" for item in dossier["contradictions"] or ["None recorded."])
    lines.extend(["", "## Uncertainty", ""])
    lines.extend(f"- {item}" for item in dossier["uncertainties"] or ["None recorded."])
    lines.extend(["", "## Routes", "", f"- Source atlas: `{value['atlas']['route']}`"])
    return "\n".join(lines) + "\n"


def _render_atlas(value: dict[str, Any]) -> str:
    atlas = value["atlas"]
    lines = [
        "---",
        f"title: {json.dumps(atlas['title'], ensure_ascii=False)}",
        f"topic_id: {json.dumps(value['topic_id'])}",
        "page_type: source_atlas",
        "status: accepted_pending_evaluation",
        f"run_id: {json.dumps(value['run_id'])}",
        "---",
        "",
        f"# {atlas['title']}",
        "",
        f"This atlas preserves all **{len(atlas['entries'])}** deterministic topic candidates and their semantic dispositions.",
        "",
    ]
    for entry in atlas["entries"]:
        lines.extend(
            [
                f"## {entry['source_id']} — {entry['repository_path']}",
                "",
                f"- Disposition: `{entry['disposition']}`",
                f"- Read status: `{entry['read_status']}`",
                f"- Authority: `{entry['authority']}`",
                f"- Freshness: `{entry['freshness']}`",
                f"- Duplicate/supersession: {entry['duplicate_or_supersession'] or 'None established.'}",
                f"- Value: {entry['individual_value']}",
                f"- Snapshot: {entry['content_snapshot']}",
                f"- Pointers: {', '.join(f'`{pointer}`' for pointer in entry['pointers']) or 'None'}",
                f"- Questions supported: {', '.join(f'`{item}`' for item in entry['questions_supported']) or 'None'}",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def import_phase2_result(run_root: Path, manifest: dict[str, Any], active_task: dict[str, Any]) -> dict[str, Any]:
    incoming = Path(active_task["incoming_path"])
    task = load_json(Path(active_task["packet_dir"]) / "task.json")
    if not incoming.is_file():
        raise ApexKBError("semantic_result_missing", f"Phase 2 result is not present: {incoming}", {"expected_path": str(incoming)})
    try:
        value = load_json(incoming)
        validate_schema(value, "phase2-result.schema.json")
        _validate_identity(value, manifest, task, "phase2")
        expected_query_map = {item["query_id"]: item["question"] for item in task["target_queries"]}
        expected_queries = set(expected_query_map)
        answers = [item["query_id"] for item in value["dossier"]["target_answers"]]
        if set(answers) != expected_queries or len(answers) != len(set(answers)):
            raise ApexKBError("target_answer_set_incomplete", "Dossier must answer every locked target query exactly once", {"expected": sorted(expected_queries), "actual": answers})
        expected_candidates = set(task["candidate_source_ids"])
        atlas_ids = [item["source_id"] for item in value["atlas"]["entries"]]
        if set(atlas_ids) != expected_candidates or len(atlas_ids) != len(set(atlas_ids)):
            raise ApexKBError("source_atlas_incomplete", "Source atlas must preserve every Phase 0 candidate exactly once", {"missing": sorted(expected_candidates - set(atlas_ids)), "unexpected": sorted(set(atlas_ids) - expected_candidates)})
        phase1 = load_json(Path(task["phase1_analysis_path"]))
        review_by_id = {item["source_id"]: item for item in phase1["source_reviews"]}
        for answer in value["dossier"]["target_answers"]:
            expected_question = expected_query_map[answer["query_id"]]
            if answer["question"] != expected_question:
                raise ApexKBError(
                    "target_question_text_mismatch",
                    f"Dossier question text differs from the locked task for {answer['query_id']}",
                    {"expected": expected_question, "actual": answer["question"]},
                )
            _validate_citations(answer["citations"], review_by_id, f"Answer {answer['query_id']}")
        for index, claim in enumerate(value["dossier"]["key_claims"], 1):
            _validate_citations(claim["citations"], review_by_id, f"Key claim {index}")
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
    except ApexKBError as exc:
        repair = _repair_file(incoming, task, exc)
        raise ApexKBError("semantic_result_invalid", exc.message, {"repair_instruction": str(repair), "validation": exc.details}) from exc
    dossier_path = run_root / value["dossier"]["route"]
    atlas_path = run_root / value["atlas"]["route"]
    atomic_text(dossier_path, _render_dossier(value))
    atomic_text(atlas_path, _render_atlas(value))
    imported = run_root / manifest["artifact_layout"]["semantic_results"] / incoming.name
    imported.parent.mkdir(parents=True, exist_ok=True)
    atomic_json(imported, value)
    return {
        "topic_id": task["topic_id"],
        "dossier_path": str(dossier_path.relative_to(run_root)),
        "atlas_path": str(atlas_path.relative_to(run_root)),
        "worker_context_id": value["worker_context_id"],
        "imported_result": str(imported.relative_to(run_root)),
    }


def create_acceptance_packet(run_root: Path, manifest: dict[str, Any], topic_id: str, drafting_context_id: str, attempt: int = 1) -> dict[str, Any]:
    topic = _topic(manifest, topic_id)
    task_id = _task_id("acceptance", topic_id, attempt)
    packet_dir = _packet_dir(run_root, manifest, task_id)
    incoming = _incoming_path(run_root, manifest, task_id)
    page_paths = [str(run_root / topic["expected_routes"]["dossier"]), str(run_root / topic["expected_routes"]["source_atlas"])]
    phase1 = load_json(run_root / "ingest-analysis" / "topics" / f"{topic_id}.analysis.json")
    evidence_paths = sorted(
        {
            str(path)
            for review in phase1["source_reviews"]
            for path in [run_root / "ingest-analysis" / "sources" / f"{review['content_hash']}.analysis.json"]
            if path.is_file()
        }
    )
    task = {
        "schema": "apex.kb.semantic-task.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "task_id": task_id,
        "task_kind": "acceptance",
        "topic_id": topic_id,
        "attempt": attempt,
        "semantic_depth": manifest["run_options"]["semantic_depth"],
        "topic": topic,
        "target_queries": topic["target_queries"],
        "drafting_context_id": drafting_context_id,
        "page_paths": page_paths,
        "evidence_paths": evidence_paths,
        "fresh_context_contract": "The application verifies only that evaluator_context_id differs from drafting_context_id. The operator or execution environment must provision a genuinely independent fresh evaluator context.",
        "required_output_schema": "acceptance-result.schema.json",
        "allowed_output_paths": [str(incoming)],
        "forbidden_writes": ["all paths except the declared incoming result"],
        "created_at": utc_now(),
    }
    validate_schema(task, "semantic-task.schema.json")
    body = template("acceptance-task.md").format(
        run_id=manifest["run_id"], config_hash=manifest["config_hash"], task_id=task_id, topic_id=topic_id,
        drafting_context_id=drafting_context_id, pages="\n".join(f"- `{item}`" for item in page_paths), incoming=str(incoming),
    )
    return _write_packet(packet_dir, task, {"schema": "apex.kb.acceptance-inputs.v2", "compiled_pages": page_paths, "resolved_evidence": task["evidence_paths"]}, "acceptance-result.schema.json", body, incoming)


def import_acceptance_result(run_root: Path, manifest: dict[str, Any], active_task: dict[str, Any]) -> dict[str, Any]:
    incoming = Path(active_task["incoming_path"])
    task = load_json(Path(active_task["packet_dir"]) / "task.json")
    if not incoming.is_file():
        raise ApexKBError("semantic_result_missing", f"Acceptance result is not present: {incoming}", {"expected_path": str(incoming)})
    try:
        value = load_json(incoming)
        validate_schema(value, "acceptance-result.schema.json")
        _validate_identity(value, manifest, task, "acceptance")
        if value["evaluator_context_id"] == task["drafting_context_id"]:
            raise ApexKBError("acceptance_context_not_fresh", "Acceptance evaluator context must differ from the Phase 2 drafting context")
        expected_queries = {item["query_id"] for item in task["target_queries"] if item["priority"] in {"critical", "routine"}}
        actual_ids = [item["query_id"] for item in value["question_evaluations"]]
        actual = {item["query_id"]: item for item in value["question_evaluations"]}
        if set(actual_ids) != expected_queries or len(actual_ids) != len(set(actual_ids)):
            raise ApexKBError(
                "acceptance_question_set_invalid",
                "Acceptance must evaluate every critical/routine query exactly once and no others",
                {"expected": sorted(expected_queries), "actual": actual_ids},
            )
        for item in value["question_evaluations"]:
            _validate_scoped_pointers(item["page_pointers"], task["page_paths"], f"Question {item['query_id']}")
        for index, claim in enumerate(value["claim_checks"], 1):
            _validate_scoped_pointers(claim["evidence_pointers"], task["evidence_paths"], f"Claim check {index}")
        if value["verdict"] == "semantic_pass":
            failed = [query_id for query_id in expected_queries if actual[query_id]["verdict"] != "pass" or actual[query_id]["raw_source_required"]]
            claim_failures = [item for item in value["claim_checks"] if item["verdict"] != "pass"]
            if not value["claim_checks"] or failed or claim_failures:
                raise ApexKBError("semantic_pass_not_supported", "semantic_pass requires a non-empty material-claim sample and all critical/routine questions and sampled claims to pass without raw-source reopening", {"questions": failed, "claim_failures": claim_failures, "claim_check_count": len(value["claim_checks"])})
    except ApexKBError as exc:
        repair = _repair_file(incoming, task, exc)
        raise ApexKBError("semantic_result_invalid", exc.message, {"repair_instruction": str(repair), "validation": exc.details}) from exc
    destination = run_root / "audit" / "semantic-acceptance" / manifest["run_id"] / f"{task['topic_id']}.json"
    atomic_json(destination, value)
    imported = run_root / manifest["artifact_layout"]["semantic_results"] / incoming.name
    imported.parent.mkdir(parents=True, exist_ok=True)
    atomic_json(imported, value)
    return {
        "topic_id": task["topic_id"],
        "verdict": value["verdict"],
        "acceptance_path": str(destination.relative_to(run_root)),
        "evaluator_context_id": value["evaluator_context_id"],
        "failed_items": value.get("failed_items", []),
        "imported_result": str(imported.relative_to(run_root)),
    }
