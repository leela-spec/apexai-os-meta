# Handover: Weekly Precap Development, Lineage & Version Verification

```yaml
handover:
  id: handover-weekly-precap-evolution-20261105
  domain: weekly-orchestration-precap
  status: active_for_verification
  date: "2026-11-05"
  author: Antigravity
  target_audience: Human Operator / Successor Agent
  purpose: >
    Provide a comprehensive audit ledger and verification guide across all 4 historical
    versions of the Weekly Precap (PrecapWeek) to inspect design evolution, schema
    simplification, contract retirement, and active truth.
```

---

## 1. Executive Summary & Core Evolution

The **Weekly Precap (`PrecapWeek`)** has evolved through four major architectural generations. Each phase tackled a specific problem: eliminating rigid numeric scoring, replacing schema bloat with human-first templates, isolating context execution, and migrating to 0-token deterministic gates.

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  v1: Monolithic Spec   │ ---> │  v2: Wrapper Agents    │ ---> │  v3: Template System   │ ---> │  v4: Forked-Skill D012 │
│  (Pre-2026)            │      │  (2026-06 / 2026-08)   │      │  (2026-07 / 2026-08)   │      │  (CURRENT TRUTH)       │
│  - 5-project roster    │      │  - `apex-precap-week`  │      │  - J02 Weekly Brief    │      │  - `context: fork`     │
│  - 1-100 numeric rating│      │  - Schema-first        │      │  - Step 3/4/5/6        │      │  - Self-contained      │
│  - Theoretical papers  │      │  - Machine bloat       │      │  - Promoted templates  │      │  - Wrapper retired     │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

---

## 2. Version-by-Version Detailed Ledger

### Version 1: Early Conceptual & Macro/Meso Specification (Pre-2026)
* **Status:** SUPERSEDED (Historical / Design Rationale Only).
* **Core Philosophy:** Theoretical, highly structured, multi-page planning papers.
* **Key Characteristics:**
  - Mandatory fixed 5-project portfolio roster.
  - Complex numeric rating formulas (1–100) required to score project capacity.
  - Required massive initial prompt context loading.
* **Originating Artifacts & Exact File Links:**
  - [WeeklyRoutine_Overview_Marco&Meso.md](file:///c:/GitDev/apexai-os-meta/apex-meta/kb/Weekly-Orchestrator/OperatorResearch/WeeklyRoutine_Overview_Marco&Meso.md) — Two-level overview of the original PreCap / FlowRecap / Status-Merge loop.
  - [PersonalOrchestrationProcessFlow.md](file:///c:/GitDev/apexai-os-meta/apex-meta/kb/Weekly-Orchestrator/OperatorResearch/PersonalOrchestrationProcessFlow.md) — Macro/meso consolidated machine-readable specification.
  - [WeeklyRoutine_Detailed.md](file:///c:/GitDev/apexai-os-meta/apex-meta/kb/Weekly-Orchestrator/OperatorResearch/WeeklyRoutine_Detailed.md) — Original multi-hour weekly routine breakdown.
  - [WeeklyRoutine_Detailed_v2(v1maybestillvalid).md](file:///c:/GitDev/apexai-os-meta/apex-meta/kb/Weekly-Orchestrator/OperatorResearch/WeeklyRoutine_Detailed_v2(v1maybestillvalid).md) — Alternative early revision.

---

### Version 2: Multi-Agent Wrapper Topology (`wrapper-agents`)
* **Status:** ARCHIVED (Preserved under `apex-meta/archive/`).
* **Core Philosophy:** Decomposing the loop into dedicated Claude wrapper subagents.
* **Key Characteristics:**
  - Specialized wrapper agent: `apex-precap-week.md`.
  - Machine-first output schema: `weekly-plan-output-contract.md`.
  - Heavy YAML validation checks; high token overhead and risk of cross-turn context contamination.
* **Archived Artifacts & Exact File Links:**
  - [apex-precap-week.md (Archived Wrapper Agent)](file:///c:/GitDev/apexai-os-meta/apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/wrapper-agents/apex-precap-week.md) — The retired wrapper agent definition.
  - [weekly-plan-output-contract.md (Archived Contract)](file:///c:/GitDev/apexai-os-meta/apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/PrecapWeek/weekly-plan-output-contract.md) — The schema-first contract that required machine validation before human review.
  - [weekly-blueprint-standard.md (Archive Copy)](file:///c:/GitDev/apexai-os-meta/apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/PrecapWeek/weekly-blueprint-standard.md) — Pre-fork standard blueprint.

---

### Version 3: The J1–J12 Operator Template System
* **Status:** PROMOTED & MERGED INTO LIVE PACKAGES.
* **Core Philosophy:** Shift from machine-first schemas to human-scannable executive templates.
* **Key Characteristics:**
  - Created the **J02 Weekly Command Brief** template.
  - 6-step promotion process (Step 1 analysis $\rightarrow$ Step 4 template design $\rightarrow$ Step 5 skill promotion $\rightarrow$ Step 6 activation & validation).
  - Established the dual-matrix layout: Project Strategy vs Capacity Allocation.
* **Design & Promotion Artifacts & Exact File Links:**
  - [J02-weekly-command-brief.md (Template Source)](file:///c:/GitDev/apexai-os-meta/apex-meta/operator-output-design/step4-operator-template-system/templates/J02-weekly-command-brief.md) — The canonical template definition.
  - [03_TEMPLATE_FAMILY_OVERVIEW.md](file:///c:/GitDev/apexai-os-meta/apex-meta/operator-output-design/step4-operator-template-system/03_TEMPLATE_FAMILY_OVERVIEW.md) — Design principles for J01–J12.
  - [02-template-promotion-map.yaml](file:///c:/GitDev/apexai-os-meta/apex-meta/operator-output-design/step5-template-promotion/02-template-promotion-map.yaml) — Mapping of J02 into `PrecapWeek`.
  - [00-activation-validation-report.okf.md](file:///c:/GitDev/apexai-os-meta/apex-meta/operator-output-design/step6-activation-validation/00-activation-validation-report.okf.md) — 13/13 activation test results confirming promotion.
  - [APEX_Weekly_Orchestration_Index_v3.md](file:///c:/GitDev/apexai-os-meta/apex-meta/kb/Weekly-Orchestrator/indexes/APEX_Weekly_Orchestration_Index_v3.md) — Master repository index for v3.

---

### Version 4: Direct Forked-Skill Dispatch (D012 / Module 00 Closed)
* **Status:** BASELINE VERIFIED (Decisions D012 & D013, August 2026).
* **Core Philosophy:** Central `weekly-orchestrator` directly dispatches `PrecapWeek` as an isolated worker with `context: fork`, eliminating all wrapper agents while keeping the human-first Weekly Command Brief as the primary output.
* **Key Characteristics:**
  - `execution.context: fork`: Runs in an isolated sub-session with zero memory leak into the parent.
  - `primary_operator_output: Weekly_Command_Brief`: No duplicate machine artifacts; downstream seed is embedded directly in the brief.
  - Dropped fixed 5-project roster and mandatory numeric ratings as hard approval gates. Active projects derive strictly from confirmed project context.
* **Authoritative Production Files & Exact Links:**
  - [.claude/skills/PrecapWeek/SKILL.md (Live Worker Contract)](file:///c:/GitDev/apexai-os-meta/.claude/skills/PrecapWeek/SKILL.md) — The live execution authority for Claude Code.
  - [.claude/skills/PrecapWeek/weekly-command-brief-template.md](file:///c:/GitDev/apexai-os-meta/.claude/skills/PrecapWeek/weekly-command-brief-template.md) — The live template rendered by `PrecapWeek`.
  - [.claude/skills/weekly-orchestrator/SKILL.md](file:///c:/GitDev/apexai-os-meta/.claude/skills/weekly-orchestrator/SKILL.md) — The orchestrator spine that dispatches `PrecapWeek`.
  - [CURRENT-STATE.md (Module 00 Closure)](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/CURRENT-STATE.md) — Verification record of the fresh-context test pass.
  - [DECISIONS.md (D012 & D013 Topology Lock)](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/DECISIONS.md) — Architectural decision log.
  - [01-weekly-command-brief/HANDOVER.md](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER.md) — Starting handover for Module 01.

---

### Version 4.1 / Active Frontier: Dual-View Layout & OpenProject PM Authority Transition (November 2026)
* **Status:** ACTIVE DESIGN & EVOLUTION IN PROGRESS (Remote fetched & merged 2026-11-06).
* **Core Developments:**
  1. **Dual-Matrix Architecture (`SPEC-DUAL-VIEW-WEEKLY-PRECAP.md`):**
     - Cleanly separates non-temporal project development (**Matrix 1: Project Architecture & Process Flow**) from calendar sequence allocation (**Matrix 2: Responsive HTML Calendar & Sprint Grid**).
     - Standardizes 4 weekly sequences: Seq 1 (Master of Arts), Seq 2 (Investment), Seq 3 (Apex OS), Seq 4 (Leela).
     - Adds structured shortlist/longlist tracking per project with process flow arrows (`Step 1 ➔ Step 2 ↻ Iteration ➔ Step 3`).
  2. **OpenProject State Authority Transition Candidate:**
     - Added via remote commits `f722cb92` and `7aa27ff9`:
       - [01-DECISION-OPENPROJECT-WEEKLY-ORCHESTRATION.okf.md](file:///c:/GitDev/apexai-os-meta/apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/01-DECISION-OPENPROJECT-WEEKLY-ORCHESTRATION.okf.md)
       - [02-CONFLICT-AND-DECISION-LOG.okf.md](file:///c:/GitDev/apexai-os-meta/apex-meta/handoff/weekly-orchestration-openproject-transition-2026-11-06/02-CONFLICT-AND-DECISION-LOG.okf.md)
     - Proposes OpenProject as the primary authority for work package status and commitments across enrolled projects, replacing legacy Hermes Kanban and shifting away from pure Apex Session task files.
     - Enforces read-only intake via the canonical Node client: `node C:\GitDev\agent-skills\skills\openproject\client\opCall.js wp.list --project <id>`.
     - Preserves fail-closed offline fallback (`[OP-OFFLINE: WP-<project>-<index>]`) to Apex Session/Sync when OpenProject is unreachable.
  3. **Module 01 Handover Assets Added:**
     - [SPEC-DUAL-VIEW-WEEKLY-PRECAP.md](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-DUAL-VIEW-WEEKLY-PRECAP.md)
     - [WEEKLY_PRECAP_DRAFT_W45.md](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.md)
     - [WEEKLY_PRECAP_DRAFT_W45.html](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_DRAFT_W45.html)
     - [HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md)
     - [HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md)

---

## 3. Comparison Matrix: How Precap Changed

| Dimension | v1 (Macro Spec) | v2 (Wrapper Agent) | v3 (Template System) | v4 (Live Truth: Forked Skill) |
| :--- | :--- | :--- | :--- | :--- |
| **Execution Actor** | Operator manual | `apex-precap-week` (Agent) | `apex-precap-week` + J02 | `PrecapWeek` (Skill via `context: fork`) |
| **Output Type** | Prose / Raw Markdown | `weekly_plan_packet.yaml` | `J02 Weekly Command Brief` | `weekly-command-brief.md` |
| **Downstream Seed** | Verbose notes | Duplicate machine artifact | Split schema | Embedded `downstream_seed` YAML block |
| **Project Roster** | Hardcoded 5 projects | Hardcoded 5 projects | Declared project roster | Dynamically derived from confirmed context |
| **Rating System** | Mandatory 1–100 formula | Hard gate validation | Optional scoring | Optional aid (never a blocking gate) |
| **Context Hygiene** | Monolithic session | Leaked across wrapper turns| Multi-file load overhead | 100% isolated session per run |

---

## 4. Verification & Audit Reproduction Commands

To independently verify this lineage and inspect the files directly in your environment, run these commands:

```powershell
# 1. Search the QMD index for PrecapWeek across the weekly orchestration collection:
qmd search -c apex-weekly-orchestration "PrecapWeek Weekly Command Brief"

# 2. View the live PrecapWeek contract lines 1-50:
qmd get apex-weekly-orchestration/01-weekly-command-brief/HANDOVER.md:1:50

# 3. Inspect git commit history for PrecapWeek's migration to forked skill:
git -C "c:\GitDev\apexai-os-meta" show fda9645f --stat

# 4. Verify that all 6 wrapper agents are safely archived:
Get-ChildItem "c:\GitDev\apexai-os-meta\apex-meta\archive\weekly-orchestration\topology-pre-forked-skills-2026-08\wrapper-agents"
```

---

## 5. Next Steps & Open Work

1. **Module 01 Execution:** The next open action is starting `01-weekly-command-brief` to refine the Q&A flow and visualization layout (refer to [01-weekly-command-brief/HANDOVER.md](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER.md)).
2. **OpenMausBot Translation:** The live v4 `PrecapWeek` skill maps directly to the isolated OpenMausBot routine scheduled for `0 9 * * SUN` running under `approval: full`.
