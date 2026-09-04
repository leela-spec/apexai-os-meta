# KI Basis — Agent Operating Context

**Scope:** any nontrivial task touching `ki-basis/**`, its Docker runtime, Hermes bridge, or the installed KI Basis applications.

**Purpose:** stable operating handbook for agents. This file explains what KI Basis is, how it is supposed to be operated, what interfaces are legitimate, and which safety boundaries are locked.

**Not stored here:** current progress, old implementation chronology, or historical debugging detail. Current progress belongs in `CURRENT-STATE.md`. Historical plans remain in the repo for provenance and are opened only when a concrete contradiction requires them.

---

## 1. System objective

KI Basis is a local operator platform, not seven unrelated containers.

The intended long-term control path is:

```text
Operator
-> heavy-reasoning CLI agent
-> authenticated Hermes localhost API
-> Hermes provider-backed routing/execution
-> verified real Hermes product skills
-> Paperless / Firefly / OpenProject
```

The external CLI agent is the upstream planner/reasoner. Hermes is the local routing/execution boundary. Hermes still has its own inference provider.

Until the real product skills are installed, do not normalize direct product-control logic inside Claude, Codex, Antigravity, or ad-hoc helper scripts.

---

## 2. Runtime architecture

```text
Windows 11
-> Docker Desktop background runtime
-> Hyper-V Linux-container backend
-> one Docker Engine
-> one Compose project: ki-basis
-> one Docker network: ki-basis-net
```

Normal operation is CLI-first. Docker Dashboard is optional and should not be required for routine work.

Preferred laptop operating model:

```text
not using KI Basis
-> stack stopped
-> Docker Desktop stopped

need KI Basis
-> start Docker Desktop in background
-> start ki-basis
-> work
-> stop ki-basis gracefully
-> stop Docker Desktop
```

Do not migrate to WSL2 or a manually managed Hyper-V Linux VM unless a later explicit architecture decision authorizes that migration.

---

## 3. Canonical services

| Service | Purpose | Normal host surface | Important boundary |
|---|---|---|---|
| `postgres` + pgvector | durable shared DB substrate | none | internal only |
| `valkey` | Paperless queue/cache dependency | none | internal only |
| `firefly` | finance application | `127.0.0.1:8086` | use supported app behavior, not DB writes |
| `paperless` | document/OCR application | `127.0.0.1:8010` | use supported app behavior, not DB writes |
| `openproject` | project/work application | `127.0.0.1:8082` | use API/UI, not DB writes |
| `nginx` | local health/entry surface | `127.0.0.1:8084` | not the product-control bus |
| `hermes` | local AI routing/execution surface | API `127.0.0.1:8642`, dashboard `127.0.0.1:9119` | loopback-only, no Docker socket |

All seven services belong to `ki-basis-net`.

PostgreSQL and Valkey must remain unexposed to the Windows host.

Hermes must not mount `/var/run/docker.sock` and must not depend on legacy Ubuntu/WSL bind mounts.

---

## 4. Ownership boundaries

### CLI agent owns

- heavy reasoning/planning;
- task decomposition;
- repository/runtime inspection;
- deciding which bounded operation is needed;
- calling Hermes through the generic authenticated bridge;
- infrastructure administration only when explicitly authorized.

### Hermes owns

- local routing/tool-execution layer;
- future product skill selection/execution;
- interaction with supported product APIs once real skills exist.

### Product applications own

- their domain state and validation rules;
- Paperless documents/OCR metadata;
- Firefly finance data;
- OpenProject project/work-package state.

### Docker owns

- process/container lifecycle and network isolation;
- not product semantics.

Do not move responsibilities across these boundaries merely because one path looks easier.

---

## 5. Interfaces to prefer

Use this order unless the task explicitly requires otherwise:

1. existing verified repository scripts/verifiers;
2. Hermes localhost API for agent-to-Hermes interaction;
3. verified real product skill using the supported product API;
4. direct supported product API for bounded verification/debugging when explicitly justified;
5. product web UI for operator setup/seeding;
6. Docker CLI/Compose for infrastructure administration.

Never use direct database mutation as a shortcut for application behavior.

Do not add a new generic orchestration service simply because an agent can write one.

---

## 6. Safe task start

For a nontrivial KI Basis task:

1. read `ki-basis/AGENTS.md` if it was not already supplied by the runtime;
2. read this file;
3. read `CURRENT-STATE.md` only if the task depends on current progress/unfinished setup;
4. inspect current Git branch/HEAD/worktree;
5. inspect only the runtime/config surfaces relevant to the task;
6. classify the task as `READ_ONLY` or `MUTATE`;
7. state the exact target and acceptance evidence;
8. preserve unrelated dirty work;
9. use the smallest supported existing interface;
10. stop at secret/operator/architecture gates instead of inventing workarounds.

For a simple read-only question, do not force this entire procedure if `AGENTS.md` already gives enough context.

---

## 7. Mutation authority

Before a meaningful mutation, establish:

```yaml
mode: READ_ONLY | MUTATE
explicit_goal:
target_repository: leela-spec/apexai-os-meta
target_environment: local Windows KI Basis
allowed_reads:
allowed_mutations:
forbidden_mutations:
operator_decisions_required:
acceptance_evidence:
rollback:
```

Classify proposed actions:

- `EXPLICITLY_AUTHORIZED` -> may execute;
- `NECESSARY_TO_EXECUTE` -> inspect/test only unless mutation is unavoidable and within scope;
- `PLAUSIBLE_OR_USEFUL` -> record/defer;
- `THINK/REVIEW/ANALYZE` -> zero writes;
- material architecture ambiguity -> operator gate.

Do not infer broad execution authority from adjacent repository content.

---

## 8. Secrets and credentials

Never print, commit, paste into chat, or write to tracked files:

- `HERMES_API_SERVER_KEY`;
- `OPENROUTER_API_KEY`;
- Firefly/Paperless/OpenProject API credentials;
- database/application secrets.

Runtime secrets belong in ignored/local supported secret stores.

If a secret or account action is required:

1. prepare everything else first;
2. tell the operator exactly what local action is needed;
3. do not ask the operator to paste the secret into the agent conversation;
4. verify only non-secret state afterward.

---

## 9. Docker lifecycle and recovery

### Normal start

Use the existing lifecycle script if present. Otherwise use supported Docker Desktop + Compose behavior.

Expected sequence:

```text
Docker Desktop background runtime starts
-> Docker Engine ready
-> ki-basis Compose starts
-> dependencies become healthy
-> Hermes/API/app surfaces verified
```

### Normal stop

Gracefully stop the Compose stack before stopping Docker Desktop so PostgreSQL and other stateful services have time to flush cleanly.

Do not delete containers/volumes/images merely to stop the laptop workload.

### Sleep/resume control-plane failure

If Docker hangs after sleep/resume:

1. run one `docker desktop status`;
2. run one bounded engine probe such as `docker ps`;
3. if it hangs/fails, stop issuing more Docker commands;
4. do not edit Compose as a reaction;
5. restart Docker Desktop once through a supported path;
6. retry the same probe once;
7. if still unhealthy, return `BLOCKED_HUMAN_GATE`.

Do not turn a control-plane stall into speculative service reconfiguration.

---

## 10. Performance policy

The stack can be heavy for a laptop. First solve this through on-demand lifecycle behavior and measurement.

Do not pre-emptively change:

- OpenProject worker counts;
- Paperless worker/OCR counts;
- PostgreSQL memory;
- Valkey memory/eviction;
- Docker Desktop VM CPU/RAM allocation;
- per-container CPU/RAM limits;
- image topology.

If performance remains poor while KI Basis is actively needed, gather concrete evidence such as `docker stats --no-stream` and host CPU/RAM/disk symptoms, then open a separate bounded tuning decision.

---

## 11. Product-control boundary before real skills arrive

Allowed now:

- start/stop/verify KI Basis;
- inspect logs for a concrete failure;
- run stack/backup/restore verification;
- call Hermes with non-sensitive prompts;
- configure/verify Hermes provider state without exposing credentials;
- guide manual Paperless/Firefly/OpenProject smoke tests;
- perform explicit bounded API verification when necessary.

Not yet normal operation:

- creating Paperless metadata through improvised agent scripts;
- creating Firefly transactions through improvised agent scripts;
- creating OpenProject work packages through improvised agent scripts;
- building placeholder product skills that will be replaced later.

When the actual skill set arrives, product operations should move behind those verified Hermes skills.

---

## 12. Verification doctrine

Prefer evidence in this order:

```text
actual runtime/product behavior
> independent negative/denial proof
> deterministic script receipt
> config/code inspection
> agent report/prose
```

Examples:

- invalid Hermes API key must fail, valid key must succeed;
- PostgreSQL/Valkey must show no host-published ports;
- Hermes must show no Docker socket mount;
- a product skill must involve the actual product API/runtime, not a local facade;
- a lifecycle change must survive one real start/verify/stop cycle.

Do not treat a self-authored PASS field as proof.

---

## 13. Context routing / what to read when

The repository intentionally keeps history without forcing agents to load it.

| Need | Read |
|---|---|
| Stable KI Basis operating rules | this file |
| Current setup/progress / unfinished gate | `CURRENT-STATE.md` |
| Exact container/runtime configuration | relevant section of `compose.yaml` |
| Exact environment variable names | relevant section of `.env.example` |
| Start/stop/verify behavior | relevant script only |
| Stable architecture diagram/decision | `apex-meta/Alpine/ARCHITEKTUR-BASIS.md` when needed |
| Historical why/how/provenance | old implementation plans only JIT |
| Antigravity method | Antigravity `SKILL.md`; load its references only if the active action requires them |

Do not preload historical plans just because they exist.

---

## 14. Runtime-specific agent adapters

`ki-basis/AGENTS.md` is the scoped cross-agent entrypoint where that convention is supported.

If another runtime needs its own adapter (`CLAUDE.md`, `GEMINI.md`, workspace rule, etc.), the adapter should contain only:

- the few always-on core rules needed by that runtime;
- the trigger telling it when to read this operating context;
- no copied full handbook;
- no separate KI Basis policy.

This prevents drift between local CLI agents.

---

## 15. Future real-skill integration

When the actual product skill set arrives:

```text
CLI agent
-> Hermes API
-> Hermes
-> ki-basis-control (future bundle)
   -> verified Paperless skill
   -> verified Firefly skill
   -> verified OpenProject skill
-> applications
```

At that time:

1. review the supplied skills against current product versions/interfaces;
2. install only the skills actually needed;
3. configure only required product credentials;
4. verify each skill independently with positive + denial proof;
5. create the `ki-basis-control` bundle only over proven real skills;
6. add write workflows only where operator value is clear.

No runtime migration should be needed merely to add the real skills.

---

## 16. Invocation pattern

For an agent runtime that does not automatically discover `AGENTS.md`:

```text
Read and obey:
C:\GitDev\apexai-os-meta\ki-basis\AGENTS.md

This is a KI Basis task.
Follow its context-routing rules instead of loading all KI Basis documentation.

Task: <operator task>
```

For a nontrivial runtime/product task, `AGENTS.md` will route the agent to this file. For a current-status task, it will additionally route to `CURRENT-STATE.md`.

If a later accepted architecture decision conflicts with this handbook, update this file rather than creating a competing KI Basis instruction owner.
