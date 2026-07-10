# R03 — Independent Semantic Quality Gate

```yaml
research_report:
  id: R03
  title: independent_semantic_quality_gate
  repository: leela-spec/apexai-os-meta
  branch: main
  mode: bounded_read_only_research_with_report_write_only
  completed_at: 2026-07-10
  repository_content_modified: false
  report_artifact_added: true
```

## Verdict

```yaml
verdict:
  recommendation: adopt_limited_independent_semantic_gate
  minimum_gate: >
    A clean-context semantic evaluator must test declared target queries and
    verify two or three material claims against resolved source excerpts before
    Phase 2 pages can be promoted to query-ready. The evaluator may be the same
    model in a separate invocation, but it must not reuse the drafting context,
    drafting rationale, or self-reported completion evidence.
  mandatory_components:
    - deterministic_quality_report_must_pass_or_be_explicitly_bounded
    - query_based_blind_review
    - claim_to_source_entailment_review
    - evidence_cited_reason_coded_verdict
    - operator_escalation_for_material_disagreement_or_unresolvable_evidence
  not_required_by_default:
    - different_model_for_every_page
    - operator_review_of_every_page
    - numeric_page_quality_score
    - fixed_word_or_source_threshold
    - full_claim_verification_of_every_sentence
```

The smallest defensible gate is not a general second opinion and not another drafting pass. It is a bounded acceptance test over the actual intended outcome:

1. Can the page answer its declared target queries using only its content?
2. Are two or three material claims supported by the cited source passages?
3. Does the page preserve material uncertainty, contradiction, and scope limits?
4. Are routes and raw-source reopen triggers operationally useful rather than generic placeholders?

A page fails promotion when any material claim is unsupported, a cited pointer does not support the claim, the page cannot answer its declared core query, or the page conceals a material contradiction. Missing or inaccessible evidence yields `insufficient_evidence`, not a guessed pass or fail.

## Evidence Summary by File

| Repository file | Evidence class | Decisive finding |
|---|---|---|
| `log/max-run-20260709-phase2-quality-failure-root-cause.md` | observed failure | The run optimized for file existence, headings, and read-back. The quality command was not executed and its current heuristic cannot catch heading-complete thin pages. |
| `.claude/skills/apex-kb/SKILL.md` | active lifecycle contract | Phase 2 owns semantic synthesis and requires ranked sources, layered synthesis, claim pointers, routes, and uncertainty. Query-ready additionally requires deterministic postflight and quality/query checks. |
| `references/kb-contract.md` | active semantic contract | Depth and source breadth must adapt to page scope. Key claims require specific pointers, confidence, and labels. Macro/Meso/Micro must provide distinct levels of synthesis. |
| `templates/wiki-page-templates.md` | drafting template | Templates define useful content shapes but explicitly avoid fixed source counts and page scores. Template conformance is therefore necessary but not sufficient. |
| `references/ingest-query-lint-audit-rules.md` | operational boundary | Deterministic quality is intentionally structural and cannot grade semantic usefulness. Semantic flags include unsupported claims, missing pointers, contradictions, and source conflicts. |
| `outputs/queries/evals/query-eval-pack.json` | current query acceptance input | The pack exists but `queries` is empty. It cannot currently test query usefulness or route correctness. |
| `references/acceptance-tests.md` | executable fixture contract | Current fixtures test structure and behavior, but the example Phase 2 page contains placeholder synthesis and a placeholder pointer. Such a fixture can validate mechanics while teaching the wrong semantic success pattern. |

## Sampled Pages and Claim-Support Findings

### 1. Known thin but structurally complete page

```yaml
page: wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
category: observed_thin_structurally_complete
verdict: semantic_fail
```

Findings:

- The mechanism distinctions are broadly supported by the Phase 1 analysis: skills are repeatable procedures, hooks are event-triggered, subagents isolate context, plugins bundle components, and MCP connects external systems.
- The page’s central rule, “Choose the smallest Claude Code surface that satisfies the job,” is a reasonable synthesis but is not directly supported by its only claim pointer. It should be labeled as a design inference or policy, not a high-confidence source-backed claim.
- The Micro section does not contain micro-level evidence. It only states that queries should route to this page.
- Its one key claim compresses several dimensions—repeatability, enforcement, isolation, distribution, and connectivity—into a broad policy while citing only a file path, not the relevant claims or passages.
- The route is plausible but untested because the query-eval pack contains no queries.

Blocking reasons: macro/meso/micro do not provide distinct evidence value; material policy is mislabeled as source-backed; pointer specificity is insufficient for the breadth of the claim; page usefulness is too limited for its broad decision-model scope.

### 2. Strongest available summary candidate

```yaml
page: wiki/summaries/max-run-20260709/production-agent-readiness-and-risk-model.md
category: strongest_available_summary
verdict: semantic_partial
```

Findings:

- The claim that production rosters should stay small and explicit is supported by the cited Phase 1 source.
- The broader readiness model—clear task class, bounded tools, validation route, rollback/deprecation, and operator promotion—is not established by the cited claim source. It is a useful Apex policy synthesis but should be explicitly labeled as inference or operator doctrine.
- The ranked source set lists an official subagent source, but the key claim points only to the Phase 1 synthesis. The official source does not establish the Apex-specific production-promotion policy.
- The page can answer “When is an agent ready for production use?” at a high level, but does not explain how each criterion is verified or which failures block promotion.

Nonblocking strengths: clear query route; visible operator escalation; narrow claim count is acceptable only if the page scope is narrowed from “readiness model” to “roster and promotion principle.”

### 3. Strongest available concept candidate

```yaml
page: wiki/concepts/max-run-20260709/source-preserving-kb-compile.md
category: strongest_available_concept
verdict: semantic_partial
```

Findings:

- The canonical/derived distinction and the requirement that generated pages retain source pointers are directly supported by the KB contract and skill.
- The statement that source custody, semantic summaries, and rebuildable indexes are separate layers is supported.
- The Micro statement about the empty source-payload manifest is run-specific defect evidence, not a micro-level explanation of the concept. It also relies on a source not declared in `source_refs`.
- The page does not explain how source preservation is proven, how pointers are resolved, or what prevents derived artifacts from becoming authority. Therefore it only partially answers the likely target query.

Blocking issue for full pass: a material run-specific claim uses an undeclared source and the three synthesis layers are not distinct enough for a concept page of this scope.

### 4. Narrow entity or mechanism page

```yaml
page: wiki/entities/max-run-20260709/claude-code-subagents.md
category: narrow_entity_or_mechanism_page
verdict: semantic_partial
```

Findings:

- The official source supports that subagents are specialized assistants, run in separate context windows, can have custom prompts/tool access/permissions, and return summaries to preserve main-context space.
- The page’s core claim about side work in a separate context and returned summaries is supported.
- The listed use cases—research, exploration, planning, and complex multi-step work—are supported by the official documentation’s built-in-agent descriptions.
- “This KB treats subagents as bounded routing tools, not automatic persistent runtime truth” is Apex doctrine, not a claim from the official subagent source. It is useful, but mislabeled as a source-backed entity fact.

This is a valid concise-page candidate after relabeling the Apex-specific Micro statement as doctrine/inference and adding a passage-level pointer. It demonstrates why length or source count must not be a blocking metric by itself.

### 5. Page with explicit uncertainty

```yaml
page: wiki/summaries/max-run-20260709/failure-analysis-and-feedback-loop.md
category: page_with_explicit_uncertainty
verdict: semantic_partial
```

Findings:

- The Phase 1 analysis supports that the payload manifest was empty, that legacy artifacts predated the improved Phase 2 contract, and that deterministic quality should remain structural.
- The page’s central “layer collapse” diagnosis is plausible synthesis but is broader than the sole key claim and is not tied to specific evidence.
- The key claim that old outputs are comparison material is a run policy, not a factual conclusion entailed by the cited Phase 1 file.
- The uncertainty trigger is operationally useful, but its pointer to the lifecycle runbook is not declared in `source_refs` and the trigger is not attached to a specific unresolved claim.

The page preserves uncertainty visibly, which is positive, but still requires clearer separation of observed failure, inferred diagnosis, and operator policy.

## Semantic Failure Types the Gate Must Detect

```yaml
semantic_failure_taxonomy:
  grounding:
    - sources_listed_but_not_used
    - source_pointer_is_file_level_only_for_broad_claim
    - claim_pointer_does_not_entail_claim
    - source_not_declared_in_source_refs
    - broad_claim_based_on_narrow_source
    - inference_mislabeled_as_source_backed_fact
  usefulness:
    - page_cannot_answer_declared_target_query
    - routes_do_not_match_real_user_queries
    - page_repeats_titles_or_taxonomy_without_decision_value
    - accurate_but_query_useless
  synthesis:
    - macro_meso_micro_are_redundant
    - micro_section_contains_routing_or_policy_instead_of_specific_evidence
    - source_summaries_are_concatenated_without_cross_source_synthesis
    - excessive_detail_without_decision_or_query_value
  uncertainty:
    - contradictions_removed_or_hidden
    - confidence_exceeds_source_support
    - reopen_trigger_is_generic
    - uncertainty_pointer_does_not_identify_the_uncertain_claim
  evaluator_failure:
    - headings_present_equals_pass
    - source_refs_present_equals_grounded
    - long_page_equals_high_quality
    - evaluator_accepts_drafter_self_report
    - average_score_hides_one_critical_grounding_failure
```

## Relevant External Evidence and Limitations

| Evidence | Applicable finding | Limitation for Apex KB |
|---|---|---|
| G-Eval, arXiv:2303.16634 | Explicit criteria and form-filling can improve alignment with human judgments. | Reported summarization correlation is useful but not sufficient for source entailment; the paper also notes potential bias toward LLM-generated text. |
| Self-Preference Bias in LLM-as-a-Judge, arXiv:2410.21819 | Judges may prefer familiar or self-like outputs; same-model certification is not independent. | Bias magnitude depends on model/task; using a different model reduces correlation but does not guarantee correctness. |
| Judging the Judges, arXiv:2406.07791 | Position and presentation can alter LLM judgments. | Primarily pairwise evaluation; Apex should prefer direct evidence findings over pairwise page ranking. |
| Prometheus / Prometheus 2, arXiv:2310.08491 and 2405.01535 | Custom rubrics and reference materials materially improve evaluator reliability. | Benchmark agreement does not prove validity on Apex-specific source custody and query-usefulness criteria. |
| FActScore, arXiv:2305.14251 | Breaking long text into atomic facts and checking each against evidence is more diagnostic than a single holistic rating. | Full atomic verification is too costly for every page; Apex should sample two or three material claims and escalate when those fail. |
| QAFactEval, arXiv:2112.08542 | QA-based and entailment-based checks provide complementary factual-consistency signals. | Question generation and answerability components materially affect results; automatic QA is not a substitute for inspecting cited passages. |
| Data-QuestEval / QuestEval family, arXiv:2104.07555 | Querying source and generated text can test semantic coverage without a reference summary. | Domain adaptation and question quality are limitations; target queries should be operator- or Phase-1-derived, not generated solely by the evaluator. |

External research supports a hybrid gate: rubric-based direct judgment, query trials, and claim-level source verification. It does not support treating any single LLM verdict or numeric score as authoritative.

## Comparison of Feasible Evaluator Designs

| Design | Independence | Evidence quality | Cost | Gaming/bias risk | Recommendation |
|---|---:|---:|---:|---:|---|
| Same model, same context | very low | low | low | very high | Reject as certification. Useful only as drafting self-check. |
| Same model, clean context | medium-low | medium | low-medium | medium-high | Minimum default when provided resolved evidence and a fixed rubric. |
| Different model, clean context | medium | medium-high | medium | medium | Use for high-impact pages, disputed verdicts, or calibration samples. |
| Query-based blind evaluation | high for usefulness | high for route/coverage | medium | medium | Mandatory component once target queries exist. |
| Claim-to-source verification | high for grounding | high | medium | low-medium | Mandatory component; inspect two or three material claims per page. |
| Operator review | highest contextual authority | high when evidence is shown | high | human inconsistency | Escalation surface, not default review of every page. |

No evaluator is automatically independent merely because it is a second LLM. Independence increases when the evaluator has a clean context, does not see drafting rationale, receives fixed target queries and resolved evidence, and must produce pointer-backed findings.

## Recommended Minimum Gate

```yaml
minimum_semantic_gate:
  preconditions:
    - deterministic_quality_report_available
    - page_content_and_page_type_available
    - declared_scope_available
    - source_refs_resolved_or_marked_unresolvable
    - at_least_one_target_query_per_page
  review_steps:
    - step: blind_query_trial
      action: >
        Attempt the declared target queries using the page only. Record whether
        the page gives a correct, bounded, decision-useful answer and what
        essential evidence is missing.
    - step: material_claim_selection
      action: >
        Select two or three claims that carry the page's main conclusion,
        decision rule, or factual identity. Do not let the page nominate only
        its easiest claims.
    - step: source_entailment_check
      action: >
        Compare each selected claim with the resolved cited excerpt. Classify
        supported, partially supported, contradicted, or unresolvable.
    - step: synthesis_and_uncertainty_check
      action: >
        Verify that synthesis adds distinct value, preserves material limits,
        and does not relabel inference as source fact.
    - step: verdict
      action: >
        Produce pass, partial, fail, or insufficient_evidence with reason-coded,
        pointer-backed findings. No averaged quality score.
  evaluator_surface:
    default: same_model_clean_context_separate_invocation
    stronger_option: different_model_clean_context
    escalation: operator_review
```

### Required Evaluator Inputs

```yaml
required_inputs:
  - page_content
  - page_path
  - page_type
  - declared_scope
  - declared_target_queries
  - source_refs
  - resolved_source_excerpts_for_selected_claims
  - deterministic_quality_report
  - active_phase2_contract
  - evaluator_rubric_version
prohibited_inputs_by_default:
  - drafting_chain_of_thought
  - drafter_self_assessment
  - completion_claim
  - desired_verdict
  - page_length_target
```

## Verdict Definitions

```yaml
verdict_schema:
  semantic_pass:
    definition: >
      The page answers its core target queries, selected material claims are
      supported at the stated scope, inference is labeled, uncertainty is
      preserved, and no blocking defect is found.
  semantic_partial:
    definition: >
      The page is materially useful and mostly grounded, but has bounded repair
      needs that do not invalidate its core answer. It may remain draft or
      needs_review but must not be promoted as fully query-ready.
  semantic_fail:
    definition: >
      A blocking defect undermines the core answer, grounding, scope, or
      uncertainty handling.
  insufficient_evidence:
    definition: >
      Required sources or pointers cannot be resolved, so support cannot be
      judged. This blocks promotion but must not be reported as factual failure.
```

## Blocking Criteria

```yaml
blocking_criteria:
  - unsupported_or_contradicted_material_claim
  - cited_pointer_does_not_support_material_claim
  - page_cannot_answer_declared_primary_query
  - material_inference_presented_as_high_confidence_source_fact
  - broad_scope_not_supported_by_source_breadth
  - material_contradiction_or_uncertainty_hidden
  - route_claims_query_coverage_that_page_does_not_provide
  - source_required_for_core_claim_is_unresolvable
  - evaluator_finding_lacks_page_and_source_evidence
nonblocking_criteria:
  - concise_page_when_scope_is_narrow_and_complete
  - stylistic_or_elegance_preference
  - absence_of_line_numbers_when_source_format_cannot_supply_them
  - missing_optional_cross_links
  - additional_detail_that_would_not_change_query_answer_or_decision
```

## Required Evidence for Each Finding

```yaml
finding_contract:
  required_fields:
    - finding_id
    - criterion
    - verdict
    - page_pointer
    - source_pointer_when_applicable
    - reason
    - repair_action
    - confidence
    - evidence_status
  evidence_status_allowed:
    - resolved_and_supporting
    - resolved_and_partial
    - resolved_and_contradicting
    - unresolvable
    - not_applicable
  rule: >
    A blocking finding without a page pointer and, when applicable, a resolved
    source pointer is invalid and must not determine promotion.
```

## Anti-Gaming Checks

```yaml
anti_gaming_tests:
  - ignore_heading_presence_as_semantic_evidence
  - ignore_source_list_length_as_grounding_evidence
  - ignore_total_word_count_as_value_evidence
  - select_material_claims_independently_of_page_key_claim_list
  - test_at_least_one_query_not_copied_verbatim_from_routes_here
  - detect_policy_or_inference_labeled_source_backed_summary
  - check_whether_ranked_sources_are_used_in_claims_or_synthesis
  - check_whether_macro_meso_micro_could_be_reordered_without_information_loss
  - check_whether_reopen_trigger_names_a_real_uncertainty_and_evidence_path
  - prohibit_average_score_from_overriding_any_blocking_failure
  - repeat_pairwise_or_order_sensitive_tests_with_reversed_order_when_used
```

## Operator Escalation

```yaml
operator_escalation_required_when:
  - evaluator_and_drafter_disagree_on_a_material_claim
  - two_clean_context_evaluators_disagree_on_blocking_status
  - source_authority_is_ambiguous_or_conflicting
  - proposed_page_promotes_candidate_doctrine_to_runtime_policy
  - repair_would_change_operator_intent_or_scope
  - target_queries_are_missing_or_contested
  - source_cannot_be_resolved_but_page_is_needed_for_a_high_impact_decision
  - page_contains_security_permission_legal_or_other_high_stakes_runtime_guidance
```

## Lifecycle Integration Point

```yaml
lifecycle_integration:
  location: after_phase2_draft_and_deterministic_quality_before_query_ready_promotion
  sequence:
    - phase2_draft
    - deterministic_index_and_quality_checks
    - independent_semantic_gate
    - targeted_page_repair_if_partial_or_fail
    - rerun_deterministic_checks_for_changed_pages
    - semantic_recheck_only_for_repaired_blocking_findings
    - promote_to_query_ready
  completion_rules:
    compiled: semantic_pages_exist_but_may_be_unreviewed
    validated: deterministic_checks_pass_and_semantic_gate_has_no_fail
    query_ready: target_query_trials_pass_and_retrieval_is_fresh
```

The gate should not occur before deterministic checks: malformed pages, unresolved files, missing headings, stale indexes, and absent source references should be eliminated cheaply first. It must occur before query-ready promotion because structural validation cannot establish semantic value.

## Positive Exemplar Requirements

```yaml
positive_exemplar:
  scope:
    - states_what_question_the_page_answers
    - breadth_matches_available_sources
  grounding:
    - material_claims_have_resolvable_specific_pointers
    - source_rank_rationales_match_actual_use
    - inference_and_policy_are_labeled_as_such
  synthesis:
    - macro_states_cross_source_or_system_level_conclusion
    - meso_explains_patterns_relationships_or_decision_rules
    - micro_provides_concrete_evidence_or_mechanism_details
  usefulness:
    - answers_real_target_queries_without_raw_source_for_basic_use
    - routes_to_related_pages_or_raw_sources_when_limits_are_reached
  uncertainty:
    - exposes_material_gaps_contradictions_and_confidence_limits
    - reopen_triggers_identify_the_claim_source_and_decision_condition
  concision:
    - no_requirement_for_length_beyond_what_scope_and_evidence_need
```

## Structurally Complete Page That Must Still Fail

```yaml
failed_example_characteristics:
  headings_present: true
  source_refs_present: true
  ranked_sources_present: true
  macro_meso_micro_present: true
  key_claims_present: true
  routes_present: true
  uncertainty_present: true
  failure_reasons:
    - one_broad_claim_with_file_level_pointer
    - macro_meso_micro_are_one_sentence_and_redundant
    - micro_contains_routing_or_policy_not_evidence
    - ranked_sources_are_not_used_to_support_claims
    - page_cannot_answer_its_declared_decision_query
    - inference_is_labeled_as_source_backed_fact
    - uncertainty_trigger_is_generic_and_not_claim_specific
```

`claude-code-mechanism-decision-model.md` is the current concrete instance closest to this pattern.

## Unresolved Operator Decisions

```yaml
unresolved_operator_decisions:
  - decision: target_query_authority
    question: >
      Should target queries be authored during Phase 1, selected by the operator,
      or accepted from a populated query-eval pack?
  - decision: semantic_partial_promotion
    question: >
      May partial pages enter normal retrieval with `needs_review`, or must they
      be excluded from query-ready indexes?
  - decision: different_model_threshold
    question: >
      Which page classes require a different-model evaluator rather than a clean
      same-model invocation?
  - decision: calibration_set_ownership
    question: >
      Who approves the gold and structurally-complete-fail exemplars used to
      calibrate semantic review?
  - decision: source_pointer_minimum
    question: >
      When source formats lack stable lines, which section, heading, quote hash,
      or passage identifier is the minimum acceptable pointer?
```

## Final Recommendation

```yaml
final_recommendation:
  adopt: limited_independent_semantic_gate
  default_evaluator: same_model_clean_context_separate_invocation
  mandatory_methods:
    - query_based_blind_evaluation
    - two_or_three_material_claim_source_checks
    - reason_coded_pointer_backed_verdict
  stronger_review_when_needed:
    - different_model_clean_context
    - operator_review
  mandatory_before_next_phase2_query_ready_claim:
    - populate_target_queries
    - resolve_claim_evidence
    - run_deterministic_quality
    - run_independent_semantic_gate
    - repair_blocking_findings
  do_not_add:
    - universal_numeric_quality_score
    - universal_word_threshold
    - full_second_drafting_pass
    - mandatory_operator_review_of_every_page
    - assumption_that_different_model_equals_correct
    - headings_or_source_lists_as_acceptance_proof
```

The recommended gate is deliberately small. It samples material claims rather than re-verifying every sentence, tests actual queries rather than rewarding section completion, and escalates only ambiguous or high-impact cases. This directly addresses the observed proxy-substitution failure without turning semantic review into a second full compile or a new layer of process paralysis.
