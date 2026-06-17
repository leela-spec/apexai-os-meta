# MISTAKES

## Purpose

Reusable Knowledge Bank failure patterns and countermeasures. This file is compact; detailed evidence remains in `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** scaffold guidance derived from source ledgers and anti-drift appendix
- **Promotion caution:** patterns here are operational safeguards, not shared governance mutation.

## Failure patterns

### MK-KB-001 — Candidate-to-canon leak

- **Pattern:** A strong candidate is copied into scaffold prose without status, evidence pointer, or validator boundary.
- **Trigger conditions:** high-ranked ledger item; urgency to make KB “complete”; missing candidate ledger row.
- **Consequence:** candidate material becomes de facto accepted truth.
- **Countermeasure:** store candidate details in `APPENDIX_KB_CANDIDATE_LEDGER.md`; summarize only compactly; route promotion through the governed path.
- **Evidence refs:** `KB-KB-CAND-008`; `KB-KB-DRIFT-001`; `KB-KB-DRIFT-004`.

### MK-KB-002 — Scaffold bloat / appendix bypass

- **Pattern:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, or `LEARNING_QUEUE.md` starts carrying raw source bodies, long rationale, or archive excerpts.
- **Trigger conditions:** broad source ingestion; desire to preserve every nuance; missing appendix pointer.
- **Consequence:** activation files become low-retrieval and context-heavy.
- **Countermeasure:** move detail to appendices; keep scaffold entries as rule, condition, evidence pointer, and next action.
- **Evidence refs:** `KB-KB-INFO-011`; `KB-KB-DRIFT-002`; `KB-KB-DRIFT-003`.

### MK-KB-003 — Density gate bypass

- **Pattern:** a scratchpad, source bundle, or generated artifact is treated as usable KB structure before density and self-containment are checked.
- **Trigger conditions:** staged generation fatigue; scaffold drafted before ranking ledger; missing validator pass.
- **Consequence:** prose blobs and ambiguous units enter reusable KB surfaces.
- **Countermeasure:** run density gate before scaffold drafting; ensure every scaffold item is compact and independently understandable.
- **Evidence refs:** `KB-META-OPS-023`; `KB-KB-DRIFT-001`.

### MK-KB-004 — Local grammar invention

- **Pattern:** the agent invents new bullet labels, relation types, status values, or file classes instead of using existing ledgers/canons.
- **Trigger conditions:** incomplete context; format discomfort; attempt to make the current artifact “cleaner.”
- **Consequence:** cross-agent retrieval and validation degrade.
- **Countermeasure:** reuse existing typed signal words and status semantics; unresolved grammar changes go to `LEARNING_QUEUE.md`.
- **Evidence refs:** `KB-META-OPS-009`; `KB-META-OPS-034`; `KB-KB-DRIFT-002`.

### MK-KB-005 — Blind rewrite of critical KB files

- **Pattern:** a critical KB scaffold or appendix is regenerated wholesale instead of patched or updated by bounded section.
- **Trigger conditions:** long document; stale source; pressure to harmonize everything at once.
- **Consequence:** omissions, semantic drift, and loss of auditability.
- **Countermeasure:** patch one named file or section at a time; define invariants before editing; fetch back after each write.
- **Evidence refs:** `KB-PROMPTS-WORKFLOWS-032`; `KB-KB-DRIFT-003`.

### MK-KB-006 — Waterfall overfit

- **Pattern:** the agent freezes a complete skeleton too early and forces emerging knowledge into premature structure.
- **Trigger conditions:** uncertain source body; demand for formal output before evidence stabilizes.
- **Consequence:** false completeness, missing hard sections, or structural debt hidden under neat headings.
- **Countermeasure:** use hypothesis-first structure for uncertain material, then density/validation before final scaffold summary.
- **Evidence refs:** `KB-META-OPS-025`; `KB-KB-DRIFT-006`.

### MK-KB-007 — Evidence overgeneralization

- **Pattern:** a failure/postmortem source is treated as universal doctrine instead of bounded evidence.
- **Trigger conditions:** vivid failure case; strong score; missing evidence-only marker.
- **Consequence:** local incident logic hardens into broad KB law.
- **Countermeasure:** mark postmortem-derived items as evidence_only unless separately validated by the owner/validator pair.
- **Evidence refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#evidence-only-register`.

### MK-KB-008 — Connector replacement disguised as patch execution

- **Pattern:** A GitHub connector `update_file` or `create_file` replacement is described as if it were native unified-diff patch execution.
- **Trigger conditions:** no local checkout; urgency to finish; patch pack treated as equivalent to applied git diff.
- **Consequence:** validation claims become false because `git apply --check`, `git apply`, `git diff --check`, and exact changed-file verification did not run.
- **Countermeasure:** when native `git apply` is unavailable, stop after producing exact unified diffs and a zero-freedom Codex prompt; do not execute connector whole-file replacement.
- **Evidence refs:** `PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md`; `KB_SYSTEM_RELIABILITY_AUDIT_V1`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#anti-drift-evidence-ledger`.

### MK-KB-009 — Legacy promptflow basis leak

- **Pattern:** an older Knowledge Bank promptflow is used as the basis for current KB updates after a corrected promptflow exists.
- **Trigger conditions:** old scaffold source-basis references; source manifest execution lock still names old promptflow; no quarantine step.
- **Consequence:** corrected execution rules are bypassed, including direct-main execution, no branch creation, and Codex-only git-apply requirements.
- **Countermeasure:** record legacy promptflows as historical_context_only; use only the corrected promptflow as current authority; stop if unresolved conflict appears.
- **Evidence refs:** `APPENDIX_KB_SOURCE_MANIFEST.md`; `ESSENCE.md`; `PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md`.

## Closure rule

A mistake pattern is closed only when the triggering scaffold, appendix, or learning queue entry has been corrected and the correction remains traceable to the relevant candidate/evidence row.
