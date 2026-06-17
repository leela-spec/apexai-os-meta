# APPENDIX_KB_EXAMPLES

## Purpose

Provide compact applied examples for safe source-to-KB routing in the `special_ops__knowledge_bank` KB.

Examples are illustrative. They do not create promptflow law, promotion authority, or shared governance.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** active examples appendix
- **Scope:** examples of KB placement, status preservation, and appendix-first structure
- **Non-scope:** prompt design, global file taxonomy, promotion approval, runtime config

## Example index

|example_id|example_type|input|output_surface|status|
|---|---|---|---|---|
|EX-KB-001|source_to_note|corrected promptflow|`APPENDIX_KB_SOURCE_NOTES.md`|active|
|EX-KB-002|source_note_to_candidate|`KBFuture.md` recommendation|`APPENDIX_KB_PROMOTION_TRACE.md`|active|
|EX-KB-003|candidate_to_learning_queue|examples expansion follow-up|`LEARNING_QUEUE.md`|active|
|EX-KB-004|candidate_to_scaffold|source notes practice|`BEST_PRACTICES.md`|active|
|EX-KB-005|evidence_to_anti_drift|connector replacement warning|`APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|active|

### EX-KB-001 — Corrected promptflow to source note

- **Example type:** source_to_note
- **Input:** corrected promptflow says Codex must apply exact unified diffs directly on `main` and old promptflows are historical only.
- **Transformation:** store the reusable observation as a compact row with source role `promptflow`.
- **Output surface:** `APPENDIX_KB_SOURCE_NOTES.md`
- **Why this is safe:** the note records execution constraints without applying them as global law outside this KB.
- **Do not:** treat the source note as proof that git apply execution happened.

### EX-KB-002 — Future recommendation to promotion trace

- **Example type:** source_note_to_candidate
- **Input:** `KBFuture.md` recommends adding a promotion trace appendix as P0/P1 work.
- **Transformation:** once operator-approved, create a trace row showing `approved_for_patch_pack`, target surface, validator, and decision.
- **Output surface:** `APPENDIX_KB_PROMOTION_TRACE.md`
- **Why this is safe:** it records KB-internal patch approval and explicitly avoids shared truth mutation.
- **Do not:** use `approved_for_patch_pack` as approval for shared governance or config changes.

### EX-KB-003 — Examples expansion to learning queue

- **Example type:** candidate_to_learning_queue
- **Input:** examples are useful but should expand only after schema surfaces stabilize.
- **Transformation:** capture expansion as a candidate follow-up with evidence refs and review due date.
- **Output surface:** `LEARNING_QUEUE.md`
- **Why this is safe:** the learning queue is candidate-only and cannot self-promote.
- **Do not:** expand examples until they illustrate stable schema, not provisional guesses.

### EX-KB-004 — Source notes practice to scaffold

- **Example type:** candidate_to_scaffold
- **Input:** source manifest records which sources were used; source notes record what a source contributed.
- **Transformation:** summarize the distinction as a compact best practice with appendix pointer.
- **Output surface:** `BEST_PRACTICES.md`
- **Why this is safe:** scaffold receives only rule, why, evidence, and use condition.
- **Do not:** paste source-note table rows into scaffold files.

### EX-KB-005 — Connector replacement warning to anti-drift evidence

- **Example type:** evidence_to_anti_drift
- **Input:** corrected promptflow forbids GitHub connector whole-file replacement as patch execution.
- **Transformation:** capture the risk as an anti-drift evidence row and reusable mistake pattern.
- **Output surface:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`; `MISTAKES.md`
- **Why this is safe:** it prevents a known execution failure without performing an unauthorized connector write.
- **Do not:** claim commit success without Codex final proof.

## Use constraints

- **Constraint:** examples illustrate storage and routing patterns only.
- **Constraint:** examples do not replace source manifest, candidate ledger, promotion trace, or QA plan rows.
- **Constraint:** examples must stay compact and avoid raw source bodies.
- **Constraint:** retire examples when their target schema changes materially.
