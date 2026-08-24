# R03 — Agency Agents Integration and Fit

Status: **RESEARCH REQUIRED**  
Depends on: R01  
Candidate identity: `msitarzewski/agency-agents`

## Decision question

Does Agency Agents provide a verified superior specialist-agent layer for the Hermes-centered Master of Arts stack, and does its current first-party Hermes router integration work in a way that improves specialist coverage without context bloat, duplicate identities or unreliable routing?

## Primary source families

- https://github.com/msitarzewski/agency-agents
- current `integrations/hermes/README.md` and generated plugin/source
- current releases/commits/tests/CI
- current issues/PRs/discussions relevant to Hermes schema/routing/delegation
- current Hermes plugin/delegation documentation where needed

## Research tasks

### 1. Establish current package state

Verify:

- current roster size/divisions;
- agent definition format and content quality;
- license/commercial-use status;
- current activity/release mechanism;
- generated-tool conversion architecture;
- supported harnesses;
- current Hermes integration status.

Do not accept “production-ready/battle-tested” labels without operational evidence.

### 2. Reproduce the official Hermes integration on paper

Verify current source for:

```text
Agency Agents repository
 -> conversion/generation step
 -> `agency-agents-router` Hermes plugin
 -> installation under Hermes home
 -> plugin enablement
 -> tool schema loaded by Hermes
 -> search specialist
 -> inspect specialist
 -> load specialist prompt
 -> delegate via Hermes delegate_task where available
 -> result returns to current Hermes task/session
```

Record exact tools/parameters/current generated roster count and any prerequisites.

Classify every edge as native/official/config/custom.

### 3. Compare against current specialist architecture

Current baseline uses:

- Hermes profiles as durable specialist identities/process separation;
- BMAD persona/workflow skills;
- MarketingSkills;
- future approved skills;
- project context/QMD from current workdir.

Determine whether Agency Agents should:

- replace some Hermes profiles;
- provide an on-demand roster that Hermes profiles invoke;
- replace/overlap BMAD personas;
- complement MarketingSkills;
- be used only for gaps;
- not be installed.

Identify conflicting persona/output/tool instructions and ownership of memory/reviewer separation.

### 4. Context/token analysis

Verify whether the Hermes router truly avoids preloading the full roster and what stays in startup context:

- tool schemas;
- agent index/data;
- selected agent body;
- delegated task context;
- project context;
- skill context.

Estimate comparative context cost using evidence from the actual plugin architecture, not generic token assumptions.

### 5. Specialist-quality / value audit

Sample a representative set relevant to MoA:

- marketing/brand/content;
- research/strategy;
- project/program management;
- workshop/learning/education if present;
- operations/business;
- independent review/QA;
- software/product bridge.

For each compare role specificity, method depth, output contract, tool assumptions, software bias and overlap against the current BMAD/MarketingSkills/profile layer.

Use content evidence, not agent-name count.

### 6. User-story simulations

Trace:

1. Hermes receives an ambiguous marketing task and selects an Agency specialist.
2. Same specialist type works in Project A then Project B with local context isolation.
3. Multi-disciplinary task searches and delegates to several specialists without preloading all agents.
4. Agency specialist produces artifact -> independent Hermes reviewer requests changes.
5. Missing/bad specialist selection is corrected.
6. Plugin unavailable/schema mismatch/restart recovery.

### 7. Operational reliability

Search current issues/PRs/CI for:

- Hermes tool-schema bugs/fixes;
- delegate-task compatibility;
- generated plugin drift;
- conversion/install failures;
- stale specialist definitions;
- tests that cover Hermes integration.

State affected versions/status and whether current main/release contains the fix.

### 8. Learning/update interaction

Verify whether Agency specialist definitions are static upstream content, project-local content, or mutable Hermes learning. Determine:

- who updates them;
- whether Curator touches them;
- how learned procedures coexist with selected Agency prompts;
- whether custom/forked agent definitions would create maintenance drift.

Prefer upstream package unchanged.

## Required output

1. plain-language Agency Agents architecture;
2. exact Hermes router integration flow;
3. roster/specialist quality audit;
4. current specialist-layer overlap matrix;
5. context/token behavior;
6. six user-story simulations;
7. operational issue/test evidence;
8. update/learning ownership;
9. cost/license/security/platform implications;
10. recommendation: `ADD_NOW | PILOT | DEFER | REJECT | REPLACE_SPECIFIC_LAYER` with exact scope;
11. switching conditions;
12. source registry.

## Pass standard

Pass only when the recommendation is based on the actual current Hermes plugin, actual sampled specialist content and current reliability evidence. A large agent count or impressive labels are not enough.
