# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for Meta Strategy learning. This file is never runtime truth.

## Write permissions

- `meta_strategy` may add candidate entries
- `meta_detective` may add validation notes
- no writer may self-promote entries into accepted files

## Entry schema

```yaml
learning_entry:
  id:
  status: candidate | strong_candidate | needs_validation | rejected | archived
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
  owner: meta_strategy
  validator: meta_detective
  overlap_check:
  review_due:
```

## Pending entries

```yaml
learning_entry:
  id: candidate_meta_strategy_sub_lane_pack_v0
  status: strong_candidate
  source_ref:
    - docs/working/META_STRATEGY_ORIENTATION_WORKING.md
    - docs/working/META_STRATEGY_LOGIC_ARCHITECT_WORKING.md
    - docs/working/META_STRATEGY_SCENARIO_TIMING_WORKING.md
    - docs/working/META_STRATEGY_CREATIVE_REFRAMER_WORKING.md
    - docs/working/META_STRATEGY_ASSUMPTION_LEVERAGE_WORKING.md
    - docs/working/META_STRATEGY_SYNTHESIZER_WORKING.md
  summary: Candidate internal sub-lane system for Meta Strategy. The pack defines Logic Architect, Scenario & Timing Strategist, Creative Reframer, Assumption & Leverage Mapper, and Strategy Synthesizer as working sub-lanes/modes rather than permanent sub-agents. It supports bounded multi-frame triangulation, cross-frame confrontation, recommendation packets, Detective validation handoffs, and Meta Ops mission briefs.
  candidate_target: mixed_pack
  candidate_targets:
    - essence
    - best_practice
    - mistake
    - template
  evidence_refs:
    - uploaded strategy framework research set
    - uploaded logic and synthesis framework research
    - uploaded scenario, timing, and uncertainty research
    - uploaded challenge and debiasing research
    - docs/working/META_STRATEGY_ORIENTATION_WORKING.md
  scores:
    score_scale: 1-100
    EVD: 80
    IMP: 85
    RSK: 35
  owner: meta_strategy
  validator: meta_detective
  overlap_check: required before promotion; verify boundaries with meta_ops, meta_detective, prompts/workflows, AI routing, knowledge_bank, and informatics design before accepted KB promotion.
  review_due: 2026-07-25
```

## Promotion route

1. capture candidate here
2. score `EVD` / `IMP` / `RSK` on the 1-100 handoff scale
3. route to the target file class or classes
4. validate with `meta_detective`
5. package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
6. apply only through the governed promotion path
