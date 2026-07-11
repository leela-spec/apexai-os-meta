# APEX Step 4 Template Implementation Handoff

```yaml
document:
  id: apex-step4-template-implementation-handoff
  title: APEX Step 4 Template Implementation Handoff
  status: bounded_handoff_ready
  created_date: 2026-07-11
  repository: leela-spec/apexai-os-meta
  branch: main
  source_package: apex-meta/operator-output-design/step3-output-design-system/
  target_stage: step4_template_implementation
  record_type: implementation_handoff
```

## 1. Purpose

```yaml
purpose:
  objective: >
    Translate the completed Step 3 operator-facing design system into a bounded
    template implementation plan for J1-J12 without creating runtime workflows,
    changing domain schemas, or silently treating unapplied Round 6 patches as
    already merged into their source design files.
  this_file_authorizes:
    - template_inventory_and_sequence_design
    - template_file_specification
    - shared_component_reuse_rules
    - validation_checklist_design
    - example_and_fixture_planning
  this_file_does_not_authorize:
    - applying_round6_patches_to_source_designs
    - creating_templates_in_this_iteration
    - modifying_skill_contracts
    - executing_prompts
    - creating_runtime_orchestration
    - creating_agents_schedulers_or_calendar_writes
    - mutating_durable_project_state
```

## 2. Authority stack

Use the following authority order. Later files clarify or project earlier files but do not replace domain-owned schemas.

```yaml
authority_stack:
  1_package_inventory:
    path: 00-package-manifest.okf.yaml
    role: package_inventory_and_status_authority
  2_design_principles:
    path: 01-operator-output-design-principles.okf.yaml
    role: operator_presentation_principles
  3_shared_anatomy:
    path: 02-shared-card-and-brief-anatomy.okf.yaml
    role: shared_human_first_machine_second_structure
    overlay_required: round6-patches/01-shared-card-canonical-names.patch
  4_artifact_designs:
    paths:
      - 03-planning-artifact-designs.okf.yaml
      - 04-flow-execution-card-design.okf.yaml
      - 05-prompt-file-and-index-design.okf.yaml
      - 06-execution-evidence-handoff-design.okf.yaml
      - 07-skip-marker-low-priority-design.okf.yaml
      - 10-flow-recap-result-card-design.okf.yaml
      - 11-usage-learning-card-design.okf.yaml
      - 14-status-merge-decision-card-design.okf.yaml
      - 15-project-kb-update-card-design.okf.yaml
      - 16-project-status-overview-design.okf.yaml
      - 17-ai-routing-card-design.okf.yaml
    overlay_required:
      - round6-patches/02-j3-j4-depth-separation.patch
      - round6-patches/03-j9-durable-merge-confirmation.patch
      - round6-patches/04-j10-durable-update-result.patch
      - round6-patches/06-j11-project-status-contract-alignment.patch
      - round6-patches/07-j12-routing-contract-alignment.patch
  5_local_relationships:
    paths:
      - 03-planning-artifact-designs.okf.yaml
      - 08-round3-cross-artifact-relationship.okf.yaml
      - 12-round4-cross-artifact-relationship.okf.yaml
      - 18-round5-cross-artifact-relationships.okf.yaml
    overlay_required:
      - round6-patches/05-j9-j10-j11-confirmed-truth-path.patch
  6_cross_cutting_resolution:
    path: 20-round6-cross-cutting-consistency-resolution.okf.yaml
    role: state_vocabulary_and_translation_authority
  7_canonical_projection:
    path: 21-canonical-artifact-family-and-lifecycle-map.okf.yaml
    role: complete_J1_to_J12_navigation_and_lifecycle_map
  8_round6_closeout:
    path: 22-round6-decision-and-verification-record.okf.yaml
    role: accepted_target_state_and_unapplied_patch_status
  9_domain_contracts:
    role: final_schema_authority
    rule: existing_skill_and_reference_contracts_override_template_inference
```

## 3. Patch-pending operating rule

```yaml
patch_pending_rule:
  source_design_status: pre_round6_text_with_verified_patch_overlays
  patch_application_status: not_applied
  implementation_interpretation: >
    When specifying a template, read the source design and its listed Round 6
    patch together as one intended target design. Never state or imply that the
    source file itself already contains the patch.
  required_template_metadata:
    - source_design_ref
    - round6_overlay_refs_when_applicable
    - domain_contract_refs
  forbidden:
    - copying_stale_names_from_unpatched_sources
    - implementing_J3_with_complete_J4_execution_depth
    - showing_J9_merged_without_durable_confirmation
    - treating_prepared_J10_write_as_J11_truth
    - creating_J11_workstreams
    - using_unverified_exact_model_as_J12_route_truth
```

## 4. Canonical template inventory

```yaml
template_inventory:
  J1:
    artifact: Project_State_Success_Card
    template_priority: high
    template_role: planning_input_summary
  J2:
    artifact: Weekly_Command_Brief
    template_priority: high
    template_role: cross_project_week_direction
  J3:
    artifact: PreCap_Next_Day_Brief
    template_priority: high
    template_role: compact_day_level_three_sprint_outline
  J4:
    artifact: Flow_Execution_Card
    template_priority: critical
    template_role: complete_single_flow_execution_workspace
  J5:
    artifact: Prompt_Files_and_Index
    template_priority: critical
    template_role: directly_openable_prompt_assets_and_mapping
  J6:
    artifact: Execution_Evidence_Handoff
    template_priority: high
    template_role: conditional_evidence_preparation
    conditional_subtemplate: Skip_Marker
  J7:
    artifact: FlowRecap_Result_Card
    template_priority: critical
    template_role: execution_interpretation_and_candidate_change
  J8:
    artifact: Usage_Learning_Card
    template_priority: medium
    template_role: lightweight_advisory_usage_learning
  J9:
    artifact: Status_Merge_Decision_Card
    template_priority: critical
    template_role: candidate_state_review_and_merge_proposal
  J10:
    artifact: Project_KB_Update_Card
    template_priority: critical
    template_role: durable_write_preparation_execution_and_confirmation
  J11:
    artifact: Project_Status_Overview
    template_priority: high
    template_role: confirmed_cross_project_truth_and_ranked_attention
  J12:
    artifact: AI_Routing_Card
    template_priority: high
    template_role: advisory_stable_surface_route_recommendation
```

## 5. Shared template anatomy

Every primary template should follow the same presentation order unless its design explicitly requires less.

```yaml
shared_template_anatomy:
  layer_1_result_card:
    required:
      - title
      - result_or_current_state
      - exact_next_action
      - review_needed
    conditional:
      - blocker_or_warning
      - confidence
      - durable_change_status
  layer_2_operator_actions:
    rule: show_only_actions_valid_for_this_artifact
  layer_3_supporting_context:
    rule: include_only_context_needed_to_understand_or_act
  layer_4_provenance_and_confidence:
    rule: compact_by_default_expand_only_when_material
  layer_5_machine_handoff:
    rule: minimum_fields_for_next_consumer_only
  layer_6_validation:
    rule: technical_checks_after_operator_value_not_before
```

## 6. Per-template implementation requirements

```yaml
per_template_requirements:
  J1:
    must_show:
      - relevant_project_state
      - success_context
      - constraints
    must_not:
      - create_weekly_or_daily_plan
  J2:
    must_show:
      - represented_projects
      - weekly_direction
      - prioritized_work
      - constraints
    must_not:
      - become_daily_execution_workspace
  J3:
    must_show:
      - day_goal
      - ordered_flows
      - concise_S1_S2_S3_outline_per_flow
      - flow_execution_card_refs
    must_not:
      - repeat_complete_tasks_inputs_prompts_done_conditions_or_stop_conditions
  J4:
    must_show:
      - complete_flow_context
      - full_three_sprint_plan
      - tasks_inputs_dependencies_outputs
      - done_and_stop_or_review_conditions
      - direct_prompt_file_links
    must_not:
      - duplicate_prompt_content
      - duplicate_routing_reasoning
  J5:
    must_show:
      - one_directly_openable_file_per_prompt
      - lightweight_sprint_to_prompt_mapping
      - target_surface
      - routing_ref
    must_not:
      - repeat_flow_plan
  J6:
    must_show:
      - planned_vs_actual_evidence
      - outputs_decisions_blockers_unresolved_questions
      - readiness_for_recap
    conditional:
      - normalize_only_when_evidence_complexity_requires_it
      - use_minimal_Skip_Marker_when_not_executed
    must_not:
      - interpret_project_meaning
  J7:
    must_show:
      - planned_vs_actual
      - outcome_and_artifacts
      - decisions_blockers_unresolved_questions
      - candidate_project_status_delta
      - evidence_and_confidence
    must_not:
      - accept_or_write_candidate_state
  J8:
    must_show:
      - usage_evidence_summary
      - one_allowed_route_signal
      - outcome_quality
      - confidence
    must_not:
      - override_routing
  J9:
    must_show:
      - current_accepted_state
      - candidate_change
      - evidence_and_conflicts
      - review_decision
      - merge_proposal
    merged_display_gate:
      required: durable_write_confirmation_ref
    must_not:
      - write_project_KB
  J10:
    must_show:
      - accepted_change_ref
      - target_KB_location
      - change_type
      - provenance
      - write_execution_status
      - effective_change
      - updated_freshness
    durable_confirmation_gate:
      required_for_executed_or_partially_executed: durable_update_result_ref
    must_not:
      - treat_prepared_or_awaiting_confirmation_as_durable_truth
  J11:
    must_show:
      - project_task_subtask_hierarchy
      - priority_urgency_date_ratings
      - ranked_task_view
      - temporary_unassigned_when_needed
      - operator_validation_flags_when_needed
    must_not:
      - create_workstreams
      - accept_candidate_updates
      - invent_missing_status
  J12:
    must_show:
      - task_context
      - selected_surface_class
      - fallback_surface
      - rationale_constraints_confidence
      - alternatives_when_material
      - operator_decision
    optional:
      verified_model_ref:
        requires:
          - current_verification_evidence
          - verification_date_or_window
          - source_ref
    must_not:
      - execute_route
      - finalize_volatile_model_mapping
```

## 7. Recommended implementation sequence

```yaml
implementation_sequence:
  batch_1_shared_foundation:
    outputs:
      - shared_result_card_partial
      - shared_operator_action_partial
      - shared_provenance_partial
      - shared_machine_handoff_partial
    validation_goal: prove_human_first_machine_second_structure
  batch_2_execution_spine:
    templates:
      - J3
      - J4
      - J5
      - J6
    validation_goal: prove_day_outline_execution_prompt_and_evidence_non_duplication
  batch_3_recap_and_state:
    templates:
      - J7
      - J9
      - J10
      - J11
    validation_goal: prove_candidate_approval_write_and_truth_separation
  batch_4_planning_and_learning:
    templates:
      - J1
      - J2
      - J8
    validation_goal: prove_context_planning_and_advisory_learning_boundaries
  batch_5_routing:
    templates:
      - J12
    validation_goal: prove_stable_surface_class_and_operator_approval_boundary
  batch_6_examples_and_cross_artifact_test:
    outputs:
      - one_minimal_example_per_template
      - one_end_to_end_J3_to_J11_fixture
      - one_J8_and_J11_to_J12_fixture
    validation_goal: prove_handoffs_without_schema_duplication
```

## 8. File creation rules for Step 4

```yaml
file_creation_rules:
  preferred_template_location: apex-meta/operator-output-design/step4-templates/
  naming_pattern: "J{number}-{canonical-artifact-name}-template.okf.md"
  shared_components_location: apex-meta/operator-output-design/step4-templates/shared/
  examples_location: apex-meta/operator-output-design/step4-templates/examples/
  validation_location: apex-meta/operator-output-design/step4-templates/validation/
  one_primary_template_per_artifact: true
  skip_marker_rule: subtemplate_or_small_shared_partial_not_full_primary_template
  prompt_file_rule: J5_may_define_file_and_index_patterns_but_not_final_prompt_doctrine
  machine_blocks: compact_and_contract_referenced
  no_runtime_code: true
```

## 9. Validation gates

```yaml
validation_gates:
  G1_yaml_and_markdown_integrity:
    checks:
      - structured_blocks_parse
      - links_and_relative_paths_are_valid
      - no_duplicate_top_level_keys
  G2_operator_first_screen:
    checks:
      - state_or_result_visible
      - exact_next_action_visible
      - review_needed_visible
      - blocker_or_warning_visible_when_material
  G3_single_job_and_non_duplication:
    checks:
      - one_primary_operator_job
      - no_neighbor_artifact_content_ownership
      - machine_block_does_not_repeat_full_human_output
  G4_contract_boundary:
    checks:
      - domain_contract_referenced
      - no_domain_schema_redefinition
      - unknown_fields_not_invented
  G5_lifecycle_boundary:
    checks:
      - candidate_not_equal_accepted
      - approval_not_equal_execution
      - prepared_write_not_equal_confirmed_truth
      - advisory_route_not_equal_execution
  G6_patch_overlay_integrity:
    checks:
      - every_patch_pending_template_lists_overlay_ref
      - no_false_claim_that_patch_was_applied
      - canonical_names_used
  G7_cross_artifact_handoff:
    checks:
      - minimum_required_refs_preserved
      - source_and_target_domain_states_preserved
      - evidence_or_confirmation_ref_preserved_when_required
```

## 10. Definition of done for Step 4

```yaml
step4_definition_of_done:
  required:
    - shared_template_components_created
    - J1_to_J12_primary_templates_created
    - Skip_Marker_subtemplate_created
    - minimal_examples_created
    - cross_artifact_fixture_created
    - all_validation_gates_passed
    - patch_pending_sources_labeled_correctly
    - no_runtime_or_schema_mutation
  not_required:
    - applying_round6_patches
    - production_runtime_integration
    - autonomous_execution
    - calendar_integration
    - final_exact_model_mapping
```

## 11. Open decisions before template creation

```yaml
open_decisions:
  O1_patch_application:
    question: Should the seven Round 6 patches be applied before templates are created?
    current_default: no_apply_use_explicit_overlay_refs
    authority_required: explicit_operator_authorization
  O2_template_file_format:
    question: Should primary templates be Markdown with YAML blocks or pure YAML?
    recommended_default: Markdown_with_compact_YAML_blocks
  O3_shared_partial_mechanism:
    question: Should shared anatomy be copied minimally or referenced as reusable partial files?
    recommended_default: reusable_shared_partials_plus_small_local_overrides
  O4_example_depth:
    question: Should examples be minimal fixtures or realistic full operator cases?
    recommended_default: minimal_first_then_one_end_to_end_realistic_fixture
```

## 12. Handoff status

```yaml
handoff_status:
  step3_design_layer: complete
  round6_patch_artifacts: verified_but_unapplied
  step4_handoff: complete
  templates_created: false
  runtime_created: false
  next_safe_action: begin_step4_batch_1_shared_foundation_after_operator_or_new_chat_review
```
