---
title: "Fable Multi-Agent Orchestration — Execution Completion Plan"
purpose: "Execution-first recovery and completion plan for Chat 1 to build, run, evaluate, and finish the final multi-agent orchestration system."
created: 2026-07-11
updated: 2026-07-12
status: execution_required
authority: apex-meta/fable-orchestrator/target-log.md
---

# Target

Build and prove the final Claude Code multi-agent orchestration system that merges:

- the accepted accountabilities and useful doctrine from old Apex v1/v2;
- `apex-plan`, `apex-sync`, and `apex-session` as bounded Meta Ops capabilities;
- the mechanism, resilience, deterministic/LLM, review, state, and token-design lessons from `claude-code-orchestration-design`;
- the seven workflows in `APEX_Orchestration_User_Stories/user-stories.md` as the regression and acceptance corpus.

The deliverable is a working multi-agent system, not another plan, audit, prompt pack, weekly plan, or architectural narrative.

# Non-target and contamination boundary

```yaml
weekly_orchestrator:
  paths:
    - apex-meta/kb/Weekly-Orchestrator/
    - .claude/skills/weekly-orchestrator/
    - artifacts/weekly-plans/
    - artifacts/next-day-plans/
    - artifacts/flow-packets/
    - artifacts/flow-recap-packets/
  relationship: separate_existing_workflow_and_control_plane
  may_be_read_as_reference: false
  may_be_used_as_fable_completion_evidence: false
  may_be_modified_by_this_plan: false
  exception: "Only an explicit later operator instruction naming a weekly path can reopen it."
```


# Operating directive 

```yaml
execution_directive:
  mode: build_until_done
  first_action: read_current_truth_and_create_the_missing_runtime_surface
  default: execute_the_next_unblocked_build_item
  do_not_substitute:
    - research_for_implementation
    - plan_updates_for_files
    - structural_lint_for_behavioral_execution
    - claimed_commits_for_files_visible_in_the_current_checkout
  stop_only_for:
    - an operator decision whose alternatives materially change the system
    - an unsafe or unauthorized durable mutation
    - missing source material that cannot be recovered or truthfully substituted
  progress_rule: "Every iteration ends with a built artifact plus its proportionate validation."
  completion_claim_rule: "Never say complete until every Definition of Done item has direct evidence."
```

# Authoritative inputs

Read in this order and use refs rather than copying bodies into the main context:

1. `target-log.md` — target and milestones.
2. `decisions.md` — full-final-system requirement and orchestration process.
3. `design-lock-answers.md` — Q1–Q8 architecture decisions; resolve stale proposal labels against current operator instructions.
4. `evaluation-matrix.md` and `discovery-notes.md` — source-system strengths, failures, and uncertainty.
5. `APEX_Orchestration_User_Stories/user-stories.md` — required behavior and seven acceptance workflows.
6. `apex-meta/handoff/agent-skill-system-research/best-practice-report.md`.
7. Targeted pages from `apex-meta/kb/claude-code-orchestration-design/`, selected by the active build item.
8. Old Apex doctrine files only through a deterministic inventory/worker assignment; never load the whole corpus into the lead context.
9. Live contracts for `.claude/skills/apex-plan/`, `apex-sync/`, and `apex-session/`.


# Target architecture to materialize

The build must create one current, navigable system package. Use `apex-meta/orchestration/` unless an already-present, equivalent canonical path is proven in the current checkout.

```text
apex-meta/orchestration/
├── 00-START-HERE.md
├── ARCHITECTURE.md
├── CURRENT-SYSTEM-MANIFEST.yaml
├── agents/
│   ├── ACCOUNTABILITY-MAP.md
│   ├── DOCTRINE-MANIFEST.md
│   ├── alfred/
│   ├── meta-strategy/
│   ├── meta-ops/
│   ├── meta-detective/
│   ├── knowledge-bank/
│   ├── informatics-design/
│   └── prompts-workflows/
├── schemas/
│   ├── handoff-packet.md
│   ├── authority-state.md
│   ├── review-verdict.md
│   └── run-record.md
├── workflows/
│   ├── orchestrator-run.md
│   ├── detective-review.md
│   ├── correction-and-revalidation.md
│   └── operator-gate.md
├── tests/
│   ├── static/
│   ├── behavioral/
│   └── negative/
└── simulations/
    ├── US-SEQ-01/
    ├── US-MEDIA-01/
    ├── US-LEELA-01/
    ├── US-WORKSHOP-01/
    ├── US-IDEA-01/
    ├── US-OFFER-01/
    └── US-COMP-01/
```

Runtime discovery surfaces remain in their canonical Claude locations:

- `.claude/agents/` for executable agent definitions;
- `.claude/skills/` for executable skills;
- `scripts/` for deterministic computation;
- `apex-meta/orchestration/` for the final system map, doctrine ownership, shared contracts, workflows, tests, and evidence.

# Iterative execution sequence

At most one milestone is `in_progress`. Independent file/doctrine evaluations inside a milestone may fan out in parallel. Do not pause after a successful milestone while an unblocked next milestone exists.

## M0 — Establish recoverable current truth

**Purpose:** prevent another cross-chat takeover without turning recovery into the deliverable.

Actions:

1. Record branch, HEAD, worktree root, and relevant dirty paths in `apex-meta/orchestration/CURRENT-SYSTEM-MANIFEST.yaml`.
2. Check whether the Chat 1 claimed commits or equivalent files exist locally or remotely.
3. If absent, record them as `unavailable_claimed_history` once and build from current authoritative sources. Do not repeatedly search for them.
4. Inventory existing Fable-related `.claude/agents/`, skills, schemas, workflows, and orchestration packages. Classify each as `reuse`, `adapt`, `replace`, `historical`, or `weekly_out_of_scope`.
5. Confirm no planned write path targets the weekly boundary above.

Required output:

- `CURRENT-SYSTEM-MANIFEST.yaml` containing the inventory and exact target paths.

Gate:

- Every claimed current component resolves to a file in the current checkout.
- Weekly paths are explicitly classified `weekly_out_of_scope`.
- Continue immediately to M1.

## M1 — Lock and materialize the macro architecture

Actions:

1. Resolve the runtime topology from Q1/Q4/Q8 and the current Claude Code mechanism constraints.
2. Define which accountabilities live in the main conversation and which are spawned, with reasons based on identity, isolation, tool restriction, verbosity, and plan ownership.
3. Define the seven durable accountability/specialist domains:
   - Alfred;
   - Meta Strategy;
   - Meta Ops;
   - Meta Detective;
   - Knowledge Bank;
   - Informatics Design;
   - Prompts & Workflows.
4. Define temporary domain workers as scoped invocations, not permanent roster growth.
5. Specify spawn authority, allowed nesting, maximum fan-out, return shape, context/source slicing, stop conditions, and failure propagation.
6. Specify where durable state, run state, accepted decisions, candidate learning, and evidence live.
7. Specify the deterministic/LLM boundary and the one mutation boundary.

Required outputs:

- `ARCHITECTURE.md` — macro topology and invariants.
- `agents/ACCOUNTABILITY-MAP.md` — owns / must-not-own / tools / invocation / inputs / outputs / validator.
- `CURRENT-SYSTEM-MANIFEST.yaml` updated with the final file map.

Gate:

- Every user-story stage maps to exactly one accountable owner.
- No important action is ownerless or multiply authoritative.
- Spawn wiring is executable in the chosen Claude environment, not merely described.
- Main-conversation versus spawned-agent decisions are explicit.

## M2 — Build the shared contracts and enforcement boundary

Actions:

1. Implement one handoff envelope for agent, worker, deterministic-tool, review, and gate returns.
2. Keep `authority.state` separate from `operator_validation`.
3. Bind reviews to immutable content/evidence digests without creating a self-invalidating hash loop; use a sidecar or excluded authority fields where necessary.
4. Implement criterion-level validity and alignment verdict schemas.
5. Implement correction ownership and scoped revalidation rules.
6. Implement run identity, attempt number, supersession, and resume pointers.
7. Define the exact canon-changing write path and its executable checks.

Required outputs:

- all files under `schemas/`;
- all files under `workflows/`;
- deterministic validation script or existing-script binding for schema/digest/write checks;
- negative fixtures for candidate-to-canon leakage, stale digest, missing evidence, reviewer mutation, and unauthorized writes.

Gate:

- Schemas parse.
- Negative tests fail closed.
- A killed run can resume using only durable files and `run_id`.
- No role label alone grants mutation authority.

## M3 — Create executable agent definitions

Actions:

1. Build or update the `.claude/agents/` definitions for every spawned accountability/specialist.
2. Create main-conversation contracts for any accountabilities that must remain in the lead thread.
3. Give every definition:
   - precise trigger/description;
   - accountability and non-ownership;
   - narrow tools;
   - preloaded skills and on-demand references;
   - source-slice rules;
   - expected return contract;
   - stop condition;
   - correction owner;
   - doctrine-domain pointer.
4. Prove spawn rights and invocation syntax with a minimal live dispatch per agent type.
5. Do not reuse weekly stage-agent identities as substitutes for Fable accountabilities.

Required outputs:

- executable definitions in `.claude/agents/`;
- corresponding accountability domains under `apex-meta/orchestration/agents/`;
- registration and live-dispatch evidence under `tests/behavioral/`.

Gate:

- Every definition registers.
- Tool allowlists match ownership.
- Each agent can be invoked and returns the shared contract.
- Reviewers are read-only and cannot implement fixes.

## M4 — Evaluate and migrate old-Apex doctrine deterministically

Actions:

1. Inventory every relevant v1/v2 role file: ESSENCE, BEST_PRACTICES, MISTAKES, TEMPLATES, LEARNING_QUEUE, and appendices.
2. Assign bounded workers by role/domain. Each returns one row per source file/item with:
   - source path and source hash;
   - `keep_verbatim`, `translate`, `reference_only`, `superseded`, `unsafe`, or `empty`;
   - target owner;
   - reason tied to current architecture;
   - conflicts or volatile claims.
3. Copy verbatim material deterministically and verify hashes.
4. Put translations in clearly named current-doctrine files; never silently modify historical evidence.
5. Keep LEARNING_QUEUE material candidate-only unless independently accepted.
6. Reject provider ceilings, fabricated claims, dead paths, execution-control assumptions, and duplicated current contracts.

Required output:

- `agents/DOCTRINE-MANIFEST.md` with complete source-to-target coverage;
- accepted doctrine in the owning agent domains;
- verification report proving every copied file and every dropped item has a verdict.

Gate:

- No relevant source file is unclassified.
- Every accepted doctrine file has a live consumer pointer.
- No historical KB file is deleted or rewritten.

## M5 — Integrate Plan, Sync, and Session under Meta Ops

Actions:

1. Build `agents/meta-ops/INTEGRATION-apex-plan-sync-session.md` from the live skill contracts.
2. Bind intent to capability:
   - Plan proposes structure and dependencies;
   - Sync performs exact computation and dry-run reports;
   - Session records only confirmed mutation and continuation context.
3. Preserve the preview → review → confirmed-write sequence.
4. Specify routing rejections so each package refuses work outside its boundary.
5. Execute real dry-run fixtures against repository task records.
6. Test that no spawned agent can perform a non-dry-run canon write.

Required outputs:

- Meta Ops integration contract;
- executable routing in the Meta Ops definition/workflow;
- real Plan/Sync/Session behavioral test records.

Gate:

- Proposal, computation, and mutation cannot be conflated.
- Sync outputs are preserved exactly.
- Session mutation requires both verified evidence and operator confirmation.
- No Weekly Orchestrator file is changed.

## M6 — Build and run the review/correction loop

Actions:

1. Freeze a real candidate artifact and declared evidence set.
2. Dispatch validity and alignment lenses independently and in parallel.
3. Aggregate verdicts deterministically.
4. Route every failed criterion to its actual owner.
5. Apply a bounded correction and prove the diff.
6. Re-run only the affected lens when the diff proves the rest of the reviewed basis is unchanged; otherwise rerun the full review.
7. Record residual same-family/model-correlation limitations honestly. Do not claim model-family independence without a runtime surface that enforces it.

Required output:

- complete review → correction → revalidation evidence under `tests/behavioral/`.

Gate:

- At least one planted or naturally discovered defect is caught.
- Reviewers do not fix it.
- Deterministic aggregation matches the schema.
- Corrected evidence is genuinely re-read and passed.

## M7 — Run all seven user-story simulations

One simulation per story is mandatory. Static mapping or hypothetical walkthroughs do not count.

Execution order, chosen to build confidence from lower to higher consequence:

1. `US-IDEA-01` — intake, source preservation, placement, review, bounded action choice.
2. `US-SEQ-01` — ambiguous concept to method/pilot workflow.
3. `US-MEDIA-01` — parallel worker fan-out and cross-asset consistency.
4. `US-LEELA-01` — bounded requirements and implementation gate.
5. `US-WORKSHOP-01` — safety boundary and qualified-human handoff.
6. `US-OFFER-01` — demand evidence before asset fan-out.
7. `US-COMP-01` — external-authority, compliance evidence, recurring state, and stop conditions.

Each simulation must contain:

```yaml
simulation_record:
  story_id: required
  run_id: required
  actual_repo_input: required
  agent_invocations: required
  deterministic_commands: required
  artifacts_created: required
  review_and_correction: required_when_consequential
  operator_gate_reached: required_when_defined
  state_mutation: "performed only if authorized; otherwise proven held"
  defects_found: required
  result: pass | partial | fail
  evidence_paths: required
```

Gate per story:

- Run used real repository material.
- Required agents actually spawned.
- Handoffs parsed.
- Planned parallel branches actually ran independently.
- Defects and degraded behavior are recorded honestly.
- Consequential action stops at the operator/professional boundary when not authorized.

Do not postpone failed stories. Repair the owning system component, rerun the failed story, and preserve the failed attempt as evidence before advancing.

## M8 — System-level resilience and efficiency evaluation

Actions:

1. Extract testable rules from the primary Claude orchestration-design KB pages used by this build.
2. Score the built system with file/behavior evidence: pass, partial, fail, not_applicable.
3. Test:
   - interruption and resume;
   - stale or missing source;
   - contradictory worker returns;
   - blocked agent;
   - invalid handoff twice;
   - reviewer disagreement;
   - same-run rerun/idempotence;
   - concurrent independent branches;
   - token/context growth across multiple stages;
   - unauthorized mutation attempt.
4. Measure per-agent input references, output size, tool calls, and observed token use when available.
5. Fix every correctness failure. Optimize high-cost stages without removing evidence needed for safety or auditability.

Required outputs:

- `tests/system-audit-vs-orchestration-design-kb.md`;
- `tests/token-and-context-evaluation.md`;
- failure fixtures and rerun evidence;
- updated architecture/contracts for every accepted correction.

Gate:

- Zero unresolved correctness failures.
- Any partial result has a named external limitation rather than missing implementation work.
- The system resumes from files without chat-memory reconstruction.
- Token-efficiency claims are supported by measurements, not entrypoint size alone.

## M9 — Finalize current truth and handoff

Actions:

1. Regenerate `CURRENT-SYSTEM-MANIFEST.yaml` from the final files.
2. Validate every current path and remove stale current-truth references; keep history only in logs/audits.
3. Update `00-START-HERE.md`, `ARCHITECTURE.md`, and the Fable target status to match direct evidence.
4. Ensure Weekly Orchestrator is described only as a separate compatible workflow, never as Fable completion evidence.
5. Run final static, behavioral, negative, story, and resume gates.
6. Commit and push the exact Fable paths. Report hashes and remaining genuine external limitations.

Required output:

- final manifest;
- final acceptance report;
- clean navigation from Fable entrypoint to every runtime and evidence surface.

# Iteration protocol

For each milestone:

```yaml
iteration:
  announce: "milestone, files to produce, acceptance command/test"
  build: "create or modify the target artifacts"
  verify: "run the smallest test that proves the artifact works"
  repair: "fix failures immediately; do not open unrelated work"
  persist: "commit coherent completed milestone or durable sub-batch"
  advance: "start the next unblocked milestone"
```

Parallelize only independent bounded work. The lead agent owns target fidelity, integration, and verification. Worker summaries never substitute for reading their produced artifacts.

# Definition of Done

The Fable multi-agent orchestration system is complete only when all are true:

```yaml
definition_of_done:
  generalized_architecture_materialized: true
  current_system_manifest_resolves: true
  accountabilities_and_nonownership_complete: true
  spawn_and_tool_permissions_proven_live: true
  shared_handoff_authority_review_and_run_schemas_parse: true
  correction_and_revalidation_loop_executed: true
  old_apex_doctrine_fully_classified_and_migrated: true
  plan_sync_session_integrated_under_meta_ops: true
  deterministic_and_llm_boundaries_tested: true
  unauthorized_mutation_fails_closed: true
  all_seven_user_story_simulations_pass: true
  interruption_resume_test_passes: true
  concurrency_and_idempotence_tests_pass: true
  token_efficiency_measured_and_optimized: true
  weekly_orchestrator_remains_separate_and_unchanged: true
  no_draft_placeholder_or_false_completion_status: true
  final_files_committed_and_pushed: true
```

Not done:

- only architecture documents exist;
- agents exist but cannot be spawned;
- skills exist but are not wired to owners;
- doctrine is summarized without complete source disposition;
- Plan/Sync/Session are mentioned but not behaviorally tested;
- one demonstration is used to imply seven-story coverage;
- weekly-loop packets are used as Fable evidence;
- tests are structural only;
- the agent reports a commit that cannot be resolved in the current repository;
- unresolved implementation work is relabeled as a future optimization.

# Final report shape

```yaml
completion_report:
  commit_and_branch: required
  built_runtime_surfaces: required
  agent_registration_and_spawn_results: required
  doctrine_migration_counts_and_manifest: required
  plan_sync_session_test_results: required
  seven_story_verdicts: required
  negative_and_resume_test_results: required
  token_measurements: required
  weekly_boundary_check: required
  unresolved_external_limitations: required
```
