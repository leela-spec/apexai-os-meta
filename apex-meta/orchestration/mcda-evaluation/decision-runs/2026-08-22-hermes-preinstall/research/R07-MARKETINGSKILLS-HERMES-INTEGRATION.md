# R07 — MarketingSkills + Hermes Integration Research

Status: **RESEARCH REQUIRED / PRE-INSTALL**  
Priority: **P0 — MarketingSkills is a locked target package**  
Depends on: R02 project hierarchy, R05 specialist priming  
Decision owner: Human CEO

## Decision question

Can Corey Haines' current **MarketingSkills** package be installed and used inside Hermes as an upstream Agent Skills package across multiple Master of Arts project families **without custom middleware, per-project agent duplication, or conflicting product-marketing context**?

The target is to install the upstream package, not rewrite it.

## Primary official sources

- MarketingSkills repository: https://github.com/coreyhaines31/marketingskills
- MarketingSkills README: https://github.com/coreyhaines31/marketingskills/blob/main/README.md
- Product Marketing skill: https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md
- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes Context Files: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/
- Hermes Kanban/workdirs: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Agent Skills specification where relevant

## Current verified upstream facts to recheck

MarketingSkills currently documents:

- Agent Skills compatibility;
- installation through `npx skills add coreyhaines31/marketingskills`;
- universal-agent installation under `.agents/skills/`;
- a large skill catalog including content, copy, social, video, customer research, launch, offers, pricing, marketing plan, marketing loops and others;
- the `product-marketing` skill as foundational context for the other skills;
- `.agents/product-marketing.md` as the canonical marketing context document inside a project;
- version/changelog behavior for that context file.

Hermes currently documents project-local `.agents/skills/` discovery and trust.

## Research tasks

### 1. Installation path

Verify the exact current command(s) and resulting paths for installing MarketingSkills for an Agent-Skills-compatible runtime.

Compare supported upstream options:

- `npx skills add`;
- clone/copy;
- git submodule;
- any Hermes tap/hub path if officially available;
- another current upstream-supported package-management path.

Score each on:

- upstream support;
- reproducibility/version pinning;
- ease of updates;
- cross-client reuse;
- risk of Hermes modifying the package;
- suitability for a private monorepo.

Do not invent a package-sync process.

### 2. Hermes discovery and trust

Verify:

- whether `.agents/skills/` at the MasterOfArts Git root is discovered by Hermes;
- required `hermes skills trust` behavior;
- precedence against global/local skills;
- whether project skills are protected from Curator mutation;
- whether `skill_manage` can modify them;
- safest supported update strategy.

### 3. The critical product-marketing context question

The upstream `product-marketing` skill stores context at:

```text
.agents/product-marketing.md
```

and states that other marketing skills read this context.

MasterOfArts contains multiple distinct offers/project families. Determine exactly how the upstream skill resolves `.agents/product-marketing.md` relative to the working directory/project root.

Test at least these possibilities against actual behavior/source:

- one company-wide product-marketing file at Git root;
- separate nested project/family product-marketing files;
- starting Hermes from different workdirs;
- multiple Git worktrees/submodules if relevant;
- any supported path/config option in MarketingSkills;
- whether the skill hardcodes repo-root behavior.

This is decision-critical. Do not assume nested context works merely because Hermes `AGENTS.md` supports nesting.

### 4. Multi-project compatibility simulation

Use:

#### Project A
Specific Awakenings/workshop launch.

#### Project B
A materially different Master of Arts offer/project.

For each show:

```text
WORKDIR:
HERMES PROJECT CONTEXT:
MARKETING SPECIALIST PROFILE:
MARKETINGSKILLS LOCATION:
PRODUCT-MARKETING CONTEXT FILE FOUND:
OTHER SKILLS ACTIVATED:
PROJECT-SPECIFIC INPUTS:
OUTPUTS:
RISK OF CONTEXT CONTAMINATION:
```

Pass only if the same upstream package can serve both correctly without copying all skills or manually swapping files in an unreliable way.

### 5. Skill catalog fit

Map actual current MarketingSkills to Master of Arts use cases:

- product/offer positioning;
- customer research;
- content strategy;
- website/landing copy;
- social content;
- video content;
- launch planning;
- pricing;
- offers;
- marketing plan;
- marketing loops;
- community;
- email;
- PR/influencer/partnership where relevant.

Mark each as:

`DIRECT_FIT | NEEDS_PROJECT_CONTEXT_ONLY | SOFTWARE_BIASED | NOT_RELEVANT`.

Do not claim a skill is suitable without reading its current SKILL.md where the fit is consequential.

### 6. Inputs/outputs and token behavior

For representative skills record:

| Skill | Trigger/input | Required context file | Other skills referenced | AI reasoning? | Deterministic tools? | External APIs? | Output | Token driver |
|---|---|---|---|---|---|---|---|---|

At minimum inspect:

- product-marketing;
- customer-research;
- content-strategy;
- copywriting;
- social;
- video;
- launch;
- offers;
- pricing;
- marketing-plan;
- marketing-loops.

### 7. External-service and billing audit

Some marketing skills may suggest or call external tools/APIs. For every relevant tool integration distinguish:

- pure instruction skill;
- deterministic local CLI;
- external SaaS/API;
- API key required;
- extra billing required;
- data sent externally;
- optional vs required.

The base marketing capability should not be described as free/local if a required skill actually depends on a paid external service.

### 8. Upstream updates

Determine the supported way to update MarketingSkills while preserving:

- upstream skill integrity;
- Master of Arts project context files;
- any operator-approved configuration;
- version visibility;
- rollback possibility.

Avoid forking/customizing unless the upstream package cannot meet the use case otherwise; if a fork is required, classify that as a blocker for the reuse-first target.

### 9. Cross-client reuse

Verify whether the same installed skill files can be used by:

- Hermes;
- Codex;
- Claude Code;
- other Agent Skills-compatible CLIs;
- web AIs only as ordinary repo files where native skill activation is absent.

Note runtime-specific install locations where the upstream installer differs.

## Required output

1. current package/version/license evidence;
2. installation/update strategy using upstream mechanisms;
3. Hermes discovery/trust/precedence result;
4. product-marketing context path analysis;
5. two-project compatibility simulation;
6. use-case fit map;
7. representative skill I/O/token/API matrix;
8. cross-client portability matrix;
9. unresolved blockers;
10. verdict:
   - `MARKETINGSKILLS_HERMES_CONFIRMED`
   - `MARKETING_CONTEXT_PATH_CONFLICT`
   - `UPSTREAM_CONFIGURATION_REQUIRED`
   - `CUSTOM_FORK_REQUIRED`.

## Failure condition

If Master of Arts must maintain copied MarketingSkills trees per project, manually swap context files, or fork the package just to obtain correct project scoping, report the blocker. Do not implement the workaround in this research run.
