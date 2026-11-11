---
type: export-example-study
id: M01-NORTHSTAR-EXPORTS-WEEK-20261109
title: Actual OpenProject outputs and proposed Northstar week
description: API-derived examples of native export formats, a verified source-field bridge, and a Northstar project overview with proposed priorities for 9–15 November 2026.
status: draft_for_operator_review
date: 2026-11-07
scope: [exports, northstar, actual_data, weekly_priority_proposals]
---

# Actual OpenProject outputs and proposed Northstar week

## Invariants

- [P0 | I99] Generated examples are local API-derived renderings, not native OpenProject downloads.
- [P0 | I98] Native subjects, statuses, priorities, hierarchy and relation types remain source facts; weekly ranks and slices are labelled proposals.
- [P0 | I97] Missing source dates, estimates, assignees and acceptance proof remain unknown.
- [P0 | I96] The fixture creates no PM commitments, calendar allocation, work-package mutation or implementation claim.

## Open the result

- [Export gallery](index.html): examples, native-route results and the source-to-Northstar mapping.
- [Northstar project overview and proposed week](northstar-next-week.html): all 186 non-sample work packages across 13 project containers, with exact states and typed relations.
- [Portfolio workbook](portfolio-and-proposed-week.xlsx): source tasks, full descriptions, projects, relations and a separate proposed-week sheet.
- [Weekly feed](northstar-weekly-feed.json): native portfolio facts plus six separate priority proposals.
- [Actual export-to-Northstar read-back trace](export-to-northstar-trace.json): CSV rows joined to XLSX description and relation sheets by native ID, then compared to the source snapshot.

## Output examples

The common comparison scope is six real Sequencing work packages: #215, #216, #217, #218, #219 and #220. Full-portfolio files separately retain every non-sample item, including PM-closed items. No mock work packages or invented dependency edges are used.

| Format example | File | What it retains |
|---|---|---|
| PDF Table | [One-page table](example-pdf-table.pdf) | Native ID, subject, type, state, priority and parent. |
| PDF Report | [Ten-page report](example-pdf-report.pdf) | Contents, complete source descriptions and the four relations inside the common scope. Source Markdown is preserved as readable source text rather than presented as an exact native report layout. |
| PDF Report with images option | [Ten-page report](example-pdf-report-with-images.pdf) | Same source scope; no embedded image references exist in the selected descriptions, so none are invented. |
| Spreadsheet table | [XLSX table equivalent](example-table.xlsx) | Native table fields and provenance notes. This is not a renamed XLS file. |
| Spreadsheet with descriptions | [XLSX description equivalent](example-descriptions.xlsx) | Native rows and exact full descriptions in a separate sheet. |
| Spreadsheet with relations | [XLSX relation equivalent](example-relations.xlsx) | Native rows and exact typed relation endpoints/IDs in a separate sheet. |
| CSV | [Six-item CSV](example-work-packages.csv) | Common comparison scope in UTF-8 CSV. |
| Atom | [Snapshot feed](example-snapshot.atom) | Six source subjects, descriptions and native update timestamps. This is not a journal/change feed. |
| Gantt availability | [Date readiness CSV](gantt-data-readiness.csv) | Missing native dates are explicit. No schedule is fabricated. Native Gantt export was not advertised in the tested representation list. |

Additional full-portfolio outputs: [projects CSV](portfolio-projects.csv), [work packages and descriptions CSV](portfolio-work-packages.csv), [relations CSV](portfolio-relations.csv), and [live snapshot JSON](live-snapshot.json). The snapshot includes the two sample projects for source provenance; the 13-project Northstar scope excludes them.

## Native export boundary

[Native-export test receipts](native-export-status.json) preserve advertised representation URLs without credentials and the HTTP outcomes from the available API credential. PDF Table, PDF Report, PDF Report with images, XLS, XLS with descriptions, XLS with relations and CSV returned HTTP 406. Atom returned HTTP 302 to login. No native file was obtained. These outcomes do not establish that exports fail for a signed-in browser user. No browser was used against OpenProject and no web-login credential was requested.

The read-only fallback used the canonical skill's shared `opClient.js`. It generated openly labelled local examples from authenticated API data. No substitute was named `.xls`; modern XLSX equivalents carry their actual format. The XLSX variants illustrate equivalent information, not native worksheet/layout fidelity. The PDF examples likewise illustrate source content rather than pixel-identical native export styling.

Primary references:

- [Canonical OpenProject skill](C:/GitDev/agent-skills/skills/openproject/SKILL.md).
- [Native export documentation](https://www.openproject.org/docs/user-guide/work-packages/exporting/).
- [Native PDF report documentation](https://www.openproject.org/docs/user-guide/work-packages/exporting/pdf-report/).
- [Version 17.8.0 work-package controller](https://github.com/opf/openproject/blob/v17.8.0/app/controllers/work_packages_controller.rb).

## How exports feed Northstar

1. Read ID, subject, project, type, state, native Priority and parent from CSV/XLSX. The item name becomes the visible heading and exact state receives a visible indicator.
2. Join full descriptions by ID. Preserve acceptance criteria and descriptive baseline claims without turning them into proven implementation status.
3. Join relation IDs, types and endpoints. `follows` remains ordering, `requires` remains a prerequisite and `relates` remains association. Parentage is separate.
4. Build the project overview from the complete API snapshot, including PM-closed prerequisites. An open-only collection is insufficient for a complete dependency view.
5. Add proposed rank, rationale, preconditions, bounded slice and acceptance as a separate interpretation layer.

The read-back trace performs steps 1–3 on the actual generated files. Northstar's full portfolio and weekly feed use the same fresh source snapshot; Northstar does not need to parse a PDF. A concrete trace is #218: CSV says New; the description says the validation-memo/formula objective remains open; relation #89 says #218 follows #217. Proposed action: verify A/B1 evidence and the current execution gate, then identify the bounded C3 gap. No source status is rewritten.

## Proposed priorities for 9–15 November 2026

These ordinal ranks express a reasoned example, not an operator-approved priority order or a capacity-feasible commitment. Saturday remains available in principle; Sunday is off by default. No dates or slots are assigned to tasks.

| Rank | Actual source work | Why now | Suggested bounded result |
|---|---|---|---|
| 1 | #211 and #212 | Source descriptions report runtime completion and timer failures. #211 requires #207, which is PM-closed but still needs current evidence. No edge says #212 blocks #211. | Verify the reported current gap and select one focused runtime fix if it still exists. |
| 2 | #159, #187 and #188 | Observed relations #80/#81 make canonical identity a prerequisite for #196 and #164. | Validate one canonical identity / durable placement contract and a reuse/reorder example. |
| 3 | #215–#218 | A/B1 descriptions say landed while PM states say New; the native follows chain puts C3 before C4/C5. | Reconcile the baseline and bound the remaining C3 objective before selecting implementation. |
| 4, alternative | #228 and #225 | Architecture inventory can inform the automation comparison; this ordering is a planning suggestion, not a native dependency. | Source-backed inventory and bounded benchmark question. |
| 5, alternative | #163 | A broad content program needs a selected slice. | Select and review one actual listed source-to-public-component example. |
| 6, alternative | #174 | Source identifies likely stale evidence rather than a proven broken feature. | Re-attest the BP boundary or record the actual discrepancy. |

Current repository implementations, acceptance results and estimates have not been independently verified by this export task. Downstream #219/#220 and identity consumers do not become executable merely because they are visible in the overview. All other project goals remain available; lack of a weekly proposal is not an operator decision to defer them.

## Verification and reproduction

[Browser verification](verification-browser.json) records source preservation, 186 static work-package rows, 13 project cards, six proposals, valid local download links, parent-aware search, hash navigation, full expansion, no runtime exceptions and no-JavaScript content. Layouts were checked at widths 1440, 430 and 360 with no page-level horizontal overflow. The user's embedded file viewer was not directly tested.

[File verification](verification-files.json) records six source IDs read back from CSV/XLSX, exact description-cell equality, four relation rows, six Atom entries, 186 portfolio workbook rows, and PDF page counts. Poppler rendered all 21 PDF pages. [Table preview](pdf-qa/table-1.png) and [report page contact sheet](pdf-qa/report-contact-sheet.png) were visually inspected. The image-option report uses the same source content and layout with its explicit no-images note.

Browser previews: [gallery phone](gallery-mobile.png), [gallery desktop](gallery-desktop.png), [Northstar desktop](northstar-desktop.png), and [Northstar phone](northstar-mobile.png).

Reproduction uses Node with `C:/GitDev/agent-skills/skills/openproject/client/opClient.js`: `getRoot`, `getMe`, and authenticated `request('GET', path, cfg)`. Paginate projects/work packages/relations with `pageSize=100` and `offset`; explicitly request all work-package statuses using `[{"status":{"operator":"*","values":[]}}]`. Verify unique IDs against API totals. The read returned 227 work packages, 15 projects and 91 relations overall; excluding project IDs 1 and 2 yields 186 work packages, 13 containers and 83 internal relations. Of the non-sample work packages, 154 were open; direct field inspection returned no populated start, finish, estimate or assignee values for those open items.

Local examples were produced with Python `csv`, `xml.etree.ElementTree`, `openpyxl` and ReportLab. Spreadsheet validation re-opened files with `openpyxl`; XML validation used ElementTree; PDF page counts and renders used Poppler `pdfinfo` and `pdftoppm`. Chromium automation used only local HTML files.

## Open questions and failure guards

- [P0 | I99] Approve, reduce or reorder the priority proposals before treating them as commitments.
- [P0 | I98] Verify current implementation and predecessor acceptance evidence before starting a source-described gap.
- [P0 | I97] Do not treat an API-authentication export failure as proof that signed-in native exports are unavailable.
- [P0 | I96] Do not imply a native export was downloaded or that a calendar-feasible plan exists.
- [P0 | I95] Keep this private-data bundle local unless the operator explicitly authorizes sharing.
