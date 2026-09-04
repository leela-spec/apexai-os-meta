# KI Basis — Agent Operating Context

**Scope:** all work that touches `ki-basis/**`, its local Docker runtime, Hermes bridge, or the installed KI Basis applications.

**Purpose:** give any local CLI/agent enough context to operate the stack safely without creating a second architecture or rediscovering prior decisions.

## 1. Canonical operating model

KI Basis is a local Windows platform, not a collection of unrelated containers.

```text
Operator
  -> heavy-reasoning CLI agent
  -> authenticated Hermes localhost API
  -> Hermes provider-backed routing/tool execution
  -> real Hermes product skills (installed later)
  -> Firefly / Paperless / OpenProject
```

The CLI agent is the upstream planner/reasoner. Hermes is the local routing/execution plane. The CLI agent does **not** replace Hermes' own inference provider.

Until the real product skills arrive, direct product APIs are allowed only for verification/debugging or an explicitly authorized bounded test. Do not build a parallel permanent product-control implementation in Claude/Codex/Antigravity scripts.

## 2. Runtime architecture

```text
Windows 11
  -> Docker Desktop background runtime
  -> Hyper-V Linux-container backend
  -> one Docker Engine
  -> one Compose project: ki-basis
  -> one network: ki-basis-net
```

Routine operation is CLI-first. The Docker Dashboard is not required for normal operation.

Target laptop operating mode after onboarding:

- Docker/KI Basis **off when not needed**;
- start the stack explicitly for work;
- stop it gracefully afterward;
- Docker Desktop sign-in autostart disabled unless the operator later chooses otherwise;
- Dashboard autostart disabled;
- no speculative CPU/RAM/worker/database tuning without measurements.

A true no-Docker-Desktop Linux Engine would require another Linux-VM migration and is **not** authorized by this context.

## 3. Services and responsibilities

| Service | Role | Host access |
|---|---|---|
| `postgres` + pgvector | shared durable DB substrate | internal only `postgres:5432` |
| `valkey` | Paperless queue/cache dependency | internal only `valkey:6379` |
| `firefly` | finance application | `127.0.0.1:8086` |
| `paperless` | document/OCR application | `127.0.0.1:8010` |
| `openproject` | project/work application | `127.0.0.1:8082` |
| `nginx` | local entry/health surface | `127.0.0.1:8084` |
| `hermes` | local AI routing/execution surface | API `127.0.0.1:8642`, dashboard `127.0.0.1:9119` |

All seven services belong to `ki-basis-net`.

PostgreSQL and Valkey must remain unexposed to the Windows host.

Hermes must not receive `/var/run/docker.sock` and must not depend on legacy Ubuntu WSL bind mounts.

## 4. Current capability boundary

Current phase:

- platform migration complete;
- backup/restore/auth hardening complete;
- Hermes machine-to-machine bridge implemented/proven locally;
- OpenRouter/provider setup and final bridge synchronization may still need operator completion depending on current local state;
- final Firefly/Paperless/OpenProject Hermes skills are intentionally **not** installed yet;
- `ki-basis-control` is intentionally deferred until those real skills exist.

Do not treat missing final skills as a reason to invent substitutes.

## 5. Agent start contract

Before meaningful KI Basis work, an agent must:

1. read this file;
2. inspect current Git branch/HEAD/worktree and preserve unrelated dirty files;
3. inspect current runtime state before changing it;
4. classify the task as `READ_ONLY` or `MUTATE`;
5. name the exact target and acceptance evidence;
6. use the smallest existing supported interface that satisfies the task;
7. stop at an operator/secret/architecture gate rather than inventing a workaround.

For nontrivial Antigravity runs, also read:

- `apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/SKILL.md`
- its `references/lessons-learned.md`
- its `references/prompt-patterns.md`

## 6. Safe interfaces

Preferred order:

1. existing repository scripts and verified Compose lifecycle;
2. Hermes localhost API for machine-to-machine agent interaction;
3. supported product application APIs when required by a verified skill/test;
4. product web UI for operator setup/seeding when that is simpler and safer;
5. Docker CLI/Compose only for infrastructure administration.

Do not use direct database mutation as a substitute for supported application behavior.

## 7. Secrets

Never print, commit, paste into chat, or write into tracked files:

- `HERMES_API_SERVER_KEY`
- `OPENROUTER_API_KEY`
- Firefly/Paperless/OpenProject API credentials
- database/application secrets

Runtime secrets belong only in ignored/local supported secret stores.

If a secret or account action is required, prepare everything else and request the smallest exact operator action.

## 8. Forbidden shortcuts

Without explicit architecture authorization, do **not**:

- add Docker socket access to Hermes;
- publish PostgreSQL or Valkey host ports;
- create a second generic orchestration service;
- bypass product APIs with direct DB writes;
- build placeholder product skills that will be replaced later;
- create separate product-control implementations per CLI agent;
- migrate to WSL2 or a manual Hyper-V Linux VM;
- modify `.wslconfig`;
- add speculative memory/CPU limits or worker/database/cache tuning;
- upgrade OpenProject merely for MCP;
- add sync daemons/new mounts merely for convenience;
- update/uninstall/move the executing CLI agent itself as part of a KI Basis task.

## 9. Docker control-plane recovery

If Docker CLI/control-plane calls hang after sleep/resume:

1. run one `docker desktop status`;
2. run one bounded engine probe such as `docker ps`;
3. if it hangs/fails, stop issuing Docker commands;
4. do not edit Compose as a reaction;
5. use one supported Docker Desktop restart;
6. retry once;
7. if still unhealthy, return `BLOCKED_HUMAN_GATE`.

## 10. What agents may do before real skills arrive

Allowed examples:

- inspect/start/stop/verify the KI Basis runtime;
- inspect logs for a concrete failure;
- run backup/restore/stack verification scripts;
- call the authenticated Hermes bridge with non-sensitive prompts;
- help the operator configure OpenRouter locally without seeing the key;
- guide manual application smoke tests and seed data;
- modify repository configuration when explicitly authorized and independently verified.

Not yet the default:

- create Paperless documents/tags through improvised agent API code;
- create Firefly transactions through improvised agent API code;
- create OpenProject work packages through improvised agent API code.

Those become normal agent operations only after the real Hermes skills are installed and verified.

## 11. Invocation pattern

For any local CLI agent, the operator can start with:

```text
Read and obey:
C:\GitDev\apexai-os-meta\ki-basis\AGENT-OPERATING-CONTEXT.md

Treat it as the canonical KI Basis operating context for this task.
Do not create alternative product-control logic.
First inspect current state and tell me the exact safe next step.

Task: <operator task>
```

For the guided onboarding/setup run, use:

`apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/ANTIGRAVITY-OPERATOR-ONBOARDING-LAUNCHER.md`

## 12. Authority and drift rule

Runtime truth comes from the current local `ki-basis/compose.yaml`, actual runtime evidence, and the accepted architecture documents—not from stale chat history.

If this context conflicts with a later explicit architecture decision, update this file rather than creating another competing KI Basis instruction owner.
