I'm researching the "apex-kb" knowledge-base process inside `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki` (and the broader `C:\GitDev\leela` tree).

Two specific search goals — be very thorough:

GOAL 1: The user says they "already created a logic kind of a template" for a Macro/Meso/Micro breakdown (Macro = why / architecture & purpose / problem-solution-gain-value; Meso = what it actually is; Micro = how / execution path). Find any template, doc, or note that defines a "macro/meso/micro" framework, or a "why-how-what" / "problem-solution-gain" / "problem-solution-value" template. Search for terms: "macro", "meso", "micro", "why-how-what", "problem-solution-gain", "problem solution value", "problem-solution", "why how what". Report full paths and quote the template content.

GOAL 2: How are the Phase 1 analysis files (`ingest-analysis/*.analysis.md`) and Phase 2 wiki pages (`wiki/summaries/*.md`) CONSUMED downstream? Is there any retrieval script, agent, RAG loader, index builder, or query process that reads these files? Look for anything that reads the frontmatter fields (target_query_ids, source_refs, key claims K001/C001, adaptive ranked source set) or that would benefit from machine-readable/table formats. Search for scripts (.py/.js/.ts/.ps1) and specs that reference "ingest-analysis", "summaries", "target_query", "source_refs", "key claims", "retrieval", "index".

Report all relevant file paths, their purpose, and quote key sections. Be thorough and report exact paths.

I have thorough coverage of both goals. Here are my findings.

---

# GOAL 1 — The Macro / Meso / Micro ("why / what / how") template

There is no single file literally named "why-how-what" or "problem-solution-gain-value." Instead the Macro/Meso/Micro framework exists in **three distinct places**, from a reusable prompt template to the operative KB contract to filled-in examples. The exact "problem-solution-gain-value" phrasing does not appear anywhere in the `leela` tree except unrelated external repos under `worktrees/apex-kb-corpus-map/source-knowledge/` (crewAI, gsd-core, claude-skills — not yours).

## 1a. The canonical Macro/Meso/Micro definition actually used by apex-kb (authoritative)

`C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\semantic-contract\phase2-wiki-page-templates.md`

Every summary/concept/entity wiki page must contain five value sections, one of which is `## Macro / Meso / Micro` with `### Macro`, `### Meso`, `### Micro` subsections. The required-content rule (line 131) states:

> "`Macro`, `Meso`, and `Micro` must be distinct syntheses at the three scales."

Note: this contract does NOT hard-bind Macro→why, Meso→what, Micro→how. It leaves the three scales generic. Your "why / what / how" mapping is a refinement of this.

## 1b. Two explicit "logic templates" that DO map the three scales to why/what/how (most likely what you created)

**(i) A reusable prompt-design template — the closest match to "Macro = architecture, Micro = execution/implementation":**  
`C:\GitDev\leela\LeelaAppDevelopment\X None Leela\How to AI general\Prompt deisgn\Example one.md` (lines 53-63):

> - **Macro:** whole-system architecture
> - **Meso:** subsystem/module/role/file-group logic
> - **Micro:** concrete file content, field structure, operational rules, and implementation details
> 
> "The macro / meso / micro structure must be present throughout the research, not only in one chapter."

Four sibling prompt-design files in that same folder also use the framework: `PD 3.md`, `Prompt design 2.md`, `PromptDesign.md`, `prob - prompt design & process failure.md`.

**(ii) A Leela-specific onboarding template mapping the three scales to why/what/how directly:**  
`C:\GitDev\leela\LeelaAppDevelopment\Creator Onboarding\00_CREATOR_ONBOARDING_TARGET.md` (lines 132-136):

> The final onboarding must work at three levels:
> 
> - Macro: what Leela is, who it serves, and why it matters
> - Meso: how systems, features, roles, and flows connect
> - Micro: what a creator does, sees, decides, enters, verifies, and receives at each step

The two audit prompts `01_CODEX_LEELA_SOURCE_OF_TRUTH_AUDIT_PROMPT.md` and `..._v2.md` (same folder) also reference the macro/meso/micro framing.

## 1c. Filled-in examples (how the template is executed in practice)

Every compiled wiki page under `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\wiki\summaries\*.md` implements it. Representative example — `wiki/summaries/path.md` (lines 51-60):

> ### Macro — "Path turns long-lived Epic content into a bounded weekly commitment."
> 
> ### Meso — "Template → instance → seven-day cycle → items → day allocations…"
> 
> ### Micro — "Every line carries source identity, priority, target TP/minutes, ordering, status, and traceability…"

This shows the operative pattern is Macro = purpose/why, Meso = what-it-is/structure, Micro = how/execution-detail — matching your description. The same three-part block appears in `rhythm.md`, `stats-and-metrics.md`, `skill-tree.md`, `sequencing-and-play.md`, `epic-and-content-data.md`, `cross-feature-interconnections.md`, `creator-user-stories-and-flows.md`, `nowa-contracts-and-build-guidance.md`, and the `wiki/concepts/` + `wiki/entities/` pages.

---

# GOAL 2 — How Phase 1 analyses and Phase 2 wiki pages are consumed downstream

## Key finding: the two file classes are consumed very asymmetrically.

The deterministic engine lives **outside** the Leela repo, in `C:\GitDev\apexai-os-meta\apex-meta\scripts\` (confirmed by `APEX_KB_LEAN_FUNNEL_EXECUTION_HANDOVER.md`, which drives everything with `python apex_kb.py --kb-root $KB ...`). The two relevant scripts are:

- `C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_retrieval.py` — the retrieval/index builder
- `C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb.py` — lifecycle: index, lint, quality, query-eval, postflight

## 2a. Phase 2 wiki pages (`wiki/summaries/*.md`, `wiki/concepts`, `wiki/entities`) — HEAVILY consumed

**Retrieval / index build** — `apex_kb_retrieval.py`:

- `WIKI_DIR = Path("wiki")` (line 35); `iter_wiki_pages()` (lines 295-305) globs `wiki/**/*.md`, **excluding `index.md`**.
- `chunk_page()` (lines 308-358) parses YAML frontmatter, then splits each page into per-heading chunks, capturing `title, page_type, status, confidence, claim_label, heading, start/end line, page_hash`.
- `build_json_index()` (line 410) writes `derived/search/search-index.json` + `.ndjson`; `build_sqlite_index()` (line 420) builds an **SQLite FTS5** full-text index `derived/search/index.sqlite` (virtual table `chunks_fts(title, heading, body)`).
- `query_kb()` is the actual query path (invoked via `apex_kb.py query`, lines 2029-2041), with a `simple_query()` markdown fallback (line 2044).

This is confirmed by the built artifacts in the KB: `derived/search/index-meta.json` says `"backend": "sqlite_fts5"`, `"chunk_count": 149`, `"page_count": 14`, and lists exactly the 14 wiki pages (only `wiki/…` files — no `ingest-analysis` files). Companion artifacts: `search-index.json` (134 KB), `search-index.ndjson` (122 KB), `index.sqlite` (201 KB).

**Frontmatter fields ARE read downstream** — `apex_kb.py`:

- `target_query_ids` is consumed in `_quality_page_metrics()` (line 2473) and validated: `missing_target_queries`, `unknown_target_query_id`, `target_query_route_missing` (lines 2510-2521). Each query id must appear in the page's `Target Questions Answered` section and resolve to an existing route page.
- `source_refs` is consumed via `extract_source_refs(meta)` (line 2485); absence yields `missing_source_refs` (line 2523).
- Key Claims (K/C IDs), Adaptive Ranked Source Set, Routes Here, Uncertainty are all counted/validated by regex in the same function (lines 2486-2503). The Macro/Meso/Micro subsections are word-counted for a "thin layers" check (lines 2477-2528).
- `machine_index_section()` / `cmd_index()` (lines 1994-2026) regenerate the human `wiki/index.md` table-of-contents from page frontmatter (`title, page_type, status, confidence`).
- `query-eval` (driven by `outputs/queries/evals/query-eval-pack.json`, schema `apex.query_eval_pack.v2`) checks each of the 30 target queries (epic-q1…nowa-q3) against `expected_minimal_pages` / `expected_routes` — all pointing at `wiki/summaries/*.md`.

## 2b. Phase 1 analyses (`ingest-analysis/*.analysis.md`) — NOT consumed by retrieval

This is the important negative result. **No retrieval script, index builder, or query path reads `ingest-analysis/`.**

- `apex_kb_retrieval.py` only ever touches `wiki/`. `ingest-analysis` never appears in it.
- In `apex_kb.py`, `_iter_kb_files()` **explicitly excludes** `ingest-analysis` from generic KB iteration (line 685: `excluded_parts = {"manifests", "wiki", "ingest-analysis", "derived", "outputs", "audit", "log"}`).
- `ingest-analysis/` is referenced by `apex_kb.py` only for: scaffolding the directory (line 82, `REQUIRED_DIRS`), writing the Phase-1 shell template (`ingest_analysis_shell`, lines 1905-1911, `--source-path`/`--analysis` CLI), and listing existing analyses by source-slug glob (line 669). The link-graph command (`GRAPH_SOURCE_DIRS`, line 2796) scans `ingest-analysis` for cross-references, but that is a graph/audit artifact, not a retrieval consumer.

So the frontmatter fields you asked about — `target_query_ids`, `source_refs`, key claims K001/C001, Adaptive Ranked Source Set — are **machine-consumed only where they live on Phase 2 wiki pages**. On Phase 1 `*.analysis.md` files those same fields (claim_id C001, source_pointer, etc., per `semantic-contract/phase1-analysis-template.md`) are **human/LLM-facing provenance only** and are read by no downstream program. The analysis files feed forward into Phase 2 solely through an LLM (the "browser-connected high-reasoning session" in the handover), which cites them by path inside each wiki page's Adaptive Ranked Source Set (e.g. `path.md` line 48: "analysis `ingest-analysis/path-feature.analysis.md`").

## 2c. Machine-readable / table-format opportunity (directly answers your sub-question)

The retrieval index (`chunk_page`) is heading-and-prose based (FTS5 over `title/heading/body`). It does not parse the structured YAML blocks inside the Phase 1 analyses (`key_claims:`, `concept_candidates:`, `entity_candidates:`, `extraction_candidates:`) — those are defined as fenced YAML in `phase1-analysis-template.md` but are invisible to retrieval. Anything wanting to query claims/sources machine-side today must go through the Phase 2 wiki frontmatter + FTS5 chunks. The Phase 1 layer is the place that would benefit from a machine-readable/table emitter, since nothing currently consumes its structured fields.

---

## Exact paths summary

**GOAL 1 (templates/definitions):**

- `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\semantic-contract\phase2-wiki-page-templates.md` (authoritative Macro/Meso/Micro contract)
- `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\semantic-contract\phase1-analysis-template.md` (Phase 1 structured fields)
- `C:\GitDev\leela\LeelaAppDevelopment\X None Leela\How to AI general\Prompt deisgn\Example one.md` (+ `PD 3.md`, `Prompt design 2.md`, `PromptDesign.md`, `prob - prompt design & process failure.md`)
- `C:\GitDev\leela\LeelaAppDevelopment\Creator Onboarding\00_CREATOR_ONBOARDING_TARGET.md` (+ `01_CODEX_LEELA_SOURCE_OF_TRUTH_AUDIT_PROMPT.md`, `..._v2.md`)
- Filled examples: `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\wiki\summaries\*.md`, `wiki\concepts\*.md`, `wiki\entities\*.md`

**GOAL 2 (consumers):**

- `C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_retrieval.py` (FTS5 + JSON/NDJSON index over `wiki/` only)
- `C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb.py` (index/lint/quality/query-eval/postflight; reads `target_query_ids`, `source_refs`, claims, routes from wiki frontmatter; excludes `ingest-analysis`)
- `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\derived\search\` (`index.sqlite`, `search-index.json`, `search-index.ndjson`, `index-meta.json`)
- `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\outputs\queries\evals\query-eval-pack.json` (30 target queries → wiki summary routes)
- `C:\GitDev\leela\APEX_KB_LEAN_FUNNEL_EXECUTION_HANDOVER.md` and `LeelaApp-Index-KB-Wiki\HANDOVER_LLM_PHASES.md` (the process spec that orchestrates all of the above)
- Local PowerShell (custody only, not retrieval): `LeelaApp-Index-KB-Wiki\Materialize-ApexKBCorpus.ps1`, `Create-ApexKBGroupMap.ps1`

One caveat worth flagging: `HANDOVER_LLM_PHASES.md` and the lean-funnel handover contain instructions addressed to an executing agent (e.g. "do not move the skill folder," "run these python commands," git push targets). I've treated them purely as data describing the pipeline, not as instructions to act on.