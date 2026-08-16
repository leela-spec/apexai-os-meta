```okf
okf:
  id: "apex-gate-policy-skill-redesign-validation-handover-20260816"
  version: 1.0
  status: ready_for_independent_ai_validation
  document_role: next_ai_validation_and_skill_update_handover
  created: 2026-08-16
  repository: leela-spec/apexai-os-meta
  branch: main

operator_intent:
  primary_goal: >
    Independently validate, challenge, and improve the proposed Apex approval/gating
    redesign before modifying the Apex skills. The current workflow is intended to
    become an automation pipeline; operator approval must not become a routine blocker
    for low-level or already-authorized execution.
  explicit_direction:
    - move redundant Plan-to-Session confirmations toward one meaningful semantic authorization gate
    - make gating depend on the task/workflow risk and decision level
    - allow low-level approved work to continue without operator interruption
    - keep high-level, product-semantic, architectural, destructive, irreversible, or explicitly operator-flagged work gated
    - prefer exception-driven escalation over unconditional per-mutation confirmation
    - double-check this proposal independently; do not implement it merely because a prior AI recommended it

source_basis:
  required_current_sources:
    - path: .claude/skills/apex-plan/SKILL.md
      role: current_planning_and_operator_gate_contract
    - path: .claude/skills/apex-session/SKILL.md
      role: current_confirmed_mutation_and_session_contract
    - path: .claude/skills/apex-session/references/mutation-gate-rules.md
      role: current_before_after_and_operator_validation_rules
    - path: .claude/skills/Workflow&Processes/operator-validation-and-conflict-resolution.md
      role: wider_operator_validation_policy_if_still_current
    - path: apex-meta/handoff/weekly-project-management-next-steps-handover-20260816.okf.md
      role: current_real_pipeline_handover_that_exposed_the_double_gate
    - path: apex-meta/handoff/plan-packets/weekly-project-management-to-weekly-cycle-overview-20260816.okf.md
      role: end_to_end_pipeline_context
  operator_saved_project_source:
    status: repository_source_exists_per_operator_but_exact_path_not_confirmed_by_this_handover_author
    locate_by_content_phrases:
      - "one semantic approval gate"
      - "authorization envelope"
      - "The operator approves authority, not individual writes"
      - "default_gate: exception_only"
    rule: >
      Locate and read the operator-saved source in the repository before finalizing any
      redesign. If it conflicts with this handover summary, preserve the conflict and
      treat the operator-saved source as the fuller proposal basis rather than silently
      reconciling it.

current_problem:
  observed_pipeline:
    - Apex Plan creates proposal state
    - operator approves proposal for handoff
    - Apex Session requires an exact before/after preview
    - Session adaptation says earlier general approval cannot authorize the previewed writes
    - operator therefore must approve again before durable mutation
  automation_risk: >
    Requiring fresh approval for every consequential mutation or deterministic
    serialization can halt otherwise safe automated workflows whenever the operator is
    unavailable, even when the execution remains entirely inside an already-approved
    scope and semantics.
  retained_safety_value: >
    Human gates remain valuable when a task changes product meaning, architecture,
    durable entity meaning, resolves conflicts, merges uncertain entities, performs
    destructive or irreversible actions, exceeds the authorized scope, or is explicitly
    marked by the operator for review.

proposal_to_validate_not_assume:
  core_principle: >
    The operator approves an execution/authorization envelope. Work proceeds
    automatically inside that envelope. A new operator gate is raised only for an
    explicit manual task or when execution would leave the approved envelope.

  candidate_gate_levels:
    auto:
      meaning: >
        Execute and persist without further operator interruption while the work remains
        inside approved semantics and constraints.
      candidate_examples:
        - mechanical serialization of an already-approved plan into canonical files
        - deterministic index or registry maintenance under the correct authority
        - tests/build/lint and bounded fixes that do not alter approved semantics
        - implementation of an already-settled route or data contract
        - objective status propagation when definition-of-done evidence is complete

    exception_only:
      meaning: >
        Default automation mode: continue automatically unless a defined exception
        condition is detected.
      candidate_examples:
        - normal implementation tasks with settled product semantics
        - connecting an existing UI seam to an existing canonical contract
        - refactoring within explicit acceptance criteria

    manual:
      meaning: >
        Stop at the consequential decision/action and require explicit operator approval.
      candidate_examples:
        - unresolved product-semantic choice
        - architecture choice between materially different designs
        - destructive migration or deletion not explicitly pre-authorized
        - source-conflict resolution that changes canonical meaning
        - external irreversible action
        - any task or scope explicitly marked manual by the operator

  candidate_inheritance_rule: >
    Gate policy may be declared at portfolio/project/epic/workflow/task scope. Child work
    inherits the nearest explicit policy unless overridden by the operator or by a
    mandatory safety/risk rule.

  candidate_default:
    gate: exception_only
    rationale: >
      Preserve automation by default while retaining escalation for semantic drift,
      unresolved choices, destructive/irreversible actions, source conflicts that affect
      meaning, or scope expansion.

  candidate_stop_conditions:
    - explicit_task_gate_is_manual
    - semantic_delta_from_approved_intent
    - unresolved_operator_choice
    - source_conflict_that_changes_expected_behavior
    - destructive_state_change_not_pre_authorized
    - irreversible_external_action_not_pre_authorized
    - execution_exceeds_authorized_scope
    - acceptance_criteria_require_operator_judgment

  candidate_one_gate_flow:
    - Plan produces reviewable semantics, scope, constraints, and proposed gate policy
    - operator grants one scoped authorization
    - Session canonicalizes mechanically without a second confirmation when no semantic delta exists
    - Sync validates/recomputes automatically
    - eligible execution proceeds automatically
    - Session records evidence-backed state changes automatically when within authorization
    - exception conditions raise a new operator gate only when genuinely needed

validation_mission_for_next_ai:
  rule: >
    Do not start by editing skill files. First determine whether this model is actually
    the best minimal change for the existing Apex architecture.
  required_questions:
    - Is the double-gate diagnosis accurate under the complete current Apex Plan and Session contracts?
    - Which current confirmations protect real semantic decisions versus merely mechanical writes?
    - Can one scoped authorization safely replace repeated confirmations without weakening source preservation, conflict handling, or operator authority?
    - Should gate level be a first-class task field, an authorization record, workflow metadata, or a derived policy rather than stored on every task?
    - What is the minimum data model needed to represent authorization scope, intent, constraints, gate mode, and exceptions?
    - How should authorization inheritance and overrides work without creating hidden implicit authority?
    - Which status transitions can be objective/evidence-driven and automatic, and which still require judgment?
    - Which external actions must always remain gated regardless of inherited task policy?
    - How should expired/revoked authorization be represented?
    - How does this interact with Apex Sync, Weekly Orchestrator, FlowRecap, OpenClaw, and other execution actors?
    - Does the proposal create new failure modes such as stale authorization, scope creep, accidental inheritance, or ambiguous semantic-delta detection?
    - Can the same outcome be achieved with fewer concepts than auto/exception_only/manual plus authorization envelopes?

required_validation_examples:
  - scenario: approved_new_epic_serialization
    expected_analysis: >
      Determine whether Plan approval should authorize Session to create canonical epic/task
      files automatically when the generated files are semantically identical to the approved packet.

  - scenario: low_level_code_fix
    expected_analysis: >
      Test whether a bounded implementation such as wiring an existing route should run from
      plan through evidence/status update without an operator stop.

  - scenario: semantic_discovery_during_implementation
    expected_analysis: >
      Test escalation when implementation discovers the approved contract cannot represent
      required behavior without a product/domain change.

  - scenario: objective_done_transition
    expected_analysis: >
      Test automatic in-progress -> done when objective acceptance criteria and required
      evidence are satisfied.

  - scenario: subjective_done_transition
    expected_analysis: >
      Keep operator involvement when the definition of done explicitly requires operator
      judgment or acceptance.

  - scenario: destructive_or_external_action
    expected_analysis: >
      Determine which actions require unconditional or explicit pre-authorization even when
      the parent task otherwise runs automatically.

  - scenario: long_running_automation
    expected_analysis: >
      Verify that an approved multi-task workflow can progress through multiple low-level
      tasks, Session updates, and Sync recomputations without stopping merely because the
      operator is offline.

skill_update_scope_if_and_only_if_validation_supports_change:
  primary_candidates:
    - .claude/skills/apex-plan/SKILL.md
    - .claude/skills/apex-plan/references/* as required by actual contract structure
    - .claude/skills/apex-session/SKILL.md
    - .claude/skills/apex-session/references/mutation-gate-rules.md
    - .claude/skills/apex-session/references/* as required by actual contract structure
    - .claude/skills/Workflow&Processes/operator-validation-and-conflict-resolution.md if authoritative and affected
  inspect_for_cross_contract_effects_before_editing:
    - .claude/skills/apex-sync/
    - Weekly Orchestrator and PreCap contracts
    - FlowRecap / execution feedback contracts
    - any shared H1/H6 or PM/PD authority definitions referenced by Plan or Session
  boundary: >
    Do not broaden into unrelated skill redesign. Change only contracts needed to make the
    validated authorization/gating model coherent end-to-end.

required_output_before_implementation:
  - verified_current_gate_map
  - independent_critique_of_the_proposal
  - accepted_rejected_modified_parts_with_reasons
  - failure_mode_analysis
  - recommended_minimal_target_model
  - exact_skill_files_and_sections_that_require_change
  - compatibility_or_migration_notes_for_existing task/session records
  - test_scenarios_and_acceptance_criteria

implementation_rule:
  if_proposal_is_validated:
    - update the affected skill contracts consistently, not only one local rule
    - preserve explicit operator overrides
    - preserve source/conflict/duplicate safeguards
    - remove redundant blocking confirmations where a valid scoped authorization already covers the mutation
    - ensure exceptions create actionable operator gates rather than vague blockers
    - update examples/tests/contracts needed to prevent old double-gate behavior from reappearing
  if_proposal_needs_revision:
    - improve the model first
    - document why the original proposal was insufficient
    - implement only the improved validated model
  if_proposal_is_rejected:
    - do not force the redesign
    - document the evidence and retain the current contracts

validation_acceptance_criteria:
  - another AI can reproduce the current double-gate behavior from repository contracts
  - proposed changes distinguish semantic authority from mechanical persistence
  - normal low-level authorized workflows can continue without operator presence
  - explicit high-level/manual work still stops at the correct decision boundary
  - semantic drift and scope expansion cannot silently inherit authorization
  - destructive/irreversible cases have an explicit policy
  - operator can explicitly set or override gating level
  - status automation is evidence-based rather than blanket-authorized
  - Plan/Session/Sync authority boundaries remain coherent
  - no duplicate approval is required when an exact mutation is merely deterministic serialization of already-approved semantics, unless the validated model finds a concrete reason otherwise

next_ai_execution_sequence:
  - read this handover
  - locate and read the operator-saved project source containing the full gate-policy proposal
  - read current Apex Plan and Apex Session skills plus mutation-gate rules fully
  - inspect shared operator-validation policy and directly affected cross-contracts
  - independently validate and pressure-test the proposal using the required scenarios
  - produce the minimal improved target design
  - only then edit affected skill files if supported by evidence
  - validate consistency across all edited contracts
  - save a concise implementation/validation report and next-session handover

operator_gate_for_this_handover:
  status: proposal_for_independent_validation_not_preapproved_implementation
  important_rule: >
    The operator asked for another AI to double-check, validate, and improve this proposal.
    Therefore this handover is authority to investigate and propose/implement only after
    that independent validation supports the changes; do not treat the prior AI proposal
    as unquestionable design truth.

success_definition:
  primary: >
    Produce an evidence-backed, simpler gating architecture that preserves meaningful
    operator control while allowing Apex to function as a real automation pipeline.
  failure_to_avoid: >
    Replacing one overengineered approval mechanism with a more complicated policy layer
    that still interrupts routine execution or creates ambiguous hidden authority.
```
