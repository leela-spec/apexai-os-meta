# Apex KB Wiki Page Templates v3

Phase 2 creates only pages named by the generated instruction file. The standard output for one primary topic is a concept dossier plus a source atlas.

## Shared frontmatter

```yaml
title: "<title>"
page_type: dossier | source_atlas | concept | entity
kb_slug: "<kb-slug>"
topic_id: "<topic-id>"
semantic_contract_version: "3"
semantic_run_id: "<run-id>"
config_hash: "sha256:<64-hex>"
target_query_ids: []
source_refs:
  - source_id: "<id>"
    source_path: "<path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<pointer>"
    claims: []
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: high | medium | low | mixed | unknown
status: active | needs_review | partial | superseded
```

## Topic dossier — `wiki/summaries/<topic-id>.md`

```markdown
---
<shared frontmatter with page_type: dossier>
---

# <Topic Name>

## Direct Answers

| query_id | direct answer | route/evidence |
|---|---|---|
| `<id>` | `<answer sufficient for future retrieval>` | `<section and source pointers>` |

## Macro — Why

<Architectural context, problem, value, and important design choice.>

## Meso — What It Is

<Components, internal structure, boundaries, data shape, and peer relationships.>

## Micro — How It Works

<Trigger, ordered steps, outcomes, preconditions, and error paths. Include one inline flow chain.>

## Current / Proposed / Open

| item | state | explanation | evidence |
|---|---|---|---|
| `<claim or design>` | present / proposed / open | `<meaning>` | `<claim IDs/pointers>` |

## Operating Rules and Constraints

- <rule with claim/source pointer>

## Relationships and Routes

| related page/concept | relationship | why a future question routes here |
|---|---|---|

## Key Claims

| claim_id | claim | state | confidence | source pointer |
|---|---|---|---|---|

## Contradictions and Uncertainty

| id | issue | affected questions | evidence | treatment |
|---|---|---|---|---|

## Source Atlas Route

See `wiki/summaries/<topic-id>-source-atlas.md` for the complete candidate landscape and individual source value.
```

## Source atlas — `wiki/summaries/<topic-id>-source-atlas.md`

```markdown
---
<shared frontmatter with page_type: source_atlas>
---

# <Topic Name> — Source Atlas

## Coverage Summary

- Total Phase 0 candidates:
- Reviewed completely:
- Reviewed selectively:
- Duplicates collapsed:
- Historical/prototype/contextual:
- Blocked/unreadable:
- Irrelevant after review:

## Candidate Landscape

| source_id | path | why surfaced | read status | disposition | individual content snapshot | individual value | authority/freshness | duplicate/version/supersession | relevant pointers | questions supported |
|---|---|---|---|---|---|---|---|---|---|---|

Every Phase 0 candidate appears exactly once. Unopened files are custody records, never evidence.

## Read Order for Future Maintenance

1. <current/core sources>
2. <implementation sources>
3. <historical/prototype sources>
4. <contextual sources>

## Contradiction and Version Map

| subject | current candidate | alternatives | resolution or uncertainty | evidence |
|---|---|---|---|---|

## Blocked and Unreadable Sources

| source_id | path | reason | what would unlock it | possible impact |
|---|---|---|---|---|
```

## Optional concept/entity pages

Create only when the Phase 1 file and generated Phase 2 instructions explicitly approve the path because it answers an independent recurring question. Use the dossier sections relevant to that narrower subject and retain the same claim/source contracts.
