#!/usr/bin/env python3
"""Strict Start frontend for Apex KB.

Reads the compact operator YAML, validates it, resolves a safe primary-main
worktree without mutating Git, derives the current control-plane inputs, writes
Start/topic-registry artifacts, and delegates run initialization to
apex_kb_control.py.

This script never fetches, pulls, creates, switches, removes, prunes, or merges
worktrees or branches. It never mixes evidence from multiple worktrees.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Dict, List, Mapping, Optional, Sequence

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover - explicit runtime blocker
    yaml = None

START_SCHEMA = "apex.kb.start-input.v2"
OUTPUT_MAP = {
    "analysis_only": "analysis_only",
    "compiled_kb": "compiled_full",
    "query_ready": "query_ready",
}
COMPAT_PHASE1_MIN_COVERAGE = 0.6
EXAMPLE_MARKERS = (
    "velvet-vice",
    "bar-operations",
    "menus-and-cocktails",
    "consent-and-play-guidelines",
    "signature cocktail menu",
    "spanking session",
)


class StartError(RuntimeError):
    def __init__(self, code: str, message: str, paths: Optional[Sequence[str]] = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.paths = list(paths or [])


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-") or "topic"


def load_control() -> Any:
    path = Path(__file__).resolve().with_name("apex_kb_control.py")
    spec = importlib.util.spec_from_file_location("apex_kb_control_for_start", path)
    if spec is None or spec.loader is None:
        raise StartError("control_runtime_unavailable", f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_config(path: Path) -> Dict[str, Any]:
    if yaml is None:
        raise StartError(
            "yaml_parser_unavailable",
            "PyYAML is required for apex_kb_start.py. Install the approved dependency before using Start.",
        )
    if not path.is_file():
        raise StartError("start_config_missing", f"Configuration file does not exist: {path}", [str(path)])
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        raise StartError("start_yaml_invalid", f"Configuration YAML is invalid: {exc}", [str(path)]) from exc
    if not isinstance(value, dict):
        raise StartError("start_root_invalid", "Start configuration must be a YAML object")
    return value


def validate_config(value: Dict[str, Any], control: Any) -> None:
    errors = control.validate_schema(value, control.load_schema("start-input.schema.json"))
    if errors:
        raise StartError("start_schema_validation_failed", "; ".join(errors[:20]))
    rendered = json.dumps(value, ensure_ascii=False).lower()
    leftovers = [item for item in EXAMPLE_MARKERS if item in rendered]
    if leftovers:
        raise StartError("example_values_not_replaced", "Replace example values: " + ", ".join(leftovers))
    for key, selected in value["run_options"].items():
        if isinstance(selected, str) and "/" in selected:
            raise StartError("unresolved_option", f"Choose one value for run_options.{key}; remove slash alternatives")


def git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ["git", "--no-optional-locks", "-C", str(repo), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=30,
            check=False,
            shell=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise StartError("git_unavailable", f"Read-only Git command failed: {exc}") from exc


def parse_worktrees(text: str) -> List[Dict[str, str]]:
    result: List[Dict[str, str]] = []
    current: Dict[str, str] = {}
    for raw in text.splitlines() + [""]:
        line = raw.strip()
        if not line:
            if current:
                result.append(current)
                current = {}
            continue
        key, _, data = line.partition(" ")
        if key == "worktree":
            current["path"] = str(Path(data).expanduser().resolve())
        elif key == "HEAD":
            current["head"] = data
        elif key == "branch":
            current["branch"] = data.removeprefix("refs/heads/")
        elif key == "detached":
            current["detached"] = "true"
    return result


def remote_slug(url: str) -> Optional[str]:
    value = url.strip().removesuffix(".git").rstrip("/")
    if value.startswith("git@") and ":" in value:
        value = value.split(":", 1)[1]
    elif "://" in value:
        value = value.split("://", 1)[1]
        value = value.split("/", 1)[1] if "/" in value else value
    parts = [item for item in value.split("/") if item]
    return "/".join(parts[-2:]) if len(parts) >= 2 else None


def resolve_primary_worktree(start: Path, repository: str, control: Any) -> Dict[str, Any]:
    probe = git(start, "rev-parse", "--show-toplevel")
    if probe.returncode:
        raise StartError("repository_not_found", probe.stderr.strip() or "No Git repository found", [str(start)])
    invoked = Path(probe.stdout.strip()).resolve()
    listing = git(invoked, "worktree", "list", "--porcelain")
    if listing.returncode:
        raise StartError("worktree_list_failed", listing.stderr.strip() or "git worktree list failed")
    worktrees = parse_worktrees(listing.stdout)
    if not worktrees:
        raise StartError("worktree_topology_empty", "Git returned no worktree records")
    primary = Path(worktrees[0]["path"]).resolve()
    branch = worktrees[0].get("branch")
    if branch != "main":
        raise StartError(
            "primary_worktree_not_main",
            f"Primary worktree is on {branch or 'detached HEAD'}, not main. Apex KB will not switch branches automatically.",
            [str(primary)],
        )
    origin = git(primary, "remote", "get-url", "origin")
    detected = remote_slug(origin.stdout) if origin.returncode == 0 else None
    if detected and detected.lower() != repository.lower():
        raise StartError(
            "repository_identity_mismatch",
            f"Configuration names {repository}, but primary worktree origin is {detected}",
            [str(primary)],
        )

    state = control.classify_git_state(primary)
    if not state.get("safe_for_kb_write"):
        raise StartError("primary_worktree_unsafe", str(state.get("reason")), state.get("changed_paths", []))
    refreshed_head = git(primary, "rev-parse", "HEAD")
    primary_head = refreshed_head.stdout.strip() if refreshed_head.returncode == 0 else worktrees[0].get("head") or state.get("head")
    return {
        "schema": "apex.kb.worktree-safety.v1",
        "policy": "primary_main_read_only",
        "invoked_root": str(invoked),
        "primary_root": str(primary),
        "fallback_applied": invoked != primary,
        "primary_branch": branch,
        "primary_head": primary_head,
        "worktree_count": len(worktrees),
        "ignored_worktrees": worktrees[1:],
        "git_state": state,
        "rules": [
            "never_fetch_or_pull",
            "never_create_worktree",
            "never_switch_branch",
            "never_mix_worktree_content",
            "never_stash_reset_clean_merge_or_rebase_operator_work",
            "write_only_to_the_configured_non_overlapping_kb_destination",
        ],
    }


def repo_path(root: Path, value: str, field: str) -> Path:
    raw = Path(value)
    if raw.is_absolute() or ".." in raw.parts:
        raise StartError("start_path_invalid", f"{field} must be repository-relative without '..': {value}")
    resolved = (root / raw).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise StartError("start_path_outside_repository", f"{field} resolves outside repository") from exc
    return resolved


def overlaps(a: Path, b: Path) -> bool:
    try:
        a.resolve().relative_to(b.resolve())
        return True
    except ValueError:
        pass
    try:
        b.resolve().relative_to(a.resolve())
        return True
    except ValueError:
        return False


def topic_registry(topics: List[Dict[str, Any]]) -> Dict[str, Any]:
    rows = []
    used: Dict[str, int] = {}
    for topic in topics:
        base = slug(topic["name"])
        used[base] = used.get(base, 0) + 1
        topic_slug = base if used[base] == 1 else f"{base}-{used[base]}"
        page = f"wiki/summaries/{topic_slug}.md"
        queries = []
        for index, question in enumerate(topic["questions"], start=1):
            queries.append({
                "query_id": f"{topic_slug}-q{index}",
                "question": question,
                "priority": "critical",
                "answer_requirements": ["Directly answer the complete operator question."],
                "expected_page": f"{page}#Macro",
                "raw_source_required": False,
            })
        rows.append({
            "slug": topic_slug,
            "name": topic["name"],
            "status": "not_started",
            "target_page": page,
            "phrases": topic["phrases"],
            "aliases": [],
            "supporting_terms": [],
            "negative_terms": topic["ambiguous_or_negative_terms"],
            "ambiguous_terms": [],
            "target_queries": queries,
        })
    return {"schema": "apex.kb.topic-registry.v2", "topics": rows}


def stable_hash(value: Any) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temp.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def success(output: str) -> str:
    return {
        "analysis_only": "Produce deterministic maps and reviewed semantic analysis for all configured questions.",
        "compiled_kb": "Produce independently accepted compiled dossiers and source atlases for all configured questions.",
        "query_ready": "Produce accepted compiled knowledge, pass postflight, and leave retrieval fresh.",
    }[output]


def run(args: argparse.Namespace) -> Dict[str, Any]:
    control = load_control()
    config_path = Path(args.config).expanduser().resolve()
    value = parse_config(config_path)
    validate_config(value, control)
    topology = resolve_primary_worktree(Path(args.repo_root or Path.cwd()).resolve(), value["repository"], control)
    root = Path(topology["primary_root"])
    sources = [
        Path(item).expanduser().resolve() if Path(item).is_absolute() else repo_path(root, item, "source_folders")
        for item in value["source_folders"]
    ]
    missing = [str(item) for item in sources if not item.is_dir()]
    if missing:
        raise StartError("source_folder_missing", "All source folders must exist", missing)
    kb_root = repo_path(root, value["kb_destination"]["folder"], "kb_destination.folder")
    for source in sources:
        if overlaps(source, kb_root):
            raise StartError("source_destination_overlap", "KB destination and source folders must not overlap", [str(source), str(kb_root)])
    registry = topic_registry(value["topics"])
    options = value["run_options"]
    frontend_output = options["output"]
    config_hash = stable_hash(value)
    run_id = f"run-{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}-{config_hash[:8]}"
    topic_slugs = [item["slug"] for item in registry["topics"]]
    topic_names = [item["name"] for item in registry["topics"]]
    exclusions = value["exclusions"]
    derived = {
        "run_id": run_id,
        "kb_root": str(kb_root),
        "kb_slug": kb_root.name,
        "operator_intent": f"Build a {frontend_output} Apex KB covering {', '.join(topic_names)}.",
        "kb_identity": f"This KB covers {', '.join(topic_names)} from {value['repository']}.",
        "source_locus": f"{value['repository']}: {', '.join(value['source_folders'])}",
        "source_roots": [str(item) for item in sources],
        "out_of_scope": [f"{item['path']} [{item['reason']}]" for item in exclusions],
        "success_definition": success(frontend_output),
        "output_tier": OUTPUT_MAP[frontend_output],
        "output_tier_rationale": f"Frontend selection {frontend_output} maps deterministically to {OUTPUT_MAP[frontend_output]}.",
        "execution_route": "terminal_backed",
        "corpus_breadth": "broad" if len(value["source_folders"]) > 1 or any(item in {".", "./"} or Path(item).is_absolute() for item in value["source_folders"]) else "narrow",
        "phase1_min_coverage": COMPAT_PHASE1_MIN_COVERAGE,
        "semantic_depth": options["semantic_depth"],
        "non_text_policy": options["non_text"],
        "source_storage_mode": options["source_handling"],
        "topic_slugs": topic_slugs,
        "target_repository": value["repository"],
        "target_commit": topology["primary_head"],
        "ai_help_after_preflight": options["ai_help_after_preflight"],
    }
    result = {
        "schema": "apex.kb.start-result.v1",
        "status": "planned" if args.dry_run or not args.allow_write else "ready",
        "submitted": value,
        "derived": derived,
        "worktree_safety": topology,
        "config_hash": config_hash,
    }
    if args.dry_run or not args.allow_write:
        result["operator_action"] = "Review derived values, then repeat with --allow-write."
        return result
    if (kb_root / "manifests/run-state.json").exists():
        raise StartError("run_state_exists", "A controlled run already exists at the KB destination")
    atomic_json(kb_root / "manifests/start-input.json", {
        "schema": START_SCHEMA,
        "submitted": value,
        "config_hash": config_hash,
        "created_at": now(),
    })
    atomic_json(kb_root / "manifests/worktree-safety.json", topology)
    atomic_json(kb_root / "manifests/topic-registry.json", registry)
    init = SimpleNamespace(
        kb_root=str(kb_root), allow_write=True, dry_run=False, strict=args.strict,
        run_id=run_id, mode="compile", operator_intent=derived["operator_intent"],
        kb_identity=derived["kb_identity"], source_locus=derived["source_locus"],
        source_root=derived["source_roots"], source_spec=[], out_of_scope=derived["out_of_scope"],
        success_definition=derived["success_definition"], output_tier=derived["output_tier"],
        output_tier_rationale=derived["output_tier_rationale"], execution_route="terminal_backed",
        corpus_breadth=derived["corpus_breadth"], broad_breadth_reason=None,
        phase1_min_coverage=derived["phase1_min_coverage"], topic_slug=topic_slugs,
        target_repository=value["repository"], target_commit=topology["primary_head"],
        title=None, replace_unconfirmed=False,
    )
    result["control_result"] = control.control_init(init)
    result["status"] = result["control_result"].get("status", "failed")
    result["operator_action"] = result["control_result"].get("operator_action")
    return result


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Apex KB strict Start frontend")
    parser.add_argument("--config", required=True)
    parser.add_argument("--repo-root")
    parser.add_argument("--allow-write", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args(argv)
    try:
        result = run(args)
    except StartError as exc:
        result = {"schema": "apex.kb.start-result.v1", "status": "blocked", "reason_code": exc.code, "message": exc.message, "paths": exc.paths}
    except Exception as exc:  # fail closed with visible error
        result = {"schema": "apex.kb.start-result.v1", "status": "error", "reason_code": "start_internal_error", "message": str(exc)}
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if result.get("status") in {"ok", "planned", "ready", "needs_operator"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
