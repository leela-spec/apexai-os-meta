---
type: Design Brief
title: <Screen/Component Name> — Claude Design Brief
description: One-sentence summary of what is being designed and why.
resource: lib/features/<feature>/<file>.dart
tags: [leela, flutter, ui, claude-design]
sources:
  - id: <short-id>
    resource: <path relative to repo root>
  # one entry per file this brief cites below — see "Grounding and handoff mechanics"
---

# Grounding and handoff mechanics (read first — this governs the whole brief)

A Claude Design chat has **no live access to this repository**, connector or no connector. It only
ever sees what gets pasted or uploaded into that specific conversation. There is no background
"connected repository" it can browse on its own, even when a GitHub integration shows as
"Connected" — confirmed failure mode, not a hypothetical. Treat every claim in this brief as
something that must physically travel into the Design chat as text/files, or it does not exist from
Design's point of view.

This changes two things about how this template is used:

1. **Verify every `sources:` entry resolves to a real file before marking this brief usable.** A
   brief that cites a file which does not exist on disk will not fail loudly in Design — Design will
   either invent plausible content to fill the gap (the exact hallucination risk this process exists
   to prevent) or silently ignore the citation. Check with a real file read/listing, not from memory
   of a prior audit, manifest, or an earlier version of this brief.
2. **Package the verified sources into one bundle file before handoff**, rather than attaching files
   one by one through a chat "+" picker or a GitHub connector. The reliable method found in practice:
   run `npx repomix --include "<comma-separated paths from sources:>" --style markdown --output
   <bundle>.md` from the repo root. This produces a single file containing the literal contents of
   every listed source, with a token count and a secret-leak scan reported up front. Re-run it any
   time a source file changes — there is nothing to "sync."
3. **Handoff is manual, not a connection.** Open a **new** Claude Design chat (session memory and
   brand context do not carry over from a previous one), then paste this brief's body and the
   generated bundle's contents directly into that conversation (or upload the bundle file as an
   attachment) before sending the opening prompt. "Sending" or "uploading" a file to Claude Design
   always means this manual step — there is no separate automated transport.

# Context (read-only — do not implement, only reference)

- App: Leela (Flutter habit/gamification app), Dart/Flutter, not web.
- Design system already in use (do not invent new colors/fonts — reuse these):
  - Background: <#hex>
  - Primary accent: <#hex>
  - Secondary accent: <#hex>
  - Font family: <name>
  - Corner radius / spacing scale: <values>
- Reference screenshot(s) and the generated source bundle (see "Grounding and handoff mechanics")
  describe current visual language — match it, don't redesign it, unless explicitly asked.

# Task (what Claude Design should actually do)

- Screen/component: <name, e.g. "Rhythm Week Workstation — day analysis row">
- Goal: <what problem this screen solves for the user>
- Must include (content/data, from real app state — do not invent fields):
  - <field 1>
  - <field 2>
- Must NOT include / out of scope:
  - No backend logic, no state management, no data fetching
  - No new color palette, no new typography
  - No Flutter/Dart code — HTML/CSS/JS prototype only, used as a visual reference
- Interactions to demonstrate: <e.g. hover states, tab switching, drag>

# Constraints (explicit rules, not preferences)

- Output format: interactive HTML/CSS/JS prototype (Claude Design's native output).
- Do not attempt to produce Dart, Flutter widgets, or pubspec changes — Design cannot run or validate that; it will be re-implemented manually afterward.
- Keep component boundaries matching Flutter widget boundaries described above, so re-implementation maps 1:1.
- Flag anything ambiguous instead of guessing.

# Handback (what comes back into this repo)

- Resulting prototype link/screenshot → re-implemented in: <target .dart file path>
- Record the decision in `docs/data-architecture/STATE.md` per this repo's save-step discipline once implemented.

# Minimal checklist before this brief is usable

- [ ] Every `sources:` entry verified against a real file on disk (not recalled from memory/a prior brief)
- [ ] `npx repomix` run against those exact paths; bundle file generated and its security scan passed
- [ ] Bundle token count checked against a reasonable chat budget before pasting
- [ ] Brief body + bundle pasted/uploaded into one fresh Claude Design chat together, before the opening prompt is sent
