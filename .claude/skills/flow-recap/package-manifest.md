# Flow Recap Package Manifest

```yaml
package_manifest:
  package_name: flow-recap
  package_path: .claude/skills/flow-recap/
  package_role: minimal_interface_for_post_flow_recap
  primary_artifact: flow_recap_packet
  status: interface_package_present
  read_when:
    - operator_inspects_package_structure
    - validating_flow_recap_package_files
    - preparing_or_auditing_flow_recap_output

  source_authority_summary:
    inspected_or_gap_recorded: true
    resolved_sources:
      - path: .claude/skills/raw-flow-dump-normalize/references/skipped-flow-marker-contract.md
        status: inspected
        handling: skipped_flow_marker_ref remains optional input

  package_boundaries:
    owns:
      - flow_recap_packet
      - recap_summary
      - evidence_ref_summary
      - candidate_project_status_delta
      - model_usage_delta_candidate
      - next_step_proposal
      - unresolved_questions
      - operator_validation_gate_for_recap
    must_not_own:
      - normalized_raw_flow_dump_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - prompt_packet_schema
      - accepted_project_status_update
      - project_kb_durable_schema
      - model_usage_delta_final_schema
      - usage_summary_schema
      - status_merge_packet_schema
      - updated_all_project_status_packet
      - next_PreCapNextDay_input_context
      - runtime_execution

  global_rules:
    interface_only: true
    no_runtime_or_scheduler: true
    no_agent: true
    no_automatic_state_overwrite: true
    no_project_work_execution: true
    no_status_merge_execution: true
    no_project_kb_write: true
    no_calendar_event_write: true
    candidate_deltas_not_accepted_state: true
    model_usage_candidate_not_final_usage_log: true
```

## File Index

```yaml
file_list:
  - path: .claude/skills/flow-recap/SKILL.md
    status: created
    purpose: Skill entrypoint, trigger conditions, procedure, boundaries, supporting-file map, failure modes, output requirements, and completion gate.
    read_when:
      - skill_invocation
      - entrypoint_review
      - validating_skill_frontmatter

  - path: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
    status: created
    purpose: Minimal schema and boundary contract for flow_recap_packet.
    read_when:
      - creating_flow_recap_packet
      - validating_flow_recap_packet
      - checking_candidate_delta_or_usage_candidate_boundary

  - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
    status: created
    purpose: Candidate-only project status delta contract for FlowRecap outputs.
    read_when:
      - creating_candidate_project_status_delta
      - validating_candidate_delta
      - checking_status_merge_or_project_kb_boundary

  - path: .claude/skills/flow-recap/templates/flow-recap-packet-template.md
    status: created
    purpose: Operator-facing blank FlowRecap packet template.
    read_when:
      - drafting_operator_facing_recap
      - presenting_recap_for_review
      - avoiding_schema_heavy_output

  - path: .claude/skills/flow-recap/examples/apex-minimal-flow-recap-example.md
    status: created
    purpose: Synthetic APEX-only one-flow example for manual validation.
    read_when:
      - examples_needed
      - manual_validation
      - checking_negative_outputs

  - path: .claude/skills/flow-recap/package-manifest.md
    status: created
    purpose: Lightweight file index, package boundary summary, and completion status.
    read_when:
      - operator_inspects_package_structure
      - validating_package_files
```

## Downstream Interface Map

```yaml
downstream_interface_map:
  operator_review:
    consumes:
      - flow_recap_packet
      - candidate_project_status_delta
      - model_usage_delta_candidate
      - next_step_proposal
      - operator_review_flags
    gate: operator_validation_gate_for_recap

  status_merge:
    consumes:
      - flow_recap_packet
      - candidate_project_status_delta
    boundary: accepts_or_rejects_candidate_delta_later
    not_created_by_this_package: true

  model_usage_log:
    consumes:
      - model_usage_delta_candidate
    boundary: finalizes_usage_delta_later
    not_created_by_this_package: true

  project_kb_manager:
    consumes:
      - accepted_or_operator_confirmed_updates_only
    boundary: durable_project_kb_write_owner
    not_mutated_by_this_package: true

  PreCapNextDay:
    consumes:
      - future_context_only_after_status_merge_or_project_kb_acceptance
    boundary: next_day_plan_owner
    not_created_by_this_package: true
```

## Current Completion Status

```yaml
completion_status:
  source_files_inspected_or_gaps_recorded: true
  package_path_created: true
  flow_recap_packet_contract_created: true
  project_status_delta_contract_created: true
  template_created: true
  apex_minimal_example_created: true
  manifest_created: true
  SKILL_md_created_with_valid_frontmatter: true
  candidate_deltas_not_treated_as_accepted_state: true
  model_usage_candidate_not_treated_as_final_usage_log: true
  no_runtime_or_automation_created: true
  downstream_status_merge_and_model_usage_inputs_are_clear: true
```

## Package Ready Note

```yaml
package_ready_note:
  entrypoint_present: true
  package_invokable: true
  candidate_deltas_not_treated_as_accepted_state: true
  remaining_action: apply_patch_pack_review_only
```
