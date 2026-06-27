#!/usr/bin/env python3
"""Local derived retrieval for Apex KB wiki pages.

Policy:
- Standard library only; optional modules are detected but not required.
- No network, no shell-outs.
- Default mode is dry-run. Writes require --allow-write.
- Writes are restricted to <kb-root>/derived/search and, for saved query
  packets, <kb-root>/outputs/queries.
- SQLite FTS5 is used only after a runtime probe. JSON/markdown fallback is
  always available.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import sqlite3
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

INDEX_DIR = Path("derived/search")
SQLITE_NAME = "index.sqlite"
JSON_NAME = "search-index.json"
NDJSON_NAME = "search-index.ndjson"
META_NAME = "index-meta.json"
QUERY_DIR = Path("outputs/queries")
WIKI_DIR = Path("wiki")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slugify(value: str, default: str = "item") -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or default


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str, kb_root: Path, allow_write: bool, dry_run: bool) -> Dict[str, Any]:
    ensure_inside(kb_root, path)
    action = "create" if not path.exists() else "update"
    changed = (not path.exists()) or read_text(path) != text
    result = {"path": relpath(kb_root, path), "action": action, "changed": changed, "written": False}
    if changed and allow_write and not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="\n")
        result["written"] = True
    return result


def remove_file(path: Path, kb_root: Path, allow_write: bool, dry_run: bool) -> Dict[str, Any]:
    ensure_inside(kb_root, path)
    result = {"path": relpath(kb_root, path), "exists": path.exists(), "removed": False}
    if path.exists() and allow_write and not dry_run:
        path.unlink()
        result["removed"] = True
    return result


def resolve_kb_root(value: str) -> Path:
    root = Path(value).expanduser().resolve()
    return root


def relpath(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def ensure_inside(root: Path, path: Path) -> None:
    root_r = root.resolve()
    path_r = path.resolve()
    try:
        path_r.relative_to(root_r)
    except ValueError as exc:
        raise SystemExit(f"Refusing path outside kb_root: {path}") from exc


def effective_dry_run(args: argparse.Namespace) -> bool:
    return bool(args.dry_run or not args.allow_write)


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
    if args.json:
        json_print(obj)
    else:
        human_print(obj)


def detect_optional_modules() -> Dict[str, bool]:
    return {
        "markdown_it": importlib.util.find_spec("markdown_it") is not None,
        "frontmatter": importlib.util.find_spec("frontmatter") is not None,
        "yaml": importlib.util.find_spec("yaml") is not None,
    }


def detect_tools() -> Dict[str, bool]:
    return {"git": shutil.which("git") is not None, "rg": shutil.which("rg") is not None}


def probe_fts5() -> Dict[str, Any]:
    info: Dict[str, Any] = {
        "sqlite3_module": True,
        "sqlite_version": sqlite3.sqlite_version,
        "fts5_available": False,
        "compile_options": [],
        "error": None,
    }
    try:
        conn = sqlite3.connect(":memory:")
        info["compile_options"] = [row[0] for row in conn.execute("PRAGMA compile_options").fetchall()]
        conn.execute("CREATE VIRTUAL TABLE apex_kb_fts_probe USING fts5(body)")
        conn.execute("INSERT INTO apex_kb_fts_probe(body) VALUES ('probe')")
        conn.execute("SELECT rowid FROM apex_kb_fts_probe WHERE apex_kb_fts_probe MATCH 'probe'").fetchall()
        info["fts5_available"] = True
        conn.close()
    except Exception as exc:  # pragma: no cover - environment dependent
        info["error"] = str(exc)
    return info


def parse_minimal_yaml(text: str) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    current_key: Optional[str] = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        list_match = re.match(r"^\s*-\s+(.*)$", line)
        if list_match and current_key:
            data.setdefault(current_key, []).append(strip_yaml_scalar(list_match.group(1)))
            continue
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            if value == "":
                data[key] = []
            else:
                data[key] = strip_yaml_scalar(value)
    return data


def strip_yaml_scalar(value: str) -> Any:
    value = value.strip()
    if value in {"[]", ""}:
        return []
    if value in {"{}"}:
        return {}
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    return value


def parse_frontmatter(markdown: str) -> Tuple[Dict[str, Any], str, int]:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, markdown, 1
    end_idx: Optional[int] = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}, markdown, 1
    fm_text = "\n".join(lines[1:end_idx])
    body = "\n".join(lines[end_idx + 1 :])
    meta: Dict[str, Any] = {}
    try:
        if importlib.util.find_spec("yaml") is not None:
            import yaml  # type: ignore

            loaded = yaml.safe_load(fm_text)
            if isinstance(loaded, dict):
                meta = loaded
        else:
            meta = parse_minimal_yaml(fm_text)
    except Exception:
        meta = parse_minimal_yaml(fm_text)
    return meta, body, end_idx + 2


def first_h1(markdown_body: str) -> Optional[str]:
    for line in markdown_body.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return None


@dataclass
class Chunk:
    chunk_id: str
    kb_slug: str
    rel_path: str
    title: str
    page_type: str
    status: str
    confidence: str
    claim_label: str
    heading: str
    heading_level: int
    start_line: int
    end_line: int
    text: str
    page_hash: str
    source_mtime: float


def iter_wiki_pages(kb_root: Path) -> List[Path]:
    wiki = kb_root / WIKI_DIR
    if not wiki.exists():
        return []
    pages = []
    for path in sorted(wiki.rglob("*.md")):
        if path.name.lower() == "index.md":
            continue
        if path.is_file():
            pages.append(path)
    return pages


def chunk_page(kb_root: Path, path: Path) -> List[Chunk]:
    raw = read_text(path)
    meta, body, body_start_line = parse_frontmatter(raw)
    rel = relpath(kb_root, path)
    page_hash = sha256_file(path)
    stat = path.stat()
    title = str(meta.get("title") or first_h1(body) or path.stem)
    page_type = str(meta.get("page_type") or "unknown")
    status = str(meta.get("status") or "unknown")
    confidence = str(meta.get("confidence") or "unknown")
    claim_label = str(meta.get("claim_label") or "unknown")

    lines = body.splitlines()
    headings: List[Tuple[int, int, str]] = []
    in_fence = False
    fence_marker = ""
    for offset, line in enumerate(lines, start=body_start_line):
        stripped = line.strip()
        fence = re.match(r"^(```+|~~~+)", stripped)
        if fence:
            marker = fence.group(1)[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            text = re.sub(r"\s+#*$", "", m.group(2)).strip()
            headings.append((offset, level, text))

    chunks: List[Chunk] = []
    if not headings:
        text = body.strip()
        if text:
            chunks.append(make_chunk(kb_root, rel, title, page_type, status, confidence, claim_label, title, 1, body_start_line, body_start_line + len(lines), text, page_hash, stat.st_mtime))
        return chunks

    line_lookup = {body_start_line + i: line for i, line in enumerate(lines)}
    for idx, (start, level, heading) in enumerate(headings):
        end = headings[idx + 1][0] - 1 if idx + 1 < len(headings) else body_start_line + len(lines) - 1
        section_lines = [line_lookup.get(n, "") for n in range(start, end + 1)]
        text = "\n".join(section_lines).strip()
        if not text:
            continue
        chunks.append(make_chunk(kb_root, rel, title, page_type, status, confidence, claim_label, heading, level, start, end, text, page_hash, stat.st_mtime))
    return chunks


def make_chunk(kb_root: Path, rel: str, title: str, page_type: str, status: str, confidence: str, claim_label: str, heading: str, level: int, start: int, end: int, text: str, page_hash: str, mtime: float) -> Chunk:
    kb_slug = kb_root.name
    chunk_basis = f"{kb_slug}\n{rel}\n{heading}\n{start}\n{end}\n{page_hash}"
    return Chunk(
        chunk_id=sha256_bytes(chunk_basis.encode("utf-8"))[:24],
        kb_slug=kb_slug,
        rel_path=rel,
        title=title,
        page_type=page_type,
        status=status,
        confidence=confidence,
        claim_label=claim_label,
        heading=heading,
        heading_level=level,
        start_line=start,
        end_line=end,
        text=text,
        page_hash=page_hash,
        source_mtime=mtime,
    )


def collect_chunks(kb_root: Path) -> List[Chunk]:
    chunks: List[Chunk] = []
    for page in iter_wiki_pages(kb_root):
        chunks.extend(chunk_page(kb_root, page))
    return chunks


def current_file_state(kb_root: Path) -> Dict[str, Dict[str, Any]]:
    state: Dict[str, Dict[str, Any]] = {}
    for page in iter_wiki_pages(kb_root):
        state[relpath(kb_root, page)] = {"hash": sha256_file(page), "mtime": page.stat().st_mtime}
    return state


def index_meta(kb_root: Path, chunks: List[Chunk], backend: str) -> Dict[str, Any]:
    return {
        "schema_version": "1.0",
        "kb_slug": kb_root.name,
        "generated_at": utc_now(),
        "backend": backend,
        "page_count": len(current_file_state(kb_root)),
        "chunk_count": len(chunks),
        "files": current_file_state(kb_root),
        "policy": "derived_rebuildable_not_canonical",
    }


def build_json_index(kb_root: Path, chunks: List[Chunk], allow_write: bool, dry_run: bool) -> List[Dict[str, Any]]:
    index_dir = kb_root / INDEX_DIR
    rows = [asdict(c) for c in chunks]
    writes = []
    writes.append(write_text(index_dir / JSON_NAME, json.dumps(rows, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, allow_write, dry_run))
    ndjson = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows)
    writes.append(write_text(index_dir / NDJSON_NAME, ndjson, kb_root, allow_write, dry_run))
    return writes


def build_sqlite_index(kb_root: Path, chunks: List[Chunk], allow_write: bool, dry_run: bool) -> Dict[str, Any]:
    index_dir = kb_root / INDEX_DIR
    db_path = index_dir / SQLITE_NAME
    ensure_inside(kb_root, db_path)
    fts = probe_fts5()
    result: Dict[str, Any] = {"fts5": fts, "db_path": relpath(kb_root, db_path), "written": False, "skipped": False}
    if not fts["fts5_available"]:
        result["skipped"] = True
        result["reason"] = "fts5_unavailable"
        return result
    if not allow_write or dry_run:
        result["skipped"] = True
        result["reason"] = "dry_run"
        return result
    index_dir.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(
            """
            DROP TABLE IF EXISTS documents;
            DROP TABLE IF EXISTS chunks_fts;
            CREATE TABLE documents (
              chunk_id TEXT PRIMARY KEY,
              kb_slug TEXT NOT NULL,
              rel_path TEXT NOT NULL,
              title TEXT NOT NULL,
              page_type TEXT NOT NULL,
              status TEXT NOT NULL,
              confidence TEXT NOT NULL,
              claim_label TEXT NOT NULL,
              heading TEXT NOT NULL,
              heading_level INTEGER NOT NULL,
              start_line INTEGER NOT NULL,
              end_line INTEGER NOT NULL,
              page_hash TEXT NOT NULL,
              source_mtime REAL NOT NULL
            );
            CREATE VIRTUAL TABLE chunks_fts USING fts5(
              chunk_id UNINDEXED,
              title,
              heading,
              body,
              tokenize = 'unicode61'
            );
            """
        )
        doc_rows = [
            (
                c.chunk_id,
                c.kb_slug,
                c.rel_path,
                c.title,
                c.page_type,
                c.status,
                c.confidence,
                c.claim_label,
                c.heading,
                c.heading_level,
                c.start_line,
                c.end_line,
                c.page_hash,
                c.source_mtime,
            )
            for c in chunks
        ]
        conn.executemany("INSERT INTO documents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", doc_rows)
        conn.executemany("INSERT INTO chunks_fts(chunk_id,title,heading,body) VALUES (?,?,?,?)", [(c.chunk_id, c.title, c.heading, c.text) for c in chunks])
        conn.commit()
        result["written"] = True
        result["chunk_count"] = len(chunks)
    finally:
        conn.close()
    return result


def cmd_health(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    return {
        "command": "health",
        "kb_root": str(kb_root),
        "kb_root_exists": kb_root.exists(),
        "python_version": sys.version.split()[0],
        "tools": detect_tools(),
        "optional_modules": detect_optional_modules(),
        "sqlite": probe_fts5(),
        "derived_search_dir": str(kb_root / INDEX_DIR),
    }


def cmd_build_index(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    chunks = collect_chunks(kb_root)
    writes = build_json_index(kb_root, chunks, args.allow_write, dry_run)
    sqlite_result = build_sqlite_index(kb_root, chunks, args.allow_write, dry_run)
    meta = index_meta(kb_root, chunks, "sqlite_fts5" if sqlite_result.get("written") else "json_fallback")
    writes.append(write_text(kb_root / INDEX_DIR / META_NAME, json.dumps(meta, indent=2, ensure_ascii=False, sort_keys=True) + "\n", kb_root, args.allow_write, dry_run))
    return {
        "command": "build-index",
        "kb_root": str(kb_root),
        "dry_run": dry_run,
        "allow_write": args.allow_write,
        "page_count": len(current_file_state(kb_root)),
        "chunk_count": len(chunks),
        "writes": writes,
        "sqlite": sqlite_result,
    }


def load_meta(kb_root: Path) -> Optional[Dict[str, Any]]:
    meta_path = kb_root / INDEX_DIR / META_NAME
    if not meta_path.exists():
        return None
    try:
        return json.loads(read_text(meta_path))
    except Exception:
        return None


def stale_report(kb_root: Path) -> Dict[str, Any]:
    meta = load_meta(kb_root)
    current = current_file_state(kb_root)
    if not meta or not isinstance(meta.get("files"), dict):
        return {"status": "missing", "added": sorted(current), "deleted": [], "modified": [], "message": "index metadata missing or unreadable"}
    old = meta["files"]
    old_keys = set(old)
    new_keys = set(current)
    added = sorted(new_keys - old_keys)
    deleted = sorted(old_keys - new_keys)
    modified = sorted(k for k in old_keys & new_keys if old.get(k, {}).get("hash") != current.get(k, {}).get("hash"))
    status = "stale" if added or deleted or modified else "fresh"
    return {"status": status, "added": added, "deleted": deleted, "modified": modified, "generated_at": meta.get("generated_at")}


def cmd_stale(args: argparse.Namespace) -> Dict[str, Any]:
    return {"command": "stale", "kb_root": str(resolve_kb_root(args.kb_root)), **stale_report(resolve_kb_root(args.kb_root))}


def load_json_chunks(kb_root: Path) -> List[Dict[str, Any]]:
    path = kb_root / INDEX_DIR / JSON_NAME
    if not path.exists():
        return [asdict(c) for c in collect_chunks(kb_root)]
    try:
        data = json.loads(read_text(path))
        if isinstance(data, list):
            return [x for x in data if isinstance(x, dict)]
    except Exception:
        pass
    return [asdict(c) for c in collect_chunks(kb_root)]


def query_terms(query: str) -> List[str]:
    return [t.lower() for t in re.findall(r"[A-Za-z0-9_]+", query) if len(t) > 1]


def fts_query_string(query: str) -> str:
    terms = query_terms(query)
    if not terms:
        return '"' + query.replace('"', ' ') + '"'
    return " OR ".join(f'"{t}"' for t in terms[:12])


def make_snippet(text: str, terms: Sequence[str], radius: int = 140) -> str:
    compact = re.sub(r"\s+", " ", text).strip()
    if not compact:
        return ""
    lower = compact.lower()
    positions = [lower.find(t.lower()) for t in terms if lower.find(t.lower()) >= 0]
    pos = min(positions) if positions else 0
    start = max(0, pos - radius)
    end = min(len(compact), pos + radius)
    prefix = "... " if start > 0 else ""
    suffix = " ..." if end < len(compact) else ""
    return prefix + compact[start:end] + suffix


def query_sqlite(kb_root: Path, query: str, limit: int) -> Tuple[bool, List[Dict[str, Any]], Optional[str]]:
    db_path = kb_root / INDEX_DIR / SQLITE_NAME
    if not db_path.exists() or not probe_fts5()["fts5_available"]:
        return False, [], "sqlite_fts5_unavailable_or_index_missing"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    match = fts_query_string(query)
    sql = """
        SELECT d.chunk_id, d.kb_slug, d.rel_path, d.title, d.page_type, d.status,
               d.confidence, d.claim_label, d.heading, d.start_line, d.end_line,
               bm25(chunks_fts) AS score,
               snippet(chunks_fts, 3, '[', ']', ' ... ', 28) AS snippet
        FROM chunks_fts
        JOIN documents d ON d.chunk_id = chunks_fts.chunk_id
        WHERE chunks_fts MATCH ?
        ORDER BY score
        LIMIT ?
    """
    try:
        rows = [dict(r) for r in conn.execute(sql, (match, limit)).fetchall()]
        return True, rows, None
    except Exception as exc:
        return False, [], str(exc)
    finally:
        conn.close()


def query_fallback(kb_root: Path, query: str, limit: int) -> List[Dict[str, Any]]:
    chunks = load_json_chunks(kb_root)
    terms = query_terms(query)
    scored: List[Tuple[float, Dict[str, Any]]] = []
    for row in chunks:
        text = str(row.get("text", ""))
        hay_body = text.lower()
        hay_heading = (str(row.get("title", "")) + " " + str(row.get("heading", ""))).lower()
        score = 0.0
        for term in terms:
            score += hay_heading.count(term) * 4
            score += hay_body.count(term)
        if score > 0 or not terms:
            out = {k: row.get(k) for k in ["chunk_id", "kb_slug", "rel_path", "title", "page_type", "status", "confidence", "claim_label", "heading", "start_line", "end_line"]}
            out["score"] = score
            out["snippet"] = make_snippet(text, terms)
            scored.append((score, out))
    scored.sort(key=lambda x: (-x[0], str(x[1].get("rel_path", "")), int(x[1].get("start_line") or 0)))
    return [row for _, row in scored[:limit]]


def query_kb(kb_root: Path, query: str, limit: int = 8, prefer_fts: bool = True) -> Dict[str, Any]:
    stale = stale_report(kb_root)
    backend = "json_fallback"
    error = None
    results: List[Dict[str, Any]] = []
    if prefer_fts:
        used, rows, error = query_sqlite(kb_root, query, limit)
        if used:
            backend = "sqlite_fts5_bm25"
            results = rows
        else:
            results = query_fallback(kb_root, query, limit)
    else:
        results = query_fallback(kb_root, query, limit)
    return {
        "query": query,
        "kb_slug": kb_root.name,
        "backend": backend,
        "stale": stale,
        "result_count": len(results),
        "results": results,
        "fallback_error": error,
        "generated_at": utc_now(),
        "policy": "read_only; derived indexes are not canonical",
    }


def save_query_packet(kb_root: Path, packet: Dict[str, Any], allow_write: bool, dry_run: bool, output: Optional[str] = None) -> Dict[str, Any]:
    query_slug = slugify(str(packet.get("query", "query")))[:80]
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rel_out = Path(output) if output else QUERY_DIR / f"{stamp}-{query_slug}.md"
    path = kb_root / rel_out
    lines = [
        "---",
        f'title: "Query: {packet.get("query", "")}"',
        "page_type: query_output",
        f'kb_slug: "{kb_root.name}"',
        f'created_at: "{packet.get("generated_at", utc_now())}"',
        'confidence: "unknown"',
        'claim_label: "source_backed_summary"',
        'status: "active"',
        "---",
        "",
        f"# Query: {packet.get('query', '')}",
        "",
        f"- KB: `{kb_root.name}`",
        f"- Backend: `{packet.get('backend')}`",
        f"- Stale status: `{packet.get('stale', {}).get('status')}`",
        f"- Generated: `{packet.get('generated_at')}`",
        "",
        "## Evidence results",
        "",
    ]
    for idx, row in enumerate(packet.get("results", []), start=1):
        lines.extend(
            [
                f"### {idx}. {row.get('title') or row.get('rel_path')}",
                "",
                f"- Path: `{row.get('rel_path')}`",
                f"- Heading: `{row.get('heading')}`",
                f"- Lines: `{row.get('start_line')}-{row.get('end_line')}`",
                f"- Confidence: `{row.get('confidence')}`",
                f"- Claim label: `{row.get('claim_label')}`",
                "",
                "> " + str(row.get("snippet", "")).replace("\n", " "),
                "",
            ]
        )
    lines.extend(["## Raw JSON", "", "```json", json.dumps(packet, indent=2, ensure_ascii=False, sort_keys=True), "```", ""])
    return write_text(path, "\n".join(lines), kb_root, allow_write, dry_run)


def cmd_query(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    packet = query_kb(kb_root, args.query, args.limit, prefer_fts=not args.no_fts)
    if args.save or args.output:
        packet["saved_query_output"] = save_query_packet(kb_root, packet, args.allow_write, dry_run, args.output)
    return packet


def cmd_export(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    chunks = [asdict(c) for c in collect_chunks(kb_root)]
    if args.format == "json":
        text = json.dumps(chunks, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        name = JSON_NAME
    else:
        text = "".join(json.dumps(c, ensure_ascii=False, sort_keys=True) + "\n" for c in chunks)
        name = NDJSON_NAME
    out = Path(args.output) if args.output else INDEX_DIR / name
    write = write_text(kb_root / out, text, kb_root, args.allow_write, dry_run)
    return {"command": "export", "kb_root": str(kb_root), "format": args.format, "chunk_count": len(chunks), "write": write, "dry_run": dry_run}


def cmd_clear_index(args: argparse.Namespace) -> Dict[str, Any]:
    kb_root = resolve_kb_root(args.kb_root)
    dry_run = effective_dry_run(args)
    if args.confirm_clear_index != "clear derived search index":
        return {"command": "clear-index", "status": "blocked", "required_confirmation": "clear derived search index", "dry_run": dry_run}
    files = [kb_root / INDEX_DIR / SQLITE_NAME, kb_root / INDEX_DIR / JSON_NAME, kb_root / INDEX_DIR / NDJSON_NAME, kb_root / INDEX_DIR / META_NAME]
    return {"command": "clear-index", "dry_run": dry_run, "results": [remove_file(f, kb_root, args.allow_write, dry_run) for f in files], "policy": "derived_only_canonical_untouched"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Apex KB local retrieval over compiled wiki pages")
    parser.add_argument("--kb-root", required=True, help="Path to one KB root, e.g. apex-meta/kb/<kb-slug>/")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    parser.add_argument("--allow-write", action="store_true", help="Permit deterministic writes inside kb_root")
    parser.add_argument("--dry-run", action="store_true", help="Preview writes even when --allow-write is present")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("health", help="Probe sqlite3/FTS5 and optional modules").set_defaults(func=cmd_health)
    sub.add_parser("build-index", help="Build derived JSON index and SQLite FTS5 index when available").set_defaults(func=cmd_build_index)
    sub.add_parser("stale", help="Compare wiki page hashes to index metadata").set_defaults(func=cmd_stale)

    q = sub.add_parser("query", help="Query compiled wiki chunks")
    q.add_argument("--query", required=True)
    q.add_argument("--limit", type=int, default=8)
    q.add_argument("--save", action="store_true", help="Save markdown query packet under outputs/queries")
    q.add_argument("--output", help="Optional output path relative to kb_root for saved query packet")
    q.add_argument("--no-fts", action="store_true", help="Force JSON fallback search")
    q.set_defaults(func=cmd_query)

    ex = sub.add_parser("export", help="Export deterministic chunk index")
    ex.add_argument("--format", choices=["json", "ndjson"], default="json")
    ex.add_argument("--output", help="Output path relative to kb_root; defaults to derived/search")
    ex.set_defaults(func=cmd_export)

    clear = sub.add_parser("clear-index", help="Remove derived search index files only")
    clear.add_argument("--confirm-clear-index", default="")
    clear.set_defaults(func=cmd_clear_index)
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = args.func(args)
        emit(args, result)
        status = result.get("status") if isinstance(result, dict) else None
        if status in {"blocked", "error"}:
            return 2
        return 0
    except SystemExit:
        raise
    except Exception as exc:
        error = {"command": getattr(args, "command", "unknown"), "status": "error", "error": str(exc)}
        emit(args, error)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
