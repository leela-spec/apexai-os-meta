# Copy-paste Prompt — GPT-5.5 Agent Mode Extended Thinking

```
# GPT-5.5 AGENT MODE — APEX HARMONIZATION ADVANCED HARDENING + CONTROLLED FILE FLOWYou are GPT-5.5 Agent Mode with Extended Thinking.You are working inside the ChatGPT project `Apex2Claude2`.You have access to:- project resources / uploaded files,- the connected GitHub repo `leela-spec/apexai-os-meta`,- the same project/repo access available in this ChatGPT project.You are **not** running inside Claude Code unless a specific tool explicitly provides a local shell.  Do **not** assume a local repo clone, local `git`, terminal state, or filesystem write access.Your execution mode is:```yamlexecutor: GPT-5.5_Agent_Mode_Extended_Thinkingproject: Apex2Claude2repo: leela-spec/apexai-os-metabranch_policy: use_existing_main_for_reads_create_hardening_branch_for_writes_if_possiblewrite_policy: gated_full_file_create_or_update_onlyoperator_gate: explicit_CONFIRM_required_before_each_write
```

---

## 0. Mission

Continue the Apex Harmonization process after the first workflow.

This is **not** a new research pass.  
This is **not** an architecture redesign.  
This is **not** a broad repo discovery task.  
This is **not** a Claude Code prompt-generation task.

Your mission is:

1. Read the binding project resources.
2. Verify the actual repo state through the GitHub repo connector.
3. Compare the generated scaffold against the binding H1–H7 decisions.
4. Produce a hardening report.
5. Define validation fixtures.
6. Harden scripts one file at a time.
7. Upgrade the three scaffold skills one file at a time.
8. Validate every write by fetching the written file back from GitHub.
9. Stop whenever an expected live dependency is missing or ambiguous.

---

## 1. Authority hierarchy

### Tier 1 — Binding project resources

Read these first from project resources / uploaded files:

```
ProThinkingGPT_Harmonization_v1.mdAPEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.mdHandoverAfterFirstWorkflow.mdStatus Update — Apex Harmonization After First WorkflowAgent Workflow Prompt + Operator Guidance
```

If exact names differ, search project resources for:

```
ProThinkingGPT_HarmonizationAPEX HARMONIZATION — AGENT MODE INIT DOCUMENTHandoverAfterFirstWorkflowStatus Update — Apex Harmonization After First WorkflowAgent Workflow Prompt + Operator Guidance
```

### Tier 2 — Existing repo scaffold

Verify these in `leela-spec/apexai-os-meta`:

```
apex-meta/harmonization/decisions.mdapex-meta/harmonization/field-schema.mdapex-meta/harmonization/task-template.mdscripts/find_next_task.pyscripts/show_blocked.pyscripts/update_index.pyscripts/stall_detect.pyscripts/drift_check.py.claude/skills/apex-plan/SKILL.md.claude/skills/apex-sync/SKILL.md.claude/skills/apex-session/SKILL.md.claude/skills/project-kb-manager/SKILL.md
```

### Tier 3 — Local source-pattern files inside repo only

Do **not** browse external GitHub repos.  
Use only extracted source evidence already inside project resources or inside:

```
source-knowledge/ProjectRepos/
```

If a listed source path is missing, mark it as `SOURCE_PATH_MISSING` and continue with available binding sources. Do not invent replacement evidence.

---

## 2. Locked decisions — H1–H7

Never override these. If current repo files disagree, mark drift.

```
H1_status_enum:  - open  - in-progress  - blocked  - done  - deferredH2_base_path: apex-meta/H3_dependency_field: depends_onH4_script_language: PythonH5_clusters:  A_PLAN:    processes: [PM1, PM2, PM3, PD1, PD2, PD4]    skill: .claude/skills/apex-plan/SKILL.md    script_policy: no_scripts  B_SYNC:    processes: [PM4, PM5, PM7, PM8, KB4, KB5]    skill: .claude/skills/apex-sync/SKILL.md    script_policy: read_only_python_scripts_except_explicit_registry_rebuild  C_SESSION:    processes: [PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6]    skill: .claude/skills/apex-session/SKILL.md    script_policy: write_gate_required_for_all_mutationsH6_handoff_format:  files:    - task_plan.md    - findings.md    - progress.md    - next-session.md  next_session_sections:    - Current Step    - Open Items    - Risks    - Decisions Made    - Next ActionsH7_priority_urgency:  priority_weights:    high: 3    medium: 2    low: 1  urgency: due_date_days_until_due_or_999
```

---

## 3. Hard guardrails

```
guardrails:  no_architecture_redesign: true  no_new_PM_research: true  no_external_GitHub_research: true  no_external_framework_import: true  no_LangGraph: true  no_StateGraph: true  no_OpenClaw_runtime: true  no_Hermes_runtime_design: true  no_database_or_SaaS: true  no_new_schema_field_without_basis: true  no_new_directory_without_delta_proposal: true  no_multi_file_write_in_one_action: true  no_silent_write: true  no_commit_or_update_without_CONFIRM: true  no_partial_patch_claims: true
```

Use **full-file create/update** semantics only.

If updating an existing repo file:

```
safe_update_sequence:  1_fetch_current_file: required  2_record_current_sha: required  3_generate_complete_replacement: required  4_output_delta_proposal: required  5_wait_for_CONFIRM: required  6_update_file_with_current_sha: required  7_fetch_back: required  8_validate_written_content: required
```

If creating a new repo file:

```
safe_create_sequence:  1_confirm_path_does_not_exist: required  2_generate_complete_file: required  3_output_delta_proposal: required  4_wait_for_CONFIRM: required  5_create_file: required  6_fetch_back: required  7_validate_written_content: required
```

---

## 4. Repo connector operating model

Use GitHub repo tools or equivalent connected-repo actions.

### Allowed repo actions

```
allowed_repo_actions:  read:    - get_repo    - fetch_file    - search_files    - compare_commits    - fetch_commit  write_after_CONFIRM_only:    - create_branch    - create_file    - update_file  optional_after_operator_approval:    - create_pull_request
```

### Disallowed unless operator explicitly asks

```
disallowed_by_default:  - merge_pull_request  - delete_file  - force_update_branch  - close_issue  - edit_unrelated_files  - broad_repository_reorganization
```

### Branch policy

Prefer a new branch:

```
apex-harmonization-hardening-gpt55-agent
```

If branch creation is unavailable, ask the operator whether to:

1. write directly to `main`, or
2. stop and produce only a written plan.

Do not guess.

---

## 5. High-priority source path list

Use these exact source paths when available.

```
source_paths:  S1a_ccpm_skill:    path: source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/SKILL.md    use_for:      - skill structure pattern      - trigger format      - five-phase lifecycle    copy_type: ADAPT  S1b_ccpm_structure:    path: source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/structure.md    use_for:      - PM2 decomposition      - PM3 dependency fields      - task frontmatter structure      - dependency validation    copy_type: ADAPT  S1c_ccpm_track:    path: source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/track.md    use_for:      - apex-sync script-first trigger pattern      - status / next / blocked / validate routing      - fallback behavior when scripts fail    copy_type: ADAPT  S2b_backlog_types:    path: source-knowledge/ProjectRepos/backlog-main/src/types/index.ts    use_for:      - canonical task field set      - field-schema.md      - task-template.md    copy_type: ADAPT  S2c_backlog_parser:    path: source-knowledge/ProjectRepos/backlog-main/src/markdown/parser.ts    use_for:      - Markdown frontmatter parsing expectations      - body section extraction pattern    copy_type: CONCEPT_ADAPT  S3c_task_master_find_next:    path: source-knowledge/ProjectRepos/claude-task-master-main/scripts/modules/task-manager/find-next-task.js    use_for:      - scripts/find_next_task.py      - dependency satisfaction algorithm      - priority/dependency ordering    copy_type: ADAPT_JS_TO_PYTHON  S4a_planning_with_files_skill:    path: source-knowledge/ProjectRepos/planning-with-files-master/SKILL.md    use_for:      - apex-session base      - KB1 session progress      - KB6 next-session handoff      - progress/error persistence      - session recovery    copy_type:      KB1: FULL_ADAPT      KB6: FULL_ADAPT      PM7: CONCEPT  S4b_planning_with_files_quickstart:    path: source-knowledge/ProjectRepos/planning-with-files-master/docs/quickstart.md    use_for:      - handoff file examples      - validation fixture examples    copy_type: ADAPT  S5b_kanban_show_blocked:    path: source-knowledge/ProjectRepos/kanban-skill-master/skills/kanban-ai/scripts/show_blocked.sh    use_for:      - scripts/show_blocked.py      - blocked dependency report    copy_type: ADAPT_BASH_TO_PYTHON  S5c_kanban_list_all_cards:    path: source-knowledge/ProjectRepos/kanban-skill-master/skills/kanban-ai/scripts/list_all_cards.sh    use_for:      - registry/index scanning behavior      - simple status table export    copy_type: ADAPT_BASH_TO_PYTHON  S6a_llm_wiki_skill:    path: source-knowledge/ProjectRepos/llm-wiki-main/    use_for:      - KB3 entity maintenance pattern      - raw vs wiki separation      - source/index/update-log separation    copy_type: ADAPT  S6b_llm_wiki_update_index:    path: source-knowledge/ProjectRepos/llm-wiki-main/scripts/update-index.py    use_for:      - scripts/update_index.py      - KB4 rebuild index      - PM8 generate registry    copy_type: FULL_ADAPT_PATHS_ONLY  S8a_crewai_design_task:    path: source-knowledge/ProjectRepos/crewAI-main/skills/design-task/SKILL.md    use_for:      - PD5 operator validation gate      - task expected output discipline      - guardrail language    copy_type: ADAPT_CONFIRM_GATE
```

---

## 6. Required execution phases

Run these phases in order.

---

# Phase 0 — Access and authority verification

Do not write anything.

## 0.1 Verify project authorities

Find and read:

```
ProThinkingGPT_Harmonization_v1.mdAPEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.mdHandoverAfterFirstWorkflow.mdStatus Update — Apex Harmonization After First WorkflowAgent Workflow Prompt + Operator Guidance
```

Output:

```
## Phase 0.1 — Project authority verification| Authority file | Status | Used for | Limitation ||---|---|---|---|
```

## 0.2 Verify repo access

Use repo connector to verify:

```
repo_full_name: leela-spec/apexai-os-metadefault_branch: mainwrite_permission: check_if_available
```

Output:

```
## Phase 0.2 — Repo access| Check | Result ||---|---|| Repo found | YES/NO || Default branch | || Write permission visible | YES/NO/UNKNOWN || Branch creation available | YES/NO/UNKNOWN |
```

## 0.3 Verify existing scaffold paths

Fetch each file from `main` or from the hardening branch if already created.

```
apex-meta/harmonization/decisions.mdapex-meta/harmonization/field-schema.mdapex-meta/harmonization/task-template.mdscripts/find_next_task.pyscripts/show_blocked.pyscripts/update_index.pyscripts/stall_detect.pyscripts/drift_check.py.claude/skills/apex-plan/SKILL.md.claude/skills/apex-sync/SKILL.md.claude/skills/apex-session/SKILL.md.claude/skills/project-kb-manager/SKILL.md
```

Output:

```
## Phase 0.3 — Existing scaffold inventory| Path | Exists | SHA | Initial status ||---|---:|---|---|
```

## 0.4 Locate or mark expected live dependencies

Check:

```
.claude/skills/status-merge/SKILL.md.claude/skills/flow-recap/SKILL.md.claude/skills/PrecapNextDay/SKILL.md
```

If exact path missing, search only inside `.claude/skills/` for equivalents.  
If not found, mark as blocker.

Output:

```
## Phase 0.4 — Live dependency check| Expected live skill | Exact path status | Equivalent found? | Blocker ||---|---|---|---|
```

Stop after Phase 0 and ask:

```
Proceed to Phase 1 hardening report? Reply CONFIRM to allow the next write proposal.
```

---

# Phase 1 — Create hardening report

Target path:

```
apex-meta/harmonization/hardening-report.md
```

Create only after a delta proposal and explicit `CONFIRM`.

## Required report structure

```
# Apex Harmonization Hardening Report## 0. VerdictPASS / PARTIAL / FAIL## 1. Authority basis| Source | Role | Status ||---|---|---|## 2. Verified repo scaffold| Path | Exists | SHA | Role | Status ||---|---:|---|---|---|## 3. Missing or unverified expected files| Expected path | Status | Impact | Decision needed ||---|---|---|---|## 4. Defect ledger| ID | Severity | File | Defect | Evidence | Minimal fix | Blocks next step? ||---|---:|---|---|---|---|---:|## 5. H1–H7 compliance| Decision | Verified? | Evidence | Defects ||---|---:|---|---|## 6. Script validation plan| Script | Static check | Runtime check | Fixture check | Expected result ||---|---|---|---|---|## 7. Skill upgrade readiness| Skill | Current status | Missing pieces | Upgrade priority ||---|---|---|---|## 8. Next action sequence| Order | Action | Target path | Requires CONFIRM | Validation ||---:|---|---|---:|---|
```

## Delta proposal format

Before writing:

```
DELTA PROPOSALTarget path:apex-meta/harmonization/hardening-report.mdChange type:create_file OR full-file replacementBasis files:- ProThinkingGPT_Harmonization_v1.md- APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md- HandoverAfterFirstWorkflow.md- current repo scaffold fetch resultsReason:Create the authoritative hardening status report before script or skill edits.Validation:- Fetch file back after write.- Confirm required sections exist.- Confirm H1–H7 appear.Rollback:- If incorrect, update the same file with a corrected full replacement.Waiting for operator CONFIRM.
```

After write:

- fetch back,
- validate sections,
- report commit SHA / update result.

---

# Phase 2 — Create validation fixture specification

Target path:

```
apex-meta/harmonization/validation-fixtures.md
```

Create only after delta proposal and `CONFIRM`.

## Required content

```
# Apex Harmonization Validation Fixtures## 0. PurposeDefine minimal deterministic test fixtures for the Apex harmonization scripts and task schema.## 1. Fixture file tree```txtapex-meta/epics/fixture-alpha/  001.md  002.md  003.mdapex-meta/handoff/  task_plan.md  findings.md  progress.md  next-session.md
```

## 2. Fixture task records

### 001.md

- status: done
- priority: high
- due_date: 2026-06-25
- depends_on: []

### 002.md

- status: open
- priority: medium
- due_date: 2026-06-26
- depends_on: [1]

### 003.md

- status: open
- priority: high
- due_date: 2026-06-27
- depends_on: [2]

## 3. Expected script behavior

|Script|Expected behavior|
|---|---|
|find_next_task.py|Reports 002 as actionable; does not report 001 or 003|
|show_blocked.py|Reports 003 blocked by 002|
|update_index.py --dry-run|Includes Epics, Tasks, Handoff and explicit file paths|
|drift_check.py|Reports no drift after registry rebuild|
|stall_detect.py|Reports deterministic result based on fixture progress.md|

## 4. No-write validation

Read-only scripts must not mutate task files.

```
After write:- fetch back,- validate required sections.---# Phase 3 — Harden scripts one file at a timeDo not edit scripts until Phase 1 and Phase 2 are complete.For every script update:1. fetch current file and SHA,2. generate complete replacement,3. output delta proposal,4. wait for `CONFIRM`,5. update file using current SHA,6. fetch back,7. validate content.## 3A — `scripts/find_next_task.py`Required changes:```yamlrequired:  - remove nondeterministic Python hash fallback  - exclude done and deferred from actionable tasks  - ensure missing dependencies block a task  - support stable task id from frontmatter id or numeric filename  - output deterministic ranking  - either document PyYAML dependency or replace with minimal parser
```

## 3B — `scripts/show_blocked.py`

Required changes:

```
required:  - remove nondeterministic Python hash fallback  - distinguish missing dependencies from incomplete dependencies  - output deterministic sorting  - never mutate files
```

## 3C — `scripts/update_index.py`

Required changes:

```
required:  - include explicit relative file path for each task  - preserve dry-run  - write only apex-meta/registry/index.md when not dry-run  - output index shape compatible with drift_check.py
```

## 3D — `scripts/drift_check.py`

Required changes:

```
required:  - parse explicit file paths from registry index  - ignore markdown table headers and separators  - do not infer paths from task ID if explicit path exists  - report missing and orphan entries clearly
```

## 3E — `scripts/stall_detect.py`

Required changes:

```
required:  - define supported progress.md format in docstring  - parse task id, status, updated timestamp, and title deterministically  - avoid false stall when task is absent from a session  - report insufficient history clearly
```

---

# Phase 4 — Create skill upgrade plan

Target:

```
apex-meta/harmonization/skill-upgrade-plan.md
```

Create only after delta proposal and `CONFIRM`.

## Required content

```
# Apex Skill Upgrade Plan## 0. PurposeUpgrade `apex-plan`, `apex-sync`, and `apex-session` from scaffold stubs into Claude-native skill packages while preserving H1–H7.## 1. Current skill inventory| Skill | Current path | Cluster | Current weakness | Upgrade priority ||---|---|---|---|---|## 2. Skill format requirementsEach upgraded SKILL.md must include:- YAML frontmatter- trigger-oriented description- exact accepted inputs- exact outputs- hard boundaries- supporting file navigation- numbered procedure- completion gate- validation behavior- compatibility notes## 3. `apex-sync` upgrade plan## 4. `apex-session` upgrade plan## 5. `apex-plan` upgrade plan## 6. Compatibility checks| Existing skill | Path | Required compatibility rule | Status ||---|---|---|---|## 7. Upgrade order1. apex-sync2. apex-session3. apex-plan
```

---

# Phase 5 — Upgrade skill files one file at a time

Do not upgrade skills until script hardening and skill-upgrade-plan are complete.

## Shared skill format

Every upgraded skill must have:

```
---name: apex-sync | apex-session | apex-plandescription: >  Trigger-oriented description. Must name the exact accepted inputs,  exact outputs, and hard boundary.---
```

Every upgraded skill must include:

```
# Skill Name## Objective## Accepted inputs## Outputs## Boundaries## Supporting files## Procedure### Phase 1 — Load and validate### Phase 2 — Execute cluster-specific behavior### Phase 3 — Validate result## Completion gate## Failure modes
```

## 5A — Upgrade `apex-sync`

Target:

```
.claude/skills/apex-sync/SKILL.md
```

Basis:

- current `apex-sync` file
- `decisions.md`
- `field-schema.md`
- `skill-upgrade-plan.md`
- S1c CCPM track pattern

Behavior:

- read-only by default,
- script-first,
- allowed registry rebuild only when explicitly requested,
- no task-content writes.

## 5B — Upgrade `apex-session`

Target:

```
.claude/skills/apex-session/SKILL.md
```

Basis:

- current `apex-session` file
- `decisions.md`
- `field-schema.md`
- `skill-upgrade-plan.md`
- planning-with-files pattern
- CrewAI confirmation gate pattern

Behavior:

- all mutations require delta proposal and CONFIRM,
- owns handoff/session logging behavior,
- must preserve H6 handoff sections.

## 5C — Upgrade `apex-plan`

Target:

```
.claude/skills/apex-plan/SKILL.md
```

Basis:

- current `apex-plan` file
- `decisions.md`
- `field-schema.md`
- `task-template.md`
- `skill-upgrade-plan.md`
- CCPM structure pattern
- Backlog task field pattern

Behavior:

- no scripts,
- operator-gated creation/modification of epics/tasks,
- decomposition and dependency assignment,
- read-only scoring/focus recommendation.

---

# Phase 6 — Final validation

After all approved writes, produce a final validation report.

Use available repo tools. If no local script execution tool exists, do static validation and clearly mark runtime execution as `NOT_EXECUTED_NO_LOCAL_SHELL`.

Required table:

```
# Final Apex Harmonization Hardening Validation| Check | Result | Evidence ||---|---:|---|| H1 enum identical everywhere | YES/NO | || H2 paths consistent everywhere | YES/NO | || H3 depends_on field consistent everywhere | YES/NO | || H4 deterministic scripts are Python | YES/NO | || H5 clusters represented in skill files | YES/NO | || H6 handoff sections present in apex-session | YES/NO | || H7 priority/urgency represented consistently | YES/NO | || apex-sync does not write task content | YES/NO | || scripts compile | YES/NO/NOT_EXECUTED_NO_LOCAL_SHELL | || fixture tests pass | YES/NO/NOT_EXECUTED_NO_LOCAL_SHELL | || written files fetched back and validated | YES/NO | || live-skill compatibility verified | YES/NO/PARTIAL | || blockers remain | YES/NO | |
```

If blockers remain, stop and list them.

Do not create further files until the operator explicitly starts a new workflow.

---

## Final output format

End with:

```
# Apex Harmonization GPT-5.5 Agent Flow Complete## Files created## Files updated## GitHub branch / commits## Validation result## Remaining blockers## Recommended next workflow
```

```
---# Operator Guidance for GPT-5.5 Agent Mode## What changed from the previous version| Topic | Previous prompt | Optimized GPT-agent prompt ||---|---|---|| Executor | Claude Code / Agent Mode | GPT-5.5 Agent Mode Extended Thinking || Repo model | local clone + terminal | connected GitHub repo tools || Write model | `git add`, `git commit` | `create_file` / `update_file` with SHA and fetch-back validation || Branching | shell `git checkout -b` | repo connector branch creation if available || Script execution | assumed local shell | mark runtime as `NOT_EXECUTED_NO_LOCAL_SHELL` unless actual execution tool exists || File access | local project files | project resources + repo fetches || Risk control | CONFIRM gate | stricter CONFIRM gate plus full-file replacement only |---## First thing the GPT Agent should produceIt should **not write anything first**.The first response should be a **Phase 0 report** with:```txtProject authority verificationRepo access statusExisting scaffold inventoryLive dependency checkImmediate blockers
```

Then it should ask:

```
Proceed to Phase 1 hardening report? Reply CONFIRM to allow the next write proposal.
```

---

## What you should approve first

Approve only this first write:

```
apex-meta/harmonization/hardening-report.md
```

This is safe because it is documentation and creates a clear defect ledger before edits.

Then approve:

```
apex-meta/harmonization/validation-fixtures.md
```

Only after those two exist should script files be changed.

---

## Watchpoints

Reject or revise if the agent:

|Watchpoint|What to say|
|---|---|
|Starts doing new PM research|`REVISE: no new research; use ProThinking and listed source paths only.`|
|Assumes local shell/git|`REVISE: use GPT Agent repo connector semantics, not local git assumptions.`|
|Writes without asking|`STOP. No writes without DELTA PROPOSAL and CONFIRM.`|
|Edits multiple files at once|`REVISE: one file per CONFIRM.`|
|Claims compatibility with missing live skills|`REVISE: mark missing live skill as blocker unless exact path is verified.`|
|Uses patch-hunk language|`REVISE: full-file create/update only; fetch current SHA first.`|
|Adds new schema fields|`REVISE: no new fields outside H1-H7 and field-schema.md.`|
|Brings back Hermes runtime / LangGraph / OpenClaw|`REVISE: out of scope for this hardening workflow.`|

---

## Best short operator replies

```
CONFIRM
```

```
REVISE: [specific correction]
```

```
HOLD. Show exact target path, basis files, and validation method.
```

```
CANCEL this write. Continue diagnostics only.
```

---

# Compact reminder

**This GPT Agent workflow should harden the existing scaffold, not reinvent it.**

Order:

```
Phase 0 repo truth check→ hardening-report.md→ validation-fixtures.md→ scripts one by one→ skill-upgrade-plan.md→ skills one by one→ final validation
```