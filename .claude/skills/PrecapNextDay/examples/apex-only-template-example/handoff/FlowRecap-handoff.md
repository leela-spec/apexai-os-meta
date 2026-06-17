# FILE: .claude/skills/PrecapNextDay/examples/apex-only-template-example/handoff/FlowRecap-handoff.md

# FlowRecap Handoff — APEX example

Prepared by PreCap Next Day. FlowRecap was not run and no FlowRecap output was created.

```yaml
FlowRecap_handoff_status:
  handoff_id: FlowRecap_handoff_2026_06_18_apex_template_layer
  source_next_day_plan_ref: ../next-day-plan.md
  handoff_status: prepared_not_run
  FlowRecap_output_created: false
  project_execution_status: not_executed
  validation_status: operator_review_recommended
```

## F1

```yaml
handoff_block:
  flow_id: F1
  APEX_operator_label: APEX_repo_foundation
  flow_packet_ref: ../flows/F1-flow-packet.md
  prompt_pack_ref: ../prompts/F1-flow-prompt-pack.md
  planned_goal: Resolve repo package path and target file placement.
  capture_ref: ../capture/raw-flow-dump-template.md#F1
  review_flags:
    - Path strategy unresolved.
```

## F2

```yaml
handoff_block:
  flow_id: F2
  APEX_operator_label: APEX_skill_database_contracts
  flow_packet_ref: ../flows/F2-flow-packet.md
  prompt_pack_ref: ../prompts/F2-flow-prompt-pack.md
  planned_goal: Map contract authority versus template authority.
  capture_ref: ../capture/raw-flow-dump-template.md#F2
  review_flags:
    - Watch for schema drift.
```

## F3

```yaml
handoff_block:
  flow_id: F3
  APEX_operator_label: APEX_output_templates_examples
  flow_packet_ref: ../flows/F3-flow-packet.md
  prompt_pack_ref: ../prompts/F3-flow-prompt-pack.md
  planned_goal: Create templates and example artifacts.
  capture_ref: ../capture/raw-flow-dump-template.md#F3
  review_flags:
    - Example package needs operator critique.
```

## F4

```yaml
handoff_block:
  flow_id: F4
  APEX_operator_label: APEX_validation_handover
  flow_packet_ref: ../flows/F4-flow-packet.md
  prompt_pack_ref: ../prompts/F4-flow-prompt-pack.md
  planned_goal: Check outputs and prepare handoff.
  capture_ref: ../capture/raw-flow-dump-template.md#F4
  review_flags:
    - Validation is draft until critique.
```

## Next Use

Use this handoff only after actual operator execution has produced filled capture notes. Until then, this remains a preparation artifact.
