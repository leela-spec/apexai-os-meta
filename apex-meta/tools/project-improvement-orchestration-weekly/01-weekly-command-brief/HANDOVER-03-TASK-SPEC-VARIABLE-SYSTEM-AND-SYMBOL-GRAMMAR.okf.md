---
type: handover
id: HANDOVER-03-TASK-SPEC-VARIABLE-SYSTEM-AND-SYMBOL-GRAMMAR-v1.0
title: Handover — Standardized G-I-P-S-O Task Specification, Logical Variable System, Symbol Grammar & Recursive Process Trees
description: Defines the universal G-I-P-S-O task specification contract, variable resolution grammar, Leela-inspired semantic symbol set, Matrix 1 recursive cube-tree UI behavior, and OpenProject task-creation synchronization 2do.
status: ready_for_operator_verification
date: 2026-11-09
tags: [weekly-orchestration, task-specification, variable-system, symbols, matrix-1, openproject-2do, em-09, em-13]
---

# Handover — Standardized G-I-P-S-O Task Specification, Logical Variable System & Symbol Grammar

## 1. Mission & Architectural Gap

Precap Week Matrix 1 moves from verbose prose containers and full-width task banners to a compact, visual **Goal-Cube Tree** paired with a **universal machine- and human-readable Task Specification (`G-I-P-S-O`)**. This handover specifies the variable schema, contextual compression rules in clickable UI cubes, the shared visual symbol vocabulary, and the downstream OpenProject (`opCall.js`) template alignment.

---

## 2. 4-Dimensional Handover Contract (`EM-09`)

### 2.1 Input & Priority Ledger
- **P1 Authoritative Core Rules**:
  - [`task-specification.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/informatics/final/specs/execution-modes/task-specification.md) (`ADPT-EXEC-TASKSPEC-v0.1` / `EM-13`): Six-field pre-work contract (`Input`, `Sources`, `Process`, `Skills`, `Output`, `Redraft`).
  - [`SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md) (`v2.0`): Layered Matrix 1 specification (`L1 Priority Goals`, `L2 Nice-to-Haves`, `L3 Other Work Packages`).
- **P2 Operator Visual & Sketch Inputs**:
  - Hand-drawn Goal-to-Subtask tree sketch ([`media_1794217434721_8a89b35e.jpg`](file:///C:/Users/gehma/.gemini/antigravity/brain/0cf33bfc-6b5b-4769-8480-c20209391e36/.user_uploaded/media_1794217434721_8a89b35e.jpg)): Top row `Goals` cubes -> on `Click` -> tree bus fanning downward into side-by-side child cubes & inline task specs.
  - Annotated Matrix 1 feedback ([`media_1794217212691_918d426d.png`](file:///C:/Users/gehma/.gemini/antigravity/brain/0cf33bfc-6b5b-4769-8480-c20209391e36/.user_uploaded/media_1794217212691_918d426d.png)): Compact cube buttons always visible on Level 1; bulky green outcome banner removed.
- **P3 Visual Symbol Reference**:
  - [`stats_cube_symbol.dart`](file:///c:/GitDev/Leela-Cloud-2026/lib/features/stats/stats_cube_symbol.dart): Leela cube visual hierarchy (`Chunk` hollow glyph cube, `Sequence` gold envelope, `Epic` 3x3 Rubik cube, `Branch` solid color cube).
- **Deliberately Excluded**: Temporal calendar scheduling (belongs to Matrix 2 / [`HANDOVER-02`](file:///c:/GitDev/apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/HANDOVER-02-TIMELINE-CALENDAR-SEQUENCE-SPRINT-VIEW.md)); mutating live OpenProject production records during design verification.

### 2.2 Process & Logical Rules
- [P0 | I98/E90/R06] **G-I-P-S-O Canonical Schema**: Every task across OpenProject, Precap Week (`L1`/`L2`/`L3`), Precap Next Day, and agent prompts binds five structured properties:
  1. **`Goal` (`G`)**: Hierarchical dot/breadcrumb variable path: `{{Goal}} > {{Task}} > {{Subtask}}`.
  2. **`Input` (`I`)**: Ranked `Sources by Priority` (`[P1] <path_or_wp> · [P2] <path_or_wp>`), plus explicit exclusions where noise risks drift.
  3. **`Process` (`P`)**: Explicitly named logical path or reasoning/execution framework (e.g., `Top-Down Wireframe -> Schema Freeze -> Redraft`, `Critical Path DAG Sort`, `Comparative Bake-Off`, `3x3 Pomodoro Execution`).
  4. **`Skills` (`S`)**: Prioritized skill sets (`[P1] <skill_id> · [P2] <skill_id>`), mapping to registered agent skills or operator domain capabilities.
  5. **`Output` (`O`)**: Concrete expected artifacts + structural redraft:
     - **If multiple files**: Enumerate every target file path (`file_a.py`, `file_b.md`).
     - **If single file**: Specify exact section headers / skeleton headings and a 1-2 line structural preview/draft.
- [P0 | I95/E95/R05] **Contextual Omission Rule in UI Tree Drill-Down**:
  - When clicking a **Priority Goal cube** (`L1`) or **Nice-to-Have cube** (`L2`) whose label already declares the Goal/Outcome (`{{Goal}}`), the expanded inline Task Specification drawer **omits redundant top `Goal` repetition** and focuses vertically on `Input` -> `Process` -> `Skills` -> `Output` + child fan-out cubes.
  - On standalone **`L3` Work Package rows** or standalone exports, the full `Goal > Task > Subtask` breadcrumb header renders explicitly.
- [P0 | I94/E85/R08] **Recursive Cube-Tree Fan-Out Interaction**:
  - Clicking a top-row cube (`L1` or `L2`) reveals a downward tree connector (`|` -> horizontal distribution bar -> child cubes) matching the operator sketch.
  - Each child cube represents a concrete sub-output or process phase and is itself clickable, recursively opening its finer-grained `I-P-S-O` spec or sub-tree until leaf deliverable depth is reached.
- [P1 | I92/E82/R10] **OpenProject Task Creation & Symbol Synchronization (`2do`)**:
  - Map `G-I-P-S-O` fields to structured OpenProject description markdown blocks / custom fields and standardize icon prefix tokens so `opCall.js wp.create` and `wp.get` natively preserve symbol + variable fidelity.

### 2.3 Output Specification & Concrete Structural Draft

#### A. Logical Variable Grammar Template
```yaml
task_spec:
  vars:
    repo: "MasterOfArts"
    goal: "MoA Public Website Draft"
    task: "Hero & Navigation Flexbox Architecture"
    subtask: "Mobile Drawer & Essay Index Integration"
    op_id: "OP-WP#163"
    layer: "L1_PRIORITY_GOAL" # L1_PRIORITY_GOAL | L2_NICE_TO_HAVE | L3_OTHER_WP
  symbol: "cube_output_critical"
  G: "${goal} > ${task} > ${subtask}" # Omitted inline when expanded directly under ${goal} cube
  I_sources_by_priority:
    - "[P1] MasterOfArts/content/essays-index.md (live copy source)"
    - "[P2] MasterOfArts/styles/layout.css (grid tokens)"
  P_framework: "Progressive Wireframe -> Component Skeleton -> Responsive Breakpoint Check"
  S_skills_by_priority:
    - "[P1] Frontend UI Architecture"
    - "[P2] Editorial Copy Editing"
  O_deliverable:
    type: "multi_file" # multi_file | single_file_headers
    artifacts:
      - path: "MasterOfArts/src/index.html"
        headers: ["#hero-statement", "#essay-catalog", "#reading-drawer", "#contact-cta"]
      - path: "MasterOfArts/src/styles/nav.css"
        draft_note: "CSS grid sticky header + <details> drawer toggle"
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
- Standardize OpenProject description template containing strict `## Goal`, `## Input (Sources by Priority)`, `## Process (Framework)`, `## Skills (Priority)`, and `## Output (Files / Headers & Draft)` anchors.
- Extend `agent-skills/skills/openproject` read/write validator to parse and verify `G-I-P-S-O` completeness before promoting a work package into `PrecapWeek` Priority Goals.

### 2.4 Definition of Done (`DoD`)
1. Every Matrix 1 node (`L1` Priority Goal, `L2` Nice-to-Have, `L3` Work Package) validates cleanly against the `G-I-P-S-O` variable schema.
2. Interactive tree mockup renders top-row clickable cubes fanning vertically into child cubes + concise `I-P-S-O` drawers without repeating parent Goal text unnecessarily.
3. Symbol table maps 1:1 to both HTML CSS glyphs and OpenProject task templates, with OpenProject sync steps verified via read-only `opCall.js` inspection in follow-up execution.

---

## 3. 5-Component Verification Readiness Note

1. **Observation**: `ADPT-EXEC-TASKSPEC-v0.1` (`EM-13`) already established the 6 pre-work alignment fields (`Input`, `Sources`, `Process`, `Skills`, `Output`, `Redraft`), and Leela's `stats_cube_symbol.dart` already implements a 4-tier cube/envelope symbol taxonomy (`Chunk`, `Sequence`, `Epic`, `Branch`).
2. **Logic Chain**: Combining `EM-13`'s epistemic rigor (`Goal` path + ranked `Sources` + explicit `Process` framework + file/header `Output` draft) with Leela's visual cube grammar yields a single unified task primitive that drives both Matrix 1 recursive tree drill-downs and OpenProject task authoring.
3. **Caveats**: OpenProject server custom-field support is not yet live-verified in this handover; markdown-header standardization inside WP `description` requires zero DB schema risk and acts as the default first slice.
4. **Conclusion**: Handover ready for operator direction review prior to implementing UI prototype and OpenProject template patches.
5. **Verification Method**: Validate JSON/YAML fixtures of `G-I-P-S-O` across all 5 repos against zero missing priority/framework/output fields and inspect clickable tree expansion in a standalone Matrix 1 prototype.
