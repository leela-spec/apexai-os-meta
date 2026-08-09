# ADR-0002: Week origin

Status: ACCEPTED -- the provider billing week (Sunday origin) is
authoritative for all rendered labels. `report.py` must use
`billing_week_start()`; `calendar.week_start()` stays ISO and is not to be
changed.

## Context

`apexcalc.calendar.week_start()` returns the ISO (Monday) week start.
`apexcalc.calendar.billing_week_start()` returns the Sunday-origin start the
provider's billing system actually uses.

## Decision

Rendered week labels use the billing (Sunday) origin via
`billing_week_start()`. Internal ISO-week bookkeeping in `calendar.py` is
unaffected.
