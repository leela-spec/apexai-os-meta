# R06 — Hermes Continuous Learning Research

Status: **RESEARCH REQUIRED / PRE-INSTALL**  
Priority: **P0 — blocks learning/Curator configuration**  
Depends on: R04 knowledge lifecycle, R05 specialist priming  
Decision owner: Human CEO

## Decision question

How can Master of Arts use **Hermes' existing continuous-learning, memory, skill-creation and Curator mechanisms** so that useful experience becomes reusable across projects without creating uncontrolled drift, duplicated factual knowledge, or silent mutation of approved upstream skills?

Do not invent a cross-runtime memory synchronization system.

## Primary official sources

- Hermes Memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes Curator: https://hermes-agent.nousresearch.com/docs/user-guide/features/curator
- Hermes work-with-skills guide: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills
- Hermes self-improvement/background-review documentation if separately documented in current official sources
- Hermes Kanban for durable task/review state

## Current upstream behavior to verify

Current Hermes documentation describes:

- profile `MEMORY.md` / `USER.md` persistent memory;
- skills as procedural knowledge loaded on demand;
- agent-created skills written into Hermes skill storage;
- background/self-improvement creation paths;
- Curator usage telemetry and lifecycle states;
- optional LLM consolidation;
- backups;
- append-only mutation ledger;
- rollback;
- archive/purge controls;
- project-local skills excluded from Curator maintenance;
- hub-installed skills protected from Curator mutation;
- external writable skills potentially mutable by skill-management operations.

These claims must be rechecked against current docs before using them.

## Research tasks

### 1. Map every learning destination

Create:

| Learning type | Exact Hermes/project storage | Created by | Auto/manual | Curator manages? | Shared across projects? | Canonical project truth? | Token impact |
|---|---|---|---|---|---|---|---|

At minimum distinguish:

- current conversation/session;
- profile `MEMORY.md`;
- `USER.md`;
- agent-created skill;
- user-directed skill;
- bundled skill;
- hub-installed skill;
- project-local `.agents/skills/`;
- BMAD/MarketingSkills project skills;
- project factual files;
- Kanban comments/attachments/state;
- QMD index.

### 2. What actually creates learning?

Verify the trigger paths for:

- agent offering to save a procedure as a skill;
- foreground user-directed skill creation;
- background self-improvement review;
- Curator prune/archive;
- Curator consolidation;
- user/manual update;
- project knowledge update.

For each identify whether an AI model call occurs and whether cloud/local tokens are consumed.

### 3. Approved upstream skills protection

The target includes BMAD and MarketingSkills. Determine the supported way to keep those approved upstream skill packages from unwanted autonomous edits while still allowing Hermes to learn separately.

Investigate:

- project-local skill behavior;
- hub-installed protections;
- external directory mutability;
- filesystem read-only permissions where officially recommended;
- profile/toolset separation if relevant;
- Curator scope;
- skill provenance/precedence;
- update path for upstream package upgrades.

Do not fork upstream skills merely to freeze them unless no supported update-safe method exists.

### 4. Learning promotion flow

Use this example:

> A workshop marketing launch reveals a repeatable launch sequence that materially improved output quality.

Trace the supported lifecycle:

```text
task experience
 -> candidate reusable procedure
 -> Hermes-supported learning destination
 -> review/evidence
 -> accepted/rejected
 -> available to another project
 -> future use recorded
```

Identify which steps are existing Hermes features and which require ordinary human approval/repo review.

### 5. Factual learning vs procedural learning

Use examples:

- "Awakenings audience prefers X" = project/family fact;
- "For launch tasks, first check positioning context" = procedure;
- "Operator prefers no public S+ content" = organization/operator rule;
- "This task failed because QMD collection was stale" = operational lesson.

For each determine the correct existing destination.

The system fails if everything gets dumped into `MEMORY.md` or automatically converted into skills.

### 6. Curator configuration

Determine the appropriate official configuration for this use case:

- `prune_builtins`;
- consolidation on/off;
- backup settings;
- archive/purge behavior;
- pinning/adoption behavior where supported;
- audit ledger review;
- rollback workflow;
- cadence/cost of LLM consolidation;
- whether Curator should run automatically or on demand initially.

The recommendation must protect reliability while preserving actual learning value.

### 7. Token/cost impact

Quantify or estimate from official behavior:

- memory injection every session;
- skill index size;
- full skill loading;
- background review model calls;
- Curator deterministic pass;
- Curator LLM consolidation calls;
- duplicate/near-duplicate skill pollution risk.

### 8. Cross-project learning simulation

Simulate:

1. Project A generates useful procedure.
2. Procedure is accepted through the supported mechanism.
3. Project B begins later with the same specialist.
4. Hermes discovers/uses the procedure.
5. Project A factual context does not leak into Project B unless intentionally shared.

Show exact files/state/tool calls.

### 9. Failure/rollback simulation

Simulate:

- bad learned skill;
- duplicate learned skill;
- Curator archives something still needed;
- agent patches wrong skill;
- upstream BMAD/MarketingSkills update arrives;
- learned skill conflicts with upstream package.

Show supported audit/restore/rollback path.

## Required output

1. learning-destination matrix;
2. exact learning trigger map;
3. approved upstream-skill protection strategy using existing mechanisms;
4. learning promotion workflow;
5. factual vs procedural examples;
6. Curator configuration recommendation;
7. token/cost analysis;
8. cross-project simulation;
9. rollback simulation;
10. verdict:
   - `HERMES_LEARNING_MODEL_CONFIRMED`
   - `LEARNING_REQUIRES_GOVERNANCE_CONFIGURATION`
   - `LEARNING_DRIFT_UNRESOLVED`
   - `CUSTOM_MEMORY_SYNC_REQUIRED`.

## Failure condition

If useful learning can only be shared by building a new synchronization service between Hermes, the repo, Claude, Codex or other runtimes, report the blocker. Do not build or design that service in this run.
