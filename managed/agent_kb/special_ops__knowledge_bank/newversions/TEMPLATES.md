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

## Use constraints

- **Constraint:** Do not add new status values casually.
- **Constraint:** Do not paste full source bodies into template examples.
- **Constraint:** Do not use templates as permission to bypass source manifest and validator review.
