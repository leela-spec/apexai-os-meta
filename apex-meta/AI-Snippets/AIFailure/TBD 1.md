Yes. We found the real mistake.

## The actual mismatch

Your **Weekly Orchestrator is not a Hermes-native orchestrator**. It is explicitly designed as a **file-driven `.claude` main-thread control plane** with isolated stage forks. Its contract says it reads Session/Sync artifacts and dispatches `PrecapWeek`/`PrecapNextDay`; it does not depend on Hermes Kanban tooling.

Meanwhile, native `kanban_list` is a Hermes-profile capability. Current Hermes documentation confirms that it only appears in a Hermes session with the Kanban toolset explicitly enabled. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference?utm_source=chatgpt.com "Toolsets Reference | Hermes Agent"))

So we kept trying to bridge the **tool surface** between two runtimes.

That is unnecessary.

## The architecture you had already chosen was right

Your accepted D02 already says:

```text
Hermes repo boards
        ↓
asynchronous deterministic read-only rollup
        ↓
Apex portfolio state
```

and explicitly says **do not mirror tasks into Apex**.

We accidentally tried to bypass that design.

### Correct target

```text
HERMES PM RUNTIME
4 isolated Kanban boards
        │
        │ deterministic / 0 LLM
        ▼
PORTFOLIO STATE PUBLISHER
runs in WSL beside Hermes
        │
        ├── full machine snapshot
        └── compact weekly-frontier.json
                    │
                    ▼
          APEX REPO / FILE INTERFACE
                    │
                    ▼
       Weekly Orchestrator
       PrecapWeek → NextDay
```

**The Weekly Orchestrator never needs Kanban tools.**

It only needs a fresh file.

That also makes the architecture client-independent: Claude Code, Hermes, Antigravity, or something else can all consume the same state feed.

---

## What actually needs fixing

|Problem|Fix|
|---|---|
|Snapshot is 1 day stale|refresh publisher much more frequently|
|Weekly session can't access Kanban|irrelevant — it reads the feed|
|Current rollup uses legacy Windows paths for Apex/MoA|patch to canonical `/root/workspaces/*`|
|Full snapshot too noisy for LLM|produce a compact `portfolio-frontier.json`|
|Frequent updates would dirty Git|live frontier should be runtime/gitignored; durable checkpoints separate|
|PrecapWeek currently expects Session/Sync|add Frontier as project-execution-state input|
|Apex Sync duplicates Hermes PM|don't feed Hermes tasks into Apex Sync|

There is a **real bug** in the current publisher: Apex and MasterOfArts still prefer `/mnt/c/GitDev/...`, despite the implemented architecture having moved the canonical repos to `/root/workspaces/*`. The recovery evidence confirms `/root/workspaces/*` is now canonical.

And the current systemd publisher only runs daily at 09:00. That explains the stale state.

### I would use a 5-minute deterministic refresh

Four SQLite reads plus four `git rev-parse` calls every five minutes are trivial. No model calls.

But **do not continually modify tracked Git files**.

Use:

```text
apex-meta/orchestration/runtime/
    portfolio-snapshot.json
    portfolio-frontier.json
    health-receipt.yaml
```

as gitignored live runtime state.

Then optionally preserve a durable snapshot only:

```text
when Weekly planning starts
or
when explicitly requested
```

This gives you:

> Hermes Kanban = live PM truth  
> runtime Frontier = cross-runtime read model  
> Git = durable architecture/evidence  
> Weekly = semantic portfolio planner

---

## Don't do these anymore

Do **not**:

- expose `~/.hermes` to the Weekly Docker container;
    
- enable Kanban tools just to make Weekly work;
    
- build a Kanban MCP bridge;
    
- make Weekly shell out to Hermes;
    
- import Hermes tasks into Apex epics;
    
- require ProjectStatus to reconstruct local PM state.
    

Those are all extra coupling.

---

## The next implementation should happen outside the failed Weekly session

Use the host-capable WSL/Antigravity executor once to repair the **publisher**, then rerun Weekly normally.

A much shorter instruction is enough:

Implement the smallest bridge between Hermes Kanban PM and Apex Weekly Orchestration.

Authority:

- `apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions/D02-KANBAN-TOPOLOGY.md`
    
- `scripts/hermes/apex_portfolio_rollup.py`
    
- current canonical workspace architecture under `/root/workspaces/*`
    

Do NOT try to expose Hermes `kanban_*` tools to Weekly Orchestrator.

Target architecture:

Hermes boards → deterministic WSL publisher → compact file-based Frontier → Weekly Orchestrator.

Required work:

1. Inspect the current publisher and systemd service/timer in the actual WSL runtime.
    
2. Patch the publisher so all Git HEAD checks use canonical `/root/workspaces/*` repos only; remove legacy `/mnt/c/GitDev/*` preference.
    
3. Keep board reads read-only and fail-closed.
    
4. Add a compact `portfolio-frontier.json` containing per project:  
    board, repo HEAD, freshness, status counts, running/review/blocked work, and a bounded set of ready candidates with source task IDs.
    
5. Put frequently refreshed live outputs in a gitignored runtime directory so the repository is not continuously dirty.
    
6. Change the deterministic systemd refresh from daily-only to a reasonable near-live cadence, initially 5 minutes.
    
7. Verify two consecutive refreshes, board completeness, current repo HEADs, atomic publication, and zero model calls.
    
8. Do not modify Weekly/Precap/ProjectStatus yet.
    

Existing-file changes must be exact-match patches, not whole-file rewrites.

Return:

- exact patches;
    
- runtime paths;
    
- timer/service configuration;
    
- verification evidence;
    
- fresh Frontier contents;
    
- no Weekly production changes yet.
    

Then the **next** Weekly test becomes almost boring:

```text
Read fresh portfolio-frontier.json
+
read Apex-native Session/Sync state
→ PrecapWeek
→ PrecapNextDay
```

That is exactly what we want. If the connection is good, it should become boring infrastructure rather than another agent-integration problem.