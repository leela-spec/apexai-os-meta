# R00 — Verified Current Pipeline Baseline

Status: **RESEARCH REQUIRED**  
Priority: **P0 — defines the control architecture**

## Decision question

What capabilities and value does the current Hermes-centered Master of Arts pipeline **actually have evidence for today**, after the completed R01-R07 research, and which parts remain configuration, supported inference, or untested pilot behavior?

Do not compare alternatives yet. This file creates the fair control against which CrewAI, Agency Agents, Superpowers, Semantic Router and AnythingLLM will later be measured.

## Inputs

Read:

- `ADR-002-full-functional-hermes-target.md`;
- completed ChatGPT Work state;
- all completed R01-R07 result files;
- current MasterOfArts repo where the results cite repo structure;
- current official sources behind all decision-changing baseline claims.

Do not simply summarize the prior reports. Re-open load-bearing upstream sources and preserve their evidence status.

## Research tasks

### 1. Reconstruct the real pipeline

Produce a flow showing only mechanisms supported by evidence:

```text
CEO intent
 -> orchestration/task state
 -> specialist selection/priming
 -> project context
 -> skill/workflow activation
 -> retrieval
 -> model execution
 -> artifact
 -> independent review
 -> durable persistence
 -> learning/reuse
```

For every edge record:

`from | to | exact mechanism | automatic/manual | deterministic/AI/hybrid | persistent state | evidence status | source`.

### 2. Capability inventory

Evaluate separately:

- Hermes runtime/orchestration;
- Kanban/dependencies/review/retry/recovery;
- root/family/micro project context;
- project files as durable truth;
- reusable Hermes profiles;
- BMAD roles/workflows;
- MarketingSkills;
- QMD retrieval;
- memory;
- Curator/learning;
- provider/subscription/local-model path;
- security controls;
- cross-client/web-AI artifact portability.

For each classify:

`PROVEN_NOW | VERIFIED_MECHANISM_NEEDS_CONFIGURATION | SUPPORTED_INFERENCE_REQUIRES_QA | OPEN | CONTRADICTED`.

### 3. Established-value audit

For every component distinguish:

- existence of feature;
- integration with the selected stack;
- operational/recovery semantics;
- evidence that the feature creates value for a real MoA user story;
- remaining QA that has not happened because software is not installed.

A completed research PASS is not the same as an installed production proof. State that distinction precisely.

### 4. Current module ownership

Build one responsibility-owner matrix:

| Responsibility | Current owner | Canonical state | Derived state | Runtime only | Known overlap |
|---|---|---|---|---|---|

The goal is to make later duplication visible. Examples: project facts, task state, semantic retrieval, specialist identity, procedures, memory, review, routing.

### 5. Current costs and constraints

Verify:

- software/license cost;
- API/subscription/local execution paths;
- provider calls/token drivers;
- local model use;
- persistent local databases/indexes;
- data egress;
- Windows/WSL constraints;
- installation/maintenance complexity;
- known upstream contradictions or unsupported assumptions.

### 6. Current user-story baseline

Trace the baseline on:

1. research -> knowledge -> workshop/artifact;
2. one marketing specialist across two project families;
3. maker -> reviewer -> revise -> accept;
4. interruption/recovery;
5. project-scoped retrieval;
6. reusable procedural learning;
7. private/local project execution.

Mark each step as `verified mechanism`, `configuration`, `supported inference`, or `not yet proven in live install`.

### 7. Alternative-entry points

Without yet evaluating candidates, identify the exact modules an alternative could plausibly improve or replace. Do not invent gaps merely to create space for alternatives.

Examples to test rather than assume:

- specialist roster quality;
- semantic routing;
- multi-agent workflow runtime;
- knowledge/RAG UX;
- workflow discipline/review methodology;
- durable state/recovery;
- learning.

## Required output

1. plain-language current pipeline explanation;
2. verified flowchart;
3. capability/evidence-status table;
4. responsibility-owner matrix;
5. proven vs not-yet-live-proven distinction;
6. cost/token/privacy/platform matrix;
7. seven user-story traces;
8. exact candidate insertion/replacement boundaries for later research;
9. source registry;
10. verdict: `BASELINE_READY_FOR_COMPARISON` or `BASELINE_BLOCKED`.

## Pass standard

Pass only when later researchers can compare alternatives against a precise evidence-backed baseline without treating research conclusions as installed production proof and without forgetting capabilities already covered by the current stack.
