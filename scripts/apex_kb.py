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
PHASE0_DIR = Path("manifests/phase0")
WIKI_REQUIRED_FIELDS = ["title", "page_type", "kb_slug", "source_refs", "created_at", "updated_at", "confidence", "claim_label", "status"]
CONFIDENCE_ALLOWED = {"high", "medium", "low", "mixed", "unknown"}
CLAIM_LABEL_ALLOWED = {"raw_source", "source_backed_summary", "behavioral_inference", "working_hypothesis", "operator_question", "practitioner_question"}
STATUS_ALLOWED = {"draft", "active", "needs_review", "deprecated", "superseded"}
PAGE_TYPE_ALLOWED = {"summary", "concept", "entity", "index", "query_output", "audit_item"}
TEXT_EXTS = {".md", ".mdx", ".txt", ".yaml", ".yml", ".json", ".csv", ".py", ".toml"}
RAW_SUBDIRS = ["raw/articles", "raw/papers", "raw/notes", "raw/refs", "raw/other"]
REQUIRED_DIRS = RAW_SUBDIRS + ["ingest-analysis", "wiki/concepts", "wiki/entities", "wiki/summaries", "manifests", "manifests/phase0", "derived/search", "audit/resolved", "outputs/queries", "log"]
REQUIRED_FILES = ["README.md", "kb-schema.md", "wiki/index.md", "manifests/source-manifest.json"]


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
    if not lines or lines[0].strip() != "---":
        return {}, markdown, "missing"
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
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
    roots = [kb_root / "raw"]
    files: List[Path] = []
    for root in roots:
        if root.exists():
            for p in sorted(root.rglob("*")):
                if p.is_file() and p.suffix.lower() in TEXT_EXTS:
                    files.append(p)
    return files


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
    files = iter_source_files(kb_root)
    structures = [parse_markdown_structure(p, kb_root) for p in files]
    heading_map = [{"path": r["path"], "source_type_guess": r["source_type_guess"], "h1_title": r["h1_title"], "headings": r["headings"], "parser_warnings": r["parser_warnings"]} for r in structures]
    link_map = [{"path": r["path"], "markdown_links": r["markdown_links"], "wikilinks": r["wikilinks"]} for r in structures]
    frontmatter_map = [{"path": r["path"], **r["frontmatter"]} for r in structures]
    keyword_hits, topic_map = keyword_artifacts(kb_root, files)
    profile = corpus_profile(kb_root, files, structures, keyword_hits)
    priority = priority_candidates(kb_root, files, structures, keyword_hits)
    report = phase0_report(kb_root, files, structures)
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
    return {"command": "phase0", "dry_run": dry_run, "source_file_count": len(files), "artifact_count": len(writes), "writes": writes, "phase_boundary": "no ingest-analysis, wiki semantic pages, embeddings, or vector stores created"}


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


def corpus_profile(kb_root: Path, files: List[Path], structures: List[Dict[str, Any]], hits: List[Dict[str, Any]]) -> str:
    ext_counts = Counter(p.suffix.lower() or "[none]" for p in files)
    sizes = [(relpath(kb_root, p), p.stat().st_size) for p in files]
    sizes.sort(key=lambda x: x[1], reverse=True)
    warnings = Counter(w for s in structures for w in s.get("parser_warnings", []))
    noise = [path for path, size in sizes if size > 1_000_000 or any(part in path.lower() for part in ["node_modules", "dist/", "build/", "vendor/"])]
    lines = ["# Phase 0 Corpus Profile", "", f"Generated: `{utc_now()}`", "", "## source_inventory_status", "", f"- Files scanned: `{len(files)}`", f"- Total bytes: `{sum(size for _, size in sizes)}`", "", "## file_count_by_extension", ""]
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
    stale = stale_index_status(kb_root)
    if stale != "fresh":
        issues.append({"type": "index", "issue": stale})
    severity = "fail" if issues and args.strict else "warn" if issues else "pass"
    return {"command": "lint", "status": severity, "issue_count": len(issues), "issues": issues, "deterministic_only": True}


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
        "index_status": stale_index_status(kb_root),
        "phase0_artifacts_present": (kb_root / PHASE0_DIR / "phase0-navigation-report.md").exists(),
        "search_index_present": (kb_root / "derived/search/index-meta.json").exists(),
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
    parser = argparse.ArgumentParser(description="Apex KB deterministic lifecycle helper")
    parser.add_argument("--kb-root", required=True, help="Path to one KB root, e.g. apex-meta/kb/<kb-slug>/")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Preview writes even when --allow-write is present")
    parser.add_argument("--allow-write", action="store_true", help="Permit deterministic writes inside kb_root")
    parser.add_argument("--strict", action="store_true", help="Treat lint warnings as failure")
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
    lint_cmd.add_argument("--strict", action="store_true", default=argparse.SUPPRESS)
    lint_cmd.set_defaults(func=cmd_lint)
    sub.add_parser("audit").set_defaults(func=cmd_audit)
    sub.add_parser("status").set_defaults(func=cmd_status)
    sub.add_parser("health").set_defaults(func=cmd_health)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = args.func(args)
        emit(args, result)
        status = result.get("status") if isinstance(result, dict) else None
        return 2 if status in {"blocked", "fail", "error"} else 0
    except SystemExit:
        raise
    except Exception as exc:
        emit(args, {"command": getattr(args, "command", "unknown"), "status": "error", "error": str(exc)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
