# TEMPLATES

## Purpose

Reusable Knowledge Bank forms for source manifesting, candidate capture, validation, and improvement capture.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** scaffold template surface
- **Rule:** templates are forms only; they do not create hidden promptflow law.

## Template index

|template_id|use_when|related_appendix|
|---|---|---|
|TPL-KB-001|recording a source used for KB-base construction|`appendices/APPENDIX_KB_SOURCE_MANIFEST.md`|
|TPL-KB-002|capturing a candidate extracted from source ledgers|`appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`|
|TPL-KB-003|ranking an information unit for scaffold or appendix placement|`appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`|
|TPL-KB-004|recording anti-drift evidence or evidence-only material|`appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|
|TPL-KB-005|capturing out-of-mode improvements without applying them|`LEARNING_QUEUE.md`|
|TPL-KB-006|fetch-back verification after KB file writes|all scaffold and appendix files|
|TPL-KB-007|recording candidate-to-review-to-promotion trace|`appendices/APPENDIX_KB_PROMOTION_TRACE.md`|
|TPL-KB-008|recording source observations beyond provenance|`appendices/APPENDIX_KB_SOURCE_NOTES.md`|
|TPL-KB-009|recording QA, readiness, and next research|`appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|
|TPL-KB-010|declaring a Markdown database schema row contract|`appendices/APPENDIX_KB_DATABASE_SCHEMA.md`|
|TPL-KB-011|recording source-to-KB applied examples|`appendices/APPENDIX_KB_EXAMPLES.md`|
|TPL-KB-012|reporting Codex git-apply execution proof|corrected promptflow final proof|

## TPL-KB-001 — Source manifest row

```md
|priority|source_path|source_role|read_status|use_in_this_build|
|---|---|---|---|---|
|<n>|`<repo-relative path>`|primary/supporting/evidence|read/skipped/blocked|<bounded use>|
```

## TPL-KB-002 — Candidate ledger row

```md
|candidate_id|rank_or_source|candidate_title|candidate_summary|source_path|candidate_target|validation_partner|status|notes|
|---|---:|---|---|---|---|---|---|---|
|KB-KB-CAND-###|<rank or supporting source>|<title>|<one compact unit>|`<source>`|`<target file>`|`special_ops__informatics_design`|candidate/strong_candidate/evidence_only|<promotion caution or use note>|
```

## TPL-KB-003 — Information ranking row

```md
|info_id|source_path|source_role|source_section_or_candidate_id|information_unit|agent_relevance|actionability|evidence_strength|reuse_frequency_likelihood|drift_risk|recommended_target_file|appendix_pointer|scaffold_summary_needed|status|
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
|KB-KB-INFO-###|`<source>`|<role>|<section or id>|<self-contained unit>|0-100|0-100|0-100|0-100|0-100|`<file>`|`<appendix#anchor>`|yes/no|active/evidence_only/excluded|
```

## TPL-KB-004 — Anti-drift evidence row

```md
|evidence_id|source_ref|failure_or_risk|safeguard|target_surface|status|
|---|---|---|---|---|---|
|KB-KB-DRIFT-###|`<candidate id or source path>`|<risk>|<countermeasure>|`<surface>`|active_evidence/evidence_only|
```

## TPL-KB-005 — Improvement opportunity capture

Use this when a better idea appears but is outside the authorized mode or target surface.

```md
### IMP-KB-### — <short title>

- **Affected area:** <file, appendix, scaffold, or process>
- **Type:** source_gap | structure_improvement | validation_improvement | template_improvement | routing_improvement
- **Observed issue:** <what was noticed>
- **Why it may improve the system:** <one compact explanation>
- **Why it was not applied now:** <scope or mode boundary>
- **Smallest safe future mode:** <candidate capture, validator review, bounded patch, promotion packet>
- **Risk if left unchanged:** <risk>
- **Risk if changed during this run:** <risk>
- **Status:** not_applied_in_this_run
```

## TPL-KB-006 — Fetch-back verification checklist

```md
## Fetch-back verification

- [ ] file exists at exact repo-relative path
- [ ] file is under `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/`
- [ ] no non-target repo is used as active source or target
- [ ] scaffold file remains compact
- [ ] appendix file contains deep detail rather than scaffold bloat
- [ ] candidate/evidence status is explicit
- [ ] no shared governance or accepted truth was changed
```

## TPL-KB-007 — Promotion trace row

```md
|trace_id|candidate_id|source_status|validator|promotion_target|promotion_packet|decision|date|notes|
|---|---|---|---|---|---|---|---|---|
|KB-PROMO-###|<candidate id>|candidate/strong_candidate/evidence_only|`special_ops__informatics_design`|`<target>`|`<packet or pending>`|approved/rejected/deferred/pending|YYYY-MM-DD|<bounded note>|
```

## TPL-KB-008 — Source notes row

```md
|note_id|source_path|source_role|agent_relevance|usable_units|risk_or_caveat|candidate_links|status|
|---|---|---|---|---|---|---|---|
|KB-SN-###|`<repo-relative path>`|primary/supporting/evidence/audit/promptflow|<why this source matters to KB>|<compact reusable units>|<risk or caveat>|<candidate ids>|active/evidence_only/deferred|
```

## TPL-KB-009 — QA and next research row

```md
|item_id|item_type|finding_or_question|evidence_refs|priority|owner|validator|status|next_action|
|---|---|---|---|---|---|---|---|---|
|KB-QA-###|qa_finding/research_question/patch_candidate/readiness_gap|<bounded item>|<refs>|P0/P1/P2/P3|`special_ops__knowledge_bank`|`special_ops__informatics_design`|open/closed/deferred|<next action>|
```

## TPL-KB-010 — Markdown database schema declaration

```md
### <database file path>

- **Database role:** <source_manifest | candidate_ledger | evidence_ledger | promotion_trace | source_notes | qa_plan | examples>
- **Required row id prefix:** <prefix>
- **Required status field:** yes/no
- **Allowed status values:** `<value>` | `<value>`
- **Required owner field:** yes/no
- **Required validator field:** yes/no
- **Scaffold link rule:** <how this database may be summarized in scaffold files>
- **Deletion rule:** <what proof is required before row deletion>
```

## TPL-KB-011 — Applied example block

```md
### EX-KB-### — <example title>

- **Example type:** source_to_note | note_to_candidate | candidate_to_learning_queue | candidate_to_scaffold | evidence_to_anti_drift
- **Input:** <minimal source unit or prior row>
- **Transformation:** <what changes between surfaces>
- **Output surface:** `<target>`
- **Why this is safe:** <candidate/status/source boundary>
- **Do not:** <specific unsafe generalization>
```

## TPL-KB-012 — Codex git-apply final proof

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/
git_apply_check_passed:
git_apply_passed:
git_diff_check_passed:
changed_file_set_expected:
changed_file_set_actual:
changed_file_set_matches_expected:
forbidden_paths_changed:
fetch_back_or_cat_verified:
commit_created:
commit_sha:
pushed_to_origin_main:
status:
notes:
```

## Use constraints

- **Constraint:** Do not add new status values casually.
- **Constraint:** Do not paste full source bodies into template examples.
- **Constraint:** Do not use templates as permission to bypass source manifest and validator review.
- **Constraint:** Do not use templates as proof that git apply execution occurred.
