---
title: "FEE / Local Execution Layer — Operator Decision Lock, Round 3 — Local Model Execution"
doc_type: operator_decision_lock
initiative: local-orchestration-engine
created: 2026-08-08
authority: operator-session-2026-08-08
status: "local-model behavior Q&A complete; 7–8B is the primary research hypothesis, not a production lock; model/runtime selection remains research- and benchmark-gated"
depends_on:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-SELECTION-RESEARCH-GATE-2026-08-07.md
  - apex-meta/local-orchestration-engine/HANDOVER-2026-08-08-LOCAL-MODEL-QA-RESEARCH.md
  - apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md
  - apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md
  - apex-meta/orchestration/00-START-HERE.md
  - apex-meta/orchestration/workflows/orchestrator-run.md
  - apex-meta/orchestration/workflows/detective-review.md
branch_policy: "WORK DIRECTLY ON main ONLY. Do not create branches unless the operator explicitly asks for one."
---

# Operator Decision Lock — 2026-08-08, Round 3

## 1. Scope and correction

The operator completed and verified the deeper Local Model Decision Game required by the Local Model Selection Research Gate and Round-2 lock.

This document is the highest local authority for local-model execution behavior and research shaping inside the Local Orchestration Engine initiative.

**Correction recorded 2026-08-08:** an earlier draft interpreted the operator as wanting to move away from the 7–8B practical center toward the strongest/largest reasoning model that could fit. That was incorrect. The operator's intended position is:

> **7–8B is the expected practical optimum and primary research/bake-off center. It is a strong prior, not an irreversible lock.**

The research must therefore center 7–8B-class candidates, compare them against a smaller efficiency control, and test larger/higher-cost challengers only when they plausibly offer enough execution-quality gain to justify the additional resource burden.

This correction does **not** change the planner-routed model-selection decision. It corrects only the size/reasoning prior.

No model family, exact parameter count, quantization, runtime, executor platform or production configuration is selected here.

## 2. Core operating law

```text
Subscription / deep-reasoning AI
  -> substantive planning, synthesis, strategy, project-management intelligence

Scarce CLI AI (Claude Code / Codex)
  -> hard coding, architecture, difficult debugging, consequential technical work

Local-model execution layer
  -> bounded operational execution, constrained reasoning inside explicit authority,
     browser/tool operation, routine recovery, evidence preparation, bounded coding

Deterministic layer
  -> exact transforms, capability enforcement, schemas, validators, ledgers,
     checkpoints, routing enforcement, reproducible computation
```

Locked clarifications:

1. **Local models remain operators, not authority owners.** More reasoning never grants more authority by itself.
2. **7–8B is the working optimum hypothesis.** It is expected to provide the best balance of reasoning, tool reliability, latency and coexistence on the operator's machine.
3. **The hypothesis must still be tested.** A smaller model may win if it performs the approved flows equally well with materially better resource economics. A larger model may win a task class only if its measured gains justify its extra cost and coexistence impact.
4. **Do not optimize around 4B merely for footprint.** The operator's correction was intended to move above that smaller default assumption, toward the 7–8B practical center.

## 3. Pattern-before-invention law

For local execution, recovery, routing, containment, state, handoff, evaluation, browser operation, coding and human gates:

> **Identify established reference patterns first; adopt, adapt, combine or explicitly reject them before inventing an APEX-specific mechanism.**

External patterns are precedents, not APEX authority, and may not override the two APEX orchestration systems or operator locks.

Useful pattern families already identified include:

- orchestrator/worker and routing;
- worker-as-tool versus control handoff;
- durable checkpoint + interrupt/resume;
- retryable external activities with explicit recovery boundaries;
- generator/evaluator separation and independent review;
- least-privilege capability containment and sandboxing;
- tool-level guardrails rather than prompt-only safety;
- just-in-time context retrieval rather than context stuffing;
- trajectory + environment-outcome evaluation rather than answer-only grading.

Research prompts must verify current primary sources before treating any external pattern as implementation evidence.

## 4. Coding authority — locked

| ID | Decision | Locked meaning |
|---|---|---|
| LM-1 | **C — bounded micro-coder** | May execute exact patchspecs and make tiny locally inferred fixes only inside a severe scope/test envelope. No architectural change or open-ended feature work. |
| LM-2 | **C — tiered repair** | Deterministic retry -> known recovery -> mechanical repair -> at most one authorized micro-fix -> evidence + escalation. Ambiguous behavioral/architectural/security failures escalate. |
| LM-3 | **B — stage + commit on `main`, no automatic push initially** | May inspect/status/diff/stage/commit when explicitly granted. No branches/worktrees by default for this initiative; no auto-push. |
| LM-4 | **D — explicit multi-root/repo scope + dynamic retrieval** | A job may access one or more explicitly declared roots. Permission scope does not imply loading whole repos into context. |
| LM-5 | **C — failure-class escalation** | Known operational/mechanical failures stay local; ambiguity, architecture, unknown regression, security/permission problems, Git conflict and unexpected scope expansion escalate by type. |

### Micro-fix envelope

A locally inferred code fix requires all of:

- declared repository/root;
- bounded files/surface;
- no architecture change;
- no public API change unless explicitly specified;
- explicit acceptance test or validator;
- one local inferred-fix attempt maximum;
- unexpected diff/failure => stop and escalate.

Default-prohibited locally: branch/worktree proliferation, force push, destructive history rewrite/reset, branch deletion, arbitrary file deletion and undeclared cross-project Git operations.

## 5. Weekly Orchestrator execution — locked

| ID | Decision | Locked meaning |
|---|---|---|
| LM-6 | **C — explicit operational work packet** | Objective, roots, provider/tool, prompt/ref, allowed actions/follow-ups, capture, success, recovery and stop/escalation conditions are fixed before execution. |
| LM-7 | **B — closed-state classification** | Local model may classify among declared execution states, including `UNKNOWN`; it may not redesign the weekly flow. |
| LM-8 | **C — bounded conditional multi-turn** | Multi-turn subscription work follows predeclared conditional follow-up classes. |
| LM-9 | **C — declared upload/download scope** | May transfer only declared inputs/outputs under approved roots; missing files do not trigger semantic substitution. |
| LM-10 | **C — durable leave/restart/resume** | Job state lives outside model memory and resumes from persisted checkpoints/session references. |
| LM-11 | **C — per-task overnight repair/containment** | Blocked jobs checkpoint; independent safe jobs continue. Security/auth/consequential ambiguity halts the affected path. |
| LM-12 | **C — semantic bounded browser recovery** | May resolve UI changes to an equivalent already-declared intent; may not invent a new workflow or consequential mode. |
| LM-13 | **C — bounded concurrent scheduler** | Several jobs may be in flight, while active local inference/heavy operations remain resource-budgeted. |
| LM-14 | **C — decomposed multi-repo by default; explicit atomic cross-repo packets allowed** | Prefer repo-bounded jobs; permit atomic cross-repo work only with declared roots, acceptance checks and provenance. |
| LM-15 | **C — raw evidence preserved + derived execution index** | Structural extraction and small non-authoritative descriptions are allowed; downstream reasoning owns substantive interpretation. |

Weekly invariant:

```text
Weekly/deep reasoning
  -> frozen work packet
  -> durable scheduler/checkpoint
  -> browser/tools/files
  -> local closed-state judgement and bounded recovery
  -> raw evidence + execution index
  -> FlowRecap / stronger reasoning
```

## 6. Multi-Agent Orchestration support — locked

| ID | Decision | Locked meaning |
|---|---|---|
| LM-16 | **B — worker-as-tool / explicit workflow node** | Executes a bounded Meta Ops packet and returns result/evidence. Meta Ops retains orchestration. |
| LM-17 | **B — Detective evidence + contradiction candidates only** | May collect evidence and flag possible contradictions/anomalies; may not issue validity/authority verdicts. |
| LM-18 | **C — role-bounded support for KB, Informatics and Prompts & Workflows** | Each specialist may use local execution under its own capability contract. Semantic redesign remains with the owning reasoning role. |
| LM-19 | **B — candidate artifact creation allowed** | Local executor may create candidate artifacts; creation grants zero automatic authority. |
| LM-20 | **A — promotion boundary absolute** | Local executor never promotes candidate -> verified and never grants confirmed mutation. |
| LM-21 | **B — typed escalation + enforced router** | Local model classifies a failure/escalation type from a closed vocabulary; deterministic routing sends it to the correct destination. |
| LM-22 | **C — layered hostile-content containment** | Trust labels + capability broker + sandbox/allowlists + tool guards + approval gates. Captured content is data, never new authority. |

Authority ladder:

```text
local executor -> creates candidate
independent review -> may verify exact reviewed version
operator gate -> may confirm consequence
single gated mutation path -> may apply durable mutation
```

Model capability improvements do not change this ladder.

## 7. Model-shaping requirements — locked/open status

| ID | Status | Decision |
|---|---|---|
| LM-23 | **Locked** | **C — target ~32K reliably usable working context with just-in-time retrieval; benchmark 64K as stretch.** |
| LM-24 | **Locked** | **C — schema-constrained output + semantic validation + external capability guardrails + bounded retry.** |
| LM-25 | **Locked** | **C — reliability-first with bounded latency tolerance.** Optimize successful bounded jobs per wall time/intervention/escalation, not raw tokens/sec. |
| LM-26 | **Locked** | **B — laptop coexistence is a hard requirement.** Browser sessions, IDE/terminals, tests and occasional CLI agents must remain viable. |
| LM-27 | **Revised and locked conceptually** | **Planner-routed validated model selection.** A dedicated execution-planning/routing function analyzes each task and proposes a validated model/profile; deterministic policy validates the route before execution. |
| LM-28 | **OPEN BY DESIGN** | **Do not pre-lock one model, model ladder, generalist/coder split, or number of local models.** Benchmark evidence determines which profiles deserve registry entries. |
| LM-29 | **Runtime requirement; selection open** | Runtime must support Windows 11, reproducible config, stable local API, health/readiness, controlled load/unload/switching, structured output, context control, observability and resource measurement. |
| LM-30 | **Methodology locked** | Only benchmark-certified model+runtime configurations enter the routing registry; relevant regressions rerun after material configuration changes. |

## 8. Planner-routed model selection

```text
approved task/work packet
          |
          v
execution planner
  infers required capability profile
          |
          v
routing proposal
          |
          v
deterministic policy validator
  - profile is benchmark-certified for task class
  - context requirement fits
  - tool/authority contract fits
  - current resource budget permits it
  - fallback is valid
          |
          v
validated model+runtime profile
          |
          v
bounded execution
```

The execution planner is not a new APEX orchestration authority. It decides how much already-approved local capability a task needs, not what the project should do next.

## 9. Research objective — 7–8B-centered, evidence-gated

The research objective is:

> **Test the operator's hypothesis that a strong current 7–8B-class local model provides the optimal balance of reasoning quality, bounded execution reliability and laptop coexistence for APEX, while retaining smaller and larger comparators that can falsify that hypothesis.**

Research order/prior:

1. **Primary practical-center class: ~7–8B** — main shortlist and expected winner class.
2. **Efficiency control: ~3–4B** — establishes what can be done with less compute and whether 7–8B materially improves execution.
3. **Larger challenger: ~12–14B** — include when current runtime/hardware evidence makes local testing credible and when expected quality gains could justify the cost.
4. **Beyond ~14B:** only when concrete hardware/runtime evidence makes a configuration plausible enough to be decision-relevant; do not include merely because it reasons better on generic benchmarks.
5. **Coding-specialized challengers:** compare where they plausibly reduce CLI escalation, with the same authority envelope.

Do not treat these buckets as production locks. A 7–8B candidate remains a hypothesis until APEX fixtures and coexistence tests support it.

Do not select by generic leaderboard, advertised maximum context, raw tokens/sec or platform defaults.

## 10. Model + harness + runtime is the evaluated system

Evaluate:

```text
model artifact
+ representation/quantization
+ inference runtime/backend
+ generation configuration
+ prompt/work-packet contract
+ context/retrieval policy
+ schemas/tool interface
+ validators/guardrails
+ resource environment
```

Never report a model conclusion without identifying this configuration.

## 11. Hard benchmark gates

Final certification must distinguish:

1. structure validity;
2. semantic action/state correctness;
3. authority compliance;
4. unsafe/unauthorized trajectory attempts;
5. final environment/artifact outcome;
6. real resource/coexistence behavior.

System-level hard requirement:

> **Successful unauthorized actions must be zero.**

Unauthorized attempts remain model-quality failures even when containment blocks them.

False success, missed escalation, injection following, scope drift, wrong-root access and authority-promotion attempts are first-class metrics.

## 12. Machine profile

Known operator machine evidence:

```text
HP OmniBook X Flip 16-as0xxx
Windows 11
Intel Core Ultra 7 258V
~31.6 GB system RAM
Intel Arc 140V integrated graphics
```

Geekbench is hardware context only. Do not infer real LLM throughput or dedicated VRAM from it.

## 13. Research authorization

The Q&A prerequisite is complete. Authorized next steps:

1. benchmark/user-story portfolio;
2. current model landscape research centered on ~7–8B;
3. bounded-coding research;
4. Weekly + Multi-Agent model research;
5. Windows/Intel runtime research;
6. benchmark-harness design;
7. synthesis into planner-routed capability-profile hypotheses;
8. final operator model/runtime/bake-off decision.

Still not authorized:

- production model selection without evidence;
- production runtime selection without runtime/platform reconciliation;
- implementation that assumes an unvalidated topology;
- additional authority because a model is more capable;
- automatic challenger promotion;
- reopening the separation between Weekly and Multi-Agent Orchestration.

## 14. Success condition

Round 3 is satisfied when research can test the operator's **7–8B practical-optimum hypothesis** against smaller and larger controls while preserving planner routing, benchmark certification, real coexistence testing and unchanged APEX authority boundaries.
