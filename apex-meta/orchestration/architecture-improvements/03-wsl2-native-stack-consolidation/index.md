---
okf_version: "0.2"
---

# WSL2-Native Stack Consolidation (03)

Consolidate the **private (ki-basis)** and **community (lika-community)** Docker stacks onto a
single **WSL2-native Docker engine ("Apex")**, run both against **one shared PostgreSQL container
with separate databases**, and retire **Docker Desktop**. This bundle preserves the verified
current-state analysis, the decision ledger, the migration runbook, and the open operator questions,
so any agent or human can resume the work without chat history.

* [Architecture & Gaps](01-architecture-and-gaps.md) — verified current-state topology (engines, containers, ports, networks, databases, repos, VMs) plus the gaps and risks found.
* [Decisions Log](02-decisions-log.md) — accepted and proposed architecture decisions, with the isolation tension surfaced (ledger).
* [Execution Plan](03-execution-plan.md) — detailed, safely-ordered migration runbook (backup → shared Postgres → restore → cut over → retire Docker Desktop) with rollback points and exact commands.
* [Open Questions (Q&A)](04-open-questions.md) — operator questions that must be resolved before or during execution.
* [Continuation Handover](05-handover.md) — how another chat/agent resumes from the current state, with references, context rules, and safety boundaries.
* [Change log](log.md) — dated history for this bundle.

**Status: EXECUTED — runbook Phases 0–9 complete as of 2026-09-26.** Both stacks (private + community)
run on the single WSL2-native "Apex" engine against one shared PostgreSQL (`comm_*`/`priv_*` DBs,
isolation proven live). Docker Desktop is uninstalled. See [log.md](log.md) for the full execution
narrative and [02-decisions-log](02-decisions-log.md) D-13…D-17 for incidents hit and fixed along the
way — read those before making further changes to either stack. Remaining items are non-blocking
tuning/documentation follow-ups, tracked in [05-handover](05-handover.md) under "Still open".
