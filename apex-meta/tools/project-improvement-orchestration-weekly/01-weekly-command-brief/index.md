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
| [`SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](SPEC-PRECAP-WEEK-ITERATIONS.okf.md) | **Specification** | Single canonical UI & domain spec (`00..05`, 6 Portfolios, `EM-13` `G\|I\|P\|S\|O\|C`, OP `## Heading` & epistemology, `<920px` non-`rowspan`, `T1/T2`). |
| [`render_precap_cockpit.py`](render_precap_cockpit.py) | **Compiler & Validator** | Validating Python compiler (`stdlib`-only) emitting the `v0.5` HTML Cockpit, OKF v0.2 Brief (`D1–D12`), and handoff JSON from `schemas/` + `02-weekly-dispersal/`. |
| [`schemas/operator-weekly-command-brief.schema.json`](schemas/operator-weekly-command-brief.schema.json) | **Schema (Stage 1A)** | Draft 2020-12 schema for lightweight Stage 1A Operator Weekly Command Brief intake. |
| [`schemas/precap-week-cockpit.schema.json`](schemas/precap-week-cockpit.schema.json) | **Schema (Stage 1B)** | Draft 2020-12 schema for compiled 6-Portfolio Matrix 1/2 Cockpit payloads. |
| [`schemas/presentation-handoff.schema.json`](schemas/presentation-handoff.schema.json) | **Schema (Handoff)** | Draft 2020-12 handshake schema for `PrecapNextDay` (`artifact_type: Weekly_Command_Brief`). |
| [`precap-week-cockpit-W45-actual-data-v03.html`](precap-week-cockpit-W45-actual-data-v03.html) | **Compiled Cockpit** | Generated interactive `v0.5` HTML Cockpit (`#s00..#s05`) compiled from `fixtures/`. |
| [`fixtures/index.md`](fixtures/index.md) | **Fixture Sub-Bundle** | Verified W46 reference intake, cockpit JSON, OKF v0.2 brief, and handoff JSON. |
