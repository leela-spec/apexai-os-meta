#!/usr/bin/env python3
"""Bounded deterministic prework for large local corpora.

The script creates navigation artifacts for later LLM work without doing
semantic ingest, embeddings, wiki generation, or source copying.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


DEFAULT_EXCLUDE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
    ".next",
    ".turbo",
    "node_modules",
    "dist",
    "build",
    "out",
    "coverage",
    "target",
    "vendor",
    "site-packages",
}

DEFAULT_TEXT_EXTS = {
    ".md",
    ".mdx",
    ".txt",
    ".rst",
    ".adoc",
    ".yaml",
    ".yml",
    ".json",
    ".jsonl",
    ".ndjson",
    ".toml",
    ".ini",
    ".cfg",
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".go",
    ".rs",
    ".java",
    ".cs",
    ".rb",
    ".php",
    ".sh",
    ".ps1",
    ".sql",
    ".csv",
    ".tsv",
}

PACKAGE_MANIFESTS = {
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "gemfile",
    "composer.json",
}

DEFAULT_BINARY_EXTS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
    ".svg",
    ".pdf",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".rar",
    ".exe",
    ".dll",
    ".so",
    ".dylib",
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
    ".mp3",
    ".mp4",
    ".mov",
    ".avi",
    ".lock",
}

KEYWORD_GROUPS = {
    "llm_design": ["llm", "ai agent", "agent", "claude", "chatgpt", "prompt", "system prompt", "role", "instruction"],
    "skill_package": ["skill.md", "skill", "frontmatter", "allowed_tools", "allowed-tools", "progressive disclosure"],
    "workflow": ["workflow", "process", "pipeline", "phase", "handoff", "task", "orchestration"],
    "knowledge_base": ["knowledge base", "kb", "wiki", "source manifest", "retrieval", "index", "fts5", "bm25"],
    "evaluation": ["eval", "evaluation", "test", "fixture", "validation", "benchmark", "failure mode"],
    "memory": ["memory", "context", "state", "session", "checkpoint", "resume"],
    "mcp_tooling": ["mcp", "tool", "tools", "connector", "plugin", "api"],
}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
MD_LINK_RE = re.compile(r"(?<!!)\[([^\]\n]+)\]\(([^)\n]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]\n]+)\]\]")
FENCE_RE = re.compile(r"^(```+|~~~+)\s*([^`]*)$")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def split_csv(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def rel(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def stable_json(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def looks_textual(path: Path, text_exts: set[str]) -> bool:
    name = path.name.lower()
    ext = path.suffix.lower()
    return ext in text_exts or name in PACKAGE_MANIFESTS or name in {"readme", "license", "makefile"}


def path_signal(path_text: str, file_name: str) -> tuple[int, list[str]]:
    low_path = path_text.lower()
    low_name = file_name.lower()
    score = 0
    reasons: list[str] = []
    exact = {
        "skill.md": 120,
        "readme.md": 50,
        "package.json": 35,
        "pyproject.toml": 35,
        "package-manifest.md": 80,
    }
    if low_name in exact:
        score += exact[low_name]
        reasons.append(f"filename:{low_name}+{exact[low_name]}")
    for token, value in {
        "prompt": 45,
        "agent": 35,
        "claude": 45,
        "skill": 45,
        "workflow": 35,
        "process": 25,
        "memory": 30,
        "eval": 25,
        "evaluation": 30,
        "manifest": 25,
        "quickstart": 25,
        "guide": 20,
        "reference": 20,
        "example": 15,
        "template": 15,
    }.items():
        if token in low_name:
            score += value
            reasons.append(f"filename-token:{token}+{value}")
    for token, value in {
        "/docs/": 30,
        "/doc/": 20,
        "/examples/": 20,
        "/templates/": 20,
        "/skills/": 50,
        "/prompts/": 45,
        "/workflows/": 35,
        "/knowledge": 25,
        "/kb": 20,
        "/research": 15,
    }.items():
        if token in f"/{low_path}":
            score += value
            reasons.append(f"path-token:{token.strip('/')}+{value}")
    return score, reasons


def keyword_signal(text: str) -> tuple[int, list[str], dict[str, int]]:
    low = text.lower()
    score = 0
    reasons: list[str] = []
    hits: dict[str, int] = {}
    for group, terms in KEYWORD_GROUPS.items():
        count = 0
        for term in terms:
            count += low.count(term.lower())
        if count:
            hits[group] = count
            score += min(count, 10) * 4
            reasons.append(f"keyword-group:{group}x{count}")
    return score, reasons, hits


def parse_frontmatter(lines: list[str]) -> dict[str, Any]:
    if not lines or lines[0].strip().lstrip("\ufeff") != "---":
        return {"present": False, "end_line": None, "raw_keys": [], "status": "none"}
    end = None
    for idx, line in enumerate(lines[1:], start=2):
        if line.strip() == "---":
            end = idx
            break
    if end is None:
        return {"present": True, "end_line": None, "raw_keys": [], "status": "malformed"}
    keys = []
    for line in lines[1 : end - 1]:
        if not line.startswith((" ", "\t")) and ":" in line:
            key = line.split(":", 1)[0].strip()
            if key and re.match(r"^[A-Za-z0-9_-]+$", key):
                keys.append(key)
    return {"present": True, "end_line": end, "raw_keys": sorted(set(keys)), "status": "detected"}


def parse_structure(path: Path, source_root: Path, max_lines: int) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    headings = []
    links = []
    wikilinks = []
    code_blocks = []
    in_fence = False
    fence_start = 0
    fence_marker = ""
    fence_lang = ""
    for idx, line in enumerate(lines[:max_lines], start=1):
        stripped = line.strip()
        fm = FENCE_RE.match(stripped)
        if fm:
            marker = fm.group(1)[:3]
            if not in_fence:
                in_fence = True
                fence_start = idx
                fence_marker = marker
                fence_lang = fm.group(2).strip().split()[0] if fm.group(2).strip() else ""
            elif marker == fence_marker:
                code_blocks.append({"language": fence_lang, "start_line": fence_start, "end_line": idx})
                in_fence = False
            continue
        if in_fence:
            continue
        hm = HEADING_RE.match(line)
        if hm:
            headings.append({"level": len(hm.group(1)), "text": re.sub(r"\s+#*$", "", hm.group(2)).strip(), "line": idx})
        for lm in MD_LINK_RE.finditer(line):
            links.append({"text": lm.group(1), "target": lm.group(2), "line": idx})
        for wm in WIKILINK_RE.finditer(line):
            raw = wm.group(1).strip()
            target, _, alias = raw.partition("|")
            wikilinks.append({"raw": raw, "target": target.strip(), "alias": alias.strip() or None, "line": idx})
    key_score, key_reasons, key_hits = keyword_signal(text)
    return {
        "path": rel(source_root, path),
        "line_count": len(lines),
        "frontmatter": parse_frontmatter(lines),
        "h1": next((h["text"] for h in headings if h["level"] == 1), None),
        "headings": headings[:200],
        "markdown_links": links[:200],
        "wikilinks": wikilinks[:200],
        "code_blocks": code_blocks[:100],
        "keyword_score": key_score,
        "keyword_reasons": key_reasons,
        "keyword_hits": key_hits,
        "parser_warnings": ["unclosed_code_fence"] if in_fence else [],
    }


def iter_inventory(source_root: Path, exclude_dirs: set[str], text_exts: set[str], max_files: int) -> Iterable[dict[str, Any]]:
    seen = 0
    for root, dirs, files in os.walk(source_root):
        dirs[:] = sorted([d for d in dirs if d not in exclude_dirs], key=str.lower)
        root_path = Path(root)
        for name in sorted(files, key=str.lower):
            seen += 1
            if max_files and seen > max_files:
                return
            path = root_path / name
            try:
                stat = path.stat()
            except OSError:
                continue
            path_text = rel(source_root, path)
            ext = path.suffix.lower()
            is_binary_or_asset = ext in DEFAULT_BINARY_EXTS
            is_text_candidate = looks_textual(path, text_exts) and not is_binary_or_asset
            p_score, p_reasons = path_signal(path_text, name)
            yield {
                "path": path_text,
                "name": name,
                "extension": ext,
                "size_bytes": stat.st_size,
                "mtime_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
                "is_text_candidate": is_text_candidate,
                "is_binary_or_asset": is_binary_or_asset,
                "is_package_manifest": name.lower() in PACKAGE_MANIFESTS,
                "path_score": p_score,
                "path_reasons": p_reasons,
            }


def select_candidates(inventory: list[dict[str, Any]], max_bytes_per_file: int, max_candidates: int) -> list[dict[str, Any]]:
    candidates = []
    for rec in inventory:
        if not rec["is_text_candidate"]:
            continue
        if rec["size_bytes"] > max_bytes_per_file:
            continue
        if rec["path_score"] <= 0 and rec["extension"] not in {".md", ".mdx", ".txt", ".rst", ".adoc"}:
            continue
        candidates.append(dict(rec))
    candidates.sort(key=lambda r: (-r["path_score"], r["size_bytes"], r["path"]))
    return candidates[:max_candidates]


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json.dumps(row.get(k), ensure_ascii=False) if isinstance(row.get(k), (dict, list)) else row.get(k) for k in fields})


def write_output_options(path: Path) -> None:
    text = """# Large Corpus Prework Output Options

This script is meant to create deterministic footing for later LLM work. It does
not decide truth, write wiki pages, create embeddings, or copy source material.

## Option 1: Inventory Only

Use when the corpus is unknown, huge, or risky.

- Reads file metadata only.
- Produces inventory, size/noise profile, and candidate path guesses.
- Best first run for unfiltered repos, databases, exports, and KB dumps.

## Option 2: Candidate Routing

Use when you want the LLM to read a bounded set first.

- Reads only text candidates under `--max-bytes-per-file`.
- Extracts headings, frontmatter keys, links, wikilinks, code-fence spans, and keyword groups.
- Produces `llm-routing-packet.md` and `candidate-files.*`.

## Option 3: Structure Maps

Use when Markdown/wiki navigation matters.

- Keeps detailed structure records in NDJSON.
- Good for later graph or broken-link work.
- Still avoids semantic interpretation.

## Option 4: Search/Retrieval Prep

Future extension, not enabled here by default.

- SQLite FTS5 or JSON search export.
- Requires local runtime checks and explicit derived-artifact policy.

## Questions To Decide Before Large Production Runs

1. Should the output optimize for human review, LLM routing, or machine indexing?
2. What is the maximum file size an LLM should be allowed to inspect in one pass?
3. Should code files be ranked equally with docs, or only included when path/keyword signals are strong?
4. Should hashes be computed for all files, only candidates, or never during fast inventory?
5. Should database files be inventoried only, exported by a domain tool, or excluded until a schema-specific pass exists?
6. Which keyword groups are project-specific enough to add before scanning?
7. Should future runs create a local lexical search index, or is the routing packet enough?
"""
    path.write_text(text, encoding="utf-8", newline="\n")


def write_reports(output_root: Path, source_root: Path, inventory: list[dict[str, Any]], candidates: list[dict[str, Any]], structures: list[dict[str, Any]], args: argparse.Namespace, started: float) -> dict[str, Any]:
    output_root.mkdir(parents=True, exist_ok=True)
    by_ext = Counter((r["extension"] or "[none]") for r in inventory)
    total_bytes = sum(r["size_bytes"] for r in inventory)
    largest = sorted(inventory, key=lambda r: (-r["size_bytes"], r["path"]))[:50]
    skipped_large = [r for r in inventory if r["is_text_candidate"] and r["size_bytes"] > args.max_bytes_per_file]
    skipped_large.sort(key=lambda r: (-r["size_bytes"], r["path"]))
    structure_by_path = {s["path"]: s for s in structures}
    for rec in candidates:
        s = structure_by_path.get(rec["path"])
        if s:
            rec["keyword_score"] = s["keyword_score"]
            rec["keyword_hits"] = s["keyword_hits"]
            rec["score"] = rec["path_score"] + s["keyword_score"]
            rec["reasons"] = rec["path_reasons"] + s["keyword_reasons"]
            rec["h1"] = s["h1"]
            rec["line_count"] = s["line_count"]
        else:
            rec["keyword_score"] = 0
            rec["keyword_hits"] = {}
            rec["score"] = rec["path_score"]
            rec["reasons"] = rec["path_reasons"]
            rec["h1"] = None
            rec["line_count"] = None
    candidates.sort(key=lambda r: (-r["score"], r["path"]))

    summary = {
        "generated_at": utc_now(),
        "source_root": str(source_root),
        "output_root": str(output_root),
        "mode": args.mode,
        "profile": args.profile,
        "runtime_seconds": round(time.perf_counter() - started, 3),
        "files_seen": len(inventory),
        "text_candidate_files": sum(1 for r in inventory if r["is_text_candidate"]),
        "binary_or_asset_files": sum(1 for r in inventory if r["is_binary_or_asset"]),
        "candidate_count": len(candidates),
        "structure_records": len(structures),
        "total_bytes_seen": total_bytes,
        "extension_counts": dict(sorted(by_ext.items())),
        "largest_files": largest[:20],
        "largest_skipped_by_byte_limit": skipped_large[:20],
        "bounds": {
            "max_files": args.max_files,
            "max_candidates": args.max_candidates,
            "max_bytes_per_file": args.max_bytes_per_file,
            "max_structure_lines": args.max_structure_lines,
        },
    }

    (output_root / "scan-run-summary.json").write_text(stable_json(summary), encoding="utf-8")
    (output_root / "corpus-inventory.ndjson").write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in inventory), encoding="utf-8")
    write_csv(output_root / "corpus-inventory.csv", inventory, ["path", "name", "extension", "size_bytes", "mtime_utc", "is_text_candidate", "is_binary_or_asset", "is_package_manifest", "path_score", "path_reasons"])
    (output_root / "candidate-files.json").write_text(stable_json(candidates), encoding="utf-8")
    (output_root / "structure-map.ndjson").write_text("".join(json.dumps(s, ensure_ascii=False, sort_keys=True) + "\n" for s in structures), encoding="utf-8")

    keyword_lines = []
    for s in structures:
        for group, count in s["keyword_hits"].items():
            keyword_lines.append({"path": s["path"], "keyword_group": group, "count": count})
    (output_root / "keyword-hits.ndjson").write_text("".join(json.dumps(k, ensure_ascii=False, sort_keys=True) + "\n" for k in keyword_lines), encoding="utf-8")

    md = ["# Candidate Files", "", f"Generated: `{summary['generated_at']}`", "", f"Source root: `{source_root}`", "", "| score | path | size | reason |", "| ---: | --- | ---: | --- |"]
    for rec in candidates:
        md.append(f"| {rec['score']} | `{rec['path']}` | {rec['size_bytes']} | {'; '.join(rec['reasons'][:5])} |")
    (output_root / "candidate-files.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")

    routing = ["# LLM Routing Packet", "", "## Purpose", "", "Use this packet to choose what to read first. It is deterministic evidence, not semantic analysis.", "", "## Scan Snapshot", ""]
    routing.extend([
        f"- source_root: `{source_root}`",
        f"- files_seen: `{len(inventory)}`",
        f"- text_candidate_files: `{summary['text_candidate_files']}`",
        f"- candidate_count: `{len(candidates)}`",
        f"- total_bytes_seen: `{total_bytes}`",
        "",
        "## Read First",
        "",
    ])
    for rec in candidates[:50]:
        routing.append(f"- `{rec['path']}`")
        routing.append(f"  - score: {rec['score']}")
        routing.append(f"  - reasons: {'; '.join(rec['reasons'][:6])}")
        if rec.get("h1"):
            routing.append(f"  - h1: {rec['h1']}")
    routing.extend(["", "## Large Files Requiring Separate Handling", ""])
    routing.extend([f"- `{r['path']}`: {r['size_bytes']} bytes" for r in skipped_large[:50]] or ["- None."])
    routing.extend(["", "## Suggested Next Questions", "", "- Should this corpus get only a curated-source allowlist, or also a local lexical search index?", "- Are databases/exports present that need schema-specific extractors?", "- Which project-specific keyword groups should be added before the next scan?"])
    (output_root / "llm-routing-packet.md").write_text("\n".join(routing) + "\n", encoding="utf-8", newline="\n")

    write_output_options(output_root / "output-options.md")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Create deterministic prework artifacts for large local corpora.")
    parser.add_argument("--source-root", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--mode", choices=["inventory", "candidates", "structure", "full"], default="candidates")
    parser.add_argument("--profile", choices=["quick", "balanced", "deep"], default="balanced")
    parser.add_argument("--exclude-dir", action="append", default=[])
    parser.add_argument("--include-ext", default="")
    parser.add_argument("--max-files", type=int, default=100000)
    parser.add_argument("--max-candidates", type=int, default=500)
    parser.add_argument("--max-bytes-per-file", type=int, default=512000)
    parser.add_argument("--max-structure-lines", type=int, default=4000)
    parser.add_argument("--hash-candidates", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    started = time.perf_counter()
    source_root = Path(args.source_root).expanduser().resolve()
    output_root = Path(args.output_root).expanduser().resolve()
    if not source_root.exists():
        print("SOURCE_ROOT_MISSING")
        return 2
    exclude_dirs = DEFAULT_EXCLUDE_DIRS | set(args.exclude_dir)
    text_exts = DEFAULT_TEXT_EXTS | set(split_csv(args.include_ext))

    inventory = list(iter_inventory(source_root, exclude_dirs, text_exts, args.max_files))
    candidates: list[dict[str, Any]] = []
    structures: list[dict[str, Any]] = []
    if args.mode in {"candidates", "structure", "full"}:
        candidates = select_candidates(inventory, args.max_bytes_per_file, args.max_candidates)
        for rec in candidates:
            path = source_root / rec["path"]
            try:
                structures.append(parse_structure(path, source_root, args.max_structure_lines))
                if args.hash_candidates:
                    rec["sha256"] = sha256_file(path)
            except Exception as exc:
                rec["read_error"] = str(exc)
    elif args.mode == "inventory":
        candidates = select_candidates(inventory, args.max_bytes_per_file, args.max_candidates)

    summary = write_reports(output_root, source_root, inventory, candidates, structures, args, started)
    if args.json:
        print(stable_json(summary), end="")
    else:
        print(f"files_seen: {summary['files_seen']}")
        print(f"candidate_count: {summary['candidate_count']}")
        print(f"runtime_seconds: {summary['runtime_seconds']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
