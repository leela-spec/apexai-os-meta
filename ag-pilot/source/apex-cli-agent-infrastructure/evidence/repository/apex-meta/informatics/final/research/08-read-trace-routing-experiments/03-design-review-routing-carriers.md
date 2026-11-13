---
type: Evidence
id: EVIDENCE-ROUTING-DESIGN-REVIEW-v0.1
title: Where task routing lives in the informatics design and what the Mindful Bar blueprint added
description: Review of the four places that route tasks to files in the informatics design and the Mindful Bar repository, and what the project blueprint added beyond the contract triggers.
status: draft
tags: [design-review, routing, authoring-blueprint, contract-triggers, router, mindful-bar]
---

# Where task routing lives, and what the Mindful Bar blueprint added

## Summary

- The informatics design already routes tasks to files in three places. The Mindful Bar blueprint was a fourth, added locally.
- The blueprint carried one thing the design cannot: the Mindful Bar domain map. Stage 1 showed that stating that map inline in `AGENTS.md` works better than pointing to a router.

## Status

- Facts below were read from files on 2026-11-07. Paths in backticks belong to the Mindful Bar repository.
- No rule, spec or decision changes here.

## Where routing exists

| Carrier | What it routes | Owner |
|---|---|---|
| Seven `when=` and `ref=` triggers in the always-on contract (`<align>`, `<editing>`, `<authoring>`, `<trade_off>`, `<handover>`, `<iterative>`, `<schemas>`) | Task type to one execution-mode or spec file | [apex_contract_v1.0_ultra.xml](../../specs/apex_contract_v1.0_ultra.xml), copied inline into every carrier |
| [general-informatics-router.md](../../specs/general-informatics-router.md) | Conditional dispatch to writing profile, file architecture, execution modes, anti-drift and schemas | Informatics specs. Vendored into Mindful Bar and listed in `systems/apex/README.md`, but neither `AGENTS.md` nor the blueprint points to it |
| `systems/authoring-blueprint.md` | Task type to generic specs and to the Mindful Bar design files | Mindful Bar repository, added in commit `9493aa4` on 2026-11-07 |
| `AGENTS.md` Layer 2 sentence and a README bullet | Pointer to the blueprint | Mindful Bar repository |

## Facts about the blueprint

- It arrived when the APEX copy moved under `systems/`. The meta change record [operations/20](../../operations/20-CHANGE-RECORD-2026-11-06-07.md) item C19 says it "mixed routing, restated lifecycle rules, provenance and guards" and was cut back to a routing table.
- Its generic rows (edit an existing file, handover, decision, iterative work) repeat contract triggers.
- Its Mindful Bar rows (domain map, filing and identity, custody) are the only content the master contract cannot hold, because the contract is a shared block.

## Facts about the contract triggers

- The terminal `<pointers>` rule says to open a reference only when its condition matches and the inline summary is insufficient. Agents that treat the inline summary as enough do not open the ref. That fits the low gate-following counts in stage 1.
- The `<authoring>` ref in the Mindful Bar copy points at `file-architecture.md`, a departure the carrier map allows. It does not name the Mindful Bar domain map.
- Earlier evidence: [RESULTS-01](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md) rated gating efficacy unverified. [operations/17](../../operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md) measured `<handover>` and `<trade_off>` at 0 of 2 each.

## What stage 1 adds

- A pointer to a router was ignored (1 of 24 cells).
- Two sentences in `AGENTS.md` that name the domain map and the filing rules gave correct placement in 12 of 12 cells and made 14 of 24 cells open the map.
- The Mindful Bar-specific routing therefore belongs in the Layer 2 text of `AGENTS.md`, one hop from the agent, not in a separate router file.

## Rule

Keep generic routing in the contract triggers and project-specific routing in the project's `AGENTS.md` Layer 2. Do not add a second router that restates either.
