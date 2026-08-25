# VERDICT

**Winner:** `AgriciDaniel/claude-obsidian` (aka "claude-obsidian" / LLM-Wiki implementation) — a 15-skill Claude Code plugin implementing Karpathy's RAW→WIKI pattern, with ~10–11k GitHub stars, immutable source ingestion, hash-based delta tracking, entity/concept reconciliation, contradiction flagging, and file-locking for safe incremental writes.[[github](https://github.com/AgriciDaniel/claude-obsidian)][2][[x](https://x.com/gippp69/status/2079163156258037777)][4]

**Runner-up:** `basicmachines-co/basic-memory` — 3.4k-star MCP server giving Claude/ChatGPT/Cursor read-write access to a local Markdown knowledge graph, mature (44 releases, 795 commits), but weaker on transcript-specific chunking and deterministic dedup tooling.[[skillsllm](https://skillsllm.com/skill/claude-obsidian)][6][[github](https://github.com/AgriciDaniel/claude-obsidian/blob/main/skills/wiki-ingest/SKILL.md)]

**Confidence: 62/100.** Both finalists pass all hard filters on adoption and format, but neither has a _dedicated, proven_ mechanism for bounding a single 1–3 hour transcript into progressive chunks — this is the one hard filter (HF4) both satisfy only partially, via generic file-reading rather than an explicit chunk/checkpoint protocol.

---

# HARD-GATED CANDIDATES

|Candidate|Battle-tested evidence|Host|PASS/FAIL|Reason|
|---|---|---|---|---|
|AgriciDaniel/claude-obsidian|~10–11k stars, active v1.9.2, multiple third-party writeups/tutorials[2][[x](https://x.com/gippp69/status/2079163156258037777)][8]|Claude Code (plugin/skill), portable to Codex/OpenCode/Gemini via `setup-multi-agent.sh`[[x](https://x.com/gippp69/status/2079163156258037777)]|**PASS**|Meets HF1–HF9; only HF4 (chunking) is partial|
|basicmachines-co/basic-memory|3.4k stars, 44 releases, 9 contributors, 795 commits[6][[github](https://github.com/AgriciDaniel/claude-obsidian/blob/main/skills/wiki-ingest/SKILL.md)]|Claude Desktop/Code, ChatGPT, Cursor (MCP)[[skillsllm](https://skillsllm.com/skill/claude-obsidian)]|**PASS**|Meets HF1–HF3, HF5–HF6, HF9; HF4/HF7/HF8 rely on generic MCP tools, not a packaged transcript-ingest skill|
|scaccogatto/okf-skills (OKF toolkit)|55 stars, trending, June 2026 creation[[github](https://github.com/basicmachines-co/basic-memory)][10]|Claude Code plugin + 20+ agents via skills.sh[[basicmachines](https://www.basicmachines.co/blog/100-github-stars/)]|**FAIL**|HF1: too new/low adoption; built for documenting _codebases_, not ingesting long transcripts — no chunking mechanism shown|
|parkscloud/okf-author, fabricioctelles/okf-open-knowledge-format|No star/usage data found|Claude Code, Codex[12][[whatstrendinginai](https://whatstrendinginai.com/projects/basicmachines-co-basic-memory-mcp-server/)]|**FAIL**|HF1: no adoption evidence found; conceptual/early tooling|
|mehmetcakoglu/claude-obsidian-vault-skill|**1 star, 0 forks**[14]|Claude Code|**FAIL**|HF1: unvalidated hobby project; also only ingests Claude Code's own session JSONL logs, not general transcripts|
|glebis/claude-skills transcript-analyzer|Marketplace-listed[[agricidaniel](https://agricidaniel.com/blog/claude-obsidian-ai-second-brain)]|Claude Code|**FAIL**|HF3: hard-requires a separately billed Cerebras API for its extraction step|
|kepano/obsidian-skills|46.8k stars — very high adoption[16]|Claude Code, Codex, OpenCode|**FAIL (as complete package)**|HF2/HF5: it's a formatting/CLI toolkit (Markdown, Bases, JSON Canvas), not a transcript→KB extraction+reconciliation workflow. Valid only as a **format companion (Category D)**|

---

# FINALIST MATRIX

|Rank|Candidate|Proven (25)|Knowledge (20)|Long-doc (15)|Automation (10)|Host (10)|Ops (5)|Total/100|Main weakness|
|---|---|---|---|---|---|---|---|---|---|
|1|claude-obsidian|22|18|8|9|10|5|**72**|No explicit chunk/checkpoint protocol for one giant transcript|
|2|basic-memory|20|13|6|6|9|4|**58**|Reconciliation/dedup is manual-semantic, not scripted; no transcript-specific skill|
|—|okf-skills|6|12|4|8|8|5|(FAIL, not ranked)|Fails HF1 adoption + not built for transcripts|

---

# FINALIST ARCHITECTURES

### 1. claude-obsidian — 3-hour transcript workflow

```
transcript.txt dropped in .raw/transcripts/
  → wiki-ingest skill (SKILL.md, Claude Code)
      - hash file, check .raw/.manifest.json (skip if unchanged) [DETERMINISTIC]
      - Read source "completely" (relies on Claude's native Read/context, not a packaged chunker) [PARTIAL/MISSING: no explicit bounded-chunk loop]
      - extract entities/concepts → wiki/entities/*.md, wiki/concepts/*.md
      - check wiki/index.md before creating pages (dedup by search) [SEMANTIC, not deterministic]
      - wiki-lock.sh acquire/release per file (flock-based) [DETERMINISTIC concurrency safety]
  → wiki/sources/<transcript>.md (provenance: .raw path, date, frontmatter)
  → cross-reference pass, contradiction callouts if conflicting with existing pages
  → wiki/log.md appended (append-only audit trail = resume anchor)
  → wiki/hot.md updated (session-start cache)
  → Obsidian graph view = index/visualizer
```

- **Bounded reading:** MISSING as a dedicated primitive — depends on host context window and "read completely" instruction, not a chunk-loop.
- **Concept creation:** explicit steps 4–5 of Single Source Ingest (entity/concept pages).[4]
- **Existing-concept lookup:** "check the index and search before creating".[4]
- **Duplicate prevention:** hash-based manifest for whole sources; page-level dedup is semantic (index/search), not hashed.
- **Provenance:** `.raw/` immutable originals + `source_url`/`fetched` frontmatter + `wiki/log.md` entries.[4]
- **Interrupt/resume:** batch ingest explicitly "checks in with user after every 10 sources," and log.md/manifest give a resumable audit trail. For a single giant transcript specifically, no mid-source resume — MISSING.[4]
- **Second transcript updates same KB:** yes — Batch/Single Ingest always checks `wiki/index.md` first, updates existing entity/concept pages, and flags contradictions.[4]

### 2. basic-memory — same scenario

```
transcript.txt
  → user/agent manually chunks (no packaged chunker) [MISSING]
  → write_note (MCP tool) per chunk/summary
  → search_notes / build_context to find related existing notes [semantic, agent-driven]
  → notes stored as Markdown files with observations + relations (basic-memory's schema)
  → sync engine indexes files into local knowledge graph
  → Obsidian can open the same folder
```

- **Bounded reading:** MISSING — no dedicated chunking skill; up to the calling agent.
- **Concept creation / existing-concept lookup:** via `search_notes`/`build_context`, semantic only.
- **Duplicate prevention:** relies on agent judgment; no hash/manifest layer found in documentation reviewed.
- **Provenance:** notes carry source references if the agent writes them, not enforced.
- **Resume:** MCP server + file sync is inherently resumable (files persist), but no explicit "queue/checkpoint" primitive like claude-obsidian's log/manifest.

---

# SKILL PACKAGE CONTENTS

**claude-obsidian (15 skills, v1.9.2):** wiki (scaffold), wiki-ingest (extraction+filing), wiki-query, wiki-retrieve (hybrid BM25+rerank), wiki-lint, wiki-mode (LYT/PARA/Zettelkasten routing), wiki-cli, wiki-fold, save, autoresearch, canvas, think. Deterministic scripts: `scripts/detect-transport.sh`, `scripts/wiki-mode.py`, `scripts/wiki-lock.sh` (flock-based per-file locking), `scripts/allocate-address.sh` (atomic counter with `--rebuild`/`--peek`), `.raw/.manifest.json` (SHA/MD5 delta tracking + address_map), `claude-obsidian.py init` with `--approved-plan-sha256` gating. Semantic work (entity/concept extraction, contradiction detection, editorial judgment) runs entirely inside Claude's own context — no external API required.[[x](https://x.com/gippp69/status/2079163156258037777)][4][8]

**basic-memory:** 17 MCP tools (`write_note`, `search_notes`, `build_context`, etc.), sync engine for file↔index consistency, SQLite index alongside canonical Markdown, Obsidian compatibility. Deterministic tooling is thinner — mostly indexing/sync, not manifest/hash/lock primitives.[[skillsllm](https://skillsllm.com/skill/claude-obsidian)][[skillsllm](https://skillsllm.com/skill/okf-skills)]

---

# INSTALLABILITY

|Host|claude-obsidian|basic-memory|
|---|---|---|
|ChatGPT|UNSUPPORTED (no filesystem/plugin path documented)|VERIFIED via MCP (`basic-memory mcp` works with "anything that speaks MCP," including ChatGPT per project docs)[[skillsllm](https://skillsllm.com/skill/claude-obsidian)]|
|Codex CLI|VERIFIED — `bash bin/setup-multi-agent.sh --host codex --apply`[[x](https://x.com/gippp69/status/2079163156258037777)]|VERIFIED — MCP-compatible per docs|
|Claude Code|VERIFIED — `claude plugin marketplace add AgriciDaniel/claude-obsidian` + `claude plugin install claude-obsidian@agricidaniel-claude-obsidian`, or `git clone` + `bin/setup-vault.sh`[[github](https://github.com/AgriciDaniel/claude-obsidian)][[x](https://x.com/gippp69/status/2079163156258037777)]|VERIFIED — `claude mcp add basic-memory -- uvx basic-memory mcp`, plus `claude plugin install basic-memory@basicmachines-co`[[skillsllm](https://skillsllm.com/skill/claude-obsidian)]|
|Google Antigravity|UNVERIFIED — no documented install path found in either project|UNVERIFIED|

---

# KNOWLEDGE OUTPUT

claude-obsidian's on-disk layout matches the requested target structure closely:

```
wiki/
  index.md          # master index
  hot.md            # session-start cache (~500 words)
  log.md            # append-only ingest audit trail
  overview.md
  sources/<name>.md # per-source page (provenance, frontmatter)
  entities/<name>.md
  concepts/<name>.md
.raw/
  <original files>  # immutable
  .manifest.json    # {hash, ingested_at, pages_created, pages_updated, address_map}
.vault-meta/
  transport.json, mode.json, address-counter.txt
```

This is a near-exact match to the requested `knowledge/index.*`, `sources/*`, `concepts/*`, `entities/*`, `metadata/state/*` shape.[4]

basic-memory's output is plain Markdown notes with YAML frontmatter and `- relation` / `- observation` semantic markup, indexed in a local SQLite file for search — human- and machine-readable, but without the entities/concepts/sources folder taxonomy.[[skillsllm](https://skillsllm.com/skill/claude-obsidian)]

---

# FAILURE MODES

- **claude-obsidian:** No packaged chunk-by-chunk reader for a single very long transcript — "read completely, do not skim" is a semantic instruction, not a bounded loop; risks context overflow on a genuinely 3-hour raw transcript unless the host truncates/paginates automatically. Address allocation is explicitly "single-writer only" in this phase — concurrent multi-agent ingestion of the _same_ source is not supported. No ChatGPT path.
- **basic-memory:** No dedicated transcript-ingestion skill or hash-based delta/duplicate-avoidance layer; concept reconciliation depends entirely on the calling agent remembering to search first — a weaker HF7/HF8 story than claude-obsidian's manifest+lock system.

---

# RECOMMENDED IMPLEMENTATION

- **Install:** `claude plugin marketplace add AgriciDaniel/claude-obsidian` → `claude plugin install claude-obsidian@agricidaniel-claude-obsidian`, or clone + `bin/setup-vault.sh`.[[x](https://x.com/gippp69/status/2079163156258037777)]
- **Configure:** run `/wiki` once to scaffold; optionally choose a methodology mode (Generic/PARA/Zettelkasten) via `wiki-mode.py`.
- **Use:** drop the transcript file into `.raw/`, run `/claude-obsidian:wiki-ingest` (or say "ingest this"); repeat for each new transcript — existing pages are reused/updated automatically via index lookup and contradiction flags.[4]
- **Unavoidable adaptation:** for transcripts exceeding a single comfortable context read, you must manually pre-split the transcript into time-bounded segments (e.g., 20–30 min blocks) and run Batch Ingest per segment, since no native chunker exists for a single oversized source — this is the one piece of custom glue needed.

---

# SOURCES

Adoption/star and mechanism evidence for claude-obsidian; basic-memory evidence; failed candidates evidence.[[github](https://github.com/AgriciDaniel/claude-obsidian)][2][[x](https://x.com/gippp69/status/2079163156258037777)][4][[skillsllm](https://skillsllm.com/skill/claude-obsidian)][6][[github](https://github.com/AgriciDaniel/claude-obsidian/blob/main/skills/wiki-ingest/SKILL.md)][8][[github](https://github.com/basicmachines-co/basic-memory)][10][[basicmachines](https://www.basicmachines.co/blog/100-github-stars/)][14][[agricidaniel](https://agricidaniel.com/blog/claude-obsidian-ai-second-brain)][16][[skillsllm](https://skillsllm.com/skill/okf-skills)][18][[trendshift](https://trendshift.io/repositories/156758)][20]

**Final answer to your question:** the most proven existing installable skill package today is **claude-obsidian** (`AgriciDaniel/claude-obsidian`) for Claude Code — it is the only candidate with real adoption (~10k+ stars), a documented transcript-to-wiki workflow, deterministic hash/lock/address tooling, and a local Git-friendly Markdown KB — with the caveat that true bounded/chunked reading of a single very long transcript is not yet a built-in, proven primitive and requires manual pre-segmentation.