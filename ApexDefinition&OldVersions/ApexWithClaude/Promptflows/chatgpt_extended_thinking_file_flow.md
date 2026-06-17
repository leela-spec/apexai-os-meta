# ChatGPT Extended-Thinking Prompt Flow — Create Claude-Ready Apex Alfred Predefinition Files

```yaml
flow_metadata:
  id: chatgpt-extended-thinking-apex-alfred-file-flow-v0-2
  status: ready_for_test_run
  executor: ChatGPT_extended_thinking_mode
  output_target: Claude_Code_authoring_environment_files
  paired_source_index: chatgpt_extended_thinking_source_index.md
```

---

# 0. Purpose

This prompt flow is used **inside ChatGPT extended-thinking mode** to create a sequence of Claude-ready Markdown files.

ChatGPT, not Claude, is the authoring agent.

The generated files are intended to be given to Claude / Claude Code later as a prepared file pack. Claude is not expected to run this prompt flow, interpret the source set, or create the files itself.

The flow creates one final file per task, in a controlled sequence, with minimal public output and extensive private source inspection.

---

# 1. Binding controller files

Before executing any file-generation prompt, ChatGPT must load and obey:

```yaml
required_controller_context:
  prompt_flow_file:
    name: chatgpt_extended_thinking_file_flow.md
    role: execution_contract
  source_index_file:
    name: chatgpt_extended_thinking_source_index.md
    role: source_router_and_file_specific_lookup_policy
```

The source index is separate from this flow. This file defines **how to execute** the file chain. The source index defines **which sources to inspect for which generated file**.

---

# 2. Execution mode

```yaml
execution_mode:
  model_mode: extended_thinking
  reason: >
    Each file may require searching many project sources, but the visible output
    should be only one complete target file plus checklist and next prompt.

  public_output_policy:
    - Do not provide broad analysis outside the required response structure.
    - Do not summarize all searched sources unless the target file requires it.
    - Do not expose private chain of thought.
    - Use concise public reasoning only inside Assumptions, Boundaries, or Validation sections.

  source_use_policy:
    - Search the paired source index first.
    - Search only the source groups relevant to the current target file.
    - Prefer current design-state files over older superseded drafts.
    - Treat historical Hermes/OpenCLAW/Apex terminology as source logic, not target runtime language.
```

---

# 3. Hard scope

Only create files for the Claude Code authoring environment:

```yaml
allowed_output_paths:
  - CLAUDE.md
  - .claude/agents/*.md
  - .claude/skills/*/SKILL.md
  - .claude/workflows/*.md
```

Do not create:

```yaml
forbidden_outputs:
  - .claude/settings.json
  - schemas
  - tests
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
  - SOUL.md
  - AGENTS.md
  - OpenCLAW runtime files
  - generic multi-agent framework files
```

This is a **Claude-ready predefinition slice**, not the full implementation stack.

---

# 4. Target architecture

```yaml
target_system:
  name: Apex Alfred
  created_by: ChatGPT_extended_thinking_mode
  later_used_by: Claude_or_Claude_Code
  target_runtime_language: Claude-native
  core_goal: >
    Prepare a compact Claude-native orchestration predefinition layer for
    operator-facing request intake, role routing, handoff packets, strategic
    decomposition, operational file/workflow packaging, and detective validation.

stable_control_plane:
  permanent_roles:
    - alfred
    - meta_strategist
    - meta_operations
    - meta_detective_controller

anti_sprawl_rule: >
  Do not create additional permanent agents. Additional capabilities must become
  skills, workflow specs, temporary role references inside a workflow, or future
  TODOs.
```

---

# 5. Translation boundary

The source material may contain Hermes, OpenCLAW, Apex, Alfred, and earlier repo-specific terminology.

For this prompt flow:

```yaml
translation_boundary:
  source_material_role: historical_logic_and_design_input
  target_material_role: Claude_ready_file_content
  preserve:
    - process logic
    - role boundary logic
    - handoff discipline
    - validation discipline
    - source-control discipline
    - anti-sprawl lessons
    - file creation sequence discipline
  translate_or_omit:
    - Hermes runtime language
    - Hermes profile mechanics
    - Hermes Kanban mechanics
    - Hermes cron mechanics
    - SOUL.md conventions
    - OpenCLAW runtime assumptions
    - generic swarm implementation details
```

Translation table:

| Source concept | Claude-ready target in this flow |
|---|---|
| Hermes profile / profile identity | `.claude/agents/*.md` durable role definition |
| Hermes skill | `.claude/skills/<name>/SKILL.md` Claude Code skill |
| Hermes Kanban graph | `.claude/workflows/*.md` workflow specification |
| Cron / scheduled routine | Out of scope; mention only as future trigger concept if unavoidable |
| SOUL.md | Out of scope; translate identity content into `.claude/agents/*.md` |
| AGENTS.md | Out of scope unless explicitly started as a later build phase |
| Handoff packet schema | Structured section inside skills/workflows, not standalone schema |
| Runtime deployment | Out of scope |

Never drift back into Hermes implementation.

---

# 6. Global output contract

Every file-generation response must output exactly this structure:

```md
# FILE: <target path>

<complete final file content>

---

# VALIDATION CHECKLIST

- [ ] Exactly one file was produced.
- [ ] The file path is one of the approved Claude-ready paths.
- [ ] The file is final, not a draft or outline.
- [ ] The file follows the current file-specific source instructions from `chatgpt_extended_thinking_source_index.md`.
- [ ] The file does not create infrastructure, schemas, CI, Docker, Kubernetes, secrets, runtime state, task boards, Hermes runtime artifacts, SOUL.md, or AGENTS.md.
- [ ] The file uses Claude-native terminology only.
- [ ] Any Hermes/OpenCLAW/Apex source concepts were translated into Claude-ready terms or omitted.
- [ ] The file does not invent additional permanent agents beyond the approved four control-plane roles.
- [ ] The file has clear role boundaries, trigger conditions, inputs, outputs, and completion criteria where relevant.
- [ ] Open questions are recorded inside the file only when they are genuinely blocking or intentionally deferred.

---

# NEXT PROMPT

Paste this next:
> <next prompt text>
```

No commentary outside this structure.

---

# 7. Fixed file sequence

Create files in exactly this order:

1. `CLAUDE.md`
2. `.claude/agents/alfred.md`
3. `.claude/agents/meta_strategist.md`
4. `.claude/agents/meta_operations.md`
5. `.claude/agents/meta_detective_controller.md`
6. `.claude/skills/alfred-intake-router/SKILL.md`
7. `.claude/skills/handoff-packet-writer/SKILL.md`
8. `.claude/skills/source-constraint-map/SKILL.md`
9. `.claude/skills/goal-skeleton-fill-verify-loop/SKILL.md`
10. `.claude/skills/detective-validation-gate/SKILL.md`
11. `.claude/skills/workflow-normalizer/SKILL.md`
12. `.claude/workflows/intake_to_handoff.md`
13. `.claude/workflows/handoff_to_strategy.md`
14. `.claude/workflows/strategy_to_operations.md`
15. `.claude/workflows/operations_to_detective_validation.md`
16. `.claude/workflows/validated_file_creation_loop.md`
17. `.claude/workflows/workflow_index.md`

After file 17, stop and report that the Claude-ready predefinition set is complete.

---

# 8. File-specific execution rule

For every file:

```yaml
per_file_execution:
  step_1: Read this prompt-flow file.
  step_2: Read the paired source-index file.
  step_3: Locate the target file entry in the source-index file.
  step_4: Search/read only the required and recommended sources for that file.
  step_5: Extract only the logic needed for the target file.
  step_6: Translate source logic into Claude-ready terminology.
  step_7: Produce exactly one file under the global output contract.
  step_8: Emit the next prompt for the next fixed-sequence file.
```

If relevant sources conflict:

```yaml
conflict_resolution_order:
  1: explicit operator decisions in recent project files
  2: current Claude-ready prompt-flow/source-index files
  3: current design review files
  4: current process/information architecture files
  5: source indexes and source maps
  6: older Hermes/OpenCLAW/Alfred research files
  7: generic best practices
```

---

# 9. File-by-file requirements

## 1. `CLAUDE.md`

Purpose:

- Root Claude Code instruction file.
- Establish Apex Alfred as a Claude-ready orchestration predefinition system.
- Define the four stable roles.
- Explain that detailed procedures live in `.claude/skills/`.
- Explain that orchestration specs live in `.claude/workflows/`.
- Explain that durable role definitions live in `.claude/agents/`.
- Ban adding new permanent agents.
- Ban infrastructure/runtime work in this phase.
- Include a Claude-only translation rule.

Must include:

- Mission
- Allowed file families
- Permanent roles
- Role boundary summary
- Skill usage policy
- Workflow usage policy
- Anti-sprawl rules
- Validation-before-completion rule
- Out-of-scope list

Next prompt:
`Create File 2 from the fixed sequence: .claude/agents/alfred.md`

## 2. `.claude/agents/alfred.md`

Purpose:

- Define Alfred as intake/router.

Must include:

- Alfred receives operator requests.
- Alfred clarifies ambiguity.
- Alfred creates handoff packets inside the conversation or target artifact.
- Alfred routes to meta_strategist, meta_operations, or meta_detective_controller.
- Alfred does not implement.
- Alfred does not validate final completion.

Next prompt:
`Create File 3 from the fixed sequence: .claude/agents/meta_strategist.md`

## 3. `.claude/agents/meta_strategist.md`

Purpose:

- Define strategy/decomposition role.

Must include:

- Goal interpretation.
- Priority ranking.
- Dependency mapping.
- Risk sequencing.
- Determining what work should happen first.
- Escalating unclear or contradictory requests back to Alfred or meta_detective_controller.

Next prompt:
`Create File 4 from the fixed sequence: .claude/agents/meta_operations.md`

## 4. `.claude/agents/meta_operations.md`

Purpose:

- Define workflow and packaging role.

Must include:

- Convert strategic decisions into workflow specs.
- Convert repeatable procedures into skill specs.
- Produce implementation-ready file contents.
- Maintain handoff compatibility.
- Avoid overriding strategy priorities.
- Avoid final validation veto.

Next prompt:
`Create File 5 from the fixed sequence: .claude/agents/meta_detective_controller.md`

## 5. `.claude/agents/meta_detective_controller.md`

Purpose:

- Define validator/drift-controller role.

Must include:

- Validate role boundaries.
- Check contradictions.
- Detect source drift.
- Verify completion criteria.
- Veto incomplete or unsafe files.
- Produce concrete correction reports.

Next prompt:
`Create File 6 from the fixed sequence: .claude/skills/alfred-intake-router/SKILL.md`

## 6. `.claude/skills/alfred-intake-router/SKILL.md`

Purpose:

- Reusable intake and routing procedure for Alfred.

Must include:

- When to use: every new operator request, unclear task, or request needing role routing.
- Inputs: user request, known constraints, source material, target artifact type.
- Procedure: classify request; detect ambiguity; decide whether clarification is needed; choose target role; produce handoff packet; define next action.
- Output format: route brief + handoff packet.
- Boundary: Alfred routes but does not execute deep work.

Next prompt:
`Create File 7 from the fixed sequence: .claude/skills/handoff-packet-writer/SKILL.md`

## 7. `.claude/skills/handoff-packet-writer/SKILL.md`

Purpose:

- Reusable handoff packet creation skill.

Must include packet fields:

- packet_id
- source_role
- target_role
- objective
- context
- constraints
- inputs
- outputs
- acceptance_criteria
- validation_required
- open_questions
- next_step

Rules:

- Packets must be bounded.
- No hidden assumptions.
- No unassigned ownership.
- Every output must have acceptance criteria.

Next prompt:
`Create File 8 from the fixed sequence: .claude/skills/source-constraint-map/SKILL.md`

## 8. `.claude/skills/source-constraint-map/SKILL.md`

Purpose:

- Reusable source/constraint mapping skill.

Must include:

- Extract facts, assumptions, constraints, contradictions, gaps.
- Separate known facts from inferred assumptions.
- Identify which source controls when sources conflict.
- Identify what must be clarified before execution.
- Produce a compact source-constraint table.

Next prompt:
`Create File 9 from the fixed sequence: .claude/skills/goal-skeleton-fill-verify-loop/SKILL.md`

## 9. `.claude/skills/goal-skeleton-fill-verify-loop/SKILL.md`

Purpose:

- Universal serious-output creation loop.

Must include phases:

1. Intake
2. Goal contract
3. Source and constraint map
4. Divergent options
5. Synthesis and selection
6. Skeleton first
7. Fill
8. Verify
9. Revise
10. Learning capture

Must not reveal chain of thought. Use concise public reasoning summaries only.

Next prompt:
`Create File 10 from the fixed sequence: .claude/skills/detective-validation-gate/SKILL.md`

## 10. `.claude/skills/detective-validation-gate/SKILL.md`

Purpose:

- Reusable validation gate for meta_detective_controller.

Must include checks:

- File path correct.
- One file only.
- Role boundaries respected.
- No extra permanent agents.
- Claude-only terminology.
- No out-of-scope runtime artifacts.
- Completion criteria present.
- Contradictions flagged.
- Next step valid.

Output:

- PASS / FAIL
- Blocking issues
- Non-blocking issues
- Required corrections
- Promotion decision

Next prompt:
`Create File 11 from the fixed sequence: .claude/skills/workflow-normalizer/SKILL.md`

## 11. `.claude/skills/workflow-normalizer/SKILL.md`

Purpose:

- Convert messy chat/source material into Claude workflow definitions.

Must include:

- Identify trigger.
- Identify roles.
- Identify inputs.
- Identify sequence.
- Identify temporary workers if needed.
- Identify outputs.
- Identify validation gates.
- Identify failure handling.
- Produce a workflow spec, not executable code.

Next prompt:
`Create File 12 from the fixed sequence: .claude/workflows/intake_to_handoff.md`

## 12. `.claude/workflows/intake_to_handoff.md`

Purpose:

- Workflow spec for Alfred intake into a handoff packet.

Must include:

- Trigger: new user/operator request.
- Roles: Alfred, optionally meta_detective_controller for ambiguity/validity.
- Steps: intake request; classify; clarify or proceed; select target role; create handoff packet; validate packet completeness.
- Output: handoff packet.

Next prompt:
`Create File 13 from the fixed sequence: .claude/workflows/handoff_to_strategy.md`

## 13. `.claude/workflows/handoff_to_strategy.md`

Purpose:

- Workflow spec for turning a handoff packet into strategic decomposition.

Must include:

- Roles: Alfred, meta_strategist, meta_detective_controller.
- Steps: receive packet; map goal and constraints; rank priorities; map dependencies; define recommended sequence; validate strategic consistency.
- Output: strategy packet.

Next prompt:
`Create File 14 from the fixed sequence: .claude/workflows/strategy_to_operations.md`

## 14. `.claude/workflows/strategy_to_operations.md`

Purpose:

- Workflow spec for turning strategy into operational file/action plan.

Must include:

- Roles: meta_strategist, meta_operations, meta_detective_controller.
- Steps: receive strategy packet; identify file/artifact targets; define operational sequence; package work into one-file-per-step plan; define validation gate.
- Output: operations packet.

Next prompt:
`Create File 15 from the fixed sequence: .claude/workflows/operations_to_detective_validation.md`

## 15. `.claude/workflows/operations_to_detective_validation.md`

Purpose:

- Workflow spec for validating operational outputs.

Must include:

- Roles: meta_operations, meta_detective_controller.
- Steps: receive output; check against packet; check role boundaries; check Claude-only scope; check completion criteria; approve or reject.
- Output: validation report.

Next prompt:
`Create File 16 from the fixed sequence: .claude/workflows/validated_file_creation_loop.md`

## 16. `.claude/workflows/validated_file_creation_loop.md`

Purpose:

- Workflow spec for this exact one-file-per-prompt process.

Must include:

- Fixed sequence rule.
- Exactly one file per prompt.
- No side files.
- Validation checklist after every file.
- Next prompt emitted after every file.
- Stop condition after final file.
- Failure behavior if a file is incomplete or violates scope.

Next prompt:
`Create File 17 from the fixed sequence: .claude/workflows/workflow_index.md`

## 17. `.claude/workflows/workflow_index.md`

Purpose:

- Index of all Claude workflow specs.

Must include:

- Table of all workflow files.
- Trigger for each workflow.
- Roles used.
- Inputs.
- Outputs.
- Validation gate.
- Relationship to skills and agents.

Next prompt:
`STOP. Report that the Claude-ready predefinition set is complete.`

---

# 10. First prompt to start the flow

Use this as the first prompt in a new ChatGPT extended-thinking chat:

```text
You are executing `chatgpt_extended_thinking_file_flow.md` with paired source index `chatgpt_extended_thinking_source_index.md`.

Create File 1 from the fixed sequence: `CLAUDE.md`.

Important:
- You are ChatGPT extended-thinking mode, not Claude.
- You are creating a Claude-ready file to later give to Claude / Claude Code.
- Use the paired source index to decide which project files to inspect.
- Produce exactly one final file.
- Do not create AGENTS.md, SOUL.md, settings, schemas, tests, CI, infrastructure, runtime state, deployment files, or Hermes runtime artifacts.
- Translate all Hermes/OpenCLAW/Apex historical source terms into Claude-ready terms or omit them.
- Follow the global output contract exactly.
```
