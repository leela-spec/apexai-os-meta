from __future__ import annotations

import json
import os
import re
import sqlite3
import tempfile
from pathlib import Path
from typing import Any

from ..errors import ApexKBError
from ..io import atomic_json, atomic_text, canonical_hash, load_json, sha256_file, utc_now, utc_stamp, validate_schema

INDEX_SCHEMA = "apex.kb.retrieval-index.v2"
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
TOKEN_RE = re.compile(r"[^\W_]+(?:[-'][^\W_]+)*", re.UNICODE)
SOURCE_ID_RE = re.compile(r"\bsrc-[a-f0-9]{16}\b")


def _strip_frontmatter(lines: list[str]) -> tuple[list[str], int]:
    if not lines or lines[0].strip() != "---":
        return lines, 1
    for index in range(1, min(len(lines), 400)):
        if lines[index].strip() in {"---", "..."}:
            return lines[index + 1 :], index + 2
    return lines, 1


def _page_meta(text: str, path: Path) -> dict[str, str]:
    lines = text.splitlines()
    meta: dict[str, str] = {"title": path.stem, "topic_id": "unknown", "page_type": "page"}
    if lines and lines[0].strip() == "---":
        for line in lines[1:200]:
            if line.strip() in {"---", "..."}:
                break
            if ":" in line:
                key, value = line.split(":", 1)
                if key.strip() in meta:
                    meta[key.strip()] = value.strip().strip('"\'')
    return meta


def _frontmatter_status(text: str) -> str | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:200]:
        if line.strip() in {"---", "..."}:
            return None
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        if key.strip() == "status":
            return value.strip().strip('"\'')
    return None


def _chunks(path: Path, run_root: Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8")
    meta = _page_meta(text, path)
    raw_lines = text.splitlines()
    lines, first_line = _strip_frontmatter(raw_lines)
    page_hash = sha256_file(path)
    page_source_pointers = sorted(set(SOURCE_ID_RE.findall(text)))
    chunks: list[dict[str, Any]] = []
    current_heading = meta["title"]
    current_level = 1
    current_start = first_line
    body: list[str] = []

    def flush(end_line: int) -> None:
        content = "\n".join(body).strip()
        if not content:
            return
        local_pointers = sorted(set(SOURCE_ID_RE.findall(content))) or page_source_pointers
        chunks.append(
            {
                "chunk_id": canonical_hash({"path": str(path.relative_to(run_root)), "heading": current_heading, "start": current_start})[:24],
                "path": str(path.relative_to(run_root)).replace("\\", "/"),
                "topic_id": meta["topic_id"],
                "page_type": meta["page_type"],
                "title": meta["title"],
                "heading": current_heading,
                "heading_level": current_level,
                "start_line": current_start,
                "end_line": end_line,
                "body": content,
                "content_hash": canonical_hash(content),
                "page_hash": page_hash,
                "source_pointers": local_pointers,
            }
        )

    for offset, line in enumerate(lines, first_line):
        match = HEADING_RE.match(line)
        if match:
            flush(offset - 1)
            body = []
            current_heading = match.group(2).strip()
            current_level = len(match.group(1))
            current_start = offset
        else:
            body.append(line)
    flush(len(raw_lines))
    if not chunks and text.strip():
        chunks.append(
            {
                "chunk_id": canonical_hash({"path": str(path.relative_to(run_root)), "heading": meta["title"], "start": 1})[:24],
                "path": str(path.relative_to(run_root)).replace("\\", "/"),
                "topic_id": meta["topic_id"],
                "page_type": meta["page_type"],
                "title": meta["title"],
                "heading": meta["title"],
                "heading_level": 1,
                "start_line": 1,
                "end_line": len(raw_lines),
                "body": text,
                "content_hash": canonical_hash(text),
                "page_hash": page_hash,
                "source_pointers": page_source_pointers,
            }
        )
    return chunks

def _accepted_pages(run_root: Path, manifest: dict[str, Any], accepted_topic_ids: list[str]) -> list[Path]:
    pages: list[Path] = []
    topics = {item["topic_id"]: item for item in manifest["topics"]}
    for topic_id in accepted_topic_ids:
        topic = topics.get(topic_id)
        if not topic:
            raise ApexKBError("accepted_topic_unknown", f"Accepted topic is not in manifest: {topic_id}")
        for route in topic["expected_routes"].values():
            path = run_root / route
            if not path.is_file():
                raise ApexKBError("accepted_page_missing", f"Accepted compiled page is missing: {path}")
            if _frontmatter_status(path.read_text(encoding="utf-8")) != "accepted":
                raise ApexKBError("page_not_accepted", f"Retrieval may index only semantically accepted pages: {path}")
            pages.append(path)
    return sorted(set(pages))


def build_retrieval(run_root: Path, manifest: dict[str, Any], accepted_topic_ids: list[str]) -> dict[str, Any]:
    accepted_topic_ids = sorted(set(accepted_topic_ids))
    pages = _accepted_pages(run_root, manifest, accepted_topic_ids)
    chunks = [chunk for page in pages for chunk in _chunks(page, run_root)]
    chunks.sort(key=lambda item: (item["path"], item["start_line"], item["chunk_id"]))
    derived = run_root / "derived" / "search"
    derived.mkdir(parents=True, exist_ok=True)
    db_path = derived / "search.sqlite"
    fd, temp_name = tempfile.mkstemp(prefix=".search.", suffix=".sqlite", dir=derived)
    os.close(fd)
    temp_path = Path(temp_name)
    try:
        try:
            connection = sqlite3.connect(temp_path)
            try:
                connection.executescript(
                    """
                    PRAGMA journal_mode=DELETE;
                    PRAGMA synchronous=FULL;
                    PRAGMA auto_vacuum=NONE;
                    PRAGMA page_size=4096;
                    CREATE TABLE metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL) WITHOUT ROWID;
                    CREATE VIRTUAL TABLE chunks_fts USING fts5(
                        chunk_id UNINDEXED,
                        path UNINDEXED,
                        topic_id UNINDEXED,
                        page_type UNINDEXED,
                        start_line UNINDEXED,
                        end_line UNINDEXED,
                        heading_level UNINDEXED,
                        page_hash UNINDEXED,
                        source_pointers UNINDEXED,
                        title,
                        heading,
                        body,
                        content_hash UNINDEXED,
                        tokenize='porter unicode61'
                    );
                    """
                )
                connection.executemany(
                    "INSERT INTO chunks_fts(chunk_id,path,topic_id,page_type,start_line,end_line,heading_level,page_hash,source_pointers,title,heading,body,content_hash) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    [
                        (
                            item["chunk_id"], item["path"], item["topic_id"], item["page_type"],
                            item["start_line"], item["end_line"], item["heading_level"], item["page_hash"],
                            json.dumps(item["source_pointers"], ensure_ascii=False, separators=(",", ":")),
                            item["title"], item["heading"], item["body"], item["content_hash"],
                        )
                        for item in chunks
                    ],
                )
                metadata = {
                    "schema": INDEX_SCHEMA,
                    "run_id": manifest["run_id"],
                    "config_hash": manifest["config_hash"],
                    "built_at": manifest["created_at"],
                    "page_count": len(pages),
                    "chunk_count": len(chunks),
                    "backend": "sqlite_fts5",
                }
                connection.executemany(
                    "INSERT INTO metadata(key,value) VALUES(?,?)",
                    [(key, json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))) for key, value in sorted(metadata.items())],
                )
                connection.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('optimize')")
                connection.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('integrity-check')")
                connection.commit()
                connection.execute("VACUUM")
            finally:
                connection.close()
        except sqlite3.Error as exc:
            raise ApexKBError(
                "fts5_unavailable",
                f"SQLite FTS5 is unavailable or failed during index creation: {exc}",
            ) from exc
        os.replace(temp_path, db_path)
    finally:
        temp_path.unlink(missing_ok=True)
    page_hashes = {str(page.relative_to(run_root)).replace("\\", "/"): sha256_file(page) for page in pages}
    index_manifest = {
        "schema": INDEX_SCHEMA,
        "backend": "sqlite_fts5",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "built_at": manifest["created_at"],
        "database_path": str(db_path.relative_to(run_root)).replace("\\", "/"),
        "database_sha256": sha256_file(db_path),
        "accepted_topics": accepted_topic_ids,
        "page_hashes": page_hashes,
        "page_count": len(pages),
        "chunk_count": len(chunks),
        "fts5": True,
        "derived_rebuildable": True,
        "canonical_markdown_preserved": True,
    }
    atomic_json(derived / "index-manifest.json", index_manifest)
    index_lines = ["# Apex KB index", "", f"Generated from accepted pages for run `{manifest['run_id']}`.", ""]
    for topic_id in accepted_topic_ids:
        topic = next(item for item in manifest["topics"] if item["topic_id"] == topic_id)
        index_lines.extend([f"## {topic['name']}", "", f"- [{topic['name']}]({Path(topic['expected_routes']['dossier']).relative_to('wiki').as_posix()})", f"- [Source atlas]({Path(topic['expected_routes']['source_atlas']).relative_to('wiki').as_posix()})", ""])
    atomic_text(run_root / "wiki" / "index.md", "\n".join(index_lines))
    health = retrieval_health(run_root)
    if not health["fresh"] or not health["integrity_ok"]:
        raise ApexKBError("retrieval_build_invalid", "Derived retrieval index did not pass freshness and integrity checks", health)
    result = {
        "schema": "apex.kb.stage-result.v2",
        "run_id": manifest["run_id"],
        "config_hash": manifest["config_hash"],
        "stage": "retrieval",
        "status": "completed",
        "started_at": manifest["created_at"],
        "completed_at": manifest["created_at"],
        "artifacts": [str(db_path.relative_to(run_root)), "derived/search/index-manifest.json", "wiki/index.md"],
        "reason_code": None,
        "message": f"Indexed {len(chunks)} heading sections from {len(pages)} accepted pages.",
        "metrics": health,
    }
    validate_schema(result, "stage-result.schema.json")
    atomic_json(run_root / manifest["artifact_layout"]["stage_results"] / "retrieval.json", result)
    return {"manifest": index_manifest, "health": health, "result": result}

def retrieval_health(run_root: Path) -> dict[str, Any]:
    manifest_path = run_root / "derived" / "search" / "index-manifest.json"
    db_path = run_root / "derived" / "search" / "search.sqlite"
    if not manifest_path.is_file() or not db_path.is_file():
        return {"available": False, "fresh": False, "integrity_ok": False, "reason": "index_missing"}
    index = load_json(manifest_path)
    changed = []
    missing = []
    current_manifest_path = run_root / "run-manifest.json"
    current_manifest = load_json(current_manifest_path) if current_manifest_path.is_file() else {}
    run_identity_matches = (
        index.get("run_id") == current_manifest.get("run_id")
        and index.get("config_hash") == current_manifest.get("config_hash")
    )
    for relative, expected in index.get("page_hashes", {}).items():
        path = run_root / relative
        if not path.is_file():
            missing.append(relative)
        elif sha256_file(path) != expected:
            changed.append(relative)
    database_sha256_matches = sha256_file(db_path) == index.get("database_sha256")
    sqlite_integrity_ok = False
    sqlite_integrity_result: list[str] = []
    fts5_healthy = False
    metadata_matches = False
    embedded_metadata: dict[str, Any] = {}
    row_count = None
    error = None
    try:
        connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        try:
            sqlite_integrity_result = [str(row[0]) for row in connection.execute("PRAGMA integrity_check").fetchall()]
            sqlite_integrity_ok = sqlite_integrity_result == ["ok"]
            embedded_metadata = {
                str(key): json.loads(value)
                for key, value in connection.execute("SELECT key, value FROM metadata ORDER BY key").fetchall()
            }
            expected_metadata = {
                "schema": index.get("schema"),
                "run_id": index.get("run_id"),
                "config_hash": index.get("config_hash"),
                "built_at": index.get("built_at"),
                "page_count": index.get("page_count"),
                "chunk_count": index.get("chunk_count"),
                "backend": index.get("backend"),
            }
            metadata_matches = embedded_metadata == expected_metadata
            row_count = connection.execute("SELECT count(*) FROM chunks_fts").fetchone()[0]
            fts_definition = connection.execute(
                "SELECT sql FROM sqlite_master WHERE type='table' AND name='chunks_fts'"
            ).fetchone()
            connection.execute("SELECT rowid FROM chunks_fts WHERE chunks_fts MATCH ? LIMIT 1", ("apex",)).fetchall()
            fts5_healthy = bool(fts_definition and "USING fts5" in str(fts_definition[0]))
        finally:
            connection.close()
    except (json.JSONDecodeError, sqlite3.Error) as exc:
        error = str(exc)
    deterministic_identity_matches = database_sha256_matches and metadata_matches
    integrity_ok = (
        sqlite_integrity_ok
        and fts5_healthy
        and row_count == index.get("chunk_count")
        and deterministic_identity_matches
    )
    return {
        "available": True,
        "fresh": run_identity_matches and not changed and not missing and deterministic_identity_matches,
        "integrity_ok": integrity_ok,
        "run_identity_matches": run_identity_matches,
        "database_sha256_matches": database_sha256_matches,
        "deterministic_identity_matches": deterministic_identity_matches,
        "metadata_matches": metadata_matches,
        "embedded_metadata": embedded_metadata,
        "sqlite_integrity_ok": sqlite_integrity_ok,
        "sqlite_integrity_result": sqlite_integrity_result,
        "fts5_healthy": fts5_healthy,
        "changed_pages": changed,
        "missing_pages": missing,
        "row_count": row_count,
        "expected_row_count": index.get("chunk_count"),
        "error": error,
    }


def _fts_query(text: str) -> str:
    terms = [match.group(0) for match in TOKEN_RE.finditer(text) if len(match.group(0)) > 1]
    if not terms:
        raise ApexKBError("query_empty", "Query contains no searchable terms")
    return " OR ".join('"' + term.replace('"', '""') + '"' for term in terms[:30])


def query_retrieval(run_root: Path, query: str, limit: int = 8, allow_stale: bool = False, topic_id: str | None = None) -> dict[str, Any]:
    health = retrieval_health(run_root)
    if not health["available"]:
        raise ApexKBError("retrieval_missing", "Retrieval index is not available", health)
    if (not health["fresh"] or not health["integrity_ok"]) and not allow_stale:
        raise ApexKBError("retrieval_stale", "Retrieval index is stale or unhealthy; rebuild before reliance", health)
    db_path = run_root / "derived" / "search" / "search.sqlite"
    index_manifest = load_json(run_root / "derived" / "search" / "index-manifest.json")
    run_manifest = load_json(run_root / "run-manifest.json")
    topics = {item["topic_id"]: item for item in run_manifest["topics"]}
    match = _fts_query(query)
    sql = """
        SELECT chunk_id, path, topic_id, page_type, start_line, end_line, heading_level,
               page_hash, source_pointers, title, heading,
               snippet(chunks_fts, 11, '[', ']', ' … ', 24) AS excerpt,
               bm25(chunks_fts, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 3.0, 1.0, 0.0) AS score
        FROM chunks_fts
        WHERE chunks_fts MATCH ?
    """
    parameters: list[Any] = [match]
    if topic_id:
        sql += " AND topic_id = ?"
        parameters.append(topic_id)
    sql += " ORDER BY score, path, start_line LIMIT ?"
    parameters.append(max(1, min(limit, 100)))
    connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = [dict(row) for row in connection.execute(sql, parameters).fetchall()]
    except sqlite3.Error as exc:
        raise ApexKBError("retrieval_query_failed", f"FTS5 query failed: {exc}") from exc
    finally:
        connection.close()
    for row in rows:
        try:
            row["source_pointers"] = json.loads(row["source_pointers"] or "[]")
        except json.JSONDecodeError:
            row["source_pointers"] = []
        topic = topics.get(row["topic_id"])
        row["source_atlas_path"] = topic["expected_routes"]["source_atlas"] if topic else None
        row["evidence_pointer"] = f"{row['path']}#L{row['start_line']}-L{row['end_line']}"
    result = {
        "schema": "apex.kb.query-result.v2",
        "backend": "sqlite_fts5",
        "query": query,
        "topic_id": topic_id,
        "created_at": utc_now(),
        "run_id": index_manifest["run_id"],
        "config_hash": index_manifest["config_hash"],
        "index_manifest_path": "derived/search/index-manifest.json",
        "index_database_sha256": index_manifest["database_sha256"],
        "retrieval_fresh": health["fresh"],
        "result_count": len(rows),
        "raw_source_reopen_guidance": "Use the accepted dossier and source atlas first. Reopen raw sources only when the answer is absent, acceptance marks insufficient evidence, or source drift invalidates the compiled pages.",
        "results": rows,
    }
    output_root = run_root / "outputs" / "queries"
    stem = f"{utc_stamp()}-{canonical_hash({'query': query, 'topic': topic_id})[:10]}"
    json_path = output_root / f"{stem}.json"
    markdown_path = output_root / f"{stem}.md"
    result["output_paths"] = [str(json_path.relative_to(run_root)), str(markdown_path.relative_to(run_root))]
    atomic_json(json_path, result)
    lines = [
        f"# Query — {query}", "",
        f"- Backend: **sqlite_fts5**", f"- Run: `{result['run_id']}`", f"- Config: `{result['config_hash']}`",
        f"- Retrieval fresh: **{health['fresh']}**", f"- Results: **{len(rows)}**", "",
        result["raw_source_reopen_guidance"], "",
    ]
    for index, row in enumerate(rows, 1):
        lines.extend([
            f"## {index}. {row['title']} — {row['heading']}", "",
            f"- Evidence: `{row['evidence_pointer']}`", f"- Page hash: `{row['page_hash']}`",
            f"- Topic: `{row['topic_id']}`", f"- Source atlas: `{row['source_atlas_path']}`",
            f"- Source pointers: {', '.join(f'`{item}`' for item in row['source_pointers']) or 'None recorded'}",
            f"- BM25 score: `{row['score']}`", "", row["excerpt"], "",
        ])
    atomic_text(markdown_path, "\n".join(lines))
    return result
