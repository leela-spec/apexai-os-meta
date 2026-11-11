---
type: handover
id: HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR-v1.0
title: Handover — L1/L2 Goal Selection and Six-Field Specification
description: "Operator-corrected design: selecting a goal opens a single horizontal Goal/Input/Process/Skills/Output/Continuation row; no recursive tree or L3. OpenProject alignment remains pending."
status: ready_for_operator_verification
date: 2026-11-10
tags: [weekly-orchestration, task-specification, variable-system, symbols, matrix-1, openproject-2do, em-09, em-13]
---

# Handover — L1/L2 Goal Selection and Six-Field Specification

## 1. Mission & Architectural Gap

Precap Week Matrix 1 presents ranked `L1` goal cubes and folded `L2` nice-to-have cubes. Selecting either reveals six fields in one full-width horizontal row: `Goal | Input | Process | Skills | Output | Continuation`. The row has no visible specification heading, no child goal tree, and no `L3`. This is a **cockpit presentation contract**; universal agent/OpenProject serialization remains a separate pending compatibility decision.

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
- [P0 | I97/E95/R05] **Presentation Contract**: Click one goal cube to expand exactly one row immediately below that cube's `L1`/`L2` group. The six fields span available width in one horizontal line (responsive reflow at narrow widths). A selected goal's label supplies context, while the `Goal` field itself still renders. Zero recursive child-cube trees, zero `L3`, zero extra heading banner, and zero separate execution card.
- [P0 | I94/E90/R08] **Variable and Cross-System Compatibility (`EM-13`)**: Existing `EM-13` requires `Input / Sources / Process / Skills / Output / Redraft`. The six-field cockpit presentation contract does not automatically overwrite it. Map `EM-13` `Sources` to `Input.sources`; preserve `Redraft` separately until its role in `Output` is explicitly resolved. Define one canonical placeholder grammar later; do not silently treat `{{name}}` and `${name}` as interchangeable.
- [P1 | I92/E82/R10] **OpenProject Task Creation & Symbol Synchronization (`2do`)**:
  - `TODO`: Define and test lossless mappings for `G/I/P/S/O/C`, upstream vs downstream dependencies, and preserved `EM-13` `Redraft` before any live `opCall.js` mutation. Read-only inspection is permitted; no custom-field support is assumed.

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
| `⚙` / Process Gear | Method / Logical Path (`P`) | Inside clicked G-I-P-S-O drawer | Process Field |
| `📥` / Input Stack | Priority Sources (`I`) | Ranked source list inside G-I-P-S-O drawer | Input Field |
| `🎯` / `📦` | Goal (`G`) / File Output Draft (`O`) | Top breadcrumb (when non-redundant) & deliverable skeleton | Goal & Output Fields |

#### C. Concrete OpenProject Synchronization `2do` Checklist
- Propose (do not yet mandate) OpenProject description anchors for `Goal`, `Input/Sources`, `Upstream Dependencies`, `Process`, `Skills`, `Output`, and `Continuation/Downstream`. Preserve provenance and status of missing fields.
- After the operator decides the `EM-13`/`Redraft` mapping, inspect the live canonical OpenProject skill read-only and prove a lossless read/write contract in a controlled test; do not modify production work packages from this design patch.

### 2.4 Definition of Done (`DoD`)
1. Only `L1` and `L2` cubes exist; both reveal six horizontal fields directly below that cube strip on selection, including `Goal` and `Continuation`.
2. No recursive child cubes, `L3`, redundant specification heading, fabricated skill/file/WP IDs, or invented dependency links.
3. `Input.sources`, `Input.upstream_dependencies`, and `Continuation.downstream` remain distinct and traceable. `EM-13` compatibility is explicitly unresolved, not silently rewritten.
4. Visual symbol matching is an optional styling concern, not an excuse to infer task identity/priority or to require Leela symbol semantics.

---

## 3. 5-Component Verification Readiness Note

1. **Observation**: `ADPT-EXEC-TASKSPEC-v0.1` (`EM-13`) already established the 6 pre-work alignment fields (`Input`, `Sources`, `Process`, `Skills`, `Output`, `Redraft`), and Leela's `stats_cube_symbol.dart` provides an optional visual vocabulary (`Chunk`, `Sequence`, `Epic`, `Branch`).
2. **Logic Chain**: The cockpit adopts an `L1`/`L2` goal-to-six-field horizontal inspection surface (`Goal | Input | Process | Skills | Output | Continuation`). `EM-13` serialization and OpenProject field mapping are open compatibility questions rather than assumed universal replacements.
3. **Caveats**: OpenProject server custom-field support is not yet live-verified in this handover; markdown-header standardization inside WP `description` requires zero DB schema risk and acts as the default candidate path pending operator sign-off.
4. **Conclusion**: Handover updated to `v05` operator corrections; ready for verification in cockpit HTML and Matrix 1 module execution (`T3`).
5. **Verification Method**: Test both `L1`/`L2` selection and the six-field horizontal row against source-backed project examples; verify upstream vs downstream links separately; leave missing fields unresolved. Do not require a fixed five-repo roster.
