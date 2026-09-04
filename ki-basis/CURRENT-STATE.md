# KI Basis — Current State Snapshot

**Purpose:** compact handover for agents. Read this instead of reconstructing the last implementation rounds from historical plans or chat logs.

## Current target

```text
Windows 11
-> Docker Desktop background runtime (Hyper-V Linux backend)
-> one Docker Engine
-> one Compose project: ki-basis
-> seven services on ki-basis-net

heavy-reasoning CLI agent
-> authenticated Hermes localhost API
-> Hermes provider-backed routing/execution
-> real Hermes product skills later
-> Paperless / Firefly / OpenProject
```

## What is already established

- Seven-service stack exists: `postgres`, `valkey`, `firefly`, `paperless`, `openproject`, `nginx`, `hermes`.
- PostgreSQL and Valkey stay internal-only.
- Hermes must remain loopback-only on the host and must not receive the Docker socket.
- Backup/restore/auth/isolation hardening has already been exercised; do not reopen it without a concrete failure.
- Hermes official container path `command: gateway run` was verified; the temporary manual `sleep infinity` workaround was rejected.
- A transient WMI detachment was used once to survive an executor Job Object. It did not become persistent architecture and must not be recreated as a service/task/startup mechanism.
- Docker Dashboard is not required for normal operation.
- The real Paperless/Firefly/OpenProject Hermes skills are intentionally deferred until the actual skill set is supplied.

## Current unfinished items

1. **Git reconciliation first.** A local bridge commit was previously reported (`b336aca1...`), while remote `main` advanced independently. Inspect actual local/remote state; preserve both; never assume the old SHA is still current.
2. **OpenRouter:** intended Hermes provider, but operator still needs to enter the private key interactively and then verify provider/model + one non-sensitive Hermes API call.
3. **Laptop operating mode:** always-on KI Basis materially hurts responsiveness. Preferred target is on-demand start/stop. Measure once, test full graceful shutdown, then disable Docker sign-in autostart if the improvement is real. Do not tune individual services first.
4. **Agent orientation:** local CLI agents need the canonical `ki-basis/AGENT-OPERATING-CONTEXT.md`, not separate per-agent KI Basis manuals.
5. **Manual application fixtures:** add tiny harmless test objects in Paperless, Firefly and OpenProject through their normal UIs so the future real skills have known objects to verify against.

## Do not revisit now unless evidence forces it

- no WSL2 migration;
- no manual Hyper-V Linux VM migration;
- no Docker socket in Hermes;
- no direct DB product control;
- no placeholder product skills;
- no `ki-basis-control` until real skills exist;
- no speculative OpenProject/Paperless worker tuning;
- no PostgreSQL/Valkey tuning;
- no Docker VM CPU/RAM tuning without measurements;
- no executor self-update/uninstall/move inside a KI Basis task.

## Current next-step order

```text
0. reconcile local/remote Git safely
1. configure + prove OpenRouter in Hermes
2. establish on-demand Docker/KI Basis lifecycle
3. prove one CLI agent consumes the canonical operating context
4. manually seed/test Paperless, Firefly, OpenProject
5. run bounded acceptance and stop
```

## Just-in-time evidence sources

Read only when the active step needs them:

- runtime topology/config: `ki-basis/compose.yaml`
- environment template: `ki-basis/.env.example`
- scripts/verifiers: `ki-basis/scripts/`
- stable architecture reference: `apex-meta/Alpine/ARCHITEKTUR-BASIS.md`
- detailed historical implementation plans: **do not preload**; open only to resolve a concrete contradiction.

Live local runtime evidence outranks stale reports.
