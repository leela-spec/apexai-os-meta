# Current State


## Active improvement state — 2026-11-11 (Precap Week & Dispersal `T1/T2` Convergence)

**Operator directive:** Ground the weekly command brief in live OpenProject work packages, the 4-flow daily structure (3x3 standard repetition), the Sequencing integration system, and Google Calendar time-blocking.

**Accepted operator decisions:** D014 OpenProject-first dependency intake (`http://127.0.0.1:8083` via `opCall.js` with `D019` `[OP-OFFLINE]` fallback); D017 Monday–Sunday planning (`week-blueprint.json`: `4 × 120m` Flows Mon–Fri `08:00–24:00`, `2 × 120m` Flows Sat–Sun `12:00–16:00`); D018/D020 `3x3` Dispersal (`T1/T2` `slot-inventory.json` + `week-allocation.json`), 6-Portfolio standard (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`), and unified `EM-13` `G|I|P|S|O|C` contract.

**Current state & verified deliverables:**
1. **Single-Owner Precap Week Specification & Modular Suite (`D021`):** Consolidated all UI/domain rules into `01-weekly-command-brief/SPEC-PRECAP-WEEK-MASTER.okf.md` and dedicated modular specifications (`SPEC-MATRIX-1-PORTFOLIOS.okf.md`, `SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md`, `SPEC-SEQUENCING.okf.md`, `SPEC-PRECAP-INTERFACES-HANDOFF.okf.md`), clock windows into `02-weekly-dispersal/week-blueprint.json`, calendar deformation into `.claude/skills/PrecapWeek/calendar-planning-guidance.md`, and eliminated redundant handover/blueprint/manifest files.
2. **Machine-Readable Compiler & Schemas (`D021`):** Added Draft 2020-12 `schemas/*.schema.json`, `render_precap_cockpit.py`, OKF v0.2 reference brief, `PrecapNextDay` handoff fixture, and compiled `v0.5` cockpit `precap-week-cockpit-2026-W46.html` (`#s00..#s05`, 6 Portfolio Areas, unified `EM-13` `G|I|P|S|O|C`).
3. `T1/T2` Dispersal generated & mirrored: `02-weekly-dispersal/slot-inventory.json`, `02-weekly-dispersal/epics.json`, and `02-weekly-dispersal/week-allocation.json` (`240` bound slots, `2,880m` Flow TP, `3,706.0` XP, `100.0` BP); GCal writer moved to `02-next-day-brief/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`.

**Next action:** Module 02 (`02-next-day-brief` / `PrecapNextDay`) intake using the unified `presentation_handoff` and `week-allocation.json`.

**Verification note:** `render_precap_cockpit.py` (`--validate-only` + compile), `okf_validator.py` (`0` errors on `01-weekly-command-brief/`, `fixtures/`, `02-weekly-dispersal/`, `precap-week-handovers/`), Playwright desktop/mobile (`0` console errors, `0` overflow), and forked `PrecapWeek` `D011` smoke test passed; `0` broken links across `80` checks and `0` drift hits; post-write OP mutations remain dry-run.

---

## Historical Archive & Module 00 Provenance

**Archived History:** Module 00 completion diary, post-closure repair pass, and 12-phase execution record have been archived to [`apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/MODULE-00-CLOSURE-DIARY.md`](../../archive/weekly-orchestration/topology-pre-forked-skills-2026-08/MODULE-00-CLOSURE-DIARY.md).

**Live Topology (`D012`):** Central `weekly-orchestrator` dispatches six stage components (`PrecapWeek`, `PrecapNextDay`, `raw-flow-dump-normalize`, `flow-recap`, `status-merge`, `ProjectStatus`) with isolated `context: fork`, supported by two blind reviewer agents (`apex-review-validity`, `apex-review-alignment`), `apex-session`/`apex-sync` backbone, and on-demand dependencies (`PromptEngineer`, `AIRouting`, `model-usage-log`).
