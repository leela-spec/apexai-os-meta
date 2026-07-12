---
title: "Run Record Schema"
purpose: >
  Run identity, attempt numbering, supersession, and resume pointers — formalizing the
  layout US-IDEA-01 established. A run must be resumable from these files alone.
created: 2026-07-12
---

# Run Record Schema

## Run identity

```yaml
run:
  run_id: "<STORY-ID>-<yyyymmdd>"        # also the run folder name under simulations/
  story_id: "US-…-01"
  attempt: 1                              # increments only on full-run restart; failed attempts preserved as <run_id>-attempt-N/
  supersedes: null | "<prior run_id>"     # set when a rerun replaces a failed run as current evidence
```

## Run folder layout (files ARE the state; numbering = resume pointer)

`NN-<name>.md`, strictly increasing. The highest `NN` present tells a resuming session exactly where the run stopped; each file's `expected_action` names what happens next. Artifact versions are immutable (`<name>.v2.md`, never edited in place); verdicts bind to sha256.

Canonical sequence (US-IDEA-01 reference): `00` intake → `01` candidate (+`.vN`) → `02` specialist packet(s) → `03` deterministic/computed packet → `04` artifact lock (+vN blocks) → `05/06` lens verdicts → `07` review decision → `08` promotion gate (authority sidecar — DL-1) → `09` gate presentation → `10` mutation record. Stories with fan-out insert additional `02x`/`05x` files; the ordering rule, not the exact count, is the contract.

## Resume rule

A fresh session resumes with ONLY: the run folder path + this schema. It must not need chat memory. Verified behaviorally: `tests/behavioral/resume-test-20260712.md`.

## Validation

`python3 scripts/orchestration_check.py packet <run folder>/NN-*.md` — every packet file parses against the handoff schema; `canon-write` gates any mutation step.
