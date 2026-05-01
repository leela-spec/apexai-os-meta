# BEST_PRACTICES

## Purpose

Accepted validated practices for Meta Strategy.

## Entry schema

```yaml
practice_entry:
  id:
  status: accepted | deprecated
  practice:
  context_conditions:
  evidence_refs:
  scores:
    score_scale: 1-100
    EVD:
    IMP:
    RSK:
  owner: meta_strategy
  validator: meta_detective
  review_due:
```

## Score convention

All `EVD` / `IMP` / `RSK` scores use the active 1-100 scale. No 1-5 metric scale is used in this KB.

## Accepted practices

```yaml
practice_entry:
  id: MSTR-BP-001
  status: accepted
  practice: Use the five internal Meta Strategy sub-lanes as reasoning modes before high-impact recommendations when one frame would be too narrow.
  context_conditions:
    - more than one viable path exists
    - timing, leverage, risk, or reversibility materially affects the decision
    - the recommendation could drift if produced from only one strategy frame
  evidence_refs:
    - docs/working/META_STRATEGY_ORIENTATION_WORKING.md
    - managed/agent_kb/meta_strategy/LEARNING_QUEUE.md
  scores:
    score_scale: 1-100
    EVD: 80
    IMP: 88
    RSK: 30
  owner: meta_strategy
  validator: meta_detective
  review_due: 2026-07-25
```

```yaml
practice_entry:
  id: MSTR-BP-002
  status: accepted
  practice: Keep the five Meta Strategy sub-lanes as internal modes, not separate agents, until governed promotion criteria prove recurring independent need.
  context_conditions:
    - a prompt or workflow tries to create separate Meta Strategy sub-agents
    - a strategy task benefits from specialist reasoning but not from separate activation, KB roots, or handoff ownership
  evidence_refs:
    - docs/working/META_STRATEGY_ORIENTATION_WORKING.md
    - managed/agent_kb/meta_strategy/ESSENCE.md
  scores:
    score_scale: 1-100
    EVD: 85
    IMP: 90
    RSK: 20
  owner: meta_strategy
  validator: meta_detective
  review_due: 2026-07-25
```

```yaml
practice_entry:
  id: MSTR-BP-003
  status: accepted
  practice: Confront sub-lane outputs instead of averaging them; record agreements, conflicts, missing details, and surviving synthesis.
  context_conditions:
    - multiple strategy frames produce different conclusions
    - creative reframing expands options beyond the original logic tree
    - scenario/timing analysis conflicts with leverage or assumption mapping
  evidence_refs:
    - docs/working/META_STRATEGY_ORIENTATION_WORKING.md
    - docs/working/META_STRATEGY_SYNTHESIZER_WORKING.md
  scores:
    score_scale: 1-100
    EVD: 80
    IMP: 92
    RSK: 25
  owner: meta_strategy
  validator: meta_detective
  review_due: 2026-07-25
```

## Internal sub-lane index

| Sub-lane | Working source | Use when | Main output | Boundary guardrail |
|---|---|---|---|---|
| Logic Architect | `docs/working/META_STRATEGY_LOGIC_ARCHITECT_WORKING.md` | the problem structure is unclear, overlapping, or logically fragile | issue tree, claim/evidence/assumption map, logic gaps | structures reasoning; does not validate facts or execute |
| Scenario & Timing Strategist | `docs/working/META_STRATEGY_SCENARIO_TIMING_WORKING.md` | uncertainty, timing, reversibility, or act/wait/stage choice is central | scenario comparison, timing pressure, reversibility notes | recommends timing logic; does not assign work |
| Creative Reframer | `docs/working/META_STRATEGY_CREATIVE_REFRAMER_WORKING.md` | the option space is too narrow or trapped in inherited framing | alternative frames, stakeholder views, option expansion | expands options; does not become final authority |
| Assumption & Leverage Mapper | `docs/working/META_STRATEGY_ASSUMPTION_LEVERAGE_WORKING.md` | assumptions, root causes, validation gates, or leverage points need surfacing | assumption ledger, leverage map, Detective challenge questions | identifies what to test; does not validate itself |
| Strategy Synthesizer | `docs/working/META_STRATEGY_SYNTHESIZER_WORKING.md` | multiple lane outputs need one decision-ready recommendation | recommendation packet, Detective handoff, Meta Ops mission brief | synthesizes and hands off; does not execute or audit |

## Prompt-flow realization

Use this flow when activating Meta Strategy for a non-trivial decision:

```text
1. Read Meta Strategy ESSENCE for boundary and sub-lane map.
2. Select the smallest useful subset of the five sub-lanes.
3. Run selected lanes as internal reasoning modes.
4. Confront outputs instead of voting or averaging.
5. Produce one recommendation packet.
6. Route weak assumptions, contradictions, or high-risk claims to Meta Detective.
7. Route accepted execution coordination to Meta Ops only after the recommendation is bounded.
8. Capture reusable improvements in LEARNING_QUEUE.md using 1-100 EVD / IMP / RSK scores.
```

## Empty-state marker or initial entries

Initial accepted Meta Strategy practices for internal sub-lane use are present. Add further entries only after validation and promotion from `LEARNING_QUEUE.md`.
