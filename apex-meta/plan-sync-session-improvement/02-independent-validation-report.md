# Apex Gate Policy Redesign — Independent Validation Report

Date: 2026-08-16
Repository: `leela-spec/apexai-os-meta`
Original validation branch: `validation/gate-policy-20260816`
Starting handover commit: `76b5ae2af1a6eb41f837958fe7f4740d5f9df383`
Validation base observed later on `main`: `d2f9d1d82bcfea6a11a16f48d9271f83f7591376`
Status: **proposal validated directionally, but not safe to implement verbatim**

## Executive conclusion

The double-gate diagnosis is real. `apex-plan` requires operator approval before mutation handoff, while `apex-session` independently requires `operator_validation: confirmed` for consequential mutation records. The real W34 run then produced a Session mutation preview that explicitly required another confirmation before canonicalization, even though its source basis already included operator approval of the Plan proposal.

The proposal's central idea is sound: **operator approval should authorize a bounded action/semantic scope, and Session should not demand another confirmation merely because it mechanically persists already-approved meaning.**

However, the proposed `auto / exception_only / manual` task/workflow gate model is too coarse as the primary stored policy. Risk varies by **action**, not only by task. A task can be safe to serialize into Apex state while containing a future manual decision or external action. Two concrete W34 examples prove this:

- ApexKB task 006 can be safely canonicalized, but the actual `continue / freeze / replace / hybrid` choice must remain operator-owned.
- An invoice task can be safely canonicalized, while actually sending an invoice is an external consequential action and needs its own authorization boundary.

### Recommended minimal target model

Use a **pinned, action-scoped authorization record** rather than copying inherited gate modes onto every task.

Minimum fields/concepts:

1. `authorization_ref` — durable reference to the operator-confirmed artifact or decision.
2. `basis_digest` — immutable digest of the approved packet/source basis.
3. `allowed_actions` — exact action classes covered, e.g. `canonicalize_exact_plan`, `objective_status_transition`, `bounded_code_fix`, optionally a specific external action.
4. `scope` — explicit project/epic/task/file/action boundaries; no implicit child authority when coverage is ambiguous.
5. `constraints` — semantic invariants and exclusions that must remain true.
6. `validity` — active/revoked/expired, with optional expiry when appropriate.
7. `exception_conditions` — source conflict, semantic delta, scope expansion, operator judgment, destructive action, duplicate merge, changed approval basis, missing objective evidence, etc.

Session then answers one question before a mutation: **Is this exact action still covered by an active pinned authorization whose basis and constraints remain unchanged?** If yes, it may validate and apply without a new operator gate. If no, it produces a preview/tradeoff and stops.

This keeps one semantic approval gate without inventing a broad new three-level policy layer.

## Verified current gate map

### Apex Plan

- Produces proposal-only planning packets.
- Requires an `operator_gate` before mutation handoff.
- Hands confirmed write/status work to Apex Session.

### Apex Session

- Owns confirmed canonical writes, status mutation, entity updates, and Session handoff state.
- Requires a before/after preview and an operator-validation record for consequential mutations.
- Treats `operator_validation: confirmed` as necessary before consequential mutation is confirmed.
- Preserves source conflicts and duplicate-entity risk rather than resolving them silently.

### Apex Sync

- Deterministic read-side computation by default.
- Registry write is the only write exception and already has a specific authorization mechanism: explicit operator request for `registry --dry-run false`.
- This explicit rule should not be silently weakened by a generic inherited `auto` mode.

### Weekly Orchestrator / Status Merge

- Weekly gates are separate semantic workflow gates, not just mutation confirmations.
- G1/G2/G3/G4/G5 carry stage decisions and evidence transitions.
- Confirmed G5 is routed to Apex Session, where the current Session contract can require another mutation confirmation.
- Review wiring correctly keeps changed source/digest, unresolved risk, and reviewer disagreement as reasons to stop.

### FlowRecap

- Candidate-only; never durable state.
- Appropriate separation should remain unchanged.

## Real-run evidence

The W34 portfolio run provides a concrete reproduction:

1. Plan proposal set was operator-approved.
2. Session wrote `session-mutation-preview-20260816-w34-portfolio.okf.md` with source basis including `operator approval in current workflow`.
3. That preview still declared `required_under_current_contract: explicit operator confirmation of this exact preview`.
4. Canonicalization then occurred only after that second confirmation.
5. Session handoff recorded both the earlier proposal approval and the exact Session preview confirmation.

This is a genuine duplicate approval for a deterministic serialization case.

## Independent critique of the proposal

### Accept

- **One meaningful semantic authorization should replace duplicate Plan-to-Session confirmation** when Session is only serializing approved meaning.
- **Exception-driven escalation** is better suited to unattended automation than unconditional per-write confirmation.
- **Semantic drift, source conflicts, destructive actions, scope expansion, and operator judgment remain stop conditions.**
- **Objective evidence-based status transitions can be eligible for automatic application.**
- **Explicit operator overrides must always remain possible.**

### Modify

- Replace task-level `gate_mode` as the primary mechanism with **action-scoped authorization reuse**.
- Treat `auto / exception_only / manual` as optional presentation labels or derived UI summaries, not necessarily canonical fields on every task.
- Require an immutable approval basis (`basis_digest`) for reuse.
- Define revocation/expiry explicitly before automation uses authorization across long-running workflows.
- For code changes, do not rely on an LLM-only `semantic_delta` judgment. Pair bounded authorization with deterministic path/test/acceptance constraints and evidence.
- External actions should be authorized by action/payload class, not inherited merely because their parent task is automatic.

### Reject as written

- **Automatic deterministic registry maintenance** as a generic candidate rule. Current Apex Sync deliberately requires an explicit operator non-dry-run request for the registry write. Changing that is a separate policy decision.
- **Implicit nearest-parent inheritance when exact coverage is unclear.** Ambiguous child scope must fail closed.
- **A single task gate describing every operation on that task.** Real tasks mix safe persistence, automated analysis, human decisions, and external effects.

## Simulation

Saved artifacts:

- `03-gate-policy-simulation.py`
- `04-simulation-results.txt`

Three abstract policies were tested against 16 scenarios:

- Current posture: `10/16` matched the provisional oracle, `0` unsafe allows, `6` over-blocks.
- Proposal as written: `12/16` matched, `1` unsafe allow, `0` over-blocks, `3` undefined cases.
- Minimal pinned authorization: `16/16` matched this test oracle, `0` unsafe allows, `0` over-blocks.

The one unsafe proposal result is a registry write without explicit write authorization. The three undefined cases are changed approval basis, revoked authorization, and ambiguous inherited scope.

Long-run simulation of 20 low-level covered actions:

- Current abstract posture: 20 repeated gates.
- Proposal-as-written: 0 repeated gates when no exception occurs.
- Minimal pinned authorization: 0 repeated gates when no exception occurs.
- Both exception models stop at action 13 when semantic drift is **detected**.

### Important limitation

A false-negative semantic-delta detector can defeat either exception-based model. Therefore this simulation validates policy structure only. It does **not** prove arbitrary code automation is safe.

## Failure modes and required countermeasures

| Failure mode | Consequence | Minimal countermeasure |
|---|---|---|
| Stale authorization | Old approval silently governs changed inputs | Pin basis digest; changed basis invalidates reuse |
| Revoked/expired authority | Automation continues after operator intent changed | Explicit active/revoked/expired state |
| Scope creep | Child/new work inherits broader authority than intended | Exact scope match; ambiguous coverage gates |
| Semantic detector false negative | Material behavior change auto-passes | Deterministic bounds, tests, reviewed acceptance criteria, action-specific evidence |
| Task/action conflation | Safe record write accidentally authorizes external/manual action | Authorize action classes, not task identity alone |
| Source conflict | Canonical meaning chosen silently | Existing conflict preservation + gate |
| Duplicate identity merge | Entity meaning corrupts | Existing duplicate-merge operator gate |
| Blanket auto-Done | Incorrect completion state | Require objective evidence; operator judgment remains gated |
| Registry policy erosion | Generic exception mode bypasses Sync contract | Keep explicit Sync registry-write authorization unless separately changed |
| External side effect leakage | Email/send/publish/pay/trade happens under unrelated task approval | Explicit external action/payload pre-authorization or gate |

## Recommended implementation boundary

Do **not** edit skills until the operator chooses the authorization representation and external-action policy below.

If the minimal model is approved, likely changes are limited to:

1. `.claude/skills/apex-plan/SKILL.md`
   - Operator gate output should produce/reference a reusable scoped authorization record when approval is granted.
   - No need to make Plan a mutation owner.

2. `.claude/skills/apex-session/SKILL.md`
   - Replace unconditional fresh confirmation for every consequential mutation with: valid reusable authorization **or** fresh operator confirmation.
   - Keep before/after preview/evidence as an audit artifact even when it is non-blocking.

3. `.claude/skills/apex-session/references/mutation-gate-rules.md`
   - Add authorization-reference/basis/scope validation.
   - Add explicit invalidation and exception rules.
   - Preserve conflict/duplicate/source safeguards.

4. `.claude/skills/apex-session/references/state-delta-and-entity-rules.md`
   - Only small references needed so conflicts/duplicate merges always override reusable authorization.

5. Weekly Orchestrator handoff schema / Status Merge
   - Prefer minimal compatibility edits only if needed to pass the already-confirmed packet's authorization reference/digest to Session.
   - Do not remove G1-G5 as part of this change.

6. Apex Sync
   - No change required for the core Plan-to-Session fix.
   - Registry non-dry-run policy should remain as-is unless separately approved.

## Compatibility / migration

- Existing task records do not need a new `gate_mode` field.
- Existing `operator_validation: confirmed` artifacts can remain valid historical evidence.
- New reusable authorization should apply prospectively to approvals that record sufficient scope and a basis digest.
- Old approvals without a stable digest/scope should not be retroactively treated as reusable authority unless explicitly normalized/confirmed.
- Existing weekly packets already contain `basis_digest` infrastructure in their authority envelope; this can be reused rather than inventing another digest mechanism.

## Acceptance tests for an implementation

1. Approved Plan packet with unchanged digest -> Session canonicalizes exact files without another operator question.
2. Preview differs semantically from approved packet -> Session gates.
3. Approved packet changes after approval -> prior authorization invalid.
4. Explicit authorization revoked -> all later covered writes gate.
5. New child task not clearly covered -> gate.
6. Objective status transition with required evidence -> may auto-apply if explicitly authorized.
7. Subjective/operator-acceptance DoD -> gate.
8. Source conflict -> gate regardless of inherited/active authorization.
9. Duplicate entity merge -> gate.
10. Destructive action -> gate unless separate exact destructive authorization policy is explicitly adopted.
11. External action not listed in allowed actions -> gate.
12. Explicitly pre-authorized external payload/action -> behavior follows the operator's chosen external-action policy.
13. Sync registry dry-run -> no gate beyond normal invocation.
14. Sync registry non-dry-run -> retain current explicit operator request requirement unless separately changed.
15. 20 low-level covered steps -> no repeated authorization prompt while basis/scope/constraints remain unchanged.
16. Detected semantic drift on step N -> stop exactly at N with an actionable decision packet.

## Operator decisions required before skill edits

### Decision A — canonical authorization representation

**Recommendation: A1.**

- **A1 — Pinned action-scoped authorization record (recommended):** minimal new concept; authorization references approved packet/digest, allowed actions, scope, constraints, validity, exceptions.
- **A2 — Store `gate_mode` on tasks/workflows:** simpler-looking UI, but conflates action risk and creates inheritance ambiguity.
- **A3 — Keep current Session confirmations:** safest change-wise, but fails the automation objective and preserves the verified double gate.

### Decision B — external irreversible actions

**Recommendation: B1 for initial rollout.**

- **B1 — Always require an action-specific operator gate for external/irreversible actions:** safest first version; internal automation still gains most of the benefit.
- **B2 — Permit exact pre-authorization of named external actions/payload classes:** more autonomous, but requires stronger payload binding, expiry, idempotency, and receipts.

### Decision C — registry writes

**Recommendation: C1.**

- **C1 — Preserve current Apex Sync rule:** non-dry-run registry write still requires explicit operator request.
- **C2 — Fold registry write into reusable authorization:** possible later, but this is a separate change from fixing Plan-to-Session duplicate confirmation.

## Missing source warning

The validation handover states that a fuller operator-saved project-source copy exists and should be located using phrases such as `one semantic approval gate`, `authorization envelope`, and `default_gate: exception_only`. Repository search at the handover commit found those phrases only in the handover itself. This validation therefore treats the fuller source as **unverified/missing**. If it is later located, compare it against this report before implementation and preserve any differences explicitly.

## Final recommendation

Proceed with the redesign **only after the operator chooses A/B/C above**. The smallest resilient version is:

> **Reuse a prior operator approval only for exact, pinned, action-scoped mutations whose approved basis, scope, constraints, and evidence still match; otherwise raise an exception gate.**

Do not add a broad inherited task-gating taxonomy unless later evidence shows the action-scoped model is insufficient.
