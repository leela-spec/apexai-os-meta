---
type: Adapter
id: HO-PW-DEC-03
title: "Handover 03 — Section 01 Operator Decision Brief (New / Ongoing / Standard + G1)"
description: "Documents the v05 3-card collapsible Decision Brief contract, catches the Mon/Wed vs Mon-Wed and unverified OPERATOR OVERRIDE bugs in v03.html, and reconciles config dials with Gate G1 approvals."
status: current
date: 2026-11-11
tags: [weekly-orchestration, operator-decisions, handover-04, v05, gate-g1]
---

# 03 · Handover: Section `01 · Operator Decision Brief`

## 1. Purpose

Stabilize Section `01 · Operator Decision Brief` so it cleanly presents weekly configuration levers (`New | Ongoing | Standard`) **and** explicit Gate `G1` approvals (`PROPOSED | APPROVED | REJECTED | DEFERRED`), without fabricating overrides or repeating stale dropdown toolbars.

---

## 2. Input & Priority Ledger

| Priority | Source Path | Role & Grounding | Ignore / Exclude |
|---|---|---|---|
| **P1 (Spec)** | `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md:21,96-109,302` | Section `01` collapse semantics, strict **`New \| Ongoing \| Standard`** left-to-right order, preview summaries (`UX-01`). | Reintroducing standalone control toolbars. |
| **P1 (Module Spec)** | `01-weekly-command-brief/HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN.okf.md` | Canonical `01` bucket rules (`New`, `Ongoing`, `Standard`) and Override Evidence Anti-Drift Rule (`:44`). | Stale line `:24` row anatomy (`Dropdown Selector + (i) Button`) contradicted by `:60,66`. |
| **P1 (Clock Owner)** | `02-weekly-dispersal/week-blueprint.json:43-68,219-223` | Authoritative `Mon–Wed` `Project Night (20:30–22:00)`, `Thu–Fri` `Freizeit`, `Sat–Sun 12:00–16:00`, `Day Outro 22:00–22:30`, `Saturday_or_Sunday` StatusMerge. | Legacy `Sun OFF` / `21:00` defaults or `Mon & Wed` mismatches. |
| **P2 (Governance)** | `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md` (`93ebded1` `v1.0`) & `.claude/skills/PrecapWeek/weekly-command-brief-template.md:9-15` | Explicit Gate `G1` sign-off structure (`[P0-P3 \| I/E/R]`, Anchor, Action Required, `PROPOSED \| APPROVED \| REJECTED \| DEFERRED`). | Mixing gate state silently into UI text without provenance. |
| **Prototype Audit** | `01-weekly-command-brief/precap-week-cockpit-W45-actual-data-v03.html:20,33-76` | Working `<details class="vitem">` collapse mechanics (`#toggle-01`, `#cards-01`). | Unverified `ov:true` overrides (`:41-42`) & misrouted `WC Meister` (`New` vs `Ongoing`). |

---

## 3. Forensic Diff — Latest vs Added (`Nov 9–11`) vs Lost / Broken

### Locked State & Additions (`Nov 9–11`)
- **Whole-section collapse with live previews (`HANDOVER-04:15,64-66`):** Closed by default (`#cards-01 data-open="false"`); header retains **3 visible preview cards in order `New | Ongoing | Standard`** showing short `setting: value` summaries (empty category-only headers prohibited).
- **Bucket separation (`HANDOVER-04:28-43,71`):**
  - `New`: Weekly topic changes (`F1–F4`), scope pauses, special project evenings, verified overrides.
  - `Ongoing`: Carried work and ambient calendar holds (declined/ignored events stay visible without becoming tasks).
  - `Standard`: Standing OP intake rules, `3×3` Flow cadence (`4 Mon–Fri / 2 Sat–Sun`), and `week-blueprint.json` clock.
- **Anti-Drift Override Rule (`HANDOVER-04:44`):** `OPERATOR OVERRIDE` badge may render **only** when **both** `(a) baseline default` and `(b) operator choice` are verified by source evidence; otherwise mark `unverified`.
- **Demoted Nov 9 -> Nov 10:** Reordered `Standard | New | Ongoing` -> `New | Ongoing | Standard`; retired dense `[Label : Value ▾] [(i)]` toolbar/dropdown buttons (`diff:239-289`); removed `21:00 Shutdown` & `Sun OFF` (`diff:233,273`); removed ungrounded `<5s` timing claims (`diff:298`).

### Specific Bugs & Losses Exposed in `v03.html` & `HANDOVER-04`
1. **Stale Row Anatomy Inside `HANDOVER-04:24`:** Still prints `[Category Tag] + [Variable Label] + [Active Value Chip / Dropdown Selector] + [(i) More Info Button]`, contradicting `:60,66` (`<details>` inline reveal, zero extra `(i)` button strip).
2. **`Mon & Wed` vs `Mon–Wed` Contradiction:** `HANDOVER-04:29` and `v03.html:44` title `"Mon & Wed Project Night (20:30-22:00)"`, while `v03.html:44` detail prose and `week-blueprint.json:43-54` both lock **Monday, Tuesday, AND Wednesday** as `Project Night (20:30–22:00)`.
3. **Unverified `OPERATOR OVERRIDE` Violations (`v03.html:41-42`):** `D-W45-02 · WC Meister` and `D-W45-03 · Leela weekly scope` render `ov:true` (`OPERATOR OVERRIDE`) without stating the system/OP default (`opCall.js` was never called in `v03.html`), violating `HANDOVER-04:44`.
4. **`New` vs `Ongoing` Routing Contradiction (`v03.html:41`):** Places `WC Meister` (background calendar event ignored) inside **`New`** instead of **`Ongoing`**, violating `HANDOVER-04:30,42,71` (`WC Meister`, `Munich Dance` belong in `Ongoing`).
5. **Lost Gate `G1` Approval Semantics (`v1.0` -> `v05`):** Early specs carried `[P0 | I/E/R]` + explicit `PROPOSED | APPROVED | REJECTED | DEFERRED` state for `G1`. `v05` (`01`) turns decisions into passive display cards without stating which rows block `G1` sign-off.

---

## 4. Process & Anti-Drift Boundaries

- Enforce `<details>` accordion inside `#cards-01` — no duplicate control bar above or below cards.
- Every `New` override row MUST store `{system_default, operator_choice, evidence_ref, gate_status}`. Render `OPERATOR OVERRIDE` ONLY if `system_default != operator_choice` and both cite real artifacts/operator input; else label `UNVERIFIED`.
- Dynamically hydrate `Standard` directly from `week-blueprint.json` + `opCall.js` status (`ONLINE | [OP-OFFLINE]`) — never hardcode clock numbers in prose.
- Route calendar event holds & declines cleanly into **`Ongoing`** (non-task holds); route deliberate weekly theme overrides & scope pauses into **`New`**.

---

## 5. Output & Concrete Examples

### Canonical Targets to Update
1. `01-weekly-command-brief/HANDOVER-04-OPERATOR-DECISION-BRIEF-VARIABLE-DROPDOWN-REDESIGN.okf.md` (patch `:24` `<details>` anatomy, resolve `Mon–Wed` vs `Mon & Wed`, lock `G1` approval field, move `status: ready_for_operator_verification` -> `current`).
2. `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md` (`§4.2`).
3. `01-weekly-command-brief/precap-week-cockpit-W45-actual-data-v03.html` (`decisionCards` `#s01`).

### Concrete Row Data Shape (`New | Ongoing | Standard`)
```json
{
  "bucket": "New",
  "id": "DEC-W46-01",
  "title": "Mon–Wed Project Night themes (20:30–22:00)",
  "active_value": "Mon/Wed Studio & Content; Tue Billing sprint",
  "system_default": "week-blueprint.json weekday_project (Mon-Wed Project Night, unsplit)",
  "operator_choice": "Mon/Wed theme split supplied in Operator Weekly Command Brief",
  "override_verified": true,
  "gate_status": "PROPOSED_FOR_G1",
  "source_ref": "operator_weekly_command_brief#special_evenings"
}
```
```json
{
  "bucket": "Ongoing",
  "id": "CAL-W46-01",
  "title": "WC Meister (Thu evening hold)",
  "active_value": "IGNORED — Keep Thu Freizeit untouched",
  "system_default": "Google Calendar busy event",
  "operator_choice": "calendar_ignores: WC Meister",
  "override_verified": true,
  "gate_status": "CONFIRMED_INPUT",
  "source_ref": "gcal:primary + operator_weekly_command_brief"
}
```

---

## 6. Operator Resolution Ledger (`DEC-Q1..Q2` — Ratified `2026-11-11`)

1. **`Mon–Wed` vs `Mon/Wed` (`Project Night`):** **Ratified:** `Mon + Tue + Wed` all run `20:30–22:00` `Project Night` per `week-blueprint.json` (`Standard` baseline), while week-specific theme splits (e.g., `Mon & Wed` themed evenings) sit in `New`.
2. **Gate `G1` Sign-Off Inside `01`:** **Ratified Option A:** Render a compact `G1: PROPOSED / APPROVED` chip on `New` decision items inside Section `01`, and require verified `{system_default, operator_choice, source_ref}` before showing `OPERATOR OVERRIDE` (`WC Meister` routed to `Ongoing`).

---

## 7. Definition of Done (DoD)

1. `HANDOVER-04:24` matches `:60,66` (`<details>` accordion, zero duplicate toolbar/dropdowns).
2. Zero unverified `OPERATOR OVERRIDE` badges (`v03.html:41-42` repaired or marked `unverified`).
3. Calendar holds (`WC Meister`, `Munich Dance`) live cleanly inside `Ongoing`; weekly choices/pauses in `New`; `week-blueprint.json` clock rules in `Standard`.
4. Fresh render verifies collapsed `#cards-01` still shows legible `setting: value` previews across `New | Ongoing | Standard` at desktop & mobile widths.

## 8. Fresh-Chat Starter Prompt

```text
Read apex-meta/tools/project-improvement-orchestration-weekly/precap-week-handovers/03-HANDOVER-OPERATOR-DECISIONS.md and 00-RULE-CANONICAL-DECISION-LOCK.md.
Resolve the Mon/Wed vs Mon-Wed Project Night rule and G1 approval chip choice with me, fix HANDOVER-04:24, enforce the verified system_default -> operator_choice guard on every OPERATOR OVERRIDE row, move calendar holds into Ongoing, and update SPEC §4.2 + Cockpit #s01 cleanly.
```
