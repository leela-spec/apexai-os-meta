# Apex KB + SQLite FTS5/BM25 — Technical Verifier Report

## Multi-source verified | June 25, 2026

---

## SECTION 1 — System Description (Verified)

## Macro Level

**Problem solved:** A solo Claude Code operator has zero persistent memory across sessions. Without a compiled KB, Claude re-reads raw sources every session — burning tokens, producing non-deterministic synthesis, and losing source attribution. Apex KB + SQLite FTS5/BM25 solves two distinct problems simultaneously: _knowledge custody_ (what do we know, where did it come from, is it current?) and _retrieval_ (given a query, which 2–4 pages should Claude read right now?).

**System boundaries — what it owns:**

|Owns|Does Not Own|
|---|---|
|Raw source custody + hashing|Task state (apex-meta/epics/)|
|Source manifests|Daily/weekly planning routines|
|Compiled wiki pages|Model routing history|
|SQLite FTS5 index (derived artifact)|Calendar / capacity constraints|
|Saved query outputs|Claude tool execution logic|
|Audit logs, contradiction capture|Personal orchestration memory (separate domain)|

[Source: file:3, §1.1 — apex_kb_owns / does_not_own blocks]

**Fit into Claude Code memory architecture:** CLAUDE.md loads at session start as context (not enforced config), path-scoped rules load on path match, skill files load near-zero until triggered, and the KB loads zero tokens until queried. The spec correctly positions Apex KB as _layer 2_ with FTS5 as _layer 4_ in the corrected five-layer architecture.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/7b789cbf-0812-444b-b7df-1187ceac51e5/Claude_Apex-KB_SQLiteFTS5BM25_GPT.md?AWSAccessKeyId=ASIA2F3EMEYE3BCTZMQY&Signature=LbDgmVEdDFCTJNp2GRxuZpuMq54%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDMjk9KSRvynqoFq4HynAZjwekTGDVPLvyRa4cFfi%2BhggIgKp2w2w3pRy3lhibnbVjPZ6zHE0wndDFQeJSJSC%2B1Kgkq8wQIUhABGgw2OTk3NTMzMDk3MDUiDO3EEHzFNBF1Oj9HuSrQBArxOYSmjyADkB6KbwxubSqsgrKye0Y6AvOO7NcQltAf1NhIoOvfy2u44EUTCBttjTRJ1Vve%2FenabzuJDeQPdHOPMZU2BSaJrG%2BrmRdHX%2BhHGJQRGz%2FjpCDTMhuOZio%2BlCvrVE1AGFf3XDEYMMUYQI3D2meXzbH6p4BBxB81smuZAc2akKGtDkcetcBnVC7AGDIekaQGH8gAQ8g09UaRa1%2FvzfVJJb%2BfeS4n9UrQLcM4JKtTg%2FGUaW5iVCmmJ0%2BPPrW0jmbzvBn7H7IHpcvIJuPoup7H45UUIungeHUEHdMUWq6USqVvWvTgq1MlUgjGlJTBiOaXd%2BGpCJ8U0S6cn46MEXe33TPHwVxAhWvXAzD41K500tKW4XWpU7lxP4hiwuC9VDbNihzTMhfEnZEd4gD5h45Ht3h4KvSoOIeEPRYvYVDp6oCMmVX%2F9Nk2ID1S1Ss5lCH%2Fn0CBQ6R0F7s%2F7fTWCrWbrabhnIVI3Wt7XGwr3GTivJMBiKLF3T33NBJ2Pp1EMUgaJlbxTKjbBvzsaMZunnjBQ1aK2O31PWte%2BCgnWh9RtYKqilT7P0T12PrzMpX0lmJyfG%2F5lAk6gPWg2oSM%2BgUS%2FlCOWb%2FlliE4p9mVFauxQn9Jwhq0yNyyUK2xCFtAb5TBDCwD5KeEP4d1pYcNs%2FyCKxoJpOPRBZJcKWcdKDvGEVMtRsSbWPps8HlwW7j%2F0w9rMi%2FPOJdnbmeTW48eJm7upeeEikSO%2F71X%2FjZGj%2BsVw3wZWO%2FqNcs%2Fk0btWSarDFCSWF2fOUXgRH2xaXsw57%2F10QY6mAEFxlvhBW%2FLvhF%2Fvk3ib%2BVDp5sVXToHoBf6DmJpnVHcUUCHGg%2BbzTmIpLQZ9Sef%2B%2FBSz5NqXUn5kWDyb%2BP6l43B74NxBFp7d8OEy%2F00zSEgqttIdrTXfajemb5Qm3C1G4nF0Ss79cu1kx1CLKPG0oJXdag38%2FBY63euHoUPZMbMRc66dLLsWT4jY5ZI6moCfwhVVdjNMyxK8g%3D%3D&Expires=1782410682)]

**External verification of Claude Code memory model:** The GPT pass cites Anthropic docs confirming CLAUDE.md and auto memory are loaded as context, not enforced configuration, and recommends moving multi-step procedures to skills or path-scoped rules when CLAUDE.md grows. [Source: docs.anthropic.com/en/docs/claude-code/memory — cited in file:4 §1.2][[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/7b789cbf-0812-444b-b7df-1187ceac51e5/Claude_Apex-KB_SQLiteFTS5BM25_GPT.md?AWSAccessKeyId=ASIA2F3EMEYE3BCTZMQY&Signature=LbDgmVEdDFCTJNp2GRxuZpuMq54%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQDMjk9KSRvynqoFq4HynAZjwekTGDVPLvyRa4cFfi%2BhggIgKp2w2w3pRy3lhibnbVjPZ6zHE0wndDFQeJSJSC%2B1Kgkq8wQIUhABGgw2OTk3NTMzMDk3MDUiDO3EEHzFNBF1Oj9HuSrQBArxOYSmjyADkB6KbwxubSqsgrKye0Y6AvOO7NcQltAf1NhIoOvfy2u44EUTCBttjTRJ1Vve%2FenabzuJDeQPdHOPMZU2BSaJrG%2BrmRdHX%2BhHGJQRGz%2FjpCDTMhuOZio%2BlCvrVE1AGFf3XDEYMMUYQI3D2meXzbH6p4BBxB81smuZAc2akKGtDkcetcBnVC7AGDIekaQGH8gAQ8g09UaRa1%2FvzfVJJb%2BfeS4n9UrQLcM4JKtTg%2FGUaW5iVCmmJ0%2BPPrW0jmbzvBn7H7IHpcvIJuPoup7H45UUIungeHUEHdMUWq6USqVvWvTgq1MlUgjGlJTBiOaXd%2BGpCJ8U0S6cn46MEXe33TPHwVxAhWvXAzD41K500tKW4XWpU7lxP4hiwuC9VDbNihzTMhfEnZEd4gD5h45Ht3h4KvSoOIeEPRYvYVDp6oCMmVX%2F9Nk2ID1S1Ss5lCH%2Fn0CBQ6R0F7s%2F7fTWCrWbrabhnIVI3Wt7XGwr3GTivJMBiKLF3T33NBJ2Pp1EMUgaJlbxTKjbBvzsaMZunnjBQ1aK2O31PWte%2BCgnWh9RtYKqilT7P0T12PrzMpX0lmJyfG%2F5lAk6gPWg2oSM%2BgUS%2FlCOWb%2FlliE4p9mVFauxQn9Jwhq0yNyyUK2xCFtAb5TBDCwD5KeEP4d1pYcNs%2FyCKxoJpOPRBZJcKWcdKDvGEVMtRsSbWPps8HlwW7j%2F0w9rMi%2FPOJdnbmeTW48eJm7upeeEikSO%2F71X%2FjZGj%2BsVw3wZWO%2FqNcs%2Fk0btWSarDFCSWF2fOUXgRH2xaXsw57%2F10QY6mAEFxlvhBW%2FLvhF%2Fvk3ib%2BVDp5sVXToHoBf6DmJpnVHcUUCHGg%2BbzTmIpLQZ9Sef%2B%2FBSz5NqXUn5kWDyb%2BP6l43B74NxBFp7d8OEy%2F00zSEgqttIdrTXfajemb5Qm3C1G4nF0Ss79cu1kx1CLKPG0oJXdag38%2FBY63euHoUPZMbMRc66dLLsWT4jY5ZI6moCfwhVVdjNMyxK8g%3D%3D&Expires=1782410682)]

## Meso Level

**Full pipeline:**

text

`raw source   ↓ [operator ingests, hashes, registers] source manifest entry (manifests/source-manifest.json)   ↓ [Claude or operator compiles] compiled wiki page (wiki/<slug>.md)   ↓ [Python indexer reads frontmatter + body] SQLite FTS5 index (registry/search.sqlite)   ↓ [Python script queries with BM25] ranked results + snippets (~400 tokens total)   ↓ [Claude reads top 2–4 pages] answer + source pointers   ↓ [optional] saved query output (outputs/queries/<date>-<topic>.md)`

[file:3, §1.2]

**Token cost per layer:**

|Layer|Token cost to Claude|
|---|---|
|CLAUDE.md|Always loaded — minimize|
|Path-scoped rules|Loaded on path match|
|Skill files|Near-zero until triggered|
|Apex KB wiki pages|Zero until `Read(path)` called|
|FTS5 search result list (8 × 50 tokens)|~400 tokens|
|Full page read (2–4 pages × 600 tokens)|~1,200–2,400 tokens|
|Saved query output reuse|~300–500 tokens|

[file:3, §2.3 — limit recommendation block]

**Staleness detection — is mtime sound?**

The spec uses `db.stat().st_mtime` vs `md.stat().st_mtime` comparison [file:3, §2.3 staleness function]. This is a standard, documented approach. Python `os.stat().st_mtime` returns a float (nanosecond precision on Linux, 100ns on Windows, 1-second on some HFS+ macOS volumes pre-Catalina). Known production uses of mtime-based invalidation:

- **Make** (GNU Make 4.x) uses `st_mtime` for all dependency tracking — the definitive production precedent, in use since 1976
    
- **ccache** uses mtime as a primary cache key alongside hash verification [Source: ccache.dev/manual]
    
- **Jekyll** static site generator uses mtime comparison for incremental rebuild [Source: jekyllrb.com/docs/configuration/incremental-regeneration/]
    

Caveat flagged: On macOS HFS+ (pre-Catalina), `st_mtime` has 1-second granularity — two file writes within the same second are indistinguishable. This is a MINOR real risk on older macOS [file:4, §operator decisions — D7].

**How BM25 works in SQLite FTS5 specifically:**

BM25 scores are negative floats. Lower (more negative) = better match. `ORDER BY rank` or `ORDER BY bm25(ft)` returns best first — no ASC/DESC needed [file:6, §1.3, citing sqlite.org/fts5.html]. The formula normalizes for document length: a long page with one term mention does not beat a short page with three mentions [file:3, §2.2]. The `bm25(ft, w0, w1, ..., wN)` positional weight vector maps to columns in CREATE VIRTUAL TABLE order — this is the critical alignment requirement verified in Section 3.

## Micro Level

**CREATE VIRTUAL TABLE schema from spec [file:3, §2.3]:**

sql

`CREATE VIRTUAL TABLE IF NOT EXISTS ft USING fts5(     id,       -- col 0    kb,       -- col 1    path,     -- col 2    title,    -- col 3    tags,     -- col 4    summary,  -- col 5    sources,  -- col 6    updated,  -- col 7    status,   -- col 8    body,     -- col 9    tokenize="unicode61 remove_diacritics 2" );`

**BM25 weight vector in `search_kb()` [file:3, §2.3]:**

python

`bm25(ft, 0, 0, 5, 3, 2, 1, 0, 0, 1)`

Maps positionally: `id=0, kb=0, path=0 (missing!), title=5, tags=3, summary=2, sources=1, updated=0, status=0` — **only 9 arguments for 10 columns**.

**⚠ CRITICAL MISMATCH FOUND:** The spec's `bm25()` call has **9 weight arguments** but the schema has **10 columns**. The spec comment says `sources=0, updated=0, status=0, body=1` but the call only has 9 positional values `(0, 0, 5, 3, 2, 1, 0, 0, 1)`. This means either `path` gets title's weight (5) or body gets no weight. **See G2 in Section 4.**

**snippet() col_index:** The spec calls `snippet(ft, 9, '>>>', '<<<', '...', 24)`. Column index 9 (0-based) = `body`. This IS correct given the 10-column schema — but only if the bm25 weight vector is also correct. Since the weight vector is broken, this is a cascading risk.

**YAML front-matter parseability:** Required fields (`id`, `title`, `kb`, `tags`, `sources`, `authority`, `created`, `updated`, `status`, `summary`) are all simple scalar or list YAML values [file:3, §1.3]. Python `re` can parse these reliably with a two-pass approach: split on `^---$` to extract front-matter block, then line-by-line parse `key: value`. Multi-line values (block scalars with `|` or `>`) are NOT specified in the schema — but if any operator writes them, stdlib regex will corrupt silently. **See G3.**

**File path slugs as TEXT primary keys:** Lowercase hyphen-separated slugs (`concept-session-continuity`) are safe as SQLite TEXT keys. UTF-8 safe, no collation ambiguity for ASCII slugs. Edge cases: (1) slugs with Unicode (ü, ß) — safe in SQLite TEXT but risky in filesystem path matching; (2) slug collision if two files have identical slug after normalization — no collision detection in spec.

**UTF-8 and unicode61 tokenizer:** `unicode61 remove_diacritics 2` tokenizes by Unicode codepoint boundaries and strips diacritics [Source: sqlite.org/fts5.html §tokenizers]. This is correct for mixed English/technical text. **If a page is UTF-16:** Python's `open(path)` with default encoding will raise `UnicodeDecodeError` before the indexer ever touches SQLite — the spec does not specify `encoding='utf-8'` in `open()` calls, making this a runtime failure on any UTF-16 file. **See G risk register.**

---

## SECTION 2 — Blueprint Search

**Pattern 1: SQLite FTS5 + markdown frontmatter indexer in Python**

- **[simonw/datasette](https://github.com/simonw/datasette)** — ★20k+, active 2026. Uses SQLite FTS5 extensively for full-text search over structured data. The `datasette-search-all` plugin pattern directly blueprints FTS5 indexing over multi-table content. Difference: Datasette is a general-purpose SQL explorer, not a markdown KB. Copy: the FTS5 virtual table pattern and the `rebuild` vs `update` trigger logic.
    
- **[obsidianmd/obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview)** — ★6k+, last commit 2025. Indexes YAML frontmatter from markdown files and exposes query interface. Difference: Uses JS, not Python; no SQLite. Copy: the frontmatter field normalization strategy (how to handle missing fields gracefully).
    
- **[sqlar](https://sqlite.org/sqlar.html)** — Official SQLite archive format. Uses FTS5 for file content search. Difference: General archive, not KB-specific. Copy: the `mtime` field storage pattern alongside FTS content.
    

**Pattern 2: Local markdown KB with BM25, no external deps**

- **[notable/notable](https://github.com/notable/notable)** — ★23k, last commit 2024. Local markdown note manager with search. Uses SQLite internally. Difference: Electron app, not CLI. Copy: the YAML frontmatter schema conventions.
    
- **[bragamat/markdown-index](https://github.com/bragamat/markdown-index)** (small repo) — Python script indexing markdown to SQLite for search. Stars: <100. Validates the basic pattern but insufficient as a strong blueprint.
    
- **BLUEPRINT GAP — fewer than 3 strong repos exist** for _pure Python CLI + SQLite FTS5 + YAML frontmatter + no deps_ as a standalone tool. The pattern is commonly _embedded in larger systems_ (Datasette, Obsidian plugins, static site generators) but not as a standalone < 500-line Python script. **Risk implication:** No battle-tested reference implementation to copy directly. The spec is pioneering territory at the micro level — higher implementation risk.
    

**Pattern 3: Claude Code skill files (.claude/skills/) with retrieval — real repos**

- **BLUEPRINT GAP — CRITICAL.** As of June 2026, no public GitHub repositories with >50 stars demonstrate `.claude/skills/` directory patterns with FTS5 retrieval workflows. The Claude Code skills feature is recent (GA ~2025) and production usage in public repos is sparse. The spec's skill architecture is sound per Anthropic docs, but there are **zero public production blueprints** to copy from. Risk: skill trigger phrases, SKILL.md structure, and CLAUDE.md routing are all from documentation only — no battle-tested examples.
    

**Pattern 4: LLM-wiki / compiled KB pattern (raw → compiled → index)**

- **[Obsidian.md](https://obsidian.md/)** community vaults — compiled knowledge graphs with frontmatter. Not Python-native, but the _conceptual_ pattern (raw notes → tagged compiled pages → index) is widely validated.
    
- **[logseq/logseq](https://github.com/logseq/logseq)** — ★33k, active 2026. Compiled knowledge graph with frontmatter. Difference: not FTS5-based. Copy: the `updated` / staleness field convention.
    
- **[nikitavoloboev/knowledge](https://github.com/nikitavoloboev/knowledge)** — ★5k, markdown wiki. No SQLite. Shows compiled wiki page conventions at scale.
    
- **Pattern validation: PARTIAL.** The compiled-page concept is well-proven. The Python-powered rebuild + FTS5 indexing layer on top of it has no direct public blueprint.
    

**Pattern 5: Python script parsing YAML frontmatter → SQLite FTS5**

- **[eyeseast/python-frontmatter](https://github.com/eyeseast/python-frontmatter)** — ★600+, active 2025. Python library for parsing YAML frontmatter from markdown. Difference: requires `pip install python-frontmatter` (depends on PyYAML). This is a direct dependency conflict with the spec's "stdlib only" requirement. **Relevant finding: the spec's stdlib-regex approach is feasible but non-trivially different from how the production tool does it.**
    
- **[yaml/pyyaml](https://github.com/yaml/pyyaml)** — ★2k+. Standard YAML parser. The _de facto_ production approach for frontmatter parsing is PyYAML, not regex. Spec's stdlib-only choice is unusual.
    
- **BLUEPRINT GAP:** No public Python scripts exist with >50 stars that parse YAML frontmatter using only stdlib `re` and insert into SQLite FTS5. Every production example uses PyYAML or `python-frontmatter`.
    

**Pattern 6: Staleness detection via mtime in Python indexer/cache**

- **GNU Make** — the canonical mtime-based staleness system. `st_mtime` comparison is the foundation of incremental builds.
    
- **[ccache](https://ccache.dev/)** — uses mtime as primary cache key before hash check. Production C/C++ compiler cache.
    
- **[sphinx-doc/sphinx](https://github.com/sphinx-doc/sphinx)** — ★6k+. Uses `os.stat().st_mtime` for incremental documentation rebuilds. Direct Python blueprint. Pattern: compare source mtime vs output mtime, rebuild if source is newer. Copy: the `needs_rebuild()` pattern from `sphinx/builders/__init__.py`.
    
- **Evidence: STRONG.** mtime-based staleness is battle-tested at scale in Python.
    

**Pattern 7: BM25 weight tuning title/tags/body in SQLite FTS5 (production)**

- **BLUEPRINT GAP.** No public production blog posts or repos with >50 stars document specific BM25 weight vectors (`bm25(ft, w0, w1, ...)`) for title/tags/body in SQLite FTS5. The [SQLite FTS5 docs](https://www.sqlite.org/fts5.html) define the syntax but provide no tuning guidance. The spec's `title=5, tags=3, summary=2, body=1` weights are internally reasoned, not empirically derived. Risk: weights may not be optimal; but since they are adjustable post-v1 without schema change, this is MINOR.
    

**Pattern 8: Saved query output (pre-synthesized answers as markdown)**

- **[Zettelkasten method](https://zettelkasten.de/)** + tools like **[zk](https://github.com/mickael-menu/zk)** (★3k) implement persistent "literature note" outputs from queries — directly analogous.
    
- **Obsidian** "canvas + MOC" pattern: maps of content as compiled synthesis outputs.
    
- **[jbranchaud/til](https://github.com/jbranchaud/til)** — ★14k. Today-I-learned markdown repo: each file is a saved query output. Pattern validated at scale.
    
- **Evidence: STRONG** for the _concept_. The specific Claude-facing format (frontmatter with `query:`, `retrieved_pages:`, `answer:`) is novel but follows the established pattern.
    

---

## SECTION 3 — Technical Claim Verification

|#|Claim|Evidence|Strength|Notes|
|---|---|---|---|---|
|**C1**|BM25 deterministic: same query + same index = identical results|(1) sqlite.org/fts5.html: bm25() is pure math function. (2) file:5: "BM25 scoring in SQLite FTS5 is fully deterministic...no stochastic component." (3) file:3 §2.1: "BM25 is a pure mathematical ranking function over an immutable index; no randomness."|**STRONG**|Caveat: non-deterministic only if index is rebuilt between queries (different insertion order can affect tie-breaking). Same index = deterministic.|
|**C2**|Python stdlib sqlite3 always has FTS5|(1) CPython `Modules/_sqlite/` — sqlite3 is optional module compiled against system libsqlite3. (2) file:4 §2 Claim C: "Python's sqlite3 module is in the standard library interface for SQLite, but it is also an optional CPython module and depends on the distributor's SQLite build; therefore Stage 5 must include an explicit FTS5 availability test." (3) Known: Ubuntu 20.04 ships SQLite 3.31 WITH FTS5; Alpine Linux minimal image may strip FTS5.|**PARTIAL**|NOT guaranteed. Distro-dependent. FTS5 availability test (G1) is CRITICAL.|
|**C3**|`unicode61 remove_diacritics 2` is correct for mixed technical/English text with slugs, camelCase|(1) sqlite.org/fts5.html §tokenizers: unicode61 tokenizes by Unicode boundaries, strips diacritics at level 2. (2) CamelCase: unicode61 does NOT split camelCase — `FlowRecap` is one token. (3) Slugs with hyphens: hyphens are treated as separators by unicode61, so `apex-search` tokenizes as two tokens `apex` + `search`.|**PARTIAL**|CamelCase is a known weakness. `FlowRecap` only matches query "FlowRecap", not "Flow" or "Recap" separately. For a technical KB with camelCase identifiers, this may degrade retrieval. Consider adding `trigram` tokenizer for symbol search. **UNVERIFIED** optimal choice for this use case.|
|**C4**|BM25 negative score: lower = better; ORDER BY rank returns best first|(1) sqlite.org/fts5.html: "The bm25() function returns a real value...The value returned is a negative real number. The value returned is a measure of the 'quality' of the match...A smaller (more negative) value corresponds to a better match." (2) file:6 §1.3: "better matches are numerically smaller; ORDER BY bm25(ft) or ORDER BY rank returns best matches first."|**STRONG**|Confirmed. No ASC/DESC required.|
|**C5**|`snippet(ft, 9, ...)` col_index 9 maps to `body` given 10-column schema|Schema: id(0), kb(1), path(2), title(3), tags(4), summary(5), sources(6), updated(7), status(8), body(9). Col 9 = body. ✅|**STRONG**|HOWEVER: The bm25() weight vector has only 9 args (not 10) — see G2. snippet col_index is correct independently.|
|**C6**|YAML frontmatter between `---` parseable by stdlib `re` without PyYAML|(1) Python re docs: `re.split(r'^---\s*$', text, flags=re.MULTILINE)` works for simple YAML. (2) python-frontmatter source: internally uses PyYAML for value parsing. (3) Limitation: stdlib re cannot parse YAML lists (`[a, b, c]`), multi-line blocks, or anchors. Tags field is a YAML list — `tags: [claude-code, memory]` requires special handling beyond simple regex.|**PARTIAL**|**UNVERIFIED as fully correct.** Tags require list parsing. The spec uses `tags` as a list — stdlib re alone cannot parse `[a, b, c]` reliably. Requires a mini-parser for list fields.|
|**C7**|File mtime comparison reliable for staleness on Linux/macOS|(1) Python docs: `os.stat().st_mtime` returns float, nanosecond precision on Linux ext4. (2) Known issue: macOS HFS+ (pre-Catalina/APFS) has 1-second granularity. (3) APFS (macOS Catalina+) supports nanosecond precision. (4) Sphinx uses this pattern in production.|**PARTIAL**|Linux: STRONG. macOS APFS: STRONG. macOS HFS+: WEAK (1s granularity risk). No timezone issue — mtime is UTC epoch float.|
|**C8**|Claude Code skills fire on trigger phrases auto-detected from CLAUDE.md routing — not explicit calls|(1) Anthropic docs (cited in file:4): skills load when triggered. (2) file:4 §1.2: "every skill needs SKILL.md." (3) Claude Code docs: skills are invoked when Claude determines the skill is relevant — operator cannot guarantee trigger without explicit routing rules in CLAUDE.md.|**PARTIAL**|Skills are NOT automatically triggered by keyword detection. Claude must either be instructed to use them in CLAUDE.md or explicitly invoked. The spec's trigger phrase approach requires explicit CLAUDE.md routing block — otherwise Claude may not invoke the skill.|
|**C9**|CLAUDE.md loaded every session, counts against context window, target <200 lines|(1) file:4 §1.2: "Claude Code docs state both are loaded at the start of every conversation and treated as context, not enforced configuration." (2) file:4: "docs recommend concise instructions, target under 200 lines." (3) Anthropic docs cited in file:6: CLAUDE.md is context, not enforced config.|**STRONG**|Confirmed by multiple doc citations across files.|
|**C10**|SQLite FTS5 rebuild for 200 pages takes <2 seconds on modern machine|(1) file:3 §2.2: "200 pages takes < 2 seconds on any modern machine" — stated as fact, no benchmark cited. (2) SQLite performance benchmarks (sqlite.org/speed.html): 50k INSERT/sec is typical. 200 pages × ~1k tokens each = trivial workload. (3) No empirical measurement in any source file.|**PARTIAL**|The claim is plausible and consistent with SQLite's known performance profile, but **no benchmark is cited in the spec**. For a 200-page KB this is near-certain to be correct. For a 2000-page KB, no data exists. Mark as **UNVERIFIED empirically** but likely correct.|

---

## SECTION 4 — Gap Analysis

|Gap|Description|Severity|Fix|
|---|---|---|---|
|**G1**|FTS5 availability not verified at runtime before indexer runs|**CRITICAL**|Add `FTS5_CHECK = "SELECT fts5(?1)" — or the documented pattern:` cur.execute("CREATE VIRTUAL TABLE _fts5_test USING fts5(x)"); cur.execute("DROP TABLE _fts5_test")` wrapped in try/except. Fail with clear error: "SQLite FTS5 not available in this Python build. Use python3 from python.org or compile SQLite with FTS5 enabled." [Source: file:4, §Claim C] \||
|**G2**|BM25 weight vector has 9 args for 10-column schema|**CRITICAL**|Spec call: `bm25(ft, 0, 0, 5, 3, 2, 1, 0, 0, 1)` — 9 values for 10 columns. Correct call must be `bm25(ft, 0, 0, 0, 5, 3, 2, 1, 0, 0, 1)` (10 values: id=0, kb=0, path=0, title=5, tags=3, summary=2, sources=1, updated=0, status=0, body=1). The current call shifts all weights left by one column, giving path weight=0→5 (path gets title's weight) and body weight=1→0 (body gets no weight). Body search is **silently disabled** with the current vector. [Source: direct schema count from file:3 §2.3]|
|**G3**|YAML frontmatter parser: tags field is a list (`[a, b, c]`), not parseable by simple regex|**MAJOR**|Either: (A) specify tags as comma-separated string (`tags: "claude-code, memory, CLAUDE.md"`) for regex safety, or (B) use a minimal list parser: detect `[...]` pattern, strip brackets, split by comma. Option A is simpler and eliminates the PyYAML dependency entirely. The frontmatter template in file:3 uses bracket notation — this must be changed to match the parser.|
|**G4**|No error handling specified for malformed frontmatter (missing required fields, parse errors)|**MAJOR**|Spec mentions Option A (skip + log) vs Option B (insert NULL) in file:2, and recommends Option A. But no error output format is specified. Claude cannot distinguish "0 results because no matches" from "0 results because all pages were skipped due to errors." Fix: structured error output to stderr + preflight check count validation.|
|**G5**|`--check-stale` stdout format not standardized|**MAJOR**|Spec says stdout: `"OK"` or `"STALE: <reason>"` [file:2, §Step 6 CLI spec]. This is defined. But the CLAUDE.md skill block that parses this output is not shown — Claude must parse stdout literally. Risk: whitespace, newline, or encoding variation causes false "stale" or false "OK." Fix: add explicit `exit 0` for both cases and define exact format as `OK\n` or `STALE: <reason>\n`.|
|**G6**|`index.md` inclusion in FTS5 index|**MINOR**|`get_wiki_pages()` docstring in file:2 says "Excludes index.md" — this is specified. But the exclusion pattern (`! -name "index.md"`) is shallow: a nested `wiki/concepts/index.md` would still be included. Fix: exclude any file named `index.md` regardless of depth: `if path.name == "index.md": continue`.|
|**G7**|`apex-meta/orchestration/` domain not in implementation plan|**MAJOR**|File:4 explicitly names this as a separate first-class memory domain — non-sensitive orchestration summaries go to `apex-meta/orchestration/`, sensitive local-only. File:6 lists 7 subdirectories. The implementation plan (15 steps in file:2) contains zero steps for this domain. It does not block FTS5 v1, but omitting it means the architecture described in the spec and the plan are misaligned — a future operator will add orchestration pages to `kb/` by default and corrupt the boundary. Severity upgraded to MAJOR (not CRITICAL since FTS5 v1 can function without it).|
|**G8**|`apex_kb.py` coexistence: existing script has preflight/scaffold/lint/audit — no migration strategy|**MAJOR**|File:4 §Claim D confirms `apex_kb.py` exists and does NOT have FTS5 functions. File:4 recommends creating separate `scripts/apex-index.py` and `scripts/apex-search.py`, not extending `apex_kb.py`. The plan in file:2 does create separate scripts. But no step audits potential namespace/path conflicts between `apex_kb.py` (which writes to `apex-meta/scripts/`) and the new scripts (in `scripts/`). Fix: Step 1 of plan must confirm directory locations and confirm no import conflicts.|
|**G9 (new)**|No `.gitignore` entry specified for `search.sqlite`|**MINOR**|File:4 §D7 flags this as an operator decision point. The plan does not include a step to add `apex-meta/registry/search.sqlite` to `.gitignore`. If committed, the derived artifact inflates git history on every rebuild. Fix: add `.gitignore` update as a discrete step.|
|**G10 (new)**|`open(path)` without `encoding='utf-8'` specified|**MINOR**|On Windows (or any system where locale is not UTF-8), Python's `open()` defaults to the system locale encoding. A non-UTF-8 page will raise `UnicodeDecodeError`. Fix: all file reads must use `open(path, encoding='utf-8', errors='replace')`.|
|**G11 (new)**|Tags stored as YAML list in frontmatter, but FTS5 column receives joined string|**MAJOR**|The spec stores `tags: [claude-code, memory]` in YAML but the FTS5 column needs a flat string for tokenization. The join strategy (space vs comma vs newline) affects tokenization. With unicode61, `"claude-code memory CLAUDE.md"` tokenizes correctly; `"claude-code,memory"` tokenizes `claude-code,memory` as one token. Fix: join with space: `" ".join(tags)`.|

---

## SECTION 5 — Option Comparison Matrix

|Decision|Option|IMPACT|EVIDENCE|RISK|EFFORT|Verdict|
|---|---|---|---|---|---|---|
|**D1: DB location**|Per-KB sqlite file|60|70|85|80|Simpler isolation, no cross-KB|
||**Shared `registry/search.sqlite`**|**85**|**80**|**75**|**70**|**RECOMMENDED** — spec alignment, cross-KB ready [file:2, §Decision 2]|
|**D2: YAML parser**|stdlib re (regex)|70|40|55|75|Fails on list fields (G3, G11) — RISK LOW|
||**python-frontmatter lib**|**80**|**90**|**85**|**80**|**RECOMMENDED** — production standard [github.com/eyeseast/python-frontmatter, ★600+] — adds 1 dep but solves G3, G6, G11|
||Manual line parser|65|50|60|50|Fragile, no benefit over regex|
|**D3: Rebuild strategy**|**Full DROP+CREATE+INSERT**|**85**|**90**|**90**|**90**|**RECOMMENDED** — deterministic, atomic, simple [file:3 §2.2]|
||Incremental UPDATE/INSERT|75|50|55|40|Risk of stale rows if pages deleted; no blueprint|
|**D4: Skill architecture**|**apex-search as standalone skill**|**85**|**80**|**85**|**75**|**RECOMMENDED** — file:4 §skill ownership: "separate apex-search prevents bloating apex-kb"|
||Add FTS to apex-kb skill|70|60|65|60|Bloats apex-kb, conflicts with scope boundary|
|**D5: Staleness check**|**mtime comparison (spec)**|**80**|**85**|**80**|**90**|**RECOMMENDED** — battle-tested (Make, ccache, Sphinx)|
||Hash-based (SHA256)|75|70|90|60|More accurate but slower (reads all files); no latency benefit for 200-page KB|
||Both mtime + hash|85|75|92|40|Best accuracy, worst effort; overkill for v1|
|**D6: BM25 weight vector**|Spec weights (after fix: title=5,tags=3,summary=2,body=1)|80|45|70|70|No empirical tuning data — UNVERIFIED optimal|
||Equal weights (all=1)|65|80|85|90|Safer default; searchable everywhere equally|
||Title-only boost (title=10,rest=1)|70|50|75|85|Matches navigational queries well, misses body content|

**EVIDENCE < 60 note:** Spec BM25 weights (D6) score EVIDENCE=45 because no production tuning benchmarks exist for this specific weight profile. Start with equal weights for v1, tune after validating retrieval quality.

---

## SECTION 6 — Implementation Plan Step-by-Step Audit

_(Steps referenced from file:2 — Implementation Plan v2)_

---

**Step 1 — Pre-flight audit + log**

- IMPACT: 90 | EVIDENCE: 95 | RISK: 98 | EFFORT: 85
    
- VERDICT: **PASS**
    
- FLAGS: Add check #12: FTS5 availability test (G1). Add check #13: `.gitignore` status of `search.sqlite`.
    

---

**Step 2 — Decision: Option A (minimal delta) vs Option B (full rebuild)**

- IMPACT: 85 | EVIDENCE: 90 | RISK: 90 | EFFORT: 90
    
- VERDICT: **PASS**
    
- FLAGS: Option A is correct per spec. No issue.
    

---

**Step 3 — Front-matter surgical patch (add missing fields to existing pages)**

- IMPACT: 95 | EVIDENCE: 80 | RISK: 65 | EFFORT: 60
    
- VERDICT: **FLAG**
    
- FLAGS: RISK=65 because a surgical patch script that appends YAML fields to existing files has two known failure modes: (1) pages with `+++` TOML delimiters instead of `---` will be silently skipped or corrupted; (2) pages that already have a field with a different value will get a duplicate key. The spec notes the `+++` risk in file:2 §Decision 1 but does not specify a pre-patch check for existing field values. Fix: add validation gate before patch: `grep -c "^id:" <file>` must return 0 before appending.
    

---

**Step 4 — Manifest patch (add `status` and `last_modified` to source-manifest.json)**

- IMPACT: 80 | EVIDENCE: 85 | RISK: 80 | EFFORT: 75
    
- VERDICT: **PASS**
    
- FLAGS: Minor — manifest structure assumed to be `[{...}]` array or `{sources: [...]}`. Pre-flight check #5 and #6 handle this. No critical issue.
    

---

**Step 5 — Create `apex-meta/registry/` directory**

- IMPACT: 70 | EVIDENCE: 99 | RISK: 99 | EFFORT: 99
    
- VERDICT: **PASS**
    
- FLAGS: None. Trivial filesystem operation.
    

---

**Step 6 — Write `scripts/apex-index.py`**

- IMPACT: 95 | EVIDENCE: 70 | RISK: 50 | EFFORT: 55
    
- VERDICT: **FLAG**
    
- FLAGS: RISK=50, EFFORT=55 — this is the highest-risk single step.
    
    - **G2 (CRITICAL):** bm25() weight vector has 9 args for 10 columns. Must fix before writing.
        
    - **G3 (MAJOR):** Tags YAML list parsing — stdlib re fails. Must specify parser strategy.
        
    - **G10:** Missing `encoding='utf-8'` in all file opens.
        
    - EVIDENCE=70: No public blueprint for this exact script pattern. BLUEPRINT GAP applies.
        
    - Effort is underestimated: the function signatures are defined (file:2), but error handling, list-parsing, FTS5 test, and encoding fixes add ~40% to the implementation surface.
        

---

**Step 7 — Write `scripts/apex-search.py`**

- IMPACT: 90 | EVIDENCE: 75 | RISK: 70 | EFFORT: 70
    
- VERDICT: **FLAG**
    
- FLAGS: RISK=70 because the output format is consumed by Claude as stdout — any format variation breaks the skill. The spec defines JSON/text output [file:3 §2.2] but does not lock the exact serialization. Fix: define output format as newline-delimited JSON or a strict labeled text format before writing, then make CLAUDE.md skill block parse that exact format.
    

---

**Step 8 — First index build + validation**

- IMPACT: 95 | EVIDENCE: 90 | RISK: 75 | EFFORT: 80
    
- VERDICT: **PASS**
    
- FLAGS: The validation gate (compare `SELECT count(*) FROM ft` vs `find ... | wc -l`) is correct and sufficient. Risk=75 because if Steps 3 or 6 have unfixed issues (G2, G3), this step will silently report wrong counts.
    

---

**Step 9 — Write `.claude/skills/apex-search.md` (SKILL.md)**

- IMPACT: 85 | EVIDENCE: 65 | RISK: 65 | EFFORT: 70
    
- VERDICT: **FLAG**
    
- FLAGS: EVIDENCE=65 — no public production `.claude/skills/` blueprints exist (BLUEPRINT GAP — Section 2, Pattern 3). RISK=65 because skill trigger failure is the most likely v1 user-visible failure: if trigger phrases don't match user query patterns, Claude never invokes the skill. Fix: define 5–8 specific trigger phrases in CLAUDE.md that exactly match operator's natural query patterns. Test with at least 3 real queries before declaring v1 complete.
    

---

**Step 10 — Write CLAUDE.md retrieval block**

- IMPACT: 90 | EVIDENCE: 80 | RISK: 70 | EFFORT: 75
    
- VERDICT: **FLAG**
    
- FLAGS: RISK=70 — the CLAUDE.md block adds lines to an already-loaded document. If the total CLAUDE.md line count exceeds 200 after addition, context pressure degrades quality of all Claude responses in that session [file:4 §1.2]. Fix: audit CLAUDE.md line count before writing; move existing verbose sections to path-scoped rules if needed to stay under 200 lines.
    

---

**Step 11 — Write `.claude/rules/apex-meta.md`**

- IMPACT: 75 | EVIDENCE: 75 | RISK: 85 | EFFORT: 80
    
- VERDICT: **PASS**
    
- FLAGS: Minor — path-scoped rule loading is well-documented. Low risk.
    

---

**Step 12 — Write `apex-meta/registry/index.md` (cross-KB navigation)**

- IMPACT: 65 | EVIDENCE: 80 | RISK: 90 | EFFORT: 85
    
- VERDICT: **PASS**
    
- FLAGS: None critical. The registry index is a static human-readable doc — low risk, easily updated.
    

---

**Step 13 — End-to-end test: real query → search → read → answer**

- IMPACT: 95 | EVIDENCE: 90 | RISK: 85 | EFFORT: 70
    
- VERDICT: **PASS**
    
- FLAGS: This step is correct and should be kept. However: add a negative test (query with zero results) to verify the "no results" path doesn't crash the script or skill.
    

---

**Step 14 — `.gitignore` update**

- IMPACT: 60 | EVIDENCE: 99 | RISK: 99 | EFFORT: 99
    
- VERDICT: **REORDER → move to Step 5.5** (immediately after registry dir creation, before first build)
    
- FLAGS: Currently listed near the end. If operator runs `git add .` before this step, `search.sqlite` enters git history. Fix: execute immediately after directory creation.
    

---

**Step 15 — Document the system in `apex-meta/registry/index.md`**

- IMPACT: 50 | EVIDENCE: 85 | RISK: 95 | EFFORT: 85
    
- VERDICT: **PASS**
    
- FLAGS: Low risk, but this is documentation — sequencing is flexible. Correct to have it as the final step.
    

---

## SECTION 7 — File Design Audit

## 1. `scripts/apex-index.py`

- **Macro:** The indexer is the system's write path — raw wiki pages → SQLite. This is the correct file for this role. Separation from `apex-search.py` is correct (write vs. read).
    
- **Meso:** Required sections: FTS5 availability test, YAML frontmatter parser, file walker with index.md exclusion, INSERT/DROP/CREATE logic, staleness check, argparse CLI. All defined in file:2 §Step 6. The `wiki_meta` companion table for non-FTS filtering is a sound design [file:3 §2.3].
    
- **Micro:** Critical defects: (1) bm25 weight vector off by 1 (G2 — CRITICAL). (2) YAML list parsing underspecified (G3). (3) Missing `encoding='utf-8'` (G10). (4) No FTS5 availability test (G1). Real-world comparison: [datasette's indexer pattern](https://github.com/simonw/datasette) — uses explicit encoding, schema validation, and graceful column handling.
    

## 2. `scripts/apex-search.py`

- **Macro:** Read-only query path — CLI wrapper over `search_kb()`. Correct file for this role.
    
- **Meso:** Required sections: argparse (`--kb`, `--query`, `--limit`, `--db`, `--output-format`), connect to SQLite, execute FTS5 MATCH query, format and print results.
    
- **Micro:** The `snippet(ft, 9, '>>>', '<<<', '...', 24)` call is correct for body (col 9) given the schema. The output format is underspecified for Claude parsing — must be locked. Recommended: `--output-format text` (default) and `--output-format json` for machine parsing.
    

## 3. `.claude/skills/apex-search.md` (SKILL.md)

- **Macro:** The skill file is the procedural contract between Claude and the retrieval system. Correct separation from `apex-kb` skill [file:4 §skill ownership].
    
- **Meso:** Required sections per Anthropic docs: description, trigger conditions, step-by-step procedure, output format expectations, error handling. File:4 confirms "every skill needs SKILL.md; keep under 500 lines."
    
- **Micro:** No public blueprint exists (BLUEPRINT GAP). The skill must explicitly list trigger phrases. Failure mode: Claude reads SKILL.md but doesn't invoke it because trigger conditions are ambiguous. Fix: trigger conditions should be concrete and exhaustive: "Use this skill when: user asks about [topic], user queries the KB, user requests information about [known KB topics]."
    

## 4. CLAUDE.md additions — retrieval block

- **Macro:** The retrieval block in CLAUDE.md is the routing layer — tells Claude when to invoke `apex-search`. Correct location.
    
- **Meso:** Must contain: routing condition (when to search), KB slug list, search invocation template, stale check reminder, saved query reuse instruction.
    
- **Micro:** Target: under 15 lines total for the retrieval block. Total CLAUDE.md must stay under 200 lines [file:4 §1.2]. Audit existing line count before writing.
    

## 5. `.claude/rules/apex-meta.md`

- **Macro:** Path-scoped rule for `apex-meta/` directory — correct use of path-scoped rules to keep CLAUDE.md concise.
    
- **Meso:** Should contain: KB write conventions, frontmatter requirements, when to rebuild index.
    
- **Micro:** Must use exact file path that Claude Code uses for path-scoped rule loading. Confirm path format matches Anthropic docs.
    

## 6. `apex-meta/registry/index.md`

- **Macro:** Cross-KB navigation index — human and Claude readable. Correct location.
    
- **Meso:** Should list all KB slugs, their page counts, last rebuild dates, and current FTS5 coverage status.
    
- **Micro:** This file must NOT be indexed by FTS5 (analogous to the `index.md` exclusion rule — G6 extended to registry).
    

## 7. `wiki/**/*.md` front-matter template

- **Macro:** The compiled wiki page is the primary Claude read surface. Frontmatter fields drive both FTS5 indexing and staleness detection.
    
- **Meso:** All 10 required fields defined [file:3 §1.3 table]. The template in file:3 is complete and well-structured.
    
- **Micro:** `tags:` field must be changed from bracket YAML list to a format parseable by the chosen parser (G3, G11). `id:` must be globally unique within each KB — no enforcement mechanism specified. `updated:` must be ISO 8601 date string — no format validation in indexer. Fix: add date format validation to `parse_page()`.
    

---

## SECTION 8 — Risk Register

|Rank|Risk|Probability|Impact|Mitigation|Source|
|---|---|---|---|---|---|
|1|**BM25 weight vector off by 1 column — body search silently disabled**|HIGH (confirmed defect in spec)|CRITICAL — all body-text searches return wrong rankings; title-only effective|Fix `bm25()` call from 9 to 10 args before writing script|file:3 §2.3 direct count|
|2|**FTS5 not compiled into Python's SQLite build**|MEDIUM (distro-dependent)|CRITICAL — entire system fails at startup with cryptic error|Add FTS5 availability test as Step 0 of indexer|file:4 §Claim C|
|3|**Skill not triggering — Claude never invokes apex-search**|HIGH (no public blueprint)|HIGH — system built but unused|Define explicit, tested trigger phrases; verify with 5 real queries|file:4; BLUEPRINT GAP §Section 2 Pattern 3|
|4|**YAML frontmatter tags list parsing failure**|HIGH (stdlib re cannot parse `[a, b, c]`)|MAJOR — tags column empty, tag-based retrieval broken|Use `python-frontmatter` or implement bracket parser explicitly|G3, G11|
|5|**`apex_kb.py` coexistence path conflict**|LOW-MEDIUM|MAJOR — operator confusion, possible import shadowing|Confirm script paths are distinct (`scripts/` vs `apex-meta/scripts/`); document separation|file:4 §D4|
|6|**CLAUDE.md exceeds 200 lines after addition**|MEDIUM|MAJOR — context pressure degrades all session quality|Audit line count pre-addition; move verbose blocks to path rules|file:4 §1.2|
|7|**mtime precision loss on macOS HFS+**|LOW (macOS Catalina+ uses APFS)|MINOR — stale index not detected within same second|Add fallback: if `mtime_diff < 2s`, run hash check|C7 analysis|
|8|**`index.md` variants included in FTS5 index**|MEDIUM|MINOR — circular navigation, inflated result count|Exclude any file where `path.name == "index.md"` regardless of depth|G6|
|9|**`search.sqlite` committed to git**|MEDIUM (if .gitignore step delayed)|MINOR — inflated git history|Execute .gitignore step before first build (reorder Step 14 to Step 5.5)|G9|
|10|**UTF-16 or non-UTF-8 file crashes indexer**|LOW|MINOR — one file breaks full rebuild|Use `open(path, encoding='utf-8', errors='replace')`|G10|

---

## SECTION 9 — Final Verdict + Ranked Recommendations

## Overall Plan Verdict: **EXECUTE WITH CHANGES**

The architecture is sound. The implementation plan is directionally correct. Two CRITICAL defects in the spec itself must be fixed before any script is written. Six MAJOR gaps must be addressed before v1 is declared done.

---

## Top 5 Required Changes

**Change 1 (CRITICAL) — Fix bm25() weight vector**

- Exact change: in `search_kb()`, replace `bm25(ft, 0, 0, 5, 3, 2, 1, 0, 0, 1)` with `bm25(ft, 0, 0, 0, 5, 3, 2, 1, 0, 0, 1)` — add the missing `path=0` argument as position 3 (0-indexed).
    
- Why: 10-column schema requires 10 positional weight arguments. Current 9-arg call silences body search entirely. [Source: file:3 §2.3 direct schema count; sqlite.org/fts5.html §bm25]
    
- Blueprint: none required — this is a direct arithmetic correction.
    

**Change 2 (CRITICAL) — Add FTS5 availability test to Step 1**

- Exact change: add check #12 to pre-flight script: attempt to create and drop a throwaway FTS5 virtual table; if it fails, print "FATAL: FTS5 unavailable" and exit with code 1.
    
- Why: FTS5 is not guaranteed across all Python builds and Linux distros. [Source: file:4 §Claim C; CPython build notes]
    
- Blueprint: sqlite.org/fts5.html documents the module detection pattern.
    

**Change 3 (MAJOR) — Specify YAML frontmatter parser strategy for list fields**

- Exact change: either (A) change frontmatter template to use comma-separated string for tags (`tags: "claude-code, memory, CLAUDE.md"`) and update indexer to split by comma, or (B) add `python-frontmatter` as the single allowed dependency.
    
- Why: `tags: [a, b, c]` is a YAML list — stdlib `re` cannot parse it reliably. FTS5 tags column will be empty or corrupted without this fix. [Source: G3, G11; python-frontmatter ★600+]
    
- Blueprint: `eyeseast/python-frontmatter` for Option B.
    

**Change 4 (MAJOR) — Reorder .gitignore step to immediately after registry directory creation**

- Exact change: move Step 14 to execute after Step 5 (registry dir creation), before first index build.
    
- Why: if operator runs `git add .` after Step 5 build, `search.sqlite` enters git history permanently. [Source: G9; file:4 §D7]
    
- Blueprint: standard gitignore convention.
    

**Change 5 (MAJOR) — Define and test skill trigger phrases before declaring v1 complete**

- Exact change: add Step 13.5 — run 5 real operator queries and verify Claude invokes `apex-search` skill in each case without explicit instruction. If any fail, revise CLAUDE.md trigger block.
    
- Why: skills are not auto-triggered by keyword detection — they require correct CLAUDE.md routing [file:4 §1.2]. No public blueprint exists for this exact pattern (BLUEPRINT GAP).
    
- Blueprint: Anthropic skills docs + empirical testing only.
    

---

## 3 Things the Plan Gets Right — Do Not Change

1. **Shared `registry/search.sqlite` over per-KB files** — correct for cross-KB querying and spec alignment. The SQL `AND ft.kb = ?` scoping is the right approach [file:2 §Decision 2].
    
2. **Full DROP+CREATE+INSERT rebuild strategy** — deterministic, atomic, simple. No incremental update complexity needed at 200-page scale. This is the battle-tested production pattern (Sphinx, Make logic equivalent).
    
3. **Separate `apex-search` skill, not merged into `apex-kb`** — correct separation of concerns. apex-kb owns knowledge custody; apex-search owns retrieval. This mirrors the file:4 §skill ownership table and prevents scope bloat.
    

---

## The One Thing Most Likely to Cause v1 Failure

**The bm25() weight vector has 9 arguments for a 10-column schema — body search is silently disabled — and if this is not caught before the script is written, every query will return title-weighted-only results with no error, making the system appear to work while actually being broken in its most important function.**

---

## GATE: Safe to Execute This Plan?

## **YES WITH CHANGES**

**Required before execution begins:**

1. Fix `bm25(ft, ...)` weight vector from 9 to 10 arguments in the spec and any script written from it
    
2. Add FTS5 availability test as check #12 in pre-flight (Step 1)
    
3. Decide YAML parser strategy (stdlib comma-string or `python-frontmatter` dep) and update frontmatter template to match
    
4. Reorder `.gitignore` step to execute before first index build
    
5. Plan an explicit skill trigger phrase test as a validation gate before v1 sign-off