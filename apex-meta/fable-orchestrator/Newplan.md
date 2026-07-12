# Fable Orchestration — Iterative Completion Plan (validated against current checkout)

## Context

The uploaded build-plan (M0–M9) is a recovery plan written for a chat that lost state. This session **has** the state: much of M1–M6 is already built, tested, and pushed on `claude/fable-orchestrator-setup-9pc5pu`. The corrected plan below keeps the uploaded plan's gates and Definition of Done, marks what is already done with evidence, and executes only the genuinely remaining work — no renames of working files, no redone milestones, no trivial-task ceremony.

Operator gate answers just collected (recorded as `operator_validation: confirmed` this turn):
- **G1 = accept + write lesson** → US-IDEA-01 stage 6 mutation is authorized (one numbered lesson into `fable-execution-best-practices.md`, bounded).
- **G2 = approve registry write** → `apex_sync.py registry --dry-run false` authorized (preview + drift already on record).
- **Push target = `main`** (the operator merged `claude/fable-orchestrator-setup-9pc5pu` into `main` on 2026-07-12 to keep one working surface; commit to `main` after each iteration, no other branches).

## Doctrine efficiency work (done 2026-07-12, before Iteration 4) — see plan `this-sounds-like-a-scalable-cherny`

Executed Fixes 1+2+3 from the approved efficiency plan, ahead of Iteration 4:
- **Fix 1 (done):** `CORE.md` created for the 4 populated roles (`meta-detective`, `knowledge-bank`,
  `informatics-design`, `prompts-workflows`) — distilled operational cores replacing a fresh full
  doctrine re-read every spawn. Measured: 2,935 → 326 lines (~89% reduction) across the four chains,
  with the manifest-binding parts (1-100 metric convention, 5-mode boundaries) preserved verbatim.
  `.claude/agents/<role>.md` doctrine-read lines updated to point at `CORE.md` first.
- **Fix 2 (done):** repaired the 404 — `alfred`/`meta-strategy`/`meta-ops` were instructed to read
  BEST_PRACTICES/MISTAKES files that were never populated (SKIP-ped in migration). Runtime `.md`
  files now correctly point at `ESSENCE.md` only for these three thin roles.
- **Fix 3 (done):** added optional `sources_excerpt` field to `handoff-packet.schema.md` — lets a
  packet author who already has a source file open pass pre-extracted cited lines to a reviewer,
  without removing the reviewer's full-file access or carrying any producer rationale (independence
  invariants unaffected; regression-tested against `orchestration_check.py` and existing fixtures).
- **Root-cause fix (found during verification):** `DOCTRINE-MANIFEST.md`'s own central "read order"
  rule still said the old ESSENCE→BEST_PRACTICES→MISTAKES→TEMPLATES chain, and since the runtime
  contract also tells agents to consult that manifest for translation rules, it was overriding the new
  `CORE.md`-first pointer. Fixed the manifest's read-order section to say CORE.md-first explicitly.

**Verification status — honest, not fully closed:** file/path/schema checks all pass (zero 404s,
regression suite green, doctrine size reduction confirmed on disk). The live behavioral A/B re-test
(re-running US-SEQ-01's stage-2 assumption-check against the same frozen v1 memo) was inconclusive on
the token-savings claim specifically: two consecutive spawns in *this* session — one before and one
after the `DOCTRINE-MANIFEST.md` fix — both still read the full ESSENCE/BEST_PRACTICES/MISTAKES chain
and never opened `CORE.md`, despite the on-disk runtime file being confirmed correct. Likely cause:
Claude Code appears to snapshot a custom subagent's system prompt when its type first becomes
available in a session, so mid-session edits to `.claude/agents/*.md` may not take effect for spawns
in that same session. **Next verification step: re-run the same US-SEQ-01 stage-2 A/B test in a fresh
session** (e.g., when Iteration 4 begins) and confirm token count drops meaningfully below the
82,839-token baseline with `CORE.md` actually being the file opened. Content quality was not in
question either way — both re-test runs still independently caught the same substantive defects.

## Model routing per iteration (operator switches models manually between iterations)

The operator runs Claude Code interactively and pays per token/model tier. Iterations differ sharply in how much genuine judgment vs. mechanical execution they require, so each is assigned the cheapest model that won't compromise the review/contract guarantees this system exists to prove. **The agent must stop at the end of every iteration, commit, and tell the operator exactly which model to select next before continuing** — never assume the operator has already switched.

| Iteration | Work | Recommended model | Mode | Why |
|---|---|---|---|---|
| 1 | Close US-IDEA-01 stage 6 + M0 manifest | **Sonnet 5** | standard | One bounded content write + running an existing script + an inventory file. No open judgment calls. |
| 2 | `orchestration_check.py` + negative fixtures + small schemas | **Sonnet 5** | standard | Deterministic script authoring mirroring an existing convention (`apex_sync.py`); fixtures are enumerated, not discovered. |
| 3–6 | The six story simulations (core work: live agent dispatch, meta-strategy/meta-detective judgment, cross-asset consistency, catching real contract defects) | **Opus 4.8** | **per-role split, not blanket high** (see "Per-role effort split" below); xhigh for US-WORKSHOP-01's safety-boundary review and US-COMP-01's compliance/external-authority review specifically | This is where the system's actual claims get tested. Under-thinking the *review* passes reproduces the exact failure this system was built to prevent — a reviewer silently smoothing over a defect instead of routing it back. But not every spawn in a story is a review pass; blanket-high was measured as real waste in Iteration 3 (see below). |
| 7 | Resilience/efficiency evaluation, token measurement, KB audit re-score | **Sonnet 5** for gathering the recorded token/tool-call numbers and running the remaining behavioral probes; **Opus 4.8 (high)** only for the repair/escalation judgment calls and any high-cost-stage optimization decision | mixed — switch mid-iteration if needed, and say so when stopping | Data collection is mechanical; deciding what a contradictory-return or reviewer-disagreement probe *means* is not. |
| 8 | Final truth + acceptance report, Definition-of-Done | **Opus 4.8** | high | Synthesis across the whole system with real stakes (the acceptance claims must be evidence-backed, not optimistic). Cheapest place to under-invest is also the place a wrong verdict costs the most to unwind. |

Stop-and-switch protocol: after each iteration's commit, the agent reports what was done, then states plainly: *"Iteration N done and committed. Select model **X** before continuing to Iteration N+1."* It does not start the next iteration in the same turn even if the operator hasn't responded yet.

### Token-efficiency learning from Iteration 3 (US-SEQ-01) — candidate, operator-reviewed, applies starting Iteration 4

**Status: candidate learning, not yet promoted into `fable-execution-best-practices.md`** (per the
system's own rule — after-action learning stays candidate until independently reviewed and
operator-accepted; no agent rewrites its own doctrine). Recorded here in the operative plan because
the operator asked for it directly and it governs *how* the remaining iterations run, not a canon
doctrine change.

**Measured cost, US-SEQ-01 stage 2 alone:** ~172K tokens / ~10.5 min across 3 spawns (detective
assumption-check 82,839 tok, strategy correction 47,466 tok, scoped re-review 41,434 tok) — for ONE
story's stage 2, before the heavier fan-out stories (US-MEDIA-01 alone: 4 domain workers + 2
specialists). Blanket "Opus high for every spawn" does not scale to the remaining 5 stories.

**Root cause of the cost (not the effort setting):**
1. Every spawn is a fresh isolated context, so both `meta-detective` spawns in US-SEQ-01 independently
   re-read the *same* ~95KB of source KB files (Hermes DB + ProcessRanking) from scratch — no sharing
   across spawns.
2. `meta-detective`'s doctrine chain (ESSENCE+BEST_PRACTICES+MISTAKES+TEMPLATES,
   `apex-meta/orchestration/agents/meta-detective/`) is ~1,150 lines, also re-read fresh on every
   spawn, every story — it does not change between spawns within a run.
3. The `review_verdict` schema's three prose fields per criterion (`falsification_attempt`,
   `evidence_refs`, `reasoning_summary`) are output-token-heavy even for a narrow, already-scoped
   re-review.

**Per-role effort split (replaces blanket "high" for Iterations 4-6):**

| Role / stage | Effort | Why |
|---|---|---|
| meta-strategy — macro framing (drafting theses/options) | **medium** | Generative, not adversarial; rigor is supplied downstream by review, not by self-checking. |
| meta-detective — first-pass assumption-check / validity / alignment | **high** | This is where subtle overstatement gets caught (US-SEQ-01's C3: conflating "the act of writing a positioning doc" with "the specific positioning content" — a genuinely subtle distinction a shallower pass plausibly misses). Do not cut here. |
| meta-strategy / domain worker — applying routed corrections | **medium** | Bounded, specified fixes; care in re-verifying anchors against source matters more than reasoning depth. |
| meta-detective — scoped re-review (named criteria only) | **high**, but keep the *scope* narrow | Last gate before `authority: verified`; keep effort, don't keep breadth. |
| domain workers (coaching-method, pilot-design, media, script, offer-copy, etc. — Iterations 4-6) | **medium** | Narrow, source-grounded production tasks, not adversarial judgment. |
| US-WORKSHOP-01 safety review, US-COMP-01 compliance/external-authority review | **xhigh** | Unchanged — genuinely high-stakes, narrow-scope reviews where the cost is justified. |

**Process changes to reduce redundant re-reads (apply starting Iteration 4, not retroactive to
already-committed Iteration 3 work):**
- Where a story's stage reviews the same source material across multiple spawns (e.g. assumption-check
  → re-review), give the agent a **pre-extracted excerpt pack** (the specific cited lines ± a few lines
  of context) instead of pointing it at the full source file to re-open from scratch each time. Full-file
  access stays available if the agent needs to verify something outside the excerpt — this is a default,
  not a hard restriction.
- Keep re-reviews criterion-scoped (already the design, per `detective-review.md` step 8) and keep the
  verdict schema's fuller three-block-per-criterion shape for stage-6 dual-lens milestone reviews;
  lighter stage-2-style checks may compress `falsification_attempt` + `reasoning_summary` into one field.

**What NOT to change:** the review loop itself, the blind/parallel protocol, the diff-proof requirement
for corrections, or the operator-gate boundary. The cost lesson is about redundant context and
effort-per-role, not about reviewing less rigorously.

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