# FILE: .claude/skills/prompt-engineering/references/provider-style-contract-gemini.md

```markdown id="g7m2vp"
# Provider Style Contract — Gemini

```yaml
provider_style_contract_gemini:
  artifact_name: provider_style_contract_gemini
  file_role: provider_specific_prompt_adaptation_contract
  purpose: >
    Define Gemini-specific prompt adaptation rules for long-context digestion,
    broad document comparison, multimodal or visual-adjacent briefing, and
    structured synthesis. This file uses stable surface classes only and does
    not claim current pricing, exact model rankings, exact product limits,
    routing-decision schema, or prompt_packet schema.

  ownership:
    owns:
      - Gemini_prompt_style_rules
      - Gemini_fit_conditions
      - Gemini_long_context_digest_prompt_patterns
      - Gemini_broad_document_comparison_prompt_patterns
      - Gemini_visual_or_multimodal_briefing_prompt_patterns
      - Gemini_output_contract_preferences
      - Gemini_failure_modes
      - Gemini_minimal_examples
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
      - long_context_task_fit
      - broad_comparison_task_fit
      - multimodal_or_visual_adjacent_task_fit
    volatile_claims_forbidden_without_current_verification:
      - exact_model_rankings
      - exact_product_limits
      - current_pricing
      - current_availability
      - benchmark_claims
```

## Gemini Prompt Style Rules

```yaml id="7e9z32"
Gemini_prompt_style_rules:
  general_style:
    preferred:
      - explicit_context_map
      - clear_source_boundaries
      - section_by_section_processing
      - comparison_axes_before_comparison
      - structured_synthesis_after_extraction
      - explicit_instruction_to_preserve_source_hierarchy
      - compact_intermediate_notes_for_long_inputs
      - final_output_contract_after_processing_steps
    avoid:
      - dumping_large_context_without_navigation_instructions
      - asking_for_global_summary_before_extraction
      - mixing_source_extraction_and_opinion_without_labels
      - vague_compare_everything_requests
      - implicit_output_shape
      - unsupported_current_product_or_model_claims

  instruction_shape:
    recommended_order:
      1: role
      2: task
      3: context_inventory
      4: source_authority_rules
      5: processing_steps
      6: comparison_or_synthesis_axes
      7: output_contract
      8: validation_criteria
      9: stop_condition

  copy_paste_prompt_body_rules:
    metadata_outside_prompt_body: true
    source_document_names_inside_prompt_body: false
    mandatory_machine_readable_capture_block: false
    citations_only_when_task_requires_sources: true
    final_prompt_must_be_directly_executable: true
```

## When Gemini Is a Good Fit

```yaml id="l51k5q"
Gemini_fit_conditions:
  good_fit_for:
    long_context_digest:
      use_when:
        - many_documents_or_large_context_blocks
        - source_structure_must_be_preserved
        - operator_needs_compressed_yet_complete_digest
        - cross_document_patterns_matter
      value: "Useful when the task benefits from reading broad context before producing a structured synthesis."

    broad_document_comparison:
      use_when:
        - multiple_documents_need_side_by_side_comparison
        - contradictions_or_overlaps_must_be_found
        - formats_or_contracts_need_alignment
        - operator_needs_gap_map_or_convergence_summary
      value: "Useful when the task requires comparing many inputs across shared axes."

    multimodal_or_visual_adjacent_briefing:
      use_when:
        - visual_or_spatial_reasoning_is_helpful
        - image_or_layout_description_is_part_of_the_task
        - operator_needs_visual_brief_or_design_analysis
        - diagrams_or_screenshots_are_relevant_inputs
      value: "Useful for prompts that combine structured text reasoning with visual, spatial, or multimodal context."

    structured_synthesis:
      use_when:
        - large_source_set_needs_distillation
        - source_fidelity_is_important
        - operator_needs_macro_meso_summary
        - output_should_preserve_document_logic
      value: "Useful when the final answer must preserve broad source coverage while remaining operator-readable."

  weaker_fit_for:
    - tiny_single_prompt_rewrites_without_long_context
    - exact_current_product_or_pricing_claims_without_verification
    - highly_agentic_file_execution_without_tooling_scope
    - tasks_requiring_provider_specific_capabilities_not_currently_verified

  fit_decision_note: >
    Final routing authority belongs to ai-routing-and-usage-tracking. This file
    only describes Gemini prompt adaptation and stable surface fit.
```

## Long-Context Digest Prompt Patterns

```yaml id="8v623j"
Gemini_long_context_digest_prompt_patterns:
  pattern_role: long_context_digest_analyst

  use_when:
    - many_files_or_long_documents_supplied
    - source_coverage_matters_more_than_short_answer_speed
    - operator_needs_compression_without_semantic_loss
    - document_structure_must_remain_visible

  prompt_requirements:
    - identify_input_inventory
    - preserve_source_hierarchy
    - separate_macro_meso_micro_findings_when_useful
    - distinguish_repeated_themes_from_unique_details
    - mark_uncertain_or_missing_sections
    - avoid_silent_compression_of_decisions
    - produce_final_digest_after_extraction

  preferred_output_shapes:
    - synthesis_brief
    - markdown_document
    - compact_markdown_packet
    - comparison_table

  avoid:
    - summary_only_without_source_structure
    - collapsing_all_documents_into_one_flat_list
    - omitting_outliers_or_contradictions
    - inventing_missing_context
```

## Broad Document Comparison Prompt Patterns

```yaml id="9m6y9z"
Gemini_broad_document_comparison_prompt_patterns:
  pattern_role: cross_document_comparison_analyst

  use_when:
    - multiple_sources_need_alignment
    - contradictions_need_detection
    - version_differences_need_review
    - operator_needs_gap_analysis
    - reusable_contracts_or_rules_need_consolidation

  prompt_requirements:
    - define_comparison_axes_before_comparing
    - compare_like_with_like
    - identify_convergence
    - identify_conflicts
    - identify_missing_or_underdefined_parts
    - separate_source_facts_from_recommendations
    - produce_operator_decision_points_when_needed

  preferred_output_shapes:
    - comparison_table
    - decision_matrix
    - critique_report
    - synthesis_brief

  avoid:
    - comparing_documents_without_axes
    - treating_newest_document_as_authority_without_instruction
    - merging_conflicting_rules_without_flagging
    - excessive_table_columns
```

## Visual or Multimodal Briefing Prompt Patterns

```yaml id="vz5zqu"
Gemini_visual_or_multimodal_briefing_prompt_patterns:
  pattern_role: visual_context_synthesis_analyst

  use_when:
    - visual_layout_or_spatial_structure_matters
    - screenshots_or_image_descriptions_are_part_of_context
    - operator_needs_visual_briefing_for_design_or_generation
    - multimodal_inputs_need_textual_structuring

  prompt_requirements:
    - describe_visual_inputs_only_when_provided
    - separate_observation_from_interpretation
    - map_visual_details_to_task_relevance
    - preserve_layout_or_spatial_relationships
    - produce_clean_brief_or_analysis
    - flag_missing_visual_context

  preferred_output_shapes:
    - markdown_document
    - compact_markdown_packet
    - comparison_table
    - prompt_pack

  avoid:
    - pretending_to_see_visual_inputs_that_are_not_supplied
    - making_unverified_identity_or_current_claims
    - overdescribing_irrelevant_visual_details
    - mixing_visual_analysis_with_unrequested_design_execution
```

## Output Contract Preferences

```yaml id="1z9ial"
Gemini_output_contract_preferences:
  preferred:
    context_inventory_first:
      use_when:
        - many_inputs_are_supplied
        - operator_needs_traceability
        - long_context_digest_needed
      pattern:
        - input_inventory
        - source_grouping
        - processing_scope
        - missing_or_unclear_inputs

    comparison_table_then_synthesis:
      use_when:
        - multiple_documents_or_options_are_compared
        - contradictions_or_gaps_matter
      pattern:
        - comparison_axes
        - compact_table
        - convergence_summary
        - conflicts_and_gaps
        - recommendation_or_operator_questions

    structured_digest:
      use_when:
        - large_context_needs_compression
        - final_output_must_remain_readable
      pattern:
        - macro_summary
        - meso_structure
        - key_details
        - decisions_or_rules
        - open_questions

    visual_brief:
      use_when:
        - visual_or_spatial_context_is_relevant
        - design_or_image_generation_prompting_is_downstream
      pattern:
        - observed_visual_elements
        - spatial_or_layout_relationships
        - task_relevant_interpretation
        - brief_for_next_step

  avoid:
    - unstructured_long_summary
    - table_with_too_many_low_value_columns
    - hiding_contradictions_inside_general_synthesis
    - flattening_source_hierarchy_when_hierarchy_is_relevant
```

## Failure Modes

```yaml id="yd9v0i"
Gemini_failure_modes:
  context_flattening:
    trigger: "The prompt asks Gemini to summarize many documents without preserving source structure."
    correction: "Add context inventory, grouping rules, and hierarchy-preservation instructions."

  comparison_without_axes:
    trigger: "The prompt asks for broad comparison without comparison criteria."
    correction: "Define comparison axes before asking for document comparison."

  synthesis_before_extraction:
    trigger: "The prompt jumps directly to conclusions before extracting relevant source details."
    correction: "Require extraction first, then synthesis, then recommendations."

  visual_context_hallucination:
    trigger: "The prompt implies visual analysis when no visual input or visual description is supplied."
    correction: "Tell the model to flag missing visual context instead of inventing it."

  source_authority_confusion:
    trigger: "The prompt provides conflicting documents but no authority order or conflict policy."
    correction: "Require conflicts to be surfaced and ask for operator decision when authority is unclear."

  overlong_digest:
    trigger: "The output becomes a second version of the source rather than a usable digest."
    correction: "Add density target and require macro/meso compression with only critical details retained."

  volatile_claim_without_verification:
    trigger: "The prompt asks for current limits, pricing, rankings, or availability without current verification."
    correction: "Require current verification or mark the claim as unknown."

  provider_style_leak_into_schema:
    trigger: "The provider style file starts defining routing or prompt_packet schema."
    correction: "Remove schema definitions and reference the owning contract files."
```

## Minimal Examples

### Long-context digest prompt

```text id="c2rs21"
You are a long-context digest analyst.

Task:
Digest the supplied documents into a structured operator-ready summary.

Context:
<PASTE DOCUMENTS OR FILE CONTENT>

Processing rules:
1. First create a short input inventory.
2. Preserve the main hierarchy of each source.
3. Separate repeated themes from unique details.
4. Flag contradictions, missing sections, and unresolved questions.
5. Do not invent missing context.

Output:
1. Input inventory
2. Macro summary
3. Meso structure by source/theme
4. Key decisions or rules
5. Contradictions and gaps
6. Operator-relevant next questions

Stop when the digest is complete and no source structure critical to interpretation has been silently removed.
```

### Broad document comparison prompt

```text id="n4ch8f"
You are a cross-document comparison analyst.

Task:
Compare the supplied documents across the following axes:
- purpose
- scope
- output format
- rules or constraints
- conflicts
- missing elements

Context:
<PASTE DOCUMENTS>

Output:
1. Compact comparison table
2. Convergence summary
3. Conflicts that require operator decision
4. Gaps or missing definitions
5. Recommended consolidation approach

Validation:
Do not merge conflicting rules silently. State when the authority order is unclear.
```

### Visual or spatial briefing prompt

```text id="is7s66"
You are a visual context synthesis analyst.

Task:
Analyze the supplied visual or spatial context and turn it into a clean brief.

Input:
<PASTE IMAGE DESCRIPTION, SCREENSHOT CONTEXT, OR VISUAL NOTES>

Rules:
- Separate observation from interpretation.
- Preserve spatial/layout relationships.
- Flag missing visual information instead of inventing it.
- Focus only on details relevant to the task.

Output:
1. Observed elements
2. Spatial/layout relationships
3. Task-relevant interpretation
4. Brief for the next design or prompt step
```

### Prompt-refinement prompt for Gemini

```text id="jbs5d1"
You are a prompt improvement specialist for long-context Gemini use.

Task:
Improve the supplied prompt so it handles broad context more reliably without changing the operator's intent.

Input prompt:
<PASTE PROMPT>

Improve for:
- source inventory
- source hierarchy preservation
- comparison axes
- extraction before synthesis
- explicit output contract
- clear stop condition

Output:
1. Revised copy-paste prompt
2. Short change rationale
3. Failure hints

Constraints:
Do not add new goals. Do not define provider rankings, pricing, or current limits.
```
```

---

# VALIDATION — FILE-SPECIFIC CHECKS

- [ ] The file defines Gemini prompt style rules.
- [ ] The file defines when Gemini is a good fit.
- [ ] The file defines long-context digest prompt patterns.
- [ ] The file defines broad document comparison prompt patterns.
- [ ] The file defines visual or multimodal briefing prompt patterns.
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
> Prompt PE8:
> Create exactly one file.
>
> # FILE: .claude/skills/prompt-engineering/references/provider-style-contract-openrouter-todo.md
>
> File type: provider_style_contract_todo.
> Schema ownership: owns OpenRouter placeholder boundaries and TODO adaptation notes.
> Context carry-forward: load PE1, PE2, PE3, PE4, PE5, PE6, and PE7 outputs before writing.
>
> This file must define:
> - OpenRouter_later status
> - allowed placeholder use
> - low-reasoning supplemental API patterns
> - current verification requirements
> - forbidden volatile claims
> - boundary with ai-routing-and-usage-tracking
> - failure modes
> - minimal examples
>
> Rules:
> - Do not finalize OpenRouter model mapping.
> - Do not claim current pricing, exact model rankings, exact product limits, or exact availability.
> - Do not define routing-decision schema owned by ai-routing-and-usage-tracking.
> - Do not duplicate prompt_packet schema.
> - Keep examples short and copy-paste clean.
>
> Next prompt target: Prompt PE9.
