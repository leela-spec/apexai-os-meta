# FILE: CLAUDE.md

# Section 1 — System Identity

Apex is a v0.1 Claude-native orchestration system for Marco. It creates structured plans, lets Marco execute the work, then converts execution evidence into durable project state.

# Section 2 — Core Loop

```
core_loop:  1:    process: PreCapWeek    writes: weekly_plan_packet    gate: weekly_plan_operator_approval  2:    process: PreCapNextDay    writes: next_day_plan    gate: next_day_plan_operator_approval  3:    process: OperatorExecutesPlannedFlow    writes: raw_flow_dump_or_skipped_flow_marker    gate: flow_completion_state_confirmation  4:    process: FlowRecap    writes: flow_recap_packet    gate: next_step_and_status_delta_validation  5:    process: APSU    writes: updated_all_project_status_packet    gate: only_conflicts_or_high_impact_changes  6:    process: next_PreCapNextDay    writes: next_day_plan    gate: operator_manual_trigger_and_validation
```

# Section 3 — Operator Gates

```
operator_gates:  G1: {position: after_PreCapWeek, strictness: always_required}  G2: {position: after_PreCapNextDay, strictness: always_required}  G3: {position: after_operator_executes_flow, strictness: always_required}  G4: {position: during_FlowRecap, strictness: next_step_and_status_delta_required}  G5: {position: during_APSU, strictness: only_conflicts_high_impact_or_ambiguity}
```

# Section 4 — Skill Index

skills:
  PrecapNextDay:
    trigger_phrase: "run precap-next-day"
    skill_path: .claude/skills/PrecapNextDay/Skill_precap-next-day.md
    input_artifact: best_available_context
    output_artifact: next_day_plan
    operator_gate: G2
    status: present
  PrecapWeek:
    trigger_phrase: "run precap-week"
    skill_path: .claude/skills/PrecapWeek/Skill_Precap-Week.md
    input_artifact: weekly_intent
    output_artifact: precap_week_output
    operator_gate: G1
    status: present
  ProjectStatus:
    trigger_phrase: "run project-status-overview"
    skill_path: .claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md
    input_artifact: manual_notes
    output_artifact: current_project_status_overview
    operator_gate: none
    status: present
  AIRouting:
    trigger_phrase: "run ai-routing-and-usage-tracking"
    skill_path: .claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md
    input_artifact: operator_task
    output_artifact: routing_recommendation_packet
    operator_gate: none
    status: present
  PromptEngineer:
    trigger_phrase: "run prompt-engineering"
    skill_path: .claude/skills/PromptEngineer/SKILL_prompt-engineering.md
    input_artifact: operator_task
    output_artifact: prompt_packet
    operator_gate: none
    status: present
  WorkflowProcesses:
    trigger_phrase: "run workflow-process-design"
    skill_path: .claude/skills/Workflow&Processes/workflow-process-design-SKILL.md
    input_artifact: operator_task
    output_artifact: workflow_process_validation_summary
    operator_gate: none
    status: present
  FlowRecap:
    trigger_phrase: "run flow-recap"
    skill_path: .claude/skills/flow-recap/Skill_flow-recap.md
    input_artifact: flow_packet_plus_raw_flow_dump
    output_artifact: flow_recap_packet
    operator_gate: G4
    status: missing
  StatusMerge:
    trigger_phrase: "run status-merge"
    skill_path: .claude/skills/status-merge/Skill_status-merge.md
    input_artifact: flow_recap_packets_plus_apex_project_status
    output_artifact: updated_all_project_status_packet
    operator_gate: G5
    status: missing
  RawFlowDumpNormalize:
    trigger_phrase: "run raw-flow-dump-normalize"
    skill_path: .claude/skills/raw-flow-dump-normalize/Skill_raw-flow-dump-normalize.md
    input_artifact: raw_operator_input
    output_artifact: raw_flow_dump
    operator_gate: none
    status: missing
  ModelUsageLog:
    trigger_phrase: "run model-usage-log"
    skill_path: .claude/skills/model-usage-log/Skill_model-usage-log.md
    input_artifact: flow_recap_packet
    output_artifact: model_usage_delta
    operator_gate: none
    status: missing

# Section 5 — Artifact Paths

```
artifact_paths:  apex_project_status: state/apex-project-status.md  consumed_recap_registry: state/consumed-recap-registry.md  weekly_plan_packets: artifacts/weekly-plans/  next_day_plans: artifacts/next-day-plans/  flow_packets: artifacts/flow-packets/  flow_recap_packets: artifacts/flow-recap-packets/
```

# Section 6 — Session Startup Protocol

session_startup:
  1: Read CLAUDE.md.
  2: Read state/apex-project-status.md.
  3: Confirm skill status — present vs missing — from Section 4.
  4: Do not execute anything until Marco issues a trigger phrase.

# Section 7 — Claude Behavior Rules

## 7a. Allowed actions

- Read active skill files under .claude/skills/.
- Read state and artifacts needed for a triggered skill.
- Produce one requested output artifact.
- Report missing inputs and conflicts.

## 7b. Forbidden actions

- Do not write files into source-knowledge/.
- Do not auto-trigger any skill without operator instruction.
- Do not create cron jobs or schedulers.
- Do not create Kanban tasks or calendar events automatically.
- Do not overwrite state/ files — append or flag conflicts only.
- Do not load files from source-knowledge/ unless operator requests skill conversion.
- Do not batch-write multiple output files without operator confirmation.
- Do not use the terms listed in Section 8.

## 7c. Missing input handling

If a required input artifact is missing when a skill is triggered, halt, report which file is missing, and ask Marco to provide it before proceeding.

## 7d. Output write behavior

Write the file, then report done in one summary line.

