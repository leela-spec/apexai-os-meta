---
okf_version: "0.2"
type: future-development
title: Make Feature/Epic/User story/Bug active-by-default for new OpenProject projects
description: All 7 work-package types are now enabled on every existing project, but 4 of them do not carry forward to projects created in the future. Three fix attempts failed; this records what's confirmed, what's untried, and concrete next steps for whoever picks it up.
tags: [openproject, types, admin, deferred, future-development]
status: deferred
decided: 2026-10-03
program_ref: none — operational gap, not tied to a program task
---

# Make 4 types default for future projects

## Current state (done, verified)

All 7 globally-defined work-package types — Task, Milestone, Summary task, Feature, Epic, User
story, Bug — are enabled on all 8 **existing** projects (Demo project, Scrum project, Leela,
PM Infrastructure, Leela & Mastery, MoA-Content, MoA-Business, ApexAI-OS). Done via each type's
own **Projects** tab (`Administration → Work packages → Types → <type> → Projects` → "Enable for
all projects" toggle), operator-driven in the live UI on 2026-10-03.

## The actual gap

The Types list (`Administration → Work packages → Types`) has an **"Active in new projects"**
column. It is checked for Task, Milestone, Summary task only. Enabling a type for all *existing*
projects (above) does **not** change this column — it stayed unchecked for Feature/Epic/User
story/Bug even immediately after using "Enable for all projects" on User story. So any project
created from today onward will **not** automatically get those 4 types; only the 3 core ones.

## What was tried and ruled out (2026-10-03)

1. **API**: `PATCH /api/v3/projects/{id}` with `_links.types` — returns `200 OK` but silently
   changes nothing. Confirmed via `GET /api/v3/projects/schema` (no `types` field exists on the
   Project resource at all), `GET /api/v3/projects/{id}/types` (read-only, no update/form link),
   `GET /api/v3/types/schema` (404). **No API path exists for this on OpenProject 17.8.0.**
   Full detail: `C:\GitDev\agent-skills\research\LEARNINGS.md` #8.
2. **Type edit tabs** (Details, Defaults, Form configuration, Workflows, Project attributes,
   Projects, Generate PDF) — none of the 7 tabs has a control for "active in new projects".
   Checked live against this instance; not a documentation gap, an actual absence.
3. **Clicking the column directly** in the Types list — not interactive, confirmed by the
   operator live.

## Untried — do these next, in this order

0. **Check the instance's actual license/subscription state first.** The operator raised this
   live (2026-10-03), unverified: this self-hosted Community-edition instance may never have
   activated even the **free Enterprise trial/token** OpenProject offers independent of a paid
   plan. Check `Administration → Enterprise edition` (or `Billing`/similar) for current plan
   status. If no trial/token is active, activating the free one first might resolve this item
   *and* the other Enterprise-gated banners already seen (Defaults tab's "Work Package Subject
   Generation", Form configuration tab's "Edit Attribute Groups") in one step — cheaper to check
   than steps 1–4 below, do this first.
1. **Project templates.** OpenProject supports marking a project as a template
   (`Administration → Projects → <project> → mark as template`, or a toggle in project settings —
   exact location not yet checked on this instance/version). If a template project with all 7
   types pre-enabled can be used as the basis for new-project creation, that achieves the same
   outcome without needing the missing flag at all. **Not yet attempted. Highest-value next step.**
2. **Global/system default settings.** Check `Administration → System settings` (not yet opened
   during this investigation) for a project-defaults section that might govern type defaults
   project-wide, separate from the per-type Types admin page.
3. **OpenProject's own community forum / GitHub issues** (`community.openproject.org`,
   `github.com/opf/openproject`) for "active in new projects" or "default type for new project" —
   this may be a known, documented Community-vs-Enterprise edition split (this instance already
   shows Enterprise upsell banners elsewhere: the Defaults tab's "Work Package Subject Generation"
   and the Form configuration tab's "Edit Attribute Groups" are both gated to paid plans — the
   same could be true here, which would make this a pricing-tier limitation, not a bug to work
   around).
4. **Direct database inspection only — read-only, never write.** If 1–3 come up empty, confirming
   via `isDefault` in the `types` table (read-only `SELECT`, never `UPDATE` — this skill's rules
   forbid writing Postgres directly) would at least settle whether it's a seed-time-only field
   with genuinely no runtime mutation path in this OpenProject version.

## Accepted workaround until this is resolved

Whenever a new project is created: open each of Feature/Epic/User story/Bug's **Projects** tab
and re-run **"Enable for all projects"**. ~30 seconds total. Not automatic, but not a blocker.

## Related
- `C:\GitDev\agent-skills\research\LEARNINGS.md` #8 — the API investigation in full, including the
  exact schema probes run and their results.
- `C:\GitDev\agent-skills\skills\openproject\client\opCall.js` — the `project.update` operation's
  corrected comment, pointing here.
- [README.md](README.md) — this folder's index.
