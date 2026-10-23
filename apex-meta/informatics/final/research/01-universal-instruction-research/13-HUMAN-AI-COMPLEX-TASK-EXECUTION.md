---
type: OperationalCompanion
title: Human-AI Complex Task Execution Guide
description: Human-facing orchestration entrypoint for turning one complex task into disciplined instructions for another AI while using the Universal AI Instruction System by reference and progressive disclosure.
status: operational_companion_candidate
created: 2026-09-07
---

# Human-AI Complex Task Execution Guide

## Purpose

Use this file when a human has a **specific complex task** and wants one AI to act as the **orchestrator/instruction architect** for another AI that will execute the work.

This file is not a replacement for the Universal AI Instruction System. It is the operational companion that tells the orchestrator **how to combine the system's rules into one bounded execution packet without copying every module into one giant prompt**.

Primary flow:

```text
HUMAN / OPERATOR
    |
    | gives target, context, constraints, repository/environment
    v
ORCHESTRATOR AI
    |
    | establishes current truth
    | resolves the substantive target
    | grounds material real-world assumptions
    | prefers proven reuse before invention
    | chooses proportional workflow
    | loads only relevant deeper instructions
    | produces one execution packet
    v
EXECUTOR AI / AGENT
    |
    | executes bounded work
    | returns evidence, diff/results, uncertainty, blockers
    v
ORCHESTRATOR / HUMAN
    |
    | validates the actual outcome
    v
NEXT AUTHORIZED STEP OR STOP
```

The orchestrator is responsible for **instruction quality and discipline**. The executor is responsible for **doing the authorized work**. The human retains authority over material choices, permissions, and gates that have not been delegated.

---

# 1. Authority order

Before instructing another AI, establish which material is current authority.

For the Universal AI Instruction System itself, read in this order:

1. `README.md` — live current truth, locked architecture, module state.
2. `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` — current candidate compact contract.
3. Completed `module-deepening/<ID>-<slug>/README.md` results only when the task requires that module's deeper semantics.
4. `10-UNIVERSAL-SHORT-RULE-COVERAGE-TODO.md` — unresolved controls that must not be forgotten during final synthesis.
5. `11-ONLINE-MODEL-PATCH-HANDOFF-DECISION.md` — browser/subscription-model repository mutation boundary when relevant.
6. `12-PENDING-ARCHITECTURE-PATCHES-AUTHORITY-MUTATION.md` — pending, not-yet-canonical A14/C04 integration proposals.
7. Older architecture/research files only as background evidence when needed.

Do not treat an older file as current merely because it is more detailed.

Do not silently promote pending candidates into canonical rules. When a pending candidate is operationally useful before formal module completion, label it explicitly as **provisional**.

---

# 2. The orchestrator's job

The orchestrator must translate the human's request into a worker instruction that is:

- faithful to the substantive intended outcome;
- bounded by scope and authority;
- grounded in current external reality where material;
- biased toward battle-proven reuse rather than custom invention;
- proportionate to complexity, uncertainty, coupling, and consequence;
- based on current project/repository state;
- explicit about what the executor may change and what it must not change;
- explicit about validation and stop conditions;
- compact enough that the executor can act rather than drown in process.

The orchestrator must not substitute its own architecture project for the user's task.

The orchestrator must not write a long process merely because the task is complex. Every instruction should earn its place by reducing a material execution risk or improving the likelihood of the intended outcome.

---

# 3. Complex-task preflight

Before writing the worker prompt, resolve the following.

## 3.1 Target

State the **substantive useful outcome**, not merely the artifact name or observable proxy.

Ask:

- What must be true when this task is genuinely successful?
- What user-facing, system-level, research, design, or operational capability is being requested?
- Which tests/files/checklists are evidence rather than the target itself?

If the request says "create a Skill", the target is not merely `SKILL.md` existing. The target is a Skill that reliably teaches the intended capability.

If the request says "evaluate the architecture", implementation is not progress unless implementation was authorized.

## 3.2 Current truth

Identify the current authoritative project/repository/environment state before instructing changes.

For repository work, establish at minimum when available:

- repository;
- branch/ref;
- relevant current files;
- current architecture/SSOT;
- existing implementation that may already satisfy the need;
- active constraints and recent superseding decisions.

Do not reconstruct live state from memory when the repository or connected source can be read.

## 3.3 Scope

Separate:

- work directly required by the target;
- supporting work that materially enables the target;
- governing constraints;
- adjacent improvements;
- speculative future work;
- explicitly excluded work.

Do not use scope control to justify shallow under-delivery.

Do not use a broad target to justify opportunistic cleanup that does not materially contribute to it.

## 3.4 Authority

**Provisional pending control until A14 is formally deepened:** scope does not automatically imply permission to perform every side effect.

Determine whether the executor is authorized to:

- read/search/analyze;
- create new files;
- modify existing files;
- commit/push;
- delete/move/rename;
- install dependencies;
- change configuration;
- contact external services;
- deploy/publish/send;
- perform costly, destructive, privileged, or irreversible actions.

Where authority is not clear and the action is consequential, preserve the decision for the human rather than inferring permission from task relevance alone.

## 3.5 Actual tool capability

Verify what the **actual execution surface** can do.

Do not infer that a capability documented for a CLI, SDK, API, local coding agent, shell runtime, or another product is available to the current browser/subscription model or connector.

Examples of capabilities that must be verified rather than assumed:

- localized file editing;
- shell/Git commands;
- native patch application;
- branch creation;
- connector writes;
- external browsing;
- test execution;
- local filesystem access.

Design the workflow around tools that actually exist in the active environment.

---

# 4. Ground before designing

For material decisions that depend on real-world facts, current software behavior, integrations, methods, standards, maturity, reliability, or available products, do not let model reasoning become the primary evidence.

Use the current A13 candidate behavior:

```text
model reasoning
    +
current authoritative external evidence
    +
direct observed use/test when feasible
    ->
real-world-grounded decision
```

Research should answer concrete load-bearing questions such as:

- Does this capability actually exist?
- Is this integration officially supported?
- Is this product maintained and mature enough for the target?
- Does the documented workflow match the actual execution environment?
- Is the recommended practice current?
- Are there known limitations that invalidate the design?

Distinguish:

- documented fact;
- observed/tested behavior;
- reasonable inference;
- unresolved uncertainty.

Never fill an evidence gap with a plausible architectural assumption without labeling it.

---

# 5. Reuse before invention

For nontrivial capability, establish whether a proven solution already exists before instructing custom construction.

Preferred realization order:

```text
1. reuse proven project-local capability
2. reuse battle-proven external capability in established form
3. compose proven components
4. adapt only the smallest verified project-specific surface
5. custom-build only the residual gap that proven options cannot satisfy
```

Do not satisfy this rule by mentioning existing products and then recreating them locally.

Do not blindly adopt a popular tool either. Proven pedigree is evidence, not automatic proof of fit. Validate the reused solution against the actual target, constraints, and environment.

For consequential reuse/build decisions, the rejection of proven options should be evidence-backed rather than based on statements such as "custom will be cleaner" or "this seems easier".

---

# 6. Choose workflow depth proportionately

Use the task's actual complexity rather than a fixed ritual.

### Direct execution

Use when the task is:

- clear;
- bounded;
- low risk;
- low coupling;
- easily reversible;
- supported by current context.

Do not create unnecessary plans, matrices, agents, or review gates.

### Structured execution

Increase planning/decomposition when the task has material:

- ambiguity;
- dependency chains;
- multiple subsystems;
- external integrations;
- expensive or irreversible effects;
- high consequence;
- competing solution alternatives;
- long-running or restart-sensitive work;
- independent workstreams suitable for delegation.

For multilevel work, use the established realization direction:

```text
TARGET / SYSTEM
    ↓
MESO / MODULES / INTERFACES
    ↓
MICRO / IMPLEMENTATION

then validate upward:

MICRO RESULT
    ↑
MODULE / INTERFACE VERIFICATION
    ↑
SYSTEM / TARGET VALIDATION
```

Keep lower-level work traceable to the parent outcome.

---

# 7. Progressive disclosure

Do not make the worker read the whole Universal AI Instruction System by default.

The orchestrator should load and cite only the modules/deeper material relevant to the task.

Typical routing:

| Need | Owner |
|---|---|
| substantive outcome / anti-proxy / completion validation | A01 `<target>` |
| task boundaries / non-goals | A02 `<scope>` |
| proven reuse before custom build | A03 `<reuse>` |
| planning/decomposition/review depth | A04 `<workflow>` |
| material ambiguity / clarification threshold | A05 `<intent>` |
| context minimization / JIT retrieval | A06 `<context>` |
| hierarchical realization / V&V | A07 `<realization>` |
| evidence/provenance/freshness/uncertainty | A08 `<evidence>` |
| recovery/escalation | A10 `<recovery>` |
| authoritative current state | A11 `<current_truth>` |
| communication economy | A12 `<communication>` |
| external real-world grounding | A13 `<grounding>` candidate/current program owner |
| action authority / side effects | A14 `<authority>` pending candidate |
| trade-study / operator decision | C01 `<decision>` |
| deeper research method | C02 `<research>` |
| Informatics/formal repository authoring | C03 `<informatics>` |
| browser/subscription-model existing-file mutation | C04 `<mutation>` pending candidate |

Load a deeper method only when its trigger is genuinely present.

---

# 8. Repository mutation boundary

When the orchestrator itself is an online/browser subscription model using a repository connector that rewrites existing files as whole-file replacements, use the current patch-handoff decision:

> **Existing repository files are patch-proposal only.**

Preferred reference format:

> **Aider `editor-diff` / SEARCH-REPLACE blocks**

The browser model should:

1. read the current target file;
2. propose the bounded patch/change;
3. hand it to a separate authorized editor/executor;
4. require the executor to apply against current state;
5. inspect/verify the resulting change before considering the work complete;
6. re-read and regenerate if the target state no longer matches rather than improvising around the mismatch.

Do not infer `git apply`, shell patching, API `apply_patch`, or other local-agent functionality merely because another environment supports it.

Creation of a genuinely new explicitly authorized file is a separate case because no existing file body is overwritten.

---

# 9. Recovery discipline

When execution encounters a problem:

- diagnose the actual failure;
- preserve target and scope;
- use the narrowest proven recovery that restores progress;
- do not turn incidental failure into a redesign project;
- do not repeatedly repair the same failing subsystem without learning whether the approach itself is wrong;
- preserve completed expensive work when safe;
- avoid retrying durable/external effects blindly.

If the failure changes the architecture choice, target, authorization, safety, or integrity of the result, escalate rather than hiding the decision inside a workaround.

Retry/replay/idempotency ownership is still an open final-synthesis item in `10-UNIVERSAL-SHORT-RULE-COVERAGE-TODO.md`; treat duplicate durable side effects as a material risk until that ownership is finalized.

---

# 10. What the orchestrator must give the executor

For a complex task, produce one **Execution Packet** with only the information the executor needs.

## Required packet structure

### 1. ROLE

Who the executor is for this task.

### 2. TARGET

The substantive useful outcome in one compact statement.

### 3. CURRENT AUTHORITY / STATE

Repository/project/environment and the exact current sources that govern the work.

### 4. SCOPE

In scope, materially enabling work, governing constraints, explicit non-goals.

### 5. AUTHORITY

What the executor may and may not mutate or externalize. Mark provisional authority assumptions explicitly if the A14 module is not yet canonical.

### 6. GROUNDING REQUIREMENTS

Which material questions require current external verification and which source types have priority.

### 7. REUSE REQUIREMENT

Existing project assets and external battle-proven solutions that must be checked before custom construction. Define what evidence would authorize custom work.

### 8. EXECUTION METHOD

The smallest sufficient plan/decomposition. Include dependencies, ordering, delegation, and checkpoints only where needed.

### 9. CONTEXT / REFERENCES TO LOAD

Only the files, modules, Skills, standards, or sources needed for the active task.

### 10. MUTATION METHOD

For repository work, define how changes are handed off/applied. If the worker is an online subscription model without safe localized editing of existing files, require **Aider `editor-diff` / SEARCH-REPLACE patch handoff**.

### 11. VALIDATION

Define observable evidence that the substantive target was achieved. Mechanical tests/checks are evidence, not substitutes for outcome validation.

### 12. STOP / ESCALATION CONDITIONS

State when the worker must stop rather than infer a consequential decision.

### 13. FINAL REPORT

Require concise reporting of:

- work completed;
- actual result;
- evidence/verification;
- files/artifacts changed;
- unresolved uncertainty;
- deviations from the plan and why;
- blockers or human decisions still required.

---

# 11. Worker-prompt quality gate

Before sending the packet to the executor, the orchestrator must check:

- **Target:** Does the prompt optimize the useful outcome rather than an artifact/checkmark?
- **Grounding:** Are real-world assumptions verified rather than invented?
- **Reuse:** Does it require proven reuse before custom capability where material?
- **Scope:** Does it allow necessary supporting work without adjacent drift?
- **Authority:** Does it distinguish relevance from permission?
- **Current truth:** Are instructions based on live authoritative state?
- **Tool realism:** Does the worker actually possess the capabilities the prompt assumes?
- **Workflow:** Is process complexity proportionate?
- **Context:** Is only relevant deeper material loaded?
- **Realization:** Are dependencies/interfaces preserved for multilevel work?
- **Mutation:** Is existing-file editing handled safely for the actual environment?
- **Evidence:** Are claims and completion grounded in observable evidence?
- **Recovery:** Are failures handled narrowly rather than by uncontrolled redesign?
- **Stop:** Does the worker know what it must not decide autonomously?

If the packet fails one of these checks materially, fix the packet before execution.

---

# 12. Human launcher — use this to instruct an orchestrator AI

The human can provide this file together with a specific task and use the following compact launcher:

```text
Use `apex-meta/handoff/universal-ai-instruction-system/13-HUMAN-AI-COMPLEX-TASK-EXECUTION.md` as the operational orchestration guide.

Your role is the orchestration/instruction AI, not automatically the executor.

Given my task below:

1. establish the live current state and governing sources;
2. identify the substantive target, scope, constraints, authority, and non-goals;
3. externally ground material real-world assumptions instead of relying on model reasoning alone;
4. check project-local and battle-proven external reuse before authorizing custom construction;
5. verify the actual tool capabilities of the intended executor;
6. choose a complexity-proportionate workflow;
7. load only relevant deeper Universal AI Instruction System modules/references;
8. produce one self-contained Execution Packet for the worker AI using the structure in the guide;
9. preserve explicit human decision gates for consequential unresolved choices;
10. do not execute the underlying task unless I explicitly ask you to also be the executor.

TASK:
[INSERT THE SPECIFIC COMPLEX TASK]
```

---

# 13. If the orchestrator is also the executor

Sometimes one AI can safely perform both roles.

In that case it must still conceptually separate:

```text
UNDERSTAND / GROUND / DESIGN INSTRUCTIONS
                ↓
CHECK TARGET + SCOPE + AUTHORITY
                ↓
EXECUTE
                ↓
VERIFY + VALIDATE
```

Do not let execution begin while material target, scope, authority, external-grounding, or tool-capability questions remain unresolved.

Do not create a second agent merely for ceremony when one competent agent can execute safely and verifiably.

---

# 14. Final system-coverage requirement

This guide is operational, not proof that the Universal AI Instruction System is complete.

Before live universal propagation, `10-UNIVERSAL-SHORT-RULE-COVERAGE-TODO.md` must still be resolved so every high-value control is:

- `COVERED`;
- `MERGED`;
- or `REJECTED WITH EVIDENCE`.

Particular unresolved/pending areas currently include:

- formal A13 completion if still queued;
- A14 authority ownership;
- C04 repository mutation ownership;
- retry/replay/idempotency ownership;
- final cross-agent evaluation;
- final compact root budget and overlap review.

This file may be used now as an orchestration companion, but unfinished candidates must remain labeled as such until the live README says otherwise.

---

# 15. Core invariant

For complex work, preserve this order:

```text
UNDERSTAND THE REAL TARGET
        ↓
ESTABLISH CURRENT TRUTH
        ↓
BOUND SCOPE + AUTHORITY
        ↓
VERIFY EXTERNAL REALITY
        ↓
REUSE WHAT IS PROVEN
        ↓
PLAN ONLY AS MUCH AS COMPLEXITY REQUIRES
        ↓
LOAD ONLY RELEVANT CONTEXT
        ↓
REALIZE TOP-DOWN
        ↓
EXECUTE THROUGH ACTUAL AVAILABLE TOOLS
        ↓
VERIFY BOTTOM-UP
        ↓
VALIDATE THE SUBSTANTIVE OUTCOME
        ↓
REPORT MATERIAL RESULT / UNCERTAINTY / DECISIONS
```

The process is successful when it improves the probability of the **actual requested outcome** while reducing hallucinated architecture, unnecessary custom invention, hidden scope expansion, unsafe side effects, context bloat, and superficial checkmark completion.
