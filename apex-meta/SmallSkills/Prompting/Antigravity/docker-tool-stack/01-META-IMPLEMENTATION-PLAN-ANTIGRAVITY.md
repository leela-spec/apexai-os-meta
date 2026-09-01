# Meta Implementation Plan — Antigravity Docker Tool Stack

## Target

Create one local Docker Compose stack where the logical tools nginx, PostgreSQL/pgvector, Valkey, Firefly III, Paperless-ngx, OpenProject and Hermes share one Docker bridge network and remain independently replaceable/upgradable.

Hermes is the AI control surface. Human-facing tools retain one dedicated Homepage/localhost port each.

## Authority

Read first:
- `00-START-HERE.md`
- `../antigravity-instruction-orchestrator/SKILL.md`
- its `references/lessons-learned.md`
- its `references/prompt-patterns.md`

## Architecture laws

1. One Compose project, one explicit shared network.
2. Service-name DNS, never fixed container IPs.
3. PostgreSQL and Valkey internal-only by default.
4. App UIs bind to `127.0.0.1:<host-port>`.
5. One database/user per application on shared PostgreSQL.
6. Use official upstream application images unless a custom image solves a demonstrated need.
7. Alpine only where technically appropriate; never force complex upstream products onto Alpine.
8. Preserve persistent data in named/bind volumes.
9. No real secrets in Git.
10. Hermes operates applications via supported APIs, not direct DB writes.
11. No Docker socket in Hermes initial scope.

## M0 — Inventory / preflight only

**Execution mode:** verification only. Do not mutate Docker state.

Inspect and record:
- current containers and images;
- current volumes;
- current networks;
- current Homepage port assignments;
- current compose files;
- existing nginx configuration;
- current PostgreSQL/Valkey state;
- any existing Firefly/Paperless/OpenProject/Hermes installation;
- persistent data that must be preserved;
- machine architecture;
- Hermes repo/workspace mounts and isolation state.

Also inspect the repository for the existing platform architecture and Docker files relevant to this target.

### M0 proof

Return exact command outputs or compact machine-readable evidence for the observed state. Do not infer a tool is absent merely because one expected path is missing.

### M0 stop

Produce:
1. current-state inventory;
2. port table;
3. data-preservation risks;
4. target-vs-current delta;
5. any correction required to this implementation plan;
6. recommended M1 patch scope.

STOP. Do not implement M1.

## M1 — Stack skeleton

Run only after M0 approval.

Create/patch the minimum common stack surfaces:
- one Compose project;
- explicit shared network, recommended name `ki-basis-net` unless live repository authority says otherwise;
- named volumes required by approved services;
- `.env.example` only;
- host-port variables copied from the verified M0 registry;
- health/dependency wiring where deterministic.

Do not start installing all services during M1.

### M1 negative checks

- `docker compose config` must fail if a required variable/reference is deliberately removed.
- no fixed IPs;
- no PostgreSQL/Valkey host ports;
- no real secrets committed.

### M1 acceptance

- Compose renders successfully;
- shared network is explicit;
- ports do not collide with M0 inventory;
- no existing persistent state is destroyed;
- changed files are limited to the approved stack skeleton.

Commit M1 only, then STOP.

## Subsequent module order

1. PostgreSQL/pgvector
2. Valkey
3. Firefly
4. Paperless-ngx
5. OpenProject
6. nginx
7. Hermes
8. Hermes connectors
9. integration + backup/restore

Each module reads only this meta plan plus its own module file and directly owned repository/runtime evidence.
