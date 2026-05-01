# APPENDIX_DAILY_COMMAND_BOARD_AND_HANDOFFS

## Purpose

Operational appendix for Alfred's Daily Command Board and Alfred -> MetaOps craft-flow handoffs.

This appendix defines how Alfred converts Night outputs, Session Export-derived planning packets, calendar reality, and project packets into a bounded daily board for the four-craft-flow working day.

It uses the corrected process-handover priority model:

```yaml
EVD / IMP / RSK + URG
```

No `value / urgency / leverage / fit` fields are used.

## Authority boundary

```yaml
file_status: subordinate_operational_appendix
canonical_owner: managed/agent_kb/alfred/BEST_PRACTICES.md
source_decision_lock: managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md
related_appendix: managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md
process_contract_reference: managed/processes/AGENT_HANDOFF_CONTRACTS.md
```

The Daily Command Board is a planning and recommendation surface. It does not silently mutate SSOT, OpState, calendar, or canonical KB.

## Daily Command Board v1

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
      priority_class: P0|P1|P2|P3
      EVD: 1-100
      IMP: 1-100
      RSK: 1-100
      URG: 1-100
      readiness: ready|partial|missing_input|blocked|operator_decision_needed
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

## Project Packet v1

A Project Packet is a compact planning input. It tells Alfred what work is available, why it matters, whether it can be acted on, and where it should route.

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

## Four craft-flow working day

```yaml
default_daily_craft_flow_allocation:
  CF1: leela_1
  CF2: leela_2
  CF3: master_of_arts
  CF4: wildcard_highest_current_priority
```

Rules:

- CF1 and CF2 normally protect Leela-related app/product/build/spec work.
- CF3 normally protects Master of Arts business/system work.
- CF4 remains wildcard.
- Urgent overrides are allowed only when Alfred names the tradeoff and displaced work.
- A normal day has at most four assigned P1 craft-flow items.
- P0 items are surfaced before normal allocation and are not auto-assigned by default.

## Daily priority stack

The priority stack is not a weighted score list. It is a sorted planning view based on P-class, hard flags, readiness, lane protection, and visible rationale.

Recommended ordering:

1. P0 risks/repairs requiring operator decision or schedule repair.
2. P1 craft-flow candidates eligible for today's four flows.
3. P2 valid default-lane or backlog work.
4. P3 deferred, blocked, missing-input, or clarification items.

Each item must expose why it is placed where it is.

## Rhythm profile separation

`rhythm_profile` is separate from execution cards.

Purpose:

- preserve craft-flow essence without bloating every card
- keep physical and mental chunk candidates visible
- support branch balance and afterwork regeneration
- avoid turning the board into a giant dashboard

Do not inline every physical, mental, and regeneration detail into each craft-flow card.

## Board lock rule

```yaml
board_lock_rule:
  before_operator_lock: editable
  after_operator_lock: immutable
  changes_after_lock: create_daily_board_revision
```

Operator edits before lock may update proposed placement. After lock, changes create a revision. Do not silently mutate the locked board.

## Deferred / not today handling

```yaml
deferred_or_not_today_item:
  project_packet_id:
  reason:
  revisit_rule:
  displaced_by:
  evidence_note:
```

A deferred item must say why it did not receive a craft-flow slot. Valid reasons include:

- lower P-class than selected work
- missing input
- blocked state
- insufficient readiness
- displaced by P0 repair
- displaced by higher-URG item
- no available work window

## P0 risks and repairs

P0 items are displayed in `risks_and_repairs`, not silently placed into CF1.

```yaml
p0_risk_or_repair:
  risk:
  trigger:
  repair:
  decision_needed:
  affected_flows: []
  operator_confirmation_required: true
```

Examples:

- hard deadline needs operator confirmation before displacing a protected lane
- calendar conflict requires Rhythm repair
- hygiene hold blocks safe execution
- operator decision needed blocks downstream work

## MetaOps Craft Flow Handoff v1

Local craft-flow briefs should be short enough for MetaOps to structure execution without receiving a raw project dump.

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

## Relationship to AGENT_HANDOFF_CONTRACTS

| Situation | Required shape |
|---|---|
| Local Alfred -> MetaOps craft-flow brief | use `metaops_craft_flow_handoff_v1` |
| Material first-wave handoff crossing governed process boundaries | use formal `handoff_packet` from `AGENT_HANDOFF_CONTRACTS.md` |
| High-impact or high-risk handoff | include validator path and preserve `EVD / IMP / RSK` |
| Time-sensitive handoff | include `URG` as process-handover extension |

A local craft-flow brief does not override the formal handoff contract.

## Examples

### Normal Leela flow

```yaml
flow_id: CF1
lane: leela_1
project_id: leela
objective: Prepare one implementation-ready feature delta.
priority_control:
  EVD: 75
  IMP: 85
  RSK: 35
  URG: 55
  readiness: ready
  hard_flags: []
  priority_class: P1
metaops_handoff_needed: true
```

### Urgent Master of Arts override

```yaml
risk_or_repair:
  risk: Master of Arts deadline pressure may displace protected Leela work.
  trigger: hard_deadline with URG 90
  repair: operator confirms whether CF3 and/or CF4 should absorb the work before touching CF1/CF2.
  decision_needed: true
```

### Low-evidence discovery handoff

```yaml
flow_id: CF4
lane: wildcard
priority_control:
  EVD: 30
  IMP: 70
  RSK: 60
  URG: 35
  readiness: missing_input
  hard_flags: [missing_input]
  priority_class: P3
requested_metaops_action: discovery_or_clarification_packet
```

### Overloaded day with deferred P1

```yaml
deferred_or_not_today:
  - project_packet_id: pkt_leela_secondary
    reason: fifth P1 candidate exceeds four-flow day capacity
    revisit_rule: review tomorrow morning or if operator removes another flow
    displaced_by: pkt_master_of_arts_deadline
```

## Operator edit tracking

```yaml
operator_edit_log_entry:
  edited_at:
  field_path:
  old_value:
  new_value:
  reason:
  before_or_after_lock: before_lock|after_lock
  revision_id:
```

Before lock, edits update the board draft. After lock, edits create a revision.

## Anti-patterns

- Daily Command Board as giant dashboard.
- Mixing every Rhythm detail into every craft-flow card.
- Auto-mutating board after operator lock.
- Sending raw project dumps to MetaOps.
- Assigning more than four P1 craft-flow items.
- Auto-assigning P0 without operator confirmation.
- Reintroducing `value / urgency / leverage / fit` fields.
- Hiding low evidence behind confident prose.
- Treating lane as importance score.
- Letting a craft-flow brief replace a formal first-wave handoff when the formal process applies.

## Source basis

- `managed/agent_kb/alfred/working/APEX_VARIABLES_HANDOFF_DECISION_LOCK.md`
- `managed/agent_kb/alfred/working/ALFRED_WORKFLOW_DECISION_LOCK.md`
- `managed/agent_kb/alfred/appendices/APPENDIX_PROCESS_HANDOVER_PRIORITY.md`
- `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
- `managed/rituals/NIGHT_PLANNING_PROTOCOL.md`
- `managed/rituals/SESSION_EXPORT_PROTOCOL.md`
- uploaded Daily Flows and Craft Flows materials for rhythm/craft-flow structure

## Future improvements

- Add full Weekly Rhythm Plan v1.1 after enough Daily Command Board tracking exists.
- Add Daily Command Board visualization only after the v1 schema proves stable.
- Calibrate P-class overflow handling from real operator edits.
- Define low-risk auto-suggestion classes for recurring board corrections.

## Simplification check

| Question | Verdict |
|---|---|
| What could be removed? | Detailed examples can later move to templates if the appendix grows too large. |
| What is necessary? | Board schema, Project Packet, four-flow rule, P0/P1 rules, MetaOps handoff, board lock, deferred handling. |
| What is over-engineered? | Nothing material yet; `rhythm_profile` prevents card bloat and preserves a minimal board. |
