
# Provider Style Contract — ChatGPT
```yamlprovider_style_contract_chatgpt:  artifact_name: provider_style_contract_chatgpt  file_role: provider_specific_prompt_adaptation_contract  purpose: >    Define ChatGPT-specific prompt adaptation rules for high-reasoning,    deep-research, and agent-run prompt use. This file uses stable surface    classes only and does not claim current pricing, exact model rankings,    exact product limits, routing-decision schema, or prompt_packet schema.  ownership:    owns:      - ChatGPT_prompt_style_rules      - ChatGPT_fit_conditions      - ChatGPT_high_reasoning_prompt_patterns      - ChatGPT_deep_research_prompt_patterns      - ChatGPT_agent_run_prompt_patterns      - ChatGPT_output_contract_preferences      - ChatGPT_failure_modes      - ChatGPT_minimal_examples    must_not_own:      - routing_decision_schema      - monthly_quota_schema      - exact_model_rankings      - exact_pricing      - exact_product_limits      - prompt_packet_schema      - workflow_stage_taxonomy      - process_stage_taxonomy  volatility_policy:    stable_claims_allowed:      - abstract_surface_classes      - general_prompting_style_preferences      - high_reasoning_task_fit      - deep_research_task_fit      - agent_run_task_fit    volatile_claims_forbidden_without_current_verification:      - exact_model_rankings      - exact_product_limits      - current_pricing      - current_availability      - benchmark_claims
```

## ChatGPT Prompt Style Rules

```
ChatGPT_prompt_style_rules:  general_style:    preferred:      - explicit_role_and_task      - clear_context_boundary      - structured_output_contract      - direct_success_criteria      - explicit_validation_or_self_check      - concise_but_complete_constraints      - concrete_examples_when_shape_matters      - phased_reasoning_instructions_for_complex_tasks    avoid:      - vague_role_only_prompts      - hidden_or_implicit_output_contracts      - excessive_meta_discussion      - multiple_parallel_deliverables_without_priority      - ambiguous_source_authority      - unbounded_research_scope      - unscoped_agent_execution  instruction_shape:    recommended_order:      1: role      2: task      3: source_context_or_input_boundary      4: constraints      5: output_contract      6: validation_criteria      7: stop_condition  copy_paste_prompt_body_rules:    metadata_outside_prompt_body: true    source_document_names_inside_prompt_body: false    mandatory_machine_readable_capture_block: false    citations_only_when_task_requires_sources: true    final_prompt_must_be_directly_executable: true
```

## When ChatGPT Is a Good Fit

```
ChatGPT_fit_conditions:  good_fit_for:    high_reasoning:      use_when:        - complex_synthesis        - strategic_planning        - prompt_design        - architecture_tradeoffs        - critique_and_revision        - ambiguous_problem_framing      value: "Useful when reasoning quality, tradeoff handling, and structured synthesis matter."    deep_research:      use_when:        - source_grounded_research_needed        - current_information_or_verification_needed        - multi_source_comparison_needed        - claims_need_citations_or_evidence      value: "Useful when the prompt requires a research workflow, source comparison, and evidence-grounded synthesis."    agent_run:      use_when:        - bounded_multi_step_task        - tool_use_or_file_navigation_needed        - iterative_task_completion_needed        - operator_wants_task_execution_scaffold      value: "Useful when a task can be decomposed into bounded steps with progress checks and final deliverables."  weaker_fit_for:    - extremely_long_static_context_when_no_research_or_reasoning_is_needed    - purely_mechanical_low_value_batch_transformations    - tasks_requiring_exact_current_product_limits_without_verification    - tasks_with_unclear_permissions_or_unbounded_autonomous_action  fit_decision_note: >    Final routing authority belongs to ai-routing-and-usage-tracking. This file    only describes ChatGPT prompt adaptation and stable surface fit.
```

## High-Reasoning Prompt Patterns

```
ChatGPT_high_reasoning_prompt_patterns:  pattern_role: high_reasoning_structured_problem_solver  use_when:    - impact_is_high    - risk_is_high    - ambiguity_is_high    - evidence_need_is_moderate_or_high    - operator_needs_tradeoff_card_or_decision_support  prompt_requirements:    - define_problem_precisely    - list_assumptions    - separate_knowns_unknowns_and_inferences    - evaluate_options_against_criteria    - surface_tradeoffs    - produce_decision_or_next_step    - include_validation_check  preferred_output_shapes:    - decision_matrix    - synthesis_brief    - implementation_plan    - critique_report    - compact_markdown_packet  avoid:    - asking_for_unbounded_brainstorming    - requesting_long_chain_of_thought    - mixing_final_answer_with_private_reasoning_request    - allowing_unranked_option_sprawl
```

## Deep Research Prompt Patterns

```
ChatGPT_deep_research_prompt_patterns:  pattern_role: source_grounded_researcher  use_when:    - external_information_needed    - current_verification_needed    - source_conflict_possible    - claims_require_citations    - operator_needs_research_summary_or_decision_basis  prompt_requirements:    - define_research_question    - define_scope_and_exclusions    - define_source_quality_preferences    - request_source_diversity_when_relevant    - require_fact_assumption_uncertainty_split    - require_citations_for_source_based_claims    - request_date_sensitivity_check    - ask_for_insufficient_evidence_notice  preferred_output_shapes:    - research_summary    - synthesis_brief    - comparison_table    - decision_matrix  avoid:    - asking_for_current_claims_without_sources    - accepting_low_quality_sources_without_flagging    - hiding_uncertainty    - overquoting_source_text
```

## Agent-Run Prompt Patterns

```
ChatGPT_agent_run_prompt_patterns:  pattern_role: bounded_task_agent  use_when:    - task_has_multiple_steps    - progress_can_be_checked    - deliverable_is_explicit    - source_or_tool_actions_are_needed    - operator_accepts_agentic_execution_style  prompt_requirements:    - define_exact_goal    - define_allowed_actions    - define_forbidden_actions    - define_artifact_or_output_target    - define_progress_checkpoints    - define_stop_conditions    - require_uncertainty_or_blocker_reporting    - prevent_unbounded_follow_on_tasks  preferred_output_shapes:    - implementation_plan    - markdown_document    - compact_markdown_packet    - critique_report    - code_patch  safety_boundaries:    - do_not_assume_permission_for_state_changing_actions    - do_not_expand_scope_without_operator_instruction    - do_not_create_unrequested_files_or_infrastructure    - stop_and_report_when_required_input_or_permission_is_missing
```

## Output Contract Preferences

```
ChatGPT_output_contract_preferences:  preferred:    markdown_structured:      use_when:        - operator_readability_matters        - synthesis_or_planning_needed        - critique_report_needed      pattern:        - Summary        - Findings_or_Output        - Validation        - Open_Questions_or_Next_Actions    compact_packet:      use_when:        - output_feeds_downstream_skill        - operator_needs_fast_review        - flow_prompt_pack_context      pattern:        - metadata        - core_output        - rationale        - validation_status        - operator_review_flags    table:      use_when:        - comparison_needed        - decision_options_need_side_by_side_review        - routing_or_tradeoff_view_needed      constraints:        - keep_columns_few        - avoid_dense_nested_text        - include_decision_relevant_fields_only    YAML_block:      use_when:        - machine_readability_matters        - enum_or_contract_output_needed        - downstream_file_uses_structured_fields      constraints:        - use_2_space_indentation        - avoid_collapsed_YAML        - define_schema_once  avoid:    - long_unstructured_essay_when_contract_output_needed    - excessive_variants_without_selection    - unclear_markdown_heading_hierarchy    - mixing_metadata_into_copy_paste_prompt_body
```

## Failure Modes

```
ChatGPT_failure_modes:  unbounded_reasoning_prompt:    trigger: "The prompt asks for broad reasoning without decision criteria, output contract, or stop condition."    correction: "Add explicit criteria, output shape, and stop condition."  source_authority_blur:    trigger: "The prompt mixes supplied context, web/current research, and assumptions without boundaries."    correction: "Separate supplied context, allowed external research, assumptions, and uncertainty."  research_scope_sprawl:    trigger: "The deep research prompt asks for everything about a topic without scope, exclusions, or source quality rules."    correction: "Narrow the research question, source type, timeframe, and final decision use."  agent_run_overreach:    trigger: "The agent-run prompt permits broad autonomous action or unrequested file/infrastructure creation."    correction: "Define allowed actions, forbidden actions, checkpoints, and stop conditions."  variant_sprawl:    trigger: "The prompt requests many alternatives but no selection or synthesis rule."    correction: "Require one selected primary output and keep alternatives as brief comparison material."  hidden_output_contract:    trigger: "The requested answer shape is implied but not explicitly specified."    correction: "Add exact headings, fields, table columns, or artifact format."  reasoning_trace_request:    trigger: "The prompt asks for private chain-of-thought or hidden reasoning."    correction: "Ask for concise rationale, assumptions, checks, or decision basis instead."  volatile_claim_without_verification:    trigger: "The prompt asks for current limits, pricing, rankings, or availability without current verification."    correction: "Require current verification or mark the claim as unknown."
```

## Minimal Examples

### High-reasoning prompt

```
You are a strategic reasoning analyst.Task:Evaluate the following decision and recommend the best path.Context:<PASTE CONTEXT>Decision to resolve:<PASTE DECISION>Criteria:- impact- risk- reversibility- dependency load- operator effort- long-term leverageOutput:1. Recommendation2. Decision matrix3. Key assumptions4. Risks and mitigations5. Next concrete actionValidation:Separate facts from assumptions. Flag missing information that could change the recommendation.Stop when the recommendation is decision-ready.
```

### Deep research prompt

```
You are a source-grounded researcher.Research question:<PASTE QUESTION>Scope:- Include: <INCLUDE>- Exclude: <EXCLUDE>- Time sensitivity: <STATE WHETHER CURRENT INFORMATION MATTERS>Source preferences:Prioritize primary sources, official documentation, reputable research, and clearly dated material.Output:1. Executive summary2. Findings with citations3. Source disagreements4. Uncertainty and missing evidence5. Practical recommendationValidation:Do not present uncertain or outdated claims as settled. State when evidence is insufficient.
```

### Agent-run prompt

```
You are a bounded task agent.Goal:<PASTE GOAL>Allowed actions:- inspect supplied material- propose or produce the requested artifact- report blockersForbidden actions:- do not create unrequested files- do not change scope- do not assume missing permissions- do not continue into follow-on tasks after the deliverable is completeDeliverable:<DEFINE EXACT OUTPUT>Progress checks:Report blockers immediately. If the task becomes ambiguous, choose the safest compliant path and flag the assumption.Stop condition:Stop after the deliverable is complete and validated against the stated criteria.
```

### Prompt-refinement prompt for ChatGPT

```
You are a prompt improvement specialist.Task:Improve the supplied prompt for ChatGPT use without changing the operator's intent.Input prompt:<PASTE PROMPT>Improve for:- clearer task framing- explicit output contract- stronger validation criteria- better stop condition- less ambiguityOutput:1. Revised copy-paste prompt2. Short change rationale3. Failure hintsConstraints:Do not add new goals. Do not create multiple alternative prompt systems unless explicitly requested.
```