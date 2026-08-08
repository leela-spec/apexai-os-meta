---
title: "FEE / Local Execution Layer — Operator Decision Lock, Round 3 — Local Model Execution"
doc_type: operator_decision_lock
initiative: local-orchestration-engine
created: 2026-08-08
authority: operator-session-2026-08-08
status: "local-model behavior Q&A complete; model/runtime selection remains research- and benchmark-gated"
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

## 1. Scope and authority

The operator completed and verified the deeper Local Model Decision Game required by the Local Model Selection Research Gate and Round-2 lock.

This document is now the **highest local authority for local-model execution behavior and local-model research shaping** inside the Local Orchestration Engine initiative.

It does **not** select a model family, parameter count, quantization, inference backend, runtime, executor platform, or production deployment configuration.

Where this document conflicts with Round 2 only on the deeper local-model questions that Round 2 explicitly left open, this Round-3 lock controls. Round-2 platform/FEE decisions remain authoritative.

Implementation remains gated. Research and benchmark design are now authorized.

## 2. Core operating law

The four-layer allocation remains:

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

Two clarifications are now locked together:

1. **Local models remain operators, not authority owners.** Better reasoning never grants more authority by itself.
2. **Local-model research is reasoning-first, not size-first.** Seek the strongest practically sustainable reasoning that materially improves approved execution behavior on the operator's machine. Do not optimize around the old 7–8B assumption or around "smallest model that barely passes."

A stronger local model is desirable when it improves bounded decisions such as ambiguous-state recognition, recovery classification, evidence comparison, tool selection, bounded code repair and correct escalation — while staying inside the same external authority envelope.

## 3. Pattern-before-invention law

The operator explicitly directed the project to avoid inventing orchestration mechanisms unnecessarily.

For local execution, recovery, routing, containment, state, handoff, evaluation, browser operation, coding and human gates:

> **Identify established reference patterns first; adopt, adapt, combine or explicitly reject them before inventing an APEX-specific mechanism.**

External patterns are precedents, not APEX authority. They may not override operator locks or the two APEX orchestration systems.

Reference families already found useful during the Q&A include:

- orchestrator/worker and routing patterns;
- worker-as-tool versus control handoff;
- durable checkpoint + interrupt/resume workflows;
- retryable external activities with explicit idempotency/recovery boundaries;
- generator/evaluator separation and independent review;
- least-privilege capability containment and sandboxing;
- tool-level guardrails rather than prompt-only safety;
- just-in-time context retrieval rather than maximum-context stuffing;
- trajectory + environment-outcome evaluation rather than answer-only grading.

These patterns are associated with current primary material from Anthropic, OpenAI, Microsoft Agent Framework, LangGraph and Temporal. Research prompts must verify current sources rather than relying on this list as implementation proof.

## 4. Coding authority — locked

| ID | Decision | Locked meaning |
|---|---|---|
| LM-1 | **C — bounded micro-coder** | May execute exact patchspecs and make tiny locally inferred fixes only inside a severe scope/test envelope. No architectural change or open-ended feature work. |
| LM-2 | **C — tiered repair** | Deterministic retry -> known recovery -> mechanical repair -> at most one authorized micro-fix -> evidence + escalation. Ambiguous behavioral/architectural/security failures escalate. |
| LM-3 | **B — stage + commit on `main`, no automatic push initially** | May inspect/status/diff/stage/commit when the job grants the capability. No branches/worktrees by default for this initiative; no auto-push. |
| LM-4 | **D — explicit multi-root/repo scope + dynamic retrieval** | A job may access one or more explicitly declared repositories/roots. Permission scope does not imply context stuffing; retrieve bounded slices as needed. |
| LM-5 | **C — failure-class escalation** | Known operational/mechanical failures stay local; ambiguity, architecture, unknown regression, security/permission problems, Git conflict and unexpected scope expansion escalate by type. |

### 4.1 Micro-fix envelope

A locally inferred code fix requires all of:

- declared repository/root;
- bounded files/surface;
- no architecture change;
- no public API change unless the work packet explicitly specifies it;
- explicit acceptance test or validator;
- one local inferred-fix attempt maximum;
- unexpected diff/failure => stop and escalate.

### 4.2 Git hard boundaries

Default-prohibited locally:

- branch creation or worktree proliferation for this initiative;
- force push;
- history rewrite;
- hard reset used destructively;
- branch deletion;
- arbitrary file deletion;
- undeclared cross-project Git operations.

## 5. Weekly Orchestrator execution — locked

The local execution layer supports Weekly execution without becoming Weekly reasoning authority.

| ID | Decision | Locked meaning |
|---|---|---|
| LM-6 | **C — explicit operational work packet** | Objective, roots, provider/tool, prompt/ref, allowed actions/follow-ups, capture, success, recovery and stop/escalation conditions are fixed before execution. |
| LM-7 | **B — closed-state classification** | Local model may classify among declared execution states, including `UNKNOWN`; it may not redesign the weekly flow. |
| LM-8 | **C — bounded conditional multi-turn** | Multi-turn subscription work is allowed through predeclared conditional follow-up classes. No free research conversation owned by the local model. |
| LM-9 | **C — declared upload/download scope** | May transfer only declared inputs and outputs under approved artifact roots; missing/ambiguous files do not trigger semantic substitution. |
| LM-10 | **C — durable leave/restart/resume** | Job state lives outside model memory. Long provider waits and process restarts resume from persisted checkpoints/session references. |
| LM-11 | **C — per-task overnight repair/containment** | Blocked job checkpoints; independent dependency-safe jobs continue. Security/auth/consequential ambiguity halts the affected path. |
| LM-12 | **C — semantic bounded browser recovery** | May resolve presentation/UI changes to an equivalent already-declared intent; may not invent a new browser workflow or choose new consequential modes. |
| LM-13 | **C — bounded concurrent scheduler** | Several jobs may be in flight, but local inference/heavy operations are resource-budgeted. Waiting remotely is not equivalent to keeping many models active. |
| LM-14 | **C — decomposed multi-repo by default; explicit atomic cross-repo packets allowed** | Prefer repo-bounded jobs; allow truly atomic cross-repo work only with declared roots, acceptance checks and provenance. |
| LM-15 | **C — raw evidence preserved + derived execution index** | Raw provider/tool/browser evidence remains available; structural extraction and small non-authoritative description are allowed, but FlowRecap/downstream reasoning owns substantive interpretation. |

### 5.1 Weekly execution invariant

```text
Weekly/deep reasoning
  -> frozen work packet
  -> durable scheduler/checkpoint
  -> browser/tools/files
  -> local closed-state judgement and bounded recovery
  -> raw evidence + execution index
  -> FlowRecap / stronger reasoning
```

The graph/work packet owns sequence. The local model supplies judgement **inside nodes**, not project-level replanning.

## 6. Multi-Agent Orchestration support — locked

The local model supports Multi-Agent Orchestration without becoming Alfred, Meta Strategy, Meta Ops or Meta Detective.

| ID | Decision | Locked meaning |
|---|---|---|
| LM-16 | **B — worker-as-tool / explicit workflow node** | Executes a bounded Meta Ops packet and returns result/evidence. Meta Ops retains orchestration and continuation. |
| LM-17 | **B — Detective evidence + contradiction candidates only** | May collect hashes/diffs/tests/source refs and flag possible contradictions/anomalies. It may not issue validity/authority verdicts. |
| LM-18 | **C — role-bounded support for KB, Informatics and Prompts & Workflows** | Each specialist may use local execution under its own capability contract. Semantic redesign/authority remains with the owning reasoning role. |
| LM-19 | **B — candidate artifact creation allowed** | Local executor may create useful candidate artifacts; creation grants zero automatic authority. |
| LM-20 | **A — promotion boundary absolute** | Local executor never promotes candidate -> verified and never grants confirmed mutation. Independent review and operator confirmation remain mandatory where required. |
| LM-21 | **B — typed escalation + enforced router** | Local model classifies a failure/escalation type from a closed vocabulary; deterministic routing sends it to the correct destination. Meta Ops retains orchestration ownership. |
| LM-22 | **C — layered hostile-content containment** | Trust labels + capability broker + sandbox/allowlists + tool guards + approval gates. Captured content is data, never new execution authority. |

### 6.1 Authority ladder

```text
local executor
  may CREATE candidate
        |
        v
independent Detective/review
  may VERIFY exact reviewed version
        |
        v
operator gate
  may CONFIRM consequence
        |
        v
single gated mutation path
  may APPLY durable mutation
```

Model capability improvements do not change this ladder.

## 7. Model-shaping requirements — locked/open status

| ID | Status | Decision |
|---|---|---|
| LM-23 | **Locked** | **C — target ~32K reliably usable working context with just-in-time retrieval; benchmark 64K as stretch.** Advertised maximum context is secondary. |
| LM-24 | **Locked** | **C — schema-constrained output + semantic validation + external capability guardrails + bounded retry.** Valid JSON is not equivalent to authorized/correct action. |
| LM-25 | **Locked** | **C — reliability-first with bounded latency tolerance.** Optimize successful bounded jobs per wall time/intervention/escalation, not raw tokens/sec. |
| LM-26 | **Locked** | **B — laptop coexistence is a hard requirement.** Browser sessions, IDE/terminals, tests and occasional CLI agents must remain viable. |
| LM-27 | **Revised and locked conceptually** | **Planner-routed validated model selection.** A dedicated execution-planning/routing function analyzes each task and proposes a validated model/profile; deterministic policy validates the route before execution. |
| LM-28 | **OPEN BY DESIGN** | **Do not pre-lock one model, model ladder, generalist/coder split, or number of local models.** Benchmark evidence determines which capability profiles deserve registry entries. |
| LM-29 | **Runtime requirement; selection open** | Runtime must support Windows 11, reproducible config, stable local API, health/readiness, controlled model load/unload/switching, structured output, context control, observability and resource measurement. Exact runtime remains research-gated. |
| LM-30 | **Methodology locked** | Only benchmark-certified model+runtime configurations enter the routing registry. Relevant regression suites rerun when model, runtime, prompts, tools, guards, context/retrieval or environment materially change; challenger configurations do not auto-promote. |

## 8. Planner-routed model selection

LM-27 replaces the earlier assumption that architecture must choose one default plus one fallback in advance.

Target shape:

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
  - profile/model is benchmark-certified for this task class
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

The execution planner is **not a new APEX orchestration authority**. It is a bounded Local Orchestration Engine function. It decides how much local capability an already-approved task needs, not what the project should do next.

The planner may only route to model/runtime profiles already present in a validated registry.

Example registry shape:

```yaml
validated_profiles:
  <profile_id>:
    model_artifact: null
    runtime: null
    certified_task_classes: []
    reasoning_tier: null
    context_tested: []
    resource_envelope: {}
    known_failure_classes: []
    benchmark_ref: null
```

## 9. Research objective — reasoning-first, evidence-gated

The research objective is now:

> **Find the highest-reasoning local model/runtime configurations that materially improve approved APEX execution behavior and remain operationally sustainable on the operator's Windows laptop, then certify task-specific profiles for planner routing.**

Do not preselect by:

- parameter count;
- 7–8B legacy preference;
- generic coding leaderboard;
- maximum advertised context;
- raw tokens/second;
- platform default model.

Parameter size becomes an observed characteristic, not the decision axis.

Research should include:

- an efficient baseline/control class;
- strong reasoning primary candidates;
- higher-reasoning stretch candidates when hardware/runtime evidence makes them plausible;
- coding-reasoning challengers;
- architecture/runtime-efficient challengers that may deliver high reasoning per resident resource.

A substantially larger model may win if it yields meaningfully better APEX outcomes and remains sustainable. A larger model loses if it materially harms coexistence or does not buy meaningful reduction in errors/escalations.

## 10. Model + harness + runtime is the evaluated system

Candidate evaluation must treat this as the unit under test:

```text
model artifact
+ quantization / representation
+ inference runtime/backend
+ generation configuration
+ prompt/work-packet contract
+ context/retrieval policy
+ schemas/tool interface
+ validators/guardrails
+ resource environment
```

Do not attribute harness failures to the model or model failures to the harness without evidence.

## 11. Hard benchmark gates

At minimum, final candidate certification must make the following distinctions measurable:

1. **Structure:** did the model produce schema-valid output?
2. **Semantics:** did it select the correct action/state/escalation?
3. **Authority:** was the requested action permitted?
4. **Trajectory:** did it attempt unauthorized scope expansion or unsafe recovery?
5. **Outcome:** did the environment/artifact end in the correct state?
6. **Resource:** did it remain operationally sustainable under real coexistence load?

System-level safety requirement:

> **Successful unauthorized actions must be zero.**

Unauthorized attempts remain model-quality failures even when containment blocks them.

False success, missed escalation, injection following, scope drift, wrong-root access and authority promotion attempts are first-class metrics.

## 12. Machine profile for runtime research

Known operator machine evidence:

```text
HP OmniBook X Flip 16-as0xxx
Windows 11
Intel Core Ultra 7 258V
~31.6 GB system RAM
Intel Arc 140V integrated graphics
```

Do not infer real LLM throughput or usable dedicated VRAM from Geekbench alone. The runtime research and local benchmark must measure actual APEX workloads and coexistence.

## 13. Research authorization

The Q&A prerequisite is now complete.

Authorized next steps:

1. materialize the benchmark/user-story portfolio;
2. run current model-landscape research;
3. run bounded-coding model research;
4. run Weekly + Multi-Agent execution model research;
5. run Windows/Intel runtime research;
6. design the reproducible benchmark harness;
7. synthesize all evidence into a planner-routed capability-registry recommendation;
8. return to the operator for final model/runtime/bake-off decisions.

Still **not** authorized by this lock:

- selecting a production local model without research + benchmark evidence;
- selecting a production runtime without platform/runtime reconciliation;
- implementation that assumes an unvalidated model topology;
- granting additional authority because a model is more capable;
- auto-promoting a benchmark challenger into production;
- reopening the separation between Weekly Orchestrator and Multi-Agent Orchestration.

## 14. Success condition

Round 3 is satisfied when research and benchmark work can proceed from a stable, operator-confirmed behavioral contract without presupposing a model family, size or topology — and when final selection is framed as **planner routing among benchmark-certified high-reasoning local execution profiles under unchanged APEX authority boundaries**.
