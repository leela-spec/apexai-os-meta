---
title: "FEE Project Charter"
doc_type: project_charter
initiative: local-orchestration-engine
created: 2026-08-10
updated: 2026-08-10
status: "operator-locked scope as corrected 2026-08-10; success thresholds follow baseline measurement"
sources_consumed:
  - apex-meta/local-orchestration-engine/project/specs/2026-08-10-fee-project-environment-design.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - .claude/skills/AIRouting/routing-decision-contract.md
  - .claude/skills/PromptEngineer/SKILL.md
  - apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md
  - operator scope correction 2026-08-10
---

# FEE Project Charter

**Sole responsibility:** why this exists, what it will and will not become, and what would count as success. Low churn — this changes only when the operator changes the product boundary. See [README.md](README.md).

## 1. Mission

Build FEE as the **operator layer** for apex-os-meta: the component that lets the orchestration systems, agents and project management **already living in this repository** delegate operational work to a bounded local LLM and a later-chosen third-party runtime — safely, and with evidence an independent reviewer can reconstruct.

FEE is a socket-filler, not a system. It exists so that work someone else planned can be *performed* by something cheaper than the operator or a scarce CLI agent, without that cheapness introducing a new class of risk.

## 2. The value being pursued

The operator's attention and the scarce CLI agents are the binding constraints on everything APEX does. Much of what consumes them is not reasoning — it is operation: driving subscription websites, submitting prompts and collecting outputs, rerunning failed scripts, gathering diffs and hashes for review, applying transformation rules someone else already decided, waiting.

FEE's value is absorbing that load into a layer that is cheap and, critically, **bounded**. A local executor that saves an hour of operation but costs an hour of supervision has produced nothing. That is why [09-EFFICIENCY-SCORECARD.md](09-EFFICIENCY-SCORECARD.md) measures human intervention minutes and CLI escalations alongside throughput, and why speed may never trade against authority safety.

**As of 2026-08-10 there is no baseline for any of this.** No flow has been run end-to-end, so there is no operator-minutes figure for FEE to beat. Establishing one is a prerequisite, not a nicety — see [00-PROJECT-COCKPIT.md](00-PROJECT-COCKPIT.md) §12.

## 3. Layer allocation — tiers, selected per step

Locked in [R1 §2](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md), refined by [R2 §3](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md) and [R3 §2](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md).

| Tier | Owns | Must never own |
|---|---|---|
| **Subscription / deep-reasoning AI** | substantive planning, research, synthesis, judgement, project-management intelligence, prompt creation, decision criteria | direct consequential execution without a frozen packet |
| **Scarce CLI AI** | hard coding, architecture, difficult diagnosis, consequential technical review, specialist escalation | routine operational work a bounded layer can do reliably |
| **Local LLM execution operator** | executing frozen plans, selecting among pre-authorized actions, driving declared interfaces, capturing evidence, bounded recovery, typed escalation | strategy, sequencing, semantic judgement, candidate promotion, inventing actions or providers |
| **Deterministic execution** | exact transforms, schema and argument validation, capability and root enforcement, ledgers, hashes, checkpoints | anything requiring genuine judgement |

**These are cost and authority tiers, not job assignments.** Which tier performs a given step is decided per step by a `routing_decision` from [`AIRouting`](../../../.claude/skills/AIRouting/), whose `route_surface_class` taxonomy — `frontier_subscription_chat`, `frontier_deep_research`, `frontier_code_agent`, `long_context_subscription_chat`, `supplemental_api`, `low_cost_batch_api`, `local_or_offline_tool`, `manual_operator_surface` — is the canonical, higher-resolution form of the same idea.

That correction matters concretely: browser subscription execution is **proven** through Claude-in-Chrome and `NOT_IMPLEMENTED` through a bounded local LLM. The same capability, two executors, two verdicts. A static layer table cannot express that, and the earlier version of this charter got it wrong as a result.

**Allocation principle:** use the lowest-cost, least-reasoning layer that can perform the task *reliably*; escalate only when the lower layer cannot safely complete the work. It is a per-task test, not a diagram.

**Authority invariant:** more model capability never grants more authority. The ladder from [R3 §6](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md) is fixed:

```text
local executor      -> may create a candidate
independent review  -> may verify the exact reviewed version
operator gate       -> may confirm consequence
single gated path   -> may apply durable mutation
```

> An audit on 2026-08-10 found the last rung, `apex-session`, is **specification only** — no executable, no file-application flow. The ladder's top three rungs are real; the fourth is currently convention. See [11-DECISION-REGISTER.md](11-DECISION-REGISTER.md).

## 4. What FEE owns

The execution-safety mechanics, and only those:

- freezing the work packet it was handed
- **accepting and validating a supplied `routing_decision`** — refusing an unvalidated or `blocked_by_missing_operator_decision` route
- action identifiers and typed argument validation
- the root and capability policy compiler
- the deterministic broker and filesystem guard
- durable state, checkpoints, and idempotency keys
- the evidence ledger and independent mutation audit
- retry budgets and the typed escalation taxonomy
- emitting the shared `validation_status` enum

## 5. In scope as served flows

FEE may serve, as each is separately approved and evidenced: Weekly Orchestration; Multi-Agent Orchestration and Meta Ops work packets; multiple projects and repositories; bounded coding and script recovery; Detective evidence collection; KB, Informatics and Prompts & Workflows hygiene; subscription execution; overnight work; and separately gated personal flows.

Weekly Orchestrator step 4 is the **first implemented seam** — the entry point, not the boundary. `D-M2` was amended by [R1 §9](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md).

> As of 2026-08-10 **none of these is a live consumer.** The step-4 seam has no call site; nothing invokes `python -m scripts.fee`. This list is prospective.

## 6. Explicit non-goals

FEE does **not**:

- become an orchestration system, or a third planning or governance authority — `D-M0` pins "orchestration system" to exactly two, and [R2 §3](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md) forbids a third
- **define which layer or surface executes a step** — that is `AIRouting`'s `routing_decision`, which FEE consumes and validates
- **author prompts** — that is `PromptEngineer`'s `prompt_packet`, which explicitly `must_not_create: project_execution`
- **define process or workflow stages** — that is `Workflow&Processes`
- integrate itself into the adopting flows — they adopt FEE against its published interface; FEE's obligation ends at that interface
- replace the planning or promotion authority of Weekly Orchestrator, Meta Ops, subscription reasoning models, CLI specialists, or the operator
- grant a local model authority proportional to its capability
- treat captured browser, document, tool or model content as anything but untrusted data
- expose a generic shell, arbitrary command generation, or uncontrolled planning to the local model
- assume machine-wide filesystem access, or make `C:\GitDev` a permanent exclusive root
- push commits, access credentials, or perform account changes automatically

Phase 0 additionally does **not**: certify any model or runtime as a precondition for the executor's narrow scope; modify `scripts/fee` or `scripts/lmbench` runtime behavior; introduce a database, dashboard, SaaS tool or always-on service; duplicate canonical task status; or declare a capability implemented because it appears in the roadmap.

> **Corrected 2026-08-10.** An earlier version of this list read *"does not install or select OpenClaw, Hermes or Odysseus."* That is **superseded**. The operator selected OpenClaw directly on 2026-08-10, and **installing it is now the active first task** — see [00-PROJECT-COCKPIT.md](00-PROJECT-COCKPIT.md) §2a. The original wording was correct while the open question was which runtime to pick; it became wrong the moment the operator answered that question, and it was mistakenly carried forward. Any document in this repository still listing runtime installation as a non-goal or a gated later task is stale.
>
> Live browser automation on the operator's own signed-in subscription sessions is likewise **no longer a non-goal** — it is the executor's entire purpose, performed under the operator's own accounts with tab-group scoping, and it is already proven practice in this repo via `apex-meta/SmallSkills/AI-Browser-Orchestration/`.

## 7. Constraints

**Authority.** Every claim traces to [README.md](README.md) §3.1 for document authority and §3.2 for execution-time authority between skills. Operator decision locks remain canonical in their own files; [11-DECISION-REGISTER.md](11-DECISION-REGISTER.md) indexes and explains them.

**Evidence.** Absent evidence is `UNMEASURED`, `UNKNOWN`, `NOT_IMPLEMENTED` or `PARTIAL`. Numeric thresholds beyond the hard safety gates are set only after baseline runs reveal real distributions, per [R2 §10](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md) and the [benchmark portfolio §11](../LOCAL-MODEL-BENCHMARK-PORTFOLIO-2026-08-08.md) — which, note, contains **no numeric repeat counts**. Any task claiming a repeat protocol must declare its own.

**Pattern before invention.** Per [R3 §3](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md): identify established reference patterns first, then adopt, adapt, combine or explicitly reject them before inventing an APEX-specific mechanism. Read strictly: **adopt the commodity mechanics, build only the authority layer.** Browser automation, OS isolation, tool libraries and session durability are solved problems with mature implementations. The frozen-packet-plus-evidence-ledger authority boundary is specific to APEX and no external project will supply it. `scripts/lmbench` already got this right once, adopting the OpenAI function-calling schema rather than inventing a tool format.

**Repository.** `main` only. Stage only the files a task names. Never stage the six untracked `.bundle` artifacts.

**Replaceability.** Any runtime sits *behind* the FEE contract and must remain replaceable. Runtime-specific code is measured as a ratio and treated as a liability.

## 8. Anti-overengineering constraints

Phase 0 uses Markdown, YAML frontmatter, existing APEX contracts and Git. Nothing else.

- one source of truth per fact class
- **consume an existing contract rather than defining a parallel one** — the `routing_decision`, `prompt_packet` and workflow-stage contracts already exist
- no component without a traced user story and an acceptance fixture
- no new persistent service, database or schema until a file-based limitation is **observed and recorded**
- no multi-runtime production architecture unless one runtime wins a flow class by a large, repeatable margin — Composition E, specialized-runtime-per-flow, scores 70 of six evaluated compositions
- no automation built to update a field that changes rarely or remains operator judgement
- summaries link to evidence rather than copying it
- record `UNMEASURED` rather than manufacturing precision

**Complexity review trigger.** A change adding any of the following requires a review in [11-DECISION-REGISTER.md](11-DECISION-REGISTER.md) naming expected value, the simpler alternative, maintenance cost, removal path and reversal trigger: an always-on process; a new durable data store; a new credential-bearing integration; another agent or runtime platform; duplicated canonical state; a privileged execution path; a new schema overlapping an existing APEX contract; or a component without a traced story and fixture.

## 9. Hard efficiency constraints

- **zero successful unauthorized actions is non-negotiable** and cannot be traded for speed. As of 2026-08-10 this holds for tool calls and has **one observed violation for output-content steering** (MA-05-16), which the broker structurally cannot observe
- a runtime that saves CLI calls but increases human babysitting is not efficient
- a faster model that omits required procedure is not more effective
- reliability-first with bounded latency tolerance, per [R3 LM-25](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md) — optimize successful bounded jobs per wall time, intervention and escalation, never raw tokens per second
- laptop coexistence is a hard requirement, per [R3 LM-26](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md), and is **unmeasured for every candidate**

## 10. Success definition

FEE succeeds when, for each explicitly approved task class:

1. the relevant hard gates in [08-QUALITY-GATES.md](08-QUALITY-GATES.md) pass with reproducible evidence, `QG-1` without exception, including the output-content steering instrument that does not yet exist;
2. the task class has a **benchmark-certified** model + runtime + harness profile in the planner-routable registry — certification being an operator decision on measured evidence, never an inference from capability;
3. the measured load absorbed exceeds the measured supervision and maintenance cost it creates, **against a real baseline**;
4. an independent reviewer can reconstruct what happened from durable evidence alone;
5. the authority ladder is intact — no candidate promoted, no planning authority absorbed, no captured content executable.

Phase 0 specifically succeeds when a fresh worker can read [README.md](README.md), [00-PROJECT-COCKPIT.md](00-PROJECT-COCKPIT.md), [15-HANDOVER.md](15-HANDOVER.md) and the canonical next task, and correctly state the mission, what is built, what is only researched, what is unbuilt, the next exact step, the allowed and forbidden writes, the operator gates and stop conditions, and why every runtime and model candidate remains evidence-gated — without consulting chat history.

## 11. Accountability

| Role | In this environment |
|---|---|
| Operator | confirms scope, priorities, consequential decisions, production authority, evidence-based reversals |
| `Workflow&Processes` | classifies and validates process and workflow fit; owns the operator-gate contract |
| `PromptEngineer` | authors prompt packets and bodies; **never executes** |
| `AIRouting` | proposes the `routing_decision`; **never executes** |
| `apex-plan` | proposes epic and task decomposition; **may not** mutate status or durable records |
| `apex-sync` | validates dependencies, actionability, registry consistency — and is real executable code |
| `apex-session` | owns operator-confirmed durable mutation — **currently specification only** |
| FEE | freezes, validates the route, brokers, checkpoints, evidences, escalates. Executes nothing it was not handed |
| Independent reviewer / Detective | tests consequential claims without repairing its own findings or promoting candidates |

The cockpit is **candidate operational documentation** during a work batch. A consequential decision or canonical status change becomes accepted only through the applicable operator and APEX mutation boundary.
