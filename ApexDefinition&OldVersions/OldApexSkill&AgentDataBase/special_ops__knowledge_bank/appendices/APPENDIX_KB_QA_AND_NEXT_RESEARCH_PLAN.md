# APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN

## Purpose

Record durable QA, readiness, known gaps, and next research for the `special_ops__knowledge_bank` KB.

This appendix prevents QA and research status from remaining chat-only.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** active QA and research appendix
- **Scope:** KB-internal scaffold and appendix surfaces only
- **Non-scope:** shared governance mutation, config mutation, provider/model changes, cross-agent promotion approval

## Run QA ledger

|item_id|item_type|finding_or_question|evidence_refs|priority|owner|validator|status|next_action|
|---|---|---|---|---|---|---|---|---|
|KB-QA-001|qa_finding|Corrected promptflow exists and supersedes old KB promptflow as current update authority.|`PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md`|P0|`special_ops__knowledge_bank`|`special_ops__informatics_design`|open|apply patch pack through Codex git apply only|
|KB-QA-002|qa_finding|Old promptflow references remain in existing scaffold/source-manifest surfaces before this patch.|`ESSENCE.md`; `APPENDIX_KB_SOURCE_MANIFEST.md`|P0|`special_ops__knowledge_bank`|`special_ops__informatics_design`|open|correct source-basis and execution-lock references|
|KB-QA-003|qa_finding|Existing KB base has strong source manifest, candidate ledger, ranking ledger, anti-drift evidence, templates, and learning queue.|`APPENDIX_KB_SOURCE_MANIFEST.md`; `APPENDIX_KB_CANDIDATE_LEDGER.md`; `TEMPLATES.md`; `LEARNING_QUEUE.md`|P2|`special_ops__knowledge_bank`|`special_ops__informatics_design`|closed|preserve architecture and add database governance layer|
|KB-QA-004|qa_finding|No native git-apply execution is available in planning chat; connector write execution is forbidden by corrected promptflow.|`PROMPTFLOW_SPECIAL_OPS_KNOWLEDGE_BANK_KB_UPDATE_CORRECTED.md`|P0|`special_ops__knowledge_bank`|`special_ops__informatics_design`|open|produce patch pack and zero-freedom Codex prompt; do not connector-write|

## Functional readiness

|surface|readiness|evidence|gap|next_action|
|---|---|---|---|---|
|`ESSENCE.md`|usable_with_patch_needed|compact boundary and constraints exist|old promptflow source-basis reference|apply corrected source-basis patch|
|`BEST_PRACTICES.md`|usable_with_patch_needed|appendix-first, candidate preservation, narrow authority stack exist|new database surfaces not yet referenced|add compact practices and pointers|
|`MISTAKES.md`|usable_with_patch_needed|major KB risks covered|connector replacement and legacy promptflow leak not covered|add failure patterns|
|`TEMPLATES.md`|usable_with_patch_needed|core source/candidate/ranking/evidence templates exist|new appendices lack templates|add rows and schemas|
|`LEARNING_QUEUE.md`|usable_with_patch_needed|candidate-only route exists|new follow-up items not represented|add follow-up entries|
|existing appendices|usable_with_patch_needed|source/candidate/ranking/evidence databases exist|schema contract and promotion/source-note/QA/example appendices missing|create new appendices|

## Research backlog

|research_id|question|priority|reason|owner|validator|status|
|---|---|---|---|---|---|---|
|KB-RSCH-001|Should KB Markdown database status values become shared across all Special Ops agent KBs?|P1|database schema consistency may need cross-agent harmonization|`special_ops__knowledge_bank`|`special_ops__informatics_design`|open|
|KB-RSCH-002|How much duplication is allowed between source manifest, source notes, candidate ledger, and promotion trace?|P1|redundancy discipline is central to retrieval and anti-sprawl|`special_ops__knowledge_bank`|`special_ops__informatics_design`|open|
|KB-RSCH-003|Should source notes remain Markdown-only or later gain machine-readable sidecars?|P2|operator preference favors Markdown; later automation may need exports|`special_ops__knowledge_bank`|`special_ops__informatics_design`|deferred|
|KB-RSCH-004|Which example set best teaches future agents safe source-to-KB routing without creating new law?|P2|examples are useful but should follow schema stabilization|`special_ops__knowledge_bank`|`special_ops__informatics_design`|open|

## Next patch candidates

|candidate_id|target|priority|smallest_safe_mode|status|
|---|---|---|---|---|
|KB-NEXT-001|cross-agent database schema alignment|P1|research packet|deferred|
|KB-NEXT-002|examples expansion after one successful Codex application|P2|bounded appendix patch|queued|
|KB-NEXT-003|promotion trace reconciliation with future promotion packets|P1|bounded appendix patch|queued|
|KB-NEXT-004|source notes compaction review|P2|validator review|queued|

## Closure rules

- **Rule:** QA findings close only when the target surface is patched and fetch-back or `cat` verification confirms the expected content.
- **Rule:** next research items close only with explicit disposition: answered, deferred, rejected, or promoted to packet.
- **Rule:** no QA item may silently mutate accepted truth.
- **Rule:** this appendix may recommend future work but cannot approve cross-agent truth changes.
