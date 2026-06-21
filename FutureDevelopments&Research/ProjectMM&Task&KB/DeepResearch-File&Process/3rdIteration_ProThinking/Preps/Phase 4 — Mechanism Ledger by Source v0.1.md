# Phase 4 Complete — Mechanism Ledger by Source v0.1

**Scope executed:** extracted reusable mechanisms from the local files read in Phase 3.  
**Scope not executed:** no package generation, no repo writes, no final process coverage table yet.

**Verdict:** `PHASE_4_PASS_FOR_RESOLVED_SOURCES_WITH_MISSING_SOURCE_CAVEATS`

---

## 0. Classification key

|Label|Meaning|
|---|---|
|**COPY**|Mechanism can be carried into Apex with only naming/path adjustment.|
|**ADAPT**|Mechanism is strong, but must be changed for Apex constraints such as Python-only scripts, H1 status enum, or local-only repo operation.|
|**CONCEPT**|Useful design principle, but not enough direct implementation detail to copy.|
|**OMIT**|Do not use for Apex v1.|

---

## 1. CCPM mechanisms — S1a/S1b/S1c

|Mechanism ID|Mechanism|Classification|Extraction|
|---|---|---|---|
|**M-S1-01**|Five-phase PM lifecycle: Plan → Structure → Sync → Execute → Track|**ADAPT**|Strong PM control spine. CCPM defines phases for requirements capture, epic/task decomposition, GitHub sync, execution, and tracking. Apex should adapt the lifecycle, but not copy the GitHub Issues/worktree coupling.|
|**M-S1-02**|Epic → numbered task-file decomposition|**ADAPT**|CCPM converts epics into sequential task files and explicitly separates task creation by type and parallelization strategy. Apex can reuse the decomposition grammar, but should write into `apex-meta/` structures, not CCPM’s original `.claude/epics/` runtime.|
|**M-S1-03**|Task frontmatter + Markdown body sections|**ADAPT**|The task file format has frontmatter for `name`, `status`, `depends_on`, `parallel`, `conflicts_with`, and body sections for Description, Acceptance Criteria, Technical Details, Dependencies, Effort Estimate, and Definition of Done. Apex should preserve the general structure but normalize to H1/H3 locks.|
|**M-S1-04**|Dependency semantics: `depends_on`, `parallel`, `conflicts_with`, circular-dependency error|**COPY / ADAPT**|`depends_on` should be copied directly because it matches H3. `parallel` and `conflicts_with` are useful optional fields. Circular dependency rejection should be copied as a deterministic validation rule.|
|**M-S1-05**|Script-first tracking for deterministic reads|**ADAPT**|CCPM explicitly routes status, standup, in-progress, next, blocked, search, and validation to scripts instead of LLM reconstruction. Apex should copy the rule but port Bash script expectations to Python-only scripts.|
|**M-S1-06**|Script failure behavior: run first, interpret after|**COPY**|The rule is directly reusable: do not guess script output; run the deterministic script first, then explain errors or interpret output only when needed.|

**CCPM decision:** best source for **decomposition, dependency metadata, and deterministic status/query discipline**. Use as a structural baseline, not as a runtime clone.

---

## 2. Backlog.md mechanisms — S2a/S2b/S2c

|Mechanism ID|Mechanism|Classification|Extraction|
|---|---|---|---|
|**M-S2-01**|Markdown task as YAML frontmatter + body|**ADAPT**|The concrete task file uses YAML frontmatter for identity/status/labels/dependencies/priority and Markdown sections for description and acceptance criteria. Apex should reuse this hybrid record style with H1 status values.|
|**M-S2-02**|Rich task schema fields|**ADAPT**|Backlog’s task interface includes dependencies, references, documentation, modified files, implementation plan/notes, comments, final summary, acceptance criteria, DoD, parent tasks, subtasks, priority, branch, source, and status-change hook. Apex should import the field ideas selectively, not the full TypeScript model.|
|**M-S2-03**|Create/update input separation|**COPY / ADAPT**|Backlog distinguishes create fields from update operations, including add/remove/check/uncheck operations for criteria and DoD. Apex should copy this as a mutation pattern for deterministic update scripts.|
|**M-S2-04**|Parser maps Markdown into typed task object|**ADAPT**|The parser normalizes frontmatter and maps frontmatter/body sections into task objects, including priority validation, acceptance criteria, DoD, comments, dependencies, and subtasks. Apex should reimplement this idea in Python.|
|**M-S2-05**|Structured acceptance criteria and Definition of Done extraction|**COPY / ADAPT**|The mechanism of parsing AC/DoD as structured checklist objects is highly reusable for PD and validation flows, but should be expressed in Apex’s schema and Python utilities.|

**Backlog decision:** best source for **repo-resident Markdown task records and mutation-friendly task fields**.

---

## 3. Task Master mechanisms — S3a/S3b/S3c

|Mechanism ID|Mechanism|Classification|Extraction|
|---|---|---|---|
|**M-S3-01**|JSON task schema with dependencies, priority, details, test strategy, subtasks|**ADAPT**|Task Master’s documented schema is strong for deterministic task graph computation. Apex should adapt the fields while keeping Markdown/YAML as the human-readable storage layer.|
|**M-S3-02**|Individual task-file projection from task data|**CONCEPT**|The task-file format is simple and useful as a projection view, but too thin compared with CCPM/Backlog task bodies.|
|**M-S3-03**|Complexity analysis → expansion prompt flow|**CONCEPT**|Task Master’s complexity report and expansion flow can inspire future PD planning, but it depends on a larger Task Master runtime. Do not copy in v1.|
|**M-S3-04**|Next-task algorithm: completed set → eligible subtasks → dependency satisfaction → priority/dependency/id sort|**ADAPT**|This is the strongest deterministic “what next?” mechanism. Apex should port it to Python, using H1 status values and H7 priority/urgency rules.|
|**M-S3-05**|Prefer eligible subtasks inside in-progress parent work|**ADAPT**|The algorithm first selects eligible subtasks under in-progress parents before falling back to top-level tasks. This is useful for Apex focus continuity.|
|**M-S3-06**|Task-manager module boundary|**CONCEPT**|The module boundary shows a coherent function set around PRD parsing, task updates, subtasks, complexity, status, and list operations, but the aggregator file itself is thin.|

**Task Master decision:** best source for **deterministic next-task selection and dependency eligibility logic**, not for Apex storage format.

---

## 4. planning-with-files mechanisms — S4a/S4b

|Mechanism ID|Mechanism|Classification|Extraction|
|---|---|---|---|
|**M-S4-01**|Three-file session memory: `task_plan.md`, `findings.md`, `progress.md`|**COPY / ADAPT**|Directly matches Apex handoff/session needs. The source assigns task phases to `task_plan.md`, research/discoveries to `findings.md`, and session/test log to `progress.md`.|
|**M-S4-02**|Read plan/progress before each turn|**COPY**|The active-session rule says to read plan and progress files before decisions. This is directly reusable for Apex session continuity.|
|**M-S4-03**|2-action persistence rule|**ADAPT**|Useful for long research phases, but in Apex it should become a “periodic evidence persistence” rule rather than a universal hard runtime rule.|
|**M-S4-04**|Update after act + log all errors|**COPY**|Strong safety rule: after a phase, mark status, log errors, and note created/modified files. Every error must be recorded to avoid repetition.|
|**M-S4-05**|Topic handoff file for long-running context|**COPY / ADAPT**|For long or multi-session topics, move durable detail into a handoff file and keep progress concise. This maps cleanly to Apex `next-session.md` / handoff files.|

**planning-with-files decision:** best source for **session continuity, handoff discipline, and anti-context-loss behavior**.

---

## 5. llm-wiki mechanisms — S6a + S6b substitute

|Mechanism ID|Mechanism|Classification|Extraction|
|---|---|---|---|
|**M-S6-01**|Compile raw sources into persistent cross-linked wiki|**ADAPT**|Strong KB model: raw material is transformed into durable wiki knowledge, with the human steering and auditing while the LLM handles writing/cross-referencing/bookkeeping.|
|**M-S6-02**|Five KB operations: compile, ingest, query, lint, audit|**ADAPT**|The operation set is reusable for Apex KB management. It should be mapped into Python-assisted index/query/lint plus Claude-assisted synthesis/audit.|
|**M-S6-03**|KB directory layout: `CLAUDE.md`, `log/`, `audit/`, `raw/`, `wiki/`, `outputs/`|**ADAPT**|Strong conceptual layout. Apex should adapt it to `apex-meta/registry`, `source`, `handoff`, and project KB paths rather than copying the exact tree wholesale.|
|**M-S6-04**|`CLAUDE.md`/schema file as session-start authority|**CONCEPT / ADAPT**|The local schema/config authority idea is useful. Exact Claude-specific naming may need harmonization with Apex’s existing repo conventions.|
|**M-S6-05**|Divide-and-conquer page splitting|**COPY / ADAPT**|Avoid fat KB pages; split complex topics into index + aspect pages. This is directly useful for Apex KB entity/concept pages.|
|**M-S6-06**|Raw file policy + large-binary pointer files|**COPY**|This is directly useful for keeping Apex git-friendly: store small text, represent large binaries through pointer files.|
|**M-S6-07**|Audit inbox as human feedback surface|**COPY / ADAPT**|Human feedback files with severity/target and resolution logging are highly compatible with Apex operator-gated correction loops.|
|**M-S6-08**|Scaffold script creates KB directory tree|**CONCEPT**|The script shows deterministic tree creation for `raw`, `wiki`, `log`, `audit`, and `outputs`, but it is not the missing index rebuild logic.|

**llm-wiki decision:** best source for **KB layout, source/raw separation, audit feedback, and page-splitting discipline**. Exact `update-index.py` mechanism remains missing.

---

## 6. CrewAI substitute mechanisms — S8a-substitute

|Mechanism ID|Mechanism|Classification|Extraction|
|---|---|---|---|
|**M-S8-01**|Task contract requires description, expected output, responsible agent|**COPY / ADAPT**|Very strong PD/task-design grammar. Apex tasks should always define purpose, expected output, and responsible actor/profile/skill.|
|**M-S8-02**|Context dependencies as explicit task inputs|**ADAPT**|CrewAI models context as outputs from other tasks. Apex can adapt this into `source_context_refs`, `depends_on`, or handoff references.|
|**M-S8-03**|Structured outputs via JSON/Pydantic-style models|**CONCEPT / ADAPT**|Useful design idea for Apex validation contracts, but not directly copied unless Python validators are built.|
|**M-S8-04**|`output_file` as durable task result target|**COPY / ADAPT**|Strong fit for Apex: every durable operation should know its output artifact path before execution.|
|**M-S8-05**|Tool-limiting and named input files|**ADAPT**|Useful for future skill safety: tasks should declare allowed tools/resources and named input files.|
|**M-S8-06**|`human_input` flag for review gate|**COPY / ADAPT**|Directly useful as an operator-gate marker in Apex task/process records.|

**CrewAI substitute decision:** best source for **task contract grammar and explicit output/context/review fields**, but it is a substitute, not the original skill-format source.

---

## 7. Missing-source mechanism status

|Source|Mechanism expected|Current classification|
|---|---|---|
|**S5a/S5b/S5c Kanban**|Card fields, `blocked_by`, due-date urgency, blocked/list scripts|**NO_LOCAL_READ_EVIDENCE**|
|**S6b exact `update-index.py`**|Index rebuild / drift detection|**NO_LOCAL_READ_EVIDENCE**|
|**S7a OpenClaw TaskFlow**|Durable taskflow lifecycle/state machine|**NO_LOCAL_READ_EVIDENCE**|
|**S8b CrewAI getting-started skill**|Skill/task config examples|**NO_LOCAL_READ_EVIDENCE**|
|**S9a/S9b Hermes governance**|Skills hub / skills guard / trust model|**NO_LOCAL_READ_EVIDENCE**|

These cannot be used as grounded mechanism sources in Phase 5 unless they are resolved and read later.

---

## 8. Cross-source mechanism synthesis

|Apex need|Strongest source mechanism|Decision|
|---|---|---|
|**Task record format**|Backlog task record + CCPM task sections|**ADAPT**|
|**Epic/project decomposition**|CCPM Structure|**ADAPT**|
|**Dependency model**|CCPM `depends_on` + Task Master eligibility|**ADAPT**|
|**Next-task selection**|Task Master `findNextTask`|**ADAPT into Python**|
|**Blocked detection**|CCPM tracking concept; Kanban missing|**PARTIAL / needs source or custom Python**|
|**Status/query/report scripts**|CCPM script-first rule|**ADAPT into Python**|
|**Session handoff**|planning-with-files|**COPY / ADAPT**|
|**KB layout**|llm-wiki|**ADAPT**|
|**KB audit feedback**|llm-wiki audit directory|**COPY / ADAPT**|
|**Task contract / expected output**|CrewAI task fields|**ADAPT**|
|**Human review gate**|CrewAI `human_input` + Apex operator gates|**ADAPT**|
|**Index rebuild**|llm-wiki expected source missing|**BLOCKED / custom or re-resolve**|
|**Governance / skill trust**|Hermes expected source missing|**BLOCKED / later**|

---

## 9. Phase 4 gate verdict

```
phase_4_verdict:  status: PASS_FOR_RESOLVED_MECHANISMS  strongest_copy_or_adapt_sources:    - CCPM:        use_for:          - lifecycle          - decomposition          - dependency metadata          - script-first rule    - Backlog:        use_for:          - markdown_task_schema          - create_update_mutation_pattern          - parser_mapping    - Task_Master:        use_for:          - deterministic_next_task_algorithm          - dependency_satisfaction_logic    - planning_with_files:        use_for:          - session_handoff          - progress_findings_task_plan_trinity          - error_persistence    - llm_wiki:        use_for:          - kb_layout          - raw_vs_wiki_split          - audit_feedback_surface    - CrewAI_task_py:        use_for:          - task_contract_fields          - expected_output          - context_refs          - output_file          - human_review_flag  unresolved_mechanisms:    - kanban_blocked_card_scripts    - exact_llm_wiki_update_index    - OpenClaw_taskflow    - CrewAI_skill_examples    - Hermes_governance_guard
```

**Next:** Phase 5 should map these extracted mechanisms across all 20 processes — PM1–PM8, KB1–KB6, PD1–PD6 — and mark any process as `FULL`, `PARTIAL`, or `BLOCKED_BY_MISSING_SOURCE`.