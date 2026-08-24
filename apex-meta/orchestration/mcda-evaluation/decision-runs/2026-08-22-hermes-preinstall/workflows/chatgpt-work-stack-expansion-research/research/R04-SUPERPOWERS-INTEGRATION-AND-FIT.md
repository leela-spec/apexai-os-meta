# R04 — Superpowers Integration and Fit

Status: **RESEARCH REQUIRED**  
Depends on: R01  
Candidate identity: `obra/superpowers`

## Decision question

Does current Superpowers add a verified workflow/review/skill methodology that improves the Master of Arts Hermes stack, or is it mainly software-development overlap with BMAD and existing review mechanisms? Is its current Hermes path actually installable/reliable today?

## Primary source families

- https://github.com/obra/superpowers
- current skills and installation docs/source
- current releases
- current issues/PRs, especially Hermes installation, security scan and tool-mapping reports
- current Hermes plugin/skills/security docs if a Hermes path is claimed

## Research tasks

### 1. Establish current product/methodology

Verify current Superpowers architecture and major workflows, including where current:

- skill discovery/mandatory skill invocation;
- brainstorming/specification;
- planning;
- subagent-driven development;
- test-driven development;
- systematic debugging;
- verification before completion;
- requesting/receiving code review;
- writing/testing skills;
- supported runtimes/harnesses.

Classify which are software-specific and which are genuinely domain-general.

### 2. Verify Hermes support from current main/release

Do not rely on an old documentation path.

Search current repo/release for:

- Hermes installer/plugin/skill target;
- exact installation command/path;
- tool-name mappings;
- Agent Skills compatibility;
- Hermes security/scan interactions;
- current open/closed issues and fixes.

If current docs and current issues conflict, state the affected version and current status.

### 3. Compare against existing MoA method layer

Map each valuable Superpowers workflow against:

- BMAD research/planning/review/persona workflows;
- Hermes Kanban maker/reviewer lifecycle;
- existing ChatGPT Work evidence-review workflow;
- MarketingSkills where relevant;
- current MoA research and workshop/non-software use cases.

For each: `UNIQUE_VERIFIED_VALUE | BETTER_THAN_BASELINE | OVERLAP | SOFTWARE_ONLY | OPEN`.

Do not recommend duplicate review/planning processes unless a concrete user story improves.

### 4. Integration models

Evaluate only current supported paths:

A. install Superpowers into Hermes as skills/plugin;
B. use Superpowers in another supported CLI on the same repo, sharing durable files only;
C. replace selected BMAD workflows with Superpowers;
D. no current stable Hermes integration; defer.

Trace exact inputs/outputs, skill activation, tool mapping, persistent artifacts and review state.

### 5. Non-software transfer test

Apply the actual skill semantics to:

- research-to-workshop design;
- workshop marketing/content;
- business/admin workflow;
- methodology/coaching development.

Do not rewrite Superpowers into a custom non-software framework. Determine whether the unchanged upstream skill meaning fits.

### 6. Token/behavioral burden

Verify how aggressively Superpowers requires skill invocation and what this means for:

- skill metadata/body loading;
- repeated procedure overhead;
- interaction with Hermes semantic skill routing;
- BMAD/MarketingSkills coexistence;
- autonomy vs forced checkpoints;
- risk of conflicting instructions.

### 7. Operational evidence

Search current releases/issues/tests for:

- Hermes install support stability;
- security scanner blocks;
- tool mapping errors;
- regressions;
- maintainer response/fixes;
- evidence of real use beyond repo popularity.

Treat stars as adoption only.

## Required output

1. current Superpowers architecture/methodology;
2. exact current Hermes support verdict;
3. BMAD/Hermes/Superpowers overlap matrix;
4. software vs non-software fit table;
5. integration options with evidence classes;
6. token/context/autonomy implications;
7. operational reliability evidence;
8. user-story simulations;
9. recommendation `ADD_NOW | PILOT | REPLACE_SELECTED_METHODS | DEFER | REJECT`;
10. exact retained/redundant components;
11. switching conditions;
12. source registry.

## Pass standard

Pass only if current upstream evidence establishes what Superpowers can do *today* in Hermes/MoA. Do not infer stable Hermes support or general business applicability from the project’s overall popularity.
