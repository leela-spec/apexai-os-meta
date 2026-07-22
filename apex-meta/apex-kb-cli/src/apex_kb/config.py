from __future__ import annotations

import copy
import subprocess
from pathlib import Path, PureWindowsPath
from typing import Any

from .errors import ApexKBError
from .io import canonical_hash, ensure_object, safe_relative, slugify, validate_schema


def absolute_string(value: str) -> bool:
    return Path(value).expanduser().is_absolute() or PureWindowsPath(value).is_absolute()


def is_within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def overlaps(left: Path, right: Path) -> bool:
    return is_within(left, right) or is_within(right, left)


def _query(topic_slug: str, index: int, raw: Any) -> dict[str, Any]:
    if isinstance(raw, str):
        return {
            "query_id": f"{topic_slug}-q{index:02d}",
            "priority": "routine",
            "question": raw,
            "answer_requirements": [],
        }
    item = ensure_object(raw, "target query")
    question = str(item.get("question", "")).strip()
    if not question:
        raise ApexKBError("target_query_missing_question", f"Topic {topic_slug} contains a target query without a question")
    return {
        "query_id": str(item.get("query_id") or f"{topic_slug}-q{index:02d}"),
        "priority": str(item.get("priority") or "routine"),
        "question": question,
        "answer_requirements": list(item.get("answer_requirements") or []),
    }


def normalize_config(raw: Any) -> dict[str, Any]:
    """Normalize the PR #10 v1 shape and the complete v2 shape into v2."""
    config = copy.deepcopy(ensure_object(raw, "configuration"))
    source = ensure_object(config.get("source"), "source")
    destination = ensure_object(config.get("destination"), "destination")
    normalized_topics: list[dict[str, Any]] = []
    for topic_index, topic_raw in enumerate(config.get("topics") or [], 1):
        topic = ensure_object(topic_raw, f"topics[{topic_index - 1}]")
        name = str(topic.get("name", "")).strip()
        if not name:
            raise ApexKBError("topic_name_missing", f"Topic {topic_index} has no name")
        topic_id = str(topic.get("topic_id") or slugify(name))
        primary = list(topic.get("primary_phrases") or topic.get("phrases") or [])
        aliases = list(topic.get("aliases") or [])
        supporting = list(topic.get("supporting_terms") or topic.get("keywords") or [])
        negative = list(topic.get("negative_terms") or topic.get("ambiguous_or_negative_terms") or [])
        ambiguous = list(topic.get("ambiguous_terms") or [])
        raw_queries = topic.get("target_queries") or topic.get("questions") or []
        queries = [_query(topic_id, index, item) for index, item in enumerate(raw_queries, 1)]
        expected_routes = topic.get("expected_routes") or {
            "dossier": f"wiki/concepts/{topic_id}.md",
            "source_atlas": f"wiki/summaries/{topic_id}-source-atlas.md",
        }
        normalized_topics.append(
            {
                "topic_id": topic_id,
                "name": name,
                "primary_phrases": [str(item).strip() for item in primary if str(item).strip()],
                "aliases": [str(item).strip() for item in aliases if str(item).strip()],
                "supporting_terms": [str(item).strip() for item in supporting if str(item).strip()],
                "negative_terms": [str(item).strip() for item in negative if str(item).strip()],
                "ambiguous_terms": [str(item).strip() for item in ambiguous if str(item).strip()],
                "target_queries": queries,
                "expected_routes": expected_routes,
            }
        )
    options = ensure_object(config.get("run_options") or {}, "run_options")
    normalized = {
        "schema": "apex.kb.run-config.v2",
        "source": {
            "repository": str(source.get("repository", "")).strip(),
            "root": str(source.get("root", "")).strip(),
            "folders": list(source.get("folders") or []),
        },
        "destination": {
            "repository": str(destination.get("repository", "")).strip(),
            "root": str(destination.get("root", "")).strip(),
            "folder": str(destination.get("folder", "")).strip(),
        },
        "exclusions": list(config.get("exclusions") or []),
        "lifecycle_hint_rules": list(config.get("lifecycle_hint_rules") or []),
        "authority_hint_rules": list(config.get("authority_hint_rules") or []),
        "topics": normalized_topics,
        "run_options": {
            "source_handling": options.get("source_handling", "pointer_only"),
            "semantic_depth": options.get("semantic_depth", "standard"),
            "output": options.get("output", "query_ready"),
            "non_text": options.get("non_text", "inventory_and_report"),
            "git_metadata": bool(options.get("git_metadata", True)),
            "graph_depth": options.get("graph_depth", "links"),
            "ai_help_after_preflight": bool(options.get("ai_help_after_preflight", False)),
            "max_semantic_repairs": int(options.get("max_semantic_repairs", 2)),
        },
    }
    validate_schema(normalized, "run-config.schema.json")
    topic_ids = [topic["topic_id"] for topic in normalized_topics]
    if len(topic_ids) != len(set(topic_ids)):
        raise ApexKBError("duplicate_topic_id", "Topic IDs must be unique", topic_ids)
    query_ids = [query["query_id"] for topic in normalized_topics for query in topic["target_queries"]]
    if len(query_ids) != len(set(query_ids)):
        raise ApexKBError("duplicate_query_id", "Target query IDs must be unique", query_ids)
    if normalized["run_options"]["output"] in {"compiled_kb", "query_ready"}:
        missing = [topic["topic_id"] for topic in normalized_topics if not topic["target_queries"]]
        if missing:
            raise ApexKBError("target_queries_required", "Compiled outputs require target queries for every topic", missing)
    return normalized


def resolve_topology(config: dict[str, Any]) -> tuple[Path, list[tuple[str, Path]]]:
    for key, raw in (
        ("source.root", config["source"]["root"]),
        ("destination.root", config["destination"]["root"]),
    ):
        if not absolute_string(raw):
            raise ApexKBError("repository_root_not_absolute", f"{key} must be an absolute path: {raw}")
    source_root = Path(config["source"]["root"]).expanduser().resolve()
    destination_root = Path(config["destination"]["root"]).expanduser().resolve()
    if not source_root.is_dir():
        raise ApexKBError("source_root_missing", f"Source repository root does not exist: {source_root}")
    if not destination_root.is_dir():
        raise ApexKBError("destination_root_missing", f"Destination repository root does not exist: {destination_root}")
    source_folders: list[tuple[str, Path]] = []
    for raw in config["source"]["folders"]:
        rel = Path(str(raw))
        if rel.is_absolute() or ".." in rel.parts:
            raise ApexKBError("source_folder_invalid", f"Source folder must be repository-relative without '..': {raw}")
        path = (source_root / rel).resolve()
        if not is_within(path, source_root) or not path.is_dir():
            raise ApexKBError("source_folder_missing", f"Source folder does not exist: {path}")
        source_folders.append((rel.as_posix(), path))
    destination_folder = Path(config["destination"]["folder"])
    if destination_folder.is_absolute() or ".." in destination_folder.parts:
        raise ApexKBError("destination_folder_invalid", "destination.folder must be repository-relative without '..'")
    run_root = (destination_root / destination_folder).resolve()
    for _, source in source_folders:
        if overlaps(source, run_root):
            raise ApexKBError("source_destination_overlap", f"Source and destination overlap: {source} <-> {run_root}")
    return run_root, source_folders


def git_snapshot(root: Path) -> dict[str, Any]:
    value: dict[str, Any] = {
        "available": False,
        "root": str(root),
        "head": None,
        "branch": None,
        "dirty": None,
        "error": None,
    }
    try:
        head = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            check=True,
            text=True,
            capture_output=True,
            timeout=20,
        ).stdout.strip()
        branch = subprocess.run(
            ["git", "-C", str(root), "branch", "--show-current"],
            check=True,
            text=True,
            capture_output=True,
            timeout=20,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain"],
            check=True,
            text=True,
            capture_output=True,
            timeout=30,
        ).stdout
        value.update({"available": True, "head": head, "branch": branch or None, "dirty": bool(status.strip())})
    except (OSError, subprocess.SubprocessError) as exc:
        value["error"] = str(exc)
    return value


def preview_config(config: dict[str, Any]) -> tuple[Path, list[tuple[str, Path]], dict[str, Any]]:
    run_root, folders = resolve_topology(config)
    source_root = Path(config["source"]["root"]).resolve()
    destination_root = Path(config["destination"]["root"]).resolve()
    source_git = git_snapshot(source_root) if config["run_options"]["git_metadata"] else {"available": False, "disabled": True}
    destination_git = git_snapshot(destination_root) if config["run_options"]["git_metadata"] else {"available": False, "disabled": True}
    readback = {
        "schema": "apex.kb.start-preview.v2",
        "config_hash": canonical_hash(config),
        "source": {
            **config["source"],
            "resolved_root": str(source_root),
            "resolved_folders": [{"configured": rel, "resolved": str(path)} for rel, path in folders],
            "git": source_git,
        },
        "destination": {
            **config["destination"],
            "resolved_root": str(destination_root),
            "resolved_run_root": str(run_root),
            "git": destination_git,
        },
        "topics": [
            {
                "topic_id": topic["topic_id"],
                "name": topic["name"],
                "target_query_count": len(topic["target_queries"]),
                "expected_routes": topic["expected_routes"],
            }
            for topic in config["topics"]
        ],
        "exclusions": config["exclusions"],
        "lifecycle_hint_rules": config["lifecycle_hint_rules"],
        "authority_hint_rules": config["authority_hint_rules"],
        "run_options": config["run_options"],
        "planned_canonical_files": ["run-config.yaml", "run-manifest.json", "run-state.json"],
        "planned_derived_roots": ["runs/", "manifests/phase0/", "ingest-analysis/", "wiki/", "audit/", "derived/search/", "outputs/queries/", "maintenance/"],
        "warnings": [],
    }
    return run_root, folders, readback


def resolved_repository_relative(path: Path, repository_root: Path) -> str:
    return safe_relative(path, repository_root)
