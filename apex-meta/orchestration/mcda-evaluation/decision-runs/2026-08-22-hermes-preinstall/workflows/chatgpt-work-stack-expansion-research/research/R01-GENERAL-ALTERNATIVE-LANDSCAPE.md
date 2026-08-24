# R01 — General Alternative Landscape

Status: **RESEARCH REQUIRED**  
Depends on: R00

## Decision question

Against the verified current-pipeline baseline, what are CrewAI, Agency Agents, Superpowers, Semantic Router and AnythingLLM **actually capable of adding, replacing or duplicating**, based on current web/upstream evidence rather than theoretical composability?

This is the first broad comparison. It frames the individual research but must not make the final recommendation.

## Candidates

- CrewAI — `crewAIInc/crewAI`
- Agency Agents — `msitarzewski/agency-agents`
- Superpowers — `obra/superpowers`
- Semantic Router — `aurelio-labs/semantic-router`
- AnythingLLM — `Mintplex-Labs/anything-llm`

## Research tasks

### 1. Candidate role classification

For each determine from current official sources whether it is primarily:

`WHOLE_STACK_REPLACEMENT | MODULE_REPLACEMENT | SUPPLEMENT | SPECIALIST_PACKAGE | WORKFLOW_METHOD | ROUTING_COMPONENT | KNOWLEDGE_COMPONENT | DUPLICATE | NO_FIT`.

Do not force all candidates into the same category.

### 2. Current capability map

Use the R00 module rows and `MATRIX-SCHEMA.yaml` to create an evidence-backed preliminary matrix. Every substantive cell must cite current evidence or be `OPEN/UNVERIFIED`.

### 3. Established-value evidence

For each candidate distinguish:

- feature exists;
- integration path exists;
- maintained/tested currently;
- adoption evidence;
- first-party or independent operational evidence;
- current issue/PR evidence that limits the claim;
- relevance to non-software MoA work.

Do not translate repository popularity into “battle-tested”.

### 4. Verified integration surface with Hermes baseline

Search specifically for current upstream evidence of:

- Hermes-native plugin/package;
- Agent Skills path;
- MCP path where roles on both sides match;
- A2A path where roles on both sides match;
- CLI/SDK/API path;
- no integration found.

Classify every edge using the workflow integration classes. Generic protocol support is not sufficient proof.

### 5. Module substitution/supplement hypotheses

Create only evidence-supported hypotheses such as:

- CrewAI vs Hermes runtime/Kanban/flows;
- Agency Agents vs current specialist profile/BMAD roster;
- Superpowers vs BMAD/review/workflow-method layer;
- Semantic Router vs existing skill/profile routing;
- AnythingLLM vs QMD/project-KB/retrieval/agent-flow layers.

Each hypothesis must identify what becomes redundant if adopted.

### 6. Cross-cutting constraints

Compare current evidence for:

- local/cloud execution;
- ChatGPT/Codex subscription compatibility vs API billing;
- Windows/WSL;
- data egress;
- persistent state;
- token/context loading;
- installation/update burden;
- security model;
- licensing/commercial use.

### 7. Research priority

Identify which unknowns in R02-R06 are most likely to change the eventual decision. Do not recommend further broad research where a precise source/code/issue check can answer the question.

## Required output

1. plain-language candidate taxonomy;
2. preliminary evidence-backed capability matrix;
3. verified integration-surface table;
4. established-value/maturity table;
5. duplication and substitution map;
6. major constraints/cost/privacy table;
7. decision-changing unknowns for R02-R06;
8. no final winner; only `INDIVIDUAL_RESEARCH_READY` or `LANDSCAPE_BLOCKED`;
9. source registry.

## Pass standard

Pass when the five candidates have evidence-based roles and integration hypotheses that the detailed tracks can falsify. Fail if the landscape relies on model-designed connections or incomparable whole-stack scoring.
