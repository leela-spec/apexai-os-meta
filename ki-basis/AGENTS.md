# KI Basis — Scoped Agent Entrypoint

**Scope:** tasks operating in or on `ki-basis/**`.

**What this file is:** the small always-on agent entrypoint for KI Basis. Runtimes that support hierarchical `AGENTS.md` discovery can load this automatically when working in this directory.

**What this file is not:** it is not the full KI Basis manual, not current project state, and not implementation history.

## Core behavior — applies even if no other file is opened

KI Basis is one local Windows/Docker platform:

```text
heavy-reasoning CLI agent
-> authenticated Hermes localhost API
-> Hermes routing/execution
-> real Hermes product skills later
-> Paperless / Firefly / OpenProject
```

Keep these rules without further lookup:

- inspect live Git/runtime state before mutation;
- preserve unrelated dirty work;
- prefer existing supported interfaces over new glue;
- normal product control belongs behind Hermes + verified real skills;
- do not create parallel per-agent Paperless/Firefly/OpenProject implementations;
- do not use direct DB writes as product behavior;
- PostgreSQL and Valkey stay internal-only;
- Hermes stays loopback-only and gets no Docker socket;
- secrets never enter chat or tracked files;
- do not update/uninstall/move the executing CLI agent as part of a KI Basis task;
- stop at a real secret/operator/architecture gate instead of inventing a workaround.

## Context routing — load only what the task needs

| Task type | Additional context to load |
|---|---|
| Simple repo read/search/explanation | none unless needed; this file is sufficient to start |
| KI Basis runtime, Docker, Hermes, app-boundary, security, or mutation work | `AGENT-OPERATING-CONTEXT.md` |
| Current setup status, unfinished work, next step, or handover | `CURRENT-STATE.md` |
| Current guided operator onboarding run | compact `CURRENT-STATE.md` + `AGENT-OPERATING-CONTEXT.md` + the current compact onboarding walkthrough |
| Exact runtime/config question | inspect only the relevant part of `compose.yaml`, `.env.example`, or script |
| Concrete contradiction/provenance question | historical architecture/implementation plans JIT only; do not preload them |

Do **not** automatically open every file above. Route by the current task.

## Current canonical supporting files

- Stable KI Basis operating handbook: `AGENT-OPERATING-CONTEXT.md`
- Compact mutable handover/status: `CURRENT-STATE.md`
- Runtime truth: `compose.yaml` + actual runtime evidence
- Historical plans: retained for provenance/debugging, not normal context

## Mutation contract

For a meaningful write or runtime mutation, first establish:

```yaml
mode: READ_ONLY | MUTATE
explicit_goal:
target:
allowed_mutations:
forbidden_mutations:
acceptance_evidence:
rollback:
```

Use the smallest scope that satisfies the explicit goal.

## Drift rule

There must be one KI Basis operating doctrine, not one per CLI agent. If an agent runtime needs its own `CLAUDE.md`, `GEMINI.md`, custom rule, or other adapter, keep that adapter thin and point it back to this scoped entrypoint / canonical operating context rather than copying the whole manual.
