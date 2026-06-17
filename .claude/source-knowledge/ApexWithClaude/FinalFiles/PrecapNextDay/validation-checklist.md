# FILE: .claude/skills/precap-next-day/references/validation-checklist.md

# PreCap Next Day Validation Checklist

```yaml
validation_checklist_contract:
  artifact_name: precap_next_day_validation_checklist
  file_role: package_validation_reference
  purpose: >
    Define the validation checklist, completion gates, operator-review triggers,
    and correction rules used before accepting PreCapNextDay outputs. This file
    validates next_day_plan, flow_packet, flow_prompt_pack, usage-tracking,
    calendar-write-request, and workflow-process-validation integration without
    redefining their schemas.

  ownership:
    owns:
      - precap_next_day_validation_checklist
      - precap_next_day_validation_report
      - package_completion_gate
      - operator_review_trigger_matrix
      - boundary_validation_rules
      - validation_correction_rules
      - degraded_mode_acceptance_rules
    must_not_own:
      - next_day_plan_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - prompt_packet_schema
      - prompt_engineering_doctrine
      - routing_decision_schema
      - planned_usage_budget_schema
      - usage_delta_schema
      - calendar_connector_behavior
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - expected_output_type_schema
      - project_status_merge
      - FlowRecap_output
      - project_execution

  validation_principles:
    schema_authority_stays_with_contract_files: true
    checklist_is_gate_not_schema_duplicate: true
    missing_inputs_allow_degraded_output: true
    missing_inputs_require_review_flags: true
    operator_choice_is_final_when_tradeoff_is_explicit: true
    calendar_writes_require_explicit_acceptance: true
    daily_plan_generation_does_not_execute_work: true
```

## Validation Status Values

```yaml
validation_status_values:
  allowed:
    - valid
    - valid_with_warnings
    - operator_review_recommended
    - low_confidence_auto_generated
    - blocked_by_missing_operator_decision

  selection_rules:
    valid:
      use_when:
        - all_required_outputs_present
        - no_boundary_violations_detected
        - no_unresolved_high_impact_conflict
        - no_operator_decision_required_before_use
    valid_with_warnings:
      use_when:
        - required_outputs_present
        - output_is_usable
        - warnings_are_low_or_medium_impact
        - operator_can_execute_with_awareness
    operator_review_recommended:
      use_when:
        - output_is_mostly_usable
        - inferred_priorities_or_routes_matter
        - calendar_or_workflow_conflicts_need_attention
        - dependencies_are_missing_but_not_blocking
    low_confidence_auto_generated:
      use_when:
        - bootstrap_mode_or_sparse_context_used
        - several important inputs_are_missing
        - flows_or_prompts_include_many_assumptions
        - operator_review_is_strongly_recommended_before_execution
    blocked_by_missing_operator_decision:
      use_when:
        - two_or_more_valid_paths_conflict
        - calendar_write_requires_acceptance
        - high_impact_priority_tradeoff_is_unresolved
        - operator_has_not_chosen_between_explicit_options
```

## Checklist Structure

```yaml
precap_next_day_validation_checklist:
  type: object
  required:
    - checklist_id
    - validation_scope
    - input_resilience_checks
    - next_day_plan_checks
    - flow_packet_checks
    - flow_prompt_pack_checks
    - dependency_checks
    - calendar_checks
    - usage_tracking_checks
    - workflow_process_checks
    - operator_review_checks
    - boundary_checks
    - final_status
  fields:
    checklist_id:
      type: string
      format: "precap_next_day_validation_<short_slug>"
      required: true
    validation_scope:
      type: string
      allowed:
        - full_package_output
        - next_day_plan_only
        - flow_packet_set
        - flow_prompt_pack_set
        - degraded_bootstrap_output
        - calendar_constrained_output
      required: true
    input_resilience_checks:
      type: object_ref
      ref: input_resilience_checks
      required: true
    next_day_plan_checks:
      type: object_ref
      ref: next_day_plan_checks
      required: true
    flow_packet_checks:
      type: object_ref
      ref: flow_packet_checks
      required: true
    flow_prompt_pack_checks:
      type: object_ref
      ref: flow_prompt_pack_checks
      required: true
    dependency_checks:
      type: object_ref
      ref: dependency_checks
      required: true
    calendar_checks:
      type: object_ref
      ref: calendar_checks
      required: true
    usage_tracking_checks:
      type: object_ref
      ref: usage_tracking_checks
      required: true
    workflow_process_checks:
      type: object_ref
      ref: workflow_process_checks
      required: true
    operator_review_checks:
      type: object_ref
      ref: operator_review_checks
      required: true
    boundary_checks:
      type: object_ref
      ref: boundary_checks
      required: true
    final_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true
    unresolved_items:
      type: list
      item_type: string
      required: false
    correction_required_before_use:
      type: boolean
      required: true
```

## Input Resilience Checks

```yaml
input_resilience_checks:
  type: object
  required:
    - execution_mode_selected
    - available_inputs_listed
    - missing_inputs_classified
    - no_complete_input_requirement
    - assumptions_marked
    - degraded_mode_reason_present_when_needed
  checklist:
    execution_mode_selected:
      type: boolean
      required_value: true
      rule: "One execution mode must be selected before output validation."
    available_inputs_listed:
      type: boolean
      required_value: true
      rule: "The output must state which supplied or inferred input categories were used."
    missing_inputs_classified:
      type: boolean
      required_value: true
      rule: "Missing important inputs must be listed, not silently ignored."
    no_complete_input_requirement:
      type: boolean
      required_value: true
      rule: "PreCapNextDay must still produce a usable degraded output when complete context is absent."
    assumptions_marked:
      type: boolean
      required_value: true
      rule: "Any inferred priority, route, calendar assumption, or workflow label must be review-flagged."
    degraded_mode_reason_present_when_needed:
      type: boolean
      required_value: true
      rule: "If degraded or bootstrap mode is used, the reason must be explicit."

  accepted_degraded_modes:
    - standard_mode_with_missing_optional_inputs
    - bootstrap_mode
    - recap_recovery_mode
    - calendar_constrained_mode
    - prompt_heavy_mode_with_missing_usage_data
    - low_confidence_degraded_mode
```

## Next-Day Plan Checks

```yaml
next_day_plan_checks:
  type: object
  required:
    - next_day_plan_present
    - daily_scope_clear
    - fixed_flow_set_handled
    - active_flows_have_reason
    - omitted_flows_have_reason
    - ranked_or_ordered_day_structure_present
    - generated_file_index_present
    - review_status_present
  checklist:
    next_day_plan_present:
      type: boolean
      required_value: true
      rule: "A next_day_plan artifact must be present."
    daily_scope_clear:
      type: boolean
      required_value: true
      rule: "The output must describe the day-level goal and planning boundary."
    fixed_flow_set_handled:
      type: boolean
      required_value: true
      rule: "F1 Leela, F2 MasterOfArts, F3 Apex, and F4 Residual must each be planned, compressed, skipped, or explicitly omitted."
    active_flows_have_reason:
      type: boolean
      required_value: true
      rule: "Every active flow must include a concise reason for inclusion."
    omitted_flows_have_reason:
      type: boolean
      required_value: true
      rule: "Every omitted flow must include a concise omission reason."
    ranked_or_ordered_day_structure_present:
      type: boolean
      required_value: true
      rule: "The daily plan must provide an executable order or explicit operator-choice order."
    generated_file_index_present:
      type: boolean
      required_value: true
      rule: "The output must list expected downstream artifacts: flow packets, prompt packs, write requests, and handoff blocks."
    review_status_present:
      type: boolean
      required_value: true
      rule: "The daily plan must include a valid validation_status value."
```

## Flow Packet Checks

```yaml
flow_packet_checks:
  type: object
  required:
    - every_active_flow_has_flow_packet
    - flow_ids_are_valid
    - sprint_structure_is_valid
    - compressed_or_omitted_sprints_have_reason
    - raw_flow_dump_template_present
    - skipped_flow_marker_template_present_when_relevant
    - FlowRecap_handoff_block_present
  checklist:
    every_active_flow_has_flow_packet:
      type: boolean
      required_value: true
      rule: "Each active flow must have a corresponding flow_packet or extractable flow-packet block."
    flow_ids_are_valid:
      type: boolean
      required_value: true
      rule: "Flow identifiers must use F1, F2, F3, or F4 only."
    sprint_structure_is_valid:
      type: boolean
      required_value: true
      rule: "Active flows must include S1, S2, and S3 unless compression or omission is explicitly stated."
    compressed_or_omitted_sprints_have_reason:
      type: boolean
      required_value: true
      rule: "Any compressed or omitted sprint must include a reason and operator review flag when uncertain."
    raw_flow_dump_template_present:
      type: boolean
      required_value: true
      rule: "Each active flow must include a raw_flow_dump_template or reference to one."
    skipped_flow_marker_template_present_when_relevant:
      type: boolean
      required_value: true
      rule: "If a flow may be skipped, the output must preserve the skipped_flow_marker path or block."
    FlowRecap_handoff_block_present:
      type: boolean
      required_value: true
      rule: "Each active flow must include a FlowRecap handoff block with expected evidence and recap inputs."
```

## Flow Prompt Pack Checks

```yaml
flow_prompt_pack_checks:
  type: object
  required:
    - every_active_flow_has_prompt_pack
    - prompt_pack_is_per_flow
    - prompt_execution_packets_present
    - prompts_are_final_copy_paste_ready
    - one_primary_prompt_system_rule_preserved
    - start_and_follow_up_prompts_separated_when_needed
    - prompt_design_rationale_present
    - provider_rationale_present
    - prompt_failure_hints_present
    - light_capture_hints_do_not_replace_raw_flow_dump
  checklist:
    every_active_flow_has_prompt_pack:
      type: boolean
      required_value: true
      rule: "Every active flow must include a flow_prompt_pack or explicit reason for missing prompt pack."
    prompt_pack_is_per_flow:
      type: boolean
      required_value: true
      rule: "Prompt packs must be organized per flow, not as one undifferentiated day-level prompt blob."
    prompt_execution_packets_present:
      type: boolean
      required_value: true
      rule: "Prompt packs must contain prompt_execution_packet units or equivalent prompt blocks."
    prompts_are_final_copy_paste_ready:
      type: boolean
      required_value: true
      rule: "Prompt bodies must be directly usable and not presented as outlines unless degraded mode is explicitly selected."
    one_primary_prompt_system_rule_preserved:
      type: boolean
      required_value: true
      rule: "Each prompt execution unit must have one primary prompt system; fallback notes may exist but parallel alternatives are not default."
    start_and_follow_up_prompts_separated_when_needed:
      type: boolean
      required_value: true
      rule: "Start prompts and follow-up prompts must be distinct when the sprint requires iteration."
    prompt_design_rationale_present:
      type: boolean
      required_value: true
      rule: "Each prompt pack must include a short prompt-design rationale."
    provider_rationale_present:
      type: boolean
      required_value: true
      rule: "Each prompt pack must include a short provider or surface rationale, or mark provider_unspecified."
    prompt_failure_hints_present:
      type: boolean
      required_value: true
      rule: "Prompt packs must include concise failure hints or recovery cues."
    light_capture_hints_do_not_replace_raw_flow_dump:
      type: boolean
      required_value: true
      rule: "Prompt capture hints may assist the operator, but canonical capture remains raw_flow_dump plus FlowRecap."
```

## Dependency Checks

```yaml
dependency_checks:
  type: object
  required:
    - prompt_engineering_dependency_checked
    - usage_tracking_dependency_checked
    - workflow_process_dependency_checked
    - missing_dependency_degraded_mode_valid
    - cross_package_authority_boundaries_preserved
  checklist:
    prompt_engineering_dependency_checked:
      type: boolean
      required_value: true
      rule: "Prompt-engineering availability must be checked or explicitly marked missing."
    usage_tracking_dependency_checked:
      type: boolean
      required_value: true
      rule: "AI routing and usage tracking availability must be checked or explicitly marked missing."
    workflow_process_dependency_checked:
      type: boolean
      required_value: true
      rule: "Workflow-process-design availability must be checked or explicitly marked missing."
    missing_dependency_degraded_mode_valid:
      type: boolean
      required_value: true
      rule: "If any dependency package is missing, the output must still be usable with low-confidence flags where appropriate."
    cross_package_authority_boundaries_preserved:
      type: boolean
      required_value: true
      rule: "PreCapNextDay may consume dependency outputs but must not redefine their owned schemas or taxonomies."
```

## Calendar Checks

```yaml
calendar_checks:
  type: object
  required:
    - calendar_state_declared
    - workflow_blocks_only
    - write_requests_separate_from_actual_writes
    - explicit_acceptance_required_for_write
    - conflicts_flagged
    - non_workflow_calendar_blocks_not_created
  checklist:
    calendar_state_declared:
      type: boolean
      required_value: true
      rule: "The output must state whether calendar context was available, unavailable, or manually supplied."
    workflow_blocks_only:
      type: boolean
      required_value: true
      rule: "Calendar write requests must apply only to workflow blocks, not general life planning."
    write_requests_separate_from_actual_writes:
      type: boolean
      required_value: true
      rule: "The planning artifact must distinguish calendar_event_write_request from actual calendar mutation."
    explicit_acceptance_required_for_write:
      type: boolean
      required_value: true
      rule: "No calendar write can be treated as approved without explicit operator acceptance."
    conflicts_flagged:
      type: boolean
      required_value: true
      rule: "Known or likely schedule conflicts must create operator_review_flags."
    non_workflow_calendar_blocks_not_created:
      type: boolean
      required_value: true
      rule: "The skill must not create meals, sleep, personal logistics, or unrelated calendar blocks."
```

## Usage Tracking Checks

```yaml
usage_tracking_checks:
  type: object
  required:
    - planned_usage_budget_or_usage_plan_present
    - usage_tracking_tags_present
    - high_end_reasoning_score_valid_when_used
    - scarce_quota_rationale_present_when_used
    - supplemental_API_default_preserved
    - exact_prices_or_limits_not_invented
  checklist:
    planned_usage_budget_or_usage_plan_present:
      type: boolean
      required_value: true
      rule: "The daily plan must include a planned usage budget, usage_tracking_plan, or explicit degraded-mode placeholder."
    usage_tracking_tags_present:
      type: boolean
      required_value: true
      rule: "Prompt packs must include usage_tracking_tags where routing decisions are made."
    high_end_reasoning_score_valid_when_used:
      type: boolean
      required_value: true
      rule: "If high-end reasoning is recommended, impact, risk, evidence_need, and ambiguity must be integers from 1 to 100."
    scarce_quota_rationale_present_when_used:
      type: boolean
      required_value: true
      rule: "Any scarce monthly mode recommendation must include a concise quota rationale."
    supplemental_API_default_preserved:
      type: boolean
      required_value: true
      rule: "API usage must remain supplemental and low-reasoning by default unless the operator chooses otherwise."
    exact_prices_or_limits_not_invented:
      type: boolean
      required_value: true
      rule: "The output must not claim current prices, exact limits, remaining usage, or exact model availability unless supplied or verified."
```

## Workflow Process Checks

```yaml
workflow_process_checks:
  type: object
  required:
    - workflow_stage_present_or_flagged
    - process_stage_present_or_flagged
    - expected_output_type_present_or_flagged
    - prompt_workflow_alignment_checked
    - mismatch_resolution_present_when_needed
    - workflow_process_fit_not_overridden_by_cost
  checklist:
    workflow_stage_present_or_flagged:
      type: boolean
      required_value: true
      rule: "Each active prompt or sprint must include a workflow_stage or explicit missing-label flag."
    process_stage_present_or_flagged:
      type: boolean
      required_value: true
      rule: "Each active prompt or sprint must include a process_stage or explicit missing-label flag."
    expected_output_type_present_or_flagged:
      type: boolean
      required_value: true
      rule: "Each active sprint must include expected_output_type or explain why it is unknown."
    prompt_workflow_alignment_checked:
      type: boolean
      required_value: true
      rule: "Prompts must be checked against workflow/process labels and expected output type."
    mismatch_resolution_present_when_needed:
      type: boolean
      required_value: true
      rule: "If a prompt does not fit the workflow/process label, the output must either correct it or flag operator review."
    workflow_process_fit_not_overridden_by_cost:
      type: boolean
      required_value: true
      rule: "Cost or routing convenience must not silently override workflow/process validity."
```

## Operator Review Checks

```yaml
operator_review_checks:
  type: object
  required:
    - operator_review_flags_present
    - high_impact_assumptions_flagged
    - tradeoff_card_present_when_conflict_exists
    - blocked_decision_explicit_when_needed
    - review_status_matches_risk
  checklist:
    operator_review_flags_present:
      type: boolean
      required_value: true
      rule: "The output must include operator_review_flags, even if the list is empty."
    high_impact_assumptions_flagged:
      type: boolean
      required_value: true
      rule: "Any high-impact inferred priority, schedule, route, or workflow label must be flagged."
    tradeoff_card_present_when_conflict_exists:
      type: boolean
      required_value: true
      rule: "When valid options conflict, present a compact tradeoff card rather than silently choosing."
    blocked_decision_explicit_when_needed:
      type: boolean
      required_value: true
      rule: "If operator choice is required before execution, status must be blocked_by_missing_operator_decision."
    review_status_matches_risk:
      type: boolean
      required_value: true
      rule: "The final validation_status must reflect actual risk and uncertainty, not optimistic completion."

  operator_review_flag_allowed:
    - missing_project_status
    - missing_weekly_plan
    - missing_prior_flow_recap
    - inferred_priority
    - inferred_flow_scope
    - compressed_flow
    - omitted_flow
    - prompt_engineering_dependency_missing
    - usage_tracking_dependency_missing
    - workflow_process_dependency_missing
    - quota_unknown
    - scarce_mode_recommended
    - provider_unspecified
    - calendar_context_missing
    - calendar_conflict
    - calendar_write_needs_acceptance
    - workflow_process_mismatch
    - expected_output_type_unclear
    - high_impact_tradeoff
    - operator_decision_required
```

## Boundary Checks

```yaml
boundary_checks:
  type: object
  required:
    - project_execution_not_performed
    - FlowRecap_not_run
    - project_status_not_merged
    - final_OpenRouter_model_map_not_created
    - prompt_doctrine_not_redefined
    - routing_schema_not_redefined
    - workflow_taxonomies_not_redefined
    - calendar_events_not_written_without_acceptance
    - no_new_permanent_agents_created
    - no_runtime_or_infrastructure_files_created
  checklist:
    project_execution_not_performed:
      type: boolean
      required_value: true
      rule: "The output may plan work but must not execute project work."
    FlowRecap_not_run:
      type: boolean
      required_value: true
      rule: "The output may prepare FlowRecap handoff blocks but must not produce FlowRecap outputs."
    project_status_not_merged:
      type: boolean
      required_value: true
      rule: "The output must not perform APSU or project-status merge."
    final_OpenRouter_model_map_not_created:
      type: boolean
      required_value: true
      rule: "The output must not finalize OpenRouter model mapping."
    prompt_doctrine_not_redefined:
      type: boolean
      required_value: true
      rule: "The output must consume prompt-engineering contracts rather than rewriting prompt doctrine."
    routing_schema_not_redefined:
      type: boolean
      required_value: true
      rule: "The output must consume routing/usage contracts rather than rewriting routing schemas."
    workflow_taxonomies_not_redefined:
      type: boolean
      required_value: true
      rule: "The output must consume workflow-process-design taxonomies rather than redefining them."
    calendar_events_not_written_without_acceptance:
      type: boolean
      required_value: true
      rule: "Calendar mutations require explicit operator acceptance."
    no_new_permanent_agents_created:
      type: boolean
      required_value: true
      rule: "The output must not add permanent agents beyond the existing control-plane roles."
    no_runtime_or_infrastructure_files_created:
      type: boolean
      required_value: true
      rule: "The output must not create runtime deployment, CI, cron, Kanban, secrets, settings, or infrastructure artifacts."
```

## Final Completion Gate

```yaml
package_completion_gate:
  next_day_plan_validated: true
  input_resilience_validated: true
  each_active_flow_has_flow_packet: true
  each_active_flow_has_prompt_pack_or_review_flag: true
  FlowRecap_handoff_blocks_present: true
  usage_tracking_plan_or_degraded_placeholder_present: true
  calendar_write_requests_are_gated: true
  workflow_process_alignment_checked: true
  operator_review_flags_present: true
  validation_status_is_canonical: true
  no_project_execution_performed: true
  no_FlowRecap_run: true
  no_status_merge_performed: true
  no_schema_authority_drift: true
  no_unapproved_calendar_write: true
  no_final_OpenRouter_model_map_created: true
```

## Correction Rules

```yaml
validation_correction_rules:
  missing_required_artifact:
    trigger: "A required plan, flow packet, prompt pack, usage plan, write request, or handoff block is absent without explanation."
    correction: "Add the artifact, add a degraded placeholder, or mark blocked_by_missing_operator_decision."

  unflagged_assumption:
    trigger: "The plan infers priority, schedule, provider, quota, workflow stage, or output type without review flag."
    correction: "Add operator_review_flags and downgrade validation_status if impact is material."

  schema_duplication_detected:
    trigger: "The checklist restates a schema owned by another contract file."
    correction: "Replace duplicated schema with a reference to the owning contract and keep only checklist logic here."

  workflow_prompt_mismatch:
    trigger: "A prompt body, provider route, or sprint task does not fit workflow_stage, process_stage, or expected_output_type."
    correction: "Revise the prompt or route, or present a tradeoff card for operator choice."

  calendar_write_not_gated:
    trigger: "Calendar event creation or update is implied without explicit operator acceptance."
    correction: "Convert it into calendar_event_write_request and mark calendar_write_needs_acceptance."

  boundary_violation:
    trigger: "The output executes work, runs FlowRecap, merges status, creates infrastructure, or finalizes OpenRouter mapping."
    correction: "Remove the violating content and replace it with a handoff, request, placeholder, or operator-review flag."
```

## Minimal Validation Report Example

```yaml
precap_next_day_validation_report:
  report_id: precap_next_day_validation_example
  validation_scope: full_package_output
  execution_mode: standard_mode
  final_status: valid_with_warnings
  correction_required_before_use: false

  passed_groups:
    - input_resilience_checks
    - next_day_plan_checks
    - flow_packet_checks
    - flow_prompt_pack_checks
    - dependency_checks
    - usage_tracking_checks
    - workflow_process_checks
    - boundary_checks

  warning_groups:
    - calendar_checks
    - operator_review_checks

  failed_groups: []

  operator_review_flags:
    - calendar_context_missing
    - quota_unknown

  unresolved_items:
    - "Calendar workflow blocks are proposed as write requests only because current calendar context is unavailable."
    - "Exact remaining quota is unknown, so scarce-mode recommendations require operator review."

  completion_gate:
    next_day_plan_validated: true
    input_resilience_validated: true
    each_active_flow_has_flow_packet: true
    each_active_flow_has_prompt_pack_or_review_flag: true
    FlowRecap_handoff_blocks_present: true
    usage_tracking_plan_or_degraded_placeholder_present: true
    calendar_write_requests_are_gated: true
    workflow_process_alignment_checked: true
    operator_review_flags_present: true
    validation_status_is_canonical: true
    no_project_execution_performed: true
    no_FlowRecap_run: true
    no_status_merge_performed: true
    no_schema_authority_drift: true
    no_unapproved_calendar_write: true
    no_final_OpenRouter_model_map_created: true
```

---

# VALIDATION — FILE-SPECIFIC CHECKS

- [ ] Exactly one file was produced.
- [ ] File target is `.claude/skills/precap-next-day/references/validation-checklist.md`.
- [ ] File owns validation checklist/report and completion gate only.
- [ ] File does not redefine next_day_plan, flow_packet, flow_prompt_pack, prompt_packet, routing, usage, calendar connector, or workflow taxonomy schemas.
- [ ] YAML uses 2-space indentation.
- [ ] Validation statuses use canonical allowed values.
- [ ] Boundary checks prevent project execution, FlowRecap, status merge, unapproved calendar writes, infrastructure creation, and final OpenRouter model mapping.
- [ ] Next prompt target is `package-manifest.md`.

---

# NEXT PROMPT

Paste this next:
> Prompt PND11:
> Create exactly one file.
>
> # FILE: .claude/skills/precap-next-day/package-manifest.md
>
> File type: package_manifest.
> Context carry-forward:
> - .claude/skills/precap-next-day/SKILL.md
> - all PreCapNextDay reference contracts created so far
> - dependency package manifests for prompt-engineering, ai-routing-and-usage-tracking, and workflow-process-design when available
>
> This file must define:
> - lightweight package index
> - package purpose
> - all package files with path, purpose, and read_when
> - package-level boundaries
> - package-level acceptance checks
>
> Rules:
> - Keep the manifest under 60 lines where practical.
> - Do not duplicate schemas, validation checklists, or dependency contracts.
> - Do not include validation_role fields.
> - Do not create runtime, calendar connector, CI, deployment, cron, Kanban, SOUL.md, AGENTS.md, or settings files.
> - Use YAML with 2-space indentation.
>
> After this file, report that the PreCapNextDay package sequence is complete.
