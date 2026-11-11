# OKF v0.2 Weekly Command Brief Output Template

Generated deterministically by [`render_precap_cockpit.py`](../../../apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/render_precap_cockpit.py) alongside the interactive `v0.5` HTML Cockpit (`D1–D12` compliance, zero duplicated spec rules).
Reference compiled output: [`w46-reference-weekly-command-brief.okf.md`](../../../apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/fixtures/w46-reference-weekly-command-brief.okf.md).

## Envelope & Frontmatter Modes

- **Standalone OKF v0.2 Report (Default):** Starts with flat OKF frontmatter (`type: Report`, `id: PRECAP-WEEK-BRIEF-{{WEEK_ID}}`, `title`, `description`, `status: draft | current`, `date`, `tags: [weekly-orchestration, precap-week, command-brief, okf-v02]`) so `okf_validator.py` passes cleanly.
- **Orchestrator `weekly_plan_packet` Wrapper (`weekly-orchestrator` runs only):** Prepend `handoff_envelope` per [`handoff-schema.md`](../weekly-orchestrator/references/handoff-schema.md) (`packet_type: weekly_plan_packet`, `gate: G1`, `accountability: meta_strategy`, `target_surface: none`, `expected_action`, `stop_condition`, populated `sources` & `uncertainties`) ahead of the OKF body.

## Required Structure (`D1` Decision Before Detail, `D2` First-10s Header)

```markdown
# Weekly Command Brief — {{WEEK_ID}} ({{ISO_DATE_SPAN}})

> **Result state:** `{{READY | READY_WITH_REVIEW | PARTIAL | BLOCKED}}` · **G1 gate:** `{{PROPOSED | APPROVED | EDITED}}`  
> **Direction:** {{HEADLINE_PORTFOLIO_OUTCOME_FRAMING}}  
> **Next action:** `{{APPROVE_WEEK | EDIT_PRIORITIES | REDUCE_SCOPE | RESOLVE_CONSTRAINT | REJECT_DIRECTION}}`  
> **Review needed:** {{HIGHEST_IMPACT_G1_FLAG_OR_NONE}}  
> **Interactive Cockpit (`v0.5`):** [{{HTML_COCKPIT_FILENAME}}]({{HTML_COCKPIT_RELPATH}})

## 00 · Portfolio Compass (`T1 / T2` Grounded)
5-row summary table hydrated from `slot-inventory.json`, `week-blueprint.json`, `week-allocation.json`, and 6-Portfolio `L1/L2` counts with `[src: <TAG>]` citations.

## 01 · Operator Decisions (`New` & `Ongoing` · `G1`)
Conscious trade-offs framed with `meta-strategy-doctrine.md` options where material:
- `New` items with `[P0-P3 | I/E/R]`, gate status (`PROPOSED_FOR_G1 | APPROVED | CONFIRMED_INPUT`), and verified `{sysDef -> opChoice}` overrides only.
- `Ongoing` standing ignores/events; refer to `02-weekly-dispersal/week-blueprint.json` for `Standard` clock defaults.

## 02 · Matrix 1 Overview (`6 Portfolio Areas`)
Compact 6-row table (`Leela`, `IPOS`, `Master of Arts`, `Apex AI`, `Mindful Bar`, `Residual`) listing `L1` priority titles (`WP` ref, `⚡`), `L2` nice-to-haves, and `Cross-Repo` edges; full `G|I|P|S|O|C` + `Tasks -> Subtasks` open in the HTML Cockpit.

## 03 · Matrix 2 Calendar Collisions & Personal Focus
Table of reconciled external meetings (`policy`, `capacity_delta_min`) + 3 personal focus lines (`Mental`, `Physical`, `Regeneration`); full `Mon–Sun` hourly timetable lives in HTML Cockpit Section `03`.

## 04 · Residual Information & 1-Hop Provenance
Deferred backlog table (`Longlist`), `[TAG]` -> source -> freshness (`CURRENT / AGED / STALE / UNKNOWN`) 1-hop ledger, `Confidence`, and `Assumptions`.

## 05 · Sequencing Orientation (`T2` Allocation)
Projected `TP / XP / BP` (`DD-16`: zero BP cutoff; `R XP = 0`) and Gaussian coupling summary (`σ = 6.0h` around `19:00`).

## Compact Downstream Handoff (`PrecapWeek -> PrecapNextDay`)
Single YAML `presentation_handoff` block strictly validating against `schemas/presentation-handoff.schema.json` (`PRECAP-WEEK-HANDOFF-v2.1`).
```

## Authority Boundaries

- Cockpit rules & `G|I|P|S|O|C`: [`SPEC-PRECAP-WEEK-ITERATIONS.okf.md`](../../../apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md)
- Machine Handoff Contract: [`presentation-handoff.schema.json`](../../../apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/schemas/presentation-handoff.schema.json)
- Option Framing Doctrine: [`meta-strategy-doctrine.md`](../weekly-orchestrator/references/roles/meta-strategy-doctrine.md)
