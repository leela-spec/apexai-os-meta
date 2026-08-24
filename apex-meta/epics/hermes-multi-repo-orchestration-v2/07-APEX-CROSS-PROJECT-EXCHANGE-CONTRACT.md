# 07 — Apex Cross-Project Exchange Contract

Status: **VERIFIED PRIMITIVES / APEX CONTRACT IS OUR CONTROL-PLANE DESIGN**  
Date: 2026-08-24

## Important distinction

There is no upstream Hermes feature called "Apex portfolio control plane." That layer is our repository architecture.

What is verified upstream are the primitives it uses:

- separate Hermes boards and machine-readable board CLI;
- repo/workspace-scoped AGENTS/project context;
- reusable profile state;
- Agent Skills / Hermes skills;
- profile distributions;
- local multi-collection QMD;
- Hermes Cron/no-agent scripts;
- Hermes Projects for named folder/workspace grouping.

Therefore Apex must exchange **small explicit contracts over proven primitives**, not pretend Hermes natively synchronizes four repositories.

## Ownership table

| Information | Canonical owner | Apex receives? | Direction |
|---|---|---:|---|
| Source code/content | source repo | pointer/summary only | repo -> Apex when consequential |
| Project facts/evidence | source repo | selected summary/pointer | repo -> Apex |
| Project AGENTS/rules | source repo | entrypoint pointer + governance metadata | repo -> Apex |
| Project task state | source Hermes board | normalized rollup | board -> Apex |
| Cross-project decision | Apex repo | yes, canonical | Apex -> affected projects by explicit action |
| Cross-project dependency/escalation | Apex board/repo | yes | source -> Apex -> explicit follow-up |
| Role raw memory | local Hermes profile | **no** | never copied |
| Generalized reusable procedure | reviewed Apex shared skill | yes | role -> review -> Apex -> runtime consumers |
| Repo-specific skill | source repo | catalog pointer only | repo-local |
| QMD index/vectors | local QMD runtime | **no** | never copied |
| QMD collection registry metadata | machine runtime + Apex desired-state registry | names/paths/freshness only | local -> Apex status |
| Credentials/secrets | local profile/secret store | **no** | never copied |
| BMAD framework/state | repo that uses BMAD | status/pointer only | repo-local |
| MarketingSkills | MasterOfArts for now | status/pointer only | repo-local for v2 |

## Exchange Bus A — portfolio status

### Source

Separate repo boards:

```text
apex
masterofarts
acim
investment
```

### Transfer

Deterministic read-only rollup from explicit board queries.

### Apex product

Current portfolio snapshot, not a duplicate task database.

Suggested normalized project record:

```yaml
project_id: investment
repo: leela-spec/Investment
default_branch: main
board: investment
snapshot_at: ...
counts:
  ready: 3
  running: 1
  blocked: 1
  review: 0
critical_tasks:
  - source_task_id: t_...
    status: blocked
    title: ...
    owner: research-strategist
    blocked_reason: ...
```

### Rule

Apex snapshot is derived status. Source board remains authoritative.

## Exchange Bus B — dependency and escalation

Because Hermes does not link tasks across boards, cross-project dependencies are explicit portfolio objects.

Example:

```yaml
id: XDEP-001
kind: cross_repo_dependency
status: open
source:
  project: investment
  board: investment
  task: t_inv123
requires:
  project: apex
  decision: D42
impact:
  projects:
    - investment
    - masterofarts
next_owner: portfolio-orchestrator
```

### Process

```text
source task encounters cross-project dependency
  -> source task records local blocked reason
  -> Apex portfolio task/decision object is created
  -> Apex resolves portfolio-level decision
  -> explicit follow-up updates affected source task(s)
```

Do not implement automatic bidirectional state mirroring in v2.

## Exchange Bus C — learning / procedural spillover

```text
role-local learned procedure
  -> deterministic candidate manifest
  -> independent semantic review
  -> accepted shared Agent Skill in Apex Git
  -> controlled deployment/discovery
```

Apex stores only the generalized procedure and provenance pointer.

Example:

```yaml
skill: authority-first-source-check
origin:
  profile: research-strategist
  source_project: investment
  source_task: t_...
promotion:
  reviewer: independent-reviewer
  verdict: PROMOTE
  approved_at: ...
scope: cross-project
contains_project_facts: false
```

## Exchange Bus D — knowledge routing

Apex should know **where knowledge lives**, not own copies of all knowledge.

Suggested repo registry fields:

```yaml
project_id: acim
repo: leela-spec/acim-secular
branch: master
workspace: ~/workspaces/acim-secular
context_entrypoints:
  - AGENTS.md
qmd_collections:
  - acim-control
  - acim-site-docs
  - acim-site-code
project_skills_path:
  - .agents/skills
board: acim
```

A portfolio question may ask QMD across selected control collections. A repo task uses only that repo's relevant collections unless the task explicitly requires cross-project evidence.

## Exchange Bus E — cross-project decisions

Apex owns decisions whose scope is genuinely portfolio-wide.

Examples:

- which repos Hermes is allowed to access;
- shared agent/profile definition;
- common safety policy;
- shared-skill promotion law;
- project priority/order;
- cross-repo dependency resolution;
- approved model/provider classes for data sensitivity.

A source repo may reference the Apex decision rather than copying its entire reasoning.

### Decision record minimum

```yaml
id: D42
title: ...
status: accepted|superseded|rejected
scope:
  - apex
  - investment
authority: apexai-os-meta
accepted_at: ...
supersedes: null
implementation_refs:
  - repo: leela-spec/Investment
    path: ...
```

## Exchange Bus F — health and freshness

Apex daily view should be able to tell whether its derived picture is stale.

Per managed repo record:

```yaml
repo:
  branch: ...
  head_sha: ...
  working_tree_state: clean|dirty|unknown
kanban:
  board: ...
  last_rollup_success: ...
qmd:
  collections: [...]
  last_update_success: ...
  pending_embeddings: ...
learning:
  last_harvest_success: ...
  candidates_pending: ...
```

No detailed logs unless troubleshooting is required.

## What Apex must NOT exchange

```text
NO raw MEMORY.md copies
NO USER.md copies
NO session histories
NO API keys / auth tokens
NO Kanban SQLite DB copies
NO QMD SQLite/vector DB copies
NO entire repo mirrors
NO BMAD `_bmad` framework copied between projects
NO MarketingSkills sprayed into repos that do not need marketing
NO automatic cross-board write synchronization in v2
```

## Daily-life user story

### Morning

Operator opens Apex portfolio view.

```text
Apex snapshot:
  Investment  -> 1 blocker
  ACIM        -> 2 ready
  MasterOfArts-> 1 review
  Apex        -> Hermes v2 decision pending
```

Operator asks:

> What needs my attention today?

Portfolio orchestrator uses:

1. latest deterministic board rollup;
2. Apex portfolio priorities/decisions;
3. explicit QMD control collections only when evidence is needed.

It does not load all four repositories into context.

### Deep work

Operator selects Investment.

```text
active execution window = Investment
board = investment
repo = Investment
QMD = investment scopes
```

Other boards remain persisted but undispatched.

### End of work

```text
Investment output -> Investment repo
Investment task status -> Investment board
new general method -> local learned skill candidate
rollup later -> Apex current status
promotion later -> shared Apex skill if accepted
```

## Efficiency law

Apex should exchange **IDs, pointers, summaries, decisions, generalized procedures and freshness metadata**.

It should not exchange raw corpora merely because they might be useful someday.

This keeps:

- Git authority unambiguous;
- prompt context smaller;
- QMD explicit;
- learning reviewable;
- synchronization one-way and reconstructible;
- recovery possible from original owners.

## Reconstruction requirement

Every Apex-derived portfolio artifact must be rebuildable from:

```text
source Git repos
+ source Hermes board query output
+ local QMD status/registry
+ reviewed Apex decisions/shared skills
```

If deleting an Apex snapshot would destroy unique project truth, the architecture is wrong.

## Primary sources

- Hermes Kanban boards: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes CLI / explicit board JSON surface / Projects: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes profile distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
- Hermes skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Agent Skills specification: https://agentskills.io/specification
- Hermes file ownership guidance: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/which-file-does-what.md
- QMD: https://github.com/tobi/qmd
- QMD scoping: https://github.com/tobi/qmd/blob/main/docs/SYNTAX.md
