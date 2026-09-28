---
type: Open Questions
title: Open questions (Q&A) — WSL2-native consolidation
description: Operator questions for the consolidation; the blocking ones were answered 2026-09-26 and are recorded here.
tags: [questions, decisions, docker, wsl2, postgres, isolation]
status: draft
generated: { by: "claude/opus-4.8", at: "2026-09-26" }
stale_after: "2026-10-31"
sources:
  - id: decisions
    resource: /02-decisions-log.md
    title: Decision ledger
  - id: plan
    resource: /03-execution-plan.md
    title: Execution plan
---

# Open questions (Q&A)

> Format note: the format you intended didn't come through (message ended at "in the following
> format"). Using a clear fill-in shape — tell me if you want a different one. **Answers recorded
> 2026-09-26; the core decisions are settled — see the [ledger](02-decisions-log.md) D-07…D-10.**

## Q1 — Shared PostgreSQL vs isolation model (BLOCKING)
**Question:** One shared PostgreSQL for both stacks (separate DBs), accepting it breaks "airtight isolation"?
**Recommendation:** Per-stack Postgres on one engine.
**Answer (2026-09-26):** **One shared PostgreSQL** for both stacks (separate databases + roles).
Operator accepted the coupled failure domain; data isolation preserved via per-role `REVOKE CONNECT`.
→ D-07. Action: supersede the "zero shared DBs" clause in the architecture doc.

## Q2 — What does "stop running 172.18.0.0 containers" mean? (BLOCKING)
**Question:** Which containers to stop (172.18 = running private on WSL, and empty duplicate on Docker Desktop)?
**Answer (2026-09-26):** Reframed by operator — *move all content to WSL2-native docker and remove
docker from Docker Desktop's VM.* So the "stop/remove" target is the **Docker Desktop side** (community
migrates off it, then Docker Desktop is uninstalled). The private `172.18` stack on WSL2 is only stopped
when deliberately reconfigured onto the shared Postgres. → D-09.

## Q3 — "Later remove the docker engine from Linux/Ubuntu" — what exactly? (BLOCKING)
**Question:** Retire Docker Desktop (keep WSL2 native) or move off WSL2 entirely?
**Answer (2026-09-26):** **Retire Docker Desktop, keep WSL2 Ubuntu native dockerd.** "The linux vm" =
Docker Desktop's LinuxKit VM (uninstall it). Ubuntu WSL2 + its native docker remain the sole engine.
→ D-09.

## Q4 — Preserve community data, or start fresh?
**Answer (2026-09-26):** **Preserve** — back up and restore the community databases + volumes. → D-10.

## Q5 — Private OpenProject on the shared DB: 17.8 or v14?
**Answer (2026-09-26):** **17.8 (`leela-op178`) is authoritative**; migrate it onto the shared cluster.
v14 stays retired, not revived. → D-10.

## Q6 — Re-wire Hermes to OpenProject?
**Answer (2026-09-26):** **Yes** — re-wire private Hermes to the 17.8 instance (restores the capability
the v14 retirement broke). → D-10.

## Q7 — WSL2 memory ceiling for two stacks + shared Postgres?
**Answer (2026-09-26):** **Raise 12 → 16 GB** with `autoMemoryReclaim=gradual` (ceiling, not
reservation); tune from live metrics. → D-10.

## Q8 — Update the authoritative records after ratification?
**Answer (2026-09-26):** **Yes** — write a superseding ADR in `apexai-os-meta` capturing the single
WSL2-engine choice and the shared-Postgres isolation decision. → D-10 (pending).

## Still to decide during execution (non-blocking)
- Exact per-role `CONNECTION LIMIT` and `max_connections`/`shared_buffers` values — tune from live
  `pg_stat_activity` (starting points in the [execution plan](03-execution-plan.md) Phase 1).
- **[UNVERIFIED]** whether OpenProject's DB role needs specific extensions (e.g. `pg_trgm`) created by
  a superuser at restore — confirm against the running schema; do not grant a shared-cluster superuser.
