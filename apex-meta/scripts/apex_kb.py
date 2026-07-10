#!/usr/bin/env python3
"""Deterministic lifecycle helper for Apex KB.

This script owns only deterministic work:
- scaffold and path validation
- source hashing and manifest shape
- source intake custody metadata
- Phase 0 corpus-navigation artifacts
- frontmatter, link, orphan, stale checks
- machine index section rebuild
- audit listing and status reports

It does not own semantic source interpretation, contradiction resolution, wiki
page drafting, or query answer synthesis. Default mode is dry-run; writes require
--allow-write and are restricted to the supplied --kb-root.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

AUTO_BEGIN = "<!-- BEGIN AUTO-GENERATED INDEX -->"
AUTO_END = "<!-- END AUTO-GENERATED INDEX -->"
LLM_BEGIN = "<!-- BEGIN LLM SUMMARY -->"
LLM_END = "<!-- END LLM SUMMARY -->"
PHASE2_APPROVAL = "approve ingest"
MANIFEST_PATH = Path("manifests/source-manifest.json")
SOURCE_PAYLOAD_MANIFEST_PATH = Path("manifests/source-payload-manifest.json")
PHASE0_DIR = Path("manifests/phase0")
SOURCE_INVENTORY_JSON = Path("manifests/source-inventory.json")
SOURCE_INVENTORY_CSV = Path("manifests/source-inventory.csv")
WIKI_REQUIRED_FIELDS = ["title", "page_type", "kb_slug", "source_refs", "created_at", "updated_at", "confidence", "claim_label", "status"]
CONFIDENCE_ALLOWED = {"high", "medium", "low", "mixed", "unknown"}
CLAIM_LABEL_ALLOWED = {"raw_source", "source_backed_summary", "behavioral_inference", "working_hypothesis", "operator_question", "practitioner_question"}
STATUS_ALLOWED = {"draft", "active", "needs_review", "deprecated", "superseded"}
PAGE_TYPE_ALLOWED = {"summary", "concept", "entity", "index", "query_output", "audit_item"}
PHASE2_VALUE_HEADINGS = [
    "Adaptive Ranked Source Set",
    "Macro / Meso / Micro",
    "Key Claims",
    "Routes Here",
    "Uncertainty / Raw Source Reopen Triggers",
]
QUALITY_REASON_CODES = (
    "missing_source_refs", "missing_phase2_value_sections", "placeholder_text",
    "no_key_claims", "claim_pointer_coverage_below_100_percent", "single_claim_summary",
    "single_claim_concept_thin", "concept_micro_not_evidenced", "thin_macro_meso_micro",
    "summary_source_breadth_below_profile", "no_query_routes",
)
QUALITY_REASON = {code: code for code in QUALITY_REASON_CODES}
TEXT_EXTS = {".md", ".mdx", ".txt", ".yaml", ".yml", ".json", ".csv", ".py", ".toml"}
HANDOVER_TEXT_EXTS = {".md", ".markdown", ".txt", ".yaml", ".yml"}
RAW_SUBDIRS = ["raw/articles", "raw/papers", "raw/notes", "raw/refs", "raw/other"]
REQUIRED_DIRS = RAW_SUBDIRS + ["ingest-analysis", "wiki/concepts", "wiki/entities", "wiki/summaries", "manifests", "manifests/phase0", "derived/search", "audit/resolved", "outputs/queries", "log"]
REQUIRED_FILES = ["README.md", "kb-schema.md", "wiki/index.md", "manifests/source-manifest.json"]
REPO_ROUTE_REQUIRED_FIELDS = [
    "repository",
    "branch",
    "exact_target_paths",
    "operation_class",
    "allowed_actions",
    "forbidden_actions",
    "pre_write_checks",
    "post_write_checks",
    "stop_conditions",
    "commit_strategy",
]
OPERATION_CLASS_ALLOWED = {"create", "update", "delete", "rename", "generated_output", "config_change"}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str, default: str = "item") -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or default


def resolve_kb_root(value: str) -> Path:
    return Path(value).expanduser().resolve()


def ensure_inside(root: Path, path: Path) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise SystemExit(f"Refusing path outside kb_root: {path}") from exc


def relpath(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str, kb_root: Path, allow_write: bool, dry_run: bool) -> Dict[str, Any]:
    ensure_inside(kb_root, path)
    exists = path.exists()
    changed = (not exists) or read_text(path) != text
    result = {"path": relpath(kb_root, path), "exists": exists, "changed": changed, "written": False}
    if changed and allow_write and not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        result["written"] = True
    return result


def copy_file(src: Path, dest: Path, kb_root: Path, allow_write: bool, dry_run: bool) -> Dict[str, Any]:
    ensure_inside(kb_root, dest)
    result = {"src": str(src), "dest": relpath(kb_root, dest), "written": False, "skipped": False}
    if dest.exists():
        if sha256_file(src) == sha256_file(dest):
            result["skipped"] = True
            result["reason"] = "identical_target_exists"
            return result
        result["skipped"] = True
        result["reason"] = "target_exists_with_different_hash"
        return result
    if allow_write and not dry_run:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        result["written"] = True
    return result


def effective_dry_run(args: argparse.Namespace) -> bool:
    return bool(args.dry_run or not args.allow_write)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def sha256_dir(path: Path) -> str:
    h = hashlib.sha256()
    for child in sorted(p for p in path.rglob("*") if p.is_file()):
        rel = child.relative_to(path).as_posix().encode("utf-8")
        h.update(rel + b"\0")
        with child.open("rb") as f:
            for block in iter(lambda: f.read(1024 * 1024), b""):
                h.update(block)
        h.update(b"\0")
    return h.hexdigest()




def sha256_payload_records(records: List[Dict[str, Any]]) -> str:
    """Hash a stable path/size/hash ledger without reading file bytes again."""
    h = hashlib.sha256()
    for record in sorted(records, key=lambda r: r["path"]):
        h.update(record["path"].encode("utf-8"))
        h.update(b"\0")
        h.update(str(record["size_bytes"]).encode("ascii"))
        h.update(b"\0")
        h.update(record["sha256"].encode("ascii"))
        h.update(b"\0")
    return h.hexdigest()


def load_payload_group_map(path: Optional[str]) -> Dict[str, str]:
    if not path:
        return {}
    group_map_path = Path(path).expanduser().resolve()
    loaded = json.loads(read_text(group_map_path))
    if isinstance(loaded, dict) and isinstance(loaded.get("groups"), dict):
        loaded = loaded["groups"]
    if not isinstance(loaded, dict):
        raise SystemExit("--group-map must be a JSON object or an object with a groups object")
    result: Dict[str, str] = {}
    for key, value in loaded.items():
        if not isinstance(key, str) or not isinstance(value, str) or not value.strip():
            raise SystemExit("--group-map entries must map string paths to non-empty string group names")
        result[key.replace("\\", "/").lstrip("/")] = value.strip()
    return result


def payload_group_for_file(kb_root: Path, raw_root: Path, path: Path, group_map: Dict[str, str]) -> str:
    rel_kb = relpath(kb_root, path)
    rel_raw = path.resolve().relative_to(raw_root.resolve()).as_posix()
    if rel_kb in group_map:
        return group_map[rel_kb]
    if rel_raw in group_map:
        return group_map[rel_raw]
    parts = rel_raw.split("/")
    return parts[0] if len(parts) > 1 else "root"


def iter_payload_files(raw_root: Path) -> List[Path]:
    if not raw_root.exists():
        return []
    return sorted(p for p in raw_root.rglob("*") if p.is_file())


def build_source_payload_manifest(kb_root: Path, raw_root: Optional[Path] = None, group_map_path: Optional[str] = None, include_generated_at: bool = False) -> Dict[str, Any]:
    raw_root = (raw_root or (kb_root / "raw")).expanduser().resolve()
    ensure_inside(kb_root, raw_root)
    group_map = load_payload_group_map(group_map_path)
    files: List[Dict[str, Any]] = []
    groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for path in iter_payload_files(raw_root):
        ensure_inside(kb_root, path)
        rel_raw = path.resolve().relative_to(raw_root.resolve()).as_posix()
        group = payload_group_for_file(kb_root, raw_root, path, group_map)
        record = {
            "path": relpath(kb_root, path),
            "raw_relative_path": rel_raw,
            "group": group,
            "size_bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        files.append(record)
        groups[group].append(record)
    source_groups = []
    for group_id in sorted(groups):
        records = sorted(groups[group_id], key=lambda r: r["path"])
        first = records[0]["path"] if records else "raw/"
        folder = "raw/" if group_id == "root" else "/".join(first.split("/")[:2])
        source_groups.append({
            "level": 2,
            "group_id": group_id,
            "folder": folder,
            "file_count": len(records),
            "total_size_bytes": sum(int(r["size_bytes"]) for r in records),
            "sha256": sha256_payload_records(records),
            "files": [r["path"] for r in records],
        })
    files_sorted = sorted(files, key=lambda r: r["path"])
    manifest: Dict[str, Any] = {
        "manifest_version": "1.0",
        "schema": "apex.source_payload_manifest.v1",
        "hash_algorithm": "sha256",
        "kb_slug": kb_root.name,
        "kb_root": kb_root.as_posix(),
        "payload_root": raw_root.as_posix(),
        "aggregate": {
            "level": 1,
            "file_count": len(files_sorted),
            "total_size_bytes": sum(int(r["size_bytes"]) for r in files_sorted),
            "sha256": sha256_payload_records(files_sorted),
        },
        "source_groups": source_groups,
        "files": files_sorted,
    }
    if group_map:
        manifest["grouping"] = {"default": "first-level folder under raw/", "root_group": "files directly under raw/", "group_map_entries": len(group_map)}
    else:
        manifest["grouping"] = {"default": "first-level folder under raw/", "root_group": "files directly under raw/"}
    if include_generated_at:
        manifest["generated_at"] = utc_now()
    return manifest


def hash_path(path: Path) -> Dict[str, Any]:
    p = path.expanduser().resolve()
    if not p.exists():
        return {"path": str(p), "exists": False, "hash_algorithm": "sha256", "source_hash": None}
    if p.is_dir():
        return {"path": str(p), "exists": True, "kind": "directory", "hash_algorithm": "sha256-tree", "source_hash": sha256_dir(p)}
    return {"path": str(p), "exists": True, "kind": "file", "hash_algorithm": "sha256", "source_hash": sha256_file(p), "size_bytes": p.stat().st_size}


def json_print(obj: Any) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False, sort_keys=True))


def human_print(obj: Any) -> None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                print(f"{key}:")
                print(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True))
            else:
                print(f"{key}: {value}")
    else:
        print(obj)


def emit(args: argparse.Namespace, obj: Any) -> None:
    json_print(obj) if args.json else human_print(obj)


def normalize_global_flag_placement(argv: Sequence[str]) -> Sequence[str]:
    normalized = list(argv)
    commands = {
        "scaffold", "source-intake", "hash", "generate-source-payload-manifest", "source-payload-manifest",
        "payload-manifest", "preflight", "phase0", "ingest-phase1", "ingest-phase2", "index", "query",
        "lint", "lint-repo-execution-router", "lint-historical-path-authority", "audit", "status", "health",
        "quality", "coverage", "query-eval", "graph", "process-graph", "postflight",
    }
    value_flags = {"--output-json"}
    bool_flags = {"--json", "--dry-run", "--allow-write", "--strict"}
    command_index = next((i for i, token in enumerate(normalized) if token in commands), None)
    if command_index is None:
        return normalized
    prefix = normalized[:command_index]
    command = normalized[command_index]
    suffix = normalized[command_index + 1:]
    moved: List[str] = []
    kept: List[str] = []
    i = 0
    while i < len(suffix):
        token = suffix[i]
        if token in bool_flags:
            moved.append(token)
            i += 1
        elif token in value_flags and i + 1 < len(suffix):
            moved.extend([token, suffix[i + 1]])
            i += 2
        else:
            kept.append(token)
            i += 1
    return prefix + moved + [command] + kept


def maybe_write_output_json(args: argparse.Namespace, result: Any, kb_root: Path) -> None:
    output_path = getattr(args, "output_json", None)
    if not output_path:
        return
    path = Path(output_path)
    if not path.is_absolute():
        path = kb_root / path
    ensure_inside(kb_root, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def read_manifest(kb_root: Path) -> Dict[str, Any]:
    path = kb_root / MANIFEST_PATH
    if not path.exists():
        return default_manifest(kb_root.name)
    try:
        loaded = json.loads(read_text(path))
    except Exception:
        return {"schema_version": "1.0", "kb_slug": kb_root.name, "sources": [], "manifest_error": "unreadable_json"}
    if isinstance(loaded, list):
        return {"schema_version": "legacy-list", "kb_slug": kb_root.name, "sources": loaded}
    if isinstance(loaded, dict):
        loaded.setdefault("schema_version", "1.0")
        loaded.setdefault("kb_slug", kb_root.name)
        loaded.setdefault("sources", [])
        if not isinstance(loaded["sources"], list):
            loaded["sources"] = []
        return loaded
    return default_manifest(kb_root.name)


def default_manifest(kb_slug: str) -> Dict[str, Any]:
    return {"schema_version": "1.0", "kb_slug": kb_slug, "created_at": utc_now(), "updated_at": utc_now(), "sources": []}


def manifest_text(data: Dict[str, Any]) -> str:
    data = dict(data)
    data["updated_at"] = utc_now()
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def parse_minimal_yaml(text: str) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    current_key: Optional[str] = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        lm = re.match(r"^\s*-\s+(.*)$", line)
        if lm and current_key:
            data.setdefault(current_key, []).append(strip_scalar(lm.group(1)))
            continue
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            data[key] = [] if value == "" else strip_scalar(value)
    return data


def strip_scalar(value: str) -> Any:
    value = value.strip()
    if value == "[]":
        return []
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_frontmatter(markdown: str) -> Tuple[Dict[str, Any], str, str]:
    lines = markdown.splitlines()
    if not lines or lines[0].strip().lstrip("\ufeff") != "---":
        return {}, markdown, "missing"
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip().lstrip("\ufeff") == "---":
            end = i
            break
    if end is None:
        return {}, markdown, "malformed"
    fm = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1 :])
    try:
        if importlib.util.find_spec("yaml") is not None:
            import yaml  # type: ignore

            loaded = yaml.safe_load(fm)
            meta = loaded if isinstance(loaded, dict) else {}
        else:
            meta = parse_minimal_yaml(fm)
        return meta, body, "parsed"
    except Exception:
        return parse_minimal_yaml(fm), body, "detected"


def starter_readme(kb_slug: str, title: str) -> str:
    return f"""# {title}

This Apex KB root is a source-preserving knowledge base for `{kb_slug}`.

Canonical paths:

- `raw/` preserves source files or durable pointers.
- `ingest-analysis/` stores Phase 1 LLM analysis before operator approval.
- `wiki/` stores approved compiled KB pages.
- `manifests/source-manifest.json` records source custody and hashes.
- `manifests/phase0/` stores deterministic navigation artifacts.
- `derived/search/` stores rebuildable retrieval indexes.
- `audit/` stores open and resolved review items.
- `outputs/queries/` stores reusable cited query packets.

Apex KB must not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap,
APSU, or personal orchestration state. Other systems may consume KB outputs as
read-only evidence packets.
"""


def starter_schema(kb_slug: str, topic_title: str) -> str:
    return f"""# KB Schema - {topic_title}

```yaml
kb_schema:
  kb_slug: "{kb_slug}"
  kb_topic_title: "{topic_title}"
  kb_source_authority_list:
    - authority_level: primary
      description: "Original source material, project-controlled contracts, direct operator-provided evidence."
    - authority_level: secondary
      description: "Interpretive summaries, implementation reports, validated external references."
    - authority_level: tertiary
      description: "Background material used only for orientation."
  kb_concept_taxonomy_top_level:
    - concepts
    - entities
    - summaries
    - contradictions
    - open_questions
  kb_language_policy:
    primary_language: english
    preserve_source_language_when_relevant: true
  kb_operator_review_policy:
    ingest_phase_2_requires_phrase: "approve ingest"
    same_prompt_approval_allowed: false
    contradiction_handling: "expose, do not silently resolve"
```
"""


def starter_index(kb_slug: str, title: str) -> str:
    return f"""---
title: "{title} Index"
page_type: index
kb_slug: "{kb_slug}"
source_refs: []
created_at: "{utc_now()}"
updated_at: "{utc_now()}"
confidence: "unknown"
claim_label: "source_backed_summary"
status: "active"
---

# {title} Index

{AUTO_BEGIN}

No compiled wiki pages indexed yet.

{AUTO_END}

{LLM_BEGIN}

No LLM summary has been approved yet.

{LLM_END}
"""


def cmd_scaffold(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    title = args.title or args.topic_title or kb_root.name.replace("-", " ").title()
    planned_dirs = [kb_root / d for d in REQUIRED_DIRS]
    dir_results = []
    for d in planned_dirs:
        ensure_inside(kb_root, d)
        exists = d.exists()
        if args.allow_write and not dry_run:
            d.mkdir(parents=True, exist_ok=True)
        dir_results.append({"path": relpath(kb_root, d), "exists": exists, "created": bool(args.allow_write and not dry_run and not exists)})
    writes = [
        write_text(kb_root / "README.md", starter_readme(kb_root.name, title), kb_root, args.allow_write, dry_run),
        write_text(kb_root / "kb-schema.md", starter_schema(kb_root.name, title), kb_root, args.allow_write, dry_run),
        write_text(kb_root / "wiki/index.md", starter_index(kb_root.name, title), kb_root, args.allow_write, dry_run),
        write_text(kb_root / MANIFEST_PATH, manifest_text(default_manifest(kb_root.name)), kb_root, args.allow_write, dry_run),
    ]
    return {"command": "scaffold", "kb_root": str(kb_root), "dry_run": dry_run, "directories": dir_results, "writes": writes}


def source_type_dir(source_type: str) -> str:
    return {"article": "articles", "paper": "papers", "note": "notes", "ref": "refs"}.get(source_type, "other")


def cmd_hash(args: argparse.Namespace) -> Dict[str, Any]:
    return {"command": "hash", **hash_path(Path(args.path))}


def duplicate_hashes(manifest: Dict[str, Any], source_hash: Optional[str]) -> List[Dict[str, Any]]:
    if not source_hash:
        return []
    return [s for s in manifest.get("sources", []) if isinstance(s, dict) and s.get("source_hash") == source_hash]


def cmd_source_intake(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    src = Path(args.source_path).expanduser().resolve() if args.source_path else None
    source_id = args.source_id or slugify(Path(args.source_path).stem if args.source_path else args.pointer or "source")
    storage_mode = args.storage_mode
    source_type = args.source_type
    hash_info = hash_path(src) if src else {"source_hash": "NA", "hash_algorithm": "NA", "exists": False}
    manifest = read_manifest(kb_root)
    copies: List[Dict[str, Any]] = []
    stored_path = args.pointer or (str(src) if src else "NA")
    if storage_mode in {"copy_into_kb", "snapshot_copy"}:
        if not src or not src.exists() or not src.is_file():
            return {"command": "source-intake", "status": "blocked", "reason": "copy modes require an existing source file", "source_path": str(src) if src else None}
        dest = kb_root / "raw" / source_type_dir(source_type) / src.name
        copies.append(copy_file(src, dest, kb_root, args.allow_write, dry_run))
        stored_path = relpath(kb_root, dest)
    entry = {
        "source_id": source_id,
        "title": args.title or source_id.replace("-", " ").title(),
        "source_type": source_type,
        "source_storage_mode": storage_mode,
        "source_path": stored_path,
        "original_source_path": str(src) if src else args.pointer or "NA",
        "source_hash": hash_info.get("source_hash") or "NA",
        "hash_algorithm": hash_info.get("hash_algorithm") or "NA",
        "no_hash_reason": "NA" if hash_info.get("source_hash") else ("pointer_only" if storage_mode == "pointer_only" else "source_unavailable"),
        "ingest_status": "source_intake_only",
        "status": "active",
        "added_at": utc_now(),
    }
    existing_ids = {s.get("source_id") for s in manifest.get("sources", []) if isinstance(s, dict)}
    dupes = duplicate_hashes(manifest, entry["source_hash"] if entry["source_hash"] != "NA" else None)
    blocked = source_id in existing_ids and not args.as_version
    if not blocked:
        if source_id in existing_ids:
            base = source_id
            n = 2
            while f"{base}-v{n}" in existing_ids:
                n += 1
            entry["source_id"] = f"{base}-v{n}"
        if not dupes or args.allow_duplicate:
            manifest.setdefault("sources", []).append(entry)
    write = None if blocked else write_text(kb_root / MANIFEST_PATH, manifest_text(manifest), kb_root, args.allow_write, dry_run)
    return {"command": "source-intake", "dry_run": dry_run, "status": "blocked" if blocked else "ok", "entry": entry, "duplicate_hash_candidates": dupes, "copies": copies, "manifest_write": write}


def cmd_preflight(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    manifest = read_manifest(kb_root)
    source_hash = None
    source_exists = None
    existing_analysis = []
    if args.source_path:
        h = hash_path(Path(args.source_path))
        source_hash = h.get("source_hash")
        source_exists = h.get("exists")
        source_slug = slugify(Path(args.source_path).stem)
        existing_analysis = [relpath(kb_root, p) for p in (kb_root / "ingest-analysis").glob(f"{source_slug}*.analysis.md")] if (kb_root / "ingest-analysis").exists() else []
    checks = {
        "kb_root_exists": kb_root.exists(),
        "kb_schema_exists": (kb_root / "kb-schema.md").exists(),
        "source_manifest_exists": (kb_root / MANIFEST_PATH).exists(),
        "source_exists": source_exists,
        "duplicate_source_hash_candidates": duplicate_hashes(manifest, source_hash),
        "existing_phase_1_analysis": existing_analysis,
        "index_freshness": stale_index_status(kb_root),
    }
    status = "ok" if checks["kb_root_exists"] and checks["kb_schema_exists"] and checks["source_manifest_exists"] else "blocked"
    return {"command": "preflight", "status": status, "kb_root": str(kb_root), "checks": checks}


def iter_source_files(kb_root: Path) -> List[Path]:
    roots = [kb_root / "sources", kb_root / "raw"]
    excluded_parts = {"manifests", "wiki", "ingest-analysis", "derived", "outputs", "audit", "log"}
    files: List[Path] = []
    seen: set[Path] = set()
    for root in roots:
        if root.exists():
            for p in sorted(root.rglob("*")):
                try:
                    rel_parts = set(p.relative_to(kb_root).parts)
                except ValueError:
                    rel_parts = set()
                resolved = p.resolve()
                if p.is_file() and p.suffix.lower() in TEXT_EXTS and not (rel_parts & excluded_parts) and resolved not in seen:
                    files.append(p)
                    seen.add(resolved)
    return files


def read_source_inventory(kb_root: Path) -> Dict[str, Any]:
    json_path = kb_root / SOURCE_INVENTORY_JSON
    csv_path = kb_root / SOURCE_INVENTORY_CSV
    result: Dict[str, Any] = {
        "json_path": SOURCE_INVENTORY_JSON.as_posix(),
        "json_exists": json_path.exists(),
        "json_readable": False,
        "json_entry_count": 0,
        "csv_path": SOURCE_INVENTORY_CSV.as_posix(),
        "csv_exists": csv_path.exists(),
        "csv_readable": False,
        "csv_entry_count": 0,
        "errors": [],
    }
    if json_path.exists():
        try:
            loaded = json.loads(json_path.read_text(encoding="utf-8-sig"))
            entries = loaded if isinstance(loaded, list) else loaded.get("sources", []) if isinstance(loaded, dict) else []
            result["json_readable"] = isinstance(entries, list)
            result["json_entry_count"] = len(entries) if isinstance(entries, list) else 0
        except Exception as exc:
            result["errors"].append({"path": SOURCE_INVENTORY_JSON.as_posix(), "error": str(exc)})
    if csv_path.exists():
        try:
            with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
                result["csv_entry_count"] = sum(1 for _ in csv.DictReader(f))
            result["csv_readable"] = True
        except Exception as exc:
            result["errors"].append({"path": SOURCE_INVENTORY_CSV.as_posix(), "error": str(exc)})
    return result




def cmd_generate_source_payload_manifest(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    raw_root = Path(args.raw_root).expanduser().resolve() if args.raw_root else kb_root / "raw"
    output = Path(args.output).expanduser().resolve() if args.output else kb_root / SOURCE_PAYLOAD_MANIFEST_PATH
    ensure_inside(kb_root, raw_root)
    ensure_inside(kb_root, output)
    manifest = build_source_payload_manifest(kb_root, raw_root, args.group_map, args.include_generated_at)
    text = json.dumps(manifest, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    write = write_text(output, text, kb_root, args.allow_write, dry_run)
    return {
        "command": "generate-source-payload-manifest",
        "dry_run": dry_run,
        "output": relpath(kb_root, output),
        "payload_root": relpath(kb_root, raw_root),
        "file_count": manifest["aggregate"]["file_count"],
        "total_size_bytes": manifest["aggregate"]["total_size_bytes"],
        "root_sha256": manifest["aggregate"]["sha256"],
        "group_count": len(manifest["source_groups"]),
        "write": write,
    }


def parse_markdown_structure(path: Path, kb_root: Path) -> Dict[str, Any]:
    text = read_text(path)
    meta, body, fm_status = parse_frontmatter(text)
    lines = text.splitlines()
    headings = []
    links = []
    wikilinks = []
    code_blocks = []
    in_fence = False
    fence_start = 0
    fence_lang = ""
    fence_marker = ""
    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        fm = re.match(r"^(```+|~~~+)\s*([^`]*)$", stripped)
        if fm:
            marker = fm.group(1)[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
                fence_start = idx
                fence_lang = fm.group(2).strip().split()[0] if fm.group(2).strip() else ""
            elif marker == fence_marker:
                code_blocks.append({"language": fence_lang, "start_line": fence_start, "end_line": idx})
                in_fence = False
            continue
        if not in_fence:
            hm = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
            if hm:
                headings.append({"level": len(hm.group(1)), "text": re.sub(r"\s+#*$", "", hm.group(2)).strip(), "line": idx})
            for lm in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", line):
                target = lm.group(2).strip()
                links.append({"text": lm.group(1), "target": target, "line": idx, "target_type": link_target_type(target), "normalized_target": normalize_link_target(target)})
            for wm in re.finditer(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", line):
                wikilinks.append({"raw": wm.group(0), "target": wm.group(1).strip(), "alias": (wm.group(2) or "").strip() or None, "line": idx})
    return {
        "path": relpath(kb_root, path),
        "source_type_guess": source_type_guess(path),
        "h1_title": next((h["text"] for h in headings if h["level"] == 1), None),
        "headings": headings,
        "markdown_links": links,
        "wikilinks": wikilinks,
        "code_blocks": code_blocks,
        "frontmatter": {"has_frontmatter": bool(meta), "raw_field_keys": sorted(meta.keys()), "parse_status": fm_status},
        "parser_warnings": (["unclosed_code_fence"] if in_fence else []),
    }


def link_target_type(target: str) -> str:
    if target.startswith("http://") or target.startswith("https://"):
        return "absolute_url"
    if target.startswith("#"):
        return "anchor"
    if target.startswith("/"):
        return "absolute_path"
    if target:
        return "relative_file"
    return "unknown"


def normalize_link_target(target: str) -> Optional[str]:
    if target.startswith("http://") or target.startswith("https://"):
        return target
    return target.split("#", 1)[0] or None


def source_type_guess(path: Path) -> str:
    lower = path.as_posix().lower()
    if "/sources/curated/academic/" in lower:
        return "academic"
    if "/sources/curated/official-docs/" in lower or "/sources/curated/official-repos/" in lower or "/sources/curated/official-pdfs/" in lower:
        return "official"
    if "/sources/operator-supplied/" in lower:
        return "operator_supplied"
    if "/papers/" in lower:
        return "paper"
    if "/articles/" in lower:
        return "article"
    if "/notes/" in lower:
        return "note"
    if "/refs/" in lower:
        return "ref"
    return "other"


def cmd_phase0(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    manifest = read_manifest(kb_root)
    inventory = read_source_inventory(kb_root)
    files = iter_source_files(kb_root)
    seen_resolved = {os.path.normcase(str(p.resolve())) for p in files}
    pointer_statuses = pointer_only_source_status(kb_root, manifest)
    pointer_files: List[Path] = []
    for status_entry in pointer_statuses:
        if status_entry["status"] != "resolved":
            continue
        resolved_path = Path(status_entry["resolved_path"])
        key = os.path.normcase(str(resolved_path))
        if key in seen_resolved:
            continue
        seen_resolved.add(key)
        pointer_files.append(resolved_path)
    scanned_files = files + pointer_files
    structures = [parse_markdown_structure(p, kb_root) for p in scanned_files]
    heading_map = [{"path": r["path"], "source_type_guess": r["source_type_guess"], "h1_title": r["h1_title"], "headings": r["headings"], "parser_warnings": r["parser_warnings"]} for r in structures]
    link_map = [{"path": r["path"], "markdown_links": r["markdown_links"], "wikilinks": r["wikilinks"]} for r in structures]
    frontmatter_map = [{"path": r["path"], **r["frontmatter"]} for r in structures]
    keyword_hits, topic_map = keyword_artifacts(kb_root, scanned_files)
    profile = corpus_profile(kb_root, scanned_files, structures, keyword_hits, inventory)
    priority = priority_candidates(kb_root, scanned_files, structures, keyword_hits)
    report = phase0_report(kb_root, scanned_files, structures)
    writes = [
        write_text(kb_root / PHASE0_DIR / "corpus-profile.md", profile, kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "heading-map.json", json.dumps(heading_map, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "markdown-link-map.json", json.dumps(link_map, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "frontmatter-map.json", json.dumps(frontmatter_map, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "keyword-hits.ndjson", "".join(json.dumps(h, ensure_ascii=False, sort_keys=True) + "\n" for h in keyword_hits), kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "topic-file-map.json", json.dumps(topic_map, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "source-priority-candidates.md", priority, kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "phase0-navigation-report.md", report, kb_root, args.allow_write, dry_run),
    ]
    warning_count = sum(1 for s in pointer_statuses if s["status"] != "resolved")
    unresolved = [s for s in pointer_statuses if s["status"] != "resolved"]
    result = {
        "command": "phase0",
        "dry_run": dry_run,
        "source_file_count": len(files),
        "source_inventory": inventory,
        "artifact_count": len(writes),
        "writes": writes,
        "phase_boundary": "no ingest-analysis, wiki semantic pages, embeddings, or vector stores created",
        "pointer_only_source_status": pointer_statuses,
        "pointer_only_scanned_count": len(pointer_files),
        "pointer_only_warning_count": warning_count,
        "pointer_only_unresolved": unresolved,
    }
    return result


POINTER_URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*://")
POINTER_UNSUPPORTED_PREFIXES = ("mailto:", "s3:", "\\\\")


def _path_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def find_repo_root(kb_root: Path, max_hops: int = 6) -> Optional[Path]:
    """Bounded ancestor walk for a `.git`/`apex-meta` marker. Never shells to
    git and never widens beyond kb_root's own ancestors; returns None (skip
    the repo-root fallback) rather than guessing when no marker is found."""
    current = kb_root.resolve()
    for _ in range(max_hops):
        if (current / ".git").exists() or (current / "apex-meta").is_dir():
            return current
        if current.parent == current:
            break
        current = current.parent
    return None


def pointer_only_source_entries(manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    sources = manifest.get("sources", [])
    if not isinstance(sources, list):
        return []
    entries = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        storage_mode = source.get("source_storage_mode") or source.get("storage_mode")
        if storage_mode != "pointer_only":
            continue
        pointer = source.get("source_path") or source.get("pointer")
        source_id = str(source.get("source_id") or source.get("id") or "unknown")
        entries.append({"source_id": source_id, "pointer": str(pointer) if pointer else None})
    return entries


def pointer_only_manifest_sources(kb_root: Path) -> List[str]:
    manifest = read_manifest(kb_root)
    return [entry["source_id"] for entry in pointer_only_source_entries(manifest)]


def resolve_pointer_only_path(kb_root: Path, repo_root: Optional[Path], pointer: str) -> Tuple[Optional[Path], Optional[str]]:
    pointer = pointer.strip()
    if not pointer:
        return None, "missing_pointer"
    if POINTER_URL_SCHEME_RE.match(pointer) or pointer.startswith(POINTER_UNSUPPORTED_PREFIXES):
        return None, "unsupported_scheme"
    normalized = pointer.replace("\\", "/")
    p = Path(normalized)
    allowed_roots = [kb_root.resolve()] + ([repo_root.resolve()] if repo_root else [])
    candidates = [p] if p.is_absolute() else [kb_root / normalized] + ([repo_root / normalized] if repo_root else [])
    reason = "not_found"
    for candidate in candidates:
        try:
            resolved = candidate.resolve()
        except OSError:
            reason = "invalid_path"
            continue
        if not any(_path_within(resolved, root) for root in allowed_roots):
            reason = "out_of_bounds"
            continue
        if not resolved.exists():
            reason = "not_found"
            continue
        if not resolved.is_file():
            reason = "not_a_file"
            continue
        if resolved.suffix.lower() not in TEXT_EXTS:
            return None, "unsupported_extension"
        return resolved, None
    return None, reason


def pointer_only_source_status(kb_root: Path, manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    repo_root = find_repo_root(kb_root)
    statuses = []
    for entry in pointer_only_source_entries(manifest):
        source_id, pointer = entry["source_id"], entry["pointer"]
        if not pointer:
            statuses.append({"source_id": source_id, "pointer": None, "status": "unresolved", "resolved_path": None, "reason": "missing_pointer"})
            continue
        try:
            resolved, reason = resolve_pointer_only_path(kb_root, repo_root, pointer)
        except Exception:
            resolved, reason = None, "internal_error"
        if resolved is None:
            statuses.append({"source_id": source_id, "pointer": pointer, "status": "unresolved", "resolved_path": None, "reason": reason})
        else:
            statuses.append({"source_id": source_id, "pointer": pointer, "status": "resolved", "resolved_path": str(resolved), "reason": None})
    return statuses


def resolve_pointer_only_text_files(kb_root: Path, manifest: Dict[str, Any]) -> List[str]:
    return [s["resolved_path"] for s in pointer_only_source_status(kb_root, manifest) if s["status"] == "resolved"]


def keyword_groups() -> Dict[str, List[str]]:
    return {
        "apex_kb": ["apex kb", "source manifest", "kb-schema", "ingest-analysis", "wiki/index"],
        "ingest": ["phase 1", "phase 2", "approve ingest", "operator gate", "contradiction"],
        "retrieval": ["fts5", "bm25", "sqlite", "query", "search index"],
        "skill_design": ["skill", "skill.md", "claude", "agent skills"],
        "orchestration_boundary": ["apex plan", "apex sync", "apex session", "precap", "flowrecap"],
    }


def keyword_artifacts(kb_root: Path, files: List[Path]) -> Tuple[List[Dict[str, Any]], Dict[str, List[str]]]:
    hits: List[Dict[str, Any]] = []
    topic_files: Dict[str, set] = {k: set() for k in keyword_groups()}
    for path in files:
        try:
            lines = read_text(path).splitlines()
        except Exception:
            continue
        for idx, line in enumerate(lines, start=1):
            low = line.lower()
            for group, keywords in keyword_groups().items():
                for kw in keywords:
                    if kw.lower() in low:
                        record = {"query_group": group, "keyword": kw, "path": relpath(kb_root, path), "line": idx, "snippet": line.strip()[:220]}
                        hits.append(record)
                        topic_files[group].add(record["path"])
    return hits, {k: sorted(v) for k, v in topic_files.items()}


def corpus_profile(kb_root: Path, files: List[Path], structures: List[Dict[str, Any]], hits: List[Dict[str, Any]], inventory: Optional[Dict[str, Any]] = None) -> str:
    ext_counts = Counter(p.suffix.lower() or "[none]" for p in files)
    sizes = [(relpath(kb_root, p), p.stat().st_size) for p in files]
    sizes.sort(key=lambda x: x[1], reverse=True)
    warnings = Counter(w for s in structures for w in s.get("parser_warnings", []))
    noise = [path for path, size in sizes if size > 1_000_000 or any(part in path.lower() for part in ["node_modules", "dist/", "build/", "vendor/"])]
    lines = ["# Phase 0 Corpus Profile", "", f"Generated: `{utc_now()}`", "", "## source_inventory_status", ""]
    if inventory:
        lines.extend([
            f"- JSON inventory present: `{inventory.get('json_exists')}`",
            f"- JSON inventory readable: `{inventory.get('json_readable')}`",
            f"- JSON inventory entries: `{inventory.get('json_entry_count')}`",
            f"- CSV inventory present: `{inventory.get('csv_exists')}`",
            f"- CSV inventory readable: `{inventory.get('csv_readable')}`",
            f"- CSV inventory entries: `{inventory.get('csv_entry_count')}`",
        ])
        if inventory.get("errors"):
            lines.append(f"- Inventory warnings: `{len(inventory.get('errors', []))}`")
    else:
        lines.append("- Inventory status: `not_checked`")
    lines.extend(["", f"- Source roots scanned: `sources/`, `raw/`", f"- Files scanned: `{len(files)}`", f"- Total bytes: `{sum(size for _, size in sizes)}`", "", "## file_count_by_extension", ""])
    for ext, count in sorted(ext_counts.items()):
        lines.append(f"- `{ext}`: {count}")
    lines.extend(["", "## largest_files", ""])
    for path, size in sizes[:20]:
        lines.append(f"- `{path}`: {size} bytes")
    lines.extend(["", "## likely_generated_or_noise_files", ""])
    lines.extend([f"- `{p}`" for p in noise[:50]] or ["- none detected"])
    lines.extend(["", "## duplicate_hash_groups", ""])
    by_hash: Dict[str, List[str]] = defaultdict(list)
    for p in files:
        try:
            by_hash[sha256_file(p)].append(relpath(kb_root, p))
        except Exception:
            pass
    dupes = [v for v in by_hash.values() if len(v) > 1]
    if dupes:
        for group in dupes[:20]:
            lines.append("- " + ", ".join(f"`{x}`" for x in group))
    else:
        lines.append("- none detected")
    lines.extend(["", "## source_group_summary", ""])
    group_counts = Counter(source_type_guess(p) for p in files)
    for group, count in sorted(group_counts.items()):
        lines.append(f"- `{group}`: {count}")
    lines.extend(["", "## parser_warning_summary", ""])
    if warnings:
        for warning, count in sorted(warnings.items()):
            lines.append(f"- `{warning}`: {count}")
    else:
        lines.append("- none detected")
    lines.extend(["", "## keyword_hit_summary", ""])
    hit_counts = Counter(h["query_group"] for h in hits)
    for group, count in sorted(hit_counts.items()):
        lines.append(f"- `{group}`: {count}")
    return "\n".join(lines) + "\n"


def priority_candidates(kb_root: Path, files: List[Path], structures: List[Dict[str, Any]], hits: List[Dict[str, Any]]) -> str:
    hit_by_path = Counter(h["path"] for h in hits)
    rows = []
    struct_by_path = {s["path"]: s for s in structures}
    for p in files:
        rel = relpath(kb_root, p)
        s = struct_by_path.get(rel, {})
        score = hit_by_path[rel] * 3 + len(s.get("headings", [])) + min(p.stat().st_size // 20000, 5)
        rows.append((score, rel, p.stat().st_size, len(s.get("headings", [])), hit_by_path[rel]))
    rows.sort(key=lambda x: (-x[0], x[1]))
    lines = ["# Source Priority Candidates", "", "These candidates are deterministic navigation hints, not semantic authority rankings.", "", "| score | path | bytes | headings | keyword_hits |", "|---:|---|---:|---:|---:|"]
    for score, rel, size, headings, hit_count in rows[:50]:
        lines.append(f"| {score} | `{rel}` | {size} | {headings} | {hit_count} |")
    return "\n".join(lines) + "\n"


def phase0_report(kb_root: Path, files: List[Path], structures: List[Dict[str, Any]]) -> str:
    return f"""# Phase 0 Navigation Report

Generated: `{utc_now()}`
KB root: `{kb_root}`
Files scanned: `{len(files)}`

## Artifacts

- `corpus-profile.md`
- `heading-map.json`
- `markdown-link-map.json`
- `frontmatter-map.json`
- `keyword-hits.ndjson`
- `topic-file-map.json`
- `source-priority-candidates.md`
- `phase0-navigation-report.md`

## Boundary

This Phase 0 run created deterministic navigation artifacts only. It did not
create Phase 1 semantic analysis, Phase 2 wiki pages, embeddings, vector stores,
Plan/Sync/Session state, PreCap outputs, FlowRecap outputs, or APSU outputs.
"""


def cmd_ingest_phase1(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    if not args.source_path:
        return {"command": "ingest-phase1", "status": "blocked", "reason": "--source-path is required"}
    src = Path(args.source_path).expanduser().resolve()
    h = hash_path(src)
    source_slug = args.source_slug or slugify(src.stem)
    path = kb_root / "ingest-analysis" / f"{source_slug}.analysis.md"
    text = ingest_analysis_shell(kb_root.name, source_slug, args.source_path, h)
    write = write_text(path, text, kb_root, args.allow_write, dry_run)
    return {"command": "ingest-phase1", "status": "operator_review_needed", "dry_run": dry_run, "analysis_shell": write, "required_halt": True, "phase_2_requires": PHASE2_APPROVAL, "semantic_note": "Shell only; LLM must fill semantic sections from the source."}


def ingest_analysis_shell(kb_slug: str, source_slug: str, source_path: str, h: Dict[str, Any]) -> str:
    return f"""---
analysis_id: "{kb_slug}-{source_slug}-analysis"
kb_slug: "{kb_slug}"
source_slug: "{source_slug}"
source_path: "{source_path}"
source_hash: "{h.get('source_hash') or 'NA'}"
hash_algorithm: "{h.get('hash_algorithm') or 'NA'}"
created_at: "{utc_now()}"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
required_confirmation_phrase: "approve ingest"
---

# Phase 1 Ingest Analysis - {source_slug}

## Source Identity

LLM must fill from source evidence only.

## Source Summary

LLM must fill from source evidence only.

## Extraction Candidates

LLM must list candidate definitions, processes, concepts, entities, claims, contradictions, and open questions.

## Proposed Wiki Changes

No wiki pages may be generated until the operator replies in a separate turn with: `approve ingest`.

## Operator Gate

```yaml
phase_2_allowed: false
required_confirmation_phrase: "approve ingest"
```
"""


def cmd_ingest_phase2(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    approved = args.approval_phrase == PHASE2_APPROVAL
    analysis_path = kb_root / "ingest-analysis" / args.analysis if args.analysis else None
    analysis_exists = bool(analysis_path and analysis_path.exists())
    status = "ok" if approved and analysis_exists else "blocked"
    return {"command": "ingest-phase2", "status": status, "approval_phrase_valid": approved, "analysis_exists": analysis_exists, "writes_performed": False, "llm_required_next": status == "ok", "boundary": "Python validates the gate; LLM drafts approved wiki pages with source pointers."}


def wiki_pages(kb_root: Path) -> List[Path]:
    root = kb_root / "wiki"
    if not root.exists():
        return []
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def page_row(kb_root: Path, path: Path) -> Dict[str, Any]:
    meta, body, _ = parse_frontmatter(read_text(path))
    title = meta.get("title") or next((m.group(1).strip() for line in body.splitlines() if (m := re.match(r"^#\s+(.+)", line))), path.stem)
    return {"rel_path": relpath(kb_root, path), "title": str(title), "page_type": str(meta.get("page_type", "unknown")), "status": str(meta.get("status", "unknown")), "confidence": str(meta.get("confidence", "unknown"))}


def machine_index_section(kb_root: Path) -> str:
    pages = [p for p in wiki_pages(kb_root) if p.name != "index.md"]
    by_type: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for p in pages:
        row = page_row(kb_root, p)
        by_type[row["page_type"]].append(row)
    lines = [AUTO_BEGIN, "", f"Generated: `{utc_now()}`", "", f"Compiled page count: `{len(pages)}`", ""]
    for page_type in sorted(by_type):
        lines.append(f"## {page_type.title()} Pages")
        lines.append("")
        for row in sorted(by_type[page_type], key=lambda r: r["rel_path"]):
            lines.append(f"- [{row['title']}]({row['rel_path'].replace('wiki/', '')}) - `{row['status']}` / `{row['confidence']}`")
        lines.append("")
    lines.append(AUTO_END)
    return "\n".join(lines)


def replace_between_markers(text: str, replacement: str) -> str:
    if AUTO_BEGIN in text and AUTO_END in text:
        pattern = re.compile(re.escape(AUTO_BEGIN) + r".*?" + re.escape(AUTO_END), re.S)
        return pattern.sub(replacement, text)
    return text.rstrip() + "\n\n" + replacement + "\n"


def cmd_index(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    index_path = kb_root / "wiki/index.md"
    current = read_text(index_path) if index_path.exists() else starter_index(kb_root.name, kb_root.name.replace("-", " ").title())
    new = replace_between_markers(current, machine_index_section(kb_root))
    write = write_text(index_path, new, kb_root, args.allow_write, dry_run)
    return {"command": "index", "dry_run": dry_run, "write": write, "page_count": len(wiki_pages(kb_root))}


def cmd_query(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    script_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(script_dir))
    try:
        import apex_kb_retrieval  # type: ignore

        packet = apex_kb_retrieval.query_kb(kb_root, args.query, args.limit)
        if args.save:
            packet["saved_query_output"] = apex_kb_retrieval.save_query_packet(kb_root, packet, args.allow_write, effective_dry_run(args), None)
        return {"command": "query", **packet}
    except Exception as exc:
        return {"command": "query", "backend": "simple_markdown_fallback", "error_from_retrieval_module": str(exc), "results": simple_query(kb_root, args.query, args.limit)}


def simple_query(kb_root: Path, query: str, limit: int) -> List[Dict[str, Any]]:
    terms = [t.lower() for t in re.findall(r"[A-Za-z0-9_]+", query) if len(t) > 1]
    scored = []
    for p in wiki_pages(kb_root):
        text = read_text(p)
        lower = text.lower()
        score = sum(lower.count(t) for t in terms)
        if score:
            scored.append((score, {"rel_path": relpath(kb_root, p), "score": score, "snippet": text[:240].replace("\n", " ")}))
    scored.sort(key=lambda x: (-x[0], x[1]["rel_path"]))
    return [r for _, r in scored[:limit]]


def lint_frontmatter(kb_root: Path) -> List[Dict[str, Any]]:
    issues: List[Dict[str, Any]] = []
    for p in wiki_pages(kb_root):
        meta, _body, status = parse_frontmatter(read_text(p))
        rel = relpath(kb_root, p)
        if status in {"missing", "malformed"}:
            issues.append({"type": "frontmatter", "path": rel, "issue": status})
            continue
        for field in WIKI_REQUIRED_FIELDS:
            if field not in meta:
                issues.append({"type": "frontmatter", "path": rel, "issue": "missing_field", "field": field})
        if meta.get("confidence") and meta.get("confidence") not in CONFIDENCE_ALLOWED:
            issues.append({"type": "frontmatter", "path": rel, "issue": "invalid_confidence", "value": meta.get("confidence")})
        if meta.get("claim_label") and meta.get("claim_label") not in CLAIM_LABEL_ALLOWED:
            issues.append({"type": "frontmatter", "path": rel, "issue": "invalid_claim_label", "value": meta.get("claim_label")})
        if meta.get("status") and meta.get("status") not in STATUS_ALLOWED:
            issues.append({"type": "frontmatter", "path": rel, "issue": "invalid_status", "value": meta.get("status")})
        if meta.get("page_type") and meta.get("page_type") not in PAGE_TYPE_ALLOWED:
            issues.append({"type": "frontmatter", "path": rel, "issue": "invalid_page_type", "value": meta.get("page_type")})
    return issues




def source_payload_manifest_status(kb_root: Path) -> str:
    path = kb_root / SOURCE_PAYLOAD_MANIFEST_PATH
    if not path.exists():
        return "missing"
    try:
        current = json.loads(read_text(path))
        expected = build_source_payload_manifest(kb_root)
        current_aggregate = current.get("aggregate", {}) if isinstance(current, dict) else {}
        expected_aggregate = expected.get("aggregate", {})
        tracked = ["file_count", "total_size_bytes", "sha256"]
        return "fresh" if all(current_aggregate.get(k) == expected_aggregate.get(k) for k in tracked) else "stale"
    except Exception:
        return "unreadable"


def lint_source_payload_manifest(kb_root: Path) -> List[Dict[str, Any]]:
    status = source_payload_manifest_status(kb_root)
    if status == "fresh":
        return []
    return [{"type": "source_payload_manifest", "issue": status, "severity": "report_only", "path": SOURCE_PAYLOAD_MANIFEST_PATH.as_posix()}]


def has_markdown_heading(text: str, heading: str) -> bool:
    return re.search(rf"(?im)^##+\s+{re.escape(heading)}\s*$", text) is not None


def lint_page_value_contract(kb_root: Path) -> List[Dict[str, Any]]:
    issues: List[Dict[str, Any]] = []
    for page in wiki_pages(kb_root):
        meta, _body, status = parse_frontmatter(read_text(page))
        page_type = meta.get("page_type") if status not in {"missing", "malformed"} else None
        if page_type not in {"summary", "concept", "entity"}:
            continue
        text = read_text(page)
        for heading in PHASE2_VALUE_HEADINGS:
            if not has_markdown_heading(text, heading):
                issues.append({"type": "page_value_contract", "severity": "report_only", "path": relpath(kb_root, page), "issue": "missing_section", "section": heading})
    return issues


def lint_paths(kb_root: Path) -> List[Dict[str, Any]]:
    issues = []
    for d in REQUIRED_DIRS:
        if not (kb_root / d).is_dir():
            issues.append({"type": "path", "issue": "missing_directory", "path": d})
    for f in REQUIRED_FILES:
        if not (kb_root / f).is_file():
            issues.append({"type": "path", "issue": "missing_file", "path": f})
    if (kb_root / "CLAUDE.md").exists():
        issues.append({"type": "path", "issue": "forbidden_root_file", "path": "CLAUDE.md"})
    if (kb_root / "SKILL.md").exists():
        issues.append({"type": "path", "issue": "forbidden_root_file", "path": "SKILL.md"})
    return issues


def lint_wikilinks(kb_root: Path) -> List[Dict[str, Any]]:
    pages = wiki_pages(kb_root)
    stems = {p.stem for p in pages}
    rels = {relpath(kb_root, p) for p in pages}
    issues = []
    inbound = Counter()
    for p in pages:
        text = read_text(p)
        for wm in re.finditer(r"\[\[([^\]|#]+)", text):
            target = wm.group(1).strip()
            if target not in stems and target not in rels:
                issues.append({"type": "wikilink", "path": relpath(kb_root, p), "issue": "dead_wikilink", "target": target})
            inbound[target] += 1
    index_text = read_text(kb_root / "wiki/index.md") if (kb_root / "wiki/index.md").exists() else ""
    for p in pages:
        if p.name == "index.md":
            continue
        rel = relpath(kb_root, p)
        if p.stem not in inbound and rel not in index_text and p.name not in index_text:
            issues.append({"type": "orphan", "path": rel, "issue": "not_linked_from_index_or_wikilinks"})
    return issues


def stale_index_status(kb_root: Path) -> str:
    index = kb_root / "wiki/index.md"
    if not index.exists():
        return "missing"
    newest_page = max((p.stat().st_mtime for p in wiki_pages(kb_root) if p.name != "index.md"), default=0)
    return "stale" if newest_page > index.stat().st_mtime else "fresh"


def cmd_lint(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    issues = []
    issues.extend(lint_paths(kb_root))
    issues.extend(lint_frontmatter(kb_root))
    issues.extend(lint_wikilinks(kb_root))
    issues.extend(lint_source_payload_manifest(kb_root))
    issues.extend(lint_page_value_contract(kb_root))
    stale = stale_index_status(kb_root)
    if stale != "fresh":
        issues.append({"type": "index", "issue": stale})
    report_only_count = sum(1 for issue in issues if issue.get("severity") == "report_only")
    blocking_issues = [issue for issue in issues if issue.get("severity") != "report_only"]
    severity = "fail" if blocking_issues and args.strict else "warn" if issues else "pass"
    return {"command": "lint", "status": severity, "issue_count": len(issues), "report_only_count": report_only_count, "issues": issues, "deterministic_only": True}


def route_contract_files(target: Path) -> List[Path]:
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(p for p in target.rglob("*") if p.is_file() and (p.suffix.lower() in HANDOVER_TEXT_EXTS or not p.suffix))
    raise FileNotFoundError(f"target not found: {target}")


def route_field_present(text: str, field: str) -> bool:
    pattern = rf"(?im)^\s*(?:[-*]\s*)?(?:{re.escape(field)})\s*:"
    return re.search(pattern, text) is not None


def route_field_values(text: str, field: str) -> List[str]:
    pattern = rf"(?im)^\s*(?:[-*]\s*)?{re.escape(field)}\s*:\s*(.+?)\s*$"
    return [m.group(1).strip().strip("\"'") for m in re.finditer(pattern, text)]


def route_field_has_list_items(text: str, field: str) -> bool:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if re.match(rf"(?i)^\s*(?:[-*]\s*)?{re.escape(field)}\s*:\s*(.*)$", line):
            value = line.split(":", 1)[1].strip()
            if value and value not in {"[]", "{}", "null", "None", "~"}:
                return True
            base_indent = len(line) - len(line.lstrip())
            for child in lines[idx + 1:]:
                if not child.strip():
                    continue
                indent = len(child) - len(child.lstrip())
                if indent <= base_indent:
                    return False
                if re.match(r"^\s*-\s+\S+", child):
                    return True
            return False
    return False


def detect_validator_executor_collapse(text: str) -> bool:
    normalized = re.sub(r"[\s_-]+", "_", text.lower())
    explicit_flags = [
        "validator_executor_collapse:_true",
        "same_actor_validates_executes_approves:_true",
        "same_actor_validate_execute_approve:_true",
        "same_actor:_validator_executor_final_approver",
    ]
    if any(flag in normalized for flag in explicit_flags):
        return True
    high_risk = bool(re.search(r"(?im)^\s*(?:risk|risk_level|operation_risk)\s*:\s*(high|critical)\b", text))
    same_actor = bool(re.search(r"(?im)^\s*(?:same_actor|single_actor|operator_override)\s*:\s*(true|yes|none)\b", text))
    role_collapse_words = all(word in normalized for word in ["validator", "executor"]) and any(word in normalized for word in ["final_approver", "self_approve", "self_approval"])
    return high_risk and (same_actor or role_collapse_words)


def lint_repo_execution_router_file(kb_root: Path, path: Path) -> Dict[str, Any]:
    text = read_text(path)
    findings: List[Dict[str, Any]] = []

    for field in ["repository", "branch", "exact_target_paths", "operation_class", "pre_write_checks", "stop_conditions", "commit_strategy"]:
        if not route_field_present(text, field):
            issue = f"missing_{field}"
            severity = "fail" if field in {"exact_target_paths", "operation_class"} else "warning"
            findings.append({"type": "repo_execution_router", "issue": issue, "severity": severity, "message": f"Missing required route contract field: {field}"})

    if not route_field_has_list_items(text, "exact_target_paths"):
        findings.append({
            "type": "repo_execution_router",
            "issue": "missing_exact_target_paths",
            "severity": "fail",
            "message": "Repo-affecting work must list exact repo-relative target paths before writes.",
        })

    operation_values = route_field_values(text, "operation_class")
    if operation_values and operation_values[0] not in OPERATION_CLASS_ALLOWED:
        findings.append({
            "type": "repo_execution_router",
            "issue": "invalid_operation_class",
            "severity": "fail",
            "message": "Operation class is required: create, update, delete, rename, generated_output, or config_change.",
            "value": operation_values[0],
        })

    if not route_field_present(text, "allowed_actions") or not route_field_present(text, "forbidden_actions"):
        findings.append({
            "type": "repo_execution_router",
            "issue": "missing_allowed_or_forbidden_actions",
            "severity": "warning",
            "message": "Allowed and forbidden actions should be explicit to prevent advisory routing collapse.",
        })

    if not route_field_present(text, "post_write_checks") or not route_field_has_list_items(text, "post_write_checks"):
        findings.append({
            "type": "repo_execution_router",
            "issue": "missing_post_write_checks",
            "severity": "warning",
            "message": "Post-write read-back or deterministic check is required for medium/high-risk work.",
        })

    if detect_validator_executor_collapse(text):
        findings.append({
            "type": "repo_execution_router",
            "issue": "validator_executor_collapse",
            "severity": "fail",
            "message": "High-risk work cannot rely on the same actor to validate, execute, and final-approve without explicit operator override.",
        })

    try:
        file_path = relpath(kb_root, path)
    except ValueError:
        file_path = str(path)
    return {"path": file_path, "finding_count": len(findings), "findings": findings}


def cmd_lint_repo_execution_router(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    target = Path(args.target).expanduser().resolve()
    files = route_contract_files(target)
    results = [lint_repo_execution_router_file(kb_root, p) for p in files]
    findings = [finding for result in results for finding in result["findings"]]
    fail_count = sum(1 for finding in findings if finding.get("severity") == "fail")
    warning_count = sum(1 for finding in findings if finding.get("severity") == "warning")
    status = "fail" if fail_count or (warning_count and args.strict) else "warn" if warning_count else "pass"
    return {
        "command": "lint-repo-execution-router",
        "status": status,
        "target": str(target),
        "file_count": len(files),
        "finding_count": len(findings),
        "fail_count": fail_count,
        "warning_count": warning_count,
        "results": results,
        "deterministic_only": True,
    }


def line_number_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def historical_path_entries(text: str) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    lines = text.splitlines()
    current: Optional[Dict[str, Any]] = None
    for idx, line in enumerate(lines, start=1):
        old_path = re.match(r"^\s*-\s+old_path\s*:\s*(.+?)\s*$", line)
        if old_path:
            if current:
                entries.append(current)
            current = {"old_path": old_path.group(1).strip().strip("\"'"), "line": idx}
            continue
        if current:
            field = re.match(r"^\s+(status|current_path)\s*:\s*(.+?)\s*$", line)
            if field:
                current[field.group(1)] = field.group(2).strip().strip("\"'")
            elif re.match(r"^\S", line) or re.match(r"^\s*-\s+\S", line):
                entries.append(current)
                current = None
    if current:
        entries.append(current)
    return entries


def add_historical_finding(findings: List[Dict[str, Any]], issue: str, severity: str, message: str, line: Optional[int] = None, value: Optional[str] = None) -> None:
    finding: Dict[str, Any] = {"type": "historical_path_authority", "issue": issue, "severity": severity, "message": message}
    if line is not None:
        finding["line"] = line
    if value is not None:
        finding["value"] = value
    findings.append(finding)


def lint_historical_path_authority_file(kb_root: Path, path: Path) -> Dict[str, Any]:
    text = read_text(path)
    low = text.lower()
    findings: List[Dict[str, Any]] = []
    canonical_values = route_field_values(text, "canonical_current_path")
    canonical_current_path = canonical_values[0] if canonical_values else ""
    entries = historical_path_entries(text)

    for entry in entries:
        line = int(entry.get("line", 1))
        status = str(entry.get("status", "")).lower()
        current_path = str(entry.get("current_path", ""))
        old_path = str(entry.get("old_path", ""))
        if status in {"active", "current", "runtime_authority", "config_authority"}:
            add_historical_finding(
                findings,
                "historical_path_used_as_current_target",
                "fail",
                "Historical path appears to be used as current implementation target.",
                line,
                old_path,
            )
        if status not in {"superseded", "deprecated", "historical", "legacy", "source_trace"}:
            add_historical_finding(findings, "unmarked_legacy_path", "warning", "Legacy path appears without historical-source marker.", line, old_path)
        if not current_path:
            add_historical_finding(findings, "missing_current_path", "fail", "Historical path entry must point to a current path.", line, old_path)
        if current_path and canonical_current_path and current_path != canonical_current_path:
            add_historical_finding(findings, "current_path_mismatch", "fail", "Historical path current_path must match canonical_current_path.", line, current_path)

    if entries and not canonical_current_path:
        add_historical_finding(findings, "missing_canonical_current_path", "fail", "Historical path mappings require canonical_current_path.")

    legacy_patterns = [
        r"\bOpenClaw\b",
        r"\bold OpenClaw\b",
        r"\blegacy runtime\b",
        r"\b[A-Za-z]:\\",
        r"\blocal Windows path\b",
    ]
    historical_context = "historical_source_evidence" in text or "historical_paths:" in text or "deprecated_appendix" in text or "migration_risk_note" in text
    for pattern in legacy_patterns:
        for match in re.finditer(pattern, text):
            if not historical_context:
                add_historical_finding(
                    findings,
                    "unmarked_legacy_path",
                    "warning",
                    "Legacy path appears without historical-source marker.",
                    line_number_for_offset(text, match.start()),
                    match.group(0),
                )

    current_authority_near_legacy = bool(re.search(r"(?is)(write to|update|replace|runtime authority|config authority).{0,120}(OpenClaw|old OpenClaw|legacy runtime|[A-Za-z]:\\)", text))
    if current_authority_near_legacy:
        add_historical_finding(findings, "historical_path_used_as_current_target", "fail", "Historical path appears to be used as current implementation target.")

    if re.search(r"\b(provider|model|cost|performance)\b", low) and re.search(r"\b(current|runtime|authority|policy)\b", low) and "current verification" not in low:
        add_historical_finding(findings, "stale_provider_or_model_claim", "warning", "Provider/model/cost/performance claim requires current verification.")

    old_role_current = bool(re.search(r"(?is)(old agent role|meta detective|meta ops|meta strategy|special ops).{0,120}(current agent|current skill|runtime role|promote|promoted)", text))
    if old_role_current and "operator decision" not in low:
        add_historical_finding(findings, "old_role_promoted_without_decision", "fail", "Old role name appears promoted into current agent/skill without recorded operator decision.")

    try:
        file_path = relpath(kb_root, path)
    except ValueError:
        file_path = str(path)
    return {"path": file_path, "finding_count": len(findings), "findings": findings}


def cmd_lint_historical_path_authority(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    target = Path(args.target).expanduser().resolve()
    files = route_contract_files(target)
    results = [lint_historical_path_authority_file(kb_root, p) for p in files]
    findings = [finding for result in results for finding in result["findings"]]
    fail_count = sum(1 for finding in findings if finding.get("severity") == "fail")
    warning_count = sum(1 for finding in findings if finding.get("severity") == "warning")
    status = "fail" if fail_count or (warning_count and args.strict) else "warn" if warning_count else "pass"
    return {
        "command": "lint-historical-path-authority",
        "status": status,
        "target": str(target),
        "file_count": len(files),
        "finding_count": len(findings),
        "fail_count": fail_count,
        "warning_count": warning_count,
        "results": results,
        "deterministic_only": True,
    }


def audit_items(kb_root: Path) -> List[Dict[str, Any]]:
    root = kb_root / "audit"
    if not root.exists():
        return []
    items = []
    for p in sorted(root.rglob("*.md")):
        if "resolved" in p.relative_to(root).parts:
            continue
        meta, _body, status = parse_frontmatter(read_text(p))
        items.append({"path": relpath(kb_root, p), "frontmatter_status": status, "status": meta.get("status", "unknown"), "title": meta.get("title", p.stem)})
    return items


def cmd_audit(args: argparse.Namespace) -> Dict[str, Any]:
    items = audit_items(resolve_kb_root(args.kb_root))
    groups: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for item in items:
        groups[str(item.get("status", "unknown"))].append(item)
    return {"command": "audit", "item_count": len(items), "groups": dict(groups), "mutations": False}


def cmd_status(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    manifest = read_manifest(kb_root)
    return {
        "command": "status",
        "kb_root": str(kb_root),
        "exists": kb_root.exists(),
        "source_count": len(manifest.get("sources", [])),
        "wiki_page_count": len(wiki_pages(kb_root)),
        "audit_item_count": len(audit_items(kb_root)),
        "wiki_index_status": stale_index_status(kb_root),
        "retrieval_index_status": retrieval_index_status(kb_root),
        "source_payload_manifest_status": source_payload_manifest_status(kb_root),
        "phase0_artifacts_present": (kb_root / PHASE0_DIR / "phase0-navigation-report.md").exists(),
        "search_index_present": (kb_root / "derived/search/index-meta.json").exists(),
    }


def retrieval_index_status(kb_root: Path) -> str:
    meta_path = kb_root / "derived/search/index-meta.json"
    if not meta_path.exists():
        return "missing"
    try:
        meta = json.loads(read_text(meta_path))
    except (OSError, json.JSONDecodeError, ValueError):
        return "unknown"
    if not isinstance(meta, dict):
        return "unknown"
    files = meta.get("files")
    if not isinstance(files, dict):
        return "unknown"
    current = {relpath(kb_root, page): sha256_file(page) for page in wiki_pages(kb_root)}
    if set(files) != set(current):
        return "stale"
    for rel, current_hash in current.items():
        entry = files.get(rel)
        if not isinstance(entry, dict) or entry.get("hash") != current_hash:
            return "stale"
    return "fresh"


def manifest_source_ids(sources: List[Any]) -> List[str]:
    ids = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        ids.append(str(source.get("source_id") or source.get("id") or source.get("pointer") or source.get("source_path") or "unknown"))
    return ids


def extract_source_refs(meta: Dict[str, Any]) -> List[str]:
    """Handle source_refs as list-of-str, list-of-object, or scalar. Never raises on garbage input."""
    if not isinstance(meta, dict):
        return []
    raw = meta.get("source_refs")
    if raw is None:
        return []
    refs: List[str] = []

    def _from_obj(obj: Dict[str, Any]) -> None:
        val = obj.get("source_id") or obj.get("source_path") or obj.get("source_pointer") or obj.get("pointer")
        if val:
            refs.append(str(val).strip())

    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, str):
                s = item.strip()
                if s:
                    refs.append(s)
            elif isinstance(item, dict):
                _from_obj(item)
    elif isinstance(raw, str):
        s = raw.strip()
        if s:
            refs.append(s)
    elif isinstance(raw, dict):
        _from_obj(raw)
    seen: set = set()
    deduped: List[str] = []
    for r in refs:
        if r not in seen:
            seen.add(r)
            deduped.append(r)
    return deduped


VALUE_PAGE_TYPES = {"summary", "concept", "entity"}
SECTION_WORD_FLOOR = 20


def _quality_section(body: str, heading: str, level: str = "##") -> str:
    """Extract the text of one heading section up to the next heading at the same level."""
    pattern = re.compile(rf"^{re.escape(level)}\s+{re.escape(heading)}\s*$", re.MULTILINE | re.IGNORECASE)
    match = pattern.search(body)
    if not match:
        return ""
    tail = body[match.end():]
    next_heading = re.search(rf"^{re.escape(level)}\s+", tail, re.MULTILINE)
    return tail[:next_heading.start()] if next_heading else tail


def _quality_words(text: str) -> int:
    text = re.sub(r"```.*?```", " ", text or "", flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    return len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE))


def _pointer_specificity(body: str) -> Dict[str, int]:
    """Classify claim source pointers as file/section/line-or-span specific.

    Directory- or file-relative pointers with no section/line suffix are
    file-level; a section/heading suffix is section-level; a line or span
    reference is the most specific.
    """
    pointers = re.findall(r"(?:source_pointer|pointer)\s*:\s*['\"]?([^\n'\"]+)", body or "", flags=re.IGNORECASE)
    result = {"file_level": 0, "section_level": 0, "line_or_span_level": 0}
    for pointer in pointers:
        if re.search(r"(?:L\d+|lines?\s*\d+|:\d+(?:-\d+)?)", pointer, flags=re.IGNORECASE):
            result["line_or_span_level"] += 1
        elif re.search(r"(?:#|§|heading|section)", pointer, flags=re.IGNORECASE):
            result["section_level"] += 1
        else:
            result["file_level"] += 1
    return result


def _quality_page_metrics(kb_root: Path, page: Path) -> Dict[str, Any]:
    """Deterministic, reason-coded page measurements: per-section narrative
    word counts, key-claim count, claim-to-pointer coverage, pointer
    specificity, ranked-source count, route count, and placeholder
    detection. No page-value score is computed; reasons stay separate and
    inspectable."""
    raw = read_text(page)
    meta, body, frontmatter_status = parse_frontmatter(raw)
    meta = meta if isinstance(meta, dict) else {}
    body = body or ""
    page_type = str(meta.get("page_type") or "unknown")

    sections = {heading: _quality_section(body, heading) for heading in PHASE2_VALUE_HEADINGS}
    macro_block = sections.get("Macro / Meso / Micro", "")
    section_words = {heading: _quality_words(text) for heading, text in sections.items()}
    section_words.update({
        "Macro": _quality_words(_quality_section(macro_block, "Macro", level="###")),
        "Meso": _quality_words(_quality_section(macro_block, "Meso", level="###")),
        "Micro": _quality_words(_quality_section(macro_block, "Micro", level="###")),
    })

    refs = extract_source_refs(meta)
    key_claims = len(re.findall(r"(?:^|\n)\s*-\s+(?:claim_id\s*:|claim\s*:)", sections.get("Key Claims", ""), flags=re.IGNORECASE))
    ranked_sources = len(re.findall(r"(?:^|\n)\s*-\s+(?:rank\s*:|source\s*:|source_id\s*:|source_path\s*:)", sections.get("Adaptive Ranked Source Set", ""), flags=re.IGNORECASE))
    routes = len(re.findall(r"(?:^|\n)\s*-\s+(?:question\s*:|leads_to\s*:)", sections.get("Routes Here", ""), flags=re.IGNORECASE))
    uncertainty_items = len(re.findall(r"(?:^|\n)\s*-\s+id\s*:", sections.get("Uncertainty / Raw Source Reopen Triggers", ""), flags=re.IGNORECASE))
    pointer_specificity = _pointer_specificity(sections.get("Key Claims", ""))
    pointer_count = sum(pointer_specificity.values())
    placeholders = sorted(set(re.findall(r"<[^>]{3,80}>|\b(?:TODO|TBD|LLM must fill)\b", body, flags=re.IGNORECASE)))
    missing_headings = [h for h in PHASE2_VALUE_HEADINGS if not has_markdown_heading(body, h)]

    reasons: List[str] = []
    if page_type in VALUE_PAGE_TYPES:
        if not refs:
            reasons.append("missing_source_refs")
        if missing_headings:
            reasons.append("missing_phase2_value_sections")
        if placeholders:
            reasons.append("placeholder_text")
        all_layers_thin = all(section_words.get(name, 0) < SECTION_WORD_FLOOR for name in ("Macro", "Meso", "Micro"))
        if key_claims == 0:
            reasons.append("no_key_claims")
        else:
            if pointer_count < key_claims:
                reasons.append("claim_pointer_coverage_below_100_percent")
            if page_type == "summary" and key_claims < 2:
                reasons.append("single_claim_summary")
            elif page_type == "concept" and key_claims < 2 and all_layers_thin:
                reasons.append("single_claim_concept_thin")
        specific_pointer_count = pointer_specificity["section_level"] + pointer_specificity["line_or_span_level"]
        if page_type == "concept" and section_words.get("Micro", 0) < SECTION_WORD_FLOOR and specific_pointer_count == 0:
            reasons.append("concept_micro_not_evidenced")
        # Narrow named entities may validly be concise with one claim and one
        # source (kb-contract.md concise_policy) - only flag entities for a
        # missing claim outright, never for thin/single-claim synthesis depth.
        if all_layers_thin and page_type != "entity":
            reasons.append("thin_macro_meso_micro")
        if page_type == "summary" and ranked_sources < 2:
            reasons.append("summary_source_breadth_below_profile")
        if routes == 0:
            reasons.append("no_query_routes")

    return {
        "path": relpath(kb_root, page),
        "page_type": page_type,
        "frontmatter_status": frontmatter_status,
        "source_refs": refs,
        "narrative_word_count": _quality_words(body),
        "section_word_counts": section_words,
        "ranked_source_count": ranked_sources,
        "key_claim_count": key_claims,
        "source_pointer_count": pointer_count,
        "pointer_specificity": pointer_specificity,
        "route_count": routes,
        "uncertainty_item_count": uncertainty_items,
        "placeholder_text": placeholders,
        "missing_phase2_value_sections": missing_headings,
        "repair_reasons": sorted(set(reasons)),
    }


def quality_report(kb_root: Path) -> Dict[str, Any]:
    manifest = read_manifest(kb_root)
    sources = manifest.get("sources", [])
    sources = sources if isinstance(sources, list) else []
    manifest_ids = manifest_source_ids(sources)
    manifest_id_set = set(manifest_ids)

    metrics = [_quality_page_metrics(kb_root, page_path) for page_path in wiki_pages(kb_root)]

    page_to_source_map: Dict[str, List[str]] = {item["path"]: item["source_refs"] for item in metrics}
    source_to_page_map: Dict[str, List[str]] = {sid: [] for sid in manifest_ids}
    unmanifested_source_refs: Dict[str, List[str]] = {}
    for page, refs in page_to_source_map.items():
        for ref in refs:
            if ref in manifest_id_set:
                source_to_page_map.setdefault(ref, []).append(page)
            else:
                unmanifested_source_refs.setdefault(ref, []).append(page)

    manifest_sources_without_pages = sorted(sid for sid, pgs in source_to_page_map.items() if not pgs)
    pages_without_source_refs = sorted(
        item["path"] for item in metrics
        if item["page_type"] in VALUE_PAGE_TYPES and not item["source_refs"]
    )
    pages_missing_phase2_value_sections = {
        item["path"]: item["missing_phase2_value_sections"]
        for item in metrics if item["missing_phase2_value_sections"]
    }

    candidates = sorted(
        ({"path": item["path"], "reasons": item["repair_reasons"]} for item in metrics if item["repair_reasons"]),
        key=lambda c: c["path"],
    )
    shell_reasons = {"placeholder_text", "no_key_claims", "thin_macro_meso_micro", "single_claim_summary", "single_claim_concept_thin", "concept_micro_not_evidenced"}
    shell_page_candidates = [c for c in candidates if shell_reasons.intersection(c["reasons"])]

    return {
        "source_to_page_map": {key: sorted(value) for key, value in sorted(source_to_page_map.items())},
        "page_to_source_map": page_to_source_map,
        "unmanifested_source_refs": unmanifested_source_refs,
        "manifest_sources_without_pages": manifest_sources_without_pages,
        "pages_without_source_refs": pages_without_source_refs,
        "pages_missing_phase2_value_sections": pages_missing_phase2_value_sections,
        "phase2_repair_candidates": candidates,
        "shell_page_candidates": shell_page_candidates,
        "page_metrics": metrics,
        "deterministic_only": True,
    }


def cmd_quality(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    report = quality_report(kb_root)
    result = {"command": "quality"}
    result.update(report)
    has_candidates = bool(report["phase2_repair_candidates"] or report["shell_page_candidates"])
    if getattr(args, "strict", False):
        result["status"] = "fail" if has_candidates else "ok"
    else:
        result["status"] = "ok"
    result["issue_count"] = len(report["phase2_repair_candidates"])
    return result


QUERY_EVAL_SCHEMA = "apex.query_eval_pack.v1"
QUERY_EVAL_LIST_FIELDS = ("expected_routes", "expected_minimal_pages", "raw_source_needed")


def query_eval_pack_path(kb_root: Path) -> Path:
    return kb_root / "outputs/queries/evals/query-eval-pack.json"


def validate_query_eval_pack(pack: Any) -> List[Dict[str, str]]:
    issues: List[Dict[str, str]] = []
    if not isinstance(pack, dict):
        return [{"field": "<root>", "message": "pack must be a JSON object"}]
    if pack.get("schema") != QUERY_EVAL_SCHEMA:
        issues.append({"field": "schema", "message": f"expected {QUERY_EVAL_SCHEMA!r}, got {pack.get('schema')!r}"})
    kb_slug = pack.get("kb_slug")
    if not isinstance(kb_slug, str) or not kb_slug.strip():
        issues.append({"field": "kb_slug", "message": "kb_slug must be a non-empty string"})
    queries = pack.get("queries")
    if not isinstance(queries, list):
        issues.append({"field": "queries", "message": "queries must be a list"})
        return issues
    for idx, entry in enumerate(queries):
        prefix = f"queries[{idx}]"
        if not isinstance(entry, dict):
            issues.append({"field": prefix, "message": "query entry must be an object"})
            continue
        query_text = entry.get("query")
        if not isinstance(query_text, str) or not query_text.strip():
            issues.append({"field": f"{prefix}.query", "message": "query must be a non-empty string"})
        for field in QUERY_EVAL_LIST_FIELDS:
            val = entry.get(field, [])
            if not isinstance(val, list):
                issues.append({"field": f"{prefix}.{field}", "message": f"{field} must be a list if present"})
            elif not all(isinstance(x, str) for x in val):
                issues.append({"field": f"{prefix}.{field}", "message": f"{field} entries must be strings"})
    return issues


def cmd_query_eval(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    pack_path = query_eval_pack_path(kb_root)
    result: Dict[str, Any] = {"command": "query-eval", "query-eval-pack.json": relpath(kb_root, pack_path)}
    empty_agg = {field: [] for field in QUERY_EVAL_LIST_FIELDS}

    if pack_path.exists():
        parse_error = None
        pack: Any = None
        try:
            pack = json.loads(read_text(pack_path))
        except (OSError, json.JSONDecodeError) as exc:
            parse_error = str(exc)
        if parse_error is not None or not isinstance(pack, dict):
            issues = [{"field": "<root>", "message": f"could not parse JSON: {parse_error}" if parse_error else "root is not an object"}]
            result.update({"status": "invalid", "issue_count": len(issues), "issues": issues, "query_count": 0})
            result.update(empty_agg)
            return result
        issues = validate_query_eval_pack(pack)
        queries = pack.get("queries") if isinstance(pack.get("queries"), list) else []
        agg = {field: [] for field in QUERY_EVAL_LIST_FIELDS}
        for entry in queries:
            if not isinstance(entry, dict):
                continue
            for field in QUERY_EVAL_LIST_FIELDS:
                val = entry.get(field)
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, str) and item not in agg[field]:
                            agg[field].append(item)
        result.update({"status": "ok" if not issues else "invalid", "issue_count": len(issues), "issues": issues, "query_count": len(queries)})
        for field in QUERY_EVAL_LIST_FIELDS:
            result[field] = sorted(agg[field])
        return result

    init_requested = bool(getattr(args, "init", False))
    if not init_requested:
        result.update({"status": "missing", "issue_count": 0, "issues": [], "query_count": 0})
        result.update(empty_agg)
        return result

    dry_run = effective_dry_run(args)
    if dry_run:
        result.update({"status": "planned", "planned_write_path": relpath(kb_root, pack_path), "issue_count": 0, "issues": [], "query_count": 0})
        result.update(empty_agg)
        return result

    initial_pack = {"schema": QUERY_EVAL_SCHEMA, "kb_slug": kb_root.name, "queries": []}
    write_result = write_text(pack_path, json.dumps(initial_pack, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run)
    result.update({"status": "initialized", "write_result": write_result, "issue_count": 0, "issues": [], "query_count": 0})
    result.update(empty_agg)
    return result


GRAPH_SOURCE_DIRS = ("raw", "sources", "ingest-analysis", "wiki")
GRAPH_ROOT_FILES = ("kb-schema.md", "README.md")
GRAPH_EXCLUDE_DIRS = {"derived", "outputs", "manifests", "audit", "log"}
GRAPH_MAX_FILE_BYTES = 2_000_000
REPO_PATH_PREFIXES = (r"\.claude/", r"apex-meta/", r"wiki/", r"raw/", r"manifests/", r"sources/", r"ingest-analysis/")
REPO_PATH_RE = re.compile(r"(?<![\w/.-])(?:" + "|".join(REPO_PATH_PREFIXES) + r")[\w./-]*[\w]")
YAML_PATH_KEY_RE = re.compile(r"^\s*(?:-\s*)?([A-Za-z0-9_-]*(?:path|file|root|source|target|output)[A-Za-z0-9_-]*)\s*:\s*(\S.*)$", re.IGNORECASE)
GRAPH_ARROW_RE = re.compile(r"([A-Za-z0-9_.\-/]+)\s*(?:->|-->|→)\s*([A-Za-z0-9_.\-/]+)")
GRAPH_SEQ_KEY_RE = re.compile(r"^\s*(?:-\s*)?(hands_off_to|depends_on)\s*:\s*(\S.*)$", re.IGNORECASE)
GRAPH_STAGE_RE = re.compile(r"^\s*#{0,6}\s*(?:Stage|Step|Phase)\s+(\d+)\s*[:.\-]\s*(.+?)\s*$", re.IGNORECASE)
GRAPH_FENCE_RE = re.compile(r"^\s*(?:```|~~~)")
GRAPH_EDGE_TYPES = ("markdown_link", "wikilink", "repo_path_reference", "yaml_path_reference", "process_sequence")


def iter_graph_source_files(kb_root: Path) -> List[Path]:
    """KB-local text files only, bounded to the known content roots, excluding
    derived/generated dirs and oversized files. Never crawls outside kb_root."""
    seen: set = set()
    results: List[Path] = []

    def consider(path: Path) -> None:
        if not path.is_file() or path.suffix.lower() not in TEXT_EXTS:
            return
        try:
            rel_parts = set(path.relative_to(kb_root).parts)
        except ValueError:
            rel_parts = set()
        if rel_parts & GRAPH_EXCLUDE_DIRS:
            return
        try:
            if path.stat().st_size > GRAPH_MAX_FILE_BYTES:
                return
        except OSError:
            return
        key = os.path.normcase(str(path.resolve()))
        if key in seen:
            return
        seen.add(key)
        results.append(path)

    for dirname in GRAPH_SOURCE_DIRS:
        base = kb_root / dirname
        if base.is_dir():
            for p in sorted(base.rglob("*")):
                consider(p)
    for name in GRAPH_ROOT_FILES:
        consider(kb_root / name)
    return results


def _graph_edge(source_path: str, target: str, edge_type: str, line: int, raw: str) -> Dict[str, Any]:
    return {"source_path": source_path, "target": target, "edge_type": edge_type, "line": line, "raw": raw.strip()[:200], "confidence": "deterministic"}


def extract_markdown_graph_edges(path: Path, kb_root: Path, structure: Dict[str, Any]) -> List[Dict[str, Any]]:
    src = relpath(kb_root, path)
    edges = []
    for link in structure.get("markdown_links", []):
        target = link.get("normalized_target") or link.get("target")
        if target:
            edges.append(_graph_edge(src, target, "markdown_link", link["line"], f"[{link['text']}]({link['target']})"))
    for wl in structure.get("wikilinks", []):
        edges.append(_graph_edge(src, wl["target"], "wikilink", wl["line"], wl["raw"]))
    return edges


def extract_repo_path_references(path: Path, kb_root: Path, lines: List[str]) -> List[Dict[str, Any]]:
    src = relpath(kb_root, path)
    edges = []
    for idx, line in enumerate(lines, start=1):
        for m in REPO_PATH_RE.finditer(line):
            edges.append(_graph_edge(src, m.group(0), "repo_path_reference", idx, line))
    return edges


def extract_yaml_path_references(path: Path, kb_root: Path, lines: List[str]) -> List[Dict[str, Any]]:
    src = relpath(kb_root, path)
    edges = []
    for idx, line in enumerate(lines, start=1):
        m = YAML_PATH_KEY_RE.match(line)
        if not m:
            continue
        value = m.group(2).split("#", 1)[0].strip()
        if not value:
            continue
        token = value.split()[0].strip("'\",;")
        if not token:
            continue
        if "/" in token or re.search(r"\.[A-Za-z0-9]{1,5}$", token):
            edges.append(_graph_edge(src, token, "yaml_path_reference", idx, line))
    return edges


def extract_process_sequence_edges(path: Path, kb_root: Path, lines: List[str]) -> List[Dict[str, Any]]:
    src = relpath(kb_root, path)
    edges: List[Dict[str, Any]] = []
    in_fence = False
    stages: List[Tuple[int, str, int]] = []
    for idx, line in enumerate(lines, start=1):
        if GRAPH_FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            # Skip arrow scanning inside code fences: Python `-> ReturnType`
            # annotations would otherwise flood this edge type with noise.
            for m in GRAPH_ARROW_RE.finditer(line):
                edges.append(_graph_edge(src, f"{m.group(1)}->{m.group(2)}", "process_sequence", idx, line))
        seq_m = GRAPH_SEQ_KEY_RE.match(line)
        if seq_m:
            value = seq_m.group(2).split("#", 1)[0].strip().strip("'\",")
            if value:
                edges.append(_graph_edge(src, value, "process_sequence", idx, line))
        stage_m = GRAPH_STAGE_RE.match(line)
        if stage_m:
            stages.append((int(stage_m.group(1)), stage_m.group(2).strip(), idx))
    stages.sort(key=lambda t: t[0])
    for (n1, label1, line1), (n2, label2, _line2) in zip(stages, stages[1:]):
        if n2 == n1 + 1:
            edges.append(_graph_edge(src, f"{label1}->{label2}", "process_sequence", line1, f"Stage {n1} -> Stage {n2}"))
    return edges


def _graph_edge_key(edge: Dict[str, Any]) -> Tuple[str, str, str, int]:
    return (edge["source_path"], edge["edge_type"], edge["target"], edge["line"])


def dedup_graph_edges(edges: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen: set = set()
    result = []
    for edge in sorted(edges, key=_graph_edge_key):
        key = _graph_edge_key(edge)
        if key in seen:
            continue
        seen.add(key)
        result.append(edge)
    return result


def process_graph_extract(kb_root: Path) -> Dict[str, Any]:
    all_edges: List[Dict[str, Any]] = []
    for path in iter_graph_source_files(kb_root):
        try:
            text = read_text(path)
        except OSError:
            continue
        lines = text.splitlines()
        structure = parse_markdown_structure(path, kb_root)
        all_edges.extend(extract_markdown_graph_edges(path, kb_root, structure))
        all_edges.extend(extract_repo_path_references(path, kb_root, lines))
        all_edges.extend(extract_yaml_path_references(path, kb_root, lines))
        all_edges.extend(extract_process_sequence_edges(path, kb_root, lines))
    edges = dedup_graph_edges(all_edges)
    edges_by_type = {edge_type: 0 for edge_type in GRAPH_EDGE_TYPES}
    for edge in edges:
        edges_by_type[edge["edge_type"]] = edges_by_type.get(edge["edge_type"], 0) + 1
    return {"edges": edges, "edge_count": len(edges), "edges_by_type": edges_by_type, "deterministic_only": True}


def cmd_graph(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    extraction = process_graph_extract(kb_root)
    graph_path = kb_root / PHASE0_DIR / "process-flow-graph.json"
    summary_path = kb_root / PHASE0_DIR / "process-flow-graph-summary.md"
    graph_json = json.dumps(
        {
            "edges": extraction["edges"],
            "edge_count": extraction["edge_count"],
            "edges_by_type": extraction["edges_by_type"],
            "deterministic_only": extraction["deterministic_only"],
        },
        indent=2, ensure_ascii=False, sort_keys=True,
    ) + "\n"
    summary_lines = ["# Process Flow Graph Summary", "", f"Total edges: {extraction['edge_count']}", ""]
    summary_lines.extend(f"- {edge_type}: {count}" for edge_type, count in sorted(extraction["edges_by_type"].items()))
    writes = [
        write_text(graph_path, graph_json, kb_root, args.allow_write, dry_run),
        write_text(summary_path, "\n".join(summary_lines) + "\n", kb_root, args.allow_write, dry_run),
    ]
    return {
        "command": "graph",
        "dry_run": dry_run,
        "edge_count": extraction["edge_count"],
        "edges_by_type": extraction["edges_by_type"],
        "deterministic_only": extraction["deterministic_only"],
        "artifacts": [relpath(kb_root, graph_path), relpath(kb_root, summary_path)],
        "writes": writes,
    }


def probe_sqlite_fts5() -> Dict[str, Any]:
    import sqlite3

    result = {"sqlite_version": sqlite3.sqlite_version, "fts5_available": False, "error": None}
    try:
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE VIRTUAL TABLE t USING fts5(x)")
        result["fts5_available"] = True
        conn.close()
    except Exception as exc:
        result["error"] = str(exc)
    return result


def cmd_health(args: argparse.Namespace) -> Dict[str, Any]:
    return {
        "command": "health",
        "python_version": sys.version.split()[0],
        "tools": {"git": shutil.which("git") is not None, "rg": shutil.which("rg") is not None},
        "optional_modules": {"markdown_it": importlib.util.find_spec("markdown_it") is not None, "frontmatter": importlib.util.find_spec("frontmatter") is not None, "yaml": importlib.util.find_spec("yaml") is not None},
        "sqlite": probe_sqlite_fts5(),
        "network_required": False,
        "shell_out_used": False,
    }


def build_parser() -> argparse.ArgumentParser:
    kb_root = resolve_kb_root(args.kb_root)
    return {
        "command": "health",
        "kb_root": str(kb_root),
        "kb_root_exists": kb_root.exists(),
        "python_version": sys.version.split()[0],
        "tools": detect_tools(),
        "optional_modules": detect_optional_modules(),
        "sqlite": probe_fts5(),
    }


POSTFLIGHT_SCHEMA = "apex.kb.postflight.v1"


def _postflight_args(args: argparse.Namespace, **overrides: Any) -> argparse.Namespace:
    values = vars(args).copy()
    values.update(overrides)
    return argparse.Namespace(**values)


def _postflight_step(
    name: str,
    blocking: bool,
    result: Dict[str, Any],
    *,
    skipped: bool = False,
    reason: Optional[str] = None,
) -> Dict[str, Any]:
    step: Dict[str, Any] = {
        "name": name,
        "blocking": blocking,
        "skipped": skipped,
        "result": result,
    }
    if reason is not None:
        step["reason"] = reason
    return step


def _postflight_failed(result: Dict[str, Any]) -> bool:
    return result.get("status") in {"blocked", "fail", "error", "internal_error"}


def _postflight_call(name: str, func: Any, call_args: argparse.Namespace) -> Tuple[Dict[str, Any], bool]:
    try:
        result = func(call_args)
        if not isinstance(result, dict):
            return {"command": name, "status": "internal_error", "error": "delegate returned non-object result"}, True
        return result, False
    except Exception as exc:
        return {"command": name, "status": "internal_error", "error": str(exc)}, True


def _postflight_retrieval_module() -> Any:
    script_dir = Path(__file__).resolve().parent
    if str(script_dir) not in sys.path:
        sys.path.insert(0, str(script_dir))
    import apex_kb_retrieval  # type: ignore

    return apex_kb_retrieval


def cmd_postflight(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    shared = _postflight_args(args, kb_root=str(kb_root))
    strict_shared = _postflight_args(args, kb_root=str(kb_root), strict=True)
    steps: List[Dict[str, Any]] = []
    blocking_failed = False
    internal_error = False

    index_result, index_internal = _postflight_call("index", cmd_index, shared)
    steps.append(_postflight_step("wiki_index", True, index_result))
    index_failed = _postflight_failed(index_result)
    blocking_failed = blocking_failed or index_failed
    internal_error = internal_error or index_internal

    retrieval_module: Any = None
    try:
        retrieval_module = _postflight_retrieval_module()
        retrieval_result, retrieval_internal = _postflight_call("build-index", retrieval_module.cmd_build_index, shared)
    except Exception as exc:
        retrieval_result = {"command": "build-index", "status": "internal_error", "error": str(exc)}
        retrieval_internal = True
    steps.append(_postflight_step("retrieval_build", True, retrieval_result))
    retrieval_failed = _postflight_failed(retrieval_result)
    blocking_failed = blocking_failed or retrieval_failed
    internal_error = internal_error or retrieval_internal

    lint_result, lint_internal = _postflight_call("lint", cmd_lint, strict_shared)
    steps.append(_postflight_step("lint_strict", True, lint_result))
    blocking_failed = blocking_failed or _postflight_failed(lint_result)
    internal_error = internal_error or lint_internal

    quality_result, quality_internal = _postflight_call("quality", cmd_quality, strict_shared)
    steps.append(_postflight_step("quality_strict", True, quality_result))
    blocking_failed = blocking_failed or _postflight_failed(quality_result)
    internal_error = internal_error or quality_internal

    audit_result, audit_internal = _postflight_call("audit", cmd_audit, shared)
    steps.append(_postflight_step("audit", False, audit_result))
    internal_error = internal_error or audit_internal

    status_result, status_internal = _postflight_call("status", cmd_status, shared)
    steps.append(_postflight_step("status", True, status_result))
    blocking_failed = blocking_failed or _postflight_failed(status_result)
    internal_error = internal_error or status_internal

    retrieval_fresh = False
    if index_failed or retrieval_failed or retrieval_module is None:
        stale_result = {"command": "stale", "status": "skipped"}
        steps.append(
            _postflight_step(
                "retrieval_stale",
                True,
                stale_result,
                skipped=True,
                reason="dependent wiki index or retrieval build failed",
            )
        )
        blocking_failed = True
    else:
        stale_result, stale_internal = _postflight_call("stale", retrieval_module.cmd_stale, shared)
        steps.append(_postflight_step("retrieval_stale", True, stale_result))
        retrieval_fresh = stale_result.get("status") == "fresh"
        blocking_failed = blocking_failed or not retrieval_fresh
        internal_error = internal_error or stale_internal

    if dry_run:
        status = "planned"
        evidence_complete = False
    elif internal_error:
        status = "internal_error"
        evidence_complete = False
    else:
        status = "fail" if blocking_failed else "pass"
        evidence_complete = not blocking_failed and retrieval_fresh

    return {
        "schema": POSTFLIGHT_SCHEMA,
        "command": "postflight",
        "kb_root": str(kb_root),
        "dry_run": dry_run,
        "status": status,
        "evidence_complete": evidence_complete,
        "steps": steps,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Apex KB deterministic lifecycle helper")
    parser.add_argument("--kb-root", help="Path to one KB root, e.g. apex-meta/kb/<kb-slug>/")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Preview writes even when --allow-write is present")
    parser.add_argument("--allow-write", action="store_true", help="Permit deterministic writes inside kb_root")
    parser.add_argument("--strict", action="store_true", help="Treat lint warnings as failure")
    parser.add_argument("--output-json", help="Write command result as JSON to file")
    sub = parser.add_subparsers(dest="command", required=True)

    sc = sub.add_parser("scaffold")
    sc.add_argument("--title")
    sc.add_argument("--topic-title")
    sc.add_argument("--force", action="store_true")
    sc.set_defaults(func=cmd_scaffold)

    si = sub.add_parser("source-intake")
    si.add_argument("--source-path")
    si.add_argument("--pointer")
    si.add_argument("--source-id")
    si.add_argument("--title")
    si.add_argument("--source-type", choices=["article", "paper", "note", "ref", "other"], default="other")
    si.add_argument("--storage-mode", choices=["pointer_only", "copy_into_kb", "snapshot_copy"], default="copy_into_kb")
    si.add_argument("--as-version", action="store_true")
    si.add_argument("--allow-duplicate", action="store_true")
    si.set_defaults(func=cmd_source_intake)

    h = sub.add_parser("hash")
    h.add_argument("--path", required=True)
    h.set_defaults(func=cmd_hash)

    pm = sub.add_parser("generate-source-payload-manifest", aliases=["source-payload-manifest", "payload-manifest"])
    pm.add_argument("--raw-root", help="Override payload root; defaults to <kb-root>/raw")
    pm.add_argument("--output", help="Override output path; defaults to manifests/source-payload-manifest.json")
    pm.add_argument("--group-map", help="Optional explicit JSON map of raw-relative or KB-relative paths to group names")
    pm.add_argument("--include-generated-at", action="store_true", help="Include a volatile generated_at timestamp; off by default for deterministic diffs")
    pm.set_defaults(func=cmd_generate_source_payload_manifest)

    pf = sub.add_parser("preflight")
    pf.add_argument("--source-path")
    pf.set_defaults(func=cmd_preflight)

    sub.add_parser("phase0").set_defaults(func=cmd_phase0)

    ip1 = sub.add_parser("ingest-phase1")
    ip1.add_argument("--source-path", required=True)
    ip1.add_argument("--source-slug")
    ip1.set_defaults(func=cmd_ingest_phase1)

    ip2 = sub.add_parser("ingest-phase2")
    ip2.add_argument("--analysis", required=True, help="Analysis filename under ingest-analysis/")
    ip2.add_argument("--approval-phrase", required=True)
    ip2.set_defaults(func=cmd_ingest_phase2)

    sub.add_parser("index").set_defaults(func=cmd_index)

    q = sub.add_parser("query")
    q.add_argument("--query", required=True)
    q.add_argument("--limit", type=int, default=8)
    q.add_argument("--save", action="store_true")
    q.set_defaults(func=cmd_query)

    lint_cmd = sub.add_parser("lint")
    lint_cmd.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
    lint_cmd.add_argument("--strict", action="store_true", default=argparse.SUPPRESS)
    lint_cmd.set_defaults(func=cmd_lint)
    router_lint = sub.add_parser("lint-repo-execution-router")
    router_lint.add_argument("--target", required=True, help="Markdown/YAML handover file or directory to lint")
    router_lint.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
    router_lint.add_argument("--strict", action="store_true", default=argparse.SUPPRESS)
    router_lint.set_defaults(func=cmd_lint_repo_execution_router)
    historical_lint = sub.add_parser("lint-historical-path-authority")
    historical_lint.add_argument("--target", required=True, help="Markdown/YAML file or directory to lint")
    historical_lint.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
    historical_lint.add_argument("--strict", action="store_true", default=argparse.SUPPRESS)
    historical_lint.set_defaults(func=cmd_lint_historical_path_authority)
    audit_cmd = sub.add_parser("audit")
    audit_cmd.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
    audit_cmd.set_defaults(func=cmd_audit)
    status_cmd = sub.add_parser("status")
    status_cmd.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
    status_cmd.set_defaults(func=cmd_status)
    health_cmd = sub.add_parser("health")
    health_cmd.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
    health_cmd.set_defaults(func=cmd_health)
    quality_cmd = sub.add_parser("quality", help="Generate quality/coverage report")
    quality_cmd.set_defaults(func=cmd_quality)
    coverage_cmd = sub.add_parser("coverage", help="Alias for quality")
    coverage_cmd.set_defaults(func=cmd_quality)
    query_eval_cmd = sub.add_parser("query-eval", help="Manage query-eval pack")
    query_eval_cmd.add_argument("--init", action="store_true", default=argparse.SUPPRESS)
    query_eval_cmd.set_defaults(func=cmd_query_eval)
    graph_cmd = sub.add_parser("graph", aliases=["process-graph"], help="Extract process-flow graph")
    graph_cmd.set_defaults(func=cmd_graph)
    sub.add_parser("postflight", help="Run the bounded seven-stage deterministic completion aggregate").set_defaults(func=cmd_postflight)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = normalize_global_flag_placement(list(argv) if argv is not None else sys.argv[1:])
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.kb_root:
        parser.error("--kb-root is required")
    try:
        result = args.func(args)
        maybe_write_output_json(args, result, resolve_kb_root(args.kb_root))
        emit(args, result)
        status = result.get("status") if isinstance(result, dict) else None
        if status == "internal_error":
            return 1
        return 2 if status in {"blocked", "fail", "error"} else 0
    except SystemExit:
        raise
    except Exception as exc:
        emit(args, {"command": getattr(args, "command", "unknown"), "status": "error", "error": str(exc)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
