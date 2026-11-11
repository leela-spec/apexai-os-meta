# Current State


## Active improvement state — 2026-11-11 (Precap Week & Dispersal `T1/T2` Convergence)

**Operator directive:** Ground the weekly command brief in live OpenProject work packages, the 4-flow daily structure (3x3 standard repetition), the Sequencing integration system, and Google Calendar time-blocking.

**Accepted operator decisions:** D014 OpenProject-first dependency intake (`http://127.0.0.1:8083` via `opCall.js` with `D019` `[OP-OFFLINE]` fallback); D017 Monday–Sunday planning (`week-blueprint.json`: `4 × 120m` Flows Mon–Fri `08:00–24:00`, `2 × 120m` Flows Sat–Sun `12:00–16:00`); D018/D020 `3x3` Dispersal (`T1/T2` `slot-inventory.json` + `week-allocation.json`), 6-Portfolio standard (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`), and unified `EM-13` `G|I|P|S|O|C` contract.

**Current state & verified deliverables:**
1. **Single-Owner Precap Week Bundle (`D021`):** Consolidated all UI/domain rules into `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`, clock windows into `02-weekly-dispersal/week-blueprint.json`, calendar deformation into `.claude/skills/PrecapWeek/calendar-planning-guidance.md`, and eliminated `16` redundant handover/blueprint/manifest files (preserved at baseline `ad10c483`).
2. **Machine-Readable Compiler & Schemas (`D021`):** Added Draft 2020-12 `schemas/*.schema.json`, `render_precap_cockpit.py`, OKF v0.2 reference brief, `PrecapNextDay` handoff fixture, and compiled `v0.5` cockpit `precap-week-cockpit-2026-W46.html` (`#s00..#s05`, 6 Portfolio Areas, unified `EM-13` `G|I|P|S|O|C`).
3. `T1/T2` Dispersal generated & mirrored: `02-weekly-dispersal/slot-inventory.json`, `02-weekly-dispersal/epics.json`, and `02-weekly-dispersal/week-allocation.json` (`240` bound slots, `2,880m` Flow TP, `3,706.0` XP, `100.0` BP); GCal writer moved to `02-next-day-brief/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md`.

**Next action:** Module 02 (`02-next-day-brief` / `PrecapNextDay`) intake using the unified `presentation_handoff` and `week-allocation.json`.

**Verification note:** `render_precap_cockpit.py` (`--validate-only` + compile), `okf_validator.py` (`0` errors on `01-weekly-command-brief/`, `fixtures/`, `02-weekly-dispersal/`, `precap-week-handovers/`), Playwright desktop/mobile (`0` console errors, `0` overflow), and forked `PrecapWeek` `D011` smoke test passed; `0` broken links across `80` checks and `0` drift hits; post-write OP mutations remain dry-run.

---

**Project phase:** Module 00 CLOSED (`ad95d50d..8c6c50ea`); Module 01 (`01-weekly-command-brief` / `PrecapWeek`) & `T1/T2` Dispersal (`02-weekly-dispersal/`) converged under `D014–D021`. Ready to open Module 02 (`02-next-day-brief`).

**Active module:** `01-weekly-command-brief` closing into `02-next-day-brief` (`PrecapNextDay`).

**Accepted topology (D012, O001 resolved), now live:** one main-session `weekly-orchestrator`; six stage components (`PrecapWeek`, `PrecapNextDay`, `raw-flow-dump-normalize`, `flow-recap`, `status-merge`, `ProjectStatus`) executed as directly-dispatched Skills with isolated `context: fork`; two retained blind reviewer agents (`apex-review-validity`, `apex-review-alignment`); `apex-session` (durable mutation) and `apex-sync` (deterministic read-side) as direct backbone; `PromptEngineer`/`AIRouting`/`model-usage-log` loaded on demand only.

## Module 00 completion state

```yaml
module_00:
  topology: accepted_and_active
  central_runtime: corrected
  wrapper_agents_active: 0
  reviewer_agents_active: 2
  forked_stage_skills_active: 6
  stale_global_authority: known_unresolved  # 2 items intentionally deferred, not a defect -- see "Post-closure repair pass" below
  fresh_architecture_test: pass  # scope: dispatch/routing/gates/bypass rules only -- did NOT exercise stage supporting_files load paths; that gap is now closed by the repair pass below and folded into future acceptance criteria
  next_module: 01_weekly_command_brief
```

**Fresh-context integration test (Phase 11/J): PASS.** Two independent Explore subagents with zero memory of this migration were given only a normal operator trigger ("resume the weekly loop") plus, for the second, a synthetic evidence-intake scenario — no architecture rationale, per `TEST-PROTOCOL.md`'s fresh-context rule. Both derived the entire dispatch architecture purely from repo content:
- Correctly routed `.claude/CLAUDE.md` -> `weekly-orchestrator/SKILL.md`, correctly distinguished it from Multi-Agent Orchestration.
- Correctly read real W34/2026-08-17 artifacts to determine the actual current loop position (G2 pending confirmation) rather than assuming a scripted stage.
- Correctly identified all six wrapper agents as retired/archived, not current dispatch targets — while correctly *not* being confused by old `produced_by: apex-precap-week`-style fields inside pre-migration historical artifacts (expected, per the plan's rule against editing historical generated content).
- Correctly applied the `raw-flow-dump-normalize` bypass/invoke rule, the `flow-recap` parallel-per-flow dispatch, the conditional `model_usage_delta` inclusion rule, the review-wiring trigger test (including a contradiction scenario correctly triggering review), and `status-merge`'s proposal-only boundary (a direct-mutation attempt correctly identified as rejected, routed to `apex-session`).

No production fixes were needed as a result of the test — both agents' findings matched the intended design exactly. Full agent transcripts are in this conversation's history; not persisted here to keep this file compact (per the instruction not to turn this into a diary).

## Post-closure repair pass — CLOSED

A follow-up sweep (after Module 00 closure, before Module 01 opened) found what the fresh-context test above genuinely missed: it exercised dispatch/routing/gates, never a stage's own `supporting_files` load path. All planned items resolved; two genuinely belong to a later module and are recorded there instead of fixed here.

1. Collapsed YAML in 4 PrecapWeek files (up to 4424-char single lines) — **fixed**, commit `0720e6aa`.
2. Collapsed YAML in `PromptEngineer/SKILL.md` — **fixed**, commit `11db9f54`.
3. Fail-unsafe generation scaffolding (a live entrypoint instructing file creation) in `AIRouting/SKILL.md` + 6 contract files — **fixed**, commit `f8a9896b`.
4. Wrong J02 template path in Module 01's own `HANDOVER.md` — **fixed**, commit `0e0fca77`.
5. Stale activation report claiming `active_and_ready` while its own numbers said `contracts_changed: 0` — **fixed** (precedence marker to D011), commit `1c405cdc`.
6. `fresh_architecture_test` scope qualifier + `stale_global_authority` correction (this file) — **fixed**, commit `8f380b86`.
7. ProjectStatus duplicate inventory (divergent versions, competing entrypoint claim) — **recorded** in `08-project-status/README.md`; **not resolved** (Module 08's content decision). Stale folders archived per operator instruction — commit `72105900`.
8. `workflow-process-design` missing from D012's on-demand dependencies despite `PrecapNextDay` declaring a failure mode for it — **logged as open question O002** in `DECISIONS.md`, commit `d46d6d4a`. Not resolved either way.
9. 28 broken `supporting_files` declarations across `AIRouting`, `PromptEngineer`, `Workflow&Processes` (shared skills, not owned by this project) — **fixed** by repointing each skill's own declarations to its real files, no moves/renames — commit `7b53bcd3`.
10. Two stale ProjectStatus folders archived — folded into item 7's commit `72105900`.
11. **Found during final verification, not in the original 10-item list:** 22 more files with the identical fail-unsafe scaffolding tail from item 3 — 9 in `PrecapNextDay/references/` (project-owned), 6 in `PromptEngineer/`, 7 in `Workflow&Processes/`. Confirmed with the operator before fixing given the 3x scope increase and first occurrence in a project-owned package. **Fixed**, commit `3c0d50b0` — including a caught-and-corrected truncation mistake (one file had a legitimate example containing a decoy `---`/`# VALIDATION` heading; verified no other file shares that trap before committing).

**Remaining, by design, not oversight:** ProjectStatus's 4 broken pointers (item 7) and `Workflow&Processes`'s `sprint-structure-rules.md` (declared, doesn't exist anywhere — logged inline in its `SKILL.md` as an open question) are both content-authority decisions outside Master repair scope. `stale_global_authority: known_unresolved` reflects exactly these two, nothing else.

## Full phase record (for provenance; Module 01 does not need to re-read this)

1. Phase 1/2 — record decision + `.claude/Claude.md` -> `.claude/CLAUDE.md`. Commits `ad95d50d`, `e24d3039`.
2. Phase 3 — central routing rewrite. Commit `91efd902`.
3. Phase 4 — all six Skills converted to fork workers. Commits `fda9645f` (PrecapWeek), `7478f4b5` (PrecapNextDay), `7c3b1324` (raw-flow-dump-normalize), `c6c2db56` (flow-recap), `46f4561b` (status-merge), `8c6c50ea` (ProjectStatus).
4. Phase 5 — routing switch + smoke test. Commit `47a01154`.
5. Phase 6 — handoff-schema.md field audit. Commit `3aee01c3`.
6. Phase 7 — authority/persistence map. Commit `d8d0d25e`.
7. Phase 8 — archive six wrapper agents. Commit `34bfbcb0`.
8. Phase 9 — doctrine cleanup (meta-strategy-doctrine.md orphan fix). Commit `4dc3d7a8`.
9. Phase 10 — static topology verification. No code change (verification-only), recorded in prior commit.
10. Phase 11 — fresh-context test. PASS, recorded above.
11. Phase 12 — closure. This file + `apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER.md`.

**Open decision:** none architectural or implementation-level remaining for Module 00.

**Next action:** operator decides when to open Module 01. Starting context for that work is `01-weekly-command-brief/HANDOVER.md` — it does not need this file's phase-by-phase history, only its `module_handover` block.

**Regression fixture:** Existing W34 planning/run artifacts (`artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md`, `artifacts/next-day-plans/next_day_plan-20260817.md`, `artifacts/flow-packets/20260817/`) and the `US-SEQ-01` simulation fixture set.

**Original scaffold commit:** `9d2811bb7e34a45a49883d9a31774887d6d95606`
