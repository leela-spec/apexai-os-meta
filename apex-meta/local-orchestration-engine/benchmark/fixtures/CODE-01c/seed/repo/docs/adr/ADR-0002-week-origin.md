# ADR-0002: Week origin

Status: PROPOSED -- unresolved. Two consumers disagree on the week origin;
do not change week_start() without a decision.

## Context

`apexcalc.calendar.week_start()` returns the ISO (Monday) week start.
`apexcalc.rollup`'s own docstring claims weeks begin Sunday, matching the
provider's billing week, but its implementation calls `week_start()`
directly and has never been reconciled with that claim.

## Decision

Not yet made. Do not assume either convention is authoritative.
