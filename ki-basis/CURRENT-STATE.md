---
status: superseded
superseded_on: 2026-09-26
superseded_scope: engine/DB architecture & topology
current: "ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md §6 (ADR-002)"
current_bundle: apex-meta/orchestration/architecture-improvements/03-wsl2-native-stack-consolidation/
---

# KI Basis — Current State Snapshot

> **⛔ OUTDATED for engine/DB architecture (2026-09-26).** This snapshot's **"no WSL2 migration"** stance is
> reversed: the stack now targets the **single WSL2-native engine "Apex"** with **one shared PostgreSQL**
> (Docker Desktop being retired). **→ Current source of truth:**
> `C:\GitDev\apexai-os-meta\apex-meta\orchestration\architecture-improvements\03-wsl2-native-stack-consolidation\`
> → **`01-architecture-and-gaps.md`** (live topology + Mermaid) · **`02-decisions-log.md`** (D-01…D-18, incl. incident decisions D-13–D-18) · **`05-handover.md`** (resume).

**Purpose:** compact handover for agents. Read this instead of reconstructing the last implementation rounds from historical plans or chat logs.

## Current architecture (post-consolidation, 2026-09-26)

```text
Windows 11
-> WSL2 (Ubuntu) — single native Docker engine "Apex"  (Docker Desktop retired/uninstalled)
-> two Compose projects on the one engine:
     • ki-basis (private):  valkey, firefly, paperless, nginx, hermes   [compose.shared-db.yaml]
     • community (lika):    its own app services                        [C:\GitDev\lika-community\compose.wsl.yaml]
-> one shared PostgreSQL container on shared-db-net:
     • priv_* databases (private) + comm_* databases (community)
     • cross-stack isolation via per-role grants + REVOKE CONNECT (verified live)
-> private OpenProject = leela-op178-openproject (17.8), a separate compose project
-> Hermes: loopback-only host API, no Docker socket; re-wired to the 17.8 OpenProject
```

Authority for this topology: **`ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6 (ADR-002)** plus the
`03-wsl2-native-stack-consolidation` bundle (decisions D-01…D-18). This snapshot is a pointer, not the source — live runtime evidence outranks it.

## Invariants that still hold

- PostgreSQL and Valkey stay internal-only; Hermes stays loopback-only on the host and never receives the Docker socket.
- Hermes runs the official container path `command: gateway run` (the `sleep infinity` workaround was rejected).
- The retired v14 `ki-basis-openproject` duplicate is **deleted** (D-18) and must not be revived.
- **Do not `docker compose up` on `ki-basis/compose.yaml`** — it drifts from the live hermes bind mounts and a naive up can wipe ~4.4 GB of bot state (D-16). The live private stack runs from **`compose.shared-db.yaml`**.
- The real Paperless/Firefly/OpenProject Hermes skills remain intentionally deferred until the actual skill set is supplied.

## Remaining work

Tracked in the program close-out plan:
`apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md`.

## Just-in-time evidence sources

Read only when the active step needs them:

- live private runtime/config: `ki-basis/compose.shared-db.yaml` (**not** the drifted `compose.yaml`)
- environment template: `ki-basis/.env.example`
- scripts/verifiers: `ki-basis/scripts/`
- architecture decision: `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6 (ADR-002)
- detailed migration record: the `03-wsl2-native-stack-consolidation` bundle

Live local runtime evidence outranks stale reports.
