# TEMPLATES

## Purpose

Reusable Knowledge Bank forms for source manifesting, candidate capture, validation, improvement capture, Apex LearningCandidate routing, and KB release-delta readiness.

## Boundary

- **Owner:** `special_ops__knowledge_bank`
- **Validator:** `special_ops__informatics_design`
- **Status:** scaffold template surface
- **Rule:** templates are forms only; they do not create hidden promptflow law.

## Template index

|template_id|use_when|related_appendix_or_surface|
|---|---|---|
|TPL-KB-001|recording a source used for KB-base construction|`appendices/APPENDIX_KB_SOURCE_MANIFEST.md`|
|TPL-KB-002|capturing a candidate extracted from source ledgers|`appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`|
|TPL-KB-003|ranking an information unit for scaffold or appendix placement|`appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`|
|TPL-KB-004|recording anti-drift evidence or evidence-only material|`appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|
|TPL-KB-005|capturing out-of-mode improvements without applying them|`LEARNING_QUEUE.md`|
|TPL-KB-006|fetch-back verification after KB file writes|all scaffold and appendix files|
|TPL-KB-007|drafting sanitized project-to-meta KB learning|`LEARNING_QUEUE.md`; `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`|
|TPL-KB-008|preparing meta-to-project KB release delta readiness|release-pack review surfaces|

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
- [ ] file is under `managed/agent_kb/special_ops__knowledge_bank/`
- [ ] no non-target repo is used as active source or target
- [ ] scaffold file remains compact
- [ ] appendix file contains deep detail rather than scaffold bloat
- [ ] candidate/evidence status is explicit
- [ ] no shared governance or accepted truth was changed
```

## TPL-KB-007 — Apex project-to-meta LearningCandidate packet

Use this when a project-local KB lesson may be useful at the Apex meta layer.

```yaml
learning_candidate:
  id:
  origin_project:
  sanitized: true | false
  raw_project_data_included: false
  source_refs:
  observed_result:
  generalized_learning:
  proposed_meta_target:
    lane: special_ops__knowledge_bank
    file: LEARNING_QUEUE.md | BEST_PRACTICES.md | MISTAKES.md | TEMPLATES.md | appendix
  candidate_status: candidate | strong_candidate | needs_validation
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  promotion_surface: managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md
  release_pack_relevance:
  notes:
```

## TPL-KB-008 — Meta-to-project KB release delta readiness

Use this when a validated KB improvement may be released from Apex meta to project repos.

```yaml
kb_release_delta:
  id:
  source_meta_file:
  target_project_pack:
  include_files:
  exclude_files:
  appendices_included: none | selected | all
  reason_for_inclusion:
  project_adoption_mode: adopt | defer | reject | project_decides
  raw_meta_history_included: false
  project_data_included: false
  validator:
  release_status: candidate | ready_for_review | approved | rejected
  notes:
```

## Use constraints

- **Constraint:** Do not add new status values casually.
- **Constraint:** Do not paste full source bodies into template examples.
- **Constraint:** Do not use templates as permission to bypass source manifest and validator review.
- **Constraint:** LearningCandidate packets must not contain raw project data.
- **Constraint:** Release-delta templates prepare review; they do not approve release.
