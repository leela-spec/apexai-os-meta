# ChatGPT Extended-Thinking Prompt Flow — Create Claude-Only Skill / Process Files

```yaml
flow_metadata:
  id: chatgpt-extended-thinking-claude-skill-process-file-flow-v0-1
  status: ready_for_test_run
  executor: ChatGPT_extended_thinking_mode
  output_target: Claude_Code_skill_and_process_files
  paired_source_index: chatgpt_extended_thinking_skill_process_source_index.md
  predecessor_flow: chatgpt_extended_thinking_file_flow.md
```

---

# 0. Purpose

This prompt flow is used **inside ChatGPT extended-thinking mode** to create one Claude-only skill/process file per prompt.

ChatGPT is the authoring agent.

Claude / Claude Code is only the later consumer of the generated files.

This flow does **not** ask Claude to create files, inspect sources, or run a prompt chain. It prepares files that can later be placed into a Claude Code authoring environment.

---

# 1. Binding controller files

Before executing any file-generation prompt, ChatGPT must load and obey:

```yaml
required_controller_context:
  prompt_flow_file:
    name: chatgpt_extended_thinking_skill_process_file_flow.md
    role: execution_contract_for_one_skill_or_process_file_per_prompt
  source_index_file:
    name: chatgpt_extended_thinking_skill_process_source_index.md
    role: file_specific_source_router
  prior_system_flow_file:
    name: chatgpt_extended_thinking_file_flow.md
    role: inherited_global_claude_only_scope_and_control_plane_context
```

The source index is separate from this file. This file defines **how to execute** the skill/process file chain. The source index defines **which project sources to inspect for each target file**.

---

# 2. Execution mode

```yaml
execution_mode:
  model_mode: extended_thinking
  reason: >
    Each target file may require searching many project sources, resolving old
    Hermes/OpenCLAW vocabulary, and converting it into Claude-native skill or
    process orchestration logic. The visible output should still be small:
    exactly one complete target file, one checklist, and the next prompt.

  public_output_policy:
    - Do not provide broad analysis outside the required response structure.
    - Do not summarize all searched sources unless the target file itself needs a source_basis section.
    - Do not expose private chain of thought.
    - Use concise public reasoning only inside Assumptions, Boundaries, or Validation sections.

  source_use_policy:
    - Search the paired source index first.
    - Search only the source groups relevant to the current target file.
    - Prefer current accepted design-state files over older superseded drafts.
    - Treat Hermes/OpenCLAW/Apex terminology as historical source logic, not target runtime language.
    - Translate process mechanics into Claude skill/workflow language.
```

---

# 3. Hard scope

Only create Claude Code authoring environment files in these families:

```yaml
allowed_output_paths:
  skill_files:
    - .claude/skills/*/SKILL.md
  process_files:
    - .claude/workflows/*.md
```

Do **not** create:

```yaml
forbidden_outputs:
  - CLAUDE.md
  - .claude/agents/*.md
  - .claude/settings.json
  - schemas
  - tests
  - evals
  - GitHub Actions
  - Docker files
  - Kubernetes files
  - secrets
  - .env
  - runtime state files
  - actual task boards
  - CI/CD files
  - deployment files
  - Hermes profile files
  - Hermes cron files
  - Hermes Kanban files
  - Hermes memory files
  - SOUL.md
  - AGENTS.md
  - OpenCLAW runtime files
  - generic multi-agent framework files
```

This is a **Claude-only skill/process predefinition slice**, not a full runtime implementation.

---

# 4. Target interpretation

```yaml
target_system:
  name: Apex Alfred Claude-Orchestration Skill Layer
  created_by: ChatGPT_extended_thinking_mode
  later_used_by: Claude_or_Claude_Code
  target_runtime_language: Claude_native
  output_grain: exactly_one_skill_or_process_file_per_prompt
  core_goal: >
    Convert existing Apex / Hermes / OpenCLAW / Alfred process knowledge into
    Claude-native skill and process files that Claude Code can later use for
    planning, execution support, recap, status updates, prompt routing, context
    packaging, and validation.
```

---

# 5. Translation boundary

The source material may contain Hermes, OpenCLAW, Apex, Alfred, Kanban, cron, profile, SOUL.md, AGENTS.md, delegation, and other runtime-specific terminology.

For this prompt flow:

```yaml
translation_boundary:
  source_material_role: historical_logic_and_design_input
  target_material_role: Claude_ready_skill_or_process_file_content

  preserve:
    - process intent
    - step logic
    - input/output contracts
    - operator gates
    - validation discipline
    - handoff discipline
    - artifact flow
    - anti-sprawl rules
    - source-control discipline
    - current accepted loop structure
    - current accepted daily flow structure

  convert:
    Hermes_skill: Claude_Code_SKILL.md
    Hermes_profile: Claude_agent_role_reference_only_if_already_defined
    Hermes_Kanban_graph: Claude_workflow_or_process_spec
    Hermes_cron_or_schedule: trigger_concept_only_not_runtime_config
    OpenCLAW_agent_or_handoff: Claude_role_reference_or_handoff_section
    SOUL_or_AGENTS_identity_content: omit_unless_needed_as_role_boundary_reference
    runtime_tool_or_plugin_detail: omit_or_restate_as future_non_goal

  omit:
    - Hermes runtime commands
    - Hermes profile creation
    - Hermes Kanban calls
    - Hermes cron files
    - OpenCLAW runtime paths
    - deployment assumptions
    - hosted automation claims
    - source citation artifacts such as filecite or cite markup inside target files
```

Never drift back into Hermes/OpenCLAW implementation. Use those sources only to recover logic.

---

# 6. File classification rule

Before writing each file, classify the target as either a **Claude skill file** or a **Claude process/workflow file**.

```yaml
classification_rule:
  create_skill_file_when:
    - procedure_is_reusable
    - procedure_can_be_invoked_by_user_intent_or_workflow_step
    - procedure_can_be_executed_by_one Claude role/session
    - output_is_a_standardized_artifact_or_decision
    - no durable multi-stage orchestration spec is required inside the file

  create_process_file_when:
    - procedure_coordinates_multiple skills or role references
    - procedure_has multiple phases, gates, or handoffs
    - procedure defines artifact flow across time
    - procedure is an orchestration map rather than one executable skill
    - procedure should tell Claude how to sequence skills and validate transitions

  default_if_unclear: skill_file_if_single_repeatable_procedure_else_process_file
```

Allowed target forms:

```yaml
target_file_forms:
  skill:
    path_pattern: .claude/skills/<kebab-name>/SKILL.md
    purpose: executable reusable procedure for Claude Code
  process:
    path_pattern: .claude/workflows/<kebab-name>.md
    purpose: orchestration/process specification for Claude Code
```

---

# 7. Global output contract

Every file-generation response must output exactly this structure:

```md
# FILE: <target path>

<complete final file content>

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] The file path is one of the approved Claude-only skill/process paths.
- [ ] The file is final, not a draft or outline.
- [ ] The file follows the current file-specific source instructions from `chatgpt_extended_thinking_skill_process_source_index.md`.
- [ ] The file uses Claude-native terminology.
- [ ] Hermes/OpenCLAW/Apex source concepts were translated into Claude skill/process orchestration logic or omitted.
- [ ] The file does not create agents, settings, schemas, tests, CI, deployment, runtime state, Hermes runtime artifacts, SOUL.md, or AGENTS.md.
- [ ] The file has clear triggers, inputs, procedure/process steps, outputs, validation rules, failure modes, and non-goals.
- [ ] The file does not contain ChatGPT citation artifacts such as `filecite`, `cite`, `turn...file...`, or sandbox links.
- [ ] Open questions are recorded only when genuinely blocking or intentionally deferred.

---

# NEXT PROMPT

Paste this next:
> <next prompt text>
```

No commentary outside this structure.

---

# 8. Claude skill file format

For `.claude/skills/*/SKILL.md`, use this shape:

```md
---
name: <kebab-name>
description: Use this skill when <clear trigger/user intent>. <One to three concise sentences explaining scope, when to invoke, and what it produces.>
---

# <Human Name>

## Purpose

<One concise paragraph.>

## When to Use

- <trigger condition>
- <trigger condition>

## Inputs

```yaml
inputs:
  required:
    - <input_name>: <meaning>
  optional:
    - <input_name>: <meaning>
```

## Procedure

1. <step>
2. <step>
3. <step>

## Output Contract

```yaml
output:
  artifact_type: <type>
  required_sections:
    - <section>
```

## Validation

- <check>
- <check>

## Failure Modes

- <failure>: <response>

## Non-Goals

- <not this>
```

Rules:

```yaml
skill_rules:
  - Use valid Agent Skills frontmatter: name and description are required.
  - `name` must be lowercase kebab-case.
  - Description must be trigger-oriented and concise.
  - Do not add unsupported runtime claims.
  - Do not create scripts, references, assets, or evals in this flow.
  - If examples are needed, include them inside the SKILL.md body only.
```

---

# 9. Claude process/workflow file format

For `.claude/workflows/*.md`, use this shape:

```md
# <Process Name>

```yaml
workflow_metadata:
  id: <kebab-id>
  status: active_spec
  target_environment: Claude_Code
  file_type: process_orchestration_spec
```

## Purpose

<One concise paragraph.>

## Trigger

```yaml
trigger:
  user_phrases:
    - <phrase>
  upstream_inputs:
    - <artifact>
```

## Source Skill / Role References

```yaml
uses:
  roles:
    - alfred
    - meta_strategist
    - meta_operations
    - meta_detective_controller
  skills:
    - <skill-name>
```

## Inputs

```yaml
inputs:
  required:
    - <artifact>
  optional:
    - <artifact>
```

## Process Steps

1. <phase>
2. <phase>
3. <phase>

## Handoff / Artifact Flow

```yaml
artifact_flow:
  - from: <source>
    to: <target>
    artifact: <artifact>
```

## Operator Gates

- <gate>

## Output Contract

```yaml
outputs:
  - <artifact>
```

## Validation

- <check>

## Failure Modes

- <failure>: <response>

## Non-Goals

- <not this>
```

Rules:

```yaml
process_rules:
  - Treat `.claude/workflows/*.md` as process specifications, not executable runtime schedulers.
  - Use only the four already-defined roles as role references.
  - Do not invent new permanent agents.
  - Do not create actual boards, schedules, background jobs, or external automations.
```

---

# 10. Initial fixed file sequence

Create files in this order unless the operator explicitly changes the sequence:

```yaml
fixed_sequence:
  01:
    target_path: .claude/skills/flow-recap/SKILL.md
    type: skill
    source_focus: FlowRecapSkill, raw flow dump, operator execution evidence, status delta, artifact index

  02:
    target_path: .claude/skills/prompt-and-ai-routing-planning/SKILL.md
    type: skill
    source_focus: prompt packets, AI surface/model routing, fallback routes, expected outputs, recap-capture metadata

  03:
    target_path: .claude/workflows/precap-week.md
    type: process
    source_focus: PreCapWeek, weekly planning, operator weekly review gate, weekly-to-daily handoff

  04:
    target_path: .claude/workflows/precap-next-day.md
    type: process
    source_focus: PreCapNextDay v0.2, four flows, three sprints, flow packets, prompt packets, context packaging

  05:
    target_path: .claude/skills/status-merge/SKILL.md
    type: skill
    source_focus: AllProjectStatusPacketUpdate, once-daily/manual merge, consumed recap registry, conflict gates

  06:
    target_path: .claude/skills/model-usage-tracking/SKILL.md
    type: skill
    source_focus: ModelSubscriptionUsageTracking, planned vs actual AI surface usage, scarce-mode notes, route learning

  07:
    target_path: .claude/skills/context-packet-preparation/SKILL.md
    type: skill
    source_focus: context upload manifests, file/source selection, prompt context preparation, compression discipline

  08:
    target_path: .claude/skills/calendar-block-creation/SKILL.md
    type: skill
    source_focus: calendar block packets, feasibility, operator approval, calendar handoff logic

  09:
    target_path: .claude/skills/branch-and-chunk-selection/SKILL.md
    type: skill
    source_focus: branch/chunk decision logic, task slicing, execution mode selection

  10:
    target_path: .claude/skills/day-plan-validation/SKILL.md
    type: skill
    source_focus: PreCapNextDay validation, operator gates, feasibility checks, four-flow constraints

  11:
    target_path: .claude/workflows/weekly-daily-flow-loop.md
    type: process
    source_focus: full PreCapWeek -> PreCapNextDay -> OperatorExecutesPlannedFlow -> FlowRecap -> status merge -> next PreCapNextDay loop

  12:
    target_path: .claude/workflows/skill-process-index.md
    type: process
    source_focus: map all generated skills/processes, triggers, dependencies, and usage order
```

---

# 11. Prompt template for each file

Use this exact prompt pattern for every step:

```md
Create the next file in the fixed skill/process sequence.

Target file: `<target_path>`

Use:
- `chatgpt_extended_thinking_skill_process_file_flow.md` as the execution contract.
- `chatgpt_extended_thinking_skill_process_source_index.md` as the source router.
- The latest already-created Claude files in this flow as binding context.

Task:
Create exactly one complete Claude-only skill/process file at the target path.

Rules:
- Output exactly one file.
- Use the global output contract.
- Convert Hermes/OpenCLAW/Apex concepts into Claude-native skill/process logic.
- Do not create agents, settings, schemas, tests, CI, deployment, runtime state, Hermes runtime files, SOUL.md, or AGENTS.md.
- Do not include citation artifacts or source-link markup inside the target file.
- End with the next prompt for the following file in the fixed sequence.
```

---

# 12. Start prompt

Paste this to start the chain:

```md
Create File 1 from the fixed skill/process sequence.

Target file: `.claude/skills/flow-recap/SKILL.md`

Use:
- `chatgpt_extended_thinking_skill_process_file_flow.md` as the execution contract.
- `chatgpt_extended_thinking_skill_process_source_index.md` as the source router.
- Existing `CLAUDE.md` and `.claude/agents/*.md` files, if available, only as role-boundary context.

Task:
Create exactly one complete Claude-only skill file for FlowRecap.

Rules:
- Output exactly one file.
- Use the global output contract.
- Convert the previous FlowRecapSkill / Hermes/process design material into Claude Code `SKILL.md` logic.
- Do not create agents, settings, schemas, tests, CI, deployment, runtime state, Hermes runtime files, SOUL.md, or AGENTS.md.
- Do not include citation artifacts or source-link markup inside the target file.
- End with the next prompt for File 2.
```

---

# 13. Continuation shorthand

If the operator writes only:

```text
g
```

Interpret it as:

```yaml
continuation_rule:
  meaning: create_the_next_file_in_the_fixed_skill_process_sequence
  required_behavior:
    - identify the next incomplete file
    - load the controller and source index
    - create exactly one file
    - provide validation checklist
    - provide next prompt
```
