# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for Knowledge Bank learning. This file is never runtime truth.

## Write permissions

- `special_ops__knowledge_bank` may add candidate entries.
- `special_ops__informatics_design` may add validation notes.
- No writer may self-promote entries into accepted shared governance or accepted truth.

## Entry schema

```yaml
learning_entry:
  id:
  status: candidate | strong_candidate | needs_validation | rejected | archived
  source_ref:
  summary:
  candidate_target: essence | best_practice | mistake | template | appendix | archive
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check:
  review_due:
```

## Pending entries

### LQ-KB-001 — Appendix-first KB build sequence

```yaml
learning_entry:
  id: LQ-KB-001
  status: strong_candidate
  source_ref: KB-KB-CAND-001
  summary: Build source manifest, ranking ledger, candidate ledger, and anti-drift appendix before scaffold drafting.
  candidate_target: best_practice
  evidence_refs:
    - appendices/APPENDIX_KB_SOURCE_MANIFEST.md
    - appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md
    - appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
  scores:
    EVD: 90
    IMP: 92
    RSK: 35
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check: meta_ops process evidence is used as support only
  review_due: 2026-07-25
```

### LQ-KB-002 — Candidate status preservation

```yaml
learning_entry:
  id: LQ-KB-002
  status: strong_candidate
  source_ref: KB-KB-CAND-008
  summary: Keep candidate, strong_candidate, and evidence_only status explicit until governed promotion occurs.
  candidate_target: best_practice
  evidence_refs:
    - appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
    - appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
  scores:
    EVD: 86
    IMP: 95
    RSK: 25
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check: promotion approval remains outside this agent
  review_due: 2026-07-25
```

### LQ-KB-003 — Density gate for scaffold entries

```yaml
learning_entry:
  id: LQ-KB-003
  status: strong_candidate
  source_ref: KB-KB-CAND-002
  summary: Do not let scaffold entries bypass density and self-containment checks.
  candidate_target: mistake
  evidence_refs:
    - appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#anti-drift-evidence-ledger
  scores:
    EVD: 86
    IMP: 90
    RSK: 20
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check: hygiene and informatics validation remain separate from KB ownership
  review_due: 2026-07-25
```

### LQ-KB-004 — Out-of-mode improvement capture

```yaml
learning_entry:
  id: LQ-KB-004
  status: strong_candidate
  source_ref: AIHowTo/Codex/Improvement_Capture_Rule.md
  summary: Detect useful improvements, but capture them as candidates instead of applying them outside the authorized run mode.
  candidate_target: best_practice
  evidence_refs:
    - appendices/APPENDIX_KB_CANDIDATE_LEDGER.md#candidate-ledger
    - TEMPLATES.md#tpl-kb-005--improvement-opportunity-capture
  scores:
    EVD: 90
    IMP: 92
    RSK: 30
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check: no direct edits outside target root
  review_due: 2026-07-25
```

### LQ-KB-005 — Critical-document patch discipline

```yaml
learning_entry:
  id: LQ-KB-005
  status: strong_candidate
  source_ref: KB-KB-CAND-009
  summary: Treat critical KB documents as patch-sensitive; avoid blind full rewrites and use section-local updates with invariants.
  candidate_target: mistake
  evidence_refs:
    - appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#reusable-failure-patterns
  scores:
    EVD: 82
    IMP: 88
    RSK: 25
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check: prompts/workflows source is evidence, not hidden runtime law
  review_due: 2026-07-25
```

### LQ-KB-006 — Promotion trace maintenance

```yaml
learning_entry:
  id: LQ-KB-006
  status: needs_validation
  source_ref: KB-UPD-001
  summary: Keep `APPENDIX_KB_PROMOTION_TRACE.md` synchronized with candidate ledger rows, validator decisions, promotion packets, and rejected or deferred candidates.
  candidate_target: appendix
  evidence_refs:
    - appendices/APPENDIX_KB_PROMOTION_TRACE.md
    - appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
    - MISTAKES.md#mk-kb-001--candidate-to-canon-leak
  scores:
    EVD: 90
    IMP: 95
    RSK: 20
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check: promotion approval remains outside this agent
  review_due: 2026-07-25
```

### LQ-KB-007 — Source notes compaction review

```yaml
learning_entry:
  id: LQ-KB-007
  status: candidate
  source_ref: KB-UPD-003
  summary: Review `APPENDIX_KB_SOURCE_NOTES.md` after the first applied update to ensure source notes remain compact and do not duplicate full source manifest rows.
  candidate_target: appendix
  evidence_refs:
    - appendices/APPENDIX_KB_SOURCE_NOTES.md
    - appendices/APPENDIX_KB_SOURCE_MANIFEST.md
    - BEST_PRACTICES.md#bp-kb-007--separate-source-notes-from-source-manifesting
  scores:
    EVD: 82
    IMP: 88
    RSK: 35
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check: source interpretation remains candidate/evidence bounded
  review_due: 2026-07-25
```

### LQ-KB-008 — Examples expansion after schema stabilization

```yaml
learning_entry:
  id: LQ-KB-008
  status: candidate
  source_ref: KB-UPD-005
  summary: Expand `APPENDIX_KB_EXAMPLES.md` only after the promotion trace, source notes, QA plan, and database schema appendices remain stable through one patch cycle.
  candidate_target: appendix
  evidence_refs:
    - appendices/APPENDIX_KB_EXAMPLES.md
    - appendices/APPENDIX_KB_DATABASE_SCHEMA.md
  scores:
    EVD: 75
    IMP: 80
    RSK: 45
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  overlap_check: examples illustrate storage and routing only; they do not create promptflow law
  review_due: 2026-07-25
```

## Promotion route

1. Capture candidate here.
2. Score `EVD` / `IMP` / `RSK`.
3. Validate placement and structure with `special_ops__informatics_design`.
4. Route to the target file class.
5. Package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` or the current governed promotion surface.
6. Apply only through the governed promotion path.

## Queue hygiene

- **Rule:** archive rejected or superseded entries with reason.
- **Rule:** never remove a candidate solely because scaffold prose now references it.
- **Rule:** if a candidate belongs mainly to another agent, keep only the placement implication here and route the body outward.
