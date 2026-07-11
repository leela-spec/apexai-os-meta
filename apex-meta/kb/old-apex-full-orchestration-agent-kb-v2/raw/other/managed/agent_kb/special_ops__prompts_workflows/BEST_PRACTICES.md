---
class: special_ops_prompts_workflows_best_practices
role: SPECIAL_OPS_PROMPTS_WORKFLOWS_ACCEPTED_PRACTICES
surface: agent_kb_scaffold
version: "2.0"
last_validated_at: "2026-05-07"
context_mode: compact
status: accepted
owner: special_ops__prompts_workflows
validator: meta_ops
source_file: BEST_PRACTICES.md
---

# BEST_PRACTICES

```yaml
purpose:
  file: accepted compact practices for Special Ops Prompts Workflows
  mode: YAML-first registry
  evidence_location: appendices

file_contract:
  output_type: accepted_practices_scaffold
  entry_groups: [critical_practices, required_practices, recommended_practices]
  entry_schema:
    required: [id, practice, context, prevents, refs, scores]
    inherited_defaults: [status, owner, validator, review_due]
  duplicate_policy:
    id_unique: true
    no_semantic_duplicates: true
    new_or_overlapping_practices_route_to: LEARNING_QUEUE.md
  structure_note: compact frontmatter plus one fenced YAML registry

practice_registry:
  active_practice_count: 11
  defaults:
    status: accepted
    owner: special_ops__prompts_workflows
    validator: meta_ops
    review_due: "2026-07-27"

  critical_practices:
    - id: PW-BP-001
      practice: "Use full final bodies or live-edit instructions when Markdown diff transport is fragile; reserve patch mode for small bounded defects with stable anchors."
      context: ["large_markdown_rewrite", "new_file_creation", "connector_output_not_line_stable", "chat_output_not_line_stable", "CRLF_or_hidden_character_risk", "malformed_unified_diff_with_visible_bounded_intent", "small_bounded_defect_with_reliable_anchors"]
      prevents: "diff transport corruption and unsafe patch-mode use on unstable bodies"
      refs: ["appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-001", "appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-001", "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-003"]
      scores: {EVD: 5, IMP: 5, RSK: 5}

    - id: PW-BP-002
      practice: "Freeze objective, target, source authority, non-goals, output contract, and stop condition before serious prompt/workflow execution."
      context: ["file_producing_prompt", "research_producing_prompt", "patch_producing_prompt", "handoff_producing_prompt", "multi_source_or_long_context_task"]
      prevents: "scope drift, output-contract drift, and unstated success criteria"
      refs: ["appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-001", "appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-002", "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-a--scope-lock"]
      scores: {EVD: 5, IMP: 5, RSK: 2}

    - id: PW-BP-004
      practice: "Make source authority a pre-step gate and verification a post-step gate; do not trust output because it looks fluent."
      context: ["source_hierarchy_matters", "reusable_or_committed_outputs", "multiple_summaries_and_original_files_exist", "conflicting_primary_sources"]
      prevents: "fluent but unverified output and authority inversion"
      refs: ["appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-006", "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-b--source-authority-preflight", "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-d--verification-gate"]
      scores: {EVD: 5, IMP: 5, RSK: 3}

    - id: PW-BP-009
      practice: "Carry execution state as an explicit frame or state block; never rely on chat-history reconstruction for current task state."
      context: ["high_risk_promptflow_execution", "multi_chat_or_operator_mediated_task_sequence", "repo_writing_or_scaffold_update_workflow", "stale_missing_or_contradictory_prior_context_possible"]
      prevents: "implicit state reconstruction and stale-context continuation"
      refs: ["appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md", "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-01--implicit-chat-history-state-reconstruction", "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-02--stale-or-missing-state_block"]
      scores: {EVD: 5, IMP: 5, RSK: 3}

    - id: PW-BP-010
      practice: "Execute high-risk tasks through an atomic task packet: one task, one target, explicit input refs, repeated scope, and a gate check before write or synthesis."
      context: ["appendix_creation", "scaffold_update", "patch_or_file_write_task", "handoff_to_chat_executor_or_operator", "constrained_source_authority_or_target_root"]
      prevents: "compound task bleed, wrong-target writes, and pre-gate synthesis"
      refs: ["appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md", "appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md", "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-03--compound-task_payload-using-andthen", "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-05--directory-scan-without-explicit-input_refs"]
      scores: {EVD: 5, IMP: 5, RSK: 3}

    - id: PW-BP-011
      practice: "Treat HALT, CLARIFY, patch-check failure, split-required conditions, and unverified external model, API, browser, runtime, or platform claims as routing controls, not prose warnings."
      context: ["ambiguity_after_gate_check", "patch_dry_run_or_preimage_validation_fails", "split_required_to_avoid_summary_substitution", "external_model_API_browser_runtime_or_platform_claim_affects_doctrine", "closure_lacks_fetch_back_or_claim_status_proof"]
      prevents: "unsafe continuation after halt signals and warning-only routing"
      refs: ["appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md", "appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md", "appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md", "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-07--unsafe-continuation-after-halt-condition", "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-11--split-required-output-that-substitutes-summary", "appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-13--external-modelplatform-claim-promoted-as-accepted-doctrine"]
      scores: {EVD: 5, IMP: 5, RSK: 4}

  required_practices:
    - id: PW-BP-003
      practice: "Use bounded, stage-gated, artifact-centered execution instead of broad autonomy or giant multi-phase prompts."
      context: ["subscription_chat_execution", "low_context_agent_handoff", "documentation_or_architecture_work", "workflow_blends_research_writing_QA_packaging_finalization"]
      prevents: "multi-phase autonomy drift and summary substitution for artifacts"
      refs: ["appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-003", "appendices/APPENDIX_KB_CANDIDATE_LEDGER.md#pw-cand-003", "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-006"]
      scores: {EVD: 5, IMP: 5, RSK: 3}

    - id: PW-BP-005
      practice: "Detect out-of-mode improvements, but capture them explicitly instead of applying them silently."
      context: ["closed_execution_mode", "adjacent_improvement_detected_by_agent", "high_confidence_out_of_scope_improvement"]
      prevents: "silent scope expansion and unreviewed adjacent edits"
      refs: ["appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-008", "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-e--out-of-mode-capture"]
      scores: {EVD: 5, IMP: 4, RSK: 3}

    - id: PW-BP-006
      practice: "Use clean handoffs across chats, agents, or execution lanes: settled state, source priority, non-redo list, exact next job, risks, and success condition."
      context: ["new_chat_continuation", "codex_handoff", "multi_stage_research_to_patch_workflow", "saturated_or_overloaded_prior_thread"]
      prevents: "handoff state loss and redundant rework"
      refs: ["appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-010", "appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#safeguard-f--handoff-reset"]
      scores: {EVD: 4, IMP: 5, RSK: 2}

    - id: PW-BP-007
      practice: "Record durable QA, gap, and next-research results in a repo appendix when a KB build or improvement pass changes what future agents should rely on."
      context: ["KB_build_or_improvement_pass", "future_scaffold_promotion_candidates_identified", "verification_gap_or_next_research_would_remain_chat_only", "multiple_appendices_or_scaffolds_may_be_affected"]
      prevents: "loss of reusable QA findings and chat-only institutional memory"
      refs: ["appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#purpose", "appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#current-qa-status", "appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#next-patch-candidates"]
      scores: {EVD: 5, IMP: 5, RSK: 3}

  recommended_practices:
    - id: PW-BP-008
      practice: "Treat prompt and workflow examples as behavioral regression tests for this lane; check target, source, mode, validation, and stop discipline."
      context: ["prompt_or_promptflow_behavior_taught_reused_or_validated", "prior_scope_drift_noop_fragile_diff_or_out_of_mode_failure", "template_needs_before_after_evidence"]
      prevents: "example drift and untested promptflow regressions"
      refs: ["appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#f5-scaffold-promotion-matrix", "appendices/APPENDIX_KB_EXAMPLES.md#purpose", "appendices/APPENDIX_KB_EXAMPLES.md#regression-checklist"]
      scores: {EVD: 5, IMP: 5, RSK: 3}

appendix_refs:
  authority:
    source_manifest: appendices/APPENDIX_KB_SOURCE_MANIFEST.md
    ranking_ledger: appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
    source_conflicts: appendices/SOURCE_CONFLICT_REPORT.md
  evidence:
    anti_drift: appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
    examples: appendices/APPENDIX_KB_EXAMPLES.md
    regression_examples: appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md
  execution:
    execution_control_contracts: appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md
    patch_transport_protocols: appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md
    runtime_template_catalog: appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md
    external_claim_verification: appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md
  maintenance:
    qa_next_research: appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
    candidate_ledger: appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
    source_notes: appendices/APPENDIX_KB_SOURCE_NOTES.md
    constant_failure_process: appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md
    constant_failure_source_notes: appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md

promotion_boundary:
  add_or_revise_practices_only_after:
    - LEARNING_QUEUE.md routing
    - evidence_refs_exist
    - meta_ops_review
```
