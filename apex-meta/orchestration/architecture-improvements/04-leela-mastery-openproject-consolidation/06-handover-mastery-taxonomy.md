---
type: Handover
title: Mastery of Arts — sub-project taxonomy (design live, then build under the root)
description: Design the Mastery-of-Arts sub-project structure WITH the operator (not unilaterally), then create the agreed sub-projects under the existing "Leela & Mastery" root in OpenProject.
tags: [handover, openproject, mastery-of-arts, taxonomy, sub-projects]
status: ready
generated: { by: "claude/opus-4.8", at: "2026-09-27" }
implementation_authority: operator-gated
---

# Handover: Mastery of Arts sub-project taxonomy

## Goal
Fill in the **Mastery** half of "Leela & Mastery" in OpenProject: agree a sub-project taxonomy **together
with the operator** (the initiative handover is explicit that this is NOT to be decided unilaterally), then
create the agreed sub-projects under the root.

## What already exists (verified 2026-09-27)
- Root project **`Leela & Mastery`** exists — **project id 4**, identifier `leela-mastery`.
- **`Leela`** (project id 3) is already a sub-project under it (renamed from "Leela Cloud 2026",
  re-parented) and holds the full imported Leela plan (83 WPs).
- So the root currently has exactly one child (Leela). Mastery sub-projects are what's missing.
- The skill can create projects: `project.create` (convenience `--name`/`--identifier`/`--description`
  or `--data`) and re-parent via `project.update --id <id> --data '{"_links":{"parent":{"href":"/api/v3/projects/4"}}}'`.
  Both are gated writes (`--confirmed` after operator OK). Run the skill from inside WSL via the installed
  Node: `wsl -d Ubuntu -- /home/gehma/nodejs/bin/node <repo>/.agents/skills/openproject/client/opCall.js …`
  with `op.env` sourced. (See `[[leela-openproject-instance-access]]` and `02-preflight-and-transport-diagnosis.md`.)

## Orientation basis (from the initiative 00-handover — DO NOT auto-assign)
Use the real `C:\GitDev\MasterOfArts` top-level folders as the conversation's orientation, not a from-scratch
invention. Verified listing (2026-09-26), infra/meta excluded:
```
ACIM            Art             AIHowTo (meta — likely excluded)
Awakening       Business        Cacao Cocoa
Coaching        Content Creation  Dance Fusion
Geopolitcs      Health          IPOS
KIdsCamp26      Legal           LHTL
Lika (EXCLUDED this round)      Meditation
Misc            Neijia New      OpenClaw / OpenClaw_Setup
Podcast         Science         Sexism
Sham            SuperHeroKids   WEbsite
workshops       Orchestration (meta — likely excluded)
```

## The live design session — questions to raise with the operator
1. Which of these are **active verticals** vs **dormant/archival** and shouldn't be PM sub-projects at all
   (`Misc`, `Sham`, `Sexism` look like non-projects in the PM sense)?
2. Which should **merge** (e.g. is `OpenClaw` / `OpenClaw_Setup` one sub-project or two)?
3. Do `AIHowTo` and `Orchestration` belong in the PM hierarchy, or are they purely meta/tooling?
4. Naming/grouping: flat list under root, or an intermediate grouping (e.g. "Content", "Wellness")?
5. Confirm **Lika stays excluded** this round (initiative decision #2 — do not add without the operator
   re-opening it). `acim-secular` (an Astro site) is a **separate repo**, distinct from the raw ACIM
   content in `MasterOfArts\ACIM\` — don't conflate.
6. For each accepted sub-project: is it just a container for now, or does the operator want any initial
   epics/work seeded (probably not — keep this round to the container hierarchy)?

## Build steps (after the operator approves the list as one plan)
1. Present the agreed sub-project list back as a single structural plan (per the safety boundary: a batch
   of sub-project creates is a structural decision the operator approves as a whole, not one confirm-prompt
   at a time).
2. For each: `project.create --data '{"name":"<Name>","identifier":"<slug>","_links":{"parent":{"href":"/api/v3/projects/4"}}}' --confirmed`
   (parent set at create, so no re-parent step needed). Verify each with `project.get`.
3. Read back `project.list` and confirm the root (id 4) now has Leela + the agreed Mastery sub-projects.

## Safety
- Do NOT invent the taxonomy; design it live. Do NOT add Lika. Do NOT touch `C:\GitDev\MasterOfArts`
  repo files — this is OpenProject structure only.
- Structural bulk-create → operator approves the whole list first.
- Every create through the skill's preview → `--confirmed` → reread gate.

## Definition of done
The operator-approved Mastery sub-projects exist under `Leela & Mastery` (id 4), verified by `project.list`,
with Lika excluded and meta/tooling folders handled per the operator's decision.
