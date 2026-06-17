# Starter Prompt Pack Example

```yaml
starter_prompt_pack_example:
  artifact_name: starter_prompt_pack_example
  file_role: prompt_engineering_example
  purpose: >
    Provide a compact, realistic example of a prompt pack using the
    prompt-engineering package contracts. This file demonstrates shape,
    granularity, metadata placement, validation, and learning-hint usage. It is
    not a schema owner, not a provider-style contract, not a routing authority,
    and not a workflow taxonomy.

  ownership:
    owns:
      - starter_prompt_pack_example
      - example_usage_notes
    must_not_own:
      - prompt_packet_schema
      - prompt_sequence_schema
      - provider_specific_style_rules
      - routing_decision_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - daily_plan_schema
      - FlowRecap_output
      - project_status_merge

  example_policy:
    illustrative_only: true
    may_be_used_for_manual_test: true
    may_be_used_for_shape_calibration: true
    must_not_be_treated_as_required_content: true
    metadata_outside_prompt_body: true
    copy_paste_prompt_body_is_clean: true
    one_primary_prompt_system_only: true
    fallback_notes_allowed: true
    mandatory_machine_readable_capture_block_inside_prompt_body: false
```

## Example Use Case

```yaml
example_use_case:
  operator_task: "Create one contract reference file for a Claude skill package."
  source_context_shape: "prior_SKILL_md_output_plus_file_prompt"
  prompt_task_type: file_generation
  expected_output_type: markdown_document
  selected_iteration_loop: generate_critique_revise
  provider_target: Claude
  provider_fit_note: "Structured file generation with strict boundaries and validation."
  workflow_stage: package_file_generation
  process_stage: file_authoring
  downstream_use: "Operator copies the generated file into the skill package."
```

## Starter Prompt Pack

```yaml
starter_prompt_pack:
  pack_id: starter_prompt_pack_skill_reference_file
  pack_role: single_file_generation_prompt_pack
  validation_status: valid

  prompt_packet:
    packet_id: prompt_packet_skill_reference_file
    packet_role: standalone_prompt_packet
    prompt_task_type: file_generation
    workflow_stage: package_file_generation
    process_stage: file_authoring
    expected_output_type: markdown_document

    expected_output_contract:
      expected_output_type: markdown_document
      output_shape: "One complete Markdown reference file with YAML-first contract sections and minimal examples."
      success_criteria:
        - "Creates exactly one target file content."
        - "Defines no schemas owned by other files."
        - "Uses valid 2-space-indented YAML blocks."
        - "Includes a compact usage example."
        - "Avoids provider-specific style rules unless the file owns them."
      forbidden_outputs:
        - daily_plan
        - project_execution
        - FlowRecap_output
        - project_status_merge
        - final_OpenRouter_model_map
      validation_method: compare_against_contract

    provider_target: Claude
    provider_rationale:
      provider_target: Claude
      rationale: "Claude is a good fit for strict Markdown file generation, schema-bound writing, and contract validation."
      confidence: medium
      fallback_surface: provider_unspecified

    prompt_design_rationale:
      rationale: "The prompt constrains generation to one file, separates metadata from the copy-paste body, and includes explicit validation rules."
      design_basis:
        - task_type
        - expected_output_type
        - validation_need
        - operator_constraint

    usage_tracking_tags:
      surface_class: subscription_frontier
      reasoning_class: high
      task_value_class: high_value
      usage_capture_needed: true
      quota_note: "Use a strong reasoning surface when the file is contract-critical."

    light_capture_hints:
      hints:
        - "After use, note whether the generated file duplicated another contract schema."
        - "Record whether the final validation checklist caught all structural defects."
      canonical_capture_location: prompt_result_feedback
      rule: prompt_body_may_include_light_capture_hint_only

    prompt_failure_hints:
      hints:
        - "May duplicate schema from another reference file if ownership is not repeated clearly."
        - "May produce multiple files unless the exact one-file boundary is explicit."
        - "May place metadata inside the copy-paste prompt body if not separated."
      common_failure_classes:
        - wrong_output_shape
        - workflow_mismatch
        - excessive_alternatives
        - insufficient_validation

    prompt_learning_hints:
      hints:
        - "Capture whether one-file generation remained stable."
        - "Capture whether YAML remained parseable."
        - "Capture whether the provider choice improved output reliability."
      feedback_capture_focus:
        - output_quality
        - validation_failures
        - provider_fit
        - reusable_pattern_candidate

    final_copy_paste_prompt:
      prompt_body: |
        You are a Claude-native skill-package file author.

        Task:
        Create exactly one complete Markdown reference file for the target path below.

        Target file:
        <PASTE TARGET FILE PATH>

        Context:
        <PASTE PRIOR PACKAGE CONTEXT>

        File contract:
        <PASTE FILE-SPECIFIC CONTRACT>

        Boundaries:
        - Create only this file content.
        - Do not create additional files.
        - Do not define schemas owned by other reference files.
        - Do not include source-document names, derivation notes, or citations.
        - Do not create daily plans, project execution output, FlowRecap output, status merges, or final OpenRouter model mappings.

        Format requirements:
        - Use Markdown.
        - Put machine-readable content in valid YAML blocks with 2-space indentation.
        - Keep examples minimal and realistic.
        - Use canonical key names supplied in the context.
        - Keep metadata outside any copy-paste prompt body.

        Output exactly:
        # FILE: <target path>

        <complete final file content>

        ---

        # VALIDATION — FILE-SPECIFIC CHECKS

        - [ ] Exactly one target file was produced.
        - [ ] YAML blocks are parseable and use 2-space indentation.
        - [ ] No externally owned schema is redefined.
        - [ ] All file-specific requirements are satisfied.

        ---

        # NEXT PROMPT

        Paste this next:
        > <next prompt text>

        Stop after the NEXT PROMPT section.
      prompt_body_rules:
        role_is_clear: true
        task_is_clear: true
        context_is_sufficient: true
        output_contract_is_explicit: true
        constraints_are_explicit: true
        validation_criteria_are_explicit: true
        stop_condition_is_present: true
      copy_boundary: copy_prompt_body_only

  prompt_quality_review:
    validation_status: valid
    scores:
      task_clarity:
        value: 5
        scale_min: 1
        scale_max: 5
      context_fit:
        value: 4
        scale_min: 1
        scale_max: 5
      output_contract_strength:
        value: 5
        scale_min: 1
        scale_max: 5
      workflow_alignment:
        value: 4
        scale_min: 1
        scale_max: 5
      routing_fit:
        value: 4
        scale_min: 1
        scale_max: 5
    review_notes:
      - "The prompt is strong for one-file contract generation."
      - "Provider choice should be rechecked if the actual task requires current external verification."
      - "The example intentionally avoids mandatory machine-readable capture blocks inside the prompt body."
    operator_review_flags: []
```

## Optional Follow-Up Prompt Example

```yaml
optional_follow_up_prompt_example:
  prompt_id: follow_up_prompt_validate_generated_file
  follow_up_role: validate
  trigger_condition: "Use after the first file draft exists and before operator copies it into the package."
  expected_delta: "Return only defects and exact fixes; do not rewrite the file unless required."

  final_copy_paste_prompt:
    prompt_body: |
      You are validating one generated Claude skill-package file.

      Task:
      Review the supplied file against its stated contract and return only:
      1. pass/fail summary
      2. critical defects
      3. exact surgical fixes
      4. final completion check

      Validation criteria:
      - YAML blocks are parseable.
      - The file creates no extra artifacts.
      - Schema ownership is respected.
      - Provider-specific, routing, workflow, and planning rules are not defined outside their owner files.
      - The output is final, not a draft.

      Constraints:
      Do not rewrite the entire file unless a defect makes it unusable.
      Do not add new package scope.

      Stop after the completion check.
    prompt_body_rules:
      role_is_clear: true
      task_is_clear: true
      context_is_sufficient: true
      output_contract_is_explicit: true
      constraints_are_explicit: true
      validation_criteria_are_explicit: true
      stop_condition_is_present: true
    copy_boundary: copy_prompt_body_only
```

## Example Validation Result

```yaml
example_validation_result:
  validation_status: valid
  checks:
    exactly_one_primary_prompt_present: true
    metadata_outside_prompt_body: true
    prompt_body_copy_paste_clean: true
    no_mandatory_machine_capture_block: true
    provider_rationale_present: true
    prompt_design_rationale_present: true
    prompt_failure_hints_present: true
    prompt_learning_hints_present: true
    expected_output_contract_present: true
    usage_tracking_tags_present: true
    operator_review_flags_present_or_empty: true

  learning_candidate:
    reusable_pattern_candidate: true
    pattern_name: one_file_generation_prompt_with_validation_tail
    capture_reason: "Useful for repeatable skill-package file generation with strict one-file boundaries."
```

## Manual Test Instructions

```yaml
manual_test_instructions:
  test_goal: "Verify that the prompt-engineering package can produce one complete, bounded file prompt pack."
  steps:
    - "Copy the starter prompt body into the intended provider."
    - "Replace target path, prior package context, and file-specific contract placeholders."
    - "Run the prompt once."
    - "Check whether exactly one file was produced."
    - "Run the optional validation follow-up if defects are likely."
    - "Record failures in prompt_result_feedback."

  expected_pass_conditions:
    exactly_one_file_output: true
    no_schema_duplication: true
    clean_copy_paste_prompt_body: true
    validation_tail_present: true
    next_prompt_present: true

  common_failures_to_record:
    - extra_file_created
    - schema_redefined
    - YAML_invalid
    - provider_style_leaked_into_generic_contract
    - prompt_body_contains_metadata
    - missing_next_prompt
```
