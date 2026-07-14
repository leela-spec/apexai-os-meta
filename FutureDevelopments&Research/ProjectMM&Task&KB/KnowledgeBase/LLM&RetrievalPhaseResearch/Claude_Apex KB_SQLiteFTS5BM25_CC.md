This is a comprehensive design document. I have full context from your prior research files. Writing the full spec now — no tools needed beyond what I've read.

---

# Apex KB + SQLite FTS5/BM25 — Complete Working Specification

---

## Chapter 1 — Apex KB Architecture

---

## 1.1 Macro: Purpose and Role

**What problem Apex KB solves:**

- Claude Code has no persistent memory across sessions. Without a compiled KB, Claude re-reads raw sources every time, burning tokens and producing non-deterministic synthesis.
    
- The KB is the **canonical, source-backed knowledge surface** — the thing Claude reads instead of re-synthesizing from scratch.
    

**What breaks without it:**

- Session continuity collapses: no stable definitions, no source-cited answers
    
- Token cost explodes: Claude reads full raw docs instead of compiled summaries
    
- Retrieval becomes non-deterministic: different sessions produce different answers from the same corpus
    

**What Apex KB owns:**

text

`apex_kb_owns:   - raw source custody (snapshots, paths, hashes)  - source manifests (what exists, what was processed, when)  - compiled wiki pages (distilled, source-backed summaries)  - the markdown index (wiki/index.md)  - saved query outputs (pre-synthesized answers)  - audit logs (what changed, when, by whom)  - entity files (canonical definitions of concepts)  - contradiction capture (open questions, flagged conflicts)`

**What Apex KB does NOT own:**

text

`apex_kb_does_not_own:   - task state (that's apex-meta/epics/, apex-meta/state/)  - daily/weekly planning routines  - model routing history  - calendar / capacity constraints  - Claude tool execution logic  - the SQLite index file itself (that's a derived artifact, not source)`

**Relationship to Claude's context window, CLAUDE.md, and skills:**

|Layer|What it does|Token cost|
|---|---|---|
|`CLAUDE.md`|Boot instructions, routing rules, system facts|Always loaded|
|Path-scoped rules|Directory-specific behavior overrides|Loaded on path match|
|Skill files (`.claude/skills/`)|Procedural instructions, loaded on trigger|Near-zero until triggered|
|Apex KB (compiled wiki)|Source-backed knowledge, loaded on retrieval|Zero until queried|
|Raw sources|Original documents|Never loaded directly unless conflict resolution|

CLAUDE.md should point to the KB; it should not contain KB content.

**Why compiled KB beats raw sources as retrieval surface:**

- Raw sources are long, unstructured, and written for human reading, not LLM ingestion
    
- Compiled wiki pages are token-dense: one page = distilled synthesis of multiple sources with front-matter Claude can parse cheaply
    
- Compiled pages have explicit `sources:` citations, so Claude can fall back to raw if needed
    
- The compilation step also resolves contradictions and captures open questions — raw sources don't do this
    

---

## 1.2 Meso: How It Works

**Full pipeline:**

text

`raw source     ↓ [operator ingests, hashes, registers] source manifest entry (manifests/source-manifest.json)     ↓ [Claude or operator compiles wiki page] compiled wiki page (wiki/<slug>.md)     ↓ [Python indexer reads front-matter + body] SQLite FTS5 index (registry/search.sqlite)     ↓ [Claude queries via Python script] ranked results with snippets     ↓ [Claude reads top N pages] answer + source pointers     ↓ [optional: Claude writes to query output] saved query output (outputs/queries/<date>-<topic>.md)`

**Who uses each layer:**

|Layer|Used by|Purpose|
|---|---|---|
|Raw sources|Operator, Claude (conflict resolution only)|Custody, evidence|
|Source manifest|Python scripts, Claude first-pass|Know what exists, detect staleness|
|Compiled wiki pages|Claude (primary read surface)|Retrieve knowledge|
|Markdown index|Claude (cheap first-pass navigation)|Decide which pages to open|
|SQLite FTS5 index|Python script exclusively|Ranked retrieval over full body text|
|Saved query outputs|Claude (reuse)|Avoid re-synthesizing known answers|

**Source manifest — required fields:**

json

`{   "source_id": "source-001",  "path": "raw/articles/claude-memory.md",  "url": "https://...",  "hash": "sha256:abc123...",  "authority": "official",  "ingested_at": "2026-06-25",  "last_modified": "2026-06-20",  "generated_pages": [    "wiki/summaries/claude-memory.md",    "wiki/concepts/session-continuity.md"  ],  "status": "compiled",  "notes": "" }`

**Compiled wiki page — what makes it a good retrieval target:**

- Short (400–1200 tokens target body length)
    
- Front-matter is machine-readable and FTS5-indexer-readable
    
- Body is written for LLM consumption: no fluff, dense facts, structured sections
    
- Has explicit `sources:` list linking back to manifest entries
    
- Has `tags:` for coarse filtering
    
- Has `updated:` date so staleness detection works
    

**Markdown index (`wiki/index.md`) — when sufficient vs. insufficient:**

|Sufficient|Insufficient|
|---|---|
|KB is small (<30 pages)|KB grows past ~40 pages|
|Query is navigational ("what pages exist on topic X")|Query requires ranking by relevance|
|Claude needs a full-corpus overview|Token cost of reading full index becomes non-trivial|
|Operator browsing manually|Claude needs to retrieve top-3 pages, not read all|

**Saved query outputs — why they reduce token load:**

- Pre-synthesized answers avoid re-querying + re-reading + re-synthesizing
    
- Claude checks query output before running FTS5 search
    
- Query output includes source pointers so provenance is preserved
    
- Format: one file per query, date-stamped, with `query:`, `retrieved_pages:`, and `answer:` fields
    

---

## 1.3 Micro: Exact Formulation

**Canonical folder layout:**

text

`apex-meta/   kb/    <kb-slug>/      raw/                        # Raw source files (snapshots)      manifests/        source-manifest.json      # Machine-readable source ledger      wiki/        index.md                  # Human + Claude navigation index        summaries/                # One page per source, distilled        concepts/                 # Cross-source concept pages        entities/                 # Canonical definitions        synthesis/                # Multi-source synthesis pages      outputs/        queries/                  # Saved query outputs          2026-06-25-<topic>.md      audit/        audit-log.md              # Append-only change log        open-questions.md         # Contradictions, gaps      logs/        session-log.md            # Append-only session log  registry/    search.sqlite                 # SQLite FTS5 index (derived artifact)    index.md                      # Cross-KB navigation index`

**Minimum required source manifest entry (JSON Schema):**

json

`{   "type": "object",  "required": ["source_id", "path", "hash", "authority", "ingested_at", "generated_pages", "status"],  "properties": {    "source_id":       { "type": "string" },    "path":            { "type": "string" },    "url":             { "type": "string" },    "hash":            { "type": "string", "pattern": "^sha256:" },    "authority":       { "enum": ["official", "community", "operator", "derived"] },    "ingested_at":     { "type": "string", "format": "date" },    "last_modified":   { "type": "string", "format": "date" },    "generated_pages": { "type": "array", "items": { "type": "string" } },    "status":          { "enum": ["raw", "compiled", "stale", "flagged"] },    "notes":           { "type": "string" }  } }`

**Minimum required compiled wiki page structure:**

text

`--- id: concept-session-continuity title: "Session Continuity in Claude Code" kb: prompt-engineer-research-base tags: [claude-code, memory, CLAUDE.md, session] sources: [source-001, source-007] authority: official created: 2026-06-20 updated: 2026-06-25 status: current          # current | stale | flagged summary: "One-sentence summary for index.md and snippet pre-filter." --- ## Overview [2–4 sentence synthesis] ## Key Facts - Fact 1 - Fact 2 ## Constraints / Caveats - Known limitation ## Open Questions - Unresolved contradiction (if any) ## Source Pointers - source-001: raw/articles/claude-memory.md §3`

**Minimum required saved query output:**

text

`--- query: "best rules for prompt-packet generation" kb: prompt-engineer-research-base date: 2026-06-25 retrieved_pages:   - wiki/concepts/prompt-packet-contract.md  - wiki/summaries/special-ops-promptflow.md result_count: 6 --- ## Answer [Synthesized answer here] ## Source Pointers - wiki/concepts/prompt-packet-contract.md §Key Facts`

**What makes a wiki page "index-ready" (fields the SQLite indexer reads):**

|Field|Required|Purpose|
|---|---|---|
|`id`|✅|Primary key in FTS5 table|
|`title`|✅|Indexed, displayed in results|
|`tags`|✅|Indexed for tag filtering|
|`summary`|✅|Indexed, used for snippet pre-filtering|
|`kb`|✅|Scoping queries to one KB|
|`updated`|✅|Staleness detection|
|`status`|✅|Exclude `stale`/`flagged` from results|
|`sources`|✅|Provenance in result output|
|Body text|✅|Primary FTS5 search target|

---

## Chapter 2 — SQLite FTS5/BM25 Retrieval Engine

---

## 2.1 Macro: Purpose and Role

**What FTS5/BM25 solves that `wiki/index.md` cannot:**

- `index.md` scales linearly with KB size: at 60 pages, Claude spends 3–5k tokens just reading the index to decide what to open
    
- BM25 returns a **ranked shortlist with snippets** — Claude reads 200–400 tokens total before deciding which 2–3 pages to open
    
- `index.md` has no relevance ranking: Claude guesses from summaries. BM25 ranks by term frequency × inverse document frequency — the result is deterministic for a fixed query string and fixed index
    

**Why determinism is critical:**

- Same query on the same index must return the same result every time
    
- Non-deterministic retrieval means Claude produces different answers in different sessions for the same question — this breaks audit trails and operator trust
    
- BM25 is a pure mathematical ranking function over an immutable index; no randomness
    

**Why this is the correct v1 engine:**

- Zero infrastructure: no Docker, no embedding model, no GPU, no API
    
- Ships with Python stdlib (`sqlite3`) — one import, no `pip install`
    
- Rebuild is deterministic: same pages → same index
    
- FTS5 `snippet()` function extracts exact text fragments, giving Claude a tight read-before-load signal
    
- Sufficient for lexical queries over a 50–500 page corpus without degradation
    

---

## 2.2 Meso: How It Works

**How FTS5 indexes content:**

- FTS5 tokenizes text by whitespace and punctuation (default tokenizer: `unicode61`)
    
- Each row in the virtual table is one document; all indexed columns are searched together
    
- The index is stored as an inverted list: term → list of (doc_id, position) pairs
    
- Columns are weighted: `title` and `tags` get higher weight than body via `bm25(ft, 10, 5, 1)` weight arguments
    

**How BM25 ranking works:**

- BM25 optimizes for: how often does this query term appear in this document, relative to how rarely it appears across all documents
    
- A term that appears frequently in one document but rarely across the KB gets a high score
    
- Document length is normalized: a long page with one mention doesn't beat a short page with three mentions
    
- In SQLite FTS5, `bm25(ft)` returns a negative float; lower (more negative) = better match; `ORDER BY rank` or `ORDER BY bm25(ft)` returns best first
    

**What `snippet()` returns and why it matters:**

- `snippet(ft, col_index, '<b>', '</b>', '...', 20)` returns a ~20-token fragment from the document body with matched terms highlighted
    
- Claude sees **why** a result matched before opening the full page
    
- This is the key token efficiency mechanism: Claude reads 50 tokens of snippet, decides if relevant, then reads the 600-token page only if it is
    

**Query flow — from string to ranked results:**

text

`query string ("prompt packet generation rules")     ↓ Python script parses args     ↓ sqlite3 connection to search.sqlite     ↓ FTS5 MATCH query with BM25 ordering     ↓ snippet() extraction per result     ↓ JSON/text output: path, title, snippet, score, sources, updated     ↓ Claude receives ranked list (default limit: 8)     ↓ Claude reads top 2–4 pages at full length`

**Index rebuild — when and how:**

- Must rebuild when: any wiki page is added, modified, or deleted
    
- Should rebuild when: `updated` date on any page is newer than the SQLite file's mtime
    
- Rebuild is full drop-and-recreate: `DROP TABLE IF EXISTS ft; CREATE VIRTUAL TABLE ft ...` then re-insert all pages
    
- Rebuild is cheap: 200 pages takes < 2 seconds on any modern machine
    
- Claude should run `python scripts/apex-index.py --rebuild --kb <slug>` after any KB update session
    

---

## 2.3 Micro: Exact Formulation

**SQLite schema:**

sql

`CREATE VIRTUAL TABLE IF NOT EXISTS ft USING fts5(     id,           -- wiki page id from front-matter    kb,           -- kb slug for scoping    path,         -- relative file path from repo root    title,        -- from front-matter title    tags,         -- from front-matter tags (joined as string)    summary,      -- from front-matter summary    sources,      -- from front-matter sources (joined)    updated,      -- from front-matter updated date    status,       -- current | stale | flagged    body,         -- full markdown body (stripped of front-matter)    tokenize="unicode61 remove_diacritics 2" ); -- Metadata table (non-FTS) for exact filtering CREATE TABLE IF NOT EXISTS wiki_meta (     id TEXT PRIMARY KEY,    path TEXT,    updated TEXT,    status TEXT,    kb TEXT );`

**Python query function:**

python

`import sqlite3 import json from pathlib import Path def search_kb(     query: str,    kb: str,    db_path: str = "apex-meta/registry/search.sqlite",    limit: int = 8,    status_filter: str = "current" ) -> list[dict]:     con = sqlite3.connect(db_path)    con.row_factory = sqlite3.Row    cur = con.cursor()    sql = """        SELECT            ft.id,            ft.kb,            ft.path,            ft.title,            ft.updated,            ft.sources,            snippet(ft, 9, '>>>', '<<<', '...', 24) AS snippet,            bm25(ft, 0, 0, 5, 3, 2, 1, 0, 0, 1) AS score        FROM ft        WHERE ft MATCH ?          AND ft.kb = ?          AND ft.status = ?        ORDER BY score        LIMIT ?    """    rows = cur.execute(sql, (query, kb, status_filter, limit)).fetchall()    con.close()    return [dict(r) for r in rows]`

**BM25 weight vector explanation** (positional, maps to columns in order):  
`id=0, kb=0, path=0, title=5, tags=3, summary=2, sources=0, updated=0, status=0, body=1`  
Title matches weight 5×, tags 3×, summary 2×, body 1×.

**Example output returned to Claude:**

text

`SEARCH RESULTS — kb: prompt-engineer-research-base — query: "prompt packet generation rules" ────────────────────────────────────────────────── 1. wiki/concepts/prompt-packet-contract.md    Title: Prompt Packet Contract and Output Schema   Updated: 2026-06-22 | Sources: source-003, source-011   Score: -4.21   Snippet: "...The >>>prompt packet<<< must include a contract section defining             expected >>>generation rules<<<, token budget, and output schema..." ────────────────────────────────────────────────── 2. wiki/summaries/special-ops-promptflow.md    Title: Special Ops PromptFlow Design   Updated: 2026-06-18 | Sources: source-002   Score: -3.07   Snippet: "...each >>>packet<<< in the special-ops flow follows explicit             >>>generation rules<<< enforced by the operator validation gate..." ────────────────────────────────────────────────── [6 more results...]`

**Recommended `--limit` value: 8**

- Reason: 8 results × ~50 token snippets = ~400 tokens total for the result list. Claude can scan all 8, then open 2–3 full pages (~600 tokens each). Total retrieval budget: ~2,200 tokens max, well within a 4k context budget for retrieval.
    
- Do not use `--limit 20+`: snippet list becomes too long and negates the token savings.
    

**Stale index detection:**

python

`import os from pathlib import Path def index_is_stale(db_path: str, wiki_dir: str) -> bool:     db = Path(db_path)    if not db.exists():        return True  # missing → rebuild required    db_mtime = db.stat().st_mtime    for md in Path(wiki_dir).rglob("*.md"):        if md.stat().st_mtime > db_mtime:            return True    return False`

Claude detects staleness by running this check before search. If stale, Claude calls `--rebuild` before querying. Claude should not proceed with a stale index — it will return outdated results without warning.

---

## Chapter 3 — Apex KB + SQLite FTS5/BM25 Combined

---

## 3.1 The Exact Interaction Loop

text

`User query     ↓ Claude reads CLAUDE.md (already loaded) → identifies KB retrieval is needed     ↓ Claude checks: does a saved query output match this query?   → YES: read outputs/queries/<file>.md, answer with source pointers, done  → NO: continue    ↓ Claude checks index staleness:   bash: python scripts/apex-search.py --check-stale --kb <slug>  → STALE: python scripts/apex-index.py --rebuild --kb <slug>    ↓ Claude runs search:   bash: python scripts/apex-search.py --kb <slug> --q "<query>" --limit 8    ↓ Claude reads ranked result list (snippets only, ~400 tokens)     ↓ Claude selects top 2–4 results by relevance of snippet     ↓ Claude reads selected wiki pages at full length (~600 tokens each)     ↓ Claude answers with inline source pointers (page path + section)     ↓ [Optional] Claude saves answer to outputs/queries/<date>-<topic>.md`

**Claude's role vs. script's role:**

|Decision|Owner|Reason|
|---|---|---|
|Which KB to query|Claude|Requires understanding query intent|
|Query string formulation|Claude|Requires NL understanding|
|Staleness check|Script|Deterministic file mtime comparison|
|Index rebuild|Script|Deterministic full-corpus operation|
|BM25 ranking|Script/SQLite|Mathematical, must be deterministic|
|Which results to read|Claude|Requires reading snippets and judging relevance|
|How many pages to open|Claude|Context budget judgment|
|Answer synthesis|Claude|Requires reasoning|
|Whether to save query output|Claude|Judgment call on reuse value|

---

## 3.2 Skill File Specification

**File:** `.claude/skills/apex-search.md`

text

``--- name: apex-search description: Retrieve ranked wiki pages from the Apex KB using SQLite FTS5/BM25 triggers:   - user asks a question that requires KB knowledge  - user says "search the KB", "look it up", "check the wiki"  - Claude needs to cite a definition, procedure, or source-backed fact  - query cannot be answered from CLAUDE.md alone --- ## Required inputs - `kb`: slug of the target KB (e.g., `prompt-engineer-research-base`) - `query`: natural language query string (Claude formulates this) ## Script call format ```bash # Check staleness first python scripts/apex-search.py --check-stale --kb <kb-slug> # If stale: python scripts/apex-index.py --rebuild --kb <kb-slug> # Then search: python scripts/apex-search.py --kb <kb-slug> --q "<query string>" --limit 8 ``` ## Output contract Script returns ranked list (stdout, plain text) with per-result: - Rank number - File path (relative to repo root) - Title - Updated date - Sources list - BM25 score (negative float; lower = better) - Snippet with matched terms wrapped in `>>>` / `<<<` ## How Claude uses the result 1. Read all snippets (do NOT open pages yet) 2. Identify top 2–4 results where snippet is clearly relevant 3. Open those pages using Read tool 4. Answer with inline source pointers: `[wiki/concepts/page.md §Section]` 5. If no snippets are relevant → see failure modes 6. If answer is high-value and likely to recur → save to `outputs/queries/` ## Do not - Do not open more than 4 pages per query without operator instruction - Do not re-run search with a rephrased query more than once without telling the user - Do not read the full index.md before running search (defeats token savings)``

---

## 3.3 What CLAUDE.md Must Say About Retrieval

**Minimum required block in CLAUDE.md:**

text

``## KB Retrieval - Canonical KB lives at `apex-meta/kb/<kb-slug>/` - **Do not read raw sources** unless resolving a flagged contradiction - Before answering any KB-dependent question:   1. Check `outputs/queries/` for a matching saved answer  2. If none, trigger skill `apex-search`  3. Read wiki pages only after reviewing search results - Index is at `apex-meta/registry/search.sqlite` - Index may be stale after any KB update session — check before querying - All answers citing KB content must include page path + section pointer ## Known KBs - `prompt-engineer-research-base` — prompt engineering, packet contracts, flow design - [add more as created]``

**Path-scoped rules needed:**

text

`# .claude/rules/apex-meta.md (scoped to apex-meta/) - Never write to wiki/ pages without operator approval - Never delete raw/ files - source-manifest.json is append-only except for status field updates - audit/audit-log.md is append-only — no deletions`

---

## 3.4 Failure Modes and Handling

**Index file missing:**

text

`Detection: --check-stale returns "MISSING" Action: Run --rebuild immediately, then proceed with search Do not: Tell user "index missing" and stop. Rebuild is cheap, do it silently.`

**Query returns zero results:**

text

`Detection: Script returns empty result list Action:   1. Try one reformulation (shorter query, different terms)  2. If still zero: fall back to reading wiki/index.md (full index scan)  3. Tell user: "No FTS5 results; falling back to index scan" Do not: Silently answer from Claude's general knowledge`

**Results are stale (index not rebuilt after KB update):**

text

`Detection: Any wiki page mtime > search.sqlite mtime Action: Rebuild index before search. Log to session-log.md: "Index rebuilt, was stale" Do not: Use stale results and answer anyway — risk citing deleted or superseded content`

**Top result is irrelevant (wrong BM25 match):**

text

`Detection: Claude reads snippet, determines it's off-topic Action:   1. Skip that result, read next in ranked list  2. If all 8 results are irrelevant, fall back to wiki/index.md scan  3. If index scan also fails, tell user explicitly: "KB does not contain this topic" Do not: Hallucinate an answer and fake a source pointer`

---

## Chapter 4 — Gap Analysis: Current Apex KB vs. SQLite FTS5 Requirements

---

## 4.1 Do current compiled wiki pages expose the fields FTS5 needs?

**Assessment: Partially. Missing fields exist.**

Current LLM-wiki pages typically have `title`, `tags`, `updated`, `sources`. They typically lack:

|Missing field|Impact|Fix|
|---|---|---|
|`id`|FTS5 needs a stable primary key per page|Add `id: <slug>` to all front-matter|
|`kb`|Required to scope queries to one KB|Add `kb: <kb-slug>` to all front-matter|
|`status`|Required to exclude stale/flagged pages|Add `status: current` to all front-matter|
|`summary`|One-sentence indexed field for pre-filtering|Add `summary:` field (not a body section — a front-matter field)|

**Recommendation:** Add these four fields to the front-matter template. Existing pages need a one-pass surgical update.

---

## 4.2 Does the current manifest contain what the indexer needs?

**Assessment: Missing two fields.**

Current manifests likely have `path`, `hash`, `ingested_at`, `generated_pages`. They lack:

|Missing field|Impact|Fix|
|---|---|---|
|`status` field per entry|Indexer cannot know if page is `compiled` vs `stale`|Add `"status": "compiled"`|
|`last_modified` on source|Cannot detect if raw source changed since compilation|Add `"last_modified": "<date>"`|

Without `status`, the indexer must assume all entries are indexable — it will index stale/flagged pages. Without `last_modified`, the operator cannot script "which pages need recompilation."

---

## 4.3 Does the current folder structure match the canonical layout?

**Assessment: Close but not exact. Two gaps.**

Current structure (from your research files): `apex-meta/kb/<slug>/raw/`, `wiki/`, `manifests/`, `audit/`, `outputs/`

Missing:

1. `apex-meta/registry/` directory — `search.sqlite` needs a canonical home outside the KB slug (it's shared across KBs and is a derived artifact, not a source)
    
2. `wiki/entities/` and `wiki/synthesis/` subdirectories — likely flat today; sub-typing pages improves FTS5 scoping
    

**No restructuring of existing directories required.** Just add `apex-meta/registry/` and optionally add subdirectories under `wiki/`.

---

## 4.4 Does the current build process conflict with the SQLite indexer?

**Assessment: No conflicts. One encoding check needed.**

- Markdown front-matter (YAML) is parseable by Python `python-frontmatter` or manual regex — no conflict
    
- Surgical edit procedures don't touch front-matter fields Claude doesn't own — no conflict
    
- Operator validation gates don't block script reads — no conflict
    
- **One check required:** confirm all wiki pages are UTF-8 encoded (SQLite FTS5 `unicode61` tokenizer requires this). If any pages were created on Windows with system encoding, run `file --mime-encoding wiki/**/*.md` to verify
    
- Naming conventions (`<slug>.md`, lowercase, hyphen-separated) are compatible with the path column in FTS5 — no change needed
    

---

## 4.5 Minimum Delta — Concrete Action Items

These are the exact additions/changes needed to make the current Apex KB SQLite-ready:

**1. Add 4 front-matter fields to all compiled wiki pages**

bash

`# For each wiki page, add to YAML front-matter: id: <page-slug>          # e.g., concept-session-continuity kb: <kb-slug>            # e.g., prompt-engineer-research-base status: current          # current | stale | flagged summary: "<one sentence>"`

Do this via a surgical pass: one Python script that reads each page, checks for missing fields, and appends them. Do not rewrite pages.

**2. Add 2 fields to source manifest entries**

json

`"status": "compiled", "last_modified": "2026-06-20"`

Add to all existing entries in `source-manifest.json`.

**3. Create `apex-meta/registry/` directory with `.gitkeep`**

bash

`mkdir -p apex-meta/registry touch apex-meta/registry/.gitkeep`

Add `apex-meta/registry/search.sqlite` to `.gitignore` (derived artifact, not versioned).

**4. Write `scripts/apex-index.py`**  
Script must:

- Parse front-matter from all `wiki/**/*.md` files in a given KB
    
- Drop and recreate FTS5 table
    
- Insert all pages with `status = current`
    
- Support `--rebuild` and `--check-stale` flags
    
- Output: `apex-meta/registry/search.sqlite`
    

**5. Write `scripts/apex-search.py`**  
Script must:

- Accept `--kb`, `--q`, `--limit` args
    
- Run the query function from §2.3
    
- Output ranked results in the format specified in §2.3
    
- Support `--check-stale` flag (returns `OK` or `STALE: <reason>`)
    

**6. Create `.claude/skills/apex-search.md`**  
Exact content specified in §3.2.

**7. Add KB retrieval block to `CLAUDE.md`**  
Exact content specified in §3.3.

**8. Add path-scoped rule file**  
`.claude/rules/apex-meta.md` with content from §3.3.

**9. Verify UTF-8 encoding of all wiki pages**

bash

`file --mime-encoding apex-meta/kb/*/wiki/**/*.md | grep -v utf-8`

Fix any non-UTF-8 files before first index build.

**10. Update `wiki/index.md` template**  
Add a column for `id` and `status` to the index table so the index and FTS5 stay in sync.

---

**Total delta: 2 new scripts, 1 new skill file, 1 new directory, 2 CLAUDE.md/rules additions, 1 one-pass front-matter update, 2 manifest field additions.** No restructuring of existing folders. No new dependencies beyond Python stdlib `sqlite3`.