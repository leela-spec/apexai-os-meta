# Handover & Interactive Orchestrator: OpenProject Mapping & Dependency Architecture

```yaml
handover:
  id: OP-ORCH-MAP-DEPS-20261106
  title: "OpenProject Portfolio Mapping & Interactive Dependency Orchestrator"
  date: "2026-11-06"
  status: ACTIVE_INTERACTIVE_ORCHESTRATOR
  target_instance: "http://127.0.0.1:8083"
  client_path: "C:\\GitDev\\agent-skills\\skills\\openproject\\client\\opCall.js"
  scope: "Portfolio-wide work package inventory, dependency mapping, and mutation guide"
```

---

## 1. Executive Summary & Purpose

This handover acts as an **interactive orchestrator** to guide the operator through mapping, linking, and managing dependencies across all projects in the private OpenProject instance.

We have live-queried and cataloged all enrolled projects. Rather than dealing with synthetic IDs or fragmented task lists, this document provides:
1. The **complete verified census** of all active projects and work packages.
2. A **step-by-step interactive workflow** to establish predecessor/successor (`follows`/`precedes`) and blocking (`requires`/`blocks`) relations.
3. The exact read and write commands (using the canonical Node client with safe `--dry-run` and preview gates) to update OpenProject.

---

## 2. Complete OpenProject Portfolio Census

The private instance (`http://127.0.0.1:8083`) currently hosts **15 enrolled projects**. Below is the verified breakdown:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              PORTFOLIO WORK PACKAGE CENSUS                             │
├──────────────────────────┬────────────┬───────────┬────────────────────────────────────┤
│ Project Name             │ Project ID │ Total WPs │ Focus & Current Scope              │
├──────────────────────────┼────────────┼───────────┼────────────────────────────────────┤
│ Investment / IPOS        │ 16         │ 6         │ Research Intake & Docling Pipeline │
│ Website (Master of Arts) │ 14         │ 2         │ Content Transformation & ACIM      │
│ ApexAI-OS                │ 8          │ 3         │ KI-Basis, QMD & Layer-1 Contracts  │
│ MoA-Content              │ 6          │ 2         │ Content Assets                     │
│ MoA-Business             │ 7          │ 0         │ Invoicing & Business Operations    │
│ Leela (Core)             │ 3          │ 128       │ Orchestration Waves & PMH Pipeline │
│ Leela & Mastery          │ 4          │ 148       │ Umbrella Container                 │
│ ├─ Skill Tree            │ 10         │ 15        │ Skill Tree Graph & Geometry        │
│ ├─ Path                  │ 9          │ 14        │ Path Navigation & Convergence      │
│ ├─ Sequencing            │ 11         │ 11        │ Delivery Waves A → B1 → C          │
│ └─ Rhythm                │ 15         │ 3         │ Rhythm Planning & Fit Metrics      │
│ PM Infrastructure        │ 5          │ -         │ Shared Tooling                     │
│ Demo / Scrum Projects    │ 1, 2       │ -         │ Default Boilerplate                │
└──────────────────────────┴────────────┴───────────┴────────────────────────────────────┘
```

---

## 3. Verified Work Package Detail (Per Project)

### Sequence 1: Master of Arts (`moa-website`, Project 14 & `moa-content`, Project 6)
* **`[OP-WP#163]`**: Content Transformation (`Status: New`)
* **`[OP-WP#204]`**: ACIM Secular: Dedicated Sources & Commentary Credits Page (`Status: New`)
* **`[OP-WP#144]`**: Content Production (`Status: New`, in `moa-content` Project 6)
* **`[OP-WP#145]`**: Asset Library (`Status: New`, in `moa-content` Project 6)
* *Gap Identified:* Project 7 (`moa-business`) currently has **0 WPs** (e.g. Invoicing / Accounting is not yet registered).

### Sequence 2: Investment (`investment-ipos`, Project 16)
* **Parent Container:** **`[OP-WP#223]`**: IPOS — Research Intake & Evidence Operations (`Status: New`)
  * **`[OP-WP#224]`**: ADR-003: Formalize Karakeep Retirement & Code Deprecation
  * **`[OP-WP#225]`**: Activepieces Probation: Benchmark Native Python/Hermes Cron vs AP Container
  * **`[OP-WP#226]`**: RI-11: Implement IBM Docling & Trafilatura Ingestion Adapter
  * **`[OP-WP#227]`**: Mission 2: Verify Hermes Weekly Telegram Digest Dispatch (`ipos/export/telegram.py`)
  * **`[OP-WP#228]`**: BMAD Handover: Research-to-Portfolio Operator Clarity & Architecture Inventory

### Sequence 3: Apex OS (`apexai-os`, Project 8)
* **`[OP-WP#139]`**: ki-basis open issues register (2026-09-29) - 12 items, P0-P3 (`Status: New`)
* **`[OP-WP#198]`**: `[CORTEX_PB]` Integrate & Control QMD Infrastructure for KI-Basis Linux Stack (`Status: New`)
* **`[OP-WP#222]`**: Layer-1 contract master is untracked — decide tracking in apexai-os-meta (`Status: New`)

### Sequence 4: Leela Feature Projects
#### A. Skill Tree (Project 10 - 15 WPs)
* **Parent:** **`[OP-WP#196]`**: Skill Tree relationship graph — Bundle, Fusion and structural relations
  * **`[OP-WP#164]`**: `[materialization]` STF-01 — compile authoritative node roster
  * **`[OP-WP#188]`**: `[materialization]` STF-23 — verify unlock semantics
  * **`[OP-WP#189]`**: `[materialization]` STF-24 — attest node positioning
  * **`[OP-WP#190]`**: `[materialization]` STF-25 — define structural relation vocabulary

#### B. Sequencing (Project 11 - 11 WPs)
* **Parent:** **`[OP-WP#215]`**: Sequencing delivery waves — A → B1 → C (dependency map)
  * **`[OP-WP#216]`**: Wave A — Sequencing domain, serializers, typed IDs and structure hashes
  * **`[OP-WP#217]`**: Wave B1 — database-neutral repository seam
  * **`[OP-WP#218]`**: Wave C3 — scoring validation memo and formula objective
  * **`[OP-WP#219]`**: Wave C4 — ranking and resolver (`ST-022` candidate comparator)
  * **`[OP-WP#220]`**: Wave C5 — fixtures parity and Wave C exit proof
  * Standalone: **`[OP-WP#160]`**: Resolve quarantined Sequencing decisions
  * Standalone: **`[OP-WP#211]`**: Wire sequence runs to real instances and completion

#### C. Path (Project 9 - 14 WPs)
* **Parent:** **`[OP-WP#161]`**: Path finalization delivery waves — Run 1 → Run 4
  * **`[OP-WP#162]`**: Path Run 1 — unblock and close out
  * **`[OP-WP#166]`**: Path Run 2 — unblock and close out
  * **`[OP-WP#168]`**: Path Run 3 — unblock and close out
  * **`[OP-WP#170]`**: Path Run 4 — unblock and close out

#### D. Rhythm (Project 15 - 3 WPs)
* **`[OP-WP#174]`**: `[materialization]` RH-B02 — re-attest BP evidence boundary
* **`[OP-WP#175]`**: `[materialization]` RH-B10 — re-attest visible planning metrics
* **`[OP-WP#176]`**: `[materialization]` RH-B21 — re-attest weekly fit feedback

---

## 4. How OpenProject Relations Work

OpenProject supports typed relations between work packages. To prevent logic errors, adhere to these definitions:

| Relation Type | Semantic Meaning | Usage Example |
| :--- | :--- | :--- |
| **`follows`** / **`precedes`** | Sequential / Temporal finish-to-start dependency. (Work package A cannot start until B finishes). | Wave B1 `[#217]` **follows** Wave A `[#216]` |
| **`requires`** / **`blocks`** | Hard structural or functional dependency. | Code unblock `[#164]` **requires** spec freeze `[#159]` |
| **`relates`** | Non-blocking informational or domain relationship. | Two feature cards that touch the same screen |
| **`parent` / `child`** | Hierarchical containment (NOT a relation; set via `parent` field). | Subtasks grouped under an Epic container |

---

## 5. The Interactive Step-by-Step Mapping Workflow

Here is how we will systematically map each project:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        INTERACTIVE MAPPING CYCLE                       │
├────────────────────────────────────────────────────────────────────────┤
│ Step 1: Select Project (e.g. Investment / IPOS, Project 16)            │
│ Step 2: Review existing WPs & determine missing epics or tasks         │
│ Step 3: Define dependency chains (What must precede what?)             │
│ Step 4: Preview command in dry-run mode (`node opCall.js ...`)         │
│ Step 5: Operator confirms -> Apply with `--confirmed`                  │
│ Step 6: Verify new graph and move to next project                      │
└────────────────────────────────────────────────────────────────────────┘
```

### CLI Command Reference for Establishing Dependencies

```powershell
# 1. Preview creating a relation (Dry-Run by default):
node C:\GitDev\agent-skills\skills\openproject\client\opCall.js relation.create --from <WP_A> --to <WP_B> --type follows

# 2. Confirmed creation (Only after operator authorization):
node C:\GitDev\agent-skills\skills\openproject\client\opCall.js relation.create --from <WP_A> --to <WP_B> --type follows --confirmed

# 3. Create a new task or subtask:
node C:\GitDev\agent-skills\skills\openproject\client\opCall.js wp.create --project <PROJECT_ID> --subject "Task Name" --parent <PARENT_WP_ID> --confirmed

# 4. View all relations for a specific work package:
node C:\GitDev\agent-skills\skills\openproject\client\opCall.js wp.get --id <WP_ID>
```

---

## 6. Project 1 Kickoff: Investment / IPOS (Project 16)

Let's begin with **Investment / IPOS (Project 16)** as our first target.

**Current WPs:**
- `[#224]` ADR-003: Formalize Karakeep Retirement
- `[#225]` Activepieces Probation: Benchmark Native Python/Hermes Cron vs AP
- `[#226]` RI-11: Implement IBM Docling & Trafilatura Ingestion Adapter
- `[#227]` Mission 2: Verify Hermes Weekly Telegram Digest Dispatch
- `[#228]` BMAD Handover: Research-to-Portfolio Operator Clarity

**Candidate Flow Chain for IPOS:**
1. Does Karakeep deprecation `[#224]` need to finish before Docling `[#226]` starts, or do they run in parallel?
2. Does Telegram digest `[#227]` depend on Docling `[#226]` ingestion delivering new articles?
3. Are there missing work packages needed for the macro data feed (FRED)?
