---
title: "FEE Project Environment"
doc_type: project_environment_index
initiative: local-orchestration-engine
created: 2026-08-10
updated: 2026-08-10
status: "program paused pending socket validation; see 15-HANDOVER.md"
sources_consumed:
  - apex-meta/local-orchestration-engine/project/specs/2026-08-10-fee-project-environment-design.md
  - apex-meta/local-orchestration-engine/project/plans/2026-08-10-fee-project-environment-implementation-plan.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
  - .claude/skills/apex-plan/references/task-record-contract.md
  - .claude/skills/AIRouting/routing-decision-contract.md
  - .claude/skills/PromptEngineer/PromptPacketContract.md
  - .claude/workflows/constant-frame-control-and-handoff.md
  - operator scope correction 2026-08-10
---

# FEE Project Environment

**Sole responsibility of this file:** navigation, read order, and the source-of-truth law. It holds no status and no evidence of its own.

## 1. What FEE is

FEE is the **operator layer**. Its job is integrating a bounded local LLM and a later-chosen third-party runtime into the *existing* apex-os-meta orchestration system as a safe, evidence-producing executor — so the agents, orchestration flows and project management that already live there can delegate operational work to it.

FEE is **not** an orchestration system. It is **not** a control plane. It owns no planning, routing, or promotion authority. `D-M0` pins "orchestration system" to exactly two, and [R2 §3](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md) states that no executor runtime or local model may become a third.

What it does own is the execution-safety mechanics that make delegation safe: freezing the packet it was handed, validating the route it was given, brokering action IDs and arguments, enforcing root and capability scope, checkpointing, and producing reconstructable evidence.

> **Superseded language, recorded so it is not reintroduced.** The approved design §2.1 and the delivery handover §2 describe FEE as a "reusable, cross-project execution and control plane," and design §5 names workstream P1 the "deterministic FEE authority spine." Both are superseded by the operator scope correction of 2026-08-10. They were an over-correction: the stale `step-4 only` wording was rightly read as too narrow, then widened in the wrong dimension — widening what FEE has *authority over* instead of which flows it can *serve*. Weekly Orchestrator step 4 remains the first seam; `D-M2` was amended by [R1 §9](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md), not deleted.

## 2. Read order

New here, or continuing in a fresh chat? Read exactly these four, in order:

1. **this file** — how the environment is organized and which source wins
2. **[00-PROJECT-COCKPIT.md](00-PROJECT-COCKPIT.md)** — one-pass current state
3. **[15-HANDOVER.md](15-HANDOVER.md)** — the constant frame: current state, the one next step, permissions, gates, stop conditions
4. **the canonical next task named by the handover** — under [`../../epics/fee-operator-layer/`](../../epics/fee-operator-layer/)

If those four do not let you state the mission, what is built, what is only researched, the next exact step, and what you may not write, this environment has failed its acceptance test and must be revised before you act.

Then, as the work requires:

| Need | File |
|---|---|
| Why this exists, what it will not become | [01-PROJECT-CHARTER.md](01-PROJECT-CHARTER.md) |
| What is built vs measured vs researched vs absent | [02-SYSTEM-BASELINE.md](02-SYSTEM-BASELINE.md) |
| Whose outcomes justify each component | [03-USER-STORY-PORTFOLIO.md](03-USER-STORY-PORTFOLIO.md) |
| Sequencing, entry/exit gates, reversal triggers | [04-ROADMAP.md](04-ROADMAP.md) |
| Workstream boundaries and what each must not own | [05-WORKSTREAMS.md](05-WORKSTREAMS.md) |
| Story → task → fixture → evidence chain | [07-TRACEABILITY-MATRIX.md](07-TRACEABILITY-MATRIX.md) |
| Gate definitions and current evidence state | [08-QUALITY-GATES.md](08-QUALITY-GATES.md) |
| Whether this is actually saving effort | [09-EFFICIENCY-SCORECARD.md](09-EFFICIENCY-SCORECARD.md) |
| Active risks, controls, triggers | [10-RISK-REGISTER.md](10-RISK-REGISTER.md) |
| What is locked, open, superseded, reversible | [11-DECISION-REGISTER.md](11-DECISION-REGISTER.md) |
| Where the evidence for any claim lives | [12-EVIDENCE-INDEX.md](12-EVIDENCE-INDEX.md) |
| Terminology and the authority ladder | [14-GLOSSARY-AND-AUTHORITY.md](14-GLOSSARY-AND-AUTHORITY.md) |
| Authoring shapes | [`templates/`](templates/) |
| The approved design and implementation plan | [`specs/`](specs/) · [`plans/`](plans/) |

## 3. Source-of-truth law

### 3.1 Document authority, when sources conflict

1. current explicit operator instruction
2. operator decision locks, newest relevant first — [R3](../OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md) for local-model behavior, [R2](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md) for the FEE/runtime boundary, [R1](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md) for four-layer scope and user flows
3. accepted APEX orchestration and Plan-Sync-Session contracts
4. measured benchmark and implementation evidence
5. platform research synthesis and candidate reports
6. earlier architecture proposals and historical handovers
7. raw research or historical notes

This ordering is what resolved the scope error that created this environment: stale `step-4 only` wording in live orientation files was outranking later operator locks because nothing made the precedence visible.

### 3.2 Execution-time authority, when skills conflict

A second, distinct axis. `AIRouting`, `PromptEngineer` and `Workflow&Processes` all three declare the *identical* order, and FEE must honour it rather than defining its own:

1. `operator_decision_from_tradeoff_card`
2. `workflow_process_fit`
3. `prompt_quality`
4. `ai_routing_cost_or_efficiency`

Document authority (§3.1) governs which text is current. Execution authority (§3.2) governs which skill's judgement wins at run time. Do not conflate them.

### 3.3 One owner per fact class

| Fact class | Sole owner | Everything else |
|---|---|---|
| Canonical task status | [`../../epics/fee-operator-layer/<id>.md`](../../epics/fee-operator-layer/) | links to it; never restates it as its own authority |
| Operator decisions | the decision-lock files in [`../`](../) | [11-DECISION-REGISTER.md](11-DECISION-REGISTER.md) **indexes and explains**; never rewrites |
| Measured verdicts | raw evidence under [`../benchmark/results/`](../benchmark/results/) and [`../research-results/`](../research-results/) | cockpit files summarize and link |
| **Which surface executes a step** | **`routing_decision` from [`AIRouting`](../../../.claude/skills/AIRouting/)** | **FEE consumes and validates it; FEE never defines allocation** |
| Prompt bodies | `prompt_packet` from [`PromptEngineer`](../../../.claude/skills/PromptEngineer/) | FEE receives a materialized body; it does not author prompts |
| Process and workflow stages | [`Workflow&Processes`](../../../.claude/skills/) | FEE consumes stage labels |
| Implementation reality | the code under [`../../../scripts/fee/`](../../../scripts/fee/) and [`../../../scripts/lmbench/`](../../../scripts/lmbench/) and its passing tests | [02-SYSTEM-BASELINE.md](02-SYSTEM-BASELINE.md) describes, never overstates |

If a cockpit file and its owner disagree, **the owner wins and the cockpit is corrected** — never the reverse.

### 3.4 Evidence law

- Absent evidence is written `UNMEASURED`, `UNKNOWN`, `NOT_IMPLEMENTED`, or `PARTIAL`. Never an optimistic estimate or manufactured precision.
- `PARTIAL` is never summarized as `PASS`. `INFRA_INVALID` is never folded into actor failure. Failed trials stay individually visible.
- A research score never fills an implementation-verdict field.
- An n=1 result may establish observed containment evidence. It never establishes long-run reliability or certification.
- **Roadmap presence is not implementation, selection, or certification.**
- **A summary never outranks the raw evidence it summarizes.** See [the 2026-08-10 adversarial re-analysis](../benchmark/results/RE-ANALYSIS-QWEN3-8B-N1-2026-08-10-ADVERSARIAL.md), which exercised this rule and corrected four claims in an existing result document.

### 3.5 Vocabularies

Task status, from the [task-record contract](../../../.claude/skills/apex-plan/references/task-record-contract.md): `open` · `in-progress` · `blocked` · `done` · `deferred`

Evidence verdict: `NOT_IMPLEMENTED` · `UNMEASURED` · `PARTIAL` · `PASS` · `FAIL` · `INFRA_INVALID`

Cross-skill validation status, shared by `AIRouting`, `PromptEngineer` and `Workflow&Processes` — FEE emits this enum rather than inventing one: `valid` · `valid_with_warnings` · `operator_review_recommended` · `low_confidence_auto_generated` · `blocked_by_missing_operator_decision`

The last value **is** the operator gate, already contracted. These three vocabularies are separate and must never be conflated. A task can be `done` because a benchmark was correctly executed while that benchmark's verdict is `FAIL`.

### 3.6 Identifiers that project rather than assert

`QG-0`..`QG-7` in [08-QUALITY-GATES.md](08-QUALITY-GATES.md) are a readable presentation of gates **already locked elsewhere**. Every entry carries an `equivalent_to` row naming its [R2 §9](../OPERATOR-DECISION-LOCK-2026-08-08-R2.md) hard-gate number, its `G-P` identifier from the [platform synthesis](../research-results/PLATFORM-RESEARCH-SYNTHESIS-2026-08-08-V2-RESULT.md), and its `T1`..`T12` fixtures. No `QG-*` may assert anything its locked equivalent does not.

Likewise `US-FEE-01`..`US-FEE-06` alias the locked `UF-A`..`UF-F` flows from [R1 §8](../OPERATOR-DECISION-LOCK-2026-08-07-R1.md). The alias is convenience; the lock is authority.

And the four layers are **cost and authority tiers that a `routing_decision` selects from per step** — not fixed job assignments. `AIRouting`'s `route_surface_class` taxonomy is the same idea at higher resolution, and it is the canonical one.

## 4. File topology

```text
project/
  README.md                      <- you are here
  00-PROJECT-COCKPIT.md
  01-PROJECT-CHARTER.md
  02-SYSTEM-BASELINE.md
  03-USER-STORY-PORTFOLIO.md
  04-ROADMAP.md
  05-WORKSTREAMS.md
  07-TRACEABILITY-MATRIX.md
  08-QUALITY-GATES.md
  09-EFFICIENCY-SCORECARD.md
  10-RISK-REGISTER.md
  11-DECISION-REGISTER.md
  12-EVIDENCE-INDEX.md
  14-GLOSSARY-AND-AUTHORITY.md
  15-HANDOVER.md
  templates/  USER-STORY · EXPERIMENT · DECISION · STATUS-UPDATE
  specs/      2026-08-10-fee-project-environment-design.md
  plans/      2026-08-10-fee-project-environment-implementation-plan.md
```

Fifteen files, not the design's seventeen. **The gaps at `06` and `13` are deliberate**, an operator-approved simplification of design §4.1 on 2026-08-10:

- **`06-DELIVERY-BACKLOG.md` was not created.** It would have re-listed the canonical task records' title, status, priority and dependencies — zero unique information, guaranteed drift. The files in [`../../epics/fee-operator-layer/`](../../epics/fee-operator-layer/) *are* the backlog; §5 indexes them.
- **`13-STATUS-AND-NEXT-ACTIONS.md` was merged into [15-HANDOVER.md](15-HANDOVER.md).** The handover's mandated `current_state` and `next_step_only` keys already carry it. Two high-churn files that must agree eventually will not; one cannot disagree with itself.

Numbers were **not** reassigned after the cuts, so every remaining filename still matches the approved design and the plan's validation lists.

**Do not add a file** unless approved content genuinely cannot fit an existing responsibility. If that happens, stop and request a design amendment rather than growing the topology.

## 5. Canonical task index

Status lives in the task files. This is a link list, refreshed from them, and owns nothing. Workstreams are `F0`–`F4` ([05-WORKSTREAMS.md](05-WORKSTREAMS.md)); horizons are `H0`–`H5` ([04-ROADMAP.md](04-ROADMAP.md)).

**Re-derived 2026-08-10 after the operator selected OpenClaw directly.** The previous 13-task map was built around a runtime bake-off — install OpenClaw, compare Hermes, decide a composition — which is moot now that the operator has chosen. It also gated the install five tasks deep, which is why a downstream agent reading this repo concluded the install was out of scope. It was not; it is task 001.

| Task | Title | WS | Depends |
|---|---|---|---|
| [001](../../epics/fee-operator-layer/001.md) | **Install and verify the OpenClaw executor harness** — run [`../../openclaw/INSTALL-AND-VERIFY.md`](../../openclaw/INSTALL-AND-VERIFY.md) | F3 | — |
| [002](../../epics/fee-operator-layer/002.md) | Write the first prompt body at the contracted `prompt-packs/bodies/` path | F1 | 1 |
| [003](../../epics/fee-operator-layer/003.md) | Add deterministic capture verification — bytes on disk against the receipt | F1 | 1 |
| [004](../../epics/fee-operator-layer/004.md) | Execute one real flow end-to-end through the executor and capture the operator-minutes baseline | F1, F3 | 2, 3 |
| [005](../../epics/fee-operator-layer/005.md) | Build the `WEEKLY-01` fixture from that real flow so it becomes regression-testable | F2 | 4 |
| [006](../../epics/fee-operator-layer/006.md) | Reconcile stale scope language across the repository, in both directions | F0 | — |
| [007](../../epics/fee-operator-layer/007.md) | Expand to the remaining providers and `WEEKLY-02`..`06` behaviours | F2, F3 | 5 |
| [008](../../epics/fee-operator-layer/008.md) | Decide whether scheduled Automations are warranted, and under what stop rules | F4 | 7 |

Eight tasks, not thirteen, because the executor's scope is a copy-paster with a browser. Tasks that existed only to serve a bake-off or a certification decision are gone. `006` has no dependency and can run any time.

Umbrella epic: [`epic.md`](../../epics/fee-operator-layer/epic.md). Dependency ordering is a proposal until validated by `apex-sync`; a task is actionable only when every id in its `depends_on` resolves to a `done` task, and computing that set belongs to `apex-sync`, not to this file.

> **Note on how these records were written.** The [task-record contract](../../../.claude/skills/apex-plan/references/task-record-contract.md) reserves durable task-file writes for `apex-session`. An audit on 2026-08-10 found `apex-session` to be **specification only** — thirteen Markdown files, zero executable, deferring writes to a "later explicit file-application flow" that does not exist in the repo. These records were therefore written directly under explicit operator authorization, each carrying `review_flags: [operator_review_needed]` and a `proposal_state` note. See [11-DECISION-REGISTER.md](11-DECISION-REGISTER.md).

## 6. Update rhythm

| When | Do this |
|---|---|
| Session start | Read [00-PROJECT-COCKPIT.md](00-PROJECT-COCKPIT.md), [15-HANDOVER.md](15-HANDOVER.md), and the canonical active task |
| Task completion | Attach evidence; update the canonical task; refresh affected projections; record regression triggers |
| Operator decision | Update [11-DECISION-REGISTER.md](11-DECISION-REGISTER.md), affected risks, roadmap, traceability and the handover in one bounded batch |
| Material model / runtime / configuration change | Rerun affected benchmark fixtures **before** changing any eligibility or routing claim |
| Session end | Ensure the handover names exactly one next step and the cockpit holds no stale completion claim |
| Milestone exit | Fresh-reader review plus link, schema, traceability and Git-scope verification |

## 7. How to audit this environment for drift

Every file here carries a `sources_consumed:` frontmatter list naming the authority documents it was derived from. **If a claim in a file cannot be traced to one of its declared sources, it is drift** — remove it or re-source it.

That mechanism exists because drift was found six times on 2026-08-10 alone, in load-bearing documents including the approved design. Two lessons worth carrying:

- **A widened scope can drift as badly as a narrow one.** The `control plane` error came from correcting `step-4 only` in the wrong dimension.
- **Search hygiene matters.** `rg` skips dot-directories unless `--hidden` is passed. A repo-wide search that omits `.claude/` will silently miss every skill contract, and did.
