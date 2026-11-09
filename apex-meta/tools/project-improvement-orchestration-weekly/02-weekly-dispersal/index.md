---
okf_version: "0.2"
title: Weekly Dispersal Bundle
description: The weekly dispersal slice — the governed specification, the generated slot inventory, the working assumptions register, and the Precap Week integration analysis.
status: current
date: 2026-11-09
tags: [sequencing, dispersal, weekly-orchestration, precap-week, slot-inventory, quota]
---
<!-- MIRROR. Source of truth: MasterOfArts/Sequencing/dispersal/ (DD-15).
     Edits here are overwritten by sync_dispersal.py. -->
# Weekly Dispersal Bundle

> **Zone:** `MasterOfArts/Sequencing/dispersal/`, mirrored read-only into
> `apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/02-weekly-dispersal/`.
> `MasterOfArts` is the single source of truth; the mirror is a one-way copy (`DD-15`).

The mechanism that decides which Mental, Physical, Craft and Regeneration content occupies which slot
of which day, and how that reaches Precap Week Matrix 2.

## Files

| File | Type | Description |
|---|---|---|
| [`SPEC-WEEKLY-DISPERSAL.okf.md`](SPEC-WEEKLY-DISPERSAL.okf.md) | **Specification** | Canonical contract: Flow composition, the three day regimes, the slot inventory, the XP/TP/BP point model, the share mechanism, the binding notation, the full decision ledger, and the failure guards. `WD-01`..`WD-48`. |
| [`slot-inventory.json`](slot-inventory.json) | Generated Data | 24 Flows, 240 slot occurrences with stable addresses, the regime map, and the resolved Mental and Physical quotas. |
| [`build_slot_inventory.py`](build_slot_inventory.py) | Generator | Produces the inventory from the Flow contract so the two cannot drift. Rejects any Flow duration but 120 minutes. |
| [`ASSUMPTIONS-AND-DECISIONS-REGISTER.md`](ASSUMPTIONS-AND-DECISIONS-REGISTER.md) | Reference | Working record: operator inputs `OD-01`..`OD-44`, assumptions `A-01`..`A-14`, conflicts `X-01`..`X-06` with evidence, and the applied Monday-Sunday amendment. |
| [`PRECAP-INTEGRATION-ANALYSIS.md`](PRECAP-INTEGRATION-ANALYSIS.md) | Reference | The collision with Precap Week v2.0 and Handovers 03-06: the point-construct reconciliation, the day geometry, and the stale weekend text. |
| [`render_blueprint.py`](render_blueprint.py) | Renderer | Generates the operator-facing week page from `slot-inventory.json`, so the page cannot disagree with the contract (`WD-36b`). |
| [`week-blueprint.html`](week-blueprint.html) | Generated View | The human-readable week: the three regimes as clock-ordered timelines with gaps shown, the Flow grid, and both share tables. Regenerate; never edit. |
| [`sync_dispersal.py`](sync_dispersal.py) | Tool | One-way mirror of this bundle into `apexai-os-meta`. Refuses to run in reverse. |

## Status

The specification carries `status: operator_review_pending`. The three blockers are closed: the
operator declared the weekday re-cut (`DD-32`), the project night at `20:00-21:30` (`DD-33`) and
**Knee** at 15% (`DD-34`, now 11 slots a week). The weekday geometry is read from the operator's
own calendar and the declared shares sit on the 5% ladder (`DD-35`). Ten decisions remain open
(`SPEC-WEEKLY-DISPERSAL.okf.md` §7.2).

**One of them blocks the allocator.** `DD-40`: the physical focus block counts toward the quota
(`DD-38`), and its pre-bound 90-minute blocks already exceed the declared shares for Martial Arts
and Dance, leaving the other three Epics owed more minutes than the Flows contain. Either the shares
move or the block stops counting.

Next in the product, not yet built: the slot-filling algorithm, the Epic database, and
`week-demand.json`. Until the allocator exists the inventory describes capacity only, so no
dispersion or spaced-repetition view can be generated.

## Related

- Precap Week specification: `apexai-os-meta/apex-meta/tools/project-improvement-orchestration-weekly/01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`
- Sequencing decisions: [`../decisions.md`](../decisions.md) — open choice `N05`
- Operator blueprint page: <https://claude.ai/artifact/4QEZffC7rxdqwKxVC9hcax>
