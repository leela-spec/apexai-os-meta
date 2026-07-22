# Phase 0 navigation report

Run: `run-20260722T183018661588Z-03d9cf49be`

## Corpus accountability

- Every discovered file is represented in `source-inventory.ndjson`: **10** files.
- Explicitly excluded: **0**.
- Included but extraction-blocked/metadata-only: **0**.
- Exact duplicate groups: **0**.
- Normalized-text duplicate groups: **0**.
- Possible filename/version families: **0**.
- Topic candidate JSON sets are exhaustive and never top-N truncated.
- Configured path hints are inspectable routing evidence only; they do not establish semantic authority.

## Extraction blockers

- None

## Duplicate and version families

### Exact

- None

### Normalized

- None

### Filename/version

- None

## Cross-topic reusable sources

- `apex-meta/kb/therapy/raw/notes/Anamesebogen.md` — topics: framework-integration, narm-model-and-core-needs, narm-personal-match-map, personal-pattern-map
- `apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md` — topics: framework-integration, methods-and-development-operating-system, narm-model-and-core-needs, narm-personal-match-map
- `apex-meta/kb/therapy/raw/notes/ManifestationHowTo.md` — topics: framework-integration, methods-and-development-operating-system, narm-model-and-core-needs, narm-personal-match-map
- `apex-meta/kb/therapy/raw/notes/MyTherapy.md` — topics: framework-integration, methods-and-development-operating-system, narm-model-and-core-needs, narm-personal-match-map, personal-pattern-map
- `apex-meta/kb/therapy/raw/notes/Notion_Surrender_Page.md` — topics: framework-integration, methods-and-development-operating-system, narm-model-and-core-needs, narm-personal-match-map, personal-pattern-map
- `apex-meta/kb/therapy/raw/notes/Psychological_Handover_Medical_Grade_v1.md` — topics: framework-integration, methods-and-development-operating-system, narm-model-and-core-needs, narm-personal-match-map, personal-pattern-map
- `apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md` — topics: framework-integration, methods-and-development-operating-system, narm-model-and-core-needs, narm-personal-match-map, personal-pattern-map
- `apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md` — topics: framework-integration, methods-and-development-operating-system, narm-personal-match-map, personal-pattern-map
- `apex-meta/kb/therapy/raw/notes/shadow_insight_v2.md` — topics: narm-model-and-core-needs, narm-personal-match-map, personal-pattern-map
- `apex-meta/kb/therapy/raw/notes/shadow_insight_v3.md` — topics: methods-and-development-operating-system, narm-model-and-core-needs, narm-personal-match-map, personal-pattern-map

## Topic routes

### NARM Model, Core Needs, Survival Adaptations, and Therapeutic Principles (`narm-model-and-core-needs`)

- Candidates: **9** — core 1, contextual 6, incidental 2, blocked 0.
- Suppressed ambiguous-only matches: **0**.
- Authoritative map: `manifests/phase0/topic-maps/narm-model-and-core-needs.json`
- Compact route: `manifests/phase0/topic-maps/narm-model-and-core-needs.md`
- Read-first families:
  - `apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md` — core, score 1216, family members 1
  - `apex-meta/kb/therapy/raw/notes/Psychological_Handover_Medical_Grade_v1.md` — contextual, score 154, family members 1
  - `apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md` — contextual, score 122, family members 1
  - `apex-meta/kb/therapy/raw/notes/MyTherapy.md` — contextual, score 110, family members 1
  - `apex-meta/kb/therapy/raw/notes/Notion_Surrender_Page.md` — contextual, score 104, family members 1
  - `apex-meta/kb/therapy/raw/notes/Anamesebogen.md` — contextual, score 98, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v2.md` — contextual, score 66, family members 1
  - `apex-meta/kb/therapy/raw/notes/ManifestationHowTo.md` — incidental, score 72, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v3.md` — incidental, score 63, family members 1
- Recommended semantic batches:
  - Core full reads: 1
  - Contextual targeted reads: 6
  - Incidental disposition checks: 2
  - Blocked/unreadable review: 0

### Personal Pattern Map, Strengths, Constraints, and Documented Observations (`personal-pattern-map`)

- Candidates: **8** — core 3, contextual 4, incidental 1, blocked 0.
- Suppressed ambiguous-only matches: **2**.
- Authoritative map: `manifests/phase0/topic-maps/personal-pattern-map.json`
- Compact route: `manifests/phase0/topic-maps/personal-pattern-map.md`
- Read-first families:
  - `apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md` — core, score 1202, family members 1
  - `apex-meta/kb/therapy/raw/notes/MyTherapy.md` — core, score 1004, family members 1
  - `apex-meta/kb/therapy/raw/notes/Psychological_Handover_Medical_Grade_v1.md` — core, score 535, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md` — contextual, score 381, family members 1
  - `apex-meta/kb/therapy/raw/notes/Anamesebogen.md` — contextual, score 155, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v3.md` — contextual, score 84, family members 1
  - `apex-meta/kb/therapy/raw/notes/Notion_Surrender_Page.md` — contextual, score 80, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v2.md` — incidental, score 63, family members 1
- Recommended semantic batches:
  - Core full reads: 3
  - Contextual targeted reads: 4
  - Incidental disposition checks: 1
  - Blocked/unreadable review: 0

### NARM-to-Personal Pattern Match Map (`narm-personal-match-map`)

- Candidates: **10** — core 0, contextual 8, incidental 2, blocked 0.
- Suppressed ambiguous-only matches: **0**.
- Authoritative map: `manifests/phase0/topic-maps/narm-personal-match-map.json`
- Compact route: `manifests/phase0/topic-maps/narm-personal-match-map.md`
- Read-first families:
  - `apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md` — contextual, score 338, family members 1
  - `apex-meta/kb/therapy/raw/notes/MyTherapy.md` — contextual, score 332, family members 1
  - `apex-meta/kb/therapy/raw/notes/Psychological_Handover_Medical_Grade_v1.md` — contextual, score 193, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md` — contextual, score 135, family members 1
  - `apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md` — contextual, score 113, family members 1
  - `apex-meta/kb/therapy/raw/notes/Anamesebogen.md` — contextual, score 86, family members 1
  - `apex-meta/kb/therapy/raw/notes/Notion_Surrender_Page.md` — contextual, score 77, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v2.md` — contextual, score 66, family members 1
  - `apex-meta/kb/therapy/raw/notes/ManifestationHowTo.md` — incidental, score 72, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v3.md` — incidental, score 63, family members 1
- Recommended semantic batches:
  - Core full reads: 0
  - Contextual targeted reads: 8
  - Incidental disposition checks: 2
  - Blocked/unreadable review: 0

### NARM, Jungian, Surrender, Hawkins, ACIM, and Practical-Method Integration (`framework-integration`)

- Candidates: **8** — core 5, contextual 3, incidental 0, blocked 0.
- Suppressed ambiguous-only matches: **0**.
- Authoritative map: `manifests/phase0/topic-maps/framework-integration.json`
- Compact route: `manifests/phase0/topic-maps/framework-integration.md`
- Read-first families:
  - `apex-meta/kb/therapy/raw/notes/Notion_Surrender_Page.md` — core, score 1213, family members 1
  - `apex-meta/kb/therapy/raw/notes/MyTherapy.md` — core, score 1077, family members 1
  - `apex-meta/kb/therapy/raw/notes/Psychological_Handover_Medical_Grade_v1.md` — core, score 667, family members 1
  - `apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md` — core, score 518, family members 1
  - `apex-meta/kb/therapy/raw/notes/ManifestationHowTo.md` — core, score 276, family members 1
  - `apex-meta/kb/therapy/raw/notes/Anamesebogen.md` — contextual, score 161, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md` — contextual, score 153, family members 1
  - `apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md` — contextual, score 152, family members 1
- Recommended semantic batches:
  - Core full reads: 5
  - Contextual targeted reads: 3
  - Incidental disposition checks: 0
  - Blocked/unreadable review: 0

### High-Impact Methods, Emotional Protocols, and Personal Development Operating System (`methods-and-development-operating-system`)

- Candidates: **8** — core 0, contextual 6, incidental 2, blocked 0.
- Suppressed ambiguous-only matches: **0**.
- Authoritative map: `manifests/phase0/topic-maps/methods-and-development-operating-system.json`
- Compact route: `manifests/phase0/topic-maps/methods-and-development-operating-system.md`
- Read-first families:
  - `apex-meta/kb/therapy/raw/notes/ET-Heller-NARM.md` — contextual, score 221, family members 1
  - `apex-meta/kb/therapy/raw/notes/Psychological_Handover_Medical_Grade_v1.md` — contextual, score 142, family members 1
  - `apex-meta/kb/therapy/raw/notes/PsychologicalHandover_ChatTherapeuticFramework_inACIM.md` — contextual, score 116, family members 1
  - `apex-meta/kb/therapy/raw/notes/ManifestationHowTo.md` — contextual, score 99, family members 1
  - `apex-meta/kb/therapy/raw/notes/MyTherapy.md` — contextual, score 92, family members 1
  - `apex-meta/kb/therapy/raw/notes/Notion_Surrender_Page.md` — contextual, score 80, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v1.md` — incidental, score 66, family members 1
  - `apex-meta/kb/therapy/raw/notes/shadow_insight_v3.md` — incidental, score 63, family members 1
- Recommended semantic batches:
  - Core full reads: 0
  - Contextual targeted reads: 6
  - Incidental disposition checks: 2
  - Blocked/unreadable review: 0

## Unresolved deterministic ambiguities

Ambiguous-only matches are preserved in each JSON topic map under `suppressed_ambiguous_matches`; they are not silently promoted to semantic workload.

## Semantic handoff rule

Phase 0 rank is navigation evidence, not semantic authority. Every candidate must receive a durable semantic disposition in Phase 1. Unopened sources may not be represented as evidence.
