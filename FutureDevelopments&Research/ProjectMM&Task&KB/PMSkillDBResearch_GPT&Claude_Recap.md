# Direct answer

There is **no single established PM/KB system** that Apex can copy wholesale and safely use as its full `project-kb-manager`.

The best answer is a **composed baseline**:

```yaml
recommended_apex_pm_kb_baseline:
  primary_pm_process_logic: CCPM
  primary_task_file_substrate: Backlog.md
  deterministic_execution_pattern: OpenClaw TaskFlow + local Python scripts
  task_contract_pattern: CrewAI task design
  future_state_machine_escalation: LangGraph
  session_continuity_reference: GSD Core
  long_task_safety_reference: planning-with-files
  file_format_convention: llms.txt-style Markdown + YAML frontmatter
```

Why: your actual need has **three layers**, and no one repo owns all three well.

|Layer|Apex needs|Best source|
|---|---|---|
|**PM logic**|define project → break into epics/chunks/tasks → determine next/blocked/status|**CCPM**|
|**State substrate**|repo-local Markdown task/project files|**Backlog.md**|
|**Execution reliability**|Python reads/writes/computes; Claude reasons only where needed|**OpenClaw + CrewAI patterns**|

This resolves the contradiction between the two research tracks: the earlier CCPM/Backlog research was strongest on **project-management structure**, while the later OpenClaw/CrewAI research was strongest on **Python + AI execution architecture**. The saved GPT recap itself says no exact community PM system was found and recommends a “layered import, not one spine” approach; it ranks OpenClaw and CrewAI for execution/task-contract patterns, not as full PM databases.

---

# Core decision

## Use **CCPM-lite + Backlog-style files + Python/Claude split**

```yaml
decision:
  do_not_clone_wholesale:
    - CCPM
    - Backlog.md
    - OpenClaw
    - CrewAI
    - LangGraph
  build_apex_from:
    - CCPM_plan_and_structure_logic
    - Backlog_markdown_task_file_grammar
    - OpenClaw_taskflow_lifecycle_pattern
    - CrewAI_task_contract_pattern
    - local_python_scripts_for_deterministic_operations
    - Claude_skill_for_reasoning
```

The reason this is not “custom invention” is that each layer uses a known external pattern:

- **CCPM:** gives the best existing Agent Skill PM flow: PRD/project definition → epic → tasks → status/next/blocked. Its README says it turns ideas into PRDs, PRDs into epics, epics into GitHub issues, with traceability; it is also an Agent Skill compatible with Claude Code and similar harnesses. ([GitHub](https://github.com/automazeio/ccpm "GitHub - automazeio/ccpm: Project management skill system for Agents that uses GitHub Issues and Git worktrees for parallel agent execution. · GitHub"))
    
- **Backlog.md:** gives the best repo-local Markdown task substrate. It supports CLI/Web/MCP workflows over the same Markdown files and can run filesystem-only without a Git dependency. ([GitHub](https://github.com/MrLesk/Backlog.md "GitHub - MrLesk/Backlog.md: Backlog.md - A tool for managing project collaboration between humans and AI Agents in a git ecosystem · GitHub"))
    
- **OpenClaw TaskFlow:** gives the best durable task-flow pattern: owner session, state bag, waits, child tasks, lifecycle, revision-checked mutations, and explicit separation between runtime state and business logic. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))
    
- **CrewAI task design:** gives a clean task contract: description, expected output, dependencies/context, structured output, guardrails, human review, and output files. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))
    

---

# Option ranking

|Rank|Option|Description|Fit|Use it how|
|--:|---|---|--:|---|
|**1**|**CCPM-lite + Backlog substrate + Python/Claude split**|Best hybrid architecture. CCPM provides PM decomposition. Backlog provides Markdown task grammar. Python handles deterministic state. Claude handles reasoning.|**92/100**|**Recommended baseline.**|
|**2**|**Backlog.md-first**|Use Backlog.md as the actual local PM layer, then add Apex reasoning around it.|**80/100**|Good if you want fastest usable local task database. Weak as planning brain.|
|**3**|**CCPM-first**|Use CCPM Agent Skill almost directly, stripping GitHub Issues/worktrees.|**76/100**|Good process logic, but risky because CCPM’s execution/status layer is GitHub Issues + worktrees.|
|**4**|**OpenClaw-first**|Use OpenClaw skills/TaskFlow as baseline.|**68/100**|Good execution model, but not a PM/KB system. Security surface too large.|
|**5**|**CrewAI/LangGraph-first**|Build Apex as a Python agent workflow app.|**63/100**|Powerful later, too much framework for v1.|

## Recommendation

Use **Option 1**.

Do **not** pick OpenClaw as the PM base. It is valuable because it has a skill ecosystem and local execution concepts, but OpenClaw itself is a full personal-assistant runtime, not a repo-native PM/KB system. Its own repo shows a local-first assistant, many channels, skills, tools, sandboxing, and workspace skill paths, but that is far broader than Apex needs. ([GitHub](https://github.com/openclaw/openclaw "GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way.  · GitHub"))

---

# What fits from each system

## 1. CCPM — import PM process logic

**Fit:** project decomposition and status flow.

CCPM’s public repo describes the chain: “ideas into PRDs, PRDs into epics, epics into GitHub issues,” and its workflow phases include Plan, Structure, Sync, Execute, and Track. The useful parts for Apex are **Plan**, **Structure**, and **Track**; the GitHub sync/execution parts should be rejected for v1. ([GitHub](https://github.com/automazeio/ccpm "GitHub - automazeio/ccpm: Project management skill system for Agents that uses GitHub Issues and Git worktrees for parallel agent execution. · GitHub"))

|CCPM part|Import?|Apex adaptation|
|---|--:|---|
|PRD / requirement capture|**Partial**|Rename to `project_intake` or `project_scope`, not “Project Brief” if that is rejected for v1.|
|Epic decomposition|**Yes**|Use `epic` as first major decomposition unit under project.|
|Task files with acceptance criteria|**Yes**|Combine with Backlog.md task grammar.|
|`depends_on`, `parallel`, `conflicts_with`|**Yes**|Use for Python dependency graph and unlock-depth.|
|“what’s next / what’s blocked”|**Yes**|Python computes candidates; Claude explains/ranks.|
|GitHub Issues sync|**No v1**|Future team layer only.|
|Git worktrees / parallel agents|**No v1**|Too much for solo local operator now.|

**Apex organization:**

```txt
.claude/kb/projects/apex-os-meta.md
.claude/kb/epics/
.claude/kb/tasks/
.claude/kb/workflows/
.claude/kb/registry.md
.claude/kb/progress-log.md
.claude/kb/next-precap-context.md
```

---

## 2. Backlog.md — import task-file grammar

**Fit:** file-based task substrate.

Backlog.md is explicitly designed for project collaboration between humans and AI agents in a Git ecosystem, supports task creation/editing/listing/search/board, has MCP integration for Claude Code/Codex/Gemini/Kiro, and can run filesystem-only without Git. ([GitHub](https://github.com/MrLesk/Backlog.md "GitHub - MrLesk/Backlog.md: Backlog.md - A tool for managing project collaboration between humans and AI Agents in a git ecosystem · GitHub"))

|Backlog.md part|Import?|Apex adaptation|
|---|--:|---|
|One Markdown file per task|**Yes**|Use for Apex `task` records once tasks become too large for project file.|
|YAML/frontmatter metadata|**Yes**|Keep fields machine-readable.|
|Acceptance criteria|**Yes**|Required for executable tasks.|
|Implementation notes|**Yes**|Use as progress log excerpts.|
|Final summary|**Yes**|Feed FlowRecap/APSU.|
|CLI/Web UI|**No v1**|Apex should not depend on TypeScript CLI.|
|MCP server|**Maybe later**|Good later if you want tool-based task edits.|

**Apex task file pattern:**

```yaml
---
id: task-apex-flowrecap-delta-contract
project: apex-os-meta
epic: epic-execution-memory-loop
chunk: chunk-flowrecap-integration
status: active
priority: 90
urgency: 85
date: NA
depends_on:
  - task-apex-project-kb-manager-foundation
unlocks:
  - task-apex-precapnextday-kb-upgrade
operator_review_needed: true
---
# Define FlowRecap → project-kb delta contract

## Expected output
...

## Acceptance criteria
- ...

## Implementation notes
- ...
```

---

## 3. OpenClaw — import durable execution pattern, not PM model

**Fit:** local skill/runtime pattern.

OpenClaw is a local-first personal assistant with skills under `~/.openclaw/workspace/skills/<skill>/SKILL.md`, and its README emphasizes a local gateway, tools, channels, sandboxing, and skills. ([GitHub](https://github.com/openclaw/openclaw "GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way.  · GitHub")) Its TaskFlow skill explicitly owns flow identity, owner session, `currentStep`, `stateJson`, waits, child tasks, lifecycle, and revision tracking, while stating that branching/business logic belongs above the runtime. ([GitHub](https://raw.githubusercontent.com/openclaw/openclaw/main/skills/taskflow/SKILL.md "raw.githubusercontent.com"))

|OpenClaw part|Import?|Apex adaptation|
|---|--:|---|
|TaskFlow lifecycle|**Yes**|Use as design model for resumable KB operations.|
|`stateJson` state bag idea|**Yes**|Use Python-generated structured packet handed to Claude.|
|Revision checks|**Yes**|Add stale/revision guards before writes.|
|Runtime owns state, not business logic|**Yes**|Python owns writes; Claude owns reasoning.|
|ClawHub marketplace skills|**No**|Security risk. Do not install third-party skills blindly.|
|Full OpenClaw runtime|**No**|Too broad for Claude Code-native Apex.|

**Security note:** OpenClaw-style skill marketplaces have real security concerns. Recent reporting and research warn that SKILL.md-style ecosystems can carry malicious instructions or executable code risks, so Apex should copy **patterns**, not install unvetted skills. ([TechRadar](https://www.techradar.com/pro/what-are-openclaw-skills-a-detailed-guide?utm_source=chatgpt.com "What are OpenClaw Skills? A detailed guide"))

---

## 4. CrewAI — import task-contract design

**Fit:** task/operation contract.

CrewAI’s project structure uses `main.py`, `crew.py`, `tools/`, `agents.yaml`, and `tasks.yaml`; this is useful as a reference for separating Python execution, config, tools, and task definitions. ([GitHub](https://github.com/crewAIInc/crewAI "GitHub - crewAIInc/crewAI: Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks. · GitHub")) The CrewAI `design-task` skill says task design is the main lever, and every task needs a `description` and `expected_output`; it also explicitly covers output formats, dependencies/context, guardrails, human input, async execution, markdown formatting, and output files. ([GitHub](https://raw.githubusercontent.com/crewAIInc/skills/main/skills/design-task/SKILL.md "raw.githubusercontent.com"))

|CrewAI part|Import?|Apex adaptation|
|---|--:|---|
|`description` + `expected_output`|**Yes**|Required fields for chunks/tasks/workflows.|
|`context` dependencies|**Yes**|Map to `depends_on` and source context.|
|Guardrails|**Yes**|Validation before Python writes.|
|Human review|**Yes**|Operator gate before state mutation.|
|Full CrewAI framework|**No v1**|Apex is Claude Code-native, not a separate CrewAI app.|

---

## 5. LangGraph — future escalation only

**Fit:** state-machine pattern if Apex outgrows scripts.

Use LangGraph later if project-kb-manager becomes a graph of many conditional operations. Do **not** use it in v1. The saved GPT recap already reached the same conclusion: LangGraph is a future state-machine layer, not needed if simple scripts are sufficient.

---

# Final architecture

```yaml
apex_project_kb_manager_architecture:
  file_format:
    standard: llms_txt_style_markdown
    structure:
      - yaml_frontmatter
      - structured_markdown_body
      - omit_null_fields
      - snake_case_keys
      - closed_enums
      - one_file_per_entity

  pm_logic:
    source: CCPM
    imported_phases:
      - plan
      - structure
      - track
    rejected_phases:
      - github_sync
      - parallel_worktree_execution

  state_substrate:
    source: Backlog.md
    imported_patterns:
      - markdown_task_files
      - acceptance_criteria
      - implementation_notes
      - final_summary
      - status_priority_dependency_fields

  deterministic_layer:
    source: OpenClaw_TaskFlow + local_python
    python_owns:
      - read_project_files
      - parse_frontmatter
      - validate_schema
      - generate_registry
      - compute_priority_score
      - compute_unlock_depth
      - detect_blockers_from_explicit_fields
      - detect_stall_condition
      - append_progress_log
      - write_validated_state

  reasoning_layer:
    source: Claude_Code_skill + CrewAI_task_contract_pattern
    claude_owns:
      - synthesize_next_action
      - rank_focus_from_context
      - detect_implicit_blockers
      - merge_flowrecap_narrative
      - produce_operator_summary
      - produce_next_precap_context_draft
```

---

# File organization proposal

## V1: one project only — Apex

```txt
.claude/
  skills/
    project-kb-manager/
      SKILL.md
      references/
        project-kb-contract.md
        python-operations-contract.md
        ranking-and-dependency-rules.md
        flowrecap-merge-rules.md
        validation-rules.md
  kb/
    registry.md
    next-precap-context.md
    progress-log.md
    projects/
      apex-os-meta.md
    epics/
      apex-os-meta__execution-memory-loop.md
      apex-os-meta__precap-integration.md
    chunks/
      apex-os-meta__flowrecap-integration.md
    tasks/
      task-apex-flowrecap-delta-contract.md
    workflows/
      workflow-apex-project-kb-update.md
  scripts/
    project_kb_query.py
    project_kb_registry.py
    project_kb_score.py
    project_kb_update.py
```

## Why this structure

|Folder|Source pattern|Purpose|
|---|---|---|
|`.claude/skills/project-kb-manager/`|Claude/Agent Skills|Routing + reasoning instructions.|
|`.claude/kb/projects/`|llms.txt + repo-native KB|One file per project.|
|`.claude/kb/epics/`|CCPM|Major outcome areas.|
|`.claude/kb/chunks/`|Apex planning layer|Flow-sized planning units.|
|`.claude/kb/tasks/`|Backlog.md|Executable work records.|
|`.claude/kb/workflows/`|WorkflowProcesses + CrewAI|Repeatable process definitions.|
|`.claude/kb/registry.md`|Python-generated|Compact planning index for PrecapNextDay.|
|`.claude/kb/next-precap-context.md`|APSU/Precap bridge|What PrecapNextDay reads next.|
|`.claude/scripts/` or `scripts/`|OpenClaw/CrewAI style|Deterministic local operations.|

This also resolves an existing integration gap: current PrecapNextDay sources refer to abstract project-state inputs, but not concrete KB paths; prior validation already flagged that `.claude/kb/registry.md` must be wired explicitly if it becomes canonical.

---

# What to take, exactly

## Import map

|Apex need|Import from|Exact pattern|Adaptation|
|---|---|---|---|
|Project decomposition|CCPM|Plan → Structure → Track|Project → Epic → Chunk → Task → Subtask|
|Task storage|Backlog.md|Markdown task files with metadata, acceptance criteria, implementation notes|One file per task, YAML frontmatter, Markdown body|
|Dependency logic|CCPM + Task Master idea|`depends_on`, `unlocks`, blocked/next|Python computes unlock depth and blocked status|
|Deterministic operations|OpenClaw + local Python|Runtime state bag, revision checks, script summaries|Python scripts read/write/score/validate|
|AI reasoning boundary|OpenClaw + CrewAI|LLM produces structured decision; runtime persists|Claude proposes, Python writes only after validation|
|Task contract quality|CrewAI|`description`, `expected_output`, `context`, guardrail, output file|Required for chunks/tasks/workflows|
|Session continuity|GSD Core|`STATE.md`, `CONTEXT.md`|Only for long Claude Code build sessions|
|Long-task safety|planning-with-files|progress log + write discipline|Use for multi-step KB updates|
|LLM-readable format|llms.txt convention|Markdown hierarchy, curated sections|Apply to all Apex KB files|

---

# What not to take

|Do not take|Why|
|---|---|
|CCPM GitHub Issues sync|Team/dev workflow. Not needed for solo local v1.|
|CCPM worktrees/parallel agents|Overkill before team scale.|
|Backlog.md CLI as required runtime|Adds TypeScript dependency. Borrow format first.|
|OpenClaw full runtime|Too broad; security and setup surface too large.|
|ClawHub marketplace skills|Unvetted executable skills are risky.|
|CrewAI framework as Apex runtime|Would move Apex away from Claude Code-native design.|
|Pure JSON database|Less readable and less aligned with Claude skill files.|
|Pure prompt-only PM|You explicitly need deterministic Python for state integrity.|

---

# Answer to the original research question

## “Can we find an already established, worked-out, clearly defined file system to use?”

**Yes, but not as one complete PM/KB product.**

The strongest established file-system pieces are:

1. **CCPM** for PM process structure and skill package organization.
    
2. **Backlog.md** for Markdown task-file conventions and repo-local task state.
    
3. **OpenClaw TaskFlow** for durable operation lifecycle and Python/AI separation.
    
4. **CrewAI task design** for explicit task contracts and validation gates.
    

## “Is there a known community skill database we can clone as baseline?”

**No, not for your full Apex use case.**

The saved GPT recap says the Hermes PM skill ecosystem was not found and no exact community PM system was discovered that can directly replace `project-kb-manager`; it recommends layered import instead. OpenClaw has a real skill ecosystem, but it is a general local assistant/plugin ecosystem, not a verified PM/KB baseline; it should be mined for patterns only. ([GitHub](https://github.com/openclaw/openclaw "GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way.  · GitHub"))

---

# Recommended next action

Do **not** research more general agent frameworks right now.

Next, inspect and extract only these concrete source files:

|Priority|Source file|Why|
|--:|---|---|
|1|CCPM `skill/ccpm/SKILL.md`|Entry routing and PM phase boundaries.|
|2|CCPM `references/plan.md`|Project intake / PRD-style logic.|
|3|CCPM `references/structure.md`|Epic → task decomposition.|
|4|CCPM `references/track.md`|“what’s next / blocked / status” logic.|
|5|CCPM `references/conventions.md`|File/frontmatter conventions.|
|6|Backlog.md task examples|Task metadata and Markdown body format.|
|7|OpenClaw `taskflow/SKILL.md`|Durable operation lifecycle.|
|8|CrewAI `design-task/SKILL.md`|Task contract and expected-output rules.|

Then produce **one Apex PM/KB Import Specification** with:

```yaml
output:
  - entity_model
  - folder_model
  - python_operations
  - claude_reasoning_operations
  - file_templates
  - first_test_run_spec
```

No files should be generated before that import spec is validated.

---

# Decision table

|Decision|Answer|
|---|---|
|Full system to copy?|**None.**|
|Primary PM logic source?|**CCPM Plan + Structure + Track.**|
|Primary file/task substrate?|**Backlog.md-style Markdown task files.**|
|Deterministic execution pattern?|**OpenClaw TaskFlow-style lifecycle + local Python scripts.**|
|Task quality contract?|**CrewAI design-task pattern.**|
|File format convention?|**llms.txt-style Markdown with YAML frontmatter.**|
|Runtime in v1?|**Claude Code + local Python. No external DB, no SaaS, no GitHub Issues dependency.**|
|Best next step?|**Create an import spec, then a first Apex-only test run.**|

The correct Apex direction is: **build `project-kb-manager` as a Claude Code skill backed by local Python scripts and llms.txt-style Markdown files, using CCPM for decomposition logic, Backlog.md for task-file grammar, OpenClaw for durable operation patterns, and CrewAI for task contracts.**