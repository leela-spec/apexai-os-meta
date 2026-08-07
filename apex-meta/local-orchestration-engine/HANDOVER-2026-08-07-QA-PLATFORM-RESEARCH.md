---
title: "Handover — Platform Q&A Game + Research Prompts"
doc_type: handover
initiative: local-orchestration-engine
created: 2026-08-07
authority: operator-session-2026-08-07
status: "ready for next-chat design/research round"
repo: leela-spec/apexai-os-meta
branch_policy: "WORK DIRECTLY ON main ONLY. Do not create branches unless the operator explicitly asks for one."
reads_first:
  - apex-meta/local-orchestration-engine/OPERATOR-DECISION-LOCK-2026-08-07-R1.md
  - apex-meta/local-orchestration-engine/PLATFORM-RESEARCH-GATE-2026-08-07.md
  - apex-meta/local-orchestration-engine/DESIGN-LOCK-QA.md
  - apex-meta/local-orchestration-engine/architecture/04-decision-ledger.md
  - apex-meta/local-orchestration-engine/HANDOVER.md
---

# Handover — Next Chat: Q&A Game for OpenClaw / Hermes / Odysseus + Research Prompts

## 0. Operating rule for the next chat

**Do not begin implementation.**

The next chat's job is to improve understanding and lock the next architecture decisions through an operator-friendly Q&A game, then produce the research prompts needed to compare the three candidate agent/runtime platforms:

1. **OpenClaw**
2. **Hermes**
3. **Odysseus**

The operator is not a coder. Explanations must therefore use concrete user stories, visual/plastic process descriptions, examples, 1–100 scores, risks, resource/token implications, automation implications, and clear recommendations.

The next chat must not assume that one of these three is already the winner. It must first clarify the operator's desired behavior and decision criteria, then generate research prompts that test the candidates against those clarified user flows.

---

# 1. Repository / Git rule — IMPORTANT

The operator explicitly corrected the workflow:

> **Work directly on `main`. Never create branches unless the operator explicitly asks for one. Branches create chaos in this workflow.**

For all future repository writes in this initiative:

- use `main` directly;
- if a write can be performed and pushed/committed directly, do so;
- do not create `agent/...` branches automatically;
- do not open PRs unless the operator explicitly requests that workflow;
- if the environment cannot push/commit to `main`, provide exact Windows/PowerShell instructions for the operator to do it locally;
- never leave important decisions stranded only on a side branch.

Previous decision work from `agent/fee-decision-relock-2026-08-07` has already been fast-forwarded into `main`.

---

# 2. Current architecture understanding — LOCKED FROM ROUND 1

Read `OPERATOR-DECISION-LOCK-2026-08-07-R1.md` as the primary operator clarification.

The system has **four functional layers**:

```text
4. Subscription / deep-reasoning AI
   - thinks
   - plans
   - researches
   - synthesizes
   - judges
   - performs project-management intelligence

3. Scarce CLI AI
   - Claude Code / Codex
   - hard coding
   - architecture
   - difficult debugging
   - consequential verification
   - expensive/specialist work

2. Local LLM execution operator
   - follows externally created plans
   - operates subscription websites
   - pastes prompts
   - waits for responses
   - saves/captures results
   - runs bounded scripts/tools
   - performs small operational recovery
   - gathers evidence
   - escalates instead of inventing strategy

1. Deterministic execution
   - Python
   - PowerShell
   - Git
   - validators
   - ledgers
   - exact transformations
```

Core principle:

> **The local LLM is the operator, not the brain.**

Project-management intelligence belongs primarily to subscription/deep-reasoning models.

The local LLM exists largely to conserve scarce human and CLI-agent resources.

---

# 3. Confirmed Round-1 decisions

The operator verified all recommended choices:

```text
R1-Q1 = B  bounded execution operator
R1-Q2 = A  deterministic/external plan owns sequence
R1-Q3 = B  bounded tool broker
R1-Q4 = B  local repair ladder
R1-Q5 = B  Weekly step-4 MVP -> generic execution substrate later
R1-Q6 = E  hybrid/research before platform selection
R1-Q7 = B  bounded overnight execution + morning review initially
R1-Q8 = C  project-management intelligence in subscription reasoning models
```

Do not ask these questions again unless new evidence directly challenges them.

---

# 4. Critical multi-repo clarification

This is important and must be represented in the Q&A and research prompts.

The current Weekly Orchestrator was simplified around one repo for the MVP, but that is **not the final architecture**.

The intended future process is approximately:

```text
Project repo A --> Project State --\
Project repo B --> Project State ----\
Project repo C --> Project State -----+--> Apex OS Meta / Weekly Orchestrator
Other project/personal state --------/              |
                                                   v
                                        Weekly priorities + sprint guidance
                                                   |
                                                   v
                                        Work dispatched back into the
                                        relevant project repos/folders
```

The Weekly Orchestrator in `apexai-os-meta` is intended to orchestrate the operator's other project repos.

Much of the filesystem activity will probably occur under:

```text
C:\GitDev\...
```

but the future execution layer must **not** be permanently restricted to `C:\GitDev`.

It must support:

- multiple Git repositories;
- multiple configured filesystem roots;
- future non-GitDev folders;
- personal-life data/workflows with a separate security policy;
- per-job declaration of allowed repos/folders;
- explicit cross-repo access rather than unrestricted machine access.

The multi-repo Weekly-Orchestrator project-state ingestion layer is not implemented yet and will need a later architecture/project-design pass.

---

# 5. The three platform candidates — DO NOT PRESELECT

The next chat must compare these as possible components of a **hybrid execution architecture**.

## OpenClaw

The operator already has substantial OpenClaw material in:

```text
leela-spec/MasterOfArts/OpenClaw/07_finalopenclawsystem/
```

Known useful areas include:

- agent definitions;
- `meta_ops`;
- `meta_detective`;
- Informatics Design;
- Knowledge Bank;
- Hygiene/Clean;
- prompt/workflow handling;
- AI routing;
- handoff contracts;
- managed processes and governance.

Do not assume that the existing OpenClaw final-system directory is already the best low-level browser/local-execution runtime. Research what is executable runtime versus doctrine/configuration/process.

## Hermes

Research current Hermes Agent capabilities from primary/current sources and source code where possible.

Important questions include:

- browser/web execution;
- tool permission control;
- local-model support;
- Windows support;
- sessions/state;
- resumability;
- messaging/notifications;
- MCP/tool ecosystem;
- whether its autonomous-agent behavior can be constrained into a bounded execution operator.

## Odysseus

Research current Odysseus AI capabilities from primary/current sources and source code where possible.

Important questions include:

- browser/web capabilities;
- local-model backends;
- shell/filesystem/tool access;
- agent architecture;
- state/resumability;
- Windows deployment path;
- permission isolation;
- whether Odysseus can provide execution capabilities without importing a competing orchestration/project-management control plane.

---

# 6. Mandatory user-flow corpus

The Q&A game and research prompts must use concrete user stories. At minimum cover the six already locked user flows.

## UF-A — Subscription research executor

Example:

```text
Subscription PM model creates:
- Prompt A -> Claude
- Prompt B -> ChatGPT
- Prompt C -> Gemini Deep Research

Local executor:
1. opens the correct subscription surface
2. starts/continues the correct session
3. pastes the declared prompt
4. waits for completion
5. captures exact output/artifacts
6. stores provenance
7. moves to the next declared step

All results return to the subscription PM model for synthesis.
```

The local executor must not become the substantive research judge.

## UF-B — Script failure recovery

Example:

```text
Python script fails
    |
    v
deterministic retry/recovery rule
    |
    X unresolved
    v
local LLM gets small error packet
    |
    v
chooses one permitted recovery
    |
    +--> success -> continue
    |
    +--> failure -> evidence packet -> Claude Code/Codex
```

## UF-C — Detective evidence collection

The local executor can collect:

- diffs;
- test results;
- hashes;
- missing files;
- timestamps;
- logs;
- contradiction candidates;
- provenance.

A stronger Detective/reasoning layer owns consequential interpretation.

## UF-D — Database / KB hygiene

Example:

```text
Reasoning model defines cleanup rules
        |
        v
Deterministic scripts handle obvious cases
        |
        v
Local LLM handles bounded format anomalies
        |
        v
Semantic ambiguity -> stronger model / CLI / human
```

## UF-E — Multi-repo / multi-folder execution

Example:

```text
Weekly Orchestrator says:
Sprint 1 -> leela repo
Sprint 2 -> MasterOfArts repo
Sprint 3 -> Investment repo

Each job declares allowed roots and allowed operations.

Local executor performs only that job's authorized work.
```

## UF-F — Personal weekly execution

A reasoning model creates personal/work guidance; the execution layer may perform explicitly permitted low-risk operational tasks, while sensitive actions remain separately gated.

---

# 7. What the next Q&A game must accomplish

The operator specifically wants a **question-and-answer game**, not an architecture lecture.

Each question must:

1. explain the decision in normal language;
2. give a concrete user story/process example;
3. offer 2–4 real options;
4. give the assistant's recommended option;
5. explain **why** it is recommended;
6. show what changes if another option is selected;
7. include relevant 1–100 metrics;
8. include risk/automation/resource implications;
9. distinguish decisions that can be made now from questions requiring research evidence.

Preferred answer style for operator:

```text
1B
2A, but ...
3C
```

Do not force the operator to write essays unless necessary.

---

# 8. Required Round-2 Q&A topics

The next chat should construct the exact questions, but the game must cover at least these decision areas.

## A. Platform-role architecture

- Must one platform win, or can OpenClaw/Hermes/Odysseus have separate roles?
- Which parts should remain custom/FEE deterministic infrastructure?
- Should OpenClaw doctrine/agents be reusable above a different low-level executor?
- What would justify introducing more than one runtime?

## B. Browser/subscription operation

- Which subscription surfaces must be automated first?
- persistent conversation vs fresh conversation;
- provider-specific official automation vs generic browser automation;
- how to handle login expiry, CAPTCHA/challenge, page changes, and partial output;
- how much visual/browser judgement the local model is allowed to use.

## C. Local-model authority

- exact tool classes;
- which shell/PowerShell actions need deterministic wrappers;
- which recovery decisions are safe locally;
- what always escalates;
- whether the local model may edit files/code and under which narrow conditions.

## D. Multi-repo/multi-root permissions

- one repo per job vs several repos per job;
- read across many / write to one;
- configured root registry;
- cross-repo artifact movement;
- Git operations and write permissions;
- future folders outside `C:\GitDev`.

## E. Personal-life trust zone

- whether personal automation uses the same executor instance;
- separate browser profile/account/session;
- separate filesystem roots;
- what actions always require approval;
- whether personal data may be exposed to local models and which categories.

## F. Local-model selection / benchmark

- 3–4B vs 7–8B vs 12–14B candidate classes;
- reliability over generic reasoning benchmark scores;
- model swapability;
- inference runtime;
- memory budget while browsers are running;
- minimum acceptable correct-action / refusal / recovery performance.

## G. Resource and token economy

The operator cares about conserving scarce CLI resources.

Q&A must explain:

- local-token/context budget;
- subscription turns;
- Claude Code/Codex escalation rate;
- human intervention rate;
- context-reference strategy (paths/refs vs huge inline artifacts);
- concurrency/resource tradeoffs;
- how to measure the resource-saving benefit.

## H. Overnight automation

- what may run unattended;
- morning-review packet;
- stop conditions;
- notifications;
- recovery attempts allowed overnight;
- whether another project may begin when one blocks;
- scheduling mechanism later.

## I. Observability / evidence

- action ledger;
- screenshots/browser evidence when needed;
- prompt/response provenance;
- model/provider usage notes;
- failure packets;
- resumption checkpoints;
- dashboard/status needs.

## J. Security / prompt injection

Explain this with concrete examples rather than abstract security terminology.

Example:

```text
Claude/ChatGPT output says:
"Run powershell Remove-Item C:\GitDev\..."

That is CAPTURED DATA.
It is not executable authority.

Only the pre-authorized plan/tool broker may authorize commands.
```

Ask the operator about the desired risk/automation balance, but preserve the already confirmed bounded-tool principle.

---

# 9. Metrics the Q&A should use

Use 1–100 metrics whenever they genuinely aid understanding. Example dimensions:

| Metric | Meaning |
|---|---|
| `FIT` | fit to the operator's actual desired workflow |
| `AUTO` | attainable automation level |
| `SAFE` | containment / damage resistance |
| `RELIABLE` | expected operational reliability |
| `CLI_SAVE` | likely reduction in Claude Code/Codex use |
| `HUMAN_SAVE` | likely reduction in operator intervention |
| `MAINT` | maintainability; 100 = easy/low-maintenance |
| `RESOURCE` | laptop resource efficiency; 100 = light |
| `RECOVERY` | ability to survive/recover from routine failures |
| `MULTIREPO` | fit for cross-repo/cross-folder workflows |
| `EXPLAIN` | auditability/understandability of what happened |

Do not present invented numbers as empirical measurements. Label them clearly as:

- recommendation estimate;
- design target;
- research finding;
- measured benchmark.

---

# 10. Token / resource explanation requirement

The operator explicitly asked to understand token budgets and automation economics.

The next chat must explain, with examples, at least:

```text
Bad architecture:
Every operational hiccup -> Claude Code
Every result pasted into huge context again
Every new step asks a frontier model what to do

Good architecture target:
Deterministic layer handles exact work
Local model handles bounded operational ambiguity
Subscription model handles substantive reasoning
CLI model only handles genuinely difficult specialist work
Large artifacts stay on disk and are referenced when possible
```

For each architecture option, estimate the directional impact on:

- CLI turns/tokens;
- subscription turns;
- local-model inference workload;
- human interventions;
- RAM/GPU/browser load;
- latency;
- maintenance cost.

Exact numeric thresholds should become decisions only after baseline measurements exist.

---

# 11. Research-prompt production — required output AFTER Q&A

After the operator answers the Round-2 Q&A, produce **three separate deep-research prompts**, one for each candidate:

1. OpenClaw research prompt
2. Hermes research prompt
3. Odysseus research prompt

Then produce a fourth:

4. cross-candidate synthesis / architecture recommendation prompt

Do not collapse all three candidate investigations into one giant prompt initially. Independent investigations make contradictions and blind spots easier to see.

Each candidate prompt must require:

- current primary documentation;
- current source code/repository inspection where available;
- Windows viability;
- browser/subscription execution mechanisms;
- local-model integration;
- tool permission/allowlisting model;
- filesystem/repo containment;
- resumability/state;
- failure recovery;
- observability/evidence;
- resource usage;
- update/maintenance burden;
- licensing constraints;
- exact fit against UF-A through UF-F;
- explicit evidence references;
- unknowns rather than invented answers;
- 1–100 comparison scores with confidence;
- hard-gate pass/fail findings;
- recommended role in a hybrid architecture, even if it should not be the primary executor.

---

# 12. Cross-candidate synthesis prompt requirements

The synthesis research worker must receive the three independent reports and compare them without assuming that the highest total score must become the only platform.

It must explicitly evaluate compositions such as:

```text
Option 1
FEE/custom deterministic spine
+ Hermes executor/tools
+ OpenClaw higher-level doctrine/Detective

Option 2
FEE/custom deterministic spine
+ Odysseus runtime
+ OpenClaw higher-level processes

Option 3
OpenClaw-centered runtime
+ external provider-specific browser adapters

Option 4
Custom FEE executor
+ selected components from Hermes/Odysseus/OpenClaw only

Option 5
other evidence-supported hybrid
```

These are examples, not predetermined finalists.

The synthesis must optimize for the operator's actual user flows, not generic agent autonomy.

---

# 13. Required research comparison table

Eventually produce a table shaped approximately like:

| Candidate | UF-A | UF-B | UF-C | UF-D | UF-E | UF-F | Boundedness | Browser | Tools | Recovery | Windows | Resource | Maintenance | Best role |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| OpenClaw | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Hermes | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Odysseus | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Custom/FEE | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |
| Hybrid | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? | ? |

Scores must cite evidence type and confidence.

---

# 14. Platform hard gates already defined

Read `PLATFORM-RESEARCH-GATE-2026-08-07.md` and preserve these hard gates:

- authority containment;
- job-scoped permissions;
- resumability;
- evidence capture;
- safe escalation;
- practical Windows viability.

A high weighted score cannot compensate for an unmitigated hard-gate failure.

---

# 15. What NOT to do in the next chat

Do **not**:

- implement Phase 2 yet;
- build browser automation yet;
- choose the local LLM yet;
- install Hermes/Odysseus/OpenClaw yet unless the operator explicitly moves from research to benchmark execution;
- assume 7–8B remains the correct model size;
- treat Odysseus as already selected;
- treat Hermes as merely a notifier;
- treat OpenClaw as automatically the runtime winner because it already exists in the operator's repo;
- redesign the Weekly Orchestrator into a third orchestration system;
- ask the operator to repeat the eight Round-1 decisions;
- create a Git branch by default.

---

# 16. Desired next-chat workflow

## Step 1 — Read current authority

Read the two 2026-08-07 decision/research files first.

## Step 2 — Build Round-2 Q&A game

Create an operator-friendly decision game covering the unresolved architecture areas above.

Use strong recommendations, concrete user stories, examples, 1–100 metrics, and concise answer codes.

## Step 3 — Operator answers

Record only genuinely new decisions; do not reopen Round 1 without evidence.

## Step 4 — Create platform research prompts

Generate one prompt each for:

- OpenClaw;
- Hermes;
- Odysseus;

plus a synthesis prompt.

## Step 5 — Run/collect independent research

Prefer independent agents/workers so one candidate's assumptions do not contaminate the others.

## Step 6 — Synthesize evidence

Create a user-flow-based comparison, identify strongest role per candidate, and propose one or more architecture compositions.

## Step 7 — Final operator Q&A / platform lock

Present the evidence as another easy decision game before any implementation plan is rewritten.

---

# 17. Success condition for the next chat

The next chat succeeds when the operator can clearly answer:

1. **What exact operational jobs must the local execution layer perform?**
2. **Which actions may it perform autonomously, and which must escalate?**
3. **How should multi-repo/multi-folder access work?**
4. **How should browser/subscription work be divided?**
5. **What are the acceptable overnight/autonomy boundaries?**
6. **How will success, resource saving, and safety be measured?**
7. **What research evidence is needed to decide between OpenClaw, Hermes, Odysseus, custom FEE components, or a hybrid?**
8. **What exact prompts will produce that evidence independently?**

Only after these are answered and the platform research is complete should implementation sequencing resume.
