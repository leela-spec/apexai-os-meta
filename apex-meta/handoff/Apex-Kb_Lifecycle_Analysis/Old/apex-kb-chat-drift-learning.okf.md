# Apex KB Chat Drift Learning Handoff

```okf
okf_document:
  id: apex_kb_chat_drift_learning_2026_07_03
  title: "Apex KB Chat Drift, Chunking, and Process-Guidance Learning"
  artifact_type: handoff_learning_file
  created_at: "2026-07-03"
  target_folder: "apex-meta/handoff/"
  target_file: "apex-meta/handoff/apex-kb-chat-drift-learning.okf.md"
  scope:
    system: Apex KB
    failure_class:
      - process_drift
      - non_optimal_chunking
      - incomplete_execution_handoffs
      - deterministic_loop_overextension
      - lifecycle_phase_confusion
      - user_context_not_preserved
    intended_consumers:
      - future_chatgpt_apex_kb_sessions
      - codex_prompt_orchestrators
      - llm_semantic_compiler_sessions
      - apex_kb_process_maintainers

source_context:
  summary: >
    The chat repeatedly failed to preserve the already-defined Apex KB process.
    The assistant kept producing partial next-step packets, options, or renewed
    deterministic validation loops after the process had already moved past those
    gates. This created unnecessary user work, cross-reference burden, and
    re-entry into already-closed lifecycle states.
  observed_user_feedback:
    - "The assistant did not create the full deterministic flow in one go."
    - "The assistant repeated partial Codex prompts instead of one closure flow."
    - "The assistant routed back to a Phase 1 decision even though the lifecycle context was already defined."
    - "The assistant should have created the next LLM handover after deterministic closure."
    - "The assistant should reduce iterative steps when not asked for."
  primary_failure: >
    The assistant optimized for local correctness of each answer rather than preserving
    the global Apex KB lifecycle state and producing the next complete executable artifact.

binding_process_memory:
  apex_kb_lifecycle_order:
    - scaffold
    - source_intake
    - deterministic_corpus_intelligence
    - ingest_phase_1_analysis
    - operator_gate
    - ingest_phase_2_wiki_compile
    - deterministic_index_validation
    - local_retrieval
    - query_packet_generation
    - lint_audit_maintenance
  deterministic_ownership:
    - scaffold_structure
    - file_hashing
    - source_manifest_shape
    - source_storage_mode_recording
    - corpus_profile
    - heading_link_frontmatter_maps
    - keyword_hit_maps
    - deterministic_index_sections
    - frontmatter_validation
    - link_orphan_stale_checks
    - retrieval_index_build_query_export
    - audit_file_listing
  llm_ownership:
    - relevance_judgment
    - source_summary
    - concept_extraction
    - entity_synthesis
    - contradiction_interpretation
    - phase_1_analysis
    - phase_2_wiki_drafting
    - query_answer_synthesis
    - knowledge_gap_framing
  core_rule: >
    Deterministic validation is a gate, not the product. Once deterministic infrastructure
    passes, the next step must return to the Apex KB lifecycle and advance the semantic
    or post-semantic stage instead of creating another validation loop.

failure_analysis:
  failure_01_partial_codex_packets:
    symptom: >
      Codex handoffs omitted complete shell execution flow, repo setup, exact validation,
      exit-code semantics, report creation, commit, push, and final YAML in one block.
    cost:
      user_cost: high
      process_cost: repeated cross-referencing and re-entry into Codex
      time_cost: multiple avoidable iterations
    corrected_rule: >
      If the user asks for a Codex execution step, emit exactly one complete deterministic
      execution packet from repo entry to final YAML. Do not split execution into analysis,
      options, and later command blocks.

  failure_02_options_when_execution_was_required:
    symptom: >
      The assistant offered options, recommendations, and alternatives when the process
      already had a defined next step.
    cost:
      user_cost: confusion and additional orchestration work
      process_cost: divergent branches from a linear lifecycle
    corrected_rule: >
      Do not offer options when the user asks for the next step in a defined Apex KB process.
      Produce the single next artifact that advances the lifecycle.

  failure_03_deterministic_loop_overextension:
    symptom: >
      After lint commands were finalized, the assistant kept creating deterministic
      validation/postflight tasks instead of returning to LLM semantic continuation.
    cost:
      user_cost: frustration and unnecessary Codex cycles
      process_cost: deterministic gates treated as lifecycle destination
    corrected_rule: >
      After deterministic closure passes, route immediately to the next lifecycle phase:
      LLM semantic compile, operator approval, or deterministic index rebuild depending
      on the already-known state.

  failure_04_phase_rewind:
    symptom: >
      The assistant suggested a Phase 1 decision/state review even though the user expected
      continuation from an already-established process state.
    cost:
      user_cost: loss of trust and perceived process reset
      process_cost: lifecycle regression
    corrected_rule: >
      Never rewind the Apex KB lifecycle unless a hard blocker proves the previous state
      invalid. Preserve accepted prior state and advance from it.

  failure_05_non_optimal_chunking:
    symptom: >
      Responses chunked work into too many conceptual steps and handovers, each requiring
      user interpretation.
    cost:
      user_cost: manual orchestration burden
      process_cost: unnecessary chat turns and context fragmentation
    corrected_rule: >
      Chunk by execution boundary, not by reasoning boundary. One chunk must equal one
      usable artifact: complete Codex command, complete LLM handover, complete report, or
      complete decision packet.

  failure_06_wrong_executor_routing:
    symptom: >
      The assistant blurred Codex, deterministic tool, LLM semantic compiler, and human
      operator responsibilities.
    cost:
      user_cost: uncertainty about where to execute next
      process_cost: wrong tool chosen for semantic work
    corrected_rule: >
      Always name the executor explicitly and do not switch executor class mid-answer.
      Codex patches scripts and deterministic files. Deterministic tools validate and index.
      LLM compiles semantic KB content. Human operator provides approval gates.

  failure_07_insufficient_state_compression:
    symptom: >
      The assistant did not compress prior facts into a stable state object before generating
      the next action.
    cost:
      user_cost: repeated correction of already-known facts
      process_cost: stale or contradictory handovers
    corrected_rule: >
      Before producing any next-step artifact, create an internal state object containing:
      current lifecycle phase, latest committed deterministic result, finalized commands,
      open blockers, executor, output path, and stop condition.

mandatory_response_protocol:
  for_apex_kb_next_steps:
    step_01_state_lock:
      description: >
        Lock the known current lifecycle state from the latest execution report or handover.
      output_visible: false
      required_fields:
        - kb_root
        - latest_commit
        - completed_phase_or_gate
        - finalized_artifacts
        - hard_failures
        - next_lifecycle_phase
    step_02_executor_select:
      description: >
        Select exactly one executor for the next artifact.
      allowed_executors:
        - CODEX
        - DETERMINISTIC_TOOL
        - LLM
        - HUMAN_OPERATOR
      rule: "Do not mix executor classes in one handoff unless explicitly requested."
    step_03_artifact_select:
      description: >
        Select exactly one artifact type.
      allowed_artifacts:
        - deterministic_execution_script
        - codex_patch_prompt
        - llm_semantic_handover
        - operator_approval_packet
        - deterministic_index_rebuild_prompt
        - final_status_report
    step_04_emit_complete_artifact:
      description: >
        Emit the complete artifact in one block with no missing execution spine.
      required_for_codex:
        - repo
        - branch
        - cd_or_repo_resolution
        - git_checkout
        - git_pull
        - dirty_tree_policy
        - exact_commands
        - expected_exit_codes
        - report_paths
        - git_add_commit_push
        - final_yaml_schema
      required_for_llm:
        - role
        - current_state
        - source_artifacts_to_read
        - lifecycle_position
        - semantic_task
        - output_path
        - stop_condition
        - final_result_schema
    step_05_no_option_sprawl:
      description: >
        Do not provide alternatives unless the user explicitly asks for options.
      default: single_next_action

hard_rules:
  - id: no_partial_codex_handoff
    rule: >
      A Codex handoff is invalid if it does not include a full executable command flow,
      validation semantics, commit/push behavior, and final YAML schema.
  - id: no_deterministic_loop_after_pass
    rule: >
      If a deterministic gate returns PASS or PASS_WITH_WARNINGS, do not create another
      deterministic validation task unless the report names a hard failure.
  - id: no_phase_rewind
    rule: >
      Do not route back to Phase 0 or Phase 1 when the process state indicates the KB is
      already past that phase, unless a missing artifact is explicitly proven.
  - id: no_optional_branches_in_execution_prompt
    rule: >
      Execution prompts must not contain optional checks, optional real-surface checks, or
      alternatives. If a check is needed, make it mandatory; otherwise omit it.
  - id: preserve_user_execution_policy
    rule: >
      For Codex prompts, work directly on main, avoid unnecessary branches and PRs, avoid
      architecture reasoning, and complete with commit and push when requested.
  - id: semantic_after_deterministic
    rule: >
      Once deterministic infrastructure is finalized, return to LLM-owned semantic KB work:
      synthesis, wiki compile, contradiction exposure, query packet generation, or index
      rebuild after semantic updates.
  - id: one_chunk_one_artifact
    rule: >
      Do not split a next step into analysis plus separate execution unless explicitly asked.
      The output must be directly usable.

executor_routing_matrix:
  codex:
    use_when:
      - script_missing_or_broken
      - deterministic command must be implemented or patched
      - report file must be created via repo commit and push
    do_not_use_when:
      - semantic synthesis is needed
      - wiki/concept/entity meaning must be compiled
      - query answer synthesis is needed
      - operator approval is needed
  deterministic_tool:
    use_when:
      - existing script command should run
      - indexes need rebuild
      - lint/audit/status/health should be checked
    do_not_use_when:
      - source interpretation is required
      - contradiction meaning must be judged
  llm:
    use_when:
      - phase_1_analysis
      - phase_2_wiki_compile
      - semantic continuation report
      - knowledge gap framing
      - query synthesis from compiled KB pages
    do_not_use_when:
      - file hashing or index rebuild is the task
      - raw repo mutation is needed without deterministic command
  human_operator:
    use_when:
      - exact approval phrase is required
      - semantic ambiguity requires business decision
      - lifecycle gate needs explicit operator consent

corrected_next_step_pattern_after_lint_closure:
  given:
    deterministic_closure: PASS_OR_PASS_WITH_WARNINGS
    commands_finalized:
      - lint-repo-execution-router
      - lint-historical-path-authority
  do:
    executor: LLM
    artifact: llm_semantic_handover
    action: >
      Continue semantic Apex KB compilation using finalized deterministic infrastructure
      as support evidence.
  do_not:
    - create another Codex validation loop
    - re-check command existence unless final report failed
    - restart Phase 1 decision if the process state is already known

minimum_next_step_schema:
  format: okf
  fields:
    NEXT_STEP:
      executor: "CODEX | DETERMINISTIC_TOOL | LLM | HUMAN_OPERATOR"
      lifecycle_position: "<current Apex KB lifecycle phase>"
      action: "<single action>"
      input_artifacts:
        - "<path>"
      output_artifact: "<path>"
      stop_condition: "<single stop condition>"
      forbidden:
        - "<specific drift prevention rule>"

quality_gate_for_future_assistant:
  before_answering_apex_kb_next_step:
    questions:
      - "Am I preserving the latest committed/executed state?"
      - "Am I advancing the lifecycle instead of reopening an earlier gate?"
      - "Did the user ask for options, or do they need one next action?"
      - "Is the executor class correct?"
      - "Is the output directly usable without cross-referencing?"
      - "Does this reduce, not increase, iterative steps?"
    fail_if_any_true:
      - "The answer requires the user to assemble commands from multiple sections."
      - "The answer offers options without being asked."
      - "The answer routes back to Codex after a deterministic PASS without hard failure."
      - "The answer restarts lifecycle discovery when state was already supplied."
      - "The answer omits commit/push/final YAML for Codex execution."
      - "The answer omits output path/final schema for LLM handover."

canonical_failure_summary:
  one_sentence: >
    The assistant repeatedly failed by treating Apex KB as a series of local prompt tasks
    instead of a stateful lifecycle, causing phase rewinds, partial execution chunks, and
    unnecessary deterministic loops after gates had already passed.

canonical_correction_summary:
  one_sentence: >
    Future Apex KB assistance must lock the current lifecycle state, select one executor,
    emit one complete artifact, and advance exactly one lifecycle step without options,
    rewinds, or validation-loop drift unless a hard blocker is proven.
```
