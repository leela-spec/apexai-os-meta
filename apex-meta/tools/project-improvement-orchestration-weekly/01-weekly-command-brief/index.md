---
okf_version: "0.2"
title: Module 01 — Precap Week Cockpit & Weekly Command Brief Bundle
description: Single-owner specification, JSON schemas, deterministic multi-surface compiler, and compiled W45/W46 cockpit fixtures (v2.1).
status: current
date: 2026-11-11
tags: [weekly-orchestration, precap-week, module-01, cockpit, index]
---

# Module 01 — Precap Week Cockpit & Weekly Command Brief Bundle

This bundle holds the **one authoritative home** for each Precap Week concern: UI/domain specification, JSON schemas, compiler, HTML cockpit, and fixtures (see [`../DECISIONS.md#d021`](../DECISIONS.md) for consolidation provenance).

## Canonical Bundle Structure

| File | Role | Description |
|---|---|---|
| [`SPEC-PRECAP-WEEK-MASTER.okf.md`](SPEC-PRECAP-WEEK-MASTER.okf.md) | **Master Specification** | Master PrecapWeek architecture specification governing 6-Portfolio standard, Section 00/01, lifecycle, and capacity math. |
| [`SPEC-MATRIX-1-PORTFOLIOS.okf.md`](SPEC-MATRIX-1-PORTFOLIOS.okf.md) | **Modular Specification** | Dedicated non-temporal portfolio specification governing goals, L1/L2 layout, and unified EM-13 `G\|I\|P\|S\|O\|C` drawers. |
| [`SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md`](SPEC-MATRIX-2-TEMPORAL-TIMETABLE.okf.md) | **Modular Specification** | Dedicated temporal timetable specification governing Monday–Sunday schedule, blueprint clock, and Personal Focus Strip. |
| [`SPEC-PRECAP-INTERFACES-HANDOFF.okf.md`](SPEC-PRECAP-INTERFACES-HANDOFF.okf.md) | **Modular Specification** | Dedicated interfaces specification governing machine schemas, Section 04 Residuals, and PrecapNextDay handoff. |
| [`render_precap_cockpit.py`](render_precap_cockpit.py) | **Compiler & Validator** | Validating Python compiler (`stdlib`-only) emitting the `v0.5` HTML Cockpit, OKF v0.2 Brief (`D1–D12`), and handoff JSON from `schemas/` + `02-weekly-dispersal/`. |
| [`schemas/operator-weekly-command-brief.schema.json`](schemas/operator-weekly-command-brief.schema.json) | **Schema (Stage 1A)** | Draft 2020-12 schema for lightweight Stage 1A Operator Weekly Command Brief intake. |
| [`schemas/precap-week-cockpit.schema.json`](schemas/precap-week-cockpit.schema.json) | **Schema (Stage 1B)** | Draft 2020-12 schema for compiled 6-Portfolio Matrix 1/2 Cockpit payloads. |
| [`schemas/presentation-handoff.schema.json`](schemas/presentation-handoff.schema.json) | **Schema (Handoff)** | Draft 2020-12 handshake schema for `PrecapNextDay` (`artifact_type: Weekly_Command_Brief`). |
| [`precap-week-cockpit-2026-W46.html`](precap-week-cockpit-2026-W46.html) | **Compiled Cockpit** | Generated interactive `v0.5` HTML Cockpit (`#s00..#s05`) compiled from live `fixtures/` (`2026-W46`). |
| [`fixtures/index.md`](fixtures/index.md) | **Fixture Sub-Bundle** | Verified W46 reference intake, cockpit JSON, OKF v0.2 brief, and handoff JSON. |
