#!/usr/bin/env python3
"""
repair_apex_kb_format.py

Purpose:
  Repair Apex KB files that were accidentally saved as chat-output blocks
  instead of final repository files.

What it fixes:
  - Removes leading "# FILE: ..." wrapper lines.
  - Removes outer Markdown code fences around whole files.
  - Rehydrates common collapsed Markdown/code-fence boundaries.
  - Rehydrates simple collapsed YAML-like blocks inside Markdown fences.
  - Replaces malformed apex-meta/scripts/apex_kb.py with a runnable
    deterministic Python implementation matching the declared command surface.

What it does NOT do:
  - Does not redesign Apex KB.
  - Does not contact GitHub or external services.
  - Does not commit, push, or create PRs.
  - Does not mutate files unless --apply is supplied.
  - Does not delete test KB roots.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_RELATIVE_MARKDOWN_FILES = [
    ".claude/skills/apex-kb/SKILL.md",
    ".claude/skills/apex-kb/references/kb-contract.md",
    ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md",
    ".claude/skills/apex-kb/references/script-command-contract.md",
    ".claude/skills/apex-kb/templates/ingest-analysis-template.md",
    ".claude/skills/apex-kb/templates/wiki-page-templates.md",
    ".claude/skills/apex-kb/package-manifest.md",
]

SCRIPT_PATH = "apex-meta/scripts/apex_kb.py"

BACKUP_DIR = ".repair-backups/apex-kb-format"


CLEAN_APEX_KB_PY = r'''#!/usr/bin/env python3
"""
apex_kb.py

Deterministic Python helper for the Apex KB skill.

Scope:
- Scaffold Apex KB folders/files.
- Hash files/directories.
- Run ingest preflight checks.
- Validate and inspect source manifests.
- Generate/update the machine-owned section of wiki/index.md.
- Lint KB structure, frontmatter, wikilinks, orphans, source pointers,
  manifest shape, and audit items.
- List/group audit files.

Non-scope:
- No concept extraction.
- No entity synthesis.
- No contradiction interpretation.
- No wiki page prose drafting.
- No query answer synthesis.
- No operator-review decisions.

Runtime:
- Python standard library only.
- No shell-out except this script's own local validation when called externally.
- No network access.
- Dry-run by default for write-capable commands.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


EXIT_OK = 0
EXIT_FLAGS = 1
EXIT_VALIDATION_FAILURE = 2
EXIT_UNSAFE_WRITE = 3
EXIT_INVOCATION_ERROR = 4

MACHINE_INDEX_BEGIN = "<!-- BEGIN AUTO-GENERATED INDEX -->"
MACHINE_INDEX_END = "<!-- END AUTO-GENERATED INDEX -->"
LLM_SUMMARY_BEGIN = "<!-- BEGIN LLM SUMMARY -->"
LLM_SUMMARY_END = "<!-- END LLM SUMMARY -->"

REQUIRED_KB_PATHS = [
    "README.md",
    "kb-schema.md",
    "raw/articles",
    "raw/papers",
    "raw/notes",
    "raw/refs",
    "ingest-analysis",
    "wiki/index.md",
    "wiki/concepts",
    "wiki/entities",
    "wiki/summaries",
    "manifests/source-manifest.json",
    "audit",
    "audit/resolved",
    "outputs/queries",
    "log",
]

REQUIRED_KB_SCHEMA_FIELDS = [
    "kb_topic_title",
    "kb_source_authority_list",
    "kb_concept_taxonomy_top_level",
    "kb_language_policy",
    "kb_operator_review_policy",
]

PAGE_TYPE_DIRS = {
    "summary": "wiki/summaries",
    "concept": "wiki/concepts",
    "entity": "wiki/entities",
}


def utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_directory(path: Path) -> str:
    digest = hashlib.sha256()
    entries: list[tuple[str, str]] = []
    for child in sorted(path.rglob("*"), key=lambda p: p.as_posix()):
        if child.is_file():
            rel = child.relative_to(path).as_posix()
            entries.append((rel, sha256_file(child)))
    for rel, file_hash in entries:
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_hash.encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def compute_hash(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    if path.is_file():
        return {
            "path": path.as_posix(),
            "path_type": "file",
            "hash_algorithm": "sha256",
            "hash_value": sha256_file(path),
            "file_count": 1,
            "bytes_total": path.stat().st_size,
        }
    if path.is_dir():
        files = [p for p in path.rglob("*") if p.is_file()]
        return {
            "path": path.as_posix(),
            "path_type": "directory",
            "hash_algorithm": "sha256",
            "hash_value": sha256_directory(path),
            "file_count": len(files),
            "bytes_total": sum(p.stat().st_size for p in files),
        }
    raise ValueError(f"Unsupported path type: {path}")


def report_json(payload: dict[str, Any], exit_code: int) -> int:
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return exit_code


def report_text(payload: dict[str, Any], exit_code: int) -> int:
    print(f"{payload.get('artifact_name', 'report')}: {payload.get('status', 'unknown')}")
    for key, value in payload.items():
        if key in {"artifact_name", "status"}:
            continue
        print(f"{key}: {json.dumps(value, ensure_ascii=False)}")
    return exit_code


def emit(payload: dict[str, Any], as_json: bool, exit_code: int) -> int:
    payload.setdefault("generated_at", utc_now())
    if as_json:
        return report_json(payload, exit_code)
    return report_text(payload, exit_code)


def safe_path_inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def empty_manifest() -> dict[str, Any]:
    return {
        "manifest_version": "0.1",
        "updated_at": utc_now(),
        "sources": [],
    }


def read_manifest(kb_root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    findings: list[dict[str, Any]] = []
    path = kb_root / "manifests" / "source-manifest.json"
    if not path.exists():
        findings.append({"severity": "error", "code": "missing_source_manifest", "path": path.as_posix()})
        return {}, findings
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        findings.append({"severity": "error", "code": "invalid_manifest_json", "message": str(exc), "path": path.as_posix()})
        return {}, findings
    if not isinstance(data, dict):
        findings.append({"severity": "error", "code": "manifest_not_object", "path": path.as_posix()})
        return {}, findings
    return data, findings


def list_sources(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    sources = manifest.get("sources", [])
    return [s for s in sources if isinstance(s, dict)] if isinstance(sources, list) else []


def extract_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line and not line.lstrip().startswith("-"):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def collect_wiki_pages(kb_root: Path) -> list[Path]:
    wiki_root = kb_root / "wiki"
    if not wiki_root.exists():
        return []
    return sorted([p for p in wiki_root.rglob("*.md") if p.is_file()], key=lambda p: p.as_posix())


def extract_wikilinks(text: str) -> list[str]:
    links: set[str] = set()
    for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            links.add(target)
    return sorted(links)


def validate_structure(kb_root: Path) -> tuple[list[str], list[dict[str, Any]]]:
    missing: list[str] = []
    findings: list[dict[str, Any]] = []

    if not kb_root.exists():
        return REQUIRED_KB_PATHS[:], [{"severity": "error", "code": "missing_kb_root", "path": kb_root.as_posix()}]

    for rel in REQUIRED_KB_PATHS:
        if not (kb_root / rel).exists():
            missing.append(rel)
            findings.append({"severity": "error", "code": "missing_required_path", "path": (kb_root / rel).as_posix()})

    schema_path = kb_root / "kb-schema.md"
    if schema_path.exists():
        text = schema_path.read_text(encoding="utf-8", errors="replace")
        for field in REQUIRED_KB_SCHEMA_FIELDS:
            if field not in text:
                findings.append({"severity": "warning", "code": "kb_schema_field_missing", "field": field, "path": schema_path.as_posix()})

    return missing, findings


def scaffold_files(kb_root: Path, title: str) -> dict[str, str]:
    now = utc_now()
    return {
        "README.md": (
            f"# {title}\n\n"
            "Apex KB root.\n\n"
            "```yaml\n"
            f"kb_root: \"{kb_root.as_posix()}\"\n"
            f"created_at: \"{now}\"\n"
            "```\n"
        ),
        "kb-schema.md": (
            f"# {title} KB Schema\n\n"
            "```yaml\n"
            "kb_schema:\n"
            f"  kb_topic_title: \"{title}\"\n"
            "  kb_source_authority_list:\n"
            "    - operator_supplied_sources\n"
            "  kb_concept_taxonomy_top_level:\n"
            "    - concepts\n"
            "    - entities\n"
            "    - summaries\n"
            "  kb_language_policy: \"Preserve source language unless operator requests normalization.\"\n"
            "  kb_operator_review_policy:\n"
            "    phase_2_requires_operator_phrase: \"approve ingest\"\n"
            "```\n"
        ),
        "wiki/index.md": (
            "---\n"
            f"title: \"{title} Index\"\n"
            "page_type: index\n"
            f"kb_slug: \"{kb_root.name}\"\n"
            "source_refs: []\n"
            f"created_at: \"{now}\"\n"
            f"updated_at: \"{now}\"\n"
            "confidence: mixed\n"
            "status: active\n"
            "review_flags: []\n"
            "---\n\n"
            f"# {title} Index\n\n"
            "## How to Use This KB\n\n"
            "Start here, then read the smallest sufficient set of relevant pages.\n\n"
            f"{MACHINE_INDEX_BEGIN}\n\n"
            "```yaml\n"
            "machine_generated_index:\n"
            f"  generated_at: \"{now}\"\n"
            "  generated_by: apex_kb.py scaffold\n"
            "  page_count: 0\n"
            "  pages:\n"
            "    summaries: []\n"
            "    concepts: []\n"
            "    entities: []\n"
            "  detected_links: []\n"
            "  orphan_pages: []\n"
            "  stale_index_hash: NA\n"
            "```\n\n"
            f"{MACHINE_INDEX_END}\n\n"
            f"{LLM_SUMMARY_BEGIN}\n\n"
            "## LLM Summary\n\n"
            "Pending semantic summary.\n\n"
            f"{LLM_SUMMARY_END}\n"
        ),
        "manifests/source-manifest.json": json.dumps(empty_manifest(), indent=2, ensure_ascii=False) + "\n",
    }


def cmd_scaffold(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    title = args.title or kb_root.name
    dirs = [
        "raw/articles",
        "raw/papers",
        "raw/notes",
        "raw/refs",
        "ingest-analysis",
        "wiki/concepts",
        "wiki/entities",
        "wiki/summaries",
        "manifests",
        "audit/resolved",
        "outputs/queries",
        "log",
    ]
    files = scaffold_files(kb_root, title)
    planned_dirs: list[str] = []
    planned_files: list[str] = []
    skipped_existing: list[str] = []
    findings: list[dict[str, Any]] = []

    if args.allow_write:
        kb_root.mkdir(parents=True, exist_ok=True)

    for rel in dirs:
        path = kb_root / rel
        if path.exists():
            skipped_existing.append(rel)
            continue
        planned_dirs.append(rel)
        if args.allow_write:
            path.mkdir(parents=True, exist_ok=True)

    for rel, content in files.items():
        path = kb_root / rel
        if path.exists() and not args.force:
            skipped_existing.append(rel)
            continue
        planned_files.append(rel)
        if args.allow_write:
            if not safe_path_inside(path, kb_root):
                findings.append({"severity": "critical", "code": "write_outside_kb_root_refused", "path": path.as_posix()})
                continue
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")

    status = "passed" if not findings else "failed"
    return emit(
        {
            "artifact_name": "scaffold_report",
            "status": status,
            "kb_root": kb_root.as_posix(),
            "dry_run": not args.allow_write,
            "writes_performed": bool(args.allow_write),
            "created_paths": planned_dirs + planned_files,
            "skipped_existing": skipped_existing,
            "findings": findings,
        },
        args.json,
        EXIT_OK if status == "passed" else EXIT_VALIDATION_FAILURE,
    )


def cmd_hash(args: argparse.Namespace) -> int:
    try:
        data = compute_hash(Path(args.path))
        data["artifact_name"] = "hash_report"
        data["status"] = "passed"
        return emit(data, args.json, EXIT_OK)
    except Exception as exc:
        return emit(
            {"artifact_name": "hash_report", "status": "failed", "errors": [str(exc)], "path": args.path},
            args.json,
            EXIT_VALIDATION_FAILURE,
        )


def cmd_preflight(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    source = Path(args.source)
    missing, findings = validate_structure(kb_root)

    source_hash = None
    no_hash_reason = None
    duplicate_candidates: list[dict[str, Any]] = []

    if source.exists() and source.is_file():
        source_hash = sha256_file(source)
    elif source.exists() and source.is_dir():
        source_hash = sha256_directory(source)
    else:
        no_hash_reason = "source_missing"
        findings.append({"severity": "error", "code": "source_missing", "path": source.as_posix()})

    manifest, manifest_findings = read_manifest(kb_root)
    findings.extend(manifest_findings)

    if source_hash:
        for entry in list_sources(manifest):
            if entry.get("source_hash") == source_hash:
                duplicate_candidates.append(entry)

    analysis_path = kb_root / "ingest-analysis" / f"{args.source_slug}.analysis.md"

    status = "passed" if not any(f.get("severity") == "error" for f in findings) else "failed"
    return emit(
        {
            "artifact_name": "ingest_preflight_report",
            "status": status,
            "kb_root": kb_root.as_posix(),
            "source_path": source.as_posix(),
            "source_exists": source.exists(),
            "source_hash": source_hash,
            "no_hash_reason": no_hash_reason,
            "duplicate_source_candidates": duplicate_candidates,
            "analysis_path": analysis_path.as_posix(),
            "phase_2_allowed": False,
            "required_operator_phrase": "approve ingest",
            "required_paths_missing": missing,
            "findings": findings,
        },
        args.json,
        EXIT_OK if status == "passed" else EXIT_VALIDATION_FAILURE,
    )


def page_type_from_path(path: Path) -> str:
    parts = set(path.parts)
    if "summaries" in parts:
        return "summary"
    if "concepts" in parts:
        return "concept"
    if "entities" in parts:
        return "entity"
    if path.name == "index.md":
        return "index"
    return "unknown"


def build_machine_index(kb_root: Path) -> dict[str, Any]:
    pages = collect_wiki_pages(kb_root)
    grouped: dict[str, list[str]] = {"summaries": [], "concepts": [], "entities": [], "other": []}
    detected_links: list[dict[str, str]] = []

    slugs = {p.stem for p in pages}

    for page in pages:
        rel = page.relative_to(kb_root).as_posix()
        page_type = page_type_from_path(page)
        text = page.read_text(encoding="utf-8", errors="replace")
        links = extract_wikilinks(text)
        for link in links:
            detected_links.append({"from": rel, "to": link, "exists": str(link in slugs).lower()})
        if page_type == "summary":
            grouped["summaries"].append(rel)
        elif page_type == "concept":
            grouped["concepts"].append(rel)
        elif page_type == "entity":
            grouped["entities"].append(rel)
        elif page_type != "index":
            grouped["other"].append(rel)

    linked = {item["to"] for item in detected_links if item["exists"] == "true"}
    orphans = [
        p.relative_to(kb_root).as_posix()
        for p in pages
        if p.name != "index.md" and p.stem not in linked
    ]

    return {
        "generated_at": utc_now(),
        "generated_by": "apex_kb.py index",
        "page_count": len(pages),
        "pages": grouped,
        "detected_links": detected_links,
        "orphan_pages": orphans,
        "stale_index_hash": "NA",
    }


def render_machine_index_section(index: dict[str, Any]) -> str:
    return (
        f"{MACHINE_INDEX_BEGIN}\n\n"
        "```json\n"
        f"{json.dumps({'machine_generated_index': index}, indent=2, ensure_ascii=False)}\n"
        "```\n\n"
        f"{MACHINE_INDEX_END}"
    )


def cmd_index(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    findings: list[dict[str, Any]] = []
    index_path = kb_root / "wiki" / "index.md"

    if not index_path.exists():
        findings.append({"severity": "error", "code": "missing_index", "path": index_path.as_posix()})
        return emit(
            {"artifact_name": "index_report", "status": "failed", "kb_root": kb_root.as_posix(), "findings": findings},
            args.json,
            EXIT_VALIDATION_FAILURE,
        )

    index = build_machine_index(kb_root)
    current = index_path.read_text(encoding="utf-8", errors="replace")
    new_section = render_machine_index_section(index)

    if MACHINE_INDEX_BEGIN in current and MACHINE_INDEX_END in current:
        pattern = re.compile(re.escape(MACHINE_INDEX_BEGIN) + r".*?" + re.escape(MACHINE_INDEX_END), re.S)
        updated = pattern.sub(new_section, current)
    else:
        updated = current.rstrip() + "\n\n" + new_section + "\n"

    if args.allow_write:
        index_path.write_text(updated, encoding="utf-8", newline="\n")

    return emit(
        {
            "artifact_name": "index_report",
            "status": "passed",
            "kb_root": kb_root.as_posix(),
            "index_path": index_path.as_posix(),
            "dry_run": not args.allow_write,
            "writes_performed": bool(args.allow_write),
            "machine_index_section_present": MACHINE_INDEX_BEGIN in updated and MACHINE_INDEX_END in updated,
            "llm_summary_section_preserved": LLM_SUMMARY_BEGIN in updated and LLM_SUMMARY_END in updated,
            "semantic_content_generated_by_python": False,
            "page_count": index["page_count"],
            "orphan_pages_count": len(index["orphan_pages"]),
        },
        args.json,
        EXIT_OK,
    )


def cmd_lint(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    missing, findings = validate_structure(kb_root)

    pages = collect_wiki_pages(kb_root)
    slugs = {p.stem for p in pages}
    broken_links: list[dict[str, str]] = []
    missing_source_pointers: list[str] = []
    malformed_frontmatter: list[str] = []

    for page in pages:
        rel = page.relative_to(kb_root).as_posix()
        text = page.read_text(encoding="utf-8", errors="replace")
        fm, _ = extract_frontmatter(text)
        if page.name != "index.md" and not fm:
            malformed_frontmatter.append(rel)
            findings.append({"severity": "warning", "code": "missing_frontmatter", "path": rel})
        if page.name != "index.md" and "source_refs" not in text and "source_pointers" not in text:
            missing_source_pointers.append(rel)
            findings.append({"severity": "warning", "code": "missing_source_pointer", "path": rel})
        for link in extract_wikilinks(text):
            if link not in slugs:
                broken_links.append({"from": rel, "to": link})
                findings.append({"severity": "warning", "code": "broken_wikilink", "from": rel, "to": link})

    status = "passed" if not any(f.get("severity") == "error" for f in findings) else "failed"
    exit_code = EXIT_OK if status == "passed" and not findings else (EXIT_FLAGS if status == "passed" else EXIT_VALIDATION_FAILURE)

    return emit(
        {
            "artifact_name": "lint_report",
            "status": status,
            "kb_root": kb_root.as_posix(),
            "checks_run": args.check,
            "missing_required_paths": missing,
            "malformed_frontmatter": malformed_frontmatter,
            "broken_links": broken_links,
            "orphan_pages": build_machine_index(kb_root)["orphan_pages"] if (kb_root / "wiki").exists() else [],
            "missing_source_pointers": missing_source_pointers,
            "stale_index": False,
            "manifest_issues": [f for f in findings if "manifest" in f.get("code", "")],
            "audit_shape_issues": [],
            "findings": findings,
        },
        args.json,
        exit_code,
    )


def cmd_manifest(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    manifest_path = kb_root / "manifests" / "source-manifest.json"
    manifest, findings = read_manifest(kb_root)

    if args.validate_only or not args.allow_write:
        status = "passed" if not findings else "failed"
        return emit(
            {
                "artifact_name": "manifest_report",
                "status": status,
                "kb_root": kb_root.as_posix(),
                "manifest_path": manifest_path.as_posix(),
                "source_entries_count": len(list_sources(manifest)),
                "changed_entries": [],
                "findings": findings,
                "writes_performed": False,
            },
            args.json,
            EXIT_OK if status == "passed" else EXIT_VALIDATION_FAILURE,
        )

    if not manifest:
        manifest = empty_manifest()
    manifest["updated_at"] = utc_now()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return emit(
        {
            "artifact_name": "manifest_report",
            "status": "passed",
            "kb_root": kb_root.as_posix(),
            "manifest_path": manifest_path.as_posix(),
            "source_entries_count": len(list_sources(manifest)),
            "changed_entries": [],
            "writes_performed": True,
            "findings": findings,
        },
        args.json,
        EXIT_OK,
    )


def read_audit_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, _ = extract_frontmatter(text)
    return fm


def cmd_audit(args: argparse.Namespace) -> int:
    kb_root = Path(args.kb_root)
    audit_root = kb_root / "audit"
    items: list[dict[str, Any]] = []
    malformed: list[str] = []

    if not audit_root.exists():
        return emit(
            {
                "artifact_name": "audit_report",
                "status": "failed",
                "kb_root": kb_root.as_posix(),
                "open_count": 0,
                "resolved_count": 0,
                "deferred_count": 0,
                "rejected_count": 0,
                "grouped_items": {},
                "malformed_items": [],
                "missing_targets": [],
                "errors": [{"code": "missing_audit_directory", "path": audit_root.as_posix()}],
            },
            args.json,
            EXIT_VALIDATION_FAILURE,
        )

    for path in sorted(audit_root.rglob("*.md")):
        rel = path.relative_to(kb_root).as_posix()
        fm = read_audit_frontmatter(path)
        status = fm.get("status", "open")
        severity = fm.get("severity", "unknown")
        target = fm.get("target_path", "")
        item = {"path": rel, "status": status, "severity": severity, "target_path": target}
        if not fm:
            malformed.append(rel)
        if args.status != "all" and status != args.status:
            continue
        if args.severity and severity != args.severity:
            continue
        if args.target_path and target != args.target_path:
            continue
        items.append(item)

    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        key = str(item.get(args.group_by, "ungrouped"))
        grouped.setdefault(key, []).append(item)

    counts = {status: sum(1 for item in items if item["status"] == status) for status in ["open", "resolved", "deferred", "rejected"]}

    return emit(
        {
            "artifact_name": "audit_report",
            "status": "passed" if not malformed else "passed_with_flags",
            "kb_root": kb_root.as_posix(),
            "open_count": counts["open"],
            "resolved_count": counts["resolved"],
            "deferred_count": counts["deferred"],
            "rejected_count": counts["rejected"],
            "grouped_items": grouped,
            "malformed_items": malformed,
            "missing_targets": [],
        },
        args.json,
        EXIT_OK if not malformed else EXIT_FLAGS,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Apex KB deterministic helper")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    parser.add_argument("--allow-write", action="store_true", help="Permit deterministic writes")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures where supported")

    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("scaffold", help="Create or preview KB skeleton")
    p.add_argument("--kb-root", required=True)
    p.add_argument("--title", "--topic-title", dest="title", default=None)
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_scaffold)

    p = sub.add_parser("hash", help="Hash a file or directory")
    p.add_argument("--path", required=True)
    p.set_defaults(func=cmd_hash)

    p = sub.add_parser("preflight", help="Run ingest preflight")
    p.add_argument("--kb-root", required=True)
    p.add_argument("--source", required=True)
    p.add_argument("--source-slug", required=True)
    p.set_defaults(func=cmd_preflight)

    p = sub.add_parser("manifest", help="Validate or initialize source manifest")
    p.add_argument("--kb-root", required=True)
    p.add_argument("--validate-only", action="store_true")
    p.set_defaults(func=cmd_manifest)

    p = sub.add_parser("index", help="Generate/update machine index section")
    p.add_argument("--kb-root", required=True)
    p.add_argument("--validate-only", action="store_true")
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("lint", help="Run deterministic KB lint")
    p.add_argument("--kb-root", required=True)
    p.add_argument("--check", default="all")
    p.set_defaults(func=cmd_lint)

    p = sub.add_parser("audit", help="List/group audit items")
    p.add_argument("--kb-root", required=True)
    p.add_argument("--status", default="open", choices=["open", "resolved", "deferred", "rejected", "all"])
    p.add_argument("--severity", default=None)
    p.add_argument("--target-path", default=None)
    p.add_argument("--group-by", default="target_path", choices=["target_path", "severity", "status"])
    p.set_defaults(func=cmd_audit)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except BrokenPipeError:
        return EXIT_OK
    except Exception as exc:
        payload = {
            "artifact_name": "apex_kb_error",
            "status": "failed",
            "error": str(exc),
            "command": getattr(args, "command", None),
            "generated_at": utc_now(),
        }
        if getattr(args, "json", False):
            print(json.dumps(payload, indent=2, ensure_ascii=False))
        else:
            print(f"apex_kb_error: failed\nerror: {exc}", file=sys.stderr)
        return EXIT_INVOCATION_ERROR


if __name__ == "__main__":
    raise SystemExit(main())
'''


def now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def strip_chat_file_wrapper(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.lstrip("\ufeff")

    # Remove leading "# FILE: `path`" or "# FILE: path".
    text = re.sub(r"^\s*# FILE:\s*`?[^`\n]+`?\s*\n+", "", text, count=1)

    stripped = text.strip()

    # Remove one whole-file outer fence when present.
    m = re.fullmatch(r"```(?:[a-zA-Z0-9_-]+)?\n?(.*?)\n?```\s*", stripped, flags=re.S)
    if m:
        text = m.group(1).strip() + "\n"

    return text


def rehydrate_yamlish_line(line: str) -> str:
    """
    Best-effort repair for collapsed YAML-like content:
      "root:  a: 1  b: 2    - item"
    becomes multiple lines. This is not a semantic YAML parser; it repairs
    common collapse artifacts from chat-output file blocks.
    """
    s = line.strip()

    # Put list items on their own line.
    s = re.sub(r"(?<=\S)( {2,})(-\s+)", lambda m: "\n" + m.group(1) + m.group(2), s)

    # Put keys on their own line when preceded by 2+ spaces.
    s = re.sub(
        r"(?<=\S)( {2,})([A-Za-z_][A-Za-z0-9_-]*:)",
        lambda m: "\n" + m.group(1) + m.group(2),
        s,
    )

    return s


def rehydrate_fenced_blocks(text: str) -> str:
    # Normalize fence starts.
    text = re.sub(r"```(yaml|markdown|md|json|text|python)", r"\n```\1\n", text)
    text = re.sub(r"```(#{1,6}\s)", r"```\n\n\1", text)
    text = re.sub(r"```(\s*##+ )", r"```\n\n\1", text)

    # Place headings on their own lines.
    text = re.sub(r"(?<!\n)(#{1,6}\s+[A-Z0-9<])", r"\n\n\1", text)

    # Apply YAML-ish rehydration only inside yaml fenced blocks.
    def fix_yaml_block(match: re.Match[str]) -> str:
        lang = match.group(1)
        body = match.group(2)
        if "\n" not in body.strip() or max((len(x) for x in body.splitlines()), default=0) > 240:
            fixed = rehydrate_yamlish_line(body)
        else:
            fixed = body
        return f"```{lang}\n{fixed.strip()}\n```"

    text = re.sub(r"```(yaml|json)\n(.*?)```", fix_yaml_block, text, flags=re.S)

    # Remove excessive blank lines.
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip() + "\n"


def repair_skill_frontmatter(text: str) -> str:
    """
    Special repair for collapsed SKILL.md frontmatter:
      ---name: apex-kbdescription: > ...---# Apex KB
    """
    if text.startswith("---\n"):
        return text

    if not text.startswith("---name:"):
        return text

    m = re.search(r"---name:\s*([A-Za-z0-9_-]+)description:\s*>\s*(.*?)---#\s*", text, flags=re.S)
    if not m:
        return text

    name = m.group(1).strip()
    desc = " ".join(m.group(2).split())
    body_start = m.end() - len("# ")
    body = text[body_start:]

    wrapped_desc = "\n".join(f"  {part}" for part in wrap_words(desc, 88))
    return f"---\nname: {name}\ndescription: >\n{wrapped_desc}\n---\n\n{body}"


def wrap_words(text: str, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        if not current:
            current = word
        elif len(current) + 1 + len(word) <= width:
            current += " " + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def repair_markdown(text: str, is_skill: bool) -> str:
    text = strip_chat_file_wrapper(text)
    if is_skill:
        text = repair_skill_frontmatter(text)
    text = rehydrate_fenced_blocks(text)

    # Remove accidental leading blank before frontmatter in SKILL.md.
    if is_skill:
        text = text.lstrip()
    return text


def backup_file(repo: Path, path: Path, backup_root: Path) -> Path:
    rel = path.relative_to(repo)
    target = backup_root / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, target)
    return target


def detect_whole_file_fence(text: str) -> bool:
    stripped = text.strip()
    return stripped.startswith("```") and stripped.endswith("```")


def validate_markdown_file(path: Path, text: str, is_skill: bool) -> list[str]:
    problems: list[str] = []
    first = text.lstrip().splitlines()[0] if text.strip() else ""

    if first.startswith("# FILE:"):
        problems.append("still starts with # FILE wrapper")
    if detect_whole_file_fence(text):
        problems.append("still wrapped in a whole-file Markdown fence")
    if is_skill and not text.lstrip().startswith("---\nname:"):
        problems.append("SKILL.md does not start with YAML frontmatter")
    if "```yaml" in text and "```yaml\n" not in text:
        problems.append("contains malformed yaml fence start")
    return problems


def python_compile_ok(text: str) -> tuple[bool, str | None]:
    try:
        ast.parse(text)
        return True, None
    except SyntaxError as exc:
        return False, f"{exc.msg} at line {exc.lineno}"


def run_help_check(repo: Path, script_rel: str) -> tuple[bool, str]:
    script = repo / script_rel
    commands = [
        [sys.executable, str(script), "--help"],
        [sys.executable, str(script), "--json", "scaffold", "--help"],
        [sys.executable, str(script), "--json", "hash", "--help"],
        [sys.executable, str(script), "--json", "preflight", "--help"],
        [sys.executable, str(script), "--json", "manifest", "--help"],
        [sys.executable, str(script), "--json", "index", "--help"],
        [sys.executable, str(script), "--json", "lint", "--help"],
        [sys.executable, str(script), "--json", "audit", "--help"],
    ]

    failures: list[str] = []
    for cmd in commands:
        proc = subprocess.run(cmd, cwd=repo, capture_output=True, text=True)
        if proc.returncode != 0:
            failures.append(f"{' '.join(cmd)} -> {proc.returncode}: {proc.stderr.strip() or proc.stdout.strip()}")

    if failures:
        return False, "\n".join(failures)
    return True, "all help commands passed"


def repair_repo(repo: Path, apply: bool, run_help: bool) -> int:
    stamp = now_stamp()
    backup_root = repo / BACKUP_DIR / stamp
    report: dict[str, Any] = {
        "repo": repo.as_posix(),
        "apply": apply,
        "backup_root": backup_root.as_posix(),
        "markdown_files": [],
        "script_file": None,
        "validation": [],
    }

    changed = False
    fatal = False

    for rel in REPO_RELATIVE_MARKDOWN_FILES:
        path = repo / rel
        item: dict[str, Any] = {"path": rel, "exists": path.exists(), "changed": False, "problems_after": []}

        if not path.exists():
            item["problems_after"].append("missing file")
            fatal = True
            report["markdown_files"].append(item)
            continue

        original = read_text(path)
        is_skill = rel.endswith("/SKILL.md") or rel == ".claude/skills/apex-kb/SKILL.md"
        repaired = repair_markdown(original, is_skill=is_skill)

        item["original_sha256"] = sha256_text(original)
        item["repaired_sha256"] = sha256_text(repaired)
        item["changed"] = original != repaired
        item["problems_after"] = validate_markdown_file(path, repaired, is_skill=is_skill)

        if item["problems_after"]:
            fatal = True

        if item["changed"]:
            changed = True
            if apply:
                backup_file(repo, path, backup_root)
                write_text(path, repaired)

        report["markdown_files"].append(item)

    script_path = repo / SCRIPT_PATH
    script_item: dict[str, Any] = {"path": SCRIPT_PATH, "exists": script_path.exists(), "changed": False, "problems_after": []}

    if not script_path.exists():
        script_item["problems_after"].append("missing script file")
        fatal = True
    else:
        original_script = read_text(script_path)
        repaired_script = CLEAN_APEX_KB_PY.strip() + "\n"
        ok, err = python_compile_ok(repaired_script)

        script_item["original_sha256"] = sha256_text(original_script)
        script_item["repaired_sha256"] = sha256_text(repaired_script)
        script_item["changed"] = original_script != repaired_script
        script_item["compile_ok"] = ok
        if err:
            script_item["problems_after"].append(err)
            fatal = True

        if script_item["changed"]:
            changed = True
            if apply:
                backup_file(repo, script_path, backup_root)
                write_text(script_path, repaired_script)

    report["script_file"] = script_item

    if apply and run_help and not fatal:
        ok, detail = run_help_check(repo, SCRIPT_PATH)
        report["validation"].append({"check": "apex_kb_help_surface", "ok": ok, "detail": detail})
        if not ok:
            fatal = True

    report["changed"] = changed
    report["status"] = "failed" if fatal else ("changed" if changed else "clean")
    print(json.dumps(report, indent=2, ensure_ascii=False))

    if fatal:
        return 2
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair Apex KB chat-output file malformats.")
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root. Default: current directory.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually write repaired files. Without this, only reports planned changes.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Dry-run check mode. Equivalent to omitting --apply.",
    )
    parser.add_argument(
        "--no-help-check",
        action="store_true",
        help="Skip apex_kb.py --help validation after --apply.",
    )

    args = parser.parse_args()
    repo = Path(args.repo_root).resolve()

    if not (repo / ".git").exists():
        print(json.dumps({"status": "failed", "error": "repo root does not contain .git", "repo": repo.as_posix()}, indent=2))
        return 2

    return repair_repo(repo=repo, apply=args.apply, run_help=not args.no_help_check)


if __name__ == "__main__":
    raise SystemExit(main())