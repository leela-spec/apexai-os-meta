# apex_plan_packet — orchestrator-regression-suite

```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: apex_plan_packet
  gate: none
  packet_id: "apex_plan_packet-20260712-orchestrator-regression-suite"
  produced_by: apex-plan-ops
  accountability: meta_ops
  lifecycle_stage: proposal
  status: complete
  target_surface: none
  next_state: "Project orchestrator-regression-suite is captured with an epic proposal and 5 proposed task records ready for operator review; on approval, confirmed writes create apex-meta/epics/orchestrator-regression-suite/."
  prerequisites: []
  expected_action: "operator reviews packet; on approval main thread routes handoff_requests to apex-sync-ops (validation/computation) and applies confirmed writes itself"
  sources:
    - apex-meta/fable-orchestrator/build-plan.md
    - apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md
    - .claude/skills/weekly-orchestrator/references/handoff-schema.md
  uncertainties:
    - "apex-meta/registry/index.md does not exist — current task-id space could not be read; ids proposed here start at 1 within the new epic folder."
    - "T3 (sync reports) and T4 (plan packet) behavioral tests are named in the dispatch but only T1 and T2 have recorded results in 03-execution-trace-verification.md; their canonical dispatch definitions must be confirmed before fixtures are authored."
  unresolved_risk: "If T3/T4 test definitions live only in chat history rather than repo files, task 2 fixtures may encode an unverified baseline."
  stop_condition: "Halt if the operator rejects the project capture, or if confirmed write is requested before operator_validation: confirmed."
  authority:
    state: candidate
    basis_digest: null
    verification_ref: null
  operator_validation: not_requested
```

## plan_packet_metadata

```yaml
plan_packet_metadata:
  package_name: apex-plan
  produced_by: apex-plan-ops
  run_date: "2026-07-12"
  planning_status: operator_review_needed
  source_summary: >
    Operator planning request (weekly-orchestrator dispatch, behavioral test T4): capture project
    "orchestrator-regression-suite" — a repeatable regression checklist that re-runs the weekly-loop
    behavioral tests (T1 evidence-normalize, T2 precap-week, T3 sync reports, T4 plan packet) whenever
    agents, skills, or the handoff schema change. Grounded in the regression goal of
    apex-meta/fable-orchestrator/build-plan.md and the executed-test record in
    apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md.
```

## project_capture_record

```yaml
project_capture_record:
  project_name: orchestrator-regression-suite
  goal: >
    A repeatable regression checklist that re-runs the weekly-loop behavioral tests
    (T1 apex-evidence-normalize, T2 apex-precap-week, T3 apex-sync-ops sync reports,
    T4 apex-plan-ops plan packet) whenever agents/, skills/, or the handoff schema change,
    producing honest pass/partial/fail records per the build-plan simulation definition.
  scope:
    in:
      - test inventory and pass criteria for T1-T4
      - reusable dispatch fixtures with expected envelope/behavior assertions
      - change-trigger map (which file changes require which tests)
      - baseline execution run with recorded results
      - operator runbook for re-running the suite
    out:
      - automated scheduling or cron triggers (forbidden by CLAUDE.md constraints)
      - CI tooling or scripts (regression runs are agent-dispatched, operator-triggered)
      - full user-story regression from APEX_Orchestration_User_Stories (separate, larger goal in build-plan.md)
  constraints:
    - "Runs are operator-triggered only; no auto-trigger."
    - "Test artifacts are written to normal artifact families and removed or marked as test artifacts after recording, matching T1/T2 precedent."
    - "Records follow the build-plan simulation_definition minimum record shape: story, actual steps, actual result, verdict with reason."
  source:
    - "operator dispatch prompt (run_date 20260712)"
    - apex-meta/fable-orchestrator/build-plan.md
    - apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md
  review_flags:
    - operator_review_needed
```

## epic_record

```yaml
epic_record:
  proposed_home: "apex-meta/epics/orchestrator-regression-suite/"
  slug: orchestrator-regression-suite
  title: "Orchestrator Regression Suite"
  goal: "Repeatable, operator-triggered regression checklist re-running behavioral tests T1-T4 on any agent/skill/schema change."
  status: open
  unresolved_scope_decisions:
    - "Where regression run records live: apex-meta/fable-orchestrator/simulations/ (build-plan says not yet created) vs. a suite-local folder — operator decision needed."
    - "Whether T3/T4 baseline results should be recorded into 03-execution-trace-verification.md (section 5) or a new record file."
  note: "Proposed only — no durable file created; apex-session owns the confirmed write."
```

## proposed_task_records

```yaml
proposed_task_records:
  - id: 1
    title: "Define regression checklist spec (test inventory T1-T4, pass criteria, record shape)"
    status: open
    priority: high
    due_date: null
    depends_on: []
    blocked_by: []
    acceptance_criteria:
      - "One spec file lists all four tests with, per test: target agent, dispatch inputs, expected envelope fields, expected behavioral assertions, and pass/partial/fail criteria."
      - "Record shape matches build-plan.md simulation_definition.minimum_record_shape."
      - "T1 and T2 entries are reconciled against the executed results in 03-execution-trace-verification.md section 5."
    definition_of_done:
      - "Spec reviewed and approved by operator."
      - "T3 and T4 definitions confirmed against their agent contracts (.claude/agents/apex-sync-ops.md, .claude/agents/apex-plan-ops.md) rather than chat memory."
    notes:
      - "This spec is the single source the fixtures (task 2) and trigger map (task 3) both consume."
    source:
      - apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md
      - "operator dispatch prompt"

  - id: 2
    title: "Author per-test dispatch fixtures with expected-result assertions"
    status: open
    priority: high
    due_date: null
    depends_on: [1]
    blocked_by: []
    acceptance_criteria:
      - "Each of T1-T4 has a self-contained dispatch prompt fixture (synthetic inputs, run_date placeholder, stated constraints) reusable without chat context."
      - "Each fixture pairs with explicit expected assertions: envelope fields, boundary refusals (e.g. T1 refuses interpretation, T4 refuses exact ranking), and output-path constraints."
    definition_of_done:
      - "Fixtures dry-read cleanly: every path they cite resolves in the repo."
      - "Operator approves fixture set for baseline run."
    notes:
      - "T1/T2 fixtures can be reconstructed from the recorded dispatch summaries; T3/T4 need confirmation (see review_flags)."
    source:
      - apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md

  - id: 3
    title: "Define change-trigger map (which file changes require which tests)"
    status: open
    priority: medium
    due_date: null
    depends_on: [1]
    blocked_by: []
    acceptance_criteria:
      - "Map covers .claude/agents/**, .claude/skills/**, and .claude/skills/weekly-orchestrator/references/handoff-schema.md, each mapped to the minimum test subset to re-run."
      - "A schema change triggers all four tests; a single-agent change triggers at least that agent's test."
    definition_of_done:
      - "Map is qualitative (checklist form), contains no automation hooks, and is operator-consultable at change time."
    notes:
      - "Purely a lookup checklist — no scheduler, no git hook, per CLAUDE.md constraints."
    source:
      - "operator dispatch prompt"
      - apex-meta/fable-orchestrator/build-plan.md

  - id: 4
    title: "Execute baseline regression run of T1-T4 and record results"
    status: open
    priority: high
    due_date: null
    depends_on: [2, 3]
    blocked_by: []
    acceptance_criteria:
      - "All four fixtures dispatched for real; per-test verdict (pass/partial/fail) recorded with actual steps, actual outputs cited, and cost where observable."
      - "Test artifacts cleaned up or marked as test artifacts after recording, matching T1/T2 precedent."
    definition_of_done:
      - "Baseline record file exists at the operator-chosen records location (see epic unresolved_scope_decisions)."
      - "Any failures produce named follow-up flags, not silent passes."
    notes:
      - "depends_on 3 is proposed because the baseline record should state which trigger conditions it certifies; if the operator prefers, 4 could depend on 2 only — flagged for apex-sync validation."
    source:
      - apex-meta/fable-orchestrator/build-plan.md

  - id: 5
    title: "Write operator runbook and link suite from orchestrator audit surface"
    status: open
    priority: medium
    due_date: null
    depends_on: [4]
    blocked_by: []
    acceptance_criteria:
      - "Runbook states: when to run (trigger map), how to dispatch each test, where records go, and what a failing verdict obligates."
      - "The weekly-orchestrator audit path or architecture KB references the suite so it is discoverable at change time."
    definition_of_done:
      - "Operator can re-run the full suite from the runbook alone, without this planning conversation."
    notes:
      - "Linking from KB/architecture files is a confirmed-write action — routed through apex-session, not performed by planning."
    source:
      - "operator dispatch prompt"
```

## dependency_plan

```yaml
dependency_plan:
  proposed_depends_on_updates:
    - task_id: 2
      depends_on: [1]
      rationale: "Fixtures encode the spec's assertions; authoring them before pass criteria exist would invert the source of truth."
      confidence: high
      review_flags: []
    - task_id: 3
      depends_on: [1]
      rationale: "The trigger map maps file changes to tests defined in the spec's inventory."
      confidence: high
      review_flags: []
    - task_id: 4
      depends_on: [2, 3]
      rationale: "The baseline run dispatches the fixtures (2) and certifies the trigger conditions (3)."
      confidence: medium
      review_flags: [dependency_uncertainty]
    - task_id: 5
      depends_on: [4]
      rationale: "The runbook documents a suite proven by at least one real baseline run, per the simulation discipline (no hypothetical walkthroughs)."
      confidence: high
      review_flags: []
  blocked_by_notes: []
  circular_dependency_check: "No direct mutual dependencies among tasks 1-5; obvious-direct-risk scan only — full graph validation is apex-sync's job."
  apex_sync_handoff_requests:
    - validate_dependencies
```

## priority_urgency_focus_rationale

```yaml
priority_urgency_focus_rationale:
  priority_rationale:
    task_1: "high — every other task consumes the spec; the regression goal in build-plan.md is unmet without it."
    task_2: "high — fixtures are what make the suite repeatable rather than a one-off memory."
    task_3: "medium — useful gate on when to run, but the suite functions manually without it."
    task_4: "high — the build-plan discipline requires a real run; nothing counts as regression coverage until executed once."
    task_5: "medium — durability/discoverability work; valuable but not blocking the first certified baseline."
  urgency_rationale: >
    No operator-supplied due dates; none recorded (null throughout). Qualitative urgency: the suite
    becomes most valuable before the next wave of agent/skill/schema changes (task list shows pending
    integration and migration work), so tasks 1-2 are urgent relative to upcoming change volume, not
    to any calendar date. No missing_due_date flag raised because no task was described as date-bound.
  provisional_focus_recommendation:
    focus_candidate_title: "Define regression checklist spec (task 1)"
    rationale: >
      Task 1 has no dependencies, unblocks all four remaining tasks, and resolves the packet's main
      uncertainty (unconfirmed T3/T4 definitions) as part of its definition of done.
    confidence: high
    assumptions:
      - "T3/T4 agent contracts under .claude/agents/ are the canonical definition source."
      - "No competing higher-priority work overrides this within the project scope."
    handoff_needed:
      - validate_dependencies
      - compute_focus_candidates
```

## review_flags

```yaml
review_flags:
  - flag: operator_review_needed
    detail: "apex-meta/registry/index.md does not exist; task-id space could not be read. Ids 1-5 assume a fresh epic folder — confirm no id collision policy applies."
  - flag: dependency_uncertainty
    detail: "Task 4 depends_on [2,3]: the 4→3 edge is a proposal (baseline should certify trigger conditions), not a proven prerequisite; apex-sync validation requested."
  - flag: unclear_scope
    detail: "T3 (sync reports) and T4 (plan packet) have no recorded results in 03-execution-trace-verification.md section 5; their canonical fixture definitions must come from the agent contracts, confirmed in task 1."
  - flag: operator_review_needed
    detail: "Records location undecided: apex-meta/fable-orchestrator/simulations/ (not yet created per build-plan.md) vs. suite-local folder — see epic unresolved_scope_decisions."
```

## handoff_requests

```yaml
handoff_requests:
  to_apex_sync:
    - request: validate_dependencies
      reason: "Confirm the proposed depends_on edges, especially the medium-confidence 4→3 edge."
    - request: compute_focus_candidates
      reason: "Registry-wide validation of the provisional focus recommendation once records are durable."
  to_apex_session:
    - request: request_operator_confirmed_write
      reason: "On operator approval, create apex-meta/epics/orchestrator-regression-suite/ (epic.md + task records 1-5) via the confirmed write path."
```

## operator_gate

```yaml
operator_gate:
  state: operator_review_needed
  required_before_mutation_handoff: true
  requested_operator_action: confirm
  accepted_states: [operator_review_needed, approved_for_handoff, needs_revision]
  note: "No durable files were created or mutated by this packet; all task records above are proposals."
```
