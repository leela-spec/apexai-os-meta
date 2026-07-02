# APPENDIX_KB_SOURCE_NOTES

## Purpose

Record reusable source observations for the `special_ops__knowledge_bank` KB.

This appendix differs from `APPENDIX_KB_SOURCE_MANIFEST.md`: the manifest records what was used; source notes record what each source contributes.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** active source-note appendix
- **Rule:** source notes are observations and candidate links, not accepted truth.
- **Rule:** do not copy full source bodies into this appendix.

## Source notes schema

|field|required|meaning|
|---|---|---|
|`note_id`|yes|stable source-note row id|
|`source_path`|yes|repo-relative path or named source surface|
|`source_role`|yes|primary, supporting, evidence, audit, promptflow, appendix|
|`agent_relevance`|yes|why this source matters to Knowledge Bank|
|`usable_units`|yes|compact reusable information units|
|`risk_or_caveat`|yes|status, drift, duplication, or authority caveat|
|`candidate_links`|yes|candidate, update, or evidence ids|
|`status`|yes|active, evidence_only, deferred, superseded|

## Source notes ledger

|note_id|source_path|source_role|agent_relevance|usable_units|risk_or_caveat|candidate_links|status|
|---|---|---|---|---|---|---|---|
|KB-SN-001|`appendices/PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md`|promptflow|current update authority for KB correction|direct-main rule; no branch; Codex git-apply only; candidate decision table; old promptflow quarantine|planning chat cannot connector-write or claim git-apply execution|KB-UPD-001 through KB-UPD-010|active|
|KB-SN-002|`appendices/KBFuture.md`|appendix|high-impact future improvements for KB database layer|promotion trace; QA plan; source notes; database schema; examples; template and learning queue updates|future research is not automatic patch authorization without operator decision|KB-UPD-001 through KB-UPD-007|active|
|KB-SN-003|`KB_SYSTEM_RELIABILITY_AUDIT_V1`|audit|system reliability and machine-contract warning input|promptflows partially unreliable; add hard execution contracts; recover useful deltas; patch only correct target files|audit is process warning input, not content source for accepted truth|KB-UPD-010|active|
|KB-SN-004|`agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`|primary|bounded source-slice map for Special Ops KBs|identifies Knowledge Bank source slice and required read surfaces|source index is basis for source discovery, not final KB prose|KB-KB-CAND-001 through KB-KB-CAND-014|active|
|KB-SN-005|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ROLE_AND_KB_TARGET_MAP.md`|primary|defines Knowledge Bank ownership and non-ownership|KB owns architecture, layering, ownership, structured information evolution; does not own canonical truth approval|role map must not be used to bypass promotion or validator review|KB-KB-INFO-001; KB-KB-CAND-012|active|
|KB-SN-006|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md`|primary|ranked candidate authority for Knowledge Bank lane|top Knowledge Bank-ranked candidates include process discipline, density gate, patch evidence, validation, bullet classes, instruction block, waterfall risk, anti-drift, and blind-updater risk|ranking rows are candidate material until validated|KB-KB-CAND-001 through KB-KB-CAND-014|active|
|KB-SN-007|`APPENDIX_KB_CANDIDATE_LEDGER.md`|appendix|existing candidate database|defines candidate statuses and target distribution|candidate presence is not promotion|KB-UPD-001; KB-UPD-004|active|
|KB-SN-008|`APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|appendix|existing drift evidence database|captures candidate-to-canon leak, appendix bypass, evidence overgeneralization, hidden improvement application|needed new rows for connector replacement and legacy promptflow basis leak|KB-UPD-010|active|

## Use rules

- **Rule:** add one note per source contribution, not one note per paragraph.
- **Rule:** source notes may link to candidate ledger, promotion trace, QA plan, or examples.
- **Rule:** source notes may not replace source manifest coverage decisions.
- **Rule:** source notes may not promote candidate material.
- **Rule:** source notes that become obsolete must be marked `superseded` with replacement pointer rather than deleted silently.
