# Phase 2 Specialized Index Compile Plan — Claude Code Orchestration Design

```yaml
kb_slug: claude-code-orchestration-design
phase: operator_review_after_ingest_phase_1
status: phase_2_compile_target_reframed_operator_review_needed
created_at: 2026-07-02
phase_2_allowed: false
required_phase_2_phrase: approve ingest
report_type: pre_phase_2_compile_plan
```

## 1. Purpose

This run-log records the corrected Phase 2 target for the Claude Code Orchestration Design KB.

The KB should not compile toward a premature implementation of a named Apex agent system, the weekly routine, or any final runtime configuration. It should compile abstract, source-grounded orchestration knowledge so later implementation agents can answer practical design questions without rereading the raw corpus.

## 2. Lifecycle position

```yaml
lifecycle_position:
  deterministic_phase0: complete
  phase1_semantic_ingest: complete
  operator_review: in_progress
  phase2_wiki_compile: blocked_until_approval
  retrieval_indexing_after_phase2: not_yet
```

Phase 2 remains blocked until the operator says exactly:

```text
approve ingest
```

## 3. Corrected compile objective

```yaml
corrected_compile_objective:
  build_specialized_indexes_that_answer:
    - how_resilient_claude_apex_orchestration_systems_should_be_designed
    - what_patterns_exist_across_the_source_corpus
    - when_a_capability_should_become_skill_workflow_subagent_agent_script_hook_or_operator_gate
    - how_agents_exchange_work_with_minimal_context_cost
    - how_agent_specific_kbs_and_verifier_loops_work_without_drift
    - how_files_and_contracts_should_be_designed_for_low_token_cost_and_auditability
```

Source examples such as existing Apex Plan/Sync/Session skills, named first-wave agents, and the weekly routine are evidence and pattern sources. They must not be treated as the final implementation target of this KB compile.

## 4. Specialized indexes to compile

```yaml
needed_specialized_indexes:
  agent_orchestration_index:
    purpose: "How to structure agents, subagents, agent KBs, verifier loops, overlap, and boundaries."
    core_questions:
      - what_is_an_agent_in_this_system
      - persistent_agent_vs_ephemeral_subagent_vs_skill_vs_workflow_vs_script
      - smallest_useful_permanent_agent_set
      - when_adding_an_agent_improves_the_system
      - when_adding_an_agent_creates_coordination_overhead
      - what_every_agent_owns_and_must_not_own
      - how_build_validation_routing_and_authority_are_separated
      - why_durable_agents_need_own_kb_or_doctrine_root
      - what_belongs_in_activation_seed_vs_deeper_kb
      - how_much_redundancy_between_agent_kbs_is_useful
      - when_redundancy_becomes_conflicting_doctrine

  handoff_contract_index:
    purpose: "How agents exchange bounded work with authority, state, validation, risk, and stop conditions."
    core_questions:
      - smallest_valid_handoff_packet
      - required_handoff_fields
      - what_must_never_be_implicit
      - authority_basis_visibility
      - source_evidence_vs_candidate_vs_validated_vs_accepted_truth
      - current_state_vs_target_state
      - when_validator_or_operator_review_is_required
      - EVD_IMP_RSK_semantics
      - mandatory_stop_conditions
      - how_input_refs_replace_full_context

  project_execution_index:
    purpose: "How project work moves through planning, deterministic computation, gated mutation, and session memory."
    core_questions:
      - semantic_planning_vs_deterministic_read_side_computation_vs_gated_write_side_mutation
      - why_these_layers_should_be_separated
      - which_components_may_propose_state_changes
      - which_components_may_compute_reports
      - which_components_may_write_confirmed_mutation_records
      - what_defaults_to_dry_run
      - how_execution_evidence_becomes_state_delta
      - how_state_delta_becomes_next_session_context
      - how_raw_source_refs_are_preserved

  weekly_routine_case_index:
    purpose: "How the general orchestration model applies to recurring weekly or daily planning loops."
    core_questions:
      - which_parts_are_generic_orchestration_stages
      - which_parts_are_specific_to_weekly_routine
      - why_the_routine_is_a_workflow_not_a_single_skill
      - which_subprocedures_could_be_skills
      - where_ephemeral_subagents_help
      - which_steps_remain_operator_gated
      - what_each_stage_reads_and_writes
      - canonical_state_vs_temporary_execution_evidence
      - how_raw_dumps_are_prevented_from_bloating_future_context

  claude_mechanism_mapping_index:
    purpose: "When to use artifacts, skills, workflows, subagents, persistent agents, scripts, hooks, plugins, MCP, or operator gates."
    core_questions:
      - when_plain_markdown_yaml_artifact_is_enough
      - when_a_procedure_becomes_a_skill
      - when_a_process_becomes_a_workflow
      - when_a_task_needs_ephemeral_subagent_context_isolation
      - when_a_persistent_agent_is_justified
      - when_a_deterministic_script_or_hook_is_required
      - when_plugin_or_mcp_is_deferred
      - which_rules_are_soft_guidance_vs_hard_enforcement

  token_economy_and_information_design_index:
    purpose: "How file design, packet design, indexes, and progressive disclosure reduce token cost, drift, hallucination, and context overload."
    core_questions:
      - what_should_be_loaded_every_session
      - what_should_be_loaded_only_when_triggered
      - what_should_almost_never_be_loaded_directly
      - compiled_kb_pages_vs_raw_sources
      - refs_not_copies
      - yaml_first_artifact_design
      - smallest_useful_file_shape
      - packet_size_budget
      - how_file_based_state_prevents_chat_history_drift
      - how_stop_conditions_save_context_and_reduce_momentum_errors
```

## 5. Cross-index master questions

```yaml
cross_index_master_questions:
  M001_minimal_resilient_orchestration_architecture:
    answered_by:
      - agent_orchestration_index
      - claude_mechanism_mapping_index
      - token_economy_and_information_design_index

  M002_agent_work_exchange_without_chat_history_transfer:
    answered_by:
      - handoff_contract_index
      - token_economy_and_information_design_index

  M003_agent_qualified_verifier_loops:
    answered_by:
      - agent_orchestration_index
      - handoff_contract_index
      - token_economy_and_information_design_index

  M004_mechanism_selection:
    question: "When should Apex use skill, workflow, subagent, persistent agent, script, hook, plugin, MCP, or operator gate?"
    answered_by:
      - claude_mechanism_mapping_index
      - agent_orchestration_index

  M005_project_work_state_flow:
    question: "How does work move from idea to plan to computation to mutation to memory?"
    answered_by:
      - project_execution_index
      - handoff_contract_index

  M006_weekly_routine_as_case_study:
    answered_by:
      - weekly_routine_case_index
      - project_execution_index
      - agent_orchestration_index

  M007_overengineering_prevention:
    answered_by:
      - claude_mechanism_mapping_index
      - token_economy_and_information_design_index
```

## 6. Phase 2 page-shape implication

Phase 2 should compile pages that answer these index questions. It should not merely mirror Phase 1 batch names.

```yaml
page_shape_rule:
  every_phase2_page_should_answer:
    - what_is_the_pattern
    - when_is_it_used
    - when_is_it_not_used
    - what_artifact_or_contract_does_it_read
    - what_artifact_or_contract_does_it_write
    - what_keeps_it_token_efficient
    - what_prevents_drift
    - what_source_or_phase1_analysis_supports_it
```

## 7. Explicit non-goals for Phase 2

```yaml
phase2_non_goals:
  - final_named_agent_implementation
  - production_runtime_setup
  - final_weekly_routine_build
  - plugin_implementation
  - MCP_configuration
  - scheduler_implementation
  - writing_hooks_or_executable_runtime_surfaces
  - mutating_Apex_Plan_Sync_Session_PreCap_FlowRecap_APSU_or_personal_orchestration_state
```

## 8. Next action

```yaml
next_action:
  required_operator_gate: approve ingest
  after_gate:
    - compile wiki summaries concepts entities around specialized indexes
    - include source pointers confidence and claim labels
    - keep contradictions and deferred implementation questions visible
    - run deterministic index lint retrieval postflight after wiki pages exist
```
