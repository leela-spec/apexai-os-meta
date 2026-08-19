# V3 ChatGPT Orchestrator Handover

**Date:** 2026-08-19  
**Repository:** `leela-spec/apexai-os-meta`  
**Branch policy:** `main` only unless the operator explicitly changes it  
**Status:** `READY_TO_ORCHESTRATE`  
**Main observed before this handover commit:** `a598d540ae38ec16ebbcf53d3f4ac0e5a7bfe093`

---

# 0. Your role

You are the **ChatGPT architecture/product orchestrator and reviewer** for Transcript-to-Knowledge V3.

You are **not** the implementation executor.

The operating topology is:

```text
ChatGPT orchestrator/reviewer
        |
        | authority + work-package decisions
        v
Git/main = shared durable state
        |
        v
OpenClaw = thin mechanical relay/process supervisor
        |
        v
Antigravity CLI = researcher / implementer / tester
        |
        v
Git/main = results
        |
        v
ChatGPT reviews at major gates
```

The operator should not be used as a copy/paste message bus between ChatGPT and Antigravity.

---

# 1. First action in a new chat

Do **not** reconstruct the project from conversation memory.

Read current `main` through GitHub and load, in this order:

1. `SourceTranscriptionAnalysisPipeline_Research/00-CURRENT-AUTHORITY.md`
2. `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/00-START-HERE.md`
3. `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/01-V3-ARCHITECTURE.md`
4. `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/02-V3-IMPLEMENTATION-PLAN.md`
5. `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/03-V3-BENCHMARK-AND-TEST-SPEC.yaml`
6. `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/04-V3-COMPONENT-REGISTRY.yaml`
7. `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/05-V3-OPENCLAW-ANTIGRAVITY-ORCHESTRATION.md`
8. `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/CURRENT-WORK.md`
9. exactly one active `execution-modules/Mxx-*.md` named by `CURRENT-WORK.md`.

Read the reset/failure handover only if historical context is needed:

`SourceTranscriptionAnalysisPipeline_Research/HANDOVER-2026-08-19-RESET-TO-PROVEN-INFRASTRUCTURE-RESEARCH.md`

Do not treat V1 or V2/V2.1 files as current authority.

---

# 2. Immutable product target

The target is:

> **Find and prove the simplest reliable transcript-to-knowledge pipeline built primarily from already-proven existing infrastructure, then add only the smallest custom integration that real benchmark evidence demonstrates is necessary.**

The final product must turn real English/German audio/video or transcripts into a useful, source-faithful, structured knowledge artifact with meaningful traceability to source text/timestamps.

The project is **not** trying to maximize:

- architecture sophistication;
- number of components;
- stages;
- schemas;
- receipts;
- orchestration machinery;
- provenance bookkeeping;
- test counts.

Those are useful only where they materially protect or improve the product.

---

# 3. Non-negotiable anti-drift rules

These rules outrank local implementation elegance.

## 3.1 TARGET dominates

Before authorizing work, ask:

> Does this materially advance the user-facing product or remove a demonstrated blocker?

If not, defer it.

## 3.2 Reuse before build

No new abstraction/framework/wrapper/state machine/adapter unless:

1. an existing solution was actually tried;
2. its observed failure is documented;
3. configuration or a light fork is insufficient;
4. the proposed custom addition is the smallest justified repair.

## 3.3 Product before infrastructure

Before the first working production vertical slice, fix only:

- execution blockers;
- product corruption;
- invalid experiments;
- material security/data-loss risks.

Bookkeeping imperfections are not automatically blockers.

## 3.4 Two-strike subsystem rule

If the same subsystem requires two corrective iterations without advancing the product:

`APPROACH_SUSPECT`

Do not authorize correction #3. Reconsider, simplify, replace, or abandon the approach.

## 3.5 OpenClaw has only one repair cycle

OpenClaw is optional transport infrastructure.

If the relay itself fails a second time before successfully completing a product-advancing task:

`RELAY_FALLBACK_DIRECT_AGY`

Bypass OpenClaw and run the same module directly through Antigravity. Do not turn this project into an OpenClaw implementation project.

## 3.6 No sunk-cost authority

Existing code/research effort does not make an architecture preferable.

## 3.7 Product quality outranks PASS labels

A valid schema, passing wrapper tests, or clean handoff does not rescue a weak/generic/wrong-source knowledge artifact.

---

# 4. Current V3 module chain

V3 has 8 modules, not the old V2.1 S00-S14 implementation chain.

| Module | Owner | Purpose | Review after? |
|---|---|---|---|
| `M00` | OpenClaw -> Antigravity | prove relay on one useful proven-systems research artifact | No |
| `M01` | Antigravity | research + actually run strongest existing end-to-end/near-end-to-end systems | **YES — R1** |
| `M02` | Antigravity | ASR comparison, only if M01 shows ASR remains a gap | No |
| `M03` | Antigravity | grounded extraction comparison, only if needed | No |
| `M04` | Antigravity | synthesis/knowledge-product comparison, only if needed | No |
| `M05` | Antigravity | evaluate finalists and select smallest production composition | **YES — R2** |
| `M06` | Antigravity | integrate only selected composition | No |
| `M07` | Antigravity | fresh three-source E2E/regression proof | **YES — R3** |

M02-M04 are conditional. If M01 finds a sufficiently strong complete/near-complete system, skip unnecessary component research.

---

# 5. Fresh-context rule

One major failure before V3 was putting too much architecture/history/work into a single AI context and asking it to execute everything.

V3 deliberately keeps **one module = one fresh Antigravity context**.

For a module Antigravity receives only:

1. `CURRENT-WORK.md`;
2. the active `Mxx` file;
3. files/resources explicitly named by that module.

Do not feed the full repository history, all V2 research, all failed runs, all future modules, or this full ChatGPT conversation into the executor.

Within the one active module Antigravity **is allowed to iterate normally**:

```text
research/run
   -> inspect
   -> test
   -> diagnose normal defect
   -> repair
   -> rerun
   -> commit useful result
```

Do not force a ChatGPT round trip for ordinary coding/test failures.

The two-strike rule still applies to repeated failures of the same approach.

---

# 6. OpenClaw boundary

OpenClaw is only a mechanical relay/process supervisor.

It may:

- read `CURRENT-WORK.md`;
- launch Antigravity;
- use headless mode only after the live installed `agy` passes the required smoke;
- otherwise launch Antigravity through PTY;
- observe process state/output;
- detect likely input waits;
- relay literal pre-authorized input;
- record exit status / observed commit / result-file existence;
- stop at review/blocker markers.

It may **not**:

- decide architecture;
- evaluate knowledge quality;
- reinterpret module goals;
- invent repair strategy;
- silently answer semantic/operator decisions;
- promote a component;
- create a new orchestration subsystem.

Do not repurpose the existing protected `apex-executor` whose authority boundary forbids becoming a planner/router/scheduler. Use the separate thin V3 relay approach defined in the V3 orchestration contract.

---

# 7. Antigravity transport rule

Do not freeze assumptions about Antigravity capability from old docs.

M00 must inspect the actually installed version and smoke-test:

1. `agy --version`;
2. authentication;
3. bounded headless text execution;
4. bounded workspace/file capability under safe permissions.

If the installed version safely supports the needed headless mode, use it where appropriate.

Otherwise OpenClaw should supervise interactive Antigravity through PTY.

Do not make `--dangerously-skip-permissions` the normal solution.

---

# 8. Git policy

Repository:

`leela-spec/apexai-os-meta`

Branch:

`main` only.

Git/main is the shared state bus.

The orchestrator must independently inspect remote GitHub state rather than trust Antigravity/OpenClaw prose about commits, files, or results.

Do not create feature branches for this workflow unless the operator explicitly changes the branch policy.

Do not require one commit per tiny internal step. Commits should represent useful module progress/results.

---

# 9. Review-gate procedure

There are only three normal ChatGPT review gates.

## R1 — after M01

Question:

> Is there an existing end-to-end or near-end-to-end system worth adopting/lightly forking, or is a component composition genuinely necessary?

Inspect:

- current M01 result file;
- actual candidate repositories/docs as needed;
- actual runnable outputs;
- install/runtime failure evidence;
- product quality on the first baseline source;
- exact gaps.

Prefer:

1. adopt existing system;
2. light fork/adaptation;
3. small composition of proven components;
4. custom implementation only for demonstrated gaps.

Do not proceed to M02-M04 merely because they exist.

## R2 — after M05

Question:

> Which smallest composition actually earned production status?

Review each proposed production component and require observed evidence that it materially improves at least one of:

- correctness/source fidelity;
- important insight recall;
- resilience;
- multilingual quality;
- runtime/token efficiency;
- operator usefulness;
- elimination of meaningful custom code.

If a component adds complexity without demonstrated value, remove it.

Freeze one primary production composition and one fallback only if needed.

## R3 — after M07

Question:

> Does the finished production pipeline actually work reliably on the required real sources?

Review the **actual knowledge artifacts**, not only test summaries.

Accept only if the 3-source E2E demonstrates useful English/German output, source identity/traceability, repeatability, and no obvious fake/stale/cross-source behavior.

---

# 10. Review outcomes

Use one of these concise outcomes when reviewing a gate/module:

- `CONTINUE -> Mxx`
- `SKIP -> Mxx` when a conditional module is unnecessary
- `REPAIR SAME MODULE` only for a real bounded defect and only within the two-strike budget
- `APPROACH SUSPECT` when repeated repair is no longer justified
- `BLOCKED`
- `OPERATOR DECISION`
- `ARCHITECTURE SELECTED -> M06`
- `ACCEPT V3 PRODUCTION`

Do not invent additional approval layers unless a concrete risk requires one.

---

# 11. Benchmark scope — do not let it expand casually

Current architecture-selection corpus is **3 primary videos**:

1. `P-h5WSQG1Sw` — long English science/interview;
2. `CygwqaNg2PY` — English technical finance;
3. `vFTuLylvYnA` — German finance.

Optional holdout only when needed:

- `oZIsMX6WgFs` — technical/procedural English.

Default component fixture sizes if component bake-offs are actually required:

- ASR: 3 clips/source = 9 total;
- semantic extraction: 4 windows/source = 12 total;
- support pairs: 8/source = 24 total.

Expand only if the result between finalists remains genuinely ambiguous.

Do not grow the benchmark because a larger count appears more rigorous.

---

# 12. Candidate/component posture

V3 preserves useful earlier research but does not preselect a large hot path.

Current serious candidates include, subject to live re-verification at execution time:

- complete/near-complete systems discovered in M01;
- existing `yt-dlp`/ffmpeg acquisition;
- faster-whisper;
- NVIDIA Parakeet challenger;
- WhisperX if alignment/speakers are a demonstrated need;
- TTK capabilities only where they beat/supplement existing systems;
- LangExtract;
- Instructor/Pydantic where structured-output seam needs it;
- DocETL as a synthesis/orchestration challenger only if needed;
- GLiNER2 / similar narrow IE only if they earn their cost;
- DeepEval / existing evaluation systems only as useful evaluation aids;
- Fabric/Open Notebook/other existing products as product baselines where useful.

Do not automatically install or integrate this list.

M01 exists specifically to discover whether a better/more complete existing solution makes most of it unnecessary.

---

# 13. Current execution state at handover

At the time this handover was created:

`CURRENT-WORK.md` says:

- status: `READY_FOR_M00`;
- active module: `execution-modules/M00-ORCHESTRATION-SMOKE.md`;
- M00 must prove OpenClaw -> Antigravity on a **product-advancing research task**;
- ping/hello-world alone is insufficient;
- after M00 PASS, M01 runs in a fresh Antigravity context;
- after M01, stop at Review Gate R1 for ChatGPT review.

Do not skip directly into the old V2.1 S01 acquisition stage.

---

# 14. How to bootstrap execution without giant prompts

Do not send Antigravity another multi-thousand-line bespoke packet.

The relay bootstrap should conceptually be only:

> Work on repository `leela-spec/apexai-os-meta`, `main` only. Read `SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/CURRENT-WORK.md`, then the active module it names, and execute exactly that module under the V3 OpenClaw↔Antigravity orchestration contract. Load only context explicitly named by the module. Perform normal research/run/test/repair iterations inside the module. Stop on PASS, BLOCKED, OPERATOR_DECISION, APPROACH_SUSPECT, or REVIEW_GATE. Commit useful module results to `main`.

The repository files contain the actual work package.

---

# 15. What the orchestrator should protect most aggressively

Protect against these recurring failure patterns:

1. **Local-fix tunnel vision:** repeatedly fixing the immediate technical defect instead of asking whether the approach remains the shortest path to the target.
2. **Infrastructure substitution:** spending project time on orchestration, receipts, state, schemas, wrappers, or testing infrastructure before real product proof.
3. **Component accumulation:** treating every researched tool as something the production pipeline needs.
4. **Framework invention before bake-off:** building custom infrastructure before running existing alternatives.
5. **Giant-context execution:** giving one executor the entire project/history and asking it to complete everything.
6. **False progress:** accepting test/metadata output when no useful knowledge artifact exists.
7. **Benchmark inflation:** expanding fixtures/runs without a decision that genuinely requires more evidence.
8. **Stale authority:** relying on old V1/V2/V2.1 files because they look detailed or call themselves authoritative.

If the orchestrator itself begins spending multiple iterations polishing orchestration or bookkeeping without a new product artifact, invoke the same anti-drift rules on itself.

---

# 16. Immediate next responsibility

The next orchestrator chat should **not redesign V3**.

Its first job is to:

1. independently verify current `main` and `CURRENT-WORK.md`;
2. help initiate/observe M00 through the thin OpenClaw relay;
3. ensure the relay consumes at most one repair cycle;
4. let M01 run in a fresh Antigravity context if M00 passes;
5. perform Review Gate R1 from remote GitHub evidence when M01 completes.

The desired first meaningful decision is **which already-proven system/path to adopt or benchmark further**, not another orchestration architecture.
