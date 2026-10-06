# Portable Obsidian Vault Contract

Use this contract in ChatGPT Work Artifact Mode when the external `llm-wiki` skill is unavailable. The original ingest procedure remains authoritative for extraction and synthesis.

## Three Layers

1. `_raw/` stores immutable source text and supplied manifests. Do not rewrite source content.
2. The compiled wiki stores interconnected Markdown under `concepts/`, `entities/`, `skills/`, `references/`, and `synthesis/`.
3. The schema layer defines frontmatter, provenance, relationships, lifecycle, links, and validation.

The root contains `index.md`, `log.md`, and `.manifest.json`.

## Common Page Contract

```yaml
---
title: Page Title
category: concepts
tags: [domain, topic]
aliases: []
relationships:
  - target: "[[concepts/related-concept]]"
    type: extends
sources: ["[[references/source-id]]"]
summary: One or two sentences, no more than 200 characters.
provenance:
  extracted: 0.72
  inferred: 0.25
  ambiguous: 0.03
base_confidence: 0.65
lifecycle: draft
lifecycle_changed: 2026-10-03
tier: supporting
created: 2026-10-03T00:00:00Z
updated: 2026-10-03T00:00:00Z
---
```

New pages start with `lifecycle: draft`. Do not claim human review or verification.

## Concept Notes

```yaml
id: concept-slug
title: Human-readable concept title
type: concept
source_ref: "[[references/source-id]]"
```

A concept page explains the definition, mechanisms, implications, source evidence, qualifications, disagreements, open questions, and related pages. Page length follows source substance, not a fixed line quota.

## Entity Notes

```yaml
id: entity-slug
name: Entity Name
type: entity
```

Create an entity page only when the source provides reusable knowledge about the person, organization, tool, project, or formulation. Do not create mention-only stubs.

## Reference Notes

```yaml
id: ref-source-id
title: Original Source Title
type: reference
media_type: interview
duration: "03:12:21"
source_url: null
```

The reference dossier records provenance, chronological structure, a quote ledger, contradictions, source limitations, and the `ingest_audit` required for long-source processing.

## Provenance

| State | Marker | Meaning |
|---|---|---|
| Extracted | No suffix | The source explicitly supports the claim. |
| Inferred | `^[inferred]` | The workflow synthesized an implication or connection. |
| Ambiguous | `^[ambiguous]` | The source is unclear or sources disagree. |

Do not convert an inference into an extracted claim during synthesis. Provenance fractions are best-effort summaries and should total approximately `1.0`.

## Typed Relationships

Allowed relationship types:

- `extends`
- `implements`
- `contradicts`
- `derived_from`
- `uses`
- `replaces`
- `related_to`

Direction runs from the declaring page to `target`. Add a typed relationship only when its direction and type are supported. Use `related_to` or omit the entry when uncertain.

## Confidence and Lifecycle

`base_confidence` is a time-independent estimate of evidence quality and independent evidence lineages. It is not certainty.

```text
base_confidence = lineage_count_score × 0.5 + source_quality_score × 0.5
lineage_count_score = min(independent_lineages / 3, 1.0)
```

Default source-quality anchors:

| Source | Score |
|---|---:|
| Peer-reviewed or primary paper | 1.0 |
| Official source | 0.9 |
| Maintained documentation | 0.85 |
| Book or technical reference | 0.8 |
| Repository evidence | 0.75 |
| Blog | 0.55 |
| Session transcript | 0.5 |
| Forum or unknown source | 0.4 |
| Unvalidated LLM synthesis | 0.3 |

Lifecycle values are `draft`, `reviewed`, `verified`, `disputed`, and `archived`. Only a human moves a page to `reviewed`, `verified`, or `disputed`. Use `superseded_by` only for an archived page with a known replacement.

## Importance Tier

- `core`: load-bearing page with broad downstream use.
- `supporting`: normal default page.
- `peripheral`: narrow or low-connectivity page.

Tier affects maintenance priority. It does not change claim truth or provenance.

## Link Format

Artifact Mode uses Obsidian wikilinks:

```markdown
[[concepts/page-name]]
[[entities/entity-name|Display label]]
```

Every link target must exist in the artifact. Prefer reciprocal links when they help navigation. Do not create empty target pages to satisfy link checks.

## Special Files

- `index.md` catalogs every compiled page and includes the Mermaid system map.
- `log.md` records the ingest operation and its outcome.
- `.manifest.json` records source hashes, produced pages, counts, warnings, and coverage status.
- `_raw/` contains source text plus any deterministic input manifest. It excludes audio and video binaries.

## Artifact Completion

Before packaging:

- apply the long-source completion gate when triggered;
- verify frontmatter and source attribution;
- verify every wikilink target;
- preserve contradictions and provenance markers;
- ensure the index references every compiled page;
- ensure packaging only collects files and does not alter their contents.
