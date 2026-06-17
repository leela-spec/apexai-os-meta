# MISTAKES

## Purpose

Compact failure-pattern and recovery-playbook surface for `special_ops__hygiene_clean`.

Detailed evidence lives in `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.

## Mistake patterns

### M-HC-001 — Repair by interpretation

- **Pattern:** A dead path, stale reference, or corrupted span is repaired by plausible redesign rather than exact minimal correction.
- **Trigger:** target file contains legacy references, missing files, or broken markdown after migration.
- **Risk:** semantic drift hidden inside cleanup.
- **Countermeasure:** use exact-span repair; stop when exact repair is impossible.
- **Evidence:** `HC-EVID-007` to `HC-EVID-009`.
- **Status:** `strong_candidate`.

### M-HC-002 — Execute-not-explain drift

- **Pattern:** A bounded execution request turns into process explanation, meta-planning, or teaching.
- **Trigger:** user asks to execute but the agent broadens into workflow explanation without a blocker.
- **Risk:** task failure, time waste, context loss, user-trust damage.
- **Countermeasure:** execute the next authorized step; explain only blockers or final verification.
- **Evidence:** `HC-EVID-010` to `HC-EVID-012`.
- **Status:** `strong_candidate`.

### M-HC-003 — Whole-file rewrite reflex

- **Pattern:** The agent proposes or performs a full rewrite for a bounded corruption, patch, or local defect.
- **Trigger:** markdown fence damage, truncation, path normalization, or local cleanup.
- **Risk:** unrelated wording changes and unreviewable semantic drift.
- **Countermeasure:** require exact target spans, protected spans, and unified-diff review.
- **Evidence:** `HC-INFO-007`, `HC-INFO-008`.
- **Status:** `strong_candidate`.

### M-HC-004 — Process-gate bypass

- **Pattern:** Process doctrine is cited but not used as a blocking gate.
- **Trigger:** agent says it understands the workflow yet proceeds without mode lock, source lock, or diff review.
- **Risk:** existing rules fail to constrain behavior.
- **Countermeasure:** require preflight proof against active gates before action.
- **Evidence:** `HC-EVID-013`, `HC-EVID-014`.
- **Status:** `strong_candidate`.

### M-HC-005 — Mode crossing

- **Pattern:** One operation mode silently becomes another, e.g. move-only becomes move plus edit plus scaffolding.
- **Trigger:** execution brief mixes migration, design, cleanup, and explanation.
- **Risk:** scope widening and audit loss.
- **Countermeasure:** declare exactly one mode; stop if completion requires crossing modes.
- **Evidence:** `HC-EVID-004`, `HC-EVID-014`.
- **Status:** `strong_candidate`.

### M-HC-006 — Target-topology drift

- **Pattern:** A process creates new target files or topology before proving existing living files cannot absorb the logic.
- **Trigger:** blueprint-to-target work without merge-map or no-fit proof.
- **Risk:** greenfield rebuild under harmonization language.
- **Countermeasure:** require merge-map/no-fit gate before target matrix or rewrite packets.
- **Evidence:** `HC-EVID-015`, `HC-EVID-016`.
- **Status:** `strong_candidate`.

### M-HC-007 — Candidate/truth contamination

- **Pattern:** A hygiene finding, postmortem, or candidate rule is treated as accepted truth.
- **Trigger:** useful lesson is copied directly into scaffold or canon without status and verification.
- **Risk:** silent self-modification of doctrine.
- **Countermeasure:** keep candidate/evidence status explicit; route through promotion when truth changes are needed.
- **Evidence:** `HC-INFO-014`, `HC-INFO-015`.
- **Status:** `strong_candidate`.

## Recovery playbook

1. **Lock:** identify exact repo, branch, target surface, mode, and closed file set.
2. **Classify:** authority drift, verification drift, rewrite drift, mode drift, scope drift, closure drift, or candidate/truth drift.
3. **Stop:** halt if exact source, target span, or authority is missing.
4. **Narrow:** define allowed spans and protected spans.
5. **Patch:** use minimal change only.
6. **Verify:** inspect diff, file existence, expected anchors, and no unintended deletions.
7. **Route:** close, backlog, escalate, or promotion-route with evidence.
