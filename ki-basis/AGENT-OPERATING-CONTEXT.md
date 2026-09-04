# KI Basis — Agent Operating Context

**Scope:** any task touching `ki-basis/**`, its Docker runtime, Hermes bridge, or the installed KI Basis applications.

**Purpose:** stable safety/architecture context. Current status belongs in `CURRENT-STATE.md`; do not duplicate history here.

## Canonical control path

```text
Operator
-> heavy-reasoning CLI agent
-> authenticated Hermes localhost API
-> Hermes routing/execution
-> real Hermes product skills later
-> Firefly / Paperless / OpenProject
```

The CLI agent is the upstream planner. Hermes is the local routing/execution boundary. Until the real skills arrive, do not build permanent direct product-control logic in Claude/Codex/Antigravity.

## Runtime

```text
Windows 11
-> Docker Desktop background runtime
-> Hyper-V Linux backend
-> one Docker Engine
-> one Compose project: ki-basis
-> one network: ki-basis-net
```

Routine operation is CLI-first; the Dashboard is optional. Preferred laptop mode is on-demand start/stop, not always-on infrastructure.

## Services

| Service | Role | Host access |
|---|---|---|
| `postgres` + pgvector | durable DB substrate | internal only |
| `valkey` | Paperless queue/cache | internal only |
| `firefly` | finance app | `127.0.0.1:8086` |
| `paperless` | document/OCR app | `127.0.0.1:8010` |
| `openproject` | project/work app | `127.0.0.1:8082` |
| `nginx` | local health/entry surface | `127.0.0.1:8084` |
| `hermes` | local AI routing/execution | API `127.0.0.1:8642`, dashboard `127.0.0.1:9119` |

## Start contract

Before mutation:

1. read this file;
2. read `CURRENT-STATE.md` if the task depends on current setup/progress;
3. inspect current Git/runtime state;
4. preserve unrelated dirty work;
5. classify `READ_ONLY` vs `MUTATE`;
6. name the exact target and acceptance evidence;
7. use the smallest supported existing interface;
8. stop at secret/operator/architecture gates instead of inventing workarounds.

## Preferred interfaces

1. existing scripts/verifiers and Compose lifecycle;
2. Hermes localhost API for agent-to-Hermes interaction;
3. supported product APIs through verified skills/tests;
4. product web UI for operator setup/seeding;
5. Docker CLI/Compose only for infrastructure administration.

Direct database mutation is not a substitute for application behavior.

## Secrets

Never print, commit, paste into chat, or write to tracked files:

- `HERMES_API_SERVER_KEY`
- `OPENROUTER_API_KEY`
- product API tokens
- DB/application secrets

Prepare everything else first, then ask the operator for the smallest local action.

## Forbidden shortcuts

Without explicit architecture authorization, do not:

- expose PostgreSQL or Valkey to the host;
- mount `/var/run/docker.sock` into Hermes;
- create another orchestration service;
- build placeholder product skills;
- create separate per-agent product-control implementations;
- bypass app APIs with direct DB writes;
- migrate to WSL2/manual Linux VM;
- tune CPU/RAM/workers/DB/cache speculatively;
- update/uninstall/move the executing CLI agent itself.

## Docker recovery

If Docker hangs after sleep/resume:

1. one `docker desktop status`;
2. one bounded engine probe;
3. if still hung, stop issuing Docker commands;
4. do not edit Compose in reaction;
5. use one supported Docker Desktop restart;
6. retry once;
7. otherwise return `BLOCKED_HUMAN_GATE`.

## Allowed before real skills arrive

Good: start/stop/verify runtime, inspect concrete logs, run backup/stack verifiers, call Hermes with non-sensitive prompts, guide OpenRouter setup, guide manual app smoke tests.

Not yet normal operation: improvised scripts that create Paperless metadata, Firefly transactions, or OpenProject work packages. Those belong to the future real Hermes skills.

## Invocation

```text
Read and obey:
C:\GitDev\apexai-os-meta\ki-basis\AGENT-OPERATING-CONTEXT.md

If current setup/progress matters, also read:
C:\GitDev\apexai-os-meta\ki-basis\CURRENT-STATE.md

Inspect current state first. Do not create alternative product-control logic.
Task: <operator task>
```

If a later accepted architecture decision conflicts with this file, update this file rather than creating a competing KI Basis instruction owner.
