# FILE: .claude/skills/prompt-engineering/references/provider-style-contract-claude.md

```markdown id="t2r9cx"
# Provider Style Contract — Claude

```yaml
provider_style_contract_claude:
  artifact_name: provider_style_contract_claude
  file_role: provider_specific_prompt_adaptation_contract
  purpose: >
    Define Claude-specific prompt adaptation rules for Claude Code file
    generation, extended-thinking work, and long structured document tasks.
    This file uses stable surface classes only and does not claim current
    pricing, exact model rankings, exact product limits, routing-decision
    schema, or prompt_packet schema.

  ownership:
    owns:
      - Claude_prompt_style_rules
      - Claude_fit_conditions
      - Claude_Code_file_generation_prompt_patterns
      - Claude_extended_thinking_prompt_patterns
      - Claude_long_structured_document_prompt_patterns
      - Claude_output_contract_preferences
      - Claude_failure_modes
      - Claude_minimal_examples
    must_not_own:
      - routing_decision_schema
      - monthly_quota_schema
      - exact_model_rankings
      - exact_pricing
      - exact_product_limits
      - prompt_packet_schema
      - workflow_stage_taxonomy
      - process_stage_taxonomy

  volatility_policy:
    stable_claims_allowed:
      - abstract_surface_classes
      - general_prompting_style_preferences
      - Claude_Code_file_generation_fit
      - extended_thinking_task_fit
      - long_structured_document_fit
    volatile_claims_forbidden_without_current_verification:
      - exact_model_rankings
      - exact_product_limits
      - current_pricing
      - current_availability
      - benchmark_claims
```

## Claude Prompt Style Rules

```yaml id="kk3uv9"
Claude_prompt_style_rules:
  general_style:
    preferred:
      - explicit_scope_and_boundaries
      - exact_file_or_artifact_target
      - strong_output_contract
      - source_authority_order
      - stepwise_execution_when_generating_files
      - concise_rationale_instead_of_hidden_reasoning
      - validation_checklist_or_completion_gate
      - preserve_semantic_fidelity_to_sources
      - ask_or_flag_only_when_blocking
    avoid:
      - vague_broad_generation_requests
      - multiple_files_when_one_file_is_requested
      - hidden_assumptions_about_repo_or_runtime_state
      - unnecessary_alternative_outputs
      - overexplaining_before_final_artifact
      - requesting_private_chain_of_thought
      - mixing_source_derivation_notes_into_final_files

  instruction_shape:
    recommended_order:
      1: role
      2: task
      3: exact_target_artifact_or_file
      4: source_context_and_authority_order
      5: constraints_and_boundaries
      6: output_contract
      7: validation_criteria
      8: next_step_or_stop_condition

  copy_paste_prompt_body_rules:
    metadata_outside_prompt_body: true
    source_document_names_inside_final_generated_files: false
    mandatory_machine_readable_capture_block: false
    citations_only_when_task_requires_sources: true
    final_prompt_must_be_directly_executable: true
    hidden_reasoning_request_forbidden: true
```

## When Claude Is a Good Fit

```yaml id="m6r01d"
Claude_fit_conditions:
  good_fit_for:
    Claude_Code_file_generation:
      use_when:
        - exact_file_path_or_package_path_is_known
        - structured_markdown_or_yaml_file_needed
        - source_constraints_must_be_preserved
        - one_file_per_prompt_flow_is_active
        - validation_gate_or_completion_check_needed
      value: "Useful when precise file authoring, package discipline, and source-bound structural compliance matter."

    extended_thinking:
      use_when:
        - architecture_decision_is_complex
        - long_source_material_requires_deep_integration
        - contradiction_or_drift_detection_needed
        - skill_package_design_needs_validation
        - multi_stage_prompt_flow_must_be_constructed
      value: "Useful when the task benefits from deliberate reasoning, constraint reconciliation, and robust validation."

    long_structured_document:
      use_when:
        - large_markdown_document_must_be_generated
        - many_sections_need_consistent_contracts
        - document_structure_is_more_important_than_style
        - semantic_fidelity_must_be_preserved
      value: "Useful when long-form structure, consistent headings, and careful preservation of source logic matter."

  weaker_fit_for:
    - tasks_requiring_exact_current_product_limits_without_verification
    - purely_mechanical_low_value_batch_transformations
    - high_volume_low_reasoning_API_batch_work
    - tasks_where_source_or_file_access_is_required_but_unavailable

  fit_decision_note: >
    Final routing authority belongs to ai-routing-and-usage-tracking. This file
    only describes Claude prompt adaptation and stable surface fit.
```

## Claude Code File-Generation Prompt Patterns

```yaml id="vjl3hy"
Claude_Code_file_generation_prompt_patterns:
  pattern_role: precise_file_author

  use_when:
    - one_exact_file_must_be_created
    - file_path_is_known
    - final_file_content_must_be_complete
    - package_or_schema_contract_exists
    - no_repo_scaffolding_is_allowed

  prompt_requirements:
    - state_exact_target_path
    - state_file_type
    - state_schema_or_section_ownership
    - state_context_carry_forward
    - state_global_constraints
    - forbid_extra_files
    - require_final_content_not_outline
    - include_file_specific_validation
    - include_next_prompt_when_in_prompt_flow

  preferred_output_shapes:
    - markdown_document
    - YAML_block
    - prompt_pack
    - workflow_record
    - compact_markdown_packet

  avoid:
    - creating_multiple_files
    - adding_repository_scaffolding
    - adding_source_citations_inside_final_files_when_forbidden
    - redefining_schema_owned_by_other_files
    - converting_reference_files_into_manifest_files
```

## Extended-Thinking Prompt Patterns

```yaml id="7b533i"
Claude_extended_thinking_prompt_patterns:
  pattern_role: constraint_reconciliation_architect

  use_when:
    - many_constraints_must_be_reconciled
    - architecture_or_package_order_matters
    - source_authority_conflicts_exist
    - operator_needs_a_validated_build_flow
    - hidden_inconsistencies_are_likely

  prompt_requirements:
    - name_authority_order
    - name_locked_decisions
    - name_forbidden_reopened_decisions
    - identify_conflicts_without_expanding_scope
    - produce_final_decision_or_artifact
    - provide_brief_rationale_not_private_reasoning
    - include_validation_or_completion_gate

  preferred_output_shapes:
    - decision_matrix
    - implementation_plan
    - synthesis_brief
    - critique_report
    - compact_markdown_packet

  avoid:
    - asking_for_private_chain_of_thought
    - producing_unbounded_analysis_without_output
    - reopening_locked_architecture_decisions
    - turning_source_review_into_new_scope
```

## Long Structured Document Prompt Patterns

```yaml id="n4k1bh"
Claude_long_structured_document_prompt_patterns:
  pattern_role: structured_document_author

  use_when:
    - document_has_many_sections
    - consistency_across_sections_matters
    - machine_readable_first_human_readable_second_is_needed
    - content_must_preserve_source_semantics
    - operator_needs_copy_paste_ready_markdown

  prompt_requirements:
    - define_document_purpose
    - define_section_order
    - define_machine_readable_blocks
    - define_human_readable_sections
    - state_preservation_rules
    - state_no_silent_omission_rule
    - include_open_questions_or_review_flags_when_needed
    - include_validation_checklist

  preferred_output_shapes:
    - markdown_document
    - compact_markdown_packet
    - YAML_block
    - implementation_plan
    - synthesis_brief

  avoid:
    - collapsing_yaml_indentation
    - repeating_same_schema_in_multiple_sections
    - converting_all_content_to_generic_prose
    - silently_simplifying_operator_specific_terms
    - overcompressing_when_fidelity_is_required
```

## Output Contract Preferences

```yaml id="dyibr9"
Claude_output_contract_preferences:
  preferred:
    exact_file_output:
      use_when:
        - one_file_per_prompt_flow_active
        - target_path_known
        - final_file_content_needed
      pattern:
        - "# FILE: <target path>"
        - "<complete file content>"
        - "---"
        - "# VALIDATION — FILE-SPECIFIC CHECKS"
        - "# NEXT PROMPT"
      constraints:
        - exactly_one_file
        - no_extra_commentary
        - final_not_outline

    structured_markdown:
      use_when:
        - operator_readability_and_copy_paste_use_matter
        - artifact_has_sections_and_validation
        - long_document_generation_needed
      pattern:
        - purpose_or_contract
        - structured_sections
        - validation
        - next_step_or_stop_condition

    compact_yaml_contract:
      use_when:
        - machine_readability_matters
        - schemas_enums_or_rules_are_needed
        - downstream_skill_references_fields
      constraints:
        - use_2_space_indentation
        - avoid_collapsed_YAML
        - define_each_schema_once
        - use_typed_constraints_for_ranges
        - use_allowed_lists_for_enums

    critique_gate:
      use_when:
        - validating_skill_or_contract_file
        - defect_detection_is_primary
        - rewrite_should_be_surgical
      pattern:
        - summary
        - critical_defects
        - surgical_fixes
        - completion_check

  avoid:
    - prose_only_contracts_when_machine_parsing_is_needed
    - manifest_files_that_duplicate_contract_logic
    - vague_next_steps_without_completion_gate
    - adding_rationale_inside_clean_copy_paste_prompt_body
```

## Failure Modes

```yaml id="q1a37r"
Claude_failure_modes:
  multi_file_drift:
    trigger: "The prompt requests exactly one file but the output creates multiple files or scaffolding."
    correction: "Return exactly one target file and place other work in the next prompt."

  schema_duplication:
    trigger: "The output redefines a schema already owned by another reference file."
    correction: "Remove duplicate schema and reference the owning key or file role."

  source_trace_leak:
    trigger: "Final generated files include source-document names, derivation notes, or citations when forbidden."
    correction: "Remove source trace from final file content and keep only operational rules."

  hidden_reasoning_request:
    trigger: "The prompt asks Claude to reveal private chain-of-thought."
    correction: "Ask for concise rationale, assumptions, validation checks, or decision basis instead."

  overbroad_document_generation:
    trigger: "The output expands beyond the requested artifact into architecture discussion or unrelated recommendations."
    correction: "Collapse back to the requested artifact and move unresolved issues to review flags."

  YAML_collapse:
    trigger: "YAML blocks lose indentation or become prose-like single-line strings."
    correction: "Rewrite YAML with valid 2-space indentation and parseable block structure."

  semantic_fidelity_loss:
    trigger: "The output simplifies, renames, or omits operator-specific terms without instruction."
    correction: "Restore original semantic ingredients and flag unclear terms instead of silently changing them."

  volatile_claim_without_verification:
    trigger: "The prompt or output claims current Claude product limits, rankings, pricing, or availability without verification."
    correction: "Replace with stable surface-class language or require current verification outside this contract."
```

## Minimal Examples

### Claude Code file-generation prompt

```text id="aw8ofw"
You are a precise Claude Code file author.

Task:
Create exactly one complete file.

Target file:
.claude/skills/example-skill/references/example-contract.md

Context:
Use the supplied SKILL.md and prior reference contracts as authority. Define only the schema owned by this file.

Constraints:
- Do not create other files.
- Do not scaffold a repo.
- Do not duplicate schemas owned by other files.
- Use valid YAML with 2-space indentation.
- Produce final content, not an outline.

Output exactly:
# FILE: .claude/skills/example-skill/references/example-contract.md

<complete file content>

---

# VALIDATION — FILE-SPECIFIC CHECKS

<checks>

Stop after the one file and validation checklist.
```

### Extended-thinking prompt

```text id="f0byid"
You are a constraint reconciliation architect.

Task:
Resolve the architecture decision using the supplied source constraints and locked operator decisions.

Authority order:
1. Latest operator decision
2. Current package contract
3. Current workflow/process validity
4. Prior examples only as calibration

Output:
1. Decision
2. Rationale summary
3. Tradeoff card
4. Risks
5. Completion check

Constraints:
Do not reveal private chain-of-thought. Do not reopen locked decisions unless they directly conflict with a higher-authority rule.

Stop when the decision is actionable.
```

### Long structured document prompt

```text id="w3wwlg"
You are a structured document author.

Task:
Create a machine-readable-first Markdown document from the supplied material.

Preservation rules:
- Preserve source semantics.
- Do not silently rename key terms.
- Do not omit rough notes that affect design logic.
- Mark unresolved items as review flags.

Output structure:
1. YAML metadata block
2. Machine-readable specification
3. Human-readable explanation
4. Validation checklist
5. Open questions if needed

Constraints:
Use valid YAML indentation. Define each schema once. Do not add unsupported claims.

Stop after the validation checklist and open questions.
```

### Claude prompt-refinement prompt

```text id="lac6ca"
You are a Claude prompt improvement specialist.

Task:
Improve the supplied prompt for Claude use without changing the operator's intent.

Input prompt:
<PASTE PROMPT>

Improve for:
- exact scope
- explicit output contract
- source authority order
- boundary conditions
- validation checklist
- stop condition

Output:
1. Revised copy-paste prompt
2. Short change rationale
3. Failure hints

Constraints:
Do not create multiple alternative prompt systems. Do not ask for private chain-of-thought. Preserve the original task semantics.
```
```

---

# VALIDATION — FILE-SPECIFIC CHECKS

- [ ] The file defines Claude prompt style rules.
- [ ] The file defines when Claude is a good fit.
- [ ] The file defines Claude Code file-generation prompt patterns.
- [ ] The file defines extended-thinking prompt patterns.
- [ ] The file defines long structured document prompt patterns.
- [ ] The file defines output contract preferences.
- [ ] The file defines failure modes.
- [ ] The file includes minimal copy-paste-clean examples.
- [ ] The file uses stable surface classes only.
- [ ] The file does not claim current pricing, exact model rankings, or exact product limits.
- [ ] The file does not define routing-decision schema owned by `ai-routing-and-usage-tracking`.
- [ ] The file does not duplicate `prompt_packet` schema.

---

# NEXT PROMPT

Paste this next:
> Prompt PE7:
> Create exactly one file.
>
> # FILE: .claude/skills/prompt-engineering/references/provider-style-contract-gemini.md
>
> File type: provider_style_contract.
> Schema ownership: owns Gemini-specific prompt adaptation rules.
> Context carry-forward: load PE1, PE2, PE3, PE4, PE5, and PE6 outputs before writing.
>
> This file must define:
> - Gemini prompt style rules
> - when Gemini is a good fit
> - long-context prompt patterns
> - broad comparison prompt patterns
> - document digestion prompt patterns
> - output contract preferences
> - failure modes
> - minimal examples
>
> Rules:
> - Use stable surface classes, not volatile model claims.
> - Do not claim current pricing, exact model rankings, or exact product limits.
> - Do not define routing-decision schema owned by ai-routing-and-usage-tracking.
> - Do not duplicate prompt_packet schema.
> - Keep examples short and copy-paste clean.
>
> Next prompt target: Prompt PE8.
