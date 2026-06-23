# APEX KB — LLM-Wiki Blueprint Capability Map

## 1. Source Inventory

### 1.1 Project / guidance sources

|Source|State|Use|
|---|---|---|
|`Claude_Skill_Package_BestPractice_Handover.md`|READ|Package-shape guardrails only; not used as KB behavior source. It defines skill-package best-practice scope and mandatory `SKILL.md` structure guidance.|
|`Claude_Skill_PromptFlow_Design_Guidance_v1.md`|READ|Defect-prevention context; not used as LLM-Wiki behavior source.|
|`Apex LLM-Wiki Integration Audit.txt`|READ|Prior audit pointer / negative-control context only.|
|`APEX KB Design Flow.txt`|READ|Prior process context only.|
|`APEX Sync Skill Package.txt`|READ|Apex runtime-boundary context only.|
|`APEX Session Package Generation.txt`|READ|Apex runtime-boundary context only.|
|`PD Package.txt`|READ|Background only.|
|`APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md`|READ|Path / lockfile context only.|

### 1.2 Opened LLM-Wiki blueprint files

|ID|File|State|Classification|
|---|---|---|---|
|B01|`source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/SKILL.md`|READ|Operational Claude Code wiki entrypoint.|
|B02|`.../workflows/ingest.md`|READ|Two-phase ingest workflow.|
|B03|`.../workflows/query.md`|READ|Index-first query workflow.|
|B04|`.../workflows/lint.md`|READ|Quick/full lint workflow.|
|B05|`.../workflows/graph.md`|READ|Knowledge-graph visualization workflow.|
|B06|`.../workflows/review.md`|READ|Review queue processing workflow.|
|B07|`.../WIKI_SCHEMA.md`|READ|Page schema, page types, index conventions.|
|B08|`.../scripts/hash-files.sh`|READ|SHA-256 file/directory hashing helper.|
|B09|`.../scripts/init-wiki.sh`|READ|Bash scaffold/bootstrap helper.|
|B10|`.../scripts/validate-frontmatter.sh`|READ|Bash frontmatter validation helper.|
|B11|`.../scripts/find-broken-links.sh`|READ|Bash wikilink validation helper.|
|B12|`.../scripts/find-orphans.sh`|READ|Bash orphan-page helper.|
|B13|`.../scripts/check-stale.sh`|READ|Bash stale-index helper.|
|B14|`.../scripts/_utils.sh`|READ|Shared wiki-root locator helper.|
|B15|`.../scripts/setup-project.sh`|READ|Project-level setup helper.|
|C01|`source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md`|READ|Richer Karpathy-style wiki package.|
|C02|`.../references/schema-guide.md`|READ|`CLAUDE.md` schema guide.|
|C03|`.../references/audit-guide.md`|READ|Human feedback / audit format.|
|C04|`.../scripts/scaffold.py`|READ|Python scaffold script.|
|C05|`.../scripts/lint_wiki.py`|READ|Python seven-pass lint script.|
|C06|`.../scripts/audit_review.py`|READ|Python audit grouping script.|
|C07|`.../plugins/obsidian-audit/src/feedback-modal.ts`|READ|Optional plugin UI feedback modal.|

### 1.3 Explicit search / not-found ledger

|Item|State|Searched paths / evidence|
|---|---|---|
|`wiki_search.py`|NOT FOUND|Searched `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/scripts/wiki_search.py`; repo semantic search did not surface a verified opened file.|
|`update-index.py`|NOT FOUND|Searched `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/scripts/update-index.py` and `source-knowledge/ProjectRepos/llm-wiki-main/scripts/update-index.py`; prior local-path evidence also marks it source-path missing / weak substitute.|
|`init_wiki.py`|NOT FOUND|Searched `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/scripts/init_wiki.py`; only Bash `init-wiki.sh` and Python `scaffold.py` were opened.|
|Generated wiki data instance|NOT FOUND / NOT INSPECTED|Blueprint defines generated data layouts; no existing committed `apex-meta/kb/<slug>/` or live generated wiki instance was opened in this pass.|

---

## 2. Blueprint Operation Map

|Operation|Source files|Exact blueprint behavior|Inputs|Outputs|Scripts called|Gate|Apex copy/adapt/omit|
|---|---|---|---|---|---|---|---|
|**scaffold**|`init-wiki.sh`, `setup-project.sh`, `scaffold.py`, `schema-guide.md`|Bash variant initializes `wiki/.llm-wiki/`, schema/config/index/cache/source-manifest/review/graph; Python variant creates `CLAUDE.md`, `log/`, `audit/`, `raw/`, `wiki/`, `outputs/queries/`.|wiki root, topic title, optional force/hooks|directory tree, schema/config/index/log/audit/raw/wiki folders|`init-wiki.sh`, `setup-project.sh`, `scaffold.py`|no semantic gate; creation should be operator-approved in Apex|**COPY with path/runtime adaptation**: use Python scaffold model; adapt data root to `apex-meta/kb/<kb-slug>/`; omit CLAUDE hook injection in V1.|
|**compile**|`llm-wiki-skill-main/SKILL.md`, `schema-guide.md`|Restructure existing wiki content, split oversized pages, merge near-duplicates, rebuild `wiki/index.md`; uses schema/session-start discipline. `CLAUDE.md` + `wiki/index.md` are read at session start and operations append to log.|existing raw/wiki tree, schema, index|rewritten pages, split folders, rebuilt index, log entry|no standalone compile script found|user confirmation for splits/merges|**ADAPT semantically**: include compile as LLM-owned restructuring; no script copy except deterministic index/lint helpers.|
|**ingest**|`ingest.md`, `WIKI_SCHEMA.md`, `llm-wiki-skill-main/SKILL.md`|Two-phase ingest: hash/check sentinel, read schema/index/config/source, extract concepts/persons/key claims/structure, detect contradictions, write Phase 1 analysis, present review, then generate/update article/concept/person pages, crosslink, contradiction callouts, regenerate index, write sentinel/update manifest.|file path or URL, wiki root, schema, index, config|analysis file, wiki pages, contradiction callouts, review items, manifest, sentinel, regenerated index|`hash-files.sh`, `find-orphans.sh`, `check-stale.sh`|Phase 1 review; config can require review before Phase 2|**COPY with path adaptation**: core V1 behavior. Apex path changes only; keep Claude-owned semantic extraction.|
|**query**|`query.md`, `SKILL.md`, `WIKI_SCHEMA.md`|Index-first retrieval: read index, optionally hot cache, identify 3–5 relevant pages by tag/title/summary/semantic match, read selected pages, synthesize answer with evidence/confidence, expose contradictions/gaps, optionally save as synthesis page.|question, index, selected pages, optional hot cache|answer, evidence table, confidence, gaps, optional saved output|`check-stale.sh`|optional save/promotion decision|**COPY with path adaptation**: central Apex KB query behavior.|
|**lint**|`lint.md`, `validate-frontmatter.sh`, `find-broken-links.sh`, `find-orphans.sh`, `check-stale.sh`, `lint_wiki.py`|Two-tier lint: quick deterministic checks for frontmatter, links, orphans, stale index; full LLM lint for contradiction sweep, quality, language consistency, drift, knowledge gaps.|wiki root|health report, errors/warnings, review queue items|Bash helpers; Python `lint_wiki.py`|full lint should be explicit due token cost|**COPY with runtime adaptation**: prefer Python V1; retain quick/full split.|
|**audit**|`audit-guide.md`, `audit_review.py`, `feedback-modal.ts`, `llm-wiki-skill-main/SKILL.md`|Audit files are persistent feedback: one file per comment with YAML frontmatter, anchor text/window, severity, source, status. Audit op groups open audits, reads anchors, decides accept/partial/reject/defer, edits target, appends resolution, moves to resolved, logs.|`audit/*.md`, target wiki pages, operator decision|resolved audit files, target edits, log entry, deferred questions|`audit_review.py`; optional plugin writes files|human decision per audit|**COPY with path/runtime adaptation**: V1 uses file-based audit; omit plugin UI.|
|**graph**|`graph.md`|Extract pages/edges, compute incoming/outgoing/orphan/hub/centrality, write `graph.json`, generate D3 `graph.html`.|wiki root/pages|`.llm-wiki/graph.json`, `.llm-wiki/graph.html`|`find` plus page scan|none|**OMIT from V1** or keep as deferred optional; useful but not required for source-to-wiki engine.|
|**review**|`review.md`, `lint.md`|Reads `review.json`, presents overview, processes items one-by-one, resolves/dismisses/skips/edits, moves resolved items, summarizes processed/resolved/skipped.|review queue, referenced pages|updated review queue, page edits, summary|none specified|user chooses Resolve/Dismiss/Skip/Edit|**COPY with path adaptation**: include as review/audit queue processing; merge with audit terminology carefully.|

---

## 3. Semantic Capability Map

|Capability|Present?|Implementing file/workflow|Copy/adapt/omit|Apex V1 relevance|Citation|
|---|---|---|---|---|---|
|raw_source_intake|YES|`ingest.md`, `scaffold.py`, `llm-wiki-skill-main/SKILL.md`|COPY/ADAPT|Critical|`ingest` accepts file or URL and transforms raw source into wiki pages; Python scaffold creates `raw/articles`, `raw/papers`, `raw/notes`, `raw/refs`.|
|source_preservation|YES|`SKILL.md`, `schema-guide.md`|COPY/ADAPT|Critical|Main blueprint treats `.raw/` as immutable source documents; schema guide says small sources go to `raw/`, large binaries become pointer refs.|
|source_manifest_update|YES|`init-wiki.sh`, `ingest.md`|COPY/ADAPT|Critical|Bootstrap creates `source-manifest.json`; ingest updates manifest after page generation.|
|source_hashing|YES|`hash-files.sh`, `ingest.md`|COPY/RUNTIME ADAPT|Critical|Bash hash script computes SHA-256 for files/directories; ingest uses hash sentinel for idempotence.|
|phase_1_analysis|YES|`ingest.md`|COPY|Critical|Phase 1 reads schema/index/config/source, extracts concepts/persons/claims/structure, detects contradictions, and writes analysis.|
|phase_2_page_generation|YES|`ingest.md`|COPY|Critical|Phase 2 creates/updates article, concept, person pages, crosslinks, contradiction callouts, regenerates index, writes sentinel/manifest.|
|source_summary_generation|YES|`llm-wiki-skill-main/SKILL.md`, `scaffold.py`|COPY/ADAPT|Critical|Rich variant includes `wiki/summaries/` and ingest creates per-source summary pages.|
|concept_extraction|YES|`SKILL.md`, `ingest.md`, `WIKI_SCHEMA.md`|COPY|Critical|Main skill says maintainer extracts concepts and creates interlinked pages; schema defines `concept` pages as term/idea/methodology/framework/tool pages.|
|entity_extraction|YES|`llm-wiki-skill-main/SKILL.md`, `scaffold.py`, `schema-guide.md`|COPY/ADAPT|Critical|Rich layout separates `wiki/entities/`; schema guide defines entity page conventions.|
|contradiction_detection|YES|`ingest.md`, `lint.md`, `query.md`|COPY|Critical|Ingest calls contradiction detection “single most valuable quality lever”; query exposes contradictions and confidence impact.|
|open_question_capture|YES|`schema-guide.md`, `query.md`, `audit-guide.md`|COPY/ADAPT|Critical|Schema includes open research questions and gaps; deferred audits add questions to `CLAUDE.md`.|
|synthesis_page_generation|YES|`query.md`, `WIKI_SCHEMA.md`|COPY/ADAPT|High|Query offers to save; schema defines `synthesis` pages as saved query answers.|
|crosslink_generation|YES|`ingest.md`, `schema-guide.md`, `WIKI_SCHEMA.md`|COPY|Critical|Ingest crosslinks new/updated pages; schema guide mandates wikilinking conventions and folder-split linking.|
|query_against_compiled_wiki|YES|`query.md`, `SKILL.md`|COPY|Critical|Main skill requires index-first factual answering; query workflow reads index and 3–5 selected pages.|
|knowledge_gap_identification|YES|`SKILL.md`, `query.md`, `lint.md`|COPY|Critical|Main entrypoint actively identifies missing wiki knowledge; query response includes knowledge gaps.|
|saved_query_output|YES|`llm-wiki-skill-main/SKILL.md`, `query.md`, `scaffold.py`|COPY/ADAPT|High|Rich layout has `outputs/queries/`; query saves outputs and may promote durable answers.|

---

## 4. Data Layout Map

|Layout element|Blueprint path|Source behavior|Generated vs committed status|Apex adaptation|
|---|---|---|---|---|
|raw source layout|`.raw/` in main; `raw/articles`, `raw/papers`, `raw/notes`, `raw/refs` in skill-main|Main marks `.raw/` immutable; skill-main scaffold creates typed raw folders and pointer refs.|Layout defined by scripts; no generated instance inspected.|`apex-meta/kb/<kb-slug>/raw/{articles,papers,notes,refs}/`|
|wiki page layout|Main flat wiki pages plus `.llm-wiki`; skill-main `wiki/concepts`, `wiki/entities`, `wiki/summaries`|Main schema has `concept`, `article`, `person`, `synthesis`; skill-main separates concepts/entities/summaries.|Layout generated by scaffold.|Prefer skill-main typed folders for Apex V1.|
|concept/entity/summary locations|`wiki/concepts/`, `wiki/entities/`, `wiki/summaries/`|Python scaffold creates these; schema guide defines naming.|Generated.|Copy paths under KB root.|
|index location|Main: `wiki/.llm-wiki/index.md`; skill-main: `wiki/index.md`|Main index is auto-generated and never edited manually; skill-main creates category skeleton.|Generated.|Use `apex-meta/kb/<slug>/wiki/index.md`; avoid hidden `.llm-wiki` unless needed later.|
|manifest location|Main: `.llm-wiki/cache/source-manifest.json`|`init-wiki.sh` creates manifest.|Generated.|`apex-meta/kb/<slug>/manifests/source-manifest.json` or keep inside `cache/`; V1 should choose visible `manifests/`.|
|log location|skill-main: `log/YYYYMMDD.md`|Operations append log entries; scaffold creates first day log.|Generated.|`apex-meta/kb/<slug>/log/YYYYMMDD.md`|
|audit location|`audit/`, `audit/resolved/`|One file per feedback; resolved archive never deleted.|Generated by scaffold / plugin.|Copy as `audit/` + `audit/resolved/`; plugin deferred.|
|query output location|`outputs/queries/`|Python scaffold creates it; query op saves answers there in rich variant.|Generated.|`apex-meta/kb/<slug>/outputs/queries/`|
|review queue|main: `.llm-wiki/review.json`; rich variant: `audit/*.md`|Main review is JSON queue; rich audit is file-per-feedback.|Generated.|V1 should prefer file audit + optional review JSON only if preserving main lint queue.|

---

## 5. Script Capability Map

|Script|Language|Exact behavior|Inputs / outputs|Dependencies|Copy 1:1?|Adaptation / portability|Apex V1 decision|Citation|
|---|---|---|---|---|---|---|---|---|
|`hash-files.sh`|Bash|Compute SHA-256 for file; for directory, hash sorted file hashes and combine.|input file/dir → hash stdout; errors on invalid target|`sha256sum`, `find`, `sort`, shell|No|Port to Python for Windows; preserve semantics.|**Include as Python hash function.**||
|`init-wiki.sh`|Bash|Create `.llm-wiki` cache/inbox, copy schema, create config/index/hot-cache/source-manifest/review/graph, symlink index.|wiki root + force → initialized wiki|shell, `date`, `cp`, symlink support|No|Symlink / hidden `.llm-wiki` less Windows/Apex-friendly.|**Partial adapt; prefer Python scaffold.**||
|`validate-frontmatter.sh`|Bash|Validate required fields, page type enum, language enum, date format for root-level wiki pages.|wiki root → issue lines; exit 0/1/2|`sed`, `grep`, `find`|No|Bash parsing brittle; port to Python using stdlib parser.|**Include semantics in Python lint.**||
|`find-broken-links.sh`|Bash|Collect page slugs/aliases and report broken `[[wikilinks]]`; skips URLs/section refs.|wiki root → issue lines; exit 0/1/2|`awk`, `sed`, `grep`, `find`|No|Port to Python; preserve alias resolution.|**Include semantics in Python lint.**||
|`find-orphans.sh`|Bash|Reports pages with zero incoming `[[wikilinks]]`.|wiki root → orphan lines|`find`, `sed`, `grep`|No|Port to Python; support nested directories.|**Include semantics in Python lint.**||
|`check-stale.sh`|Bash|Compare stored index hash with live hash of all page frontmatter; exit 0 fresh, 1 stale, 2 no hash.|wiki root → freshness report|`sha256sum`, `find`, `sed`|No|Port to Python; store hash visibly.|**Include as V1 stale-index check.**||
|`_utils.sh`|Bash|`find_wiki_root`: env var first, then `./wiki`.|none/env → root path or empty|shell|No|Replace with Python/path rules in skill.|**Adapt concept only.**||
|`setup-project.sh`|Bash|Project setup: run init, create `.raw/`, create/prepend `CLAUDE.md`, optionally configure hooks/settings, add `.gitignore`.|project root/options → project files|Bash, optional `jq`, hooks|No|Too invasive for Apex V1; hook/CLAUDE writes need strong operator gate.|**Omit from V1; adapt only raw-dir/scaffold concept.**||
|`scaffold.py`|Python|Create typed wiki tree, `CLAUDE.md`, first log, `wiki/index.md`.|wiki root + topic → scaffolded KB|Python stdlib only|Mostly yes|Adapt paths, remove/rename `CLAUDE.md` if Apex avoids schema file named `CLAUDE.md` inside KB root.|**Include/adapt as primary V1 scaffold.**||
|`lint_wiki.py`|Python|Seven-pass health check: dead links, orphans, missing index entries, unlinked concepts, log shape, audit shape, audit targets.|wiki root → stdout report; exit 0/1|Python stdlib only|Mostly yes|Adapt nested page conventions and Apex root.|**Include/adapt as primary V1 lint.**||
|`audit_review.py`|Python|Reads open/resolved audits, parses YAML-ish frontmatter, groups report by target, severity/date sorted.|wiki root + mode → grouped audit report|Python stdlib only|Mostly yes|Adapt severity/status/source enums only if needed.|**Include/adapt as primary V1 audit-list.**||
|`wiki_search.py`|—|NOT FOUND|—|—|No|No verified local file.|**Not found / unverified.**|—|
|`update-index.py`|—|NOT FOUND|—|—|No|No verified local file; `scaffold.py` is not equivalent.|**Not found / unverified.**||
|`init_wiki.py`|—|NOT FOUND|—|—|No|No verified local file.|**Not found / unverified.**|—|
|`feedback-modal.ts`|TypeScript|Obsidian modal with selected-text preview, severity radio chips, markdown comment, save/cancel flow.|selected text → severity/comment result|Obsidian API, audit-shared|No|UI plugin, not Apex V1.|**Omit V1; keep audit file format.**||

---

## 6. Copy / Adapt / Omit Matrix

```
copy_one_to_one:  semantic_workflows:    - index_first_query_behavior:        reason: "Core token-efficiency mechanism."        source: "query.md"    - two_phase_ingest_logic:        reason: "Core quality gate: analysis before generation."        source: "ingest.md"    - audit_as_persistent_feedback_surface:        reason: "Durable human correction layer."        source: "audit-guide.md"    - review_queue_processing_pattern:        reason: "Operator-visible resolution loop."        source: "review.md"  data_conventions:    - concept_entity_summary_separation:        reason: "Richer KB data model."        source: "llm-wiki-skill-main + scaffold.py"    - log_per_day_operation_entries:        reason: "Low-friction durable operation memory."        source: "schema-guide.md + scaffold.py"copy_with_path_adaptation:  mechanisms:    - raw_source_tree:        from: "raw/{articles,papers,notes,refs}/"        to: "apex-meta/kb/<kb-slug>/raw/{articles,papers,notes,refs}/"    - wiki_tree:        from: "wiki/{concepts,entities,summaries,index.md}"        to: "apex-meta/kb/<kb-slug>/wiki/{concepts,entities,summaries,index.md}"    - audit_tree:        from: "audit/, audit/resolved/"        to: "apex-meta/kb/<kb-slug>/audit/, audit/resolved/"    - query_outputs:        from: "outputs/queries/"        to: "apex-meta/kb/<kb-slug>/outputs/queries/"    - source_manifest:        from: ".llm-wiki/cache/source-manifest.json"        to: "apex-meta/kb/<kb-slug>/manifests/source-manifest.json"copy_with_runtime_adaptation:  scripts:    - hash-files.sh:        adaptation: "Bash to Python; preserve SHA-256 file/dir semantics."    - validate-frontmatter.sh:        adaptation: "Bash to Python or merge into lint_wiki.py."    - find-broken-links.sh:        adaptation: "Bash to Python, nested-directory aware."    - find-orphans.sh:        adaptation: "Bash to Python, nested-directory aware."    - check-stale.sh:        adaptation: "Bash to Python stale-index check."    - scaffold.py:        adaptation: "Retain Python, adapt names/paths."    - lint_wiki.py:        adaptation: "Retain Python, adapt Apex path/schema conventions."    - audit_review.py:        adaptation: "Retain Python, adapt Apex path/schema conventions."adapt_semantically_but_not_code:  mechanisms:    - compile_operation:        reason: "No standalone compile script; keep as LLM-owned restructure/split/merge/index operation."    - contradiction_detection:        reason: "LLM-owned semantic judgment; not deterministic script work."    - concept_extraction:        reason: "LLM-owned semantic judgment; preserve as core."    - entity_synthesis:        reason: "LLM-owned semantic judgment; preserve as core."    - query_answer_synthesis:        reason: "LLM-owned synthesis grounded in compiled wiki."    - knowledge_gap_detection:        reason: "LLM-owned judgment surfaced through query/lint/schema."omit_from_V1:  mechanisms:    - graph_html_generation:        reason: "Useful visualization but not necessary for minimal KB engine."    - D3_graph_UI:        reason: "UI dependency / non-core."    - Obsidian_plugin_UI:        reason: "External UI/plugin complexity; audit file format is enough."    - web_viewer_feedback_UI:        reason: "Not opened in this pass; plugin evidence is optional only."    - setup_project_hooks:        reason: "Writes CLAUDE.md/settings/hooks; too invasive for V1."    - bilingual_specific_behavior:        reason: "Can preserve fields, but Apex V1 likely English-first unless operator wants bilingual KB."not_found_or_unverified:  scripts:    - wiki_search.py    - update-index.py    - init_wiki.py  mechanisms:    - verified_BM25_or_semantic_search_script:        status: "Not opened in local blueprint files."    - verified_index_rebuild_python_script:        status: "No update-index.py opened; index rebuild exists as workflow behavior, not verified script."
```

---

## 7. Strongest Blueprint-Faithful V1

```
strongest_blueprint_faithful_V1:  package_generation_status: "not_generated"  required_V1_operations:    - scaffold    - ingest_phase_1_analysis    - ingest_phase_2_page_generation    - query    - lint    - audit    - review_queue_processing  required_V1_scripts:    primary_python:      - scaffold.py_adapted:          role: "Create Apex KB data root and initial schema/index/log/audit/raw/wiki/output folders."      - lint_wiki.py_adapted:          role: "Dead links, orphans, missing index entries, log shape, audit shape, audit targets."      - audit_review.py_adapted:          role: "Group and prioritize open/resolved audit feedback."    python_ports_or_integrated_checks:      - hash_files:          source: "hash-files.sh"          role: "Stable source identity and duplicate-ingest prevention."      - stale_index_check:          source: "check-stale.sh"          role: "Detect index drift."      - frontmatter_validation:          source: "validate-frontmatter.sh"          role: "Protect index/query integrity."      - broken_link_check:          source: "find-broken-links.sh"          role: "Protect navigation."      - orphan_detection:          source: "find-orphans.sh"          role: "Protect discoverability."  required_V1_data_layout:    root: "apex-meta/kb/<kb-slug>/"    children:      - "raw/articles/"      - "raw/papers/"      - "raw/notes/"      - "raw/refs/"      - "wiki/index.md"      - "wiki/concepts/"      - "wiki/entities/"      - "wiki/summaries/"      - "outputs/queries/"      - "audit/"      - "audit/resolved/"      - "log/"      - "manifests/source-manifest.json"  required_V1_LLM_semantic_workflow:    ingest:      - "Read source fully or chunk if large."      - "Extract source summary, concepts, entities, claims, structure."      - "Compare against index/pages for contradictions."      - "Write Phase 1 analysis and halt for operator review when configured."      - "Generate/update wiki pages after approval."      - "Crosslink pages and preserve source pointers."      - "Regenerate/update index."      - "Update manifest and source hash/sentinel."    query:      - "Read index first."      - "Select 3–5 pages."      - "Read pages fully."      - "Answer with evidence, contradictions, gaps, confidence."      - "Save durable query output and optionally promote to wiki."    audit:      - "Read open audit files."      - "Anchor feedback to target content."      - "Accept, partially accept, reject, or defer with rationale."      - "Move resolved items and log operation."  deferred_items:    - graph_html_generation    - D3_visualization    - Obsidian_plugin_UI    - web_viewer    - hook_setup    - wiki_search_py_if_later_found    - update_index_py_if_later_found    - automatic_planning_integration    - cross_KB_global_graph  missing_research_before_package_generation:    - "Decide final Apex-visible schema file name: keep `CLAUDE.md` inside each KB root or rename to `kb-schema.md` to avoid Claude-project-instruction ambiguity."    - "Decide whether V1 index is generated by adapted Python lint/helper or LLM workflow only."    - "Inspect actual existing `apex-meta/` tree before selecting final data root creation behavior."    - "Decide whether Bash helpers are allowed at all in Apex V1 or must be fully Python-ported."  why_blueprint_faithful:    - "Preserves LLM-Wiki’s central product: compiled durable wiki knowledge, not raw-source rereading."    - "Preserves two-phase ingest, source hashing, manifest/sentinel logic, contradiction detection, review/audit loop, index-first query, and saved query outputs."    - "Keeps semantic work LLM-owned and deterministic waste script-owned, matching the main blueprint’s design principle: LLM extracts/cross-references/contradicts; scripts hash/list/validate."
```

**Evidence basis:** `llm-wiki-main` explicitly defines the persistent compiled wiki model and raw-source → wiki → schema architecture, with the LLM responsible for reading, extracting, creating interlinked pages, and maintaining currency. Its design principle separates LLM runtime from Bash helpers: Bash handles hashing/grep/file listing while the LLM handles extraction, cross-referencing, and contradiction detection. The richer variant supplies the data model and Python script base: `raw/`, `wiki/`, `audit/`, `outputs/queries/`, `log/`, scaffold, lint, and audit scripts.

---

## 8. Guardrail Check

```
guardrail_check:  did_we_generate_package_files: "NO"  did_we_generate_SKILL_md: "NO"  did_we_generate_reference_files: "NO"  did_we_generate_templates: "NO"  did_we_generate_python_script_contents: "NO"  did_we_create_final_package_tree: "NO"  did_we_invent_new_architecture: "NO"  qualification: >    The V1 recommendation composes opened LLM-Wiki mechanisms with Apex path/runtime    adaptation only. Items without opened-file support are marked not found or deferred.  did_we_read_live_files: "YES"  evidence:    - "Connected private repo file fetches were used for the LLM-Wiki blueprint files."    - "Uploaded/local project resources were used as guidance/context only."  did_every_claim_trace_to_opened_files: "YES_OR_FLAGGED"  flags:    - "Existing generated data instances were not inspected."    - "`wiki_search.py`, `update-index.py`, and `init_wiki.py` were not found/opened."    - "`llm-wiki-skill-main/SKILL.md` is cited through the opened file output, but several exact subclaims are also supported by its opened companion scripts/references."  did_we_preserve_Apex_KB_as_independent_first_class_knowledge_engine: "YES"  final_boundary: >    Apex KB should be an independent durable knowledge compiler and AI-consumable    repo context layer. Apex plan/session/sync consume its outputs; they do not    define its core.
```