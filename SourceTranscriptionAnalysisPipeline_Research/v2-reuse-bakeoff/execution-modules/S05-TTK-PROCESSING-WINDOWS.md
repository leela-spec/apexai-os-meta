# S05 — TTK Processing Windows

**Execute only S05, then stop.**  
**Input:** TTK canonical run from S04  
**Next:** S06

## Outcome

Produce bounded Map packets with exact coverage and explicit `core` versus `context_only` evidence roles. Processing windows are transport units, not semantic chapters.

## Context to load

- this file;
- S04 handoff and `<run>/ttk/` source/state;
- TTK windowing/map-packet code;
- relevant TTK window/coverage tests.

## Recommended tool

Existing TTK windowing. Generic chunkers are not part of the first implementation unless this stage proves a concrete boundary defect.

## Work

1. Ask TTK for current next/status state.
2. Generate/confirm all Map window packets using the current bounded target/min/max settings unless a demonstrated source-specific issue requires a documented adjustment.
3. Preserve context halo but mark it non-citable.
4. Create a compact packet manifest containing ordered packet IDs, packet hashes, core segment ranges, context segment ranges, and approximate word counts.
5. Do not infer chapters or themes here.

## Tests

- every canonical source segment intended for semantic processing appears exactly in required core coverage;
- no source region is accidentally omitted or double-counted as core in a way violating TTK invariants;
- packet hashes are stable for unchanged input/config;
- packet sizes remain within configured bounds except documented edge cases;
- `context_only` segments are distinguishable from core;
- no semantic labels/headings are fabricated by deterministic code.

Run TTK validation/status commands and focused unit tests.

## Outputs

- actual TTK Map packets under the TTK run;
- `<run>/ttk/map-packet-manifest.yaml` or equivalent concise manifest if not already provided;
- S05 handoff.

Handoff must give packet directory, packet count, ordered packet IDs/hashes, window config, and any boundary anomaly S06/S07 should know.

Commit/push only stage fixes/tests if needed. Return handoff and **STOP.**