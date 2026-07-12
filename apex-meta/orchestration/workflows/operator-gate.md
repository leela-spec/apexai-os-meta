---
title: "Operator Gate Protocol"
purpose: >
  The G-item protocol generalized from US-IDEA-01's 09/10 files: how gated decisions are
  presented, answered, recorded, and executed. One primitive, applied where consequence
  lives — never everywhere.
created: 2026-07-12
---

# Operator Gate Protocol

## When a gate is required
Durable mutation, public output, spend, safety-relevant instruction, doctrine change, or professional-judgment boundary (the "consequential" definition in GLOSSARY.md). Low-consequence intermediates never acquire gates.

## Protocol

1. **Present (Alfred, main-conversation):** one gate-presentation packet (handoff schema, `status: operator_review_needed`) listing each decision as a **G-item**: what it is, verified evidence behind it (authority sidecar + digests), explicit options with consequences, and the relevant open uncertainties. Nothing executes while presented.
2. **Answer (operator):** captured verbatim, one answer per G-item. Allowed shapes: `approve` / `accept+<action>` / `edit` / `reject` / `hold` / `split` / `defer`. Silence or ambiguity = `hold`, never inferred approval.
3. **Record:** a mutation-record file (`NN-mutation-record.md`) with `operator_validation: confirmed` (or the refusing value), the answer channel + date, the authority basis (input paths, digests, sidecar refs), and per-mutation before/after.
4. **Check (deterministic):** `python3 scripts/orchestration_check.py canon-write <gate-record>` must exit 0 before execution — confirmed ∧ every input verified ∧ digests recompute-match. Exit 1/2 blocks the write (fail closed).
5. **Execute (Meta Ops, main-conversation):** through the mutation backbone only (apex-session pattern / `apex_sync.py registry --dry-run false`), exactly the approved scope.
6. **Fetch back:** re-read every mutated surface and record verification in the mutation record. A write that cannot be fetched back as expected is a failed mutation, reported, never smoothed over.

## Reference instance
US-IDEA-01: `09-gate-presentation.md` (step 1) → AskUserQuestion answers 2026-07-12 (step 2) → `10-mutation-record.md` (steps 3–6, G1 + G2, fetch-back verified, post-write drift cleared).
