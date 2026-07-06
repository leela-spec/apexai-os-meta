---
name: raw-flow-dump-normalize
description: Use this skill when messy operator execution notes, chat fragments, artifact references, or skipped-flow signals need to be normalized into a minimal raw execution handoff for APEX FlowRecap without running FlowRecap or mutating project state.
---

# raw-flow-dump-normalize

## Skill Contract

Use this skill to convert one planned APEX flow's messy post-execution evidence into either:

- `normalized_raw_flow_dump` when enough execution evidence exists
- `skipped_flow_marker` when the flow was skipped or evidence is too thin

This skill is an interface package only. It prepares clear downstream input for FlowRecap, but it does not execute FlowRecap, create status deltas, create model usage deltas, merge project status, write calendar events, run agents, schedule work, or overwrite project state.

```yaml
skill_contract:
  package_name: raw-flow-dump-normalize
  package_path: ".claude/skills/raw-flow-dump-normalize/"
  primary_outputs:
    - normalized_raw_flow_dump
    - skipped_flow_marker
  downstream_consumer:
    - FlowRecap
  owns:
    - normalized_raw_flow_dump
    - skipped_flow_marker
    - raw_operator_input_intake_rules
    - messy_evidence_normalization_rules
    - source_reference_capture_rules
    - completion_state_normalization
    - confidence_and_gap_flags
  must_not_own:
    - next_day_plan_schema
    - flow_packet_schema
    - flow_prompt_pack_schema
    - prompt_packet_schema
    - FlowRecap_output_schema
    - flow_recap_packet_schema
    - project_status_delta_schema
    - model_usage_delta_schema
    - status_merge_schema
    - project_kb_schema
    - calendar_write_schema
    - runtime_execution
```

## Supporting Files

```yaml
supporting_files:
  - path: ".claude/skills/raw-flow-dump-normalize/references/raw-flow-dump-contract.md"
    read_when: "Normalizing messy execution evidence into normalized_raw_flow_dump."
  - path: ".claude/skills/raw-flow-dump-normalize/references/skipped-flow-marker-contract.md"
    read_when: "A planned flow was skipped, blocked, replaced, or lacks enough execution evidence."
  - path: ".claude/skills/raw-flow-dump-normalize/templates/raw-flow-dump-template.md"
    read_when: "The operator needs a copy-paste raw dump template."
  - path: ".claude/skills/raw-flow-dump-normalize/examples/apex-minimal-raw-flow-dump-example.md"
    read_when: "A minimal APEX-only example is needed."
  - path: ".claude/skills/raw-flow-dump-normalize/package-manifest.md"
    read_when: "Inspecting package structure, source gaps, file roles, or package boundaries."
```

## Procedure

1. Identify the single planned flow being normalized and capture `execution_day`, `flow_id`, `source_flow_packet_ref`, and `flow_prompt_pack_ref` when available.
2. Inspect the available raw evidence: operator notes, chat excerpts, produced artifacts, missing artifacts, blocker notes, and model usage notes.
3. Decide whether evidence supports `normalized_raw_flow_dump` or whether the flow should instead become `skipped_flow_marker`.
4. Separate raw evidence from normalized interpretation; do not rewrite uncertainty into certainty.
5. Normalize completion state, produced outputs, decisions, blockers or failures, open questions, source gaps, model usage notes, confidence, and validation status.
6. Check ownership boundaries before output: no FlowRecap packet, no project status delta, no model usage delta, no status merge, no project execution, and no calendar write.
7. Return the normalized artifact or marker plus any operator review flags needed before downstream FlowRecap.

## Failure Modes

- Missing `flow_id` or `execution_day` blocks reliable normalization.
- Missing `source_flow_packet_ref` requires an explicit source gap and may require operator review.
- No real execution evidence should produce a `skipped_flow_marker`, not invented outputs.
- Ambiguous produced outputs must be marked low confidence or operator review recommended.
- Model usage notes must not be converted into a model usage delta.
- FlowRecap readiness must not be mistaken for running FlowRecap.
- Status-impact observations must not become project status deltas in this skill.
- Calendar-related notes must not become calendar write requests or calendar events.

## Output Requirements

For `normalized_raw_flow_dump`, include:

- `dump_id`
- `artifact_name: normalized_raw_flow_dump`
- `execution_day`
- `flow_id`
- `source_flow_packet_ref`
- `completion_state`
- `evidence_sources`
- `operator_summary`
- `produced_outputs`
- `decisions_made`
- `blockers_or_failures`
- `open_questions`
- `model_usage_notes`
- `normalization_confidence`
- `validation_status`

For `skipped_flow_marker`, include:

- `marker_id`
- `artifact_name: skipped_flow_marker`
- `execution_day`
- `flow_id`
- `source_flow_packet_ref`
- `skip_reason`
- `skip_type`
- `impact_on_plan`
- `recommended_next_handling`
- `validation_status`

## Completion Gate

```yaml
completion_gate:
  source_files_inspected_or_gaps_recorded: true
  package_path_created: true
  raw_flow_dump_contract_created: true
  skipped_flow_marker_contract_created: true
  template_created: true
  apex_minimal_example_created: true
  manifest_created: true
  SKILL_md_created_with_valid_frontmatter: true
  no_runtime_or_automation_created: true
  no_FlowRecap_or_status_merge_output_created: true
  downstream_flow_recap_input_is_clear: true
```
