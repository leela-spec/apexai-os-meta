# Project Packet Templates

## Purpose

Reusable Alfred project packet and MetaOps craft-flow handoff forms.

These templates support process handover priority, project packet framing, and bounded MetaOps execution handoffs.

## Boundary

Project packets and craft-flow handoffs are planning and handoff forms. They do not execute downstream work, mutate canonical files, or override MetaOps process authority.

## ALFRED-TPL-011 — Project Packet v1

Use when a work item needs compact project-facing context before MetaOps, Strategy, Detective, or KB routing.

```yaml
project_packet_v1:
  packet_id: PP-YYYYMMDD-001
  title: <short title>
  lane: leela | master_of_arts | wildcard | none
  current_state: draft | candidate | needs_validation | blocked | operator_review_required | accepted
  objective: <bounded objective>
  desired_output: <artifact or decision needed>
  context_summary: <compact context>
  metrics:
    EVD: <1-100>
    IMP: <1-100>
    RSK: <1-100>
    URG: <1-100 or null if not a process handover>
  controls:
    readiness: ready | partial | missing_input | blocked | operator_decision_needed
    hard_flags: []
    priority_class: P0 | P1 | P2 | P3
  rationale:
    impact_reason: <why it matters>
    urgency_reason: <why timing matters or none>
    unlocks: []
    risk_note: <risk>
    next_action: <smallest next action>
  stop_condition: <pause/escalation trigger>
```

## Process handover priority card

Use when only the process-priority subset is needed.

```yaml
process_handover_priority_card_v1:
  item_id:
  item:
  source_artifacts: []
  metrics:
    EVD:
    IMP:
    RSK:
    URG:
  controls:
    readiness: ready | partial | missing_input | blocked | operator_decision_needed
    lane: leela | master_of_arts | wildcard | none
    hard_flags: []
    priority_class: P0 | P1 | P2 | P3
  rationale:
    impact_reason:
    urgency_reason:
    unlocks: []
    risk_note:
    next_action:
  route:
  stop_condition:
```

## ALFRED-TPL-013 — MetaOps Craft Flow Handoff v1

Use when a Daily Command Board item becomes bounded MetaOps execution coordination.

```yaml
metaops_craft_flow_handoff_v1:
  handoff_id: HND-alfred-metaops-YYYYMMDD-001
  from_agent: alfred
  to_agent: meta_ops
  handoff_type: execution_orchestration
  board_item_ref: <Daily Command Board item id>
  lane: leela | master_of_arts | wildcard | none
  priority_class: P1 | P2 | P3
  objective: <bounded execution objective>
  expected_output: <return artifact>
  constraints:
    must_do: []
    must_not_do:
      - Do not exceed the bounded objective.
      - Do not mutate canonical files without a patch plan and approval path.
  metrics:
    EVD: <1-100>
    IMP: <1-100>
    RSK: <1-100>
    URG: <1-100>
  readiness: ready | partial | missing_input | blocked | operator_decision_needed
  hard_flags: []
  next_action: <immediate next step>
  stop_condition: <pause/escalation trigger>
  return_expected: <what MetaOps should return>
```

## MetaOps craft-flow extended fields

Use only when CF1-CF4 and sprint container fields are needed.

```yaml
metaops_craft_flow_container_v1:
  handoff_id:
  flow_id: CF1 | CF2 | CF3 | CF4
  project_id:
  created_by: Alfred
  source_artifacts: []
  intent:
    target_output:
    expected_outputs: []
    priority_reason:
    stop_condition:
    return_to: Alfred
  priority_control:
    EVD:
    IMP:
    RSK:
    URG:
    readiness:
    hard_flags: []
    priority_class:
  constraints:
    time_container_min: 120
    sprint_template: Sprint Alex
    must_use: []
    must_avoid: []
    operator_decision_needed: true | false
  requested_outputs:
    mandatory:
      - sprint_workflow
      - acceptance_criteria
      - session_export_expectation
    optional:
      - prompt_chain
      - ai_routing_plan
      - task_sequence
```

## Invalid use

- Do not use a Project Packet as accepted OpState.
- Do not hand raw source dumps to MetaOps without objective, expected output, constraints, and stop condition.
- Do not use P0 without operator confirmation or true stop-the-line condition.
- Do not use `URG` outside process-handover/time-sensitive priority scope.
