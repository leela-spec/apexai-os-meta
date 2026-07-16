I'm researching the "apex-kb" knowledge-base ingestion process. It produces Phase 1 analysis files (in `ingest-analysis/*.analysis.md`) and Phase 2 wiki summary pages (in `wiki/summaries/*.md`) inside `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki`.

Search VERY thoroughly across `C:\GitDev\leela` and especially the `LeelaApp-Index-KB-Wiki` folder and anywhere with "apex" or "apex-kb" in the name/path.

I need to find:

1. The process definition / spec / prompt that defines Phase 1 and Phase 2 (what instructs the agent to create one analysis file per high-ranked source file, and what defines the wiki page structure — Target Questions, Core Summary, Adaptive Ranked Source Set, Macro/Meso/Micro, Key Claims, Routes Here, Uncertainty). Look for markdown spec files, skill files (SKILL.md), agent prompts, or scripts (.py, .js, .ts, .ps1).
2. Any schema / template files that define the frontmatter and section structure of the analysis files and wiki pages.
3. Any scripts that orchestrate the run (the "recent run").
4. Any config listing the "target_query_ids", ranking logic ("Phase 0 navigation", "lean funnel"), or "semantic_contract_version".

For each relevant file, report its full path, its purpose, and quote the key sections (especially anything defining the file-per-source-file structure of Phase 1, and anything defining the wiki page section structure / Macro-Meso-Micro of Phase 2). Report exact file paths. Be thorough — list ALL related process/spec/template/script files you find, even if you're unsure.

I now have a complete picture. Here is my thorough report.

# Apex-KB Ingestion Process — File Inventory & Findings

The "apex-kb" process is a **two-repository system**. The **process definition, spec, schemas, and orchestration scripts live in `C:\GitDev\apexai-os-meta`** (the Apex skill), while `C:\GitDev\leela\...\LeelaApp-Index-KB-Wiki` holds a **repository-local copy of the semantic contract** plus the actual run inputs/outputs. Both are present on disk. Note: the primary process authority (`SKILL.md`, references, Python engine) is in `apexai-os-meta`, not under `leela`, by explicit design (see the handover's Section 3).

---

## 1. Process definition / spec / prompt (Phase 1 & Phase 2)

### Master handover / orchestration spec (the "recent run")

- **`C:\GitDev\leela\APEX_KB_LEAN_FUNNEL_EXECUTION_HANDOVER.md`** — The top-level v2 execution spec ("Apex KB Lean-Funnel Leela Execution Handover"). Defines the entire 7-phase run (Phase 0 capability gate → Phase 1 Q&A/target lock → Phase 2 custody → Phase 3 lean deterministic funnel → Phase 4 semantic delegation → Phase 5 acceptance → Phase 6 postflight → Phase 7 Git). This is the document that supersedes the old "full corpus" approach. Key load-bearing content:
    - The **lean funnel / ranking logic**: "Tiered field-separated ranking (filename/H1/heading/body_strong/body_weak), **no cutoff at all**"; work packs use an "elbow-cut" concentration; held-back sources stay in `held_in_custody`.
    - Names the **10 proposed locked topics** and the seven priority folders.
    - Confirms the engine is invoked cross-repo: `python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB ... phase0`.
    - Section 3 explicitly forbids moving the skill into the Leela repo.

### The skill definition (Apex repo)

- **`C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\SKILL.md`** — The authoritative apex-kb skill. Defines the execution-surface router (terminal_backed vs connector_only vs unsupported), the owned lifecycle, `llm_owns` vs `python_owns` split, output tiers (`source_only`/`analysis_only`/`compiled_minimal`/`compiled_full`/`query_ready`), truthful states, the Step-0 topic interview, and the Phase 2 per-page draft/check/retry loop. Its `description` frontmatter is what defines the adaptive page value contract (Adaptive Ranked Source Set, Macro/Meso/Micro, Key Claims, Routes Here, Uncertainty).

### The core semantic process spec

- **`C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\semantic-value-contract.md`** — THE definition of the Phase 0 funnel, ranking tiers, completion target, truthful states, topic registry v2, the semantic run ledger, Phase 1/Phase 2 traceability, `semantic_contract_version`/`target_query_ids`, and semantic acceptance. Directly defines:
    - The **3-layer funnel**: per-file facts → exhaustive tiered ranking (`filename > h1 > heading > body_strong > body_weak`, no top-N) → concentration into a work pack via elbow cut.
    - The requirement that v2 pages declare `semantic_contract_version`, `semantic_run_id`, `target_query_ids`.

### Repository-local semantic contract (the copy inside the Leela KB)

This is the `semantic-contract/` folder scaffolded into the Leela KB so a browser/connector session can read authority without crossing repos. All under `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\semantic-contract\`:

- **`README.md`** — index; lists which files to read before Phase 1; defines allowed write locations.
- **`semantic-execution-contract.md`** — the compact execution rules (lock target questions first, read raw sources, preserve contradictions, cap at `compiled_unvalidated`, never run Python/claim `query_ready`).
- **`phase1-analysis-template.md`** — see item 2.
- **`phase2-wiki-page-templates.md`** — see item 2.
- **`source-authority-and-contradictions.md`** — evidence-type labeling, contradiction preservation, "never infer from filenames" rule.
- **`browser-chat-git-connector-instructions.md`** — one-topic-at-a-time connector workflow and clean-context evaluation prompt.
- **`provenance.md`** — records that these were copied from `apexai-os-meta` commit `7ab08a57...`, listing the exact source skill files.
- **`C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\HANDOVER_LLM_PHASES.md`** — Leela-local handover summarizing the LLM-owned Phase 1/Phase 2 work and the exact required section names ("Adaptive Ranked Source Set", "Macro / Meso / Micro", "Key Claims", "Routes Here", "Uncertainty / Raw Source Reopen Triggers").

The **source templates** these were copied from (Apex repo, also present):

- `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\assets\repository-semantic-contract\` (README, phase1-analysis-template.md, phase2-wiki-page-templates.md, semantic-execution-contract.md, source-authority-and-contradictions.md, browser-chat-git-connector-instructions.md) — the packaged originals.
- `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\templates\ingest-analysis-template.md` and `wiki-page-templates.md` — the terminal-route Phase 1/Phase 2 shapes.

---

## 2. Schema / template files (frontmatter + section structure)

### Phase 1 analysis file structure (one file per selected source)

- **`C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\semantic-contract\phase1-analysis-template.md`** — Defines the per-source analysis file. Load-bearing opening line: _"Create one complete file under `ingest-analysis/` for each selected source."_ Frontmatter fields include `analysis_id`, `kb_slug`, `source_slug`, `run_profile`, `source_payload_manifest_ref`, `source_ref` (path/type/hash/algorithm), `phase: ingest_phase_1`, `status: operator_review_needed`. Eleven numbered sections: Source Identity, Payload/Source References, Authority & Limitations, Source Summary, Extraction Candidates, Concepts, Entities, Key Claims with Pointers (`claim_id C001...`), Uncertainty Triggers, Proposed Phase 2 Changes, Compile Decision (`operator_review_needed: true/false`). Plus a "Semantic Value v2 Requirements" block (target-query IDs, concept/entity disposition: `promote`/`embed_in_summary`/`defer_blocked`/`reject_no_independent_value`).

### Phase 2 wiki page structure (Macro/Meso/Micro etc.)

- **`C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\semantic-contract\phase2-wiki-page-templates.md`** — Defines summary/concept/entity page frontmatter and the five required value sections. The **Summary page** structure: `# Summary title`, `## Core Summary`, `## What This Adds`, `## Adaptive Ranked Source Set`, `## Macro / Meso / Micro` (with `### Macro`/`### Meso`/`### Micro`), `## Key Claims`, `## Routes Here`, `## Uncertainty / Raw Source Reopen Triggers`. Concept/entity pages add `## Definition`/`## Operating Rules` or `## Identity`/`## Source-Grounded Summary` plus `## Evidence`. Says to populate the Adaptive Ranked Source Set from `manifests/phase0/topic-source-rankings.json`. The "Semantic Value v2 Requirements" block mandates `semantic_contract_version`, `semantic_run_id`, `target_query_ids` frontmatter and a "Target Questions Answered" section.

### JSON schemas (Apex repo — `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\`)

- `topic-registry-v2.schema.json` — topic registry / vocabulary fields (`phrases`/`aliases`/`supporting_terms`/`negative_terms`/`ambiguous_terms`, `target_queries`).
- `topic-source-rankings.schema.json` — the exhaustive tiered ranking output shape.
- `topic-work-pack.schema.json` — the bounded work-pack shape (`held_in_custody`, `zero_signal_custody`, disclosure).
- `analysis-config.schema.json` — the `manifests/analysis-config.json` signal-toggle config (auto/on/off per signal; `reference_graph`, freshness, etc.).
- `semantic-run-ledger.schema.json`, `semantic-acceptance.schema.json`, `query-eval-pack-v2.schema.json`.
- **`C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\kb-contract.md`** (via references/) and templates `topic-work-pack-template.md`, `query-output-template.md`, `kb-schema-template.md`, `source-manifest-template.json`.
- **`C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\kb-schema.md`** — the instantiated KB schema for Leela (`kb_slug: LeelaApp-Index-KB-Wiki`, authority levels, operator-review policy `approve ingest`).

---

## 3. Orchestration scripts (the run)

### Python engine (Apex repo — `C:\GitDev\apexai-os-meta\apex-meta\scripts\`)

- **`apex_kb.py`** — The primary deterministic engine. Provides all subcommands referenced by the handover: `health`, `generate-source-payload-manifest`, `preflight`, `phase0`, `index`, `lint`, `quality`, `query-eval`, `postflight`, `semantic-acceptance-status`. `phase0` produces the source-facts, rankings, work-packs, and corpus-profile. (Also present: `apex_kb.py.bak.20260623T081018Z`.)
- **`apex_kb_retrieval.py`** — Retrieval engine (`health`, `build-index`, `stale`).
- Supporting: `large_corpus_prework.py`, `projectrepos_corpus_intelligence.py` (corpus-intelligence helpers), and tests under `apex-meta\scripts\tests\test_*.py` (handover cites 29 tests, incl. `test_custody_accounts_for_every_scanned_source`, `test_workpack_disclosure_reconciles_with_rankings`).

### PowerShell scripts (Leela KB root)

- **`C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\Materialize-ApexKBCorpus.ps1`** — Copies scoped source files from the repo into `raw/other/<group>/`, verifies SHA-256, and updates `manifests/source-manifest.json`. (Handover Phase 2 says do NOT run this for the lean run — fixed inventory/destructive.) Uses inventory CSV at `...\Creator Onboarding\source-of-truth-audit-v2\01_LOCAL_SOURCE_INVENTORY.csv`.
- **`C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\Create-ApexKBGroupMap.ps1`** — Builds `manifests/source-group-map.json` mapping each `raw/other/...` file to its source group (the eight groups: MVP User Stories & Flows, Nowa, Prototyp Spark, Upgrades, 01_Features, 02_Interconnections, Leela Content, New Leela Data).

---

## 4. Config: target_query_ids, ranking logic, Phase 0 navigation, semantic_contract_version

### The run config (Leela KB — `manifests\`)

- **`C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\manifests\topic-registry.json`** — The locked config listing all **9 topics** with `slug`, `keywords`, `target_page`, `status: complete`, and **`target_queries`** each carrying `query_id` (e.g. `epic-q1`, `skill-tree-q2`, `path-q3`, `cross-q1`, `nowa-q3`), `question`, `priority` (`critical`/`routine`), `answer_requirements`, `expected_page`. This is the source of the `target_query_ids`.
- `manifests\source-group-map.json`, `source-manifest.json`, `source-payload-manifest.json` — custody/manifest config.
- Note: the handover references `manifests/analysis-config.json` (signal toggles) and `manifests/corpus-scope.json`, but **only `topic-registry.json` currently exists** in the Leela `manifests/` folder — the analysis-config/corpus-scope files were not written for this run (defaults used).

### Phase 0 navigation / ranking outputs (Leela KB — `manifests\phase0\`)

- **`topic-source-rankings.json`** — The per-topic ranked candidate sets (`ranked_sources` with `hit_count`, `path`, `sample` line/snippet). This is the current run's flat `hit_count` ranking (the lean tiered `filename/h1/heading/body_strong/body_weak` format described in the handover is the _newer_ engine format; the on-disk file here uses the older `hit_count` shape).
- **`phase0-navigation-report.md`** — Run report: generated `2026-07-13T12:09:20Z`, 264 files scanned, lists artifacts and boundary.
- **`corpus-profile.md`** — Corpus profile: 264 files / 4.58 MB, extension counts, largest files, duplicate-hash groups, `source_group_summary`, and `generic_term_frequency` (nowa 3667, path 3201, chunk 2843...).
- Also present: `heading-map.json`, `markdown-link-map.json`, `frontmatter-map.json`, `term-frequency.json`, `process-flow-graph.json` + `process-flow-graph-summary.md`, `source-priority-candidates.md`.

There is **no `semantic_contract_version` value file**; it is a frontmatter field defined by the contract, to be stamped on v2 pages (see `semantic-value-contract.md` and `phase2-wiki-page-templates.md`). No `work-packs/` subfolder exists yet under `phase0/` (this run predates/omitted the lean work-pack output). No "lean funnel" / `semantic_contract_version` config file is on disk in the Leela KB.

---

## Run outputs & audit (the actual recent run)

- **Phase 1 analyses** (11 files): `C:\GitDev\leela\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\ingest-analysis\*.analysis.md` (e.g. `chunks-and-epics.analysis.md`, `path-feature.analysis.md`, `rhythm-feature.analysis.md`, `stats-feature.analysis.md`, `nowa-handoff-v3.analysis.md`, `wave1-contract-sheets.analysis.md`, etc.).
- **Phase 2 wiki pages** (9 summaries): `...\wiki\summaries\` (creator-user-stories-and-flows, cross-feature-interconnections, epic-and-content-data, nowa-contracts-and-build-guidance, path, rhythm, sequencing-and-play, skill-tree, stats-and-metrics).
- **Run record**: `...\audit\semantic-build-completion-2026-07-13.md` — final state `compiled_unvalidated`, `query_ready: false`, lists topics completed, sources analyzed, contradictions preserved, reopen triggers.
- **Acceptance artifacts**: `...\audit\semantic-acceptance\leela-semantic-value-canary-2026-07-13\*.json` (one per topic) + `...\audit\semantic-value-canary-closure-2026-07-13.md`.
- **Prior failed runs** (older process variants, incl. the abandoned per-source-atlas / corpus-map approach): `...\failedruns\RUN1-full-corpus-kb\` and `...\failedruns\RUN3-manual-browser-full\` each contain their own `ingest-analysis\` and `wiki\summaries\` (including `*-source-atlas.md` pages the lean funnel deliberately removed).

## Key structural facts (load-bearing quotes)

- **One analysis file per source** (Phase 1): _"Create one complete file under `ingest-analysis/` for each selected source. Read the actual raw source first..."_ — `semantic-contract\phase1-analysis-template.md`.
- **Wiki page section structure** (Phase 2 summary): `## Core Summary` / `## What This Adds` / `## Adaptive Ranked Source Set` / `## Macro / Meso / Micro` (`### Macro`/`### Meso`/`### Micro`) / `## Key Claims` / `## Routes Here` / `## Uncertainty / Raw Source Reopen Triggers` — `semantic-contract\phase2-wiki-page-templates.md`.
- **Ranking / funnel logic**: the 3-layer funnel (per-file facts → exhaustive tiered ranking `filename > h1 > heading > body_strong > body_weak`, no top-N → elbow-cut work pack with `held_in_custody`/`zero_signal_custody`) — `apexai-os-meta\...\references\semantic-value-contract.md` §"Phase 0 funnel and the topic work pack".