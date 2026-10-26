---
okf_version: "0.2"
type: future-development
title: Make Feature/Epic/User story/Bug active-by-default for new OpenProject projects
description: Mitigated via DB state patch (2026-10-08) using WorkPackageTypes::MakeDefaultService. All 7 existing work-package types now have is_default=true for newly created projects, though the upstream OpenProject 17.8.0 Admin UI toggle remains hidden behind the inactive type_variants feature flag.
tags: [openproject, types, admin, mitigated, future-development]
status: mitigated
decided: 2026-10-08
program_ref: none — DB state patched for all 7 types; upstream 17.8.0 UI regression remains for future custom types
---

# Make 4 types default for future projects (DB STATE PATCHED 2026-10-08; Upstream UI Defect Remains in 17.8.0)

## Mitigation & Live DB State (2026-10-08)

All 7 globally-defined work-package types — **Task, Milestone, Summary task, Feature, Epic, User story, Bug** — now have `is_default: true` ("Active in new projects") in `leela-op178-openproject` as well as being enabled across all existing projects. *(Note: the upstream OpenProject 17.8.0 Admin UI regression remains in the image; if a new 8th custom type is created in the future, run the `MakeDefaultService` rails runner command below plus a `memcached` TCP flush.)*

### Root Cause (Verified in OpenProject 17.8.0 Source)
- **Not an Enterprise edition limitation.** During OpenProject 17.8's `type_variants` refactoring, `check_box(name: :is_default)` was removed from `/app/app/forms/work_package_types/details_form.rb` and replaced with `make_default` / `remove_default` menu actions in `/app/app/components/work_package_types/types/type_actions_component.rb`.
- However, `/app/app/views/work_package_types/types/index.html.erb` only renders `GroupedListComponent` (which includes `TypeActionsComponent`) when `OpenProject::FeatureDecisions.type_variants_active?` is `true` (default `false`). When `false`, it renders the legacy `TableComponent` (`/app/app/components/work_package_types/types/row_component.rb`), which outputs a static `checked_image model.is_default` checkmark and omits the action menu.
- Meanwhile, `PATCH /api/v3/projects/{id}` with `_links.types` is a no-op because `/app/lib/api/v3/projects/project_representer.rb` defines `link :types` strictly as a read-only HAL navigation link.

### Fix Applied
`WorkPackageTypes::MakeDefaultService` (`/app/app/services/work_package_types/make_default_service.rb`) is not gated by the `type_variants` feature flag. Executed via `rails runner`:
```bash
wsl -d Ubuntu -u root -- docker exec leela-op178-openproject bundle exec rails runner '
  Type.where(name: ["Feature", "Epic", "User story", "Bug"]).find_each do |t|
    WorkPackageTypes::MakeDefaultService.new(type: t, user: User.system).call
  end
'
```
Followed by an in-container `memcached` TCP flush (`printf 'flush_all\r\n' | timeout 2 bash -c 'cat > /dev/tcp/127.0.0.1/11211'`).

## Related
- `apex-meta/orchestration/architecture-improvements/05-program-closeout/FINDINGS-openproject-memory-and-178-inefficiencies-2026-10-08.md` — full source-level analysis.
- [RUNBOOK-openproject-17.8-operations.md](RUNBOOK-openproject-17.8-operations.md) §3.2.
- [README.md](README.md) — this folder's index.
