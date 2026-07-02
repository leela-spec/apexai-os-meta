# APPENDIX_KB_PROMOTION_TRACE

## Purpose

Track candidate-to-review-to-promotion movement for the `special_ops__knowledge_bank` KB.

This appendix is a trace database. It does not approve truth changes by itself.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** active trace appendix
- **Promotion authority:** external governed promotion path only
- **Rule:** no candidate becomes accepted truth because it appears here.

## Row schema

|field|required|meaning|
|---|---|---|
|`trace_id`|yes|stable promotion-trace row id|
|`candidate_id`|yes|candidate, update, or source id being tracked|
|`source_status`|yes|candidate, strong_candidate, evidence_only, approved_for_patch_pack, rejected, deferred|
|`validator`|yes|expected validator or validating surface|
|`promotion_target`|yes|target surface or promotion destination|
|`promotion_packet`|yes|packet pointer or `pending` / `not_required`|
|`decision`|yes|approved, rejected, deferred, pending, applied|
|`date`|yes|decision or trace date|
|`notes`|yes|bounded rationale and caveat|

## Promotion trace ledger

|trace_id|candidate_id|source_status|validator|promotion_target|promotion_packet|decision|date|notes|
|---|---|---|---|---|---|---|---|---|
|KB-PROMO-001|KB-UPD-001|approved_for_patch_pack|`special_ops__informatics_design`|`appendices/APPENDIX_KB_PROMOTION_TRACE.md`|not_required|approved|2026-05-04|operator validated creation as KB-internal trace surface; does not approve shared truth mutation|
|KB-PROMO-002|KB-UPD-002|approved_for_patch_pack|`special_ops__informatics_design`|`appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|not_required|approved|2026-05-04|operator validated durable QA and research surface|
|KB-PROMO-003|KB-UPD-003|approved_for_patch_pack|`special_ops__informatics_design`|`appendices/APPENDIX_KB_SOURCE_NOTES.md`|not_required|approved|2026-05-04|operator validated source-note database creation|
|KB-PROMO-004|KB-UPD-004|approved_for_patch_pack|`special_ops__informatics_design`|`appendices/APPENDIX_KB_DATABASE_SCHEMA.md`|not_required|approved|2026-05-04|operator validated schema appendix creation|
|KB-PROMO-005|KB-UPD-005|approved_for_patch_pack|`special_ops__informatics_design`|`appendices/APPENDIX_KB_EXAMPLES.md`|not_required|approved|2026-05-04|operator validated examples appendix creation; expansion remains queued|
|KB-PROMO-006|KB-UPD-006|approved_for_patch_pack|`special_ops__informatics_design`|`TEMPLATES.md`|not_required|approved|2026-05-04|operator validated template additions for new appendices and final proof schema|
|KB-PROMO-007|KB-UPD-007|approved_for_patch_pack|`special_ops__informatics_design`|`LEARNING_QUEUE.md`|not_required|approved|2026-05-04|operator validated deferred follow-up queue additions|
|KB-PROMO-008|KB-UPD-008|approved_for_patch_pack|`special_ops__informatics_design`|`ESSENCE.md`|not_required|approved|2026-05-04|operator validated corrected promptflow source-basis update|
|KB-PROMO-009|KB-UPD-009|approved_for_patch_pack|`special_ops__informatics_design`|`APPENDIX_KB_SOURCE_MANIFEST.md`|not_required|approved|2026-05-04|operator validated corrected execution lock update|
|KB-PROMO-010|KB-UPD-010|approved_for_patch_pack|`special_ops__informatics_design`|`MISTAKES.md`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|not_required|approved|2026-05-04|operator validated connector-replacement and legacy-basis anti-drift additions|

## Integrity rules

- **Rule:** every future candidate marked approved, rejected, deferred, or applied must have one trace row.
- **Rule:** `promotion_packet: not_required` is allowed only for KB-internal appendix/scaffold maintenance that does not mutate shared accepted truth.
- **Rule:** shared governance, config, provider/model, and cross-agent truth changes cannot use `not_required`.
- **Rule:** deletion of a trace row requires a replacement row or explicit supersession note.

## Review

- **Review trigger:** after every KB update patch.
- **Review partner:** `special_ops__informatics_design`.
