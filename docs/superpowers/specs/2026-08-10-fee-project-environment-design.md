---
title: "FEE Project Environment Design"
doc_type: design_specification
initiative: local-orchestration-engine
created: 2026-08-10
status: operator-approved-topology; written-spec-awaiting-operator-review
authority:
  - operator direction in the 2026-08-10 Codex session
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R2.md
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-08-R3-LOCAL-MODEL.md
---

# FEE Project Environment Design

## 1. Decision summary

Create a repo-native project environment for the Flow Execution Engine (FEE) before installing an agent runtime or extending execution code.

The environment combines:

1. canonical project and task state under `apex-meta/epics/fee-orchestration-system/` using the existing APEX Plan-Sync-Session task contract; and
2. a dedicated human-readable cockpit under `apex-meta/local-orchestration-engine/project/` for scope, user stories, roadmap, workstreams, traceability, evidence, efficiency, risks, decisions, status, and handover.

This is a control system for a complex program, not a new project-management application. It uses Markdown, existing APEX contracts, Git history, and links to evidence already in the repository.

No OpenClaw, Hermes, or Odysseus installation is part of this Phase-0 deliverable. No runtime wins because it appears in the roadmap. Runtime selection remains evidence-gated.

## 2. Correct system frame

### 2.1 FEE is broader than its first integration seam

Weekly Orchestrator step 4 is the first MVP seam, not the final FEE boundary. The later operator decision locks explicitly amend the earlier `step-4 attach only` design.

FEE is the reusable, cross-project execution and control plane that aligns four functional layers:

```text
Layer 4 — Subscription / deep-reasoning AI
  Plans, researches, synthesizes, judges, and supplies decision criteria.

Layer 3 — Scarce CLI AI
  Codex / Claude Code handles hard coding, architecture, difficult diagnosis,
  consequential review, and specialist escalation.

Layer 2 — Local LLM execution operator
  Executes frozen plans, selects bounded actions, drives permitted interfaces,
  captures evidence, performs limited recovery, and escalates uncertainty.

Layer 1 — Deterministic execution
  Python, PowerShell, Git, validators, schemas, capability enforcement,
  checkpoints, ledgers, hashes, and exact transformations.
```

FEE owns the deterministic execution authority boundary: frozen work packets, action identifiers, argument validation, capability and root scope, state, checkpoints, evidence normalization, retry budgets, and typed escalation.

FEE may serve Weekly Orchestration, Multi-Agent Orchestration, multiple projects and repositories, bounded coding, evidence collection, knowledge hygiene, subscription execution, overnight work, and future explicitly approved flows. It does not replace the planning or governance authority of Weekly Orchestrator, Meta Ops, subscription reasoning models, CLI specialists, or the human operator.

### 2.2 Source hierarchy

When sources conflict, the project environment applies this order:

1. current operator instruction;
2. operator decision locks, newest relevant lock first;
3. accepted APEX orchestration and Plan-Sync-Session contracts;
4. measured benchmark and implementation evidence;
5. platform research synthesis and candidate reports;
6. earlier architecture proposals and handovers;
7. raw research or historical notes.

This ordering resolves the current scope conflict. The following files retain useful implementation history but contain a stale step-4-only description that must be reconciled:

- `apex-meta/local-orchestration-engine/00-START-HERE.md`;
- `apex-meta/local-orchestration-engine/HANDOVER.md`;
- `apex-meta/local-orchestration-engine/architecture/01-macro-architecture-decision.md`;
- `scripts/fee/README.md`;
- `scripts/fee/__init__.py`.

Reconciliation must preserve the distinction between “first MVP seam” and “long-term system scope.” It must not falsely claim that all broad-scope capabilities are already implemented.

## 3. Phase-0 goals and non-goals

### 3.1 Goals

The project environment must make it possible to answer, without reconstructing chat history:

- What is FEE trying to achieve?
- Which parts are current authority, candidate architecture, implemented, tested, benchmarked, or merely researched?
- Which projects and workstreams exist, and why?
- Which user stories justify each workstream and component?
- What is the current roadmap and next bounded action?
- What decisions are locked, open, superseded, or reversible?
- What evidence supports every completion or selection claim?
- Is the program reducing human/CLI effort and maintaining reliability?
- Is the design drifting or becoming over-engineered?
- How can another chat continue safely and efficiently?

### 3.2 Non-goals

Phase 0 does not:

- install or select OpenClaw, Hermes, or Odysseus;
- certify Qwen3-8B or any other model/runtime;
- modify the existing FEE or lmbench runtime behavior;
- introduce a new database, web dashboard, SaaS project tool, or always-on service;
- duplicate canonical task status across multiple files;
- declare broad FEE capabilities implemented because they are described in the roadmap;
- authorize browser-account automation, consequential mutation, pushing commits, or personal-data access;
- collapse Weekly Orchestrator and Multi-Agent Orchestration into FEE.

## 4. Information architecture

### 4.1 File topology

```text
apex-meta/local-orchestration-engine/project/
  README.md
  00-PROJECT-COCKPIT.md
  01-PROJECT-CHARTER.md
  02-SYSTEM-BASELINE.md
  03-USER-STORY-PORTFOLIO.md
  04-ROADMAP.md
  05-WORKSTREAMS.md
  06-DELIVERY-BACKLOG.md
  07-TRACEABILITY-MATRIX.md
  08-QUALITY-GATES.md
  09-EFFICIENCY-SCORECARD.md
  10-RISK-REGISTER.md
  11-DECISION-REGISTER.md
  12-EVIDENCE-INDEX.md
  13-STATUS-AND-NEXT-ACTIONS.md
  14-GLOSSARY-AND-AUTHORITY.md
  15-HANDOVER.md
  templates/
    USER-STORY-TEMPLATE.md
    EXPERIMENT-TEMPLATE.md
    DECISION-TEMPLATE.md
    STATUS-UPDATE-TEMPLATE.md

apex-meta/epics/fee-orchestration-system/
  epic.md
  001.md
  002.md
  ...
```

### 4.2 Responsibility and update rules

| File | Sole responsibility | Update trigger |
|---|---|---|
| `README.md` | Read order, navigation, source-of-truth rules | File topology or governance changes |
| `00-PROJECT-COCKPIT.md` | One-screen program health and orientation | Every accepted status batch or operator decision |
| `01-PROJECT-CHARTER.md` | Mission, value, scope, non-goals, success | Operator changes the product boundary |
| `02-SYSTEM-BASELINE.md` | Current architecture and implementation truth | Material architecture, implementation, or benchmark change |
| `03-USER-STORY-PORTFOLIO.md` | User outcomes and acceptance behavior | User story added, revised, accepted, or retired |
| `04-ROADMAP.md` | Horizons, milestones, sequencing, and exit gates | Milestone exit, replan, or reversal trigger |
| `05-WORKSTREAMS.md` | Subproject boundaries, interfaces, and ownership | Workstream starts, splits, merges, or closes |
| `06-DELIVERY-BACKLOG.md` | Readable projection of canonical task records | Canonical epic/task change |
| `07-TRACEABILITY-MATRIX.md` | Story-to-requirement-to-task-to-test-to-evidence mapping | Any linked element changes |
| `08-QUALITY-GATES.md` | Gate definitions and current evidence status | Gate evidence or policy changes |
| `09-EFFICIENCY-SCORECARD.md` | Measured value, cost, intervention, and complexity | Benchmark or operational measurement lands |
| `10-RISK-REGISTER.md` | Active risks, controls, owners, triggers | Risk state or mitigation evidence changes |
| `11-DECISION-REGISTER.md` | Locked, open, superseded, and reversible decisions | Operator decision or evidence-based reversal |
| `12-EVIDENCE-INDEX.md` | Navigable index of authoritative evidence | Evidence artifact added, superseded, or invalidated |
| `13-STATUS-AND-NEXT-ACTIONS.md` | Current phase, blockers, and next bounded batch | Beginning or end of a working session |
| `14-GLOSSARY-AND-AUTHORITY.md` | Canonical terminology and authority ladder | Terminology or authority ambiguity appears |
| `15-HANDOVER.md` | Constant-frame continuation for another chat | End of material session or transfer |

### 4.3 Single-source-of-truth rules

- Canonical task status lives only in `apex-meta/epics/fee-orchestration-system/*.md`.
- `06-DELIVERY-BACKLOG.md` is a readable projection and links to canonical tasks; it does not independently mutate status.
- Current operator locks remain canonical in their existing decision-lock files. `11-DECISION-REGISTER.md` indexes and explains them rather than silently rewriting them.
- Raw benchmark evidence remains in `benchmark/results/` and local evidence directories. The cockpit records summaries and links.
- Research reports remain research evidence. They do not become implementation or certification state.
- The cockpit may say `UNMEASURED`, `UNKNOWN`, `CANDIDATE`, or `NOT_IMPLEMENTED`; it must never replace missing evidence with an optimistic estimate.

### 4.4 Governance roles

| Accountability | Role in the project environment |
|---|---|
| Operator | Confirms scope, priorities, consequential decisions, production authority, and evidence-based reversals |
| Planning agent / `apex-plan` contract | Proposes epic/task decomposition, dependencies, priority, and acceptance criteria without claiming durable mutation |
| Deterministic `apex-sync` capability | Validates dependencies, actionability, registry consistency, and other exact derived state |
| Gated `apex-session` capability | Owns operator-confirmed durable task/status/session mutation under the existing APEX contract |
| Current implementation agent | Executes only the approved bounded task, preserves evidence, updates candidate project views, and prepares the next gate |
| Independent reviewer / Detective | Tests consequential claims and artifacts without repairing its own findings or promoting candidates |

The cockpit is maintained as candidate operational documentation during a work batch. A consequential decision or canonical status change becomes accepted only through the applicable operator and APEX mutation boundary.

### 4.5 Review rhythm

- At session start: read `00-PROJECT-COCKPIT.md`, `13-STATUS-AND-NEXT-ACTIONS.md`, and the canonical active task.
- At task completion: attach evidence, update the canonical task through the accepted mutation path, refresh affected projections, and record regression triggers.
- At operator decision: update the decision register, affected risks, roadmap, traceability rows, and handover in one bounded documentation batch.
- At material model/runtime/configuration change: rerun affected benchmark fixtures before changing eligibility or routing claims.
- At session end: ensure the handover names one exact next step and that the cockpit contains no stale completion claim.
- At milestone exit: run a fresh-reader review plus link, schema, traceability, and Git-scope verification.

## 5. Program decomposition

### P0 — Program governance and alignment

Purpose: maintain the project environment, source hierarchy, decision discipline, status integrity, and handover quality.

Deliverables:

- project cockpit and canonical epic;
- corrected FEE system baseline;
- decision and risk registers;
- status, evidence, and handover procedures;
- stale-document reconciliation.

Exit condition: a new worker can identify the current mission, authoritative sources, implemented state, next task, and prohibited actions without reading chat history.

### P1 — Deterministic FEE authority spine

Purpose: converge the useful `scripts/fee` and `scripts/lmbench` mechanisms into a coherent production-oriented authority boundary.

Responsibilities:

- frozen work-packet contract;
- action IDs and typed argument validation;
- root/capability policy compiler;
- deterministic broker and filesystem guard;
- durable state/checkpoint and idempotency keys;
- evidence ledger and independent mutation audit;
- retry and escalation policy.

Exit condition: the authority spine can execute a runtime-neutral fixture, deny undeclared authority, resume without duplicate consequential action, and reconstruct evidence independently.

### P2 — Local-model bounded operator

Purpose: use benchmark-certified local model/runtime profiles to choose among pre-authorized actions and bounded recovery branches.

Current evidence:

- Qwen3-8B is installed in OpenVINO GenAI and llama.cpp/Vulkan configurations;
- the llama.cpp/Vulkan n=1 calibration produced 8 actor passes, 19 actor failures, and 1 infrastructure-invalid trial;
- zero successful unauthorized actions were observed;
- no task class is certification eligible;
- observed weaknesses include procedural incompleteness, over-escalation, and routing errors.

Exit condition: a profile passes the declared repeat protocol for its authorized task classes and meets all relevant hard gates. Model capability never expands authority.

### P3 — Replaceable execution runtime

Purpose: provide browser, tool, session, sandbox, process, and recovery mechanics behind the FEE contract.

Candidate order:

1. hardened OpenClaw runtime subset;
2. bounded Hermes runtime as the directly comparable runner-up;
3. Odysseus only after durable action-level restart/resume is measurable.

The runtime may not expose a generic shell, strategy authority, uncontrolled planning, or captured-content-driven capability expansion to the local model.

Exit condition: a candidate passes the common hard-gate fixtures and materially meets the reliability, intervention, resource, and maintenance requirements for at least one approved user-story class.

### P4 — Browser and subscription execution

Purpose: safely execute externally designed prompts on declared subscription surfaces and capture exact outputs and artifacts.

Responsibilities:

- declared provider and browser profile;
- fresh versus persistent session policy;
- text and artifact upload/download scope;
- bounded UI recovery;
- auth, CAPTCHA, security, payment, and account-change stop rules;
- provenance and selective screenshots.

Exit condition: authenticated-session fixtures complete reliably without bypassing stop conditions, losing provenance, or granting captured content execution authority.

### P5 — Workflow integrations

Purpose: expose FEE as a reusable bounded executor to existing APEX flows without absorbing their planning authority.

Integration families:

- Weekly Orchestrator;
- Multi-Agent Orchestration / Meta Ops work packets;
- bounded coding and script recovery;
- Detective evidence collection;
- KB, Informatics, and Prompts & Workflows hygiene;
- multi-repo project execution;
- separately gated personal flows.

Exit condition: each integration passes its own user-story simulation and produces evidence compatible with its owning orchestration contract.

### P6 — Benchmarking, evidence, and certification

Purpose: make all safety, reliability, utility, resource, and selection claims reproducible.

Responsibilities:

- fixture and oracle separation;
- trajectory, outcome, evidence, semantic, structural, authority, and resource grading;
- repeat-count enforcement;
- configuration identity and artifact hashes;
- runtime/platform comparison using the same model where possible;
- regression selection after material changes;
- candidate profile generation without automatic certification.

Exit condition: an independent reviewer can reproduce the verdict and see failed trials rather than averages that conceal them.

### P7 — Operations and lifecycle

Purpose: operate bounded jobs on Windows with predictable resource use, recovery, maintenance, and morning review.

Responsibilities:

- health/readiness and controlled load/unload;
- one active local-model action lane initially;
- blocked-job checkpointing and independent continuation;
- process cleanup and crash recovery;
- resource coexistence with browser, IDE, tests, and CLI agents;
- upgrade/regression policy;
- backup, rollback, and evidence retention.

Exit condition: an overnight test batch completes or blocks cleanly, preserves evidence, avoids duplicate side effects, releases resources, and yields an actionable review packet.

## 6. User-story portfolio

Every program task must trace to at least one story below or to P0 governance necessary to keep those stories reliable.

### US-FEE-00 — Operator sees and controls the whole program

As the operator, I can open one cockpit and understand current scope, implementation state, evidence, risks, efficiency, open decisions, and next actions without reconstructing prior chats.

Acceptance:

- current and target state are visibly separated;
- every completion claim links to evidence;
- stale or superseded sources are identified;
- the next bounded action is explicit;
- another chat can continue from the handover without widening scope.

### US-FEE-01 / UF-A — Subscription research execution

An approved reasoning plan and prompt set are executed on declared subscription surfaces, with exact capture and provenance returned for stronger synthesis.

Acceptance:

- the work packet fixes provider, session policy, prompts, allowed follow-ups, capture, recovery, and stop conditions;
- the executor cannot invent strategy or provider changes;
- logout, CAPTCHA, security, payment, or persistent uncertainty stops and escalates;
- exact response/artifact capture is reproducible.

### US-FEE-02 / UF-B — Script failure recovery

A deterministic script failure follows a closed recovery ladder before consuming scarce CLI AI.

Acceptance:

- only declared recovery actions are attempted;
- retry count is bounded;
- an unresolved case produces a compact evidence and escalation packet;
- no arbitrary generated repair command runs.

### US-FEE-03 / UF-C — Detective evidence collection

The local executor gathers objective evidence for an independent reviewer without promoting its own interpretation to authority.

Acceptance:

- read-only scope is enforced;
- observation and verdict fields remain separate;
- hashes, diffs, tests, logs, and provenance are sufficient for independent review;
- no candidate is silently promoted.

### US-FEE-04 / UF-D — Knowledge and data hygiene

Exact transformations are deterministic; bounded anomalies may be classified locally; semantic ambiguity is queued for review.

Acceptance:

- dry-run and diff precede write;
- uncertain records are not guessed;
- writes are reversible and evidence-backed;
- the owning specialist retains semantic authority.

### US-FEE-05 / UF-E — Multi-repo project execution

An approved job can use several explicit roots with distinct read/write scopes while rejecting undeclared roots and traversal.

Acceptance:

- root A may be read/write, root B read-only, and root C forbidden;
- the same restrictions cover file and process tools;
- cross-repo provenance remains reconstructable;
- no machine-wide implicit access exists.

### US-FEE-06 / UF-F — Personal weekly execution

Low-risk personal operations use a separate trust profile, evidence namespace, credential/browser identity, and stricter gates.

Acceptance:

- personal and project trust zones cannot cross implicitly;
- sensitive or consequential operations stop for operator review;
- personal scope is not enabled by project-flow approval.

### US-FEE-07 — Bounded coding operator

The local model executes exact patch specifications or at most one authorized micro-fix inside a severe scope and test envelope.

Acceptance:

- repository, files, actions, and acceptance tests are declared;
- architecture, public API, security, conflict, and unexpected-scope issues escalate;
- diff and test evidence are preserved;
- staging or committing requires explicit capability; pushing is not automatic.

### US-FEE-08 — Multi-Agent bounded worker

Meta Ops invokes FEE as a bounded worker/tool node and receives candidate artifacts plus evidence while retaining orchestration authority.

Acceptance:

- the work packet is externally frozen;
- FEE does not activate or redesign Multi-Agent Orchestration;
- candidate artifacts have zero automatic promotion authority;
- typed escalation returns to the deterministic router and declared owner.

### US-FEE-09 — Durable overnight execution and resume

Several independent jobs may be waiting or blocked while one resource-budgeted local action lane executes safely.

Acceptance:

- a killed runtime/model/browser resumes from the FEE checkpoint;
- consequential actions are duplicate-safe;
- blocked jobs release the active lane;
- independent non-overlapping work may continue;
- morning review lists completed, recovered, blocked, and review-required jobs.

### US-FEE-10 — Independent evidence reconstruction

An independent reviewer can reconstruct requested actions, validated arguments, runtime/model/provider identities, outputs, retries, failures, artifacts, and checkpoints from durable evidence.

Acceptance:

- ordered state transitions are recoverable;
- artifacts have paths, hashes, and provenance;
- infrastructure-invalid trials are not blamed on the actor;
- missing evidence cannot silently yield PASS or certification.

## 7. Roadmap design

### Horizon 0 — Establish project control

Deliver the cockpit, canonical epic/tasks, source hierarchy, corrected baseline, user-story portfolio, roadmap, registers, traceability, scorecard, evidence index, status page, and handover.

Exit gate: US-FEE-00 passes a fresh-chat continuation review.

### Horizon 1 — Reconcile and converge the deterministic spine

Reconcile stale narrow-scope documentation, map `scripts/fee` and `scripts/lmbench` overlap, freeze the runtime-neutral interfaces, and close action-level checkpoint/idempotency gaps.

Exit gate: T3 hostile-source inertness, T7 multi-root containment, T9 restart/resume, and T11 evidence reconstruction pass without a candidate runtime.

### Horizon 2 — Run the platform bake-off

Implement the minimal FEE runtime adapter, install/configure the hardened OpenClaw candidate, run common hard gates, then compare Hermes under identical fixtures if OpenClaw remains viable. Defer Odysseus until T9 is instrumented and its resumability can be compared fairly.

Exit gate: a runtime composition is selected for one bounded pilot or all candidates are rejected with evidence and a custom-adapter reversal decision.

### Horizon 3 — Qualify the local operator

Repeat Qwen3-8B trials at declared counts, compare OpenVINO and llama.cpp configurations, improve packet/procedure adherence without weakening gates, and test other model profiles only as authorized by the benchmark portfolio.

Exit gate: at least one model/runtime profile is eligible for explicitly named task classes; certification remains an operator decision.

### Horizon 4 — First complete four-layer vertical slice

Run subscription reasoning plan creation, deterministic freeze, bounded local execution through the selected runtime, exact capture, and CLI/human escalation/review.

Exit gate: US-FEE-01 and the relevant browser/security/evidence fixtures pass at the declared reliability and intervention policy.

### Horizon 5 — Expand workflow coverage

Add script recovery, Detective, knowledge hygiene, bounded coding, Weekly, and Multi-Agent adapters one story at a time.

Exit gate: every activated integration has a recorded story simulation, acceptance verdict, regression set, and owner.

### Horizon 6 — Multi-project and overnight operations

Add multi-root scheduling, blocked-job continuation, restart safety, resource coexistence, morning review, and lifecycle operations.

Exit gate: US-FEE-05 and US-FEE-09 pass under realistic browser, model, IDE, test, and CLI coexistence load.

### Horizon 7 — Production-readiness decision

Review safety, reliability, utility, resource, maintenance, account-policy, evidence, and rollback results. Approve only the task classes and trust profiles supported by evidence.

Exit gate: explicit operator go, limited-go, revise, defer, or reject decision with reversal triggers.

## 8. Canonical epic and initial task map

Create one umbrella epic: `fee-orchestration-system`.

Initial canonical task records:

| ID | Task | Workstream | Depends on |
|---:|---|---|---|
| 001 | Materialize Phase-0 project environment | P0 | none |
| 002 | Reconcile stale FEE scope documents | P0 | 001 |
| 003 | Validate user-story portfolio and acceptance corpus | P0/P6 | 001 |
| 004 | Map and converge `scripts/fee` and `scripts/lmbench` boundaries | P1 | 002, 003 |
| 005 | Specify and test runtime-neutral action/checkpoint/evidence adapter | P1/P3 | 004 |
| 006 | Instrument T3/T7/T9/T11 common hard-gate fixtures | P1/P6 | 005 |
| 007 | Install and test hardened OpenClaw composition | P3 | 006 |
| 008 | Run identical Hermes comparison when warranted | P3 | 006, 007 |
| 009 | Decide runtime composition from measured evidence | P0/P3/P6 | 007, 008 |
| 010 | Complete Qwen3-8B repeat and runtime comparison | P2/P6 | 003 |
| 011 | Decide eligible local-model task profiles | P0/P2/P6 | 010 |
| 012 | Implement subscription research vertical slice | P4/P5 | 009, 011 |
| 013 | Implement bounded recovery, Detective, hygiene, and coding stories | P5 | 005, 011 |
| 014 | Integrate Weekly and Multi-Agent bounded worker flows | P5 | 012, 013 |
| 015 | Validate multi-project and overnight operations | P5/P7 | 014 |
| 016 | Run production-readiness decision gate | P0/P6/P7 | 015 |

Dependencies in the task records are proposals until validated by the existing deterministic APEX sync mechanism. Status mutations must follow the existing APEX session boundary.

## 9. Traceability design

The traceability matrix uses one row per acceptance requirement and the following fields:

```yaml
traceability_row:
  story_id: US-FEE-00..US-FEE-10
  requirement_id: stable story-scoped identifier
  authority_source: operator lock or accepted contract
  workstream: P0..P7
  component_or_interface: named implementation surface
  canonical_task: apex-meta/epics/fee-orchestration-system/<id>.md
  fixture_or_review: exact test, simulation, or operator gate
  evidence_ref: path or UNMEASURED
  current_verdict: NOT_IMPLEMENTED | UNMEASURED | PARTIAL | PASS | FAIL | INFRA_INVALID
  regression_trigger: material change that requires rerun
```

Rules:

- no roadmap milestone exits with an untraced acceptance requirement;
- `PARTIAL` cannot be summarized as PASS;
- `INFRA_INVALID` remains separate from actor failure;
- failed cases remain individually visible;
- a research score never fills an implementation-verdict field;
- an n=1 result may establish observed containment evidence but not long-run reliability or certification.

## 10. Quality gates

### QG-0 — Alignment and authority

- current FEE scope matches R1/R2/R3 operator locks;
- stale scope descriptions are marked or corrected;
- no component receives undeclared planning or promotion authority;
- project facts have one canonical source.

### QG-1 — Authority containment

- zero successful unauthorized actions;
- captured content cannot create actions, paths, commands, providers, or workflow steps;
- generic runtime execution paths are unreachable from the local-model interface;
- action and argument validation occur before dangerous mechanics.

### QG-2 — Job-scoped permissions

- multiple roots support distinct read/write/forbidden modes;
- file and process paths share the same scope semantics;
- traversal, alternate path representation, and undeclared-root access are denied and traced.

### QG-3 — Resumability and idempotency

- FEE checkpoint is canonical;
- action IDs or idempotency keys prevent duplicate consequential actions;
- blocked jobs release resources and lanes;
- restart does not mutate the frozen plan.

### QG-4 — Evidence and attribution

- requested action, validated arguments, result, state transition, and artifact provenance are reconstructable;
- independent manifest/audit evidence can detect broker bypass;
- infrastructure errors are not converted into actor verdicts;
- missing evidence yields UNKNOWN/PARTIAL/FAIL, never silent PASS.

### QG-5 — Safe escalation

- retry budgets and recovery actions are closed and bounded;
- auth, CAPTCHA, security, permissions, ambiguity, conflict, and unexpected scope expansion stop correctly;
- escalation type and deterministic destination are valid;
- candidate artifacts never auto-promote.

### QG-6 — Windows and resource coexistence

- runtime, browser, local model, IDE, tests, and occasional CLI agent remain usable together;
- peak RAM/shared GPU memory, CPU, latency, crashes, and cleanup are measured;
- the active local-model action lane respects resource budgets.

### QG-7 — Utility and operational value

- approved jobs complete with acceptable intervention and escalation load;
- exact procedure requirements are followed, not merely the correct final intuition;
- time and scarce CLI effort saved exceed platform maintenance and babysitting cost;
- story-level reliability is based on declared repeat counts.

## 11. Efficiency and anti-overengineering design

### 11.1 Primary efficiency measures

| Measure | Calculation | Why it matters |
|---|---|---|
| Successful bounded jobs per wall hour | actor-pass jobs / elapsed wall hours | Captures throughput with reliability |
| Human intervention minutes per successful job | intervention minutes / actor-pass jobs | Detects babysitting cost |
| CLI escalations per successful job | specialist escalations / actor-pass jobs | Measures scarce-agent savings |
| Procedure-complete rate | jobs meeting all declared steps / valid trials | Exposes the current Qwen procedural weakness |
| Safe local recovery rate | successful declared recoveries / eligible failures | Measures useful autonomy |
| Evidence completeness | reconstructable required events / required events | Prevents unreviewable success |
| Resource coexistence | measured pass/fail plus peak resource values | Protects the operator workstation |
| Maintenance effort | measured person-minutes per upgrade/config change | Detects dependency burden |
| Runtime-specific code ratio | candidate-specific adapter code / total runtime-boundary code | Detects platform lock-in |
| Reversal cost | files/interfaces/data migrations required to replace runtime | Preserves replaceability |

All initial values are `UNMEASURED` except measurements already supported by committed evidence. No target is invented where the operator locks say acceptance thresholds follow baseline measurement.

### 11.2 Hard efficiency constraints

- zero successful unauthorized actions is non-negotiable and cannot be traded for speed;
- a runtime that saves CLI calls but increases human babysitting is not efficient;
- a faster model that omits required procedure is not more effective;
- a multi-runtime production architecture requires a large, repeatable story-specific advantage;
- documentation summaries must link rather than copy long evidence bodies;
- no new persistent service or database is added until a file-based limitation is observed and recorded;
- no automation is built merely to update a field that changes rarely or remains operator-judgment based.

### 11.3 Complexity review trigger

A design change requires an explicit complexity review when it adds any of:

- an always-on process;
- a new durable data store;
- a new credential-bearing integration;
- another agent/runtime platform;
- duplicated canonical state;
- a privileged execution path;
- a new schema that overlaps an existing APEX contract;
- a component without a traced user story and acceptance fixture.

The review records expected value, simpler alternative, maintenance cost, removal path, and reversal trigger in the decision register.

## 12. Risk model

The initial risk register must include at least:

| Risk | Initial state | Required control |
|---|---|---|
| Scope drift from stale FEE documents | active | source hierarchy, reconciliation task, glossary |
| Prompt/captured-content authority injection | active hard-gate risk | structural zero-authority boundary and adversarial fixtures |
| Generic runtime shell/tool bypass | unresolved | wrapper-only action interface and reachability tests |
| Duplicate consequential action after restart | unresolved | canonical checkpoint plus idempotency test |
| Browser account suspension / terms risk | accepted but consequential | explicit account policy and operator gate before live automation |
| Authentication/CAPTCHA/security challenge | expected operational risk | fail-closed stop and typed escalation |
| Model procedural incompleteness | observed | packet/prompt experiments and repeat benchmark |
| Model over-escalation and routing errors | observed | closed routing tests and procedure grading |
| Windows resource contention | partially measured | T12/COEX measurement under real workload |
| OpenClaw/Hermes release churn | unresolved | pinned versions, adapter contract, upgrade regression |
| Multi-runtime overengineering | active design risk | one primary candidate, evidence-earned additions only |
| Personal/project trust-zone leakage | unresolved | separate credentials, roots, profiles, evidence namespaces |
| Documentation/status duplication | active PM risk | canonical ownership and link-based projections |

## 13. Current evidence baseline

The project cockpit must begin with these facts:

- Git `main` and `origin/main` were verified at commit `88ac0a44` on 2026-08-10.
- Six unrelated `.bundle` files are untracked and must remain untouched unless separately authorized.
- `scripts/fee` contains a tested candidate subset for plan compilation, frozen-plan hashing, append-only ledger, assisted capture, strict paths, and injection containment.
- All 32 `scripts/fee` tests passed on 2026-08-10.
- `scripts/lmbench` contains the broker, path guard, tool schemas, runner, evidence trace, graders, report aggregation, and 28-fixture round-1 corpus.
- All 177 `scripts/lmbench` tests passed on 2026-08-10.
- Qwen3-8B is installed under OpenVINO GenAI and llama.cpp/Vulkan configurations.
- The first real llama.cpp/Vulkan benchmark is n=1 calibration, not certification.
- Observed result: 8 actor passes, 19 actor failures, 1 infrastructure-invalid trial, 5 denied unauthorized attempts, and zero successful unauthorized actions.
- OpenVINO has not yet run the same corpus.
- OpenClaw, Hermes, and Odysseus commands were not installed/found during the 2026-08-10 audit.
- The runtime bridge, full browser automation, action-level durable resume integration, and broad workflow adapters remain unbuilt.
- Platform research recommends hardened OpenClaw first, Hermes as runner-up, and Odysseus as a selective later candidate pending resumability evidence.

## 14. Status semantics

Project status values use the existing APEX task contract:

- `open` — accepted work not started;
- `in-progress` — active bounded work;
- `blocked` — cannot progress without a named condition or decision;
- `done` — acceptance and definition of done have evidence;
- `deferred` — intentionally postponed with rationale.

Evidence verdicts use a separate vocabulary:

- `NOT_IMPLEMENTED`;
- `UNMEASURED`;
- `PARTIAL`;
- `PASS`;
- `FAIL`;
- `INFRA_INVALID`.

Planning status and evidence verdict must never be conflated. A task may be `done` because a benchmark was correctly executed even when the benchmark verdict is `FAIL`.

## 15. Project cockpit design

`00-PROJECT-COCKPIT.md` is intentionally compact. It contains:

1. one-sentence mission;
2. current phase and last verified commit;
3. four-layer system diagram;
4. implementation truth table;
5. workstream health summary;
6. user-story coverage summary;
7. quality-gate summary;
8. efficiency snapshot;
9. top active risks;
10. open operator decisions;
11. next three bounded actions;
12. links to deeper project files.

It must fit within a practical single review pass and must not embed full research reports or raw benchmark output.

## 16. Handover design

`15-HANDOVER.md` follows the repository's constant-frame workflow and contains:

```yaml
frame:
  mission: current single project objective
  current_state: verified repo, implementation, benchmark, and decision state
  next_step_only: one bounded implementation or decision action
  explicit_non_goals: visible exclusions
  source_hierarchy: ordered authority sources
  allowed_reads: exact paths or families
  allowed_writes: exact planned surfaces
  forbidden_writes: protected and unrelated surfaces
  operator_gates: unresolved consequential decisions
  stop_conditions: security, scope, dirty-tree, evidence, and authority failures
  final_report_shape: exact completion report requirements
```

The handover additionally instructs the next chat to invoke `using-superpowers`, read the current cockpit and status files, use brainstorming for any changed design, use writing-plans before implementation, apply test-driven development to code changes, and verify evidence before claiming completion.

## 17. Error and conflict handling

- If cockpit and canonical task status disagree, canonical task files win and the cockpit is corrected.
- If an old architecture file conflicts with an operator lock, the lock wins and the conflict is recorded for reconciliation.
- If a benchmark summary conflicts with raw JSONL/evidence, raw evidence wins and the summary is corrected.
- If a task lacks a traced user story or governance justification, it does not enter implementation.
- If a completion claim lacks evidence, its verdict becomes `UNMEASURED` or `PARTIAL`.
- If an external candidate requires authority beyond the FEE contract, the integration stops; the contract is not weakened to accommodate it.
- If the worktree contains unrelated changes, implementation preserves them and stages only exact project files.
- If a new chat cannot identify the exact next step from the handover, the handover fails review and is revised before transfer.

## 18. Verification of the project environment

Phase 0 is complete only when:

1. every planned cockpit and template file exists;
2. the canonical epic and initial task records conform to the existing APEX task contract;
3. all internal relative links resolve;
4. all user stories map to at least one workstream, task, quality gate, and planned evidence path;
5. all roadmap horizons have explicit entry/exit logic;
6. current implementation and benchmark facts match repository evidence;
7. stale step-4-only sources are identified without erasing their history;
8. no file describes Qwen3-8B or a runtime platform as selected/certified without evidence;
9. no PM file duplicates canonical task status as an independent truth source;
10. the handover passes a fresh-reader audit: mission, current state, next step, permissions, gates, and stops are unambiguous;
11. Git diff contains only the intended Phase-0 files;
12. the operator reviews the completed environment before runtime implementation begins.

## 19. Implementation boundary after Phase 0

Once Phase 0 is accepted, the first technical design batch is Horizon 1, not immediate OpenClaw installation. It reconciles scope documentation, maps the existing FEE/lmbench mechanisms, defines the runtime-neutral adapter, and instruments the common hard gates. This prevents a candidate platform from shaping or bypassing the FEE authority contract.

OpenClaw installation becomes actionable only through its canonical task and after the adapter/gate prerequisites are satisfied or the operator explicitly changes that dependency with recorded rationale.

## 20. Design decisions locked by this specification

- Hybrid environment: canonical APEX epic/tasks plus dedicated FEE cockpit.
- Repo-native Markdown and existing contracts; no new PM runtime.
- Broad four-layer FEE system frame; Weekly step 4 is the first seam only.
- User stories and measurable evidence drive components and roadmap.
- One source of truth per status, decision, and evidence class.
- OpenClaw-first remains a research-supported candidate order, not a selection.
- Hard-gate and runtime-neutral authority work precede live candidate integration.
- Efficiency includes human intervention, scarce CLI use, procedure fidelity, resource coexistence, maintenance, and reversal cost.
- Handover is a first-class program artifact and must preserve a constant frame.
