---
title: "Start Here"
purpose: "Reading order for this folder — read this file first, read the rest only in the order below."
created: 2026-07-11
---

# Start here

Six files in this folder. Read in this order — don't read all six in full before acting, most of the detail is reference material to pull up when a phase actually needs it.

```yaml
reading_order:
  1: {file: README.md, why: "operating model — what Fable/external-models/Codex each do", weight: small}
  2: {file: process-overview-and-flowchart.md, why: "the single-page plan + flowchart + sense-check", weight: small}
  3: {file: chosen-blueprint-processes.md, why: "the decided process ranking to build with", weight: small}
  4: {file: build-plan-recommendation.md, why: "the ordered phases + the worked simulation example", weight: medium}
  5: {file: fable-execution-best-practices.md, why: "detailed rules — model routing, verification, context-budget guardrails. Pull up per-section when a phase needs it, not all at once.", weight: large, read_style: reference_not_cover_to_cover}
  6: {file: process-blueprint-qa.md, why: "the reasoning trail behind #3 — background only, superseded by chosen-blueprint-processes.md as the operative decision", weight: large, read_style: skip_unless_disputing_a_decision}
```

Everything not-yet-created that this plan depends on (`decisions.md`, `user-stories.md`, `simulations/`) gets written by Fable during phases 0–3 — they don't exist yet, and that's expected, not a gap in this folder.
