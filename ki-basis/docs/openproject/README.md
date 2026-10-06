---
okf_version: "0.2"
type: index
title: OpenProject (Leela PM) — documentation index & map
description: Index and map of the Leela private OpenProject 17.8 pilot — operating docs, decisions, verification status, future development, and the live project hierarchy.
tags: [openproject, leela, index, map, project-management]
status: current
updated: 2026-09-28
---

# OpenProject (Leela PM) — index & map

The private **OpenProject 17.8** instance is the project-management authority for Leela. It runs on the
WSL2 "Apex" engine as `leela-op178-openproject`, reachable at http://127.0.0.1:8083. Agents operate it
through the **canonical `openproject` skill** — now a single source of truth at **`C:\GitDev\agent-skills\skills\openproject\`**,
linked into every agent's discovery dir (no per-repo copies) — using the API token in the user-level file
**`~/.config/openproject/op.env`** (= `C:\Users\gehma\.config\openproject\op.env`, outside git). See the
canonical-skill decision below.

## Live project hierarchy (verified 2026-09-28)
```
Leela & Mastery              [leela-mastery]        ← master / top-level (one priority stack)
├── Leela                    [leela-cloud-2026]     ← software development
└── PM Infrastructure        [pm-infrastructure]
Scrum project                [your-scrum-project]   ← demo (kept)
Demo project                 [demo-project]         ← demo (kept)
```
Planned but not yet created as their own sub-projects: **Mastery of Arts**, **AI Infrastructure** (see the
taxonomy design work — program task T19). Adding/arranging sub-projects under *Leela & Mastery* is how new
work stays inside the single master so it can be viewed as one priority stack.

## Documents
| Doc | What it's for |
|---|---|
| [AGENT-QUICKSTART.md](AGENT-QUICKSTART.md) | Paste-ready: how any agent (Codex/Antigravity/Claude) operates OpenProject via the skill + API — **not** the browser. |
| [RUNBOOK-openproject-17.8-operations.md](RUNBOOK-openproject-17.8-operations.md) | Operate the instance: start/stop/health, keepalive, memory, backup/recovery, ports, gaps. |
| [DECISION-2026-09-28-pilot-execution-reconciliation.md](DECISION-2026-09-28-pilot-execution-reconciliation.md) | What was actually accepted vs. the handovers (custom API-v3 skill, fresh 17.8, DRAFT executed directly); Phase A–H disposition. |
| [VERIFICATION-2026-09-28-agent-invocation.md](VERIFICATION-2026-09-28-agent-invocation.md) | Skill discovery/wiring status across Antigravity/Codex/Claude; agent-initiated read proof protocol (operator-run). |
| [FUTURE-DEVELOPMENT-least-privilege-agent-identity.md](FUTURE-DEVELOPMENT-least-privilege-agent-identity.md) | Deferred hardening (2 items): (1) scoped non-admin agent identity [T13]; (2) write-autonomy policy [T16]. Revisit when agents run more autonomously. |
| [FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md](FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md) | All 7 work-package types are enabled on every existing project; 4 of them (Feature/Epic/User story/Bug) don't carry forward to future new projects. 3 fix attempts ruled out (API, type-edit tabs, column click); untried next steps listed (project templates, system settings, community docs). |
| [INCIDENT-cache-staleness-work-package-visibility.md](INCIDENT-cache-staleness-work-package-visibility.md) | Open incident: work-package writes (and a type-enablement change) have twice been invisible on read until an OpenProject restart or the next day. Memcache-backed Rails cache with unconfirmed invalidation is the leading suspect; a separate confirmed `shared-db-net` DNS-alias collision (`leela-op178-openproject` / `community-openproject` both aliased `openproject`) was found and flagged as a related latent risk. |
| [DECISION-2026-09-28-canonical-skill-architecture.md](DECISION-2026-09-28-canonical-skill-architecture.md) | Why the skill was consolidated into one canonical repo (`C:\GitDev\agent-skills\`) linked into every agent, token moved to `~/.config/openproject/op.env`. Reasoning + cited research. |

## Handover history (superseded — read as history)
- [openproject-windows-agent-integration-v2/HANDOVER.md](openproject-windows-agent-integration-v2/HANDOVER.md) — operator-accepted target (D1–D6); banner points to the reconciliation decision.
- [openproject-cli-antigravity-pilot/HANDOVER.md](openproject-cli-antigravity-pilot/HANDOVER.md) — research handover; executed directly (see decision record).
- [openproject-cli-antigravity-pilot/DRAFT-IMPLEMENTATION-PLAN.md](openproject-cli-antigravity-pilot/DRAFT-IMPLEMENTATION-PLAN.md) — the executed draft (Phases A–H).
- [openproject-cli-agent-handover/](openproject-cli-agent-handover/) — earlier evidence handover.

## Related (apexai-os-meta)
- Program close-out plan: `apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md`
- Architecture decision ADR-002 (single WSL2 engine + shared Postgres): `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6
