---
okf_version: "0.2"
type: index
title: OpenProject (Leela PM) — documentation index & map
description: Index and map of the Leela private OpenProject 17.8 pilot — operating docs, decisions, verification status, future development, and the live project hierarchy.
tags: [openproject, leela, index, map, project-management]
status: current
updated: 2026-10-08
---

# OpenProject (Leela PM) — index & map

The private **OpenProject 17.8** instance is the project-management authority for Leela. It runs on the
WSL2 "Apex" engine as `leela-op178-openproject`, reachable at http://127.0.0.1:8083. Agents operate it
through the **canonical `openproject` skill** — now a single source of truth at **`C:\GitDev\agent-skills\skills\openproject\`**,
linked into every agent's discovery dir (no per-repo copies) — using the API token in the user-level file
**`~/.config/openproject/op.env`** (= `C:\Users\gehma\.config\openproject\op.env`, outside git). See the
canonical-skill decision below.

## Live project hierarchy (verified 2026-10-08 — 11 active projects)
```
Leela & Mastery              [leela-mastery]        ← master / top-level (one priority stack)
├── ApexAI-OS                [apexai-os]            ← AI infrastructure & agent orchestration
├── Leela                    [leela-cloud-2026]     ← software development
│   ├── Path                 [leela-path]
│   ├── Sequencing           [leela-sequencing]
│   └── Skill Tree           [leela-skill-tree]
├── MoA-Business             [moa-business]         ← Mastery of Arts (business)
├── MoA-Content              [moa-content]          ← Mastery of Arts (content)
└── PM Infrastructure        [pm-infrastructure]
Scrum project                [your-scrum-project]   ← demo (kept)
Demo project                 [demo-project]         ← demo (kept)
```
Adding/arranging sub-projects under *Leela & Mastery* keeps work inside the single master so it can be viewed as one priority stack. All 7 work-package types (`Task`, `Milestone`, `Summary task`, `Feature`, `Epic`, `User story`, `Bug`) are enabled across all 11 projects and marked `is_default: true` for future new projects.

## Documents
| Doc | What it's for |
|---|---|
| [AGENT-QUICKSTART.md](AGENT-QUICKSTART.md) | Paste-ready: how any agent (Codex/Antigravity/Claude) operates OpenProject via the skill + API — **not** the browser. |
| [RUNBOOK-openproject-17.8-operations.md](RUNBOOK-openproject-17.8-operations.md) | Operate the instance: start/stop/health, TCP memcached flush (`127.0.0.1:11211`), Option 2A memory tuning (`WEB_WORKERS=0`, `USE_JEMALLOC=true`, `MALLOC_CONF`, disabled `hocuspocus` → `~1.13 GiB` anon heap under `1536M`), backup/recovery, ports, landmines. |
| [DECISION-2026-09-28-pilot-execution-reconciliation.md](DECISION-2026-09-28-pilot-execution-reconciliation.md) | What was actually accepted vs. the handovers (custom API-v3 skill, fresh 17.8, DRAFT executed directly); Phase A–H disposition. |
| [VERIFICATION-2026-09-28-agent-invocation.md](VERIFICATION-2026-09-28-agent-invocation.md) | Skill discovery/wiring status across Antigravity/Codex/Claude; agent-initiated read proof protocol (operator-run). |
| [FUTURE-DEVELOPMENT-least-privilege-agent-identity.md](FUTURE-DEVELOPMENT-least-privilege-agent-identity.md) | Deferred hardening (2 items): (1) scoped non-admin agent identity [T13]; (2) write-autonomy policy [T16]. Revisit when agents run more autonomously. |
| [FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md](FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md) | **Mitigated (2026-10-08):** All 7 work-package types now have `is_default: true` in `priv_openproject` via `WorkPackageTypes::MakeDefaultService` (verified on newly created projects `leela-skill-tree` and `leela-sequencing`). Upstream OpenProject 17.8.0 admin UI remains gated behind the disabled `type_variants` feature flag. |
| [INCIDENT-cache-staleness-work-package-visibility.md](INCIDENT-cache-staleness-work-package-visibility.md) | **Mitigated (2026-10-08):** Root cause verified in OpenProject 17.8.0 (`ProjectType` omits `touch: true` on `belongs_to :project`, leaving `projects.updated_at` and memcache keys stale). Mitigated via 0-downtime TCP `memcached` flush (`127.0.0.1:11211`). Separate `shared-db-net` DNS-alias collision permanently resolved (`leela-openproject` service key). |
| [INCIDENT-wsl2-cold-boot-and-keepalive-fragility.md](INCIDENT-wsl2-cold-boot-and-keepalive-fragility.md) | **Open (To be checked to resolve — 2026-10-20):** Intermittent 503 / socket hangup caused by Windows shutting down idle WSL2 VM when host keepalive (`wsl-keepalive.vbs`) silently died. Subsequent cold boots trigger a 30-45s Puma warmup window where incoming agent requests fail with 503. |
| [DECISION-2026-09-28-canonical-skill-architecture.md](DECISION-2026-09-28-canonical-skill-architecture.md) | Why the skill was consolidated into one canonical repo (`C:\GitDev\agent-skills\`) linked into every agent, token moved to `~/.config/openproject/op.env`. Reasoning + cited research. |

## Handover history (superseded — read as history)
- [openproject-windows-agent-integration-v2/HANDOVER.md](openproject-windows-agent-integration-v2/HANDOVER.md) — operator-accepted target (D1–D6); banner points to the reconciliation decision.
- [openproject-cli-antigravity-pilot/HANDOVER.md](openproject-cli-antigravity-pilot/HANDOVER.md) — research handover; executed directly (see decision record).
- [openproject-cli-antigravity-pilot/DRAFT-IMPLEMENTATION-PLAN.md](openproject-cli-antigravity-pilot/DRAFT-IMPLEMENTATION-PLAN.md) — the executed draft (Phases A–H).
- [openproject-cli-agent-handover/](openproject-cli-agent-handover/) — earlier evidence handover.

## Related (apexai-os-meta)
- Live infrastructure single source of truth: `ki-basis/docs/INFRASTRUCTURE.md` (§4.2 & §4.3)
- Deep-dive memory & 17.8 findings (2026-10-08): `apex-meta/orchestration/architecture-improvements/05-program-closeout/FINDINGS-openproject-memory-and-178-inefficiencies-2026-10-08.md`
- Program close-out plan: `apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md`
- Architecture decision ADR-002 (single WSL2 engine + shared Postgres): `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6
