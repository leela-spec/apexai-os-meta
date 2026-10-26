# Operational Plan — Orchestrator 4

## Objective
Author the complete Layered Rule Knowledge Base (Rules 02–22), execute 5 Plane 4 Module Audits, compile `16-candidate-3A-ultra.md` (~950 BPE tokens), update directory indexes, and verify 0 OKF/Profile errors and 196/196 tests passing.

## Milestones & Phasing

### Phase 0: Survey
- Spawn 3 parallel survey explorers / spec miners to map:
  - Spec Miner 1: Exact rule texts, tokens, semantic blocks, and research links for Rules 02–22.
  - Spec Miner 2: Plane 4 module inventories (`WP-01`..`WP-25`, `FA-01`..`FA-13`, `EM-01`..`EM-12`, `AD-01`..`AD-26`, `GS-01`..`GS-17`), single ownership checks, and audit framework.
  - Explorer 3: 3A-Ultra compression design, target token envelopes (~900–980 BPE), delta tables, and test/validator gates.
- Aggregate into `PROJECT.md` Feature Inventory & Architecture.

### Phase 1: Milestone 1 — Rules 02 to 08
- Target files in `apex-meta/informatics/final/research/06-layered-rule-kb/`:
  - `rule-02-product-first.md`
  - `rule-03-scope.md`
  - `rule-04-communication.md`
  - `rule-05-hold-position.md`
  - `rule-06-ground.md`
  - `rule-07-reuse.md`
  - `rule-08-context.md`
- Cycle: Explorer analysis -> Worker authoring -> Reviewers -> Challengers -> Auditor -> Gate check.

### Phase 2: Milestone 2 — Rules 09 to 15
- Target files in `apex-meta/informatics/final/research/06-layered-rule-kb/`:
  - `rule-09-recovery.md`
  - `rule-10-stop-repairing.md`
  - `rule-11-current-truth.md`
  - `rule-12-surgical.md`
  - `rule-13-editing.md`
  - `rule-14-new-machinery.md`
  - `rule-15-detour.md`
- Cycle: Explorer analysis -> Worker authoring -> Reviewers -> Challengers -> Auditor -> Gate check.

### Phase 3: Milestone 3 — Rules 16 to 22
- Target files in `apex-meta/informatics/final/research/06-layered-rule-kb/`:
  - `rule-16-authoring.md`
  - `rule-17-trade-off.md`
  - `rule-18-handover.md`
  - `rule-19-iterative.md`
  - `rule-20-schemas.md`
  - `rule-21-sync.md`
  - `rule-22-pointers.md`
- Cycle: Explorer analysis -> Worker authoring -> Reviewers -> Challengers -> Auditor -> Gate check.

### Phase 4: Milestone 4 — Plane 4 Infrastructure Module Audits
- Target files in `apex-meta/informatics/final/research/06-layered-rule-kb/`:
  - `audit-module-01-writing-profile.md`
  - `audit-module-02-file-architecture.md`
  - `audit-module-03-execution-modes.md`
  - `audit-module-04-anti-drift-rules.md`
  - `audit-module-05-governance-schemas.md`
- Cycle: Explorer analysis -> Worker authoring -> Reviewers -> Challengers -> Auditor -> Gate check.

### Phase 5: Milestone 5 — 16-candidate-3A-ultra.md, Indexes & Final Verification
- Target files:
  - `apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md`
  - `apex-meta/informatics/final/research/06-layered-rule-kb/index.md`
  - `apex-meta/informatics/final/index.md`
- Validation:
  - `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` (0 errors)
  - `python -m pytest apex-meta/informatics/tests/ -q` (196/196 passed)
  - Token counts, delta table, zero live mutation, research bytes preserved.
- Cycle: Worker integration -> Reviewers -> Challengers -> Auditor -> Final Gate -> Handoff report.
