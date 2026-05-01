# APEX_VARIABLES_HANDOFF_DECISION_LOCK

## 0. File role

```yaml
file_id: APEX_VARIABLES_HANDOFF_DECISION_LOCK
repo: leela-spec/apexai-os-meta
path: managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
status: locked_working_decision_file
canonical_status: non_canonical_until_promoted
parent_context_lock: managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
purpose: lock Apex orientation variables, P-class routing, artifact contracts, handoff schemas, trace/state rules, tracking, pattern learning, and planning defaults after operator validation
owner: operator_and_alfred_workflow_design
update_rule: update only when a newer operator decision supersedes this file
promotion_rule: may be promoted into Alfred KB appendices/canonical files through normal source/audit/promotion discipline
```

This file locks the accepted decisions from the Apex Variables & Metrics Q&A. It does not replace the broader Alfred workflow decision lock. It specializes and resolves the earlier open decisions about project orientation, Daily Command Board structure, Session Export / OpState separation, MetaOps handoff design, tracking, pattern promotion, and Rhythm planning.

---

## 0.1 Supersession rule

- **Decision:** All recommendations in the final Apex Variables & Handoffs Q&A are accepted by the operator.
- **Decision:** This file supersedes older variable names, older scoring drafts, older expanded metric lists, and older schema variants where conflicts exist.
- **Decision:** This file inherits the Alfred-only naming rule from `ALFRED_WORKFLOW_DECISION_LOCK.md`.
- **Constraint:** Do not introduce a separate current-system personal assistant actor.
- **Constraint:** Do not treat the future Leela app as the current runtime.
- **Constraint:** Do not silently mutate SSOT, OpState, calendar, or canonical KB truth from these artifacts.

---

## 1. Source basis

```yaml
source_basis:
  operator_validation:
    - "All recommendations are accepted."
  research_inputs:
    - Variables&Metrics.md
    - Variables&Metrics_GEM.md
    - Variables&Metrics_Claude.md
  prior_working_context:
    - managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
    - managed/agent_kb/alfred/working/ALFRED_WORKFLOW_PREFILLED_QA.md
```

The research consensus supports a simplified four-variable orientation core, P-class routing, State-Delta-Trace separation, SBAR-style handoff minimums, candidate-to-canonical pattern learning, and low-friction tracking. This file locks the accepted synthesis for Apex AI.

---

## 2. Final decision summary

| # | Decision | Locked value |
|---:|---|---|
| 1 | Core orientation variables | `value`, `urgency`, `leverage`, `fit` |
| 2 | Score scale | 0-3 only |
| 3 | Second variable name | `urgency`, not `time_pressure` |
| 4 | Risk if deferred | absorbed by `urgency` |
| 5 | Effort | excluded in v1; absorbed by `fit` |
| 6 | Confidence | control/display modifier, not score |
| 7 | Policy lane | guardrail, not score |
| 8 | Hard flags | pre-score routing short-circuit |
| 9 | Priority model | P0-P3 classification, no weighted sum |
| 10 | P1 capacity | max 4 assigned craft-flow items per day |
| 11 | Universal artifact contract | Identity, Source, Intent, Orientation where needed, Routing, State Effect |
| 12 | Orientation required | only for planning/routing artifacts |
| 13 | Project Packet | final v1 schema locked below |
| 14 | Daily Command Board | final v1 schema with separate `rhythm_profile` locked below |
| 15 | MetaOps handoff | mandatory + optional outputs locked below |
| 16 | Session Export | immutable trace after submission |
| 17 | OpState update | delta candidate only |
| 18 | OpState approval | operator required in v1 |
| 19 | Pattern candidate threshold | create after >=2 evidence signals |
| 20 | Pattern promotion | 3 successful uses + operator approval + KB Ops placement |
| 21 | Tracking | minimal structured; process enums required |
| 22 | Mood/energy/BP-XP | excluded from v1 |
| 23 | P0 handling | surface before normal allocation; no auto-assign by default |
| 24 | Board mutation | no mutation after operator lock; revision only |
| 25 | Weekly planning | v1 light preview; v1.1 full Weekly Rhythm Plan |
| 26 | Monthly planning | later; directional only when used |

---

## 3. Apex Orientation Core v1

```yaml
apex_orientation_core_v1:
  core_scores:
    value: 0|1|2|3
    urgency: 0|1|2|3
    leverage: 0|1|2|3
    fit: 0|1|2|3

  controls:
    confidence: low|medium|high
    policy_lane: leela|master_of_arts|wildcard|none

  hard_flags:
    - hard_deadline
    - blocked
    - missing_input
    - operator_decision_needed
    - hygiene_hold
    - calendar_conflict
    - no_actionable_next_step

  output:
    priority_class: P0|P1|P2|P3
    recommended_route:
    visible_reason:
    operator_decision_needed: true|false
```

### 3.1 Variable definitions

| Variable | Definition | Practical question | Absorbs |
|---|---|---|---|
| `value` | Worth of the outcome if completed. | Why does this matter? | strategic value, importance, long-term relevance |
| `urgency` | Penalty or loss created by delay. | Why now? | deadline pressure, risk if deferred, time pressure |
| `leverage` | Unlocking or compounding effect. | What does this enable or unblock? | dependency unlock, blocker removal, opportunity enablement |
| `fit` | Practical executability in the proposed slot/context. | Can this actually be acted on now? | readiness, calendar fit, operator constraints, input availability, effective effort |

### 3.2 Scale definitions

```yaml
score_scale_0_3:
  0: none_or_not_applicable
  1: low
  2: medium_or_workable
  3: high_or_strong
```

```yaml
urgency:
  0: no meaningful penalty if deferred
  1: useful soon, but safe to defer
  2: should happen in the current planning window
  3: delay creates real loss, deadline risk, or blocked downstream work
```

```yaml
fit:
  0: cannot act now
  1: possible only with major friction or missing inputs
  2: workable with manageable constraints
  3: ready, well-scoped, and well-matched to the available container
```

### 3.3 Removed or absorbed fields

```yaml
removed_or_absorbed_fields:
  strategic_value: value
  deadline_pressure: urgency
  time_pressure: urgency
  risk_if_deferred: urgency
  dependency_unlock: leverage
  readiness_of_inputs: fit
  calendar_fit: fit
  operator_constraint_fit: fit
  effort: fit
  default_lane_alignment: policy_lane
```

---

## 4. Controls and hard flags

### 4.1 Confidence

```yaml
confidence:
  status: control_display_modifier
  not: score_variable
  values:
    low: evidence weak; expose assumption; may require discovery or operator check
    medium: sufficient for planning, but not fully verified
    high: evidence strong enough for normal routing
```

```yaml
low_confidence_routing:
  if: confidence == low and fit <= 1
  route: discovery_or_clarification
  else_if: confidence == low
  route: execution_handoff_with_warning
```

### 4.2 Policy lane

```yaml
policy_lane:
  status: guardrail
  not: score_variable
  values:
    leela: normally eligible for CF1 or CF2
    master_of_arts: normally eligible for CF3
    wildcard: normally eligible for CF4
    none: no standing lane protection
```

### 4.3 Hard flag routing

Hard flags are evaluated before normal V/U/L/F classification.

```yaml
hard_flag_routing_v1:
  blocked: route_to_unblock_or_defer
  missing_input: route_to_input_request_or_discovery
  operator_decision_needed: route_to_operator_decision
  hygiene_hold: route_to_hygiene_resolution
  calendar_conflict: route_to_rhythm_repair
  hard_deadline: evaluate_as_P0_candidate
  no_actionable_next_step: route_to_MetaOps_or_Night_for_clarification
```

---

## 5. Priority Class rules v1

Apex uses classification rules, not weighted score totals.

```yaml
priority_class_rules_v1:
  precheck:
    if hard_flags contains hygiene_hold:
      priority_class: P0
      route: hygiene_resolution
    if hard_flags contains operator_decision_needed and blocks_downstream == true:
      priority_class: P0
      route: operator_decision
    if hard_flags contains calendar_conflict and no_alternate_window == true:
      priority_class: P0
      route: rhythm_repair
    if hard_flags contains blocked or missing_input:
      priority_class: P3
      route: unblock_or_clarify

  P0:
    rule: hard_deadline == true and urgency == 3
    meaning: must_handle_now
    route: surface_before_normal_allocation

  P1:
    rule_any:
      - value >= 2 and fit >= 2
      - urgency == 3 and fit >= 1
      - leverage == 3 and fit >= 2
    meaning: should_receive_craft_flow_today
    cap: max_4_per_day

  P2:
    rule: policy_lane != none and fit >= 2 and no_hard_flags
    meaning: valid_default_lane_work

  P3:
    rule_any:
      - fit <= 1
      - no_actionable_next_step
      - stale_without_delta
      - blocked
      - missing_input
    meaning: defer_backlog_clarify_or_block
```

### 5.1 P1 capacity rule

```yaml
p1_capacity_rule:
  max_assigned_per_day: 4
  overflow_destination: deferred_or_not_today
  overflow_requires:
    - reason
    - recommended_revisit
    - displaced_by
```

### 5.2 P0 handling

```yaml
p0_handling_v1:
  auto_assign_to_flow: false
  display_surface: risks_and_repairs
  requires_operator_confirmation: true
```

---

## 6. Universal artifact contract

### 6.1 Minimum metadata for all artifacts

```yaml
mandatory_all_artifacts:
  artifact_id:
  artifact_type:
  created_by:
  created_at:
  source_artifacts: []
  target_consumer:
```

`project_id` is mandatory only for project-bound artifacts. Some Alfred/Rhythm artifacts may be day-bound rather than project-bound.

### 6.2 Full contract for planning/routing artifacts

```yaml
apex_artifact_contract_v1:
  identity:
    artifact_id:
    artifact_type:
    project_id:
    created_by:
    created_at:
    target_consumer:
  source_basis:
    source_artifacts: []
    evidence_quality: low|medium|high
  intent:
    objective:
    expected_outputs: []
    decision_needed: true|false
  orientation:
    value: 0-3
    urgency: 0-3
    leverage: 0-3
    fit: 0-3
    confidence: low|medium|high
    policy_lane: leela|master_of_arts|wildcard|none
    hard_flags: []
    priority_class: P0|P1|P2|P3
  routing:
    requested_action:
    owner_or_next_surface:
    stop_condition:
    return_to:
  state_effect:
    opstate_delta_candidate: true|false
    pattern_candidate: true|false
    kb_candidate: true|false
```

### 6.3 Orientation applicability

```yaml
orientation_required_for:
  - project_packet
  - daily_priority_stack_item
  - craft_flow_handoff

orientation_optional_for:
  - night_plan_item
  - risk_or_repair_item

orientation_not_required_for:
  - session_export_trace
  - opstate_delta_candidate
  - pattern_candidate
  - tracking_record
```

---

## 7. Project Packet v1

A Project Packet is a compact, cycle-specific planning input that tells Alfred what work is available, why it matters, whether it is actionable, and how it should route.

```yaml
project_packet_v1:
  identity:
    packet_id:
    project_id:
    created_by: Night|MetaOps|OpState|Operator
    created_at:
    source_artifacts: []

  proposed_work:
    task:
    expected_outputs: []     # max 4
    next_action:

  orientation:
    value: 0-3
    urgency: 0-3
    leverage: 0-3
    fit: 0-3
    confidence: low|medium|high
    policy_lane: leela|master_of_arts|wildcard|none
    hard_flags: []
    priority_class: P0|P1|P2|P3
    visible_reason:

  routing:
    recommended_flow: CF1|CF2|CF3|CF4|none
    requested_metaops_action:
    operator_decision_needed: true|false

  state_effect:
    opstate_delta_candidate: true|false
    pattern_candidate: true|false
    kb_candidate: true|false
```

---

## 8. Daily Command Board v1

The Daily Command Board separates work-session planning from Rhythm branch/chunk planning. Craft-flow cards reference a `rhythm_profile` rather than carrying all physical/mental/regen detail inline.

```yaml
daily_command_board_v1:
  identity:
    board_id:
    date:
    generated_at:
    created_by: Alfred
    source_window:
    source_artifacts: []
    operator_locked: false

  calendar_reality:
    hard_locks: []
    available_work_windows: []
    calendar_conflicts: []

  daily_priority_stack:
    - project_packet_id:
      priority_class:
      visible_reason:
      confidence:
      hard_flags: []

  craft_flows:
    - flow_id: CF1|CF2|CF3|CF4
      lane: leela_1|leela_2|master_of_arts|wildcard
      time_window:
      project_id:
      objective:
      expected_outputs: []
      craft_template: Sprint Alex
      metaops_handoff_needed: true|false
      operator_decision_needed: true|false
      operator_locked: false
      rhythm_profile_ref:

  rhythm_profile:
    physical_chunk_candidates_by_flow:
      CF1:
      CF2:
      CF3:
      CF4:
    mental_chunk_candidates_by_flow:
      CF1:
      CF2:
      CF3:
      CF4:
    final_break_or_reset:
    afterwork_regen_plan:

  deferred_or_not_today:
    - project_packet_id:
      reason:
      revisit_rule:

  risks_and_repairs:
    - risk:
      priority_class: P0
      repair:
      decision_needed:

  tracking_seed:
    proposed_plan_hash:
    operator_edit_log: []
```

### 8.1 Board lock rule

```yaml
board_lock_rule:
  before_operator_lock: editable
  after_operator_lock: immutable
  changes_after_lock: create_daily_board_revision
```

---

## 9. MetaOps Craft Flow Handoff v1

Alfred does not over-prescribe MetaOps internals. Handoff includes mandatory outputs for interoperability and optional outputs for richer workflows.

```yaml
metaops_craft_flow_handoff_v1:
  identity:
    handoff_id:
    flow_id:
    project_id:
    created_by: Alfred
    created_at:
    source_artifacts: []

  intent:
    target_output:
    expected_outputs: []      # max 4
    priority_reason:          # <= 2 sentences
    stop_condition:
    return_to: Alfred

  constraints:
    time_container_min: 120
    sprint_template: Sprint Alex
    must_use: []
    must_avoid: []
    operator_decision_needed: true|false

  requested_outputs:
    mandatory:
      - sprint_workflow
      - acceptance_criteria
      - session_export_expectation
    optional:
      - prompt_chain
      - ai_routing_plan
      - task_sequence

  state_effect:
    opstate_delta_candidate: false
    pattern_candidate: false
    kb_candidate: false
```

---

## 10. Session Export and OpState rules

### 10.1 Session Export mutability

```yaml
session_export_mutability:
  before_submission: editable
  after_submission: immutable
  corrections: append_correction_event
```

### 10.2 Operator-required Session Export fields

The operator should not write a full report. Alfred/Night should prefill the scaffold; the operator corrects and supplies the minimum actuals.

```yaml
operator_required_session_export_fields:
  objective_met: true|false|partial
  outputs_delivered: []
  deviations: []
  blockers_found: []
  next_highest_impact_tasks: [] # max 3
  process_worked: yes|mixed|no|unknown
  chat_flow_efficiency: high|medium|low|unknown
```

### 10.3 OpState delta candidate only

Session Exports do not directly update OpState. They create delta candidates.

```yaml
opstate_delta_candidate_v1:
  delta_id:
  project_id:
  source_session_export_id:
  field_path:
  old_value:
  proposed_value:
  reason:
  evidence:
  operator_approved: false
```

### 10.4 OpState approval rule

```yaml
opstate_delta_approval_v1:
  default: operator_required
  auto_apply: false
  later_possible_auto_apply_for:
    - typo_or_link_fix
    - completed_task_marked_done
    - next_action_replacement_with_clear_evidence
```

---

## 11. Pattern learning rules

### 11.1 Candidate creation

```yaml
pattern_detection_v1:
  create_candidate_if:
    repeated_success_count: ">=2"
    repeated_failure_same_root_cause: ">=2"
    repeated_operator_correction_same_field: ">=2"
    highly_efficient_workflow_seen: ">=2"
```

### 11.2 Canonical promotion

```yaml
pattern_promotion_v1:
  normal_requirements:
    - successful_uses >= 3
    - evidence_across >= 2_sessions_or_periods
    - operator_approved: true
    - kb_ops_placed: true
  emergency_manual_promotion:
    allowed: true
    requires_label: manual_operator_override
```

### 11.3 Rejected candidate archive

```yaml
rejected_pattern_archive:
  candidate_id:
  rejected_at:
  rejection_reason:
  source_tracking_records: []
  resurface_only_if_new_evidence_count: ">=2"
```

---

## 12. Tracking Record v1

Tracking is minimal, structured, and designed for learning. Process-learning enums are required. Mood, energy, and BP/XP remain excluded in v1.

```yaml
tracking_record_v1:
  identity:
    tracking_id:
    date:
    flow_id: CF1|CF2|CF3|CF4
    lane: leela_1|leela_2|master_of_arts|wildcard
    project_id:
    source_board_id:
    session_export_id:

  planned:
    objective:
    outputs: []
    time_window:
    craft_template: Sprint Alex
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

  candidates:
    pattern_candidates: []
    chunk_candidates: []
    kb_candidates: []

  excluded_v1:
    mood: not_tracked
    energy: not_tracked
    bp_xp: not_authoritative
```

---

## 13. Rhythm, weekly planning, and monthly planning

### 13.1 Rhythm in Daily Command Board

```yaml
rhythm_profile_decision:
  include_in_v1_board: true
  structure: separate_rhythm_profile_with_by_flow_candidates
  reason: preserve_craft_flow_essence_without_bloating_execution_cards
```

### 13.2 Afterwork regeneration

```yaml
afterwork_regen:
  planned_by_Alfred: true
  replaces_work_flow: false
  tracking_required: false
  optional_note: true
```

### 13.3 Weekly planning

```yaml
weekly_rhythm_plan:
  v1: light_preview_only
  v1_1: full_weekly_rhythm_plan
  reason: collect_daily_tracking_records_before_full_weekly_automation
```

### 13.4 Monthly planning

```yaml
monthly_direction_map:
  status: later
  allowed_now:
    - major_themes
    - known_hard_deadlines
    - risk_periods
  prohibited_now:
    - daily_flow_assignment
    - detailed_task_scheduling
```

---

## 14. Operator override learning and automation boundaries

### 14.1 Operator override learning

```yaml
operator_override_learning:
  single_override: log_as_planning_correction
  repeated_same_override_count_2: create_pattern_candidate
  canonical_change: requires_operator_validation_and_kb_ops
```

### 14.2 Low-confidence MetaOps handoff

```yaml
low_confidence_handoff_rule:
  if confidence == low and fit <= 1:
    route: discovery_handoff
  elif confidence == low:
    route: execution_handoff_with_warning
  else:
    route: normal_execution_handoff
```

### 14.3 No silent automation

```yaml
silent_automation_boundaries:
  calendar_mutation: forbidden_without_permission
  opstate_mutation: forbidden_without_operator_approval_v1
  canonical_kb_promotion: forbidden_without_operator_approval_and_kb_ops
  board_mutation_after_lock: forbidden_without_revision
  p0_auto_assignment: forbidden_by_default
```

---

## 15. Decisions now resolved from previous open-question list

This file resolves the following prior open questions from `ALFRED_WORKFLOW_DECISION_LOCK.md`:

| Prior open question | Resolution |
|---|---|
| Exact fields in Daily Command Board | `daily_command_board_v1` locked in section 8 |
| Exact fields in pre-filled Session Export scaffold | operator-required fields and Session Export/OpState rules locked in section 10 |
| First heuristic ranking model before full Algorithm | Orientation Core v1 + P-Class rules locked in sections 3-5 |
| How far ahead Alfred should plan in v1 | v1 daily + light weekly preview; full weekly in v1.1; monthly later |
| Minimum acceptable tracking format | `tracking_record_v1` locked in section 12 |
| Exact MetaOps handoff schema | `metaops_craft_flow_handoff_v1` locked in section 9 |
| Daily board operator mutability | board lock/revision rule locked in section 8.1 |
| Low-friction Session Export correction | operator-required fields locked in section 10.2 |

---

## 16. Rejected alternatives

- Weighted total scoring as v1 routing mechanism.
- 0-10 or 1-10 scoring scales.
- Keeping `risk_if_deferred` separate from `urgency`.
- Keeping `effort` as a v1 score.
- Treating `policy_lane` as a score variable.
- Treating `confidence` as a score variable.
- Assigning more than four P1 craft-flow items in one day.
- Auto-assigning P0 to CF1 by default.
- Mutating the Daily Command Board after operator lock.
- Letting Session Export directly update OpState.
- Requiring the operator to author learning/pattern candidates manually.
- Promoting a pattern after one occurrence.
- Tracking mood, energy, or BP/XP in v1.
- Building full Weekly Rhythm Plan before reliable daily tracking exists.
- Detailed monthly task scheduling in v1.

---

## 17. Next implementation path

```yaml
next_implementation_path:
  1: update_parent_decision_lock_reference_to_this_file
  2: create_appendix_APEX_ORIENTATION_AND_ROUTING.md
  3: create_appendix_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
  4: create_appendix_SESSION_EXPORT_OPSTATE_AND_TRACKING.md
  5: create_appendix_PATTERN_LEARNING_AND_RHYTHM.md
  6: patch canonical Alfred KB files only after appendices stabilize
```

---

## 18. Update log

| Date | Change |
|---|---|
| 2026-05-01 | Created after operator accepted all recommendations in Apex Variables & Handoffs Q&A. |
