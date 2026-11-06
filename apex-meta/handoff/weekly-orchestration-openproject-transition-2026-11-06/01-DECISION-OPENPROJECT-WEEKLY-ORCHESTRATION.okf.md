---
okf_version: "0.2"
type: architecture-decision-candidate
id: WEEKLY-OP-TRANSITION-2026-11-06
title: "Weekly Orchestration redesign — OpenProject state authority reconciliation"
date: 2026-11-06
status: candidate_for_operator_acceptance
repository: leela-spec/apexai-os-meta
branch: main
scope: cross_repository_weekly_orchestration
operator_direction_observed: "OpenProject has replaced Hermes-based project management as the intended Weekly planning source."
mutation_scope: "new decision and reconciliation records only; no existing production contracts modified"
related_log: "02-CONFLICT-AND-DECISION-LOG.okf.md"
repo_revisions_checked:
  apexai_os_meta: a6792617428f74ed715b49ab74dfbdf6a17bf45b
  leela_cloud_2026: fa3aacf0eb4ea8bea85062b73a89438a218c430c
  masterofarts: 78827660460d23da39001877ee1eef2f5eca594a
  investment: b83b23d87b18f4f22ea634f7ddebe71de0c332b0
  acim_secular: 96d13268bd2765da7cb59fd60447b46af849a0df
  agent_skills: 451cc1c92475aa9d1b528b8cc1f1ca9c9fdcc813
verification_boundary: "GitHub repository evidence only; no private OpenProject live API or local runtime queried"
---

# Decision candidate: new Weekly Orchestration with OpenProject

## Decision classification

| Claim | Classification | Consequence |
|---|---|---|
| Leela current execution/work commitment is in OpenProject | CONFIRMED_REPO_CONTRACT | Use OpenProject for Leela PM, not Apex task-file mirrors or old Hermes board rollups |
| Private OpenProject 17.8 and Leela & Mastery hierarchy existed | VERIFIED_IN_REPO_AS_OF_2026-10-08 | Treat as historical verified topology; refresh live state at each run |
| OpenProject has fully replaced PM for every repo | NOT_VERIFIED | Do not automatically suppress repo-local authority or import every project |
| New Weekly intake should prefer OpenProject for enrolled work | RECOMMENDATION | Operator confirmation and live trial required |
| Existing Weekly and Apex skills have already been migrated | FALSE | Existing published contracts still use Apex Session/Sync |
| Previous Hermes file-frontier bridge is current | NOT_ADOPTED | Keep as historical candidate, not as a design prerequisite |

## Proposed decision

1. **System ownership:** Define the redesigned Weekly Orchestration in leela-spec/apexai-os-meta, under the existing Weekly-specific domain. Do not place its normative contract in apex-meta/orchestration/, which the live index assigns to the separate Multi-Agent Orchestration system. Preserve the existing Weekly skill as the current implemented contract until a gated redesign supersedes it. A new design may use apex-meta/kb/Weekly-Orchestrator/ for supporting decisions; runtime entrypoint should be explicitly chosen and indexed rather than created by implication.
2. **Portfolio PM authority:** Use the private OpenProject instance and its live work packages as the preferred authority for current commitments, work statuses, assignees, dependencies, and priorities for **projects actually enrolled there**. Resolve project identifiers through the API, never assume all four historical repos have migrated.
3. **Other authorities remain distinct:** Git/repo-specific accepted decisions own code, design/product facts and artifacts. Leela's authored materialization ledger owns build-existence state; tests own verification. OpenProject cannot override these. Apex-native cross-project decisions and architecture records remain in Apex, without duplicating work packages.
4. **Hermes role:** Hermes may remain an execution agent or maintain transient executor/dispatcher queues when actually used. Its per-repo Kanban boards and August D02 rollup are not a universal PM source for the redesigned Weekly loop. Do not delete or automatically synchronize them.
5. **Read interface:** Prefer the canonical cross-agent OpenProject skill at leela-spec/agent-skills/skills/openproject/ (portable API v3 client). At planning start, perform a read-only identity/health check, enumerate current projects, then retrieve a bounded work-package frontier with pagination, status, dependencies, updated timestamp when exposed, and stable source IDs. Load details only for selected candidates.
6. **Access fallback:** If the particular planning runtime cannot use the canonical skill, allow an authorized deterministic **read-only** exporter to produce a small portable snapshot. This is a data transport fallback, not a new state authority. Do not require Hermes native toolsets, Docker host mounts, direct SQLite, a five-minute scheduler, or a new MCP bridge without demonstrated need.
7. **Stage outputs:** Preserve useful operator jobs from the prior Weekly work—weekly direction, day selection, concrete executable Flow Cards and prompts, real evidence, reconciliation, operator decisions. Whether to retain the exact G1–G5 sequence, stage names, and subagent topology is a redesign decision, not automatically accepted.
8. **Closure/write authority:** For an OpenProject-owned work package, propose status/evidence mutations against that same OpenProject work package using the existing per-action operator confirmation, current lockVersion and post-write reread. Apex Session is used only for genuinely Apex-owned records. Never route OpenProject task mutation into an Apex task-file duplicate or silently claim it is done.
9. **Failure/freshness:** The private OpenProject instance may be unavailable during a WSL cold start. Failure, stale data, absent pagination, missing project coverage, or unresolved task-vs-repo conflict must be surfaced. A last-known-good snapshot is historical evidence, not current truth.
10. **Evaluation:** Test on a real upcoming week and at least one real next-day package. The evaluator must ask operator-job questions against the artifact and observed use; no self-awarded quality scores, fabricated timers, schema-string quality proxies, or PASS merely because files were generated.

## Proposed minimal information path

- OpenProject API via canonical skill → read-only current work frontier (current enrolled projects; IDs, status, local priority, dependencies, changes, freshness).
- Apex cross-project decisions + operator intent/calendar/capacity → portfolio selection and strategy.
- Selected work package → targeted source-repo facts and constraints → next-day execution packet and prompts.
- Operator/agent execution → raw evidence → independent review when consequential → proposed OpenProject update under existing approval policy → reread → next-cycle delta.
- Apex Session/Sync can still serve Apex-native control-plane objects; do **not** mirror OpenProject work packages into their native task schemas.

## Project-level source status (as of checked repository evidence)

| Project | Confirmed source | OpenProject integration conclusion |
|---|---|---|
| Leela | Leela AGENTS.md explicitly states OpenProject owns current work; authored ledgers own build state | OpenProject PM CONFIRMED; verify live WP data at execution |
| MasterOfArts | AGENTS.md still says Hermes Kanban manages durable tasks/review cycles and separately instructs agents to use canonical OpenProject skill for requested PM operations; MoA-Content/MoA-Business containers created | HYBRID/AMBIGUOUS: distinguish durable portfolio commitments from transient agent execution; do not declare a complete migration |
| Investment | AGENTS.md lists the global OpenProject skill, while repo-local orchestration/state remain explicit | OPENPROJECT_ACCESS_CONFIRMED; authoritative PM migration NOT_VERIFIED |
| acim-secular | AGENTS.md names docs/product/ roadmap and current build slice; no OpenProject claim | REPO_LOCAL_CURRENT; OpenProject enrollment NOT_VERIFIED |
| ApexAI-OS | OpenProject hierarchy has an ApexAI-OS container, while Apex task files and Session/Sync are existing control-plane records | CANDIDATE authority split; confirm which Apex work packages were actually migrated before making OpenProject primary there |

## Conflict handling rule

When OpenProject task state differs from Git implementation/build evidence, do **not** automatically choose one. Preserve both source IDs and timestamps, identify whether they answer different questions (commitment versus realization), and ask for an operator decision only when a consequential ambiguity remains after targeted verification.

## Scope that is NOT approved by this record

- No write to OpenProject, Hermes Kanban, or project-task state.
- No automatic replacement of the published Weekly skill or .claude/CLAUDE.md.
- No change to Apex Sync, Session, PrecapWeek, PrecapNextDay, ProjectStatus, or StatusMerge.
- No daemon, cron, MCP bridge, background polling service, or database connector automatically installed.
- No new blanket autonomy for work-package creation/status changes.
- No retirement of Hermes as a general agent runtime or execution tool.
- No claim that all project families and WPs have migrated.

## Validation and promotion gate

Promote this candidate only after the operator accepts the source-of-truth split and a fresh live OpenProject read demonstrates: correct private instance identity; current project set; complete pagination; clear selected work packages; no task mirroring; a usable real Weekly/Next-Day operator packet; and correct gated post-execution write path. Existing file revisions must be narrow, exact-context patches with diff verification.

## Primary sources

- [Leela current authority contract](https://github.com/leela-spec/Leela-Cloud-2026/blob/master/AGENTS.md)
- [OpenProject index and verified hierarchy](https://github.com/leela-spec/apexai-os-meta/blob/main/ki-basis/docs/openproject/README.md)
- [Accepted canonical skill architecture](https://github.com/leela-spec/apexai-os-meta/blob/main/ki-basis/docs/openproject/DECISION-2026-09-28-canonical-skill-architecture.md)
- [Canonical OpenProject skill](https://github.com/leela-spec/agent-skills/blob/master/skills/openproject/SKILL.md)
- [OpenProject write policy](https://github.com/leela-spec/agent-skills/blob/master/skills/openproject/references/write-policy.md)
- [MasterOfArts authority](https://github.com/leela-spec/MasterOfArts/blob/main/AGENTS.md)
- [Investment authority](https://github.com/leela-spec/Investment/blob/main/AGENTS.md)
- [ACIM authority](https://github.com/leela-spec/acim-secular/blob/master/AGENTS.md)
- [Existing Weekly runtime](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/skills/weekly-orchestrator/SKILL.md)
- [Existing PrecapWeek contract](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/skills/PrecapWeek/SKILL.md)
- [Existing StatusMerge contract](https://github.com/leela-spec/apexai-os-meta/blob/main/.claude/skills/status-merge/SKILL.md)
- [Historical Hermes board decision D02](https://github.com/leela-spec/apexai-os-meta/blob/main/apex-meta/epics/hermes-multi-repo-orchestration-v2/decisions/D02-KANBAN-TOPOLOGY.md)
- [Infrastructure single source of truth](https://github.com/leela-spec/apexai-os-meta/blob/main/ki-basis/docs/INFRASTRUCTURE.md)
