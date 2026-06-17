# FILE: .claude/skills/workflow-process-design/references/operator-validation-and-conflict-resolution.md

# Operator Validation and Conflict Resolution

```yaml
operator_validation_and_conflict_resolution:
  artifact_name: operator_validation_and_conflict_resolution
  file_role: workflow_process_design_reference_rules
  purpose: >
    Define how workflow-process-design surfaces conflicts, prepares operator
    tradeoff cards, records validation status, and preserves the operator as
    final decider when skill databases disagree.

  ownership:
    owns:
      - operator_validation_rules
      - conflict_resolution_rules
      - tradeoff_card_behavior
      - operator_review_flag_rules
      - conflict_examples
    must_not_own:
      - workflow_stage_taxonomy
      - process_stage_taxonomy
      - expected_output_type_schema
      - sprint_structure_schema
      - workflow_record_schema
      - prompt_packet_schema
      - prompt_quality_validation_schema
      - routing_decision_schema
      - planned_usage_budget_schema
      - daily_plan_schema
      - calendar_event_schema

  core_policy:
    operator_is_final_decider: true
    skill_may_recommend: true
    skill_may_not_override_operator_choice: true
    skill_must_surface_material_conflicts: true
    skill_must_list_options_when_databases_disagree: true
    skill_must_explain_tradeoffs: true
    skill_must_mark_uncertainty: true
```

## Canonical Validation Status

```yaml
validation_status_policy:
  allowed:
    - valid
    - valid_with_warnings
    - operator_review_recommended
    - low_confidence_auto_generated
    - blocked_by_missing_operator_decision

  use_when:
    valid:
      meaning: "No material conflict is detected and all required labels or fields are present."
      operator_action: "Optional review only."

    valid_with_warnings:
      meaning: "The output is usable, but one or more non-blocking risks should be visible."
      operator_action: "Review warning notes when stakes are high."

    operator_review_recommended:
      meaning: "The skill can produce a recommendation, but a human tradeoff decision would materially improve correctness."
      operator_action: "Choose, edit, or approve one option."

    low_confidence_auto_generated:
      meaning: "The output was generated from thin, ambiguous, or partially missing context."
      operator_action: "Treat as provisional and correct before downstream use."

    blocked_by_missing_operator_decision:
      meaning: "The conflict cannot be resolved without choosing a priority, boundary, or tradeoff."
      operator_action: "Make an explicit decision before the package proceeds."
```

## Conflict Types

```yaml
conflict_types:
  prompt_quality_vs_workflow_fit:
    trigger: "A prompt is well-formed but does not match the workflow_stage, process_stage, sprint goal, or expected_output_type."
    default_resolution: "Favor workflow_process_fit over prompt_quality and request prompt revision."
    review_status: operator_review_recommended

  workflow_fit_vs_project_priority:
    trigger: "The best process sequence conflicts with the operator's stated project priority or deadline pressure."
    default_resolution: "List process-safe and priority-fast options without silently choosing."
    review_status: operator_review_recommended

  project_priority_vs_usage_efficiency:
    trigger: "A high-priority task would benefit from scarce or expensive AI usage, while routing efficiency suggests saving quota."
    default_resolution: "Show value, scarcity, fallback, and recommendation; operator decides."
    review_status: operator_review_recommended

  prompt_quality_vs_usage_efficiency:
    trigger: "The best prompt/provider route is higher-cost or scarcer than a sufficient lower-cost route."
    default_resolution: "Recommend based on impact, risk, evidence_need, and ambiguity, not cost alone."
    review_status: valid_with_warnings

  taxonomy_disagreement:
    trigger: "workflow_stage, process_stage, or expected_output_type classifications conflict across sources or prior outputs."
    default_resolution: "List candidate labels, evidence, and downstream effects."
    review_status: operator_review_recommended

  missing_required_operator_preference:
    trigger: "The next action depends on a preference such as speed versus quality, breadth versus depth, or finality versus exploration."
    default_resolution: "Block only when the preference changes the artifact meaning or downstream action."
    review_status: blocked_by_missing_operator_decision
```

## Authority Order

```yaml
conflict_authority_order:
  1_operator_tradeoff_decision:
    authority: final
    rule: "Use the operator's explicit decision when it is present and does not violate package boundaries."

  2_workflow_process_fit:
    authority: validation_veto
    rule: "A prompt or route that does not fit the workflow, process stage, sprint logic, or expected output must be flagged."

  3_prompt_quality:
    authority: quality_signal
    rule: "Prompt quality affects recommendation strength but does not override workflow mismatch or operator choice."

  4_ai_routing_cost_or_efficiency:
    authority: advisory_signal
    rule: "Routing and usage efficiency may influence the recommendation but must not silently override quality or fit."
```

## Tradeoff Card Schema

```yaml
operator_tradeoff_card:
  type: object
  required:
    - conflict_id
    - conflict_type
    - decision_needed
    - options
    - recommendation
    - validation_status
  fields:
    conflict_id:
      type: string
      format: "conflict_<short_slug>"
      required: true

    conflict_type:
      type: string
      allowed:
        - prompt_quality_vs_workflow_fit
        - workflow_fit_vs_project_priority
        - project_priority_vs_usage_efficiency
        - prompt_quality_vs_usage_efficiency
        - taxonomy_disagreement
        - missing_required_operator_preference
      required: true

    decision_needed:
      type: string
      required: true

    context_summary:
      type: string
      required: false

    options:
      type: list
      min_items: 2
      max_items: 5
      item_ref: tradeoff_option
      required: true

    recommendation:
      type: object_ref
      ref: tradeoff_recommendation
      required: true

    operator_override_allowed:
      type: boolean
      required: true
      default: true

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence_auto_generated
        - blocked_by_missing_operator_decision
      required: true

    operator_review_flags:
      type: list
      item_type: string
      required: false
```

```yaml
tradeoff_option:
  type: object
  required:
    - option_id
    - label
    - use_when
    - benefits
    - costs
    - downstream_effect
  fields:
    option_id:
      type: string
      format: "option_<letter_or_short_slug>"
      required: true
    label:
      type: string
      required: true
    use_when:
      type: string
      required: true
    benefits:
      type: list
      item_type: string
      min_items: 1
      max_items: 5
      required: true
    costs:
      type: list
      item_type: string
      min_items: 1
      max_items: 5
      required: true
    downstream_effect:
      type: string
      required: true
    review_flags:
      type: list
      item_type: string
      required: false

tradeoff_recommendation:
  type: object
  required:
    - recommended_option_id
    - rationale
    - confidence
  fields:
    recommended_option_id:
      type: string
      required: true
    rationale:
      type: string
      required: true
    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
      required: true
    fallback_if_operator_disagrees:
      type: string
      required: false
```

## Operator Review Flag Rules

```yaml
operator_review_flag_rules:
  flags:
    workflow_label_uncertain:
      use_when: "Multiple workflow_stage labels are plausible."
      correction: "List candidate labels and preferred label."

    process_stage_uncertain:
      use_when: "The process stage depends on missing project context or operator intent."
      correction: "Use provisional label and mark operator_review_recommended."

    expected_output_type_uncertain:
      use_when: "The requested artifact shape is ambiguous or conflicts with the workflow stage."
      correction: "List likely output types and downstream impact."

    prompt_workflow_mismatch:
      use_when: "Prompt structure does not support the classified workflow/process stage."
      correction: "Recommend prompt revision instead of silently accepting the prompt."

    project_priority_conflict:
      use_when: "Operator priority conflicts with process-safe sequencing."
      correction: "Create a tradeoff card."

    usage_efficiency_conflict:
      use_when: "Routing efficiency conflicts with project value, risk, or evidence need."
      correction: "Expose scarcity and value tradeoff."

    missing_operator_decision:
      use_when: "No safe default exists because options produce different downstream artifacts."
      correction: "Set validation_status to blocked_by_missing_operator_decision."
```

## Procedure Rules

```yaml
operator_validation_procedure_rules:
  detect:
    rule: "Check workflow fit, prompt quality, project priority, and usage efficiency for material disagreement."

  classify:
    rule: "Assign exactly one primary conflict_type and optional secondary review flags."

  prepare_options:
    rule: "Create 2-5 options with benefits, costs, and downstream effect."

  recommend:
    rule: "Recommend one option when evidence supports it, but keep operator_override_allowed true."

  block_only_when_needed:
    rule: "Use blocked_by_missing_operator_decision only when a missing decision changes output meaning or downstream action."

  record:
    rule: "Carry selected option, rationale, validation_status, and review flags into workflow_record or downstream validation summary when relevant."

  never_override:
    rule: "Do not replace a clear operator decision with the skill's preferred option."
```

## Examples

### Example 1 — Prompt quality conflicts with workflow fit

```yaml
example_prompt_quality_vs_workflow_fit:
  input_signal:
    workflow_stage: extraction
    process_stage: planning
    expected_output_type: workflow_record
    prompt_quality_signal: "Prompt asks for polished final strategy narrative."
  conflict:
    conflict_type: prompt_quality_vs_workflow_fit
    reason: "The prompt is clear but asks for finalization before extraction and normalization are complete."
  tradeoff_card:
    conflict_id: conflict_prompt_finalizes_too_early
    decision_needed: "Choose whether to extract workflow structure first or keep the final narrative prompt."
    options:
      - option_id: option_A
        label: "Extract and normalize first"
        use_when: "Workflow structure is not yet stable."
        benefits:
          - "Protects process correctness."
          - "Produces reusable workflow_record."
        costs:
          - "Slower than direct narrative generation."
        downstream_effect: "Prompt is rewritten to produce workflow_record before final narrative."
      - option_id: option_B
        label: "Use final narrative prompt now"
        use_when: "Operator needs presentation output immediately."
        benefits:
          - "Fast visible output."
        costs:
          - "Higher drift risk."
          - "Weak reusable process capture."
        downstream_effect: "Mark workflow_record as incomplete or deferred."
    recommendation:
      recommended_option_id: option_A
      rationale: "Workflow fit has higher authority than prompt polish when the workflow is not yet extracted."
      confidence: high
    operator_override_allowed: true
    validation_status: operator_review_recommended
```

### Example 2 — Priority conflicts with usage efficiency

```yaml
example_project_priority_vs_usage_efficiency:
  input_signal:
    project_priority: "Apex orchestration package must be finished today."
    usage_signal: "Scarce deep research mode is underused but not necessary for local contract writing."
    workflow_signal: "File generation from current contracts, low external evidence need."
  conflict:
    conflict_type: project_priority_vs_usage_efficiency
    reason: "Scarce mode could be spent, but current workflow does not need deep research."
  options:
    - option_id: option_A
      label: "Use regular frontier reasoning"
      use_when: "Current project sources are sufficient."
      benefits:
        - "Fast and adequate."
        - "Saves scarce research mode."
      costs:
        - "Less external verification."
      downstream_effect: "Proceed with contract generation and local validation."
    - option_id: option_B
      label: "Use scarce research mode"
      use_when: "Operator wants external current verification before finalizing."
      benefits:
        - "Better external grounding."
      costs:
        - "Consumes scarce mode on a task with low evidence_need."
      downstream_effect: "Delay file generation until research synthesis exists."
  recommendation:
    recommended_option_id: option_A
    rationale: "High project priority does not automatically justify scarce research when evidence_need is low."
    confidence: medium
  validation_status: valid_with_warnings
```

### Example 3 — Missing operator decision blocks output

```yaml
example_missing_operator_decision:
  input_signal:
    operator_task: "Turn these notes into the right workflow artifact."
    source_context: "Notes mix strategy, execution checklist, and recap observations."
    known_conflict: "Output could become workflow_record, validation_report, or prompt_pack."
  conflict:
    conflict_type: missing_required_operator_preference
    reason: "The intended downstream use is unknown and changes the artifact contract."
  tradeoff_card:
    conflict_id: conflict_output_contract_unknown
    decision_needed: "Choose the primary artifact type before generation."
    options:
      - option_id: option_A
        label: "workflow_record"
        use_when: "Goal is reusable process capture."
        benefits:
          - "Best for database quality."
        costs:
          - "Not directly executable as a prompt."
        downstream_effect: "Create normalized workflow documentation."
      - option_id: option_B
        label: "prompt_pack"
        use_when: "Goal is immediate AI execution."
        benefits:
          - "Fast operational use."
        costs:
          - "May skip durable workflow normalization."
        downstream_effect: "Send to prompt-engineering for prompt package creation."
      - option_id: option_C
        label: "validation_report"
        use_when: "Goal is checking existing process quality."
        benefits:
          - "Best for defect detection."
        costs:
          - "Does not create final operating artifact."
        downstream_effect: "Generate findings and correction list."
    recommendation:
      recommended_option_id: option_A
      rationale: "Mixed notes usually need normalization before prompt or validation output."
      confidence: low
    operator_override_allowed: true
    validation_status: blocked_by_missing_operator_decision
```

---

# VALIDATION - FILE-SPECIFIC CHECKS

- [ ] Operator is final decider when skill databases disagree.
- [ ] Tradeoff card behavior is specified with options, tradeoffs, and recommendation.
- [ ] validation_status uses canonical values.
- [ ] Conflicts between prompt quality, workflow fit, project priority, and usage efficiency are surfaced.
- [ ] No hard override of operator choice is allowed.
- [ ] The file does not create a new operator-gate system outside current decisions.

---

# NEXT PROMPT

Paste this next:
> Prompt WP10:
> Create exactly one file.
>
> # FILE: .claude/skills/workflow-process-design/examples/starter-workflow-process-example.md
>
> File type: example.
> Schema ownership: owns no schema.
> Context carry-forward:
> - all previously generated workflow-process-design files
>
> Structure constraints:
> - Example file only.
> - Use current decisions only.
> - Do not define new schemas.
>
> Content constraints:
> - Show one workflow extracted from rough project/process material.
> - Include workflow_stage labels, process_stage labels, expected_output_type, prompt-process alignment check, operator conflict resolution, and learning signal from failed prompt output.
> - Keep example compact and realistic.
>
> File-specific checks:
> - [ ] Example does not define a new schema.
> - [ ] Example includes conflict resolution.
> - [ ] Example includes learning from failed prompt output.
