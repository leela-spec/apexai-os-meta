# Fable Orchestration — Iterative Completion Plan (validated against current checkout)

## Context

The uploaded build-plan (M0–M9) is a recovery plan written for a chat that lost state. This session **has** the state: much of M1–M6 is already built, tested, and pushed on `claude/fable-orchestrator-setup-9pc5pu`. The corrected plan below keeps the uploaded plan's gates and Definition of Done, marks what is already done with evidence, and executes only the genuinely remaining work — no renames of working files, no redone milestones, no trivial-task ceremony.

Operator gate answers just collected (recorded as `operator_validation: confirmed` this turn):
- **G1 = accept + write lesson** → US-IDEA-01 stage 6 mutation is authorized (one numbered lesson into `fable-execution-best-practices.md`, bounded).
- **G2 = approve registry write** → `apex_sync.py registry --dry-run false` authorized (preview + drift already on record).
- **Push target = `main`** (the operator merged `claude/fable-orchestrator-setup-9pc5pu` into `main` on 2026-07-12 to keep one working surface; commit to `main` after each iteration, no other branches).

## Model routing per iteration (operator switches models manually between iterations)

The operator runs Claude Code interactively and pays per token/model tier. Iterations differ sharply in how much genuine judgment vs. mechanical execution they require, so each is assigned the cheapest model that won't compromise the review/contract guarantees this system exists to prove. **The agent must stop at the end of every iteration, commit, and tell the operator exactly which model to select next before continuing** — never assume the operator has already switched.

| Iteration | Work | Recommended model | Mode | Why |
|---|---|---|---|---|
| 1 | Close US-IDEA-01 stage 6 + M0 manifest | **Sonnet 5** | standard | One bounded content write + running an existing script + an inventory file. No open judgment calls. |
| 2 | `orchestration_check.py` + negative fixtures + small schemas | **Sonnet 5** | standard | Deterministic script authoring mirroring an existing convention (`apex_sync.py`); fixtures are enumerated, not discovered. |
| 3–6 | The six story simulations (core work: live agent dispatch, meta-strategy/meta-detective judgment, cross-asset consistency, catching real contract defects) | **Opus 4.8** | high (xhigh for US-WORKSHOP-01's safety-boundary story and US-COMP-01's compliance/external-authority story) | This is where the system's actual claims get tested. Under-thinking here reproduces the exact failure this system was built to prevent: a reviewer or worker silently smoothing over a defect instead of routing it back. Not a cost-saving target. |
| 7 | Resilience/efficiency evaluation, token measurement, KB audit re-score | **Sonnet 5** for gathering the recorded token/tool-call numbers and running the remaining behavioral probes; **Opus 4.8 (high)** only for the repair/escalation judgment calls and any high-cost-stage optimization decision | mixed — switch mid-iteration if needed, and say so when stopping | Data collection is mechanical; deciding what a contradictory-return or reviewer-disagreement probe *means* is not. |
| 8 | Final truth + acceptance report, Definition-of-Done | **Opus 4.8** | high | Synthesis across the whole system with real stakes (the acceptance claims must be evidence-backed, not optimistic). Cheapest place to under-invest is also the place a wrong verdict costs the most to unwind. |

Stop-and-switch protocol: after each iteration's commit, the agent reports what was done, then states plainly: *"Iteration N done and committed. Select model **X** before continuing to Iteration N+1."* It does not start the next iteration in the same turn even if the operator hasn't responded yet.

## Validation of the uploaded plan (what's already DONE — will not redo)

| Uploaded milestone | Status in checkout | Evidence |
|---|---|---|
| M1 architecture | DONE | `apex-meta/orchestration/ARCHITECTURE.md` (incl. invocation modes: Alfred+Meta Ops = main-conversation contracts; rest spawned) |
| M4 doctrine migration | DONE | `agents/DOCTRINE-MANIFEST.md`; 39 sha256-verified copies; 227 files classified (MOVE/REFERENCE/SKIP) |
| M5 plan/sync/session integration | DONE (contract + real sync runs) | `agents/meta-ops/INTEGRATION-apex-plan-sync-session.md`; real registry/drift runs in US-IDEA-01 |
| M6 review/correction loop | DONE, with a real defect caught | US-IDEA-01: blind parallel lenses → validity `revise` (2 real defects) → diff-proven v2 → scoped re-review pass |
| M7 story 1 of 7 | DONE through stage 5 | `simulations/US-IDEA-01-20260711/` + record file |
| Weekly Orchestrator boundary | respected | zero writes to weekly paths this session; will keep classifying `weekly_out_of_scope` |

Corrections to the uploaded plan: existing filenames stay (`schemas/*.schema.md`, `simulations/US-IDEA-01-20260711/`); `correction-and-revalidation` stays inside `detective-review.md` (it's already there and executed — a separate file would be duplication).

## Remaining work — iteration order (commit+push branch after each)

### Iteration 1 — Close US-IDEA-01 stage 6 + M0 manifest
- Execute the two authorized mutations per the apex-session pattern: (a) add ONE numbered lesson (repo-grounded external prompts: name system/folders/KBs) to `apex-meta/fable-orchestrator/fable-execution-best-practices.md` — content from verified `01-candidate-entry.v2.md`, no restructure; (b) run `python3 scripts/apex_sync.py registry --root . --dry-run false`, fetch back and verify `apex-meta/registry/index.md` matches the preview. Write `10-mutation-record.md` (status mutation record with `operator_validation: confirmed`, before/after) in the run folder; update the simulation record verdict to full PASS.
- Create `apex-meta/orchestration/CURRENT-SYSTEM-MANIFEST.yaml` (M0): branch/HEAD, inventory of every current component (reuse/adapt/historical/weekly_out_of_scope), exact paths.

### Iteration 2 — M2 gaps: enforcement + negative tests (fail-closed)
- `scripts/orchestration_check.py` (stdlib-only, mirroring apex_sync.py conventions): validates handoff-packet required fields, recomputes/compares sha256 digests, checks authority-closure precondition for canon writes (`operator_validation: confirmed` ∧ inputs `verified` ∧ digests match). `--json`, exit non-zero on violation.
- `apex-meta/orchestration/tests/negative/` — 5 fixtures, each must fail closed through the script: candidate-to-canon leakage, stale digest, missing evidence ref, reviewer-wrote-correction, unauthorized write (no operator_validation). Record results in `tests/negative/RESULTS.md`.
- `schemas/run-record.schema.md` (small): run_id, attempt, supersession, resume pointer — formalizing what US-IDEA-01's run folder already does.
- `workflows/operator-gate.md` (small): the G-item presentation/answer/record protocol used in 09-gate-presentation, generalized.
- Resume test (M8 item, done here since it's the same surface): demonstrate a run continues from durable files + run_id alone; record under `tests/behavioral/`.

### Iterations 3–6 — M7: the six remaining story simulations (the core work)
Order per uploaded plan: US-SEQ-01 → US-MEDIA-01 → US-LEELA-01 → US-WORKSHOP-01 → US-OFFER-01 → US-COMP-01 (1–2 stories per iteration, commit between). Each run:
- real repo input (each story's `repository_refs` name real source files in the old-apex KB — Master-of-Arts workflow DB, ProcessRanking),
- required agents actually spawned (this also completes M3's live-dispatch evidence: meta-strategy first spawns in US-SEQ-01, informatics-design + parallel worker fan-out in US-MEDIA-01, prompts-workflows in US-SEQ-01/US-WORKSHOP-01),
- handoff packets parse (checked with `orchestration_check.py`),
- Detective review where consequential; operator/professional boundaries held (safety reviewer in WORKSHOP, professionals in COMP are *recorded as required externals*, not simulated away),
- honest `simulation_record` per the uploaded YAML shape (pass/partial/fail + defects), one folder per story under `simulations/`.
- Live-dispatch + parse evidence recorded under `apex-meta/orchestration/tests/behavioral/`.
- Repair-and-rerun rule: a failed story fixes the owning component and reruns before advancing; failed attempt preserved.

### Iteration 7 — M8: resilience + efficiency evaluation
- Remaining behavioral probes not already evidenced: contradictory worker returns (route-back, no silent merge), invalid handoff twice (reject → escalate), reviewer disagreement (hold/escalate path), same-command idempotence (apex_sync reruns byte-identical), unauthorized mutation attempt (script fails closed — from Iteration 2).
- `tests/token-and-context-evaluation.md`: per-agent measurements from recorded subagent usage across all runs (tokens, tool calls, duration — real numbers already captured per spawn), plus input-slice sizes; optimize any high-cost stage found.
- Move/extend the existing KB audit into `tests/system-audit-vs-orchestration-design-kb.md` (already written; re-score anything the new work changed).

### Iteration 8 — M9: final truth + acceptance
- Regenerate `CURRENT-SYSTEM-MANIFEST.yaml` from final files; validate every path; update `00-START-HERE.md`/`ARCHITECTURE.md` status lines to direct evidence.
- Final acceptance report per the uploaded `completion_report` shape (commit/branch, spawn results, doctrine counts, plan/sync/session tests, seven story verdicts, negative/resume results, token measurements, weekly boundary check, genuine external limitations — e.g. Claude-only review family, safety/professional externals).
- Final commit+push (branch). Definition-of-Done checklist answered item-by-item with evidence paths — no `true` without a file behind it.

## Verification
- Every iteration ends with: artifact built → smallest proving test run (script exit codes, spawn returns, parse checks) → commit+push to `claude/fable-orchestrator-setup-9pc5pu`.
- The uploaded plan's per-milestone gates are the acceptance criteria; failures are repaired in-iteration, never deferred by relabeling.