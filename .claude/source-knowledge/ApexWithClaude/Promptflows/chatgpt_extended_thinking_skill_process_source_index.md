# Source Index — Claude-Only Skill / Process File Creation

```yaml
source_index_metadata:
  id: chatgpt-extended-thinking-skill-process-source-index-v0-1
  paired_prompt_flow: chatgpt_extended_thinking_skill_process_file_flow.md
  purpose: >
    Route ChatGPT extended-thinking file-generation prompts to the correct
    source groups for creating one Claude-only skill/process file per prompt.
```

---

# 0. Source-router principle

This file decides **where to look** before creating each target skill/process file.

The paired prompt flow decides **how to output** each target file.

```yaml
routing_principles:
  - Use current accepted design-state files first.
  - Use older drafts only to recover details that were not superseded.
  - Use Hermes/OpenCLAW/Alfred sources as logic sources, not as target runtime instructions.
  - Convert every source concept into Claude-native `.claude/skills/*/SKILL.md` or `.claude/workflows/*.md` logic.
  - Do not carry source citation markup into generated target files.
```

---

# 1. Global source priority

```yaml
global_source_priority:
  P0_controller:
    - chatgpt_extended_thinking_skill_process_file_flow.md
    - chatgpt_extended_thinking_skill_process_source_index.md
    - chatgpt_extended_thinking_file_flow.md

  P0_claude_skill_format:
    - SkillSpecification.md
    - SkillCreationBestPractice.md
    - OptimizingSkillDescriptions.md
    - EvaluatingSkills.md
    - SkillsTraining&Examples_Claude.md

  P0_current_architecture_decisions:
    - apex_hermes_orchestration_decisions_v0_1.md
    - Information Process Architecture.txt
    - WeeklyRoutine_Overview_Marco&Meso.md
    - WeeklyRoutine_Detailed_v2(v1maybestillvalid).md
    - Project Flow Validation.txt

  P0_current_core_loop_specs:
    - PreCap Week v0.2.md
    - PreCapNextDay_v1.md
    - PreCapNextDay_Routine_Family_v0_1.md
    - Process Handover Validation.txt
    - Process Specs Validation.txt
    - Information Process Architecture.txt

  P1_source_indexes:
    - SourceIndexAgentInteraction07OC.md
    - SourceIndexAgentInteractionAlfred.md
    - SourceIndexProjectGPT.md
    - Source Index for Hermes AI.txt

  P1_legacy_logic_sources:
    - Hermes Agent - Development Guide.md
    - HermesAgentMasterClass.md
    - BuildORCHESTRATIONSYSTEMINHERMESAGENT_Claude.md
    - WorkflowExamples_Claude.md
    - Q&A_ProfileVsAgents.md
    - Q&A_SwarmOrchestration.md
    - Q&AAgent2Workflows.md
    - Q&A_ProcessBlueprintDefinition.md
    - Q&AWorkflowsWithExamples.md
    - kanban-orchestrator_skill.md
```

---

# 2. Universal translation policy

```yaml
universal_translation_policy:
  source_terms_to_translate:
    Hermes_skill: Claude_Code_SKILL_md
    Hermes_profile: existing_Claude_agent_role_reference
    Hermes_Kanban_graph: Claude_workflow_process_spec
    Hermes_cron: trigger_or_cadence_concept_only
    Hermes_memory: durable_markdown_artifact_or_context_reference
    SOUL_md: role_boundary_material_only_if_already_represented_in_agents
    AGENTS_md: out_of_scope
    OpenCLAW_agent: source_role_pattern_or_handoff_logic
    OpenCLAW_runtime: out_of_scope
    Apex_old_workflow: Claude_skill_or_workflow_file

  target_terms_to_prefer:
    - skill
    - process
    - workflow spec
    - role reference
    - handoff packet
    - artifact
    - input contract
    - output contract
    - operator gate
    - validation check
    - non-goal
```

---

# 3. Target-file source routing

## File 1 — `.claude/skills/flow-recap/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/flow-recap/SKILL.md
  file_type: Claude_skill
  primary_sources:
    - Information Process Architecture.txt
    - Process Handover Validation.txt
    - Process Specs Validation.txt
    - Project Flow Validation.txt
  required_source_topics:
    - FlowRecapSkill as atomic execution-memory unit
    - RawFlowDumpProtocol embedded inside FlowRecap
    - planned_vs_actual execution capture
    - project status delta
    - artifact index
    - model usage delta
    - operator-validated next step
    - skipped or partial flow handling
  target_conversion:
    - Convert FlowRecapSkill into a Claude Code skill named `flow-recap`.
    - Do not mention Hermes runtime.
    - Keep operator trigger explicit.
```

## File 2 — `.claude/skills/prompt-and-ai-routing-planning/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/prompt-and-ai-routing-planning/SKILL.md
  file_type: Claude_skill
  primary_sources:
    - Support Design Spec — PromptAndAIRoutingPlanning_V0.1_Review.md
    - PreCapNextDay_v1.md
    - Process Specs Validation.txt
    - Project Flow Validation.txt
  required_source_topics:
    - prompt packets
    - AI surface inventory
    - model/surface route selection
    - fallback route
    - expected outputs
    - synthesis route
    - recap-capture metadata
    - subscription usage awareness
  target_conversion:
    - Convert the support process into a Claude skill used by PreCapNextDay and related planning processes.
    - Do not claim automatic subscription counter access.
```

## File 3 — `.claude/workflows/precap-week.md`

```yaml
source_routing:
  target_path: .claude/workflows/precap-week.md
  file_type: Claude_process
  primary_sources:
    - PreCap Week v0.2.md
    - WeeklyRoutine_Overview_Marco&Meso.md
    - WeeklyRoutine_Detailed_v2(v1maybestillvalid).md
    - Information Process Architecture.txt
  required_source_topics:
    - weekly planning purpose
    - calendar constraints
    - project status packets
    - weekly leverage prioritization
    - operator review gate
    - handoff to PreCapNextDay
  target_conversion:
    - Convert scheduled/Hermes language into a Claude workflow trigger concept.
    - Do not create cron, calendar, or automation files.
```

## File 4 — `.claude/workflows/precap-next-day.md`

```yaml
source_routing:
  target_path: .claude/workflows/precap-next-day.md
  file_type: Claude_process
  primary_sources:
    - PreCapNextDay_v1.md
    - PreCapNextDay_Routine_Family_v0_1.md
    - Information Process Architecture.txt
    - WeeklyRoutine_Overview_Marco&Meso.md
    - Project Flow Validation.txt
  required_source_topics:
    - fixed four-flow day structure
    - three sprints per flow
    - prompt packets
    - context packets
    - calendar feasibility
    - skipped-flow markers
    - FlowRecap handoff
    - no standalone DayExecution or FlowExecution
  target_conversion:
    - Convert PreCapNextDay into a Claude process/workflow spec.
    - Treat operator execution as human action, not a Claude runtime process.
```

## File 5 — `.claude/skills/status-merge/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/status-merge/SKILL.md
  file_type: Claude_skill
  primary_sources:
    - Routine Design Spec — AllProjectStatusPacketUpdate v0.1_REVIEW.md
    - Information Process Architecture.txt
    - Process Specs Validation.txt
    - Project Flow Validation.txt
  required_source_topics:
    - AllProjectStatusPacketUpdate
    - once-daily/manual status merge
    - consumes FlowRecaps
    - skipped-flow markers
    - consumed recap registry
    - conflict gate
    - next PreCapNextDay context
  target_conversion:
    - Rename future runtime concept to `status-merge` for Claude skill clarity.
    - Do not claim automatic scheduling.
```

## File 6 — `.claude/skills/model-usage-tracking/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/model-usage-tracking/SKILL.md
  file_type: Claude_skill
  primary_sources:
    - Support Design Spec — ModelSubscriptionUsageTracking v0.1_Review.md
    - Support Design Spec — PromptAndAIRoutingPlanning_V0.1_Review.md
    - Information Process Architecture.txt
    - Project Flow Validation.txt
  required_source_topics:
    - planned vs actual AI surface use
    - scarce mode usage
    - route learning
    - prompt quality
    - fallback route notes
    - no automatic subscription counters
  target_conversion:
    - Convert tracking process into manual/structured Claude skill.
    - Keep counters as operator-provided or artifact-derived.
```

## File 7 — `.claude/skills/context-packet-preparation/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/context-packet-preparation/SKILL.md
  file_type: Claude_skill
  primary_sources:
    - PreCapNextDay_Routine_Family_v0_1.md
    - PreCapNextDay_v1.md
    - Information Process Architecture.txt
    - SourceIndexProjectGPT.md
    - SourceIndexAgentInteractionAlfred.md
  required_source_topics:
    - context packet preparation
    - file upload lists
    - source selection
    - prompt packet context
    - compressed context
    - project/resource selection
  target_conversion:
    - Create a Claude skill for preparing context packets for prompts and workflows.
```

## File 8 — `.claude/skills/calendar-block-creation/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/calendar-block-creation/SKILL.md
  file_type: Claude_skill
  primary_sources:
    - PreCap Week v0.2.md
    - PreCapNextDay_v1.md
    - PreCapNextDay_Routine_Family_v0_1.md
    - Information Process Architecture.txt
  required_source_topics:
    - calendar constraints
    - calendar block packet
    - operator approval
    - feasibility check
    - day/week plan translation into time blocks
  target_conversion:
    - Create a Claude skill that drafts calendar block instructions.
    - Do not create actual Google Calendar events or API calls.
```

## File 9 — `.claude/skills/branch-and-chunk-selection/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/branch-and-chunk-selection/SKILL.md
  file_type: Claude_skill
  primary_sources:
    - PreCapNextDay_Routine_Family_v0_1.md
    - Information Process Architecture.txt
    - Process Definition Workflow.txt
    - SourceIndexAgentInteraction07OC.md
    - SourceIndexAgentInteractionAlfred.md
  required_source_topics:
    - branch and chunk selection
    - task slicing
    - dependency order
    - execution mode selection
    - avoid overloading the operator
  target_conversion:
    - Convert task-chunking and routing logic into a Claude skill.
```

## File 10 — `.claude/skills/day-plan-validation/SKILL.md`

```yaml
source_routing:
  target_path: .claude/skills/day-plan-validation/SKILL.md
  file_type: Claude_skill
  primary_sources:
    - PreCapNextDay_v1.md
    - PreCapNextDay_Routine_Family_v0_1.md
    - Routine Design Spec — PreCapNextDay v0.2_Review.md
    - Process Specs Validation.txt
    - Information Process Architecture.txt
  required_source_topics:
    - next-day plan validation
    - four-flow constraints
    - sprint constraints
    - prompt/context completeness
    - operator approval gate
    - feasibility and overload checks
  target_conversion:
    - Create validation skill for checking a PreCapNextDay plan before execution.
```

## File 11 — `.claude/workflows/weekly-daily-flow-loop.md`

```yaml
source_routing:
  target_path: .claude/workflows/weekly-daily-flow-loop.md
  file_type: Claude_process
  primary_sources:
    - Information Process Architecture.txt
    - WeeklyRoutine_Overview_Marco&Meso.md
    - WeeklyRoutine_Detailed_v2(v1maybestillvalid).md
    - PreCap Week v0.2.md
    - PreCapNextDay_v1.md
    - Project Flow Validation.txt
  required_source_topics:
    - PreCapWeek to PreCapNextDay to OperatorExecutesPlannedFlow to FlowRecap to status merge to next PreCapNextDay
    - artifact chain
    - operator gates
    - no standalone DayExecution/FlowExecution
    - status merge does not auto-trigger next day planning in v0.1 unless explicitly changed
  target_conversion:
    - Create a Claude workflow spec that coordinates the generated skills/processes.
```

## File 12 — `.claude/workflows/skill-process-index.md`

```yaml
source_routing:
  target_path: .claude/workflows/skill-process-index.md
  file_type: Claude_process
  primary_sources:
    - chatgpt_extended_thinking_skill_process_file_flow.md
    - chatgpt_extended_thinking_skill_process_source_index.md
    - all previously generated .claude/skills/*/SKILL.md files
    - all previously generated .claude/workflows/*.md files
  required_source_topics:
    - skill/process dependency map
    - trigger map
    - file order
    - when to use which skill
    - how processes chain together
  target_conversion:
    - Create a Claude workflow index, not a runtime registry.
```

---

# 4. Source-selection anti-drift rules

```yaml
anti_drift_rules:
  - If older files still mention DayExecution or FlowExecution as standalone processes, treat those as superseded unless the user explicitly reopens the decision.
  - If a source says Hermes, profile, Kanban, cron, SOUL.md, or AGENTS.md, translate to Claude skill/process language or omit.
  - If a source says workflow is not a Hermes primitive, preserve the lesson as: do not confuse design process specs with runtime automation.
  - If a source contains process examples, use them as concrete examples only if they improve the target file.
  - If a source contains review corrections, apply the corrections rather than reproducing the original mistake.
```

---

# 5. Minimal source-query prompts

When searching uploaded files for a target, use one precision query and one recall query.

Examples:

```yaml
search_query_examples:
  flow_recap:
    precision: FlowRecapSkill raw flow dump project status delta artifact index model usage operator validated next step
    recall: FlowRecap raw dump

  prompt_routing:
    precision: PromptAndAIRoutingPlanning prompt packets AI surface model routing fallback route expected outputs
    recall: prompt routing

  precap_next_day:
    precision: PreCapNextDay four flows three sprints prompt packets context packet FlowRecap handoff
    recall: PreCapNextDay

  status_merge:
    precision: AllProjectStatusPacketUpdate FlowRecap status merge skipped flow marker consumed recap registry
    recall: status merge
```
