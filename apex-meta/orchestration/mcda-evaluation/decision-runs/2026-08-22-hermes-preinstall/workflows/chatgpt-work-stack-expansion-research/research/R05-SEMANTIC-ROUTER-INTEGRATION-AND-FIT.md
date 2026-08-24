# R05 — Semantic Router Integration and Fit

Status: **RESEARCH REQUIRED**  
Depends on: R01  
Candidate identity: `aurelio-labs/semantic-router`

## Decision question

Can current Semantic Router provide an established, evidence-backed semantic decision/routing layer that materially improves the Master of Arts Hermes pipeline, and is there a supported integration path that does not require us to invent a custom router subsystem?

This candidate is not assumed to be an orchestration system. Evaluate it as a module.

## Primary source families

- https://github.com/aurelio-labs/semantic-router
- current docs/source/releases/tests/examples
- current issues/PRs for dependency/security/operational limits
- Hermes docs/source for whichever insertion point is proposed

## Research tasks

### 1. Establish current architecture

Verify current implementation of:

- Route definitions/utterances;
- encoders/embeddings;
- indexes;
- semantic similarity/route selection;
- static vs dynamic/hybrid routing if current;
- local vs remote encoders;
- persistence/index options;
- LLM/provider requirements;
- thresholds/fallbacks/evaluation/calibration;
- async/performance behavior where documented.

Document current version, Python support, license and release activity.

### 2. Identify actual MoA routing problems

Using R00, identify only routing functions that are not already adequately covered. Test separately:

- CEO intent -> workflow selection;
- task -> specialist profile selection;
- task -> skill selection;
- query -> QMD collection/project scope;
- task -> model/provider selection;
- public/private sensitivity routing;
- content/workshop/business domain classification.

For each say whether baseline already has a native mechanism and whether Semantic Router could replace it rather than merely duplicate it.

### 3. Integration proof

For every proposed insertion point, search for current **upstream-supported** integration evidence.

Possible outcomes:

- Hermes directly supports Semantic Router;
- Semantic Router provides a Hermes-compatible plugin/protocol integration;
- another already selected component officially consumes it;
- only a Python library call/custom wrapper could connect them;
- no viable integration.

Do not promote “it is a Python library” into `DOCUMENTED_CONFIGURATION`. If we must write routing code or a service, classify `CUSTOM_REQUIRED`.

### 4. Compare against existing routing

Compare with evidence:

- Hermes profile/Kanban routing;
- Hermes skill semantic selection;
- Agency Agents router if R03 proves it;
- BMAD workflow activation;
- MarketingSkills semantic activation;
- QMD retrieval/query routing;
- provider/model routing available in Hermes;
- AnythingLLM model/agent routing if R06 proves it.

Identify unique measurable benefit rather than a conceptual extra layer.

### 5. Determinism, quality and failure modes

Verify:

- whether routing result is deterministic for fixed embeddings/index/version;
- local model/inference needs;
- threshold behavior and false-route risks;
- fallback/no-route behavior;
- route updates/re-encoding;
- evaluation tools/metrics;
- debugging/explainability;
- persistence/rebuild behavior.

### 6. User-story simulations

Simulate only if an upstream-supported insertion point exists:

1. ambiguous CEO request routed to correct domain/workflow;
2. marketing task routed to specialist without loading unrelated specialists;
3. sensitive Business query prevented from crossing into unrelated scope;
4. new domain added and route index updated;
5. route uncertain -> safe fallback/explicit handling;
6. failure/restart without losing canonical project state.

If no supported insertion point exists, state that and do not invent the simulation plumbing.

### 7. Cost/token/privacy/security

Verify:

- local vs remote encoder options;
- model/API dependencies;
- index persistence;
- data egress;
- memory/CPU footprint where documented;
- extra latency;
- token savings claim evidence, if any;
- Windows/WSL;
- dependency/security advisories/current fixes;
- maintenance burden of route definitions.

### 8. Decision

Choose among:

- `ADD_NOW_AS_VERIFIED_ROUTING_MODULE`
- `PILOT_IF_MEASURABLE_ROUTING_PROBLEM`
- `DEFER_NO_CURRENT_NEED`
- `REJECT_DUPLICATE`
- `REJECT_CUSTOM_INTEGRATION_REQUIRED`

A theoretically elegant router is not enough.

## Required output

1. current Semantic Router architecture;
2. candidate insertion-point matrix;
3. exact integration evidence for every viable insertion point;
4. baseline routing overlap matrix;
5. deterministic/AI/index/failure behavior;
6. user-story simulations only for proven connections;
7. cost/token/privacy/security/platform analysis;
8. current maturity/issue evidence;
9. recommendation and switching condition defining when routing complexity justifies the component;
10. source registry.

## Pass standard

Pass only when the report determines whether there is a *real, upstream-supported and useful* insertion point. If the answer is “we could write a wrapper”, the current decision is `CUSTOM_REQUIRED`, not an implementation plan.
