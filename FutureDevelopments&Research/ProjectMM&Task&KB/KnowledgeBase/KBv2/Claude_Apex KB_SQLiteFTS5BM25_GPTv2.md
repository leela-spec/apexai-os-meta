# Step 1 — Read confirmation

I read the five requested files and also checked the two extra uploaded variants as secondary context.

|File|Approx. size|Approx. structure read|Role in audit|
|---|--:|---|---|
|`Claude_Apex KB_SQLiteFTS5BM25_CCv2.md`|485 lines|5 parts, 3 decisions, 15 steps, 6 tests|**Primary implementation plan**|
|`Claude_Apex KB_SQLiteFTS5BM25_CC.md`|531 lines|4 chapters: architecture, retrieval engine, integration loop, gaps|Original architecture/spec|
|`Claude_Apex KB_SQLiteFTS5BM25_GPT.md`|506 lines|executive verdict, repo truth, corrected claims, gaps|Prior GPT verification / repo truth pass|
|`KB-Researchv3_gpt.md`|726 lines|14 sections, scoring matrices, architecture recommendation|Research/scoring basis|
|`KB-Researchv3_gpt_FB_claude.md`|109 lines|score corrections + overall verdict|Research correction pass|
|Extra read: `Apex KB+SQLite FTS5BM25 Implementation Plan.md`|635 lines|alternate plan text|Consistency check|
|Extra read: `Claude_Apex KB_SQLiteFTS5BM25_CCv3.md`|584 lines|verifier/report variant|Secondary context, not treated as binding|

## Step 2 — Three-sentence understanding

Apex KB + SQLite FTS5/BM25 is meant to be a **local, repo-native retrieval layer**: raw sources are preserved, compiled wiki pages become the LLM-readable retrieval surface, and SQLite FTS5 provides fast lexical ranking and snippets. The system should keep `CLAUDE.md` small, load skills/rules only when relevant, and let Claude Code call local Python scripts to retrieve top pages instead of rereading large raw corpora. The plan is directionally correct, but not safe to execute as-is because FTS5 availability, BM25 vector alignment, YAML parsing limits, `.gitignore` ordering, and skill/package format details still need hard gates.

I cannot expose hidden chain-of-thought. For every score below 70, I provide the visible audit rationale and failure mode.

---

# Instruction Block 1 — System Description

## 1A — Macro level

### 1. Problem solved

**Verified description:** Apex KB + SQLite FTS5/BM25 solves the “local knowledge retrieval” problem for a solo Claude Code operator: it turns a growing repo of raw sources, manifests, compiled wiki pages, and query outputs into a searchable local memory layer. Claude Code’s official memory docs say every session starts with a fresh context window, while `CLAUDE.md` and auto memory are loaded as context, not hard configuration; this supports the plan’s premise that long-term knowledge must live in files and be retrieved intentionally, not assumed to persist in conversation. ([code.claude.com](https://code.claude.com/docs/en/memory "https://code.claude.com/docs/en/memory"))

**What breaks without it:** the operator either rereads raw sources every session or relies on `CLAUDE.md` bloat. The original Apex spec says compiled wiki pages are the primary Claude read surface and raw sources are custody/evidence; the verifier pass also says the repo is not yet a working SQLite FTS5 stack and that `apex_kb.py` is not FTS search.

**External corroboration:** LLM Wiki Compiler describes the same raw-source → compiled wiki pattern and explicitly frames it as reducing repeated raw-file rereads and making knowledge compound. ([GitHub](https://github.com/ussumant/llm-wiki-compiler "https://github.com/ussumant/llm-wiki-compiler")) OntoShip likewise uses Markdown as source of truth and regenerates derived search/index artifacts so git stays clean. ([GitHub](https://github.com/vakovalskii/ontoship "https://github.com/vakovalskii/ontoship"))

### 2. System boundaries

|Owns|Does not own|
|---|---|
|Raw source custody, source manifests, compiled wiki pages, query outputs, audit logs, search index build/search scripts|Daily planning routines, task state, model routing history, calendar/capacity constraints, Claude tool execution policy, and the SQLite DB as source artifact|

This boundary is correct: the verifier explicitly says SQLite `search.sqlite` is a derived artifact, not source, and personal orchestration must remain a separate first-class memory domain.

### 3. Fit with Claude Code memory architecture

Claude Code reads project instructions, settings, skills, subagents, workflows, rules, and auto memory from the repo and `~/.claude`; `CLAUDE.md` and rules consume context, while skills are reusable prompts/capabilities that can be invoked directly or when relevant. ([code.claude.com](https://code.claude.com/docs/en/claude-directory "https://code.claude.com/docs/en/claude-directory")) Claude’s memory docs recommend keeping `CLAUDE.md` under 200 lines and moving multi-step procedures or codebase-specific procedures to skills or path-scoped rules. ([code.claude.com](https://code.claude.com/docs/en/memory "https://code.claude.com/docs/en/memory"))

**Verdict:** the plan’s architecture is right: `CLAUDE.md` should contain only routing rules; the search procedure belongs in a skill; detailed contracts belong in reference files; DB/search behavior belongs in scripts.

### 4. Why compiled wiki pages instead of raw sources

Compiled wiki pages are the correct retrieval surface because they are shorter, structured, source-linked, and designed for LLM reading. LLM Wiki implementations explicitly preserve raw sources and compile persistent wiki pages so knowledge is not re-derived on each query. ([GitHub](https://github.com/nashsu/llm_wiki "https://github.com/nashsu/llm_wiki")) SQLite FTS5/BM25 then gives deterministic lexical ranking and snippets over those compiled pages, instead of making Claude scan an ever-growing index manually. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))

---

## 1B — Meso level

### 1. Full pipeline and ownership

|Stage|Artifact|Owner|
|---|---|---|
|Source intake|`raw/`, source snapshots, hashes|Operator / Claude under `apex-kb` rules|
|Source manifest|`source-manifest.json`|Script validates; Claude writes only under gated procedure|
|Compilation|`wiki/**/*.md` with YAML frontmatter + body|Claude/operator|
|Index build|`apex-meta/registry/search.sqlite`|`scripts/apex-index.py`|
|Query|ranked snippets|`scripts/apex-search.py`|
|Read|top-N compiled pages|Claude|
|Answer|source-pointers + optional saved query|Claude|
|Reuse|`outputs/queries/<date>-<topic>.md`|Claude/operator|

This matches the original working spec’s raw source → manifest → compiled wiki → SQLite FTS5 → ranked snippets → saved query output pipeline.

### 2. Token cost by layer

|Layer|Token cost|
|---|---|
|`CLAUDE.md`|Always loaded; should stay small|
|`.claude/rules/`|Path/topic scoped; loaded when matching|
|Skill metadata|Small routing metadata|
|`SKILL.md` body|Loaded when skill is invoked/relevant|
|Reference docs|Loaded only if the skill asks for them|
|Compiled wiki pages|On demand after search|
|Raw sources|Only for conflict/source verification|
|SQLite DB|No context cost; queried by script|

Claude’s docs state `CLAUDE.md` is loaded into the context window and recommend a target under 200 lines; auto memory’s first 200 lines or 25KB are loaded, with detailed notes read on demand. ([code.claude.com](https://code.claude.com/docs/en/memory "https://code.claude.com/docs/en/memory")) Skills are packaged as `SKILL.md` files with optional supporting resources that Claude uses when relevant. ([code.claude.com](https://code.claude.com/docs/en/agent-sdk/skills "https://code.claude.com/docs/en/agent-sdk/skills"))

### 3. mtime staleness detection

**Verdict:** acceptable for v1, but not a “sound in all cases” claim.

**Why acceptable:** comparing source file mtimes to a derived index mtime is a common build-cache pattern. Sphinx issue discussions describe outdated-file decisions based on whether source files or dependencies were modified using mtime values. ([GitHub](https://github.com/sphinx-doc/sphinx/issues/11556 "https://github.com/sphinx-doc/sphinx/issues/11556")) Python’s own import/bytecode ecosystem historically uses timestamp-based invalidation, but it has known precision failure modes on fast edits and some filesystems. ([GitHub](https://github.com/python/cpython/issues/121376 "https://github.com/python/cpython/issues/121376"))

**Required fix:** use `st_mtime_ns` when available, and optionally store SHA256 hashes for strict mode. Do not claim “no precision loss.” Mark C7 false/weak.

### 4. SQLite FTS5 BM25 mechanics

SQLite FTS5 documents that `bm25()` returns a real value where better matches are numerically lower; SQLite multiplies the usual BM25 by `-1` so ascending order returns best-first. It also documents that bm25 trailing weights map positionally to FTS table columns from left to right; missing weights default to `1.0`, extras are ignored. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))

SQLite also documents that `snippet()` selects a short fragment from a matched row and highlights query terms, while `highlight()` column indexes are numbered from left to right starting at zero. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))

---

## 1C — Micro level

### 1. Column order vs BM25 vector

Planned schema:

|Index|Column|Intended weight|
|--:|---|--:|
|0|`id`|0|
|1|`kb`|0|
|2|`path`|0|
|3|`title`|5|
|4|`tags`|3|
|5|`summary`|2|
|6|`sources`|0|
|7|`updated`|0|
|8|`status`|0|
|9|`body`|1|

**Correct vector:** `bm25(ft, 0,0,0,5,3,2,0,0,0,1)`.

**Audit finding:** the v2 plan references the correct positional vector, but the original spec’s Python query shown in `CC.md` is inconsistent/shifted. The v2 implementation should explicitly reject any function using the shorter/shifted vector.

### 2. `snippet(ft, 9, ...)`

Given the schema above, `body` is column index `9`. This is correct. SQLite column indexes for highlight/snippet-style FTS functions are zero-based and count the FTS table columns in definition order. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))

### 3. YAML frontmatter parsed by stdlib `re`

**Verdict:** safe only for a restricted subset, unsafe for all legal YAML.

What breaks:

- multi-line block scalars (`summary: |`)
    
- nested lists/maps
    
- quoted strings with colons
    
- `---` inside body if regex is not anchored
    
- comments and folded text
    
- duplicate fields
    
- arrays with mixed quoting
    

**Fix:** define a **restricted Apex frontmatter subset** if stdlib-only is mandatory: one-line scalars, bracketed lists, no nested maps, frontmatter must start at byte 0 with `---\n` and close with `\n---\n`.

### 4. `unicode61 remove_diacritics 2`

**Verdict:** good default, not fully correct for technical text.

SQLite’s `unicode61` tokenizer is suitable for Unicode text and `remove_diacritics` controls accent handling, but technical identifiers need explicit testing. Hyphen-separated terms may be split; `camelCase` may not split into `camel` + `case`; underscores may behave differently than desired; numeric suffixes need fixture coverage. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html")) Kenso’s own roadmap calls out tokenization for compound terms like `camelCase` and `snake_case` as an active search-quality area, which directly weakens any claim that default tokenization is already “correct” for technical corpora. ([PyPI](https://pypi.org/project/kenso/ "https://pypi.org/project/kenso/"))

### 5. Slug filenames as SQLite TEXT primary keys

Lowercase hyphen-separated slugs are safe as SQLite `TEXT` values. Edge cases are not SQLite reserved-word problems; they are filesystem/path policy problems: duplicate filenames across KBs, Unicode normalization, case-insensitive filesystems, Windows reserved names, and path traversal (`..`). Use compound uniqueness `(kb, id)` or globally prefix IDs with `kb-slug/filename`.

---

# Instruction Block 2 — Blueprint Search

## P1 — Python script: SQLite FTS5 + YAML frontmatter Markdown indexer

**Verdict:** **BLUEPRINT GAP** for the exact no-dependency Python + YAML-frontmatter + SQLite FTS5 + BM25 package.

|Source|Fit|Difference|Copy|
|---|---|---|---|
|OntoShip / `gitmark`|Self-contained Python stdlib CLI, Markdown source, SQLite FTS5/BM25/trigram search. ([GitHub](https://github.com/vakovalskii/ontoship "https://github.com/vakovalskii/ontoship"))|Not clearly the same YAML-frontmatter schema|Copy “derived index regenerated from Markdown; git stays clean”|
|Kenso|SQLite BM25 over Markdown, frontmatter improves retrieval, title 10× weighting, no embeddings/API costs. ([PyPI](https://pypi.org/project/kenso/ "https://pypi.org/project/kenso/"))|Package dependency, not stdlib-only; not necessarily FTS5-only|Copy writing guide + weighted title/tags/summary idea|
|markdown-vault-mcp|Frontmatter-aware Markdown indexing with FTS5 and semantic vector search. ([pvliesdonk.github.io](https://pvliesdonk.github.io/markdown-vault-mcp/3.0/ "https://pvliesdonk.github.io/markdown-vault-mcp/3.0/"))|MCP/server/hybrid; heavier than Apex v1|Copy frontmatter-aware indexing checks|

**Risk:** exact blueprint is thin; v1 script needs stronger local fixtures than “copy a known repo.”

## P2 — Local Markdown KB with BM25 search, zero infrastructure

**Verdict:** strong precedent.

|Source|Maps directly|Different|Copy|
|---|---|---|---|
|OntoShip|Markdown + git source of truth; derived FTS5 index; no service/DB/vendor. ([GitHub](https://github.com/vakovalskii/ontoship "https://github.com/vakovalskii/ontoship"))|More graph/fuzzy features|Copy derived-artifact policy|
|Kenso|BM25 keyword search over SQLite; no embeddings/vector DB/API cost. ([PyPI](https://pypi.org/project/kenso/ "https://pypi.org/project/kenso/"))|Installed package; not pure stdlib|Copy title/tags/summary weighting|
|sqlite-bm25-search|Local filesystem search using SQLite FTS5 BM25. ([GitHub](https://github.com/midclique/sqlite-bm25-search "https://github.com/midclique/sqlite-bm25-search"))|Generic files, not KB schema|Copy CLI UX and rebuild/test structure|

## P3 — Claude Code skill files in production repos

**Verdict:** strong precedent, but retrieval-specific skills are still emerging.

|Source|Maps directly|Different|Copy|
|---|---|---|---|
|Anthropic skills repo|`SKILL.md` folder format; official examples; project/plugin usage. ([GitHub](https://github.com/anthropics/skills "https://github.com/anthropics/skills"))|Mostly examples, not Apex retrieval|Copy canonical `SKILL.md` structure|
|CCPM|Skill triggers, PRD→epic→tasks, script-first status/next/blocker. ([GitHub](https://github.com/automazeio/ccpm "https://github.com/automazeio/ccpm"))|PM/GitHub-oriented|Copy “scripts for deterministic operations”|
|glebis/claude-skills|Large active skill repo, includes session-search and qmd-search style workflows. ([GitHub](https://github.com/glebis/claude-skills "https://github.com/glebis/claude-skills"))|Heterogeneous quality|Copy skill packaging + search workflow examples|

## P4 — LLM-wiki / compiled KB pattern

**Verdict:** strong precedent.

|Source|Maps directly|Different|Copy|
|---|---|---|---|
|LLM Wiki Compiler|Raw files → topic wiki; Claude/Codex plugin; reduces context costs. ([GitHub](https://github.com/ussumant/llm-wiki-compiler "https://github.com/ussumant/llm-wiki-compiler"))|Plugin ecosystem|Copy raw→compiled wiki lifecycle|
|nashsu/llm_wiki|Raw Sources → Wiki → Schema; ingest/query/lint; YAML frontmatter. ([GitHub](https://github.com/nashsu/llm_wiki "https://github.com/nashsu/llm_wiki"))|Desktop app/API/MCP|Copy schema + operation split|
|Hermes LLM Wiki docs|Persistent compounding Markdown KB; contradictions flagged and synthesis preserved. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki "https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki"))|Hermes-specific|Copy “compile once, query many” principle|
|WiCER paper|Empirical warning: blind compilation drops facts; iterative compile/evaluate/refine recovers quality. ([arXiv](https://arxiv.org/abs/2605.07068 "https://arxiv.org/abs/2605.07068"))|Research-grade|Copy diagnostic probes before trusting compiled pages|

## P5 — Python indexer parses YAML frontmatter + body into FTS5

**Verdict:** **BLUEPRINT GAP** for exact Apex constraints.

Partial blueprints: Kenso, markdown-vault-mcp, and GitHub Docs-style Markdown + YAML frontmatter. Kenso shows frontmatter improves retrieval and specific titles can be indexed 10×. ([PyPI](https://pypi.org/project/kenso/ "https://pypi.org/project/kenso/")) GitHub Docs uses Markdown files with YAML frontmatter for page behavior. ([DeepWiki](https://deepwiki.com/github/docs/5.1-content-structure-and-frontmatter "https://deepwiki.com/github/docs/5.1-content-structure-and-frontmatter")) The missing evidence is a production Python stdlib-only script with the exact schema and no YAML dependency.

## P6 — Staleness detection via file mtime

**Verdict:** production precedent exists, but with known caveats.

|Source|Maps directly|Risk|
|---|---|---|
|Sphinx|Outdated file decisions based on whether source/dependency modified using mtime. ([GitHub](https://github.com/sphinx-doc/sphinx/issues/11556 "https://github.com/sphinx-doc/sphinx/issues/11556"))|CI/new clone timestamp drift|
|Python import/pyc cache|Timestamp-based invalidation known pattern. ([GitHub](https://github.com/python/cpython/issues/121376 "https://github.com/python/cpython/issues/121376"))|Precision edge cases|
|Make/build systems|mtime is canonical build dependency method. ([groups.google.com](https://groups.google.com/g/sphinx-users/c/xaG-M43k05o "https://groups.google.com/g/sphinx-users/c/xaG-M43k05o"))|Clock skew/fresh clone problems|

**Copy:** use mtime for v1, but add `--strict-hash` later.

## P7 — BM25 weight vector tuning in SQLite FTS5

**Verdict:** enough evidence for the concept; exact weights must be empirically tuned.

SQLite official docs support per-column bm25 weights. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html")) Kenso uses title weighting and frontmatter fields to improve retrieval. ([PyPI](https://pypi.org/project/kenso/ "https://pypi.org/project/kenso/")) TreeSearch documentation describes SQLite FTS5/BM25 column weighting in an implementation context. ([DeepWiki](https://deepwiki.com/shibing624/TreeSearch/6.4-fts5-scoring-and-bm25 "https://deepwiki.com/shibing624/TreeSearch/6.4-fts5-scoring-and-bm25"))

**Copy:** title boost yes; exact `5/3/2/1` needs fixture tuning.

## P8 — Saved/cached query output as Markdown files

**Verdict:** **BLUEPRINT GAP** for exact saved-answer-as-Markdown pattern.

LLM Wiki systems support compiled query/answer behavior conceptually, and Apex’s own spec includes saved query outputs, but I did not find three strong external production sources that store pre-synthesized query answers as Markdown for future LLM reuse. Treat as Apex-specific v1 feature, not copied blueprint.

---

# Instruction Block 3 — Claim Verification Table

|ID|Claim|Evidence|Verdict|
|---|---|---|---|
|C1|FTS5 BM25 is fully deterministic: identical query/data always returns identical ranked results|SQLite BM25 is mathematical and ordered by score, but ties without secondary sort can be arbitrary. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))|**PARTIAL** — add `ORDER BY score, path`|
|C2|Python stdlib `sqlite3` always includes FTS5|Python has `sqlite3`, but SQLite features depend on underlying SQLite library; compile options vary. ([Python documentation](https://docs.python.org/3/library/sqlite3.html "https://docs.python.org/3/library/sqlite3.html"))|**FALSE / UNVERIFIED**|
|C3|`unicode61 remove_diacritics 2` correctly tokenizes hyphens, underscores, camelCase, numeric suffixes|SQLite supports tokenizer options, but technical compound handling is not guaranteed; Kenso flags compound tokenization as roadmap work. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))|**WEAK**|
|C4|`bm25()` returns negative floats; lower = better; `ORDER BY rank` best-first|Official SQLite: better matches numerically lower; multiplied by -1. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))|**STRONG**|
|C5|`snippet()` column index is 0-based FTS5 table column order|SQLite documents FTS column indexes from left to right starting at zero for auxiliary functions. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))|**STRONG**|
|C6|Python `re` safely parses YAML frontmatter between delimiters without PyYAML|Only for a restricted subset; not legal YAML generally.|**PARTIAL**|
|C7|`os.stat().st_mtime` reliable on Linux/macOS with no precision loss/timezone issues|Timestamp cache invalidation has known precision/filesystem issues. ([GitHub](https://github.com/python/cpython/issues/121376 "https://github.com/python/cpython/issues/121376"))|**FALSE**|
|C8|Claude Code skills auto-trigger on matching phrases without naming skill|Claude Code docs: skills are used when relevant or invoked directly. ([code.claude.com](https://code.claude.com/docs/en/skills "https://code.claude.com/docs/en/skills"))|**STRONG**|
|C9|`CLAUDE.md` loaded every session and recommended under 200 lines|Official docs: loaded into context; target under 200 lines. ([code.claude.com](https://code.claude.com/docs/en/memory "https://code.claude.com/docs/en/memory"))|**STRONG**|
|C10|Full rebuild for 200 pages under 2 seconds|Plausible, but no Apex benchmark or comparable direct benchmark found.|**UNVERIFIED**|
|C11|FTS5/BM25 achieves ≥80% retrieval accuracy on exact-term queries under 500 pages|Kenso reports eval metrics, but not Apex corpus or exact claim. ([PyPI](https://pypi.org/project/kenso/ "https://pypi.org/project/kenso/"))|**UNVERIFIED**|

---

# Instruction Block 4 — Gap Analysis

|Gap|Description|Severity|Fix|Blueprint|
|---|---|---|---|---|
|G1|FTS5 availability not verified at runtime|**CRITICAL**|Add preflight `CREATE VIRTUAL TABLE t USING fts5(x)` and fail clearly|SQLite FTS5 docs + Python sqlite3 dependency reality ([Python documentation](https://docs.python.org/3/library/sqlite3.html "https://docs.python.org/3/library/sqlite3.html"))|
|G2|BM25 vector / column position mismatch risk|**CRITICAL**|Lock schema + vector fixture; assert vector length == column count|SQLite bm25 positional weights ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))|
|G3|YAML parser undecided / regex too broad|**MAJOR**|Define restricted frontmatter subset or allow `python-frontmatter`|GitHub Docs / Kenso frontmatter precedent ([DeepWiki](https://deepwiki.com/github/docs/5.1-content-structure-and-frontmatter "https://deepwiki.com/github/docs/5.1-content-structure-and-frontmatter"))|
|G4|No malformed frontmatter handling|**MAJOR**|Skip invalid page, log warning, nonzero validation status||
|G5|`--check-stale` stdout not standardized|**MAJOR**|Machine output: `OK`, `STALE <reason>`, `ERROR <reason>`||
|G6|`wiki/index.md` indexed|**MAJOR**|Exclude all navigation/index files by default||
|G7|`apex-meta/orchestration/` missing from implementation plan|**MAJOR**|Add as separate future memory domain; do not mix into KB|Prior verifier already flags personal orchestration as separate|
|G8|Existing `apex_kb.py` coexistence undefined|**MAJOR**|Document `apex_kb.py` = custody/lint; `apex-index.py` = retrieval index||
|G9|No UTF-8 verification before build|**MAJOR**|Add encoding scan before indexing||
|G10|`.gitignore` for `search.sqlite` too late|**CRITICAL**|Move before first index build||
|G11|SQL query uses `MATCH ?` with user query; malformed FTS query can crash|**MAJOR**|Catch `sqlite3.OperationalError`; optionally quote/escape simple queries||
|G12|DB is shared but rebuild is per-KB; stale logic can confuse cross-KB DB|**MAJOR**|Either rebuild all KBs or preserve rows for other KBs||
|G13|No deterministic tie-breaker|**MINOR/MAJOR**|`ORDER BY score ASC, ft.path ASC`||
|G14|No fixture corpus|**CRITICAL**|Add 5–10 tiny pages with expected ranks before touching real KB||
|G15|Skill file path likely wrong|**MAJOR**|Use `.claude/skills/apex-search/SKILL.md`, not `.claude/skills/apex-search.md`; official skills use folder + `SKILL.md`. ([GitHub](https://github.com/anthropics/skills "https://github.com/anthropics/skills"))||

---

# Instruction Block 5 — Decision Options Matrix

Scores are evidence-weighted. Sub-70 scores include rationale.

|Decision|Option|Impact|Evidence|Risk|Effort|Verdict|
|---|---|--:|--:|--:|--:|---|
|D1 DB location|Per-KB sqlite|55|45|80|80|**Reject** — simpler isolation but blocks cross-KB|
||Shared `registry/search.sqlite`|85|75|70|70|**Keep with changes** — add `kb` scoping + all-KB rebuild|
|D2 YAML parser|stdlib regex|55|40|45|85|**Only restricted subset** — below 70 due legal YAML breakage|
||`python-frontmatter`|75|75|80|60|**Best parser**, but violates no-pip constraint|
||Manual line parser|70|55|70|75|**Best no-dependency compromise**|
|D3 Rebuild|Full drop/create/insert|80|80|85|80|**Keep** for v1; SQLite supports rebuild semantics ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))|
||Incremental update|70|80|55|45|Later; below 70 risk due delete/update complexity|
|D4 Skill|Standalone `apex-search`|80|80|80|70|**Keep**, but folder format|
||Merge into `apex-kb`|55|60|50|65|Reject; boundary blur|
|D5 Staleness|mtime|65|75|55|90|**Keep v1 with caveat**; precision issues|
||SHA256|85|85|90|60|Better strict mode|
||mtime + hash|90|85|90|55|Best long-term|
|D6 BM25 weights|`5/3/2/1`|70|70|65|80|Keep as default but test|
||equal weights|50|75|75|90|Too low impact|
||title-only boost|60|65|55|80|Too brittle|
|D7 Exclusions|exclude `index.md` only|55|65|55|90|Too narrow|
||exclude navigation/non-wiki files|85|80|85|75|**Adopt**|

---

# Instruction Block 6 — Step-by-Step Plan Audit

|Step|Verdict|Impact|Evidence|Risk|Effort|Flags|
|--:|---|--:|--:|--:|--:|---|
|1 Pre-flight audit|**PASS**|85|75|80|85|Add FTS5 availability test and UTF-8 test|
|2 Operator decision|**PASS**|70|60|85|90|Evidence below 70 because it is process logic, not external blueprint|
|3 Frontmatter update|**FLAG**|80|55|55|70|Regex parser unsafe; use restricted parser + dry-run|
|4 Manifest update|**PASS/FLAG**|75|60|70|75|Must preserve schema shape; validate JSON|
|5 Create registry|**REORDER**|60|70|90|95|Move `.gitignore` before generating DB|
|6 Write indexer|**FLAG**|95|80|55|60|Needs FTS5 preflight, fixture corpus, index exclusions|
|7 Write search|**FLAG**|95|80|50|65|BM25 vector and query escaping risk|
|8 First build|**REORDER**|80|70|45|80|Only after `.gitignore` + fixture pass|
|9 Search test|**PASS/EXPAND**|85|75|75|80|Add expected top-result assertions|
|10 Write skill|**REPLACE**|75|90|50|70|Must be `.claude/skills/apex-search/SKILL.md`|
|11 Update `CLAUDE.md`|**REORDER**|65|85|55|75|After skill/scripts validated; keep under 200 lines|
|12 Path rules|**PASS/FLAG**|70|80|70|75|Good, but file path must match current Claude Code rules|
|13 End-to-end test|**PASS**|90|70|75|70|Add stale DB + malformed query tests|
|14 `.gitignore`|**REORDER**|90|85|95|95|Must happen before Step 8|
|15 Registry docs|**PASS**|65|65|90|80|Below 70 impact because documentation does not affect runtime correctness|

---

# Instruction Block 7 — File Design Audit

## 1. `scripts/apex-index.py`

**Macro:** correct role: deterministic index builder. Do not combine with answering or Claude prompt logic.

**Meso:** required sections: FTS5 availability check, page discovery, restricted frontmatter parse, validation, full rebuild, stale check, JSON/text report, fixture mode.

**Micro:** must use UTF-8 explicit reads, skip malformed pages, exclude `wiki/index.md`, use `st_mtime_ns`, record indexed row count, and never write outside `apex-meta/registry/`.

## 2. `scripts/apex-search.py`

**Macro:** correct role: query interface only.

**Meso:** required sections: DB existence check, stale check delegation, safe query handling, BM25 query, result formatting, JSON mode, nonzero error mode.

**Micro:** use correct vector `0,0,0,5,3,2,0,0,0,1`; `snippet(ft,9,...)`; `ORDER BY score, path`; catch malformed MATCH queries.

## 3. `.claude/skills/apex-search/SKILL.md`

**Macro:** plan file path is wrong if it proposes `.claude/skills/apex-search.md`. Official pattern is a directory containing `SKILL.md`. ([GitHub](https://github.com/anthropics/skills "https://github.com/anthropics/skills"))

**Meso:** frontmatter must include name and description; body should be compact and route to scripts.

**Micro:** no raw SQL in skill body unless needed; no broad repo mutation permission; no generated DB checked into source.

## 4. `CLAUDE.md` retrieval block

**Macro:** right file for one compact routing rule.

**Meso:** should only say when to use Apex Search and where the skill lives.

**Micro:** must remain under 200-line target and not duplicate the full procedure. ([code.claude.com](https://code.claude.com/docs/en/memory "https://code.claude.com/docs/en/memory"))

## 5. `.claude/rules/apex-meta.md`

**Macro:** correct for path-scoped safety.

**Meso:** should include no raw deletion, no silent wiki rewrite, append-only audit rules, generated DB ignored.

**Micro:** must not claim enforcement; Claude docs say context instructions are not hard configuration. Hooks/settings are enforcement layers. ([code.claude.com](https://code.claude.com/docs/en/memory "https://code.claude.com/docs/en/memory"))

## 6. `apex-meta/registry/index.md`

**Macro:** correct as human-readable registry.

**Meso:** include active KBs, DB path, rebuild command, last build, known exclusions.

**Micro:** do not embed stale runtime data that conflicts with DB; mark DB as derived.

## 7. Wiki frontmatter template

**Macro:** correct artifact.

**Meso:** required fields: `id`, `kb`, `title`, `tags`, `sources`, `authority`, `created`, `updated`, `status`, `summary`.

**Micro:** field names are safe. `status` is not a SQLite reserved problem in this use, but `id` uniqueness must be scoped. YAML lists must be restricted if no YAML parser is used.

---

# Instruction Block 8 — Risk Register

|Risk|Probability|Impact|Level|Trigger|Detection|Mitigation|Source|
|---|---|---|---|---|---|---|---|
|R1 FTS5 missing|Medium|High|**CRITICAL**|Python SQLite build lacks FTS5|`CREATE VIRTUAL TABLE ... fts5` fails|Preflight hard fail|SQLite/Python build reality ([Python documentation](https://docs.python.org/3/library/sqlite3.html "https://docs.python.org/3/library/sqlite3.html"))|
|R2 BM25 vector mismatch|High|High|**CRITICAL**|Wrong vector copied from older spec|Fixture rank mismatch|Lock vector + schema assertion|SQLite positional weights ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))|
|R3 Regex fails frontmatter|High|Medium|**MAJOR**|multiline/nested YAML|parser warning or silent bad metadata|restricted subset/manual parser||
|R4 mtime precision loss|Medium|Medium|**MAJOR**|rapid edits, FAT/network FS|stale false negative|`st_mtime_ns` + hash mode ([GitHub](https://github.com/python/cpython/issues/121376 "https://github.com/python/cpython/issues/121376"))||
|R5 `wiki/index.md` indexed|High|Medium|**MAJOR**|navigation page included|top results are index pages|exclude index/navigation files||
|R6 `CLAUDE.md` bloat|Medium|Medium|**MAJOR**|procedure copied into CLAUDE.md|line count >200|keep only routing block ([code.claude.com](https://code.claude.com/docs/en/memory "https://code.claude.com/docs/en/memory"))||
|R7 Skill trigger mismatch|Medium|Medium|**MAJOR**|bad description|skill not invoked|eval cases + direct command||
|R8 `apex_kb.py` conflict|Medium|Medium|**MAJOR**|overlapping commands/imports|user calls wrong script|boundary doc||
|R9 DB committed|Medium|High|**CRITICAL**|`.gitignore` after DB creation|`git status` shows sqlite|move gitignore earlier||
|R10 empty snippets|Medium|Low|**MINOR**|match outside body / short doc|blank snippet|fallback to summary/title highlight||
|R11 malformed MATCH query|Medium|Medium|**MAJOR**|user query has FTS syntax chars|OperationalError|catch and fallback||
|R12 lexical misses semantic queries|High|Medium|**MAJOR**|synonym/vocabulary mismatch|no result for concept query|tags/aliases + later vector hybrid||
|R13 tie nondeterminism|Medium|Low|**MINOR**|equal BM25 score|result order changes|secondary sort path||

---

# Instruction Block 9 — Final Verdict

═══════════════════════════════════════════  
**APEX-VERIFY FINAL VERDICT**  
═══════════════════════════════════════════

**OVERALL VERDICT:** **EXECUTE WITH CHANGES**

**EXECUTION GATE:** **YES WITH CHANGES**

The architecture is sound, but the current plan is not safe to execute exactly as written. The v1 should proceed only after the critical fixes below are applied.

─── **TOP 5 REQUIRED CHANGES** ───

1. **Move `.gitignore` before first DB creation** | Reason: `search.sqlite` is a derived artifact and must not be committed | Blueprint: OntoShip derived artifacts regenerated from Markdown; git stays clean. ([GitHub](https://github.com/vakovalskii/ontoship "https://github.com/vakovalskii/ontoship"))
    
2. **Add FTS5 runtime availability preflight** | Reason: Python has `sqlite3`, but FTS5 depends on the underlying SQLite build | Blueprint: SQLite compile options and FTS5 docs. ([Python documentation](https://docs.python.org/3/library/sqlite3.html "https://docs.python.org/3/library/sqlite3.html"))
    
3. **Lock schema/vector/snippet fixtures before real indexing** | Reason: bm25 weights are positional; one older spec has a shifted vector risk | Blueprint: SQLite bm25 positional weight docs. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))
    
4. **Replace broad regex YAML parsing with a restricted no-dependency parser or allow a parser library** | Reason: stdlib regex is not safe for all YAML frontmatter | Blueprint: GitHub Docs/Kenso frontmatter usage, but Apex must define a subset. ([DeepWiki](https://deepwiki.com/github/docs/5.1-content-structure-and-frontmatter "https://deepwiki.com/github/docs/5.1-content-structure-and-frontmatter"))
    
5. **Use canonical skill package path `.claude/skills/apex-search/SKILL.md`** | Reason: Claude Code skill format is directory + `SKILL.md`, not a flat `.md` file | Blueprint: Anthropic skills repo and Claude Code docs. ([GitHub](https://github.com/anthropics/skills "https://github.com/anthropics/skills"))
    

─── **3 THINGS CORRECT — DO NOT CHANGE** ───

1. **Compiled wiki pages as retrieval surface** | Why correct: LLM Wiki implementations explicitly compile raw sources into persistent Markdown wiki pages to avoid re-deriving knowledge each query. ([GitHub](https://github.com/ussumant/llm-wiki-compiler "https://github.com/ussumant/llm-wiki-compiler"))
    
2. **SQLite FTS5/BM25 as v1 retrieval layer** | Why correct: official SQLite supports FTS5 BM25, snippets, rank ordering, and column weights locally with no server. ([sqlite.org](https://sqlite.org/fts5.html "https://sqlite.org/fts5.html"))
    
3. **Small `CLAUDE.md` + skill/rule separation** | Why correct: Claude Code docs recommend concise `CLAUDE.md`, skills for multi-step procedures, and path-scoped rules for directory-specific behavior. ([code.claude.com](https://code.claude.com/docs/en/memory "https://code.claude.com/docs/en/memory"))
    

─── **SINGLE HIGHEST FAILURE RISK** ───

The most likely silent v1 failure is **BM25/schema mismatch**: search appears to work, but ranking is wrong because weights attach to the wrong columns.

─── **BLUEPRINT GAPS** ───

- **P1:** exact Python stdlib-only Markdown YAML-frontmatter → SQLite FTS5/BM25 indexer.
    
- **P5:** exact Apex-style schema insertion into FTS5 from YAML frontmatter.
    
- **P8:** saved/cached query answers as Markdown files for future LLM reuse.
    

═══════════════════════════════════════════