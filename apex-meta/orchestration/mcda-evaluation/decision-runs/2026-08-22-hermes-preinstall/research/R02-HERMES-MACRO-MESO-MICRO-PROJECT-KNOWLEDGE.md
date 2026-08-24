# R02 — Hermes Macro/Meso/Micro Project + Knowledge Research

Status: **RESEARCH REQUIRED / PRE-INSTALL**  
Priority: **P0 — blocks project migration and Kanban setup**  
Decision owner: Human CEO

## Decision question

How should the existing MasterOfArts repository be used with **Hermes' already-built project/workspace/context/Kanban mechanisms** so that the same reusable agents can work at:

- **Macro:** Master of Arts organization/portfolio;
- **Meso:** project family/program/domain, e.g. Awakenings, dance, martial arts, Business;
- **Micro:** one concrete execution project, e.g. create/publish/advertise one workshop;

without inventing a new project-management framework or a new knowledge-base system?

## Core requirement

The desired result is a **repeatable upstream-native project pattern**. It must be understandable by Hermes and reusable across heterogeneous projects.

Do not design a custom folder taxonomy merely because it looks organized.

## Primary official sources

- Hermes Context Files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/
- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes Memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- Hermes User Stories / Kanban tutorial if current official docs provide one
- Agent Skills specification only where Hermes explicitly supports it

## Repository inputs

Inspect the current repository directly. Sample at least three materially different areas such as:

- a workshop/movement/method area;
- Business/operations;
- IPOS/Lika/research/content or another structurally different domain.

Do not assume existing old OpenClaw/Apex structures are authoritative.

## Research tasks

### 1. Map the Hermes-native primitives

Explain in plain language what each upstream concept actually owns:

- Git repository root;
- current working directory;
- root `AGENTS.md` / `.hermes.md` behavior;
- nested `AGENTS.md` progressive discovery;
- project-local skills and their Git-root scope;
- Hermes profiles;
- Kanban board;
- Kanban task;
- parent/child/dependency link;
- task workspace / board `default_workdir`;
- comments/attachments/review state;
- runtime memory.

For each state whether it is suitable for macro, meso, micro, or none.

### 2. Inspect current project reality

For each sampled domain record:

```text
PATH:
WHAT_THIS_DOMAIN_IS:
CURRENT_MAIN_FILES:
CURRENT_RAW_SOURCES:
CURRENT_FINAL_OUTPUTS:
CURRENT_PROJECT_STATUS/2DOS:
CURRENT_DECISIONS:
CURRENT_DUPLICATION/STALE_MATERIAL:
WHAT_AN_AGENT_NEEDS_TO UNDERSTAND BEFORE WORKING:
```

Do not reorganize yet.

### 3. Test the nested context mechanism

Use Hermes' documented context behavior to answer:

- If Hermes starts at repo root, what does it load?
- If Hermes starts inside a meso project family, which context chain loads?
- If Hermes starts inside one micro project, which context chain loads?
- What happens when it navigates into another subdirectory?
- Which files are injected every turn vs discovered only when relevant?
- What are the documented size/truncation limits?
- Does this mechanism actually support the desired hierarchy without another KB runtime?

Use a realistic paper path based on actual repo structure, not only a toy example.

### 4. Determine the repeating project pattern from upstream behavior

The research may propose repeated files/folders only when there is a direct consumer or operational owner.

For every proposed repeated element provide:

| Element | Upstream consumer | Why needed | Auto-loaded? | On-demand? | Durable state owner | Token effect | Existing standard/mechanism |
|---|---|---|---|---|---|---|---|

Candidate elements may include only if justified by upstream behavior:

- `AGENTS.md` / `.hermes.md`;
- project brief/status artifact;
- decisions/current-state artifact;
- source/reference directories already present;
- outputs/artifacts;
- `.agents/skills/` at the repo level where upstream packages install;
- QMD collection boundaries later validated by R03.

Do not create mandatory `knowledge/`, `canon/`, `memory/`, `meta/`, or similar folders unless an existing selected system consumes them and the user story requires them.

### 5. Project-management mapping

Find the most direct Hermes-native mapping for:

#### Macro

- portfolio priorities;
- cross-project dependencies;
- CEO decisions/exceptions;
- weekly review;
- current active projects.

#### Meso

- project-family goal;
- shared family knowledge;
- family backlog/roadmap;
- repeated outputs;
- dependencies across micro projects.

#### Micro

- concrete deliverable;
- task sequence;
- acceptance criteria;
- assigned specialist;
- files/workdir;
- review/change loop;
- completion/recovery.

Do not assume board-per-project, task-per-project, or any other mapping until current official Hermes semantics support it.

### 6. Shared-specialist test

Use one specialist identity, e.g. Marketing Executive.

Simulate:

```text
same specialist/profile
 -> project family A
 -> micro project A1
 -> work

same specialist/profile
 -> project family B
 -> micro project B1
 -> work
```

Show exactly what changes between the two runs:

- workdir;
- context chain;
- current Kanban task;
- retrieved files;
- project marketing context if relevant;

and what remains shared:

- specialist definition;
- upstream skills;
- organization-wide policy/context where appropriate.

### 7. Token-efficiency test

For each hierarchy level identify:

- information injected at startup;
- information injected on navigation;
- information merely indexed/searchable;
- files never read unless requested;
- risk of large `AGENTS.md` prompt bloat;
- official settings/behavior that manage that risk.

### 8. Online subscription AI interoperability

Without assuming equivalence to Hermes, determine which repo structures remain understandable to a web AI with GitHub access:

- can it read root/family/micro context files if explicitly directed?
- can it access the same factual project files?
- can it use repo-local skill text as instructions even if native skill discovery differs?

Do not require the project structure to be Hermes-exclusive unless an upstream Hermes feature creates material value.

## Required simulations

1. Create one concrete Awakenings-style workshop project from existing family knowledge.
2. Run a different workshop/project from the same family.
3. Run a different domain using the same shared Research or Marketing specialist.
4. Perform weekly portfolio review across at least three meso families.
5. Restart the agent and show which information/state survives and how it is rediscovered.

## Required output

1. current-repo diagnosis;
2. Hermes primitive map;
3. macro/meso/micro mapping table;
4. repeating project pattern derived from upstream mechanisms;
5. exact files/state owners and consumers;
6. shared-specialist two-project simulation;
7. token-loading matrix;
8. web-AI compatibility notes;
9. unresolved gaps;
10. verdict:
   - `HERMES_NATIVE_PROJECT_MODEL_CONFIRMED`
   - `HERMES_NATIVE_MODEL_NEEDS_DOCUMENTED_CONFIGURATION`
   - `CUSTOM_PROJECT_FRAMEWORK_REQUIRED`.

## Failure condition

If the only way to make macro/meso/micro work is to invent a new hierarchy, task database, custom project router, or manually maintained duplicate state, report the failure. Do not design the replacement inside this research run.
