---
okf: 0.2
type: continuation_handover
id: universal-ai-instruction-system-c01-correction-continuation
created: 2026-09-22
repository: leela-spec/apexai-os-meta
branch: main
base_verified: 97484ccf665c07c420dbc46f7200591eb228c99c
status: ready
---

# state

program_root:
  path: apex-meta/handoff/universal-ai-instruction-system/

live_authority:
  - README.md
  - 09-MODULE-DEEPENING-HANDOVER.md

verified_at_handover:
  main: 97484ccf665c07c420dbc46f7200591eb228c99c
  c01: DONE
  c02: NEXT
  c03: QUEUED

# operator_correction

problem:
  rejected_phrase: "smallest needed choice"
  reason: >
    Minimizing the operator interaction can cause an agent to compress away
    material dimensions of an operator-owned decision, creating drift from
    the actual intent.

replacement_principle:
  short: "Autonomy for delegated implementation decisions; fidelity for operator-owned decisions."
  semantic_rule: >
    Resolve delegated and evidence-determined trade-offs autonomously.
    When a material operator-owned choice remains, preserve the full
    intent-relevant decision surface. Do not reduce a material decision
    merely to minimize operator interaction.

approved_candidate_xml: |
  <decision when="a material operator-owned choice remains after available evidence is considered, or options are explicitly requested"
            principles="decision-analysis,trade-study,uncertainty-analysis">
    Resolve delegated and evidence-determined trade-offs autonomously. When a material operator-owned choice remains, preserve the full intent-relevant decision surface: compare viable alternatives against the decisive criteria, evidence, consequences, and uncertainty; recommend when justified, and surface the remaining choice clearly without hiding material trade-offs or inventing numerical precision.
  </decision>

# value_model

c01_purpose:
  - prevent_permission_loop:
      example: "Agent asks operator to choose between routine implementation details it should decide itself."
  - prevent_silent_intent_drift:
      example: "Agent chooses self-hosted vs SaaS, privacy vs convenience, or architecture coupling without surfacing the operator-owned trade-off."
  - prevent_choice_dumping:
      example: "Agent presents every technically possible tool instead of researching and pruning non-viable options."
  - prevent_pseudo_precision:
      example: "Agent invents 1-10 scores and arbitrary weights to manufacture a winner."
  - preserve_product_semantics:
      example: "Two technically valid implementations change user behavior; the agent must surface that product-level choice."
  - separate_fact_from_preference:
      example: "Agent researches externally knowable facts itself instead of asking the operator to decide them."

orchestration_user_stories:
  - id: US-C01-01
    context: routine_local_implementation
    expected: agent_decides_and_continues
    operator_interrupt: false
  - id: US-C01-02
    context: architecture_boundary_change
    expected: preserve_full_architecture_tradeoff_and_surface_operator_choice
    operator_interrupt: true
  - id: US-C01-03
    context: destructive_or_provenance_affecting_change
    expected: expose_reversibility_and_history_consequences_before_operator_choice
    operator_interrupt: true
  - id: US-C01-04
    context: external_fact_can_resolve_choice
    expected: research_fact_first_then_decide_if_operator_preference_no_longer_needed
    operator_interrupt: false_if_resolved
  - id: US-C01-05
    context: product_semantics_differ
    expected: surface_behavioral_difference_even_if_both_paths_pass_tests
    operator_interrupt: true
  - id: US-C01-06
    context: close_options_with_decision_changing_uncertainty
    expected: expose_uncertainty_and_do_not_manufacture_winner
    operator_interrupt: conditional

# pending_patch_packet

path:
  apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-22-c01-intent-surface-correction/

files:
  - README.md
  - P01-C01-result-preserve-full-decision-surface.patch.md
  - P02-pilot-C01-preserve-full-decision-surface.patch.md

mutation_rule:
  existing_files: exact_match_only
  whole_file_rewrite: forbidden
  reread_immediately_before_edit: required
  old_block_match_count: exactly_one
  diff_inspection_before_commit: required

# continuation_sequence

steps:
  - id: 1
    action: re_read_live_main
    files:
      - apex-meta/handoff/universal-ai-instruction-system/README.md
      - apex-meta/handoff/universal-ai-instruction-system/09-MODULE-DEEPENING-HANDOVER.md
      - apex-meta/handoff/universal-ai-instruction-system/patches/2026-09-22-c01-intent-surface-correction/README.md
    rule: live_README_overrides_handover_snapshot

  - id: 2
    action: apply_pending_C01_correction
    method: exact_match_patch_only
    patch_files:
      - P01-C01-result-preserve-full-decision-surface.patch.md
      - P02-pilot-C01-preserve-full-decision-surface.patch.md
    verify:
      - exact_match_once_per_replacement
      - no_unrelated_diff
      - C01_status_unchanged
      - C02_status_unchanged

  - id: 3
    action: commit_C01_correction
    branch: main
    atomic: true
    suggested_commit: "docs(agent-contract): preserve C01 operator decision surface"

  - id: 4
    action: re_read_live_README
    rule: >
      If main advanced or NEXT changed, trust the live README.
      Do not assume C02 merely because this handover says C02 was NEXT.

  - id: 5
    action: execute_exactly_one_live_NEXT_module
    governing_handover: 09-MODULE-DEEPENING-HANDOVER.md
    stop_after_commit: true

# preserved_boundaries

a13:
  preserve: >
    actual frame/problem/task/environment -> normal web search ->
    at least 3 verified-quality sources by default -> congruence check ->
    reason from evidence.
  expand_only_if:
    - task_or_environment_materially_complex
    - reliable_sources_materially_disagree

source_governed_execution_contract:
  file: 14-SOURCE-GOVERNED-EXECUTION-CONTRACT-CANDIDATE.md
  status: separate_later_synthesis_item
  absorb_into_c01_or_c02: false

graded_rigor:
  status: separate_cross_cutting_project_management_issue
  custom_levels_authorized: false

historical_research:
  authority: evidence_only
  current_authority: false

# stop_rule

after_next_module_commit:
  continue_to_following_module: false
  report:
    - correction_commit_sha
    - module_completed
    - final_module_wording
    - files_changed
    - module_commit_sha
    - next_live_NEXT
