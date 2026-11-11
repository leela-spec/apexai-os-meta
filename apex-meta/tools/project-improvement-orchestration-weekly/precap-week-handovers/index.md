---
okf_version: "0.2"
title: "Precap Week Governance & Canonical Owner Redirect Index"
description: "Governance handover hub retaining 00-RULE-CANONICAL-DECISION-LOCK.md while Steps 01-07 landed into single canonical owners post-baseline ad10c483."
status: current
date: 2026-11-11
tags: [weekly-orchestration, precap-week, handovers, index, single-owner]
---

# Precap Week Handovers & Single-Owner Map (`2026-11-11`)

Steps `01` through `07` have been executed, verified, and consolidated into single-owner canonical files, with redundant handover copies removed post-baseline (`ad10c483`).
Do **not** author duplicate rule copies here; update the single canonical owner listed below.

| Concern | Single Canonical Owner |
|---|---|
| **Governance Lock (`Step 0`, parallel scope)** | [00-RULE-CANONICAL-DECISION-LOCK.md](00-RULE-CANONICAL-DECISION-LOCK.md) |
| **Precap Week UX Spec (`00..05`, `EM-13`, `OP`, `<920px`)** | [SPEC-PRECAP-WEEK-ITERATIONS.okf.md](../01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md) |
| **Machine Schemas & Deterministic Compiler** | [render_precap_cockpit.py](../01-weekly-command-brief/render_precap_cockpit.py) & [operator-weekly-command-brief.schema.json](../01-weekly-command-brief/schemas/operator-weekly-command-brief.schema.json) |
| **Weekly Clock & Dispersal Engine (`T1/T2`)** | [week-blueprint.json](../02-weekly-dispersal/week-blueprint.json) & [SPEC-WEEKLY-DISPERSAL.okf.md](../02-weekly-dispersal/SPEC-WEEKLY-DISPERSAL.okf.md) |
| **Runtime Skill Entrypoint (`PrecapWeek`)** | [SKILL.md](../../../../.claude/skills/PrecapWeek/SKILL.md) |
| **GCal Flow Writer (`PrecapNextDay` only)** | [HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md](../02-next-day-brief/HANDOVER-GOOGLE-CALENDAR-FLOW-EVENTS.md) |
