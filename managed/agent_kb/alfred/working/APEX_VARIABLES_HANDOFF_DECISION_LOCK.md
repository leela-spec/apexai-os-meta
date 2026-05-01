# APEX_VARIABLES_HANDOFF_DECISION_LOCK

## 0. File role

```yaml
file_id: APEX_VARIABLES_HANDOFF_DECISION_LOCK
repo: leela-spec/apexai-os-meta
path: managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
status: locked_working_decision_file
canonical_status: non_canonical_until_promoted
parent_context_lock: managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
purpose: lock Alfred/Apex process-handover priority rules, Daily Command Board contracts, trace/state rules, tracking, pattern learning, and planning defaults after operator correction
owner: operator_and_alfred_workflow_design
update_rule: update only when a newer operator decision supersedes this file
promotion_rule: may be promoted into Alfred KB appendices/canonical files through normal source/audit/promotion discipline
```

This file locks the corrected accepted decisions for Alfred/Apex process handovers. It does not replace the broader Alfred workflow decision lock. It specializes and resolves the earlier open decisions about process-handover priority, Daily Command Board structure, Session Export / OpState separation, MetaOps handoff design, tracking, pattern promotion, and Rhythm planning.

---

## 0.1 Supersession rule

- **Decision:** The prior `value / urgency / leverage / fit` orientation model is superseded and must not be promoted as a parallel canonical metric system.
- **Decision:** Existing first-wave handoff control remains `EVD / IMP / RSK` on a 1-100 scale.
- **Decision:** Alfred/Apex process handovers add `URG` on the same 1-100 scale when time pressure, deadline pressure, or delay penalty materially affects priority.
- **Decision:** `value` is absorbed into `IMP`; `urgency` becomes `URG`; `leverage` is retained as rationale/unlock effect, not a score; `fit` becomes readiness, constraints, and hard flags rather than a score.
- **Decision:** This file inherits the Alfred-only naming rule from `ALFRED_WORKFLOW_DECISION_LOCK.md`.
- **Constraint:** Do not introduce a separate current-system personal assistant actor.
- **Constraint:** Do not treat the future Leela app as the current runtime.
- **Constraint:** Do not silently mutate SSOT, OpState, calendar, or canonical KB truth from these artifacts.

---

## 1. Source basis

```yaml
source_basis:
  operator_correction:
    - "The existing process uses evidence, impact, and risk, which is fine."
    - "The new variables ... are only to be used for the process handovers."
    - "Let's just stick with the evidence, impact, and risk and add a time variable like urgency for the night shift."
  prior_working_context:
    - managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md
    - managed/agent_kb/alfred/working/ALFRED_WORKFLOW_PREFILLED_QA.md
  process_contract:
    - managed/processes/AGENT_HANDOFF_CONTRACTS.md
  product_and_workflow_sources:
    - ALFRED_KB_BASE_BUILD_INDEX.md
    - Daily Flows.md
    - Craft Flows - Holistic Work Sequences.md
    - Sequencing SSOT Updatev2.md
    - Rhythm SSOT Updatev2.md
```

The corrected model preserves the existing evidence/impact/risk discipline and extends it only where Alfred's process handovers require time-aware prioritization: Night to Day, Session Export to Night, Daily Command Board generation, and craft-flow allocation.

---

## 2. Final decision summary

| # | Decision | Locked value |
|---:|---|---|
| 1 | Core handoff metrics | `EVD`, `IMP`, `RSK` |
| 2 | Process-handover time metric | add `URG` where time pressure matters |
| 3 | Score scale | 1-100 for `EVD / IMP / RSK / URG` |
| 4 | `value` | absorbed into `IMP` |
| 5 | `urgency` | renamed to `URG` and aligned to the 1-100 metric family |
| 6 | `leverage` | rationale/unlock effect, not score |
| 7 | `fit` | readiness/constraints/hard flags, not score |
| 8 | Confidence | evidence posture already represented by `EVD`; use source notes if needed |
| 9 | Policy lane | `lane`, a placement guardrail, not score |
| 10 | Hard flags | routing short-circuit / control gates |
| 11 | Priority model | P0-P3 classification, no weighted sum |
| 12 | P1 capacity | max 4 assigned craft-flow items per day |
| 13 | Universal artifact contract | Identity, Source, Intent, Metrics where needed, Routing, State Effect |
| 14 | Metrics required | process handovers and material handoffs; not Session Export trace itself |
| 15 | Project Packet | v1 schema locked below |
| 16 | Daily Command Board | v1 schema with separate `rhythm_profile` locked below |
| 17 | MetaOps handoff | local craft-flow brief may include `URG`; formal handoff keeps required `EVD / IMP / RSK` |
| 18 | Session Export | immutable trace after submission |
| 19 | OpState update | delta candidate only |
| 20 | OpState approval | operator required in v1 |
| 21 | Pattern candidate threshold | create after >=2 evidence signals |
| 22 | Pattern promotion | 3 successful uses + operator approval + KB Ops placement |
| 23 | Tracking | minimal structured; process enums required |
| 24 | Mood/energy/BP-XP | excluded from Alfred tracking v1 |
| 25 | P0 handling | surface before normal allocation; no auto-assign by default |
| 26 | Board mutation | no mutation after operator lock; revision only |
| 27 | Weekly planning | v1 light preview; v1.1 full Weekly Rhythm Plan |
| 28 | Monthly planning | later; directional only when used |

---

## 3. Metric boundary model

### 3.1 Agent handoff metrics

First-wave agent handoffs continue to use `EVD / IMP / RSK` exactly as governed by `managed/processes/AGENT_HANDOFF_CONTRACTS.md`.

```yaml
agent_handoff_metrics_v1:
  EVD: 1-100  # evidence strength and traceability
  IMP: 1-100  # downstream impact if accepted or implemented
  RSK: 1-100  # drift, authority, safety, reversibility, or structural risk
```

### 3.2 Process-handover priority metrics

Alfred/Apex process handovers use the same metric family and add `URG` only when time pressure affects priority.

```yaml
process_handover_priority_v1:
  metrics:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
    URG: 1-100

  controls:
    readiness: ready|partial|missing_input|blocked|operator_decision_needed
    lane: leela|master_of_arts|wildcard|none
    hard_flags: []
    priority_class: P0|P1|P2|P3

  rationale:
    impact_reason:
    urgency_reason:
    unlocks: []
    risk_note:
    next_action:
```

### 3.3 When each model applies

| Situation | Required model |
|---|---|
| Alfred to MetaOps formal first-wave handoff | `EVD / IMP / RSK`; add `URG` only if time pressure is material |
| Night output to Alfred morning planning | `EVD / IMP / RSK / URG` |
| Session Export to Night synthesis | trace fields first; Night may derive `EVD / IMP / RSK / URG` for next planning packets |
| Daily Command Board priority stack | `EVD / IMP / RSK / URG` plus readiness/lane/hard flags |
| Craft-flow allocation CF1-CF4 | P-class derived from process-handover metrics and readiness |
| Session Export trace | no priority metrics required inside raw trace |
| OpState delta candidate | evidence and approval fields; no P-class unless routed for planning |
| Pattern candidate | evidence count and source refs; no P-class unless routed for planning |

---

## 4. Metric definitions

| Metric | Definition | Practical question | Notes |
|---|---|---|---|
| `EVD` | Strength and traceability of evidence. | How well do we know this is true enough to use? | Existing process metric. Weak evidence must be visible. |
| `IMP` | Importance/downstream impact if accepted, done, or ignored. | How much does this matter? | Absorbs the prior `value` idea. |
| `RSK` | Risk of proceeding, delaying, mishandling, or mutating truth incorrectly. | What can go wrong? | Includes drift, authority, safety, reversibility, and structural risk. |
| `URG` | Time pressure, delay penalty, deadline pressure, or blocked-window pressure. | Why now? | New process-handover extension. Use only when time changes priority. |

### 4.1 Scale definitions

Use the same band logic as first-wave handoff contracts.

| Score range | Meaning |
|---:|---|
| 1-20 | low |
| 21-40 | limited |
| 41-60 | material |
| 61-80 | strong/high |
| 81-100 | decisive/highest |

### 4.2 Urgency calibration

```yaml
URG:
  1_20: no meaningful penalty if deferred
  21_40: useful soon, safe to defer
  41_60: should happen in the current planning window
  61_80: delay creates material loss or blocks downstream work
  81_100: deadline, expiring window, hard external constraint, or severe delay penalty
```

---

## 5. Replaced variable mapping

```yaml
superseded_vulf_mapping:
  value:
    replacement: IMP
    status: absorbed
  urgency:
    replacement: URG
    status: retained_as_time_metric_with_1_100_scale
  leverage:
    replacement: rationale.unlocks
    status: not_score
  fit:
    replacement:
      - controls.readiness
      - controls.hard_flags
      - constraints
    status: not_score
  confidence:
    replacement:
      - EVD
      - source_status
    status: not_priority_score
  policy_lane:
    replacement: controls.lane
    status: guardrail_not_score
```

Rejected: a second 0-3 `value / urgency / leverage / fit` metric system.

---

## 6. Controls and hard flags

### 6.1 Readiness

```yaml
readiness:
  ready: enough context and input exists to act in the proposed container
  partial: workable but caveated; handoff must expose missing assumptions
  missing_input: input request or discovery required before execution
  blocked: cannot proceed until blocker is removed
  operator_decision_needed: operator choice required before safe continuation
```

### 6.2 Lane

```yaml
lane:
  status: placement_guardrail
  not: priority_score
  values:
    leela: normally eligible for CF1 or CF2
    master_of_arts: normally eligible for CF3
    wildcard: normally eligible for CF4
    none: no standing lane protection
```

### 6.3 Hard flag routing

Hard flags are evaluated before normal P-class assignment.

```yaml
hard_flags:
  - hard_deadline
  - blocked
  - missing_input
  - operator_decision_needed
  - hygiene_hold
  - calendar_conflict
  - no_actionable_next_step
```

```yaml
hard_flag_routing_v1:
  hard_deadline: evaluate_as_P0_candidate_if_URG_high
  blocked: route_to_unblock_or_defer
  missing_input: route_to_input_request_or_discovery
  operator_decision_needed: route_to_operator_decision
  hygiene_hold: route_to_hygiene_resolution
  calendar_conflict: route_to_rhythm_repair
  no_actionable_next_step: route_to_MetaOps_or_Night_for_clarification
```

---

## 7. Priority Class rules v1

P-classes are classification results, not weighted score totals.

```yaml
priority_class_rules_v1:
  P0:
    meaning: must_handle_or_repair_before_normal_allocation
    rule_any:
      - hard_deadline and URG >= 81
      - hygiene_hold blocks safe work
      - operator_decision_needed blocks downstream work
      - calendar_conflict blocks the day plan
    handling:
      - surface_before_normal_allocation
      - no_auto_assign_to_flow
      - operator_confirmation_or_repair_required

  P1:
    meaning: should_receive_craft_flow_today
    rule_all:
      - IMP >= 61
      - readiness in [ready, partial]
      - no_blocking_hard_flag
    rule_any:
      - URG >= 41
      - rationale.unlocks is not empty
      - lane is protected and weekly/default commitment applies
    cap: max_4_per_day

  P2:
    meaning: valid_default_lane_or_backlog_work
    rule_all:
      - IMP >= 41
      - readiness in [ready, partial]
      - no_blocking_hard_flag

  P3:
    meaning: defer_backlog_clarify_or_unblock
    rule_any:
      - readiness in [missing_input, blocked]
      - no_actionable_next_step
      - EVD <= 40 and IMP >= 41
      - stale_without_delta
```

### 7.1 P1 capacity rule

```yaml
p1_capacity_rule:
  max_assigned_per_day: 4
  overflow_destination: deferred_or_not_today
  overflow_requires:
    - reason
    - recommended_revisit
    - displaced_by
```

### 7.2 P0 handling

```yaml
p0_handling_v1:
  auto_assign_to_flow: false
  display_surface: risks_and_repairs
  requires_operator_confirmation: true
```

---

## 8. Universal artifact contract

### 8.1 Minimum metadata for all artifacts

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

### 8.2 Full contract for process handover / planning artifacts

```yaml
apex_process_handover_contract_v1:
  identity:
    artifact_id:
    artifact_type:
    project_id:
    created_by:
    created_at:
    target_consumer:
  source_basis:
    source_artifacts: []
    source_status: fully_read|partially_read|not_accessible|provisional|mixed|unknown
  intent:
    objective:
    expected_outputs: []
    decision_needed: true|false
  priority_control:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
    URG: 1-100
    readiness: ready|partial|missing_input|blocked|operator_decision_needed
    lane: leela|master_of_arts|wildcard|none
    hard_flags: []
    priority_class: P0|P1|P2|P3
    visible_reason:
  rationale:
    impact_reason:
    urgency_reason:
    unlocks: []
    risk_note:
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

### 8.3 Priority-control applicability

```yaml
priority_control_required_for:
  - project_packet
  - daily_priority_stack_item
  - craft_flow_handoff_when_priority_or_time_pressure_matters
  - night_to_day_handover_item

priority_control_optional_for:
  - night_plan_item
  - risk_or_repair_item

priority_control_not_required_for:
  - raw_session_export_trace
  - opstate_delta_candidate
  - pattern_candidate
  - tracking_record
```

---

## 9. Project Packet v1

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

  priority_control:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
    URG: 1-100
    readiness: ready|partial|missing_input|blocked|operator_decision_needed
    lane: leela|master_of_arts|wildcard|none
    hard_flags: []
    priority_class: P0|P1|P2|P3
    visible_reason:

  rationale:
    impact_reason:
    urgency_reason:
    unlocks: []
    risk_note:

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

## 10. Daily Command Board v1

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
      EVD:
      IMP:
      RSK:
      URG:
      readiness:
      hard_flags: []
      visible_reason:

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

### 10.1 Board lock rule

```yaml
board_lock_rule:
  before_operator_lock: editable
  after_operator_lock: immutable
  changes_after_lock: create_daily_board_revision
```

---

## 11. MetaOps Craft Flow Handoff v1

Alfred does not over-prescribe MetaOps internals. Handoff includes mandatory outputs for interoperability and optional outputs for richer workflows.

If this remains a local Alfred-to-MetaOps craft-flow brief, it may use the compact schema below. If it becomes a material first-wave handoff under `AGENT_HANDOFF_CONTRACTS.md`, the formal handoff packet requirements and `EVD / IMP / RSK` fields remain mandatory.

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

  priority_control:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
    URG: 1-100
    readiness: ready|partial|missing_input|blocked|operator_decision_needed
    hard_flags: []
    priority_class: P0|P1|P2|P3

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

## 12. Session Export and OpState rules

### 12.1 Session Export mutability

```yaml
session_export_mutability:
  before_submission: editable
  after_submission: immutable
  corrections: append_correction_event
```

### 12.2 Operator-required Session Export fields

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

### 12.3 OpState delta candidate only

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

### 12.4 OpState approval rule

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

## 13. Pattern learning rules

### 13.1 Candidate creation

```yaml
pattern_detection_v1:
  create_candidate_if:
    repeated_success_count: ">=2"
    repeated_failure_same_root_cause: ">=2"
    repeated_operator_correction_same_field: ">=2"
    highly_efficient_workflow_seen: ">=2"
```

### 13.2 Canonical promotion

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

### 13.3 Rejected candidate archive

```yaml
rejected_pattern_archive:
  candidate_id:
  rejected_at:
  rejection_reason:
  source_tracking_records: []
  resurface_only_if_new_evidence_count: ">=2"
```

---

## 14. Tracking Record v1

Tracking is minimal, structured, and designed for learning. Process-learning enums are required. Mood, energy, and BP/XP remain excluded from Alfred tracking v1.

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

## 15. Rhythm, weekly planning, and monthly planning

### 15.1 Rhythm in Daily Command Board

```yaml
rhythm_profile_decision:
  include_in_v1_board: true
  structure: separate_rhythm_profile_with_by_flow_candidates
  reason: preserve_craft_flow_essence_without_bloating_execution_cards
```

### 15.2 Afterwork regeneration

```yaml
afterwork_regen:
  planned_by_Alfred: true
  replaces_work_flow: false
  tracking_required: false
  optional_note: true
```

### 15.3 Weekly planning

```yaml
weekly_rhythm_plan:
  v1: light_preview_only
  v1_1: full_weekly_rhythm_plan
  reason: collect_daily_tracking_records_before_full_weekly_automation
```

### 15.4 Monthly planning

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

## 16. Operator override learning and automation boundaries

### 16.1 Operator override learning

```yaml
operator_override_learning:
  single_override: log_as_planning_correction
  repeated_same_override_count_2: create_pattern_candidate
  canonical_change: requires_operator_validation_and_kb_ops
```

### 16.2 Low-evidence or low-readiness MetaOps handoff

```yaml
low_evidence_or_low_readiness_handoff_rule:
  if EVD <= 40 and readiness in [missing_input, blocked]:
    route: discovery_or_clarification_handoff
  elif EVD <= 40:
    route: execution_handoff_with_evidence_warning
  elif readiness == partial:
    route: execution_handoff_with_assumption_warning
  else:
    route: normal_execution_handoff
```

### 16.3 No silent automation

```yaml
silent_automation_boundaries:
  calendar_mutation: forbidden_without_permission
  opstate_mutation: forbidden_without_operator_approval_v1
  canonical_kb_promotion: forbidden_without_operator_approval_and_kb_ops
  board_mutation_after_lock: forbidden_without_revision
  p0_auto_assignment: forbidden_by_default
```

---

## 17. Decisions now resolved from previous open-question list

This file resolves the following prior open questions from `ALFRED_WORKFLOW_DECISION_LOCK.md`:

| Prior open question | Resolution |
|---|---|
| Exact fields in Daily Command Board | `daily_command_board_v1` locked in section 10 |
| Exact fields in pre-filled Session Export scaffold | operator-required fields and Session Export/OpState rules locked in section 12 |
| First heuristic ranking model before full Algorithm | `EVD / IMP / RSK + URG` process-handover priority model + P-Class rules locked in sections 3-7 |
| How far ahead Alfred should plan in v1 | v1 daily + light weekly preview; full weekly in v1.1; monthly later |
| Minimum acceptable tracking format | `tracking_record_v1` locked in section 14 |
| Exact MetaOps handoff schema | `metaops_craft_flow_handoff_v1` locked in section 11 |
| Daily board operator mutability | board lock/revision rule locked in section 10.1 |
| Low-friction Session Export correction | operator-required fields locked in section 12.2 |

---

## 18. Rejected alternatives

- Parallel `value / urgency / leverage / fit` metric system.
- 0-3 orientation scoring as a canonical process-handover model.
- Weighted total scoring as v1 routing mechanism.
- 0-10 or 1-10 scoring scales.
- Keeping `value` separate from `IMP`.
- Keeping `leverage` as a score.
- Keeping `fit` as a score.
- Treating `lane` as a score variable.
- Treating confidence as priority instead of evidence posture.
- Assigning more than four P1 craft-flow items in one day.
- Auto-assigning P0 to CF1 by default.
- Mutating the Daily Command Board after operator lock.
- Letting Session Export directly update OpState.
- Requiring the operator to author learning/pattern candidates manually.
- Promoting a pattern after one occurrence.
- Tracking mood, energy, or BP/XP in Alfred tracking v1.
- Building full Weekly Rhythm Plan before reliable daily tracking exists.
- Detailed monthly task scheduling in v1.

---

## 19. Next implementation path

```yaml
next_implementation_path:
  1: update_parent_decision_lock_reference_to_this_file
  2: replace_handover_prompt_flow_VULF_references_with_EVD_IMP_RSK_URG
  3: create_appendix_PROCESS_HANDOVER_PRIORITY.md
  4: create_appendix_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
  5: create_appendix_SESSION_EXPORT_OPSTATE_AND_TRACKING.md
  6: create_appendix_PATTERN_LEARNING_AND_RHYTHM.md
  7: patch canonical Alfred KB files only after appendices stabilize
```

---

## 20. Update log

| Date | Change |
|---|---|
| 2026-05-01 | Created after operator accepted all recommendations in Apex Variables & Handoffs Q&A. |
| 2026-05-01 | Corrected after operator rejected the parallel V/U/L/F model; locked `EVD / IMP / RSK + URG` for Alfred/Apex process handovers. |
