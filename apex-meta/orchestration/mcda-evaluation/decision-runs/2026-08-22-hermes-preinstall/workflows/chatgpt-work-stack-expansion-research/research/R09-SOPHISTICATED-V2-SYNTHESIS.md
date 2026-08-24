# R09 — Sophisticated V2 Synthesis and Recommendation

Status: **RESEARCH REQUIRED — FINAL TRACK**  
Depends on: R08

## Decision question

After the verified baseline, broad landscape, five individual candidate studies, evidence matrix, and adversarial audit, what is the strongest **evidence-adjusted Master of Arts target stack** now — and exactly which modules should be kept, added, piloted, replaced, deferred or rejected?

This is a decision report, not an implementation plan. Do not install anything.

## Inputs

Use accepted/corrected:

- R00;
- R01;
- R02 CrewAI;
- R03 Agency Agents;
- R04 Superpowers;
- R05 Semantic Router;
- R06 AnythingLLM;
- R07 evidence matrix after R08 corrections;
- R08 adversarial audit;
- current ADR-002 and existing QA runbook only as current decision context.

Re-open current official sources for any claim that becomes newly decisive during synthesis.

## Research tasks

### 1. Reconstruct the current control stack

Show the evidence-backed baseline before changes.

### 2. Build the recommended V2 stack

For every module, choose exactly one action:

- `KEEP`
- `ADD_NOW`
- `PILOT`
- `REPLACE`
- `DEFER`
- `REJECT`

Possible modules include but are not limited to:

- primary orchestration/runtime;
- durable task/project state;
- macro/meso/micro project context;
- project factual truth/artifacts;
- semantic/project retrieval;
- specialist roster;
- workflow/method skills;
- marketing skills;
- semantic router;
- knowledge/RAG UI/application;
- procedural learning/memory;
- reviewer separation;
- provider/model execution;
- safety controls.

If an added candidate owns no clear responsibility, reject/defer it rather than leave it floating in the architecture.

### 3. Produce before/after flowcharts

Show:

```text
CURRENT VERIFIED BASELINE
```

and

```text
RECOMMENDED V2
```

Every edge in the V2 chart must carry an evidence-backed integration class. No decorative/hypothetical arrows.

### 4. Exact connection matrix

For every retained/additional cross-component edge state:

`from | to | trigger | mechanism/protocol | exact inputs | exact outputs | local/remote | model/API | persistent state owner | retry/recovery owner | data egress | integration class | evidence IDs`.

If any required V2 edge is `CUSTOM_REQUIRED`, make that explicit and explain whether it invalidates the recommendation under the project law.

### 5. Responsibility/duplication audit

Create a final one-owner-per-responsibility table:

| Responsibility | Primary owner | Secondary/derived consumer | Canonical state | Why no duplicate truth |
|---|---|---|---|---|

Explicitly address task state, project truth, retrieval index, specialist identity, workflows/skills, memory/learning, review and routing.

### 6. User-story proof

Trace the V2 recommendation end to end for:

1. CEO intent -> routing -> project/workflow;
2. research -> knowledge -> workshop/artifact;
3. one Marketing specialist across two project families;
4. multi-specialist complex task;
5. maker -> independent reviewer -> revision;
6. interruption/recovery;
7. procedure learned in Project A -> reusable in Project B without fact leakage;
8. private/local task;
9. web subscription AI consuming durable repo artifacts;
10. failure of an optional added component and graceful fallback.

Every step must name the actual component/mechanism.

### 7. MCDA V2

Report:

- hard filters;
- viable alternatives/module decisions;
- swing-weight rationale based on observed performance spread;
- value matrix;
- sensitivity scenarios;
- switching values;
- uncertainty that can still change a decision;
- which uncertainties are *not* worth more research because they cannot change the recommendation.

Do not collapse asymmetric modules into one meaningless total ranking. Use module decisions plus any whole-stack comparison that remains genuinely relevant.

### 8. Established-value verdict

For each candidate state separately:

- verified technical capability;
- verified integration;
- current operational/maturity evidence;
- proven/reported value;
- MoA-specific value still requiring pilot;
- current action.

This section must make it impossible to confuse “technically possible” with “already proven useful”.

### 9. Cost/token/privacy/maintenance V2

Compare baseline vs V2 on:

- number of runtimes/services;
- persistent DB/index/state stores;
- model/API calls;
- subscription vs pay-per-token constraints;
- local model load;
- startup context and on-demand context;
- data egress;
- secrets;
- Windows/WSL;
- update/security surfaces;
- operator complexity;
- recovery/rollback.

If V2 adds complexity, identify the verified value that pays for it.

### 10. Realization handoff

Do not implement. Produce a precise handoff telling the existing `QA-VALIDATION-RUNBOOK-v2.md` process what must change before installation validation.

Classify each V2 recommendation as:

- `READY_FOR_EXISTING_QA`
- `NEEDS_BOUNDED_PREINSTALL_PILOT`
- `NEEDS_ONE_DECISION_CHANGING_RESEARCH_CHECK`
- `DEFERRED`

No custom subsystem design.

## Required output

1. executive recommendation in plain language;
2. candidate action table;
3. current baseline flowchart;
4. recommended V2 flowchart;
5. exact connection matrix;
6. one-owner responsibility/duplication table;
7. ten user-story traces;
8. final MCDA + sensitivity/switching analysis;
9. established-value vs technical-possibility matrix;
10. cost/token/privacy/maintenance delta;
11. unresolved blockers/uncertainties;
12. exact realization/QA handoff;
13. source registry;
14. final decision status: `V2_DECISION_READY | V2_RESEARCH_BLOCKER`.

## Pass standard

Pass only if every recommended component and every integration arrow is evidence-backed, the adversarial R08 corrections are incorporated, and the recommendation improves the required MoA operating system without hidden duplicate state or custom glue.
