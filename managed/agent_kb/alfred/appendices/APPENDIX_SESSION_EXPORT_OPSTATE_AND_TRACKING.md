# APPENDIX_SESSION_EXPORT_OPSTATE_AND_TRACKING

## Purpose

Operational appendix for Alfred's Session Export, OpState delta, and tracking loop.

This appendix defines how craft-flow sessions produce immutable trace, how Night derives next planning inputs, and how OpState remains protected from direct trace pollution.

Core rule:

```text
Session Export = trace.
OpState = state delta candidate.
Tracking Record = learning/rollup input.
```

Raw Session Export does not need priority metrics. Night may derive process-handover priority packets from Session Exports using `EVD / IMP / RSK + URG` when preparing Daily Command Board inputs.

## Authority boundary

```yaml
file_status: subordinate_operational_appendix
canonical_owner: managed/agent_kb/alfred/BEST_PRACTICES.md
source_decision_lock: managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
related_appendices:
  - managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md
  - managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md
ritual_references:
  - managed/rituals/SESSION_EXPORT_PROTOCOL.md
  - managed/rituals/NIGHT_PLANNING_PROTOCOL.md
```

This appendix does not authorize silent OpState mutation, SSOT mutation, calendar mutation, or canonical KB promotion.

## Trace vs state distinction

| Artifact | Role | Mutability | Authority |
|---|---|---|---|
| Session Export | durable record of what happened | immutable after submission; correction event only | trace authority, not accepted truth |
| OpState Delta Candidate | proposed state update from trace/evidence | reviewable candidate | not applied until operator-approved in v1 |
| Tracking Record | structured learning and rollup input | append-only or revisioned | process-learning evidence, not doctrine |
| Daily Command Board | plan/recommendation for a day | editable before lock; revision after lock | planning surface, not direct state mutation |

## Session Export mutability

```yaml
session_export_mutability:
  before_submission: editable
  after_submission: immutable
  corrections: append_correction_event
```

Do not silently overwrite a submitted Session Export. If the operator corrects something after submission, append a correction event.

## Operator-required Session Export fields

The operator should not write a long report. Alfred/Night pre-fills the scaffold; the operator corrects and supplies actuals.

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

## What Alfred/Night pre-fills

```yaml
prefill_by_Alfred_or_Night:
  planned_objective:
  expected_outputs: []
  source_board_id:
  project_id:
  flow_id:
  planned_time_window:
  planned_craft_template:
  expected_session_export_focus:
  predicted_next_tasks: []
  known_constraints: []
  known_risks: []
```

## What the operator corrects

```yaml
operator_correction_scope:
  objective_met:
  outputs_delivered:
  deviations:
  blockers_found:
  next_highest_impact_tasks:
  process_worked:
  chat_flow_efficiency:
  wrong_prefill_fields: []
```

The operator may correct the prefill rather than author the trace from scratch.

## Correction event

```yaml
session_export_correction_event_v1:
  correction_id:
  source_session_export_id:
  corrected_at:
  corrected_by: operator|Alfred|Night|MetaOps
  field_path:
  old_value:
  corrected_value:
  reason:
  affects_opstate_delta_candidate: true|false
```

## OpState delta candidate v1

Session Exports do not update OpState directly. They may create delta candidates.

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

## OpState approval v1

```yaml
opstate_delta_approval_v1:
  default: operator_required
  auto_apply: false
  later_possible_auto_apply_for:
    - typo_or_link_fix
    - completed_task_marked_done
    - next_action_replacement_with_clear_evidence
```

No auto-apply classes are active in v1.

## Tracking Record v1

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

## Mood / energy / BP-XP exclusion

Alfred tracking v1 excludes:

- mood
- energy
- complex emotional state
- authoritative BP/XP
- biometric/body signals

Reason: keep v1 low-friction and avoid overloading the operator before basic daily tracking proves useful.

## Tracking rollups

```yaml
tracking_rollups_v1:
  daily:
    - completed_flows
    - missed_or_aborted_flows
    - blockers
    - next_highest_impact_tasks
    - process_worked_distribution
    - chat_flow_efficiency_distribution
  weekly_preview:
    - planned_vs_actual_flow_count
    - recurring_blockers
    - repeated_operator_corrections
    - pattern_candidate_signals
  future_algorithm_evidence:
    - repeated_successful_flow_types
    - repeated_failed_flow_types
    - useful_metaops_handoff_patterns
    - recurring_defer_reasons
```

## How Night derives next planning inputs

Night may use Session Exports and Tracking Records to create Project Packets or Daily Command Board candidates.

```yaml
night_derivation_rule:
  raw_session_export: trace_only
  night_synthesis: may_create_project_packet
  project_packet: may_include_EVD_IMP_RSK_URG
  daily_command_board: may_classify_P0_P1_P2_P3
```

Do not write `EVD / IMP / RSK + URG` into every raw Session Export unless it is itself a planning artifact. The clean path is trace first, derived planning packet second.

## Relationship to SESSION_EXPORT_PROTOCOL.md

This appendix specializes the existing Session Export protocol for Alfred's craft-flow loop.

Preserved rules:

- Session Export is trace authority, not accepted truth.
- Session Export may inform OpState but does not replace OpState.
- Session Export must record objective, work performed, operative delta, findings, blockers, and next actions.
- Missing material Session Export is a downstream control problem.

## Relationship to NIGHT_PLANNING_PROTOCOL.md

This appendix specializes Night planning for Alfred's daily loop.

Preserved rules:

- Night consumes bounded Session Exports.
- Night may recommend OpState changes but does not directly mutate accepted truth.
- Night must preserve progress/hygiene separation.
- Night must expose missing trace, blockers, and holds.
- Night can produce next-cycle plans and project packets for Alfred's morning board.

## Examples

### Complete session

```yaml
session_export_actuals:
  objective_met: true
  outputs_delivered:
    - feature_delta_prompt_v1
  deviations: []
  blockers_found: []
  next_highest_impact_tasks:
    - validate feature_delta_prompt_v1
    - prepare Nova slice
  process_worked: yes
  chat_flow_efficiency: high
```

### Partial session

```yaml
session_export_actuals:
  objective_met: partial
  outputs_delivered:
    - rough_outline
  deviations:
    - scope_was_larger_than_expected
  blockers_found:
    - missing_current_file_map
  next_highest_impact_tasks:
    - retrieve file map
    - shrink next slice
  process_worked: mixed
  chat_flow_efficiency: medium
```

### Blocked session

```yaml
session_export_actuals:
  objective_met: false
  outputs_delivered: []
  deviations:
    - blocked_before_execution
  blockers_found:
    - operator_decision_needed
  next_highest_impact_tasks:
    - ask operator for decision
  process_worked: no
  chat_flow_efficiency: low
```

Night may convert this into a P0 or P3 Daily Command Board item depending on urgency, impact, risk, and readiness.

### Correction after submission

```yaml
session_export_correction_event_v1:
  correction_id: corr_001
  source_session_export_id: sx_2026_05_01_CF2
  corrected_at: 2026-05-01T18:30:00Z
  corrected_by: operator
  field_path: actual.objective_met
  old_value: true
  corrected_value: partial
  reason: output was drafted but not verified
  affects_opstate_delta_candidate: true
```

## Anti-patterns

- Putting full Session Export trace into OpState.
- Letting Session Export directly update OpState.
- Editing submitted trace without a correction event.
- Making the operator write essays.
- Tracking mood/energy/BP-XP in Alfred v1 despite exclusion.
- Treating tracking records as canonical doctrine.
- Using Daily Command Board metrics to silently mutate project state.
- Losing the distinction between planned, actual, derived, and approved.

## Source basis

- `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`
- `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md`
- `managed/rituals/SESSION_EXPORT_PROTOCOL.md`
- `managed/rituals/NIGHT_PLANNING_PROTOCOL.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS.md`

## Future improvements

- Define low-risk OpState auto-apply classes after operator trust and trace quality are proven.
- Add full Weekly Rhythm Plan v1.1 after sufficient daily tracking evidence.
- Add pattern-candidate automation only after repeated signals are stable.
- Reconsider mood/energy/BP-XP only after v1 tracking is low-friction and useful.

## Simplification check

| Question | Verdict |
|---|---|
| What could be removed? | Long examples can later move to templates if this appendix becomes too large. |
| What is necessary? | Trace/state distinction, correction rule, operator-required fields, OpState delta candidate, tracking schema, Night derivation rule. |
| What is over-engineered? | Nothing material yet; the design keeps raw trace clean and derives priority only where planning needs it. |
