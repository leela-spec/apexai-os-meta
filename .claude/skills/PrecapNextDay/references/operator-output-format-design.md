# FILE: .claude/skills/PrecapNextDay/references/operator-output-format-design.md

# Operator Output Format Design

```yaml
operator_output_format_design:
  artifact_name: operator_output_format_design
  file_role: precap_next_day_template_design_reference
  purpose: >
    Define how PreCap Next Day contract-owned fields are surfaced as
    operator-readable templates, dashboards, examples, and review fixtures
    without redefining schemas or implying execution.
  owns:
    - template_derivation_workflow
    - operator_readable_output_layout
    - template_file_split_rules
    - dashboard_markdown_conventions
    - APEX_only_example_policy
    - placeholder_conventions
    - roundtrip_test_method
    - no_hallucination_rules_for_examples
  must_not_own:
    - next_day_plan_schema
    - flow_packet_schema
    - flow_prompt_pack_schema
    - prompt_packet_schema
    - routing_decision_schema
    - calendar_event_write_request_schema
    - FlowRecap_output_schema
    - project_execution_schema
```

## Design Boundary

This file is a presentation reference. It explains how to turn existing PreCap Next Day contracts into usable Markdown output forms.

It does not define new required fields, statuses, routing rules, flow identity values, calendar write policies, prompt doctrine, or FlowRecap outputs.

## Template Derivation Workflow

```yaml
template_derivation_workflow:
  steps:
    - id: 1_contract_extraction
      action: Read the relevant contract and list only the fields that must be surfaced for operator use.
      output: field_surface_map
    - id: 2_operator_journey_design
      action: Decide what the operator must review first, what can be summarized, and what belongs in linked files.
      output: dashboard_section_order
    - id: 3_template_skeleton_creation
      action: Create blank Markdown templates with compact YAML status blocks, tables, placeholders, and file references.
      output: blank_template_file
    - id: 4_APEX_example_instantiation
      action: Fill one APEX-only example set using F1-F4 as APEX buildout slices.
      output: example_artifact_set
    - id: 5_roundtrip_testing
      action: Check contract-to-template, template-to-example, example-to-contract, boundary, and second-chat usability.
      output: audit_summary
    - id: 6_handoff_preparation
      action: Record unresolved decisions and next safe edits for the operator.
      output: review_handoff
```

## Field Surface Map Pattern

Use this pattern before drafting or revising a template.

```yaml
field_surface_map:
  template_path: "<template_path>"
  artifact: "<artifact_name>"
  schema_authority: "<contract_reference_path>"
  presentation_role: "<operator_dashboard_or_container_role>"
  surfaced_contract_objects:
    - "<contract_object_or_field>"
  presentation_only_fields:
    - "operator_label"
    - "operator_action"
    - "display_notes"
  forbidden:
    - do_not_define_new_required_schema_fields
    - do_not_define_new_validation_status_values
    - do_not_claim_execution_happened
    - do_not_create_calendar_events
    - do_not_run_FlowRecap
```

## Dashboard Markdown Conventions

```yaml
dashboard_markdown_conventions:
  main_format: markdown_dashboard_with_compact_yaml_status_blocks
  status_blocks:
    format: fenced_yaml
    max_lines_preferred: 20
    purpose: machine_readable_summary_before_human_tables
  tables:
    use_for:
      - flow_overview
      - generated_file_index
      - input_context
      - operator_review_flags
      - workflow_blocks
  placeholders:
    syntax: angle_brackets
    examples:
      - "<execution_day>"
      - "<plan_id>"
      - "<flow_id>"
      - "<APEX_operator_label>"
      - "<artifact_ref>"
  status_defaults:
    project_execution_status: not_executed
    prompt_execution_status: not_executed
    calendar_write_status: review_only_or_no_write_requested
    FlowRecap_status: handoff_prepared_not_run
```

## Template File Split Rules

```yaml
template_file_split_rules:
  next_day_plan:
    role: main_operator_dashboard
    includes: flow_summaries_and_file_refs
    excludes: full_flow_packets_and_full_prompt_packs
  flow_packet:
    role: per_flow_execution_container
    includes: sprint_plan_expected_outputs_capture_and_handoff_refs
    excludes: actual_execution_results
  flow_prompt_pack:
    role: per_flow_prompt_container
    includes: prompt_packet_placeholders_or_refs
    excludes: prompt_doctrine_and_provider_specific_schema
  capture_and_handoff:
    role: post_execution_capture_preparation
    includes: raw_dump_template_skipped_marker_handoff_block
    excludes: filled_execution_dump
  calendar_event_write_request:
    role: reviewable_calendar_request
    includes: approval_gate_and_workflow_block_requests
    excludes: actual_calendar_mutation
  usage_tracking_summary:
    role: usage_intent_and_capture_preparation
    includes: dependency_status_usage_intent_capture_fields
    excludes: quota_claims_without_operator_verified_source
```

## APEX-Only Example Policy

```yaml
APEX_only_example_policy:
  all_example_flows_project: APEX
  all_example_sprints_project: APEX
  allowed_operator_labels:
    F1: APEX_repo_foundation
    F2: APEX_skill_database_contracts
    F3: APEX_output_templates_examples
    F4: APEX_validation_handover
  non_APEX_project_names:
    allowed_only_as: historical_or_boundary_reference
    forbidden_as: active_flow_goal
  schema_safety_note: >
    If a contract field only allows canonical project or flow_role values, keep
    the contract-safe value and put the APEX-specific label in presentation-only
    fields such as operator_label, primary_goal, notes, or display tables.
```

## Roundtrip Test Method

```yaml
roundtrip_test_method:
  contract_to_template:
    check: Required contract-owned objects are surfaced or intentionally referenced.
  template_to_example:
    check: Blank templates can be filled into one coherent APEX-only example set.
  example_to_contract:
    check: Examples do not introduce new statuses, schemas, prompt doctrine, routing logic, or calendar policy.
  boundary_test:
    check: Outputs do not execute work, run FlowRecap, merge status, create calendar events, or activate non-APEX flows.
  second_chat_usability:
    check: A new repo-enabled chat can use the design reference, templates, and examples without inventing structure.
```

## No-Hallucination Rules

```yaml
no_hallucination_rules:
  schema_boundary:
    rule: Do not invent schema fields.
    correction: Use placeholders or clearly presentation-only labels.
  project_scope:
    rule: Do not import active goals from non-APEX projects.
    correction: Convert example content to APEX-only or remove it.
  output_status:
    rule: Do not claim execution happened.
    correction: Mark outputs as draft, planned, prepared, review_ready, or operator_review_recommended.
  prompt_boundary:
    rule: Do not create prompt doctrine in PreCap Next Day templates.
    correction: Reference prompt-engineering dependencies or use degraded generic prompt placeholders.
  calendar_boundary:
    rule: Do not create or imply actual calendar events.
    correction: Use review_only or no_write_requested with pending approval.
  FlowRecap_boundary:
    rule: Do not run FlowRecap or create FlowRecap output.
    correction: Prepare FlowRecap handoff only.
  status_merge_boundary:
    rule: Do not merge project status.
    correction: Prepare future context notes only when allowed by the output contract.
```
