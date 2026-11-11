---
type: handover
id: HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR-v1.0
title: Handover — L1/L2 Goal Selection and Six-Field Specification
description: "Operator-corrected design: selecting a goal opens a single horizontal Goal/Input/Process/Skills/Output/Continuation row; no recursive tree or L3. EM-13 unified on G|I|P|S|O|C and OpenProject ## Heading mapping locked."
status: current
date: 2026-11-11
tags: [weekly-orchestration, task-specification, variable-system, symbols, matrix-1, openproject-2do, em-09, em-13]
---

# Handover — L1/L2 Goal Selection and Six-Field Specification

## 1. Mission & Architectural Gap

Precap Week Matrix 1 presents ranked `L1` goal cubes and folded `L2` nice-to-have cubes across the **6 canonical Portfolio Areas** (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`). Selecting either reveals six fields in one full-width horizontal row: `Goal | Input | Process | Skills | Output | Continuation`. Matrix 1 UI cards stay strictly `L1 / L2` (no `L3` cubes), while inside expanded `Goal` and `Output` cells items decompose into `Tasks -> Subtasks` with short drafts/examples. `EM-13` is unified directly onto `G | I | P | S | O | C`.

---

## 2. 4-Dimensional Handover Contract (`EM-09`)

### 2.1 Input & Priority Ledger
- **P1 Authoritative Core Rules**:
  - [`task-specification.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/final/specs/execution-modes/task-specification.md) (`ADPT-EXEC-TASKSPEC-v0.1` / `EM-13`): Six-field pre-work contract (`Input`, `Sources`, `Process`, `Skills`, `Output`, `Redraft`).
  - [`SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md) (`v2.0`, `v05` operator corrections): Matrix 1 includes `L1 Priority Goals` and `L2 Nice-to-Haves` ONLY.
- **P2 Operator Visual & Sketch Inputs**:
  - Initial hand-drawn Goal-to-Subtask tree sketch ([`media_1794217434721_8a89b35e.jpg`](file:///C:/Users/gehma/.gemini/antigravity/brain/0cf33bfc-6b5b-4769-8480-c20209391e36/.user_uploaded/media_1794217434721_8a89b35e.jpg)) is superseded by the operator's later `v05` correction: Goal cubes open a full-width six-field data row; no recursive child cubes.
  - Annotated Matrix 1 feedback ([`media_1794217212691_918d426d.png`](file:///C:/Users/gehma/.gemini/antigravity/brain/0cf33bfc-6b5b-4769-8480-c20209391e36/.user_uploaded/media_1794217212691_918d426d.png)): Compact cube buttons always visible on Level 1; bulky green outcome banner removed.
- **P3 Visual Symbol Reference**:
  - [`stats_cube_symbol.dart`](file:///c:/GitDev/Leela-Cloud-2026/lib/features/stats/stats_cube_symbol.dart): Optional styling reference (`Chunk` hollow glyph cube, `Sequence` gold envelope, `Epic` 3x3 Rubik cube, `Branch` solid color cube).
- **Deliberately Excluded**: Temporal calendar scheduling (belongs to Matrix 2 / [`HANDOVER-02`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md)); mutating live OpenProject production records during design verification.

### 2.2 Process & Logical Rules
- [P0 | I98/E90/R06] **Six Fields for Both `L1` and `L2` (Ordered Left-to-Right; No Visible Contract Heading)**:
  1. **`G — Goal`**: Specific intended outcome, scope, and observable acceptance evidence.
  2. **`I — Input`**: *(a)* Verified source paths/WP links, prioritized and typed; *(b)* **upstream** prerequisites/dependencies separately; *(c)* relevant explicit exclusions. Absent fields remain unresolved, never invented.
  3. **`P — Process`**: Concrete sequence of steps and named method **only if source-supported**, with how progress/evidence will be checked. Avoid generic boilerplate frameworks.
  4. **`S — Skills`**: Verified registered skill/capability IDs where available; otherwise `unresolved`.
  5. **`O — Output`**: Actual destination artifact types, concrete file paths where known, expected structure/content, and acceptance proof; typed non-file deliverables are supported.
  6. **`C — Continuation`**: **Downstream** consumers, successor work packages, actual unblocked goals, and handoff references; unknown successors stay unresolved.
- [P0 | I97/E95/R05] **Presentation Contract**: Click one goal cube to expand exactly one row immediately below that cube's `L1`/`L2` group. The six fields span available width in one horizontal line (responsive reflow at narrow widths). Matrix 1 UI cards remain `L1 / L2` (zero `L3` cubes, zero recursive child-cube trees, zero extra heading banner), while inside the expanded `Goal` and `Output` cells, items decompose into `Tasks -> Subtasks` with short drafts/examples.
- [P0 | I96/E94/R06] **Unified `EM-13` Mapping on `G | I | P | S | O | C`**: `EM-13` (`Input / Sources / Process / Skills / Output / Redraft`) is unified on the 6-column `G | I | P | S | O | C` contract: `G (Goal)` carries desired outcome, `acceptance`, and `Tasks -> Subtasks` decomposition; `I (Input)` hosts `sources`, `upstream_dependencies`, and explicit `exclusions`; `P (Process)` hosts ordered steps and verification; `S (Skills)` hosts verified skill IDs; `O (Output)` hosts `deliverable`, `redraft` (short drafts/examples), and `Tasks -> Subtasks` output structure; `C (Continuation)` hosts `downstream` successors and handoff refs. Standard template placeholder syntax is `{{VAR_NAME}}`.
- [P1 | I92/E88/R08] **OpenProject Description `## Heading` Synchronization**:
  - Canonical Markdown headings inside OpenProject work package `description` fields: `## Goal`, `## Input / Sources`, `## Upstream Dependencies`, `## Process`, `## Skills`, `## Output`, `## Continuation / Downstream`. Read-only inspection runs by default (`opCall.js`); mutating writebacks require explicit `--confirmed` operator authorization.

### 2.3 Output Specification & Concrete Structural Draft

#### A. Logical Variable Grammar Template
```yaml
task_spec:
  layer: L1_PRIORITY_GOAL    # L1_PRIORITY_GOAL | L2_NICE_TO_HAVE
  project: MasterOfArts
  work_package: "OP-WP#163"  # verified in saved W45 source, current live freshness unverified
  G:
    outcome: "Website content draft and responsive layout"
    acceptance: "Responsive navigation and mobile drawer review"
  I:
    sources:
      - {rank: P1, ref: "OP-WP#163", kind: work_package}
      - {rank: P2, ref: null, kind: repository_file, status: exact_path_unverified}
    upstream_dependencies: []  # not asserted to be none; relation audit pending
    dependency_coverage: unresolved
  P:
    steps: ["Stage website draft content", "Implement flexbox navigation", "Implement mobile reading drawer", "Check responsive layout"]
    method_source: "saved W45 Northstar task description"
    verification: "Review responsive rendering and staged content routes"
  S:
    verified_skill_ids: []
    resolution: unresolved
  O:
    artifacts: [{type: website_content_and_layout, path: null, status: exact_path_unverified}]
    expected_evidence: ["Readable content routes", "Responsive navigation and drawer"]
  C:
    downstream: ["Public audience release (described in W45)"]
    verified_successor_wp_ids: []
    successor_coverage: unresolved
```

#### B. Semantic Symbol Vocabulary (Leela-Inspired Matrix 1 + OpenProject Set)
| Token / Glyph | Meaning | Visual Anchor | Source Mapping |
|---|---|---|---|
| `▣` / Branch-Stroked Cube | Priority Goal Cube (`L1`) | Warm amber/teal bordered square cube with outcome title | Matrix 1 `L1` + Leela `BranchCube` |
| `◇` / Hollow Cube | Nice-to-Have Cube (`L2`) | Soft slate hollow cube with output title | Matrix 1 `L2` + Leela `ChunkDisplay` |
| `⊞` / 3x3 Mini-Cube | Repository / Epic Container | Solid 3x3 Rubik badge next to project header | Leela `EpicRubikCube` |
| `✉` / Gold Sequence Envelope | Process Flow Sequence (3x3 container) | Gold badge linking Matrix 1 cubes to Matrix 2 flows | Leela `SequenceEnvelope` |
| `➔` / Conditional Edge | Critical Dependency Arrow | Drawn between L1 cubes *only* when Output A blocks Goal B | Critical Path Engine |
| `⚡` / Bolt Badge | Critical Path Flag | Highlights bottleneck cube or work package | Topological Gate |
| `⚙` / Process Gear | Method / Logical Path (`P`) | Inside clicked `G|I|P|S|O|C` 6-column row | Process Field |
| `📥` / Input Stack | Priority Sources (`I`) | Ranked `sources`, `upstream_dependencies`, and `exclusions` inside `G|I|P|S|O|C` row | Input Field |
| `🎯` / `📦` | Goal (`G`) / File Output & Redraft (`O`) | Inside `G` (`outcome + acceptance + Tasks->Subtasks`) and `O` (`deliverable + redraft`) cells | Goal & Output Fields |

#### C. OpenProject `## Heading` Synchronization Contract
- OpenProject work package `description` anchors map 1-to-1 to `## Goal`, `## Input / Sources`, `## Upstream Dependencies`, `## Process`, `## Skills`, `## Output`, and `## Continuation / Downstream`. Preserve provenance and status of missing fields.
- Live `opCall.js` inspection is read-only by default (`D019` `[OP-OFFLINE]` fallback when `:8083` is unreachable); production work packages are never modified without explicit operator `--confirmed` approval.

### 2.4 Definition of Done (`DoD`)
1. Only `L1` and `L2` cubes exist across the 6 Portfolio Areas (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`); both reveal six horizontal fields directly below that cube strip on selection (`G | I | P | S | O | C`), with `Tasks -> Subtasks` and short drafts/examples inside expanded `Goal` and `Output` cells.
2. No recursive child cubes, `L3`, redundant specification heading, fabricated skill/file/WP IDs, or invented dependency links.
3. `Input.sources`, `Input.upstream_dependencies`, `Input.exclusions`, `Goal.acceptance`, `Output.redraft`, and `Continuation.downstream` remain distinct and traceable (`EM-13` unified on `G|I|P|S|O|C`).
4. Visual symbol matching is an optional styling concern, not an excuse to infer task identity/priority or to require Leela symbol semantics.

---

## 3. 5-Component Verification Readiness Note

1. **Observation**: `ADPT-EXEC-TASKSPEC-v0.1` (`EM-13`) established the 6 pre-work alignment fields (`Input`, `Sources`, `Process`, `Skills`, `Output`, `Redraft`), now unified cleanly onto the 6-column `G | I | P | S | O | C` Matrix 1 drawer.
2. **Logic Chain**: Matrix 1 UI cards stay strictly `L1 / L2` (no `L3` cubes), while expanded `Goal` and `Output` cells decompose items into `Tasks -> Subtasks` with short drafts/examples (`Redraft`), preserving high-speed top-level scanning and full execution-ready depth in one click.
3. **Caveats**: OpenProject `description` synchronization uses standard Markdown `## Heading` sections (`zero` custom DB schema risk) and respects `D019` (`[OP-OFFLINE]` fallback when `:8083` is unreachable).
4. **Conclusion**: Handover locked as `current` (`v05` + unified `EM-13` + 6-Portfolio standard).
5. **Verification Method**: Test both `L1`/`L2` selection and the six-field horizontal row across the 6 Portfolio Areas (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`); verify `Goal.acceptance`, `Input.exclusions`, `Output.redraft`, and upstream vs downstream links separately.
