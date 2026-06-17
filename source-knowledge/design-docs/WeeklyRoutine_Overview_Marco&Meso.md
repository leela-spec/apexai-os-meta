# Two-Level Overview — PreCap / FlowRecap / Status-Merge Loop

## 1. Macro overview — very high-level process and information flow

### Core idea

The system is a **planning → execution → recap → status merge → next planning** loop.

It does not execute the operator’s work automatically. It creates structured plans, the operator works from those plans, then the system converts messy execution evidence into durable project state.

```yaml
macro_loop:
  1_PreCapWeek:
    function: define_weekly_direction
    input: previous_project_state_and_operator_intent
    output: weekly_plan_packet
    validation: operator_approves_weekly_direction
    sends_to: PreCapNextDay

  2_PreCapNextDay:
    function: turn_weekly_direction_into_executable_day_plan
    input: weekly_plan_packet_plus_current_project_state
    output: next_day_plan_with_four_flow_packets
    validation: operator_approves_next_day_plan
    sends_to: Operator

  3_OperatorExecutesPlannedFlow:
    function: human_executes_the_planned_work
    input: approved_flow_packet_and_prompt_packets
    output: raw_flow_dump_or_skipped_flow_marker
    validation: operator_marks_flow_done_partial_skipped_or_blocked
    sends_to: FlowRecap

  4_FlowRecap:
    function: digest_one_flow_into_structured_execution_memory
    input: original_flow_packet_plus_raw_flow_dump
    output: flow_recap_packet
    validation: operator_validates_next_step_and_status_delta
    sends_to: APSU

  5_APSU_StatusMerge:
    function: merge_all_flow_recaps_into_canonical_project_state
    input: unconsumed_flow_recaps_and_previous_status_packet
    output: updated_all_project_status_packet_and_next_PreCapNextDay_context
    validation: operator_reviews_only_conflicts_or_high_impact_changes
    sends_to: next_PreCapNextDay

  6_NextCycle:
    function: use_updated_state_to_plan_next_execution_day
    input: updated_status_packet_plus_next_day_context
    output: next_day_plan
    validation: operator_approves_before_execution
```

### Macro interpretation

1. **Weekly plan:** PreCapWeek creates the strategic container for the week.
    
2. **Daily plan:** PreCapNextDay translates the week into one executable day.
    
3. **Human work:** Operator executes one planned flow at a time.
    
4. **Flow memory:** FlowRecap turns messy execution evidence into structured memory.
    
5. **Project state:** APSU merges flow-level memory into project-level state.
    
6. **Next planning seed:** APSU prepares the information base for the next PreCapNextDay, but does not automatically trigger it in v0.1.
    

### Macro output chain

```yaml
macro_artifact_chain:
  weekly_plan_packet:
    produced_by: PreCapWeek
    consumed_by: PreCapNextDay

  next_day_plan:
    produced_by: PreCapNextDay
    consumed_by: Operator

  flow_packet:
    produced_by: PreCapNextDay
    consumed_by:
      - Operator
      - FlowRecap

  raw_flow_dump:
    produced_by: Operator
    consumed_by: FlowRecap

  flow_recap_packet:
    produced_by: FlowRecap
    consumed_by: APSU

  updated_all_project_status_packet:
    produced_by: APSU
    consumed_by:
      - PreCapNextDay
      - PreCapWeek

  next_PreCapNextDay_input_context:
    produced_by: APSU
    consumed_by: PreCapNextDay
```

### Macro operator gates

```yaml
macro_operator_gates:
  G1_weekly_plan:
    position: after_PreCapWeek
    strictness: always_required

  G2_next_day_plan:
    position: after_PreCapNextDay
    strictness: always_required

  G3_flow_completion:
    position: after_operator_executes_flow
    strictness: always_required

  G4_flow_recap:
    position: during_FlowRecap
    strictness: next_step_and_status_delta_required

  G5_status_merge:
    position: during_APSU
    strictness: only_conflicts_high_impact_or_ambiguity
```

---

## 2. Meso overview — process and information flow with more detail

## Stage 1 — PreCapWeek

### Function

PreCapWeek creates the weekly planning frame.

It decides what the week is trying to accomplish across the main projects and prepares the seed for the first PreCapNextDay.

### Input flow

```yaml
PreCapWeek_inputs:
  previous_all_project_status_packet:
    function: shows_current_project_state

  previous_week_summary_or_operator_context:
    function: shows_what_recently_happened

  project_priority_notes:
    function: shows_what_matters_most

  calendar_constraints:
    function: prevents_unrealistic_week_plan

  operator_weekly_intent:
    function: preserves_human_direction
```

### Processing logic

1. **Collect:** Gather project state, priorities, constraints, and intent.
    
2. **Normalize:** Convert scattered context into project-level planning inputs.
    
3. **Prioritize:** Rank Leela, MasterOfArts, Apex/Hermes, and residual pressure.
    
4. **Allocate:** Define weekly direction and execution-day emphasis.
    
5. **Draft:** Create the weekly plan packet.
    
6. **Validate:** Operator approves or edits.
    
7. **Publish:** Approved weekly plan becomes the source for PreCapNextDay.
    

### Output flow

```yaml
PreCapWeek_outputs:
  weekly_plan_packet:
    contains:
      - week_id
      - project_weekly_goals
      - daily_flow_structure
      - constraints
      - first_PreCapNextDay_seed
      - operator_validation
    sent_to:
      - PreCapNextDay
```

---

## Stage 2 — PreCapNextDay

### Function

PreCapNextDay converts the weekly plan and current project state into one executable day.

It creates the four fixed flows:

```yaml
fixed_daily_flows:
  F1: Leela
  F2: MasterOfArts
  F3: ApexAI_or_Hermes_orchestration
  F4: Residual
```

Each flow has:

```yaml
flow_sprints:
  S1: first_work_sprint
  S2: second_work_sprint
  S3: recap_planning_digest_sprint
```

### Input flow

```yaml
PreCapNextDay_inputs:
  weekly_plan_packet:
    function: gives_weekly_strategy

  all_project_status_packet:
    function: gives_current_project_state

  next_PreCapNextDay_input_context:
    function: gives_latest_status_merge_seed

  latest_flow_recaps:
    function: gives_recent_execution_learning

  skipped_flow_markers:
    function: shows_unfinished_or_recovery_work

  usage_summary:
    function: informs_AI_routing

  AI_surface_inventory:
    function: shows_available_models_and_surfaces

  calendar_constraints:
    function: shapes_realistic_day_plan
```

### Processing logic

1. **Collect:** Read weekly plan, status, recaps, skipped markers, usage, calendar.
    
2. **Validate inputs:** Mark missing or stale inputs.
    
3. **Select day:** Define execution_day_id.
    
4. **Instantiate structure:** Create F1/F2/F3/F4 skeleton.
    
5. **Assign goals:** Map current project state into each flow.
    
6. **Apply residual logic:** Decide what F4 recovers or deepens.
    
7. **Generate sprints:** Define S1/S2/S3 for each flow.
    
8. **Generate prompt packets:** Add model/surface routing and expected outputs.
    
9. **Embed context:** Put required context instructions inside each flow packet.
    
10. **Define raw dump requirements:** Specify what must be captured during S3.
    
11. **Add recap handoff:** Tell FlowRecap what it will need later.
    
12. **Validate:** Operator approves or edits the day plan.
    
13. **Publish:** Save next_day_plan and extract per-flow flow packets.
    

### Output flow

```yaml
PreCapNextDay_outputs:
  next_day_plan:
    function: whole_day_operator_view
    contains:
      - execution_day_id
      - four_flow_sequence
      - constraints
      - risk_notes
      - operator_gate

  flow_packets:
    function: per_flow_execution_and_recap_source
    storage_rule: embedded_in_next_day_plan_plus_extractable_per_flow_file

  prompt_packets:
    function: per_sprint_AI_execution_instructions
    storage_rule: embedded_inside_flow_packet

  raw_dump_instructions:
    function: define_what_operator_must_capture_for_FlowRecap
```

---

## Stage 3 — OperatorExecutesPlannedFlow

### Function

The operator executes the planned flow manually.

This is not a Hermes process. It is the human work layer.

### Input flow

```yaml
Operator_inputs:
  approved_next_day_plan:
    function: whole_day_context

  selected_flow_packet:
    function: exact_flow_instruction

  prompt_packets:
    function: AI_prompt_execution_plan

  context_instructions:
    function: tells_operator_what_context_to_include

  expected_outputs:
    function: defines_done_or_partial_done
```

### Processing logic

1. **Select:** Pick the next approved flow.
    
2. **Prepare:** Open flow packet and collect context.
    
3. **Execute S1:** Do first work sprint.
    
4. **Execute S2:** Do second work sprint.
    
5. **Execute S3:** Collect recap/digest material.
    
6. **Classify:** Mark flow as completed, partial, skipped, blocked, aborted, or moved.
    
7. **Dump:** Normalize evidence into one RawFlowDump markdown artifact.
    
8. **Handoff:** Send raw dump to FlowRecap.
    

### Output flow

```yaml
Operator_outputs:
  raw_flow_dump:
    produced_if: flow_completed_or_partially_completed
    contains:
      - flow_id
      - execution_day_id
      - what_happened
      - prompt_outputs
      - artifacts
      - decisions
      - blockers
      - model_usage_notes
      - next_step_guess

  skipped_flow_marker:
    produced_if: flow_skipped_or_no_meaningful_work_done
    contains:
      - flow_id
      - reason
      - project
      - recovery_note
```

---

## Stage 4 — RawFlowDump normalization

### Function

The raw dump is the input gate between human execution and system memory.

It accepts messy human material, but normalizes it into one markdown artifact per flow.

### Input forms

```yaml
accepted_raw_dump_inputs:
  - pasted_chat_history
  - uploaded_markdown_file
  - AI_chat_links
  - artifact_paths
  - created_or_edited_files
  - operator_voice_or_text_notes
  - decisions
  - blockers
  - unfinished_items
  - model_usage_notes
```

### Normalization rule

```yaml
raw_dump_rule:
  before_FlowRecap_runs:
    must_exist: one_raw_flow_dump_markdown_file_per_flow
    minimum_fields:
      - execution_day_id
      - flow_id
      - completion_state
      - what_happened
      - outputs_or_skip_reason
```

---

## Stage 5 — FlowRecap

### Function

FlowRecap converts one planned flow plus its raw dump into structured execution memory.

It is the atomic post-flow memory unit.

### Input flow

```yaml
FlowRecap_inputs:
  original_flow_packet:
    function: shows_what_was_planned

  raw_flow_dump:
    function: shows_what_actually_happened

  prompt_packets:
    function: enables_prompt_result_evaluation

  artifact_references:
    function: enables_output_indexing

  model_usage_notes:
    function: enables_usage_delta_capture
```

### Processing logic

1. **Load:** Read flow packet and raw dump.
    
2. **Validate:** Check flow_id, execution_day_id, completion state.
    
3. **Compare:** Planned versus actual.
    
4. **Summarize:** S1/S2/S3 result.
    
5. **Index:** Extract artifacts.
    
6. **Evaluate prompts:** Summarize prompt quality and route value.
    
7. **Extract project delta:** Define what changed in the project.
    
8. **Extract usage delta:** Capture model/surface usage.
    
9. **Detect blockers:** List blockers and unresolved questions.
    
10. **Propose next step:** Draft next executable chunk.
    
11. **Validate:** Operator approves or edits next step and status delta.
    
12. **Publish:** Save flow_recap_packet.
    

### Output flow

```yaml
FlowRecap_outputs:
  flow_recap_packet:
    contains:
      - planned_vs_actual
      - sprint_level_summary
      - artifact_index
      - prompt_result_summary
      - project_status_delta
      - model_usage_delta
      - reusable_learning
      - next_step_proposal
      - operator_validated_next_step
      - future_PreCapNextDay_context
    sent_to:
      - APSU
      - model_usage_log_optional
      - future_PreCapNextDay_indirectly
```

### F4 residual rule

```yaml
F4_residual_rule:
  one_flow_recap: true
  split_project_deltas:
    F4_S1: Leela
    F4_S2: MasterOfArts
    F4_S3: ApexAI_or_Hermes_orchestration
```

---

## Stage 6 — Model usage logging

### Function

Model usage tracking is lightweight in v0.1.

It should not block the core loop.

### Input flow

```yaml
model_usage_inputs:
  planned_prompt_packets:
    source: PreCapNextDay

  actual_model_usage_delta:
    source: FlowRecap

  operator_usage_notes:
    source: raw_flow_dump_or_FlowRecap
```

### Output flow

```yaml
model_usage_outputs:
  model_usage_delta:
    storage: section_inside_flow_recap_packet

  usage_summary:
    status: optional_in_v0_1
    used_by:
      - PreCapNextDay
      - APSU
```

---

## Stage 7 — APSU / status-merge

### Function

APSU merges all flow-level recaps into the canonical project-level status packet.

It runs once daily or manually, not after every flow.

### Input flow

```yaml
APSU_inputs:
  previous_all_project_status_packet:
    function: baseline_project_state

  flow_recap_packets_since_last_merge:
    function: new_execution_memory

  skipped_flow_markers:
    function: unfinished_or_recovery_context

  consumed_flow_recap_registry:
    function: prevents_duplicate_merges

  usage_summary:
    function: optional_routing_context

  operator_merge_notes:
    function: optional_human_override_or_context
```

### Processing logic

1. **Collect:** Gather unconsumed flow recaps and skipped markers.
    
2. **Deduplicate:** Check consumed recap registry.
    
3. **Validate:** Check whether recaps have required fields.
    
4. **Split residual:** Convert F4 residual into project-specific deltas.
    
5. **Merge Leela:** Merge F1 + F4_S1 status.
    
6. **Merge MasterOfArts:** Merge F2 + F4_S2 status.
    
7. **Merge Apex/Hermes:** Merge F3 + F4_S3 status.
    
8. **Merge blockers:** Add, resolve, or carry blockers.
    
9. **Merge artifacts:** Add artifact references into project status.
    
10. **Merge usage:** Add route/usage notes if available.
    
11. **Detect conflicts:** Flag contradictions or risky status changes.
    
12. **Generate next chunks:** Define next executable project chunks.
    
13. **Prepare next context:** Create next_PreCapNextDay_input_context.
    
14. **Validate if needed:** Operator reviews only high-impact/conflicted changes.
    
15. **Publish:** Save updated status packet and next context.
    
16. **Register:** Mark consumed flow recaps.
    

### Output flow

```yaml
APSU_outputs:
  updated_all_project_status_packet:
    function: canonical_project_state
    consumed_by:
      - PreCapNextDay
      - PreCapWeek

  next_PreCapNextDay_input_context:
    function: next_daily_planning_seed
    consumed_by:
      - PreCapNextDay

  consumed_flow_recap_registry:
    function: prevents_duplicate_status_merges
    consumed_by:
      - APSU_next_run
```

---

## Stage 8 — Next PreCapNextDay

### Function

The next PreCapNextDay uses APSU’s updated status and context, but APSU does not auto-trigger it in v0.1.

### Input flow

```yaml
next_cycle_inputs:
  updated_all_project_status_packet:
    function: latest_project_state

  next_PreCapNextDay_input_context:
    function: next_day_seed

  weekly_plan_packet:
    function: weekly_strategy_anchor

  calendar_constraints:
    function: feasibility_check
```

### Trigger rule

```yaml
APSU_to_PreCapNextDay:
  v0_1:
    trigger: operator_manual_start
    APSU_does:
      - write_updated_status_packet
      - write_next_context
      - report_ready_or_blocked_state
    APSU_does_not:
      - create_cron_job
      - directly_run_next_PreCapNextDay
      - silently_create_duplicate_task

  future_v0_2:
    allowed_after_runtime_decisions:
      - APSU_creates_PreCapNextDay_Kanban_task
    requires:
      - real_profile_names
      - absolute_paths
      - idempotency_keys
      - validated_Kanban_task_ownership
```

---

# Compressed meso flow in one chain

```yaml
compressed_meso_chain:
  1:
    process: PreCapWeek
    reads: current_project_state_plus_operator_weekly_intent
    writes: weekly_plan_packet
    gate: weekly_plan_operator_approval

  2:
    process: PreCapNextDay
    reads: weekly_plan_packet_plus_status_packet_plus_recent_context
    writes:
      - next_day_plan
      - F1_to_F4_flow_packets
      - prompt_packets
      - raw_dump_instructions
    gate: next_day_plan_operator_approval

  3:
    process: OperatorExecutesPlannedFlow
    reads: approved_flow_packet
    writes:
      - raw_flow_dump
      - skipped_flow_marker_if_needed
    gate: flow_completion_state_confirmation

  4:
    process: FlowRecap
    reads: flow_packet_plus_raw_flow_dump
    writes:
      - flow_recap_packet
      - project_status_delta
      - model_usage_delta
      - operator_validated_next_step
    gate: next_step_and_status_delta_validation

  5:
    process: APSU
    reads: unconsumed_flow_recaps_plus_previous_status_packet
    writes:
      - updated_all_project_status_packet
      - next_PreCapNextDay_input_context
      - consumed_flow_recap_registry
    gate: only_conflicts_or_high_impact_changes

  6:
    process: next_PreCapNextDay
    reads: updated_status_packet_plus_next_context_plus_weekly_plan
    writes: next_day_plan
    gate: operator_manual_trigger_and_validation
```