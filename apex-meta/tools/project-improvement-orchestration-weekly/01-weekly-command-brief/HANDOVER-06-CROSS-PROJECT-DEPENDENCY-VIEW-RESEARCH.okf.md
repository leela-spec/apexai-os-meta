---
type: handover
id: HANDOVER-06-CROSS-PROJECT-DEPENDENCY-VIEW-RESEARCH-v1.0
title: Handover — Cross-Project Consolidated Dependency Visualization Research (Replace or Drop Mermaid Deck)
description: Bounded research handover evaluating whether the bottom Consolidated Process Dependency DAG should be removed entirely, replaced by inline Goal-Cube handoff badges, or refactored into a pure Goal-Hopping map.
status: ready_for_operator_verification
date: 2026-11-09
tags: [weekly-orchestration, matrix-1, critical-path, dependency-visualization, ux-research, em-09]
---

# Handover — Cross-Project Consolidated Dependency Visualization Research

## 1. Mission & Skepticism Triggered

The current bottom Mermaid diagram (`Consolidated Cross-Repo Critical Path & Process Dependency DAG`) inside [`WEEKLY_PRECAP_NORTHSTAR_2026_W45.html`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/WEEKLY_PRECAP_NORTHSTAR_2026_W45.html) duplicates workstreams already visible inside Matrix 1 (`L1 Priority Goals`) while adding a sprawling multi-subgraph flowchart with sparse true cross-repo edges. The operator doubts this bottom deck justifies its footprint and commissioned a structured comparison research pass before deciding whether to drop, inline, or redesign it.

---

## 2. 4-Dimensional Handover Contract (`EM-09`)

### 2.1 Input & Priority Ledger
- **P1 Operator Feedback**:
  - Goals inside each repo's `Level 1: Priority Goals` already support conditional arrows when major goals depend on each other (*"They don't need to have a critical path. They might have a critical path if the major goals depend on each other, but it's not necessary"*).
  - Top-level experience goal: *"hopping from goal to goal"* cleanly across projects rather than scrolling down to parse a dense multi-box Mermaid flowchart.
- **P2 Authoritative Sources**:
  - [`SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md) (`v2.0`).
  - [`HANDOVER-20261106.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/00-openproject-dependency-intake/HANDOVER-20261106.okf.md): Live OpenProject `blocks` / `follows` cross-project link verification gate.
- **Deliberately Excluded**: Synthetic cross-repo arrows fabricated just to make a graph look connected; low-level task/sprint nodes inside any macro dependency summary.

### 2.2 Process & Research Evaluation Framework
- **Method Used**: Evidence-Bounded Trade-Off Bake-Off (`ADPT-EXEC-BAKEDEF` / Impact-Effort-Risk `(I/E/R)` scoring + `<10s` First-10-Seconds Visual Comprehension Audit).
- **Research Questions to Resolve**:
  1. Across a typical week (`MoA`, `Leela`, `IPOS`, `Apex OS`, `Residuals`), how many genuine cross-repo blocking edges (`Project A Goal -> Project B Goal`) actually exist in live OpenProject data vs independent parallel project tracks?
  2. When 0–2 cross-repo blocks exist, does a standalone 5-subgraph Mermaid deck waste vertical height and repeat L1 data cleanly solved inside repo rows?
  3. Which alternative maximizes immediate signal without introducing static graph maintenance noise?

### 2.3 Candidate Alternatives Evaluated & Concrete Redrafts

| Option | Mechanism | `(I/E/R)` Est. | Trade-off Summary |
|---|---|---|---|
| **Option A — Drop Bottom Deck Completely** | Remove consolidated Mermaid block. Intra-repo arrows render directly between `L1 Priority Goal` cubes *only* when major goals depend on each other. | `(I85/E10/R15)` | Zero duplicate prose/Mermaid bloat; loses visibility if a cross-repo handoff exists (e.g., *MoA Invoicing schema -> IPOS ledger*). |
| **Option B — Embedded Cross-Repo Link Pills on L1 Goal Cubes** *(Recommended Candidate)* | No bottom section at all. If Goal X unblocks/depends on another repo's Goal Y, attach a clickable pill (`➔ Unblocks: IPOS Time-Series`) directly on Goal X's cube; clicking scrolls/highlights Goal Y. | `(I92/E35/R10)` | Preserves true cross-repo dependencies *in situ* during Goal-to-Goal hopping with zero extra vertical deck height. |
| **Option C — Collapsible Milestone-Only Cross-Repo Strip** | Keep an ultra-compact horizontal strip *only* when >=1 live cross-repo OP relation exists (`[MoA Invoice Schema] ──blocks──▶ [IPOS Billing View]`), auto-hidden when 0 edges exist. | `(I78/E30/R20)` | Clean exception-driven surface; risks sitting empty most weeks or inviting unnecessary diagram chrome. |

#### Concrete Option B Sample (Inlined Directly on L1 Cube)
```text
[1. Master of Arts]
L1 | Priority Goals:
  [ ▣ Website Content Draft ]   [ ▣ 7 Produced Videos ]   [ ⚡ Automated PDF Billing ]
                                                               └─ 🔗 Cross-Repo: Feeds IPOS Cashflow Parser
```

### 2.4 Definition of Done (`DoD`)
1. Live audit check against OpenProject (`opCall.js wp.list` / relations) counting actual cross-project `blocks`/`precedes` edges across the 5 active repositories.
2. Concrete visual mock comparison (Option A vs Option B vs Option C) evaluated against the **First 10 Seconds Contract** and Goal-to-Goal scan time.
3. Written decision entry in [`SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md) ratifying the chosen replacement (or deletion) so Section 5.4 is no longer mandatory Mermaid boilerplate.

---

## 3. 5-Component Verification Readiness Note

1. **Observation**: In Week 45 draft v1.2, 18 nodes in the bottom Consolidated Mermaid DAG merely echoed individual repo L2 cards with only one dashed cross-repo edge (`M5 -.-> I2`).
2. **Logic Chain**: When cross-repo coupling is sparse (`0-2` edges), rendering an entire 5-cluster diagram repeats Level 1/Level 2 content without proportional clarity. Inline link badges on affected `L1` Goal cubes (`Option B`) or clean deletion (`Option A`) respects the high-density visual budget.
3. **Caveats**: True live frequency of cross-repo dependencies awaits execution of P1 read-only OpenProject relation intake (`HANDOVER-20261106.okf.md`).
4. **Conclusion**: Bottom Consolidated Process Dependency DAG should be reclassified as **`DEPRECATED_UNDER_RESEARCH`** in `SPEC-PRECAP-WEEK-ITERATIONS.okf.md` `v2.0` pending execution of this handover.
5. **Verification Method**: Execute `HANDOVER-20261106.okf.md` read-only OP relation count, render Option B pill mockup vs current Mermaid DAG side-by-side, and capture operator selection.
