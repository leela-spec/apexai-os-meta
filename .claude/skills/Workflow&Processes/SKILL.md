---
name: workflow-process-design
description: >
  Use this skill when the operator asks to classify, design, normalize, validate, or repair workflow and process structure. Accepts operator tasks, flow packets, sprint goals, prompt packets, prompt results, workflow notes, and expected-output context. Produces workflow_record, workflow_stage, process_stage, expected_output_type, prompt_workflow_alignment_review, and operator_review_flags outputs. Does not generate provider-specific prompt rules, route models or quotas, execute project work, create final daily plans, override operator decisions, or create new permanent agents.
---

# Workflow Process Design

## Skill Contract

```yaml
skill_contract:
  primary_output: workflow_process_validation_summary
  output_role: workflow_and_process_fit_validator

  accepted_inputs:
    - operator_task
    - source_context
    - project_context
    - workflow_context
    - flow_packet
    - sprint_goal
    - prompt_packet
    - prompt_sequence
    - prompt_result_feedback
    - failed_prompt_output
    - expected_output_type
    - routing_decision

  primary_outputs:
    - workflow_record
    - workflow_stage
    - process_stage
    - expected_output_type
    - prompt_workflow_alignment_review
    - sprint_structure_review
    - operator_review_flags

  classification_targets:
    workflow_stage:
      canonical_home: references/workflow-stage-taxonomy.md
    process_stage:
      canonical_home: references/process-stage-taxonomy.md
    expected_output_type:
      canonical_home: references/expected-output-type-contract.md
    workflow_record:
      canonical_home: references/workflow-record-contract.md

  validation_status:
    allowed:
      - valid
      - valid_with_warnings
      - operator_review_recommended
      - low_confidence_auto_generated
      - blocked_by_missing_operator_decision

  conflict_resolution_order:
    1: operator_decision_from_tradeoff_card
    2: workflow_process_fit
    3: prompt_quality
    4: ai_routing_cost_or_efficiency

  package_interfaces:
    provides_to_prompt_engineering:
      - workflow_stage
      - process_stage
      - expected_output_type
      - success_criteria
      - iteration_logic_review
      - red_flags
    provides_to_ai_routing_and_usage_tracking:
      - task_complexity
      - workflow_value
      - risk_level
      - expected_output_type
      - high_value_route_justification
    provides_to_PreCapNextDay:
      - workflow_process_validation_summary
      - sprint_structure_review
      - prompt_workflow_alignment_review
      - operator_review_flags

  boundaries:
    must_create_or_define:
      - workflow_stage
      - process_stage
      - expected_output_type
      - workflow_record
      - alignment_review
      - operator_review_flags
    must_not_create:
      - provider_specific_prompt_rules
      - routing_decision_schema
      - quota_map
      - prompt_packet_schema
      - final_daily_plan
      - project_execution
      - FlowRecap_output
      - project_status_merge
      - new_permanent_agents
```

## Supporting Files

```yaml
supporting_files:
  - path: references/workflow-stage-taxonomy.md
    read_when:
      - classifying_workflow_stage
      - extracting_workflow_from_notes
      - resolving_workflow_stage_ambiguity

  - path: references/process-stage-taxonomy.md
    read_when:
      - classifying_process_stage
      - mapping_sprint_to_process_role
      - resolving_process_stage_ambiguity

  - path: references/expected-output-type-contract.md
    read_when:
      - defining_expected_output_type
      - validating_output_shape
      - aligning_prompt_with_operator_deliverable

  - path: references/workflow-record-contract.md
    read_when:
      - creating_workflow_record
      - normalizing_workflow_notes
      - preserving_reusable_process_structure

  - path: references/prompt-workflow-alignment-validation.md
    read_when:
      - validating_prompt_process_fit
      - checking_prompt_against_workflow_stage
      - diagnosing_failed_prompt_output

  - path: references/sprint-structure-rules.md
    read_when:
      - validating_sprint_structure
      - checking_iteration_logic
      - reviewing_flow_packet_fit

  - path: references/operator-review-and-conflict-rules.md
    read_when:
      - skill_databases_disagree
      - operator_tradeoff_decision_needed
      - confidence_is_low

  - path: examples/starter-workflow-process-example.md
    read_when:
      - operator_requests_example
      - calibrating_workflow_process_behavior
      - testing_package_behavior

  - path: package-manifest.md
    read_when:
      - inspecting_package_structure
      - validating_file_inventory
      - reviewing_package_boundaries
```

## Procedure

1. **Load workflow context.** Read the operator task, workflow notes, flow packet, sprint goal, prompt packet, expected output context, and any prompt result feedback supplied.

2. **Classify workflow and process stage.** Assign workflow_stage and process_stage using the reference taxonomies. If the task fits multiple labels, preserve the ambiguity and mark operator_review_recommended.

3. **Define expected output type.** Translate the operator's intended deliverable into an expected_output_type with success criteria, format constraints, and minimum completion evidence.

4. **Validate sprint and iteration fit.** Check whether the proposed sprint structure, sequence, iteration loop, and review points match the workflow stage, process stage, and expected output.

5. **Review prompt/process alignment.** When prompt packets exist, validate whether the prompt asks for the right job, output type, scope, review gate, and stop condition. Do not rewrite provider-specific prompt style.

6. **Create or update workflow record.** When the workflow is reusable or should be preserved, produce a compact workflow_record with labels, inputs, outputs, gates, risks, and downstream consumers.

7. **Resolve conflicts and hand off.** When prompt quality, routing efficiency, and workflow fit disagree, list tradeoffs in the canonical authority order and return operator_review_flags instead of silently choosing.

8. **Validate completion.** Confirm that all created labels, output contracts, alignment reviews, and review flags are internally consistent and ready for prompt-engineering, AI-routing, or PreCapNextDay handoff.

## Failure Modes

```yaml
failure_modes:
  missing_workflow_context:
    trigger: "No workflow notes, operator task, flow packet, or sprint goal is available."
    correction: "Return blocked_by_missing_operator_decision and list the missing minimum workflow inputs."

  unclear_workflow_stage:
    trigger: "The same task plausibly fits multiple workflow stages."
    correction: "List candidate stages, give the tradeoff, and mark operator_review_recommended."

  unclear_process_stage:
    trigger: "The task role inside the process is ambiguous or mixed."
    correction: "Assign the safest provisional process_stage and preserve ambiguity in operator_review_flags."

  missing_expected_output:
    trigger: "The operator intent names activity but not the concrete deliverable."
    correction: "Define the likely expected_output_type and mark it low_confidence_auto_generated."

  prompt_workflow_mismatch:
    trigger: "A prompt asks for work that does not match the workflow stage, process stage, or expected output."
    correction: "Return an alignment warning and request prompt-engineering revision rather than rewriting provider style."

  sprint_structure_mismatch:
    trigger: "The sprint sequence, review point, or iteration logic does not fit the intended workflow."
    correction: "Recommend a corrected sprint structure and mark operator_review_recommended when tradeoffs remain."

  package_boundary_violation:
    trigger: "The requested output requires provider prompting doctrine, model routing, daily planning, or project execution."
    correction: "Stop at the workflow/process review boundary and hand off to the owning package or operator."

  skill_database_conflict:
    trigger: "Workflow fit, prompt quality, and routing/cost recommendations disagree."
    correction: "List options in conflict_resolution_order and preserve operator choice as the deciding authority."
```

## Output Requirements

```yaml
output_requirements:
  must_include_when_relevant:
    - workflow_stage
    - process_stage
    - expected_output_type
    - workflow_record
    - sprint_structure_review
    - prompt_workflow_alignment_review
    - success_criteria
    - operator_review_flags
    - downstream_handoff_notes

  must_use:
    - canonical_validation_status_values
    - compact_tradeoff_cards_when_conflicts_exist
    - explicit_uncertainty_flags_when_classification_is_inferred
    - workflow_fit_before_prompt_quality_before_routing_efficiency

  must_not_include:
    - "Do not generate provider-specific prompt rules."
    - "Do not route models or quotas."
    - "Do not execute project work."
    - "Do not create final daily plans."
    - "Do not override operator decisions."
    - "Do not create new permanent agents."
```

## Completion Gate

```yaml
completion_gate:
  workflow_context_loaded_or_missing_inputs_flagged: true
  workflow_stage_classified_or_ambiguity_flagged: true
  process_stage_classified_or_ambiguity_flagged: true
  expected_output_type_defined_or_missing_output_flagged: true
  sprint_structure_reviewed_when_relevant: true
  prompt_workflow_alignment_reviewed_when_prompt_exists: true
  workflow_record_created_when_reusable: true
  operator_review_flags_present_when_confidence_is_limited: true
  package_boundaries_preserved: true
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Description starts with "Use this skill when".
- [ ] Procedure includes classification, expected-output definition, sprint validation, prompt/workflow alignment, and conflict handoff.
- [ ] Skill does not generate provider-specific prompt rules, route models or quotas, execute project work, or override operator decision.
- [ ] Supporting files use YAML path plus read_when conditions.
- [ ] Completion Gate is a YAML boolean checklist.

---

# NEXT PROMPT

Paste this next:
> Prompt WPD2:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/references/workflow-stage-taxonomy.md
>
> File type: reference_taxonomy.
> Schema ownership: owns workflow_stage taxonomy.
> Context carry-forward:
> - .claude/skills/workflow-process-design/SKILL.md
>
> Structure constraints:
> - YAML-first taxonomy file.
> - Define workflow_stage exactly once.
> - Include selection rules, ambiguity handling, and minimal examples.
> - Do not duplicate process_stage taxonomy or expected_output_type contract.
>
> Content constraints:
> - Include stages for intake, exploration, extraction, normalization, planning, execution_support, validation, synthesis, recap_preparation, learning_update, and operator_decision.
> - Include use_when, avoid_when, required_inputs, likely_outputs, and review_flags for each stage.
> - Keep workflow stage separate from process stage and prompt task type.
>
> File-specific checks:
> - [ ] workflow_stage taxonomy is defined once.
> - [ ] process_stage and expected_output_type are referenced but not redefined.
> - [ ] Ambiguity handling and examples are included.
