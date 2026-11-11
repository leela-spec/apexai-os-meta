---
type: visual-planning-example
id: M01-NORTHSTAR-PORTFOLIO-VISUALS-20261107
title: Northstar portfolio overview, dependency atlas and proposed timeline
description: Whole-portfolio visual planning example with native source facts and explicitly hypothetical review windows.
status: proposed_for_operator_review
date: 2026-11-07
scope: [portfolio_overview, dependency_graphs, weekly_timeline, gantt]
---

# Northstar portfolio visual example

## Invariants

- [P0 | I99] Source subjects, states, project ownership and typed relations remain observed snapshot facts.
- [P0 | I98] Every date window is an illustrative local proposal; no native dates, durations, estimates or commitments are implied.
- [P0 | I97] Later windows remain conditional on prerequisite acceptance and current implementation evidence.
- [P0 | I96] A parallel lane does not establish available operator capacity; a bar spanning non-working days is a review window, not continuous effort.

## Open the visuals

- [Northstar visual dashboard](northstar-portfolio-visual.html).
- [Eight-page printable visual report](northstar-portfolio-visual-report.pdf).
- [Full portfolio Gantt](portfolio-gantt.svg).
- [Gantt preview image](portfolio-gantt-preview.png).
- [Proposed week preview](portfolio-week-checked.png).
- [Dependency-map preview](portfolio-dependencies-checked.png).
- [Date assumptions and proposed workflow edges](portfolio-visual-plan.json).
- [Whole-portfolio native source feed](northstar-weekly-feed.json).

## What the views show

The portfolio overview retains all 13 non-sample project containers and all 186 native work packages. Its stacked bars show native states, not a computed completion percentage. Empty project containers remain empty.

The weekly board spans 9–15 November 2026. It offers a cross-project focus scenario: runtime reliability, identity/placement, Website content, IPOS operations, Sequencing readiness, and Rhythm evidence. Primary candidates and alternatives remain visually distinct. Alternatives can replace primary work rather than increase the workload. Sunday is off.

The Gantt spans 9 November–6 December 2026 and places example review/decision windows against 38 native work packages across ten project areas. The other 148 native items have no date proposal. This is not a delivery forecast. Multi-day windows do not claim enough capacity to finish the underlying work package, and do not assign an effort estimate. A bounded content slice does not imply completion of the whole content program. Empty containers and unplaced items remain inspectable.

The dependency atlas includes eight source-grounded diagrams:

| Diagram | Meaning |
|---|---|
| [Identity and Path](dependency-identity.svg) | Canonical identity feeds two native requires relations; native ownership is separately dotted. |
| [Runtime and release](dependency-runtime.svg) | Closed outbox prerequisite and open runtime goals; relates edges remain non-blocking associations. |
| [Core interaction](dependency-core.svg) | Actual parallel branches and integration join. Four transitive duplicate arrows are omitted for readability; their relations remain in source detail. |
| [Sequencing waves](dependency-waves.svg) | Actual follows chain with status/description conflicts still visible. |
| [IPOS](dependency-ipos.svg) | Native goals; a purple dashed inventory-before-benchmark edge is a proposed interpretation. Other work remains visibly unconnected. |
| [PM approval](dependency-taxonomy.svg) | Explicitly proposed session → approval → creation → verification workflow. Native On hold remains visible. |
| [Website](dependency-website.svg) | Actual content and credits goals without inventing a recorded dependency. |
| [Rhythm](dependency-rhythm.svg) | Three independent evidence-review candidates without invented serial constraints. |

Solid prerequisite/order arrows point from predecessor to dependent. Numeric arrow-label references identify relation records, not new work-package endpoints; exact work-package IDs are on the nodes and full native direction/type is available in source detail. Grey dotted ownership is not a blocker. Blue dashed relates edges are associations. Purple dashed edges are proposals. Identity prerequisite arrows route around intermediate ownership nodes so they cannot be mistaken for dependencies on those child nodes.

## Verification

[Initial browser/data verification](portfolio-visual-verification.json) checked 186 source rows, 13 project containers, eight diagrams, seven day columns, 38 Gantt windows, matching source ownership, no duplicate IDs, task selection, project highlighting, source search, task/owner reveal, no browser exceptions and static chart content without JavaScript. It checked all 19 observed follows/requires relations whose two endpoints have proposed windows: every predecessor window ends before its dependent window starts. That check proves ordering consistency only, not feasibility or acceptance.

[Final visual verification](portfolio-visual-final-check.json) rechecked the corrected identity routing, Gantt connectors, complete source rows, no-JavaScript chart visibility and page widths 1440, 430 and 360 without page-level horizontal overflow. Wide diagrams and the Gantt intentionally pan within their own chart surfaces on a phone.

Chromium rendered only local artifact files. `Page.printToPDF` produced the [visual report](northstar-portfolio-visual-report.pdf). Poppler `pdfinfo` reported eight pages; `pdftoppm -scale-to 1600 -png` rendered them for visual inspection. The first six pages use landscape A3; the two Gantt pages use square 420 mm pages to preserve readable labels. The full SVG remains available for zooming and printing. The embedded phone attachment viewer itself was not controlled or directly tested.

The [planning data](portfolio-visual-plan.json) and [source feed](northstar-weekly-feed.json) are the reproduction inputs. The live snapshot is dated 2026-11-07T09:14:26.576Z; this rendering task did not claim a later refresh or inspect current implementation repositories. No OpenProject or calendar records changed.

## Open decisions and failure guards

- [P0 | I99] Approve the focus scope and actual capacity before using any proposed date position operationally.
- [P0 | I98] Reconcile source-description claims and current acceptance evidence before releasing a dependent window.
- [P0 | I97] Do not equate ownership nesting, association or a proposed workflow edge with an observed hard prerequisite.
- [P0 | I96] Do not treat a dated source snapshot or a PM-closed state as verified current implementation.
