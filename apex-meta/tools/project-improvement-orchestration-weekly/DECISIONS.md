---
type: decision_log
id: DEC-WEEKLY-ORCHESTRATION-MASTER
title: Durable Decisions — Weekly Orchestration Architecture
description: Canonical register of locked architectural, process, and interface decisions for the weekly orchestration system.
status: approved
tags: [weekly-orchestration, decisions, governance, informatics, v1.0-ultra]
---

# Durable Decisions — Weekly Orchestration Architecture

## D001 [P0 | I95/E20/R10] — Production Weekly Orchestrator remains the canonical runtime control plane

**Status:** locked

**Decision:** Do not create a second permanent runtime orchestrator. The improvement project's Master Orchestrator repairs and verifies the existing production Weekly Orchestrator.

**Rationale:** A second control plane would duplicate lifecycle/authority knowledge and increase drift risk.

**Scope:** whole project

**Source:** operator, 2026-08-17

---

## D002 [P1 | I85/E15/R05] — Create a durable project-improvement coordination home

**Status:** locked

**Decision:** Maintain this folder as the token/context-resilient home for the redesign project so the Master can recover orientation across long/fresh chats.

**Rationale:** Conversational context alone is too fragile for a multi-module architecture repair.

**Scope:** improvement process only

**Source:** operator, 2026-08-17

---

## D003 — Repair global orchestration before detailed output modules

**Status:** locked

**Decision:** Module 00 audits and repairs the whole Weekly Orchestration lifecycle first. Detailed output modules follow bounded handovers.

**Rationale:** Current evidence indicates the central loop itself contains stale or over-specified assumptions; module-only fixes would inherit them.

**Scope:** module sequence

**Source:** operator + repository review, 2026-08-17

---

## D004 — Master verifies every module against the whole infrastructure

**Status:** locked

**Decision:** Completed module work returns to the Master. The Master independently inspects actual production changes and verifies cross-system compatibility before testing.

**Scope:** every module

**Source:** operator, 2026-08-17

---

## D005 — Integrate first, then test fresh

**Status:** locked

**Decision:** Module design is integrated into actual production skill/agent/template files before testing. Testing then occurs in a fresh context against existing W34/example data.

**Rationale:** Isolated mock examples do not prove the production path is encoded correctly; same-chat testing can benefit from hidden design context.

**Scope:** every module

**Source:** operator, 2026-08-17

---

## D006 — Repeatability means bounded AI judgment, not identical prose

**Status:** locked

**Decision:** Process, ownership, inputs, transactions, persistence and gates should be contract-bound/repeatable. AI judgment remains valid for planning, synthesis, prioritization, prompt generation and interpretation where the task is inherently semantic.

**Scope:** architecture

**Source:** operator, 2026-08-17

---

## D007 — Preserve superseded architecture in history/archive

**Status:** locked

**Decision:** When active architecture is replaced, move obsolete material to an explicit archive/history location instead of deleting it outright or leaving it active beside the replacement.

**Rationale:** Prior designs can later prove useful, but active ambiguity must be removed.

**Scope:** repository maintenance

**Source:** operator, 2026-08-17

---

## D008 — Human-facing output design already recovered is starting design authority

**Status:** locked unless operator changes it during module design

**Decision:** Human-first, result-card-first, progressive disclosure, minimum machine payload, no duplicate surfaces, readable flow cards and real prompt files are established starting intent. The project should wire/refine them, not rediscover them from zero.

**Scope:** output modules

**Source:** recovered operator-verified design + operator confirmation, 2026-08-17

---

## D009 — No presumption that Sync, ProjectStatus, gates or universal envelopes are necessary

**Status:** locked as evaluation rule

**Decision:** These components may remain only when Module 00 demonstrates concrete current value and a named consumer. Existing presence is not sufficient justification.

**Scope:** orchestration spine

**Source:** operator review, 2026-08-17

---

## D010 — Research skill/agent composition before changing topology

**Status:** locked process rule

**Decision:** Module 00 must run `00-orchestration-spine/01-ARCHITECTURE-RESEARCH-PROMPT.md` before reorganizing or retaining the current skill/agent topology by assumption.

**Rationale:** Claude Code natively supports both Skills and Subagents, but native support does not prove that each current wrapper agent creates enough value to justify its context/instruction layer. The architecture must be selected from actual APEX requirements and current official Claude behavior.

**Scope:** orchestration spine architecture

**Source:** operator feedback + architecture review, 2026-08-17

---

## D011 — Runtime activation requires entrypoint/contract behavior, not template presence

**Status:** locked evaluation rule

**Decision:** A promoted template is not considered integrated until the active production entrypoint and runtime path require/use the intended behavior and a fresh invocation can produce it without design-chat memory.

**Rationale:** Previous activation validation reported promoted templates and passing fixtures while changing zero contracts, zero entrypoints and zero runtime behavior; current stage skills still encode the stale schema-first path.

**Scope:** all output modules

**Source:** repository evidence + operator direction, 2026-08-17

---

## Open architecture question O001 — Skill/agent physical organization

**Status:** resolved — see D012

Current official Claude Code architecture treats Skills and Subagents as distinct composable primitives: Skills provide reusable instructions/workflows; Subagents provide isolated workers with separate context and may preload Skills. The unresolved APEX question was **not** whether this composition is supported, but whether each current custom weekly stage agent delivers enough isolation, permissions, model specialization, parallelism or reusable worker value to justify the extra layer.

Resolved using `00-orchestration-spine/01-ARCHITECTURE-RESEARCH-PROMPT.md`. Accepted topology recorded in D012.

---

## D012 — O001 resolved: skill-owned, selectively-forked weekly runtime topology

**Status:** locked

**Decision:** Accept the researched topology as final for Module 00. Six weekly stage components become directly-executable Skills invoked with isolated `context: fork` from the central `weekly-orchestrator`, replacing their wrapper agents. Two blind reviewer agents are retained as independent Subagents because their isolation/blind-review value is functional, not incidental. `apex-session` and `apex-sync` remain the durable-mutation and deterministic-read-side backbone. `PromptEngineer`, `AIRouting`, and `model-usage-log` are loaded only on demand, never preloaded by default.

```okf
O001_resolution:
  status: accepted

  composition:
    main_session:
      - weekly-orchestrator

    forked_stage_skills:
      - PrecapWeek
      - PrecapNextDay
      - raw-flow-dump-normalize_when_needed
      - flow-recap_per_flow
      - status-merge_per_batch
      - ProjectStatus_when_requested

    retained_custom_agents:
      - apex-review-validity
      - apex-review-alignment

    direct_backbone:
      - apex-session
      - apex-sync

    on_demand_dependencies:
      - PromptEngineer
      - AIRouting
      - model-usage-log

  removed_from_active_runtime:
    - apex-precap-week
    - apex-precap-next-day
    - apex-evidence-normalize
    - apex-flow-recap
    - apex-status-merge
    - apex-project-status
```

**Rationale:** The six wrapper agents added an instruction/context layer without unique isolation, permission, model-specialization, or parallelism value beyond what `context: fork` on the owning Skill already provides. The two review agents are kept because their functional value (blind, independent, read-only judgment) depends specifically on being separate Subagents that never see producer rationale or each other's verdict.

**Scope:** orchestration spine architecture (Module 00 topology)

**Source:** architecture research (`01-ARCHITECTURE-RESEARCH-PROMPT.md` result) + operator acceptance, 2026-08-17

---

## D013 — Module 00 closed: forked-skill topology implemented and fresh-context verified

**Status:** locked

**Decision:** D012's topology is now live in production, not just decided. All twelve phases of `05-TARGET-STRUCTURE-IMPLEMENTATION-PLAN.md` are complete: central routing rewritten, all six stage Skills converted to self-contained fork workers, production routing switched and smoke-tested, `handoff-schema.md` simplified via per-field consumer audit, the authority/persistence map added, the six wrapper agents archived, role-doctrine loading cleaned up, static topology verification passed, and a fresh-context integration test (two independent subagents with no memory of this migration, given only a normal operator trigger and real repo state) passed without requiring any production fix. Full phase-by-phase provenance is in git history and `CURRENT-STATE.md`'s "Full phase record."

**Rationale:** D011 requires that runtime activation be proven by entrypoint/contract behavior a fresh invocation can produce without design-chat memory — the fresh-context test is that proof, not a promise of it.

**Scope:** Module 00 (`00-orchestration-spine`) only. Modules 01-08 (detailed output-artifact refinement) are separately scoped and not started.

**Source:** implementation + fresh-context verification, 2026-08-17

---

## Open question O002 — Is `workflow-process-design` an on-demand dependency of the accepted topology?

**Status:** unresolved; found during the post-Module-00 repair pass, 2026-08-18

D012's `on_demand_dependencies` lists `PromptEngineer`, `AIRouting`, and `model-usage-log` only. It omits the `Workflow&Processes` skill (frontmatter `name: workflow-process-design`) — yet `PrecapNextDay/SKILL.md` declares an explicit `workflow_process_unavailable` failure mode for exactly this dependency, and `PrecapNextDay/references/workflow-process-validation-contract.md` names it as an `authoritative_files` source.

Two readings, not resolved here:

- `workflow-process-design` is a real fourth on-demand dependency and D012 needs amending to include it.
- `PrecapNextDay`'s failure mode and contract reference are themselves dead/aspirational content, and nothing actually depends on this skill in the live weekly loop.

**Scope:** orchestration spine architecture (Module 00 topology) — an amendment here would touch D012 directly, so this is recorded as a question rather than silently resolved either way.

**Source:** post-Module-00 repair-pass verification, 2026-08-18

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

**Status:** superseded by Monday–Sunday amendment (2026-11-09) and canonical clock lock (2026-11-10).

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
2. **Unified `EM-13` (`G|I|P|S|O|C`):** Matrix 1 UI cards remain `L1 / L2` (no `L3` cubes), while expanded `Goal` and `Output` cells decompose into `Tasks -> Subtasks` with short drafts/examples (`Goal.acceptance`, `Input.exclusions`, `Output.redraft`). Cross-repo dependencies render inline via Option B `🔗 Cross-Repo:` clickable pills (`SPEC-PRECAP-WEEK-ITERATIONS.okf.md` §5.2).
3. **`T2` Dispersal & Section `05` (`SEQ-D1..D4`):** `MasterOfArts/Sequencing/dispersal/` (mirrored to `02-weekly-dispersal/`) owns `EPICS-SCHEMA.md`, `epics.json`, `ALGORITHM.md`, `week-demand.json`, `build_slot_inventory.py`, and `allocate_week.py` (`week-allocation.json`). Evening physical courses (`18:30–19:30`) drive Gaussian coupling (`σ = 6.0h`, `19:00` midpoint, `w_max = 1.5x`, no Fri→Sat bleed); `R` rotates via weighted round-robin (`XP = 0`, `DD-16` no numeric BP floor).
4. **Calendar Boundary (`Q10`):** `PrecapWeek` is strictly read-only for Google Calendar; gated `[FLOW]` event creation belongs exclusively to `PrecapNextDay` (`02-next-day-brief/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`).

**Scope:** `.claude/skills/PrecapWeek/`, `01-weekly-command-brief/`, `02-weekly-dispersal/`, `02-next-day-brief/`.

**Source:** operator verification & forensic execution, 2026-11-11.

---

## D021 — Single-Owner Precap Week Simplification, Machine Schemas, Compiler & OKF v0.2 Output

**Status:** locked and implemented (2026-11-11).

**Decision:**
1. **One Home Per Rule:** Consolidated all valid Precap Week UI/domain rules into [`01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md), clock windows into [`02-weekly-dispersal/week-blueprint.json`](02-weekly-dispersal/week-blueprint.json), calendar deformation into [`.claude/skills/PrecapWeek/calendar-planning-guidance.md`](../../../.claude/skills/PrecapWeek/calendar-planning-guidance.md), and eliminated `16` redundant handover/blueprint/manifest files (`HANDOVER-02..06`, `precap-week-handovers/01..07`, `weekly-blueprint-standard.md`, `weekly-blueprint-meeting-example.md`, `package-manifest.md`, `01-weekly-command-brief/README.md`; preserved at pushed baseline SHA `ad10c483`).
2. **Machine-Readable Background & Compiler:** Added Draft 2020-12 JSON schemas in [`01-weekly-command-brief/schemas/`](01-weekly-command-brief/schemas/precap-week-cockpit.schema.json) and deterministic `stdlib`-only Python compiler [`render_precap_cockpit.py`](01-weekly-command-brief/render_precap_cockpit.py) generating both the preserved interactive `v0.5` HTML Cockpit and OKF v0.2 Weekly Command Briefs + `PrecapNextDay` handoff JSON.
3. **Preserved Downstream Compatibility:** Retained `Weekly_Command_Brief` / `weekly_plan_packet` (`handoff_envelope`) and `presentation_handoff` contracts for `weekly-orchestrator` and `PrecapNextDay`.

**Scope:** `.claude/skills/PrecapWeek/`, `01-weekly-command-brief/`, `precap-week-handovers/`, `CURRENT-STATE.md`.

**Source:** operator SSOT simplification mandate, 2026-11-11.
