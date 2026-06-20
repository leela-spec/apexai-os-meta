# Resolved prompt configuration

**Scope correction accepted:** This prompt is **not** about the Apex PreCap/FlowRecap/APSU loop. It is only about synthesizing a new **PM / KB / PD operating model** from repo evidence, uploaded design material, and the additional analysis you will provide.

**Binding exclusions:** No Hermes runtime, no OpenClaw, no LangGraph, no project-status-overview dependency, no PreCap/FlowRecap/APSU integration. Existing `project-kb-manager` material is treated as a rough draft, not canonical. This matches the current research direction toward a layered PM/KB/PD model and a deterministic-script-plus-AI split rather than blindly preserving older Apex artifacts .

---

# Copy-paste prompt for GPT-5.5 Pro Thinking

```
# GPT-5.5 Pro Thinking Prompt — Apex PM/KB/PD Debris Digestion & Best-Practice SynthesisYou are GPT-5.5 Pro Thinking. You are working as a senior architecture synthesizer for a local, Claude Code–native system called Apex.Your task is **not** to build files. Your task is to deeply digest source debris, compare existing repo-native PM/KB/PD patterns, and produce the best analysis and guidance for what Apex should build next.The current active scope is:> Build the best possible **Project Management / Knowledge Base Management / Product Development operating model** for Apex, using evidence from existing source repos, uploaded research, and current operator decisions.## 0. Hard scope lock### In scopeYou must analyze and synthesize:1. **Project Management layer**   - Project decomposition   - Task/chunk/epic/milestone models   - Dependencies   - Blockers   - “What next?” logic   - Status/query/reporting logic   - Markdown/file-first project state2. **Knowledge Base Management layer**   - Project knowledge records   - Source ingestion   - Indexing   - Registry patterns   - Stale/conflicting knowledge detection   - Query/retrieval conventions   - File schemas and update rules3. **Product Development / Process Design layer**   - Product-development task grammar   - Spec-to-work decomposition   - Acceptance criteria   - Definition-of-done logic   - Implementation/test/handoff structure   - AI-assisted but operator-controlled development flows4. **Execution mechanics**   - What should be handled by deterministic scripts   - What should be handled by Claude/AI reasoning   - What should remain manual/operator-gated   - What should be represented as Markdown, YAML, JSON, or hybrid files5. **Source-pattern synthesis**   - Which existing repo/source pattern should be copied as-is   - Which should be adapted as a baseline   - Which should be merged from multiple sources   - Which should be rejected   - Which new Apex-specific layer is justified only after evidence proves no existing pattern fits### Out of scopeDo **not** analyze or integrate the following active loop:- PreCapWeek- PreCapNextDay- OperatorExecutesPlannedFlow- FlowRecap- APSU / AllProjectStatusPacketUpdate- next PreCapNextDayThese may be future downstream consumers, but they must **not** shape the current analysis except as a tiny “future harmonization note” at the end.Also exclude:- Hermes runtime- Hermes profiles- Hermes cron- Hermes Kanban- OpenClaw- LangGraph- Project Status Overview as a binding artifact- Existing `project-kb-manager` as binding truth- Any final `.claude/skills/` file generation- Any final runtime implementation file generationThe operator explicitly decided that integrating the Apex planning/recap loop now would create unnecessary complexity. Keep it out.---## 1. Source authority modelUse this source-priority model:```yamlsource_priority:  current_operator_instructions:    priority: P0_binding    meaning: "Highest authority. Overrides repo files, prior drafts, and earlier AI conclusions."  additional_analysis_from_operator:    priority: P0_binding_or_P1_primary    meaning: >      The operator may provide an additional analysis from another chat.      Ingest it as a major synthesis input, but still validate claims against repo evidence where possible.  uploaded_current_research:    priority: P1_primary    examples:      - Apex PM/KB/PD research      - Apex Execution Options Research      - PM skill/database research      - current chat recaps      - repo-index summaries  source_repos_under_ProjectRepos:    priority: P1_primary_evidence    meaning: >      Treat source repos as evidence for battle-tested patterns.      Do not assume a repo should be imported wholesale.  existing_Apex_files:    priority: P2_draft_evidence    meaning: >      Existing Apex artifacts are evidence of prior attempts, not canonical truth.      If they conflict with current operator direction, mark them as drift.  prior_AI_rankings:    priority: P3_context_only    meaning: >      Use as orientation. Re-rank from evidence.  public_or_native_terminology:    priority: P1_language_preference    meaning: >      Strongly prefer public/native PM, KB, PD, Claude Code, Markdown, and software-delivery terminology      over private Apex vocabulary unless a custom term is clearly necessary.
```

---

## 2. Current operator decisions

Treat these as binding:

```
operator_decisions:  prompt_mission:    primary_output: "All of the following: evidence digest, decision recommendation, implementation guidance, and downstream prompt-flow guidance."    recommendation_mode: "Recommend, but mark confidence and alternatives."    current_task_type: "Debris digestion and synthesis only."  active_system_scope:    target: "Apex PM / KB / PD combined operating model."    not_target:      - PreCapWeek_to_PreCapNextDay_loop      - project_status_overview      - Hermes_runtime      - OpenClaw      - LangGraph  source_scope:    include:      - uploaded_Apex_design_and_research_files      - GitHub_ProjectRepos_source_folders      - additional_operator_analysis_from_other_chat    exclude:      - live_web_unless_operator_explicitly_requests      - Hermes_specific_runtime_docs      - OpenClaw      - LangGraph  repo_evidence_depth:    mode: "Inspect enough files to prove or disprove reusable implementation patterns."    minimum_preference:      - README_or_overview      - skill_or_agent_entrypoint_if_present      - schema_or_conventions_file_if_present      - command_or_script_registry_if_present      - representative_implementation_file_if_present      - representative_example_or_task_file_if_present  existing_project_kb_manager:    status: "rough prior estimate only"    rule: "Replace if stronger repo pattern exists."    preserve_only:      - useful intent      - useful field ideas      - useful path ideas    do_not_preserve:      - schema if inferior      - path layout if inferior      - custom vocabulary if public/native terminology is better  project_status_overview:    status: "not important for current synthesis"    rule: "Do not use as a binding constraint."  import_strategy:    preferred: "One main baseline plus narrow supporting imports where justified."    allowed_import_modes:      - copy_exact_as_is_when_best_and_safe      - adapt_one_existing_baseline      - synthesize_new_Apex_layer_from_multiple_sources      - reject_pattern_with_reason  terminology:    preference: "Strongly prefer public and native terminology."    custom_Apex_terms: "Use only when necessary and define explicitly."  execution_model:    required: "Produce script-vs-skill-vs-manual decision matrix."    Claude_Code_first: true    Hermes_compatible_later: true    no_Hermes_design_now: true  output_style:    detail_level: "Maximal operating prompt with source index, phases, output contracts, validation gates."    exact_output_templates_required: true    final_deliverable_sequence_required: true    no_final_files: true    draft_file_list_allowed: true  validation:    require_input_output_contract_check: true    require_drift_detection: true    require_confidence_scores_1_to_100: true    require_evidence_references: true  model_behavior:    do_best_effort: true    do_not_stop_for_clarifying_questions: true    create_operator_decision_queue_for_unresolved_items: true
```

---

## 3. Candidate source repo index

The source repositories are expected under:

```
apexai-os-meta/source-knowledge/ProjectRepos/
```

Verify actual availability first. Do not assume every folder exists. If directory listing is unavailable, use repo search and known file paths.

### Mandatory candidate groups

#### A. Project Management / task systems

```
pm_candidates:  ccpm-main:    expected_role: "Spec-driven PM flow; PRD → epic → task decomposition; dependency metadata; status/next/blocked scripts."    inspect_for:      - task_hierarchy      - metadata_fields      - script_first_rules      - next_action_logic      - blocked_logic      - acceptance_criteria      - definition_of_done      - GitHub_or_worktree_coupling_to_remove_or_keep  backlog-main_or_Backlog.md-main:    expected_role: "Markdown-native task database / project board."    inspect_for:      - task_file_format      - YAML_frontmatter      - Markdown_body_sections      - status_fields      - dependency_fields      - CLI_separation_from_file_schema      - local_repo_storage  claude-task-master-main:    expected_role: "Dependency-aware task management and next-task selection."    inspect_for:      - tasks_json_or_manifest_model      - dependency_algorithm      - next_task_logic      - PRD_parsing      - priority_model      - JSON_vs_Markdown_tradeoffs      - Node_or_MCP_coupling  gsd-core-next:    expected_role: "Session continuity, state/context capture, phase-loop discipline."    inspect_for:      - STATE_or_CONTEXT_equivalent      - session_handoff      - phase_loop      - stale_context_prevention      - context_engineering_rules      - what_to_borrow_for_Apex_PM_KB_PD  planning-with-files-master:    expected_role: "Persistent planning scratchpad and context-loss survival."    inspect_for:      - task_plan_findings_progress_pattern      - 2_action_write_rule      - error_persistence      - progress_logging      - session_recovery      - what_to_borrow_as_safety_protocol
```

#### B. Knowledge Base / wiki systems

```
kb_candidates:  llm-wiki-main:    expected_role: "Persistent interlinked project wiki / KB from source docs."    inspect_for:      - index_structure      - schema_files      - raw_source_ingestion      - query_rules      - linting      - graph_or_link_model      - stale_or_conflict_detection      - surgical_update_rules  llm-wiki-skill-main:    expected_role: "Skill/package implementation variant for KB management."    inspect_for:      - skill_entrypoint      - scripts      - scaffold      - linting      - examples      - package_structure
```

#### C. Claude / AI task grammar support

```
ai_process_candidates:  crewAI-main:    expected_role: "Task design grammar and structured AI task outputs, not runtime import."    inspect_for:      - task_expected_output      - dependencies      - guardrails      - structured_outputs      - human_review      - skills_vs_tools_distinction      - what_can_be_translated_to_Claude_Code_without_importing_CrewAI_runtime
```

### Explicit exclusions

Do not inspect or use as active candidates:

```
excluded_candidates:  - OpenClaw  - LangGraph  - Hermes runtime  - Hermes Agent  - Hermes cron  - Hermes Kanban  - Apex PreCap/FlowRecap/APSU runtime specs
```

If prior research mentions excluded systems, summarize only in a footnote under “Excluded from current scope” and do not incorporate into recommendations.

---

## 4. Required analysis phases

Follow exactly these phases.

## Phase 1 — Scope confirmation and source inventory

### Tasks

1. Restate the active scope in one paragraph.
2. List excluded areas.
3. Verify which source repos/files are available.
4. Create a confirmed inventory table.

### Output template

```
## Phase 1 — Scope and Inventory### Active scope...### Explicitly excluded...### Confirmed source inventory| Source | Availability | Evidence method | Notes ||---|---:|---|---|| ccpm-main | confirmed / partial / missing | path/search | ... || backlog-main | confirmed / partial / missing | path/search | ... |
```

---

## Phase 2 — Evidence read plan

Before synthesizing, build a read plan.

### Required columns

```
| Source | Files to inspect | Why these files | Expected pattern | Minimum evidence threshold ||---|---|---|---|---|
```

### Rule

Do not make strong claims about a source until enough evidence has been inspected. If evidence is weak, mark it `low confidence`.

---

## Phase 3 — Source-by-source evidence digest

For every inspected source, produce:

```
## Source Digest — [source name]### Files inspected| File | Role | Evidence quality | Key findings ||---|---|---:|---|### Reusable patterns| Pattern | Description | Copy/adapt/synthesize/reject | Reason | Confidence ||---|---|---|---|---:|### Couplings / anti-patterns| Coupling or risk | Why it matters | Keep/remove/adapt | Confidence ||---|---|---|---:|### Native terminology to reuse- ...### Apex-specific terminology to avoid or translate- ...
```

---

## Phase 4 — Layer map: PM / KB / PD

Create a layer map that separates the system into clean subsystems.

### Required layers

```
required_layers:  project_management:    examples:      - project_decomposition      - epic_or_chunk_model      - task_model      - subtask_model      - dependencies      - blockers      - next_action      - status_reporting  knowledge_base_management:    examples:      - registry      - project_records      - source_documents      - index      - query      - update_log      - stale_detection      - conflict_detection  product_development:    examples:      - spec_intake      - acceptance_criteria      - implementation_plan      - test_strategy      - done_definition      - handoff_notes      - release_or_delivery_state  deterministic_operations:    examples:      - file_scans      - schema_validation      - registry_update      - next_task_query      - dependency_graph_check      - stale_state_detection      - report_generation  ai_reasoning_operations:    examples:      - prioritization      - next_action_synthesis      - blocker_interpretation      - ambiguity_resolution      - project_health_summary      - product_strategy_tradeoff
```

### Output template

```
## Phase 4 — Layer Map| Layer | Purpose | Best source baseline | Supporting sources | What must be custom | Confidence ||---|---|---|---|---|---:|
```

---

## Phase 5 — Pattern decision matrix

Create a matrix of all major candidate patterns.

### Required decision types

Use exactly these values:

```
decision_values:  - copy_as_is  - adapt_as_baseline  - synthesize_from_multiple_sources  - reject  - defer
```

### Output template

```
## Phase 5 — Pattern Decision Matrix| Pattern | Source(s) | Layer | Decision | Reason | Required adaptation | Confidence ||---|---|---|---|---|---|---:|
```

### Examples of patterns to evaluate

- Markdown task file with YAML frontmatter
- JSON task manifest
- Project registry
- Wiki index
- Source ingestion folder
- Dependency graph
- Next-task algorithm
- Blocked-task report
- Acceptance criteria section
- Definition of done checklist
- Implementation notes section
- Findings/progress/session log files
- Script-first status reports
- Schema-first KB records
- Manual operator review flags
- AI-generated priority scores
- Public/native PM terminology
- Private Apex custom vocabulary

---

## Phase 6 — Script vs Claude skill vs manual operator matrix

Produce a hard separation of responsibilities.

### Required output

```
## Phase 6 — Execution Responsibility Matrix| Function | Deterministic script | Claude reasoning | Manual operator | Recommended representation | Reason | Confidence ||---|---:|---:|---:|---|---|---:|
```

### Rules

Prefer deterministic scripts for:

- parsing files
- validating schemas
- finding missing fields
- updating registries
- computing dependency availability
- finding blocked tasks
- generating low-token status reports
- detecting stale timestamps
- extracting backlinks/references
- sorting already-scored items

Prefer Claude reasoning for:

- interpreting ambiguous project intent
- deciding whether a task belongs to PM, KB, or PD
- synthesizing next actions
- evaluating product-development tradeoffs
- detecting implicit blockers
- creating human-readable summaries
- choosing between alternative architectures
- explaining uncertainty

Prefer manual operator gates for:

- approving destructive changes
- accepting major architecture decisions
- resolving contradictory source patterns
- confirming high-impact priority changes
- deciding whether to copy external patterns as-is

---

## Phase 7 — Proposed Apex PM/KB/PD operating model

This is the central synthesis section.

### Required subsections

```
## Phase 7 — Recommended Apex PM/KB/PD Operating Model### 7.1 Executive recommendationOne paragraph.### 7.2 Recommended baseline architectureUse a concise diagram or tree.### 7.3 Recommended file/data modelDraft only. No final files.### 7.4 Recommended terminologyPrefer public/native terminology.### 7.5 Recommended lifecycleDescribe how a project moves from intake → active work → blocked/review/done/archive.### 7.6 Recommended query/reporting modelDescribe status, next, blocked, stale, search, and validation outputs.### 7.7 Recommended KB modelDescribe registry, project records, source docs, index, update log, and query behavior.### 7.8 Recommended PD modelDescribe spec intake, task decomposition, acceptance criteria, test strategy, done definition.### 7.9 What not to buildList rejected over-complex layers.
```

### Draft model constraints

You may propose draft file paths, but you must label them as draft:

```
draft_only: truenot_final_file_generation: true
```

Do not write file contents.

---

## Phase 8 — Contract and drift analysis

Run a contract check, but only for the PM/KB/PD system.

### Required contract checks

For every proposed subsystem, define:

```
contract_fields:  owner:  purpose:  input:  output:  mutation_authority:  upstream_source:  downstream_consumer:  validation_check:  failure_mode:  confidence:
```

### Drift analysis

Compare the recommended model against existing Apex drafts only as drift evidence.

Do not preserve older Apex material merely because it exists.

### Output template

```
## Phase 8 — Contract and Drift Register### Subsystem contracts| Subsystem | Owner | Inputs | Outputs | Mutation authority | Validation | Confidence ||---|---|---|---|---|---|---:|### Drift register| Existing artifact / idea | Drift | Keep / replace / ignore | Reason | Confidence ||---|---|---|---|---:|
```

---

## Phase 9 — Final recommendation package

Produce the final synthesis.

### Required sections

```
## Phase 9 — Final Recommendation Package### 9.1 Best overall strategyChoose one:- one_main_baseline- layered_import- custom_synthesis- defer_pending_evidence### 9.2 Source influence map| Source | Final role | Import mode | Confidence ||---|---|---|---:|### 9.3 Build-sequence recommendationDraft-only sequence. No file generation.### 9.4 Draft file/package listAllowed, but no file contents.### 9.5 Validation gates before file creationList gates.### 9.6 Operator decision queueNumbered open decisions.### 9.7 Risks and anti-patternsList with mitigation.### 9.8 Next best promptCreate the next prompt only if necessary. If not necessary, state “No second prompt needed.”
```

---

## 5. Output contract

Your final answer must use this exact top-level structure:

```
# Apex PM/KB/PD Debris Digestion & Synthesis## 0. Scope Lock## 1. Source Inventory## 2. Evidence Read Plan## 3. Source Digests## 4. Layer Map## 5. Pattern Decision Matrix## 6. Script vs Claude vs Manual Matrix## 7. Recommended Apex PM/KB/PD Operating Model## 8. Contract and Drift Register## 9. Final Recommendation Package## 10. Operator Decision Queue## 11. Confidence Summary
```

---

## 6. Evidence rules

Use evidence references whenever possible.

If line citations are available, include them.

If line citations are not available, use file paths and explain that exact line references were unavailable.

Do not cite a source for a claim it does not support.

Do not make claims about a repo’s implementation if you only read its README, unless you label the claim as README-level only.

Use confidence scoring:

```
confidence_scale:  90_100: "Strong evidence, multiple files, low ambiguity."  75_89: "Good evidence, minor uncertainty."  60_74: "Moderate evidence, likely but needs validation."  40_59: "Weak evidence, partial source coverage."  0_39: "Speculative or insufficient evidence."
```

---

## 7. Anti-confusion rules

You must obey these:

1. Do not mention PreCapWeek / PreCapNextDay / FlowRecap / APSU except in a final one-line future harmonization note.
2. Do not use Project Status Overview as an input constraint.
3. Do not treat existing `project-kb-manager` as canonical.
4. Do not import Hermes runtime assumptions.
5. Do not inspect OpenClaw or LangGraph for this prompt.
6. Do not design a scheduler.
7. Do not design a multi-agent runtime.
8. Do not create final files.
9. Do not create final schemas.
10. Do not create final `.claude/skills/` packages.
11. Prefer public/native terminology over private Apex vocabulary.
12. Treat custom Apex concepts as provisional unless clearly justified.
13. Prefer battle-tested source patterns before inventing new structure.
14. Separate file format, execution layer, and AI reasoning layer.
15. Mark missing evidence as missing evidence, not as a design gap.

---

## 8. Starting thesis to test, not assume

Test this thesis against the evidence:

```
starting_thesis:  Apex_PM_KB_PD_should_be:    - local_file_first    - Claude_Code_native    - Markdown_plus_YAML_for_human_and_AI_readability    - deterministic_scripts_for_state_queries_and_validation    - Claude_reasoning_for_synthesis_prioritization_and_ambiguity    - public_native_terminology_first    - custom_Apex_vocabulary_minimal  likely_pattern_sources:    project_management:      main_candidates:        - CCPM        - Backlog.md        - Task Master      expected_result: "Possibly one main baseline plus supporting imports."    knowledge_base:      main_candidates:        - llm-wiki-main        - llm-wiki-skill-main      expected_result: "Likely borrow index/schema/source-ingestion/update-log patterns."    product_development:      main_candidates:        - CCPM        - CrewAI task design grammar        - Backlog.md task format      expected_result: "Likely synthesize spec/task/acceptance/test/done grammar."    continuity_and_safety:      main_candidates:        - GSD Core        - planning-with-files      expected_result: "Borrow session handoff and persistent progress logging, not full PM spine."
```

Your job is to prove, disprove, or refine this thesis.

---

## 9. Final instruction

Think deeply. Prefer precise comparison over broad summary. The goal is not to be exhaustive for its own sake; the goal is to produce the clearest next architectural decision for Apex PM/KB/PD.

When in doubt, choose the path that is:

1. simpler,
2. more repo-native,
3. more Claude Code–native,
4. more deterministic where determinism is possible,
5. more aligned with public/native terminology,
6. easier to validate before file generation.