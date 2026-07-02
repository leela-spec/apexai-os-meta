# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for Meta Detective learning. This file is never runtime truth.

Meta Detective may record useful future validation patterns here, but entries remain candidates until routed through owner / validator review, overlap checks, EVD/IMP/RSK scoring, and the governed promotion path.

Promoted entries may remain visible here as trace records, but their operational doctrine must live in the promoted target file, not in the learning queue.

## Write permissions

- `meta_detective` may add candidate entries
- `special_ops__hygiene_clean` may add validation notes when structural findings matter
- no writer may self-promote entries into accepted files

## Entry schema

```yaml
learning_entry:
  id:
  status: candidate | strong_candidate | needs_validation | promoted | rejected | archived
  source_ref:
  summary:
  candidate_target: essence | best_practice | mistake | template | archive | mixed_pack
  candidate_targets: []
  evidence_refs:
  scores:
    score_scale: 1-100
    EVD:
    IMP:
    RSK:
  owner: meta_detective
  validator: special_ops__hygiene_clean
  overlap_check:
  review_due:
```

## Score convention

All `EVD`, `IMP`, and `RSK` scores use the active **1-100** scale. No 1-5 metric scale is used in this managed KB.

## Pending entries

### DET-LQ-001 — Base-rate and outside-view review pattern

```yaml
learning_entry:
  id: DET-LQ-001
  status: candidate
  source_ref: Logic Frameworks.md / Creative Strategy.md
  summary: Add a Detective pattern for comparing a recommendation against base rates, similar past cases, and the outside view before accepting inside-view claims.
  candidate_target: best_practice
  candidate_targets:
    - best_practice
    - template
  evidence_refs:
    - Logic Frameworks.md
    - Creative Strategy.md
  scores:
    score_scale: 1-100
    EVD: 72
    IMP: 84
    RSK: 62
  owner: meta_detective
  validator: special_ops__hygiene_clean
  overlap_check: Must not become Strategy scenario work; Detective role is to challenge plausibility and evidence.
  review_due: 2026-07-25
```

### DET-LQ-002 — Model/tool routing risk review

```yaml
learning_entry:
  id: DET-LQ-002
  status: needs_validation
  source_ref: OpenClaw model and AI handling source material
  summary: Add a Detective review pattern for checking whether a task used an unsuitable model, connector, or tool posture, while preserving AI Handling/Routing as the owner of routing doctrine.
  candidate_target: best_practice
  candidate_targets:
    - best_practice
    - template
  evidence_refs:
    - OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/OVERLAP_VALIDATION_MATRIX.md
  scores:
    score_scale: 1-100
    EVD: 70
    IMP: 78
    RSK: 72
  owner: meta_detective
  validator: special_ops__hygiene_clean
  overlap_check: Must route routing-doctrine changes to `special_ops__ai_handling_routing`; Detective may only flag risk.
  review_due: 2026-07-25
```

### DET-LQ-003 — High-stakes claim-level verification packet

```yaml
learning_entry:
  id: DET-LQ-003
  status: strong_candidate
  source_ref: AIHowTo/BasicFiles4Agents/Validation&Authority/Val&AuthResearchClaude.md
  summary: Promote a heavier claim-level verification template for high-stakes factual outputs and handoffs only, not for every low-risk step.
  candidate_target: template
  candidate_targets:
    - template
    - best_practice
  evidence_refs:
    - AIHowTo/BasicFiles4Agents/Validation&Authority/Val&AuthResearchClaude.md
  scores:
    score_scale: 1-100
    EVD: 86
    IMP: 80
    RSK: 54
  owner: meta_detective
  validator: special_ops__hygiene_clean
  overlap_check: Must not overload ordinary reviews; scope must be high-stakes or handoff-critical only.
  review_due: 2026-07-25
```

### DET-LQ-004 — Evidence contradiction register

```yaml
learning_entry:
  id: DET-LQ-004
  status: candidate
  source_ref: OpenClaw final-system governance and source-authority material
  summary: Add a reusable contradiction-register template for cases where two primary sources conflict and the system needs a durable hold/escalation record.
  candidate_target: template
  candidate_targets:
    - template
    - archive
  evidence_refs:
    - AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md
  scores:
    score_scale: 1-100
    EVD: 82
    IMP: 82
    RSK: 68
  owner: meta_detective
  validator: special_ops__hygiene_clean
  overlap_check: Must not replace the promotion ledger or cross-reference manifest; it is a temporary validation artifact.
  review_due: 2026-07-25
```

### DET-LQ-005 — Internal modes pack validation follow-up

```yaml
learning_entry:
  id: candidate_meta_detective_internal_modes_pack_v0
  status: promoted
  source_ref:
    - agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_ORIENTATION_WORKING.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_EVIDENCE_SOURCE_VERIFIER_WORKING.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_CONTRADICTION_LOGIC_AUDITOR_WORKING.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_BOUNDARY_AUTHORITY_GUARDIAN_WORKING.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_RISK_FAILURE_RED_TEAMER_WORKING.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_VERDICT_ESCALATION_SYNTHESIZER_WORKING.md
    - OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_HYGIENE_VALIDATION_REPORT.md
  summary: Promoted internal mode system for Meta Detective. The pack defines Evidence & Source Verifier, Contradiction & Logic Auditor, Boundary & Authority Guardian, Risk & Failure-Mode Red Teamer, and Verdict & Escalation Synthesizer as accepted internal validation modes rather than permanent sub-agents.
  candidate_target: mixed_pack
  promoted_to:
    - OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/APPENDIX_INTERNAL_MODES.md
  promotion_type: accepted_appendix
  candidate_targets:
    - essence
    - best_practice
    - mistake
    - template
  evidence_refs:
    - agent_kb_source_indexes/META_HEADS_KB_BASE_BUILD_INDEX.md
    - OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md
    - OpenClaw/07_finalopenclawsystem/managed/knowledge/OVERLAP_VALIDATION_MATRIX.md
  scores:
    score_scale: 1-100
    EVD: 80
    IMP: 88
    RSK: 30
  owner: meta_detective
  validator: special_ops__hygiene_clean
  overlap_check: Promotion finalized as appendix doctrine while preserving boundaries with meta_ops, meta_strategy, hygiene_clean, knowledge_bank, informatics_design, prompts_workflows, and ai_handling_routing.
  review_due: 2026-07-25
```

## Promotion route

1. capture candidate here
2. score `EVD` / `IMP` / `RSK` on the 1-100 scale
3. route to the target file class
4. validate with `special_ops__hygiene_clean`, escalating to `meta_ops` when execution implications matter
5. package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
6. apply only through the governed promotion path

## Queue safeguards

- This file is not runtime truth.
- Candidate entries may inform future review work only when their candidate status is visible.
- Accepted practices, mistakes, and templates must live in their target files after validation.
- Rejected or archived candidates must remain visible rather than silently disappearing.
- Working files are not canon by storage alone.
