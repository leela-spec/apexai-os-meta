# GPT Extended-Thinking Prompt Flow — Claude Skill & Process File Generation
# Version 2.0

```yaml
flow_metadata:
  id: gpt-extended-thinking-claude-skill-process-file-flow-v2-0
  status: ready
  executor: GPT_extended_thinking_mode
  output_target: Claude_Code_skill_and_process_files
  output_grain: exactly_one_complete_file_per_prompt
  source_input_type: design_spec_documents_supplied_by_operator
```

---

# 0. Purpose

This prompt flow is used inside GPT extended-thinking mode to generate exactly one final Claude Code skill or process file per prompt run.

The operator supplies source design spec documents at the start of each prompt. GPT reads those documents, translates their process logic into Claude-native file format, and outputs one complete, ready-to-use file.

The output file is final. It contains no drafts, no version history, no explanations of prior terminology, no source references, and no traces of how it was derived.

---

# 1. What you supply before running each prompt

Before running any file-generation prompt, provide:

```yaml
operator_supplied_inputs:
  source_design_specs:
    - one or more design specification documents describing the process or skill
    - paste or upload these directly into the chat
    - they may use any terminology or structure — GPT translates them
  target_file_path:
    - the exact output path for the file to be created
    - example: .claude/skills/flow-recap/SKILL.md
    - example: .claude/workflows/precap-next-day.md
  previously_created_files_if_any:
    - paste or reference already-generated files from this sequence
    - these are binding context for consistency of terminology and structure
```

No separate source index file is needed. The design specs you provide are the only source material.

---

# 2. Execution mode

```yaml
execution_mode:
  model_mode: extended_thinking

  thinking_use:
    - extract process logic from source specs
    - resolve terminology into Claude-native equivalents
    - determine correct file type (skill vs process)
    - identify required sections and fill them completely
    - verify the output against the validation checklist before writing it

  public_output_policy:
    - output exactly the required response structure: one file, one checklist, one next prompt
    - do not explain derivation, translation choices, or source analysis
    - do not show version comparisons or before/after diffs
    - do not expose chain-of-thought
    - use concise language only inside Assumptions or Open Questions sections when genuinely needed

  source_use_policy:
    - treat all supplied source documents as design logic inputs, not as copy to reproduce
    - preserve: process intent, step logic, input/output contracts, operator gates,
      validation rules, artifact flow, failure modes, non-goals
    - translate: all non-Claude terminology into Claude-native equivalents
    - omit: all traces of source terminology, version references, draft markers,
      implementation notes, and derivation commentary from the output file
```

---

# 3. Hard scope

Only create files in these two families:

```yaml
allowed_output_paths:
  skill_files:
    - .claude/skills/*/SKILL.md
  process_files:
    - .claude/workflows/*.md
```

Do not create:

```yaml
forbidden_outputs:
  - CLAUDE.md
  - AGENTS.md
  - .claude/agents/*.md
  - .claude/settings.json
  - schemas/
  - tests/
  - evals/
  - GitHub Actions files
  - Docker or Kubernetes files
  - .env or secrets files
  - runtime state files
  - task board files
  - CI/CD or deployment files
  - calendar API integration files
  - any file type not in the allowed_output_paths list above
```

---

# 4. File type decision rule

Before writing any file, classify it:

```yaml
classification_rule:
  create_SKILL_md_when:
    - the procedure is reusable and self-contained
    - it can be triggered by a single user intent or workflow step
    - one Claude session can execute it end-to-end
    - it produces a standardized artifact or decision
    - no multi-phase orchestration across multiple roles is required inside the file

  create_workflow_md_when:
    - the procedure coordinates multiple skills or role references
    - it has multiple phases, gates, or handoffs across time
    - it defines artifact flow across a planning or execution cycle
    - it is an orchestration map rather than one executable unit
    - it specifies how Claude sequences skills and validates transitions

  default_if_unclear: skill_file_for_single_repeatable_procedure
                      process_file_for_multi-step_orchestration
```

---

# 5. Translation rule

The source documents may use any terminology. Apply these translation rules silently inside thinking. The output file must contain only Claude-native language.

```yaml
translation_rules:
  preserve_as_is:
    - process intent and step logic
    - input and output contracts
    - operator gates and validation requirements
    - artifact names and handoff structure
    - failure modes and non-goals
    - anti-regression rules

  translate_to_Claude_native:
    - any runtime scheduler concept → trigger concept only, no runtime config
    - any task board or graph reference → workflow step or operator gate
    - any profile or agent role reference → role label only if already defined

  omit_entirely:
    - version numbers, draft markers, status labels
    - source document metadata and document IDs
    - implementation notes referencing external systems
    - open questions that are purely internal design history
    - all commentary explaining what was changed, removed, or translated
    - citation markup, file references, sandbox links
    - any text that reads as a note to a future implementer rather than an instruction to Claude
```

The output file must read as if it was written directly for Claude Code. No reader should be able to detect that it was derived from other documents.

---

# 6. Global output contract

Every response must follow this exact structure. Nothing else is acceptable:

```
# FILE: <target path>

<complete final file content>

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] The file path is in the approved skill or workflow family.
- [ ] The file is complete and final, not a draft or outline.
- [ ] Every required section is present and filled.
- [ ] The file uses Claude-native terminology throughout.
- [ ] No source terminology, version references, draft markers, or derivation commentary appears anywhere in the file.
- [ ] No forbidden file types were created.
- [ ] The file has clear triggers, inputs, procedure or process steps, outputs, validation rules, failure modes, and non-goals.
- [ ] No citation markup, file reference links, or sandbox paths appear in the file.
- [ ] Open questions appear only when they are genuinely blocking execution and cannot be reasonably defaulted.

---

# NEXT PROMPT

Paste this to create the next file:

> <pre-filled next prompt using the template from Section 9>
```

No commentary outside this structure.

---

# 7. Skill file format

For `.claude/skills/*/SKILL.md`:

```markdown
---
name: <kebab-case-name>
description: >
  Use this skill when <trigger condition in plain language>.
  <One to three sentences: what it takes as input, what it produces as output,
  and what it explicitly does not do.>
---

# <Human-Readable Skill Name>

## Purpose

<One focused paragraph. State what this skill does, why it exists, and what
it must not do. No implementation detail. No derivation commentary.>

## When to Use

- <trigger condition>
- <trigger condition>
- <trigger condition>

## Inputs

\`\`\`yaml
inputs:
  required:
    - <input_name>: <what it is and where it comes from>
  optional:
    - <input_name>: <what it is and when to use it>
\`\`\`

## Procedure

1. <Phase label if needed — bold>
2. <Step: one action, one outcome>
3. <Step: one action, one outcome>
...
N. <Operator gate step if required: present X to operator. Do not proceed until approved.>
N+1. <Write output step: write artifact to canonical path. Update task status.>

## Output Contract

\`\`\`yaml
output:
  artifact_type: <type>
  path_pattern: <logical slot or path pattern>
  required_sections:
    - <section name>
    - <section name>
  operator_gate_required: true | false
\`\`\`

## Validation

- <Check that must pass before the skill is considered complete>
- <Check that must pass before the skill is considered complete>

## Failure Modes

- <failure condition>: <required response>
- <failure condition>: <required response>

## Non-Goals

- <what this skill must never do>
- <what this skill must never do>
```

Skill file rules:

```yaml
skill_rules:
  - name must be lowercase kebab-case
  - description must start with "Use this skill when"
  - description must name the exact input artifact and exact output artifact
  - description must state the boundary in one clause
  - description must be under 80 words
  - procedure steps must use one verb and one outcome per step
  - operator gate steps must be explicit procedure steps, not footnotes
  - write steps must name the canonical path or logical slot
  - do not embed schema definitions inline — reference the schema name only
  - do not include examples unless they fit inside the procedure as inline values
  - do not add sections not listed in the format above
```

---

# 8. Process file format

For `.claude/workflows/*.md`:

```markdown
# <Process Name>

\`\`\`yaml
workflow_metadata:
  id: <kebab-id>
  status: active_spec
  target_environment: Claude_Code
  file_type: process_orchestration_spec
\`\`\`

## Purpose

<One focused paragraph. State what this process orchestrates, why it exists,
and what it must not do. No implementation detail. No derivation commentary.>

## Trigger

\`\`\`yaml
trigger:
  user_phrases:
    - <phrase that activates this process>
    - <phrase that activates this process>
  upstream_conditions:
    - <artifact or state that signals this process should run>
\`\`\`

## Roles Used

\`\`\`yaml
roles:
  - <role name>: <what it does in this process>
\`\`\`

## Inputs

\`\`\`yaml
inputs:
  required:
    - <artifact>: <source and meaning>
  optional:
    - <artifact>: <source and when to use>
\`\`\`

## Process Steps

1. **<Phase name>**
   <What happens in this phase. Name the skill invoked if applicable.>

2. **<Phase name>**
   <What happens. Name operator gate if present.>

3. **<Phase name>**
   <What happens. Name the artifact produced.>

## Artifact Flow

\`\`\`yaml
artifact_flow:
  - step: <step number or name>
    from: <producer>
    to: <consumer>
    artifact: <artifact name>
    gate: operator_required | automatic
\`\`\`

## Operator Gates

- **Gate <N>**: <when it occurs, what the operator must approve or reject>
- **Gate <N>**: <when it occurs, what the operator must approve or reject>

## Output Contract

\`\`\`yaml
outputs:
  primary:
    - <artifact name>: <path pattern or logical slot>
  secondary:
    - <artifact name>: <path pattern or logical slot>
\`\`\`

## Validation

- <Check that must pass before the process is complete>
- <Check that must pass before the process is complete>

## Failure Modes

- <failure condition>: <required response>
- <failure condition>: <required response>

## Non-Goals

- <what this process must never do>
- <what this process must never do>
```

Process file rules:

```yaml
process_rules:
  - workflow_metadata block is required at the top
  - roles must only reference roles already defined in the system
  - do not invent new permanent roles
  - artifact_flow must name every artifact that crosses a boundary
  - operator gates must be named in both the Process Steps and Operator Gates sections
  - do not create runtime schedulers, background jobs, or external automations
  - do not include implementation notes or future-state commentary
  - do not include version history or derivation notes
```

---

# 9. Prompt template for each file

Use this exact prompt for every file in the sequence:

```
Create the next Claude skill/process file.

Target file: `<target_path>`

Source design specs attached: [paste or upload your source documents here]

Previously created files for context: [paste or reference completed files if any]

Rules:
- Output exactly one complete file at the target path.
- Follow the global output contract from the prompt flow.
- Use Claude-native language throughout. No source terminology in the output.
- End with the validation checklist and the next prompt pre-filled.
```

---

# 10. File sequence

Create files in this order unless the operator changes it:

```yaml
sequence:
  01:
    target_path: .claude/skills/flow-recap/SKILL.md
    type: skill
    source_focus: flow execution recap, raw dump digestion, status delta, artifact index, operator gate

  02:
    target_path: .claude/skills/prompt-and-ai-routing-planning/SKILL.md
    type: skill
    source_focus: prompt packet generation, AI surface selection, fallback routes, usage tracking

  03:
    target_path: .claude/workflows/precap-week.md
    type: process
    source_focus: weekly planning, project priority setting, weekly-to-daily handoff

  04:
    target_path: .claude/workflows/precap-next-day.md
    type: process
    source_focus: daily plan generation, four flows, three sprints, prompt packets, context packaging, recap instructions

  05:
    target_path: .claude/skills/status-merge/SKILL.md
    type: skill
    source_focus: daily cross-project status merge, consumed recap registry, conflict detection

  06:
    target_path: .claude/skills/model-usage-tracking/SKILL.md
    type: skill
    source_focus: planned vs actual AI surface usage, route learning, scarce-mode warnings

  07:
    target_path: .claude/skills/context-packet-preparation/SKILL.md
    type: skill
    source_focus: context selection, file upload manifest, compression, missing context marking

  08:
    target_path: .claude/skills/calendar-block-creation/SKILL.md
    type: skill
    source_focus: calendar feasibility, block packet generation, operator approval gate

  09:
    target_path: .claude/skills/branch-and-chunk-selection/SKILL.md
    type: skill
    source_focus: task slicing, execution mode selection, next-chunk decision logic

  10:
    target_path: .claude/skills/day-plan-validation/SKILL.md
    type: skill
    source_focus: four-flow constraint check, operator gate, feasibility validation

  11:
    target_path: .claude/workflows/weekly-daily-flow-loop.md
    type: process
    source_focus: full planning-to-recap loop orchestration

  12:
    target_path: .claude/workflows/skill-process-index.md
    type: process
    source_focus: index of all generated skills and processes, triggers, dependencies, usage order
```

---

# 11. Start prompt

Paste this to begin:

```
Create File 01 from the sequence.

Target file: `.claude/skills/flow-recap/SKILL.md`

Source design specs attached: [paste your FlowRecap design spec document here]

Previously created files: none

Rules:
- Output exactly one complete SKILL.md file.
- Follow the global output contract.
- Use Claude-native language throughout. No source terminology in the output.
- End with the validation checklist and the next prompt pre-filled for File 02.
```

---

# 12. Continuation shorthand

If the operator types only:

```
g
```

Interpret it as: create the next file in the sequence. Load the source specs the operator supplied most recently. Apply all rules. Output exactly one file, the checklist, and the next prompt.
