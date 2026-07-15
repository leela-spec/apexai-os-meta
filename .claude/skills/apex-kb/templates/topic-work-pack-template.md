# Topic Work Pack Template

This documents the exact shape `phase0` generates at
`manifests/phase0/work-packs/<topic-slug>.md` (with a `.json` sibling conforming to
`references/topic-work-pack.schema.json`). It is a **generated, deterministic** artifact -- not a
wiki page, not hand-authored, and not tracked under `wiki/`. It is the bounded L3 input handed to
the semantic step; the semantic step must not read the full `topic-source-rankings.json` map or the
raw corpus as its starting point.

```text
# Topic Work Pack - <Topic Name>

Generated: `<UTC timestamp>`
Topic slug: `<topic-slug>`
Rankings reference: `manifests/phase0/topic-source-rankings.json`

## Target Questions

- `<query_id>` (`critical | routine | supporting`): <question text>
  - answer requirements: <answer_requirements, or "none recorded">
  - expected page: `<expected_page>`

(Repeat per registry target_queries entry. If the topic has none, state that explicitly --
compiled tiers require target queries per `references/semantic-value-contract.md`.)

## Concentrated Candidates

### Filename matches

- `<path>` (`source_id`) -- why: filename hit on "<phrase>"
  - pointers: `<field>:<line>` section `<start>-<end>`: "<snippet>"

### H1 matches

(same shape)

### Heading matches

(same shape)

### Body matches (concentrated)

(same shape; this is the elbow-cut portion of body_strong/body_weak -- not the full body-tier list)
- duplicates of this source: `<source_id>, <source_id>` (collapsed; read once)

## Continue By Gap

Read the concentrated candidates above first. Pull the next `held_in_custody` source (see the full
ranking entry for this topic in `topic-source-rankings.json`) only if a critical or routine target
question above is still unresolved after reading the concentrated set. Stop when every critical/
routine question is resolved, or no further readable source remains. Never stop merely because a
fixed number of sources was read, and never continue merely because more candidates exist.

## Disclosure

- candidate_count (exhaustive, this topic): `<n>`
- concentrated_count (in this work pack): `<n>`
- held_in_custody_count (signal-bearing, not concentrated): `<n>`
- zero_signal_custody_count (scanned, no signal): `<n>`
- full candidate set and custody paths: `manifests/phase0/topic-source-rankings.json`
```

## Rules this template encodes

- The work pack is **derived**, not authored: every fact here already exists in
  `topic-source-rankings.json` for this topic. Nothing here is a second source of truth.
- Concentration is by whole tier (filename/H1/heading always included in full) plus an elbow cut on
  the body tiers -- never a fixed count of files.
- `held_in_custody` and `zero_signal_custody` are disclosed by count, with a pointer back to the full
  set. A reader can always go verify what was left out and why; nothing is silently dropped.
- The semantic step's stop condition is continue-by-gap (an unresolved target question), never a
  source count and never "read everything in `held_in_custody` too."
