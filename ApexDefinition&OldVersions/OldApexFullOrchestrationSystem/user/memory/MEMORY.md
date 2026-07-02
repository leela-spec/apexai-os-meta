# MEMORY.md - Local Memory Index

> Scope: local durable memory index only.
> Main-session surface; may contain personal data.
> Not `SSOT`, not `OpState`, not `Session Export`, and not a project interface.

## What memory is for

- keep durable local context lightweight and drill-down friendly
- hold user-specific preferences, stable reference notes, recurring mistakes, and other local support context
- point to deeper local memory files when a bounded question needs them
- support session startup without loading the whole memory tree

## What memory is not for

- not accepted truth for project control or `SSOT`
- not a substitute for `managed/rules/PROJECT_INTERFACE_CONTRACT.md`
- not a substitute for `managed/rituals/SESSION_EXPORT_PROTOCOL.md`
- not a substitute for `managed/rituals/NIGHT_PLANNING_PROTOCOL.md`
- not a place for placeholder paths, fake references, or formal `OpState` behavior

## Current drill-down map

- `user/memory/context/active.md` — current local active-context snapshot
- `user/memory/MISTAKES.md` — recurring mistake patterns and standing corrections
- `user/memory/memory-daily/YYYY-MM-DD.md` — dated local journals; load only when date-specific detail matters
- other local people, project, or reference notes may be used when they already exist and the bounded task genuinely needs them

## Session loading rule

- load this file in the main session only
- start light: read this index, then drill into `context/active.md` or a dated journal only when needed
- hard cap at session start: max 5 drill-downs
- do not preload the whole local memory tree
- if a memory note claims a path, function, or flag exists, verify it locally before acting on it

## Compatibility notes

- local memory remains lightweight and local even when future project-interface instances exist
- old placeholder entries should be treated as cleanup debt, not as live truth
- detailed local memory may remain segmented, but this index should stay compact and truthful
