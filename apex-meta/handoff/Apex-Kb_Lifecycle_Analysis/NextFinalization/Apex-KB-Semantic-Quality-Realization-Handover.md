# Handover — Apex KB Semantic Quality Realization

## 0. Purpose

This handover defines the next repair wave required to make Apex KB reliably produce **high-quality LLM-owned Phase 1 and Phase 2 artifacts**, rather than structurally complete but semantically thin files.

This is a design and execution handover for another chat or executor. It is not a claim that the repair has already been implemented.

The next executor must use the live repository as authority, not chat memory.

```yaml
repo: leela-spec/apexai-os-meta
branch: main
primary_skill: .claude/skills/apex-kb/
primary_kb_under_review: apex-meta/kb/claude-code-orchestration-design/
current_problem: semantic_compile_can_satisfy_structure_while_missing_knowledge_value
required_outcome: high_quality_source_grounded_query_useful_phase1_and_phase2_files
```

---

## 1. Correct current-state verdict

The previous max-run must be described precisely:

```yaml
current_max_run:
  phase1_and_phase2_files_created: true
  requested_file_inventory_largely_present: true
  structural_phase2_headings_largely_present: true
  intended_semantic_quality_met: false_or_unproven
  deterministic_postflight_completed: false
  query_ready_promotion_allowed: false
```

The missing deterministic postflight and the semantic quality failure are separate facts:

- Missing postflight means the generated corpus was not deterministically validated, indexed, and checked after writes.
- Semantic quality failure means the LLM-authored pages were too compressed, weakly synthesized, and insufficiently useful even before postflight.

Do not collapse these two layers again.

Primary prior reports:

- `apex-meta/kb/claude-code-orchestration-design/log/max-run-20260709-execution-audit.md`
- `apex-meta/kb/claude-code-orchestration-design/log/max-run-20260709-phase2-quality-failure-root-cause.md`

---

## 2. Root failure to repair

The real target was:

> Produce source-grounded Phase 1 analyses and Phase 2 pages that deserve to be used as knowledge-base answer sources.

Execution substituted easier proxy targets:

```yaml
proxy_substitution:
  intended_target:
    - semantic_depth
    - source_use
    - synthesis_quality
    - query_usefulness
    - uncertainty_preservation
  substituted_proxies:
    - files_exist
    - commits_succeeded
    - required_headings_present
    - source_refs_field_present
    - representative_readback_succeeded
    - output_inventory_complete
```

Those proxies remain useful diagnostics, but none is sufficient for semantic success.

The repair must therefore place the intended outcome directly in the critical path. The core acceptance question is:

```yaml
semantic_acceptance_question:
  question: "Does this artifact deserve to be used as a KB evidence and answer source?"
  allowed_answers: [pass, repair_required, blocked_by_source_gap]
```

---

## 3. Why the process must be restructured

### 3.1 Long context degrades target adherence

Research shows that declared context capacity is not equivalent to reliable context use.

- Liu et al., **Lost in the Middle: How Language Models Use Long Contexts**: model performance depends strongly on where relevant information occurs, with significant degradation for information in the middle of long contexts.  
  https://arxiv.org/abs/2307.03172
- Hsieh et al., **RULER: What's the Real Context Size of Your Long-Context Language Models?**: models that perform well on simple retrieval often degrade sharply as context length and task complexity increase; advertised window size overstates effective working context.  
  https://arxiv.org/abs/2404.06654
- Hsieh et al., **Found in the Middle**: identifies intrinsic positional attention bias and shows that context position can distort relevance use.  
  https://arxiv.org/abs/2406.16008

Operational implication:

```yaml
long_context_policy:
  do_not:
    - place_the_whole_project_history_in_every_semantic_compile
    - rely_on_repeated_reminders_inside_one_ever_growing_chat
    - assume_all_prior_constraints_remain_equally_salient
  instead:
    - use_short_phase_specific_context_capsules
    - place_the_goal_and_acceptance_gate_at_both_start_and_end
    - pass_forward_only_verified_outputs_and_required_evidence
    - start_a_fresh_execution_context_for_phase2
```

### 3.2 Multi-step instruction compliance is brittle

Instruction-following research distinguishes objectively verifiable constraints from broader semantic intent.

- Zhou et al., **Instruction-Following Evaluation for Large Language Models (IFEval)**: reliable evaluation requires explicit, reproducible instruction checks; even these are limited to verifiable constraints.  
  https://arxiv.org/abs/2311.07911
- Pyatkin et al., **Generalizing Verifiable Instruction Following**: strong models still struggle to generalize to unseen instruction constraints, supporting narrower tasks and explicit verification rather than large bundles of instructions.  
  https://arxiv.org/abs/2507.02833

Operational implication:

- Do not assign source reading, corpus analysis, taxonomy planning, page drafting, quality judgment, repair, indexing, and final approval as one uninterrupted instruction bundle.
- Keep deterministic constraints machine-verifiable.
- Keep semantic quality criteria explicit and independently reviewed.
- Separate creator and acceptor roles, even when the same model family is used.

### 3.3 Proxy objectives can outperform the intended goal

- Çağatan and Zhao, **Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds**: language agents can optimize observed rewards while underperforming on hidden intended objectives; stronger optimization can widen the observed-versus-intended gap.  
  https://arxiv.org/abs/2606.15385
- Shah et al., **Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals**: systems can competently pursue an unintended goal that matches training or evaluation conditions but fails the real objective.  
  https://arxiv.org/abs/2210.01790

Operational implication:

```yaml
anti_proxy_rule:
  forbidden_completion_basis:
    - file_count
    - heading_count
    - commit_count
    - frontmatter_presence
    - source_ref_presence_without_source_use
  required_completion_basis:
    - page_answers_real_target_queries
    - claims_are_specific_and_supported
    - source_evidence_is_used_in_reasoning
    - synthesis_adds_value_beyond_source_listing
    - uncertainty_and_contradictions_are_preserved
```

### 3.4 Semantic evaluation itself can be biased

- Tripathi et al., **Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation**: evaluation protocol affects reliability; pairwise judgments can be distracted by spurious features, while absolute scoring was more robust in their experiments.  
  https://arxiv.org/abs/2504.14716

Operational implication:

- Do not ask a reviewer only whether a new page is “better than” the old page.
- Require criterion-by-criterion absolute judgments with evidence.
- Require explicit fail reasons and repair instructions.
- Do not use one aggregate “page value score” as the sole promotion gate.

---

## 4. Required lifecycle restructuring

The semantic compile must no longer be one continuous Phase 1-to-Phase 2 context by default for non-trivial corpora.

Use five bounded execution stages:

```yaml
semantic_realization_flow:
  stage_0_contract_and_evidence_packet:
    owner: deterministic_or_operator
    output: run_contract_and_bounded_source_packet

  stage_1_phase1_analysis:
    owner: llm_semantic_analyst
    output: source_grounded_phase1_files

  stage_1_acceptance:
    owner: independent_semantic_reviewer
    output: pass_or_repair_packet

  stage_2_phase2_compile:
    owner: fresh_context_llm_compiler
    input: accepted_phase1_plus_compact_contract_plus_examples
    output: compiled_wiki_pages

  stage_2_acceptance:
    owner: independent_semantic_reviewer
    output: per_page_pass_repair_or_blocked

  stage_3_deterministic_postflight:
    owner: terminal_executor
    output: index_retrieval_lint_audit_status_quality_results
```

### 4.1 Fresh-context rule

Phase 2 must start in a fresh chat or fresh execution context for medium or large compiles.

Phase 2 receives only:

1. The one-sentence outcome target.
2. The Phase 2 contract.
3. Accepted Phase 1 artifacts.
4. The exact page plan.
5. One positive exemplar.
6. One negative exemplar.
7. The semantic acceptance rubric.
8. The exact writable paths and stop conditions.

It must not receive the full historical discussion unless a specific unresolved decision requires it.

### 4.2 Iteration rule

Iteration is retained, but the unit of iteration changes.

Bad iteration:

```yaml
bad_iteration:
  pattern: keep_adding_instructions_to_one_long_chat
  consequence: context_growth_salience_loss_proxy_substitution
```

Required iteration:

```yaml
bounded_iteration:
  loop:
    - create_small_batch
    - independently_review_each_artifact
    - produce_machine_readable_repair_packet
    - repair_only_failed_criteria
    - re_review
  batch_size:
    phase1: one_source_cluster_or_one_analysis_file
    phase2: one_to_three_related_pages
```

No full-corpus Phase 2 generation may occur before a pilot batch passes.

---

## 5. Stage 0 — Run contract and context capsule

Every semantic run must begin with a compact immutable run contract.

```yaml
semantic_run_contract:
  run_id: required
  kb_root: required
  semantic_goal: "Create source-grounded, query-useful knowledge artifacts."
  selected_sources: exact_paths_or_source_ids
  output_paths: exact_paths
  phase: phase1_or_phase2
  source_authority_order: explicit
  target_queries: required
  non_goals: explicit
  positive_exemplar: exact_path
  negative_exemplar: exact_path
  acceptance_rubric: exact_path
  creator_may_self_approve: false
  completion_requires_semantic_acceptance: true
  deterministic_postflight_is_separate: true
```

The contract must fit on one screen where possible. Detailed doctrine remains linked, not duplicated.

---

## 6. Stage 1 — Phase 1 analysis protocol

### 6.1 Phase 1 goal

Phase 1 exists to create an evidence-backed semantic model of the source material before page drafting.

It is not a file inventory and not a generic summary exercise.

### 6.2 Required Phase 1 artifact contents

Each Phase 1 analysis must include:

```yaml
phase1_required_value:
  source_identity:
    - exact_source_ids_and_paths
    - authority_level
    - source_scope
  source_summary:
    - central_thesis_or_function
    - important_boundaries
    - implementation_or_operational_implications
  evidence_inventory:
    - definitions
    - mechanisms
    - processes
    - decisions
    - constraints
    - failure_modes
    - contradictions
    - uncertainties
  claim_ledger:
    - claim_id
    - claim
    - source_pointer
    - confidence
    - claim_label
  proposed_pages:
    - page_path
    - page_purpose
    - target_queries
    - evidence_set
    - why_page_is_needed
  exclusions:
    - material_not_promoted
    - reason
```

### 6.3 Phase 1 acceptance gate

Phase 1 passes only when:

- Claims are specific enough to be checked.
- Material conclusions have source pointers.
- Proposed pages map to actual operator or retrieval queries.
- Contradictions and source limitations remain visible.
- The analysis distinguishes source content from inference.
- The proposed page set is neither an arbitrary file-count target nor an exhaustive restatement of every source heading.

Phase 1 must fail when it is primarily a generic prose summary, an inventory of headings, or a page-name brainstorm without evidence mapping.

---

## 7. Stage 2 — Phase 2 compile protocol

### 7.1 Phase 2 goal

Each Phase 2 page must be the smallest sufficient durable artifact that answers its target queries from a source-grounded synthesis.

The goal is not to fill a template. The template is only a support structure.

### 7.2 Page-level work order

For each page, the compiler must perform this sequence:

1. Restate the page purpose in one sentence.
2. List the target queries the page must answer.
3. Select the minimal sufficient evidence set from accepted Phase 1.
4. Draft the claims before drafting the narrative.
5. Draft Macro/Meso/Micro synthesis around those claims.
6. Add routes and raw-source reopen triggers.
7. Run a self-check against the negative exemplar.
8. Write the page.
9. Mark it `pending_semantic_acceptance`, not complete.

### 7.3 No fixed word quota as the goal

Word counts may be used as weak shell detectors, not as semantic success criteria.

A concise page can pass when the topic is narrow and the page fully answers its queries. A long page must fail when it is repetitive, unsupported, or does not improve retrieval value.

---

## 8. Positive exemplar specification

Create a repository exemplar at a later implementation stage, preferably under:

```text
.claude/skills/apex-kb/examples/semantic-quality/phase2-positive-example.md
```

The positive exemplar must demonstrate:

```yaml
positive_exemplar:
  purpose:
    - show_actual_quality_not_just_structure
    - demonstrate_adaptive_depth
  required_characteristics:
    - explicit_target_queries
    - ranked_sources_with_reason_for_use
    - several_specific_claims_when_scope_requires_them
    - span_or_line_specific_pointers_where_available
    - macro_synthesis_that_explains_the_whole
    - meso_synthesis_that_explains_relationships_and_tensions
    - micro_details_that_support_action_or_verification
    - routes_that_help_retrieval
    - uncertainty_and_reopen_conditions
  annotations:
    - why_each_section_is_sufficient
    - what_would_make_it_fail
```

The exemplar must not become a fixed length template. It should explicitly state which aspects are adaptive.

---

## 9. Negative exemplar specification

Create a repository counterexample at a later implementation stage, preferably under:

```text
.claude/skills/apex-kb/examples/semantic-quality/phase2-negative-example.md
```

The negative exemplar must intentionally include all structural headings while still failing:

```yaml
negative_exemplar:
  headings_present: true
  frontmatter_present: true
  source_refs_present: true
  failure_patterns:
    - one_sentence_macro
    - one_sentence_meso
    - generic_micro
    - one_broad_claim
    - file_level_pointer_only
    - sources_named_but_not_used
    - routes_repeat_page_title
    - empty_uncertainty_without_justification
    - no_target_query_answered_completely
  required_annotation:
    verdict: fail
    reason: "Structural completeness is not semantic sufficiency."
```

This counterexample is critical because deterministic structural checks alone cannot teach or enforce the intended semantic boundary.

---

## 10. Mandatory semantic acceptance gate

### 10.1 Separation of roles

```yaml
semantic_roles:
  creator:
    may_draft: true
    may_self_check: true
    may_final_approve: false
  reviewer:
    must_read_artifact: true
    must_read_target_queries: true
    must_check_evidence_pointers: true
    must_return_criterion_level_verdicts: true
  operator:
    resolves_policy_or_scope_disputes: true
```

A separate model invocation is sufficient for reviewer separation when an independent human review is not practical, but it must use a fresh context and the fixed rubric.

### 10.2 Rubric

Each Phase 1 or Phase 2 artifact receives absolute criterion judgments:

```yaml
semantic_acceptance_rubric:
  source_grounding:
    pass_when: material_claims_are_supported_and_sources_are_actually_used
  claim_specificity:
    pass_when: claims_are_concrete_falsifiable_or_operationally_precise
  synthesis_value:
    pass_when: artifact_adds_relationships_patterns_or_decisions_beyond_source_listing
  query_coverage:
    pass_when: target_queries_can_be_answered_from_the_artifact_and_pointers
  uncertainty_integrity:
    pass_when: gaps_conflicts_and_reopen_triggers_are_visible
  scope_discipline:
    pass_when: artifact_is_smallest_sufficient_without_being_thin
  routing_value:
    pass_when: routes_help_a_future_retriever_find_or_escalate_evidence
```

Allowed criterion verdicts:

- `pass`
- `repair_required`
- `blocked_by_source_gap`
- `not_applicable_with_reason`

Overall pass requires all applicable criteria to pass.

### 10.3 Required review packet

```yaml
semantic_review_packet:
  artifact_path: required
  target_queries: required
  overall_verdict: pass_or_repair_required_or_blocked
  criteria:
    source_grounding:
      verdict: required
      evidence: required
    claim_specificity:
      verdict: required
      evidence: required
    synthesis_value:
      verdict: required
      evidence: required
    query_coverage:
      verdict: required
      evidence: required
    uncertainty_integrity:
      verdict: required
      evidence: required
    scope_discipline:
      verdict: required
      evidence: required
    routing_value:
      verdict: required
      evidence: required
  repair_instructions:
    - exact_section
    - exact_defect
    - required_change
  reviewer_may_not_rewrite_during_review: true
```

The reviewer must not silently repair the page while judging it. Review and repair remain separate steps so defects remain observable.

---

## 11. Pilot-first promotion protocol

Before a full compile:

```yaml
pilot_gate:
  phase1_pilot:
    artifact_count: 1
    must_pass_before_more_phase1: true
  phase2_pilot:
    artifact_count: 1
    page_type: summary_or_concept
    must_pass_before_batch_compile: true
  batch_after_pilot:
    max_related_pages: 3
    independent_review_required: true
```

A failed pilot triggers protocol repair before corpus-scale generation. It must not trigger a larger instruction bundle or more pages.

---

## 12. Status vocabulary

Use statuses that prevent false completion claims:

```yaml
semantic_statuses:
  phase1_draft: written_not_reviewed
  phase1_repair_required: reviewed_and_failed
  phase1_accepted: semantic_gate_passed
  phase2_draft: written_not_reviewed
  phase2_repair_required: reviewed_and_failed
  phase2_accepted: semantic_gate_passed
  compiled_unvalidated: semantic_gate_passed_postflight_not_run
  query_ready: semantic_gate_passed_and_deterministic_postflight_passed
```

Forbidden status collapse:

```yaml
forbidden:
  - calling_files_created_completed
  - calling_headings_present_quality_pass
  - calling_connector_readback_validation
  - calling_semantic_acceptance_query_ready_without_postflight
```

---

## 13. Required repository changes for the next executor to design

The next chat should produce an implementation patch plan for the following likely targets after inspecting live main:

```yaml
candidate_targets:
  - path: .claude/skills/apex-kb/SKILL.md
    change: split_nontrivial_phase1_and_phase2_semantic_execution_and_add_acceptance_statuses

  - path: .claude/skills/apex-kb/references/kb-contract.md
    change: define_semantic_acceptance_contract_and_status_boundary

  - path: .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
    change: define_phase_specific_context_capsules_pilot_batches_and_repair_loop

  - path: .claude/skills/apex-kb/references/lifecycle-state-machine.md
    change: add_phase1_acceptance_and_phase2_acceptance_states

  - path: .claude/skills/apex-kb/references/acceptance-tests.md
    change: add_semantic_fixture_review_protocol_separate_from_deterministic_tests

  - path: .claude/skills/apex-kb/templates/ingest-analysis-template.md
    change: make_target_queries_claim_ledger_evidence_mapping_and_exclusions_explicit

  - path: .claude/skills/apex-kb/templates/wiki-page-templates.md
    change: make_page_purpose_target_queries_and_pending_acceptance_explicit

  - path: .claude/skills/apex-kb/examples/semantic-quality/phase1-positive-example.md
    change: create

  - path: .claude/skills/apex-kb/examples/semantic-quality/phase1-negative-example.md
    change: create

  - path: .claude/skills/apex-kb/examples/semantic-quality/phase2-positive-example.md
    change: create

  - path: .claude/skills/apex-kb/examples/semantic-quality/phase2-negative-example.md
    change: create

  - path: .claude/skills/apex-kb/references/semantic-acceptance-contract.md
    change: create_if_a_dedicated_contract_is_cleaner_than_overloading_existing_files

  - path: .claude/skills/apex-kb/package-manifest.md
    change: list_any_new_reference_and_example_files
```

These are candidate paths, not pre-approved edits. The next executor must inspect current live files and produce the smallest coherent target set.

The deterministic `quality` command remains structural and non-semantic. Do not convert `apex_kb.py` into an LLM judge. It may expose stronger objective diagnostics, but semantic acceptance belongs to the LLM/operator workflow.

---

## 14. Required design decisions for the next chat

The next chat must resolve and document:

1. Whether Phase 1 acceptance is per analysis file or per source cluster.
2. Whether Phase 2 acceptance packets live under `audit/`, `log/`, or a new canonical semantic-review path.
3. Whether accepted status is stored in page frontmatter, review packets, or both.
4. How a fresh reviewer receives source evidence without inheriting the creator's full context.
5. How target queries are selected and frozen before drafting.
6. Whether a page blocked by missing evidence remains a draft, becomes an audit item, or is not created.
7. How existing thin pages are routed into a repair backlog without blind mass rewriting.
8. How positive examples remain adaptive rather than becoming new rigid proxies.

---

## 15. Non-goals

This repair must not:

- Add a subjective `page_value_score` to deterministic Python.
- Replace semantic judgment with minimum word counts.
- Require a fixed number of sources or claims for every page.
- Rebuild the entire Apex KB lifecycle.
- Merge deterministic postflight with semantic acceptance.
- Treat an LLM reviewer verdict as infallible.
- Run full-corpus regeneration before the pilot passes.
- Use the old max-run pages as positive examples.

---

## 16. Next-chat mission

Use the live repository and this handover to design a precise, minimal patch plan that realizes the semantic-quality process.

The next chat must:

1. Read this handover and the two prior max-run audit reports.
2. Inspect the live Apex KB skill, contracts, templates, lifecycle state machine, examples, and package manifest.
3. Verify which candidate target files are actually required.
4. Produce positive and negative exemplar specifications based on real source material.
5. Define the Phase 1 and Phase 2 semantic acceptance gates and review packet location.
6. Define fresh-context handoffs and bounded batch sizes.
7. Preserve deterministic/semantic ownership separation.
8. Produce an exact implementation plan and execution order.
9. Do not patch until the operator approves the plan.

The mission sentence is:

> Make high-quality semantic artifacts the directly enforced product of the Apex KB lifecycle, with structure and deterministic checks serving that goal rather than replacing it.

---

## 17. Completion criteria for this repair wave

The repair wave is complete only when all of the following are true:

```yaml
completion_criteria:
  - phase1_and_phase2_are_separate_bounded_semantic_executions_for_nontrivial_runs
  - positive_and_negative_examples_exist_and_are_referenced_by_the_workflow
  - semantic_acceptance_is_mandatory_before_semantic_completion
  - creator_cannot_final_approve_own_artifact
  - pilot_must_pass_before_batch_generation
  - target_queries_are_frozen_before_drafting
  - review_packets_record_criterion_level_evidence_and_repairs
  - status_vocabulary_distinguishes_created_accepted_and_query_ready
  - deterministic_postflight_remains_separate_and_required_for_query_ready
  - no_success_claim_can_be_based_only_on_files_headings_or_commits
```
