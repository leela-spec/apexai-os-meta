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
import subprocess
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
STATUS_ALLOWED = {
    "draft",
    "active",
    "needs_review",
    "analysis_complete_unvalidated",
    "partial",
    "compiled_unvalidated",
    "query_ready",
    "deprecated",
    "superseded",
}
PAGE_TYPE_ALLOWED = {"summary", "concept", "entity", "index", "query_output", "audit_item"}
PHASE2_VALUE_HEADINGS = [
    "Target Questions Answered",
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
    "missing_target_queries", "unknown_target_query_id", "target_query_route_missing",
    "ranked_source_not_in_source_refs", "ranked_source_not_analyzed",
    "ranked_source_without_claim_use", "source_ref_without_phase1_evidence",
    "candidate_promotion_disposition_missing", "readable_unopened_source_blocks_completion",
    "semantic_acceptance_missing", "semantic_acceptance_incomplete",
    "topic_status_inconsistent", "legacy_semantic_contract",
)
QUALITY_REASON = {code: code for code in QUALITY_REASON_CODES}
TEXT_EXTS = {".md", ".mdx", ".txt", ".yaml", ".yml", ".json", ".csv", ".py", ".toml"}
RAW_SUBDIRS = ["raw/articles", "raw/papers", "raw/notes", "raw/refs", "raw/other"]
REQUIRED_DIRS = RAW_SUBDIRS + ["ingest-analysis", "wiki/concepts", "wiki/entities", "wiki/summaries", "manifests", "manifests/phase0", "derived/search", "audit/resolved", "outputs/queries", "log"]
REQUIRED_FILES = ["README.md", "kb-schema.md", "wiki/index.md", "manifests/source-manifest.json"]
SEMANTIC_CONTRACT_VERSION = "2"
SEMANTIC_ACCEPTANCE_SCHEMA = "apex.kb.semantic-acceptance.v1"
SEMANTIC_RUN_LEDGER_SCHEMA = "apex.kb.semantic-run-ledger.v1"


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
        temp = dest.with_name(f".{dest.name}.{os.getpid()}.tmp")
        try:
            shutil.copy2(src, temp)
            os.replace(temp, dest)
        finally:
            if temp.exists():
                temp.unlink()
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
        "control", "scaffold", "source-intake", "hash", "generate-source-payload-manifest", "source-payload-manifest",
        "payload-manifest", "preflight", "topic-sanity-check", "phase0", "ingest-phase1", "ingest-phase2", "index", "query",
        "lint", "audit", "status", "health",
        "quality", "coverage", "query-eval", "semantic-acceptance-status", "graph", "process-graph", "postflight",
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
- `manifests/run-intent.md` stores operator-owned run configuration and confirmation.
- `manifests/run-state.json` stores machine-owned lifecycle progress and legal transitions.
- `manifests/topic-registry.json` stores operator/LLM-authored topic and target-query definitions.
- `manifests/source-manifest.json` records source custody and hashes.
- `ingest-analysis/` stores topic-scoped Phase 1 semantic analysis.
- `wiki/` stores compiled KB pages.
- `audit/semantic-acceptance/` stores independent semantic verdicts.
- `log/runs/` stores stage results, readbacks, and authoritative semantic handoff packets.

Derived paths:

- `manifests/phase0/` stores deterministic navigation artifacts.
- `derived/search/` stores rebuildable retrieval indexes.
- `outputs/queries/` stores reusable cited query packets.

Use `python apex-meta/scripts/apex_kb.py --kb-root <this-root> control next` to derive the exact next action. Apex KB must not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU, or personal orchestration state. Other systems may consume KB outputs as read-only evidence packets.
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
    controlled_run_default: "continuous Phase 1 to Phase 2 when the selected output tier includes wiki output"
    safe_stop_modes: [analysis_only, operator_explicit_stop_before_wiki]
    legacy_direct_command_phrase: "approve ingest"
    independent_semantic_acceptance_required_for_compiled_tiers: true
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


def repository_semantic_contract_dir() -> Path:
    return Path(__file__).resolve().parents[2] / ".claude" / "skills" / "apex-kb" / "assets" / "repository-semantic-contract"


def scaffold_semantic_contract(kb_root: Path, allow_write: bool, dry_run: bool) -> List[Dict[str, Any]]:
    source_dir = repository_semantic_contract_dir()
    if not source_dir.is_dir():
        return [{"status": "missing_package_assets", "source": str(source_dir)}]
    results: List[Dict[str, Any]] = []
    generated_from_templates = {"phase1-analysis-template.md", "phase2-wiki-page-templates.md"}
    for source in sorted(path for path in source_dir.iterdir() if path.is_file() and path.name not in generated_from_templates):
        results.append(copy_file(source, kb_root / "semantic-contract" / source.name, kb_root, allow_write, dry_run))
    package_root = source_dir.parents[1]
    results.append(copy_file(package_root / "templates" / "ingest-analysis-template.md", kb_root / "semantic-contract" / "phase1-analysis-template.md", kb_root, allow_write, dry_run))
    results.append(copy_file(package_root / "templates" / "wiki-page-templates.md", kb_root / "semantic-contract" / "phase2-wiki-page-templates.md", kb_root, allow_write, dry_run))
    return results


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
    semantic_contract = scaffold_semantic_contract(kb_root, args.allow_write, dry_run)
    return {"command": "scaffold", "kb_root": str(kb_root), "dry_run": dry_run, "directories": dir_results, "writes": writes, "semantic_contract": semantic_contract}


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
    if args.source_root:
        root = Path(args.source_root).expanduser().resolve()
        if not root.is_dir():
            return {"command": "source-intake", "status": "blocked", "reason": "--source-root must be an existing directory", "source_root": str(root)}
        manifest = read_manifest(kb_root)
        existing = {s.get("source_id"): s for s in manifest.get("sources", []) if isinstance(s, dict)}

        def belongs_to_source_root(entry: Dict[str, Any]) -> bool:
            try:
                Path(str(entry.get("original_source_path", ""))).resolve().relative_to(root)
                return True
            except (OSError, ValueError):
                return False

        existing = {k: v for k, v in existing.items() if not belongs_to_source_root(v)}
        results = []
        eligible = sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.as_posix().lower())
        for path in eligible:
            rel = path.relative_to(root).as_posix()
            source_id = "source-" + hashlib.sha256(rel.encode("utf-8")).hexdigest()[:16]
            dest = kb_root / "raw" / "other" / Path(rel)
            copy_result = copy_file(path, dest, kb_root, args.allow_write, dry_run)
            entry = {
                "source_id": source_id,
                "title": rel,
                "source_type": "other",
                "source_storage_mode": "copy_into_kb",
                "source_path": relpath(kb_root, dest),
                "original_source_path": str(path),
                "source_hash": hash_path(path).get("source_hash") or "NA",
                "hash_algorithm": "sha256-file",
                "no_hash_reason": "NA",
                "ingest_status": "source_intake_only",
                "status": "active",
                "added_at": existing.get(source_id, {}).get("added_at", utc_now()),
            }
            existing[source_id] = entry
            results.append({"source_id": source_id, "source_path": rel, "copy": copy_result})
        manifest["sources"] = [existing[k] for k in sorted(existing)]
        write = write_text(kb_root / MANIFEST_PATH, manifest_text(manifest), kb_root, args.allow_write, dry_run)
        return {"command": "source-intake", "dry_run": dry_run, "status": "ok", "source_root": str(root), "file_count": len(eligible), "results": results, "manifest_write": write}
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
    source_id_blocked = source_id in existing_ids and not args.as_version
    duplicate_blocked = bool(dupes) and not args.allow_duplicate and not args.as_version
    blocked = source_id_blocked or duplicate_blocked
    if not blocked:
        if source_id in existing_ids:
            base = source_id
            n = 2
            while f"{base}-v{n}" in existing_ids:
                n += 1
            entry["source_id"] = f"{base}-v{n}"
        manifest.setdefault("sources", []).append(entry)
    write = None if blocked else write_text(kb_root / MANIFEST_PATH, manifest_text(manifest), kb_root, args.allow_write, dry_run)
    reason_code = "source_id_exists" if source_id_blocked else ("duplicate_source_hash" if duplicate_blocked else None)
    return {"command": "source-intake", "dry_run": dry_run, "status": "blocked" if blocked else "ok", "reason_code": reason_code, "entry": entry, "duplicate_hash_candidates": dupes, "copies": copies, "manifest_write": write}


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
        existing_analysis = _phase1_analysis_files_referencing_source(kb_root, source_slug)
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


def cmd_topic_sanity_check(args: argparse.Namespace) -> Dict[str, Any]:
    """Cheap, read-only, bounded-cost gate against locking the wrong topic and
    then burning a full corpus intake + Phase 0 run on it. Run this BEFORE
    scaffold, source-intake, or phase0 for any newly locked topic - never
    after. It never reads full file contents, and never registers, hashes,
    scaffolds, or writes anything.

    It deliberately does NOT check kb-schema.md or README.md: those are
    written by the same scaffold step that locks the topic, so on a fresh KB
    they are self-authored, circular confirmation of whatever topic name the
    executor already typed in - not independent evidence. (This is exactly
    how the incident this check exists to prevent slipped through once
    already: the KB itself was titled after the wrong topic, so checking the
    KB's own title "confirmed" it.)

    Evidence is split into strong terms (phrases, aliases, the full topic
    name as one phrase) and weak terms (supporting_terms). Only a strong-term
    match, or two-or-more DISTINCT weak terms co-occurring in the same
    filename, counts as scope evidence - a single generic supporting_term
    (e.g. "process", "app") must never carry a verdict alone, mirroring why
    the registry's own vocabulary spec places such words in `ambiguous_terms`
    and requires co-occurrence before they count as a signal.

    Evidence sources: the KB root's own path components (up to 3 parents),
    sibling registry topics' strong terms, and a filename-only scan capped at
    --search-cap files (default 2000) under --search-root (default: the KB
    root's parent directory, since a KB is conventionally nested one level
    under the material it indexes).

    If the topic's strong-term vocabulary has zero correspondence to all of
    that evidence, this is a topic-lock mismatch, not a source-access
    blocker: stop and get the operator to confirm the intended subject
    before any scaffold/intake/Phase 0 write, per the failure-behavior entry
    `topic_vocabulary_mismatches_kb_scope_evidence` in SKILL.md."""
    kb_root = resolve_kb_root(args.kb_root)
    strong_terms: List[str] = []
    weak_terms: List[str] = []
    topic_slug = args.topic_slug
    registry = load_topic_registry(kb_root)
    matched_topic = None
    if topic_slug:
        for topic in registry:
            if not isinstance(topic, dict):
                continue
            slug = str(topic.get("slug") or slugify(str(topic.get("name", "topic"))))
            if slug == topic_slug:
                matched_topic = topic
                for value in (topic.get("phrases") or []) + (topic.get("aliases") or []):
                    if isinstance(value, str) and value.strip():
                        strong_terms.append(value.strip())
                for value in topic.get("supporting_terms") or []:
                    if isinstance(value, str) and value.strip():
                        weak_terms.append(value.strip())
                # The full name is one coarse phrase-level signal; splitting it into
                # individual generic words (e.g. "app", "process") would reintroduce
                # exactly the ambiguous-single-word false positives the registry's own
                # `ambiguous_terms` category exists to guard against.
                name = str(topic.get("name") or "").strip()
                if name:
                    strong_terms.append(name)
                break
    for phrase in args.phrase or []:
        if phrase and phrase.strip():
            strong_terms.append(phrase.strip())
    strong_terms = sorted({t.lower() for t in strong_terms if t})
    weak_terms = sorted({t.lower() for t in weak_terms if t and t.lower() not in strong_terms})
    if not strong_terms and not weak_terms:
        return {"command": "topic-sanity-check", "status": "blocked", "reason": "no topic terms: pass --topic-slug for a registered topic or --phrase (repeatable) for one not yet registered"}

    def _strong_hits(text: str) -> List[str]:
        low = text.lower()
        return [t for t in strong_terms if t in low]

    def _weak_cooccurrence_hit(text: str) -> bool:
        low = text.lower()
        return sum(1 for t in weak_terms if t in low) >= 2

    path_components = [kb_root.name] + [p.name for p in list(kb_root.parents)[:3]]
    path_hits = sorted({t for component in path_components for t in _strong_hits(component)})

    sibling_hits: List[str] = []
    for topic in registry:
        if not isinstance(topic, dict) or topic is matched_topic:
            continue
        label_parts = [str(topic.get("name", "")), str(topic.get("slug", ""))]
        label_parts.extend(v for v in (topic.get("phrases") or []) if isinstance(v, str))
        label_parts.extend(v for v in (topic.get("aliases") or []) if isinstance(v, str))
        sibling_hits.extend(_strong_hits(" ".join(label_parts)))
    sibling_hits = sorted(set(sibling_hits))

    search_root = Path(args.search_root).expanduser().resolve() if args.search_root else kb_root.parent
    search_cap = args.search_cap or 2000
    strong_hit_paths: List[str] = []
    weak_cooccurrence_paths: List[str] = []
    scanned_count = 0
    capped = False
    kb_root_resolved = kb_root.resolve()
    if search_root.exists():
        for path in search_root.rglob("*"):
            if scanned_count >= search_cap:
                capped = True
                break
            if not path.is_file():
                continue
            # Anything already inside kb_root is this KB's own generated output
            # (audit items, work packs, manifests) - it is written by the very
            # run being gated, so it can never be independent evidence that the
            # topic is real. Excluding it is what stops a KB from "confirming"
            # its own wrong topic after the fact, the same way kb-schema.md and
            # README.md are excluded above.
            try:
                path.resolve().relative_to(kb_root_resolved)
                continue
            except ValueError:
                pass
            scanned_count += 1
            if _strong_hits(path.name):
                if len(strong_hit_paths) < 20:
                    strong_hit_paths.append(str(path))
            elif _weak_cooccurrence_hit(path.name):
                if len(weak_cooccurrence_paths) < 20:
                    weak_cooccurrence_paths.append(str(path))

    evidence = {
        "strong_terms": strong_terms,
        "weak_terms": weak_terms,
        "path_components_checked": path_components,
        "path_component_hits": path_hits,
        "sibling_topic_strong_hits": sibling_hits,
        "filename_scan": {
            "search_root": str(search_root),
            "scanned_count": scanned_count,
            "capped": capped,
            "strong_hit_count": len(strong_hit_paths),
            "strong_hit_paths_sample": strong_hit_paths,
            "weak_cooccurrence_hit_count": len(weak_cooccurrence_paths),
            "weak_cooccurrence_paths_sample": weak_cooccurrence_paths,
            "note": "weak_cooccurrence hits are reported for transparency only and never count toward the verdict - two generic supporting_terms co-occurring in a filename (e.g. \"process\"+\"screen\") is still too weak to trust alone.",
        },
    }
    # Weak-term co-occurrence is deliberately excluded from the verdict sum: it
    # is reported above for transparency, but generic supporting_terms are too
    # unreliable to independently justify "proceed" - the asymmetric cost of a
    # false "proceed" (a burned full-corpus run) far outweighs the cost of an
    # unnecessary operator confirmation.
    total_reliable_hits = len(path_hits) + len(sibling_hits) + len(strong_hit_paths)
    verdict = "scope_evidence_found" if total_reliable_hits > 0 else "scope_evidence_absent"
    recommendation = "proceed" if total_reliable_hits > 0 else "stop_and_confirm_topic_with_operator"
    message = (
        f"Topic strong terms {strong_terms} have {total_reliable_hits} corresponding hit(s) across KB-scope evidence."
        if total_reliable_hits > 0
        else f"Topic strong terms {strong_terms} have ZERO correspondence to this KB's own scope evidence "
             f"(path, sibling topics, {scanned_count} filenames under {search_root}, excluding the KB's own "
             "generated output), and weak supporting "
             "terms alone never count. This is a topic-lock mismatch, not a source-access blocker - stop "
             "and confirm the intended subject with the operator before any scaffold, source-intake, or "
             "Phase 0 write."
    )
    return {
        "command": "topic-sanity-check",
        "status": "ok",
        "topic_slug": topic_slug,
        "evidence": evidence,
        "verdict": verdict,
        "recommendation": recommendation,
        "message": message,
    }


def _iter_kb_files(kb_root: Path, suffix_filter: Optional[set]) -> List[Path]:
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
                if not p.is_file() or (rel_parts & excluded_parts) or resolved in seen:
                    continue
                if suffix_filter is not None and p.suffix.lower() not in suffix_filter:
                    continue
                files.append(p)
                seen.add(resolved)
    return files


def iter_source_files(kb_root: Path) -> List[Path]:
    return _iter_kb_files(kb_root, TEXT_EXTS)


def iter_all_source_files(kb_root: Path) -> List[Path]:
    """Every file under sources/raw regardless of extension -- including
    non-text/binary files, so they remain visible in source-facts.json instead
    of silently vanishing from scope."""
    return _iter_kb_files(kb_root, None)


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
    section_spans = section_spans_from_headings(headings, len(lines))
    return {
        "path": relpath(kb_root, path),
        "source_type_guess": source_type_guess(path),
        "h1_title": next((h["text"] for h in headings if h["level"] == 1), None),
        "headings": headings,
        "section_spans": section_spans,
        "markdown_links": links,
        "wikilinks": wikilinks,
        "code_blocks": code_blocks,
        "frontmatter": {"has_frontmatter": bool(meta), "raw_field_keys": sorted(meta.keys()), "parse_status": fm_status},
        "parser_warnings": (["unclosed_code_fence"] if in_fence else []),
    }


def section_spans_from_headings(headings: List[Dict[str, Any]], total_lines: int) -> List[Dict[str, Any]]:
    """A heading's span runs to the line before the next heading of the same or
    shallower level (or end of file). Gives every candidate a stable line range
    to point at instead of just a single heading line."""
    spans = []
    for i, h in enumerate(headings):
        end_line = total_lines
        for later in headings[i + 1:]:
            if later["level"] <= h["level"]:
                end_line = later["line"] - 1
                break
        spans.append({"heading": h["text"], "level": h["level"], "start_line": h["line"], "end_line": max(end_line, h["line"])})
    return spans


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


def source_id_for(rel_path: str) -> str:
    return "src-" + hashlib.sha256(rel_path.encode("utf-8")).hexdigest()[:16]


def compute_hash_groups(kb_root: Path, files: List[Path]) -> Dict[str, List[str]]:
    """Exact-content hash groups (path -> sha256 -> siblings). Free -- reuses
    the same hash-then-group approach corpus_profile already did inline, but
    exposes it so rank_topic_sources and source-facts can collapse duplicates
    without rereading files."""
    groups: Dict[str, List[str]] = defaultdict(list)
    for p in files:
        try:
            groups[sha256_file(p)].append(relpath(kb_root, p))
        except Exception:
            continue
    return groups


def normalize_text_for_dedupe(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def normalized_duplicate_groups(kb_root: Path, files: List[Path]) -> List[List[str]]:
    """Near-duplicate detection: same text once whitespace/case differences are
    collapsed. Conservative -- only exact matches after normalization, never a
    fuzzy/similarity score."""
    buckets: Dict[str, List[str]] = defaultdict(list)
    for p in files:
        try:
            text = read_text(p)
        except Exception:
            continue
        norm_hash = hashlib.sha256(normalize_text_for_dedupe(text).encode("utf-8")).hexdigest()
        buckets[norm_hash].append(relpath(kb_root, p))
    return [sorted(v) for v in buckets.values() if len(v) > 1]


VERSION_TOKEN_RE = re.compile(r"(?i)[-_ ]?(v\d+|version\d+|night\d+|draft\d*|final|old|new|copy\d*|\(\d+\))(?=\.[a-z0-9]+$|[-_ ]|$)")


def version_family_candidates(kb_root: Path, files: List[Path]) -> List[Dict[str, Any]]:
    """Conservative possible-version-family grouping: same folder, same
    extension, same filename once a version-ish token (v2, Night4, draft,
    old/new/final, copy, "(2)") is stripped. Never auto-resolves supersession --
    only the LLM decides that; this is discovery evidence only."""
    groups: Dict[str, List[str]] = defaultdict(list)
    for p in files:
        stem = VERSION_TOKEN_RE.sub("", p.stem).strip("-_ ").lower()
        stem = re.sub(r"\s+", " ", stem)
        if not stem:
            continue
        key = f"{p.parent.as_posix()}::{stem}{p.suffix.lower()}"
        groups[key].append(relpath(kb_root, p))
    families = []
    for key, members in sorted(groups.items()):
        if len(members) > 1:
            families.append({"possible_family_key": key.split("::", 1)[1], "members": sorted(members), "confidence": "possible", "method": "filename_token"})
    return families


def git_last_change_map(kb_root: Path) -> Tuple[Dict[str, str], bool]:
    """Best-effort last-change date per kb-root-relative path from Git history,
    scoped to this kb_root's subtree. Read-only; never writes, never shells to
    anything but `git log`. Returns ({}, False) when no repo root is found or
    Git is unavailable/fails -- callers must fall back to file mtime."""
    repo_root = find_repo_root(kb_root)
    if repo_root is None:
        return {}, False
    try:
        kb_rel = kb_root.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        kb_rel = "."
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "log", "--format=COMMIT\t%cI", "--name-only", "--", kb_rel],
            capture_output=True, text=True, timeout=30, encoding="utf-8", errors="replace",
        )
    except (OSError, subprocess.SubprocessError, ValueError):
        return {}, False
    if result.returncode != 0:
        return {}, False
    prefix = "" if kb_rel in ("", ".") else kb_rel.rstrip("/") + "/"
    mapping: Dict[str, str] = {}
    current_date: Optional[str] = None
    for line in result.stdout.splitlines():
        if line.startswith("COMMIT\t"):
            current_date = line.split("\t", 1)[1]
            continue
        if not line.strip() or current_date is None:
            continue
        repo_rel = line.strip().replace("\\", "/")
        if prefix and not repo_rel.startswith(prefix):
            continue
        rel = repo_rel[len(prefix):] if prefix else repo_rel
        if rel not in mapping:
            mapping[rel] = current_date
    return mapping, True


def build_source_facts(
    kb_root: Path,
    all_files: List[Path],
    text_files: List[Path],
    hash_groups: Dict[str, List[str]],
    git_map: Dict[str, str],
    git_available: bool,
) -> List[Dict[str, Any]]:
    """One row per scanned file, including non-text/unreadable ones -- the L1
    custody fact sheet. Never silently drops a file: blocked_reason names why a
    file has no headings/text when it doesn't."""
    text_set = {p.resolve() for p in text_files}
    facts: List[Dict[str, Any]] = []
    for p in all_files:
        rel = relpath(kb_root, p)
        text_readable = p.resolve() in text_set
        sha, size, readable = None, None, True
        try:
            size = p.stat().st_size
            sha = sha256_file(p)
        except Exception:
            readable = False
        blocked_reason = None
        if not readable:
            blocked_reason = "unreadable"
        elif not text_readable:
            blocked_reason = "non_text"
        frontmatter_date = None
        if text_readable:
            try:
                meta, _body, _fm_status = parse_frontmatter(read_text(p))
                for key in ("date", "updated_at", "created_at"):
                    if meta.get(key):
                        frontmatter_date = str(meta[key])
                        break
            except Exception:
                pass
        last_change, last_change_source = None, None
        if git_available and rel in git_map:
            last_change, last_change_source = git_map[rel], "git"
        elif frontmatter_date:
            last_change, last_change_source = frontmatter_date, "frontmatter"
        elif readable:
            try:
                last_change = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc).date().isoformat()
                last_change_source = "mtime"
            except Exception:
                pass
        dup_group = hash_groups.get(sha, []) if sha else []
        facts.append({
            "source_id": source_id_for(rel),
            "path": rel,
            "sha256": sha,
            "size_bytes": size,
            "text_readable": text_readable,
            "blocked_reason": blocked_reason,
            "last_change": last_change,
            "last_change_source": last_change_source,
            "frontmatter_date": frontmatter_date,
            "exact_duplicate_group_size": len(dup_group),
        })
    return facts


def load_analysis_config(kb_root: Path) -> Dict[str, Any]:
    path = kb_root / "manifests" / "analysis-config.json"
    defaults = {"signals": {"freshness": "auto", "duplicate_collapse": "auto", "negative_terms": "auto", "reference_graph": "off"}, "gap_cut": {"method": "elbow", "min_tier": "body_weak"}}
    if not path.exists():
        return defaults
    try:
        loaded = json.loads(read_text(path))
    except Exception:
        return defaults
    signals = {**defaults["signals"], **(loaded.get("signals") or {})}
    gap_cut = {**defaults["gap_cut"], **(loaded.get("gap_cut") or {})}
    return {"signals": signals, "gap_cut": gap_cut}


def resolve_signal_activation(config: Dict[str, Any], availability: Dict[str, Any]) -> Dict[str, bool]:
    """`auto` resolves from measured corpus evidence, never a guess: a signal
    only turns on when the corpus-profile availability report shows material
    for it. `on`/`off` always override."""
    signals = config.get("signals", {})

    def resolve(name: str, auto_condition: bool) -> bool:
        value = signals.get(name, "auto")
        if value == "on":
            return True
        if value == "off":
            return False
        return bool(auto_condition)

    return {
        "freshness": resolve("freshness", availability.get("git_history") or availability.get("frontmatter_dates")),
        "duplicate_collapse": resolve("duplicate_collapse", (availability.get("exact_duplicates", 0) > 0) or (availability.get("normalized_duplicates", 0) > 0)),
        "negative_terms": resolve("negative_terms", availability.get("negative_terms_declared", False)),
        "reference_graph": resolve("reference_graph", availability.get("link_density", 0.0) >= 0.3),
    }


def cmd_phase0(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    manifest = read_manifest(kb_root)
    inventory = read_source_inventory(kb_root)
    files = iter_source_files(kb_root)
    all_files = iter_all_source_files(kb_root)
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
    all_scanned_files = all_files + pointer_files
    structures = [parse_markdown_structure(p, kb_root) for p in scanned_files]
    heading_map = [{"path": r["path"], "source_type_guess": r["source_type_guess"], "h1_title": r["h1_title"], "headings": r["headings"], "parser_warnings": r["parser_warnings"]} for r in structures]
    link_map = [{"path": r["path"], "markdown_links": r["markdown_links"], "wikilinks": r["wikilinks"]} for r in structures]
    frontmatter_map = [{"path": r["path"], **r["frontmatter"]} for r in structures]
    term_freq, file_hit_totals = generic_term_frequency(kb_root, scanned_files)
    topic_registry = load_topic_registry(kb_root)

    # L1 facts: exact/normalized duplicates, possible version families, Git-or-
    # mtime freshness, and a custody row for every scanned file (incl. non-text).
    hash_groups = compute_hash_groups(kb_root, all_scanned_files)
    normalized_dupe_groups = normalized_duplicate_groups(kb_root, scanned_files)
    version_families = version_family_candidates(kb_root, all_scanned_files)
    git_map, git_available = git_last_change_map(kb_root)
    source_facts = build_source_facts(kb_root, all_scanned_files, scanned_files, hash_groups, git_map, git_available)
    blocked_counts = {
        "non_text": sum(1 for f in source_facts if f["blocked_reason"] == "non_text"),
        "unreadable": sum(1 for f in source_facts if f["blocked_reason"] == "unreadable"),
    }

    analysis_config = load_analysis_config(kb_root)
    signal_availability = {
        "git_history": git_available,
        "frontmatter_dates": any(f["last_change_source"] == "frontmatter" for f in source_facts),
        "exact_duplicates": sum(1 for v in hash_groups.values() if len(v) > 1),
        "normalized_duplicates": len(normalized_dupe_groups),
        "version_families": len(version_families),
        "link_density": round(sum(len(s.get("markdown_links", [])) + len(s.get("wikilinks", [])) for s in structures) / len(structures), 3) if structures else 0.0,
        "negative_terms_declared": any(bool(t.get("negative_terms") or t.get("ambiguous_terms")) for t in topic_registry if isinstance(t, dict)),
        "generic_high_freq_terms": [row["term"] for row in term_freq[:10]],
    }
    resolved_signals = resolve_signal_activation(analysis_config, signal_availability)
    reverse_links = build_reverse_link_index(structures)

    # L2: exhaustive, tiered, field-separated ranking -- no top-N truncation.
    topic_rankings = rank_topic_sources(kb_root, scanned_files, topic_registry, structures, source_facts, hash_groups, reverse_links, resolved_signals)
    # L3: bounded per-topic work pack, concentrated from the exhaustive ranking.
    workpacks = [build_topic_workpack(entry, topic_rankings[str(entry.get("slug") or slugify(str(entry.get("name", "unnamed"))))])
                 for entry in topic_registry if isinstance(entry, dict)]

    profile = corpus_profile(kb_root, scanned_files, structures, term_freq, inventory, hash_groups, normalized_dupe_groups, version_families, signal_availability, blocked_counts)
    priority = priority_candidates(kb_root, scanned_files, structures, file_hit_totals)
    report = phase0_report(kb_root, scanned_files, structures)
    writes = [
        write_text(kb_root / PHASE0_DIR / "corpus-profile.md", profile, kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "heading-map.json", json.dumps(heading_map, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "markdown-link-map.json", json.dumps(link_map, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "frontmatter-map.json", json.dumps(frontmatter_map, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "term-frequency.json", json.dumps(term_freq, indent=2, ensure_ascii=False) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "topic-source-rankings.json", json.dumps(topic_rankings, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "source-priority-candidates.md", priority, kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "phase0-navigation-report.md", report, kb_root, args.allow_write, dry_run),
        write_text(kb_root / PHASE0_DIR / "source-facts.json", json.dumps(source_facts, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run),
    ]
    for wp in workpacks:
        writes.append(write_text(kb_root / PHASE0_DIR / "work-packs" / f"{wp['slug']}.md", wp["markdown"], kb_root, args.allow_write, dry_run))
        writes.append(write_text(kb_root / PHASE0_DIR / "work-packs" / f"{wp['slug']}.json", json.dumps(wp["json"], indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run))
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
        "topic_registry_entries": len(topic_registry),
        "signal_availability": signal_availability,
        "resolved_signals": resolved_signals,
        "work_pack_count": len(workpacks),
        "blocked_file_counts": blocked_counts,
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


STOPWORDS = frozenset({
    "the", "a", "an", "and", "or", "but", "if", "then", "else", "for", "of", "in", "on", "at", "to",
    "from", "by", "with", "as", "is", "are", "was", "were", "be", "been", "being", "this", "that",
    "these", "those", "it", "its", "you", "your", "we", "our", "they", "their", "he", "she", "his",
    "her", "not", "no", "yes", "do", "does", "did", "can", "could", "should", "would", "will", "shall",
    "may", "might", "must", "have", "has", "had", "i", "me", "my", "so", "such", "than", "too", "very",
    "just", "about", "into", "over", "under", "between", "through", "up", "down", "out", "off", "again",
    "further", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "only", "own", "same", "which", "who", "whom", "what",
})


def _tokenize_words(text: str) -> List[str]:
    return re.findall(r"[A-Za-z][A-Za-z0-9'-]{1,}", text.lower())


def generic_term_frequency(kb_root: Path, files: List[Path], top_n: int = 60) -> Tuple[List[Dict[str, Any]], Dict[str, int]]:
    """Domain-agnostic term frequency across the raw corpus. Filters only a small
    standard English stopword list -- no hardcoded topic/domain strings, so this
    runs identically regardless of what a given KB is actually about."""
    term_counts: Counter = Counter()
    term_files: Dict[str, set] = defaultdict(set)
    file_hit_totals: Counter = Counter()
    for path in files:
        try:
            text = read_text(path)
        except Exception:
            continue
        rel = relpath(kb_root, path)
        words = _tokenize_words(text)
        significant = [w for w in words if w not in STOPWORDS and len(w) > 2]
        if not significant:
            continue
        file_hit_totals[rel] += len(significant)
        for w in significant:
            term_counts[w] += 1
            term_files[w].add(rel)
    ranked = [{"term": term, "count": count, "file_count": len(term_files[term])} for term, count in term_counts.most_common(top_n)]
    return ranked, dict(file_hit_totals)


def load_topic_registry(kb_root: Path) -> List[Dict[str, Any]]:
    path = kb_root / "manifests" / "topic-registry.json"
    if not path.exists():
        return []
    try:
        data = json.loads(read_text(path))
    except Exception:
        return []
    entries = data.get("topics") if isinstance(data, dict) else data
    return entries if isinstance(entries, list) else []


def registry_query_map(kb_root: Path) -> Dict[str, Dict[str, Any]]:
    result: Dict[str, Dict[str, Any]] = {}
    for topic in load_topic_registry(kb_root):
        if not isinstance(topic, dict):
            continue
        topic_slug = str(topic.get("slug") or slugify(str(topic.get("name", "topic"))))
        for query in topic.get("target_queries", []):
            if not isinstance(query, dict):
                continue
            query_id = str(query.get("query_id") or "").strip()
            if query_id:
                result[query_id] = {**query, "topic_slug": topic_slug, "topic_status": topic.get("status")}
    return result


def topic_queries(topic: Dict[str, Any]) -> List[Dict[str, Any]]:
    value = topic.get("target_queries", []) if isinstance(topic, dict) else []
    return [entry for entry in value if isinstance(entry, dict)] if isinstance(value, list) else []


def build_reverse_link_index(structures: List[Dict[str, Any]]) -> Dict[str, set]:
    """path -> set of paths that link to it, via relative markdown links only
    (absolute URLs/anchors/wikilinks carry no reliable cross-file signal in a
    raw, non-wiki corpus). Feeds the optional reference_graph signal; never
    required for tiering or scoring when that signal is off."""
    known_paths = {s["path"] for s in structures}
    reverse: Dict[str, set] = defaultdict(set)
    for s in structures:
        source_path = s["path"]
        source_dir = Path(source_path).parent
        for link in s.get("markdown_links", []):
            if link.get("target_type") != "relative_file":
                continue
            target = link.get("normalized_target")
            if not target:
                continue
            candidate = target.lstrip("/") if target.startswith("/") else (source_dir / target).as_posix()
            candidate = os.path.normpath(candidate).replace("\\", "/")
            if candidate in known_paths:
                reverse[candidate].add(source_path)
    return reverse


TOPIC_SOURCE_RANKINGS_SCHEMA = "apex.kb.topic-source-rankings.v2"
TIER_BASE_SCORE = {"filename": 100.0, "h1": 80.0, "heading": 60.0, "body_strong": 30.0, "body_weak": 10.0}
TIER_RANK = {"filename": 0, "h1": 1, "heading": 2, "body_strong": 3, "body_weak": 4}


def _topic_vocabulary(entry: Dict[str, Any]) -> Dict[str, List[str]]:
    phrases = [str(x) for x in entry.get("phrases", []) if str(x).strip()]
    aliases = [str(x) for x in entry.get("aliases", []) if str(x).strip()]
    supporting = [str(x) for x in entry.get("supporting_terms", []) if str(x).strip()]
    if not phrases and not aliases and not supporting:
        # Back-compat: legacy registries only had `keywords`. Read them as
        # supporting_terms rather than inventing a phrase tier they never had.
        supporting = [str(x) for x in entry.get("keywords", []) if str(x).strip()]
    negative = [str(x) for x in entry.get("negative_terms", []) if str(x).strip()]
    ambiguous = [str(x) for x in entry.get("ambiguous_terms", []) if str(x).strip()]
    return {"phrases": phrases, "aliases": aliases, "supporting_terms": supporting, "negative_terms": negative, "ambiguous_terms": ambiguous}


def section_for_line(section_spans: List[Dict[str, Any]], line_no: int) -> Optional[str]:
    """The deepest heading whose span contains line_no. Spans are in document
    order, so the LAST containing span is the most specific (a nested
    subheading's span is a subset of its parent's and appears after it)."""
    best = None
    for span in section_spans:
        if span["start_line"] <= line_no <= span["end_line"]:
            best = span["heading"]
    return best


def elbow_cut_index(scores: List[float]) -> int:
    """Where the score sequence (already sorted descending) drops sharply.
    Returns len(scores) -- include everything -- unless a real relative gap
    (>=15%) is found; this is a shape-detection threshold for whether a cut is
    justified at all, never a fixed count of items to keep."""
    n = len(scores)
    if n <= 1:
        return n
    best_gap, best_idx = -1.0, n
    for i in range(n - 1):
        denom = scores[i] if scores[i] > 0 else 1.0
        gap = (scores[i] - scores[i + 1]) / denom
        if gap > best_gap:
            best_gap, best_idx = gap, i + 1
    if best_gap < 0.15:
        return n
    return max(best_idx, 1)


def _candidate_pointer(field: str, line: int, section_spans: List[Dict[str, Any]], snippet: str) -> Dict[str, Any]:
    span = None
    for s in section_spans:
        if s["start_line"] <= line <= s["end_line"]:
            span = [s["start_line"], s["end_line"]]
    return {"field": field, "line": line, "section_span": span, "snippet": snippet[:220]}


def rank_topic_sources(
    kb_root: Path,
    files: List[Path],
    registry: List[Dict[str, Any]],
    structures: List[Dict[str, Any]],
    source_facts: List[Dict[str, Any]],
    hash_groups: Dict[str, List[str]],
    reverse_links: Dict[str, set],
    resolved_signals: Dict[str, bool],
) -> Dict[str, Any]:
    """Exhaustive, field-separated, tiered ranking per registry topic. Never
    truncates the candidate set -- every signal-bearing source gets a row with
    an inspectable `why` and at least one pointer. Concentration for the
    semantic step happens separately (gap_cut/held_in_custody), not by
    removing rows here. Rankings remain navigation candidates only: rank never
    proves authority, complete reading, or material use."""
    struct_by_path = {s["path"]: s for s in structures}
    facts_by_path = {f["path"]: f for f in source_facts}
    all_rels = [relpath(kb_root, p) for p in files]
    results: Dict[str, Any] = {}

    for entry in registry:
        slug = str(entry.get("slug") or slugify(str(entry.get("name", "unnamed"))))
        vocab = _topic_vocabulary(entry)
        phrases, aliases, supporting = vocab["phrases"], vocab["aliases"], vocab["supporting_terms"]
        negative, ambiguous = vocab["negative_terms"], vocab["ambiguous_terms"]
        strong_terms = phrases + aliases
        name_supporting_terms = strong_terms + supporting
        empty_gap_cut = {"method": "elbow", "tier_boundary": "body_weak", "included_count": 0, "held_in_custody_count": 0}
        if not name_supporting_terms:
            results[slug] = {
                "schema": TOPIC_SOURCE_RANKINGS_SCHEMA, "name": entry.get("name"), "vocabulary": vocab,
                "signals_active": resolved_signals, "considered_source_count": len(files), "candidate_count": 0,
                "candidates": [], "gap_cut": empty_gap_cut, "held_in_custody": [], "zero_signal_custody": sorted(all_rels),
            }
            continue

        partial: List[Dict[str, Any]] = []
        for path in files:
            rel = relpath(kb_root, path)
            struct = struct_by_path.get(rel, {})
            try:
                text = read_text(path)
            except Exception:
                continue
            low_full = text.lower()
            filename_low = path.name.lower()
            h1_low = (struct.get("h1_title") or "").lower()
            headings = struct.get("headings", [])
            section_spans = struct.get("section_spans", [])

            filename_hit = list(dict.fromkeys(t for t in name_supporting_terms if t.lower() in filename_low))
            h1_hit = list(dict.fromkeys(t for t in name_supporting_terms if h1_low and t.lower() in h1_low))
            heading_hit: List[str] = []
            heading_line = None
            for h in headings:
                htext_low = h["text"].lower()
                for t in name_supporting_terms:
                    if t.lower() in htext_low and t not in heading_hit:
                        heading_hit.append(t)
                        if heading_line is None:
                            heading_line = h["line"]

            lines = text.splitlines()
            body_hit_count = 0
            body_hit_sections: List[str] = []
            co_occurring: set = set()
            has_supporting_body = False
            body_term_hits: set = set()
            first_body_line, first_body_snippet = None, ""
            for idx, line in enumerate(lines, start=1):
                low_line = line.lower()
                line_terms = [t for t in name_supporting_terms if t.lower() in low_line]
                if line_terms:
                    body_hit_count += len(line_terms)
                    body_term_hits.update(line_terms)
                    if first_body_line is None:
                        first_body_line, first_body_snippet = idx, line.strip()
                    sec = section_for_line(section_spans, idx)
                    if sec and sec not in body_hit_sections:
                        body_hit_sections.append(sec)
                    if len(line_terms) > 1:
                        co_occurring.update(line_terms)
                    if any(t in supporting for t in line_terms):
                        has_supporting_body = True

            strong_body_hit = bool(strong_terms) and any(t.lower() in low_full for t in strong_terms)
            negative_ambiguous_lower = {t.lower() for t in negative + ambiguous}
            # True only when every body-term hit in this file is itself a
            # negative/ambiguous term -- i.e. there is no "clean" supporting-term
            # hit anywhere to ground it. A phrase/alias match already took the
            # strong_body_hit branch above and never reaches this suppression.
            all_body_hits_are_negative_only = bool(body_term_hits) and all(t.lower() in negative_ambiguous_lower for t in body_term_hits)

            if filename_hit:
                tier, pointer = "filename", _candidate_pointer("filename", 1, section_spans, path.name)
            elif h1_hit:
                h1_line = next((h["line"] for h in headings if h.get("level") == 1), 1)
                pointer = _candidate_pointer("h1", h1_line, section_spans, struct.get("h1_title") or "")
                tier = "h1"
            elif heading_hit:
                tier, pointer = "heading", _candidate_pointer("heading", heading_line or 1, section_spans, heading_hit[0])
            elif strong_body_hit:
                tier = "body_strong"
                pointer = _candidate_pointer("body", first_body_line or 1, section_spans, first_body_snippet)
            elif has_supporting_body:
                tier = "body_strong" if (co_occurring or len(body_hit_sections) > 1) else "body_weak"
                pointer = _candidate_pointer("body", first_body_line or 1, section_spans, first_body_snippet)
            else:
                tier, pointer = None, None

            negative_suppressed = False
            if tier == "body_weak" and all_body_hits_are_negative_only and not co_occurring:
                # Only a body-only, single-section, no-co-occurrence match can be
                # suppressed by a negative/ambiguous term. Filename/H1/heading/
                # phrase evidence never reaches this branch.
                negative_suppressed = resolved_signals.get("negative_terms", False)
                if negative_suppressed:
                    tier, pointer = None, None

            if tier is None:
                continue

            partial.append({
                "path": rel,
                "source_id": source_id_for(rel),
                "sha256": facts_by_path.get(rel, {}).get("sha256"),
                "tier": tier,
                "why": {
                    "filename_hit": filename_hit, "h1_hit": h1_hit, "heading_hit": heading_hit,
                    "body_hit_count": body_hit_count, "body_hit_sections": body_hit_sections,
                    "co_occurring_terms": sorted(co_occurring), "negative_suppressed": negative_suppressed,
                },
                "pointers": [pointer] if pointer else [],
            })

        # Reference-graph rescue: a file with zero term-based signal can still
        # surface if it is linked from this topic's strong-tier sources -- but
        # only when the signal is active; it never removes a term-based match.
        strong_paths = {c["path"] for c in partial if c["tier"] in ("filename", "h1", "heading")}
        if resolved_signals.get("reference_graph"):
            already = {c["path"] for c in partial}
            for path in files:
                rel = relpath(kb_root, path)
                if rel in already:
                    continue
                linkers = reverse_links.get(rel, set()) & strong_paths
                if linkers:
                    partial.append({
                        "path": rel, "source_id": source_id_for(rel), "sha256": facts_by_path.get(rel, {}).get("sha256"),
                        "tier": "body_weak",
                        "why": {"filename_hit": [], "h1_hit": [], "heading_hit": [], "body_hit_count": 0,
                                "body_hit_sections": [], "co_occurring_terms": [], "negative_suppressed": False},
                        "pointers": [{"field": "link", "line": 1, "section_span": None, "snippet": f"linked from {len(linkers)} strong-tier source(s) for this topic"}],
                    })

        # Freshness boost (relative to this topic's own candidate set -- never
        # an absolute date constant) and reference-graph score boost.
        dated = sorted(facts_by_path.get(c["path"], {}).get("last_change") for c in partial if facts_by_path.get(c["path"], {}).get("last_change"))
        median_date = dated[len(dated) // 2] if dated else None
        for c in partial:
            fact = facts_by_path.get(c["path"], {})
            boost = 0.0
            if resolved_signals.get("freshness"):
                lc = fact.get("last_change")
                if lc:
                    fboost = 2.0 + (3.0 if median_date and lc > median_date else 0.0)
                    c["why"]["freshness"] = {"last_change": lc, "source": fact.get("last_change_source") or "none", "boost": fboost}
                    boost += fboost
                else:
                    c["why"]["freshness"] = {"last_change": None, "source": "none", "boost": 0.0}
            else:
                c["why"]["freshness"] = None
            if resolved_signals.get("reference_graph"):
                lfs = len(reverse_links.get(c["path"], set()) & strong_paths)
                c["why"]["linked_from_strong"] = lfs
                boost += min(lfs, 5) * 2.0
            else:
                c["why"]["linked_from_strong"] = 0
            if c["why"]["co_occurring_terms"]:
                boost += 5.0
            c["score"] = round(TIER_BASE_SCORE[c["tier"]] + boost, 2)

        # Duplicate collapse (evidence-gated): annotate, never remove a row.
        if resolved_signals.get("duplicate_collapse"):
            by_sha: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
            for c in partial:
                if c["sha256"]:
                    by_sha[c["sha256"]].append(c)
            for sha, members in by_sha.items():
                if len(members) < 2:
                    continue
                members.sort(key=lambda c: (TIER_RANK[c["tier"]], -c["score"], c["path"]))
                representative = members[0]["path"]
                for m in members[1:]:
                    m["duplicate_of"] = representative
        for c in partial:
            c.setdefault("duplicate_of", None)

        partial.sort(key=lambda c: (TIER_RANK[c["tier"]], -c["score"], c["path"]))
        always_include = [c for c in partial if c["tier"] in ("filename", "h1", "heading")]
        body_pool = [c for c in partial if c["tier"] in ("body_strong", "body_weak")]
        cut_idx = elbow_cut_index([c["score"] for c in body_pool])
        held = body_pool[cut_idx:]
        candidate_paths = {c["path"] for c in partial}
        zero_signal_custody = sorted(rel for rel in all_rels if rel not in candidate_paths)

        results[slug] = {
            "schema": TOPIC_SOURCE_RANKINGS_SCHEMA,
            "name": entry.get("name"),
            "vocabulary": vocab,
            "signals_active": resolved_signals,
            "considered_source_count": len(files),
            "candidate_count": len(partial),
            "candidates": partial,
            "gap_cut": {"method": "elbow", "tier_boundary": "body_weak", "included_count": len(always_include) + cut_idx, "held_in_custody_count": len(held)},
            "held_in_custody": [c["source_id"] for c in held],
            "zero_signal_custody": zero_signal_custody,
        }
    return results


TOPIC_WORK_PACK_SCHEMA = "apex.kb.topic-work-pack.v1"
CONTINUE_BY_GAP_INSTRUCTION = (
    "Read the concentrated candidates above first. Pull the next held_in_custody source "
    "(see topic-source-rankings.json for this topic) only if a critical or routine target "
    "question is still unresolved after reading the concentrated set. Stop when every "
    "critical/routine question is resolved, or no further readable source remains. Never "
    "stop merely because a fixed number of sources was read, and never continue merely "
    "because more candidates exist."
)


def build_topic_workpack(entry: Dict[str, Any], ranking: Dict[str, Any]) -> Dict[str, Any]:
    """The bounded L3 packet for one topic: filename/H1/heading tiers in full
    plus the elbow-selected portion of the body tiers, duplicates collapsed to
    one representative. Derived entirely from `ranking` -- never a second
    source of truth for source facts."""
    slug = str(entry.get("slug") or slugify(str(entry.get("name", "unnamed"))))
    name = entry.get("name") or slug
    target_queries = [
        {
            "query_id": q.get("query_id"), "question": q.get("question"), "priority": q.get("priority"),
            "answer_requirements": q.get("answer_requirements", []), "expected_page": q.get("expected_page"),
        }
        for q in topic_queries(entry)
    ]
    candidates = ranking.get("candidates", [])
    held = set(ranking.get("held_in_custody", []))
    concentrated_all = [c for c in candidates if c["source_id"] not in held]
    representatives = [c for c in concentrated_all if not c.get("duplicate_of")]
    rep_paths = {c["path"] for c in representatives}
    dup_map: Dict[str, List[str]] = defaultdict(list)
    standalone_dupes = []
    for c in concentrated_all:
        if c.get("duplicate_of"):
            if c["duplicate_of"] in rep_paths:
                dup_map[c["duplicate_of"]].append(c["source_id"])
            else:
                # Representative itself wasn't concentrated -- keep this one
                # standalone rather than silently losing it.
                standalone_dupes.append(c)
    concentrated = sorted(representatives + standalone_dupes, key=lambda c: (TIER_RANK[c["tier"]], -c["score"], c["path"]))

    json_candidates = [
        {
            "source_id": c["source_id"], "path": c["path"], "tier": c["tier"],
            "why": c["why"], "pointers": c["pointers"],
            "duplicates_of_this": sorted(dup_map.get(c["path"], [])),
        }
        for c in concentrated
    ]
    disclosure = {
        "candidate_count": ranking.get("candidate_count", 0),
        "concentrated_count": len(json_candidates),
        "held_in_custody_count": len(held),
        "zero_signal_custody_count": len(ranking.get("zero_signal_custody", [])),
        "rankings_ref": "manifests/phase0/topic-source-rankings.json",
    }
    payload = {
        "schema": TOPIC_WORK_PACK_SCHEMA, "topic_slug": slug, "topic_name": name,
        "target_queries": target_queries, "concentrated_candidates": json_candidates,
        "continue_by_gap": CONTINUE_BY_GAP_INSTRUCTION, "disclosure": disclosure,
    }
    return {"slug": slug, "json": payload, "markdown": render_topic_workpack_markdown(name, slug, target_queries, json_candidates, disclosure)}


def render_topic_workpack_markdown(name: str, slug: str, target_queries: List[Dict[str, Any]], candidates: List[Dict[str, Any]], disclosure: Dict[str, Any]) -> str:
    lines = [f"# Topic Work Pack - {name}", "", f"Generated: `{utc_now()}`", f"Topic slug: `{slug}`", "Rankings reference: `manifests/phase0/topic-source-rankings.json`", "", "## Target Questions", ""]
    if target_queries:
        for q in target_queries:
            lines.append(f"- `{q['query_id']}` (`{q['priority']}`): {q['question']}")
            reqs = q.get("answer_requirements") or []
            lines.append(f"  - answer requirements: {', '.join(reqs) if reqs else 'none recorded'}")
            lines.append(f"  - expected page: `{q.get('expected_page') or 'NA'}`")
    else:
        lines.append("- none recorded -- compiled tiers require target queries per `references/semantic-value-contract.md`.")
    lines.extend(["", "## Concentrated Candidates", ""])
    tier_titles = {"filename": "Filename matches", "h1": "H1 matches", "heading": "Heading matches", "body_strong": "Body matches (concentrated)", "body_weak": "Body matches (concentrated)"}
    grouped: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for c in candidates:
        grouped[c["tier"]].append(c)
    seen_titles: set = set()
    for tier in ("filename", "h1", "heading", "body_strong", "body_weak"):
        rows = grouped.get(tier, [])
        if not rows:
            continue
        title = tier_titles[tier]
        if title not in seen_titles:
            lines.extend([f"### {title}", ""])
            seen_titles.add(title)
        for c in rows:
            why = c["why"]
            why_bits = []
            if why.get("filename_hit"):
                why_bits.append(f"filename hit on \"{why['filename_hit'][0]}\"")
            if why.get("h1_hit"):
                why_bits.append(f"H1 hit on \"{why['h1_hit'][0]}\"")
            if why.get("heading_hit"):
                why_bits.append(f"heading hit on \"{why['heading_hit'][0]}\"")
            if why.get("body_hit_count"):
                why_bits.append(f"{why['body_hit_count']} body hit(s)")
            if why.get("linked_from_strong"):
                why_bits.append(f"linked from {why['linked_from_strong']} strong source(s)")
            lines.append(f"- `{c['path']}` (`{c['source_id']}`) -- why: {'; '.join(why_bits) if why_bits else 'signal recorded'}")
            for p in c["pointers"]:
                span = f" section {p['section_span'][0]}-{p['section_span'][1]}" if p.get("section_span") else ""
                lines.append(f"  - pointers: `{p['field']}:{p['line']}`{span}: \"{p.get('snippet', '')}\"")
            if c.get("duplicates_of_this"):
                lines.append(f"  - duplicates of this source: {', '.join(f'`{d}`' for d in c['duplicates_of_this'])}")
        lines.append("")
    lines.extend(["## Continue By Gap", "", CONTINUE_BY_GAP_INSTRUCTION, "", "## Disclosure", ""])
    for key in ("candidate_count", "concentrated_count", "held_in_custody_count", "zero_signal_custody_count"):
        lines.append(f"- {key}: `{disclosure[key]}`")
    lines.append(f"- full candidate set and custody paths: `{disclosure['rankings_ref']}`")
    return "\n".join(lines) + "\n"


def corpus_profile(
    kb_root: Path,
    files: List[Path],
    structures: List[Dict[str, Any]],
    term_freq: List[Dict[str, Any]],
    inventory: Optional[Dict[str, Any]] = None,
    hash_groups: Optional[Dict[str, List[str]]] = None,
    normalized_dupe_groups: Optional[List[List[str]]] = None,
    version_families: Optional[List[Dict[str, Any]]] = None,
    signal_availability: Optional[Dict[str, Any]] = None,
    blocked_counts: Optional[Dict[str, int]] = None,
) -> str:
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
    lines.extend(["", "## non_text_and_blocked_files", "", "See `source-facts.json` for the full per-file custody record -- every scanned file is inventoried here, including these.", ""])
    if blocked_counts:
        lines.append(f"- non_text: `{blocked_counts.get('non_text', 0)}`")
        lines.append(f"- unreadable: `{blocked_counts.get('unreadable', 0)}`")
    else:
        lines.append("- none detected")
    lines.extend(["", "## duplicate_hash_groups", ""])
    dupes = [v for v in (hash_groups or {}).values() if len(v) > 1]
    if dupes:
        for group in dupes[:20]:
            lines.append("- " + ", ".join(f"`{x}`" for x in group))
    else:
        lines.append("- none detected")
    lines.extend(["", "## normalized_text_duplicate_groups", "", "Same text once whitespace/case differences are collapsed -- not exact-hash duplicates.", ""])
    if normalized_dupe_groups:
        for group in normalized_dupe_groups[:20]:
            lines.append("- " + ", ".join(f"`{x}`" for x in group))
    else:
        lines.append("- none detected")
    lines.extend(["", "## version_family_candidates", "", "Conservative filename-token grouping (v2, Night4, draft, old/new/final, copy, \"(2)\"). Discovery evidence only -- never auto-resolved supersession.", ""])
    if version_families:
        for fam in version_families[:20]:
            lines.append(f"- `{fam['possible_family_key']}`: " + ", ".join(f"`{m}`" for m in fam["members"]))
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
    lines.extend(["", "## generic_term_frequency", "", "Domain-agnostic word counts across this corpus (standard English stopwords filtered only; no hardcoded topic assumptions).", ""])
    for row in term_freq[:30]:
        lines.append(f"- `{row['term']}`: {row['count']} hits across {row['file_count']} files")
    lines.extend(["", "## optional_signal_availability", "", "Governs which optional Phase 0 signals auto-activate for topic ranking (see `manifests/analysis-config.json`). A signal only turns on when the corpus shows material for it -- never a guess.", ""])
    if signal_availability:
        for key in ("git_history", "frontmatter_dates", "exact_duplicates", "normalized_duplicates", "version_families", "link_density", "negative_terms_declared"):
            if key in signal_availability:
                lines.append(f"- `{key}`: `{signal_availability[key]}`")
        if signal_availability.get("generic_high_freq_terms"):
            lines.append(f"- `generic_high_freq_terms`: " + ", ".join(f"`{t}`" for t in signal_availability["generic_high_freq_terms"]))
    else:
        lines.append("- not_computed")
    return "\n".join(lines) + "\n"


def priority_candidates(kb_root: Path, files: List[Path], structures: List[Dict[str, Any]], file_hit_totals: Dict[str, int]) -> str:
    rows = []
    struct_by_path = {s["path"]: s for s in structures}
    for p in files:
        rel = relpath(kb_root, p)
        s = struct_by_path.get(rel, {})
        score = file_hit_totals.get(rel, 0) // 50 + len(s.get("headings", [])) + min(p.stat().st_size // 20000, 5)
        rows.append((score, rel, p.stat().st_size, len(s.get("headings", [])), file_hit_totals.get(rel, 0)))
    rows.sort(key=lambda x: (-x[0], x[1]))
    lines = ["# Source Priority Candidates", "", "These candidates are deterministic navigation hints, not semantic authority rankings.", "", "| score | path | bytes | headings | term_hits |", "|---:|---|---:|---:|---:|"]
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
- `term-frequency.json`
- `topic-source-rankings.json`
- `source-priority-candidates.md`
- `phase0-navigation-report.md`

## Boundary

This Phase 0 run created deterministic navigation artifacts only. It did not
create Phase 1 semantic analysis, Phase 2 wiki pages, embeddings, vector stores,
Plan/Sync/Session state, PreCap outputs, FlowRecap outputs, or APSU outputs.
"""


PHASE1_INVENTORY_BEGIN = "<!-- BEGIN SOURCE INVENTORY -->"
PHASE1_INVENTORY_END = "<!-- END SOURCE INVENTORY -->"
PHASE1_RECORDS_BEGIN = "<!-- BEGIN PER-SOURCE RECORDS -->"
PHASE1_RECORDS_END = "<!-- END PER-SOURCE RECORDS -->"


def cmd_ingest_phase1(args: argparse.Namespace) -> Dict[str, Any]:
    """Scaffold or extend one topic-scoped Phase 1 shell at
    ingest-analysis/<topic-slug>.analysis.md. One file exists per registry
    topic (never one per source): a first invocation for a topic creates the
    shell with this source as its only inventory row and record; a later
    invocation for the same topic-slug with a different source appends a new
    inventory row and a new per-source record block to the existing file,
    leaving already-present sections untouched. Re-running with a source_id
    already present in the file is a no-op (already_present: true)."""
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    if not args.source_path:
        return {"command": "ingest-phase1", "status": "blocked", "reason": "--source-path is required"}
    if not args.topic_slug:
        return {"command": "ingest-phase1", "status": "blocked", "reason": "--topic-slug is required"}
    src = Path(args.source_path).expanduser().resolve()
    h = hash_path(src)
    source_id = args.source_slug or slugify(src.stem)
    topic_slug = args.topic_slug
    path = kb_root / "ingest-analysis" / f"{topic_slug}.analysis.md"
    existing = read_text(path) if path.exists() else None
    already_present = existing is not None and _phase1_topic_shell_has_source(existing, source_id)
    if already_present:
        text = existing
    elif existing is None:
        text = ingest_analysis_topic_shell(kb_root.name, topic_slug, source_id, args.source_path, h)
    else:
        text = _phase1_append_source_to_topic_shell(existing, source_id, args.source_path, h)
    write = write_text(path, text, kb_root, args.allow_write, dry_run)
    return {
        "command": "ingest-phase1",
        "status": "operator_review_needed",
        "dry_run": dry_run,
        "topic_slug": topic_slug,
        "source_id": source_id,
        "already_present": already_present,
        "analysis_shell": write,
        "required_halt": True,
        "phase_2_requires": PHASE2_APPROVAL,
        "semantic_note": "Shell only; LLM must fill semantic sections from the source.",
    }


def _phase1_topic_shell_has_source(text: str, source_id: str) -> bool:
    return bool(re.search(rf"(?m)^### {re.escape(source_id)} - authority:", text))


def _phase1_source_inventory_row(source_id: str, source_path: str, h: Dict[str, Any]) -> str:
    hash_prefix = str(h.get("source_hash") or "NA")[:8]
    return f"| unranked | {source_id} | {source_path} | unclear | unknown | accepted | {hash_prefix} |"


def _phase1_source_record_block(source_id: str, source_path: str, h: Dict[str, Any]) -> str:
    return f"""### {source_id} - authority: unclear

```yaml
source_identity:
  title: "LLM must fill from source evidence only"
  authority_rationale: "LLM must fill from source evidence only"
  scope: "LLM must fill from source evidence only"
  limitations: []
  read_status: "LLM must fill: complete | targeted | blocked"
  reviewed_passages: []

target_query_coverage: []
topic_completion_effect: "LLM must fill: supports | partial | blocks"

source_summary:
  one_sentence_core: "LLM must fill from source evidence only"
  relevant_to_kb_because: []
  likely_not_relevant_for: []

key_claims: []
concept_candidates: []
entity_candidates: []
uncertainty_triggers: []
```

<!-- source_hash: {h.get('source_hash') or 'NA'} ({h.get('hash_algorithm') or 'NA'}) -->
"""


def ingest_analysis_topic_shell(kb_slug: str, topic_slug: str, source_id: str, source_path: str, h: Dict[str, Any]) -> str:
    """One Phase 1 file per topic (never per source) - see
    references/semantic-value-contract.md and templates/ingest-analysis-template.md."""
    row = _phase1_source_inventory_row(source_id, source_path, h)
    record = _phase1_source_record_block(source_id, source_path, h)
    return f"""---
analysis_id: "{kb_slug}-{topic_slug}-analysis"
kb_slug: "{kb_slug}"
topic_slug: "{topic_slug}"
source_count: 1
created_at: "{utc_now()}"
created_by: "apex-kb"
phase: ingest_phase_1
status: operator_review_needed
required_confirmation_phrase: "approve ingest"
---

# Phase 1 Ingest Analysis - {topic_slug}

One file exists per topic, carrying every source accepted for it - never one file per source.
LLM must fill every section below from source evidence only; do not infer from filenames or
prior summaries. No wiki pages may be generated until the operator replies in a separate turn
with: `approve ingest`.

## 1. Source Inventory

{PHASE1_INVENTORY_BEGIN}
| rank | source_id | source_path | authority | recency | disposition | hash_prefix |
|------|-----------|--------------|-----------|---------|-------------|-------------|
{row}
{PHASE1_INVENTORY_END}

## 2. Per-Source Records (accepted sources only)

{PHASE1_RECORDS_BEGIN}
{record}
{PHASE1_RECORDS_END}

## 3. Cross-Source Synthesis Notes

LLM must fill: conflicts between sources, which claim wins by authority, which claims survived
reconciliation and which were discarded and why, and outstanding topic-completion blockers.
Reference claim IDs and source_ids inline.

## 4. Concept Candidate Shortlist

| concept_slug | concept_label | source_ids | disposition |
|---|---|---|---|

## 5. Entity Candidate Shortlist

| entity_slug | entity_label | entity_type | source_ids |
|---|---|---|---|

## 6. Proposed Phase 2 Changes

```yaml
proposed_wiki_pages:
  summaries: []
  concepts: []
  entities: []
audit_items: []
manifest_updates: []
```

## 7. Compile Decision

```yaml
compile_decision:
  status: operator_review_needed
  phase_2_ready: false
  unresolved_priority_query_ids: []
  additional_sources_to_read: []
  truthful_state_if_stopped: "analysis_complete_unvalidated"
```

## Operator Gate

```yaml
phase_2_allowed: false
required_confirmation_phrase: "approve ingest"
```
"""


def _phase1_append_source_to_topic_shell(existing: str, source_id: str, source_path: str, h: Dict[str, Any]) -> str:
    row = _phase1_source_inventory_row(source_id, source_path, h)
    record = _phase1_source_record_block(source_id, source_path, h)
    text = existing
    if PHASE1_INVENTORY_END in text:
        text = text.replace(PHASE1_INVENTORY_END, f"{row}\n{PHASE1_INVENTORY_END}", 1)
    if PHASE1_RECORDS_END in text:
        text = text.replace(PHASE1_RECORDS_END, f"{record}\n{PHASE1_RECORDS_END}", 1)
    count = len(re.findall(r"(?m)^### \S+ - authority:", text))
    text = re.sub(r'(?m)^source_count: \d+$', f"source_count: {count}", text, count=1)
    return text


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


def topic_guides_lines(kb_root: Path) -> List[str]:
    registry = load_topic_registry(kb_root)
    if not registry:
        return []
    lines = ["## Topic Guides", ""]
    for entry in sorted(registry, key=lambda e: str(e.get("name", ""))):
        name = entry.get("name", "Untitled topic")
        target = entry.get("target_page")
        status = entry.get("status", "not_started")
        source = entry.get("source", "unknown")
        if target:
            rel_link = str(target).replace("wiki/", "", 1)
            lines.append(f"- [{name}]({rel_link}) - `{status}` / `{source}`")
        else:
            lines.append(f"- {name} - `{status}` / `{source}` (no page yet)")
    lines.append("")
    return lines


def machine_index_section(kb_root: Path) -> str:
    pages = [p for p in wiki_pages(kb_root) if p.name != "index.md"]
    by_type: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for p in pages:
        row = page_row(kb_root, p)
        by_type[row["page_type"]].append(row)
    lines = [AUTO_BEGIN, "", f"Generated: `{utc_now()}`", "", f"Compiled page count: `{len(pages)}`", ""]
    lines.extend(topic_guides_lines(kb_root))
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


def semantic_acceptance_status(kb_root: Path) -> Dict[str, Any]:
    root = kb_root / "audit" / "semantic-acceptance"
    registry = load_topic_registry(kb_root)
    required_topics = {
        str(topic.get("slug") or slugify(str(topic.get("name", "topic")))): topic
        for topic in registry
        if isinstance(topic, dict) and any(str(query.get("priority")) in {"critical", "routine"} for query in topic_queries(topic))
    }
    files = sorted(root.rglob("*.json")) if root.exists() else []
    topic_verdicts: Dict[str, str] = {}
    issues: List[Dict[str, Any]] = []
    query_map = registry_query_map(kb_root)

    for path in files:
        rel = relpath(kb_root, path)
        try:
            artifact = json.loads(read_text(path))
        except (OSError, json.JSONDecodeError) as exc:
            issues.append({"path": rel, "issue": "invalid_json", "detail": str(exc)})
            continue
        if not isinstance(artifact, dict) or artifact.get("schema") != SEMANTIC_ACCEPTANCE_SCHEMA:
            issues.append({"path": rel, "issue": "invalid_schema"})
            continue
        topic_slug = str(artifact.get("topic_slug") or "").strip()
        if not topic_slug:
            issues.append({"path": rel, "issue": "missing_topic_slug"})
            continue
        query_results = artifact.get("query_results")
        claim_reviews = artifact.get("claim_reviews")
        verdict = str(artifact.get("verdict") or "")
        if not isinstance(query_results, list) or not isinstance(claim_reviews, list) or verdict not in {"semantic_pass", "semantic_partial", "semantic_fail", "insufficient_evidence"}:
            issues.append({"path": rel, "topic_slug": topic_slug, "issue": "incomplete_artifact"})
            topic_verdicts[topic_slug] = "semantic_partial"
            continue
        results_by_id = {str(item.get("query_id")): item for item in query_results if isinstance(item, dict)}
        for query_id, query in query_map.items():
            if query.get("topic_slug") != topic_slug or str(query.get("priority")) not in {"critical", "routine"}:
                continue
            item = results_by_id.get(query_id)
            if not item:
                issues.append({"path": rel, "topic_slug": topic_slug, "query_id": query_id, "issue": "missing_query_result"})
            elif item.get("result") != "answerable":
                issues.append({"path": rel, "topic_slug": topic_slug, "query_id": query_id, "issue": "priority_query_not_answerable", "result": item.get("result")})
            for pointer in item.get("page_pointers", []) if isinstance(item, dict) else []:
                page_rel = str(pointer).split("#", 1)[0]
                if page_rel and not (kb_root / page_rel).exists():
                    issues.append({"path": rel, "topic_slug": topic_slug, "query_id": query_id, "issue": "page_pointer_missing", "pointer": pointer})
        if not claim_reviews:
            issues.append({"path": rel, "topic_slug": topic_slug, "issue": "missing_claim_reviews"})
        elif any(not isinstance(item, dict) or item.get("result") != "supported" for item in claim_reviews):
            issues.append({"path": rel, "topic_slug": topic_slug, "issue": "claim_not_supported"})
        topic_issues = [issue for issue in issues if issue.get("topic_slug") == topic_slug]
        topic_verdicts[topic_slug] = verdict if not topic_issues else ("semantic_fail" if verdict == "semantic_fail" else "semantic_partial")

    missing_topics = sorted(set(required_topics) - set(topic_verdicts))
    for topic_slug in missing_topics:
        issues.append({"topic_slug": topic_slug, "issue": "missing_acceptance_artifact"})

    if not files:
        status = "missing"
    elif any(verdict == "semantic_fail" for verdict in topic_verdicts.values()):
        status = "fail"
    elif issues or missing_topics or any(topic_verdicts.get(topic) != "semantic_pass" for topic in required_topics):
        status = "partial"
    else:
        status = "pass"
    return {"status": status, "schema": SEMANTIC_ACCEPTANCE_SCHEMA, "required_topics": sorted(required_topics), "topics": topic_verdicts, "artifact_count": len(files), "issues": issues}


def cmd_semantic_acceptance_status(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    result = {"command": "semantic-acceptance-status"}
    result.update(semantic_acceptance_status(kb_root))
    return result


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
        "topic_registry_summary": topic_registry_summary(kb_root),
        "semantic_contract_status": "current" if (kb_root / "semantic-contract" / "semantic-execution-contract.md").exists() else "legacy_missing_repository_contract",
        "semantic_acceptance_status": semantic_acceptance_status(kb_root),
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
    # Retrieval intentionally excludes the machine-maintained wiki index;
    # status must compare the same page set as the retrieval builder.
    current = {relpath(kb_root, page): sha256_file(page) for page in wiki_pages(kb_root) if page.name != "index.md"}
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


def _frontmatter_scalar_list(raw: str, field: str) -> List[str]:
    lines = raw.splitlines()
    if not lines or lines[0].strip().lstrip("\ufeff") != "---":
        return []
    end = next((index for index, line in enumerate(lines[1:], start=1) if line.strip().lstrip("\ufeff") == "---"), None)
    if end is None:
        return []
    front = "\n".join(lines[1:end])
    inline = re.search(rf"(?m)^{re.escape(field)}:\s*\[([^\]]*)\]\s*$", front)
    if inline:
        return [strip_scalar(item.strip()) for item in inline.group(1).split(",") if item.strip()]
    block = re.search(rf"(?m)^{re.escape(field)}:[ \t]*$\n((?:[ \t]*-[ \t]+.*\n?)*)", front)
    if not block:
        return []
    return [str(strip_scalar(item.strip())) for item in re.findall(r"(?m)^[ \t]*-[ \t]+(.+?)[ \t]*$", block.group(1))]


def _analysis_files(kb_root: Path) -> List[Path]:
    root = kb_root / "ingest-analysis"
    return sorted(path for path in root.rglob("*.md") if path.is_file()) if root.exists() else []


def _source_has_analysis(kb_root: Path, source: str) -> bool:
    needle = source.strip()
    if not needle:
        return False
    return any(needle in read_text(path) for path in _analysis_files(kb_root))


def _phase1_analysis_files_referencing_source(kb_root: Path, source_slug: str) -> List[str]:
    """Find ingest-analysis files that already cover source_slug, under either shape:
    a topic-scoped file with a `### <source_slug> - authority:` per-source record, or a
    legacy pre-migration file named `<source_slug>.analysis.md` / `<source_slug>*.analysis.md`."""
    if not source_slug:
        return []
    heading_pattern = re.compile(rf"(?m)^### {re.escape(source_slug)}\b.*-\s*authority:")
    found: List[Path] = []
    for path in _analysis_files(kb_root):
        if heading_pattern.search(read_text(path)) or path.name.startswith(f"{source_slug}."):
            found.append(path)
    return [relpath(kb_root, p) for p in found]


def candidate_disposition_findings(kb_root: Path) -> List[Dict[str, Any]]:
    findings: List[Dict[str, Any]] = []
    for path in _analysis_files(kb_root):
        text = read_text(path)
        candidates = len(re.findall(r"(?m)^\s*-\s+(?:concept_slug|entity_slug):", text))
        dispositions = len(re.findall(r"(?m)^\s+disposition:\s*(?:promote|embed_in_summary|defer_blocked|reject_no_independent_value)\s*$", text))
        if candidates > dispositions:
            findings.append({"path": relpath(kb_root, path), "reason": "candidate_promotion_disposition_missing", "candidate_count": candidates, "disposition_count": dispositions})
    return findings


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
    # Human-readable v2 claims may carry resolved evidence inline in
    # parenthetical source-and-section form rather than YAML pointer keys.
    result["section_level"] += len(re.findall(
        r"\((?:LOCAL-|SRC-)[A-Za-z0-9._-]+,\s*[^)]+\)",
        body or "",
        flags=re.IGNORECASE,
    ))
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
    contract_version = str(meta.get("semantic_contract_version") or "")
    is_v2_contract = contract_version in {SEMANTIC_CONTRACT_VERSION, "2.0"}
    target_query_ids = [str(item) for item in _frontmatter_scalar_list(raw, "target_query_ids")]
    known_queries = registry_query_map(kb_root)

    sections = {heading: _quality_section(body, heading) for heading in PHASE2_VALUE_HEADINGS}
    macro_block = sections.get("Macro / Meso / Micro", "")
    section_words = {heading: _quality_words(text) for heading, text in sections.items()}
    section_words.update({
        "Macro": _quality_words(_quality_section(macro_block, "Macro", level="###")),
        "Meso": _quality_words(_quality_section(macro_block, "Meso", level="###")),
        "Micro": _quality_words(_quality_section(macro_block, "Micro", level="###")),
    })

    refs = extract_source_refs(meta)
    key_claims = len(re.findall(
        r"(?:^|\n)\s*-\s+(?:(?:claim_id|claim)\s*:|\*\*[A-Za-z0-9][A-Za-z0-9._-]*:\*\*)",
        sections.get("Key Claims", ""),
        flags=re.IGNORECASE,
    ))
    ranked_sources = len(re.findall(
        r"(?:^|\n)\s*-\s+(?:(?:rank|source|source_id|source_path)\s*:|\*\*[^*]+\*\*)",
        sections.get("Adaptive Ranked Source Set", ""),
        flags=re.IGNORECASE,
    ))
    routes_section = sections.get("Routes Here", "")
    routes = len(re.findall(r"(?:^|\n)\s*-\s+(?:question\s*:|leads_to\s*:)", routes_section, flags=re.IGNORECASE))
    if routes == 0:
        routes = len(re.findall(r"\[[^\]]+\]\([^)]+\.md(?:#[^)]+)?\)", routes_section))
    uncertainty_items = len(re.findall(r"(?:^|\n)\s*-\s+id\s*:", sections.get("Uncertainty / Raw Source Reopen Triggers", ""), flags=re.IGNORECASE))
    pointer_specificity = _pointer_specificity(sections.get("Key Claims", ""))
    pointer_count = sum(pointer_specificity.values())
    placeholders = sorted(set(re.findall(r"<[^>]{3,80}>|\b(?:TODO|TBD|LLM must fill)\b", body, flags=re.IGNORECASE)))
    missing_headings = [h for h in PHASE2_VALUE_HEADINGS if not has_markdown_heading(body, h)]

    reasons: List[str] = []
    if page_type in VALUE_PAGE_TYPES:
        if not is_v2_contract:
            reasons.append("legacy_semantic_contract")
        if is_v2_contract and not target_query_ids:
            reasons.append("missing_target_queries")
        if any(query_id not in known_queries for query_id in target_query_ids):
            reasons.append("unknown_target_query_id")
        if target_query_ids and not all(query_id in sections.get("Target Questions Answered", "") for query_id in target_query_ids):
            reasons.append("target_query_route_missing")
        for query_id in target_query_ids:
            expected_page = str(known_queries.get(query_id, {}).get("expected_page") or "").split("#", 1)[0]
            # The registry route is the primary answer page. Concepts and entities
            # may materially support the same query without replacing that route.
            if expected_page and not (kb_root / expected_page).exists():
                reasons.append("target_query_route_missing")
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
            elif not is_v2_contract and page_type == "concept" and key_claims < 2 and all_layers_thin:
                reasons.append("single_claim_concept_thin")
        specific_pointer_count = pointer_specificity["section_level"] + pointer_specificity["line_or_span_level"]
        if not is_v2_contract and page_type == "concept" and section_words.get("Micro", 0) < SECTION_WORD_FLOOR and specific_pointer_count == 0:
            reasons.append("concept_micro_not_evidenced")
        # Narrow named entities may validly be concise with one claim and one
        # source (kb-contract.md concise_policy) - only flag entities for a
        # missing claim outright, never for thin/single-claim synthesis depth.
        # Unlike the legacy-only checks above, the Macro/Meso/Micro word floor
        # applies on v2 pages too: v2's Why/What/How semantic (see
        # semantic-value-contract.md) has a defined content target, so
        # thinness is a real defect there, not an artifact of the old
        # undefined-semantic contract this guard originally protected against.
        if all_layers_thin and page_type != "entity":
            reasons.append("thin_macro_meso_micro")
        if not is_v2_contract and page_type == "summary" and ranked_sources < 2:
            reasons.append("summary_source_breadth_below_profile")
        if routes == 0:
            reasons.append("no_query_routes")
        if re.search(r"availability_class:\s*[\"']?readable_unopened", sections.get("Uncertainty / Raw Source Reopen Triggers", ""), flags=re.IGNORECASE) and re.search(r"completion_effect:\s*[\"']?blocks_priority_query", sections.get("Uncertainty / Raw Source Reopen Triggers", ""), flags=re.IGNORECASE):
            reasons.append("readable_unopened_source_blocks_completion")

        ranked = sections.get("Adaptive Ranked Source Set", "")
        ranked_ids = [value.strip() for value in re.findall(r"(?m)^\s+-\s+(?:source_id|source_path):\s*[\"']?([^\n\"']+)", ranked)]
        ranked_ids.extend(value.strip() for value in re.findall(r"(?m)^\s*-\s+\*\*([^*]+)\*\*", ranked))
        for source in ranked_ids:
            if source not in refs:
                reasons.append("ranked_source_not_in_source_refs")
            if not _source_has_analysis(kb_root, source):
                reasons.append("ranked_source_not_analyzed")
        if ranked_ids and not (
            re.search(r"(?m)^\s+claim_ids:\s*(?:\[(?!\s*\])|$)", ranked)
            or re.search(r"(?i)\bclaims?\s+[A-Za-z0-9]", ranked)
            or re.search(r"\b[A-Z][A-Z0-9]+(?:-V\d+)?-C\d+\b", ranked)
        ):
            reasons.append("ranked_source_without_claim_use")
        if any(not _source_has_analysis(kb_root, source) for source in refs):
            reasons.append("source_ref_without_phase1_evidence")

    return {
        "path": relpath(kb_root, page),
        "page_type": page_type,
        "semantic_contract_version": contract_version or None,
        "target_query_ids": target_query_ids,
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
    acceptance = semantic_acceptance_status(kb_root)
    disposition_findings = candidate_disposition_findings(kb_root)
    global_findings: List[Dict[str, Any]] = list(disposition_findings)
    has_compiled_value_pages = any(item.get("page_type") in VALUE_PAGE_TYPES for item in metrics)
    if has_compiled_value_pages and acceptance["status"] == "missing":
        global_findings.append({"reason": "semantic_acceptance_missing"})
    elif has_compiled_value_pages and acceptance["status"] != "pass":
        global_findings.append({"reason": "semantic_acceptance_incomplete", "status": acceptance["status"]})
    for topic in load_topic_registry(kb_root):
        if not isinstance(topic, dict):
            continue
        queries = topic_queries(topic)
        if topic.get("status") == "complete" and (not queries or acceptance["topics"].get(str(topic.get("slug"))) != "semantic_pass"):
            global_findings.append({"reason": "topic_status_inconsistent", "topic": topic.get("slug")})

    return {
        "source_to_page_map": {key: sorted(value) for key, value in sorted(source_to_page_map.items())},
        "page_to_source_map": page_to_source_map,
        "unmanifested_source_refs": unmanifested_source_refs,
        "manifest_sources_without_pages": manifest_sources_without_pages,
        "pages_without_source_refs": pages_without_source_refs,
        "pages_missing_phase2_value_sections": pages_missing_phase2_value_sections,
        "phase2_repair_candidates": candidates,
        "shell_page_candidates": shell_page_candidates,
        "global_findings": global_findings,
        "semantic_acceptance_status": acceptance,
        "page_metrics": metrics,
        "deterministic_only": True,
    }


def topic_registry_summary(kb_root: Path) -> Dict[str, Any]:
    registry = load_topic_registry(kb_root)
    by_status: Counter = Counter(str(e.get("status", "unknown")) for e in registry)
    query_count = sum(len(topic_queries(entry)) for entry in registry if isinstance(entry, dict))
    priority_count: Counter = Counter(str(query.get("priority", "unknown")) for entry in registry if isinstance(entry, dict) for query in topic_queries(entry))
    return {"entries": len(registry), "by_status": dict(by_status), "target_query_count": query_count, "target_queries_by_priority": dict(priority_count)}


def cmd_quality(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    report = quality_report(kb_root)
    result = {"command": "quality"}
    result.update(report)
    has_candidates = bool(report["phase2_repair_candidates"] or report["shell_page_candidates"] or report["global_findings"])
    if getattr(args, "strict", False):
        result["status"] = "fail" if has_candidates else "ok"
    else:
        result["status"] = "ok"
    result["issue_count"] = len(report["phase2_repair_candidates"]) + len(report["global_findings"])
    result["topic_registry_summary"] = topic_registry_summary(kb_root)
    return result


QUERY_EVAL_SCHEMA_V1 = "apex.query_eval_pack.v1"
QUERY_EVAL_SCHEMA = "apex.query_eval_pack.v2"
QUERY_EVAL_LIST_FIELDS = ("expected_routes", "expected_minimal_pages", "raw_source_needed")


def query_eval_pack_path(kb_root: Path) -> Path:
    return kb_root / "outputs/queries/evals/query-eval-pack.json"


def validate_query_eval_pack(pack: Any) -> List[Dict[str, str]]:
    issues: List[Dict[str, str]] = []
    if not isinstance(pack, dict):
        return [{"field": "<root>", "message": "pack must be a JSON object"}]
    schema = pack.get("schema")
    if schema not in {QUERY_EVAL_SCHEMA, QUERY_EVAL_SCHEMA_V1}:
        issues.append({"field": "schema", "message": f"expected {QUERY_EVAL_SCHEMA!r} or legacy {QUERY_EVAL_SCHEMA_V1!r}, got {schema!r}"})
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
        if schema == QUERY_EVAL_SCHEMA:
            for field in ("query_id", "priority", "answer_requirements", "expected_routes", "expected_raw_source_requirement"):
                if field not in entry:
                    issues.append({"field": f"{prefix}.{field}", "message": f"{field} is required for v2"})
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
        result["schema"] = pack.get("schema")
        result["migration_required"] = pack.get("schema") == QUERY_EVAL_SCHEMA_V1
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

    initial_queries: List[Dict[str, Any]] = []
    for topic in load_topic_registry(kb_root):
        if not isinstance(topic, dict):
            continue
        for query in topic_queries(topic):
            expected_page = str(query.get("expected_page") or topic.get("target_page") or "").strip()
            initial_queries.append({
                "query_id": str(query.get("query_id") or ""),
                "query": str(query.get("question") or ""),
                "priority": str(query.get("priority") or "supporting"),
                "answer_requirements": [str(item) for item in query.get("answer_requirements", [])],
                "expected_routes": [expected_page] if expected_page else [],
                "expected_minimal_pages": [expected_page] if expected_page else [],
                "raw_source_needed": [],
                "expected_raw_source_requirement": "not_required",
            })
    initial_pack = {"schema": QUERY_EVAL_SCHEMA, "kb_slug": kb_root.name, "queries": initial_queries}
    write_result = write_text(pack_path, json.dumps(initial_pack, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run)
    result.update({"status": "initialized", "schema": QUERY_EVAL_SCHEMA, "write_result": write_result, "issue_count": 0, "issues": [], "query_count": len(initial_queries)})
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


def audit_repair_candidate_body(kb_slug: str, target_rel: str, reasons: List[str]) -> str:
    reasons_yaml = "\n".join(f"  - {r}" for r in reasons) or "  - unspecified"
    return f"""---
title: "Repair candidate: {target_rel}"
page_type: audit_item
kb_slug: "{kb_slug}"
source_refs: []
created_at: "{utc_now()}"
updated_at: "{utc_now()}"
confidence: "unknown"
claim_label: "source_backed_summary"
status: "needs_review"
---

# Repair candidate: {target_rel}

```yaml
target_page: "{target_rel}"
residual_reasons:
{reasons_yaml}
retries_exhausted: true
completion_state_cap: partial
```

This page failed `quality --strict` after the bounded 2-redraft Phase 2 compile loop (see `SKILL.md`). It must not be promoted to `query_ready` until these reasons are resolved; move this file to `audit/resolved/` once fixed.
"""


def cmd_flag_repair_candidate(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    if not args.path:
        return {"command": "flag-repair-candidate", "status": "blocked", "reason": "--path is required"}
    reasons = [r.strip() for r in (args.reasons or "").split(",") if r.strip()]
    if not reasons:
        return {"command": "flag-repair-candidate", "status": "blocked", "reason": "--reasons is required (comma-separated reason codes)"}
    slug = slugify(Path(args.path).stem)
    audit_path = kb_root / "audit" / f"repair-candidate-{slug}.md"
    body = audit_repair_candidate_body(kb_root.name, args.path, reasons)
    write = write_text(audit_path, body, kb_root, args.allow_write, dry_run)
    return {"command": "flag-repair-candidate", "dry_run": dry_run, "status": "flagged", "target_page": args.path, "reasons": reasons, "audit_write": write, "completion_state_cap": "partial"}


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


_CONTROL_MODULE: Any = None


def _control_module() -> Any:
    global _CONTROL_MODULE
    if _CONTROL_MODULE is not None:
        return _CONTROL_MODULE
    path = Path(__file__).resolve().with_name("apex_kb_control.py")
    spec = importlib.util.spec_from_file_location("apex_kb_control", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load Apex KB control plane: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _CONTROL_MODULE = module
    return module


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

    semantic_result, semantic_internal = _postflight_call("semantic-acceptance-status", cmd_semantic_acceptance_status, shared)
    steps.append(_postflight_step("semantic_acceptance", True, semantic_result))
    semantic_pass = semantic_result.get("status") == "pass"
    blocking_failed = blocking_failed or not semantic_pass
    internal_error = internal_error or semantic_internal

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
        "semantic_acceptance": semantic_result.get("status"),
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

    control_cmd = sub.add_parser("control", help="Canonical run-state, stage orchestration, semantic packets, recovery, and Git classification")
    _control_module().configure_parser(control_cmd)

    sc = sub.add_parser("scaffold")
    sc.add_argument("--title")
    sc.add_argument("--topic-title")
    sc.add_argument("--force", action="store_true")
    sc.set_defaults(func=cmd_scaffold)

    si = sub.add_parser("source-intake")
    si.add_argument("--source-path")
    si.add_argument("--source-root", help="Recursively intake eligible files from a source directory")
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

    tsc = sub.add_parser("topic-sanity-check")
    tsc.add_argument("--topic-slug", help="Registered topic slug to check")
    tsc.add_argument("--phrase", action="append", help="Additional topic phrase/alias to check; repeatable. Required if --topic-slug is not yet registered.")
    tsc.add_argument("--search-root", help="Root for the bounded filename scan; defaults to the KB root's parent directory")
    tsc.add_argument("--search-cap", type=int, help="Max files visited by the filename scan; default 2000")
    tsc.set_defaults(func=cmd_topic_sanity_check)

    sub.add_parser("phase0").set_defaults(func=cmd_phase0)

    ip1 = sub.add_parser("ingest-phase1")
    ip1.add_argument("--source-path", required=True)
    ip1.add_argument("--topic-slug", required=True, help="Registry topic slug; matches wiki/summaries/<topic-slug>.md")
    ip1.add_argument("--source-slug", help="This source's source_id within the topic file; defaults to a slug of the filename")
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
    audit_cmd = sub.add_parser("audit")
    audit_cmd.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
    audit_cmd.set_defaults(func=cmd_audit)
    frc = sub.add_parser("flag-repair-candidate", help="Write an audit item for a page that failed quality after the bounded retry loop")
    frc.add_argument("--path", required=True, help="KB-relative path of the page that failed, e.g. wiki/summaries/x.md")
    frc.add_argument("--reasons", required=True, help="Comma-separated residual reason codes from quality --strict")
    frc.add_argument("--json", action="store_true", default=argparse.SUPPRESS)
    frc.set_defaults(func=cmd_flag_repair_candidate)
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
    semantic_cmd = sub.add_parser("semantic-acceptance-status", help="Validate repository-authored semantic acceptance artifacts without running an LLM")
    semantic_cmd.set_defaults(func=cmd_semantic_acceptance_status)
    graph_cmd = sub.add_parser("graph", aliases=["process-graph"], help="Extract process-flow graph")
    graph_cmd.set_defaults(func=cmd_graph)
    sub.add_parser("postflight", help="Run the bounded deterministic completion aggregate, including semantic-acceptance status").set_defaults(func=cmd_postflight)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = normalize_global_flag_placement(list(argv) if argv is not None else sys.argv[1:])
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.kb_root:
        parser.error("--kb-root is required")
    try:
        control = _control_module()
        if args.command == "control":
            result = control.dispatch(args, globals())
        else:
            guarded = control.guard_direct_command(args)
            result = guarded if guarded is not None else args.func(args)
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
