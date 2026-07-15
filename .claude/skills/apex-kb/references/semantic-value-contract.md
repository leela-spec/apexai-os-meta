# Semantic Value Contract

## Completion target

Compiled pages are complete only when a future AI can answer every locked critical and routine target query from compiled pages and precise source pointers without reopening a known readable canonical source for routine work. `compiled_minimal` means the minimum useful page topology; it never means shallow content.

Phase 0 rankings are navigation candidates. Rank, hit count, filename, and prior summaries do not prove authority, complete reading, material use, or topic coverage.

## Truthful states

| State | Meaning |
|---|---|
| `analysis_complete_unvalidated` | Required Phase 1 analyses exist, but Phase 2 semantic acceptance is absent. |
| `partial` | A material query, evidence, page-architecture, candidate-disposition, or acceptance gap remains. |
| `compiled_unvalidated` | Every critical and routine query has an accepted compiled route and sampled material claims are supported; deterministic postflight has not completed. |
| `query_ready` | Semantic acceptance passes, deterministic postflight passes, and retrieval is fresh. |

Connector cost, source length, context pressure, or write friction may force `partial`; they never lower these gates.

## Topic-lock mismatch is not a source-access blocker

Before writing any audit item that claims "no local source establishes this subject," validate that claim against the KB's own scope evidence: run `topic-sanity-check` (or its manual equivalent) and record the result. A literal keyword search returning zero hits is not sufficient on its own - a topic derived from a misreading of the operator's request will also return zero hits for its own (wrong) vocabulary, and that is a topic-lock error, not proof the subject lacks material. Do not check a freshly-scaffolded KB's own `kb-schema.md` or `README.md` for corroboration: those are written by the same step that locked the topic, so they confirm nothing independently. If the topic's strong terms (phrases/aliases) have zero correspondence to the KB's own path, sibling topics, and a light filename sample, stop and get the operator to confirm the intended subject before writing a blocker audit item, before scaffold/source-intake/Phase 0, and before any commit or push. See the `topic_vocabulary_mismatches_kb_scope_evidence` failure-behavior entry in `SKILL.md`.

## Topic registry v2

Each compiled in-scope topic requires `target_queries`:

```yaml
target_queries:
  - query_id: "<stable-topic-query-id>"
    question: "<question future AIs must answer>"
    priority: "critical | routine | supporting"
    answer_requirements: []
    expected_page: "wiki/<type>/<slug>.md"
```

Query count is adaptive. Broad topics cover definitions, structure, workflow, ownership, rules, relationships, present versus proposed state, examples, and edge cases where material. `source_only` and early `analysis_only` may omit queries. A compiled topic may be `complete` only when every critical and routine query has an existing accepted page route.

Optional vocabulary sharpens deterministic routing without changing semantic authority: `phrases`/`aliases` are strong signals (a filename/H1/heading match on one of these is never suppressed); `supporting_terms` are weaker single-term signals (legacy `keywords` are read as `supporting_terms` when `phrases`/`aliases` are absent); `negative_terms` suppress a body-only match only; `ambiguous_terms` require co-occurrence with another configured term to count as a strong body signal.

## Phase 0 funnel and the topic work pack

Phase 0 is a progressive funnel, not a single ranking step. Each layer reduces what the next layer
must handle, so that only a concentrated tip is ever semantic-review input:

1. **Per-file facts** (`heading-map.json`, `source-facts.json`) -- headings, section spans, size,
   hash, and (where available) freshness and duplicate/version-family membership. Free; every file
   is inventoried, including non-text/unreadable ones.
2. **Ranked routing** (`topic-source-rankings.json`) -- an *exhaustive*, field-separated ranking per
   topic: `filename > h1 > heading > body_strong > body_weak` tiers, each candidate carrying an
   inspectable `why` (exactly which field/line matched) and at least one pointer. There is no top-N
   truncation here: a real corpus with more than 30 signal-bearing files for one topic keeps all of
   them, each with a reason. Rankings remain navigation candidates only, exactly as above -- rank
   never proves authority, complete reading, or material use.
3. **Concentration into a work pack** (`work-packs/<topic-slug>.md`/`.json`) -- the filename/H1/
   heading tiers in full, plus an elbow cut (natural score gap, never a fixed count) on the body
   tiers, with duplicates collapsed to one representative. Everything not concentrated remains
   visible in `held_in_custody` (signal-bearing, not sent) and `zero_signal_custody` (no signal) --
   nothing is deleted or hidden, only deferred.

The semantic step's default input is the topic's work pack, not the full ranking map and never the
raw corpus. Its stop condition is unchanged from the existing rule below: continue reading while a
known readable canonical source (starting with `held_in_custody`, in tier order) could resolve an
unresolved critical or routine target query; stop once every critical/routine query is resolved or
no further readable source remains. The count of files read is never a completion criterion in
either direction -- reading is gated by unresolved questions, not by a target number of sources.

## Semantic run ledger

Maintain one JSON ledger per topic at `log/semantic-runs/<run-id>/topics/<topic-slug>.json`, conforming to `semantic-run-ledger.schema.json`. Record target-query status; each candidate's Phase 0 rank, duplicate state, authority, availability, read status, passages reviewed, analysis reference, supported queries, claim/page use, and next action; page-topology decisions; every concept/entity disposition; and completion blockers.

`read_status` is `complete`, `targeted`, `blocked`, or `unopened`. Targeted reading is valid only when the relevant sections and remaining query coverage are explicit. An unopened source never appears as evidence. A known readable canonical source that could answer a critical or routine unresolved query is a continuation condition and blocks completion.

## Phase 1 and Phase 2 traceability

Phase 1 is topic-scoped: one file per registry topic (`ingest-analysis/<topic-slug>.analysis.md`),
carrying every source accepted for that topic, not one file per source. This file has exactly
one reader class -- the Phase 2 synthesis LLM and the operator during review -- no deterministic
tool parses its body, so it is structured for LLM synthesis and provenance fidelity (a ranked
Source Inventory, per-source YAML records, a Cross-Source Synthesis Notes block positioned last
in the file for end-of-context weight, and deduplicated Concept/Entity Candidate Shortlists),
never for a machine parser.

Phase 1 records which target queries the source answers, partially answers, contradicts, blocks, or does not cover, plus additional evidence required and the source's topic completion effect (`supports`, `partial`, or `blocks`). Every key claim carries a `state: present | proposed | open` tag. Every concept/entity candidate receives exactly one disposition: `promote`, `embed_in_summary`, `defer_blocked`, or `reject_no_independent_value`, with rationale, affected query IDs, and destination when applicable.

### Phase 1 -> Phase 2 orchestration contract

Phase 1 collapses N sources into one topic; Phase 2 must preserve provenance without
re-ingesting source files. What Phase 1 must carry so Phase 2 synthesis is faithful and cheap:

- Claim IDs (`C001`, `C002`, ...) scoped per source within the topic, each with a `state` tag --
  Phase 2 inherits `state` unchanged into its Key Claims, never re-derives it.
- The Concept/Entity Candidate Shortlist tables -- Phase 2 copies `concept_slug`/`entity_slug`
  values directly into `related_concepts`/`related_entities` frontmatter, zero inference cost.
- The Cross-Source Synthesis Notes -- the Phase 2 LLM reads this first to resolve conflicts
  before drafting Macro/Meso/Micro; it is not copied verbatim.
- Per-source hash/pointer -- Phase 2 `source_refs` stays in object form (`source_id`,
  `source_path`, `source_hash`, `source_pointer`) with an added `claims:` sub-key listing that
  source's claim IDs. Never flatten `source_refs` to bare strings; that discards the hash.

What Phase 1 must not carry, to prevent duplication in Phase 2: full source text or excerpts
(already in the raw source), Phase 2 narrative prose (the Phase 2 LLM generates it from the
synthesis notes), or retrieval/index metadata (Phase 2 only).

V2 summary, concept, and entity pages declare `semantic_contract_version`, `semantic_run_id`, and `target_query_ids`. Their `Target Questions Answered` section gives direct answer routes. Their Adaptive Ranked Source Set contains only sources actually reviewed and materially used, with analysis references, supported query IDs, claim IDs, rationale, and coverage. Unread candidates stay only in the ledger.

### Macro / Meso / Micro definition

Each layer is a distinct scale, not a restatement, and must be a complete standalone thought at
that scale (target 3-5 sentences; a 20-word floor per layer applies on v2 pages):

- **Macro -- Why.** The architectural context the subject lives in, the problem it solves, and
  the design decision/value gained.
- **Meso -- What it is.** The feature/service/screen/model itself: components, internal
  structure, data shape, connections to peer concepts.
- **Micro -- How.** The concrete execution path -- trigger, ordered steps, outcome, key error
  paths or preconditions -- with one inline flow chain (e.g. `Trigger -> StepA -> StepB ->
  Outcome`) folded in rather than given its own heading.

### Connection Map

An optional `## Connection Map` section (directional edges to peer summary pages: `direction`,
`peer`, `what_flows`, `contract`) may follow Routes Here only when a topic has 3 or more edges.
Below that threshold, fold the edge(s) into Routes Here and omit the heading -- an unused
heading still costs a retrieval chunk. It is not one of the six required Phase 2 value headings
and is never required by the quality checker.

Do not duplicate frontmatter claims or source lists in prose merely to satisfy parsing. Do not use a boundary-only orientation page to satisfy a broad topic. A concept/entity page exists only when it has independent project-specific retrieval value; otherwise preserve the rejection disposition.

## Semantic acceptance

Run acceptance in a clean context that receives compiled pages, target questions, and resolved evidence passages, but not drafting rationale or self-assessment. Write one artifact per topic at `audit/semantic-acceptance/<run-id>/<topic-slug>.json`, conforming to `semantic-acceptance.schema.json`.

Page-only query results are `answerable`, `partial`, `not_answerable`, or `blocked`. Claim-entailment results are `supported`, `partially_supported`, `contradicted`, or `unresolvable`. Final verdicts are `semantic_pass`, `semantic_partial`, `semantic_fail`, or `insufficient_evidence`.

`semantic_pass` requires every critical and routine query to be answerable and every independently sampled material claim to be supported. Numeric averages, headings, file counts, word counts, source counts, and drafter self-report are not acceptance authority.
