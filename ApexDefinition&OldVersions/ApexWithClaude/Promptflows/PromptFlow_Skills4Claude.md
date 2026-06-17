# GPT Skill Process File Flow v3 — Claude Skill & Workflow File Generation

```yaml
flow_metadata:
  id: gpt-skill-process-file-flow-v3
  status: ready_for_operator_use
  executor: GPT_extended_thinking_mode
  output_target: Claude_skill_and_workflow_files
  output_grain: exactly_one_complete_file_per_prompt
  paired_source_index: GPT_Skill_Process_Source_Index_v3.md
  output_location_policy: chat_output_only
```

---

# 0. Purpose

This prompt flow is used in GPT extended-thinking mode to generate exactly one final Claude-native skill or workflow file per prompt run.

The operator supplies or references the relevant source design documents. GPT uses the paired source index to identify which files matter, translates all source logic into Claude-native form, and outputs one complete file in chat for the operator to copy and save manually.

The generated file is final. It must contain no draft markers, no version history, no derivation notes, no source citations, no source-file references, and no traces of legacy runtime terminology.

---

# 1. Operator-supplied inputs

Before each file-generation prompt, the operator provides:

```yaml
operator_supplied_inputs:
  target_file_path:
    required: true
    examples:
      - .claude/skills/flow-recap/SKILL.md
      - .claude/workflows/weekly-daily-flow-loop.md

  source_design_specs:
    required: recommended
    rule: >
      Paste, upload, or clearly reference the source documents named in
      GPT_Skill_Process_Source_Index_v3.md for the target file.

  previously_created_files:
    required: when_available
    rule: >
      Paste or reference already generated files from this same sequence when
      terminology, artifact names, or handoff contracts must remain consistent.
```

The assistant must not write files to disk. The assistant outputs the final file content in chat only.

---

# 2. Hard scope

Only create files in these families:

```yaml
allowed_output_paths:
  skill_files:
    - .claude/skills/*/SKILL.md

  workflow_files:
    - .claude/workflows/*.md
```

Do not create or propose content for:

```yaml
forbidden_outputs:
  - CLAUDE.md
  - .claude/agents/*.md
  - .claude/settings.json
  - schemas/
  - tests/
  - evals/
  - GitHub Actions files
  - Docker files
  - Kubernetes files
  - secrets
  - .env files
  - runtime state files
  - task board files
  - CI/CD files
  - deployment files
  - calendar API integration files
  - identity files outside .claude/skills and .claude/workflows
  - any file type not listed in allowed_output_paths
```

---

# 3. Claude-native formatting rule

Every generated target file must use Claude-native file logic.

```yaml
claude_formatting_rule:
  always:
    - Use Claude skill or Claude workflow structure.
    - Use Claude-readable trigger descriptions.
    - Use precise input and output artifact names.
    - Use explicit operator gates where human approval is required.
    - Use artifact handoffs instead of runtime automation assumptions.
    - Use final instruction language, not planning commentary.

  never:
    - Do not preserve source runtime vocabulary.
    - Do not explain how the file was translated.
    - Do not include old terms, source names, source citations, or version history.
    - Do not create implementation notes for external schedulers or runtime systems.
    - Do not present the output as a draft.
```

---

# 4. File type decision rule

Classify each target before writing.

```yaml
classification_rule:
  create_SKILL_md_when:
    - the procedure is reusable and self-contained
    - it can be triggered by one clear user intent
    - one Claude session can execute it end-to-end
    - it produces a standardized artifact, decision, packet, or validation result
    - it does not require script-level orchestration across many subagents

  create_workflow_md_when:
    - the file coordinates multiple skills
    - the file defines artifact flow across a larger loop
    - the file maps phases, gates, and handoffs across time
    - the file is an orchestration spec rather than one executable procedure
    - the file explains how Claude sequences existing skills and validates transitions

  default_if_unclear:
    - Use SKILL.md for repeatable planning, recap, merge, routing, validation, and logging procedures.
    - Use workflow markdown only for cross-skill loop orchestration.
```

For this flow, `precap-week` and `precap-next-day` are skills. The loop-level file is a workflow.

---

# 5. Legacy-term purge

Generated target files must not contain legacy runtime terminology or old system labels.

```yaml
legacy_term_purge:
  banned_from_generated_target_files:
    - Hermes
    - OpenCLAW
    - OpenClaw
    - SOUL.md
    - AGENTS.md
    - cron
    - Kanban
    - profile
    - runtime implementation
    - draft
    - v0.1
    - v0.2
    - previous version
    - source document
    - derived from
    - translated from

  replacement_policy:
    old_runtime_skill: skill
    old_runtime_process: workflow step or skill procedure
    old_runtime_profile: role reference
    old_runtime_schedule: trigger condition
    old_runtime_graph: workflow spec or artifact flow
    old_identity_file: role boundary already available to Claude
```

Exception: the prompt-flow and source-index files may name source files exactly so the operator can find them. The generated target files may not.

---

# 6. Role boundary rule

Generated files may reference only these role labels when role ownership or validation is needed:

```yaml
allowed_role_references:
  - alfred
  - meta_strategist
  - meta_operations
  - meta_detective_controller
```

Rules:

```yaml
role_rules:
  - Do not invent additional permanent roles.
  - Do not turn skills into roles.
  - Do not use role labels where a skill trigger is sufficient.
  - Temporary specialization may be described only as a temporary review lane inside a workflow, not as a new role file.
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
- [ ] The file path is in `.claude/skills/*/SKILL.md` or `.claude/workflows/*.md`.
- [ ] The file is complete and final, not a draft or outline.
- [ ] The file uses Claude-native terminology and Claude-native file logic throughout.
- [ ] The file contains no banned legacy terms.
- [ ] The file contains no source citations, source-file references, sandbox links, or derivation notes.
- [ ] The file creates no forbidden infrastructure, schemas, tests, settings, CI, secrets, task boards, or deployment files.
- [ ] The file has clear triggers, inputs, procedure or workflow steps, outputs, validation rules, failure modes, and non-goals.
- [ ] Operator gates are explicit procedure or workflow steps where required.
- [ ] Assumptions and open questions appear only when needed for safe execution.

---

# NEXT PROMPT

Paste this next:
> <pre-filled next prompt text>
```

Do not output commentary outside this structure.

---

# 8. Skill file format

Use this structure for every `.claude/skills/*/SKILL.md` file:

````md
---
name: <kebab-case-skill-name>
description: >
  Use this skill when <trigger condition>. It consumes <exact input artifact(s)>
  and produces <exact output artifact>. It does not <main boundary>.
allowed-tools:
  - Read
  - Write
  - Grep
  - Glob
---

# <Human-Readable Skill Name>

## Purpose

<One focused paragraph explaining what the skill does, why it exists, what it produces, and what it must not do.>

## When to Use

- <Trigger condition>
- <Trigger condition>
- <Trigger condition>

## Inputs

```yaml
inputs:
  required:
    - <input_name>: <source and meaning>
  optional:
    - <input_name>: <source and when to use>
````

## Procedure

1. —
    
2. —
    
3. — Present <artifact/decision> to the operator and wait for explicit approval, edit, or rejection before continuing.
    
4. — Produce with the required sections.
    

## Output Contract

```yaml
outputs:
  primary:
    artifact: <artifact_name>
    format: markdown_with_yaml_blocks | markdown | yaml
    logical_location: <logical slot or path pattern>
  secondary:
    - <artifact_name>: <purpose>
```

## Validation

## Failure Modes

- :
    
- :
    

## Assumptions

## Open Questions

## Non-Goals

````

Skill rules:

```yaml
skill_rules:
  - Frontmatter is required.
  - The skill name must be lowercase kebab-case.
  - The description must begin with "Use this skill when".
  - The description must name exact input and output artifacts.
  - The description must include one boundary clause.
  - The description should stay concise enough to work as a routing key.
  - Use `allowed-tools` only for tools actually needed by the skill.
  - Use `Read`, `Write`, `Grep`, and `Glob` as the default set for artifact-producing markdown skills.
  - Do not include tool names for external services unless the target file genuinely requires them.
  - Procedure steps must be executable instructions, not explanations.
  - Operator gates must be explicit numbered steps.
  - Output contracts must name the primary artifact clearly.
  - Assumptions and open questions are allowed but must be short and operational.
````

---

# 9. Workflow file format

Use this structure for every `.claude/workflows/*.md` file:

````md
# <Workflow Name>

```yaml
workflow_metadata:
  id: <kebab-case-id>
  target_environment: Claude_Code
  file_type: workflow_spec
````

## Purpose

<One focused paragraph explaining the loop or orchestration this workflow coordinates, why it exists, and what it must not do.>

## Trigger

```yaml
trigger:
  user_phrases:
    - <phrase>
    - <phrase>
  upstream_conditions:
    - <artifact or state condition>
```

## Roles Used

```yaml
roles:
  - <allowed_role_reference>: <role in this workflow>
```

## Skills Used

```yaml
skills:
  - <skill-name>: <when this workflow uses it>
```

## Inputs

```yaml
inputs:
  required:
    - <artifact>: <source and meaning>
  optional:
    - <artifact>: <source and when to use>
```

## Workflow Steps

1. —
    
2. —
    
3. — <what the operator approves, edits, or rejects>
    
4. —
    

## Artifact Flow

```yaml
artifact_flow:
  - step: <step or phase>
    from: <producer>
    to: <consumer>
    artifact: <artifact_name>
    gate: operator_required | automatic
```

## Operator Gates

- **Gate** :
    

## Output Contract

```yaml
outputs:
  primary:
    - <artifact_name>: <logical slot or path pattern>
  secondary:
    - <artifact_name>: <purpose>
```

## Validation

## Failure Modes

- :
    
- :
    

## Assumptions

## Open Questions

## Non-Goals

````

Workflow rules:

```yaml
workflow_rules:
  - Workflow files coordinate skills and artifact flow.
  - Workflow files do not define new permanent roles.
  - Workflow files do not create schedulers, background jobs, external automation, or infrastructure.
  - Artifact flow must name every artifact crossing a boundary.
  - Operator gates must appear in both Workflow Steps and Operator Gates.
  - Use only generated or already-known skills in Skills Used.
  - Do not include source history, version history, or implementation commentary.
````

---

# 10. Pre-output validation pass

Before writing the visible answer, silently validate:

```yaml
pre_output_validation:
  path_check:
    - target path matches allowed_output_paths
    - exactly one target file will be produced

  source_check:
    - source routing was consulted
    - new version sources were prioritized where available
    - review files were applied as corrections and constraints
    - low-priority patch sources were not used unless needed
    - excluded sources were not used

  terminology_check:
    - no banned legacy terms in generated target file
    - no source file names in generated target file
    - no citation markup in generated target file

  claude_format_check:
    - skill frontmatter exists for SKILL.md files
    - workflow metadata exists for workflow files
    - trigger, inputs, steps, outputs, validation, failure modes, and non-goals are present
    - operator gates are explicit where required
    - assumptions and open questions are concise and execution-relevant

  completion_check:
    - output follows the exact global output contract
    - checklist is included
    - next prompt is pre-filled
```

---

# 11. File sequence

Create files in this order:

```yaml
sequence:
  01:
    target_path: .claude/skills/flow-recap/SKILL.md
    type: skill
    source_focus: flow recap, raw dump digestion, planned-versus-actual comparison, artifact index, project status delta, model usage delta, operator-validated next step

  02:
    target_path: .claude/skills/prompt-and-ai-routing-planning/SKILL.md
    type: skill
    source_focus: prompt packets, AI surface routing, fallback routes, synthesis plan, context manifest, recap-capture metadata

  03:
    target_path: .claude/skills/model-usage-log/SKILL.md
    type: skill
    source_focus: planned versus actual AI surface usage, prompt quality, route reuse or avoidance, scarce-mode notes, operator-provided usage evidence

  04:
    target_path: .claude/skills/precap-next-day/SKILL.md
    type: skill
    source_focus: next-day planning, four fixed flows, three sprints per flow, prompt packets, context instructions, operator approval gate, FlowRecap handoff

  05:
    target_path: .claude/skills/status-merge/SKILL.md
    type: skill
    source_focus: cross-project status merge, flow recap consumption, skipped-flow markers, conflict detection, next planning context

  06:
    target_path: .claude/skills/precap-week/SKILL.md
    type: skill
    source_focus: weekly planning, project prioritization, calendar constraints, weekly plan packet, first next-day planning seed, operator approval gate

  07:
    target_path: .claude/workflows/weekly-daily-flow-loop.md
    type: workflow
    source_focus: overall planning-to-recap-to-status loop, skill sequence, artifact chain, operator gates, no autonomous project execution
```

The workflow index is outside this flow.

---

# 12. Prompt template for each file

Use this exact prompt for every file in the sequence:

```md
Create File <NN> from GPT Skill Process File Flow v3.

Target file: `<target_path>`

Use the paired source index entry for this target file.

Source design specs attached or available:
- <paste, upload, or reference the source files listed in the source index>

Previously created files:
- <paste or reference previously created files from this sequence, or write "none">

Rules:
- Output exactly one complete final file.
- Do not write to disk.
- Use Claude-native terminology and Claude-native file structure throughout.
- Do not include source citations, source-file names, derivation notes, draft markers, version history, or banned legacy terms in the generated file.
- Include assumptions and open questions only when operationally needed.
- End with the validation checklist and the next prompt pre-filled.
```

---

# 13. Start prompt

Paste this to begin:

```md
Create File 01 from GPT Skill Process File Flow v3.

Target file: `.claude/skills/flow-recap/SKILL.md`

Use the paired source index entry for this target file.

Source design specs attached or available:
- Skill Design Spec — FlowRecapSkill v0.1.md
- Skill Design Spec — FlowRecapSkill v0.1_Review.md
- Example Flow Package — PreCapNextDay System v0.1.md
- Information-Process Architecture — Next Work Plan v0.1.md
- WeeklyRoutine_Overview_Marco&Meso.md

Previously created files:
- none

Rules:
- Output exactly one complete final SKILL.md file.
- Do not write to disk.
- Use Claude-native terminology and Claude-native file structure throughout.
- Do not include source citations, source-file names, derivation notes, draft markers, version history, or banned legacy terms in the generated file.
- Include assumptions and open questions only when operationally needed.
- End with the validation checklist and the next prompt pre-filled for File 02.
```

---

# 14. Continuation shorthand

If the operator types only:

```md
g
```

Interpret it as:

```yaml
continuation_meaning:
  action: create_the_next_file_in_sequence
  source_policy: use_the_paired_source_index_entry
  prior_context: use_previously_created_files_when_available
  output_policy: exact_global_output_contract
```