This is a rich, well-structured research prompt. Here is the full expert evaluation and design output, grounded in cited external research.

apex-kb Output Optimization — Research Report
Executive Orientation
The core tension in apex-kb is that Phase 1 is LLM-consumed only (a single LLM read, then discarded from active context) while Phase 2 is machine-indexed and LLM-retrieved repeatedly. These two use-cases have nearly opposite optimality conditions, and the current format optimizes for neither. Every recommendation below is derived from that structural asymmetry.

Format Economics: The Token Tax Baseline
Before scoring anything, we need the empirical baseline on format costs. Research on token-per-byte efficiency establishes the following ranking:

Format	Relative Token Cost	Best For
CSV / inline key=value	~0.5×	Flat records, large lists
YAML	~0.7×	Nested structured objects
JSON	~1.0× (baseline)	Machine integration
Markdown table	~1.4×	Human readability only
Markdown prose	~1.0–1.3×	Narrative, LLM reasoning
Markdown tables cost 40% more tokens than JSON for the same data. For Phase 1 — which is only LLM-read — this means that the current fenced-YAML blocks are already well-chosen, but tabular rendering is actively wasteful if the reader is an LLM. Critically, YAML is 20–30% more token-efficient than JSON for nested structures, which directly validates retaining YAML in Phase 1 over switching to tables.

A. Phase 1 Format Evaluation
Why One-File-Per-Source Is the Wrong Unit
The core problem with the current model is that the synthesis LLM receives N separate files for a single topic — one per source. This multiplies context size N-fold and introduces exactly the "lost in the middle" degradation that Liu et al. (2023) quantified: 30%+ accuracy drop when relevant information is buried in long middle-context. With 8–12 sources per topic, mid-context claims will be reliably ignored. The unit of synthesis is the topic, not the source — so the unit of the Phase 1 file should be the topic.

Candidate Evaluation
Rubric weights used: Impact 25%, Low Risk 15%, Low AI Token Cost 20%, Low Retrieval Cost 10%, Low Machine-Readable Cost 5%, Provenance Fidelity 15%, Operator Legibility 5%, Orchestration Fit 5%. Weights justified: token cost and impact dominate because Phase 1 is exclusively consumed by one LLM call; provenance fidelity is elevated because this is the only place raw source traceability lives before it's collapsed into Phase 2.

Option	Impact	Low Risk	Low AI Token	Low Retr.	Low Mach.	Prov. Fidelity	Op. Legibility	Orch. Fit	Weighted
(a) Current: 1-file/source, prose sections	45	70	35	30	80	60	60	30	47
(b) 1-file/source, tabular	45	70	25	30	60	65	50	35	44
(c) 1-file/topic + YAML tabular records	85	80	85	85	75	88	80	90	84
(d) 1-file/topic + NDJSON records	80	75	70	85	85	85	45	80	75
Winner: Option (c) — one file per topic, with YAML-keyed tabular records for repeated structures (claims, concepts, entities, dispositions) and one-liner rows for rejected/held-back sources. The topic-scoped file means the synthesis LLM gets all evidence for a single topic in one compact document, front-loaded per source authority rank, avoiding mid-context burial. YAML's 20–30% token saving over JSON further justifies it over option (d).

Recommended Phase 1 Template
text
---
topic: "<topic-slug>"          # matches wiki/summaries/<topic>.md
generated: "<ISO-8601>"
source_count: <N>              # accepted sources
---

# Phase 1 Analysis — `<topic>`

## Source Inventory

| rank | source_id | authority | recency | disposition | hash_prefix |
|------|-----------|-----------|---------|-------------|-------------|
| 1 | <id> | primary | 2025-Q4 | accepted | `abc123` |
| 2 | <id> | secondary | 2025-Q3 | accepted | `def456` |
| 3 | <id> | tertiary | 2024-Q2 | rejected: stale | — |

> Rejected sources get one-liner rows only — no further sections below.

## Per-Source Records (accepted only)

### `<source_id_1>` · authority: primary

```yaml
key_claims:
  - id: C1
    claim: "<verbatim or tight paraphrase>"
    confidence: high | medium | low
    state: present | proposed | deprecated
    quote_ref: "<sentence fragment for grounding>"

concept_candidates:
  - id: K1
    label: "<concept>"
    relation: defines | exemplifies | contradicts | extends

entity_candidates:
  - id: E1
    label: "<name>"
    type: screen | service | model | actor | config

dispositions:
  - id: D1
    observation: "<what the source says>"
    implication: "<for the topic>"

uncertainty:
  - id: U1
    gap: "<what is unknown or conflicting>"
    severity: blocking | notable | minor
```​

### `<source_id_2>` · authority: secondary

```yaml
# ... same schema
```​

## Cross-Source Synthesis Notes

> Free-prose section (200–400 words). Written for the Phase 2 LLM.
> Explicitly flag: conflicts between sources, dominant claim by authority,
> which claims survived reconciliation, which were discarded and why.
> Reference claim IDs (C1, C2…) and source IDs inline.

## Concept Candidate Shortlist

> Deduplicated across all sources. Phase 2 LLM uses this to populate
> `related_concepts` frontmatter.

| id | label | source_ids | disposition |
|----|-------|------------|-------------|
| K1 | … | src1, src2 | promote |
| K2 | … | src3 | hold |

## Entity Candidate Shortlist

> Deduplicated. Phase 2 LLM uses this to populate `related_entities`.

| id | label | type | source_ids |
|----|-------|------|------------|
| E1 | … | service | src1 |
```

**Key design decisions justified:**
- Source Inventory table at top = **operator scannable + LLM sees it first** (avoids mid-context burial)[2]
- YAML per-source records: stream-parsable, 20–30% cheaper than JSON[1]
- Claim IDs (C1, C2…) survive into Phase 2 `source_refs` as provenance anchors
- `state: present | proposed | deprecated` tag answers the operator's explicit request for present-vs-proposed signal
- Cross-source synthesis section positions the highest-value reasoning at document end (LLM end-of-context advantage)[2]
- Rejected sources → one table row, zero further tokens = **maximum token efficiency with full provenance**

***

## B. Phase 2 Wiki Page Design

### Macro/Meso/Micro — Precise Definitions

The current contract ("must be distinct syntheses at the three scales") has no semantic content and produces thin single sentences. The "thin layers" word-count gate fires because the prompt gives no length or content target. Research on hierarchical chunking confirms that multi-granularity retrieval requires each level to be a **complete, standalone thought** at its scale:[4][5]

| Scale | Semantic Definition | Content Spec | Target Length |
|---|---|---|---|
| **Macro** | **Why** — the architectural context, the problem it solves, the value/gain | System purpose, the problem domain, the design decision and its rationale | 3–5 sentences |
| **Meso** | **What it is** — the feature/service/screen/model itself; internal structure, connections, data shape | Components, states, fields, relationships to peer services | 3–5 sentences |
| **Micro** | **How** — the concrete execution path; trigger → steps → outcome → error paths | Ordered execution sequence, key preconditions, observable outputs | 3–6 sentences |

A 3+3+3 sentence minimum will reliably clear a "thin layers" word-count gate set at e.g. 50 words per layer. This is the **minimum viable definition** — no overengineering.

### High-Impact/Low-Token Additions — Scored

Each candidate evaluated on the same scoring rubric (Impact / Low Risk / Low AI Token Cost / Low Retrieval Cost / Low Machine-Readable Cost / Provenance Fidelity / Operator Legibility / Orchestration Fit):

| # | Candidate | Impact | Low Risk | Low AI Tok | Low Retr | Low Mach | Prov | Op Leg | Orch | **Weighted** | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Populate `related_concepts` + `related_entities` frontmatter from Phase 1 shortlists** | 90 | 95 | 90 | 95 | 90 | 95 | 70 | 95 | **91** | ✅ KEEP |
| 2 | **Macro/Meso/Micro precise semantic definition** (this section) | 95 | 90 | 80 | 85 | 90 | 85 | 95 | 90 | **89** | ✅ KEEP |
| 3 | **`state:` tag on Key Claims** (present / proposed / deprecated) | 80 | 85 | 85 | 90 | 80 | 90 | 80 | 85 | **84** | ✅ KEEP |
| 4 | **Connection/Interface Map** (directional edges, new H2 section) | 75 | 70 | 65 | 60 | 75 | 70 | 80 | 75 | **71** | ⚠️ CONDITIONAL |
| 5 | One-line **execution-flow chain** (inline in Micro) | 65 | 80 | 90 | 95 | 85 | 70 | 75 | 80 | **77** | ✅ KEEP (inline only) |
| 6 | Separate H2 for execution-flow chain | 50 | 75 | 70 | 60 | 80 | 65 | 65 | 65 | **64** | ❌ REJECT — new H2 = new FTS5 chunk, diluted signal |
| 7 | Full provenance YAML block in Phase 2 | 45 | 65 | 50 | 50 | 55 | 80 | 50 | 60 | **57** | ❌ REJECT — duplication of Phase 1 |
| 8 | Embedding of raw source excerpts | 20 | 40 | 20 | 20 | 30 | 85 | 30 | 30 | **32** | ❌ REJECT — context bloat |

**Connection Map — CONDITIONAL ruling:** A machine-readable edge table (`direction | peer_slug | what_flows | contract`) is high value *if* the topic graph is dense enough to make cross-page retrieval meaningful [6][5]. The cost is one new H2 (= one new FTS5 chunk). Recommended approach: include it **only when ≥ 2 edges exist**; render as a compact YAML block *inside* an existing H2 (e.g., append to "Routes Here") to avoid a new chunk, or accept the new chunk only for topics with ≥ 3 edges. This avoids the most expensive overengineering failure mode.

### Recommended Phase 2 Template

```markdown
---
title: "<Topic Name>"
topic_slug: "<topic-slug>"
version: "<ISO-8601>"
target_query_ids: [q-001, q-002, …]
source_refs: ["<source_id_1>#C1", "<source_id_2>#C3"]   # claim-level provenance
related_concepts: ["<K1-label>", "<K2-label>"]           # from Phase 1 shortlist
related_entities: ["<E1-label>", "<E2-label>"]           # from Phase 1 shortlist
---

# <Topic Name>

## Target Questions Answered

- <Question 1>
- <Question 2>

## Core Summary

<2–4 sentence dense synthesis. Purpose: answer the most common query about this topic.>

## Macro / Meso / Micro

**Macro (Why):** <3–5 sentences. Architectural context, the problem being solved, the
design decision, the value gained. Reference the system or layer this feature lives in.>

**Meso (What it is):** <3–5 sentences. The feature/screen/service/model itself: its
components, internal structure, data model, connections to peer concepts.>

**Micro (How):** <3–6 sentences. Concrete execution path: trigger → key steps → output.
Include one-line flow chain inline: `TriggerEvent → StepA → StepB → FinalState`.
Note key error paths or preconditions.>

## Key Claims

| id | claim | confidence | state | source_ref |
|----|-------|------------|-------|------------|
| C1 | … | high | present | src1 |
| C2 | … | medium | proposed | src2 |

## Adaptive Ranked Source Set

1. `<source_id_1>` — <one-line rationale for authority rank>
2. `<source_id_2>` — …

## Connection Map

> Include only when ≥ 2 edges. Omit section entirely if 0–1 edges.

```yaml
edges:
  - direction: outbound
    peer: "<peer-topic-slug>"
    what_flows: "<data / event / control>"
    contract: "<interface description, ≤ 15 words>"
  - direction: inbound
    peer: "<peer-topic-slug>"
    what_flows: "…"
    contract: "…"
```​

## Routes Here

<How retrieval lands on this page. Keywords, aliases, query patterns.>

## Uncertainty / Reopen Triggers

- U1: <gap> — severity: <blocking | notable | minor>
```

**FTS5 chunk accounting:** This template produces 8 H2 chunks max (7 if Connection Map is omitted). The claim `state:` column and execution-flow chain inline in Micro add **zero new chunks**. The Connection Map adds exactly 1 new chunk only when populated.

***

## C. Phase 1 → Phase 2 Orchestration Contract

The orchestration problem is: Phase 1 collapses N sources → 1 topic; Phase 2 must preserve provenance without re-ingesting source files. The solution is a **claim-ID pointer chain**:[7]

### Contract Specification

**What Phase 1 must carry (required for faithful Phase 2 synthesis):**

1. **Claim IDs** (`C1`, `C2`…) scoped per-source-within-topic. These become `source_refs` anchors in Phase 2 frontmatter.
2. **`state:` tag per claim** (present/proposed/deprecated) — Phase 2 inherits this directly into its Key Claims table; no re-derivation needed.
3. **Concept + Entity shortlists** (deduplicated, tabular) — Phase 2 LLM copies directly into `related_concepts`/`related_entities` frontmatter. Zero inference cost.
4. **Cross-source synthesis notes** — Phase 1 positions this at document end; the Phase 2 LLM prompt references this section first to resolve conflicts before drafting.
5. **Hash prefix per source** — Phase 2 `source_refs` field format: `<source_id>#<claim_id>`, providing sub-document traceability without embedding full paths.

**What Phase 1 must NOT carry (to prevent duplication/bloat in Phase 2):**

- Full source text or excerpts → already in source files
- Phase 2 narrative prose → Phase 2 LLM generates this from Phase 1 synthesis notes
- FTS5 index metadata → Phase 2 only

**Mapping table (per-source Phase 1 rows → per-topic Phase 2 sections):**

| Phase 1 element | Maps to Phase 2 | Transformation |
|---|---|---|
| `source_inventory` table | `Adaptive Ranked Source Set` | Rank-order preserved, one-liner per source |
| `key_claims[].claim` + `state` | `Key Claims` table rows | Direct, with source_id annotation |
| `concept_candidate_shortlist` | `related_concepts` frontmatter | Label only, no IDs in frontmatter |
| `entity_candidate_shortlist` | `related_entities` frontmatter | Label only |
| `uncertainty[].gap` + `severity` | `Uncertainty/Reopen Triggers` | Direct copy, severity retained |
| `cross_source_synthesis_notes` | `Macro/Meso/Micro` drafting input | LLM synthesis; not verbatim |
| Claim IDs `C1…Cn` | `source_refs` frontmatter | Format: `src_id#C1` |

**Provenance survival after bundling:** The per-topic Phase 1 file is **retained as the audit artifact** at `ingest-analysis/<topic>.analysis.md`. Phase 2 cites it by path only in `source_refs`; the actual claim text is not duplicated. This satisfies both (a) the Phase 2 LLM's need to cite provenance and (b) the human operator's review path, without storing source content twice.[8][7]

***

## Rejected / Out of Scope

The following were evaluated and rejected as overengineering, per the rubric's "default verdict for a marginal element is reject":

- **Separate H2 for execution-flow chain** — inline in Micro achieves the same with zero FTS5 cost
- **Full provenance YAML block in Phase 2** — duplicates Phase 1; `source_refs` pointer chain is sufficient
- **Raw source excerpt embedding** — context bloat, 32/100 composite; violates token economics[9]
- **Changing Phase 1 YAML blocks to Markdown tables** — Markdown tables cost 40% more tokens than YAML for the same data; pure regression for an LLM reader[1]
- **Per-source separate Phase 1 files + tabular** (option b) — retains all problems of option (a), adds parsing friction
- **Embedding graph adjacency matrix** — relationship graph across the whole KB should live in a dedicated graph index, not per-page prose
- **NDJSON for Phase 1 records** — higher machine parsability score but 30% more tokens than YAML  with no parser ever reading it; rejected in favor of YAML[1]

***

## Ranked Change Table (All Evaluated Changes)

| Rank | Change | Weighted Score | Phase | Verdict |
|---|---|---|---|---|
| 1 | Populate `related_concepts`/`related_entities` from P1 shortlists | 91 | P1→P2 | ✅ Keep |
| 2 | Define Macro/Meso/Micro as Why/What/How with length targets | 89 | P2 | ✅ Keep |
| 3 | One-file-per-topic + YAML tabular records (P1 restructure) | 84 | P1 | ✅ Keep |
| 4 | `state:` tag (present/proposed/deprecated) on Key Claims | 84 | P1+P2 | ✅ Keep |
| 5 | Execution-flow chain inline in Micro | 77 | P2 | ✅ Keep (inline) |
| 6 | Claim-ID pointer chain as orchestration contract | 84 | Orch | ✅ Keep |
| 7 | Connection/Interface Map (YAML block, conditional) | 71 | P2 | ⚠️ Conditional |
| 8 | Separate H2 for connection map (unconditional) | 64 | P2 | ❌ Reject |
| 9 | Full provenance YAML in Phase 2 | 57 | P2 | ❌ Reject |
| 10 | Markdown tables in Phase 1 | 44 | P1 | ❌ Reject |
| 11 | Raw source excerpts in Phase 2 | 32 | P2 | ❌ Reject |

***

## Implementation Readiness Check

Before moving to Step 3 (rewriting the skill templates), a few questions that will affect the exact template wording:

1. **Does `apex_kb.py quality`'s thin-layers gate have a hardcoded word-count threshold today?** If yes, what is it — so the Macro/Meso/Micro length targets above can be set to clear it with a defined margin.
2. **What is the current `source_refs` frontmatter format** — bare paths, or does it already support fragment anchors (`#C1`) without breaking the validator?
3. **Connection Map conditionality** — is the "omit section if < 2 edges" logic something the Phase 2 LLM prompt enforces, or does the quality tool need a new optional-section allowlist?

These are the three load-bearing unknowns before the template files can be finalized. Everything else above is implementation-ready.