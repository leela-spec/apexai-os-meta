---
title: "APEX KB Full Lifecycle Simulation Report"
page_type: audit_item
kb_slug: "lika-verein-taxes-accounting"
source_refs: []
created_at: "2026-06-30T15:10:00Z"
updated_at: "2026-06-30T15:10:00Z"
confidence: "unknown"
claim_label: "raw_source"
status: "needs_review"
---

# APEX_KB_FULL_LIFECYCLE_SIMULATION_REPORT

```yaml
verdict: PARTIAL

repo_assumption:
  all_prior_outputs_saved_to_repo: true
  branch: main
  repo_access_verified: true
  repo: leela-spec/apexai-os-meta
```

## 1. Skill loaded

```yaml
skill_loaded:
  files_read:
    - ".claude/skills/apex-kb/SKILL.md"
    - ".claude/skills/apex-kb/references/kb-contract.md"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
  lifecycle_understood: true
  ownership_split_understood: true
```

Evidence:

- The live repo skill defines the lifecycle from `scaffold` through source intake, Phase 0, Phase 1, operator gate, Phase 2 wiki compile, deterministic validation, local retrieval, query packets, and lint/audit maintenance.
    
- It explicitly forbids mutation of Apex Plan, Sync, Session, PreCap, FlowRecap, APSU/status-merge, and personal orchestration state.
    
- It defines Python/Codex ownership versus LLM ownership cleanly.
    
- The operation rules enforce that Phase 0 must not create ingest-analysis files, wiki pages, semantic summaries, or vector stores; Phase 2 requires `approve ingest`.
    

## 2. Target KB loaded

```yaml
target_kb_loaded:
  root: "apex-meta/kb/lika-verein-taxes-accounting/"
  files_read:
    - README.md
    - kb-schema.md
    - manifests/source-manifest.json
    - manifests/phase0/corpus-profile.md
    - manifests/phase0/phase0-navigation-report.md
    - ingest-analysis/group-1-core-tax-law.analysis.md
    - wiki/index.md
    - wiki/summaries/core-tax-law-invoicing-gobd.md
    - derived/search/index-meta.json
    - outputs/queries/20260628T204003Z-verein-steuer-buchhaltung-spenden-rechnung-gemeinn-tzigkeit.md
    - log/llm-phase2-report_20260629_180000.md
  compiled_pages_found: true
  ingest_analysis_found: true
  phase0_artifacts_found: true
  retrieval_outputs_found: true
```

Evidence:

- The KB README declares the canonical paths for raw custody, ingest analysis, wiki, source manifest, Phase 0, derived search, audit, and query outputs.
    
- The schema defines this KB’s slug, topic, source authority levels, taxonomy, English-primary language policy, and `approve ingest` review policy.
    
- The manifest exists and records source custody fields including `source_hash`, `source_path`, `source_storage_mode`, `source_type`, and status.
    

---

# 3. Lifecycle simulation

## S1 — Source custody

```yaml
source_custody:
  status: PASS
  evidence:
    - "README declares raw/, source-manifest.json, and custody structure."
    - "source-manifest.json exists and records hashed copied sources."
  issues:
    - "Fetched manifest excerpt only showed first entries, not complete manifest count."
  workaround:
    - "Use manifest existence and field shape as sufficient simulation evidence; delegate complete inventory/count verification to Codex."
```

The source-manifest sample shows SHA-256 hashes, storage mode `copy_into_kb`, active status, source path, source type, and source IDs.

## S2 — Phase 0 navigation

```yaml
phase0_navigation:
  status: PASS_WITH_MINOR_GAPS
  evidence:
    - "Phase 0 report exists."
    - "103 files scanned."
    - "Required Phase 0 artifact list exists."
    - "Boundary statement confirms no semantic/wikified/vector outputs."
  issues:
    - "corpus-profile reports source-inventory JSON/CSV not present/readable, even though source-manifest exists."
    - "Phase 0 report is structurally thin: artifact list + boundary, not a rich read-first/read-later navigation report."
  workaround:
    - "Use corpus-profile, heading/link/frontmatter maps, keyword hits, topic map, and source-priority candidates together, not phase0-navigation-report alone."
```

Phase 0 scanned 103 files and produced the expected artifact list. It also states the run created deterministic navigation artifacts only and did not create semantic analysis, wiki pages, embeddings, vector stores, or orchestration state.

The corpus profile confirms 103 scanned files, 2,680,053 bytes, 81 Markdown files, duplicate hash groups, and large source candidates.

## S3 — Phase 1 ingest analysis

```yaml
phase1_ingest_analysis:
  status: PARTIAL_PASS
  evidence:
    - "Grouped Phase 1 analysis exists."
    - "It contains source_refs, status operator_review_needed, key claims, concepts, entities, source-quality notes, and open risk handling."
  issues:
    - "Grouped analysis is not one analysis per source."
    - "Frontmatter uses claim_label: source_grounded_analysis, which is not in the allowed claim_label enum."
    - "phase_2_allowed remains false in the Phase 1 file, which is correct for the gate but means Phase 2 provenance must be handled separately."
  workaround:
    - "Treat grouped Phase 1 as an approved grouped bridge layer, but flag source-specific Phase 1 backfill as a quality patch."
```

The group-1 Phase 1 file is present, marked `ingest_phase_1` and `operator_review_needed`, and lists its source refs. It contains source-quality notes, key claims, concepts, and entities.

Contract mismatch: `source_grounded_analysis` appears as a `claim_label`, but the KB contract allows only `raw_source`, `source_backed_summary`, `behavioral_inference`, `working_hypothesis`, `operator_question`, and `practitioner_question`.

## S4 — Phase 2 compiled wiki

```yaml
phase2_wiki:
  status: PARTIAL_PASS
  evidence:
    - "wiki/index.md exists and names six compiled summaries."
    - "At least one compiled summary page exists in repo with source_refs and source pointers."
  issues:
    - "Phase 2 report still says artifacts were chat_output_only and repo_written: false, which now contradicts repo state because summary pages are present."
    - "Index auto-generated section says compiled page count before Phase 2 was 0 and deterministic rebuild is required."
    - "Concept/entity pages are still deferred."
  workaround:
    - "Use the repo-written summary pages as current evidence, but mark Phase 2 provenance/log metadata stale until postflight index/lint/audit updates it."
```

The wiki index now lists six compiled summaries and routing guidance. The `core-tax-law-invoicing-gobd.md` summary exists with source refs, hashes, source pointers, confidence, claim label, status, review flags, claims, contradictions, and open questions.

However, the Phase 2 report says “No repository files were written in this chat” and marks Phase 2 artifacts `chat_output_only`. It also says `repo_written: false` and deterministic postflight was not run. This is now stale or contradictory relative to the repo-visible summary pages.

## S5 — Retrieval

```yaml
retrieval:
  status: FAIL_CURRENT_STATE_BUT_IMPLEMENTATION_READY
  evidence:
    - "derived/search/index-meta.json exists."
    - "retrieval script can build JSON/NDJSON/SQLite indexes from wiki pages."
  issues:
    - "current index-meta has page_count: 0 and chunk_count: 0."
    - "saved query packet has result_count: 0."
    - "retrieval index predates repo-written Phase 2 pages."
  workaround:
    - "Do not rely on current retrieval outputs. Rebuild retrieval index after deterministic wiki/index rebuild."
```

The current derived search metadata says `backend: sqlite_fts5`, `page_count: 0`, `chunk_count: 0`, and no indexed files. The saved query packet reports `result_count: 0`.

The implementation itself is capable: `apex_kb_retrieval.py` chunks wiki pages, builds JSON/NDJSON, probes FTS5, writes SQLite where available, and writes index metadata.

## S6 — Query packet

```yaml
query_packet:
  status: PARTIAL_FAIL
  evidence:
    - "query packet file exists."
    - "It records backend, query, stale status, and raw JSON."
  issues:
    - "It contains zero evidence results."
    - "It is from 2026-06-28, before Phase 2 pages were saved/reconciled."
  workaround:
    - "Generate a fresh query packet only after index and retrieval rebuild."
```

The existing query packet is structurally present, but empty.

## S7 — Lint / audit / status

```yaml
lint_audit_status:
  status: NOT_EXECUTED_HERE
  evidence:
    - "scripts implement lint, audit, status."
    - "Phase 2 report explicitly requires deterministic postflight."
  issues:
    - "No fresh command output from current repo state is available in this chat."
    - "Cannot honestly claim py_compile, status, lint, audit, or retrieval build executed."
  workaround:
    - "Delegate to Codex with exact command block; continue semantically from repo evidence only."
```

The script implements `lint`, `audit`, `status`, and `health` subcommands. The Phase 2 report explicitly lists required postflight commands and states deterministic postflight had not run.

---

# 4. Final answer-quality simulation

## Test query

> “What should Lika read first for invoice, e-invoice, and receipt custody questions?”

## Small read set

```yaml
small_read_set:
  - "wiki/index.md"
  - "wiki/summaries/core-tax-law-invoicing-gobd.md"
```

## Simulated KB-grounded answer

Lika should start with `wiki/summaries/core-tax-law-invoicing-gobd.md` for invoice, small-invoice, E-Rechnung, and Belegablage questions. The wiki index explicitly routes invoice/E-Rechnung queries to that summary.

The current compiled summary says the strongest inspected legal anchors are BMJ/Gesetze im Internet invoice sources and §33 UStDV for `Kleinbetragsrechnung`; it treats the BMF E-Rechnung FAQ as relevant but lower-confidence because the capture contains web-navigation noise.

Limitations remain: the summary does not resolve whether every event ticket is a sufficient invoice, and it warns not to rely on the current high-noise BMF GoBD Markdown capture for detailed GoBD claims.

---

# 5. Deterministic steps needed

```yaml
deterministic_steps_needed:
  - step: "compile scripts"
    reason: "Verify current main scripts compile in the actual repo runtime."
  - step: "run status/lint/audit"
    reason: "Detect current structural issues after Phase 2 pages exist."
  - step: "rebuild deterministic wiki index"
    reason: "wiki/index.md auto-generated section still says compiled page count before Phase 2 was 0."
  - step: "rebuild retrieval index"
    reason: "derived/search/index-meta.json currently has page_count 0 and chunk_count 0."
  - step: "rerun retrieval query"
    reason: "Existing saved query packet has result_count 0."
  - step: "inventory exact file set"
    reason: "Confirm all six summary pages and any concept/entity pages actually exist."
```

## Codex prompt

````markdown
# Codex Task — Apex KB Deterministic Lifecycle Postflight

Work directly on `main`.

Repo:

```text
leela-spec/apexai-os-meta
````

Target KB:

```text
apex-meta/kb/lika-verein-taxes-accounting/
```

Do not create branches.  
Do not redesign files.  
Do not modify semantic content.  
Do not mutate Apex Plan, Apex Sync, Apex Session, PreCap, FlowRecap, APSU/status-merge, or personal orchestration files.

## Goal

Run deterministic postflight after repo-written Phase 2 summary pages.

## Commands to run

```bash
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py

python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json health
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json status
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json lint
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json audit

python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json --allow-write index

python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json health
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json stale
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json --allow-write build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json query --query "Verein Steuer Buchhaltung Spenden Rechnung Gemeinnützigkeit" --limit 8 --save --allow-write
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/lika-verein-taxes-accounting --json stale
```

## Exact inventory checks

List these paths and report present/missing:

```text
apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/core-tax-law-invoicing-gobd.md
apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/association-accounting-process.md
apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/events-vat-tickets.md
apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/artist-contractor-obligations.md
apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/source-judgment-and-open-risks.md
apex-meta/kb/lika-verein-taxes-accounting/wiki/summaries/source-quality-and-custody.md
apex-meta/kb/lika-verein-taxes-accounting/wiki/concepts/
apex-meta/kb/lika-verein-taxes-accounting/wiki/entities/
apex-meta/kb/lika-verein-taxes-accounting/derived/search/index-meta.json
apex-meta/kb/lika-verein-taxes-accounting/outputs/queries/
```

## Required report

```yaml
CODEX_DETERMINISTIC_STEP_REPORT:
  branch:
  commit_before:
  dirty_before:
  commands_run:
    - command:
      exit_code:
      stdout_summary:
      stderr_summary:
  files_created:
  files_modified:
  files_deleted:
  commit_created:
  pushed_to_main:
  deterministic_result:
    py_compile:
    health:
    status:
    lint:
    audit:
    wiki_index_rebuild:
    retrieval_health:
    retrieval_stale_before:
    retrieval_build:
    retrieval_query:
    retrieval_stale_after:
  exact_inventory:
    present:
    missing:
  problems_found:
  recommended_next_actor: LLM_CHAT | CODEX | OPERATOR
  recommended_next_action:
```

````

---

# 6. Apex KB design findings

```yaml
apex_kb_design_findings:
  inefficiencies:
    - "Phase 2 repo state and Phase 2 report/log state drifted: report says chat_output_only/repo_written false while pages now exist."
    - "Phase 0 report is too thin for an LLM lifecycle executor; useful data is spread across corpus-profile, maps, priority candidates, and report."
    - "Retrieval was built before compiled pages existed, causing page_count/chunk_count 0 and a useless query packet."
    - "Grouped Phase 1 gives fast coverage but weak source-specific traceability."
    - "Manual operator must remember to run deterministic postflight after semantic writes."

  contract_mismatches:
    - "Phase 1 grouped analysis uses claim_label: source_grounded_analysis, which violates allowed claim_label enum."
    - "Phase 2 report path/status says repo_written false even though compiled pages are now in repo."
    - "wiki/index.md auto-generated section still reports compiled page count before Phase 2 chat-output compile: 0."
    - "Some older command text used --write, but live scripts use --allow-write."

  implementation_gaps:
    - "No confirmed fresh lint/audit/status after Phase 2 pages."
    - "No confirmed fresh retrieval index after Phase 2 pages."
    - "No concept/entity page compile complete yet."
    - "No deterministic audit item materialization for high-risk unresolved tax questions visible in the checked subset."
    - "No verified source-specific Phase 1 backfill for all high-priority sources."

  useful_workarounds:
    - "Use wiki/index.md LLM summary routing first, then 1-2 summary pages."
    - "Treat retrieval outputs as invalid until derived/search is rebuilt."
    - "Treat grouped Phase 1 as a bridge layer, not final per-source ingest."
    - "Use source-quality-and-custody and source-judgment summaries to avoid trusting noisy captures."

  recommended_patches:
    - "Run deterministic postflight and commit updated wiki/index.md plus derived/search outputs if changed."
    - "Update llm-phase2-report or add a new postflight log explaining that Phase 2 pages are now repo-written."
    - "Normalize Phase 1 claim_label values to allowed enum, likely source_backed_summary or working_hypothesis depending on section."
    - "Add a lifecycle status page or log generated after every major phase."
    - "Create audit items for R001-R005 high-risk open items listed in the Phase 2 report."
    - "Compile at least the 23 deferred concept pages or explicitly mark them as deferred in `wiki/index.md`."
````

---

# 7. Final next action

```yaml
final_next_action:
  actor: CODEX
  action: >
    Run deterministic postflight on main: compile scripts, status, lint, audit,
    rebuild wiki index, rebuild retrieval index, rerun query, and report exact
    file inventory. Do not change semantic content.
```

**Bottom line:** the lifecycle is no longer missing Phase 2 as a category; Phase 2 summary pages are present in repo. The lifecycle is still **not a PASS** because deterministic postflight and retrieval are stale/empty, Phase 2 provenance logs contradict current repo state, and concept/entity backfill is incomplete.