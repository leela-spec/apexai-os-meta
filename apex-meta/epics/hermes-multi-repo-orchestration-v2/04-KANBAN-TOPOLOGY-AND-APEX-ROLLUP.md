# 04 — Kanban Topology and Apex Portfolio Rollup

Status: **D02 RESEARCH REVISED / RECOMMENDATION READY**  
Date: 2026-08-24

## Decision-changing finding

The earlier v2 candidate `one board + repo tenants` is **not recommended now**.

Current upstream evidence shows:

1. Hermes explicitly supports many boards, including one per repo/project/domain.
2. Each board has its own SQLite DB, workspaces and logs.
3. Dispatcher-spawned workers are pinned to one board with `HERMES_KANBAN_BOARD`.
4. Cross-board `kanban_link` dependencies are intentionally forbidden.
5. Tenants are documented as soft namespaces, while boards are the hard isolation boundary.
6. Open issue #85497 (2026-08-13) reports tenant-based memory isolation described by documentation is not implemented and profile memory can pollute across tenants.

Therefore use **hard board separation per repository** and aggregate asynchronously into Apex.

## Recommended topology

```text
Hermes installation
|
+-- board: apex
|    repo/project: apexai-os-meta
|
+-- board: masterofarts
|    repo/project: MasterOfArts
|
+-- board: acim
|    repo/project: acim-secular
|
+-- board: investment
     repo/project: Investment

Apex portfolio rollup
  <- READS board summaries from all four boards
  -> DOES NOT clone/mirror every task
```

## Use native Hermes Projects where useful

Current Hermes has a first-class `hermes project` primitive:

- a project is a human-named workspace;
- it can contain one or multiple folders/repos;
- it can be bound to a Kanban board;
- state is per-profile.

Recommended initial use is deliberately simple:

| Hermes project | Primary folder | Board |
|---|---|---|
| `apex` | `~/workspaces/apexai-os-meta` | `apex` |
| `masterofarts` | `~/workspaces/MasterOfArts` | `masterofarts` |
| `acim` | `~/workspaces/acim-secular` | `acim` |
| `investment` | `~/workspaces/Investment` | `investment` |

Do **not** make a routine worker project spanning all four repos initially. A broad multi-folder project increases accidental scope and is unnecessary for normal project work.

A future `portfolio` project spanning folders may be tested only for the orchestrator/desktop if a real navigation need appears. It is not a substitute for Apex's durable Git control plane and it does not create cross-board dependencies.

### Current upstream project caveat

Open issue #76285 reports `hermes project bind-board` can accept a board slug that does not exist and still exit successfully. Implementation must therefore verify the board exists before/after binding instead of trusting the success message alone.

## Why not one global board?

### Option A — one board + tenants

**Advantages**
- native task dependency graph can span tenants;
- one board/dashboard;
- no aggregation script.

**Risks**
- tenant is a soft boundary;
- open issue #85497 reports tenant memory isolation is not actually enforced;
- large board increases accidental cross-project task visibility;
- one operator mistake can link/assign across domains unintentionally;
- less aligned with user's desired project siloing.

**Verdict:** reject as initial production topology.

### Option B — one board per repo + manual Apex overview

**Advantages**
- strongest native Hermes separation;
- board DB/workspaces/logs physically separate;
- maps directly to repos;
- user can switch board intentionally.

**Costs**
- no native cross-board dependency links;
- no single native dependency graph;
- portfolio overview requires aggregation.

**Verdict:** safe foundation, but manual-only overview is inefficient.

### Option C — one board per repo + asynchronous deterministic Apex rollup

**Advantages**
- keeps hard repo boundaries;
- status rollup does not have to be real-time;
- can be script-only / zero-model-cost;
- Apex can become daily portfolio surface;
- source boards remain authoritative;
- failure can be detected independently.

**Costs**
- one small deterministic aggregation process;
- cross-board dependencies remain references, not native Hermes links;
- rollup freshness must be visible.

**Verdict:** **recommended.**

## Rollup contract

The rollup is **read-only against source boards** in v1.

Input for each board:

```bash
hermes kanban --board apex list --json
hermes kanban --board masterofarts list --json
hermes kanban --board acim list --json
hermes kanban --board investment list --json
```

Current Hermes CLI documents `--board <slug>` as a global Kanban flag and `list --json` as machine-readable output.

Do not depend on ambient `kanban boards switch` state inside automation.

### Output candidate

```text
apexai-os-meta/
  apex-meta/
    portfolio/
      projects.yaml
      current/
        kanban-rollup.json
        kanban-rollup.md
      history/
        YYYY-MM-DD.json      # optional later, retention bounded
```

Do not create this production location until the rollup schema is acceptance-tested.

### Minimum normalized record

```yaml
source_board: investment
source_repo: leela-spec/Investment
snapshot_at: 2026-08-24T...
source_task_id: t_...
title: ...
status: ready|running|blocked|review|done
priority: ...
assignee: ...
updated_at: ...
blocked_reason: ...
source_reference: hermes-board-task-id
```

No task body, raw logs, secrets or entire comment history by default.

## Apex cross-repo dependencies

Hermes cannot link tasks across boards. Do not fake this by duplicating every task.

For a genuine portfolio dependency, create one Apex-board task that references source tasks:

```yaml
apex_task: Launch dependency — Investment data before portfolio review
references:
  - board: investment
    task: t_123
  - board: masterofarts
    task: t_456
kind: cross_repo_dependency
owner: portfolio_orchestrator
```

This Apex task is the **portfolio-level decision/escalation object**. Source tasks remain authoritative for their local execution.

Initial v2 behavior is intentionally not bidirectional:

```text
source boards --> deterministic read-only rollup --> Apex
Apex decisions --> human/orchestrator explicitly creates/updates source tasks when required
```

Do not automatically mutate source tasks from rollup state until a concrete need and conflict policy are defined.

## Scheduling recommendation

User requirement: synchronization does not need to be simultaneous.

Recommended cadence candidate:

- normal rollup: every 1–4 hours during active operation, or once daily initially;
- on-demand: run before CEO/portfolio review;
- no polling faster than needed.

### Hermes Cron fit

Hermes supports `no_agent=True` script-only cron:

- zero model calls;
- zero provider tokens;
- script stdout/output only;
- non-zero exit is supposed to alert;
- jobs with workdir are serialized.

However, current issue history shows cron persistence/false-silent failure classes. Therefore the first implementation must acceptance-test the installed Hermes version before cron becomes authoritative.

Safer staged rollout:

```text
Stage 1: manual deterministic rollup command
Stage 2: repeat manual + compare deterministic output
Stage 3: Hermes no-agent cron OR OS scheduler
Stage 4: verify last-success timestamp/heartbeat
Stage 5: use rollup in daily Apex operation
```

The automation is only healthy when:

```text
last_success_at is recent
AND source board list succeeded for every configured board
AND output validates against schema
```

Empty output is not proof of success.

## Board-level user stories

### US-K1 — Work only on Investment

```text
operator -> Investment task
board = investment
workspace = ~/workspaces/Investment
profile = research-strategist
QMD = investment-* only

result -> Investment repo
status -> investment board
later rollup -> Apex summary
```

No MasterOfArts/ACIM task state is available to the worker through Kanban tools.

### US-K2 — Daily CEO review

```text
rollup reads four boards
  -> normalized portfolio snapshot
  -> portfolio-orchestrator reads snapshot
  -> identifies only blockers/decisions/cross-repo dependencies
  -> creates Apex board tasks for portfolio-level work
```

No full task duplication.

### US-K3 — Cross-repo dependency

```text
Investment task is blocked
because Apex policy decision is required

Investment task:
  status = blocked
  reason = "needs portfolio policy D42"

Apex:
  one portfolio task references Investment task ID

After decision:
  operator/orchestrator records durable Apex decision
  source Investment task receives explicit comment/update
```

This is asynchronous and auditable.

## Acceptance tests

- [ ] create all four boards;
- [ ] prove each board has separate DB/path;
- [ ] query each with explicit `--board ... list --json`;
- [ ] prove a worker on `investment` cannot list `masterofarts` through Kanban tools;
- [ ] prove cross-board `link` is rejected;
- [ ] create matching Hermes Project and bind to board only after verifying board exists;
- [ ] run deterministic rollup twice with unchanged source and obtain semantically identical output;
- [ ] intentionally fail one board query and prove rollup fails rather than publishing partial healthy state;
- [ ] record `snapshot_at` and per-board source status;
- [ ] no source board is modified by v1 rollup;
- [ ] no tenant-based memory isolation assumption is used.

## Primary sources

- Hermes Kanban official docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes Kanban source docs: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/kanban.md
- Hermes CLI commands / `--board` / Projects: https://hermes-agent.nousresearch.com/docs/reference/cli-commands
- Tenant memory isolation issue #85497: https://github.com/NousResearch/hermes-agent/issues/85497
- Historical cross-board query issue #54464: https://github.com/NousResearch/hermes-agent/issues/54464
- Project bind validation issue #76285: https://github.com/NousResearch/hermes-agent/issues/76285
- Hermes Cron: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron
