# Matrix 1 — Design exploration review guide

**Date:** 2026-11-06  
**Status:** Operator design exploration; NOT a production runtime patch or live OpenProject snapshot.  
**Source:** Historical W45 draft in `leela-spec/apexai-os-meta`, plus current AGENTS.md documents in MasterOfArts, Investment and Leela-Cloud-2026. All four projects' tasks, priorities, relationships and statuses in this interactive gallery are illustrations, not established live truth.  
**Working preference:** V3 progressive drilldown.

## Open the prototype

Double-click `matrix1-design-showroom.html` in a browser. It is self-contained and should work offline. Choose any of the **12 designs** in the gallery, then expand projects and workstreams. Select another project using the dropdown. The *Stage →* / *↑ Prioritize* controls update **local demonstration state**, not project records. The JSON export produces a clearly labelled **unapproved demo selection**.

Use the **Q2 · Hierarchy lab** to understand source-native task structure versus display grouping. Use the **Q3 · Graph lab** to compare five dependency notations. The **Synthesis** tab explains proposed combinations.

## Twelve directions to compare

| Design | Distinct operator experience | Main tradeoff |
|---|---|---|
| 01 Northstar | Strategic portfolio overview, calm expandable cards | Complex dependency joins need secondary detail |
| 02 Command Center | Dense telemetry, priority signals, technical focus | Can feel operationally noisy |
| 03 The Editorial | Narrative-first chapters, accessible weekly briefing | More scrolling and less density |
| 04 Portfolio Ledger | Source-auditable rows with expanded project inspector | Less visual process intuition |
| 05 The Atlas | Horizontal workstreams, parallel opportunities | Wide presentation needs mobile fallback |
| 06 Priority Horizons | Distinct shortlist/longlist/opportunity board | Require linked dependency inspector |
| 07 Outcome Staircase | Ordered acceptance gates, easy development sequence | Poorer for simultaneous joins/forks |
| 08 Evidence Dossier | Source provenance and contradictions first | Too compliance-oriented for daily planning |
| 09 Constellation | Exploratory portfolio relationships | Must never render weak associations as blockers |
| 10 The Switchboard | Operator intervention and priority choices | Interaction must not imply PM writes |
| 11 Focus Studio | One important project's full progressive detail | Requires separate portfolio-comparison layer |
| 12 Signal & Story | Plain-language questions and next steps | Task identity needs explicit inspector |

## Question 2 — Why different hierarchies?

**Illustrative example: Invoice schema.** OpenProject could own a work package below a broad operational parent, the repository could store implementation under `Business/`, and the operator-facing section could present the task under `Invoice-to-accounting`. Those are *different views of one work item*, not three work items. If native OP hierarchy differs from intended operator explanation, display grouping adds useful interpretation **without moving, copying or rewriting any OP work packages**.

**Illustrative example: Investment.** A pipeline timeout and dashboard wiring might have different native owners/epics, while the operator wants to read them together as `Ingestion → reliable data → dashboard`. Their original reference IDs stay unchanged.

**Illustrative example: Leela/Apex shared dependency.** A Leela prerequisite can be linked in an Apex project process; both owners and native identities remain separate, and the link becomes a *blocking prerequisite* only with verified evidence.

- A = show native OP hierarchy only.
- B = preserve native ownership and work refs; add presentation-only workstream groupings **(recommended for review, not accepted)**.
- C = create a replacement canonical hierarchy **(not recommended; risks duplicate PM truth)**.

## Question 3 — What should a dependency look like?

1. **Process ribbon:** for serial work (schema → PDF → export).
2. **Branch-and-join DAG:** for parallel prerequisites (interceptor → latency and HUD → release).
3. **Acceptance gate:** for operator comprehension (release waits for two proofs), especially at the overview level.
4. **Cross-project swimlane:** for work requiring a result owned by another project.
5. **Review/rework annotation:** for iteration; not a cyclic prerequisite edge.

A strong V3 hybrid would show a one-sentence blocker at collapsed project level, an acceptance-gate or ribbon in expanded epics, and a full fork/join diagram only where its extra detail makes the next decision clearer.

## Shortlist and longlist: working semantics

- **Shortlist**: operator-chosen, outcome-linked, highest-priority proposed weekly work. Not a fixed count, not committed until operator approval. Each entry should say *why now*, what evidence would show success, and which upstream dependency determines readiness.
- **Longlist**: worthy opportunities, nice-to-haves and work deferred behind real prerequisites. Distinguish optional work from blocked work to avoid hiding readiness constraints.
- **Dynamic scope**: one project may receive one meaningful outcome and another six; task count is determined by operator intent, goal complexity, readiness and available capacity. Prioritization can be hierarchical (portfolio → project → epic → task), without a synthetic master score.

## Design-review perspectives (human-authored, not spawned agents)

| Lens | Strong candidates | Main concern |
|---|---|---|
| Operator scan speed | Northstar, Signal & Story | Make the next consequential action visible immediately |
| Deep project navigation | Focus Studio, Northstar | Preserve all levels without losing overall context |
| Dependency comprehension | Atlas, Outcome Staircase plus branch/merge on demand | Do not draw unverified critical paths |
| Source authority and evidence | Evidence Dossier, Portfolio Ledger | OP task status does not prove working code |
| Weekly outcome selection | Priority Horizons, Switchboard | High priority versus optional/blocked should be explicit |

**Synthesis hypothesis:** V3 overall, Northstar as overview, Focus Studio for expanded project detail, Priority Horizons for shortlist/longlist, Evidence Dossier for verification, and a compact gate-or-graph inside relevant epics.

## Validation and remaining decisions

- Twelve layouts were rendered with Chromium, and navigation, four-project content, hierarchy lab, five dependency diagrams and local priority controls were checked. Desktop and narrow mobile widths were exercised.
- Live OpenProject project enrolment, work package status and dependency directions were **not** verified; the demo never makes up numeric work package IDs.
- **Operator input still needed:** hierarchy choice after examples (M1-D02), graphical dependency treatment (M1-D03), preferred top two or three layouts/features, and whether global Q13 source/rendering solution is to be decided later as planned.
- All production files and PM records are untouched. Source and proposed decisions are recorded in GitHub research documents; this interactive HTML is a standalone chat-delivered artifact, not a production-committed template.
