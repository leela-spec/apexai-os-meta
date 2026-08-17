# APEX OS

APEX OS contains two separate orchestration systems and one shared capability backbone. This file is the compact project activation and routing surface. Load detailed instructions only from the entrypoint selected by explicit operator intent.

## Orchestration systems

| System | Activate only when | Runtime entrypoint | Owns |
|---|---|---|---|
| **Weekly Orchestrator** | The operator asks to run, resume, locate, or audit the weekly operational loop. | `.claude/skills/weekly-orchestrator/SKILL.md` | PrecapWeek, PrecapNextDay, operator execution and evidence intake, FlowRecap, StatusMerge, ProjectStatus, and the next planning cycle. |
| **Multi-Agent Orchestration** | The operator explicitly requests a Multi-Agent Orchestration run or explicitly routes a bounded problem into it. | `apex-meta/orchestration/00-START-HERE.md` | Alfred-led intake and gates, Meta Strategy framing, Meta Ops integration, bounded specialist work, independent review, and run closure. |

The two systems are independent. Running one does not activate the other.

## Plan-Sync-Session Backbone

The following packages are shared APEX OS capabilities, not a third orchestration system:

- `.claude/skills/apex-plan/SKILL.md` — proposal and decomposition.
- `.claude/skills/apex-sync/SKILL.md` — deterministic computation and reports.
- `.claude/skills/apex-session/SKILL.md` — confirmed mutation, handoff, and closure.

Multi-Agent Orchestration uses the backbone through the Meta Ops integration contract at `apex-meta/orchestration/agents/meta-ops/INTEGRATION-apex-plan-sync-session.md`.

Weekly Orchestrator reads the confirmed Session planning feed and relevant Sync reports, and routes approved project or task changes through `apex-session`. It does not treat `apex-plan` as an implicit weekly stage and does not activate Multi-Agent Orchestration.

## Separation and transfer rules

- Do not activate either orchestration system merely because the other is running.
- The shared `.claude/agents/` directory is a runtime location, not evidence that the two systems share an orchestration contract.
- Cross-system transfer requires explicit operator instruction, an explicit handoff packet, or a confirmed durable-artifact reference.
- Do not reinterpret a packet or artifact from one system as authorization to start the other.

## Navigation

- Repository map: `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`.
- Weekly design and evidence: `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md`.
- Multi-Agent architecture and terminology: `apex-meta/orchestration/ARCHITECTURE.md` and `apex-meta/orchestration/GLOSSARY.md`.
- Skill-specific triggers, failure behavior, gates, and output contracts remain owned by each selected `SKILL.md`.
- Agent-specific delegation conditions remain owned by the selected `.claude/agents/*.md` contract.

## Global boundaries

- Never auto-trigger a skill or orchestration system without operator intent.
- Never infer, default, or fabricate operator confirmation.
- An explicitly requested autonomous run may batch interaction, but it never fabricates confirmation or performs confirmed mutation outside the selected entrypoint's gate contract.
- Durable project or task mutation goes through `apex-session`; registry writes use the explicit `apex-sync` write path only after its required preview, drift report, and gate.
- Read only the active entrypoint and the state, packets, reports, or references needed for the selected request.
- Never write into `source-knowledge/`; load it only when the operator explicitly requests source conversion or recovery work.
- Load `.repair-backups/`, recovery, staging, verification, report, and validation-report directories only when the operator explicitly requests the relevant recovery or audit task.
- Never create cron jobs, schedulers, Kanban tasks, or calendar events automatically.
- On missing or unsafe input, follow the selected entrypoint's failure contract and report the unresolved condition.
