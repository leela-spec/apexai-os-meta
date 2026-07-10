---
title: "Skill and Agent Evolution and Learning"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "skill-agent-evolution-and-learning"
source_refs:
  - source_id: "skill-creator-skill-md"
    source_path: "raw/source-groups/_source-acquisitions/skill-best-practices-official-2026-06-23/raw/official-repos/anthropics-skills/skills/skill-creator/SKILL.md"
    source_hash: "e030e7685e26283b"
    source_pointer: "lines 8-30, high-level iterative improvement loop"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "1b61082b311fd82d"
    source_pointer: "claim B01-C008"
    source_storage_mode: "pointer_only"
created_at: "2026-07-10T21:00:00Z"
updated_at: "2026-07-10T21:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Skill and Agent Evolution and Learning

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source_id: "skill-creator-skill-md"
    rationale: "The only source in this corpus that documents skill evolution as an explicit, repeatable procedure with named steps, rather than as a general principle to keep skills up to date."
    coverage: "The full draft-eval-rewrite-repeat loop, including how to handle a user who already has a draft, and the separate description-triggering optimizer step."
  - rank: 2
    source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Independently-extracted Phase 1 claim corroborates the loop's structure from the same primary source, confirming this isn't a single-pass misreading."
    coverage: "The loop as a sequence of five named stages, cross-referenced against this KB's own claim extraction."
```

## Macro / Meso / Micro

### Macro

"Learning" for a Claude Code skill is not automatic and not implicit -- it is a named, human-in-the-loop procedure with a specific stopping condition, and the mechanism is the same whether the skill is brand new or already has a draft. The loop treats a skill the way the rest of this KB treats a wiki page: draft it, measure it against something real, and only keep the parts that survive measurement. The critical design choice is that evaluation is explicitly both qualitative (a human judging results) and quantitative (benchmarks), and a rewrite is triggered by *either* -- either the user's judgment of the results, or "glaring flaws that become apparent from the quantitative benchmarks." Neither signal alone is treated as sufficient on its own to justify skipping the other.

### Meso

The loop has five stages, and where a user enters the loop depends on what they already have: capture intent and rough approach, write a draft, create a few test prompts and run them with and without the skill active, evaluate qualitatively and quantitatively, then rewrite based on that feedback and repeat until satisfied -- followed by a separate final stage, expanding the test set and trying again at larger scale, which is explicitly a distinct step from the per-iteration loop rather than folded into it. A user who already has a draft skips straight to the eval/iterate portion rather than restarting from intent-capture, and a user who explicitly doesn't want to run evaluations can be accommodated by skipping benchmarking entirely -- the loop's stages are named as a default sequence, not a mandatory gate at every stage.

### Micro

Two structural details make this evolution loop enforceable rather than aspirational. First, evaluation runs are organized by iteration on disk (`iteration-1/`, `iteration-2/`, ...) with both the with-skill and baseline (without-skill) runs spawned in the same turn for each test case -- so a benchmark comparison is always against a same-turn baseline, not a stale one from an earlier session. Second, skill-description optimization is treated as a separate, optional final stage from content iteration: "after the skill is done... you can also run the skill description improver... to optimize the triggering of the skill" -- i.e. whether a skill's *content* is good and whether a skill's *description* reliably triggers it are two distinct things this KB's own quality contract doesn't yet separate for wiki pages, but the skill-creator process does separate for skills.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Skill evolution is a five-stage default loop: capture intent, write a draft, create test prompts and run with/without the skill, evaluate qualitatively and quantitatively, then rewrite and repeat -- followed by a distinct final stage of expanding the test set and retrying at larger scale."
    source_pointer: "skill-creator/SKILL.md lines 10-20"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "A rewrite is triggered by either qualitative user judgment of results or quantitative benchmark flaws -- neither signal is treated as sufficient alone, and both are checked before revising."
    source_pointer: "skill-creator/SKILL.md line 18"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Evaluation runs must spawn both the with-skill and baseline (without-skill) test in the same turn per test case, so every benchmark comparison is against a fresh same-turn baseline rather than a result from an earlier iteration or session."
    source_pointer: "skill-creator/SKILL.md lines 163-180"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Optimizing a skill's description (so it triggers reliably) is treated as a separate, later, optional stage from iterating on the skill's actual content -- the two are not folded into one evaluation step."
    source_pointer: "skill-creator/SKILL.md line 28"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "How is a Claude Code skill supposed to actually improve over time, and who decides when it's good enough?"
    leads_to: "wiki/summaries/skill-agent-evolution-and-learning.md"
    rationale: "Gives the named five-stage loop and its explicit stopping condition, not a general claim that skills should be iterated on."
  - question: "What's the difference between a skill not working because its content is wrong versus because it isn't triggering?"
    leads_to: "wiki/summaries/skill-agent-evolution-and-learning.md"
    rationale: "The source treats content iteration and description-trigger optimization as two distinct, separately-run stages."
  - related_page: "wiki/concepts/agent-learning-queue-candidate-only.md"
    relation: "Covers candidate-status learning items generally; this page covers the specific, named skill-evolution procedure one primary source documents."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The loop is documented for skills specifically (via the skill-creator tool); it is not verified in this bounded source set whether persistent agents or subagent definitions follow an equivalent named evolution procedure, or rely on a different, undocumented mechanism."
    proposed_handling: "revisit_source"
  - id: U002
    description: "This KB's own Phase 2 compile process does not currently apply an equivalent same-turn with/without-skill baseline comparison to itself when evaluating whether a redesigned page contract actually improves outcomes -- the parallel to this session's own quality-gate work is noted but not resolved here."
    proposed_handling: "audit_item"
