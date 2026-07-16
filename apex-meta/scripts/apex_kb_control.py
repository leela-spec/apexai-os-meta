#!/usr/bin/env python3
"""Deterministic Apex KB control plane.

This module is deliberately a delegated implementation detail of ``apex_kb.py``.
It owns run intent/state, legal transitions, exact next-command derivation,
semantic packet rendering, restart/reconciliation, input drift detection, and
read-only Git/worktree classification. Existing Apex KB domain commands remain
owned by ``apex_kb.py`` and are called in-process; this module never copies their
corpus, retrieval, lint, quality, or postflight logic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple


RUN_INTENT_SCHEMA = "apex.kb.run-intent.v1"
RUN_STATE_SCHEMA = "apex.kb.run-state.v1"
STAGE_RESULT_SCHEMA = "apex.kb.stage-result.v1"
PACKET_SCHEMA = "apex.kb.semantic-handoff-packet.v1"

RUN_INTENT_PATH = Path("manifests/run-intent.md")
RUN_STATE_PATH = Path("manifests/run-state.json")
TOPIC_REGISTRY_PATH = Path("manifests/topic-registry.json")
SOURCE_MANIFEST_PATH = Path("manifests/source-manifest.json")
SOURCE_PAYLOAD_MANIFEST_PATH = Path("manifests/source-payload-manifest.json")
PHASE0_RANKINGS_PATH = Path("manifests/phase0/topic-source-rankings.json")
RUN_LOG_ROOT = Path("log/runs")

OUTPUT_TIERS = (
    "source_only",
    "analysis_only",
    "compiled_minimal",
    "compiled_full",
    "query_ready",
)
EXECUTION_ROUTES = ("terminal_backed", "connector_only", "unsupported")
CONTROLLED_DIRECT_COMMANDS = {
    "scaffold",
    "source-intake",
    "generate-source-payload-manifest",
    "source-payload-manifest",
    "payload-manifest",
    "phase0",
    "ingest-phase1",
    "ingest-phase2",
    "index",
    "postflight",
}
SEMANTIC_STAGE_BASES = {"phase1", "phase2", "semantic_acceptance"}
GLOBAL_STAGE_ORDER = (
    "scaffold",
    "intent_lock",
    "preflight",
    "source_intake",
    "phase0",
    "phase1",
    "phase2",
    "semantic_acceptance",
    "postflight",
    "complete",
)


class ControlError(RuntimeError):
    """Reason-coded deterministic control-plane failure."""

    def __init__(self, code: str, message: str, *, paths: Optional[Sequence[str]] = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.paths = list(paths or [])


# ---------------------------------------------------------------------------
# Paths, atomic IO, fingerprints
# ---------------------------------------------------------------------------


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def repository_root() -> Path:
    return Path(__file__).resolve().parents[2]


def skill_root() -> Path:
    return repository_root() / ".claude" / "skills" / "apex-kb"


def schema_path(name: str) -> Path:
    return skill_root() / "references" / name


def template_path(name: str) -> Path:
    return skill_root() / "templates" / name


def resolve_kb_root(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = repository_root() / path
    return path.resolve()


def ensure_inside(root: Path, path: Path) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise ControlError("path_outside_kb_root", f"Path is outside KB root: {path}", paths=[str(path)]) from exc


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        with temp.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError as exc:
        raise ControlError("required_file_missing", f"Required JSON file is missing: {path}", paths=[str(path)]) from exc
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        raise ControlError("invalid_json", f"JSON file is unreadable: {path}: {exc}", paths=[str(path)]) from exc


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_path(path: Path) -> str:
    if path.is_file():
        return sha256_file(path)
    if path.is_dir():
        digest = hashlib.sha256()
        for item in sorted((p for p in path.rglob("*") if p.is_file()), key=lambda p: p.as_posix().lower()):
            rel = item.relative_to(path).as_posix()
            digest.update(rel.encode("utf-8"))
            digest.update(b"\0")
            digest.update(sha256_file(item).encode("ascii"))
            digest.update(b"\0")
        return digest.hexdigest()
    raise ControlError("fingerprint_input_missing", f"Cannot fingerprint missing path: {path}", paths=[str(path)])


def path_key(kb_root: Path, path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(kb_root.resolve()).as_posix()
    except ValueError:
        pass
    try:
        return "repo://" + resolved.relative_to(repository_root()).as_posix()
    except ValueError:
        return str(resolved)


def resolve_path_key(kb_root: Path, key: str) -> Path:
    if key.startswith("repo://"):
        return repository_root() / key[len("repo://") :]
    candidate = Path(key)
    if candidate.is_absolute():
        return candidate
    return kb_root / candidate


def rel_or_abs(kb_root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(kb_root.resolve()).as_posix()
    except ValueError:
        try:
            return "repo://" + path.resolve().relative_to(repository_root()).as_posix()
        except ValueError:
            return str(path.resolve())


# ---------------------------------------------------------------------------
# JSON Schema subset validator. Schema documents are canonical owners.
# ---------------------------------------------------------------------------


def load_schema(name: str) -> Dict[str, Any]:
    value = read_json(schema_path(name))
    if not isinstance(value, dict):
        raise ControlError("schema_invalid", f"Schema root must be an object: {name}")
    return value


def _resolve_json_pointer(root: Dict[str, Any], ref: str) -> Dict[str, Any]:
    if not ref.startswith("#/"):
        raise ControlError("unsupported_schema_ref", f"Only local JSON Schema refs are supported: {ref}")
    current: Any = root
    for token in ref[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or token not in current:
            raise ControlError("schema_ref_missing", f"JSON Schema ref does not resolve: {ref}")
        current = current[token]
    if not isinstance(current, dict):
        raise ControlError("schema_ref_invalid", f"JSON Schema ref is not an object: {ref}")
    return current


def _type_matches(value: Any, expected: str) -> bool:
    if expected == "null":
        return value is None
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


def validate_schema(value: Any, schema: Dict[str, Any], *, root: Optional[Dict[str, Any]] = None, location: str = "$") -> List[str]:
    root = root or schema
    errors: List[str] = []
    if "$ref" in schema:
        return validate_schema(value, _resolve_json_pointer(root, str(schema["$ref"])), root=root, location=location)
    if "const" in schema and value != schema["const"]:
        errors.append(f"{location}: expected const {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{location}: value {value!r} is not in enum")
    expected_type = schema.get("type")
    if expected_type is not None:
        expected_types = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(_type_matches(value, str(item)) for item in expected_types):
            errors.append(f"{location}: expected type {expected_types}, got {type(value).__name__}")
            return errors
    if isinstance(value, str):
        if len(value) < int(schema.get("minLength", 0)):
            errors.append(f"{location}: string shorter than minLength")
        pattern = schema.get("pattern")
        if pattern and re.search(str(pattern), value) is None:
            errors.append(f"{location}: string does not match pattern {pattern!r}")
    if isinstance(value, (int, float)) and not isinstance(value, bool) and "minimum" in schema:
        if value < schema["minimum"]:
            errors.append(f"{location}: value is below minimum {schema['minimum']}")
    if isinstance(value, list):
        if len(value) < int(schema.get("minItems", 0)):
            errors.append(f"{location}: array shorter than minItems")
        if schema.get("uniqueItems"):
            rendered = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in value]
            if len(rendered) != len(set(rendered)):
                errors.append(f"{location}: array items are not unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, item in enumerate(value):
                errors.extend(validate_schema(item, item_schema, root=root, location=f"{location}[{index}]"))
    if isinstance(value, dict):
        if len(value) < int(schema.get("minProperties", 0)):
            errors.append(f"{location}: object has fewer than minProperties")
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{location}: missing required property {key!r}")
        properties = schema.get("properties", {})
        if isinstance(properties, dict):
            for key, property_schema in properties.items():
                if key in value and isinstance(property_schema, dict):
                    errors.extend(validate_schema(value[key], property_schema, root=root, location=f"{location}.{key}"))
        extras = set(value) - set(properties if isinstance(properties, dict) else {})
        additional = schema.get("additionalProperties", True)
        if additional is False and extras:
            errors.append(f"{location}: unexpected properties {sorted(extras)}")
        elif isinstance(additional, dict):
            for key in sorted(extras):
                errors.extend(validate_schema(value[key], additional, root=root, location=f"{location}.{key}"))
    return errors


def require_schema(value: Any, schema_name: str) -> None:
    schema = load_schema(schema_name)
    errors = validate_schema(value, schema)
    if errors:
        raise ControlError("schema_validation_failed", f"{schema_name}: " + "; ".join(errors[:20]))


# ---------------------------------------------------------------------------
# Run intent/state and compact results
# ---------------------------------------------------------------------------


def stage_result(
    run_id: str,
    stage: str,
    status: str,
    *,
    reason_code: Optional[str] = None,
    artifact: Any = None,
    next_stage: Optional[str] = None,
    operator_action: Optional[str] = None,
) -> Dict[str, Any]:
    result = {
        "schema": STAGE_RESULT_SCHEMA,
        "run_id": run_id,
        "stage": stage,
        "status": status,
        "reason_code": reason_code,
        "artifact": artifact,
        "next_stage": next_stage,
        "operator_action": operator_action,
    }
    require_schema(result, "stage-result.schema.json")
    return result


def parse_run_intent(path: Path) -> Tuple[Dict[str, Any], str]:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except FileNotFoundError as exc:
        raise ControlError("run_intent_missing", f"Run intent is missing: {path}", paths=[str(path)]) from exc
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ControlError("run_intent_frontmatter_missing", f"Run intent must start with JSON-compatible YAML frontmatter: {path}")
    end = next((index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"), None)
    if end is None:
        raise ControlError("run_intent_frontmatter_malformed", f"Run intent frontmatter is not closed: {path}")
    frontmatter = "\n".join(lines[1:end]).strip()
    try:
        intent = json.loads(frontmatter)
    except json.JSONDecodeError as exc:
        raise ControlError("run_intent_not_json_compatible", f"Run intent frontmatter must remain JSON-compatible YAML: {exc}") from exc
    if not isinstance(intent, dict):
        raise ControlError("run_intent_invalid", "Run intent frontmatter must be an object")
    require_schema(intent, "run-intent.schema.json")
    return intent, "\n".join(lines[end + 1 :])


def render_run_intent(intent: Dict[str, Any]) -> str:
    template = template_path("run-intent-template.md").read_text(encoding="utf-8")
    return template.replace("{{RUN_INTENT_JSON}}", json.dumps(intent, indent=2, ensure_ascii=False, sort_keys=True)).replace("{{RUN_ID}}", intent["run_id"])


def load_state(kb_root: Path) -> Dict[str, Any]:
    state = read_json(kb_root / RUN_STATE_PATH)
    if not isinstance(state, dict):
        raise ControlError("run_state_invalid", "Run state root must be an object")
    require_schema(state, "run-state.schema.json")
    return state


def save_state(kb_root: Path, state: MutableMapping[str, Any], *, increment: bool = True) -> None:
    updated = dict(state)
    if increment:
        updated["revision"] = int(updated.get("revision", 0)) + 1
    updated["updated_at"] = utc_now()
    require_schema(updated, "run-state.schema.json")
    atomic_write_json(kb_root / RUN_STATE_PATH, updated)
    state.clear()
    state.update(updated)


def persist_state_and_result(kb_root: Path, state: MutableMapping[str, Any], result: Dict[str, Any], *, initial: bool = False) -> None:
    require_schema(result, "stage-result.schema.json")
    sequence = int(state.get("revision", 1) if initial else int(state.get("revision", 0)) + 1)
    safe_stage = re.sub(r"[^A-Za-z0-9._-]+", "-", str(result["stage"]))
    result_rel = RUN_LOG_ROOT / state["run_id"] / "stage-results" / f"{sequence:04d}-{safe_stage}.json"
    atomic_write_json(kb_root / result_rel, result)
    state.setdefault("artifact_references", {})[f"stage_result_{sequence:04d}"] = result_rel.as_posix()
    save_state(kb_root, state, increment=not initial)


def blocked_reason(code: str, message: str, *, action: Optional[str] = None, paths: Optional[Sequence[str]] = None) -> Dict[str, Any]:
    return {"code": code, "message": message, "action": action, "paths": list(paths or [])}


def set_blocked(state: MutableMapping[str, Any], code: str, message: str, *, action: Optional[str] = None, paths: Optional[Sequence[str]] = None) -> None:
    state["blocked_reason"] = blocked_reason(code, message, action=action, paths=paths)
    state["truthful_state"] = "partial"


def set_waiting(state: MutableMapping[str, Any], code: str, message: str, *, action: Optional[str] = None, paths: Optional[Sequence[str]] = None) -> None:
    state["blocked_reason"] = blocked_reason(code, message, action=action, paths=paths)


def clear_blocked(state: MutableMapping[str, Any]) -> None:
    state["blocked_reason"] = None
    if state.get("truthful_state") == "partial":
        state["truthful_state"] = "initialized"


def _run_intent_path(kb_root: Path) -> Path:
    return kb_root / RUN_INTENT_PATH


def _run_state_path(kb_root: Path) -> Path:
    return kb_root / RUN_STATE_PATH


def _load_topic_registry(kb_root: Path) -> List[Dict[str, Any]]:
    path = kb_root / TOPIC_REGISTRY_PATH
    if not path.exists():
        return []
    value = read_json(path)
    if isinstance(value, dict):
        topics = value.get("topics", [])
        return [item for item in topics if isinstance(item, dict)] if isinstance(topics, list) else []
    return []


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-") or "topic"


def _topic_states(kb_root: Path, requested: Sequence[str]) -> List[Dict[str, Any]]:
    registry = _load_topic_registry(kb_root)
    registry_by_slug = {_slug(str(item.get("slug") or item.get("name") or "topic")): item for item in registry}
    requested_slugs = list(dict.fromkeys(requested))
    missing = [slug for slug in requested_slugs if slug not in registry_by_slug]
    if missing:
        raise ControlError(
            "topic_registry_entry_missing",
            "Every requested topic must exist in manifests/topic-registry.json before control init",
            paths=[f"{TOPIC_REGISTRY_PATH.as_posix()}#{slug}" for slug in missing],
        )
    slugs = requested_slugs or list(registry_by_slug)
    topics: List[Dict[str, Any]] = []
    for slug in slugs:
        item = registry_by_slug.get(slug, {})
        expected: List[str] = []
        for query in item.get("target_queries", []) if isinstance(item.get("target_queries"), list) else []:
            if isinstance(query, dict) and query.get("expected_page"):
                expected.append(str(query["expected_page"]).split("#", 1)[0])
        if item.get("target_page"):
            expected.append(str(item["target_page"]).split("#", 1)[0])
        if not expected:
            expected.append(f"wiki/summaries/{slug}.md")
        topics.append(
            {
                "slug": slug,
                "name": str(item.get("name") or slug.replace("-", " ").title()),
                "expected_pages": sorted(dict.fromkeys(expected)),
                "status": "not_started",
            }
        )
    return topics


def _scaffold_complete(kb_root: Path) -> bool:
    required = (
        kb_root / "README.md",
        kb_root / "kb-schema.md",
        kb_root / "wiki" / "index.md",
        kb_root / SOURCE_MANIFEST_PATH,
    )
    return all(path.exists() for path in required)


def _parse_source_specs(values: Sequence[str]) -> List[Dict[str, Any]]:
    specs: List[Dict[str, Any]] = []
    for raw in values:
        try:
            item = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ControlError("source_spec_invalid", f"--source-spec must be a JSON object: {exc}") from exc
        if not isinstance(item, dict):
            raise ControlError("source_spec_invalid", "--source-spec must be a JSON object")
        normalized = {
            "path": item.get("path"),
            "pointer": item.get("pointer"),
            "storage_mode": item.get("storage_mode", "pointer_only"),
            "source_type": item.get("source_type", "other"),
            "source_id": item.get("source_id"),
            "title": item.get("title"),
            "as_version": bool(item.get("as_version", False)),
            "allow_duplicate": bool(item.get("allow_duplicate", False)),
        }
        if not normalized["path"] and not normalized["pointer"]:
            raise ControlError("source_spec_invalid", "Each --source-spec needs path or pointer")
        specs.append(normalized)
    return specs


def _intent_from_args(args: argparse.Namespace, kb_root: Path) -> Dict[str, Any]:
    source_roots = list(dict.fromkeys(str(item) for item in (args.source_root or [])))
    source_inputs = _parse_source_specs(args.source_spec or [])
    topic_slugs = list(dict.fromkeys(_slug(item) for item in (args.topic_slug or [])))
    phase1_min_coverage = getattr(args, "phase1_min_coverage", None)
    if phase1_min_coverage is None:
        phase1_min_coverage = 0.6
    now = utc_now()
    return {
        "schema": RUN_INTENT_SCHEMA,
        "schema_version": "1",
        "run_id": args.run_id,
        "kb_root": args.kb_root,
        "kb_slug": kb_root.name,
        "mode": args.mode,
        "operator_intent": args.operator_intent,
        "kb_identity": args.kb_identity,
        "source_locus": args.source_locus,
        "source_roots": source_roots,
        "source_inputs": source_inputs,
        "out_of_scope": list(args.out_of_scope or []),
        "success_definition": args.success_definition,
        "output_tier": args.output_tier,
        "output_tier_rationale": args.output_tier_rationale,
        "execution_route": args.execution_route,
        "corpus_breadth": args.corpus_breadth,
        "broad_breadth_reason": args.broad_breadth_reason,
        "phase1_min_coverage": phase1_min_coverage,
        "topic_slugs": topic_slugs,
        "topic_sanity_check": {},
        "operator_confirmed": False,
        "operator_confirmation_quote": "",
        "confirmed_at": None,
        "target_repository": args.target_repository,
        "target_commit": args.target_commit,
        "created_at": now,
        "updated_at": now,
    }


def _initial_state(intent: Dict[str, Any], kb_root: Path, title: Optional[str]) -> Dict[str, Any]:
    topics = _topic_states(kb_root, intent["topic_slugs"])
    if intent["output_tier"] != "source_only" and not topics:
        raise ControlError("topics_required", "At least one topic is required for analysis or compiled output tiers")
    stage = "intent_lock" if _scaffold_complete(kb_root) else "scaffold"
    now = utc_now()
    return {
        "schema": RUN_STATE_SCHEMA,
        "schema_version": "1",
        "run_id": intent["run_id"],
        "kb_root": intent["kb_root"],
        "kb_title": title or intent["kb_identity"],
        "mode": intent["mode"],
        "source_roots": intent["source_roots"],
        "source_inputs": intent["source_inputs"],
        "target_repository": intent["target_repository"],
        "target_commit": intent.get("target_commit"),
        "execution_route": intent["execution_route"],
        "topics": topics,
        "output_tier": intent["output_tier"],
        "phase1_min_coverage": intent.get("phase1_min_coverage", 0.6),
        "operator_confirmation": {"confirmed": False, "quote": "", "confirmed_at": None},
        "current_stage": stage,
        "completed_stages": [],
        "blocked_reason": None,
        "next_legal_stage": stage,
        "artifact_references": {
            "run_intent": RUN_INTENT_PATH.as_posix(),
            "run_state": RUN_STATE_PATH.as_posix(),
        },
        "input_fingerprints": {},
        "truthful_state": "initialized",
        "revision": 1,
        "created_at": now,
        "updated_at": now,
    }


# ---------------------------------------------------------------------------
# Stage model, transitions, drift and recovery
# ---------------------------------------------------------------------------


def _completed(state: Mapping[str, Any], stage: str) -> bool:
    return stage in state.get("completed_stages", [])


def _topic_slugs(state: Mapping[str, Any]) -> List[str]:
    return [str(item["slug"]) for item in state.get("topics", []) if isinstance(item, dict) and item.get("slug")]


def _topic(state: Mapping[str, Any], slug: str) -> Dict[str, Any]:
    for item in state.get("topics", []):
        if isinstance(item, dict) and item.get("slug") == slug:
            return item
    raise ControlError("topic_not_in_run", f"Topic is not in run state: {slug}")


def _update_topic_status(state: MutableMapping[str, Any], stage: str) -> None:
    if ":" not in stage:
        return
    base, slug = stage.split(":", 1)
    item = _topic(state, slug)
    item["status"] = {
        "phase1": "phase1_complete",
        "phase2": "phase2_complete",
        "semantic_acceptance": "accepted",
    }.get(base, item.get("status", "not_started"))


def mark_stage_complete(state: MutableMapping[str, Any], stage: str) -> None:
    completed = state.setdefault("completed_stages", [])
    if stage not in completed:
        completed.append(stage)
    _update_topic_status(state, stage)
    state["blocked_reason"] = None


def _truthful_completion(output_tier: str) -> str:
    if output_tier == "source_only":
        return "source_only_complete"
    if output_tier == "analysis_only":
        return "analysis_complete_unvalidated"
    if output_tier in {"compiled_minimal", "compiled_full"}:
        return "compiled_unvalidated"
    return "query_ready"


def compute_next_stage(state: Mapping[str, Any]) -> str:
    if not _completed(state, "scaffold"):
        return "scaffold"
    if not bool(state.get("operator_confirmation", {}).get("confirmed")):
        return "intent_lock"
    if not _completed(state, "intent_lock"):
        return "intent_lock"
    if state.get("mode") == "scaffold":
        return "complete"
    if not _completed(state, "preflight"):
        return "preflight"
    if not _completed(state, "source_intake"):
        return "source_intake"
    if state["output_tier"] == "source_only":
        return "complete"
    if not _completed(state, "phase0"):
        return "phase0"
    for slug in _topic_slugs(state):
        stage = f"phase1:{slug}"
        if not _completed(state, stage):
            return stage
    if state["output_tier"] == "analysis_only":
        return "complete"
    for slug in _topic_slugs(state):
        stage = f"phase2:{slug}"
        if not _completed(state, stage):
            return stage
    for slug in _topic_slugs(state):
        stage = f"semantic_acceptance:{slug}"
        if not _completed(state, stage):
            return stage
    if state["output_tier"] in {"compiled_minimal", "compiled_full"}:
        return "complete"
    if not _completed(state, "postflight"):
        return "postflight"
    return "complete"


def refresh_stage(state: MutableMapping[str, Any]) -> str:
    next_stage = compute_next_stage(state)
    state["current_stage"] = next_stage
    state["next_legal_stage"] = None if next_stage == "complete" else next_stage
    if next_stage == "complete":
        if not _completed(state, "complete"):
            state.setdefault("completed_stages", []).append("complete")
        state["truthful_state"] = _truthful_completion(str(state["output_tier"]))
        state["blocked_reason"] = None
    return next_stage


def record_fingerprint(state: MutableMapping[str, Any], kb_root: Path, path: Path, invalidate_from: str) -> None:
    if not path.exists():
        return
    state.setdefault("input_fingerprints", {})[path_key(kb_root, path)] = {
        "sha256": sha256_path(path),
        "invalidate_from": invalidate_from,
        "recorded_at": utc_now(),
    }


def detect_drift(state: Mapping[str, Any], kb_root: Path) -> List[Dict[str, str]]:
    changes: List[Dict[str, str]] = []
    for key, record in state.get("input_fingerprints", {}).items():
        if not isinstance(record, dict):
            continue
        path = resolve_path_key(kb_root, str(key))
        current = sha256_path(path) if path.exists() else "missing"
        if current != record.get("sha256"):
            changes.append(
                {
                    "path": str(key),
                    "expected": str(record.get("sha256")),
                    "actual": current,
                    "invalidate_from": str(record.get("invalidate_from") or "phase0"),
                }
            )
    return changes


def _reset_topic_statuses(state: MutableMapping[str, Any]) -> None:
    completed = set(state.get("completed_stages", []))
    for item in state.get("topics", []):
        if not isinstance(item, dict):
            continue
        slug = item["slug"]
        if f"semantic_acceptance:{slug}" in completed:
            item["status"] = "accepted"
        elif f"phase2:{slug}" in completed:
            item["status"] = "phase2_complete"
        elif f"phase1:{slug}" in completed:
            item["status"] = "phase1_complete"
        else:
            item["status"] = "not_started"


def invalidate_from(state: MutableMapping[str, Any], invalidate_stage: str) -> None:
    completed = list(state.get("completed_stages", []))
    if invalidate_stage == "intent_lock":
        keep = {stage for stage in completed if stage == "scaffold"}
        state["operator_confirmation"] = {"confirmed": False, "quote": "", "confirmed_at": None}
    elif invalidate_stage in {"source_intake", "phase0"}:
        keep = {stage for stage in completed if stage in {"scaffold", "intent_lock", "preflight", "source_intake"}}
        if invalidate_stage == "source_intake":
            keep.discard("source_intake")
    elif invalidate_stage == "phase1":
        keep = {
            stage
            for stage in completed
            if not (
                stage.startswith("phase1:")
                or stage.startswith("phase2:")
                or stage.startswith("semantic_acceptance:")
                or stage in {"postflight", "complete"}
            )
        }
    elif invalidate_stage.startswith("phase1:"):
        _, slug = invalidate_stage.split(":", 1)
        keep = {
            stage
            for stage in completed
            if stage not in {f"phase1:{slug}", f"phase2:{slug}", f"semantic_acceptance:{slug}", "postflight", "complete"}
        }
    elif invalidate_stage.startswith("phase2:"):
        _, slug = invalidate_stage.split(":", 1)
        keep = {
            stage
            for stage in completed
            if stage not in {f"phase2:{slug}", f"semantic_acceptance:{slug}", "postflight", "complete"}
        }
    elif invalidate_stage.startswith("semantic_acceptance:"):
        _, slug = invalidate_stage.split(":", 1)
        keep = {stage for stage in completed if stage not in {f"semantic_acceptance:{slug}", "postflight", "complete"}}
    else:
        keep = {stage for stage in completed if stage not in {"postflight", "complete"}}
    state["completed_stages"] = [stage for stage in completed if stage in keep]
    state["truthful_state"] = "initialized"
    state["blocked_reason"] = None
    _reset_topic_statuses(state)
    refresh_stage(state)


# ---------------------------------------------------------------------------
# Exact command derivation and operator readback
# ---------------------------------------------------------------------------


def ps_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def _control_command(state: Mapping[str, Any], action: str, extra: str = "") -> str:
    root = ps_quote(str(state["kb_root"]))
    suffix = f" {extra.strip()}" if extra.strip() else ""
    return f"python apex-meta/scripts/apex_kb.py --kb-root {root} --allow-write --json control {action}{suffix}"


def _packet_rel(state: Mapping[str, Any], stage: str, slug: str, extension: str) -> Path:
    return RUN_LOG_ROOT / str(state["run_id"]) / "packets" / f"{stage}-{slug}.{extension}"


def derive_next_result(state: Mapping[str, Any], kb_root: Path) -> Dict[str, Any]:
    next_stage = compute_next_stage(state)
    if state.get("blocked_reason"):
        reason = state["blocked_reason"]
        waiting_status = {
            "operator_confirmation_required": "needs_operator",
            "semantic_executor_required": "needs_semantic_executor",
        }.get(str(reason["code"]), "blocked")
        return stage_result(
            str(state["run_id"]),
            str(state["current_stage"]),
            waiting_status,
            reason_code=str(reason["code"]),
            artifact=(reason.get("paths") or [RUN_STATE_PATH.as_posix()])[0],
            next_stage=str(state.get("next_legal_stage") or state["current_stage"]),
            operator_action=reason.get("action"),
        )
    if next_stage == "complete":
        return stage_result(
            str(state["run_id"]),
            "complete",
            "ok",
            artifact=RUN_STATE_PATH.as_posix(),
            next_stage=None,
            operator_action=None,
        )
    if next_stage == "intent_lock":
        readback = RUN_LOG_ROOT / str(state["run_id"]) / "operator-readback.md"
        if (kb_root / readback).exists():
            action = _control_command(state, "confirm", "--confirmation-quote '<operator affirmative>'")
        else:
            action = _control_command(state, "run")
        return stage_result(
            str(state["run_id"]),
            next_stage,
            "needs_operator",
            reason_code="operator_confirmation_required",
            artifact=readback.as_posix() if (kb_root / readback).exists() else RUN_INTENT_PATH.as_posix(),
            next_stage=next_stage,
            operator_action=action,
        )
    base, _, slug = next_stage.partition(":")
    if base in SEMANTIC_STAGE_BASES and slug:
        packet_md = _packet_rel(state, base, slug, "md")
        if (kb_root / packet_md).exists():
            trigger = f"Execute the Apex KB packet at {packet_md.as_posix()}; write only the declared outputs; return the completion response exactly."
            return stage_result(
                str(state["run_id"]),
                next_stage,
                "needs_semantic_executor",
                reason_code="semantic_executor_required",
                artifact=packet_md.as_posix(),
                next_stage=next_stage,
                operator_action=trigger,
            )
    return stage_result(
        str(state["run_id"]),
        next_stage,
        "needs_operator",
        reason_code="run_next_stage",
        artifact=RUN_STATE_PATH.as_posix(),
        next_stage=next_stage,
        operator_action=_control_command(state, "run"),
    )


def _operator_readback(intent: Mapping[str, Any], sanity: Mapping[str, Any]) -> str:
    lines = [
        "# Apex KB Operator Readback",
        "",
        f"Run ID: `{intent['run_id']}`",
        f"KB identity: {intent['kb_identity']}",
        f"Mode: `{intent['mode']}`",
        f"Operator intent: {intent['operator_intent']}",
        f"Source locus: {intent['source_locus']}",
        f"Source roots: {', '.join(f'`{item}`' for item in intent['source_roots']) or 'none'}",
        f"Out of scope: {', '.join(intent['out_of_scope']) or 'none stated'}",
        f"Success definition: {intent['success_definition']}",
        f"Recommended output tier: `{intent['output_tier']}` — {intent['output_tier_rationale']}",
        f"Execution route: `{intent['execution_route']}`",
        f"Corpus breadth: `{intent['corpus_breadth']}`",
        f"Topics: {', '.join(f'`{item}`' for item in intent['topic_slugs']) or 'none'}",
        "",
        "## Topic-sanity results",
        "",
    ]
    if sanity:
        for slug in sorted(sanity):
            item = sanity[slug]
            lines.append(f"- `{slug}`: `{item.get('verdict', 'unknown')}` — {item.get('message', 'no message')}")
    else:
        lines.append("- not applicable for this source-only run")
    lines.extend(
        [
            "",
            "## Confirmation",
            "",
            "Confirm only when this readback matches the intended run. The confirmation command stores the verbatim affirmative in `manifests/run-intent.md` and `manifests/run-state.json`.",
            "",
        ]
    )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Read-only Git/worktree classifier
# ---------------------------------------------------------------------------


def _find_repository_root(start: Path, explicit: Optional[str] = None) -> Optional[Path]:
    if explicit:
        candidate = Path(explicit).expanduser().resolve()
        return candidate if (candidate / ".git").exists() else None
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return None


def _git_dir(repo_root: Path) -> Path:
    marker = repo_root / ".git"
    if marker.is_dir():
        return marker
    if marker.is_file():
        text = marker.read_text(encoding="utf-8-sig").strip()
        if text.lower().startswith("gitdir:"):
            value = text.split(":", 1)[1].strip()
            candidate = Path(value)
            return (repo_root / candidate).resolve() if not candidate.is_absolute() else candidate.resolve()
    return marker


def classify_git_state(start: Path, explicit_root: Optional[str] = None) -> Dict[str, Any]:
    repo = _find_repository_root(start, explicit_root)
    if repo is None:
        return {
            "schema": "apex.kb.git-state.v1",
            "classification": "no_repository",
            "repository_root": None,
            "branch": None,
            "head": None,
            "upstream": None,
            "ahead": None,
            "behind": None,
            "tracked_change_count": 0,
            "untracked_count": 0,
            "unmerged_count": 0,
            "operation": None,
            "safe_for_kb_write": True,
            "reason": "No Git repository was discovered; no Git mutation was attempted.",
        }
    command = [
        "git",
        "--no-optional-locks",
        "-C",
        str(repo),
        "status",
        "--porcelain=v2",
        "--branch",
        "--untracked-files=all",
    ]
    try:
        completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30, check=False, shell=False)
    except (OSError, subprocess.SubprocessError) as exc:
        return {
            "schema": "apex.kb.git-state.v1",
            "classification": "git_unavailable",
            "repository_root": str(repo),
            "branch": None,
            "head": None,
            "upstream": None,
            "ahead": None,
            "behind": None,
            "tracked_change_count": 0,
            "untracked_count": 0,
            "unmerged_count": 0,
            "operation": None,
            "safe_for_kb_write": False,
            "reason": f"Read-only git status could not run: {exc}",
        }
    if completed.returncode != 0:
        return {
            "schema": "apex.kb.git-state.v1",
            "classification": "git_status_failed",
            "repository_root": str(repo),
            "branch": None,
            "head": None,
            "upstream": None,
            "ahead": None,
            "behind": None,
            "tracked_change_count": 0,
            "untracked_count": 0,
            "unmerged_count": 0,
            "operation": None,
            "safe_for_kb_write": False,
            "reason": completed.stderr.strip() or "git status returned non-zero",
        }
    branch = head = upstream = None
    ahead = behind = None
    tracked = untracked = unmerged = 0
    changed_paths: List[str] = []
    for line in completed.stdout.splitlines():
        if line.startswith("# branch.oid "):
            head = line[len("# branch.oid ") :].strip()
        elif line.startswith("# branch.head "):
            branch = line[len("# branch.head ") :].strip()
        elif line.startswith("# branch.upstream "):
            upstream = line[len("# branch.upstream ") :].strip()
        elif line.startswith("# branch.ab "):
            match = re.search(r"\+(\d+)\s+-(\d+)", line)
            if match:
                ahead, behind = int(match.group(1)), int(match.group(2))
        elif line.startswith("u "):
            unmerged += 1
            fields = line.split(" ", 10)
            if len(fields) > 10:
                changed_paths.append(fields[10])
        elif line.startswith("1 "):
            tracked += 1
            fields = line.split(" ", 8)
            if len(fields) > 8:
                changed_paths.append(fields[8])
        elif line.startswith("2 "):
            tracked += 1
            fields = line.split(" ", 9)
            if len(fields) > 9:
                changed_paths.append(fields[9].split("\t", 1)[0])
        elif line.startswith("? "):
            untracked += 1
            changed_paths.append(line[2:])
    git_dir = _git_dir(repo)
    operation = None
    if (git_dir / "rebase-merge").exists() or (git_dir / "rebase-apply").exists():
        operation = "rebase"
    elif (git_dir / "MERGE_HEAD").exists():
        operation = "merge"
    elif (git_dir / "CHERRY_PICK_HEAD").exists():
        operation = "cherry_pick"
    elif (git_dir / "REVERT_HEAD").exists():
        operation = "revert"
    elif (git_dir / "BISECT_LOG").exists():
        operation = "bisect"
    if operation:
        classification = f"{operation}_in_progress"
    elif unmerged:
        classification = "conflicted"
    elif tracked or untracked:
        classification = "dirty"
    elif ahead and behind:
        classification = "clean_diverged"
    elif ahead:
        classification = "clean_ahead"
    elif behind:
        classification = "clean_behind"
    elif upstream:
        classification = "clean_synced"
    else:
        classification = "clean_no_upstream"
    safe = operation is None and unmerged == 0
    return {
        "schema": "apex.kb.git-state.v1",
        "classification": classification,
        "repository_root": str(repo),
        "branch": branch,
        "head": head,
        "upstream": upstream,
        "ahead": ahead,
        "behind": behind,
        "tracked_change_count": tracked,
        "untracked_count": untracked,
        "unmerged_count": unmerged,
        "changed_paths": sorted(changed_paths),
        "operation": operation,
        "safe_for_kb_write": safe,
        "reason": "Apex KB classified repository state read-only; it did not fetch, pull, reset, stash, merge, commit, or push.",
    }


# ---------------------------------------------------------------------------
# Packet rendering and semantic output validation
# ---------------------------------------------------------------------------


def _packet_input_hashes(kb_root: Path, inputs: Iterable[str]) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for item in inputs:
        path = resolve_path_key(kb_root, item)
        if path.exists():
            result[item] = sha256_path(path)
    return result


def _bullets(items: Sequence[str], *, code: bool = False) -> str:
    if not items:
        return "- none"
    return "\n".join(f"- `{item}`" if code else f"- {item}" for item in items)


def _render_packet_markdown(packet: Mapping[str, Any], packet_json_path: str) -> str:
    template = template_path("semantic-handoff-packet-template.md").read_text(encoding="utf-8")
    replacements = {
        "{{PACKET_JSON_PATH}}": packet_json_path,
        "{{RUN_ID}}": str(packet["run_id"]),
        "{{STAGE}}": str(packet["stage"]),
        "{{TOPIC_ID}}": str(packet["topic_id"]),
        "{{EXACT_INPUT_FILES}}": _bullets(packet["exact_input_files"], code=True),
        "{{CANONICAL_OWNERS}}": _bullets(packet["canonical_template_or_schema_owner"], code=True),
        "{{EXACT_OUTPUT_PATH}}": str(packet["exact_output_path"]),
        "{{ADDITIONAL_OUTPUT_PATHS}}": _bullets(packet["additional_output_paths"], code=True),
        "{{ALLOWED_WRITES}}": _bullets(packet["allowed_writes"], code=True),
        "{{FORBIDDEN_WRITES}}": _bullets(packet["forbidden_writes"], code=True),
        "{{STOP_CONDITIONS}}": _bullets(packet["stop_conditions"]),
        "{{SUCCESS_CONDITIONS}}": _bullets(packet["success_conditions"]),
        "{{REQUIRED_READBACK}}": _bullets(packet["required_readback"], code=True),
        "{{COMPLETION_RESPONSE}}": str(packet["completion_response"]),
        "{{SHORT_TRIGGER}}": str(packet["short_trigger"]),
    }
    for key, value in replacements.items():
        template = template.replace(key, value)
    return template


def _workpack_paths(slug: str) -> Tuple[Path, Path]:
    return (
        Path("manifests/phase0/work-packs") / f"{slug}.json",
        Path("manifests/phase0/work-packs") / f"{slug}.md",
    )


def _candidate_inputs(kb_root: Path, slug: str) -> List[str]:
    workpack_json, _ = _workpack_paths(slug)
    value = read_json(kb_root / workpack_json)
    candidates = value.get("concentrated_candidates", []) if isinstance(value, dict) else []
    paths: List[str] = []
    for item in candidates if isinstance(candidates, list) else []:
        if isinstance(item, dict) and item.get("path"):
            paths.append(str(item["path"]))
    return sorted(dict.fromkeys(paths))


def _phase1_packet(state: Mapping[str, Any], kb_root: Path, slug: str) -> Dict[str, Any]:
    workpack_json, workpack_md = _workpack_paths(slug)
    exact_inputs = [
        "semantic-contract/semantic-execution-contract.md",
        "semantic-contract/phase1-analysis-template.md",
        TOPIC_REGISTRY_PATH.as_posix(),
        PHASE0_RANKINGS_PATH.as_posix(),
        workpack_json.as_posix(),
        workpack_md.as_posix(),
        *_candidate_inputs(kb_root, slug),
    ]
    missing = [item for item in exact_inputs if not resolve_path_key(kb_root, item).exists()]
    if missing:
        raise ControlError("phase1_packet_input_missing", "Phase 1 packet inputs are missing", paths=missing)
    output = f"ingest-analysis/{slug}.analysis.md"
    ledger = f"log/semantic-runs/{state['run_id']}/topics/{slug}.json"
    completion = f"APEX_KB_PACKET_COMPLETE run_id={state['run_id']} stage=phase1 topic={slug} output={output}"
    packet = {
        "schema": PACKET_SCHEMA,
        "run_id": state["run_id"],
        "stage": "phase1",
        "topic_id": slug,
        "exact_input_files": sorted(dict.fromkeys(exact_inputs)),
        "canonical_template_or_schema_owner": [
            ".claude/skills/apex-kb/references/semantic-value-contract.md",
            ".claude/skills/apex-kb/references/semantic-run-ledger.schema.json",
            "semantic-contract/phase1-analysis-template.md",
        ],
        "exact_output_path": output,
        "additional_output_paths": [ledger],
        "allowed_writes": [output, ledger],
        "forbidden_writes": [
            "wiki/**",
            "manifests/**",
            "derived/**",
            "outputs/**",
            "any Apex Plan, Sync, Session, PreCap, FlowRecap, APSU, or personal-orchestration path",
        ],
        "stop_conditions": [
            "Stop with truthful partial state when a required source cannot be read or the packet input fingerprint no longer matches.",
            "Do not stop merely because a fixed source count was read; continue by gap while a readable source can resolve a critical or routine query.",
            "Do not draft wiki pages or certify semantic acceptance in this stage.",
        ],
        "success_conditions": [
            "Every concentrated candidate is dispositioned or the ledger records why it remains held in custody.",
            "Every critical and routine query has an answered, partial, contradicted, blocked, or not-covered result with exact pointers.",
            "Every concept and entity candidate has exactly one permitted disposition.",
            "The exact Phase 1 output and ledger contain no template placeholders and have been reread in full.",
        ],
        "required_readback": [output, ledger],
        "completion_response": completion,
        "short_trigger": f"Execute the Apex KB packet at {_packet_rel(state, 'phase1', slug, 'md').as_posix()}; write only the declared outputs; return the completion response exactly.",
        "input_fingerprints": _packet_input_hashes(kb_root, exact_inputs),
        "preexisting_wiki_files": [],
    }
    require_schema(packet, "semantic-handoff-packet.schema.json")
    return packet


def _analysis_declared_outputs(text: str) -> List[str]:
    outputs: List[str] = []
    for match in re.finditer(r"(?m)^\s*destination_page:\s*[\"']?([^\n\"']+)[\"']?\s*$", text):
        value = match.group(1).strip()
        if value and value != "NA" and value.startswith("wiki/"):
            outputs.append(value)
    for match in re.finditer(r"(?m)^\s*-\s*(wiki/(?:summaries|concepts|entities)/[^\s#]+\.md)\s*$", text):
        outputs.append(match.group(1))
    return sorted(dict.fromkeys(outputs))


def _phase2_packet(state: Mapping[str, Any], kb_root: Path, slug: str) -> Dict[str, Any]:
    topic = _topic(state, slug)
    analysis = Path("ingest-analysis") / f"{slug}.analysis.md"
    ledger = Path("log/semantic-runs") / str(state["run_id"]) / "topics" / f"{slug}.json"
    exact_inputs = [
        "semantic-contract/semantic-execution-contract.md",
        "semantic-contract/phase2-wiki-page-templates.md",
        TOPIC_REGISTRY_PATH.as_posix(),
        analysis.as_posix(),
        ledger.as_posix(),
    ]
    missing = [item for item in exact_inputs if not resolve_path_key(kb_root, item).exists()]
    if missing:
        raise ControlError("phase2_packet_input_missing", "Phase 2 packet inputs are missing", paths=missing)
    expected = list(topic["expected_pages"])
    declared = _analysis_declared_outputs((kb_root / analysis).read_text(encoding="utf-8-sig"))
    allowed = sorted(dict.fromkeys([*expected, *declared, ledger.as_posix()]))
    exact_output = expected[0]
    additional = sorted(dict.fromkeys([*expected[1:], *declared, ledger.as_posix()]))
    completion = f"APEX_KB_PACKET_COMPLETE run_id={state['run_id']} stage=phase2 topic={slug} output={exact_output}"
    preexisting = sorted(path.relative_to(kb_root).as_posix() for path in (kb_root / "wiki").rglob("*.md") if path.is_file()) if (kb_root / "wiki").exists() else []
    packet = {
        "schema": PACKET_SCHEMA,
        "run_id": state["run_id"],
        "stage": "phase2",
        "topic_id": slug,
        "exact_input_files": exact_inputs,
        "canonical_template_or_schema_owner": [
            ".claude/skills/apex-kb/references/semantic-value-contract.md",
            "semantic-contract/phase2-wiki-page-templates.md",
        ],
        "exact_output_path": exact_output,
        "additional_output_paths": additional,
        "allowed_writes": allowed,
        "forbidden_writes": [
            "raw/**",
            "manifests/**",
            "derived/**",
            "outputs/**",
            "any wiki path not already declared in the Phase 1 analysis or target registry",
            "any Apex Plan, Sync, Session, PreCap, FlowRecap, APSU, or personal-orchestration path",
        ],
        "stop_conditions": [
            "Stop if the Phase 1 analysis or ledger no longer matches its packet fingerprint.",
            "Stop with partial state if a critical or routine query still requires a readable unopened source.",
            "Do not create pointer-only concept or entity pages and do not self-certify semantic acceptance.",
        ],
        "success_conditions": [
            "Every required target page directly answers its declared queries and uses only reviewed, materially used evidence.",
            "Macro, Meso, and Micro are distinct Why, What-it-is, and How layers with exact source pointers.",
            "Every written page is one of the exact allowed paths and has been reread in full.",
            "The topic ledger records page decisions, source use, claims, and remaining blockers.",
        ],
        "required_readback": sorted(dict.fromkeys([*expected, *declared, ledger.as_posix()])),
        "completion_response": completion,
        "short_trigger": f"Execute the Apex KB packet at {_packet_rel(state, 'phase2', slug, 'md').as_posix()}; write only the declared outputs; return the completion response exactly.",
        "input_fingerprints": _packet_input_hashes(kb_root, exact_inputs),
        "preexisting_wiki_files": preexisting,
    }
    require_schema(packet, "semantic-handoff-packet.schema.json")
    return packet


def _acceptance_packet(state: Mapping[str, Any], kb_root: Path, slug: str) -> Dict[str, Any]:
    topic = _topic(state, slug)
    analysis = f"ingest-analysis/{slug}.analysis.md"
    ledger = f"log/semantic-runs/{state['run_id']}/topics/{slug}.json"
    exact_inputs = [TOPIC_REGISTRY_PATH.as_posix(), analysis, ledger, *topic["expected_pages"]]
    missing = [item for item in exact_inputs if not resolve_path_key(kb_root, item).exists()]
    if missing:
        raise ControlError("acceptance_packet_input_missing", "Semantic acceptance packet inputs are missing", paths=missing)
    output = f"audit/semantic-acceptance/{state['run_id']}/{slug}.json"
    completion = f"APEX_KB_PACKET_COMPLETE run_id={state['run_id']} stage=semantic_acceptance topic={slug} output={output}"
    packet = {
        "schema": PACKET_SCHEMA,
        "run_id": state["run_id"],
        "stage": "semantic_acceptance",
        "topic_id": slug,
        "exact_input_files": exact_inputs,
        "canonical_template_or_schema_owner": [
            ".claude/skills/apex-kb/references/semantic-acceptance.schema.json",
            ".claude/skills/apex-kb/references/browser-git-connector-semantic-runbook.md",
        ],
        "exact_output_path": output,
        "additional_output_paths": [],
        "allowed_writes": [output],
        "forbidden_writes": [
            "ingest-analysis/**",
            "wiki/**",
            "manifests/**",
            "derived/**",
            "outputs/**",
            "log/semantic-runs/**",
            "any Apex Plan, Sync, Session, PreCap, FlowRecap, APSU, or personal-orchestration path",
        ],
        "stop_conditions": [
            "Fix page-only query verdicts before opening raw evidence passages.",
            "Return insufficient_evidence rather than inferring support when an exact source passage is unavailable.",
            "Do not repair the drafted pages in the evaluator context and do not certify based on counts, headings, or drafter self-report.",
        ],
        "success_conditions": [
            "Every critical and routine target query is evaluated from compiled pages first.",
            "At least two material claims per page, or all claims when fewer exist, are checked against resolved source passages.",
            "The exact acceptance JSON validates and records reason-coded repairs and a truthful verdict.",
        ],
        "required_readback": [output],
        "completion_response": completion,
        "short_trigger": f"Execute the Apex KB packet at {_packet_rel(state, 'semantic_acceptance', slug, 'md').as_posix()}; write only the declared output; return the completion response exactly.",
        "input_fingerprints": _packet_input_hashes(kb_root, exact_inputs),
        "preexisting_wiki_files": [],
    }
    require_schema(packet, "semantic-handoff-packet.schema.json")
    return packet


def build_packet(state: Mapping[str, Any], kb_root: Path, stage: str) -> Dict[str, Any]:
    base, separator, slug = stage.partition(":")
    if not separator or not slug:
        raise ControlError("semantic_stage_invalid", f"Semantic stage must include topic: {stage}")
    if base == "phase1":
        return _phase1_packet(state, kb_root, slug)
    if base == "phase2":
        return _phase2_packet(state, kb_root, slug)
    if base == "semantic_acceptance":
        return _acceptance_packet(state, kb_root, slug)
    raise ControlError("semantic_stage_invalid", f"Unsupported semantic stage: {stage}")


def write_packet(state: MutableMapping[str, Any], kb_root: Path, stage: str, packet: Dict[str, Any]) -> Tuple[str, str]:
    base, _, slug = stage.partition(":")
    json_rel = _packet_rel(state, base, slug, "json")
    md_rel = _packet_rel(state, base, slug, "md")
    atomic_write_json(kb_root / json_rel, packet)
    atomic_write_text(kb_root / md_rel, _render_packet_markdown(packet, json_rel.as_posix()))
    state.setdefault("artifact_references", {})[f"packet_{base}_{slug}"] = md_rel.as_posix()
    return json_rel.as_posix(), md_rel.as_posix()


def _load_packet(state: Mapping[str, Any], kb_root: Path, base: str, slug: str) -> Dict[str, Any]:
    path = kb_root / _packet_rel(state, base, slug, "json")
    packet = read_json(path)
    if not isinstance(packet, dict):
        raise ControlError("packet_invalid", f"Packet root must be an object: {path}")
    require_schema(packet, "semantic-handoff-packet.schema.json")
    return packet


def _packet_input_drift(packet: Mapping[str, Any], kb_root: Path) -> Optional[ControlError]:
    changed: List[str] = []
    fingerprints = packet.get("input_fingerprints", {})
    if not isinstance(fingerprints, dict):
        return ControlError("packet_fingerprint_invalid", "Packet input_fingerprints must be an object")
    for key, expected in fingerprints.items():
        path = resolve_path_key(kb_root, str(key))
        actual = sha256_path(path) if path.exists() else "missing"
        if actual != expected:
            changed.append(str(key))
    if changed:
        return ControlError(
            "packet_input_changed",
            "One or more packet inputs changed after the packet was rendered; render a fresh packet before accepting semantic outputs",
            paths=sorted(changed),
        )
    return None


def _wrong_path_matches(kb_root: Path, expected: Path) -> List[str]:
    if expected.exists():
        return []
    return sorted(path.relative_to(kb_root).as_posix() for path in kb_root.rglob(expected.name) if path.is_file())


def _phase1_validation(state: MutableMapping[str, Any], kb_root: Path, slug: str, core: Mapping[str, Any]) -> Optional[ControlError]:
    packet_path = kb_root / _packet_rel(state, "phase1", slug, "json")
    if not packet_path.exists():
        return None
    try:
        packet = _load_packet(state, kb_root, "phase1", slug)
    except ControlError as exc:
        return exc
    drift_issue = _packet_input_drift(packet, kb_root)
    if drift_issue is not None:
        return drift_issue
    output = kb_root / "ingest-analysis" / f"{slug}.analysis.md"
    if not output.exists():
        wrong = _wrong_path_matches(kb_root, output)
        if wrong:
            return ControlError("output_wrong_path", f"Phase 1 output exists outside its exact path: {wrong}", paths=wrong)
        return None
    text = output.read_text(encoding="utf-8-sig")
    if "LLM must fill" in text or re.search(r"<(?:kb|topic|source|stable|exact|explicit|known|what|why|how)[^>]*>", text, flags=re.IGNORECASE):
        return ControlError("phase1_placeholders_remain", f"Phase 1 output still contains template placeholders: {output}", paths=[rel_or_abs(kb_root, output)])
    if state["output_tier"] not in {"source_only", "analysis_only"} and not re.search(r"(?m)^\s*phase_2_ready:\s*true\s*$", text):
        return ControlError("phase1_not_ready", "Phase 1 compile decision does not declare phase_2_ready: true", paths=[rel_or_abs(kb_root, output)])
    ledger = kb_root / "log" / "semantic-runs" / str(state["run_id"]) / "topics" / f"{slug}.json"
    if not ledger.exists():
        return ControlError("semantic_ledger_missing", f"Topic ledger is missing: {ledger}", paths=[rel_or_abs(kb_root, ledger)])
    try:
        ledger_value = read_json(ledger)
        if not isinstance(ledger_value, dict):
            raise ControlError("semantic_ledger_invalid", "Topic ledger root must be an object")
        errors = validate_schema(ledger_value, load_schema("semantic-run-ledger.schema.json"))
        if errors:
            return ControlError("semantic_ledger_schema_failed", "; ".join(errors[:20]), paths=[rel_or_abs(kb_root, ledger)])
    except ControlError as exc:
        return exc
    finding_func = core.get("candidate_disposition_findings")
    if callable(finding_func):
        findings = finding_func(kb_root)
        rel_output = output.relative_to(kb_root).as_posix()
        if any(item.get("path") == rel_output for item in findings if isinstance(item, dict)):
            return ControlError("candidate_disposition_missing", "Phase 1 candidate disposition is incomplete", paths=[rel_output])
    ranked = len(_candidate_inputs(kb_root, slug))
    opened = len(set(re.findall(r"(?m)^### (\S+) - authority:", text)))
    floor = float(state.get("phase1_min_coverage") or 0.6)
    coverage = (opened / ranked) if ranked else 1.0
    if ranked and coverage < floor:
        return ControlError(
            "phase1_source_coverage_below_floor",
            f"{opened}/{ranked} work-pack concentrated-candidate sources analyzed "
            f"(coverage {coverage:.2f}, floor {floor:.2f}); open more ranked sources or "
            f"record them as rejected in the Source Inventory before completing this topic",
            paths=[rel_or_abs(kb_root, output)],
        )
    workpack_json, workpack_md = _workpack_paths(slug)
    record_fingerprint(state, kb_root, kb_root / workpack_json, f"phase1:{slug}")
    record_fingerprint(state, kb_root, kb_root / workpack_md, f"phase1:{slug}")
    record_fingerprint(state, kb_root, output, f"phase2:{slug}")
    record_fingerprint(state, kb_root, ledger, f"phase2:{slug}")
    mark_stage_complete(state, f"phase1:{slug}")
    return None


def _phase2_validation(state: MutableMapping[str, Any], kb_root: Path, slug: str, core: Mapping[str, Any]) -> Optional[ControlError]:
    packet_path = kb_root / _packet_rel(state, "phase2", slug, "json")
    if not packet_path.exists():
        return None
    try:
        packet = _load_packet(state, kb_root, "phase2", slug)
    except ControlError as exc:
        return exc
    drift_issue = _packet_input_drift(packet, kb_root)
    if drift_issue is not None:
        return drift_issue
    required = [packet["exact_output_path"], *[item for item in packet["additional_output_paths"] if str(item).startswith("wiki/")]]
    missing = [item for item in required if not (kb_root / item).exists()]
    if missing:
        wrong: List[str] = []
        for item in missing:
            wrong.extend(_wrong_path_matches(kb_root, kb_root / item))
        if wrong:
            return ControlError("output_wrong_path", f"Phase 2 output exists outside its exact path: {sorted(set(wrong))}", paths=sorted(set(wrong)))
        return None
    preexisting = set(packet.get("preexisting_wiki_files", []))
    allowed = {item for item in packet["allowed_writes"] if str(item).startswith("wiki/")}
    current = {path.relative_to(kb_root).as_posix() for path in (kb_root / "wiki").rglob("*.md") if path.is_file()}
    unauthorized = sorted(current - preexisting - allowed)
    if unauthorized:
        return ControlError("phase2_unauthorized_write", "Phase 2 created wiki files outside the packet allowlist", paths=unauthorized)
    metrics_func = core.get("_quality_page_metrics")
    for item in sorted(set(required)):
        page = kb_root / item
        if callable(metrics_func):
            metrics = metrics_func(kb_root, page)
            reasons = list(metrics.get("repair_reasons", [])) if isinstance(metrics, dict) else []
            if reasons:
                return ControlError("phase2_structural_validation_failed", f"{item}: {', '.join(reasons)}", paths=[item])
        record_fingerprint(state, kb_root, page, f"semantic_acceptance:{slug}")
    analysis = kb_root / "ingest-analysis" / f"{slug}.analysis.md"
    record_fingerprint(state, kb_root, analysis, f"phase2:{slug}")
    mark_stage_complete(state, f"phase2:{slug}")
    return None


def _acceptance_validation(state: MutableMapping[str, Any], kb_root: Path, slug: str) -> Optional[ControlError]:
    packet_path = kb_root / _packet_rel(state, "semantic_acceptance", slug, "json")
    if not packet_path.exists():
        return None
    try:
        packet = _load_packet(state, kb_root, "semantic_acceptance", slug)
    except ControlError as exc:
        return exc
    drift_issue = _packet_input_drift(packet, kb_root)
    if drift_issue is not None:
        return drift_issue
    path = kb_root / "audit" / "semantic-acceptance" / str(state["run_id"]) / f"{slug}.json"
    if not path.exists():
        wrong = _wrong_path_matches(kb_root, path)
        if wrong:
            return ControlError("output_wrong_path", f"Acceptance output exists outside its exact path: {wrong}", paths=wrong)
        return None
    try:
        value = read_json(path)
        if not isinstance(value, dict):
            raise ControlError("semantic_acceptance_invalid", "Acceptance root must be an object")
        errors = validate_schema(value, load_schema("semantic-acceptance.schema.json"))
        if errors:
            return ControlError("semantic_acceptance_schema_failed", "; ".join(errors[:20]), paths=[rel_or_abs(kb_root, path)])
    except ControlError as exc:
        return exc
    if value.get("run_id") != state["run_id"] or value.get("topic_slug") != slug:
        return ControlError("semantic_acceptance_identity_mismatch", "Acceptance run/topic identity does not match state", paths=[rel_or_abs(kb_root, path)])
    query_failures = [item for item in value.get("query_results", []) if isinstance(item, dict) and item.get("result") != "answerable"]
    claim_failures = [item for item in value.get("claim_reviews", []) if isinstance(item, dict) and item.get("result") != "supported"]
    if value.get("verdict") != "semantic_pass" or query_failures or claim_failures:
        return ControlError("semantic_acceptance_not_passed", "Independent semantic acceptance did not pass; repair and reevaluate in a fresh context", paths=[rel_or_abs(kb_root, path)])
    record_fingerprint(state, kb_root, path, "postflight")
    mark_stage_complete(state, f"semantic_acceptance:{slug}")
    return None


def reconcile_semantic_outputs(state: MutableMapping[str, Any], kb_root: Path, core: Mapping[str, Any]) -> Tuple[bool, Optional[ControlError]]:
    progressed = False
    while True:
        stage = compute_next_stage(state)
        base, separator, slug = stage.partition(":")
        if not separator or base not in SEMANTIC_STAGE_BASES:
            break
        if base == "phase1":
            issue = _phase1_validation(state, kb_root, slug, core)
        elif base == "phase2":
            issue = _phase2_validation(state, kb_root, slug, core)
        else:
            issue = _acceptance_validation(state, kb_root, slug)
        if issue is not None:
            return progressed, issue
        if not _completed(state, stage):
            break
        progressed = True
    refresh_stage(state)
    return progressed, None


# ---------------------------------------------------------------------------
# Existing-domain delegation
# ---------------------------------------------------------------------------


def _core_args(state: Mapping[str, Any], cli_args: argparse.Namespace, **overrides: Any) -> argparse.Namespace:
    values: Dict[str, Any] = {
        "kb_root": str(state["kb_root"]),
        "allow_write": bool(getattr(cli_args, "allow_write", False)),
        "dry_run": bool(getattr(cli_args, "dry_run", False)),
        "strict": bool(getattr(cli_args, "strict", False)),
        "json": True,
        "output_json": None,
        "title": state.get("kb_title"),
        "topic_title": None,
        "source_path": None,
        "source_root": None,
        "source_type": "other",
        "storage_mode": "pointer_only",
        "source_id": None,
        "source_slug": None,
        "topic_slug": None,
        "pointer": None,
        "as_version": False,
        "allow_duplicate": False,
        "approval_phrase": None,
        "analysis": None,
        "query": None,
        "limit": 8,
        "save": False,
        "raw_root": None,
        "output": None,
        "group_map": None,
        "include_generated_at": False,
        "init": False,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


def _call_core(core: Mapping[str, Any], name: str, args: argparse.Namespace) -> Dict[str, Any]:
    function = core.get(name)
    if not callable(function):
        raise ControlError("core_runtime_unavailable", f"Required apex_kb.py function is unavailable: {name}")
    result = function(args)
    if not isinstance(result, dict):
        raise ControlError("core_result_invalid", f"{name} did not return an object")
    return result


def _core_failed(result: Mapping[str, Any]) -> bool:
    return str(result.get("status", "ok")).lower() in {"blocked", "fail", "failed", "error"}


def _resolve_source_path(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = repository_root() / path
    return str(path.resolve())


def _source_spec_id(spec: Mapping[str, Any]) -> str:
    if spec.get("source_id"):
        return str(spec["source_id"])
    basis = str(spec.get("path") or spec.get("pointer") or "source")
    return _slug(Path(basis).stem)


def _source_spec_already_intaken(kb_root: Path, spec: Mapping[str, Any]) -> bool:
    if bool(spec.get("as_version")):
        return False
    manifest_path = kb_root / SOURCE_MANIFEST_PATH
    if not manifest_path.exists():
        return False
    value = read_json(manifest_path)
    sources = value.get("sources", []) if isinstance(value, dict) else []
    source_id = _source_spec_id(spec)
    entry = next((item for item in sources if isinstance(item, dict) and item.get("source_id") == source_id), None)
    if entry is None or entry.get("source_storage_mode") != spec.get("storage_mode", "pointer_only"):
        return False
    if spec.get("pointer"):
        pointer = str(spec["pointer"])
        return pointer in {str(entry.get("source_path") or ""), str(entry.get("original_source_path") or "")}
    source_path = _resolve_source_path(str(spec.get("path") or ""))
    if not source_path:
        return False
    path = Path(source_path)
    if not path.is_file():
        return False
    expected_hash = sha256_file(path)
    if entry.get("source_hash") != expected_hash:
        return False
    original = str(entry.get("original_source_path") or "")
    try:
        return Path(original).expanduser().resolve() == path.resolve()
    except (OSError, ValueError):
        return original == source_path


def _registered_source_ids(kb_root: Path) -> set[str]:
    value = read_json(kb_root / SOURCE_MANIFEST_PATH)
    sources = value.get("sources", []) if isinstance(value, dict) else []
    return {str(item.get("source_id")) for item in sources if isinstance(item, dict) and item.get("source_id")}


def _git_stage_issue(state: Mapping[str, Any], git_state: Mapping[str, Any]) -> Optional[ControlError]:
    target_commit = str(state.get("target_commit") or "").strip()
    head = str(git_state.get("head") or "").strip()
    if target_commit and (not head or not head.startswith(target_commit)):
        return ControlError(
            "target_commit_mismatch",
            f"Run state targets commit {target_commit}, but the read-only Git classifier reports {head or 'no HEAD'}",
        )
    if not git_state.get("safe_for_kb_write"):
        return ControlError(
            "git_worktree_unsafe",
            f"Git state is {git_state.get('classification')}; Apex KB will not mutate Git or write lifecycle artifacts until the operator resolves it.",
            paths=list(git_state.get("changed_paths", [])),
        )
    return None


def run_deterministic_stage(state: MutableMapping[str, Any], kb_root: Path, stage: str, args: argparse.Namespace, core: Mapping[str, Any]) -> Any:
    if stage == "scaffold":
        result = _call_core(core, "cmd_scaffold", _core_args(state, args))
        if _core_failed(result) or not _scaffold_complete(kb_root):
            raise ControlError("scaffold_failed", "Scaffold did not establish all required core paths")
        mark_stage_complete(state, "scaffold")
        return {"kind": "core_result", "command": "scaffold"}
    if stage == "preflight":
        result = _call_core(core, "cmd_preflight", _core_args(state, args))
        if _core_failed(result):
            raise ControlError("preflight_failed", json.dumps(result.get("checks", result), ensure_ascii=False))
        mark_stage_complete(state, "preflight")
        return {"kind": "core_result", "command": "preflight"}
    if stage == "source_intake":
        if not state.get("source_roots") and not state.get("source_inputs"):
            manifest = kb_root / SOURCE_MANIFEST_PATH
            existing = read_json(manifest) if manifest.exists() else {}
            sources = existing.get("sources", []) if isinstance(existing, dict) else []
            if not sources:
                raise ControlError("source_inputs_missing", "No source roots or source specs are configured and the source manifest is empty")
        for root in state.get("source_roots", []):
            result = _call_core(core, "cmd_source_intake", _core_args(state, args, source_root=_resolve_source_path(str(root))))
            if _core_failed(result):
                raise ControlError("source_intake_failed", json.dumps(result, ensure_ascii=False))
        for spec in state.get("source_inputs", []):
            if isinstance(spec, dict) and _source_spec_already_intaken(kb_root, spec):
                continue
            source_path = _resolve_source_path(spec.get("path")) if isinstance(spec, dict) else None
            result = _call_core(
                core,
                "cmd_source_intake",
                _core_args(
                    state,
                    args,
                    source_path=source_path,
                    pointer=spec.get("pointer") if isinstance(spec, dict) else None,
                    source_type=spec.get("source_type", "other") if isinstance(spec, dict) else "other",
                    storage_mode=spec.get("storage_mode", "pointer_only") if isinstance(spec, dict) else "pointer_only",
                    source_id=spec.get("source_id") if isinstance(spec, dict) else None,
                    title=spec.get("title") if isinstance(spec, dict) else None,
                    as_version=bool(spec.get("as_version", False)) if isinstance(spec, dict) else False,
                    allow_duplicate=bool(spec.get("allow_duplicate", False)) if isinstance(spec, dict) else False,
                ),
            )
            if _core_failed(result):
                raise ControlError("source_intake_failed", json.dumps(result, ensure_ascii=False))
            recorded_id = str(result.get("entry", {}).get("source_id") or _source_spec_id(spec)) if isinstance(spec, dict) else ""
            if recorded_id and recorded_id not in _registered_source_ids(kb_root):
                raise ControlError("source_intake_not_recorded", f"Source intake returned without recording {recorded_id} in the source manifest")
        payload = _call_core(core, "cmd_generate_source_payload_manifest", _core_args(state, args))
        if _core_failed(payload) or not (kb_root / SOURCE_PAYLOAD_MANIFEST_PATH).exists():
            raise ControlError("source_payload_manifest_failed", "Source payload manifest was not generated")
        mark_stage_complete(state, "source_intake")
        record_fingerprint(state, kb_root, kb_root / SOURCE_MANIFEST_PATH, "phase0")
        record_fingerprint(state, kb_root, kb_root / SOURCE_PAYLOAD_MANIFEST_PATH, "phase0")
        return {"kind": "core_result", "command": "source-intake+generate-source-payload-manifest"}
    if stage == "phase0":
        result = _call_core(core, "cmd_phase0", _core_args(state, args))
        if _core_failed(result):
            raise ControlError("phase0_failed", json.dumps(result, ensure_ascii=False))
        required = [kb_root / PHASE0_RANKINGS_PATH]
        for slug in _topic_slugs(state):
            required.extend(kb_root / path for path in _workpack_paths(slug))
        missing = [rel_or_abs(kb_root, path) for path in required if not path.exists()]
        if missing:
            raise ControlError("phase0_output_missing", "Phase 0 did not produce required rankings/work packs", paths=missing)
        mark_stage_complete(state, "phase0")
        record_fingerprint(state, kb_root, kb_root / TOPIC_REGISTRY_PATH, "phase0")
        record_fingerprint(state, kb_root, kb_root / PHASE0_RANKINGS_PATH, "phase1")
        for slug in _topic_slugs(state):
            for path in _workpack_paths(slug):
                record_fingerprint(state, kb_root, kb_root / path, f"phase1:{slug}")
        return {"kind": "core_result", "command": "phase0"}
    if stage == "postflight":
        result = _call_core(core, "cmd_postflight", _core_args(state, args))
        if _core_failed(result) or str(result.get("status", "")).lower() not in {"pass", "ok"}:
            raise ControlError("postflight_failed", json.dumps(result, ensure_ascii=False))
        mark_stage_complete(state, "postflight")
        return {"kind": "core_result", "command": "postflight"}
    raise ControlError("stage_not_deterministic", f"Stage is not an executable deterministic stage: {stage}")


# ---------------------------------------------------------------------------
# Control actions
# ---------------------------------------------------------------------------


INTENT_CONFIGURATION_FIELDS = (
    "schema",
    "schema_version",
    "run_id",
    "kb_root",
    "kb_slug",
    "mode",
    "operator_intent",
    "kb_identity",
    "source_locus",
    "source_roots",
    "source_inputs",
    "out_of_scope",
    "success_definition",
    "output_tier",
    "output_tier_rationale",
    "execution_route",
    "corpus_breadth",
    "broad_breadth_reason",
    "topic_slugs",
    "target_repository",
    "target_commit",
)


def _intent_configuration(intent: Mapping[str, Any]) -> Dict[str, Any]:
    return {key: intent.get(key) for key in INTENT_CONFIGURATION_FIELDS}


def control_init(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    intent = _intent_from_args(args, kb_root)
    require_schema(intent, "run-intent.schema.json")
    existing_path = kb_root / RUN_STATE_PATH
    if existing_path.exists():
        existing = load_state(kb_root)
        if existing.get("run_id") == intent["run_id"]:
            existing_intent, _ = parse_run_intent(kb_root / RUN_INTENT_PATH)
            if _intent_configuration(existing_intent) != _intent_configuration(intent):
                return stage_result(
                    str(existing["run_id"]),
                    str(existing["current_stage"]),
                    "blocked",
                    reason_code="run_init_mismatch",
                    artifact=RUN_INTENT_PATH.as_posix(),
                    next_stage=compute_next_stage(existing),
                    operator_action="Reuse the exact original run configuration, choose a new run ID/KB root, or replace only an unconfirmed scaffold-only run.",
                )
            return derive_next_result(existing, kb_root)
        can_replace = bool(args.replace_unconfirmed) and not existing.get("operator_confirmation", {}).get("confirmed") and set(existing.get("completed_stages", [])) <= {"scaffold"}
        if not can_replace:
            return stage_result(
                str(existing.get("run_id", "unknown")),
                str(existing.get("current_stage", "init")),
                "blocked",
                reason_code="run_state_exists",
                artifact=RUN_STATE_PATH.as_posix(),
                next_stage=str(existing.get("next_legal_stage") or existing.get("current_stage") or "init"),
                operator_action="Use the existing run, choose a different KB root, or pass --replace-unconfirmed only for an unconfirmed run with no work beyond scaffold.",
            )
    state = _initial_state(intent, kb_root, args.title)
    require_schema(state, "run-state.schema.json")
    if not args.allow_write or args.dry_run:
        return stage_result(
            intent["run_id"],
            "init",
            "needs_operator",
            reason_code="write_authorization_required",
            artifact={"run_intent": RUN_INTENT_PATH.as_posix(), "run_state": RUN_STATE_PATH.as_posix()},
            next_stage=state["current_stage"],
            operator_action="Repeat the same control init command with --allow-write and without --dry-run.",
        )
    ensure_inside(kb_root, kb_root / RUN_INTENT_PATH)
    atomic_write_text(kb_root / RUN_INTENT_PATH, render_run_intent(intent))
    initial_result = stage_result(
        intent["run_id"],
        "init",
        "ok",
        artifact={"run_intent": RUN_INTENT_PATH.as_posix(), "run_state": RUN_STATE_PATH.as_posix()},
        next_stage=state["current_stage"],
        operator_action=_control_command(state, "next").replace(" --allow-write", ""),
    )
    persist_state_and_result(kb_root, state, initial_result, initial=True)
    return initial_result


def _run_topic_sanity(state: Mapping[str, Any], kb_root: Path, args: argparse.Namespace, core: Mapping[str, Any]) -> Dict[str, Any]:
    results: Dict[str, Any] = {}
    function = core.get("cmd_topic_sanity_check")
    if not callable(function):
        raise ControlError("core_runtime_unavailable", "cmd_topic_sanity_check is unavailable")
    for slug in _topic_slugs(state):
        result = function(_core_args(state, args, topic_slug=slug, phrase=[], search_root=None, search_cap=2000))
        if not isinstance(result, dict):
            raise ControlError("topic_sanity_result_invalid", f"Topic sanity check returned invalid result for {slug}")
        results[slug] = {
            "verdict": result.get("verdict", result.get("status", "unknown")),
            "recommendation": result.get("recommendation"),
            "message": result.get("message", result.get("reason", "")),
            "evidence": result.get("evidence", {}),
        }
    return results


def prepare_intent_readback(state: MutableMapping[str, Any], kb_root: Path, args: argparse.Namespace, core: Mapping[str, Any]) -> str:
    intent, _ = parse_run_intent(kb_root / RUN_INTENT_PATH)
    sanity = _run_topic_sanity(state, kb_root, args, core) if _topic_slugs(state) else {}
    intent["topic_sanity_check"] = sanity
    intent["updated_at"] = utc_now()
    require_schema(intent, "run-intent.schema.json")
    atomic_write_text(kb_root / RUN_INTENT_PATH, render_run_intent(intent))
    rel = RUN_LOG_ROOT / str(state["run_id"]) / "operator-readback.md"
    atomic_write_text(kb_root / rel, _operator_readback(intent, sanity))
    state.setdefault("artifact_references", {})["operator_readback"] = rel.as_posix()
    set_waiting(
        state,
        "operator_confirmation_required",
        "Operator must confirm the deterministic readback before expensive or mutating lifecycle stages.",
        action=_control_command(state, "confirm", "--confirmation-quote '<operator affirmative>'"),
        paths=[rel.as_posix(), RUN_INTENT_PATH.as_posix()],
    )
    state["current_stage"] = "intent_lock"
    state["next_legal_stage"] = "intent_lock"
    return rel.as_posix()


def control_confirm(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    state = load_state(kb_root)
    if compute_next_stage(state) != "intent_lock":
        return stage_result(
            state["run_id"],
            str(state["current_stage"]),
            "blocked",
            reason_code="illegal_transition",
            artifact=RUN_STATE_PATH.as_posix(),
            next_stage=compute_next_stage(state),
            operator_action="Run control next and follow the derived action.",
        )
    readback = kb_root / RUN_LOG_ROOT / str(state["run_id"]) / "operator-readback.md"
    if not readback.exists():
        return stage_result(
            state["run_id"],
            "intent_lock",
            "blocked",
            reason_code="operator_readback_missing",
            artifact=RUN_INTENT_PATH.as_posix(),
            next_stage="intent_lock",
            operator_action=_control_command(state, "run"),
        )
    if not args.allow_write or args.dry_run:
        return stage_result(
            state["run_id"],
            "intent_lock",
            "needs_operator",
            reason_code="write_authorization_required",
            artifact=readback.relative_to(kb_root).as_posix(),
            next_stage="intent_lock",
            operator_action="Repeat control confirm with --allow-write and without --dry-run.",
        )
    quote = args.confirmation_quote.strip()
    if not quote:
        raise ControlError("confirmation_quote_empty", "Operator confirmation quote must not be empty")
    intent, _ = parse_run_intent(kb_root / RUN_INTENT_PATH)
    now = utc_now()
    intent["operator_confirmed"] = True
    intent["operator_confirmation_quote"] = quote
    intent["confirmed_at"] = now
    intent["updated_at"] = now
    require_schema(intent, "run-intent.schema.json")
    atomic_write_text(kb_root / RUN_INTENT_PATH, render_run_intent(intent))
    state["operator_confirmation"] = {"confirmed": True, "quote": quote, "confirmed_at": now}
    mark_stage_complete(state, "intent_lock")
    record_fingerprint(state, kb_root, kb_root / RUN_INTENT_PATH, "intent_lock")
    refresh_stage(state)
    result = stage_result(
        state["run_id"],
        "intent_lock",
        "ok",
        artifact=RUN_INTENT_PATH.as_posix(),
        next_stage=state["next_legal_stage"],
        operator_action=_control_command(state, "run"),
    )
    persist_state_and_result(kb_root, state, result)
    return result


def control_status(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    state = load_state(kb_root)
    drift = detect_drift(state, kb_root)
    if drift:
        action = _control_command(state, "reconcile")
        return stage_result(
            state["run_id"],
            str(state["current_stage"]),
            "blocked",
            reason_code="canonical_input_changed",
            artifact={"run_state": RUN_STATE_PATH.as_posix(), "changed_paths": [item["path"] for item in drift]},
            next_stage=str(state.get("next_legal_stage") or state["current_stage"]),
            operator_action=action,
        )
    return derive_next_result(state, kb_root)


def control_next(args: argparse.Namespace) -> Dict[str, Any]:
    return control_status(args)


def _persist_block(args: argparse.Namespace, kb_root: Path, state: MutableMapping[str, Any], error: ControlError) -> Dict[str, Any]:
    action = _control_command(state, "reconcile") if error.code == "canonical_input_changed" else _control_command(state, "next").replace(" --allow-write", "")
    set_blocked(state, error.code, error.message, action=action, paths=error.paths)
    state["current_stage"] = compute_next_stage(state)
    state["next_legal_stage"] = state["current_stage"]
    result = stage_result(
        state["run_id"],
        str(state["current_stage"]),
        "blocked",
        reason_code=error.code,
        artifact={"run_state": RUN_STATE_PATH.as_posix(), "paths": error.paths},
        next_stage=str(state["next_legal_stage"]),
        operator_action=action,
    )
    if args.allow_write and not args.dry_run:
        persist_state_and_result(kb_root, state, result)
    return result


def control_run(args: argparse.Namespace, core: Mapping[str, Any]) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    state = load_state(kb_root)
    if not args.allow_write or args.dry_run:
        return stage_result(
            state["run_id"],
            compute_next_stage(state),
            "needs_operator",
            reason_code="write_authorization_required",
            artifact=RUN_STATE_PATH.as_posix(),
            next_stage=compute_next_stage(state),
            operator_action="Repeat control run with --allow-write and without --dry-run.",
        )
    drift = detect_drift(state, kb_root)
    if drift:
        return _persist_block(args, kb_root, state, ControlError("canonical_input_changed", "Canonical inputs changed after their accepted stage; reconcile before continuing", paths=[item["path"] for item in drift]))
    progressed, issue = reconcile_semantic_outputs(state, kb_root, core)
    if issue is not None:
        return _persist_block(args, kb_root, state, issue)
    stage = compute_next_stage(state)
    if stage == "complete":
        refresh_stage(state)
        result = stage_result(state["run_id"], "complete", "ok", artifact=RUN_STATE_PATH.as_posix(), next_stage=None, operator_action=None)
        persist_state_and_result(kb_root, state, result)
        return result
    git_state = classify_git_state(kb_root)
    require_schema(git_state, "git-state.schema.json")
    git_issue = _git_stage_issue(state, git_state)
    if git_issue is not None:
        return _persist_block(args, kb_root, state, git_issue)
    if stage == "intent_lock":
        try:
            artifact = prepare_intent_readback(state, kb_root, args, core)
            result = stage_result(
                state["run_id"],
                "intent_lock",
                "needs_operator",
                reason_code="operator_confirmation_required",
                artifact=artifact,
                next_stage="intent_lock",
                operator_action=_control_command(state, "confirm", "--confirmation-quote '<operator affirmative>'"),
            )
            persist_state_and_result(kb_root, state, result)
            return result
        except ControlError as exc:
            return _persist_block(args, kb_root, state, exc)
    base, separator, slug = stage.partition(":")
    if separator and base in SEMANTIC_STAGE_BASES:
        try:
            packet = build_packet(state, kb_root, stage)
            _json_path, md_path = write_packet(state, kb_root, stage, packet)
            set_waiting(
                state,
                "semantic_executor_required",
                f"The {base} semantic packet must be executed by the designated semantic executor.",
                action=packet["short_trigger"],
                paths=[md_path],
            )
            state["current_stage"] = stage
            state["next_legal_stage"] = stage
            result = stage_result(
                state["run_id"],
                stage,
                "needs_semantic_executor",
                reason_code="semantic_executor_required",
                artifact=md_path,
                next_stage=stage,
                operator_action=packet["short_trigger"],
            )
            persist_state_and_result(kb_root, state, result)
            return result
        except ControlError as exc:
            return _persist_block(args, kb_root, state, exc)
    if state["execution_route"] != "terminal_backed":
        return _persist_block(
            args,
            kb_root,
            state,
            ControlError("terminal_executor_required", f"Stage {stage} requires terminal-backed deterministic execution"),
        )
    try:
        artifact = run_deterministic_stage(state, kb_root, stage, args, core)
        refresh_stage(state)
        result = stage_result(
            state["run_id"],
            stage,
            "ok",
            artifact=artifact,
            next_stage=state["next_legal_stage"],
            operator_action=None if state["next_legal_stage"] is None else _control_command(state, "next").replace(" --allow-write", ""),
        )
        persist_state_and_result(kb_root, state, result)
        return result
    except ControlError as exc:
        return _persist_block(args, kb_root, state, exc)


def control_reconcile(args: argparse.Namespace, core: Mapping[str, Any]) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    state = load_state(kb_root)
    was_blocked = state.get("blocked_reason") is not None
    drift = detect_drift(state, kb_root)
    if drift and not args.accept_input_change:
        error = ControlError("canonical_input_changed", "Canonical inputs changed; use --accept-input-change to invalidate dependent stages without deleting artifacts", paths=[item["path"] for item in drift])
        return _persist_block(args, kb_root, state, error)
    if drift and args.accept_input_change:
        if not args.allow_write or args.dry_run:
            return stage_result(
                state["run_id"],
                str(state["current_stage"]),
                "needs_operator",
                reason_code="write_authorization_required",
                artifact={"changed_paths": [item["path"] for item in drift]},
                next_stage=str(state["current_stage"]),
                operator_action="Repeat control reconcile --accept-input-change with --allow-write and without --dry-run.",
            )
        for change in drift:
            invalidate_from(state, change["invalidate_from"])
            path = resolve_path_key(kb_root, change["path"])
            if path.exists():
                state["input_fingerprints"][change["path"]] = {
                    "sha256": sha256_path(path),
                    "invalidate_from": change["invalidate_from"],
                    "recorded_at": utc_now(),
                }
            else:
                state["input_fingerprints"].pop(change["path"], None)
        clear_blocked(state)
    progressed, issue = reconcile_semantic_outputs(state, kb_root, core)
    if issue is not None:
        return _persist_block(args, kb_root, state, issue)
    refresh_stage(state)
    result = derive_next_result(state, kb_root)
    if args.allow_write and not args.dry_run and (drift or progressed or was_blocked != (state.get("blocked_reason") is not None)):
        persist_state_and_result(kb_root, state, result)
    return result


def control_git_state(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    state = load_state(kb_root)
    value = classify_git_state(kb_root, args.repo_root)
    require_schema(value, "git-state.schema.json")
    artifact: Any = {"classification": value["classification"], "safe_for_kb_write": value["safe_for_kb_write"]}
    if args.allow_write and not args.dry_run:
        rel = RUN_LOG_ROOT / str(state["run_id"]) / "git-state.json"
        atomic_write_json(kb_root / rel, value)
        artifact = rel.as_posix()
    status = "ok" if value["safe_for_kb_write"] else "blocked"
    return stage_result(
        state["run_id"],
        "git_state",
        status,
        reason_code=None if status == "ok" else "git_worktree_unsafe",
        artifact=artifact,
        next_stage=compute_next_stage(state),
        operator_action=None if status == "ok" else "Resolve the reported Git operation or conflicts outside Apex KB, then rerun control git-state.",
    )


def cmd_doctor(args: argparse.Namespace) -> Dict[str, Any]:
    """Read-only self-check of the apex-kb skill package's own internal consistency - not a
    specific KB instance. Never touches --kb-root; catches the class of bug where the skill
    package itself ships internally inconsistent documentation or code."""
    root = repository_root()
    skill = skill_root()
    checks: List[Dict[str, Any]] = []

    def add_check(name: str, ok: bool, detail: str = "") -> None:
        checks.append({"check": name, "status": "ok" if ok else "fail", "detail": detail})

    schema_dir = skill / "references"
    schema_files = sorted(schema_dir.glob("*.schema.json")) if schema_dir.exists() else []
    for schema_file in schema_files:
        try:
            value = json.loads(schema_file.read_text(encoding="utf-8-sig"))
            add_check(f"schema_parses:{schema_file.name}", isinstance(value, dict), "" if isinstance(value, dict) else "schema root is not an object")
        except json.JSONDecodeError as exc:
            add_check(f"schema_parses:{schema_file.name}", False, str(exc))

    template_dir = skill / "templates"
    schema_names = {schema_file.name for schema_file in schema_files}
    template_files = sorted(template_dir.glob("*.md")) if template_dir.exists() else []
    referenced_missing: List[str] = []
    for template_file in template_files:
        text = template_file.read_text(encoding="utf-8-sig")
        for match in re.finditer(r"([\w.-]+\.schema\.json)", text):
            name = match.group(1)
            if name not in schema_names:
                referenced_missing.append(f"{template_file.name} -> {name}")
    add_check("template_schema_refs_exist", not referenced_missing, "; ".join(referenced_missing))

    def _canonical_block(text: str, key: str) -> Optional[List[str]]:
        match = re.search(rf"{key}:\n((?:  - .+\n)+)", text)
        if not match:
            return None
        return [line.strip("- ").strip() for line in match.group(1).splitlines() if line.strip()]

    skill_md_text = (skill / "SKILL.md").read_text(encoding="utf-8-sig")
    kb_contract_text = (skill / "references" / "kb-contract.md").read_text(encoding="utf-8-sig")
    skill_paths = _canonical_block(skill_md_text, "canonical_paths")
    contract_paths = _canonical_block(kb_contract_text, "canonical")
    if skill_paths is None or contract_paths is None:
        add_check("canonical_paths_match", False, "could not locate a canonical_paths block in SKILL.md and/or kb-contract.md")
    else:
        missing_from_contract = sorted(set(skill_paths) - set(contract_paths))
        missing_from_skill = sorted(set(contract_paths) - set(skill_paths))
        detail_parts = []
        if missing_from_contract:
            detail_parts.append(f"in SKILL.md only: {missing_from_contract}")
        if missing_from_skill:
            detail_parts.append(f"in kb-contract.md only: {missing_from_skill}")
        add_check("canonical_paths_match", not detail_parts, "; ".join(detail_parts))

    test_dir = root / "apex-meta" / "scripts" / "tests"
    control_tests = sorted(test_dir.glob("test_apex_kb_control*.py")) if test_dir.exists() else []
    add_check("control_test_discovery_path_resolves", len(control_tests) >= 2, f"found {len(control_tests)} at {test_dir}")

    control_path = Path(__file__).resolve()
    try:
        compile(control_path.read_text(encoding="utf-8-sig"), str(control_path), "exec")
        add_check("control_module_compiles", True)
    except SyntaxError as exc:
        add_check("control_module_compiles", False, str(exc))

    parser_for_check = argparse.ArgumentParser()
    configure_parser(parser_for_check)
    actions_choices: List[str] = []
    for action in parser_for_check._actions:
        if isinstance(action, argparse._SubParsersAction):
            actions_choices = sorted(action.choices.keys())
            break
    dispatch_source = control_path.read_text(encoding="utf-8-sig")
    missing_dispatch = [name for name in actions_choices if f'action == "{name}"' not in dispatch_source]
    add_check("every_control_action_has_dispatch_branch", not missing_dispatch, f"missing: {missing_dispatch}" if missing_dispatch else "")

    all_ok = all(item["status"] == "ok" for item in checks)
    return stage_result(
        "doctor",
        "doctor",
        "ok" if all_ok else "failed",
        reason_code=None if all_ok else "doctor_check_failed",
        artifact={"checks": checks},
        next_stage=None,
        operator_action=None if all_ok else "Fix the failing skill-package consistency check(s) listed in artifact.checks",
    )


# ---------------------------------------------------------------------------
# Parser integration, dispatch, and direct-command guard
# ---------------------------------------------------------------------------


def configure_parser(parser: argparse.ArgumentParser) -> None:
    actions = parser.add_subparsers(dest="control_action", required=True)

    init = actions.add_parser("init", help="Create canonical run intent and machine state")
    init.add_argument("--run-id", required=True)
    init.add_argument("--mode", choices=["scaffold", "ingest", "compile"], default="compile")
    init.add_argument("--operator-intent", required=True)
    init.add_argument("--kb-identity", required=True)
    init.add_argument("--source-locus", required=True)
    init.add_argument("--source-root", action="append", default=[])
    init.add_argument("--source-spec", action="append", default=[], help="Repeatable JSON object for one pointer/copy/snapshot source")
    init.add_argument("--out-of-scope", action="append", default=[])
    init.add_argument("--success-definition", required=True)
    init.add_argument("--output-tier", choices=OUTPUT_TIERS, required=True)
    init.add_argument("--output-tier-rationale", required=True)
    init.add_argument("--execution-route", choices=EXECUTION_ROUTES, required=True)
    init.add_argument("--corpus-breadth", choices=["narrow", "broad"], default="narrow")
    init.add_argument("--broad-breadth-reason")
    init.add_argument(
        "--phase1-min-coverage",
        type=float,
        default=0.6,
        help="Minimum ratio (0-1) of a topic's work-pack concentrated-candidate sources that "
        "must have a per-source analysis record before that topic's phase1 stage completes",
    )
    init.add_argument("--topic-slug", action="append", default=[])
    init.add_argument("--target-repository", required=True)
    init.add_argument("--target-commit")
    init.add_argument("--title")
    init.add_argument("--replace-unconfirmed", action="store_true")

    confirm = actions.add_parser("confirm", help="Record the operator's verbatim confirmation")
    confirm.add_argument("--confirmation-quote", required=True)

    actions.add_parser("status", help="Read and validate canonical state")
    actions.add_parser("next", help="Derive the exact next legal command or semantic trigger")
    actions.add_parser("run", help="Execute exactly the current deterministic stage or render its semantic packet")

    reconcile = actions.add_parser("reconcile", help="Resume from files, detect drift, and invalidate affected downstream stages")
    reconcile.add_argument("--accept-input-change", action="store_true")

    git_state = actions.add_parser("git-state", help="Classify Git/worktree state without mutating it")
    git_state.add_argument("--repo-root")

    actions.add_parser("doctor", help="Validate skill-package internal consistency (independent of any specific KB)")


def dispatch(args: argparse.Namespace, core: Mapping[str, Any]) -> Dict[str, Any]:
    try:
        action = args.control_action
        if action == "init":
            return control_init(args)
        if action == "confirm":
            return control_confirm(args)
        if action == "status":
            return control_status(args)
        if action == "next":
            return control_next(args)
        if action == "run":
            return control_run(args, core)
        if action == "reconcile":
            return control_reconcile(args, core)
        if action == "git-state":
            return control_git_state(args)
        if action == "doctor":
            return cmd_doctor(args)
        raise ControlError("unknown_control_action", f"Unknown control action: {action}")
    except ControlError as exc:
        run_id = "unknown"
        stage = getattr(args, "control_action", "control")
        try:
            kb_root = resolve_kb_root(args.kb_root)
            if (kb_root / RUN_STATE_PATH).exists():
                state = load_state(kb_root)
                run_id = str(state["run_id"])
                stage = str(state["current_stage"])
        except Exception:
            pass
        return stage_result(
            run_id,
            stage,
            "failed",
            reason_code=exc.code,
            artifact={"paths": exc.paths} if exc.paths else None,
            next_stage=stage,
            operator_action=exc.message,
        )


def guard_direct_command(args: argparse.Namespace) -> Optional[Dict[str, Any]]:
    """Block direct mutation only for a KB that has opted into run-state control.

    Legacy KBs without ``manifests/run-state.json`` remain compatible. A
    control-managed run must use ``control run`` so state and artifacts cannot
    drift behind a directly invoked low-level command.
    """

    command = str(getattr(args, "command", ""))
    if command == "control" or command not in CONTROLLED_DIRECT_COMMANDS:
        return None
    try:
        kb_root = resolve_kb_root(str(args.kb_root))
    except Exception:
        return None
    if not (kb_root / RUN_STATE_PATH).exists():
        return None
    try:
        state = load_state(kb_root)
        return stage_result(
            str(state["run_id"]),
            str(state["current_stage"]),
            "blocked",
            reason_code="direct_command_bypasses_control_plane",
            artifact=RUN_STATE_PATH.as_posix(),
            next_stage=compute_next_stage(state),
            operator_action=_control_command(state, "next").replace(" --allow-write", ""),
        )
    except ControlError as exc:
        return stage_result(
            "unknown",
            command,
            "blocked",
            reason_code=exc.code,
            artifact=RUN_STATE_PATH.as_posix(),
            next_stage=None,
            operator_action=exc.message,
        )
