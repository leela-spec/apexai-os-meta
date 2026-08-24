# Week 1 — Scoping, Governance & SSoT Lock (Lika & ACIM)

```
week_theme: scoping_governance_and_ssot_lock
primary_projects: [Lika, ACIM]
secondary_projects: [Apex]
exit_gate: G1_SSoT_Lock
blueprint_basis: weekly-blueprint-standard.md (standard no-meeting weekday)
project_flow_priority_applied: Lika > MasterOfArts(ACIM) > Apex > Investment(deferred) > Residual
time_precision: 15-minute internal precision, block-level human output
```

## Week Outcome Statement

By Friday's day_outro, every document in `Lika/` and `ACIM/` is either declared
canonical or redirected to a canonical file via the new SSoT index; governance
decision logging is live; the scope-lock addendum for both families is accepted.
Apex receives exactly two blocks of orchestration hygiene work and nothing more.

## Daily Block Breakdown

### Monday — Inventory & Governance Bootstrap

- **Morning routine** (fixed): wake anchor → hydration + 10-min mobility →
  review of this week's plan + gate G1 checklist → intention setting. No project work inside block.
- **work_flow_1 (Lika)**: Full file inventory of `Lika/` including
  `Lika Operating System/`, `UpdateProcessSSOTS/`, `Research Files & Problems/`,
  `workshops/`, `marketing/`. Record path, purpose-guess, last-modified. Output:
  `Lika/SSoT/inventory-lika.md`.
- **work_flow_2 (ACIM)**: Same inventory for `ACIM/`
  (`content/`, `marketing/`, `workshops/`, `sources/`, therapy docs DE/EN).
  Output: `ACIM/SSoT/inventory-acim.md`. Flag obvious duplicates
  (e.g. CouplesTherapy.md vs CouplesTherapy_DE.md — language variants, not dupes; record rule).
- **lunch_prep / lunch_break** (fixed): protected.
- **admin_or_2Do**: Open governance decision log at
  `Orchestration/decision-runs/2026-W35-decision-log.md`; write entries D-001…D-003
  (inventory rules, language-variant rule, SSoT index location). Kanban board seeded with G1 tasks.
- **work_flow_3 (Lika)**: Draft SSoT index schema: canonical_id, path, owner,
  status (canonical/redirect/archive), redirect_target.
- **work_flow_4 (Apex)**: Verify Orchestration ADR pointers still resolve
  (00-MCDA through 09-handover). Read-only pass; note broken references only.
- **Evening** (physical_social_or_evening_blocks): physical block (training/walk) — preserve.
- **day_outro** (fixed): shutdown ritual — commit inventory files, log day summary, preview Tuesday.
- **sleep_routine** (fixed): boundary enforced.

### Tuesday — Canonicalization Sprint

- **Morning routine** (fixed): as standard + 5-min review of yesterday's inventory counts.
- **work_flow_1 (Lika)**: Populate `Lika/SSoT/index.yaml`: declare canonical
  files for Operating System, shift-schedule review checklist, workshop shells,
  marketing assets. Every non-canonical file gets status=redirect or archive.
- **work_flow_2 (Lika)**: Resolve conflicts found during indexing — same-topic
  files in two locations. Decision per conflict logged (D-004+). No silent deletions.
- **lunch_prep / lunch_break** (fixed): protected.
- **admin_or_2Do**: Inbox/2Do sweep capped at one block; anything touching Lika/ACIM
  routed into the index as a task instead of being done inline.
- **work_flow_3 (ACIM)**: Populate `ACIM/SSoT/index.yaml`; canonical sources in
  `sources/` take precedence over inline citations elsewhere.
- **work_flow_4 (ACIM)**: Reconcile marketing claims in `ACIM/marketing/`
  against locked content — flag overclaims for Thursday rewrite, don't fix yet.
- **Evening**: social/evening block — preserve if realistic; compress with reason if indexing overran.
- **day_outro / sleep_routine** (fixed).

### Wednesday — Cross-Family Reconciliation (hardest day)

- **Morning routine** (fixed): standard + explicit energy check; Wednesday carries peak cognitive load.
- **work_flow_1 (Lika↔ACIM)**: Cross-family overlap scan: shared vocabulary,
  duplicated source material, contradictory guidance between Lika ops docs and
  ACIM therapeutic content. Output: `Orchestration/weekly-simulations/Week-01/cross-family-overlap.md`.
- **work_flow_2 (Lika)**: Fix overlaps inside Lika scope only; anything needing
  ACIM-side edits queued as tasks with exact file paths.
- **lunch_prep / lunch_break** (fixed): protected.
- **work_flow_3 (ACIM)**: Execute queued ACIM-side fixes; re-run duplicate scan to zero.
- **admin_or_2Do**: Update decision log (D-008…D-012); prune Kanban stale items.
- **work_flow_4 (Apex)**: Write scope-lock addendum draft:
  `Orchestration/03-SCOPE-LOCK-addendum-W1-lika-acim.md` — what is IN scope for
  Weeks 1–5 per family, what is explicitly out.
- **Evening**: recovery-weighted evening (no social commitment after heavy day) — blueprint's avoid_overfilling rule applied.
- **day_outro / sleep_routine** (fixed).

### Thursday — Validation & Acceptance

- **Morning routine** (fixed): standard.
- **work_flow_1 (Lika)**: Validation pass — script/checklist walk of
  `Lika/SSoT/index.yaml`: every listed path exists; every file under `Lika/`
  appears exactly once (canonical or redirect). Fix violations.
- **work_flow_2 (ACIM)**: Same validation for ACIM index + rewrite flagged
  marketing overclaims from Tuesday against locked content.
- **lunch_prep / lunch_break** (fixed): protected.
- **admin_or_2Do**: QMD index refresh check (`moa-lika`, `moa-acim`) so retrieval reflects post-lock reality; note any stale chunks.
- **work_flow_3 (Governance)**: Persona stress-test round 1 — run The Auditor
  and The Skeptic personas against the SSoT lock (see persona section below);
  record findings and remediate blockers only.
- **work_flow_4 (Apex)**: Finalize scope-lock addendum; mark ACCEPTED in decision log (D-013).
- **Evening**: physical/social block — full preservation earned by lighter load.
- **day_outro / sleep_routine** (fixed).

### Friday — Gate Review & Handoff Seed

- **Morning routine** (fixed): standard + read gate G1 checklist top to bottom.
- **work_flow_1**: Gate G1 execution — walk all four checklist items from
  `00_SIMULATION_OVERVIEW.md`; collect evidence paths for each checkbox.
- **work_flow_2 (ACIM/Lika residual)**: Close remaining redirects; archive list
  written but archives NOT deleted (operator decision reserved).
- **lunch_prep / lunch_break** (fixed): protected.
- **admin_or_2Do**: Decision log finalization for week (D-001…D-015 target); Kanban end-of-week sweep.
- **work_flow_3**: Write Week 2 handoff seed: what W2 curricula may consume
  (locked doc IDs), known gaps, open questions. Save to `Week-01/handoff-to-week-02.md`.
- **work_flow_4 (Residual)**: Residual overflow block — capture anything displaced during the week; lowest priority respected.
- **Evening**: light social/evening block; week-close reflection (10 min max).
- **day_outro / sleep_routine** (fixed). Sunday precap session prepares Week 2.

## Conflict Handling Applied This Week

| Situation | Response per blueprint |
|---|---|
| Wednesday overlap scan threatens work_flow_3 | Compressed admin_or_2Do, reason recorded |
| Thursday validation overrun risk vs evening block | Deferred overflow to Friday work_flow_2, evening preserved |
| Residual items competing with fixed project work | Kept lowest; single Friday block granted |

## Persona Stress Tests (W1)

- **The Auditor**: demanded evidence paths for each gate checkbox → satisfied by Friday work_flow_1 output. Finding: pre-W1 provenance was weakest link; decision log closes it.
- **The Operator**: flagged that Wednesday's dual-family reconciliation exceeds a single morning block if inventories exceed ~150 files → mitigation: hard timebox + defer-with-reason to Thursday work_flow_1.
- **The Skeptic**: challenged "canonical" declarations lacking acceptance criteria → added rule: a canonical file must state owner + review date in frontmatter.
- **The Integrator**: warned Lika ops vocabulary and ACIM therapeutic vocabulary will collide again in W2/W4 → logged for W5 glossary task.

## Exit Criteria (Gate G1)

All four G1 checkboxes evidenced; decision log ≥ 15 entries; handoff seed exists;
zero unresolved red-status conflicts in either SSoT index.
