# Prompt Packet Contract
```yaml
prompt_packet_contract:  artifact_name: prompt_packet  file_role: prompt_engineering_reference_contract  purpose: >    Define the minimum valid structure for prompt packets, prompt sequences,    final copy-paste prompts, start prompts, follow-up prompts, rationales,    failure hints, learning hints, expected output contracts, usage tags, and    light capture hints. This file owns prompt-packet schema. Other files may    reference these keys but must not redefine them.  ownership:    owns:      - prompt_packet      - prompt_sequence      - final_copy_paste_prompt      - start_prompt      - follow_up_prompt      - prompt_design_rationale      - provider_rationale      - prompt_failure_hints      - prompt_learning_hints      - expected_output_contract      - usage_tracking_tags      - light_capture_hints    must_not_own:      - routing_decision      - planned_usage_budget      - workflow_stage_taxonomy      - process_stage_taxonomy      - daily_plan      - flow_packet      - FlowRecap_output      - project_status_merge  global_rules:    metadata_outside_prompt_body: true    one_primary_prompt_system_only: true    fallback_notes_allowed: true    parallel_alternative_prompt_systems_forbidden_by_default: true    mandatory_machine_readable_capture_block_inside_every_prompt: false    copy_paste_prompt_body_must_be_clean: true    source_document_names_forbidden_inside_final_prompt_body: true    citations_forbidden_inside_final_prompt_body_unless_operator_requests: true
```

## Schema: prompt_packet

```
prompt_packet:  type: object  required:    - packet_id    - packet_role    - prompt_task_type    - expected_output_contract    - provider_target    - provider_rationale    - prompt_design_rationale    - final_copy_paste_prompt    - prompt_failure_hints    - prompt_learning_hints    - validation_status  fields:    packet_id:      type: string      format: "prompt_packet_<short_slug>"      required: true    packet_role:      type: string      allowed:        - start_prompt        - follow_up_prompt        - prompt_sequence_container        - standalone_prompt_packet      required: true    prompt_task_type:      type: string      allowed:        - research        - synthesis        - planning        - coding        - critique        - file_generation        - creative_generation        - visual_briefing        - long_context_digestion        - validation        - workflow_extraction        - workflow_normalization        - prompt_refinement        - operator_defined      required: true    workflow_stage:      type: string      required: false      nullable: true    process_stage:      type: string      required: false      nullable: true    expected_output_type:      type: string      required: false      nullable: true    expected_output_contract:      type: object_ref      ref: expected_output_contract      required: true    provider_target:      type: string      allowed:        - ChatGPT        - Claude        - Gemini        - OpenRouter_later        - provider_unspecified      required: true    provider_rationale:      type: object_ref      ref: provider_rationale      required: true    prompt_design_rationale:      type: object_ref      ref: prompt_design_rationale      required: true    final_copy_paste_prompt:      type: object_ref      ref: final_copy_paste_prompt      required: true    prompt_failure_hints:      type: object_ref      ref: prompt_failure_hints      required: true    prompt_learning_hints:      type: object_ref      ref: prompt_learning_hints      required: true    usage_tracking_tags:      type: object_ref      ref: usage_tracking_tags      required: false    light_capture_hints:      type: object_ref      ref: light_capture_hints      required: false    validation_status:      type: string      allowed:        - valid        - valid_with_warnings        - operator_review_recommended        - low_confidence_auto_generated        - blocked_by_missing_operator_decision      required: true    operator_review_flags:      type: list      item_type: string      required: false
```

## Schema: prompt_sequence

```
prompt_sequence:  type: object  required:    - sequence_id    - sequence_role    - start_prompt    - validation_status  fields:    sequence_id:      type: string      format: "prompt_sequence_<short_slug>"      required: true    sequence_role:      type: string      allowed:        - single_sprint_prompt_sequence        - full_flow_prompt_sequence        - follow_up_iteration_sequence        - provider_comparison_sequence      required: true    start_prompt:      type: object_ref      ref: start_prompt      required: true    follow_up_prompts:      type: list      item_ref: follow_up_prompt      min_items: 0      max_items: 6      required: false    sequence_logic:      type: string      allowed:        - start_then_optional_follow_up        - generate_critique_revise        - research_synthesize_decide        - outline_expand_compress        - extract_normalize_validate        - compare_provider_outputs_select_finalize        - prompt_result_learn_update        - operator_defined      required: false    stop_conditions:      type: list      item_type: string      min_items: 1      max_items: 8      required: false    validation_status:      type: string      allowed:        - valid        - valid_with_warnings        - operator_review_recommended        - low_confidence_auto_generated        - blocked_by_missing_operator_decision      required: true
```

## Schema: final_copy_paste_prompt

```
final_copy_paste_prompt:  type: object  required:    - prompt_body    - prompt_body_rules  fields:    prompt_body:      type: string      required: true      constraints:        directly_executable: true        copy_paste_ready: true        contains_metadata_header: false        contains_required_machine_capture_block: false        contains_source_document_names: false        contains_citations_by_default: false    prompt_body_rules:      type: object      required: true      fields:        role_is_clear:          type: boolean          required_value: true        task_is_clear:          type: boolean          required_value: true        context_is_sufficient:          type: boolean          required_value: true        output_contract_is_explicit:          type: boolean          required_value: true        constraints_are_explicit:          type: boolean          required_value: true        validation_criteria_are_explicit:          type: boolean          required_value: true        stop_condition_is_present:          type: boolean          required_value: true    copy_boundary:      type: string      allowed:        - copy_prompt_body_only      required: false
```

## Schema: start_prompt

```
start_prompt:  type: object  required:    - prompt_id    - final_copy_paste_prompt    - purpose  fields:    prompt_id:      type: string      format: "start_prompt_<short_slug>"      required: true    purpose:      type: string      allowed:        - initiate_work        - initiate_research        - initiate_file_generation        - initiate_validation        - initiate_workflow_extraction        - initiate_prompt_refinement        - operator_defined      required: true    final_copy_paste_prompt:      type: object_ref      ref: final_copy_paste_prompt      required: true    expected_first_response:      type: string      required: false    handoff_to_follow_up:      type: string      required: false
```

## Schema: follow_up_prompt

```
follow_up_prompt:  type: object  required:    - prompt_id    - follow_up_role    - final_copy_paste_prompt  fields:    prompt_id:      type: string      format: "follow_up_prompt_<short_slug>"      required: true    follow_up_role:      type: string      allowed:        - critique        - revise        - compress        - expand        - validate        - compare        - extract        - normalize        - decide        - continue        - operator_defined      required: true    trigger_condition:      type: string      required: false    final_copy_paste_prompt:      type: object_ref      ref: final_copy_paste_prompt      required: true    expected_delta:      type: string      required: false
```

## Schema: prompt_design_rationale

```
prompt_design_rationale:  type: object  required:    - rationale  fields:    rationale:      type: string      max_words:        type: integer        min: 1        max: 80      required: true    design_basis:      type: list      item_type: string      allowed_items:        - task_type        - expected_output_type        - workflow_stage        - process_stage        - iteration_loop        - validation_need        - operator_constraint        - source_context_shape      required: false
```

## Schema: provider_rationale

```
provider_rationale:  type: object  required:    - provider_target    - rationale  fields:    provider_target:      type: string      allowed:        - ChatGPT        - Claude        - Gemini        - OpenRouter_later        - provider_unspecified      required: true    rationale:      type: string      max_words:        type: integer        min: 1        max: 80      required: true    confidence:      type: string      allowed:        - high        - medium        - low        - needs_current_verification      required: false    fallback_surface:      type: string      required: false
```

## Schema: prompt_failure_hints

```
prompt_failure_hints:  type: object  required:    - hints  fields:    hints:      type: list      item_type: string      min_items: 1      max_items: 6      required: true    common_failure_classes:      type: list      item_type: string      allowed_items:        - missing_context        - wrong_output_shape        - overbroad_answer        - hallucinated_source_claim        - insufficient_validation        - provider_mismatch        - workflow_mismatch        - excessive_alternatives      required: false
```

## Schema: prompt_learning_hints

```
prompt_learning_hints:  type: object  required:    - hints  fields:    hints:      type: list      item_type: string      min_items: 1      max_items: 6      required: true    feedback_capture_focus:      type: list      item_type: string      allowed_items:        - output_quality        - missing_context        - provider_fit        - instruction_clarity        - validation_failures        - reusable_pattern_candidate        - operator_edit_needed      required: false
```

## Schema: expected_output_contract

```
expected_output_contract:  type: object  required:    - expected_output_type    - output_shape    - success_criteria  fields:    expected_output_type:      type: string      allowed:        - markdown_document        - compact_markdown_packet        - YAML_block        - comparison_table        - decision_matrix        - critique_report        - implementation_plan        - code_patch        - research_summary        - synthesis_brief        - prompt_pack        - workflow_record        - operator_defined      required: true    output_shape:      type: string      required: true    success_criteria:      type: list      item_type: string      min_items: 1      max_items: 10      required: true    forbidden_outputs:      type: list      item_type: string      required: false    validation_method:      type: string      allowed:        - self_check        - checklist        - compare_against_contract        - operator_review        - source_grounding_review        - code_or_schema_validation        - not_applicable      required: false
```

## Schema: usage_tracking_tags

```
usage_tracking_tags:  type: object  required:    - surface_class    - reasoning_class  fields:    surface_class:      type: string      allowed:        - subscription_frontier        - quota_limited_frontier        - scarce_monthly_mode        - supplemental_API_low_reasoning        - later_OpenRouter        - unknown      required: true    reasoning_class:      type: string      allowed:        - low        - medium        - high        - highest_available        - unknown      required: true    task_value_class:      type: string      allowed:        - low_value        - medium_value        - high_value        - strategic_bottleneck        - unknown      required: false    usage_capture_needed:      type: boolean      required: false    quota_note:      type: string      required: false
```

## Schema: light_capture_hints

```
light_capture_hints:  type: object  required:    - hints  fields:    hints:      type: list      item_type: string      min_items: 0      max_items: 5      required: true    canonical_capture_location:      type: string      allowed:        - raw_flow_dump        - FlowRecap        - prompt_result_feedback        - not_required      required: true    rule:      type: string      allowed:        - prompt_body_may_include_light_capture_hint_only        - capture_belongs_outside_prompt_body      required: true
```

## Valid Examples

### Minimal prompt packet

```
prompt_packet:  packet_id: prompt_packet_validate_skill_file  packet_role: standalone_prompt_packet  prompt_task_type: validation  workflow_stage: skill_package_validation  process_stage: review  expected_output_type: critique_report  expected_output_contract:    expected_output_type: critique_report    output_shape: "Short markdown report with pass/fail checks and surgical fixes."    success_criteria:      - "Checks frontmatter."      - "Checks section order."      - "Checks YAML parseability."      - "Names only necessary corrections."    validation_method: checklist  provider_target: Claude  provider_rationale:    provider_target: Claude    rationale: "Claude fits structured file validation and instruction-following."    confidence: high  prompt_design_rationale:    rationale: "The prompt constrains the reviewer to contract checks, not broad rewriting."    design_basis:      - expected_output_type      - validation_need  final_copy_paste_prompt:    prompt_body: |      You are validating one Claude skill file against a fixed package contract.      Task:      Review the supplied SKILL.md and return only:      1. pass/fail summary      2. critical defects      3. exact surgical fixes      Constraints:      Do not rewrite the whole file unless a defect makes it unusable.      Do not add new package scope.      Output:      Markdown report with headings: Summary, Critical Defects, Surgical Fixes, Completion Check.      Stop when all contract checks are addressed.    prompt_body_rules:      role_is_clear: true      task_is_clear: true      context_is_sufficient: true      output_contract_is_explicit: true      constraints_are_explicit: true      validation_criteria_are_explicit: true      stop_condition_is_present: true    copy_boundary: copy_prompt_body_only  prompt_failure_hints:    hints:      - "Watch for rewriting drift instead of validation."      - "Check whether YAML blocks are parseable."    common_failure_classes:      - wrong_output_shape      - workflow_mismatch  prompt_learning_hints:    hints:      - "Capture whether the reviewer found repeated schema definitions."      - "Capture whether the provider choice was sufficient."    feedback_capture_focus:      - output_quality      - validation_failures  usage_tracking_tags:    surface_class: subscription_frontier    reasoning_class: high    task_value_class: high_value    usage_capture_needed: true  light_capture_hints:    hints:      - "After use, note whether the validation missed structural defects."    canonical_capture_location: prompt_result_feedback    rule: prompt_body_may_include_light_capture_hint_only  validation_status: valid  operator_review_flags: []
```

### Prompt sequence example

```
prompt_sequence:  sequence_id: prompt_sequence_generate_critique_revise  sequence_role: follow_up_iteration_sequence  sequence_logic: generate_critique_revise  start_prompt:    prompt_id: start_prompt_generate_contract    purpose: initiate_file_generation    final_copy_paste_prompt:      prompt_body: |        Create one reference contract file for the supplied skill package.        Use valid YAML blocks, define each schema once, and include one minimal example.        Do not create other files.        Output exactly:        # FILE: <path>        <complete file content>      prompt_body_rules:        role_is_clear: true        task_is_clear: true        context_is_sufficient: true        output_contract_is_explicit: true        constraints_are_explicit: true        validation_criteria_are_explicit: true        stop_condition_is_present: true  follow_up_prompts:    - prompt_id: follow_up_prompt_contract_critique      follow_up_role: critique      trigger_condition: "Use after the first draft exists."      final_copy_paste_prompt:        prompt_body: |          Critique the generated contract for schema duplication, invalid YAML,          missing typed constraints, and unclear ownership. Return only required fixes.        prompt_body_rules:          role_is_clear: true          task_is_clear: true          context_is_sufficient: true          output_contract_is_explicit: true          constraints_are_explicit: true          validation_criteria_are_explicit: true          stop_condition_is_present: true      expected_delta: "Defects and exact fixes only."  stop_conditions:    - "All required schemas are defined once."    - "No metadata appears inside the clean copy-paste prompt body."    - "Validation status is assignable."  validation_status: valid
```

## Edge-Case Examples

### Missing provider target

```
prompt_packet:  packet_id: prompt_packet_missing_provider  packet_role: standalone_prompt_packet  prompt_task_type: synthesis  expected_output_contract:    expected_output_type: synthesis_brief    output_shape: "Compact markdown synthesis brief."    success_criteria:      - "Uses supplied context only."      - "Separates facts from assumptions."  provider_target: provider_unspecified  provider_rationale:    provider_target: provider_unspecified    rationale: "No routing decision was supplied; prompt remains provider-neutral."    confidence: low  prompt_design_rationale:    rationale: "Provider-neutral language preserves usefulness until routing is decided."  final_copy_paste_prompt:    prompt_body: |      Synthesize the supplied material into a compact brief.      Separate:      - confirmed facts      - inferred assumptions      - unresolved questions      Do not add outside claims.    prompt_body_rules:      role_is_clear: true      task_is_clear: true      context_is_sufficient: true      output_contract_is_explicit: true      constraints_are_explicit: true      validation_criteria_are_explicit: true      stop_condition_is_present: true  prompt_failure_hints:    hints:      - "May be less effective without provider-specific adaptation."  prompt_learning_hints:    hints:      - "Record whether provider-neutral wording was sufficient."  validation_status: operator_review_recommended  operator_review_flags:    - missing_provider_target
```

### Capture block drift correction

```
capture_block_drift_correction:  invalid_pattern:    prompt_body_requires:      - "Return a mandatory YAML capture block after every answer."  valid_pattern:    light_capture_hints:      hints:        - "After running this prompt, note major failures in prompt_result_feedback if useful."      canonical_capture_location: prompt_result_feedback      rule: prompt_body_may_include_light_capture_hint_only  reason: >    Canonical execution capture belongs to raw_flow_dump, FlowRecap, or    prompt_result_feedback. It does not belong as a mandatory block inside    every final copy-paste prompt.
```