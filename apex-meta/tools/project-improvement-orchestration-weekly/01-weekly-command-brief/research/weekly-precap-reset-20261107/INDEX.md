---
type: artifact-index
id: M01-PRECAP-RESET-INDEX-20261107
title: Weekly Precap conversation artifact index
description: Complete scoped index of authored conversation artifacts, the modified showroom and this review packet, classified by purpose and authority.
status: complete_scoped_inventory
date: 2026-11-07
scope: [artifact_inventory, research_provenance, handover]
---

# Weekly Precap conversation artifact index

## Read before using these files

- [P0 | I99] Use [HANDOVER.md](HANDOVER.md) and [SOURCE-FINDINGS.md](SOURCE-FINDINGS.md) to establish authority before reusing an artifact.
- [P0 | I98] A source snapshot, mock supplement, proposed date, rendered chart and runtime specification have different authority.

## Scope and reproduction

This index covers the task-owned folders identified in the conversation tool history: `research/northstar-mock/`, `research/northstar-exports-week-20261109/`, the conversation decision note, the workspace design screenshots/render helpers/diagnostics, the modified original showroom, and this handover folder. It does not assert authorship over unrelated dirty repository files. User-provided attachments and temporary browser/runtime caches are excluded. ZIP members are not counted again as separately authored files.

Inventory command: `rg --files --hidden --no-ignore <four task-owned artifact roots>`, plus the named decision note, workspace root `northstar-portfolio*.png` files, the modified showroom and the six packet files. [ARTIFACT-MANIFEST.json](ARTIFACT-MANIFEST.json) records exact absolute paths; [VERIFICATION.json](VERIFICATION.json) records checks.

Existing conversation artifacts: **157 newly created files**, plus **one modified existing showroom**. This packet adds **six files**. Total indexed files: **164**. These counts derive from the command above and the explicit packet list, not a count of all dirty Git paths.

## Group counts

| Group | Files |
|---|---:|
| Download bundles | 2 |
| Export and report examples | 28 |
| Handover packet | 6 |
| Individual design screenshots | 12 |
| Local render helpers | 3 |
| Mock data and stress research | 4 |
| Modified pre-existing source | 1 |
| Other generated evidence | 1 |
| PDF page renders and QA | 40 |
| Proposed planning data | 7 |
| Recorded conversation decisions | 1 |
| Rendered previews | 19 |
| Research notes and local READMEs | 4 |
| Source snapshots and checks | 7 |
| Verification and refinement receipts | 8 |
| Visual planning experiments | 18 |
| Workspace diagnostic previews | 3 |

## Useful entry points

- [Handover README](<README.md>) → [handover](<HANDOVER.md>) → [source map and drift findings](<SOURCE-FINDINGS.md>).
- [Recursive Northstar stress fixture](<../northstar-mock/northstar-stress-test.html>) — useful hierarchy reference, with mock content.
- [Latest visual dashboard](<../northstar-exports-week-20261109/northstar-portfolio-visual.html>) — charts/timeline experiment, not the accepted primary workflow.
- [Specific display decisions](<../NORTHSTAR-DECISIONS-AND-2DO-20261106.md>) — preserve accepted choices; ranking and dependency presentation remain open.

## Original source references — not created in this conversation

- [Original design review guide](<../prototypes/Matrix1-Review-Guide.md>).
- [Original twelve-design overview](<../prototypes/matrix1-twelve-designs-overview.png>).
- [Original design wall](<../prototypes/matrix1-design-wall-16x9.png>).

## Complete file inventory

### Download bundles

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/openproject-outputs-and-northstar.zip](<../northstar-exports-week-20261109/openproject-outputs-and-northstar.zip>) | Packaged artifact snapshot; contents may represent a specific prototype stage | Convenience archive; do not infer production authority from packaging |
| [northstar-exports-week-20261109/portfolio-visual-bundle.zip](<../northstar-exports-week-20261109/portfolio-visual-bundle.zip>) | Packaged artifact snapshot; contents may represent a specific prototype stage | Convenience archive; do not infer production authority from packaging |

### Export and report examples

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/example-descriptions.xlsx](<../northstar-exports-week-20261109/example-descriptions.xlsx>) | Locally generated XLSX equivalent / portfolio workbook | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/example-pdf-report-with-images.pdf](<../northstar-exports-week-20261109/example-pdf-report-with-images.pdf>) | Locally rendered report/table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/example-pdf-report.pdf](<../northstar-exports-week-20261109/example-pdf-report.pdf>) | Locally rendered report/table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/example-pdf-table.pdf](<../northstar-exports-week-20261109/example-pdf-table.pdf>) | Locally rendered report/table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/example-relations.xlsx](<../northstar-exports-week-20261109/example-relations.xlsx>) | Locally generated XLSX equivalent / portfolio workbook | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/example-snapshot.atom](<../northstar-exports-week-20261109/example-snapshot.atom>) | Locally rendered snapshot feed, not journal history | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/example-table.xlsx](<../northstar-exports-week-20261109/example-table.xlsx>) | Locally generated XLSX equivalent / portfolio workbook | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/example-work-packages.csv](<../northstar-exports-week-20261109/example-work-packages.csv>) | Locally generated source table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/gantt-data-readiness.csv](<../northstar-exports-week-20261109/gantt-data-readiness.csv>) | Native date-readiness report | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/northstar-portfolio-visual-report.pdf](<../northstar-exports-week-20261109/northstar-portfolio-visual-report.pdf>) | Locally rendered report/table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/northstar-portfolio-visuals.pdf](<../northstar-exports-week-20261109/northstar-portfolio-visuals.pdf>) | Locally rendered report/table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/example-descriptions.xlsx](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/example-descriptions.xlsx>) | Locally generated XLSX equivalent / portfolio workbook | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/example-pdf-report-with-images.pdf](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/example-pdf-report-with-images.pdf>) | Locally rendered report/table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/example-pdf-report.pdf](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/example-pdf-report.pdf>) | Locally rendered report/table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/example-pdf-table.pdf](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/example-pdf-table.pdf>) | Locally rendered report/table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/example-relations.xlsx](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/example-relations.xlsx>) | Locally generated XLSX equivalent / portfolio workbook | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/example-snapshot.atom](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/example-snapshot.atom>) | Locally rendered snapshot feed, not journal history | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/example-table.xlsx](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/example-table.xlsx>) | Locally generated XLSX equivalent / portfolio workbook | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/example-work-packages.csv](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/example-work-packages.csv>) | Locally generated source table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/gantt-data-readiness.csv](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/gantt-data-readiness.csv>) | Native date-readiness report | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/portfolio-and-proposed-week.xlsx](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/portfolio-and-proposed-week.xlsx>) | Locally generated XLSX equivalent / portfolio workbook | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/portfolio-projects.csv](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/portfolio-projects.csv>) | Locally generated source table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/portfolio-relations.csv](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/portfolio-relations.csv>) | Locally generated source table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/portfolio-work-packages.csv](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/portfolio-work-packages.csv>) | Locally generated source table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/portfolio-and-proposed-week.xlsx](<../northstar-exports-week-20261109/portfolio-and-proposed-week.xlsx>) | Locally generated XLSX equivalent / portfolio workbook | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/portfolio-projects.csv](<../northstar-exports-week-20261109/portfolio-projects.csv>) | Locally generated source table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/portfolio-relations.csv](<../northstar-exports-week-20261109/portfolio-relations.csv>) | Locally generated source table | API-derived example; not a native OpenProject export download or accepted plan |
| [northstar-exports-week-20261109/portfolio-work-packages.csv](<../northstar-exports-week-20261109/portfolio-work-packages.csv>) | Locally generated source table | API-derived example; not a native OpenProject export download or accepted plan |

### Handover packet

| File | Purpose | Authority / caveat |
|---|---|---|
| [weekly-precap-reset-20261107/ARTIFACT-MANIFEST.json](<ARTIFACT-MANIFEST.json>) | Machine-readable inventory | Review documentation; no production behavior change |
| [weekly-precap-reset-20261107/HANDOVER.md](<HANDOVER.md>) | Next-session contract and recovery route | Review documentation; no production behavior change |
| [weekly-precap-reset-20261107/INDEX.md](<INDEX.md>) | Complete scoped artifact links | Review documentation; no production behavior change |
| [weekly-precap-reset-20261107/README.md](<README.md>) | Entry point and spec locations | Review documentation; no production behavior change |
| [weekly-precap-reset-20261107/SOURCE-FINDINGS.md](<SOURCE-FINDINGS.md>) | Specification authority and drift evidence | Review documentation; no production behavior change |
| [weekly-precap-reset-20261107/VERIFICATION.json](<VERIFICATION.json>) | Packet verification receipt | Review documentation; no production behavior change |

### Individual design screenshots

| File | Purpose | Authority / caveat |
|---|---|---|
| [design-previews/atlas.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/atlas.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/command.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/command.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/constellation.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/constellation.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/dossier.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/dossier.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/editorial.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/editorial.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/focus.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/focus.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/kanban.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/kanban.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/ledger.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/ledger.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/northstar.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/northstar.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/signal.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/signal.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/stair.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/stair.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |
| [design-previews/switchboard.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/design-previews/switchboard.png>) | Static top-of-design screenshot from the original twelve-design showroom | Viewing aid; not interactive or a planning specification |

### Local render helpers

| File | Purpose | Authority / caveat |
|---|---|---|
| [visual-render-work/render-charts.cjs](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/visual-render-work/render-charts.cjs>) | Local generation helper; may lag exact-match output refinements | Diagnostic source only; reconcile before reuse |
| [visual-render-work/render-pages.cjs](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/visual-render-work/render-pages.cjs>) | Local generation helper; may lag exact-match output refinements | Diagnostic source only; reconcile before reuse |
| [visual-render-work/visual.css](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/visual-render-work/visual.css>) | Local generation helper; may lag exact-match output refinements | Diagnostic source only; reconcile before reuse |

### Mock data and stress research

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-mock/northstar-portfolio-mock.json](<../northstar-mock/northstar-portfolio-mock.json>) | Native records with labelled hypothetical detail, state, priority or dependency overlays | Mock proposal; not accepted project truth |
| [northstar-mock/northstar-portfolio-review.html](<../northstar-mock/northstar-portfolio-review.html>) | Static portfolio/data review fixture | Prototype; not accepted PrecapWeek behavior |
| [northstar-mock/northstar-stress-test.html](<../northstar-mock/northstar-stress-test.html>) | Northstar stress fixture with recursive hierarchy and optional controls | Prototype; not accepted PrecapWeek behavior |
| [northstar-mock/scenario-proposals.json](<../northstar-mock/scenario-proposals.json>) | Native records with labelled hypothetical detail, state, priority or dependency overlays | Mock proposal; not accepted project truth |

### Modified pre-existing source

| File | Purpose | Authority / caveat |
|---|---|---|
| [prototypes/matrix1-design-showroom.html](<../prototypes/matrix1-design-showroom.html>) | Original twelve-design showroom; added initial hash-based design selection | Source design gallery; not a verified per-design mobile viewer link |

### Other generated evidence

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/portfolio-visual-manifest.json](<../northstar-exports-week-20261109/portfolio-visual-manifest.json>) | Generated study output | Inspect provenance before reuse |

### PDF page renders and QA

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/pdf-qa/report-contact-sheet.png](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/pdf-qa/report-contact-sheet.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/pdf-qa/table-1.png](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/pdf-qa/table-1.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-01.png](<../northstar-exports-week-20261109/pdf-qa/report-01.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-02.png](<../northstar-exports-week-20261109/pdf-qa/report-02.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-03.png](<../northstar-exports-week-20261109/pdf-qa/report-03.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-04.png](<../northstar-exports-week-20261109/pdf-qa/report-04.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-05.png](<../northstar-exports-week-20261109/pdf-qa/report-05.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-06.png](<../northstar-exports-week-20261109/pdf-qa/report-06.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-07.png](<../northstar-exports-week-20261109/pdf-qa/report-07.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-08.png](<../northstar-exports-week-20261109/pdf-qa/report-08.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-09.png](<../northstar-exports-week-20261109/pdf-qa/report-09.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-10.png](<../northstar-exports-week-20261109/pdf-qa/report-10.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-contact-sheet.png](<../northstar-exports-week-20261109/pdf-qa/report-contact-sheet.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-01.png](<../northstar-exports-week-20261109/pdf-qa/report-images-01.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-02.png](<../northstar-exports-week-20261109/pdf-qa/report-images-02.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-03.png](<../northstar-exports-week-20261109/pdf-qa/report-images-03.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-04.png](<../northstar-exports-week-20261109/pdf-qa/report-images-04.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-05.png](<../northstar-exports-week-20261109/pdf-qa/report-images-05.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-06.png](<../northstar-exports-week-20261109/pdf-qa/report-images-06.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-07.png](<../northstar-exports-week-20261109/pdf-qa/report-images-07.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-08.png](<../northstar-exports-week-20261109/pdf-qa/report-images-08.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-09.png](<../northstar-exports-week-20261109/pdf-qa/report-images-09.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/report-images-10.png](<../northstar-exports-week-20261109/pdf-qa/report-images-10.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/pdf-qa/table-1.png](<../northstar-exports-week-20261109/pdf-qa/table-1.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-final-pdf-qa/page-1.png](<../northstar-exports-week-20261109/visual-final-pdf-qa/page-1.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-final-pdf-qa/page-2.png](<../northstar-exports-week-20261109/visual-final-pdf-qa/page-2.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-final-pdf-qa/page-3.png](<../northstar-exports-week-20261109/visual-final-pdf-qa/page-3.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-final-pdf-qa/page-4.png](<../northstar-exports-week-20261109/visual-final-pdf-qa/page-4.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-final-pdf-qa/page-5.png](<../northstar-exports-week-20261109/visual-final-pdf-qa/page-5.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-final-pdf-qa/page-6.png](<../northstar-exports-week-20261109/visual-final-pdf-qa/page-6.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-final-pdf-qa/page-7.png](<../northstar-exports-week-20261109/visual-final-pdf-qa/page-7.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-final-pdf-qa/page-8.png](<../northstar-exports-week-20261109/visual-final-pdf-qa/page-8.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-pdf-qa/page-1.png](<../northstar-exports-week-20261109/visual-pdf-qa/page-1.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-pdf-qa/page-2.png](<../northstar-exports-week-20261109/visual-pdf-qa/page-2.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-pdf-qa/page-3.png](<../northstar-exports-week-20261109/visual-pdf-qa/page-3.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-pdf-qa/page-4.png](<../northstar-exports-week-20261109/visual-pdf-qa/page-4.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-pdf-qa/page-5.png](<../northstar-exports-week-20261109/visual-pdf-qa/page-5.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-pdf-qa/page-6.png](<../northstar-exports-week-20261109/visual-pdf-qa/page-6.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-pdf-qa/page-7.png](<../northstar-exports-week-20261109/visual-pdf-qa/page-7.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |
| [northstar-exports-week-20261109/visual-pdf-qa/page-8.png](<../northstar-exports-week-20261109/visual-pdf-qa/page-8.png>) | Rasterized PDF page or contact sheet for layout inspection | QA derivative; not planning input |

### Proposed planning data

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/export-example-data.json](<../northstar-exports-week-20261109/export-example-data.json>) | Normalized example/export scope and actual portfolio data | Source mapping evidence, not acceptance or calendar proof |
| [northstar-exports-week-20261109/export-to-northstar-trace.json](<../northstar-exports-week-20261109/export-to-northstar-trace.json>) | Read-back join of generated CSV/XLSX files by native ID | Source mapping evidence, not acceptance or calendar proof |
| [northstar-exports-week-20261109/northstar-weekly-feed.json](<../northstar-exports-week-20261109/northstar-weekly-feed.json>) | Actual non-sample PM records joined with six proposed attention candidates | Dated source facts plus unapproved planning interpretation |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/export-example-data.json](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/export-example-data.json>) | Normalized example/export scope and actual portfolio data | Source mapping evidence, not acceptance or calendar proof |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/export-to-northstar-trace.json](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/export-to-northstar-trace.json>) | Read-back join of generated CSV/XLSX files by native ID | Source mapping evidence, not acceptance or calendar proof |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/northstar-weekly-feed.json](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/northstar-weekly-feed.json>) | Actual non-sample PM records joined with six proposed attention candidates | Dated source facts plus unapproved planning interpretation |
| [northstar-exports-week-20261109/portfolio-visual-plan.json](<../northstar-exports-week-20261109/portfolio-visual-plan.json>) | Illustrative day focus and four-week review windows; proposed workflow edges | Hypothetical dates/order; no resource-feasible commitment |

### Recorded conversation decisions

| File | Purpose | Authority / caveat |
|---|---|---|
| [NORTHSTAR-DECISIONS-AND-2DO-20261106.md](<../NORTHSTAR-DECISIONS-AND-2DO-20261106.md>) | Northstar choices, proposed information ranking and open dependency visualization 2do | Accepted display choices plus separately labelled proposals |

### Rendered previews

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/gallery-desktop.png](<../northstar-exports-week-20261109/gallery-desktop.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/gallery-mobile.png](<../northstar-exports-week-20261109/gallery-mobile.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/northstar-desktop.png](<../northstar-exports-week-20261109/northstar-desktop.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/northstar-mobile.png](<../northstar-exports-week-20261109/northstar-mobile.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/gallery-desktop.png](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/gallery-desktop.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/gallery-mobile.png](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/gallery-mobile.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/northstar-desktop.png](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/northstar-desktop.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/northstar-mobile.png](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/northstar-mobile.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/portfolio-dependencies-checked.png](<../northstar-exports-week-20261109/portfolio-dependencies-checked.png>) | Checked visual preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/portfolio-gantt-preview.png](<../northstar-exports-week-20261109/portfolio-gantt-preview.png>) | Gantt scenario image | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/portfolio-visual-dependencies.png](<../northstar-exports-week-20261109/portfolio-visual-dependencies.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/portfolio-visual-gantt-view.png](<../northstar-exports-week-20261109/portfolio-visual-gantt-view.png>) | Gantt scenario image | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/portfolio-visual-mobile.png](<../northstar-exports-week-20261109/portfolio-visual-mobile.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/portfolio-visual-overview.png](<../northstar-exports-week-20261109/portfolio-visual-overview.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/portfolio-visual-report-contact.png](<../northstar-exports-week-20261109/portfolio-visual-report-contact.png>) | PDF contact sheet | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-exports-week-20261109/portfolio-week-checked.png](<../northstar-exports-week-20261109/portfolio-week-checked.png>) | Checked visual preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-mock/northstar-stress-desktop.png](<../northstar-mock/northstar-stress-desktop.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-mock/northstar-stress-detail.png](<../northstar-mock/northstar-stress-detail.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |
| [northstar-mock/northstar-stress-mobile.png](<../northstar-mock/northstar-stress-mobile.png>) | Browser/layout preview | Viewing/QA aid; underlying source and assumptions still govern |

### Research notes and local READMEs

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/README.md](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/README.md>) | Findings, assumptions, boundaries and links for an experiment | Research/reference; not the governing runtime specification |
| [northstar-exports-week-20261109/portfolio-visual-notes.md](<../northstar-exports-week-20261109/portfolio-visual-notes.md>) | Findings, assumptions, boundaries and links for an experiment | Research/reference; not the governing runtime specification |
| [northstar-exports-week-20261109/README.md](<../northstar-exports-week-20261109/README.md>) | Findings, assumptions, boundaries and links for an experiment | Research/reference; not the governing runtime specification |
| [northstar-mock/README.md](<../northstar-mock/README.md>) | Findings, assumptions, boundaries and links for an experiment | Research/reference; not the governing runtime specification |

### Source snapshots and checks

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/live-snapshot.json](<../northstar-exports-week-20261109/live-snapshot.json>) | Dated all-status OpenProject API snapshot | PM observation at retrieval; not current implementation proof |
| [northstar-exports-week-20261109/native-export-status.json](<../northstar-exports-week-20261109/native-export-status.json>) | HTTP receipts for native export routes under the available API credential | Dated read receipts; native-export failures do not prove browser export unavailable |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/live-snapshot.json](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/live-snapshot.json>) | Dated all-status OpenProject API snapshot | PM observation at retrieval; not current implementation proof |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/native-export-status.json](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/native-export-status.json>) | HTTP receipts for native export routes under the available API credential | Dated read receipts; native-export failures do not prove browser export unavailable |
| [northstar-mock/endpoint-checks-20261106.json](<../northstar-mock/endpoint-checks-20261106.json>) | Direct reads resolving initially missing relation endpoints | Dated read receipts; native-export failures do not prove browser export unavailable |
| [northstar-mock/openproject-all-statuses-20261106.json](<../northstar-mock/openproject-all-statuses-20261106.json>) | Dated all-status OpenProject API snapshot | PM observation at retrieval; not current implementation proof |
| [northstar-mock/openproject-snapshot-20261106.json](<../northstar-mock/openproject-snapshot-20261106.json>) | Initial default-status discovery snapshot; incomplete for closed prerequisites | Dated discovery evidence only |

### Verification and refinement receipts

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/verification-browser.json](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/verification-browser.json>) | Machine/file/layout or exact-match refinement receipt | Technical evidence only; not requirement or operator acceptance |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/verification-files.json](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/verification-files.json>) | Machine/file/layout or exact-match refinement receipt | Technical evidence only; not requirement or operator acceptance |
| [northstar-exports-week-20261109/portfolio-visual-final-check.json](<../northstar-exports-week-20261109/portfolio-visual-final-check.json>) | Machine/file/layout or exact-match refinement receipt | Technical evidence only; not requirement or operator acceptance |
| [northstar-exports-week-20261109/portfolio-visual-refinement.json](<../northstar-exports-week-20261109/portfolio-visual-refinement.json>) | Machine/file/layout or exact-match refinement receipt | Technical evidence only; not requirement or operator acceptance |
| [northstar-exports-week-20261109/portfolio-visual-verification.json](<../northstar-exports-week-20261109/portfolio-visual-verification.json>) | Machine/file/layout or exact-match refinement receipt | Technical evidence only; not requirement or operator acceptance |
| [northstar-exports-week-20261109/verification-browser.json](<../northstar-exports-week-20261109/verification-browser.json>) | Machine/file/layout or exact-match refinement receipt | Technical evidence only; not requirement or operator acceptance |
| [northstar-exports-week-20261109/verification-files.json](<../northstar-exports-week-20261109/verification-files.json>) | Machine/file/layout or exact-match refinement receipt | Technical evidence only; not requirement or operator acceptance |
| [northstar-mock/northstar-stress-verification.json](<../northstar-mock/northstar-stress-verification.json>) | Machine/file/layout or exact-match refinement receipt | Technical evidence only; not requirement or operator acceptance |

### Visual planning experiments

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-exports-week-20261109/dependency-core.svg](<../northstar-exports-week-20261109/dependency-core.svg>) | Native/proposed dependency illustration; inspect legend | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/dependency-identity.svg](<../northstar-exports-week-20261109/dependency-identity.svg>) | Native/proposed dependency illustration; inspect legend | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/dependency-ipos.svg](<../northstar-exports-week-20261109/dependency-ipos.svg>) | Native/proposed dependency illustration; inspect legend | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/dependency-rhythm.svg](<../northstar-exports-week-20261109/dependency-rhythm.svg>) | Native/proposed dependency illustration; inspect legend | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/dependency-runtime.svg](<../northstar-exports-week-20261109/dependency-runtime.svg>) | Native/proposed dependency illustration; inspect legend | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/dependency-taxonomy.svg](<../northstar-exports-week-20261109/dependency-taxonomy.svg>) | Native/proposed dependency illustration; inspect legend | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/dependency-waves.svg](<../northstar-exports-week-20261109/dependency-waves.svg>) | Native/proposed dependency illustration; inspect legend | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/dependency-website.svg](<../northstar-exports-week-20261109/dependency-website.svg>) | Native/proposed dependency illustration; inspect legend | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/index.html](<../northstar-exports-week-20261109/index.html>) | Export gallery with link to visual dashboard | Prototype, not approved layered weekly workflow |
| [northstar-exports-week-20261109/northstar-next-week.html](<../northstar-exports-week-20261109/northstar-next-week.html>) | Weekly priorities/project-detail example | Prototype, not approved layered weekly workflow |
| [northstar-exports-week-20261109/northstar-portfolio-print.html](<../northstar-exports-week-20261109/northstar-portfolio-print.html>) | Print-layout source | Prototype, not approved layered weekly workflow |
| [northstar-exports-week-20261109/northstar-portfolio-visual.html](<../northstar-exports-week-20261109/northstar-portfolio-visual.html>) | Whole-portfolio visual prototype; project task source list remains flat | Prototype, not approved layered weekly workflow |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/index.html](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/index.html>) | Export gallery with link to visual dashboard | Prototype, not approved layered weekly workflow |
| [northstar-exports-week-20261109/openproject-outputs-and-northstar/northstar-next-week.html](<../northstar-exports-week-20261109/openproject-outputs-and-northstar/northstar-next-week.html>) | Weekly priorities/project-detail example | Prototype, not approved layered weekly workflow |
| [northstar-exports-week-20261109/portfolio-gantt-a.svg](<../northstar-exports-week-20261109/portfolio-gantt-a.svg>) | Four-week Gantt scenario | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/portfolio-gantt-b.svg](<../northstar-exports-week-20261109/portfolio-gantt-b.svg>) | Four-week Gantt scenario | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/portfolio-gantt.svg](<../northstar-exports-week-20261109/portfolio-gantt.svg>) | Four-week Gantt scenario | Reference visual; dates/proposed edges remain assumptions |
| [northstar-exports-week-20261109/portfolio-status.svg](<../northstar-exports-week-20261109/portfolio-status.svg>) | Native state-count chart | Reference visual; dates/proposed edges remain assumptions |

### Workspace diagnostic previews

| File | Purpose | Authority / caveat |
|---|---|---|
| [northstar-portfolio-final.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/northstar-portfolio-final.png>) | Browser capture / layout diagnostic | Diagnostic only; not acceptance proof |
| [northstar-portfolio-mobile-verified.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/northstar-portfolio-mobile-verified.png>) | Browser capture / layout diagnostic | Diagnostic only; not acceptance proof |
| [northstar-portfolio-mobile.png](<C:/Users/gehma/Documents/Codex/2026-11-06/recently-in-the-apex-ai-os/northstar-portfolio-mobile.png>) | Browser capture / layout diagnostic | Diagnostic only; not acceptance proof |

## Failure guards

- [P0 | I99] Do not infer current source freshness or operator acceptance from a linked filename.
- [P0 | I98] Do not rerun render helpers without reconciling manual output refinements and the restored specification scope.
- [P0 | I97] Keep individual project planning and resource planning as the next design phase; this inventory implements neither.
