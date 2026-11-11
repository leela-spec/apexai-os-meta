---
type: design-decision-record
id: M01-NORTHSTAR-DECISIONS-20261106
title: Northstar display decisions and dependency visualization 2do
description: Accepted operator display decisions, source findings, proposed information order, and unresolved dependency presentation choices.
status: working
date: 2026-11-06
scope: [northstar, matrix_1, display_logic]
tags: [weekly-precap, northstar, design-decisions]
---

# Northstar display decisions and dependency visualization 2do

## Invariants

- [P0 | I98] Preserve native OpenProject work-package identities, types, statuses, hierarchy, and relation types.
- [P0 | I97] Label mock details at their point of display; never present them as live OpenProject facts.
- [P0 | I96] Keep Matrix 1 focused on project development and selection; sequence, sprint, and calendar allocation belong downstream.
- [P0 | I95] This record authorizes no OpenProject mutations and makes no claim that the prototype implements these decisions.

## Accepted operator decisions

| ID | Decision | Display consequence |
|---|---|---|
| NS-D01 | Use Northstar as the selected design direction. | Develop its progressive project drilldown as the baseline. |
| NS-D02 | Outcome is the name of the item. | Use the item name as its primary heading; do not add a separate mandatory Outcome field. For a live work package, use its subject. Keep deliverables and acceptance evidence in detail. Do not rename source records. |
| NS-D03 | Represent current state with a visible icon or similar visual indicator. | Put a state indicator beside the item name. Preserve the exact native status in an accessible label and inspectable text. The visual encoding remains open. |
| NS-D04 | Use real live data; create mock details where live data lacks sufficient detail. | Preserve observed fields and add visibly labelled mock supplements. A mock relation must remain distinct from an observed relation. |
| NS-D05 | Create a 2do to evaluate dependency visualization. | Compare a layered, expandable bullet-list menu with the existing Northstar presentation. Neither dependency visualization is accepted yet. |

## Findings and evidence

Existing research already identifies baseline, next target, expected artifact, completion proof, critical prerequisite, and decision needed as separate information needs. It recommends progressive disclosure and compact blockers with deeper graphs on demand. It does not establish the ranked display order below as an accepted operator decision.

Source documents:

- [Matrix 1 target capability and data contract](ORCHESTRATOR-MATRIX-1-DESIGN-HANDOVER-20261106.okf.md), sections 3 and 4.
- [Working design and typed dependency pipeline](MATRIX1-R1-WORKING-DESIGN-20261106.okf.md), operator story and non-temporal pipeline.
- [Review guide](prototypes/Matrix1-Review-Guide.md), Question 3 and shortlist/longlist semantics.
- [Accepted source authority and Matrix 1 boundaries](OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md), decision ledger and Q06.
- [Current showroom](prototypes/matrix1-design-showroom.html).
- [Canonical OpenProject skill](C:/GitDev/agent-skills/skills/openproject/SKILL.md).

Live read receipts from this session on 2026-11-06; these are observations, not an automatic refresh:

| Command through the canonical Node client | Observed result | Design implication |
|---|---|---|
| `opCall.js root` | OpenProject 17.8.0 | Use instance terminology. |
| `opCall.js whoami` | User 4, OpenProject Admin | Authenticated reads succeeded. |
| `opCall.js doctor --project 8` | Pass; project ApexAI-OS | The selected project is accessible. |
| `opCall.js type.list --project 8` | Task, Milestone, Summary task, Feature, Epic, User story, Bug | Types are source data; do not impose a universal Epic-to-Task hierarchy. |
| `opCall.js status.list` | Native statuses include New, In progress, Developed, In testing, Tested, Closed, On hold, Rejected | Icon mapping must preserve meaningful distinctions and exact labels. |
| `opCall.js wp.get --id 220` | Task #220, subject Wave C5 — fixtures parity and Wave C exit proof; project Sequencing; parent #215; status New; description says BLOCKED | Native status and descriptive blocker claims are separate facts. |
| `opCall.js relation.list` | Returned relation #91: #220 follows #219; sampled relations also include requires and relates | Preserve relation direction and type. The sampled relation collection is not a complete dependency audit. |

Client path for reproducing these commands: `C:/GitDev/agent-skills/skills/openproject/client/opCall.js`; invoke with `node`. No OpenProject records were changed.

## Proposed information order

This order incorporates NS-D02 and NS-D03; the ranking remains a design proposal.

| Rank | Information | Initial presentation |
|---|---|---|
| 1 | Item name, representing the outcome | Primary heading; exact subject for a native work package. |
| 2 | Current state | Visible indicator beside the name, with exact status accessible. |
| 3 | Next actionable work package | Name, identity, and why it moves the project forward. |
| 4 | Dependencies and readiness | Immediate prerequisite, what it unlocks, and unknowns; presentation pending NS-T01. |
| 5 | Weekly selection and why now | Proposed or selected shortlist; distinct from native Priority. |
| 6 | Deliverable and completion evidence | Inspectable detail describing what success produces and proves. |
| 7 | Decision or intervention needed | Elevate to the collapsed card when action is required. |
| 8 | Hierarchy and ownership | Native parent, children, type, project, and assignee in drilldown. |
| 9 | Deferred opportunities | Longlist with reason and reconsideration trigger. |
| 10 | Supporting metadata | Source, freshness, dates, estimates, attachments, and activity on inspection. |

Source/mock provenance accompanies every affected value regardless of this ranking. A consequential blocker or decision can rise to the project summary.

## 2do: NS-T01 — choose the dependency visualization

Status: OPEN. Deliverable: side-by-side examples using the same work packages and relations, with a recommendation for operator review.

- [ ] Render option A: a layered, expandable bullet-list menu. Clearly distinguish hierarchy nesting from dependency references; a child is not automatically a prerequisite.
- [ ] Render option B: the existing Northstar card/drilldown treatment, with typed dependency details inside the relevant item.
- [ ] Use the same live example in both options, starting with #220 and its observed relation to #219 after fresh reads.
- [ ] Add labelled mock cases for any missing comparison cases: parallel prerequisites joining one result, cross-project dependency, unknown prerequisite state, and review/rework.
- [ ] Check whether the operator can identify what comes first, what is blocked, what can run in parallel, and what unlocks the next result.
- [ ] Check phone readability, expansion depth, keyboard access, and exact relation/source traceability.
- [ ] Recommend a presentation and record the operator decision before promoting it to the design.

## Open questions

| ID | Question |
|---|---|
| NS-Q01 | Which icon vocabulary should represent each native status, and which states can share an icon while retaining exact labels? |
| NS-Q02 | Should dependency readiness have a second indicator beside native status, or appear only in the dependency detail? |
| NS-Q03 | Which dependency presentation wins NS-T01, and how many levels should open initially? |
| NS-Q04 | At portfolio level, should an item heading show the project name or its currently selected work-package name? Work-package headings use their source subject. |
| NS-Q05 | Where should a non-outcome-oriented source subject be supplemented with explanatory text while preserving its exact name? |
| NS-Q06 | How should description/status conflicts such as #220's BLOCKED description and New status be surfaced? |
| NS-Q07 | What exact rule should derive readiness from relation type, predecessor state, and acceptance evidence? Do not assume Closed proves working implementation. |
| NS-Q08 | Which projects and how much of their work-package frontier should the next live prototype include? |

## Failure guards

- [P0 | I99] Never infer dependency edges from list order, visual nesting, parentage, or similar names.
- [P0 | I98] Never collapse follows, requires, blocks, and relates into one generic blocking relation.
- [P0 | I97] Never infer executable readiness solely from absence of observed blockers in a partial read.
- [P0 | I96] Never communicate status solely through color or an unexplained icon.
- [P0 | I95] Keep proposed rankings, visual mappings, and open questions distinct from accepted operator decisions.
