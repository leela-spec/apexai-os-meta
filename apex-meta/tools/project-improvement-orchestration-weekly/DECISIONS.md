---
type: decision_log
id: DEC-WEEKLY-ORCHESTRATION-MASTER
title: Durable Decisions — Weekly Orchestration Architecture
description: Canonical register of locked architectural, process, and interface decisions for the weekly orchestration system.
status: approved
tags: [weekly-orchestration, decisions, governance, informatics, v1.0-ultra]
---

# Durable Decisions — Weekly Orchestration Architecture

## Module 00 Locked Decisions Summary (`D001–D013`)

> **Archived Verbatim:** Full verbatim text of `D001` through `D013`, `O001`, and `O002` is preserved at [`apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/MODULE-00-DECISIONS-VERBATIM.md`](../../archive/weekly-orchestration/topology-pre-forked-skills-2026-08/MODULE-00-DECISIONS-VERBATIM.md).

| Decision | Status | Scope | Summary / Rationale |
|---|---|---|---|
| **D001** Production Weekly Orchestrator canonical control plane | locked | whole project | Do not create a second permanent runtime orchestrator; master repairs existing weekly-orchestrator. |
| **D002** Durable project-improvement coordination home | locked | improvement process | Maintain coordination folder as context-resilient home across long chats. |
| **D003** Repair global orchestration before detailed output modules | locked | module sequence | Module 00 audits/repairs central lifecycle first; detailed output modules follow. |
| **D004** Master verifies every module against whole infrastructure | locked | every module | Completed module work returns to Master for independent whole-system verification. |
| **D005** Integrate first, then test fresh | locked | every module | Integrate changes into production files before fresh-context testing on real W34 fixtures. |
| **D006** Repeatability means bounded AI judgment | locked | architecture | Ownership, transactions, and gates are contract-bound; AI judgment reserved for semantic synthesis. |
| **D007** Preserve superseded architecture in history/archive | locked | repo maintenance | Move obsolete material to explicit archive/history paths; eliminate active ambiguity. |
| **D008** Human-facing output design starting authority | locked | output modules | Human-first, result-card-first, progressive disclosure, zero duplicate surfaces. |
| **D009** No presumption of necessity | locked | orchestration spine | Components remain only with proven current value and named consumer. |
| **D010** Research skill/agent composition before changing topology | locked | orchestration spine | Empirical research prompt (01-ARCHITECTURE-RESEARCH-PROMPT.md) before topology change. |
| **D011** Runtime activation requires entrypoint/contract behavior | locked | output modules | Proven by active entrypoint behavior and fresh-context execution, not template presence. |
| **D012** Skill-owned, selectively-forked weekly runtime topology | locked | orchestration spine | 6 stage components become fork workers; 2 blind reviewers retained; apex-session/sync backbone. |
| **D013** Module 00 closed: forked-skill topology verified | locked | Module 00 | All 12 phases complete and fresh-context verified without production defects. |

### Closed Questions (`O001`, `O002`)

- **O001 (Skill/Agent physical topology):** CLOSED — Resolved by D012 (`context: fork` on Skills replacing 6 wrapper agents).
- **O002 (`workflow-process-design` dependency):** CLOSED — Confirmed non-blocking/dead dependency; live on-demand dependencies remain PromptEngineer, AIRouting, model-usage-log per D012.

---

## D014 — OpenProject dependency frontier precedes weekly critical-path selection

**Status:** operator accepted design priority; live source verification OPEN (2026-11-06).

**Decision:** P1 must first read the current private OpenProject work-package and dependency graph for projects actually enrolled. Use verified relation types, source identities, status, and freshness to derive dependency readiness and blocked work before ranking or shaping Matrix 1 and Matrix 2. The repository's historical WP hierarchy is not a current live read. Do not claim a mathematically proven critical path without trustworthy durations and calendar assumptions; otherwise report dependency-driven chains/blockers.

**Execution:** bounded, read-only local-agent handover `00-openproject-dependency-intake/HANDOVER-20261106.okf.md`. Current ChatGPT GitHub access does not reach the private `127.0.0.1` OpenProject API. Missing identity, pagination, dependency direction or cross-project counterpart must be flagged rather than invented.

**Scope:** global weekly planning input order, project PM authority, Matrix 1/2 data provenance; no production mutation.

**Source:** operator, 2026-11-06 (follow-up to macro handover).

---

## D015 — M02=B accepted: owner-aware PM writeback after recap

**Status:** operator accepted target; NOT YET production-implemented/tested (2026-11-06).

**Decision:** After evidence -> FlowRecap candidates -> StatusMerge -> operator G5, verified OpenProject-owned WPs must be updated through the canonical OpenProject skill with per-action authorization, current lockVersion and post-write reread. Apex Session remains for verified Apex-native objects only. Never mirror canonical OP task state into the old Apex PM graph or elevate a draft recap to confirmed state. No new RecapDay stage by assumption.

**Dependency:** D014 real OP owner/enrollment/source evidence and later narrow multi-WP recap interface verification. Write autonomy is NOT granted here.

**Scope:** StatusMerge/G5, weekly router, next-day intake, owner-aware mutation receipt.

**Source:** operator M02=B, 2026-11-06.

---

## D016 — M05=B accepted: dedicated, stateless sequencing skill (definition deferred)

**Status:** operator accepted capability choice; design/build DEFERRED until OpenProject intake and later sequence semantics (2026-11-06).

**Decision:** Provide a dedicated stateless sequencing Skill rather than only an inlined PrecapNextDay helper. It may be on-demand under the existing D012 orchestrator. Reuse existing Workflow&Processes, PrecapWeek, PrecapNextDay and source OP client; do not duplicate their workflow validation, PM state, scheduler, agents or calendar writers. Concrete input/output/connector examples and ownership must be designed after the OpenProject dependency contract and operator's broader sequence definition.

**Critical reservation:** M04 remains OPEN. The operator explicitly said **a sequence is more than a flow and will be defined later**. Previous M04-B recommendation (one sequence to one or several flows) is NOT accepted; neither 1:1 nor 1:N nor N:M is decided. Do not build a premature flow mapping or sprint model into the new skill.

**Placement:** assess canonical `leela-spec/agent-skills` for cross-agent reuse, not a copied skill in product repos. No new Skill files created in this decision step.

**Source:** operator M05=B and M04 correction, 2026-11-06.

---

## D017 — M06=A superseded: Monday–Sunday planning with weekday/weekend regimes

**Status:** superseded by D018 / D020 / Monday–Sunday canonical clock lock (`week-blueprint.json`).

**Decision:** Weekly orchestration plans **Monday through Sunday** (both Saturday and Sunday active). Monday–Friday run the weekday regime (`08:00–24:00`, `4 × 120m` Flows); Saturday and Sunday run the weekend regime (`12:00–16:00`, `2 × 120m` Flows). Weekly Precap and `StatusMerge` run on Saturday or Sunday (`A-12` closed).

**Scope:** calendar/week scope, PrecapWeek, validation, canonical `02-weekly-dispersal/week-blueprint.json`.

**Source:** operator OD-04 / OD-26 / OD-43, 2026-11-09.

---

## D018 — Operator weekly flow architecture: `3x3` standard & Sequencing integration

**Status:** locked operator decision (2026-11-08; clock & dispersal alignment 2026-11-10).

**Decision:** The weekly operating structure runs `24` weekly `120m` Flows (`4/day` Mon–Fri, `2/day` Sat–Sun; `72` `P/M/C` iterations + `24` `R` breaks). Sequencing is a distribution system powered by interleaving, spaced repetition, chunking, and testing across Mental, Physical, Regeneration, and Craft/Project Epics. All calendar timestamps and protected anchors (`08:00–24:00` weekday with `22:00–22:30` Day Outro; `12:00–16:00` weekend) are governed solely by [`02-weekly-dispersal/week-blueprint.json`](02-weekly-dispersal/week-blueprint.json). Algorithm rules (`ALGORITHM.md`) and weekly operator dials (`week-demand.json`) live in the `02-weekly-dispersal` bundle (`MasterOfArts/Sequencing/dispersal/`).

**Scope:** weekly orchestration, `3x3` flow standard, single blueprint clock ownership, Sequencing dispersal.

**Source:** operator + T1 alignment, 2026-11-10.

---

## D019 — External service intake: live read-only OpenProject and Calendar with offline fallback

**Status:** locked operator decision (2026-11-11).

**Decision:** When running `PrecapWeek` or `PrecapNextDay`, query OpenProject (`127.0.0.1:8083`, read-only via `opCall.js`) and Google Calendar when reachable to pull live work packages, relations, and fixed commitments. If `:8083` or Calendar is unreachable (`ECONNREFUSED` or auth error), do not block planning: fall back automatically to confirmed offline snapshots/Session feeds and tag affected items `[OP-OFFLINE]`.

**Scope:** external data intake (`T0`), `PrecapWeek`, `PrecapNextDay`, Matrix 1 & 2 provenance.

**Source:** operator verification, 2026-11-11.

---

## D020 — Precap Week v2.1 (`00..05`), 6-Portfolio Standard, Unified `EM-13` (`G|I|P|S|O|C`), and `T2` Dispersal Closure

**Status:** locked and implemented (2026-11-11).

**Decision:**
1. **6-Portfolio Standard (`02-PORTFOLIO-COMPASS`):** Portfolio-level views, Matrix 1 grouping, and Craft (`C`) Epics use the 6 canonical Portfolio Areas: **`Leela`** (`OP #10`), **`IPOS`** (`OP #16`), **`Master of Arts`** (`OP #14`), **`Apex AI`** (`OP #8`), **`Mindful Bar`** (`OP null`), and **`Residual`** (`OP null`).
2. **Unified `EM-13` (`G|I|P|S|O|C`):** Matrix 1 UI cards remain `L1 / L2` (no `L3` cubes), while expanded `Goal` and `Output` cells decompose into `Tasks -> Subtasks` with short drafts/examples (`Goal.acceptance`, `Input.exclusions`, `Output.redraft`). Cross-repo dependencies render inline via Option B `🔗 Cross-Repo:` clickable pills (`SPEC-MATRIX-1-PORTFOLIOS.okf.md` §5).
3. **`T2` Dispersal & Section `05` (`SEQ-D1..D4`):** `MasterOfArts/Sequencing/dispersal/` (mirrored to `02-weekly-dispersal/`) owns `EPICS-SCHEMA.md`, `epics.json`, `ALGORITHM.md`, `week-demand.json`, `build_slot_inventory.py`, and `allocate_week.py` (`week-allocation.json`). Evening physical courses (`18:30–19:30`) drive Gaussian coupling (`σ = 6.0h`, `19:00` midpoint, `w_max = 1.5x`, no Fri→Sat bleed); `R` rotates via weighted round-robin (`XP = 0`, `DD-16` no numeric BP floor).
4. **Calendar Boundary (`Q10`):** `PrecapWeek` is strictly read-only for Google Calendar; gated `[FLOW]` event creation belongs exclusively to `PrecapNextDay` (`02-next-day-brief/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`).

**Scope:** `.claude/skills/PrecapWeek/`, `01-weekly-command-brief/`, `02-weekly-dispersal/`, `02-next-day-brief/`.

**Source:** operator verification & forensic execution, 2026-11-11.

---

## D021 — Single-Owner Precap Week Simplification, Machine Schemas, Compiler & OKF v0.2 Output

**Status:** locked and implemented (2026-11-11).

**Decision:**
1. **One Home Per Rule:** Consolidated all valid Precap Week UI/domain rules into [`01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md`](01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md) and dedicated modular specifications ([`SPEC-MATRIX-1-PORTFOLIOS.okf.md`](01-weekly-command-brief/SPEC-MATRIX-1-PORTFOLIOS.okf.md), [`SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md`](01-weekly-command-brief/SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md), [`SPEC-PRECAP-INTERFACES-HANDOFF.okf.md`](01-weekly-command-brief/SPEC-PRECAP-INTERFACES-HANDOFF.okf.md)), clock windows into [`02-weekly-dispersal/week-blueprint.json`](02-weekly-dispersal/week-blueprint.json), calendar deformation into [`.claude/skills/PrecapWeek/calendar-planning-guidance.md`](../../../.claude/skills/PrecapWeek/calendar-planning-guidance.md), and eliminated `16` redundant handover/blueprint/manifest files (`HANDOVER-02..06`, `precap-week-handovers/01..07`, `weekly-blueprint-standard.md`, `weekly-blueprint-meeting-example.md`, `package-manifest.md`, `01-weekly-command-brief/README.md`; preserved at pushed baseline SHA `ad10c483`).
2. **Machine-Readable Background & Compiler:** Added Draft 2020-12 JSON schemas in [`01-weekly-command-brief/schemas/`](01-weekly-command-brief/schemas/precap-week-cockpit.schema.json) and deterministic `stdlib`-only Python compiler [`render_precap_cockpit.py`](01-weekly-command-brief/render_precap_cockpit.py) generating both the preserved interactive `v0.5` HTML Cockpit and OKF v0.2 Weekly Command Briefs + `PrecapNextDay` handoff JSON.
3. **Preserved Downstream Compatibility:** Retained `Weekly_Command_Brief` / `weekly_plan_packet` (`handoff_envelope`) and `presentation_handoff` contracts for `weekly-orchestrator` and `PrecapNextDay`.

**Scope:** `.claude/skills/PrecapWeek/`, `01-weekly-command-brief/`, `precap-week-handovers/`, `CURRENT-STATE.md`.

**Source:** operator SSOT simplification mandate, 2026-11-11.
