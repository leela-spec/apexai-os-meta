# Transcript-to-Knowledge — Current Decision Workspace

**Status:** CURRENT DECISION WORKSPACE  
**Date:** 2026-08-20  
**Branch policy:** work directly on `main` only.  
**Purpose:** turn the failed V2.1/V3 implementation history, Deep Research, public evidence, and operator decisions into a controlled decision process before another architecture is frozen.

## 1. Target

Develop a working, repeatable pipeline that turns real video/audio/transcript input into a genuinely valuable source-specific knowledge artifact.

This workspace is **not V4** and is **not an implementation plan**. It is the place where options are compared, experiments are defined, recommendations are updated, and operator decisions are locked before implementation.

## 2. Authority order

1. Explicit current operator decisions in `02-DECISIONS.md`.
2. Current unresolved questions/tests in `05-OPEN-QUESTIONS-AND-TESTS.md`.
3. Current recommendation in `04-CURRENT-RECOMMENDATION.md`.
4. Option evidence in `03-PIPELINE-OPTIONS-MATRIX.md` and `06-SCENARIO-SIMULATIONS.md`.
5. Research sources indexed in `01-RESEARCH-SOURCE-INDEX.md`.
6. V3/V2.1 architecture documents as historical/research evidence only where not reaffirmed.

A recommendation must never silently become an operator decision.

## 3. Operating principles

- **Reuse before invention.** Existing maintained systems own capabilities first.
- **Battle-proven before AI-designed.** Do not invent a capability because an AI thinks it can.
- **Measure before remove.** A reusable candidate that plausibly adds material value gets a bounded test before rejection.
- **Product value dominates architecture elegance.** Do not optimize stage count by itself.
- **Local-first is a preference, not an absolute prohibition.** External/API use must earn its place through significant demonstrated value.
- **AI does not own deterministic workflow state.** Code/workflow runtime owns sequence, state, retry and recovery.
- **CLI autonomy is allowed only when it produces large enough value and is made reliable; avoid it by default because prior attempts repeatedly failed.**
- **Do not confuse source support with external truth.** They are separate concerns when either is in scope.
- **No new authoritative architecture until the open decision/test set is sufficiently closed.**

## 4. Read order

1. `02-DECISIONS.md`
2. `04-CURRENT-RECOMMENDATION.md`
3. `03-PIPELINE-OPTIONS-MATRIX.md`
4. `05-OPEN-QUESTIONS-AND-TESTS.md`
5. `06-SCENARIO-SIMULATIONS.md`
6. `01-RESEARCH-SOURCE-INDEX.md`
7. source captures under `sources/`
8. `07-FUTURE-DEVELOPMENT.md` only when explicitly working on deferred scope

## 5. Required separation

```text
RESEARCH
  -> OPTIONS MATRIX
  -> CURRENT RECOMMENDATION
  -> OPEN QUESTIONS / EXPERIMENTS
  -> OPERATOR DECISIONS
  -> IMPLEMENTATION PLAN
  -> IMPLEMENTATION
```

Research may change the recommendation. It does not overwrite operator decisions. Experiments may reopen decisions when their stated reversal trigger is met.

## 6. Current decision state

The operator verified the initial operating-model recommendations except for explicit corrections recorded in `02-DECISIONS.md`:

- subscription CLI agents may be autonomous (`Q5=C`), but this is high-risk and should be avoided unless there is a large value gain and a reliable implementation path;
- Macro/Meso/Micro is one possible representation, **not** a mandatory output contract;
- exact claim-to-transcript/timestamp evidence is configurable by use case, not universally mandatory;
- non-factual provenance requirements are deferred;
- visual-only video evidence is deferred to a future project;
- the synthesis comparison in Q20 is provisionally accepted but requires a clearer explanation before it is treated as fully understood;
- local Qwen experiments are mandatory work, not operator questions.

## 7. Implementation stop condition

Do not start another broad implementation pass from this workspace merely because files exist. First close the high-leverage open questions through public evidence and/or bounded real runs, then freeze a selected architecture and implementation plan.