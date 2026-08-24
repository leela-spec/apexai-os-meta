# R07 — Evidence Matrix V1 + Preliminary Recommendation

Status: **RESEARCH REQUIRED**  
Depends on: R02, R03, R04, R05, R06

## Decision question

After the individual research, what does the first complete evidence-backed module matrix say about retaining, adding, piloting, replacing, deferring or rejecting CrewAI, Agency Agents, Superpowers, Semantic Router and AnythingLLM relative to the current Hermes stack?

This is V1. It must be adversarially audited by R08 before it becomes the final recommendation.

## Inputs

Use only:

- R00 baseline;
- R01 landscape;
- accepted R02-R06 individual results;
- current sources re-opened as necessary;
- `MATRIX-SCHEMA.yaml`;
- methodology sources in `SOURCE-REGISTRY.md`.

Do not silently rely on producing-chat memory.

## Research tasks

### 1. Build the full capability matrix

Use every row/column in `MATRIX-SCHEMA.yaml`.

Every substantive cell must include:

- role;
- evidence status;
- evidence IDs;
- exact mechanism;
- integration class;
- local/remote/API/provider consequences;
- state/data-egress/token effect;
- maturity evidence;
- limitations/confidence.

No evidence = `OPEN/UNVERIFIED`.

### 2. Apply hard filters

For each proposed use of a candidate, apply F01-F07 from the schema.

A candidate may pass for one module and fail for another. Do not hard-filter the whole project merely because one integration is unsuitable.

### 3. Build substitution/supplement map

For each baseline module state exactly:

`KEEP_BASELINE | REPLACE_WITH_X | SUPPLEMENT_WITH_X | PILOT_X | NO_CHANGE`.

If an addition is recommended, identify what new value exists and what duplication it introduces.

### 4. User-story comparative matrix

Compare candidates only on user stories they plausibly serve:

- CEO intent routing;
- research-to-artifact;
- shared marketing specialist across projects;
- retrieval/project isolation;
- maker/reviewer;
- recovery;
- learning;
- local/private execution;
- web-AI durable artifact portability.

Do not score Semantic Router as a full orchestration platform or Agency Agents as a knowledge database.

### 5. MCDA after hard filters

For viable complete or module decisions:

1. define the observed best-to-worst performance range on each dimension;
2. assign swing weights based on the value of moving from worst to best;
3. document the rationale;
4. calculate the preliminary value model;
5. run sensitivity scenarios from `MATRIX-SCHEMA.yaml`;
6. identify switching values where another decision wins.

Do not use a preselected arbitrary 1–5 weighted table.

### 6. Complexity/duplication budget

For every proposed addition quantify qualitatively and, where evidence permits, numerically:

- new install/runtime;
- new config/state DB/index;
- extra model calls/token context;
- extra updater/security surface;
- duplicate responsibilities;
- new failure/recovery modes;
- operator concepts to understand.

An addition must earn this cost with verified value.

### 7. Preliminary recommendation

Return a module-level action for every candidate:

`KEEP | ADD_NOW | PILOT | REPLACE | DEFER | REJECT`.

This remains provisional pending R08.

## Required output

1. complete evidence-backed matrix;
2. hard-filter results;
3. module substitution/supplement map;
4. comparative user-story matrix;
5. MCDA swing-weight model;
6. sensitivity/switching analysis;
7. complexity/duplication ledger;
8. preliminary action per candidate and per affected baseline module;
9. explicit evidence gaps that could change the preliminary result;
10. source registry;
11. verdict: `V1_READY_FOR_ADVERSARIAL_AUDIT` or `MATRIX_BLOCKED`.

## Pass standard

Pass only if a reviewer can trace every consequential recommendation to specific R00-R06 evidence and current sources. A polished but uncited matrix fails.
