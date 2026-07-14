# Apex KB / Query / Retrieval Integration — Final Patch Pack

## Executive verdict

The best production-ready path for Apex is a **hybrid local retrieval architecture**:

- **canonical sources stay in markdown pages, source manifests, and raw source snapshots**
- **derived search indexes are built locally in SQLite FTS5**
- **the retrieval boundary stays inside `apex-kb` as a script contract**, not a separate top-level skill
- **index scope is hybrid**: per-KB indexes for locality and determinism, plus an optional global cross-KB index for orchestration and parent-memory routing
- **chunking should be heading-section based**, with page-level fallback for short pages
- **query output should be dual-format**: machine-readable JSON plus a human-auditable markdown artifact

That architecture is the strongest fit because SQLite FTS5 already provides the exact production primitives Apex needs for local retrieval: `MATCH`-based full-text search, BM25 ranking, tokenizer configuration, `highlight()`/`snippet()` support for readable excerpts, and deterministic on-disk rebuilds through the Python stdlib `sqlite3` module. At the same time, SQLite/FTS5 availability is not universal across every Python/SQLite build, so the production design must include explicit runtime probing and health checks instead of assuming support. citeturn13view0turn10view0turn10view2turn10view3turn10view4turn9view1turn11view1

I could **not** read the selected repository through public GitHub web endpoints in this run. The repository root URL returned 404, and a direct raw-file request for `.claude/Claude.md` also returned 404. Because of that, all explicitly listed repo paths must be treated as **unavailable in this run**, and any repo-specific patch anchoring against current file contents is necessarily **unverified**. I am therefore providing the strongest possible **patch-ready file pack** with explicit replacement/addition sections, while clearly separating verified external evidence from repo-inaccessible assumptions. citeturn5view0turn4view0

## Source-read ledger and current Apex state map

### Source-read ledger

The selected GitHub repository could not be opened from its public web URL in this run, so the following explicitly listed repository paths are marked **unavailable**:

- `.claude/Claude.md`
- `.claude/skills/apex-kb/SKILL.md`
- `.claude/skills/apex-kb/package-manifest.md`
- `.claude/skills/apex-kb/references/kb-contract.md`
- `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`
- `.claude/skills/apex-kb/references/script-command-contract.md`
- `.claude/skills/apex-kb/templates/ingest-analysis-template.md`
- `.claude/skills/apex-kb/templates/wiki-page-templates.md`
- `apex-meta/scripts/apex_kb.py`
- targeted KB sample paths under `apex-meta/kb/*/...`
- targeted orchestration-surface paths under `.claude/skills/apex-plan/`, `.claude/skills/apex-sync/`, `.claude/skills/apex-session/`, `.claude/skills/PrecapNextDay/`, and `.claude/skills/PrecapWeek/`

That unavailable status is grounded in the failed repository-root fetch and the failed direct raw-file fetch. citeturn5view0turn4view0

| source_id | repo_or_file_origin | exact_path | lines_or_sections_read | read_status | extracted_mechanism | copy_adapt_decision | reason |
|---|---|---|---|---|---|---|---|
| apex-repo-root-probe | selected repo | `https://github.com/leela-spec/apexai-os-meta` | root fetch | unavailable | repository public web entrypoint unavailable | OMIT | cannot use as evidence in this run citeturn5view0 |
| apex-claude-md-probe | selected repo | `https://raw.githubusercontent.com/leela-spec/apexai-os-meta/main/.claude/Claude.md` | direct file fetch | unavailable | explicit file probe failed | OMIT | cannot use as evidence in this run citeturn4view0 |
| sqlite-fts5-core | SQLite official docs | `fts5.html` | query syntax, auxiliary functions, build notes | opened_and_read | MATCH queries, BM25, snippet/highlight, tokenizer config, build options | COPY / ADAPT | primary source for local full-text design citeturn13view0turn10view0turn10view2turn10view3turn10view4 |
| sqlite-compile-options | SQLite official docs | `compile.html` | overview, `PRAGMA compile_options` | opened_and_read | runtime validation for build flags | COPY | needed for FTS5 health probing citeturn11view1 |
| python-sqlite3 | Python official docs | `sqlite3` module docs | module overview and connect flow | opened_and_read | stdlib DB access path | COPY | avoids server/runtime sprawl citeturn9view1 |
| python-frontmatter-pypi | PyPI | `python-frontmatter` | project description and usage | opened_and_read | optional robust YAML/frontmatter parsing | ADAPT | useful as soft dependency, not mandatory citeturn9view3 |

### Current Apex state map

Because the repository itself was unavailable, the only trustworthy current-state inputs for Apex in this run are the **operator-supplied contract facts** in your prompt. From that contract, the important integration constraints are:

- Apex is a **Claude-native orchestration system**
- the orchestration loop is **PreCapWeek → PreCapNextDay → OperatorExecutesPlannedFlow → FlowRecap → APSU → next PreCapNextDay**
- the KB system must support **project KBs**, **cross-project parent memory**, and **personal orchestration memory as a first-class domain**
- retrieval must stay **source-grounded, auditable, deterministic, and non-mutating** with respect to task state

I am treating those statements as operator constraints, **not as repository evidence**.

## Blueprint mechanisms copied or adapted and final decisions

### Blueprint mechanisms copied or adapted

Even though repo-specific implementation blueprints were unavailable from the allowed GitHub scope in this run, the official SQLite and Python documentation still exposes the production mechanisms that matter most for the retrieval implementation.

| mechanism | source file | COPY / ADAPT / CONCEPT / OMIT | reason | target Apex file or behavior |
|---|---|---|---|---|
| FTS5 virtual table search via `MATCH` | SQLite FTS5 docs | COPY | core retrieval primitive, deterministic and local | `apex-meta/scripts/apex_kb_retrieval.py` query engine citeturn13view0 |
| BM25 ranking | SQLite FTS5 docs | COPY | ranked search without external vector infra | query ordering and scoring citeturn10view0 |
| `highlight()` / `snippet()` | SQLite FTS5 docs | COPY | human-auditable excerpts for Claude and operators | query output formatting citeturn10view2turn10view3 |
| configurable tokenizer using `porter unicode61` | SQLite FTS5 docs | ADAPT | good default for English-heavy markdown KBs with light stemming | FTS schema creation citeturn10view4 |
| runtime validation via `PRAGMA compile_options` and explicit FTS table probe | SQLite compile docs plus FTS build notes | COPY | production readiness requires proving FTS5 support, not assuming it | `health` command and startup checks citeturn11view1turn13view0 |
| stdlib SQLite access via `sqlite3` | Python docs | COPY | keeps deployment lightweight and local | Python script implementation citeturn9view1 |
| optional frontmatter dependency | PyPI `python-frontmatter` | ADAPT | gives robust YAML parsing when installed, but should not become a hard requirement | parser fallback chain citeturn9view3 |

### Final decisions

| decision | selected option | rejected options | evidence | confidence | risk | implementation consequence |
|---|---|---|---|---|---|---|
| D1 retrieval backend | **hybrid markdown manifest plus SQLite FTS5** | markdown-only, pure Python inverted index, mandatory vector | FTS5 already covers lexical ranking, snippets, tokenization, local rebuilds, and advanced operators. citeturn13view0turn10view0turn10view2turn10view3turn10view4turn9view1 | High | FTS5 build variance | implement health probe and fallback error path |
| D2 SQLite now or not | **yes, implement now** | postpone SQLite; vector now | SQLite is accessible through stdlib Python, and FTS5 is a mature local search engine when present. citeturn9view1turn13view0turn11view1 | High | some Python/SQLite builds may lack FTS5 | add `health` and `PRAGMA compile_options` validation |
| D3 skill boundary | **extend `apex-kb` with a retrieval script contract** | separate `apex-query` skill; script-only outside skill | retrieval belongs with KB ingestion, manifests, auditability, and source custody | Medium | repo docs unavailable, so exact wording anchors are unverified | create `apex_kb_retrieval.py` and append docs in `apex-kb` |
| D4 DB scope | **hybrid local plus global** | per-KB only; repo-global only; project-only only | per-KB gives locality and deterministic rebuild; global index supports cross-project routing and personal memory lookup | Medium | index fan-out if unmanaged | build per-KB by default, global on demand |
| D5 source of truth | **markdown pages + manifests + raw snapshots are canonical; SQLite is derived** | SQLite as canonical | derived DBs should always be rebuildable; shadow-table internals reinforce that FTS state is implementation detail, not canon. citeturn10view1turn9view0 | High | stale indexes | explicit stale checks and rebuild commands |
| D6 chunking unit | **heading section with page fallback** | page only; paragraph only; source-record only | aligns with markdown structure and yields better snippets than whole-page retrieval | Medium | some pages may have weak heading hygiene | fallback whole-page chunk for headingless pages |
| D7 metadata schema | **common core + domain fields** | one flat minimal schema | project, personal, and cross-project memory have different routing needs | Medium | schema drift | enforce shared required keys in docs and index tables |
| D8 frontmatter parser | **soft optional dependency plus stdlib fallback** | hard dependency, or stdlib-only absolutism | optional `python-frontmatter` is production/stable, but zero-dependency operation remains valuable. citeturn9view3turn9view1 | Medium | metadata edge cases if fallback parser used | fallback parser only supports simple frontmatter reliably |
| D9 output contract | **JSON + markdown artifact** | plain text only | Claude needs machine-readable structure; operators need auditable artifact | High | artifact sprawl | write under `outputs/queries/` with retention discipline |
| D10 orchestration integration | **read-only retrieval packets feeding planning/session skills** | task mutation from query | preserves control-plane separation | High | overloading query results into action state | retrieval outputs remain evidence packets, never state mutation |
| D11 scalability | **sufficient now for small and large KBs** | pure markdown grep; vector-first | FTS5 supports ranking, prefix/boolean/NEAR search, snippets, optimization, and merge behavior for larger indexes. citeturn13view0turn9view0 | High | cross-KB rebuild time | global index opt-in, per-KB default |
| D12 final patch surface | **new retrieval script + new contracts + append-only doc updates + `.gitignore`** | full repo rewrite | minimizes blast radius given missing repo access | Medium | exact anchors unverified | use additive patches where possible |

## Final architecture and integration map

### Final architecture

The final architecture has **three memory domains**:

1. **Project KBs**  
   One KB per project or compiled knowledge bundle. Each KB keeps markdown pages, wiki pages, and source manifests as canonical artifacts. Each KB gets its own derived SQLite index at `apex-meta/kb/<kb>/derived/search/index.sqlite`.

2. **Personal orchestration memory**  
   This remains a first-class domain, not collapsed into ordinary project KBs. It uses the exact same technical indexing pipeline, but carries `domain = personal_orchestration` so routing and query policies can treat it differently.

3. **Cross-project / parent memory**  
   This is served through an optional global index at `apex-meta/kb/.global/derived/search/index.sqlite`, built from multiple KBs. The global layer is for alignment, routing, status recall, and high-level orchestration prompts, not as a replacement for per-project custody.

The **source of truth** remains the file layer: markdown pages, source manifests, and raw-source snapshots. The SQLite database is a **derived cache** that can be rebuilt deterministically at any time. That is the right posture technically and operationally: FTS5 tables are implementation apparatus with shadow tables and optimization commands, not the place where canonical memory policy should live. citeturn10view1turn9view0

### Retrieval and index schema

SQLite is the selected backend, so the schema policy is:

- **per-KB DB path**: `apex-meta/kb/<kb>/derived/search/index.sqlite`
- **global DB path**: `apex-meta/kb/.global/derived/search/index.sqlite`
- **canonical files remain in place**
- **index rebuild is destructive-and-rebuildable**, never source-authoritative
- **health checks must prove FTS5 support before indexing**

`sqlite3` in the Python stdlib provides the local storage layer, while FTS5 provides ranking, tokenizer configuration, snippets, and auxiliary functions. citeturn9view1turn13view0turn10view0turn10view2turn10view3turn10view4

Recommended logical schema:

- `documents`
  - `id`
  - `kb_id`
  - `domain`
  - `rel_path`
  - `title`
  - `source_mtime`
  - `page_hash`
  - `indexed_at`

- `chunks`
  - `id`
  - `doc_id`
  - `ordinal`
  - `section_title`
  - `heading_path`
  - `anchor`
  - `body`
  - `token_count`

- FTS table
  - `title`
  - `heading_path`
  - `body`
  - tokenizer: `porter unicode61 remove_diacritics 1`

- optional diagnostics
  - `PRAGMA compile_options`
  - `fts5vocab(...)` when available for vocabulary health inspection and basic search QA. citeturn11view1turn10view1

Ranking behavior:

- primary sort by `bm25()`
- column weighting:
  - title weight high
  - heading path medium
  - body normal
- snippet generation from `snippet()`
- optional exact-match emphasis from result post-processing when query terms appear in titles/headings

SQLite’s BM25 implementation is intentionally inverted so better matches sort toward lower numeric scores with ascending order. That should be used directly rather than re-implementing ranking in Python. citeturn10view0

### Query flow and output contract

The query flow is:

1. resolve scope: one KB, personal memory KB, or global
2. verify index health and FTS5 availability
3. execute ranked FTS query
4. return:
   - JSON to stdout for downstream skill consumption
   - optional markdown artifact under `outputs/queries/`

The query output must include:

- query text
- scope and KB IDs
- run timestamp
- index path
- health/status flags
- ranked results with score
- `rel_path`
- `heading_path`
- `section_title`
- snippet
- canonical source path

That is the right shape for both Claude consumption and human audit because FTS5 can generate the compact evidence fragments directly through `snippet()` and `highlight()`. citeturn10view2turn10view3

### Final integration map

The retrieval system should feed other Apex surfaces **read-only**:

- **`apex-kb`**  
  owns ingestion, query, health, stale-check, and rebuild commands

- **`apex-plan`**  
  consumes project-specific query packets for planning context and open-decision recall

- **`apex-sync`**  
  consumes query packets that summarize latest status pages and evidence-bearing KB sections

- **`apex-session`**  
  uses retrieval packets to preload session-relevant context without over-reading whole KBs

- **`PreCapWeek`**  
  queries parent-memory and project KBs for weekly signal extraction

- **`PreCapNextDay`**  
  queries personal orchestration memory plus current project KBs for constraints, routines, and active context

- **`FlowRecap`**  
  writes new recap pages to canonical markdown, then calls index rebuild or stale-check

- **`APSU / StatusMerge`**  
  queries cross-project/global index for status synthesis, but never mutates task state from retrieval results

- **personal orchestration memory**  
  uses the same indexing pipeline, but query policy should prioritize recency and routine-oriented metadata

The hard rule is simple: **retrieval emits evidence packets; it never mutates plans, tasks, or control state directly**.

## Patch-ready file pack

Because the repository files were unavailable, I am using the safest practical patch style:

- **full contents for all new files**
- **append-only or replacement sections for existing files**
- **clear risk notes whenever exact current-file anchoring is unverified**

### File change plan

| path | create/update | reason | risk |
|---|---|---|---|
| `apex-meta/scripts/apex_kb_retrieval.py` | create | full retrieval/search implementation with SQLite FTS5 | low |
| `.claude/skills/apex-kb/references/retrieval-contract.md` | create | formalizes architecture, canonical-vs-derived rules, query output contract | low |
| `.claude/skills/apex-kb/templates/query-output-template.md` | create | standard markdown artifact template for query outputs | low |
| `.claude/skills/apex-kb/SKILL.md` | update | teach operators and Claude when/how to use query/index commands | medium because existing anchors unread |
| `.claude/skills/apex-kb/package-manifest.md` | update | register new retrieval assets | medium |
| `.claude/skills/apex-kb/references/kb-contract.md` | update | add canonical/derived and metadata requirements | medium |
| `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md` | update | add retrieval, stale-index, and non-mutation rules | medium |
| `.claude/skills/apex-kb/references/script-command-contract.md` | update | document new CLI surface | medium |
| `.gitignore` | update | ignore derived SQLite artifacts | low |
| `apex-meta/scripts/apex_kb.py` | update | optional delegation hook into new retrieval script | high because current command-parser structure unread |

### New file content for `apex-meta/scripts/apex_kb_retrieval.py`

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
KB_ROOT = REPO_ROOT / "apex-meta" / "kb"
GLOBAL_KB_ID = ".global"
IGNORED_PARTS = {"derived", "outputs", ".git", "__pycache__"}
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
SIMPLE_KV_RE = re.compile(r"^([A-Za-z0-9_.-]+)\s*:\s*(.*)$")
TOKENIZER = "porter unicode61 remove_diacritics 1"

SCHEMA_SQL = f"""
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS index_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY,
    kb_id TEXT NOT NULL,
    domain TEXT NOT NULL,
    rel_path TEXT NOT NULL,
    title TEXT NOT NULL,
    source_mtime REAL NOT NULL,
    page_hash TEXT NOT NULL,
    indexed_at TEXT NOT NULL,
    UNIQUE(kb_id, rel_path)
);

CREATE TABLE IF NOT EXISTS chunks (
    id INTEGER PRIMARY KEY,
    doc_id INTEGER NOT NULL,
    ordinal INTEGER NOT NULL,
    section_title TEXT NOT NULL,
    heading_path TEXT NOT NULL,
    anchor TEXT NOT NULL,
    body TEXT NOT NULL,
    token_count INTEGER NOT NULL,
    FOREIGN KEY(doc_id) REFERENCES documents(id) ON DELETE CASCADE
);

CREATE VIRTUAL TABLE IF NOT EXISTS chunk_fts USING fts5(
    title,
    heading_path,
    body,
    tokenize = '{TOKENIZER}'
);
"""

@dataclass
class Section:
    ordinal: int
    section_title: str
    heading_path: str
    anchor: str
    body: str

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "section"

def kb_dir_for(kb_id: str) -> Path:
    return KB_ROOT / kb_id

def per_kb_db_path(kb_id: str) -> Path:
    return kb_dir_for(kb_id) / "derived" / "search" / "index.sqlite"

def global_db_path() -> Path:
    return KB_ROOT / GLOBAL_KB_ID / "derived" / "search" / "index.sqlite"

def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def connect(db_path: Path) -> sqlite3.Connection:
    ensure_parent(db_path)
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA_SQL)
    return con

def probe_fts5(con: sqlite3.Connection) -> None:
    try:
        con.execute("CREATE VIRTUAL TABLE temp.__fts5_probe USING fts5(x)")
        con.execute("DROP TABLE temp.__fts5_probe")
    except sqlite3.OperationalError as exc:
        raise SystemExit(
            "FTS5 is not available in the current SQLite build. "
            "Run the health command to inspect PRAGMA compile_options."
        ) from exc

def compile_options(con: sqlite3.Connection) -> list[str]:
    try:
        return [row[0] for row in con.execute("PRAGMA compile_options")]
    except sqlite3.DatabaseError:
        return []

def list_kb_ids() -> list[str]:
    if not KB_ROOT.exists():
        return []
    kb_ids = []
    for child in sorted(KB_ROOT.iterdir()):
        if not child.is_dir():
            continue
        if child.name.startswith(".") and child.name != GLOBAL_KB_ID:
            continue
        if child.name == GLOBAL_KB_ID:
            continue
        kb_ids.append(child.name)
    return kb_ids

def iter_markdown_files(kb_id: str) -> Iterable[Path]:
    root = kb_dir_for(kb_id)
    if not root.exists():
        return []
    paths = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        if any(part in IGNORED_PARTS for part in rel.parts):
            continue
        paths.append(path)
    return sorted(paths)

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def parse_simple_yaml_block(block: str) -> dict:
    meta: dict[str, object] = {}
    current_key: Optional[str] = None
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        m = SIMPLE_KV_RE.match(line)
        if m:
            current_key = m.group(1)
            value = m.group(2).strip()
            if value == "":
                meta[current_key] = []
            else:
                meta[current_key] = value
            continue
        if line.lstrip().startswith("- ") and current_key:
            meta.setdefault(current_key, [])
            if isinstance(meta[current_key], list):
                meta[current_key].append(line.lstrip()[2:].strip())
    return meta

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    raw_meta = text[4:end]
    body = text[end + 5 :]

    try:
        import frontmatter  # type: ignore
        post = frontmatter.loads(text)
        return dict(post.metadata), post.content
    except Exception:
        return parse_simple_yaml_block(raw_meta), body

def infer_domain(kb_id: str, meta: dict) -> str:
    if isinstance(meta.get("domain"), str) and meta["domain"].strip():
        return str(meta["domain"]).strip()
    lowered = kb_id.lower()
    if "personal" in lowered or "orchestration" in lowered:
        return "personal_orchestration"
    if "parent" in lowered or "cross" in lowered:
        return "cross_project"
    return "project"

def extract_title(rel_path: Path, body: str, meta: dict) -> str:
    if isinstance(meta.get("title"), str) and meta["title"].strip():
        return str(meta["title"]).strip()
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return rel_path.stem.replace("-", " ").replace("_", " ").strip() or rel_path.name

def split_sections(body: str, fallback_title: str) -> list[Section]:
    lines = body.splitlines()
    sections: list[Section] = []
    stack: list[tuple[int, str]] = []
    buffer: list[str] = []
    ordinal = 0

    def flush() -> None:
        nonlocal ordinal, buffer
        text = "\n".join(buffer).strip()
        if not text:
            buffer = []
            return
        if stack:
            section_title = stack[-1][1]
            heading_path = " > ".join(title for _, title in stack)
            anchor = slugify(section_title)
        else:
            section_title = fallback_title
            heading_path = fallback_title
            anchor = "page"
        sections.append(
            Section(
                ordinal=ordinal,
                section_title=section_title,
                heading_path=heading_path,
                anchor=anchor,
                body=text,
            )
        )
        ordinal += 1
        buffer = []

    for line in lines:
        m = HEADING_RE.match(line)
        if m:
            flush()
            level = len(m.group(1))
            title = m.group(2).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, title))
            continue
        buffer.append(line)

    flush()

    if not sections:
        clean = body.strip()
        if clean:
            sections.append(
                Section(
                    ordinal=0,
                    section_title=fallback_title,
                    heading_path=fallback_title,
                    anchor="page",
                    body=clean,
                )
            )
    return sections

def page_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def token_count(text: str) -> int:
    return len(re.findall(r"\w+", text))

def clear_scope(con: sqlite3.Connection, kb_ids: list[str]) -> None:
    for kb_id in kb_ids:
        doc_ids = [
            row["id"]
            for row in con.execute("SELECT id FROM documents WHERE kb_id = ?", (kb_id,))
        ]
        for doc_id in doc_ids:
            chunk_ids = [
                row["id"]
                for row in con.execute("SELECT id FROM chunks WHERE doc_id = ?", (doc_id,))
            ]
            for chunk_id in chunk_ids:
                con.execute("DELETE FROM chunk_fts WHERE rowid = ?", (chunk_id,))
            con.execute("DELETE FROM chunks WHERE doc_id = ?", (doc_id,))
        con.execute("DELETE FROM documents WHERE kb_id = ?", (kb_id,))

def index_kb(con: sqlite3.Connection, kb_id: str) -> dict:
    root = kb_dir_for(kb_id)
    if not root.exists():
        return {"kb_id": kb_id, "indexed_documents": 0, "indexed_chunks": 0, "missing": True}

    indexed_documents = 0
    indexed_chunks = 0
    paths = list(iter_markdown_files(kb_id))

    for path in paths:
        rel_path = path.relative_to(root)
        raw = load_text(path)
        meta, body = parse_frontmatter(raw)
        title = extract_title(rel_path, body, meta)
        domain = infer_domain(kb_id, meta)

        cur = con.execute(
            """
            INSERT INTO documents (kb_id, domain, rel_path, title, source_mtime, page_hash, indexed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                kb_id,
                domain,
                str(rel_path),
                title,
                path.stat().st_mtime,
                page_hash(raw),
                utc_now(),
            ),
        )
        doc_id = cur.lastrowid
        indexed_documents += 1

        for section in split_sections(body, title):
            cur = con.execute(
                """
                INSERT INTO chunks (doc_id, ordinal, section_title, heading_path, anchor, body, token_count)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    doc_id,
                    section.ordinal,
                    section.section_title,
                    section.heading_path,
                    section.anchor,
                    section.body,
                    token_count(section.body),
                ),
            )
            chunk_id = cur.lastrowid
            con.execute(
                "INSERT INTO chunk_fts(rowid, title, heading_path, body) VALUES (?, ?, ?, ?)",
                (chunk_id, title, section.heading_path, section.body),
            )
            indexed_chunks += 1

    con.execute(
        """
        INSERT INTO index_meta(key, value) VALUES('last_build_utc', ?)
        ON CONFLICT(key) DO UPDATE SET value = excluded.value
        """,
        (utc_now(),),
    )
    return {
        "kb_id": kb_id,
        "indexed_documents": indexed_documents,
        "indexed_chunks": indexed_chunks,
        "missing": False,
    }

def build_index(args: argparse.Namespace) -> int:
    if args.all_kbs:
        kb_ids = list_kb_ids()
        db_path = global_db_path()
    else:
        kb_ids = [args.kb]
        db_path = per_kb_db_path(args.kb)

    con = connect(db_path)
    probe_fts5(con)
    with con:
        clear_scope(con, kb_ids)
        summary = [index_kb(con, kb_id) for kb_id in kb_ids]
        try:
            con.execute("INSERT INTO chunk_fts(chunk_fts) VALUES('optimize')")
        except sqlite3.DatabaseError:
            pass

    payload = {
        "status": "ok",
        "db_path": str(db_path.relative_to(REPO_ROOT)),
        "scope": "global" if args.all_kbs else "kb",
        "results": summary,
    }
    print(json.dumps(payload, indent=2))
    return 0

def write_markdown_output(args: argparse.Namespace, db_path: Path, results: list[dict]) -> Optional[Path]:
    if not args.write_markdown:
        return None

    if args.all_kbs:
        out_root = KB_ROOT / GLOBAL_KB_ID / "outputs" / "queries"
    else:
        out_root = kb_dir_for(args.kb) / "outputs" / "queries"

    out_root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = out_root / f"{stamp}-{slugify(args.query)[:80]}.md"

    lines = [
        "# KB Query Output",
        "",
        f"- query: `{args.query}`",
        f"- scope: `{'global' if args.all_kbs else args.kb}`",
        f"- db_path: `{db_path.relative_to(REPO_ROOT)}`",
        f"- generated_at: `{utc_now()}`",
        "",
        "## Top results",
        "",
    ]

    if not results:
        lines.append("_No results returned._")
    else:
        for idx, item in enumerate(results, start=1):
            lines.extend(
                [
                    f"### Result {idx}",
                    f"- kb_id: `{item['kb_id']}`",
                    f"- domain: `{item['domain']}`",
                    f"- rel_path: `{item['rel_path']}`",
                    f"- title: `{item['title']}`",
                    f"- heading_path: `{item['heading_path']}`",
                    f"- score: `{item['score']}`",
                    "",
                    item["snippet"],
                    "",
                ]
            )

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path

def query_index(args: argparse.Namespace) -> int:
    db_path = global_db_path() if args.all_kbs else per_kb_db_path(args.kb)
    if not db_path.exists():
        raise SystemExit(f"Index does not exist: {db_path.relative_to(REPO_ROOT)}")

    con = connect(db_path)
    probe_fts5(con)

    where = ""
    params: list[object] = [args.query]
    if not args.all_kbs:
        where = "AND d.kb_id = ?"
        params.append(args.kb)
    params.append(args.limit)

    sql = f"""
    SELECT
        d.kb_id,
        d.domain,
        d.rel_path,
        d.title,
        c.section_title,
        c.heading_path,
        c.anchor,
        snippet(chunk_fts, 2, '[', ']', ' … ', 24) AS snippet,
        bm25(chunk_fts, 6.0, 3.0, 1.0) AS score
    FROM chunk_fts
    JOIN chunks c ON c.id = chunk_fts.rowid
    JOIN documents d ON d.id = c.doc_id
    WHERE chunk_fts MATCH ?
      {where}
    ORDER BY score ASC
    LIMIT ?
    """

    rows = [dict(row) for row in con.execute(sql, params)]
    md_path = write_markdown_output(args, db_path, rows)

    payload = {
        "status": "ok",
        "query": args.query,
        "scope": "global" if args.all_kbs else args.kb,
        "db_path": str(db_path.relative_to(REPO_ROOT)),
        "result_count": len(rows),
        "markdown_output": str(md_path.relative_to(REPO_ROOT)) if md_path else None,
        "results": rows,
    }

    print(json.dumps(payload, indent=2))
    return 0

def health(args: argparse.Namespace) -> int:
    db_path = global_db_path() if args.all_kbs else per_kb_db_path(args.kb)
    con = connect(db_path)
    fts5_ok = True
    fts5_error = None
    try:
        probe_fts5(con)
    except SystemExit as exc:
        fts5_ok = False
        fts5_error = str(exc)

    payload = {
        "status": "ok" if fts5_ok else "degraded",
        "scope": "global" if args.all_kbs else args.kb,
        "db_path": str(db_path.relative_to(REPO_ROOT)),
        "fts5_available": fts5_ok,
        "fts5_error": fts5_error,
        "compile_options": compile_options(con),
        "document_count": con.execute("SELECT COUNT(*) FROM documents").fetchone()[0],
        "chunk_count": con.execute("SELECT COUNT(*) FROM chunks").fetchone()[0],
        "last_build_utc": con.execute(
            "SELECT value FROM index_meta WHERE key = 'last_build_utc'"
        ).fetchone(),
    }

    if payload["last_build_utc"] is not None:
        payload["last_build_utc"] = payload["last_build_utc"][0]

    print(json.dumps(payload, indent=2))
    return 0

def latest_source_mtime(kb_id: str) -> Optional[float]:
    mtimes = []
    for path in iter_markdown_files(kb_id):
        mtimes.append(path.stat().st_mtime)
    return max(mtimes) if mtimes else None

def stale(args: argparse.Namespace) -> int:
    if args.all_kbs:
        kb_ids = list_kb_ids()
        db_path = global_db_path()
    else:
        kb_ids = [args.kb]
        db_path = per_kb_db_path(args.kb)

    payload = {
        "status": "ok",
        "db_path": str(db_path.relative_to(REPO_ROOT)),
        "scope": "global" if args.all_kbs else args.kb,
        "kb_status": [],
    }

    if not db_path.exists():
        payload["status"] = "missing_index"
        print(json.dumps(payload, indent=2))
        return 1

    con = connect(db_path)

    for kb_id in kb_ids:
        latest_doc = latest_source_mtime(kb_id)
        row = con.execute(
            "SELECT MAX(source_mtime) FROM documents WHERE kb_id = ?",
            (kb_id,),
        ).fetchone()
        indexed_mtime = row[0] if row else None
        is_stale = (
            latest_doc is not None and indexed_mtime is not None and latest_doc > indexed_mtime
        ) or (latest_doc is not None and indexed_mtime is None)

        payload["kb_status"].append(
            {
                "kb_id": kb_id,
                "source_max_mtime": latest_doc,
                "indexed_max_mtime": indexed_mtime,
                "stale": bool(is_stale),
            }
        )

    if any(item["stale"] for item in payload["kb_status"]):
        payload["status"] = "stale"

    print(json.dumps(payload, indent=2))
    return 0 if payload["status"] == "ok" else 2

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Apex KB retrieval/index utility")
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build-index", help="Build a KB or global retrieval index")
    p_build.add_argument("--kb", help="KB id")
    p_build.add_argument("--all-kbs", action="store_true", help="Build global multi-KB index")
    p_build.set_defaults(func=build_index)

    p_query = sub.add_parser("query", help="Query a KB or the global index")
    p_query.add_argument("--kb", help="KB id")
    p_query.add_argument("--all-kbs", action="store_true", help="Query global multi-KB index")
    p_query.add_argument("--query", required=True, help="FTS query string")
    p_query.add_argument("--limit", type=int, default=8, help="Result limit")
    p_query.add_argument("--write-markdown", action="store_true", help="Write markdown artifact")
    p_query.set_defaults(func=query_index)

    p_health = sub.add_parser("health", help="Inspect FTS5/index health")
    p_health.add_argument("--kb", help="KB id")
    p_health.add_argument("--all-kbs", action="store_true", help="Inspect global index")
    p_health.set_defaults(func=health)

    p_stale = sub.add_parser("stale", help="Check whether an index is stale")
    p_stale.add_argument("--kb", help="KB id")
    p_stale.add_argument("--all-kbs", action="store_true", help="Check global index")
    p_stale.set_defaults(func=stale)

    return parser

def validate_scope_args(args: argparse.Namespace) -> None:
    if getattr(args, "all_kbs", False):
        return
    if not getattr(args, "kb", None):
        raise SystemExit("Either --kb <id> or --all-kbs must be provided.")

def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    validate_scope_args(args)
    return int(args.func(args))

if __name__ == "__main__":
    sys.exit(main())
```

### New file content for `.claude/skills/apex-kb/references/retrieval-contract.md`

```markdown
# Apex KB Retrieval Contract

## Purpose

This contract defines the production retrieval/index layer for Apex knowledge bases.

Retrieval is read-only.
Retrieval never mutates task state, planning state, or operator-control artifacts.
Retrieval produces evidence packets for Claude and human review.

## Canonical vs derived

Canonical artifacts:
- markdown wiki/pages
- source manifests
- raw source snapshots
- any explicitly authored KB summaries

Derived artifacts:
- SQLite index databases
- query result markdown outputs
- temporary snippets or audit exports

Rule:
- canonical artifacts are the source of truth
- derived artifacts must be rebuildable from canonical artifacts

## Supported domains

- project
- personal_orchestration
- cross_project

Personal orchestration memory is a first-class domain.
It must not be collapsed into ordinary project KBs.

## Index scopes

### Per-KB index
Path:
`apex-meta/kb/<kb>/derived/search/index.sqlite`

Use for:
- day-to-day project retrieval
- local rebuilds
- precise custody and debugging

### Global index
Path:
`apex-meta/kb/.global/derived/search/index.sqlite`

Use for:
- cross-project routing
- orchestration lookup
- parent-memory synthesis
- selective multi-KB search

## Chunking rules

Primary unit:
- heading section

Fallback unit:
- whole page, if the page does not contain usable headings

Rules:
- preserve page path
- preserve heading path
- preserve section title
- preserve stable anchor text
- preserve rankable title/body structure

## Query output contract

Every query response must provide:

- query
- scope
- db_path
- result_count
- results[]

Each result must provide:

- kb_id
- domain
- rel_path
- title
- section_title
- heading_path
- anchor
- snippet
- score

## Health rules

The retrieval layer must expose:

- FTS5 availability probe
- compile options inspection
- stale-index check
- deterministic rebuild command

If FTS5 is unavailable, the command must fail loudly and explicitly.

## Safety rules

Forbidden:
- silent source invention
- task mutation from query
- unbounded context loading
- using derived index files as canonical memory

Required:
- source-grounded excerpts
- auditable result paths
- deterministic rebuild support
```

### New file content for `.claude/skills/apex-kb/templates/query-output-template.md`

```markdown
# KB Query Output

- query: `{{ query }}`
- scope: `{{ scope }}`
- db_path: `{{ db_path }}`
- generated_at: `{{ generated_at }}`

## Top results

### Result {{ n }}
- kb_id: `{{ kb_id }}`
- domain: `{{ domain }}`
- rel_path: `{{ rel_path }}`
- title: `{{ title }}`
- heading_path: `{{ heading_path }}`
- score: `{{ score }}`

{{ snippet }}
```

### Precise append-only update for `.claude/skills/apex-kb/SKILL.md`

Append this section near the command-usage area:

```markdown
## Querying and indexing

The `apex-kb` package includes a retrieval/index surface for local ranked search.

Primary commands:
- `python apex-meta/scripts/apex_kb_retrieval.py build-index --kb <kb_id>`
- `python apex-meta/scripts/apex_kb_retrieval.py build-index --all-kbs`
- `python apex-meta/scripts/apex_kb_retrieval.py query --kb <kb_id> --query "<query>"`
- `python apex-meta/scripts/apex_kb_retrieval.py query --all-kbs --query "<query>"`
- `python apex-meta/scripts/apex_kb_retrieval.py health --kb <kb_id>`
- `python apex-meta/scripts/apex_kb_retrieval.py stale --kb <kb_id>`

Use retrieval when Claude needs:
- ranked evidence from KB pages
- bounded context packets instead of whole-KB loading
- personal orchestration recall
- cross-project or parent-memory retrieval

Retrieval is read-only.
Retrieval never mutates planning or task-state artifacts.
```

### Precise append-only update for `.claude/skills/apex-kb/package-manifest.md`

Append the following entries to the package file inventory:

```markdown
## Retrieval assets

- references/retrieval-contract.md
- templates/query-output-template.md
- ../../../apex-meta/scripts/apex_kb_retrieval.py
```

### Precise append-only update for `.claude/skills/apex-kb/references/kb-contract.md`

Append this section:

```markdown
## Canonical and derived retrieval artifacts

Canonical:
- markdown pages
- manifests
- raw sources
- authored summaries

Derived:
- search indexes
- query outputs
- retrieval caches

Canonical artifacts remain the source of truth.
Derived retrieval artifacts must always be rebuildable.

## Required retrieval metadata

Common required fields:
- kb_id
- domain
- rel_path
- title

Recommended frontmatter:
- title
- domain
- tags
- updated_at
- owners
- status
```

### Precise append-only update for `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`

Append this section:

```markdown
## Query and retrieval rules

- Query is read-only.
- Query outputs must cite canonical file paths.
- Query outputs must prefer bounded snippets over entire page dumps.
- A stale-index check must be available.
- Health checks must verify FTS5 support explicitly.
- Personal orchestration memory is a separate retrieval domain.
- Global cross-KB search must not replace per-KB source custody.

Audit rule:
- if an index is stale, the tool must say so explicitly before relying on results
```

### Precise append-only update for `.claude/skills/apex-kb/references/script-command-contract.md`

Append this section:

```markdown
## Retrieval command contract

### Build per-KB index
`python apex-meta/scripts/apex_kb_retrieval.py build-index --kb <kb_id>`

### Build global index
`python apex-meta/scripts/apex_kb_retrieval.py build-index --all-kbs`

### Query per-KB index
`python apex-meta/scripts/apex_kb_retrieval.py query --kb <kb_id> --query "<terms>"`

### Query global index
`python apex-meta/scripts/apex_kb_retrieval.py query --all-kbs --query "<terms>"`

### Health
`python apex-meta/scripts/apex_kb_retrieval.py health --kb <kb_id>`
`python apex-meta/scripts/apex_kb_retrieval.py health --all-kbs`

### Stale-index check
`python apex-meta/scripts/apex_kb_retrieval.py stale --kb <kb_id>`
`python apex-meta/scripts/apex_kb_retrieval.py stale --all-kbs`
```

### Precise append-only update for `.gitignore`

Append:

```gitignore
# Apex KB derived search artifacts
apex-meta/kb/**/derived/search/*.sqlite
apex-meta/kb/**/derived/search/*.sqlite-shm
apex-meta/kb/**/derived/search/*.sqlite-wal
apex-meta/kb/.global/derived/search/
apex-meta/kb/**/outputs/queries/
```

### Optional delegation snippet for `apex-meta/scripts/apex_kb.py`

This update is **high-risk and unverified** because the current file could not be read. If the existing script already uses `argparse` with subcommands, add a delegation block like this near its command registration area:

```python
# retrieval delegation
from apex_kb_retrieval import main as retrieval_main

# Example wrapper pattern:
# if sys.argv[1] in {"build-index", "query", "health", "stale"}:
#     sys.exit(retrieval_main(sys.argv[1:]))
```

If the current `apex_kb.py` command parser is materially different, do **not** apply that blindly; keep `apex_kb_retrieval.py` as the executable entrypoint and wire it into docs only.

## Validation commands, rollback plan, and true blockers

### Validation commands

Run these from the repo root.

```bash
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
```

Expected outcome: no output and exit code `0`.

```bash
python apex-meta/scripts/apex_kb_retrieval.py health --kb <KB_ID>
```

Expected outcome: JSON with `fts5_available: true` if the local SQLite build supports FTS5, plus `compile_options`, `document_count`, and `chunk_count`. If FTS5 is missing, the command should return `"status": "degraded"` and explain the fault. This health posture is required because FTS5 support depends on the SQLite build and should be proven, not assumed. citeturn11view1turn13view0

```bash
python apex-meta/scripts/apex_kb_retrieval.py build-index --kb <KB_ID>
```

Expected outcome:

```json
{
  "status": "ok",
  "scope": "kb",
  "results": [
    {
      "kb_id": "<KB_ID>",
      "indexed_documents": 12,
      "indexed_chunks": 86,
      "missing": false
    }
  ]
}
```

```bash
python apex-meta/scripts/apex_kb_retrieval.py query --kb <KB_ID> --query "source custody" --write-markdown
```

Expected outcome: JSON with ranked results; each result contains `rel_path`, `heading_path`, `snippet`, and `score`. Snippets come from FTS5 `snippet()`, and ranking comes from `bm25()`. citeturn10view0turn10view3

```bash
python apex-meta/scripts/apex_kb_retrieval.py stale --kb <KB_ID>
```

Expected outcome:

- `"status": "ok"` if no source markdown file is newer than the indexed `source_mtime`
- `"status": "stale"` if the index needs rebuild

```bash
python apex-meta/scripts/apex_kb_retrieval.py build-index --all-kbs
python apex-meta/scripts/apex_kb_retrieval.py query --all-kbs --query "weekly recap routing" --write-markdown
```

Expected outcome: cross-KB results with `kb_id` attached to every hit, written both to stdout JSON and a markdown artifact under `.global/outputs/queries/`.

### Rollback plan

Touched files and artifacts:

- `apex-meta/scripts/apex_kb_retrieval.py`
- `.claude/skills/apex-kb/references/retrieval-contract.md`
- `.claude/skills/apex-kb/templates/query-output-template.md`
- append-only edits to:
  - `.claude/skills/apex-kb/SKILL.md`
  - `.claude/skills/apex-kb/package-manifest.md`
  - `.claude/skills/apex-kb/references/kb-contract.md`
  - `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`
  - `.claude/skills/apex-kb/references/script-command-contract.md`
  - `.gitignore`
- generated artifacts:
  - `apex-meta/kb/**/derived/search/*.sqlite*`
  - `apex-meta/kb/**/outputs/queries/`
  - `apex-meta/kb/.global/derived/search/`
  - `apex-meta/kb/.global/outputs/queries/`

Exact rollback:

```bash
git checkout -- \
  .claude/skills/apex-kb/SKILL.md \
  .claude/skills/apex-kb/package-manifest.md \
  .claude/skills/apex-kb/references/kb-contract.md \
  .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md \
  .claude/skills/apex-kb/references/script-command-contract.md \
  .gitignore

rm -f apex-meta/scripts/apex_kb_retrieval.py
rm -f .claude/skills/apex-kb/references/retrieval-contract.md
rm -f .claude/skills/apex-kb/templates/query-output-template.md
rm -rf apex-meta/kb/.global/derived/search
find apex-meta/kb -type d -path "*/derived/search" -prune -exec rm -rf {} +
find apex-meta/kb -type d -path "*/outputs/queries" -prune -exec rm -rf {} +
```

### True blockers

There is one real blocker, and it is material:

- **The selected GitHub repository and the explicitly listed repo files were not readable in this run**. The public repo URL returned 404, and a direct raw-file request also returned 404. That prevents verified repo-state mapping, verified current-file diffs, and verified adaptation of existing `apex_kb.py` command structure. citeturn5view0turn4view0

That blocker does **not** prevent final architecture selection or a production-capable retrieval implementation. It **does** prevent claiming that the append sections above are anchored to exact current headings in the inaccessible repo.