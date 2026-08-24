# Hermes Pre-Install Realization & Decision Runbook v2

Status: **ARCHITECTURE ACCEPTED / PRE-INSTALL QA / NO INSTALLATION**  
Date: 2026-08-22  
Architecture accepted: 2026-08-23  
Active target: **Hermes full-functional stack**  
Decision owner: Human CEO  
Alternative-system comparison: **DEFERRED**  
Optional Agency Agents pre-install pilot: **SKIPPED / FUTURE DEVELOPMENT**  
First semantic-provider trial: **OpenRouter -> `stealth/ox-alpha` (Ox Alpha), non-sensitive scope only**

## 0. Purpose

This runbook is the authoritative interactive process for proving or falsifying the complete Hermes target stack before installation.

It supersedes `QA-VALIDATION-RUNBOOK.md` for active execution. The older file remains historical evidence only.

The run is not allowed to make a requirement easier by replacing it with a reduced implementation. It must prove that the actual required Master of Arts operating loop can work end to end using existing upstream systems and documented integrations.

The active target includes:

- Hermes Agent;
- Hermes Kanban;
- existing MasterOfArts project folders;
- Hermes native hierarchical context;
- BMAD;
- MarketingSkills;
- official Hermes/QMD integration;
- Hermes memory and Curator;
- one verified semantic model/provider path;
- a low-friction safety configuration built only from Hermes-supported security controls.

OpenClaw is deferred and must not be evaluated during this run unless the operator explicitly reopens that work later. The 2026-08-23 operator review additionally deferred Agency Agents, AnythingLLM, and Semantic Router to future development; no optional stack-expansion pilot is part of this pre-install run.

For the first provider/model integration test, use Hermes' supported OpenRouter path with `stealth/ox-alpha` (Ox Alpha). Treat this as a **trial provider/model selection, not a production lock**. Current OpenRouter evidence shows the model is free during its stealth preview and that its provider retains prompts and completions. Therefore the first trial must use a non-sensitive or deliberately redacted project scope; Business/ACIM/private material must not be transmitted through this route until the operator explicitly resolves the privacy/isolation policy.

---

## 1. Operating law

### FULL_FUNCTION

A capability passes only if the required real workflow works end to end.

Do not substitute:

- a toy example for the actual project hierarchy;
- a short script for a missing orchestration capability;
- a manually pasted handover for durable context/state;
- an ad-hoc folder convention for an upstream project mechanism unless the upstream system explicitly expects that convention;
- a reduced "pilot version" that avoids the hard part of the user story;
- a second hidden task database for missing Hermes behavior.

The run may use paper simulations before installation, but the simulation must trace the complete production-intent flow and identify the exact upstream mechanism for every edge.

### UPSTREAM_ONLY

For every mechanism classify:

- `NATIVE_HERMES`
- `OFFICIAL_HERMES_INTEGRATION`
- `ESTABLISHED_AGENT_SKILL_PACKAGE`
- `DOCUMENTED_CONFIGURATION`
- `CUSTOM_REQUIRED`

`CUSTOM_REQUIRED` is a blocker in this run. Do not design the missing subsystem.

### EVIDENCE

Load-bearing claims require current official documentation or official repositories. Secondary material may identify questions but cannot establish a capability.

### NO_INSTALL

Do not install Hermes, QMD, BMAD, MarketingSkills or any other runtime component during this validation run.

### OPERATOR_WALKTHROUGH

Work phase by phase. At the end of every phase:

1. explain the verified result in plain language;
2. show the evidence matrix;
3. identify only decision-changing unknowns;
4. ask the operator for the relevant decision/confirmation;
5. update `state.yaml` if repository writes are authorized;
6. continue only after the phase is understood.

---

## 2. Authoritative read order

Read only what is needed for the current phase.

### Always read first

1. `ADR-002-full-functional-hermes-target.md`
2. `state.yaml`
3. `Orchestration/03-SCOPE-LOCK.md`
4. `Orchestration/07-INTEGRATED-AGENT-OPERATING-MODEL.md`
5. `Orchestration/02-PILOT-PROTOCOL.md`

### Historical/background only

- `ADR-001-provisional-hermes-stack.md`
- `QA-VALIDATION-RUNBOOK.md`
- `Orchestration/09-PRIMARY-ORCHESTRATION-SELECTION-HANDOVER.md`
- prior research runs

Use those only to recover evidence or understand why a question exists. They do not override ADR-002 or this runbook.

### Research tracks

Load the corresponding research file only when that phase begins:

1. `research/R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md`
2. `research/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md`
3. `research/R03-HERMES-QMD-REPO-INTEGRATION.md`
4. `research/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md`
5. `research/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md`
6. `research/R06-HERMES-CONTINUOUS-LEARNING.md`
7. `research/R07-MARKETINGSKILLS-HERMES-INTEGRATION.md`

---

# PHASE A — Verify the target stack edges

## A1. Show the whole call path

Use this exact target as the starting point:

```text
CEO
 -> Hermes Agent
    -> Hermes Kanban
       -> selected board/task/workspace
       -> real MasterOfArts project directory
    -> reusable specialist/profile
       -> BMAD skills
       -> MarketingSkills
       -> other approved Agent Skills
    -> project context
       -> root/family/project context files through Hermes-native discovery
       -> project files/assets/sources
    -> QMD
       -> official Hermes QMD skill
       -> Hermes native MCP client
       -> local QMD process/index
       -> scoped project/repo search results
    -> model/provider
       -> semantic reasoning
    -> review/request-changes/CEO gate
    -> durable task/artifact state
    -> governed Hermes memory/learning/Curator
```

## A2. Connection matrix

For every edge fill:

| From | To | Exact mechanism | Installed where | Local/remote | API/key | AI call? | Deterministic? | Persistent state | Custom code | Official source |
|---|---|---|---|---|---|---|---|---|---|---|

No blank `mechanism` cells are allowed.

## A3. Component fact cards

For every component produce:

```text
NAME:
MAKER:
WHAT_IT_IS:
ROLE_IN_TARGET:
MANDATORY_OR_SUPPORTING:
HOW_INSTALLED:
RUNS_LOCAL_OR_REMOTE:
WHAT_IT_READS:
WHAT_IT_WRITES:
NETWORK_REQUIRED:
API_OR_AUTH_REQUIRED:
DATA_LEAVING_MACHINE:
BILLING_PATH:
LICENSE:
DETERMINISTIC_OR_AI:
TOKEN_IMPACT:
OFFICIAL_SOURCE:
```

Required components:

- Hermes Agent
- Hermes Kanban
- Hermes context files
- Hermes profiles/worker identities
- Hermes memory
- Hermes Curator
- Agent Skills
- BMAD
- MarketingSkills
- QMD
- MCP specifically as Hermes <-> QMD transport
- selected model/provider path
- Git/GitHub only in the role actually required by the target

### Gate A

Operator question:

> Do all component roles and communication paths make sense, and is every edge currently verified as existing upstream behavior rather than an AI-designed connection?

Allowed state:

- `A_PASS`
- `A_BLOCKER:<edge>`

---

# PHASE B — Hermes safety on the local machine

Execute `research/R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md`.

The result must not be a generic cybersecurity essay. It must produce a concrete Hermes safety configuration profile for the target machine that protects the host without making normal Master of Arts work unusable.

Required normal operations that must remain possible:

- read/write approved MasterOfArts project files;
- normal Git status/diff/add/commit and ordinary push when explicitly authorized by workflow;
- run QMD locally;
- install/update approved upstream packages through a deliberate operator-controlled installation step;
- run deterministic scripts/checks in the project;
- create outputs/artifacts;
- use Hermes Kanban;
- use approved provider credentials without exposing unnecessary host secrets.

Required protected operations include at least:

- destructive disk/device operations;
- uncontrolled recursive deletion outside allowed workspace;
- force-push or destructive Git history operations unless separately authorized;
- pipe-to-shell remote execution;
- credential exfiltration;
- unrestricted messaging access;
- arbitrary access to unrelated local folders where a supported isolation mechanism can prevent it.

The research must compare official Hermes controls such as command approvals/deny rules, write-safe roots, local vs Docker backend, credential filtering, gateway user authorization and context-file scanning.

### Gate B

Operator chooses one evidence-backed Hermes security profile or marks a decision-changing blocker.

Allowed state:

- `B_SAFETY_PROFILE_CONFIRMED`
- `B_BLOCKER`

---

# PHASE C — Macro / meso / micro project and knowledge structure

Execute `research/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md`.

## C1. Inspect real projects

Use at least three materially different existing MasterOfArts areas. Do not normalize them before inspection.

For every sample record:

```text
PATH:
PURPOSE:
CURRENT_FILES_AND_ASSETS:
CURRENT_STATUS/PM_INFORMATION:
CURRENT_CANONICAL_OR_AMBIGUOUS_SOURCES:
WHAT_HERMES_LOADS_AUTOMATICALLY:
WHAT_HERMES_ONLY_READS_ON_DEMAND:
CURRENT_NAVIGATION/ORIENTATION_GAP:
```

## C2. Verify the upstream hierarchy

The desired semantic levels are:

- Macro: Master of Arts organization/portfolio;
- Meso: one project family/program/domain;
- Micro: one concrete delivery project.

The researcher must map those to actual Hermes concepts and actual repo context-discovery behavior. It may not invent a new project-management language.

For each level answer:

- Which Hermes board/task/workdir concept owns the execution state?
- Which context file(s) can be discovered natively?
- What is always loaded?
- What is progressively loaded?
- What factual knowledge remains ordinary project files?
- Which information is durable after restart?
- How does a shared specialist move into this context?
- How does another project remain out of context?

## C3. Repeating project structure

The research must determine whether Hermes/upstream Agent Skills already imply a repeatable project/family structure that can be applied consistently.

Do not design a custom folder taxonomy from scratch.

If a repeated file/folder is proposed, record:

```text
UPSTREAM_CONSUMER:
OFFICIAL_MECHANISM:
WHY_REQUIRED:
AUTOMATICALLY_DISCOVERED:
ALWAYS_LOADED_OR_ON_DEMAND:
WHAT_BREAKS_WITHOUT_IT:
```

A file/folder with no upstream consumer cannot be mandatory.

### Gate C

Allowed state:

- `C_NATIVE_PROJECT_MODEL_CONFIRMED`
- `C_NATIVE_MODEL_NEEDS_DOCUMENTED_CONFIGURATION`
- `C_CUSTOM_PROJECT_FRAMEWORK_REQUIRED` -> fail current target

---

# PHASE D — Hermes + QMD + current repo

Execute `research/R03-HERMES-QMD-REPO-INTEGRATION.md`.

QMD is a locked target component. This phase determines **how it is integrated correctly**, not whether it should be omitted for convenience.

Required proof:

1. official Hermes QMD skill installation path;
2. QMD installation/runtime requirements;
3. supported Windows/WSL path for the target environment;
4. exact Hermes -> MCP -> QMD call path;
5. exact repo paths/collections QMD should index based on the validated project model;
6. index/update behavior when files change;
7. project scoping so one specialist can search the current project without flooding context from unrelated projects;
8. deterministic vs local-model vs cloud-model work;
9. token impact;
10. local storage and data-egress boundaries;
11. failure/recovery and index rebuild behavior;
12. whether QMD can retrieve only relevant passages/files without becoming canonical project truth.

### Required simulation

Use at least:

- an exact known-file query;
- a semantic project query;
- a cross-document synthesis query;
- a query scoped to one project family;
- a query that must not pull irrelevant unrelated project material;
- a file-change then re-index/update scenario.

### Gate D

Allowed state:

- `D_QMD_INTEGRATION_CONFIRMED`
- `D_QMD_PLATFORM_BLOCKER`
- `D_QMD_REQUIRES_CUSTOM_CONNECTION` -> fail target until resolved

---

# PHASE E — Project knowledge lifecycle and freshness

Execute `research/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md`.

This phase answers how each project remains understandable and current after weeks/months of work.

It must distinguish:

- durable project facts/decisions;
- raw sources/research;
- current project status;
- finished artifacts;
- reusable procedures/skills;
- Hermes runtime/profile memory;
- QMD derived index.

The solution must come from existing Hermes/context/skill/project mechanisms and ordinary version-controlled project files. Do not invent a second KB engine.

Required lifecycle simulation:

```text
new source arrives
 -> agent works on it
 -> decision/output produced
 -> relevant durable project information updated
 -> QMD refresh sees the change
 -> next session retrieves current information
 -> obsolete/conflicting information remains distinguishable
```

The phase must identify how current project state and factual knowledge stay synchronized without asking the operator to maintain duplicate summaries manually.

### Gate E

Allowed state:

- `E_KNOWLEDGE_LIFECYCLE_CONFIRMED`
- `E_DUPLICATE_MANUAL_TRUTH_REQUIRED` -> blocker
- `E_CUSTOM_KB_REQUIRED` -> fail current target

---

# PHASE F — Shared specialists and priming

Execute `research/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md`.

The target pattern is:

```text
ONE REUSABLE SPECIALIST
 + shared role/profile instructions
 + shared proven skills
 + organization context
 + current project/family context
 + current micro-project task state
```

Not:

```text
Awakenings Marketing Agent
Lika Marketing Agent
Business Marketing Agent
...
```

unless Hermes itself requires separate profiles for a verified execution reason.

Required proof:

- where specialist identity/profile configuration lives;
- what is automatically injected;
- how skills are indexed and loaded on demand;
- how project context reaches the same specialist;
- how role instructions remain stable while project knowledge changes;
- how a reviewer profile differs from a maker profile;
- what another compatible CLI can reuse from the repo;
- what is Hermes-specific.

### Required two-project simulation

Use one shared Marketing specialist on:

1. a specific workshop launch;
2. a materially different Master of Arts offer/project.

Record exact context and skill loading for both.

### Gate F

Allowed state:

- `F_SHARED_SPECIALISTS_CONFIRMED`
- `F_DUPLICATED_AGENT_PER_PROJECT_REQUIRED` -> blocker

---

# PHASE G — Continuous learning

Execute `research/R06-HERMES-CONTINUOUS-LEARNING.md`.

The research must map the actual Hermes learning lifecycle rather than saying "the agent learns".

For each learning type identify exact storage and mechanism:

1. session-only information;
2. profile/runtime factual memory;
3. agent-created procedural skill;
4. hub/project/shared approved skill;
5. project factual knowledge/decision;
6. QMD index representation.

Required questions:

- What can Hermes create automatically?
- What does the background self-improvement process create?
- What does the Curator actually manage?
- What is excluded from Curator modification?
- How are usage, stale/archive state, backups, audit ledger and rollback implemented?
- When does an operator approve/pin/promote something?
- How can useful procedural learning become reusable across projects without silently changing approved upstream skills?
- How does factual learning return to the relevant project rather than being trapped in one profile memory?
- What model/token cost does continuous learning create?

### Gate G

Allowed state:

- `G_LEARNING_LIFECYCLE_CONFIRMED`
- `G_LEARNING_DRIFT_OR_CUSTOM_SYNC_REQUIRED` -> blocker

---

# PHASE H — MarketingSkills integration

Execute `research/R07-MARKETINGSKILLS-HERMES-INTEGRATION.md`.

MarketingSkills is a locked target skill package.

Required verification:

- exact current upstream source and license;
- exact supported installation mechanism into `.agents/skills/`;
- Hermes discovery/trust behavior for those project skills;
- how MarketingSkills' `product-marketing` context file works;
- whether its `.agents/product-marketing.md` assumption is compatible with a monorepo containing multiple project families;
- whether project-specific context is discovered relative to the active project or always from repo root;
- how the same MarketingSkills package can serve several project families without overwriting or mixing positioning context;
- whether any upstream-supported installation mode solves this directly;
- what other marketing skills read automatically vs on demand;
- whether the package performs semantic AI work only or includes deterministic tool/API integrations;
- external API/billing requirements per relevant skill;
- update/version behavior.

Do not customize/fork the package merely to make the architecture fit. If its context assumptions conflict with the MasterOfArts monorepo and no upstream-supported configuration solves it, record that as a real blocker.

### Gate H

Allowed state:

- `H_MARKETINGSKILLS_HERMES_CONFIRMED`
- `H_MARKETINGSKILLS_CONTEXT_CONFLICT`
- `H_CUSTOM_FORK_REQUIRED` -> blocker

---

# PHASE I — Integrated end-to-end user stories

Only begin after B–H evidence is recorded.

For every step in every user story fill:

| Step | Exact input | Component | Automatic context | On-demand context | Tool/skill | D/AI/H | Model/provider | Token driver | Data egress | Exact output | Durable location | Review/gate | Upstream status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

No row may say "agent knows" or "system handles it".

## US-1 — Research -> knowledge -> workshop

CEO asks a real bounded research question relevant to one Master of Arts project.

Required flow:

```text
CEO intent
 -> Hermes task/board context
 -> current project workdir/context
 -> QMD retrieval of existing project knowledge
 -> BMAD research workflow
 -> fresh web research where required
 -> research artifact + provenance
 -> independent reviewer
 -> request changes if needed
 -> CEO consequential decision
 -> accepted project knowledge/output update
 -> workshop workflow
 -> decision-ready workshop artifact
 -> durable project/task state
```

## US-2 — Workshop -> marketing launch

```text
approved workshop
 -> same project/family context
 -> shared Marketing specialist
 -> MarketingSkills product/positioning context
 -> launch/content skills
 -> landing copy + channel plan + social/video outputs
 -> reviewer
 -> CEO gate where consequential
 -> durable launch artifacts/tasks
```

## US-3 — Same Marketing specialist on another project

Repeat US-2 on a different project family without copying the specialist definition or manually pasting the previous project's context.

Pass only if the new project receives the right context and unrelated previous-project context is not automatically injected.

## US-4 — Weekly CEO operating cycle

Across at least three different Master of Arts areas:

```text
collect durable board/task/project state
 -> detect blocked/stale/dependent work
 -> retrieve project facts only where needed
 -> continue approved routine work
 -> surface consequential decisions
 -> persist CEO choices
 -> schedule/prepare next work
```

A fresh Hermes session must be able to answer:

- what matters now;
- why;
- what is blocked;
- what changed;
- who/what acts next;
- what needs CEO decision.

## US-5 — Failure/recovery

Simulate:

- Hermes process/session ends;
- model quota/auth fails;
- reviewer rejects output;
- project file changes during execution;
- QMD index is stale or missing;
- one worker never completes;
- parent task still has required unfinished work.

Show exact durable state and resume path.

## US-6 — Learning reuse

A successful task reveals a repeatable procedure.

Trace:

```text
observed procedure
 -> Hermes learning mechanism
 -> agent-created skill or other native learning destination
 -> Curator/audit behavior
 -> review/promotion decision
 -> next project can reuse procedure
```

Keep project facts separate.

## US-7 — Web subscription AI repo work

Verify per actual web AI/client:

- can read the private repo through an official connector/app;
- can read the same project context files;
- can inspect `SKILL.md` files;
- whether it natively activates Agent Skills or only follows them as documents;
- whether it can write approved repo artifacts;
- whether it can call local Hermes/QMD (do not assume);
- which useful tasks remain possible without local runtime access.

The objective is truthful interoperability, not pretending web and local CLIs are identical.

---

# PHASE J — Token, determinism, cost and privacy audit

For the integrated user stories report:

| Element | Always loaded? | On demand? | AI tokens? | Local compute? | External call? | Persistent? | Deterministic? |
|---|---|---|---|---|---|---|---|
| Root context | | | | | | | |
| Family context | | | | | | | |
| Micro-project context | | | | | | | |
| Skill index | | | | | | | |
| Full BMAD skill | | | | | | | |
| Full Marketing skill | | | | | | | |
| QMD query | | | | | | | |
| QMD returned passages | | | | | | | |
| Kanban state action | | | | | | | |
| Model reasoning | | | | | | | |
| Reviewer pass | | | | | | | |
| Hermes memory injection | | | | | | | |
| Curator pass | | | | | | | |

For every external provider/service record:

- authentication;
- subscription/API billing path;
- exact data transmitted;
- whether private project content leaves the machine;
- whether local execution is available;
- whether the component is mandatory for that user story.

---

# PHASE K — Installation blueprint, still not execution

Only after A–J pass, create an exact implementation blueprint using **official commands/config only**.

Required order:

1. safety prerequisites;
2. Hermes install;
3. provider/auth configuration;
4. safety configuration;
5. repo/workdir verification;
6. Hermes project-context verification;
7. BMAD install/discovery;
8. MarketingSkills install/discovery;
9. QMD install;
10. Hermes QMD skill/MCP configuration;
11. QMD collection/index configuration derived from validated project structure;
12. Kanban/project configuration;
13. memory/Curator configuration;
14. smoke tests;
15. full user-story acceptance tests;
16. rollback/uninstall path.

For every command include its official source and expected result. If a command is not verified, label `NOT VERIFIED — DO NOT EXECUTE`.

No custom script may silently stand in for a failed upstream installation/configuration step.

---

# PHASE L — Final CEO decision

Present exactly these options:

- `APPROVE_INSTALL_HERMES_TARGET_STACK`
- `RESEARCH_BLOCKER:<name>`
- `REJECT_HERMES_TARGET_STACK`

Do not offer OpenClaw in this run.

Do not infer approval from partial agreement.

---

## Required final deliverable

Before installation, the validating chat must produce:

1. **Verified architecture flowchart** — every edge upstream-supported.
2. **Component interaction matrix** — local/remote/API/auth/data/custom work.
3. **Safety configuration decision** — exact official controls and expected friction.
4. **Macro/meso/micro project model** — mapped to actual Hermes/project mechanisms.
5. **Project knowledge package/lifecycle** — complete, repeatable, current and retrievable.
6. **QMD integration design** — official path, collections/scoping/update behavior, Windows/WSL support.
7. **BMAD integration result**.
8. **MarketingSkills integration result** including multi-project product-marketing context behavior.
9. **Specialist priming model** — shared roles across projects.
10. **Continuous-learning model** — memory vs skills vs project facts, Curator boundaries.
11. **User-story simulation matrices**.
12. **Deterministic vs AI execution matrix**.
13. **Token/context/cost/privacy matrix**.
14. **Web subscription AI capability matrix**.
15. **Failure/recovery matrix**.
16. **Official installation blueprint**.
17. **Unresolved blockers** — only genuine blockers, no invented repair architecture.
18. **CEO decision** — one option from Phase L.

## Run acceptance standard

The run is complete only when the operator can explain in plain language:

- what Hermes owns;
- where Master of Arts projects and knowledge live;
- how macro/meso/micro context works;
- how the same specialist serves multiple projects;
- where BMAD and MarketingSkills live and how Hermes discovers them;
- how QMD indexes and retrieves the repo;
- what MCP connects in this exact stack;
- what gets loaded automatically vs retrieved on demand;
- which steps call an AI and which are deterministic;
- what consumes cloud tokens/quota;
- what information leaves the machine;
- how Hermes is constrained on the local system without blocking normal work;
- what Hermes learns and where that learning goes;
- what remains usable from a web subscription AI;
- how interrupted work resumes;
- which parts are upstream and whether any required custom subsystem remains.

If any answer still depends on "we will build something for that," the target has not passed.
