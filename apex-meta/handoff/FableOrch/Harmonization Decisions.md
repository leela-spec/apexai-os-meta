## step: 1  
status: locked  
generated: 2026-06-19

# Harmonization Decisions

## H1 — STATUS ENUM

The Apex project defines its status enumeration as: **open**, **in‑progress**, **blocked**, **done**, and **deferred**.

**Sources & evidence**

- **S1b**: `source‑knowledge/ProjectRepos/ccpm‑main/skill/ccpm/references/structure.md` (copy type ADAPT).
- **S2b**: `source‑knowledge/ProjectRepos/backlog‑main/src/types/index.ts` (copy type ADAPT).

## H2 — FILE PATH CONVENTION

All Apex files reside under the `apex‑meta/` directory. It contains subdirectories:

- `harmonization/` for governance files (`decisions.md`, `field‑schema.md`, `task‑template.md`, etc.),
- `epics/<slug>/` with numbered task files (`001.md`, `002.md`, …),
- `handoff/` containing `task_plan.md`, `findings.md`, `progress.md`, and `next‑session.md`,
- `registry/` with `index.md` (auto‑generated, do not edit),
- `scripts/` for all Python scripts, and
- `.claude/skills/` for the skill definitions.

**Sources & evidence**

- **S1b**: `source‑knowledge/ProjectRepos/ccpm‑main/skill/ccpm/references/structure.md` (copy type ADAPT).
- **S4a**: `source‑knowledge/ProjectRepos/planning‑with‑files‑master/SKILL.md` (copy type FULL/CONCEPT).

## H3 — DEPENDENCY FIELD

The dependency field is named **depends_on**. It is an array of task IDs (`int` values), e.g. `depends_on: [1, 3]`. A task is actionable only when _all_ referenced tasks have `status` set to `done`.

**Sources & evidence**

- **S1b**: `source‑knowledge/ProjectRepos/ccpm‑main/skill/ccpm/references/structure.md` (copy type ADAPT).
- **S3c**: `source‑knowledge/ProjectRepos/claude‑task‑master‑main/scripts/modules/task‑manager/find‑next‑task.js` (copy type ADAPT).

## H4 — SCRIPT LANGUAGE

All deterministic operations in Apex must be implemented in **Python**; Bash, TypeScript or other shell scripts are not permitted.

**Sources & evidence**

- **S6b**: `source‑knowledge/ProjectRepos/llm‑wiki‑main/scripts/update‑index.py` (copy type FULL).
- **S3c**: `source‑knowledge/ProjectRepos/claude‑task‑master‑main/scripts/modules/task‑manager/find‑next‑task.js` (copy type ADAPT).

## H5 — CLUSTER ASSIGNMENT

Apex divides processes into three clusters:

- **Cluster A — PLAN**: pure SKILL.md, no scripts; requires an operator gate before any write. Processes: PM1, PM2, PM3, PD1, PD2, PD4.
- **Cluster B — SYNC**: SKILL.md plus read‑only Python scripts; never writes task content. Processes: PM4, PM5, PM7, PM8, KB4, KB5.
- **Cluster C — SESSION**: SKILL.md plus write‑gate scripts; all mutations require a CONFIRM step. Processes: PM6, KB1, KB2, KB3, KB6, PD3, PD5, PD6.

**Sources & evidence**

- **S1b**: `source‑knowledge/ProjectRepos/ccpm‑main/skill/ccpm/references/structure.md` (copy type ADAPT).
- **S4a**: `source‑knowledge/ProjectRepos/planning‑with‑files‑master/SKILL.md` (copy type FULL/CONCEPT).

## H6 — HANDOFF FORMAT

The handoff directory `apex‑meta/handoff/` contains four files: `task_plan.md`, `findings.md`, `progress.md`, and `next‑session.md`. For `next‑session.md`, the required sections are: **Current Step**, **Open Items**, **Risks**, **Decisions Made**, and **Next Actions**.

**Sources & evidence**

- **S4a**: `source‑knowledge/ProjectRepos/planning‑with‑files‑master/SKILL.md` (copy type FULL/CONCEPT).

## H7 — PRIORITY & URGENCY

The `priority` field can be **high**, **medium**, or **low**, with weights of 3, 2, and 1 respectively.  
The `urgency` field derives from the `due_date` (an ISO8601 date). Urgency scores are computed as the number of days between the due date and today (lower values are more urgent); if no `due_date` is provided, the urgency defaults to 999.

**Sources & evidence**

- **S3c**: `source‑knowledge/ProjectRepos/claude‑task‑master‑main/scripts/modules/task‑manager/find‑next‑task.js` (copy type ADAPT).
- **S5b**: `source‑knowledge/ProjectRepos/kanban‑skill‑master/skills/kanban‑ai/scripts/show_blocked.sh` (copy type ADAPT).