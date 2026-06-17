# FILE: .claude/skills/workflow-process-design/examples/starter-workflow-process-example.md

# Starter Workflow Process Example

## Example Metadata

```yaml
example_metadata:
  artifact_name: starter_workflow_process_example
  file_role: workflow_process_design_example
  schema_ownership: none
  purpose: >
    Show one compact, realistic example of extracting a workflow from rough
    project/process material, assigning workflow and process labels, defining
    the expected output, checking prompt-process alignment, resolving an
    operator-level conflict, and capturing a learning signal from a failed
    prompt output. This file illustrates existing contracts only and does not
    define new schemas.
  package_context: workflow-process-design
  example_scope: single_flow_single_sprint
  related_flow: F3
  related_project: Apex
  example_status: illustrative_only

boundaries:
  does_not_define:
    - workflow_stage_taxonomy
    - process_stage_taxonomy
    - expected_output_type_schema
    - workflow_record_schema
    - prompt_packet_schema
    - routing_decision_schema
    - daily_plan_schema
  does_not_perform:
    - provider_specific_prompt_generation
    - model_or_quota_routing
    - project_execution
    - status_merge
    - FlowRecap
```

## Rough Source Material

The following rough material is the only input used by the example. It is intentionally incomplete and slightly conflicted.

```yaml
rough_source_material:
  source_type: operator_notes
  source_status: messy_but_usable
  note: >
    For Apex F3 I need to turn the current prompt-flow decisions into a stable
    workflow/process design database. The immediate thing is probably a file
    that defines how to classify stages and expected outputs, but I also want
    the prompt pack later to use these labels. The last prompt I tried asked
    for a full daily plan and also a workflow record, and the output mixed
    planning, prompt writing, and validation too much. We need a cleaner
    reusable process object first.
  implied_goal: Create reusable workflow/process structure before generating more prompts.
  known_conflict: >
    The operator wants both immediate prompt usefulness and durable workflow
    database quality, but the rough source names multiple possible outputs.
```

## Extracted Workflow

```yaml
extracted_workflow:
  workflow_label: apex_workflow_process_database_buildout
  workflow_summary: >
    Convert rough process-design notes into reusable workflow/process labels,
    expected-output definitions, alignment checks, and conflict-resolution
    rules that other skills can consume.
  primary_operator_intent: reusable_database_quality
  secondary_operator_intent: future_prompt_pack_support
  current_work_unit:
    flow_id: F3
    sprint_id: S1
    sprint_goal: Define one reusable workflow/process artifact before prompt generation.
  reusable: true
  validation_status: valid_with_warnings
  operator_review_flags:
    - immediate_prompt_pack_usefulness_is_secondary_to_database_quality
    - downstream_prompt_generation_should_wait_for_stage_and_output_labels
```

## Labels Applied

```yaml
labels_applied:
  workflow_stage:
    selected: extraction
    rationale: >
      The source material contains messy process notes and implicit workflow
      structure that must be extracted before it can be normalized or used for
      prompt generation.
    alternatives_considered:
      - normalization
      - planning
      - validation
    review_flags:
      - normalization_is_next_stage_after_extraction

  process_stage:
    selected: structure_definition
    rationale: >
      The task is not executing project work. It is defining a reusable
      process structure that can later guide prompt packs and validation.
    alternatives_considered:
      - output_validation
      - prompt_preparation
    review_flags:
      - prompt_preparation_depends_on_this_structure

  expected_output_type:
    selected: workflow_record
    rationale: >
      A workflow_record preserves reusable process structure better than a
      prompt pack or a validation report for this source state.
    format_constraints:
      - compact_markdown_with_yaml_blocks
      - one_primary_workflow_object
      - labels_must_reference_taxonomies
      - no_provider_specific_prompt_rules
    minimum_completion_evidence:
      - workflow_summary_present
      - workflow_stage_present
      - process_stage_present
      - expected_output_type_present
      - inputs_outputs_gates_and_risks_present
      - operator_review_flags_present
    validation_status: valid_with_warnings
```

## Workflow Record Example

This is an example instance of a workflow record. It follows the existing workflow-record contract; it does not redefine that contract.

```yaml
workflow_record_example:
  workflow_record_id: workflow_record_apex_process_database_buildout_example
  workflow_name: apex_process_database_buildout
  workflow_status: draft_ready_for_operator_review
  workflow_stage: extraction
  process_stage: structure_definition
  expected_output_type: workflow_record
  source_context_summary: >
    Operator notes indicate a need to convert rough prompt-flow and process
    decisions into a reusable workflow/process design database before creating
    more prompt packs.
  inputs:
    - rough_operator_notes
    - current_package_sequence
    - prior_failed_prompt_output_summary
  outputs:
    - workflow_record
    - workflow_stage_label
    - process_stage_label
    - expected_output_type
    - prompt_process_alignment_review
    - operator_review_flags
  operator_gates:
    - confirm_primary_artifact_type_before_prompt_generation
    - approve_conflict_resolution_when_database_quality_and_daily_use_disagree
  downstream_consumers:
    - prompt-engineering
    - ai-routing-and-usage-tracking
    - precap-next-day
  risks:
    - prompt_generation_may_start_before_workflow_labels_are_stable
    - expected_output_type_may_be_confused_with_prompt_task_type
    - operator_may_need_daily_execution_output_before_database_quality_is_ready
  validation_status: valid_with_warnings
  operator_review_flags:
    - verify_that_workflow_record_is_the_desired_primary_output
    - preserve_prompt_pack_as_downstream_output_not_current_output
```

## Prompt-Process Alignment Check

```yaml
prompt_process_alignment_check:
  source_prompt_summary: >
    Previous prompt asked for a full daily plan, a workflow record, and prompt
    generation in one pass.
  alignment_status: invalid
  mismatch_type:
    - mixed_expected_outputs
    - workflow_stage_mismatch
    - process_stage_mismatch
    - premature_prompt_generation
  expected_process_fit:
    workflow_stage: extraction
    process_stage: structure_definition
    expected_output_type: workflow_record
  actual_prompt_behavior:
    workflow_stage: planning
    process_stage: prompt_preparation
    expected_output_type: mixed_daily_plan_and_workflow_record
  correction_required: >
    Ask for one workflow_record first. Defer prompt pack generation until the
    workflow_stage, process_stage, and expected_output_type labels are stable.
  validation_status: operator_review_recommended
  operator_review_flags:
    - previous_prompt_should_be_rewritten_by_prompt_engineering_after_labels_are_confirmed
    - daily_plan_generation_is_out_of_scope_for_workflow_process_design
```

## Operator Conflict Resolution Example

```yaml
operator_conflict_resolution_example:
  conflict_id: conflict_database_quality_vs_immediate_prompt_use
  conflict_type: workflow_process_fit_vs_daily_execution_speed
  conflict_summary: >
    The operator wants a useful prompt pack soon, but the current source state
    first needs a stable workflow/process object to prevent repeated prompt
    drift.
  authority_order:
    1: operator_decision_from_tradeoff_card
    2: workflow_process_fit
    3: prompt_quality
    4: ai_routing_cost_or_efficiency
  tradeoff_card:
    decision_needed: Choose the next artifact before prompt generation.
    options:
      - option_id: option_A
        label: Create workflow_record first.
        use_when: Reusable process/database quality matters most.
        benefits:
          - Stabilizes labels before prompt generation.
          - Prevents prompt packs from absorbing workflow doctrine.
          - Creates reusable input for PreCapNextDay.
        costs:
          - Delays immediate copy-paste prompt use.
        downstream_effect: Prompt-engineering can generate cleaner prompts later.
      - option_id: option_B
        label: Generate prompt pack now with provisional labels.
        use_when: Immediate execution matters more than database stability.
        benefits:
          - Faster daily use.
          - Produces immediate operator-facing prompt material.
        costs:
          - Higher risk of workflow/prompt boundary drift.
          - Labels may need later correction.
        downstream_effect: Workflow-process-design should later validate and repair the prompt pack.
      - option_id: option_C
        label: Produce validation report only.
        use_when: The operator only needs defect detection.
        benefits:
          - Fastest quality gate.
          - Avoids creating premature final artifacts.
        costs:
          - Does not create reusable workflow structure.
          - Does not create executable prompts.
        downstream_effect: Requires a second generation step.
    recommendation:
      recommended_option_id: option_A
      rationale: >
        The current source material is structurally unstable. A workflow_record
        is the safest primary artifact because it can feed later prompt packs
        and validation checks without merging responsibilities.
      confidence: medium
    operator_override_allowed: true
  validation_status: operator_review_recommended
```

## Learning Signal From Failed Prompt Output

```yaml
failed_prompt_learning_signal:
  source_status: summarized_not_quoted
  failure_observed: >
    A previous prompt produced a mixed artifact that tried to be a daily plan,
    workflow record, prompt pack, and validation report at the same time.
  likely_root_causes:
    - expected_output_type_not_fixed_before_generation
    - workflow_stage_and_process_stage_not_explicit
    - prompt_generation_started_before_process_structure_was_stable
    - package_boundaries_not_reinforced
  reusable_learning:
    rule: >
      When source material names multiple deliverables, workflow-process-design
      must force an expected_output_type decision before prompt-engineering
      generates copy-paste prompts.
    apply_when:
      - rough_notes_include_multiple_artifact_types
      - prompt_requests_workflow_and_prompt_generation_in_one_pass
      - daily_execution_pressure_conflicts_with_database_quality
    correction_pattern: >
      First create or validate the workflow_record. Then hand off the stable
      labels and expected_output_type to prompt-engineering.
  downstream_hint_for_prompt_engineering: >
    Future prompt should request exactly one artifact and include workflow_stage,
    process_stage, expected_output_type, validation criteria, and stop condition.
  validation_status: valid
```

## Compact Human-Readable Result

```text
Recommended current artifact: workflow_record.
Reason: source material is still structurally mixed; prompt generation would likely absorb workflow doctrine.
Workflow stage: extraction.
Process stage: structure_definition.
Expected output type: workflow_record.
Next handoff: after operator approval, send stable labels to prompt-engineering for one prompt pack or prompt packet.
Main review flag: operator must confirm whether reusable database quality beats immediate prompt generation for this step.
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Example does not define a new schema.
- [ ] Example includes one workflow extracted from rough source material.
- [ ] Example includes workflow_stage labels.
- [ ] Example includes process_stage labels.
- [ ] Example includes expected_output_type.
- [ ] Example includes prompt-process alignment check.
- [ ] Example includes operator conflict resolution.
- [ ] Example includes learning from failed prompt output.
- [ ] Example remains compact and realistic.

---

# NEXT PROMPT

Paste this next:
> Prompt WP11:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/package-manifest.md
>
> File type: package_manifest.
> Schema ownership: owns no schema.
> Context carry-forward:
> - all workflow-process-design package files
>
> Structure constraints:
> - Lightweight manifest index only.
> - Maximum 60 lines before validation and next prompt sections.
> - Each file entry must include only path, purpose, and read_when.
> - Do not duplicate schemas, taxonomies, examples, validation rules, or package contracts.
>
> Content constraints:
> - List every workflow-process-design package file in order.
> - Include package-level boundaries.
> - Include package acceptance checks.
>
> File-specific checks:
> - [ ] Manifest is an index only.
> - [ ] Manifest contains all workflow-process-design files.
> - [ ] No schemas are duplicated.
> - [ ] Manifest stays under 60 lines before validation and next prompt sections.
