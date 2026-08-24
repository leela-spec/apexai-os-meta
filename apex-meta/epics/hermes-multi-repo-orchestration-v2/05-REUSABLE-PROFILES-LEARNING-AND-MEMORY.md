# 05 — Reusable Profiles, Learning and Memory

Status: **D03/D04 VERIFIED WITH SAFETY CONDITIONS / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24

## Core decision

Reusable Hermes profiles remain the recommended model, but only with an explicit **sequential ownership rule** across repositories.

```text
profile = durable role / agent identity
repo    = project facts and workspace
board   = project work queue
skill   = reusable procedure
memory  = small role/user learning, never a project KB
```

Do not create `research-strategist-acim`, `research-strategist-investment`, etc. merely because the repositories differ.

Do not run the same writable `research-strategist` profile in two worker processes simultaneously.

## Why this is verified

Hermes official profile documentation states that each profile has its own:

- config;
- `.env` / credentials;
- SOUL;
- memory;
- sessions;
- skills;
- cron;
- state DB.

It explicitly warns:

> Never point two agent processes at the same profile.

The reason is automatic memory/state writing: simultaneous writers can compound each other's state.

Hermes also separates profile from workspace and sandbox: a profile does not inherently belong to one repo.

## Important cross-board concurrency finding

Current Kanban documentation exposes `kanban.max_in_progress_per_profile`, but an open August 2026 issue reports `max_in_progress` is enforced independently per board, not as a gateway-wide cap. The gateway dispatcher sweeps active boards independently.

Therefore v2 must **not assume** setting `max_in_progress_per_profile: 1` creates a machine-wide single lane across four boards.

### Initial safe mode

```text
all repo boards exist
all repo state can be read/rolled up
BUT
only one repo board is actively dispatched for autonomous work at a time
```

Recommended initial control:

```yaml
kanban:
  dispatch_in_gateway: false
  auto_decompose: false
```

Exact installed-version keys must be verified before implementation.

Work is dispatched intentionally against one explicit board:

```text
active execution window = investment
  -> investment board may dispatch
  -> same role profile is not dispatched elsewhere

window ends
  -> task finishes
  -> learning candidate persists
  -> rollup/promotion may occur

next execution window = acim
```

This fits the user's stated requirement that cross-repo learning does not have to happen simultaneously.

### Why disable automatic all-board dispatch initially

Current Hermes gateway behavior sweeps every active board. Issue history also records accidental unbounded worker swarms and per-board concurrency multiplication. Until the installed version passes a global concurrency test, background multi-board autonomous dispatch is not part of v2.

## Memory ownership model

### USER.md

Use for stable operator preferences and interaction expectations.

Not for:
- project status;
- repo architecture;
- source facts;
- task state.

### MEMORY.md

Use for small durable role/environment lessons that should be present at session start.

Hermes documents MEMORY as bounded (~2,200 chars / ~800-token class). It is injected in every session for that profile.

This makes it valuable but expensive relative to on-demand retrieval.

Allowed examples:

```text
"Prefer current official sources over cached research when versions change."
"For long research, persist evidence before context reset."
```

Avoid:

```text
"Investment currently uses provider X."
"ACIM file Y is current authority."
"MasterOfArts launch is blocked on Z."
```

Those are project facts and belong in repo files / AGENTS / task state / QMD.

### AGENTS.md / project context

Hermes' own "Which File Does What" guidance says:

```text
SOUL.md   = who the agent is
USER.md   = who the user is
MEMORY.md = what the agent learned
AGENTS.md = what the project needs
```

Use this separation as a v2 invariant.

## User story — one Research Strategist learns across repositories

### Investment execution window

```text
profile    = research-strategist
board      = investment
workspace  = ~/workspaces/Investment
context    = Investment/AGENTS.md
QMD scope  = investment-control, investment-evidence
```

Researcher discovers:

1. **Project fact:** data provider X has stale series Y.
2. **General procedure:** when time-series providers disagree, compare observation date, release date and revision/vintage before treating values as contradictions.

Ownership:

```text
project fact      -> Investment repo evidence/decision
procedure         -> candidate learned role skill
raw task state    -> Investment Kanban
portfolio impact  -> later Apex rollup/decision if consequential
```

### Later ACIM execution window

Same `research-strategist` profile works inside `acim-secular`.

It may reuse the generalized evidence-validation procedure.
It must not rely on Investment provider facts unless explicitly retrieving Investment because the task is genuinely cross-repo.

## Learning spillover model

```text
repo experience
   |
   +-- facts ----------------------> source repo
   |
   +-- task status ----------------> source board
   |
   +-- role-local lesson ----------> role MEMORY or learned skill
   |                                  (prefer skill for procedure)
   |
   +-- generalizable procedure ---> reviewed promotion candidate
                                      |
                                      v
                                 Apex shared skill
```

### Prefer skills over MEMORY for reusable methods

Reasons:

1. MEMORY is included in every session.
2. Skills are progressively disclosed and full instructions load on demand.
3. A skill can carry scripts/references/verification steps.
4. A skill is portable and versionable under the Agent Skills specification.
5. A reviewed skill can be made available to more than one profile without sharing raw memory.

## Same-role vs cross-role spillover

### Same role across repos

Native profile reuse provides continuity:

```text
research-strategist
  Investment -> ACIM -> Apex -> MasterOfArts
```

Subject to the sequential single-writer rule.

### Cross-role

Do **not** share the raw profile home.

Instead:

```text
research-strategist learned skill
  -> reviewer
  -> generalized approved skill
  -> shared library
  -> independent-reviewer / other applicable roles can discover it
```

## Profile distributions — promising Apex-native control-plane mechanism

Hermes profile distributions are Git repositories that can package:

- SOUL;
- selected config;
- skills;
- cron definitions;
- MCP configuration;
- plugins.

Hermes deliberately does **not** distribute/overwrite:

- memories;
- sessions;
- auth;
- `.env`;
- state DB/logs.

This fits the desired Apex role well:

```text
Apex Git
  canonical reviewed agent specification
      |
      v
Hermes profile distribution
      |
      v
local installed role profile
  + local memory
  + local sessions
  + local credentials
```

However, distributions are unsigned by default and update semantics need acceptance testing before Apex becomes authoritative for live profiles. Treat as a v2 pilot, not an automatic migration step.

## Profile hierarchy candidate

Apex may version definitions such as:

```text
apex-meta/orchestration/hermes/profiles/
  portfolio-orchestrator/
  research-strategist/
  independent-reviewer/
  workshop-designer/
  marketing-executive/     # only if still needed outside current MasterOfArts installation
```

Each may contain reviewed:

```text
distribution.yaml
SOUL.md
selected config defaults
approved skills
optional cron templates
MCP declarations
```

No `memories/`, sessions, auth or secrets.

Do not create this production hierarchy until the profile-distribution pilot passes update/preservation tests.

## Acceptance tests

### Role reuse

- [ ] launch same role sequentially in repo A then repo B;
- [ ] confirm repo-specific AGENTS/context changes;
- [ ] confirm project-specific QMD scope changes;
- [ ] confirm no stale source-repo facts are used without retrieval;
- [ ] confirm generic procedure remains usable.

### Concurrency

- [ ] disable all-board background dispatch initially;
- [ ] create ready same-profile tasks on two boards;
- [ ] prove operating procedure dispatches only one;
- [ ] verify no two same-profile worker processes exist simultaneously;
- [ ] do not enable global autonomous dispatch until installed Hermes proves a machine-wide safe cap.

### Memory contamination

- [ ] inspect role MEMORY before repo A;
- [ ] run representative task;
- [ ] inspect after;
- [ ] verify project facts were written to source repo, not role memory;
- [ ] repeat with repo B;
- [ ] deliberate contamination test must be detected/reviewed.

### Profile distribution pilot

- [ ] publish a disposable test distribution from Apex-controlled source;
- [ ] install test profile;
- [ ] add local memory/session;
- [ ] update distribution source;
- [ ] run `hermes profile update`;
- [ ] verify SOUL/approved distributed files update;
- [ ] verify local memory/session/auth remain untouched;
- [ ] verify untrusted cron is not silently activated.

## Primary sources

- Hermes Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Hermes profile source docs: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/profiles.md
- Profile Distributions: https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions
- Hermes Memory: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md
- Which File Does What: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/which-file-does-what.md
- Hermes Kanban concurrency: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Per-board concurrency regression #78122: https://github.com/NousResearch/hermes-agent/issues/78122
- Worker swarm risk history #29034: https://github.com/NousResearch/hermes-agent/issues/29034
