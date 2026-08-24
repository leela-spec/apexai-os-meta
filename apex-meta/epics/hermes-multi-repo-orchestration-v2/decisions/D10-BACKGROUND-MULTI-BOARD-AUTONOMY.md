# D10 Appendix — Background Multi-Board Autonomy Is Deferred

**Decision status:** DEFERRED SAFETY GATE  
**Decision ledger:** `../DECISIONS.md`  
**Primary incident:** `../incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md`  
**Primary subject files:** `../03-MULTI-REPO-EFFICIENCY-RISKS-AND-SAFETY.md`, `../11-IMPLEMENTATION-ROADMAP.md`

## What this decision means in plain language

This decision does **not** disable Hermes automation, Kanban, Docker, reusable agents, cron, QMD or multi-repo operation.

It disables only this initial behavior:

```text
Hermes gateway wakes up
  -> independently starts workers from Apex board
  -> independently starts workers from MasterOfArts board
  -> independently starts workers from ACIM board
  -> independently starts workers from Investment board
  -> several workers may reuse role profiles and dynamic Docker workspaces simultaneously
```

Initial v2 instead does:

```text
choose one active repo/board
  -> launch intended role
  -> verify exact repo/workspace/mount
  -> execute
  -> verify host-side artifact/commit
  -> finish/checkpoint
  -> later work another repo
```

All four boards still exist. Rollups and scheduled read-only jobs may still run. The restriction is specifically on **concurrent autonomous execution workers across multiple boards**.

## Why this exists

The intended architecture has three moving boundaries at once:

1. **board boundary** — which project's task is running;
2. **profile boundary** — which reusable role's memory/state is being mutated;
3. **Docker workspace boundary** — which host repository the worker is actually allowed to modify.

Current upstream evidence contains open defects/regressions in exactly these intersections. Until the installed Hermes version proves them safe, enabling background multi-board execution would turn a known uncertainty into unattended file mutation.

## Forces

- operator wants automation but does not require simultaneous synchronization/execution;
- separate boards are accepted under D02;
- reusable profiles are accepted under D03;
- Docker is the single execution-isolation boundary;
- source repositories must never receive work intended for a different repo;
- a successful command/commit inside a container is insufficient if the workspace is not actually host-backed.

## Incident summary

The separate incident file records four relevant current issue classes:

- profile cwd overriding/broadening intended task mount;
- host path/container cwd disagreement across tool calls;
- Kanban Docker workspace not persisting completed work to host;
- concurrency limits applying per board rather than protecting a shared profile globally.

See `../incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md`.

## Risks if D10 were ignored now

- worker edits wrong repository;
- work appears committed but disappears with sandbox/container state;
- two boards concurrently mutate the same role profile memory/state;
- sandbox receives broader host access than the task intended;
- terminal/file/code tools operate against different effective directories;
- autonomous jobs report success while durable host state is wrong.

## Shortcomings of this decision

- initial v2 cannot fully exploit parallel autonomous workers across repos;
- role reuse is sequential unless separate profiles are deliberately created;
- unattended overnight execution throughput is lower;
- board queues are initially task tracking/dispatch inputs rather than fully autonomous multi-board execution sources.

These are accepted because the user explicitly does not require simultaneous execution or synchronization.

## What is still allowed

- four independent boards;
- manual or controlled sequential Hermes execution;
- asynchronous deterministic board rollups;
- script-only/no-model scheduled health/rollup jobs after scheduler validation;
- QMD indexing/retrieval;
- delayed learning-candidate harvest;
- separate distinct role profiles operating concurrently when they do not violate tested workspace/profile safety rules;
- future live experiments specifically designed to close this gate.

## Gate to enable background autonomy later

All of the following must pass on the **installed Hermes version**, not merely in documentation:

1. create a disposable task workspace for repo A;
2. prove terminal, file tools and code execution all resolve to the same effective repo A workspace;
3. write a disposable file and verify it immediately on the WSL host outside the container;
4. create a disposable Git commit and verify the commit exists in the host repo after worker/container exit;
5. prove repo B/unrelated host paths are inaccessible from the repo A worker unless deliberately mounted;
6. prove profile configuration does not override/broaden the task workspace;
7. run workers on two different boards and prove same-profile state cannot be concurrently mutated or is globally serialized;
8. restart Hermes/Docker and prove task/output durability;
9. intentionally trigger a mount/workspace failure and prove automation fails closed rather than publishing success;
10. record exact Hermes version and rerun these tests after relevant Hermes upgrades.

Only after all pass may D10 change from `DEFERRED SAFETY GATE` to `AUTHORIZED`.

## Rejected alternatives

1. **Enable background autonomy because the happy-path MasterOfArts test worked** — rejected: the multi-board topology adds new concurrency/workspace interactions.
2. **Create custom sandbox/orchestration middleware immediately** — rejected: would add complexity before upstream/native behavior is tested/fixed.
3. **Disable Docker to avoid workspace issues** — rejected: removes the chosen execution-isolation boundary.
4. **Create one profile per repo to hide the concurrency problem** — rejected as the default because it fragments role learning and does not solve host-workspace persistence defects.

## Watch / revisit conditions

Re-check D10 whenever:

- Hermes is upgraded beyond the version against which the incident was recorded;
- relevant upstream issues close with released fixes;
- the project needs genuine simultaneous cross-repo execution strongly enough to justify a dedicated acceptance run.

## Evidence links

- Hermes Kanban: https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban
- Hermes profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Incident: `../incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md`
- Risk register: `../12-RISK-REGISTER.yaml`
- Implementation roadmap: `../11-IMPLEMENTATION-ROADMAP.md`
