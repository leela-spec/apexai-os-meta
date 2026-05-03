Yes. The broad Q&A was already mostly answered and was too redundant. The remaining Q&A should only lock the still-undefined operational templates.

Also: I am applying the decision-lock correction: **Alfred only**. No separate current-system Sid actor. The working file says the current-system personal assistant is Alfred, and current-system user stories/templates must not use future app naming.

# Targeted Q&A Lock — unresolved definitions only

## A. Daily Command Board template

### A1. What project packets appear?

|Field|Proposed answer|
|---|---|
|**Question**|Which project packets should Alfred include in the Daily Command Board?|
|**Proposed answer**|Include only packets from active projects that have a valid Night output, Session Export, OpState delta, operator request, hard deadline, or unresolved blocker relevant to the next working day.|
|**Options**|all project packets / only top-priority packets / active relevant packets|
|**Recommendation**|**Active relevant packets only.** Avoid dumping every project into the day board.|
|**Validation status**|Proposed|

**Packet inclusion rule:**

```yaml
include_project_packet_if:
  - has_night_output: true
  - has_session_export_delta: true
  - has_operator_requested_attention: true
  - has_deadline_within_window: true
  - has_blocker_requiring_operator_judgment: true
  - is_default_lane_project: true # Leela or Master of Arts
exclude_if:
  - stale_without_new_delta: true
  - no_actionable_next_step: true
  - blocked_without_operator_action: true
```

### A2. What does a project packet contain?

|Field|Proposed answer|
|---|---|
|**Question**|What fields must each project packet expose to Alfred?|
|**Proposed answer**|Each packet must expose project, source artifact, proposed next tasks, priority signals, blockers, required operator decisions, expected outputs, and MetaOps readiness.|
|**Options**|minimal / operational / full trace|
|**Recommendation**|**Operational packet.** Enough for planning, not full history.|
|**Validation status**|Proposed|

```yaml
project_packet_v0:
  project_id:
  project_name:
  source_artifacts:
    - night_plan:
    - session_exports:
    - opstate:
    - handout:
  proposed_next_tasks:
    - task:
      expected_output:
      owner_candidate:
      estimated_fit:
      blockers:
  priority_signals:
    deadline_pressure: 0-5
    strategic_value: 0-5
    dependency_unlock: 0-5
    default_lane_relevance: 0-3
    readiness: 0-5
    risk_if_deferred: 0-5
  operator_decisions_needed: []
  metaops_ready:
    ready: true|false
    missing_inputs: []
```

### A3. What priority/ranking metrics are visible?

|Field|Proposed answer|
|---|---|
|**Question**|Which ranking metrics should Alfred show to the operator?|
|**Proposed answer**|Show a compact visible score with the main reasons: deadline pressure, strategic value, dependency unlock, readiness, calendar fit, default lane alignment, risk if deferred.|
|**Options**|hidden ranking / visible simple reason / visible score table|
|**Recommendation**|**Visible score table plus human-readable reason.**|
|**Validation status**|Proposed|

```yaml
visible_priority_metrics_v0:
  deadline_pressure: 0-5
  strategic_value: 0-5
  dependency_unlock: 0-5
  readiness_of_inputs: 0-5
  calendar_fit: 0-5
  default_lane_alignment: 0-3
  risk_if_deferred: 0-5
  confidence: high|medium|low
  visible_reason:
```

**Example display:**

|Rank|Project|Score reason|Confidence|
|--:|---|---|---|
|1|Leela|default lane + dependency unlock + ready inputs|high|
|2|Master of Arts|deadline pressure + strategic value|medium|
|3|Wildcard project|urgent blocker but weak readiness|low|

### A4. How are the four craft flows displayed?

|Field|Proposed answer|
|---|---|
|**Question**|How should the four workday craft flows appear in the Daily Command Board?|
|**Proposed answer**|Display them as four session cards with lane, project, target output, Sprint Alex template, physical/mental chunks, MetaOps handoff, success condition, and editable fields.|
|**Options**|list / cards / schedule grid|
|**Recommendation**|**Cards inside a day schedule.**|
|**Validation status**|Proposed|

```yaml
craft_flow_card_v0:
  flow_id: CF1|CF2|CF3|CF4
  lane: leela_1|leela_2|master_of_arts|wildcard
  proposed_time_window:
  project:
  target_output:
  expected_outputs: []
  why_this_flow:
  craft_template: Sprint Alex
  sprint_structure:
    sprints: 3
    per_sprint: "2 activity + 3 mental + 1 pre-cap + 28 deep work + 1 re-cap"
    final_break_min: 15
  physical_chunk_candidate:
  mental_chunk_candidate:
  regen_or_break_chunk:
  metaops_handoff:
    needed: true
    brief_id:
  success_condition:
  operator_editable_fields: []
```

### A5. What is editable by the operator?

|Field|Proposed answer|
|---|---|
|**Question**|Which Daily Command Board fields can the operator edit during morning review?|
|**Proposed answer**|Operator can edit priority order, flow assignment, time windows, target outputs, chunk choices, constraints, deferred items, and override notes.|
|**Options**|none / limited / broad|
|**Recommendation**|**Broad correction, but tracked.** Edits should become planning feedback.|
|**Validation status**|Proposed|

```yaml
operator_editable_fields:
  - priority_order
  - flow_project_assignment
  - target_output
  - expected_outputs
  - time_window
  - physical_chunk_candidate
  - mental_chunk_candidate
  - defer_or_swap_decision
  - constraints
  - override_reason
track_operator_edits_as:
  - preference_signal
  - planning_correction
  - pattern_candidate
  - algorithm_training_signal_future
```

### A6. What gets sent to MetaOps?

|Field|Proposed answer|
|---|---|
|**Question**|What should Alfred send to MetaOps after the Daily Command Board is accepted or corrected?|
|**Proposed answer**|Send one Craft Flow Handoff per work session requiring project execution structure.|
|**Options**|full board / one handoff per flow / raw tasks|
|**Recommendation**|**One handoff per flow.**|
|**Validation status**|Proposed|

```yaml
metaops_craft_flow_handoff_v0:
  handoff_id:
  flow_id:
  project_id:
  target_output:
  expected_outputs: []
  priority_reason:
  source_artifacts: []
  constraints:
    time_container_min: 120
    sprint_template: Sprint Alex
    must_use: []
    must_avoid: []
  requested_metaops_outputs:
    - sprint_workflow
    - prompt_chain
    - task_sequence
    - AI_routing_plan
    - acceptance_criteria
    - final_session_export_expectation
  stop_condition:
  return_to: Alfred
```

### A7. What gets tracked from the board?

|Field|Proposed answer|
|---|---|
|**Question**|What board-level data should become tracking input?|
|**Proposed answer**|Track planned vs. accepted board, operator edits, flow assignments, deferred items, and later actual completion.|
|**Options**|no tracking / final plan only / proposed plus corrected plus actual|
|**Recommendation**|**Track proposed → corrected → actual.** This is crucial for learning.|
|**Validation status**|Proposed|

```yaml
daily_board_tracking_v0:
  proposed_by_alfred:
    priority_order: []
    craft_flows: []
  corrected_by_operator:
    priority_order_changes: []
    flow_assignment_changes: []
    target_output_changes: []
    chunk_changes: []
    defer_changes: []
  actual_by_day_end:
    completed_flows: []
    partial_flows: []
    missed_flows: []
    major_deviations: []
  learning_candidates:
    - planning_pattern
    - operator_preference
    - recurring_constraint
    - ranking_error
```

---

## B. Expected Session Export Scaffold

### B1. What does Night pre-fill?

|Field|Proposed answer|
|---|---|
|**Question**|What should Night pre-fill before the session happens?|
|**Proposed answer**|Night pre-fills intended objective, expected outputs, planned sprints, anticipated next tasks, likely blockers, source artifacts, and expected MetaOps workflow.|
|**Options**|minimal / operational / detailed prediction|
|**Recommendation**|**Operational prediction.** Enough to correct quickly after the session.|
|**Validation status**|Proposed|

```yaml
night_prefill_v0:
  session_identity:
    date:
    flow_id:
    project_id:
    session_type:
    lane:
  intended_objective:
  expected_outputs: []
  planned_sprints:
    - sprint_id:
      focus:
      expected_output:
      metaops_prompt_or_task:
  anticipated_next_highest_impact_tasks: []
  anticipated_blockers: []
  source_artifacts: []
  expected_workflow_package:
  open_questions_for_operator: []
```

### B2. What does the operator correct?

|Field|Proposed answer|
|---|---|
|**Question**|What should the operator correct after the craft flow?|
|**Proposed answer**|Correct actual outputs, sprint completion, deviations, blockers, next tasks, changed priorities, created artifacts, and whether the workflow worked.|
|**Options**|freeform / checklist / structured correction|
|**Recommendation**|**Structured correction with optional notes.**|
|**Validation status**|Proposed|

```yaml
operator_correction_v0:
  actual_outputs: []
  sprints_completed: 0|1|2|3
  planned_vs_actual:
    matched:
    changed:
    skipped:
  deviations:
    - deviation:
      reason:
  blockers_found: []
  next_highest_impact_tasks: []
  priority_changes: []
  artifacts_created_or_updated: []
  workflow_effectiveness:
    process_worked: yes|mixed|no|unknown
    chat_flow_efficiency: high|medium|low|unknown
  notes_optional:
```

### B3. What does Alfred check?

|Field|Proposed answer|
|---|---|
|**Question**|What should Alfred check after the operator correction?|
|**Proposed answer**|Alfred checks completeness, contradictions, next-action clarity, priority implications, pattern candidates, chunk candidates, and whether MetaOps/Night need additional processing.|
|**Options**|no check / validation only / synthesis check|
|**Recommendation**|**Synthesis check.**|
|**Validation status**|Proposed|

```yaml
alfred_post_session_check_v0:
  completeness:
    planned_output_accounted_for: true|false
    actual_output_recorded: true|false
    next_task_defined: true|false
    blocker_status_clear: true|false
  synthesis:
    priority_changed: true|false
    project_state_changed: true|false
    needs_metaops_processing: true|false
    needs_night_attention: true|false
  candidates:
    pattern_candidates: []
    chunk_candidates: []
    kb_candidates: []
    workflow_improvement_candidates: []
  warnings:
    - missing_trace
    - unclear_next_action
    - unresolved_blocker
    - possible_hygiene_issue
```

### B4. What does MetaOps receive?

|Field|Proposed answer|
|---|---|
|**Question**|What should MetaOps receive from the corrected Session Export?|
|**Proposed answer**|MetaOps receives actual outputs, unresolved work, next highest-impact tasks, blockers, workflow-efficiency feedback, and requested overnight processing.|
|**Options**|full export / filtered MetaOps packet / raw notes|
|**Recommendation**|**Filtered MetaOps packet derived from export.**|
|**Validation status**|Proposed|

```yaml
metaops_session_packet_v0:
  source_session_export:
  project_id:
  actual_outputs: []
  unfinished_outputs: []
  next_highest_impact_tasks: []
  blockers: []
  required_overnight_processing:
    - research
    - synthesis
    - workflow_generation
    - prompt_chain_improvement
    - validation
    - handout_generation
  workflow_feedback:
    process_worked:
    chat_flow_efficiency:
    failure_points: []
  return_expected:
    - next_day_project_packet
    - proposed_craft_flow_target
    - priority_signal
    - blockers_or_decisions_needed
```

### B5. What becomes a Pattern Library candidate?

|Field|Proposed answer|
|---|---|
|**Question**|What events in the Session Export should become pattern candidates?|
|**Proposed answer**|Repeated success, repeated failure, operator correction, unexpectedly efficient workflow, recurring blocker, useful chunk combination, or effective handoff structure.|
|**Options**|repeated only / success only / success + failure + correction|
|**Recommendation**|**Success + failure + correction.**|
|**Validation status**|Proposed|

```yaml
pattern_candidate_trigger_v0:
  create_candidate_if:
    repeated_success: true
    repeated_failure: true
    operator_corrected_same_field_repeatedly: true
    workflow_efficiency_high: true
    workflow_efficiency_low: true
    recurring_blocker: true
    useful_chunk_combo: true
    effective_metaops_handoff: true
  candidate_fields:
    pattern_type:
    evidence_sessions: []
    observed_effect:
    proposed_reuse_rule:
    confidence: low|medium|high
    needs_kb_review: true
```

### B6. What goes into OpState?

|Field|Proposed answer|
|---|---|
|**Question**|Which Session Export information should become an OpState update candidate?|
|**Proposed answer**|Only live project state changes: active/blocked/next/done/hold status, current next action, blocker, owner, or decision needed. Not pattern learning or full trace.|
|**Options**|full export / state delta only / nothing|
|**Recommendation**|**State delta only.**|
|**Validation status**|Proposed|

```yaml
opstate_delta_candidate_v0:
  project_id:
  from_session_export:
  state_changes:
    active_work_changed: true|false
    blocked_work_changed: true|false
    next_action_changed: true|false
    hold_opened_or_closed: true|false
  new_next_action:
  blocker:
  owner_or_execution_surface:
  operator_decision_needed:
  confidence:
  should_update_opstate: true|false
```

---

## C. Tracking v1

## C0. Tracking principle

|Field|Proposed answer|
|---|---|
|**Question**|What is the tracking posture for v1?|
|**Proposed answer**|Track enough to learn from execution without turning the process into burdensome quantified self-work. No mood/energy tracking in v1.|
|**Options**|no tracking / minimal / detailed|
|**Recommendation**|**Minimal structured tracking.**|
|**Validation status**|Proposed|

### C1. Exact v1 tracking fields

|Field|Required?|Proposed values|Notes|
|---|--:|---|---|
|`date`|yes|ISO date|Needed for daily/weekly aggregation.|
|`flow_id`|yes|CF1–CF4|Maps to four-flow day.|
|`lane`|yes|`leela_1`, `leela_2`, `master_of_arts`, `wildcard`|Default allocation learning.|
|`project_id`|yes|string|Project-level trace.|
|`planned_objective`|yes|text|From Daily Command Board.|
|`actual_outcome`|yes|text|Operator correction.|
|`planned_outputs`|yes|list|Expected outputs.|
|`actual_outputs`|yes|list|Produced outputs.|
|`sprints_completed`|yes|0/1/2/3|Better than yes/no only.|
|`flow_completion`|yes|`complete`, `partial`, `missed`, `aborted`|Board-level actual.|
|`next_highest_impact_task`|yes|text/list|Feeds Night.|
|`blockers`|yes|list|Feeds MetaOps/Night.|
|`deviation_reason`|yes if changed|enum + note|Explains drift.|
|`process_worked`|yes|`yes`, `mixed`, `no`, `unknown`|Pattern signal.|
|`chat_flow_efficiency`|yes|`high`, `medium`, `low`, `unknown`|Workflow learning.|
|`pattern_candidate`|optional|list|Candidate only.|
|`chunk_candidate`|optional|list|Candidate only.|
|`mood`|no|excluded|Future maybe.|
|`energy`|no|excluded|Future maybe.|

### C2. Exact tracking schema

```yaml
tracking_record_v1:
  identity:
    date:
    flow_id: CF1|CF2|CF3|CF4
    lane: leela_1|leela_2|master_of_arts|wildcard
    project_id:
    session_export_id:
  planned:
    objective:
    outputs: []
    time_window:
    craft_template: Sprint Alex
    physical_chunk:
    mental_chunk:
    metaops_workflow_id:
  actual:
    flow_completion: complete|partial|missed|aborted
    sprints_completed: 0|1|2|3
    outputs: []
    next_highest_impact_tasks: []
    blockers: []
    deviation_reason:
      type: calendar|scope|blocker|operator_choice|workflow_failure|unknown
      note:
  process_learning:
    process_worked: yes|mixed|no|unknown
    chat_flow_efficiency: high|medium|low|unknown
    useful_prompt_or_workflow:
    failed_prompt_or_workflow:
  candidates:
    pattern_candidates: []
    chunk_candidates: []
    kb_candidates: []
  excluded_v1:
    mood: not_tracked
    energy: not_tracked
    bp_xp: not_authoritative
```

### C3. How does tracking roll up?

|Field|Proposed answer|
|---|---|
|**Question**|What should Alfred do with tracking records?|
|**Proposed answer**|Roll them into day review, weekly Rhythm review, pattern candidate register, and future Algorithm evidence.|
|**Options**|store only / daily only / daily + weekly + pattern|
|**Recommendation**|**Daily + weekly + pattern.**|
|**Validation status**|Proposed|

```yaml
tracking_rollup_v1:
  daily:
    completed_flows:
    missed_or_partial_flows:
    major_deviations:
    next_day_candidates:
  weekly:
    lane_balance:
    recurring_blockers:
    workflow_efficiency_patterns:
    planning_accuracy:
  pattern_library:
    new_candidates:
    strengthened_candidates:
    rejected_candidates:
  future_algorithm_evidence:
    ranking_errors:
    default_lane_overrides:
    calendar_fit_misses:
    dependency_unlock_successes:
```

---

## D. Rhythm logic

## D0. Rhythm definition lock

|Field|Proposed answer|
|---|---|
|**Question**|What is Rhythm for Alfred?|
|**Proposed answer**|Rhythm is Alfred’s gamified life/time planning logic for placing work, branches, and regeneration across days, weeks, and eventually months.|
|**Options**|app feature / separate agent / planning logic|
|**Recommendation**|**Planning logic / KB reference first.**|
|**Validation status**|Proposed|

---

## D1. How does Alfred plan one day?

|Field|Proposed answer|
|---|---|
|**Question**|What is Alfred’s one-day Rhythm logic?|
|**Proposed answer**|Alfred protects the four craft-flow workday, places sessions into available windows, applies project priority, includes physical/mental chunk candidates, and keeps afterwork regeneration outside the four flows.|
|**Options**|schedule only / priority only / integrated|
|**Recommendation**|**Integrated day placement.**|
|**Validation status**|Proposed|

```yaml
rhythm_day_plan_v0:
  inputs:
    calendar_reality:
    night_project_packets:
    default_four_flow_policy:
    project_priorities:
    operator_constraints:
  process:
    - identify_available_work_windows
    - protect_four_craft_flow_slots_if_possible
    - assign_default_lanes
    - apply_priority_overrides_with_tradeoff_notes
    - place physical_and_mental_chunk_candidates
    - reserve_afterwork_regen
  outputs:
    daily_command_board:
    metaops_handoffs:
    risks_and_repairs:
```

---

## D2. How does Alfred plan one week?

|Field|Proposed answer|
|---|---|
|**Question**|What is Alfred’s weekly Rhythm logic?|
|**Proposed answer**|Alfred creates a weekly craft-flow allocation map that balances default lanes, known deadlines, calendar constraints, project momentum, and regeneration needs.|
|**Options**|no week planning / simple calendar / weekly Rhythm plan|
|**Recommendation**|**Weekly Rhythm Plan in v1.1 or early v1 if needed.**|
|**Validation status**|Proposed|

```yaml
alfred_weekly_rhythm_plan_v0:
  week_start:
  source_inputs:
    calendar_week:
    active_project_packets:
    prior_week_tracking_rollup:
    known_deadlines:
  default_capacity:
    planned_workdays:
    craft_flows_per_day: 4
  allocation:
    leela_flows_target:
    master_of_arts_flows_target:
    wildcard_flows_target:
    protected_deep_work_windows: []
  risk_controls:
    overload_days: []
    underfilled_days: []
    deadline_conflicts: []
    required_operator_decisions: []
  output:
    week_flow_map:
    daily_board_seeds:
    metaops_preparation_requests:
```

---

## D3. How does Alfred plan one month?

|Field|Proposed answer|
|---|---|
|**Question**|What is Alfred’s monthly Rhythm logic?|
|**Proposed answer**|Alfred should not micromanage a month. He should create a monthly direction map: major themes, deadline clusters, protected project arcs, expected weekly emphasis, and risk periods.|
|**Options**|no monthly / detailed month schedule / direction map|
|**Recommendation**|**Monthly Direction Map, not detailed schedule.**|
|**Validation status**|Proposed|

```yaml
alfred_monthly_direction_map_v0:
  month:
  major_themes:
    - theme:
      projects:
      desired_outcomes:
  deadline_clusters: []
  protected_arcs:
    leela:
    master_of_arts:
    other:
  weekly_emphasis:
    - week:
      emphasis:
      risks:
  known_low_capacity_periods: []
  review_points: []
```

---

## D4. How does Rhythm handle the four craft-flow workday?

|Field|Proposed answer|
|---|---|
|**Question**|How should Rhythm logic treat the four craft-flow workday?|
|**Proposed answer**|Treat four craft flows as the normal workday structure and only reduce or override them when calendar reality or explicit operator override makes them impossible.|
|**Options**|rigid / flexible / discarded|
|**Recommendation**|**Protected baseline with explicit override.**|
|**Validation status**|Proposed|

```yaml
four_flow_protection_rule:
  default: protect_4_flows
  reduce_only_if:
    - calendar_reality_blocks
    - explicit_operator_override
    - degraded_day_declared
  if_reduced:
    - name_lost_flow
    - name_displaced_project
    - name_recovery_or_reschedule_plan
```

---

## D5. How does Alfred plan afterwork regeneration?

|Field|Proposed answer|
|---|---|
|**Question**|Where does afterwork regeneration sit?|
|**Proposed answer**|Afterwork regeneration is outside the four work craft flows. Alfred may plan it lightly as part of daily Rhythm, but it does not normally replace a work flow.|
|**Options**|inside four flows / after work / optional only|
|**Recommendation**|**After work, lightly planned.**|
|**Validation status**|Proposed|

```yaml
afterwork_regen_v0:
  placement: after_four_work_flows
  purpose:
    - downshift
    - recovery
    - body_reset
    - next_day_readiness
  examples:
    - walk
    - mobility
    - sauna_or_shower
    - easy reading
    - social_time
    - shutdown_ritual
  tracking:
    required: false
    optional_note: true
```

---

## D6. How does Alfred handle calendar conflicts?

|Field|Proposed answer|
|---|---|
|**Question**|How should Rhythm logic handle calendar conflicts?|
|**Proposed answer**|Alfred reads hard locks, identifies which craft flows fit, compresses or reschedules only with explicit tradeoffs, and never silently mutates calendar.|
|**Options**|ignore / auto-reschedule / recommend repair|
|**Recommendation**|**Recommend repair.**|
|**Validation status**|Proposed|

```yaml
calendar_conflict_rule_v0:
  if_hard_lock_blocks_flow:
    - identify_lost_time
    - propose_compressed_or_shifted_flow
    - name_displaced_output
    - ask_or_apply_standing_rule
  never:
    - silently_delete_flow
    - silently_move_calendar_event
    - hide_tradeoff
```

---

## D7. How does Alfred handle project priority conflicts?

|Field|Proposed answer|
|---|---|
|**Question**|How should Alfred resolve project priority conflicts?|
|**Proposed answer**|Alfred scores conflict candidates, checks default lanes, deadlines, dependency unlock, readiness, and risk if deferred, then names the tradeoff.|
|**Options**|default always wins / deadline always wins / weighted tradeoff|
|**Recommendation**|**Weighted tradeoff with visible reason.**|
|**Validation status**|Proposed|

```yaml
project_priority_conflict_v0:
  compare:
    - deadline_pressure
    - strategic_value
    - dependency_unlock
    - readiness
    - default_lane_alignment
    - risk_if_deferred
    - calendar_fit
  output:
    recommended_flow_assignment:
    displaced_work:
    reason:
    confidence:
    operator_decision_needed:
```

---

## D8. How does Alfred balance physical/mental/regen branches?

|Field|Proposed answer|
|---|---|
|**Question**|How should Alfred balance physical, mental, and regen branches?|
|**Proposed answer**|Each craft flow includes physical and mental chunks by default; regen appears as the final break/reset inside a flow and larger afterwork regeneration outside the four flows. Alfred should rotate candidates to avoid monotony and build useful pattern data.|
|**Options**|ignore / fixed chunks / rotating candidates|
|**Recommendation**|**Rotating candidates with operator correction.**|
|**Validation status**|Proposed|

```yaml
branch_balance_v0:
  per_craft_flow:
    physical_chunk: required_candidate
    mental_chunk: required_candidate
    final_break_or_reset: required
  afterwork:
    regen_block: optional_recommended
  rotation_logic:
    avoid_repeating_same_physical_chunk_too_often: true
    avoid_overloading_body_area: true
    align_mental_chunk_with_work_type: true
    allow_operator_correction: true
  tracking:
    physical_chunk_candidate: yes
    mental_chunk_candidate: yes
    regen_afterwork: optional
```

---

# Final validation list

Please validate or correct these **four locks**:

|Lock|Proposed default|
|---|---|
|**Daily Command Board**|Operational board with project packets, visible ranking, four craft-flow cards, operator edits, MetaOps handoffs, and proposed→corrected→actual tracking.|
|**Expected Session Export Scaffold**|Night pre-fills; operator corrects; Alfred checks; MetaOps receives filtered processing packet; OpState receives state delta only.|
|**Tracking v1**|Minimal structured tracking: planned/actual flow, outputs, sprint completion, next task, blocker, process/chat efficiency, pattern/chunk candidates; no mood/energy.|
|**Rhythm logic**|Alfred reference logic for day/week/month planning, four-flow protection, afterwork regen, calendar conflict repair, priority conflict tradeoffs, and branch balance.|