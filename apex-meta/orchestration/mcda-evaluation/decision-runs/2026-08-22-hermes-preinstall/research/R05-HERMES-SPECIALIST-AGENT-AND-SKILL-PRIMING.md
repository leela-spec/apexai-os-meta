# R05 — Hermes Specialist Agent + Skill Priming Research

Status: **RESEARCH REQUIRED / PRE-INSTALL**  
Priority: **P0 — blocks agent/profile setup**  
Depends on: R02 project model  
Decision owner: Human CEO

## Decision question

How should reusable Master of Arts specialist roles be represented and primed using **existing Hermes profile/context/skill mechanisms** so that the same specialist can work across many projects with the correct organization, project-family and micro-project context?

The goal is not to design dozens of bespoke agents. The goal is to use Hermes' existing role/profile/skill architecture correctly.

## Target behavior

```text
SHARED SPECIALIST ROLE
   + shared role/profile instructions
   + shared upstream skills
   + organization-wide rules/context
   + current project-family context
   + current micro-project task/workdir
   + on-demand project knowledge via files/QMD
```

The role should remain reusable while the project context changes.

## Primary official sources

- Hermes Context Files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes Kanban/profiles: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes SOUL/personality/profile documentation where current official docs define role identity
- Hermes Memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/
- BMAD current installer/agent/skill packaging: https://github.com/bmad-code-org/BMAD-METHOD
- Agent Skills specification only where current Hermes officially supports it

## Research tasks

### 1. Inventory Hermes identity/config layers

Explain exactly what each is for and when it is loaded:

- profile;
- SOUL.md;
- USER.md;
- MEMORY.md;
- AGENTS.md / `.hermes.md`;
- project-local skill;
- local/global skill;
- BMAD persona/agent skill;
- Kanban assignee/profile;
- current task body/comments/attachments/workdir.

Create:

| Layer | Purpose | Scope | Automatically loaded? | Mutable by Hermes? | Shared across projects? | Should contain project facts? |
|---|---|---|---|---|---|---|

### 2. Define a specialist using only existing mechanisms

Use at least these candidate roles:

- Marketing Executive;
- Research Strategist/Researcher;
- Workshop Designer;
- Independent Reviewer.

For each identify which upstream artifact should hold:

- role mission;
- activation conditions;
- preferred skills;
- allowed tools;
- expected output contract;
- review/escalation behavior;
- tone/personality only where relevant;
- project context references.

Do not create custom fields unless an upstream profile/skill format consumes them.

### 3. Skill activation

Verify how Hermes:

- indexes skills;
- selects/loads skills on demand;
- exposes slash commands;
- handles project-local vs global/local vs external skills;
- handles project trust;
- resolves precedence;
- exposes skill settings/config;
- records skill usage.

Explain token implications of the skill index vs full skill body.

### 4. Project priming

Simulate the same Marketing specialist on two different workdirs.

For each show exactly:

```text
PROFILE/ROLE LOADED:
ROOT CONTEXT LOADED:
FAMILY CONTEXT LOADED:
MICRO CONTEXT LOADED:
KANBAN TASK STATE:
SKILL INDEX:
FULL SKILLS ACTIVATED:
QMD COLLECTION/SCOPE:
PROJECT FILES RETRIEVED:
MODEL CALLS:
OUTPUT:
```

Pass only if project-specific information changes without duplicating the specialist definition.

### 5. Organization-wide vs project-specific knowledge

Determine the verified upstream place for:

- Master of Arts-wide public/private policy;
- general brand/business identity;
- specialist role behavior;
- project-family facts;
- micro-project facts;
- reusable procedures.

The research must prevent two failure modes:

1. stuffing all organization/project knowledge into every specialist prompt;
2. copying the same specialist into every project just to give it local context.

### 6. Reviewer separation

Verify how Hermes profiles/Kanban can assign a distinct reviewer to inspect an artifact/evidence without inheriting hidden maker chat state.

Show:

- exact durable inputs reviewer receives;
- task/review state;
- request-changes loop;
- whether a separate profile/process is required and is upstream-native;
- token/context cost.

### 7. BMAD roles vs Hermes profiles

BMAD may package personas/agents as skills. Determine how those relate to Hermes profiles:

- Does a BMAD agent skill replace the need for a Hermes profile?
- Can a Hermes profile load a BMAD persona/workflow skill?
- Which layer owns persistent worker identity vs temporary task methodology?
- Could duplicate persona instructions cause conflicting context?

Do not merge them by intuition. Verify from actual upstream behavior and examples.

### 8. Cross-client portability

For each shared role/skill artifact classify whether it can be consumed by:

- Hermes;
- Codex CLI;
- Claude Code;
- web ChatGPT/Claude with repo access.

Distinguish:

- native skill activation;
- explicit file reading/following;
- runtime-specific profile configuration;
- inaccessible local state.

### 9. Token-efficiency simulation

Estimate what enters the prompt for a real task:

- role/profile material;
- project context chain;
- skill index;
- full activated skills;
- QMD snippets;
- task comments/state;
- model output.

Identify upstream progressive-disclosure behavior rather than proposing custom prompt compression.

## Required user stories

### US-1 — Marketing Executive / workshop A

Launch one workshop using MarketingSkills and project-local context.

### US-2 — Same Marketing Executive / different project B

Work on a materially different offer without duplicating the role definition.

### US-3 — Researcher -> reviewer handoff

Researcher produces evidence/artifact; independent reviewer receives durable inputs and requests changes.

### US-4 — Workshop Designer uses accepted research

Workshop specialist uses project knowledge + skill package without receiving irrelevant marketing or unrelated project context.

## Required output

1. Hermes identity/priming layer map;
2. recommended specialist representation using only upstream mechanisms;
3. role vs skill vs project-context ownership matrix;
4. two-project shared-specialist simulation;
5. reviewer separation simulation;
6. BMAD-persona vs Hermes-profile result;
7. cross-client portability matrix;
8. token-loading matrix;
9. required configuration only;
10. verdict:
   - `SHARED_SPECIALIST_MODEL_CONFIRMED`
   - `PROFILE_SKILL_CONFLICT`
   - `DUPLICATED_AGENT_PER_PROJECT_REQUIRED`
   - `CUSTOM_PRIMING_LAYER_REQUIRED`.

## Failure condition

If reliable work requires a separate custom prompt router, project-specific copies of every specialist, or manual context-paste handoffs, report the failure instead of designing that layer.
