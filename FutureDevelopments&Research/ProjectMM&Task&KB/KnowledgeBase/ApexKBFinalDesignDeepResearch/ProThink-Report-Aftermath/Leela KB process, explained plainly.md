# Leela KB process, explained plainly

## Direct answers

### Are the 197 scanned sources all files selected for this run?

**Yes.** They are the complete source universe passed into this corpus-map run.

Important qualification: only **146 are text-readable sources** from which headings/text can be parsed. The remaining **51 are non-text/binary files**. They can be inventoried and hashed, but they cannot provide headings or semantic passages to this text pipeline.

### Does `source-postings.json` contain the headings for every readable file?

**Yes.** It has one record for each of the 197 sources. For a readable Markdown source it records:

- source ID;
- path;
- SHA-256 hash;
- `text_readable`;
- every Markdown heading the parser recognizes—H1 through H6—with its original line number;
- Markdown and wiki links.

For a binary/non-text source, the headings and links are empty.

Actual shortened record:

```json
{
  "source_id": "src-d63050c3fd476a1b",
  "path": "LeelaAppDevelopment/01_Features/101 - Chunks & Chunk Database.md",
  "sha256": "d63050c3fd476a1b…",
  "text_readable": true,
  "headings": [
    {"level": 2, "line": 2, "text": "0) Purpose & Scope"},
    {"level": 2, "line": 18, "text": "1) Core Concepts & Relationships"},
    {"level": 3, "line": 20, "text": "1.1 Conceptual Model"}
  ],
  "links": []
}
```

“Line 18” simply means that the heading begins on line 18 of the canonical source file. That lets a later reader jump to the correct place without copying the source.

### Why is there also a `heading-map.json`?

The honest answer is: **it substantially duplicates `source-postings.json`.**

- `source-postings.json`: 197 source records, 4,310 headings in total.
- `heading-map.json`: 146 readable-source records, the same 4,310 headings.

The heading map contains only 146 records because only those 146 sources can be parsed as text/Markdown. It adds three small facts:

- `h1_title`: the first H1, if present;
- `parser_warnings`: syntax problems noticed by the parser, such as an unclosed code fence;
- `source_type_guess`: a heuristic label such as `other`, not an authoritative classification.

Actual shortened record:

```json
{
  "path": "LeelaAppDevelopment/Upgrades/Night4/Updates new/Cross-FeatureContractsv2.md",
  "h1_title": "Cross-Feature Contracts",
  "headings": [
    {"level": 1, "line": 1, "text": "Cross-Feature Contracts"},
    {"level": 2, "line": 3, "text": "Purpose"},
    {"level": 2, "line": 7, "text": "Status"},
    {"level": 2, "line": 18, "text": "Scope"}
  ],
  "parser_warnings": [],
  "source_type_guess": "other"
}
```

The unique value is modest. These two files could be one normalized per-source structure, or the heading map could be generated on demand from postings. As currently stored, the heading information is duplicated.

## What the topic map actually means

A **candidate** is supposed to mean: “this source file may contain evidence for this topic; a semantic reviewer should consider it.”

The current code uses a much broader meaning: **every source is a candidate for every topic.**

The process is:

```text
For topic 1:
    create a candidate card for source 1
    create a candidate card for source 2
    ...through source 197

For topic 2:
    create another candidate card for source 1
    ...through source 197

Repeat for all 10 topics
```

That creates 1,970 candidate cards.

For each topic/source pair, the script checks whether one of that topic's configured terms occurs in five places:

- `path`: the complete source path;
- `filename`: only the filename;
- `heading`: the combined heading text;
- `body`: the source's full readable text;
- `link`: Markdown link text.

The body itself is **not copied into the map**. If `body` contains `skill tree`, the map records only that the term was found somewhere. It does not record every occurrence, the sentence, or the occurrence count.

Actual shortened candidate card:

```json
{
  "candidate_id": "cand-…",
  "source_id": "src-…",
  "path": "LeelaAppDevelopment/01_Features/101 Chunks & 102 Epics.md",
  "classification": "direct",
  "signal_evidence": {
    "path": [],
    "filename": [],
    "heading": ["epic"],
    "body": ["epic", "content"],
    "link": []
  },
  "content_pointer": {
    "path": "LeelaAppDevelopment/01_Features/101 Chunks & 102 Epics.md",
    "headings": [
      {"level": 1, "line": 1, "text": "101 Chunks"}
    ]
  }
}
```

`content_pointer` is not content. It is another copy of the source path plus that source's complete heading list. It is intended as a navigation aid: “open this source and look around these sections.”

There are 4,310 headings across the readable sources. The topic map embeds those same 4,310 headings once for each topic: **43,100 heading objects**. The one-topic projections repeat them again.

## Confirmed overlap

The generator has no condition that says “only append this source if it has a topic signal.” If no signal exists, the source is still appended and generally falls back to `contextual`.

Read-only measurement of zero-signal candidates:

| Topic | All candidates | Candidates with no topic signal |
|---|---:|---:|
| Epic | 197 | 44 |
| Skill Tree | 197 | 62 |
| Path | 197 | 67 |
| Sequence | 197 | 43 |
| Rhythm | 197 | 63 |
| Stats | 197 | 52 |
| Algorithm | 197 | 61 |
| Feature interconnections | 197 | 49 |
| User stories | 197 | 77 |
| Creator/Epic content | 197 | 68 |

Across the map, **586 of 1,970 candidate cards have zero configured topic signals**. The remaining signal matches are still only substring hints; a match does not prove semantic relevance.

## What the semantic ledger does

The deterministic script cannot understand product meaning. The semantic stage is supposed to open sources and decide:

- Is this source genuinely useful for the topic?
- Is it irrelevant?
- Is it an exact duplicate?
- Is it historical or superseded?
- Is it unreadable?
- If useful, what claim does it support and where is the evidence?

The topic ledger is primarily the **review receipt** for those decisions. It is not the final explanation of the topic, and it does not provide a numeric rating.

For Skill Tree, the semantic ledger recorded:

| Decision | Count | Plain meaning |
|---|---:|---|
| `material_source` | 5 | useful evidence for the final Skill Tree explanation |
| `irrelevant_after_review` | 72 | opened/reviewed, not useful for Skill Tree |
| `blocked_unreadable` | 52 | no usable text passage |
| `exact_duplicate_reused` | 43 | duplicate content; do not analyze twice |
| `historical_or_superseded` | 25 | context only, not current authority |

So the semantic system processed 197 ledger entries to retain **five** material sources.

Actual useful ledger entry:

```json
{
  "source_path": "LeelaAppDevelopment/01_Features/102 - Epics (Database + Skill Tree).md",
  "read_scope": "Full canonical source opened through GitHub connector.",
  "source_snapshot": "Directly reviewed material source supporting the Skill Tree hierarchy/state and Path-handoff questions.",
  "distinctive_value": "Direct evidence for the compiled Skill Tree dossier.",
  "evidence_pointer": "Relevant feature data-model and contract headings.",
  "analysis_ref": ".../ingest-analysis/01-features-102-epics-database-skill-tree.md",
  "disposition": "material_source"
}
```

Actual rejected entry:

```json
{
  "source_path": "LeelaAppDevelopment/Prototyp Spark/.../SCR_PlayModeSelection Nowa Prompt Flow.md",
  "source_snapshot": "Reviewed canonical source: # Nowa Prompt Flow v3 — SCR_PlayModeSelection.",
  "target_query_support": "Does not directly support a final material claim for this topic.",
  "analysis_ref": null,
  "disposition": "irrelevant_after_review"
}
```

This is real classification work, but much of the ledger is boilerplate:

- 192 records share the result “does not directly support a final material claim.”
- 140 share the same generic “reviewed for topic relevance” distinctive-value sentence.
- only 5 point to material analyses.

The ledger therefore has custody/audit value, but low information density for a browser trying to understand Skill Tree.

## Where the actual semantic value appears

The final Skill Tree dossier is the short useful product. It says:

> Skill Tree is the navigational projection between canonical content and weekly planning. It makes the Epic graph legible and selectable without changing the Epic graph.

It then records four claims, including:

```text
SKT-C001: Skill Tree is a projection and selection surface over Epic content.
Evidence: 102 - Epics (Database + Skill Tree).md, lines 202–240.

SKT-C002: Picker mode returns planning information to Path through PathAllocationDraft.
Evidence: the same source, lines 241–303.
```

That is the semantic value: a compact explanation, specific claims, and evidence pointers. The 197-row ledger explains how the system got there and what it rejected.

## Macro, meso, and micro flow

### Macro: the whole system

```text
197 selected source files
        ↓
Mechanical scan: hashes, headings, links, term presence
        ↓
Topic routing: 10 exhaustive lists of 197 source cards
        ↓
Semantic review: useful / irrelevant / duplicate / old / unreadable
        ↓
Topic ledger: receipt for all 197 decisions
        ↓
Topic dossier: short explanation and evidence-backed claims
        ↓
Acceptance: check whether required questions were actually answered
```

### Meso: responsibilities

| Stage | What it can do | What it cannot do | Primary value |
|---|---|---|---|
| Deterministic scan | exact parsing, hashing, headings, links, simple term presence | understand product meaning | reliable inventory/navigation |
| Topic map | show which configured terms occur in which structural areas | decide genuine relevance | exhaustive custody, weak routing |
| Semantic review | read meaning, compare authority, reject noise, form claims | guarantee deterministic completeness by itself | knowledge synthesis |
| Acceptance | check required questions/claims against a contract | repair content automatically in this audit | quality gate |

### Micro: one source through the pipeline

```text
Source: 102 - Epics (Database + Skill Tree).md
  ↓ deterministic parser
Finds headings such as “Skill Tree — Product Definition” and their line numbers
  ↓ topic mapper
Skill Tree terms appear in filename/headings/body → candidate marked direct
  ↓ semantic reviewer
Opens the canonical file and decides it is one of five material sources
  ↓ Phase 1 analysis
Extracts the Skill Tree role and Skill Tree-to-Path handoff
  ↓ dossier
Creates SKT-C001 and SKT-C002 with line-specific evidence
```

## Is the process “complete shit”?

Not completely. Three pieces have clear value:

1. The per-source structural inventory is useful and deterministic.
2. The semantic disposition distinguishes five useful Skill Tree sources from 192 non-material entries.
3. The final dossier contains concise, evidence-backed product claims.

The weak design is the boundary between them:

- headings are stored repeatedly;
- “candidate” means “every file,” not “plausibly relevant file”;
- the exhaustive custody artifact is also used as a semantic work queue;
- ledgers and atlasses repeat many generic sentences;
- the semantic browser is asked to handle audit evidence and knowledge synthesis together.

So the process is not valueless. It has a useful scanner and a useful final product, connected by an oversized and inefficient custody/review layer.

## H1–H5 as direct answers

| Question | Answer |
|---|---|
| H1: Are deterministic files corrupt? | **No evidence of corruption.** All JSON parses and hashes link correctly. Semantic correctness is a separate issue. |
| H2: Is the combined map too large/poorly shaped for browser work? | **Yes, it is confirmed poorly shaped.** It is 9.17 MB and repeats all topics. Whether a particular connector request exceeded a hidden service limit cannot be proven without connector telemetry. |
| H3: Is duplicated data present? | **Yes, confirmed.** The same headings and source cards are copied across postings, heading map, topic map, projections, ledgers, and atlasses. |
| H4: Did raw Git blob/tree timeout cause the browser failure? | **Not locally provable.** The observed behavior supports it, but the local artifacts contain no browser action log or timeout response. A local test cannot reproduce a remote connector limit. |
| H5: Are real semantic/content gaps present? | **Yes, confirmed.** Acceptance identifies missing details such as Skill Tree display-state semantics. |

## Tests actually performed

Without running the prohibited semantic/write workflow, the audit did perform read-only tests:

- parsed all 66 JSON files;
- verified every projection against the combined map SHA-256;
- executed Apex and retrieval health checks;
- measured all topic candidates and zero-signal candidates;
- inspected the generator branch that appends every source unconditionally;
- compared the 4,310 headings in postings against the same 4,310 in heading map;
- counted real Skill Tree ledger dispositions and repeated templates;
- inspected the five material source records and the final four claims.

A true H4 test would require browser/Git connector telemetry or deliberately exercising the external action path. That was both unavailable locally and outside the original read-only/no-semantic-run assignment.

## Smallest sensible correction

Keep the exhaustive all-source map for custody. Do not hand it to the semantic browser as its work queue.

Instead, derive a separate topic work pack:

- one source record stored once;
- references to that record rather than copied headings;
- candidates with actual signals first;
- zero-signal sources retained in exhaustive custody, not sent for routine semantic review;
- semantic task receives a small selected evidence set;
- ledger remains a review receipt;
- dossier remains the final knowledge product.

This preserves completeness without copying canonical sources or creating a second corpus.
