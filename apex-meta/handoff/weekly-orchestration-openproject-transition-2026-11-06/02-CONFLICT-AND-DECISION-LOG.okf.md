---
okf_version: "0.2"
type: decision-and-conflict-log
id: WEEKLY-OP-LOG-2026-11-06
date: 2026-11-06
status: evidence_reconciled_candidate
decision_ref: 01-DECISION-OPENPROJECT-WEEKLY-ORCHESTRATION.okf.md
evidence_scope: github_repository_sources_only
live_openproject_api_verified: false
---

# Weekly Orchestration: authority and migration log

## Decision timeline

| Date | Source / event | Disposition for new Weekly |
|---|---|---|
| 2026-07-11 | [APEX orchestration index](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md): separate Weekly, Multi-Agent and Plan-Sync-Session | Preserve separation unless deliberately redesigned |
| 2026-08-24 | [Hermes D02](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions/D02-KANBAN-TOPOLOGY.md): four isolated Kanban boards and asynchronous deterministic rollup | Historical accepted Hermes architecture, NOT automatically the new Weekly PM authority |
| 2026-08-25/26 | Reported in conversation: stale shadow v1 and unsuccessful live Kanban v2, no G2 signoff | Negative evidence; not proof of a functional live frontier |
| 2026-09-26/28 | [WSL infra](https://github.com/leela-spec/apexai-os-meta/blob/main/ki-basis/docs/INFRASTRUCTURE.md) and [canonical OpenProject skill decision](https://github.com/leela-spec/apexai-os-meta/blob/main/ki-basis/docs/openproject/DECISION-2026-09-28-canonical-skill-architecture.md) | Later accepted infrastructure and cross-agent API route |
| 2026-09-27/28 | [OpenProject consolidation](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/orchestration/architecture-improvements/04-leela-mastery-openproject-consolidation/index.md): Leela work-package import and MoA/Apex project containers | Confirmed for that date, not proof of universal repo migration |
| 2026-10-08 | [OpenProject index](https://github.com/leela-spec/apexai-os-meta/blob/main/ki-basis/docs/openproject/README.md): private instance, project tree | Recheck live data when running new Weekly |
| 2026-11-06 | [Leela AGENTS](https://github.com/leela-spec/Leela-Cloud-2026/blob/master/AGENTS.md): OpenProject owns current work, materialization build state, tests verification, SSOT product facts | Current high authority for Leela PM |
| 2026-11-06 | Operator initiates OpenProject-based Weekly redesign | New user direction; no automatic existing-file mutation |

## Conflict register

| ID | Existing authority | Conflict | Proposed resolution | Status |
|---|---|---|---|---|
| C01 | [Weekly Orchestrator](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/skills/weekly-orchestrator/SKILL.md) sends confirmed project/task mutation through Apex Session | OpenProject-owned work may be mutated in a second Apex graph | OpenProject WP updates via existing gated OpenProject skill; Apex Session only Apex-native state | PROPOSED_NOT_PATCHED |
| C02 | [PrecapWeek](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/skills/PrecapWeek/SKILL.md) prefers Apex Session/Sync for current project input | Enrolled WPs may be absent or stale | Current OpenProject WP frontier first for enrolled projects; preserve separate authorities | PROPOSED_NOT_PATCHED |
| C03 | [StatusMerge](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/skills/status-merge/SKILL.md) proposes an Apex Session mutation | Wrong write-target for OpenProject work | Route proposals by ownership to OpenProject or Apex Session | PROPOSED_NOT_PATCHED |
| C04 | [Apex Sync](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/skills/apex-sync/SKILL.md) computes status and dependencies from Apex epic task files | OpenProject has its own WP hierarchy and dependencies | Keep Apex Sync Apex-native; never silently mirror OP objects | PROPOSED_NOT_PATCHED |
| C05 | [ProjectStatus](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/skills/ProjectStatus/SKILL.md) builds compact ratings | Potential duplicate of OpenProject state | Measure unique value; optional presentation only if useful | DEFERRED |
| C06 | [Hermes D02](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions/D02-KANBAN-TOPOLOGY.md) board lifecycle | OpenProject migration changes PM boundaries | D02 remains Hermes scoped; no automatic cross-sync | HISTORICAL_SCOPE |
| C07 | [MasterOfArts AGENTS](https://github.com/leela-spec/MasterOfArts/blob/main/AGENTS.md) says Hermes Kanban manages task/review cycles and OP skill handles OP PM | Hybrid ownership not resolved | Clarify durable OP commitments vs ephemeral Hermes execution queue through real examples | OPEN |
| C08 | [Investment AGENTS](https://github.com/leela-spec/Investment/blob/main/AGENTS.md) references OP skill and repo-local orchestration | WP migration scope unverified | Confirm live OP enrollment before declaring it primary | OPEN |
| C09 | [ACIM AGENTS](https://github.com/leela-spec/acim-secular/blob/master/AGENTS.md) owns roadmap in docs/product | OP inclusion unverified | Preserve repo-local roadmap until explicitly enrolled | OPEN |
| C10 | [Apex router](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/CLAUDE.md) owns Apex tasks via Session/Sync; OpenProject has ApexAI-OS container | Potential dual task state | Separate Git architectural decisions from actual enrolled OP WPs, reconcile before migration | OPEN |
| C11 | [Old WF01](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/orchestration/new_final_v4/workflow_plans/WF01_WEEKLY_META_ORCHESTRATION.md) is a Hermes-driven infra health sweep | Name looks like operator weekly planning; old Docker Desktop assumptions | Classify WF01 as distinct historical infra workflow, not new Weekly spec | CLASSIFIED |
| C12 | Prior prompts tried Docker-terminal Hermes CLI and then unavailable native kanban_list | Wrong execution/tool context | Stop treating Weekly as a Hermes Kanban client; use independent OP skill or bounded data export | CORRECTED |
| C13 | Prior suggestion: 5-minute Kanban rollup + runtime Frontier | Adds unused legacy infra after OP switch | Reject as default; first test on-demand read-only OP queries | REJECTED_DEFAULT |
| C14 | [OpenProject write policy](https://github.com/leela-spec/agent-skills/blob/master/skills/openproject/references/write-policy.md) requires approval; admin token remains | Autonomous Weekly updates not authorized | Per-action preview, operator confirmation, reread; least-privilege and autonomy separate decisions | OPEN |
| C15 | [OpenProject cold boot incident](https://github.com/leela-spec/apexai-os-meta/blob/main/ki-basis/docs/openproject/INCIDENT-wsl2-cold-boot-and-keepalive-fragility.md) | Failure may look like empty work queue | Distinguish unavailable from empty, stale from current | OPEN |

## Project coverage: repository evidence, not live API read

| Project | Authority finding | Current interpretation |
|---|---|---|
| Leela | OpenProject owns current work (AGENTS.md) | CONFIRMED_FOR_PM |
| MasterOfArts | Hermes execution Kanban + canonical OP skill explicitly documented | HYBRID_UNRESOLVED |
| Investment | OpenProject skill discoverable; repo state/plan still local | ENROLLMENT_UNVERIFIED |
| acim-secular | Product roadmap in docs/product; no asserted OP migration | REPO_LOCAL |
| ApexAI-OS | OP project container exists; Apex task graph still implemented | MIGRATION_SCOPE_UNVERIFIED |

## New Weekly design continuation

1. Verify live private OpenProject identity and current project coverage using the canonical skill (read-only).
2. Decide source-of-truth matrix: work commitment and status (OpenProject only for enrolled work); code/build/product evidence (source repo); Apex strategy and control-plane decisions (Apex); calendar constraints (calendar).
3. Define minimal read-only WP frontier with source IDs, statuses, priorities, dependency readiness and freshness; paginate rather than assuming a truncated list is complete.
4. Generate a real operator-facing weekly plan, next-day plan, task-specific prompts and flow cards.
5. Test operator review, task execution evidence, and separately approved OP writeback (preview, confirmed, reread).
6. Only after measured success propose exact-context patches to Weekly and stage owners. Do not patch existing contracts in this recording step.
7. Preserve Hermes Kanban for any still-active execution queue; never mirror all OP WPs into Hermes or Apex task files.

## Verification boundary

- GitHub current repo contents reviewed on 2026-11-06, commits recorded in Decision 01.
- The private OpenProject live API, local Hermes runtime, and old uncommitted shadow evidence were not directly inspected in this chat.
- The 2026-08-26 Wednesday plan is historical only; no present-day G2 status is claimed.
- This is an operator-reviewable transition candidate, NOT an automatic overwrite of existing accepted source contracts.
