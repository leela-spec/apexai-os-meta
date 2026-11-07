---
type: design-fixture
id: M01-NORTHSTAR-PORTFOLIO-MOCK-20261106
title: Northstar live-grounded portfolio mock
description: Full visible OpenProject goal coverage with proposed detail, dependency and priority examples at several complexities.
status: draft_for_operator_review
date: 2026-11-06
scope: [mock_data, northstar, project_management]
---

# Northstar live-grounded portfolio mock

## Boundary

Native work-package names, states, priorities, hierarchy and relations are snapshot facts. Additional detail items, their example states, proposed relations and attention categories are mock proposals. No OpenProject records, services, messages or project implementations were changed. This is a planning example supporting the goals, not proof that the goals are complete or that the proposed plan is sufficient.

## Open the result

- [Northstar style stress test](northstar-stress-test.html): all 249 items in Northstar cards and nested detail, with state icons, typed dependencies, eight complexity entry points, and optional browser search/filter controls. Core content is pre-rendered for viewers that suppress JavaScript.
- [Desktop preview](northstar-stress-desktop.png), [phone preview](northstar-stress-mobile.png), and [phone detail preview](northstar-stress-detail.png).
- [Stress-test browser verification](northstar-stress-verification.json): content coverage, search context, exact-state filters, ancestor opening, expansion controls, JavaScript-disabled content, runtime exceptions, and fully expanded width checks at 1440, 430 and 360 pixels. All checks passed; all 762 expandable sections fit without page-level horizontal overflow. The embedded phone file viewer remains untested.
- [Expandable portfolio review](northstar-portfolio-review.html): static HTML with native details/summary controls; content does not depend on JavaScript. This is a data review, not the final Northstar visual design.
- [Complete mock dataset](northstar-portfolio-mock.json): machine-readable portfolio, native records, mock children, priorities, readiness caveats, typed relations and dependency-compatible review layers.
- [Authored scenario proposals](scenario-proposals.json): rationale, additional acceptance examples and proposed relations.
- [All-status live snapshot](openproject-all-statuses-20261106.json): authoritative input for this fixture.
- [Direct endpoint checks](endpoint-checks-20261106.json): explains why relation endpoints missing from the initial collection remained accessible by direct read.
- [Initial default-view discovery snapshot](openproject-snapshot-20261106.json): discovery evidence only; the default status filter omitted closed work. Do not use it as the complete task inventory.
- [Northstar decisions and dependency visualization 2do](../NORTHSTAR-DECISIONS-AND-2DO-20261106.md).

## Coverage and verification

The paginated all-status API read returned 15 projects, 227 work packages, and 91 relations. The fixture retains every native work package, including closed/rejected records and sample-project records, and adds 22 local mock detail items plus 25 proposed relations. The resulting 249 items and 116 relations have valid endpoints. Native objects were compared field-for-field with the snapshot; names and statuses were checked separately. The combined proposed ordering graph and parent hierarchy were checked for cycles. Review-layer calculation produced 15 layers; those are not calendar slots or critical-path duration estimates.

These counts come from the inline Node snapshot and verification commands executed in this session, using `opClient.request('GET', path, cfg)` from the canonical skill client. Pagination checked unique IDs against API totals. The all-status work-package path was `/api/v3/work_packages?filters=[{"status":{"operator":"*","values":[]}}]&pageSize=100&offset=<page>` with the filters value URL-encoded. Projects and relations were paginated similarly. The skill CLI did not forward pagination for `relation.list`, so the shared client provided the intent-preserving read-only fallback.

The static review page contains a visible icon and exact status label for each item. Every native and mock item was verified to have an HTML anchor. All proposed attention categories remain unapproved. A 430-pixel-wide Chromium screenshot was used for phone-layout inspection; the user's embedded viewer itself was not controlled or tested.

## Detail levels and complexities

| Example | Actual native anchors | Detail and dependency shape |
|---|---|---|
| Rhythm evidence refresh | #174, #175, #176 | Simple independent work; three mock review details, no invented serial chain. |
| Website content | #163, #204 | Source selection → transformation → review, plus a separate credits branch joining one illustrative ACIM publication. Other content does not inherit that dependency. |
| IPOS research intake | #223–#228 | Native parent plus five real goals; local sample acceptance details cover intake, digest checking, alternative evaluation and retirement approval. Proposed retirement checkpoint waits for replacement evidence. |
| PM taxonomy | #121 → #126 → #127–#130 | Three native work-package hierarchy levels; proposed session → human approval → authorized creation → verification. The example does not perform creation. |
| Sequencing waves | #215 → #216–#220 | Observed follows chain plus mock acceptance details; descriptions saying landed/BLOCKED remain separate from native New status. |
| Identity and progression | #159/#187/#188, #196/#189/#190, #164/#192/#193 | Cross-project fan-out from canonical identity into Skill Tree relations and Path-owned progression. Structural relations do not become unlock policy. |
| Runtime release | #205, #206–#212 | Closed native prerequisites plus two open independent fixes; proposed seven-fix evidence review joins both branches. Native relates edges remain associations. |
| Core interaction | #59–#67 | Existing parallel branches, serial constraints and integration join; preserved without needing mock dependencies. |

The general drilldown is portfolio → project → native parent/child levels → local mock acceptance detail. Native types do not impose a universal hierarchy. Dependency references are separate from ownership nesting.

## Priority and dependency logic

Native Priority is preserved unchanged. The additional `proposedPriority` bucket explains suggested attention: enabler candidate, design/readiness review, reconcile first, decision needed, ordinary goal candidate, deferred candidate, history, sample-only, or outside-workstation-scope. These categories do not establish a total order between unrelated project goals. Dependency-compatible review layers show permissible ordering for inspection; operator intent and capacity still determine selection.

`follows` retains ordering semantics. `requires` retains prerequisite semantics. `relates` is never interpreted as a blocker. Both native and proposed edges keep their provenance. The mock graph includes only proposed requires/follows edges with a concrete rationale. Parent/child structure does not automatically create an edge or completion gate.

Closed means PM-closed, not independently proven implementation. Rejected means excluded, not successful. Missing predecessor evidence and unresolved description/status conflicts prevent a claim of executable readiness. Mock acceptance criteria describe desired evidence, never fabricated passing results.

## Findings and open decisions

- The default work-package collection omitted 36 closed/rejected items. Explicit all-status retrieval recovered them and resolved all relation endpoints against the complete inventory.
- Sequencing #216/#217 describe landed work while native status remains New. Verify repository evidence and PM freshness before treating them as new implementation tasks.
- #219/#220 describe BLOCKED while their native status remains New. Northstar needs a separate dependency/readiness explanation alongside the exact status icon.
- #205's description requires seven accepted fixes, while relations to #211/#212 are relates. The proposed release checkpoint makes acceptance explicit without changing the native relation semantics.
- Empty native project containers remain empty. No goals were invented for MoA-Business, MoA-Content, or the Leela & Mastery portfolio container.
- The ApexAI-OS stack-related work remains visible metadata, categorized outside workstation execution scope; no separate stack was accessed.
- Operator decisions remain open: relative project focus, acceptance of proposed dependencies/details, reconciliation of stale PM state, missing implementation evidence, and the layered-menu versus Northstar dependency presentation choice in NS-T01.

## Failure guards

- [P0 | I99] Do not publish mock priorities, states or relations as OpenProject facts.
- [P0 | I98] Do not infer executable readiness from a topological layer or a Closed predecessor alone.
- [P0 | I97] Do not send the IPOS Telegram digest, retire services, create projects or execute the described work as part of inspecting this fixture.
- [P0 | I96] Re-read live records and accepted repository evidence before using this dated snapshot for real planning.
