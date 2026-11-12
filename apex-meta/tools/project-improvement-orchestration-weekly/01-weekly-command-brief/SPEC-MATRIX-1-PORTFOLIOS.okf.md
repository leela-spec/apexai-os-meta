---
type: specification
id: SPEC-MATRIX-1-PORTFOLIOS-v3.0
title: "Precap Week Modular Specification — Matrix 1 (6 Portfolio Goals & G|I|P|S|O|C)"
description: "Governs the non-temporal Matrix 1 domain: 6 Portfolio Areas, L1/L2 layout, EM-13 unified G|I|P|S|O|C drawers, Tasks->Subtasks, and OpenProject alignment."
status: current
date: 2026-11-12
scope: [weekly-orchestration, precap-week, matrix-1, task-spec, g-i-p-s-o-c, six-portfolios]
tags: [matrix-1, g-i-p-s-o-c, six-portfolios, okf-v02]
parent_spec: SPEC-PRECAP-WEEK-MASTER.okf.md
references: [SPEC-PRECAP-WEEK-MASTER.okf.md, SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md, SPEC-SEQUENCING.okf.md, SPEC-PRECAP-INTERFACES-HANDOFF.okf.md]
---

# Precap Week — Matrix 1 Specification (Non-Temporal Portfolio Goals)

## Section 1 — Architecture & Non-Temporal Invariants

Matrix 1 models strategic, architectural, and directional portfolio goals for the planning week. It deliberately isolates work package deliverables, observable acceptance criteria, required sources, procedural steps, and dependencies from calendar scheduling.

### Core Non-Temporal Invariants

- [P0 | I98/E95/R05] **Zero Sprints / Zero Calendar Times**: Matrix 1 contains strictly zero calendar times, zero day assignments, and zero sprint allocations. All temporal mechanics and sprint bindings belong exclusively to Matrix 2 ([`SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md`](SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md)).
- [P0 | I97/E94/R06] **Directional Scope Isolation**: Matrix 1 defines *what* is authorized and *why* it matters across the 6 canonical portfolios. Downstream execution agents and `PrecapNextDay` consume Matrix 1 definitions as authoritative work package scope.
- [P0 | I96/E95/R05] **Section Collapse & Header Preview**: In the collapsed state, the Matrix 1 section header (`#m1-previews`) retains up to three top-priority `L1` goal cards reflecting current weekly execution order. Expanding the section discloses the full 6-Portfolio stacked view.

---

## Section 2 — Project & Level Layout Hierarchy (L1, L2, No L3)

The layout of Matrix 1 adheres strictly to progressive disclosure without visual recursion:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ 02 · MATRIX 1 — PORTFOLIO GOALS                                        │
│ Collapsed Header: [Top L1 Goal A] [Top L1 Goal B] [Top L1 Goal C]      │
└────────────────────────────────────────────────────────────────────────┘
  ▼ [Expanded Content]
┌────────────────────────────────────────────────────────────────────────┐
│ PORTFOLIO 1: Leela                                                     │
│   L1 Priority Cards (Side-by-Side):                                    │
│   ┌──────────────────────────────┐  ┌──────────────────────────────┐   │
│   │ ⚡ Skill Tree Crown Engine   │  │ ⚡ SpatialViewNode Placement │   │
│   │ §F.1-§F.5 (6/9 Pass)         │  │ & Placement Contracts        │   │
│   └──────────────────────────────┘  └──────────────────────────────┘   │
│   ▼ [Click to expand unified 6-column drawer below strip]              │
│   ┌──────┬──────┬─────────┬────────┬────────┬──────────────┐           │
│   │ Goal │Input │ Process │ Skills │ Output │ Continuation │           │
│   └──────┴──────┴─────────┴────────┴────────┴──────────────┘           │
│   L2 Candidates (Folded):                                              │
│   ▶ [Repo-Efficiency Over-Engineering Audit] (Click to unfold)         │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Vertical Portfolio Stacking**: Expanded content stacks the **6 canonical Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`) vertically in fixed canonical order.
2. **Horizontal L1 Priority Goals**: Each portfolio displays its active **L1 Priority Goals** side-by-side from left to right in verified execution priority order. Artificial one-or-two card limits are prohibited; active scope governs card count.
3. **Folded L2 Nice-to-Haves**: Directly beneath the L1 strip, actionable secondary candidates are grouped under an `L2 Nice-to-Haves` drawer that starts folded by default. Unfolding an L2 item exposes the identical card structure and 6-column drawer.
4. **Permanent Prohibition of L3 Cards**: UI cards are strictly restricted to `L1` (active weekly priority) and `L2` (actionable candidate). Recursive `L3` cubes, nested child trees, and multi-level card hierarchies are permanently banned. Deeper technical decomposition is handled strictly within the `Goal` and `Output` fields as `Tasks -> Subtasks` with concrete `redraft` examples.
5. **Metadata Parsimony**: Bulky outcome banners, technical database ID columns, and redundant numerical priority scores are suppressed on card surfaces.

---

## Section 3 — Unified EM-13 Six-Field Drawer Contract (`G | I | P | S | O | C`)

Clicking any `L1` or `L2` card expands exactly one full-width 6-column interactive drawer directly beneath that card strip with zero extra heading banners. Narrow viewports reflow responsively to 3 columns (tablet) or 1 column (mobile).

### Six-Field Data Contract (`{{VAR_NAME}}` Syntax)

| Field | Drawer Column Header | Core Contents & Epistemic Constraints | Symbol |
|---|---|---|:---:|
| **G** | **Goal** | Concrete headline outcome, observable `acceptance` criteria, and structured `Tasks -> Subtasks` breakdown. Statements must define verifiable completion. | `▣` |
| **I** | **Input** | Ranked `sources` (path:line or URL), explicitly separated `upstream_dependencies`, and mandatory `exclusions` (what will NOT be done). Missing items marked `unresolved`. | `◇` |
| **P** | **Process** | Step-by-step verification commands, test procedures, and method names. Never generic boilerplate or empty prose. | `⊞` |
| **S** | **Skills** | Exact registered skill IDs or tool names required for execution. Unmapped skills marked `unresolved`. | `✉` |
| **O** | **Output** | Target deliverable file paths, structured `Tasks -> Subtasks` mapping, and concrete `redraft` worked examples (outlines, code snippets, or draft paragraphs). Grounded Git SHA or test pass required. | `➔` |
| **C** | **Continuation** | Downstream consumers, successor work packages, `selected_work_reference[]` slot hints for Matrix 2, and physical handoff location. | `↳` |

### Tasks -> Subtasks & Redraft Standard

Inside the expanded `Goal` and `Output` columns:
- Complex deliverables must be broken into `Tasks -> Subtasks` (e.g. `Task 1: Spec authoring -> Subtask 1.1: Frontmatter, Subtask 1.2: Sections`).
- The `Output` column must provide a compact `redraft` worked example (Level L0–L3) demonstrating what the delivered asset looks like, eliminating ambiguity before execution begins.

---

## Section 4 — OpenProject Intake Epistemology & Description Synchronization

To maintain epistemic integrity across all weekly orchestration surfaces, OpenProject interaction follows strict rules:

### Intake Precedence Ladder (`Findings A–I`)

1. **Primary Grounding**: Query live OpenProject via `opCall.js` (`127.0.0.1:8083`, read-only paginated) alongside Apex Session `planning_feed` and `sync/next.json`.
2. **Fallback Sequence**: If live OpenProject is unreachable, read verified local artifacts in descending priority: `00-openproject-dependency-intake/EVIDENCE-20261106.okf.md`, `next-session.md`, `ProjectStatus`, and raw `FlowRecap` logs.
3. **Offline Token Grammar (`D019`)**:
   - When the OpenProject server is unreachable (`ECONNREFUSED` or auth failure), emit the non-blocking token `[OP-OFFLINE]` and load the confirmed snapshot.
   - When a local goal has no mapped OpenProject Work Package ID, mark it explicitly as `[OP-UNRESOLVED]`.
   - Never block compilation on offline services; never invent or guess synthetic numeric IDs (e.g. `WP-BIZ-01` is strictly forbidden).

### Relational Graph Integrity

- Never collapse `follows`, `requires`, `blocks`, or `relates` edges into a flat unstructured list.
- Explicitly flag contradictions between work package descriptions and status states (e.g. `WP#220` marked completed while description indicates open items).

### OpenProject `## Heading` Synchronization Contract

Work package descriptions inside OpenProject synchronize 1-to-1 with canonical Markdown headings matching the six-field contract:
```markdown
## Goal
[Headline outcome, acceptance criteria, Tasks -> Subtasks]

## Input / Sources
[Ranked sources, exclusions]

## Upstream Dependencies
[Blocking work packages, prerequisites]

## Process
[Step-by-step verification commands, methods]

## Skills
[Registered skill IDs or CLI tools]

## Output
[Deliverable file paths, redraft worked examples]

## Continuation / Downstream
[Successor packages, Matrix 2 slot hints, consumers]
```

*Safety Policy*: Live OpenProject reads are read-only (`doctor`, `whoami`, `project.list`, `wp.get`). All mutating calls (`wp.create`, `wp.update`) require explicit `--confirmed` operator authorization.

---

## Section 5 — Visible Card Surface & Inline Cross-Repo Pills (`Option B`)

### Card Surface Architecture (`NS-D03` / `NS-D04`)

Each rendered L1 card exposes:
- **Outcome Title**: Clean human-readable target (e.g. `Skill Tree Crown Engine §F.1-§F.5`).
- **Critical Path Cue**: Leading `⚡` badge if the work package is on the weekly critical path.
- **Inline Cross-Repo Dependency Pills (`Option B`)**: Verified cross-repository blocking dependencies render as clickable `🔗 Cross-Repo:` pills directly on the affected card surface (e.g. `🔗 Cross-Repo: Feeds IPOS Ingestion`). Clicking the pill scrolls smoothly to the dependent target.
- **Native Accessible Status**: Realized execution status displayed with accessible labels.
- **Opaque ID Placement**: Technical numeric work package IDs (e.g. `OP-WP#234`) are retained within the expanded six-field drawer rather than cluttering the top card face.

### Ratification of Option B & Retirement of Bottom Mermaid Deck

- Historical multi-subgraph bottom Mermaid DAG charts are permanently retired (`HANDOVER-06`).
- Cross-repository dependencies render exclusively via inline `🔗 Cross-Repo:` pills.
- Synthetic or speculative cross-repo links are prohibited; pills render only for verified OpenProject relations (`OP-REL#80-91`).

---

## Section 6 — `selected_work_reference[]` Export Contract

Matrix 1 serves as the authoritative source of work package scope for temporal scheduling. It compiles and exports the `selected_work_reference[]` array to Matrix 2 Flow `C` slots:

```json
{
  "selected_work_refs": [
    {
      "portfolio_id": "leela",
      "op_ref": "OP-WP#234",
      "title": "Skill Tree Crown Engine §F.1-§F.5 (ST-G1 · 6/9 Pass)",
      "tier": "L1",
      "readiness": "READY",
      "cross_repo_links": [],
      "slot_hint": "Thu F1/F2"
    }
  ]
}
```

*Architectural Principle*: Matrix 1 passes typed pointers and metadata. It never clones entire task databases or duplicates temporal scheduling logic.

---

## Section 7 — Operative Failure-Mode Guards & Circuit Breakers

In accordance with `WP-25`, Matrix 1 terminates with operative failure-mode guards:
1. **Zero Temporal Leakage Guard**: Matrix 1 contains strictly zero sprints, clock times, or calendar coordinates. Injecting temporal scheduling data into Matrix 1 causes immediate validation failure.
2. **Hierarchy Depth Guard**: Card layout is strictly limited to L1 Priority Outcomes and folded L2 Nice-to-Haves. Any recursive cube nesting or L3 structure triggers schema rejection.
3. **OpenProject Mutation Guard**: All external OpenProject operations must be read-only (`opCall.js`). Mutating calls without an explicit `--confirmed` flag are rejected.
4. **Relational Truth Guard**: Cross-repository dependency pills (`Option B`) require verified relations (`OP-REL#80-91`). Speculative cross-repo links are prohibited.
