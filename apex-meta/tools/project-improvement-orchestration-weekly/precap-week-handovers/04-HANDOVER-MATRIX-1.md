---
type: Adapter
id: HO-PW-M1-04
title: "Handover 04 — Section 02 Matrix 1 (Non-Temporal Goals, G|I|P|S|O|C, Live OP, Cross-Repo Edges)"
description: "Complete Matrix 1 forensic baseline consolidating HANDOVER-01/03/06/MATRIX-1 and OP intake evidence; tracks v05 L1/L2 + 6-col locks, dropped EM-13/shortlist/longlist/🔗 pills, and fake W45 data."
status: current
date: 2026-11-11
tags: [weekly-orchestration, matrix-1, g-i-p-s-o-c, openproject, cross-repo, handover-03]
---

# 04 · Handover: Section `02 · Matrix 1` (Non-Temporal Architecture)

## 1. Purpose

Finalize Matrix 1 as the non-temporal portfolio architecture surface (`L1 Priority Goals` + folded `L2 Nice-to-Haves`, 6-column `G|I|P|S|O|C` specification, verified live OpenProject provenance, cross-repo dependency pills, and clean `Selected_Work_Reference` export to Matrix 2).

---

## 2. Input & Priority Ledger

| Priority | Source Path | Role & Grounding | Ignore / Exclude |
|---|---|---|---|
| **P1 (Cockpit Lock)** | `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md:22,112-156,303-305` | `v05` Matrix 1 laws (`<=3` L1 header previews, vertical dynamic projects, horizontal `L1`, folded `L2`, NO `L3`, NO recursive child-cube trees, single-row `G\|I\|P\|S\|O\|C` with NO extra heading). | Fixed 5-project assumption; bottom SVG/Mermaid chart (`DEPRECATED_UNDER_RESEARCH`). |
| **P1 (6-Col Contract)** | `01-weekly-command-brief/HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR.okf.md` (`ec3e12f3`) | Canonical `G\|I\|P\|S\|O\|C` semantics (`Input.sources` vs `upstream_dependencies` vs `exclusions`, `Goal.acceptance`, `Continuation.downstream`, OP `## Heading` proposal). | Stale Table 2.3.B (`:87-89`) still citing `"G-I-P-S-O drawer"` & top breadcrumbs. |
| **P1 (Live OP Proof)** | `00-openproject-dependency-intake/HANDOVER-20261106.okf.md` & `EVIDENCE-20261106.okf.md` | Live `:8083` `opCall.js` pagination rules + verified Nov 6 OP dataset (`15` projects, `91` relations `OP-REL#80–91`, Apex `#139/#198/#222`, IPOS `#223–228`, MoA `#163/#204`, Leela `#39–48` + Skill Tree). | Fabricated tokens `WP-BIZ-01`, `WP-APEX-01`, unverified `#232/#233/#188`. |
| **P1 (Design Frame)** | `01-weekly-command-brief/HANDOVER-MATRIX-1-DESIGN-ASSUMPTION-FIRST-20261106.okf.md` & `research/MATRIX1-R1-WORKING-DESIGN-20261106.okf.md` | `V3` progressive drilldown lock (`:233,254`), required Shortlist/Longlist (`:234`), flexible shortlist counts (`M1-D05`), `I/E/R` (`E=evidence`), OP vs Git build truth (`:309`), `Matrix 1 -> Matrix 2` reference contract (`:287-299`). | Unapplied R2 mocks / temporary `W45-LOCAL-*` slugs once live OP runs. |
| **P1 (Cross-Repo DAG)** | `01-weekly-command-brief/HANDOVER-06-CROSS-PROJECT-DEPENDENCY-VIEW-RESEARCH.okf.md` | Option B (`🔗 Cross-Repo:` inline clickable pills on L1 cubes) recommended (`:42,45-51`); bottom DAG deprecated (`:65`). | Wrong cite at `:62` (`M5 -.-> I2`; `generate_northstar_html.py:732-734` drew 3 edges). |
| **Archive Candidate** | `01-weekly-command-brief/HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md` | Only its `[OP-OFFLINE]` concept (`D019`) & non-temporal rule (`no Seq 1-4`). | Formally superseded 5-tier 30m sprint rules, fixed 5-project list, Mermaid DAG (`HANDOVER-MATRIX-1:47-64`). |

---

## 3. Forensic Diff — Latest vs Added (`Nov 9–11`) vs Lost / Broken

### Locked State (`ec3e12f3` `v05`)
- Collapsible Section `02` keeps `<=3` L1 priority preview cards (`#m1-previews`) when collapsed (`v03.html:21,77-81`); `@media print` expands all hidden views.
- Expanded view stacks dynamic projects vertically; each project shows horizontal `L1 Priority Goals` + folded `L2 Nice-to-Haves` (**zero `L3`**, **zero recursive cube trees**, **zero calendar times or 30m sprints**).
- Clicking any `L1` or `L2` card toggles **one** single-row 6-col panel directly underneath that `(repo, layer)` strip: **`G Goal | I Input | P Process | S Skills | O Output | C Continuation`** with **no visible spec heading**.
- Namespace strictly protected: Matrix 1 `P` (Process) & `C` (Continuation) never collide with Matrix 2 / Flow `P/M/R` or `C` (30m Craft sprint).

### Seven Critical Losses, Conflicts & Incomplete Features Found
1. **Live OpenProject Ignored in `v03.html`:** `v03.html:23,27` ran zero `opCall.js` reads; retains phantom tokens (`WP-BIZ-01`, `WP-APEX-01`), cites WPs absent from `EVIDENCE-20261106` (`#232, #233, #188`), omits verified Apex/IPOS WPs (`#139, #198, #222, #223, #225`), and leaves `upstream: []` on 12/13 L1 goals despite 91 live OP relations!
2. **Dropped `Goal.acceptance` & `Input.exclusions` + Unresolved `EM-13`:** `HANDOVER-03:34-35,55` requires `Goal` acceptance evidence and explicit `Input` exclusions; **both were dropped** in `v03.html:89-90`! `EM-13` (`Input | Sources | Process | Skills | Output | Redraft`) vs `G|I|P|S|O|C` and `{{var}}` vs `${var}` remain unresolved (`HANDOVER-03:41`), alongside the OP `## Heading` WP `description` sync proposal (`:42-43,92-93,107`).
3. **Dropped Cross-Repo `🔗` Pills (`HANDOVER-06`) & `➔` / `⚡` Cues:** `v03.html` deleted the bottom SVG DAG **without implementing Option B (`🔗` clickable pills on L1 cubes)**, lost `moa-billing -> IPOS` edge (`v03.html:27` vs `HANDOVER-06:41,50`), and removed any visual `⚡` distinction on L1 critical-path cards.
4. **Shortlist/Longlist + Readiness + Matrix 2 Handoff Lost:** `HANDOVER-MATRIX-1` (`:144,150,234,287-299`) & `MATRIX1-R1` (`:234-235,259`) locked Shortlist vs Longlist (deferrals with reason + revisit trigger), iteration/review loops, readiness flags, and explicit `selected_work_reference` export to Matrix 2. `v03.html:27` dumped future-phase/backlog WPs (`#204`, `Stripe`, `#227`) into `L2 Nice-to-Haves` with caution flags!
5. **Portfolio Scope Ambiguity (`M1-D10`):** `"Priority Website"` (`HANDOVER-01:38`) disappeared without classification; `"Residuals"` remains Repo 5 in `v03.html:27` (`op: "No OpenProject identity supplied"`) even though `HANDOVER-MATRIX-1:80` routed personal routines to Sequencing rather than project DAGs.
6. **Stale Residue Inside `HANDOVER-03`:** Lines `87-89` still say `"Inside clicked G-I-P-S-O drawer"` and top breadcrumbs despite the `ec3e12f3` `G|I|P|S|O|C` update.
7. **Unfinished `M1-D02..D15` Decisions (`MATRIX1-R1:252-260`, `HANDOVER-MATRIX-1:238-247`):** OP vs repo grouping (`M1-D02`), dependency/loop grammar (`M1-D03`), cross-project display (`M1-D04`), OP vs Git build-truth resolution (`M1-D06`), degraded OP UX (`M1-D14`).

---

## 4. Process & Anti-Drift Boundaries

- **OP Truth Precedence:** Query OpenProject read-only (`node C:\GitDev\agent-skills\skills\openproject\client\opCall.js`) with pagination (`limit/offset`) for projects, WPs, and relations. Keep OP `follows/requires/blocks/relates` relation types intact (`NORTHSTAR` `[P0]`). Use Git/test artifacts (never OP status alone) to claim build completion (`HANDOVER-MATRIX-1:309`). On `:8083` failure (`D019`), mark `[OP-OFFLINE]`; for unmapped non-OP items use `OP-UNRESOLVED` — never invent numeric WP IDs.
- **Hierarchy Cap:** Maximum 2 visible card tiers (`L1`, `L2`) + 1 inline 6-col detail row. Never add `L3` or nested child cubes.

---

## 5. Output & Concrete Examples

### Canonical Targets to Update
1. `01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md` (`§5`).
2. `01-weekly-command-brief/HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR.okf.md` (clean `:87-89`, close `EM-13` & OP `## Heading` anchor spec).
3. `01-weekly-command-brief/HANDOVER-06-CROSS-PROJECT-DEPENDENCY-VIEW-RESEARCH.okf.md` (ratify Option B `🔗` pills or winner).
4. Live Matrix 1 JSON/HTML renderer replacing stale W45 `DATA.repos` inside `v03.html`.
5. **Archive via `git mv` (`CDL-05`):** `HANDOVER-01-PROJECT-MATRIX-EPICS-CRITICAL-PATH.md` (once verified) & superseded research snapshots (`MATRIX1-R1`, `ORCHESTRATOR-MATRIX-1`, `NORTHSTAR` exports) -> `apex-meta/archive/weekly-orchestration/precap-week-drafts-2026-11/`.

### Concrete Example — Valid `L1` Node + `G|I|P|S|O|C` + `selected_work_reference`
```json
{
  "id": "apex-hid",
  "tier": "L1",
  "title": "OpenMouse Kernel HID Binding",
  "state_badge": "IN_PROGRESS",
  "op_ref": "OP-WP#139",
  "cross_repo_links": [{ "pill": "🔗 Apex -> Leela N2", "target_ref": "OP-WP#48", "relation": "blocks" }],
  "spec": {
    "G": { "outcome": "Verified HID input stream under Windows hook test", "acceptance": "pytest/integration pass + commit SHA" },
    "I": { "sources": ["repo/driver.c"], "upstream_dependencies": ["OP-WP#198"], "exclusions": ["macOS daemon"] },
    "P": ["Step 1: Audit descriptor -> Step 2: Patch hook -> Step 3: Run latency bench"],
    "S": ["code-understand", "ApexSession"],
    "O": { "deliverable": "Working HID build + test log", "redraft_note": "Update WP#139 comment after test" },
    "C": { "downstream": ["OP-WP#222 Dark Factory Gate"], "matrix2_slot_hint": "Weekday C slots" }
  }
}
```

---

## 6. Operator Resolution Ledger (`M1-Q1..Q5` & `06-PORTFOLIO` — Ratified `2026-11-11`)

| ID | Question | Locked Operator Ruling |
|---|---|---|
| **06-PORTFOLIO** | Canonical Portfolio Roster | **Ratified 6-Portfolio Standard:** **`Leela`**, **`IPOS`**, **`Master of Arts`**, **`Apex AI`**, **`Mindful Bar`**, and **`Residual`**. |
| **M1-Q1 (`EM-13`)** | Reconcile `EM-13` into `G\|I\|P\|S\|O\|C` + `{{var}}` | **Ratified:** `EM-13` is unified on the 6 visual columns `G \| I \| P \| S \| O \| C` (`G` includes `acceptance` + `Tasks -> Subtasks`; `I` includes `sources + upstream_dependencies + exclusions`; `O` includes `deliverable + redraft` + `Tasks -> Subtasks` drafts/examples; cards stay strictly `L1 / L2` with no `L3` cubes; `{{VAR}}` placeholder syntax). |
| **M1-Q2 (`OP Sync`)** | OpenProject `description` `## Heading` structure | **Ratified:** Markdown headings (`## Goal`, `## Input / Sources`, `## Upstream Dependencies`, `## Process`, `## Skills`, `## Output`, `## Continuation / Downstream`) with read-only `opCall.js` inspection and `D019` `[OP-OFFLINE]` fallback. |
| **M1-Q3 (`HANDOVER-06`)** | Cross-Repo & Critical Path display | **Ratified Option B:** Inline clickable `🔗 Cross-Repo:` pills + `⚡` critical-path indicator on `L1` cubes; standalone bottom Mermaid DAG retired. |
| **M1-Q4 (`M1-D10`)** | Portfolio Roster & `L2` vs Longlist | **Ratified:** 6 Portfolio Areas (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`); `L2 Nice-to-Have` holds actionable secondary candidates only, while blocked/future-phase backlog items (`#204`, `Stripe`, `#227`) move to `Longlist Deferred` in Section `04`. |
| **M1-Q5 (`M1-D02..D15`)** | Matrix 1 R1/R2 locks | **Ratified:** Portfolio grouping across the 6 areas, iteration badges inline, Git/test artifacts required for build completion truth, and `selected_work_reference[]` exported cleanly to Matrix 2. |

---

## 7. Definition of Done (DoD) & Verification Commands

1. Execute fresh read-only paginated OP check (`node C:\GitDev\agent-skills\skills\openproject\client\opCall.js project.list` and `wp.list` / relations) — zero phantom tokens (`WP-BIZ-01`, `WP-APEX-01` gone).
2. Cockpit Section `02` renders `L1` + folded `L2` **only**, zero `L3`, zero recursive trees, zero 30m sprints/times, and a single full-width 6-col `G|I|P|S|O|C` row per clicked card (desktop 6-col, tablet 3-col, mobile 1-col, collapsed `#m1-previews`, print expansion).
3. Both `Input.exclusions`, `Goal.acceptance`, and approved `HANDOVER-06` cross-repo links render explicitly; `Matrix 1 -> Matrix 2` `selected_work_reference` contract emits without duplicating a task database.
4. `HANDOVER-03:87-89` stale `G-I-P-S-O drawer` text patched.

## 8. Fresh-Chat Starter Prompt

```text
Read apex-meta/tools/project-improvement-orchestration-weekly/precap-week-handovers/04-HANDOVER-MATRIX-1.md and 00-RULE-CANONICAL-DECISION-LOCK.md.
Run a live read-only OpenProject intake check via opCall.js first (respecting D019 fallback if :8083 is off), walk me through M1-Q1..M1-Q5 to lock EM-13, OP ## headings, Option B 🔗 pills, L2 vs Longlist, and Residuals placement, then update SPEC §5, HANDOVER-03/06, and Section 02 of the cockpit HTML while archiving superseded HANDOVER-01.
```
