# Plain-language addendum: why the Leela deterministic output is large

This addendum corrects the main point that was too buried in the earlier diagnostic: **the map generator currently places every one of the 197 scanned source records into every one of the 10 topics.** It is not a topic-isolated candidate list.

## The short answer

The deterministic scan itself has a sensible, small per-file output:

- `manifests/phase0/source-postings.json` — **721,859 bytes**. It has 197 records: source ID, path, SHA-256, whether the file is text-readable, that file's headings, and links.
- `manifests/phase0/heading-map.json` — **532,795 bytes**. It has 146 Markdown-file records: path, title, a list of headings with line numbers, parser warnings, and a source-type guess.

Those are the files that answer “for each file, what headings does it have?” They are not abnormally large: together they are about 1.25 MB, and each source appears once.

The oversized file is different:

- `manifests/phase0/topic-source-map.json` — **9,172,513 bytes**. It has 10 topic records × 197 candidates = 1,970 candidate records.

The current generator does **not** count every occurrence of every keyword. For each topic term, it records only whether that term appears in one of five places—path, filename, headings, body, or links. The large size comes mainly from repeating every source's path, hash, heading list, duplicate/version metadata, and signal object ten times, once per topic.

## Concrete file snapshots

### 1. The compact, per-file heading report

File: `manifests/phase0/source-postings.json` (721,859 bytes)

One of 197 records looks like this (shortened):

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

This is close to the intended “one report per source file.” It does not contain the source body.

### 2. The other per-file heading report

File: `manifests/phase0/heading-map.json` (532,795 bytes)

One of 146 Markdown records looks like this (shortened):

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

### 3. Keyword summary—not individual hit occurrences

File: `manifests/phase0/term-frequency.json` (small global summary; 60 rows)

```json
{"term": "nowa", "count": 1811, "file_count": 80}
```

This is an aggregate count and file count. It is not a list of 1,811 individual occurrences.

### 4. The oversized topic map

File: `manifests/phase0/topic-source-map.json` (9,172,513 bytes)

One candidate inside one topic looks like this (shortened):

```json
{
  "candidate_id": "cand-21c66e85823af40d",
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
    "headings": [{"level": 1, "line": 1, "text": "101 Chunks"}, "…"]
  }
}
```

This is not a source-body copy, but it repeats the heading list and metadata. The candidate ID is different in each topic because it is derived from `topic-slug + NUL + source-path`.

### 5. What the browser should receive for one topic

File: `manifests/phase0/acceptance-candidate-projections/skill-tree.json` (86,469 bytes)

```json
{
  "schema": "apex.kb.acceptance-candidate-projection.v1",
  "source_map_path": "manifests/phase0/topic-source-map.json",
  "source_map_sha256": "e47a391b…",
  "topic_slug": "skill-tree",
  "candidate_count": 197,
  "candidates": ["same record shape as above, for this topic"]
}
```

This is far smaller than the 9 MB map, but it still contains all 197 sources because it is currently a one-topic *projection of an exhaustive list*, not a ranked/filtered evidence pack.

### 6. What the semantic run created from that list

File: `manifests/topic-ledgers/skill-tree.json` (262,141 bytes)

```json
{
  "topic": "skill-tree",
  "review_status": "analysis_complete_unvalidated",
  "candidate_count": 197,
  "candidates": [{
    "candidate_id": "cand-…",
    "source_id": "src-…",
    "source_path": "LeelaAppDevelopment/…",
    "read_scope": "…",
    "source_snapshot": "…",
    "distinctive_value": "…",
    "disposition": "…"
  }]
}
```

This is the semantic/provenance layer. It repeats all 197 candidates again, now with a human/semantic disposition.

## Why all 10 topics have all 197 candidates

The relevant generator logic is effectively:

```text
for each topic:
    for each source record:
        calculate signals in path / filename / headings / body / links
        assign direct, dense, contextual, linked, or exact_duplicate
        append a candidate record
```

There is **no “if there are relevant signals, append it” filter**. If no signal is present, the fallback classification is `contextual`, and the source is still appended.

So the overlap is real and confirmed:

- It is not evidence that the semantic browser accidentally mixed topics.
- It is a property of the deterministic map's current contract/implementation: every topic carries the whole 197-source inventory.
- The navigation Markdown is less noisy because it displays only candidates with a signal (or exact duplicate), but the JSON map, projections, ledgers, and atlasses retain the exhaustive 197 records.

## Are H1–H5 “there” or not?

| Hypothesis | Plain answer | Why |
|---|---|---|
| H1: corrupt deterministic files | **No evidence of corruption.** | JSON parses and projections hash-link correctly. |
| H2: full map is a bad browser retrieval payload | **Very likely.** | One 9.17 MB / estimated 2.29M-token JSON object is a poor browser connector payload; local parsing works while browser reported empty. Exact service limit is unknown. |
| H3: duplication harms browser completion | **Yes, if read together.** | The system repeats the same inventory in map → projection → ledger → atlas. The repetition is not inherently invalid, but an unbounded browser read is harmful. |
| H4: raw Git blob/tree action limits caused the large browser failure | **Likely, but not proven locally.** | The reported atomic raw Git failure versus successful topic commits fits this explanation; there are no connector logs/telemetry here. |
| H5: remaining acceptance failures are content gaps | **Yes, definitely present.** | Acceptance records name specific missing content (for example, Skill Tree display-state semantics). It is not possible locally to say whether these are the *main* cause versus an execution failure preventing repair. |

## The minimal, understandable fix direction

Do **not** delete the full map. It can remain the deterministic “we considered every source” evidence.

But do separate two things:

1. **Custody list:** all 197 sources, machine-readable, retained in the full map/projection.
2. **Semantic work pack:** a topic-local navigation/selection list and only the named evidence sources needed for this task.

The open design question is not whether the source corpus should be copied or replaced. It is whether the deterministic generator should add a second, small topic evidence pack (for example, only direct/dense/linked records, with contextual records still retained in custody). That would preserve exhaustive coverage while giving the browser an actually isolated, usable task input.
