# GPT Skill Process Source Index v3 — Claude Skill & Workflow File Creation

```yaml
source_index_metadata:
  id: gpt-skill-process-source-index-v3
  paired_prompt_flow: GPT_Skill_Process_File_Flow_v3.md
  purpose: >
    Route GPT extended-thinking file-generation prompts to the correct project
    source documents for creating one Claude-native skill or workflow file per prompt.
```

---

# 0. Source-router principle

This file decides where GPT should look before generating each target file.

The paired prompt flow decides how GPT must output each target file.

```yaml
routing_principles:
  - Use current accepted design-state files first.
  - Use files in NewVersions as the highest-priority source set when they contain the same target topic.
  - Use review files as patches, corrections, and constraints on top of the base spec.
  - Use older drafts only to recover details that were not superseded.
  - Use examples as grounding/test material, not as output structure unless explicitly useful.
  - Convert every source concept into Claude-native skill or workflow logic.
  - Do not carry source citations, source file names, or source terminology into generated target files.
  - Do not generate files outside `.claude/skills/*/SKILL.md` and `.claude/workflows/*.md`.
```

---

# 1. Global source priority

```yaml
global_source_priority:
  P0_operator_current_instructions:
    rule: >
      Current operator instructions in the active chat override every stored source.

  P0_controller:
    - GPT_Skill_Process_File_Flow_v3.md
    - GPT_Skill_Process_Source_Index_v3.md

  P0_new_versions:
    rule: >
      Files in NewVersions have highest priority when they correspond to a target file
      or supersede a same-topic file outside NewVersions.
    visible_examples:
      - WeeklyRoutine_Detailed.md
      - WeeklyRoutine_Detailed_v2(v1maybestillvalid).md
      - WeeklyRoutine_Overview_Marco&Meso.md

  P0_claude_setup_and_format:
    - ClaudePhase1FilePreparation.md
    - ClaudeSetupGeneral.md
    - Apex_Alfred_Skill_Definition_Guide.md
    - deep-research-report (11).md

  P0_current_loop_and_architecture:
    - Information Process Architecture.txt
    - Information-Process Architecture — Next Work Plan v0.1.md
    - WeeklyRoutine_Overview_Marco&Meso.md
    - Example Flow Package — PreCapNextDay System v0.1.md
    - Apex_Prompt_1_Planning.md
    - Apex_Prompt_2_Preparation.md

  P0_current_design_specs:
    - Skill Design Spec — FlowRecapSkill v0.1.md
    - Support Design Spec — PromptAndAIRoutingPlanning v0.1.md
    - Support Design Spec — ModelSubscriptionUsageTracking v0.1.md
    - Routine Design Spec — PreCapNextDay v0.2.md
    - Routine Design Spec — AllProjectStatusPacketUpdate v0.1.md
    - PreCap Week v0.2.md

  P0_review_corrections:
    rule: >
      Review files do not replace base specs. Apply them as correction and gap
      layers on top of the matching base spec.
    files:
      - Skill Design Spec — FlowRecapSkill v0.1_Review.md
      - Support Design Spec — PromptAndAIRoutingPlanning_V0.1_Review.md
      - Support Design Spec — ModelSubscriptionUsageTracking v0.1_Review.md
      - Routine Design Spec — PreCapNextDay v0.2_Review.md
      - Routine Design Spec — AllProjectStatusPacketUpdate v0.1_REVIEW.md

  P1_weekly_sources:
    - WeeklyRoutine_Detailed_v2(v1maybestillvalid).md
    - WeeklyRoutine_Overview_Marco&Meso.md
    - PreCap Week v0.2.md
    - WeeklyRoutine_Detailed.md

  P2_patch_sources:
    use_only_when_needed:
      - PatchPrecap.md
      - PatchPreCapNextDay.md
      - ProcessDefinitionFB.md
      - ProcessDefinitionFB3.md

  excluded_sources:
    - VerificationByDevineHermesAgentChecklist.md
    - GPTChatHistoryToCreatehProcessDefinitions.md
    - Handover Prompt.md
```

---

# 2. Conflict resolution

```yaml
conflict_resolution_order:
  1: Current operator instructions in the active chat
  2: GPT_Skill_Process_File_Flow_v3.md
  3: GPT_Skill_Process_Source_Index_v3.md
  4: NewVersions files for the same topic
  5: Matching review file corrections
  6: Matching base design spec
  7: Information-process architecture and current loop overview
  8: Claude setup and skill-format guidance
  9: Examples and workflow packages
  10: Low-priority patch sources
  11: Older drafts only for missing details
```

If two sources conflict, preserve the newer accepted architecture and remove old implementation assumptions.

---

# 3. Universal translation policy

```yaml
universal_translation_policy:
  target_terms_to_prefer:
    - skill
    - workflow
    - workflow spec
    - role reference
    - handoff packet
    - artifact
    - input contract
    - output contract
    - operator gate
    - validation check
    - non-goal
    - logical location
    - trigger condition

  generated_target_files_must_not_contain:
    - legacy runtime names
    - source file names
    - old version labels
    - draft markers
    - source citations
    - derivation commentary
    - implementation notes for external automation systems

  preserve:
    - process intent
    - step logic
    - artifact names when already Claude-safe
    - input/output contracts
    - operator gates
    - validation requirements
    - failure modes
    - non-goals
    - anti-regression rules
    - four-flow daily structure
    - three-sprint flow structure
    - flow recap and status merge handoff logic

  convert_or_omit:
    old_runtime_schedule: trigger_condition_only
    old_runtime_task_graph: workflow_step_or_artifact_flow
    old_runtime_identity_boundary: allowed_role_reference_only
    old_runtime_memory: durable_markdown_artifact_or_context_reference
    old_runtime_profile: role_reference
    old_runtime_skill: Claude_SKILL_md
```

---

# 4. File sequence and routing

## File 01 — `.claude/skills/flow-recap/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/flow-recap/SKILL.md
  file_type: Claude_skill

  primary_sources:
    - Skill Design Spec — FlowRecapSkill v0.1.md
    - Skill Design Spec — FlowRecapSkill v0.1_Review.md
    - Information Process Architecture.txt
    - Information-Process Architecture — Next Work Plan v0.1.md
    - WeeklyRoutine_Overview_Marco&Meso.md

  grounding_examples:
    - Example Flow Package — PreCapNextDay System v0.1.md

  low_priority_sources:
    - ProcessDefinitionFB.md
    - ProcessDefinitionFB3.md

  required_source_topics:
    - one-flow recap procedure
    - raw flow dump digestion
    - skipped or partial flow handling
    - planned versus actual execution capture
    - sprint-level summary
    - artifact index
    - prompt result summary
    - model usage delta
    - project status delta
    - reusable learning
    - blocker and open-question detection
    - operator-validated next step
    - future next-day planning context
    - residual flow project-delta splitting

  target_conversion:
    - Create a Claude skill named `flow-recap`.
    - Treat the operator as the executor of the actual work.
    - Treat FlowRecap as the atomic post-flow memory procedure.
    - Include an explicit operator validation gate for next step and status delta.
    - Do not update cross-project status directly.
```

Search prompts:

```yaml
search_queries:
  precision: FlowRecapSkill raw flow dump planned versus actual artifact index project status delta model usage delta operator validated next step
  recall: FlowRecap raw dump
```

---

## File 02 — `.claude/skills/prompt-and-ai-routing-planning/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/prompt-and-ai-routing-planning/SKILL.md
  file_type: Claude_skill

  primary_sources:
    - Support Design Spec — PromptAndAIRoutingPlanning v0.1.md
    - Support Design Spec — PromptAndAIRoutingPlanning_V0.1_Review.md
    - Routine Design Spec — PreCapNextDay v0.2.md
    - Routine Design Spec — PreCapNextDay v0.2_Review.md
    - Information-Process Architecture — Next Work Plan v0.1.md

  grounding_examples:
    - Example Flow Package — PreCapNextDay System v0.1.md

  required_source_topics:
    - flow packet seed
    - prompt packet generation
    - task decomposition
    - AI surface inventory
    - model or mode route selection
    - fallback routes
    - context manifest
    - synthesis plan
    - expected output contract
    - quality checks
    - recap capture requirements
    - usage tracking fields
    - no automatic subscription counter access

  target_conversion:
    - Create a Claude skill named `prompt-and-ai-routing-planning`.
    - Make the AI surface inventory an operator-provided or artifact-provided input.
    - Produce prompt packets and routing recommendations.
    - Do not claim automatic access to subscription counters.
    - Do not execute prompts for the operator.
```

Search prompts:

```yaml
search_queries:
  precision: PromptAndAIRoutingPlanning prompt packets AI surface inventory fallback route synthesis plan recap capture usage tracking
  recall: prompt routing
```

---

## File 03 — `.claude/skills/model-usage-log/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/model-usage-log/SKILL.md
  file_type: Claude_skill

  primary_sources:
    - Support Design Spec — ModelSubscriptionUsageTracking v0.1.md
    - Support Design Spec — ModelSubscriptionUsageTracking v0.1_Review.md
    - Skill Design Spec — FlowRecapSkill v0.1.md
    - Skill Design Spec — FlowRecapSkill v0.1_Review.md
    - Support Design Spec — PromptAndAIRoutingPlanning v0.1.md
    - Support Design Spec — PromptAndAIRoutingPlanning_V0.1_Review.md
    - WeeklyRoutine_Overview_Marco&Meso.md

  required_source_topics:
    - planned versus actual AI surface usage
    - planned versus actual model or mode
    - prompt quality
    - reuse value
    - route repeat or avoid recommendation
    - failed or wasted calls
    - scarce mode usage
    - operator-provided usage notes
    - daily or per-flow usage summary
    - routing recommendations for later planning
    - manual tracking only

  target_conversion:
    - Create a Claude skill named `model-usage-log`.
    - Use operator-provided evidence and flow recap artifacts.
    - Keep the output lightweight and non-blocking.
    - Do not fetch subscription counters automatically.
    - Do not block the core loop when usage evidence is missing.
```

Search prompts:

```yaml
search_queries:
  precision: ModelSubscriptionUsageTracking planned actual AI surface model usage route learning prompt quality scarce mode operator notes
  recall: model usage
```

---

## File 04 — `.claude/skills/precap-next-day/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/precap-next-day/SKILL.md
  file_type: Claude_skill

  primary_sources:
    - Routine Design Spec — PreCapNextDay v0.2.md
    - Routine Design Spec — PreCapNextDay v0.2_Review.md
    - Information-Process Architecture — Next Work Plan v0.1.md
    - WeeklyRoutine_Overview_Marco&Meso.md
    - Apex_Prompt_1_Planning.md

  grounding_examples:
    - Example Flow Package — PreCapNextDay System v0.1.md

  low_priority_sources:
    - PatchPreCapNextDay.md
    - ProcessDefinitionFB.md
    - ProcessDefinitionFB3.md

  required_source_topics:
    - next execution day planning
    - weekly plan context
    - project status context
    - latest flow recap context
    - skipped flow marker handling
    - fixed four-flow structure
    - three-sprint structure
    - prompt packets
    - context instructions
    - model usage summary
    - available AI surface inventory
    - calendar constraints
    - operator approval gate before execution
    - handoff to flow recap
    - no standalone execution process

  target_conversion:
    - Create a Claude skill named `precap-next-day`.
    - Treat it as a repeatable planning skill that produces one next-day plan.
    - Include four flow packets and three sprints per flow.
    - Include prompt packets or invoke the routing-planning skill.
    - Include flow recap instructions for every flow.
    - Do not execute the flows.
```

Search prompts:

```yaml
search_queries:
  precision: PreCapNextDay four flows three sprints prompt packets context instructions skipped flow markers FlowRecap handoff operator approval
  recall: PreCapNextDay
```

---

## File 05 — `.claude/skills/status-merge/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/status-merge/SKILL.md
  file_type: Claude_skill

  primary_sources:
    - Routine Design Spec — AllProjectStatusPacketUpdate v0.1.md
    - Routine Design Spec — AllProjectStatusPacketUpdate v0.1_REVIEW.md
    - Information-Process Architecture — Next Work Plan v0.1
    - WeeklyRoutine_Overview_Marco&Meso.md
    - Apex_Prompt_1_Planning.md

  grounding_examples:
    - Example Flow Package — PreCapNextDay System v0.1.md

  required_source_topics:
    - cross-project status merge
    - previous all-project status packet
    - flow recaps since last merge
    - skipped flow markers
    - consumed recap registry
    - conflict detection
    - project status entries
    - artifact index update
    - blocker updates
    - priority or urgency changes
    - prompt and model route learning
    - next planning context
    - operator gate for conflicts or high-impact changes
    - no automatic next-day planning trigger

  target_conversion:
    - Create a Claude skill named `status-merge`.
    - Merge multiple flow recap artifacts into the canonical project state artifact.
    - Include duplicate-consumption protection.
    - Include conflict and high-impact change gate.
    - Do not execute project work.
    - Do not create the next day plan directly.
```

Search prompts:

```yaml
search_queries:
  precision: AllProjectStatusPacketUpdate status merge FlowRecaps skipped flow markers consumed recap registry conflict gate next PreCapNextDay context
  recall: status merge
```

---

## File 06 — `.claude/skills/precap-week/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/precap-week/SKILL.md
  file_type: Claude_skill

  primary_sources:
    - PreCap Week v0.2.md
    - WeeklyRoutine_Detailed_v2(v1maybestillvalid).md
    - WeeklyRoutine_Overview_Marco&Meso.md
    - Information-Process Architecture — Next Work Plan v0.1
    - Apex_Prompt_1_Planning.md

  secondary_sources:
    - WeeklyRoutine_Detailed.md

  low_priority_sources:
    - PatchPrecap.md

  required_source_topics:
    - weekly direction setting
    - project priority review
    - calendar constraints
    - project status context
    - weekly plan packet
    - day-by-day direction
    - first next-day planning seed
    - operator approval gate
    - no external scheduling or automation setup

  target_conversion:
    - Create a Claude skill named `precap-week`.
    - Treat it as a repeatable weekly planning skill.
    - Produce a weekly plan packet and first next-day planning seed.
    - Include operator approval before downstream use.
    - Do not create calendar events or automation files.
```

Search prompts:

```yaml
search_queries:
  precision: PreCap Week weekly planning project priorities calendar constraints weekly plan packet first PreCapNextDay seed operator review
  recall: PreCap Week
```

---

## File 07 — `.claude/workflows/weekly-daily-flow-loop.md`

```yaml
source_routing:
  target_path: .claude/workflows/weekly-daily-flow-loop.md
  file_type: Claude_workflow

  primary_sources:
    - WeeklyRoutine_Overview_Marco&Meso.md
    - Information-Process Architecture — Next Work Plan v0.1.md
    - Apex_Prompt_1_Planning.md
    - Routine Design Spec — PreCapNextDay v0.2.md
    - Skill Design Spec — FlowRecapSkill v0.1.md
    - Routine Design Spec — AllProjectStatusPacketUpdate v0.1.md
    - PreCap Week v0.2.md

  include_previously_generated_files:
    - .claude/skills/flow-recap/SKILL.md
    - .claude/skills/prompt-and-ai-routing-planning/SKILL.md
    - .claude/skills/model-usage-log/SKILL.md
    - .claude/skills/precap-next-day/SKILL.md
    - .claude/skills/status-merge/SKILL.md
    - .claude/skills/precap-week/SKILL.md

  required_source_topics:
    - complete planning to execution support to recap to status merge loop
    - PreCapWeek to PreCapNextDay handoff
    - operator execution as human action
    - FlowRecap after each flow
    - model usage logging as lightweight support
    - status merge once daily or manually
    - artifact chain
    - operator gates
    - no standalone execution process
    - no automatic project work
    - no workflow index in this flow

  target_conversion:
    - Create a Claude workflow spec that coordinates the generated skills.
    - Do not define new skills inside the workflow.
    - Do not create a workflow index.
    - Do not add external scheduling or automation.
    - Preserve all operator gates.
```

Search prompts:

```yaml
search_queries:
  precision: PreCapWeek PreCapNextDay OperatorExecutesPlannedFlow FlowRecap status merge artifact chain operator gates weekly daily flow loop
  recall: weekly daily flow loop
```

---

# 5. Source-specific handling rules

```yaml
source_handling_rules:
  review_files:
    rule: >
      Treat review files as correction layers. Apply their corrections and gap
      notes silently when generating the target file. Do not reproduce review
      wording or meta-analysis in the generated file.

  new_versions:
    rule: >
      Prefer NewVersions files when they cover the same topic. If a NewVersions
      file conflicts with an older base file, use the NewVersions logic unless
      the operator says otherwise.

  weekly_detailed_v2:
    rule: >
      Treat WeeklyRoutine_Detailed_v2(v1maybestillvalid).md as the strongest
      detailed weekly source. Use WeeklyRoutine_Overview_Marco&Meso.md for
      macro and meso loop clarity.

  example_package:
    rule: >
      Use Example Flow Package — PreCapNextDay System v0.1.md as a concrete
      test fixture for flow, sprint, prompt packet, raw dump, recap, and residual
      handling. Do not copy example-specific project text unless the target file
      needs a generic pattern.

  patch_sources:
    rule: >
      Use PatchPrecap.md and PatchPreCapNextDay.md only when primary and review
      sources leave a gap.

  excluded_sources:
    rule: >
      Do not use excluded sources for target-file generation.
```

---

# 6. Anti-drift rules

```yaml
anti_drift_rules:
  - Do not revive standalone day execution as a generated file.
  - Do not revive standalone flow execution as a generated file.
  - Do not make the operator's actual work an automated Claude process.
  - Do not create new permanent roles.
  - Do not create identity files.
  - Do not create external automation, scheduler, task-board, calendar, CI, or deployment files.
  - Do not store large structured artifacts as memory instructions.
  - Do not allow status merge to silently resolve conflicts.
  - Do not allow status merge to automatically create the next day plan.
  - Do not allow PreCapNextDay to execute flows.
  - Do not allow FlowRecap to update the all-project status packet directly.
  - Do not allow model usage logging to claim automatic access to real subscription counters.
  - Do not include source terminology in generated target files.
```

---

# 7. Minimal source-loading protocol for the later chat

For every target file, the later chat should:

```yaml
source_loading_protocol:
  1_identify_target:
    - Read target path from the operator prompt.
    - Locate the matching File NN entry in this source index.

  2_load_sources:
    - Load primary sources first.
    - Load matching review sources as correction layers.
    - Load grounding examples only when needed.
    - Load low-priority patch sources only if a required topic remains unresolved.
    - Do not load excluded sources.

  3_extract:
    - Extract process intent.
    - Extract trigger conditions.
    - Extract required inputs.
    - Extract required outputs.
    - Extract operator gates.
    - Extract artifact handoffs.
    - Extract validation checks.
    - Extract failure modes and non-goals.
    - Extract open questions only if still execution-relevant.

  4_translate:
    - Convert all source logic into Claude-native file structure.
    - Remove banned terms.
    - Remove source metadata.
    - Remove derivation commentary.
    - Remove old version history.

  5_validate:
    - Apply the pre-output validation pass from GPT_Skill_Process_File_Flow_v3.md.
    - Output exactly one complete file, checklist, and next prompt.
```

---

# 8. Next prompt chain

```yaml
next_prompt_chain:
  file_01:
    target: .claude/skills/flow-recap/SKILL.md
    next_target: .claude/skills/prompt-and-ai-routing-planning/SKILL.md

  file_02:
    target: .claude/skills/prompt-and-ai-routing-planning/SKILL.md
    next_target: .claude/skills/model-usage-log/SKILL.md

  file_03:
    target: .claude/skills/model-usage-log/SKILL.md
    next_target: .claude/skills/precap-next-day/SKILL.md

  file_04:
    target: .claude/skills/precap-next-day/SKILL.md
    next_target: .claude/skills/status-merge/SKILL.md

  file_05:
    target: .claude/skills/status-merge/SKILL.md
    next_target: .claude/skills/precap-week/SKILL.md

  file_06:
    target: .claude/skills/precap-week/SKILL.md
    next_target: .claude/workflows/weekly-daily-flow-loop.md

  file_07:
    target: .claude/workflows/weekly-daily-flow-loop.md
    next_target: none
    completion_message: >
      The Claude-native skill and workflow file flow is complete.
```