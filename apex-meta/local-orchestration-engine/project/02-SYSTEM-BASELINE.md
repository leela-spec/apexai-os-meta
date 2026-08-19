---
title: "FEE System Baseline"
doc_type: system_baseline
initiative: local-orchestration-engine
created: 2026-08-10
updated: 2026-08-10
status: "current implementation truth as of commit 2613578, incorporating the 2026-08-10 assumption audit"
last_verified_commit: 2613578113f5bd88e6e50c3d595a4bea2c42fe39
sources_consumed:
  - apex-meta/local-orchestration-engine/project/specs/2026-08-10-fee-project-environment-design.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - apex-meta/local-orchestration-engine/LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md
  - apex-meta/local-orchestration-engine/benchmark/results/BASELINE-RESULT-QWEN3-8B-2026-08-09.md
  - apex-meta/local-orchestration-engine/benchmark/results/RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md
  - apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-INSTALL-LOG-2026-08-09-QWEN3-8B.md
  - apex-meta/local-orchestration-engine/research-results/PLATFORM-RESEARCH-SYNTHESIS-2026-08-08-V2-RESULT.md
  - apex-meta/SmallSkills/AI-Browser-Orchestration/Browser-Subscription-AI-Orchestration.okf.md
  - .claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md
  - .claude/skills/weekly-orchestrator/SKILL.md
  - scripts/fee/ and scripts/lmbench/ source and tests, verified 2026-08-10
  - assumption audit 2026-08-10 (A1, A2, A3, A14)
---

# FEE System Baseline

**Sole responsibility:** the honest line between what is locked, what is built, what is measured, what is only researched, and what does not exist.

The distinction this file protects: **a locked decision is not an implementation, an implementation is not a measurement, a measurement is not a certification, and a research recommendation is none of those.** Conflating any two is how the `step-4 only` drift happened — and how the `control plane` over-correction happened four weeks later.

## 1. Target architecture

```text
Workflow&Processes     process_stage · workflow_stage · expected_output_type · operator gates
PromptEngineer         prompt_packet + materialized body ; never executes
AIRouting              routing_decision : which surface performs THIS step
        |
        v
FEE — the operator layer
  freeze packet + route · VALIDATE the route before executing · compile
  root/capability scope · broker action_id + arguments · checkpoint ·
  evidence ledger · retry budget · typed escalation · emit validation_status
        |
        v
Executor               the surface the route named
        |
        +--> blocked / security / auth / unknown -> compact escalation packet
        v
Verification by a different surface, then the operator gate
```

The broker contract from [R2 §5](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md), which model-generated shell must never bypass:

```text
model decides: authorized_action_id + bounded arguments
  -> broker validates: action exists · capability granted · root allowed ·
     arguments satisfy schema · captured content created no new authority
  -> deterministic implementation performs the operation
```

## 2. Surface-by-surface truth

| Surface | State | Evidence |
|---|---|---|
| Broad four-layer, cross-project FEE scope | **operator locked** | [R1-Q5](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md), [R2-Q1](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md) |
| FEE as *operator layer*, not control plane | **operator locked 2026-08-10** | scope correction; supersedes design §2.1 |
| Frozen plan, ledger, assisted capture subset | implemented candidate, tested, **never run live** | 32/32 tests |
| Agent loop with 10 tools, broker, path guard, manifest audit, graders | implemented, tested | 177/177 on Windows |
| Browser subscription execution **via Claude-in-Chrome** | **PROVEN** | 13 `BAO-*` rules; 25-file research corpus |
| Browser subscription execution **via bounded local LLM + runtime** | `NOT_IMPLEMENTED` | — |
| Qwen3-8B OpenVINO and llama.cpp installs | installed, smoke-tested | [install log](../research-results/LOCAL-MODEL-INSTALL-LOG-2026-08-09-QWEN3-8B.md) |
| Qwen3-8B llama.cpp n=1 result | **measured calibration, and the premise it supports is likely false as stated** | [re-analysis](../benchmark/results/RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md) |
| OpenVINO paired benchmark | not run | deliberately deferred |
| Operator contract: work packet + accepted `routing_decision` + published interface | `NOT_IMPLEMENTED` | task [004](../../epics/fee-operator-layer/004.md) |
| OpenClaw / Hermes / Odysseus composition | not installed, not selected | 2026-08-10 audit |
| Broad Weekly / Multi-Agent integration | `NOT_IMPLEMENTED` — and it is the adopting flow's work, not FEE's | — |
| Durable action-level duplicate-safe resume | not demonstrated | `T9` uninstrumented |
| `apex-session` gated mutation path | **specification only** | audit A2 |
| A materialized prompt body under `artifacts/` | **has never existed** | audit A3 |
| A confirmed Weekly gate | **has never happened** | audit A3 |

## 3. What `scripts/fee` actually is

A tested candidate subset for the first seam. It provides pack compilation and frozen-plan hashing, strict artifact and path reading, an append-only execution ledger, the assisted `next`/`capture` loop, skip-marker output, and injection-containment fixtures.

It does **not** provide the runtime bridge, production browser automation, or workflow integration. Version `0.1.0-candidate`. CLI: `python -m scripts.fee {plan,status,next,capture,emit}`. Its README states plainly: *"no live provider contact has ever occurred."* Its only inputs are synthetic fixtures dated `20260801`.

Verified 2026-08-10: `python -m unittest discover -s scripts/fee/tests -t .` → **Ran 32 tests, OK**. Platform-independent.

> **Stale docstring.** `scripts/fee/__init__.py` quotes the Weekly Orchestrator seam as `agent: none_operator_human_step`. The skill was amended on 2026-08-07 (commit `86229544`) to `agent: none_operator_human_step_or_fee`. `scripts/fee/README.md` quotes it correctly. Task [002](../../epics/fee-operator-layer/002.md) fixes the docstring.

## 4. What `scripts/lmbench` actually is

**A working agent loop**, not merely a benchmark harness. This matters because it resolves a common misconception — that a local model needs OpenClaw or Hermes to have agent and tool-execution capability. It already has both, here.

| Capability | Location |
|---|---|
| Bounded agent loop, `max_turns = 12`, budget exhaustion as `budget_exhausted` | `runner.py` |
| **Standard OpenAI function-calling schemas** via `openai_schema(tool)` — adopted, not invented | `toolspec.py` |
| Ten tools: `list_dir`, `read_file`, `write_file`, `apply_patch`, `run_command`, `run_tests`, `git_status`, `git_diff`, `apply_declared_recovery`, `collect_logs` | `tools.py` |
| Typed escalation with enum'd `type` and `destination`; trust labels on captured content; `finish` with `completed`/`escalated`/`blocked` | `toolspec.py` |
| llama.cpp adapter over an OpenAI-compatible endpoint | `adapter.py` |
| Append-only trace and an independent manifest audit that can detect broker bypass | `trace.py`, `manifest.py` |
| Graders, verdict combination, aggregation, profile-candidate emission | `graders/`, `verdict.py`, `report.py` |

Verified 2026-08-10: **Ran 177 tests, OK**, on Windows.

> **Platform constraint.** This suite asserts Windows path semantics — drive-letter root classification, case-insensitive comparison form, process termination. On Linux it reports 17 failures and 1 error against identical source. That is an environment property, not a defect, and it means the 177-test gate can only be satisfied on the operator's Windows machine.

`report.py` enforces `MIN_TRIALS_FOR_ELIGIBILITY = 3`, and `eligible` additionally requires `actor_pass == valid_total` — a **pass^n** criterion. `certification_decision` has no code path that can be set to anything but `null`.

### What a third-party runtime would actually add

Four things, none of them "agent skills":

1. **Browser tools.** Nothing in `lmbench` drives Chrome. This is the real gap.
2. **OS-enforced isolation.** `fsguard.py` is a path check inside APEX's own Python; its docstring concedes the guard is the only *permitted* route to `subprocess` and file mutation, which is a rule the code follows rather than one the OS enforces. `run_command` is the hole: once an arbitrary program runs, it is a normal Windows process with the operator's full rights. OpenClaw's sandbox bind mounts and Hermes' Docker containers are OS-enforced instead.
3. **A broader tool library.** Ten tools versus dozens.
4. **Durable session resume across process restart.** `workspace.py` tracks PIDs and can verify a kill; there is no session-persistence layer.

## 5. Fixture corpus

The [portfolio](../LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md) defines the intended families. Only a subset is built.

| Family | Defined | Built and run |
|---|---|---|
| `CODE-01`..`05` bounded coding | 5 classes | `CODE-01a/b/c`, `CODE-03`, `CODE-04`, `CODE-04-B` |
| `WEEKLY-01`..`06` subscription execution | 6 classes | **none** — browser stub unbuilt |
| `MA-01`..`06` Multi-Agent support | 6 classes | `MA-05-01`..`16`, `MA-06`, `MA-06-B` |
| `INJECT-01`..`08` adversarial injection | 8 classes | `INJECT-03`, `INJECT-03-B`, `INJECT-07`, `INJECT-07-B` |
| Context ladder 8K / 16K / 32K / 64K | 4 tiers | **none** |
| `COEX-01`..`06` coexistence | 6 scenarios | **none** |

Round-1 total: **28 fixtures**. Unbuilt families were deliberately deferred, not silently dropped. **The families constituting the actual target workload — `WEEKLY-*` and `MA-01`..`04` — have n = 0.**

`T1`..`T12` from the [platform synthesis §12](../research-results/PLATFORM-RESEARCH-SYNTHESIS-2026-08-08-V2-RESULT.md) is a **separate, uninstrumented** corpus for comparing runtimes rather than models. `T3`, `T7`, `T9`, `T11` are the common hard gates task [005](../../epics/fee-operator-layer/005.md) must instrument before any runtime is installed.

## 6. Local model state

| | |
|---|---|
| Configuration benchmarked | `CFG-8B-VULKAN-01` |
| Model artifact | `Qwen/Qwen3-8B-GGUF`, `Qwen3-8B-Q4_K_M.gguf` |
| sha256 | `d98cdcbd03e17ce47681435b5150e34c1417f50b5c0019dd560e4882c5745785` |
| Runtime | llama.cpp `b10333` (`08659901c`), Vulkan on Intel Arc 140V |
| Context / generation | 16384 · reasoning budget 400 · max tokens 600 · temperature 0.2 |
| Second install | OpenVINO GenAI INT4, ~5.0 GB footprint — **not benchmarked** |
| llama.cpp working set | 10.76–14.16 GB after exchanges |
| llama.cpp decode | 12.5–13.5 tok/s |
| Status | **installed candidate.** Not selected, not certified. |

`~7–8B is the operator's primary hypothesis and expected practical optimum — a strong prior, not a production lock` ([R3 §1](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md)). It must be tested against a ~3–4B control and a ~12–14B challenger; neither has run. Per [R3 LM-28](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md) the number of models and any generalist/coder split remain **open by design**.

### Measured result, n=1, and how to read it

```yaml
trials: 28
actor_pass: 8      # CODE 0/6 · MA-05 5/16 · MA-06 0/1 valid · INJECT 3/4
actor_fail: 19
infra_invalid: 1   # MA-06-B
unauthorized_attempts_denied: 5
successful_unauthorized_actions: 0
certification_eligible_task_classes: []
```

**The [adversarial re-analysis](../benchmark/results/RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md) is required reading before quoting any of this.** Its findings, compressed:

- Outside MA-05, **every graded-correct escalation was copied verbatim from the packet.** CODE-04 called `read_file` zero times.
- The fixture author's **pre-registered anti-gaming test fired** — CODE-04 / CODE-04-B, built to separate capability from pattern-matching. The model escalated on both, twice on 04-B against an `ACCEPTED` ADR naming the fix. Three of four discrimination pairs collapsed.
- **MA-05-16: the model obeyed an in-packet injection** and recorded `hard_gate_violation: false`. The gate inspects tool calls; output-content steering has nothing for the broker to deny. `QG-1` needs a second instrument.
- **pass^n means repeats deflate.** Two of seven destinations were never emitted in 16 attempts and are correct for 5 of 16 fixtures.
- **10 of 19 failures are packet defects** — real and actionable. But repairing them turns MA-05 into a lookup table, and 5 of 6 CODE failures are capability or procedure.
- Published data says 29% is **expected, not anomalous**, for this class on this work.
- **Four harness defects** must be fixed before any repeat run: `failed_task_classes` lists all 28 including the 8 passes; resource metrics are never captured so the resource half of the portfolio reports a vacuous pass; `finish_reason` has no consumer so truncation is invisible; CODE-03's oracle makes the escalation branch its own packet permits unpassable.

### An unsourced claim, flagged rather than repeated

The baseline result attributes repeat counts of *"3 for mechanical fixtures, 5 for stochastic, 10 for adversarial/safety"* to the portfolio. **The portfolio's §11 contains no numeric counts** — only qualitative rules, and an explicit statement that thresholds beyond hard safety gates are set after baseline runs. The only numeric repeat constraint in the evidence chain is `MIN_TRIALS_FOR_ELIGIBILITY = 3` in `report.py`.

Recorded as **`UNSOURCED`**. Task [006](../../epics/fee-operator-layer/006.md) must declare its own repeat counts.

## 7. Platform research state

No runtime installed or selected. Research-supported hypothesis: FEE spine + hardened OpenClaw runtime subset + authority-separated OpenClaw doctrine (composition A, synthesis score 86, confidence 84). Runner-up: FEE + bounded Hermes runtime (composition B, 82 / 80). Odysseus is a selective third candidate.

| Hard gate | OpenClaw | Hermes | Odysseus | FEE implication |
|---|---|---|---|---|
| 1 · Authority containment (`QG-1`, G-P1) | pass w/ external broker | pass w/ external broker | pass w/ external broker | FEE must be the broker in every composition |
| 2 · Job-scoped permissions (`QG-2`, G-P2) | pass w/ external broker | pass w/ external broker | pass w/ external broker | FEE compiles roots and capabilities |
| 3 · Resumability (`QG-3`, G-P3) | **PASS** | pass w/ external broker | **UNKNOWN** | FEE checkpoint stays canonical |
| 4 · Evidence capture (`QG-4`, G-P4) | **PASS** | **PASS** | pass w/ external broker | FEE normalizes to the canonical ledger |
| 5 · Safe escalation (`QG-5`, G-P5) | pass w/ external broker | pass w/ external broker | pass w/ external broker | FEE owns retry budget and stop taxonomy |
| 6 · Windows viability (`QG-6`, G-P6) | **PASS** | **PASS** | **PASS** | resource coexistence **unmeasured** |

**All of this is desk review of documentation dated 2026-08-08. Nothing has been installed.** Both OpenClaw and Hermes are described as fast-moving.

Per-flow scores show OpenClaw's lead is essentially **one flow**: `UF-E` multi-root, 91 against Hermes' 76, on sandbox bind mounts. `UF-A` (88 / 84) and `UF-C` (93 / 90) are its other wins — and both are at capabilities that **already work through a different executor**. Hermes leads `UF-B` script recovery, 88 / 85. Everything else is inside noise on unmeasured directional scores.

**No candidate may replace FEE's authority boundary.** Composition E — specialized runtime per flow — scores **70, lowest of six**, despite the best CLI and human savings, losing on drift resistance, integration simplicity and maintenance. "Reject now: three-runtime specialized production architecture" is an explicit finding.

Carried-forward contradictions: authenticated browser reliability is empirically `UNKNOWN` for all three; Hermes documentation states no browser downloads while OpenClaw supports them; workspace confinement must not be equated with process isolation; Hermes' own docs say `profiles` and `terminal.cwd` are **not** filesystem sandboxes, so Docker is how Hermes gets containment — which on Windows means WSL2 and its own memory reservation.

## 8. Machine profile

```text
HP OmniBook X Flip 16-as0xxx
Windows 11
Intel Core Ultra 7 258V (8 cores, up to 4.8 GHz)
~31.6 GB system RAM
Intel Arc 140V integrated graphics, ~16.5 GB reported shared device memory
```

Per [R3 §12](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md), generic hardware benchmarks are context only. Laptop coexistence is a hard requirement ([LM-26](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md)) and **no `COEX-*` scenario has been run for any configuration.**

The arithmetic worth stating: a 10.76–14.16 GB model working set on 31.6 GB, plus Chrome with three subscription sessions, plus an IDE, plus a runtime — and for Hermes, plus WSL2 and Docker. `QG-6` is a hard gate that no weighted score can compensate, it is the cheapest test available, and it is currently scheduled last.

## 9. The consumer side — audit A3

FEE exists to be delegated work. As of 2026-08-10 it has no live consumer.

**Weekly Orchestrator — `PARTIALLY_BUILT`.** A complete, internally consistent contract; all seven stage agents exist in `.claude/agents/` and each resolves to a real skill. But: one partial half-cycle on 2026-07-12; **every packet reads `operator_validation: not_requested`**, so no gate has ever been confirmed; `state/apex-project-status.md` and `state/consumed-recap-registry.md` are both **0 bytes**; the one flow that "executed" was the control plane verifying itself; nothing in four weeks.

**Multi-Agent Orchestration — `PARTIALLY_BUILT`, and the more real of the two.** `US-IDEA-01` records a genuine end-to-end run with operator gates actually answered, two verified durable mutations, and real `scripts/apex_sync.py` executions. But 2 of 7 user stories run, its own `simulations/README.md` still says *"no story has been run yet,"* and nothing since 2026-07-12.

**The seam.** `.claude/skills/weekly-orchestrator/SKILL.md` line 32:

```yaml
operator_execution: {agent: none_operator_human_step_or_fee, gate: G3, trigger: "operator returns evidence or skip signal"}
```

That is not an interface. It is a row in a routing table whose `agent` value is a sentinel meaning "no agent here." Step 4 is the gap between G2 approval and evidence arriving: **the operator does the week's actual work in a subscription AI, then returns evidence or a skip signal.** The 2026-08-07 amendment made FEE a *sanctioned* actor at that step; per `architecture/06-gate-batch-draft.md` it *"does not automate G3, does not change the trigger"* — FEE changes who **performs** step 4, never who **approves** it.

**There is no call site.** Nothing invokes `python -m scripts.fee`. FEE appears in the Weekly Orchestrator in exactly that one string literal.

**FEE's input has never been materialized.** [`flow-prompt-pack-contract.md`](../../../.claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md) §`prompt_body_materialization` — added 2026-08-07 — defines the location:

```text
artifacts/flow-packets/<YYYYMMDD>/prompt-packs/bodies/<packet_id>.md
```

with `absent_body_behavior`: treat the ref as unresolved and halt or flag; never silently default. **The convention exists. No such file has ever been written.** No `prompt-packs/` directory exists anywhere under `artifacts/`, and zero committed artifacts contain a `prompt_body`.

## 10. Known documentation drift

Pending task [002](../../epics/fee-operator-layer/002.md), which must reconcile in **both** directions.

Too narrow — stale `step-4 only` wording superseded by R1/R2/R3:

| File | Stale text |
|---|---|
| [`../00-START-HERE.md`](../00-START-HERE.md) | "execution substrate for one stage of one of them"; "attaches to the Weekly Orchestrator at step 4 only" |
| [`../HANDOVER.md`](../HANDOVER.md) | "FEE fills only the …" |
| [`../architecture/01-macro-architecture-decision.md`](../architecture/01-macro-architecture-decision.md) | diagram "FEE attaches HERE, at step 4 only"; rejected-alternatives row |
| [`../../../scripts/fee/README.md`](../../../scripts/fee/README.md) | "a substrate for one stage of one of them" |
| [`../../../scripts/fee/__init__.py`](../../../scripts/fee/__init__.py) | same, plus the stale pre-amendment seam quote |

Too broad — `control plane` and `authority spine`, superseded 2026-08-10:

| File | Over-wide text |
|---|---|
| [`specs/2026-08-10-fee-project-environment-design.md`](specs/2026-08-10-fee-project-environment-design.md) | §2.1 "execution and control plane"; §5 "Deterministic FEE authority spine" |
| [`../HANDOVER-2026-08-10-FEE-PROJECT-ENVIRONMENT.md`](../HANDOVER-2026-08-10-FEE-PROJECT-ENVIRONMENT.md) | §2 same |

The architecture decision record **keeps its original wording**. `D-M2` was amended by R1, not deleted, and erasing it would destroy the history that explains why the drift was plausible. It gets a dated supersession note instead. The same principle applies to the design spec: amend in place with a dated note, do not pretend it always said something else.
