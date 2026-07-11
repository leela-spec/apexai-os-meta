# APEX Step 4 Template Implementation Handoff

## 1. Document Identity

```yaml
document:
  id: apex-step4-template-implementation-handoff
  title: APEX Step 4 Template Implementation Handoff
  status: bounded_handoff_ready
  created_date: 2026-07-11
  repository: leela-spec/apexai-os-meta
  branch: main
  file_path: >
    apex-meta/operator-output-design/step3-output-design-system/
    23-step4-template-implementation-handoff.okf.md
  source_package: apex-meta/operator-output-design/step3-output-design-system/
  target_stage: step4_template_implementation
  recovery_state_before_repair: file_exists_partial_or_invalid
  purpose: >
    Provide the smallest safe continuation brief from the completed Step 3
    design layer into operator-facing template implementation without applying
    Round 6 patches, changing domain contracts, or creating runtime behavior.
```

## 2. Current Authority State

```yaml
current_authority_state:
  primary_authorities:
    - 22-round6-decision-and-verification-record.okf.yaml
    - 21-canonical-artifact-family-and-lifecycle-map.okf.yaml
    - 00-package-manifest.okf.yaml
  authority_rule: >
    Use file 22 for the recorded closeout and mutation boundary, file 21 for
    canonical J1-J12 names and lifecycle relationships, and file 00 for package
    inventory. Existing skill and reference contracts remain final schema
    authority.

  step3_state:
    design_layer: complete
    round6_closeout_record: present
    templates_created: false
    runtime_created: false

  source_designs_02_03_14_15_16_17_18:
    current_state: mixed_recorded_workspace_state
    explanation: >
      File 22 records that these source designs were modified before its
      closeout record. They must therefore not be described uniformly as
      untouched pre-Round-6 text.
    patches_pending: true
    uniform_patch_application_must_not_be_assumed: true

  patch_artifacts:
    registered_count: 7
    application_authorized: false
    application_status: not_uniformly_established
    live_availability_rule: verify_only_the_overlay_needed_for_the_active_batch

  recorded_discrepancy:
    manifest_claim: patch_artifacts_present_and_source_designs_unmodified
    closeout_claim: source_designs_previously_modified_and_patch_workspace_missing
    handling: >
      Do not resolve this discrepancy by inference. Verify the exact active
      source and overlay before implementing each bounded template batch.
```

## 3. Step 4 Objective

```yaml
step4_objective:
  goal: >
    Convert accepted operator-output designs into compact, reusable templates
    that preserve human-first presentation and machine-readable handoffs.
  template_role: presentation_projection
  domain_schema_role: none
  first_success_condition: >
    J3 and J4 templates clearly separate the next-day outline from the complete
    single-flow execution workspace without duplicating content.
  implementation_policy:
    existing_skill_contracts_remain_schema_authority: true
    templates_define_presentation_not_domain_schema: true
    must_not_silently_assume_patches_are_applied: true
    must_label_overlay_fields_or_rules: true
```

## 4. Source Overlay Rule

```yaml
source_overlay_rule:
  intended_target_state_uses:
    - 20-round6-cross-cutting-consistency-resolution.okf.yaml
    - 21-canonical-artifact-family-and-lifecycle-map.okf.yaml
    - 22-round6-decision-and-verification-record.okf.yaml
    - available_round6_patch_artifacts

  overlay_map:
    02-shared-card-and-brief-anatomy.okf.yaml:
      overlay: round6-patches/01-shared-card-canonical-names.patch
    03-planning-artifact-designs.okf.yaml:
      overlay: round6-patches/02-j3-j4-depth-separation.patch
    14-status-merge-decision-card-design.okf.yaml:
      overlay: round6-patches/03-j9-durable-merge-confirmation.patch
    15-project-kb-update-card-design.okf.yaml:
      overlay: round6-patches/04-j10-durable-update-result.patch
    18-round5-cross-artifact-relationships.okf.yaml:
      overlay: round6-patches/05-j9-j10-j11-confirmed-truth-path.patch
    16-project-status-overview-design.okf.yaml:
      overlay: round6-patches/06-j11-project-status-contract-alignment.patch
    17-ai-routing-card-design.okf.yaml:
      overlay: round6-patches/07-j12-routing-contract-alignment.patch

  interpretation_policy:
    - Read only the source design required for the active batch.
    - Verify the exact overlay file required for that source design.
    - Treat the source plus verified overlay as intended presentation guidance.
    - Do not apply the overlay during template implementation.
    - Do not state that an overlay is already present in the source file.
    - Do not infer missing domain fields from presentation guidance.

  required_template_metadata:
    - source_design_ref
    - round6_overlay_ref_when_applicable
    - domain_contract_refs
    - overlay_application_status
```

## 5. First Implementation Batch

```yaml
first_batch:
  strict_scope: J3_and_J4_only
  artifact: J3_PreCap_Next_Day_Brief
  paired_artifact: J4_Flow_Execution_Card
  reason: >
    Their depth boundary was explicitly corrected in Round 6 and they provide
    the clearest small template pair for validating operator presentation,
    linking, and non-duplication.

  J3_requirement:
    role: compact_day_level_three_sprint_outline
    must_show:
      - day_goal
      - ordered_flows
      - concise_S1_S2_S3_outline_per_flow
      - flow_execution_card_refs
    must_not_show:
      - complete_tasks
      - complete_inputs
      - full_prompt_content
      - full_dependencies
      - done_conditions
      - stop_or_review_conditions

  J4_requirement:
    role: complete_single_flow_execution_workspace
    must_show:
      - complete_flow_context
      - full_three_sprint_plan
      - tasks_inputs_dependencies_outputs
      - done_conditions
      - stop_or_review_conditions
      - direct_prompt_file_links
    must_not_show:
      - duplicated_prompt_content
      - duplicated_routing_reasoning

  batch_limit:
    create_all_J1_to_J12_templates: false
    create_shared_template_system_first: false
    create_examples_in_same_iteration: false
```

## 6. Template Sequence

```yaml
template_sequence:
  first_batch:
    - J3_and_J4
  later_batches:
    - J5_and_J6
    - J7_and_J8
    - J9_and_J10
    - J11_and_J12
    - J1_and_J2
    - cross_artifact_validation
  status: guidance_only
  authorization_effect: none
  rule: >
    Completion of one batch does not authorize the next batch. Each batch must
    remain separately bounded and explicitly approved.
```

## 7. Validation Requirements

```yaml
validation_requirements:
  structure:
    - markdown_is_readable
    - yaml_blocks_parse
    - relative_links_are_valid
    - no_duplicate_top_level_fields
  operator_value:
    - result_or_current_state_is_visible_first
    - exact_next_action_is_visible
    - review_need_is_visible
    - warnings_are_visible_when_material
  authority:
    - domain_contract_refs_are_explicit
    - no_domain_schema_is_redefined
    - no_unknown_required_field_is_invented
    - overlay_status_is_explicit
  J3_J4_boundary:
    - J3_remains_a_compact_day_outline
    - J4_contains_complete_execution_depth
    - J3_links_to_J4
    - J3_does_not_repeat_J4_detail
    - J4_does_not_embed_full_prompt_files
  mutation_check:
    - source_design_files_modified: false
    - round6_patches_applied: false
    - skill_contracts_modified: false
    - runtime_modified: false
    - durable_state_modified: false
```

## 8. Explicit Non-Goals

```yaml
explicit_non_goals:
  - Do not apply any Round 6 patch.
  - Do not edit files 00 through 22.
  - Do not update the package manifest in the same iteration.
  - Do not create all J1-J12 templates at once.
  - Do not redesign accepted Step 3 architecture.
  - Do not change skill or reference contracts.
  - Do not create runtime files, scripts, agents, schedulers, or workflows.
  - Do not execute prompts or project work.
  - Do not write calendar events.
  - Do not mutate durable project state.
  - Do not create a pull request unless explicitly requested.
```

## 9. Stop Conditions

```yaml
stop_conditions:
  - The required source design cannot be fetched from main.
  - The exact required overlay cannot be verified.
  - The source and overlay conflict in a way not resolved by files 20-22.
  - A template would require inventing or redefining domain schema.
  - The owning skill contract cannot be identified or read.
  - J3 and J4 cannot be separated without modifying source designs.
  - The requested iteration expands beyond J3 and J4.
  - Applying a patch becomes necessary.
  - Any runtime, calendar, or durable-state mutation becomes necessary.
  - Explicit operator authorization for template creation is absent.
```

## 10. Next Chat Starting Instruction

```yaml
next_chat_starting_instruction: >
  After explicit operator authorization for Step 4 implementation, inspect only
  this handoff, files 22 and 21, the J3/J4 portions of
  03-planning-artifact-designs.okf.yaml, the verified
  round6-patches/02-j3-j4-depth-separation.patch overlay, and the owning domain
  contracts needed for J3 and J4. Create only the J3 PreCap Next Day Brief
  template and the J4 Flow Execution Card template. Keep J3 compact, keep full
  execution depth in J4, link J3 to J4, do not apply patches, and do not modify
  any other file or begin later batches.
```
