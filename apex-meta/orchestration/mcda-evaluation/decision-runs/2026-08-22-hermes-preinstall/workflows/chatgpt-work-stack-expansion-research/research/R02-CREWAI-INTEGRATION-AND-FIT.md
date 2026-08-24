# R02 — CrewAI Integration and Fit

Status: **RESEARCH REQUIRED**  
Depends on: R01  
Candidate identity: `crewAIInc/crewAI`

## Decision question

Would current CrewAI provide verified additional value to the Master of Arts pipeline as a replacement or supplement to Hermes, and if so, **through what exact upstream-supported integration and operating process**?

Do not assume that an agent framework is useful merely because it can run multiple agents.

## Primary source families

- https://github.com/crewAIInc/crewAI
- https://docs.crewai.com
- current releases/tests/examples/source
- current CrewAI issues/PRs where needed for operational limitations
- Hermes official A2A documentation if an A2A integration is claimed
- A2A standard only to explain protocol semantics, never as sole proof of product integration

## Research tasks

### 1. What CrewAI actually is today

Verify current implementation of:

- Crews;
- Flows;
- task/process/delegation model;
- persistence/state/checkpoint/recovery;
- memory and knowledge;
- guardrails/review/human input;
- tools/MCP;
- A2A support and exact client/server roles;
- local models/provider/API requirements;
- observability/deployment/enterprise pieces;
- Agent Skills or coding-agent skill support if current.

Record exact package/release/version evidence.

### 2. Replacement analysis

Compare CrewAI directly against current owners of:

- Hermes orchestration/runtime;
- Hermes Kanban durable state/review/retry;
- Hermes profiles/shared specialists;
- root/family/micro project context;
- BMAD workflow/method layer;
- QMD retrieval;
- Hermes memory/Curator.

For each: `BETTER_VERIFIED | EQUIVALENT | WEAKER | DIFFERENT_ROLE | OPEN` with evidence.

Do not count a feature as equivalent unless durability/recovery/review semantics actually match the MoA requirement.

### 3. Supplement/integration analysis

Investigate exact current integration patterns:

A. CrewAI fully replaces Hermes for a workflow.
B. Hermes delegates a bounded workflow/task to CrewAI.
C. CrewAI delegates to Hermes.
D. Both interoperate through A2A or another current official mechanism.
E. No established integration; custom Python/API wrapper would be required.

For every viable pattern record:

`trigger -> transport -> receiver -> context passed -> task state owner -> model execution -> result return -> review -> failure/retry -> persistence`.

If A2A is used, verify both CrewAI and Hermes current source/docs implement the required roles and distinguish protocol interoperability from complete MoA workflow integration.

### 4. Project/knowledge integration

Prove how CrewAI would receive:

- MasterOfArts organization context;
- family/project context;
- micro-project context;
- QMD or equivalent retrieval;
- repo file truth;
- shared specialist methods.

Does this reuse existing files/configuration, or create a second knowledge/state system? Identify exact duplication.

### 5. User-story simulations

Trace with exact product mechanisms:

1. CEO asks for a research-to-workshop workflow.
2. One Marketing specialist works on two different project families.
3. Maker/reviewer/request-changes cycle.
4. Worker/model interruption and recovery.
5. CrewAI/Hermes handoff if supplement architecture is viable.
6. Private/local task using local models where possible.

### 6. Cost/token/privacy

Verify:

- open-source/commercial license;
- install/runtime dependencies;
- API-provider defaults;
- local-model support;
- whether ChatGPT/Codex subscription OAuth can be used directly or not;
- recurring prompt/context overhead;
- Crew/Flow state persistence;
- telemetry/external services;
- data egress;
- Windows/WSL;
- paid enterprise/cloud dependencies for any claimed feature.

### 7. Established-value test

Find current evidence beyond marketing claims:

- release cadence;
- tests/CI;
- issue quality/resolution;
- first-party production/customer examples with specific mechanisms/results;
- package/repo adoption as adoption only;
- current limitations relevant to flows, recovery, A2A or knowledge.

### 8. Decision

Evaluate these outcomes separately:

- `CREWAI_REPLACE_HERMES`
- `CREWAI_SUPPLEMENT_HERMES`
- `CREWAI_PILOT_BOUNDED_WORKFLOW`
- `CREWAI_DEFER`
- `CREWAI_REJECT_FOR_CURRENT_STACK`

Do not choose based on feature count. Identify exactly what existing component becomes unnecessary or what verified new value is gained.

## Required output

1. current CrewAI architecture in plain language;
2. version/license/maturity evidence;
3. baseline replacement matrix;
4. exact integration patterns and evidence classes;
5. detailed viable flowchart(s);
6. project/knowledge/state ownership map;
7. six user-story simulations;
8. cost/token/privacy/platform table;
9. operational evidence and current limitations;
10. duplication/maintenance analysis;
11. decision and switching conditions;
12. source registry.

## Pass standard

Pass only when the result can say whether CrewAI adds/replaces real value without relying on “we could write a Python integration”. Custom glue is a negative finding, not an implementation task.
