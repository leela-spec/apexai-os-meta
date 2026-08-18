# Transcript Semantic Prompt Templates

## Contents

1. Macro
2. Meso
3. Micro
4. External verification pass
5. Self-review

These are prompt fragments for a semantic worker. The deterministic parser must not execute them as if semantic output were mechanically derivable.

## Macro

**Goal:** Build the global orientation layer from completed Meso modules, not by rereading the full transcript by default.

Produce Markdown with:

```markdown
# [[<Session Topic>]] — Macro

## Core Thesis
<one precise paragraph>

## Global Takeaways
- <3-5 high-impact conclusions, each with source-module/segment anchors>

## Taxonomy
- [[Topic]] — <role in session>
- [[Entity]] — <role in session>

## Speaker / Context Profile
- <only transcript-supported or externally verified context>

## Contradictions / Uncertainty
- <tensions, unresolved questions, and raw-source reopen triggers>

## Next Reads
- [[Meso Module A]]
- [[Meso Module B]]
```

Rules:
- Keep the main synthesis under 500 words unless the task packet requires otherwise.
- Preserve uncertainty and opposing positions.
- Do not add credentials, motives, or bias claims that the evidence does not support.
- Cite segment IDs for load-bearing synthesis claims.
- Use CoD-style density only as a revision heuristic: increase useful entities/details without sacrificing readability or faithfulness. Do not run repeated density passes by default.

## Meso

**Goal:** Convert one bounded transcript chunk into self-contained thematic knowledge modules.

For each real theme, produce:

```markdown
# [[<Module Title>]]

**Transcript range:** <start-end or unavailable>
**Source segments:** `seg-000001` … `seg-000042`

## Why This Matters
<short orientation>

## Mechanism / Argument
- <premise, causal relation, conceptual structure, or mechanism> `[seg-...]`

## Protocol / Process
1. <step only if source actually describes a process> `[seg-...]`

## Caveats / Counterarguments
- <scope limit, uncertainty, exception, disagreement> `[seg-...]`

## Related
- [[Topic]]
- [[Entity]]
- [[Claim-...]]
```

Rules:
- Treat deterministic chunk boundaries as context windows, not chapter truth.
- Merge duplicate themes across overlapping chunks during compilation.
- Preserve contradictory claims as separate claims with separate anchors.
- Do not invent steps to force narrative material into a protocol.

## Micro

**Goal:** Extract forensic, atomic propositions with exact transcript grounding.

For each candidate:

```markdown
# [[Claim-<stable-id>]]

**Proposition:** <single falsifiable claim>
**Status:** [UNVERIFIED]
**Speaker:** <label or unknown>
**Anchor:** `seg-000123` · <HH:MM:SS.mmm or timing unavailable>
**Exact quote:** “<verbatim source text>”
**Speaker posture:** <fact / cited research / hypothesis / anecdote / estimate / opinion, only when source supports this classification>

## Verification request
**Question:** <narrow question that would confirm or refute the proposition>
**Preferred evidence:** <official data / primary paper / specification / etc.>

## External evidence
- <empty until live verification actually runs>

## Context
<necessary nuance, including conditions or counter-evidence>

## Links
- [[Topic]]
- [[Entity]]
```

Rules:
- Atomic means one proposition that can independently be true or false.
- The quote must be copied exactly from the prepared transcript; never back-fill a quote from memory.
- Use word timing from `transcript.json` when available; otherwise segment timing.
- Advice, value judgments, predictions, and personal preference are not factual claims; classify them `[OPINION]` or omit from factual verification.
- Keep `[UNVERIFIED]` until evidence exists.

## External verification pass

For each `[UNVERIFIED]` factual claim:
1. search the exact proposition plus decisive entities/quantities;
2. prioritize primary sources;
3. collect evidence for and against;
4. set `[CONFIRMED]`, `[CONTRADICTED]`, `[MIXED]`, or keep `[UNVERIFIED]`;
5. record citation metadata and added context;
6. never alter the original transcript quote or anchor.

Do not browse for every sentence. Verify only testable claims whose truth matters to downstream use.

## Self-review

Before accepting generated knowledge, check:
- every Macro takeaway traces to Meso/source evidence;
- every Meso mechanism has at least one segment anchor;
- every Micro quote is exact and anchor-valid;
- overlapping chunks did not create duplicate claim notes;
- contradictions remain visible;
- no external verification status lacks external evidence;
- wikilinks are meaningful concepts/entities/claims, not decorative tags.
