# Apex Plan / Weekly / Session Authorization — Local Code Handover

Date: 2026-08-16
Format: OKR-oriented implementation handover
Repository: `leela-spec/apexai-os-meta`
Required branch: `main`
Handover base commit: `8b6aa657236ad29dc10f50ce39ef2487cf8225be`
Canonical project folder: `apex-meta/plan-sync-session-improvement/`
Status: **ready for local reproduction and implementation planning; production skill edits remain gated by the explicit P1/W1 operator decision unless separately confirmed**

---

## Objective O1 — Reproduce the validated design state locally without relying on chat memory

### Intent

A local coding agent must be able to reconstruct the complete design, evidence, decisions, constraints, and remaining decision boundary from repository files alone.

### Key Results

- **KR1.1:** local checkout is on `main` and contains commit `8b6aa657236ad29dc10f50ce39ef2487cf8225be` or a later descendant that has been inspected for changes affecting this line.
- **KR1.2:** all files in `apex-meta/plan-sync-session-improvement/` are read in the prescribed order before production edits.
- **KR1.3:** `10-carrier-spike.py` is executed locally and reproduces the expected `17/17`, `0 unsafe allows`, `0 overblocks`, and `0 repeated operator gates across 50 covered internal actions` result before any production contract change is attempted.
- **KR1.4:** no agent uses this chat transcript as the authoritative source when a repository artifact exists.

### Local start procedure

PowerShell-oriented commands:

```powershell
git status
git branch --show-current
git checkout main
git pull --ff-only
git rev-parse HEAD
Get-ChildItem apex-meta/plan-sync-session-improvement
python apex-meta/plan-sync-session-improvement/10-carrier-spike.py
```

Expected invariant before edits:

```text
branch = main
carrier_spike.policy_correctness = 17/17
carrier_spike.unsafe_allows = 0
carrier_spike.overblocks = 0
carrier_spike.repeated_operator_gates_across_50_covered_internal_actions = 0
```

If local `main` is ahead of the handover base commit, inspect all intervening changes that touch Plan, Session, Weekly Orchestrator, Status Merge, Sync, shared operator validation, or the canonical project folder before continuing. Do not assume the design is still current merely because file paths are unchanged.

---

## Objective O2 — Preserve the operator-validated architecture and prevent decision drift

### Locked decisions

These are the accepted design direction unless explicitly superseded by a later operator decision recorded in the repository:

#### A1′ — Commit-time action authorization

A prior operator approval may authorize a later internal durable action only when the exact pending action is still covered immediately before the durable effect by the same:

- authorization identity;
- durable authority reference;
- approved basis digest;
- allowed action class;
- target scope;
- constraints;
- lifecycle state;
- required objective evidence;
- optional payload digest when exact payload binding is required.

The authorization check occurs at the real durable-effect boundary, not merely at planning time.

#### B1 — External / irreversible actions stay action-specifically gated in v1

The first rollout must not allow reusable internal authorization to silently execute:

- external sends;
- publishes;
- payments or trades;
- destructive deletions/migrations;
- irreversible effects outside bounded internal persistence;
- any action explicitly marked manual by the operator.

A task record may describe one of these future actions without authorizing execution of that action.

#### C1 — Apex Sync protected registry write remains unchanged

- normal dry-run/read-side Sync behavior remains normal Sync behavior;
- `registry --dry-run false` still requires the current explicit operator request;
- generic reusable authorization must not weaken or replace this rule in the core Plan -> Session redesign.

### Additional locked architecture constraints

- deterministic authorization checks precede optional AI semantic review;
- AI semantic review may escalate but must never override a deterministic denial;
- source conflicts remain preserved and gated;
- duplicate-entity merge risk remains gated;
- operator-judgment-required completion remains gated;
- ambiguous scope fails closed;
- changed basis invalidates prior reusable authority;
- revoked or expired authorization fails closed on the next action;
- no implicit parent/project/epic/task inheritance when exact coverage is ambiguous;
- no canonical task-wide `auto / exception_only / manual` field as the root authority primitive;
- Weekly Orchestrator G1-G5 remain intact;
- no new global authorization registry, service, daemon, scheduler, or database for this redesign;
- no production change should be justified merely by architectural symmetry.

### Key Results

- **KR2.1:** no implementation changes any locked decision without a new explicit operator decision artifact.
- **KR2.2:** any discovered conflict between this handover and current repository contracts is recorded rather than silently reconciled.
- **KR2.3:** historical research files `01` through `12` remain evidence/history and are not rewritten to make a new implementation look retrospectively inevitable.

---

## Objective O3 — Use the smallest canonical authorization contract that solves the verified double-gate problem

### Verified problem

The live pipeline can require two approvals for one unchanged semantic decision:

1. Apex Plan produces proposal state and obtains operator approval for mutation handoff.
2. Apex Session creates an exact before/after mutation preview.
3. Current Session rules can require another explicit confirmation before deterministic canonicalization.

The W34 portfolio trace reproduced this behavior in the repository.

### Target behavior

When Session is only mechanically persisting already-approved meaning and the commit-time witness is still valid, Session must not ask for another semantic approval solely because it is writing the approved result.

If the witness is missing, stale, changed, revoked, expired, out of scope, blocked by an existing hard safety rule, or otherwise invalid, the existing fresh operator-confirmation path remains the fallback.

### Minimal witness shape

Do not add fields unless a concrete failure case requires them.

```yaml
authorization_witness:
  authorization_id: <stable-id>
  authority_ref: <repo-relative operator-confirmed packet or decision>
  basis_digest: "sha256:<digest>"
  allowed_actions: []
  target_scope: []
  constraints: []
  issued_at: <timestamp>
  expires_at: <timestamp-or-null>
  status: active | revoked | expired
```

Optional exact binding only when needed:

```yaml
payload_binding:
  required: true | false
  payload_digest: null | "sha256:<digest>"
```

### Commit-time validation order

The implementation must preserve this precedence because it keeps permission logic understandable and fail-closed:

1. **Hard gate:** explicit manual override, destructive action, B1 external/irreversible action, source conflict, duplicate identity risk, operator judgment required.
2. **Witness state:** witness exists, status active, not expired when expiry exists.
3. **Basis binding:** current basis digest equals approved basis digest.
4. **Action binding:** pending action class is explicitly allowed.
5. **Scope binding:** exact target is inside explicit scope; ambiguity gates.
6. **Payload binding:** if required, current payload/mutation digest matches.
7. **Constraints/evidence:** deterministic constraints and required objective evidence pass.
8. **Optional semantic review:** may escalate; may never convert a deterministic denial to allow.
9. **Effect:** execute idempotently or detect exact prior application, then preserve a durable receipt.

### Key Results

- **KR3.1:** exact approved Plan serialization needs one semantic approval, not two.
- **KR3.2:** existing fresh confirmation remains available whenever reusable authorization cannot prove coverage.
- **KR3.3:** no new task schema field is required.
- **KR3.4:** no global lookup infrastructure is required; the approved packet is the durable witness container.

---

## Objective O4 — Carry authorization through existing Plan / Weekly / Status Merge / Session structures

### Carrier design validated by the spike

#### Apex Plan

Existing carrier: `operator_gate` and approved handoff state.

Minimal change:

- when an operator approval is intended to authorize deterministic downstream internal actions, freeze/reference the witness in the approved Plan packet;
- Plan remains proposal-only and does not become a mutation owner;
- do not add authorization fields to canonical task records.

Candidate shape:

```yaml
operator_gate:
  state: approved_for_handoff
  operator_validation: confirmed
  authorization:
    authorization_id: ...
    authority_ref: ...
    basis_digest: ...
    allowed_actions: [...]
    target_scope: [...]
    constraints: [...]
    issued_at: ...
    expires_at: null
    status: active
```

#### Weekly Orchestrator

Existing carriers already available:

- `operator_validation`;
- `authority.state`;
- `authority.basis_digest`;
- `verification_ref`;
- existing invalidation when packet/source changes.

Minimal extension only when a confirmed packet is intended to confer reusable internal authority:

```yaml
authority:
  state: verified
  basis_digest: "sha256:<digest>"
  verification_ref: <existing review ref>
  authorization_id: <id>
  authorization_ref: <confirmed packet path>
operator_validation: confirmed
```

Do not create another Weekly authorization engine. Weekly transports evidence and preserves its existing G1-G5 gate semantics.

#### Apex Status Merge

Status Merge should preserve/pass the confirmed authorization reference/digest to Session when applicable.

It must not:

- independently reinterpret the authorization policy;
- bypass G5;
- become a canonical mutation authority;
- duplicate the policy algorithm.

#### Apex Session

Session consumes references, resolves the witness, and performs the commit-time check at the actual durable-effect boundary.

Minimal input shape:

```yaml
mutation_input:
  operator_validation: confirmed
  authorization_id: <id>
  authorization_ref: <confirmed packet path>
  authorization_basis_digest: "sha256:<digest>"
```

Confirmation basis becomes:

```yaml
confirmation_basis:
  one_of:
    - fresh_operator_confirmation
    - valid_commit_time_authorization_witness
```

The before/after preview remains valuable audit evidence. Under a valid unchanged witness it ceases to be a second semantic approval request.

#### Apex Sync

No reusable-authorization change is required for the core fix.

C1 remains separate and explicit.

#### Canonical task record

No change expected.

Do not add:

- `gate_mode`;
- authorization id;
- inherited policy;
- task-wide risk authority.

### Key Results

- **KR4.1:** Plan carries authority without acquiring mutation ownership.
- **KR4.2:** Weekly reuses existing digest/validation carriers with at most the required scalar reference additions.
- **KR4.3:** Status Merge passes evidence without owning policy.
- **KR4.4:** Session is the only canonical policy consumer unless repository evidence proves a distinct durable writer.
- **KR4.5:** Sync and canonical task records remain unchanged for the core redesign.

---

## Objective O5 — Resolve the existing durable-writer ambiguity without inventing a subsystem

### Existing ambiguity

Current Session mutation-gate wording says final mutation records are authoritative input to a later explicit file-application flow and do not themselves imply silent repository writes. Weekly wording also describes Session as validating/applying confirmed mutation.

The design spike and repository search did not identify a separately named file-application/writer component.

This is an existing contract ambiguity. It is **not** evidence that Apex needs a new writer service.

### W1 — recommended handling

Clarify the real existing durable-write boundary during implementation:

- if Session is effectively the writer, including an immediate application step it owns, perform the final A1′ check there;
- if a real distinct downstream writer already exists, Session passes the witness and that existing writer revalidates immediately before the effect;
- if the boundary is implicit, clarify it in the smallest existing Session contract/reference edit;
- do not create a new writer or authorization actor solely to host the validation rule.

### W2 — rejected without new evidence

Do not create a dedicated writer/authorization subsystem unless empirical repository evidence demonstrates an existing unsolved execution need that cannot be handled by W1.

### Key Results

- **KR5.1:** the actual durable-effect boundary is explicitly identified before production completion.
- **KR5.2:** final authorization is checked immediately before that effect.
- **KR5.3:** no new writer subsystem is created merely to resolve documentation ambiguity.

---

## Objective O6 — Make the remaining architecture decision explicit rather than silently choosing it

### P1 — Session-owned canonical authorization reference — recommended

Candidate production home:

`.claude/skills/apex-session/references/authorization-policy.md`

Reasons:

- Session currently owns confirmed mutation semantics and mutation validation;
- Plan and Weekly need only transport/reference instructions;
- the policy belongs closest to the real mutation boundary;
- this minimizes discovery and context overhead;
- it can be shared/moved later if multiple independent writers are actually demonstrated.

### P2 — shared Workflow & Processes policy

Alternative: put the full canonical policy in a shared Workflow & Processes location immediately.

Use only if repository evidence demonstrates multiple independent durable writers that need to own the same complete validation algorithm now.

### Decision status

**P1/W1 are recommendations, not silently converted into operator approval by this handover.**

The local agent may reproduce the design spike and inspect production contracts immediately. Before making production contract edits that depend on policy placement, it must use the latest repository decision artifact or explicit current operator direction as authority.

### Key Results

- **KR6.1:** no policy location is chosen by assumption.
- **KR6.2:** if P1 is approved, the policy remains Session-local until evidence proves sharing is needed.
- **KR6.3:** if later evidence proves multiple real writers, movement to shared policy is an explicit migration, not hidden duplication.

---

## Objective O7 — Implement with the smallest production edit surface if P1/W1 are approved

### Expected minimum files

1. `.claude/skills/apex-plan/SKILL.md`
   - small carrier/output change only;
   - retain proposal-only authority.

2. `.claude/skills/apex-session/SKILL.md`
   - change consequential confirmation rule from unconditional fresh confirmation to fresh confirmation **or** valid commit-time witness;
   - identify final commit-time validation responsibility.

3. `.claude/skills/apex-session/references/mutation-gate-rules.md`
   - reference the canonical authorization policy;
   - preserve before/after preview;
   - preserve conflict/duplicate/manual hard gates;
   - clarify the actual write/application boundary.

4. `.claude/skills/apex-session/references/authorization-policy.md`
   - new compact canonical policy if P1 is approved;
   - contain schema, precedence, invalidation, and fallback behavior;
   - do not become a large framework document.

5. `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
   - add only authorization id/reference fields needed to carry reusable authority through the existing `authority` envelope.

### Edit only if current wording proves pass-through is otherwise ambiguous

- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/apex-status-merge/SKILL.md`

These edits, if needed, should be transport wording only, not another copy of authorization policy.

### Expected no-change surfaces for the core fix

- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/apex-plan/references/task-record-contract.md`
- `.claude/skills/apex-session/references/state-delta-and-entity-rules.md` except possibly a minimal cross-reference if required for clarity.

### Key Results

- **KR7.1:** one canonical policy copy exists.
- **KR7.2:** no full policy prose is duplicated into Plan, Weekly, Status Merge, or Sync.
- **KR7.3:** no unrelated skill redesign is bundled into this change.
- **KR7.4:** no new runtime service/process is introduced.

---

## Objective O8 — Validate safety, automation value, lifecycle behavior, and complexity before calling the redesign complete

### Required regression/eval source

Use:

`apex-meta/plan-sync-session-improvement/09-authorization-eval-matrix.md`

The production implementation must cover at least R01-R30 defined there.

### Required primary metrics

```yaml
acceptance_metrics:
  unsafe_allow_count: 0
  false_block_count_on_explicitly_authorized_internal_fixtures: 0
  duplicate_operator_gates_across_50_unchanged_covered_internal_actions: 0
  changed_basis_acceptance_rate: 0%
  revoked_or_expired_acceptance_rate: 0%
  out_of_scope_acceptance_rate: 0%
  external_or_irreversible_auto_execution_under_B1: 0
  source_conflict_or_duplicate_merge_auto_execution: 0
  sync_registry_non_dry_run_without_explicit_operator_request: 0
  new_canonical_task_fields_required: 0
  new_global_registry_service_or_daemon_required: 0
  canonical_policy_copies: 1
```

### Lifecycle requirements

- recent active witness may allow when all other checks pass;
- exactly at expiry => gate;
- after expiry => gate;
- `expires_at: null` may remain reusable only while all other checks still pass;
- revocation must affect the next action;
- basis change during a long-running workflow must gate at the first changed-basis action;
- restart/new AI session may resume from durable repository evidence if the witness still validates;
- missing/unreadable witness => gate/fallback to fresh operator confirmation.

### Performance/efficiency constraints

Do not invent latency targets before production measurements exist.

Architectural expectation:

- resolve a shared witness once per mutation batch when possible;
- O(1) status/action/scope checks per action after witness load;
- no network authorization service;
- no external authorization dependency;
- no persistent cache layer;
- no repeated human wait inside an unchanged covered batch.

If repeated reads become measurably expensive later, process-local caching is acceptable only with digest revalidation before commit. Persistent cache infrastructure is not justified by this redesign.

---

## Objective O9 — Keep local implementation resilient and non-drifting

### Mandatory anti-drift procedure before each production edit batch

1. `git pull --ff-only` on `main`.
2. Re-read `00-START-HERE.md` and this handover.
3. Inspect `git log` / diff since the last implementation commit for touched contracts.
4. If an affected contract changed, re-evaluate compatibility before editing it.
5. Make one coherent, bounded change.
6. Run relevant local checks/evals.
7. Commit the bounded change to `main` with an explicit message.
8. Save updated evidence/decision notes in this canonical folder when the design state changes materially.

### Commit discipline

Prefer incremental commits such as:

```text
docs: clarify commit-time authorization contract
feat: carry Plan authorization witness to Session handoff
feat: accept valid authorization witness in Session mutation gate
test: add authorization lifecycle regression fixtures
docs: record production authorization validation
```

Do not accumulate a large unreviewed cross-skill rewrite before committing.

### Fail-closed rules

Stop and record an operator decision request if implementation reveals:

- a second independent durable writer that materially changes policy placement;
- a need to pre-authorize B1 external/irreversible actions;
- a need to weaken C1 Sync registry protection;
- a need for task-level inherited authority;
- a source conflict that changes canonical behavior;
- a migration that would retroactively treat old unscoped approvals as reusable;
- a requirement for a global registry/service/daemon;
- a material semantic change beyond the approved A1′/B1/C1 model.

Do not solve those cases by expanding the subsystem automatically.

---

## Objective O10 — Preserve compatibility and migration safety

### Existing records

- historical `operator_validation: confirmed` records remain historical evidence;
- they do not need to be rewritten;
- old approvals lacking stable digest/scope/action evidence must not become reusable merely because the new policy exists;
- reusable authorization applies prospectively when sufficient witness data is recorded;
- no migration should add `gate_mode` to canonical tasks.

### Existing Weekly authority envelope

Reuse current `basis_digest` infrastructure and its existing invalidation behavior rather than creating a second digest system.

### Existing Session preview

Keep the before/after preview. It becomes:

- approval evidence requiring confirmation when no valid reusable witness exists;
- audit evidence when a still-valid witness already authorizes the exact internal mutation.

### Existing safeguards

The new authorization path must never bypass:

- source preservation;
- source conflict handling;
- duplicate identity protection;
- explicit operator manual overrides;
- subjective/operator acceptance requirements;
- destructive-action protection;
- B1 external/irreversible gate;
- C1 Sync registry write gate.

---

## Objective O11 — Give the local coding agent one authoritative reading order

### Required canonical folder reading order

1. `apex-meta/plan-sync-session-improvement/00-START-HERE.md`
2. `01-original-validation-handover.okf.md`
3. `02-independent-validation-report.md`
4. `03-gate-policy-simulation.py`
5. `04-simulation-results.txt`
6. `05-external-web-benchmark.md`
7. `06-operator-decisions-and-current-direction.md`
8. `07-source-and-history-index.md`
9. `08-authorization-policy-contract-draft.md`
10. `09-authorization-eval-matrix.md`
11. `10-carrier-spike.py`
12. `11-carrier-spike-results.txt`
13. `12-carrier-spike-verdict-and-compatibility-map.md`
14. `13-local-code-implementation-handover.okr.md` — this document

### Required live production contracts to inspect before edits

At minimum:

- `.claude/skills/apex-plan/SKILL.md`
- `.claude/skills/apex-plan/references/task-record-contract.md`
- `.claude/skills/apex-session/SKILL.md`
- `.claude/skills/apex-session/references/mutation-gate-rules.md`
- `.claude/skills/apex-session/references/state-delta-and-entity-rules.md`
- `.claude/skills/Workflow&Processes/operator-validation-and-conflict-resolution.md`
- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
- `.claude/skills/apex-status-merge/SKILL.md`
- relevant FlowRecap / execution-feedback contracts referenced by Weekly or Session.

Do not rely on this handover's summaries in place of reading the current live contract before editing it.

---

## Objective O12 — Define completion and handback precisely

### Implementation is not complete until all of these are true

- exact already-authorized Plan serialization no longer requires a redundant Session semantic approval;
- changed/revoked/expired/out-of-scope authority fails closed;
- hard safety gates override reusable authority;
- B1 external/irreversible actions still stop;
- C1 Sync non-dry-run registry writes still stop without explicit request;
- Weekly G1-G5 remain intact;
- canonical tasks gained no root authorization/gate field;
- one canonical authorization policy exists;
- no global authorization service/registry/daemon was introduced;
- actual durable-write boundary is explicitly identified and validates immediately before effect;
- R01-R30 are represented in executable or otherwise reproducible validation;
- long-run covered workflow produces zero duplicate operator gates;
- restart/resume depends on repository evidence rather than chat memory;
- final validation evidence and implementation handover are saved back into `apex-meta/plan-sync-session-improvement/`.

### Required final handback artifact

Create a new numbered artifact in this folder that records:

```yaml
implementation_handback:
  base_commit: ...
  final_commit: ...
  operator_decisions_used: ...
  files_changed: []
  files_intentionally_not_changed: []
  durable_writer_resolved_as: ...
  authorization_policy_location: ...
  regression_results: ...
  unsafe_allows: 0
  overblocks: 0
  duplicate_gates_long_run: 0
  known_limitations: []
  deferred_decisions: []
  compatibility_notes: []
  rollback_or_revert_boundary: ...
  next_safe_step: ...
```

Do not call the work complete from prose confidence alone. Completion requires repository state plus reproducible evidence.

---

# Decision / Authority Summary

```yaml
operator_direction:
  validated:
    - A1_prime_commit_time_action_authorization
    - B1_external_irreversible_action_specific_gate_v1
    - C1_preserve_sync_non_dry_run_registry_gate
  required_properties:
    - simple
    - efficient
    - resilient
    - valuable
    - on_target
    - non_drifting
    - avoid_over_engineering

recommended_but_not_silently_approved:
  P1: session_owned_canonical_authorization_policy_reference
  W1: clarify_existing_durable_writer_boundary_without_new_subsystem

explicitly_not_selected:
  - task_wide_gate_mode_as_root_authority
  - implicit_parent_scope_inheritance_when_ambiguous
  - AI_only_semantic_permission_engine
  - new_global_authorization_registry
  - new_authorization_service_or_daemon
  - weakening_B1_without_new_operator_decision
  - weakening_C1_without_new_operator_decision
```

# Success Definition

The successful implementation is intentionally modest:

> **One meaningful operator approval can authorize many deterministic internal effects, but each durable effect is still checked against the exact approved action, basis, scope, constraints, lifecycle, and evidence immediately before commit. Real semantic decisions and protected external/destructive boundaries still stop. The system gains automation without gaining a new authorization platform.**
