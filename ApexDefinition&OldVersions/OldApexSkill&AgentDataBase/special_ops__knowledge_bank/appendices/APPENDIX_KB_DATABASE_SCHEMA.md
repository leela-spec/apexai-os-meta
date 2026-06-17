# APPENDIX_KB_DATABASE_SCHEMA

## Purpose

Define the shared schema contract for Markdown database appendices inside the `special_ops__knowledge_bank` KB.

This appendix governs database consistency inside this KB only. It does not define global OpenClaw file law.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** active schema appendix
- **Scope:** appendices under `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/appendices/`
- **Non-scope:** global file taxonomy, shared governance, config schema, provider/model configuration

## Database surface register

|database_file|database_role|required_row_id_prefix|required_status_field|allowed_status_values|required_owner_field|required_validator_field|scaffold_link_rule|deletion_rule|
|---|---|---|---|---|---|---|---|---|
|`APPENDIX_KB_SOURCE_MANIFEST.md`|source_manifest|`GAP-` for gaps; source rows use priority|yes|read; skipped; blocked; excluded; included as evidence; approved_for_patch_pack|no|no|scaffold may cite source basis only|do not delete source rows unless source was listed in error and replacement is recorded|
|`APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`|information_ranking|`KB-KB-INFO-`|yes|active; evidence_only; excluded; superseded|no|no|scaffold may summarize active units only|do not delete ranked units; mark superseded or excluded|
|`APPENDIX_KB_CANDIDATE_LEDGER.md`|candidate_ledger|`KB-KB-CAND-`|yes|strong_candidate; candidate; evidence_only; excluded; superseded|no|yes|scaffold may summarize strong candidates with caveat|do not delete candidates without promotion/rejection/supersession trace|
|`APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|evidence_ledger|`KB-KB-DRIFT-`; `KB-KB-EVID-`|yes|active_evidence; evidence_only; superseded|no|no|scaffold may summarize safeguards only|do not delete evidence rows; mark superseded|
|`APPENDIX_KB_PROMOTION_TRACE.md`|promotion_trace|`KB-PROMO-`|yes|candidate; strong_candidate; evidence_only; approved_for_patch_pack; rejected; deferred; applied|yes through owner surface|yes|scaffold may cite trace existence, not approval authority|do not delete rows without replacement or explicit supersession|
|`APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|qa_plan|`KB-QA-`; `KB-RSCH-`; `KB-NEXT-`|yes|open; closed; deferred; queued|yes|yes|scaffold may cite durable QA status only|close with evidence; do not silently remove open items|
|`APPENDIX_KB_SOURCE_NOTES.md`|source_notes|`KB-SN-`|yes|active; evidence_only; deferred; superseded|no|no|scaffold may cite compact source observations only|mark superseded rather than deleting|
|`APPENDIX_KB_EXAMPLES.md`|examples|`EX-KB-`|yes|active; candidate; retired|no|no|scaffold may cite examples as illustrations only|retire obsolete examples with reason|

## Shared ID rules

- **Rule:** every database-like appendix must use stable row IDs when rows can be referenced by another surface.
- **Rule:** IDs are local to the Knowledge Bank KB unless explicitly promoted elsewhere.
- **Rule:** new prefixes require validator review before use.
- **Rule:** do not reuse deleted or retired IDs.

## Shared status rules

- **Rule:** status values must be visible in a table cell or YAML field.
- **Rule:** candidate status is not truth status.
- **Rule:** `approved_for_patch_pack` means approved for the current KB-internal patch pack only.
- **Rule:** `applied` may be used only after Codex final proof confirms commit and push.
- **Rule:** `not_required` in promotion packet fields is valid only for KB-internal maintenance that does not mutate shared accepted truth.

## Table versus YAML rule

|use table row when|use YAML block when|
|---|---|
|many rows share the same fields|one item needs nested fields|
|the database needs quick scanning|the item needs structured subfields|
|the item is likely to be sorted or filtered|the item needs multiline evidence or scores|

## Linkage rules

- **Rule:** scaffold files should point to appendices rather than duplicating database rows.
- **Rule:** source notes may link to candidate ledger and promotion trace.
- **Rule:** promotion trace may link to candidate ledger, QA plan, and eventual promotion packets.
- **Rule:** QA plan may link to all KB database surfaces.
- **Rule:** examples may link to source notes, candidate rows, learning queue entries, and anti-drift evidence.

## Anti-overengineering rule

- **Constraint:** this schema does not require JSON sidecars.
- **Constraint:** this schema does not require repo-wide metadata backfill.
- **Constraint:** this schema does not create global OpenClaw file law.
- **Constraint:** this schema must stay compact enough for future agents to apply without broad traversal.

## Review

- **Review trigger:** any new database-like appendix or new row-id prefix.
- **Review partner:** `special_ops__informatics_design`.
