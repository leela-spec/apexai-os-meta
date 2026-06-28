# Apex KB Retrieval Contract

## Retrieval boundary

```yaml
retrieval:
  source_of_truth: compiled wiki pages plus manifests and raw sources
  derived_indexes:
    - derived/search/index.sqlite
    - derived/search/search-index.json
    - derived/search/search-index.ndjson
    - derived/search/index-meta.json
  rule: indexes are rebuildable and never canonical
  mandatory_vector_search: false
  hosted_retrieval_required: false
  mutates_plan_sync_session: false
```

## Backend policy

1. Build a deterministic JSON/NDJSON chunk index for every rebuild.
2. Probe SQLite FTS5 at runtime before using it.
3. Use SQLite FTS5/BM25 when available.
4. Fall back to markdown/JSON lexical search when FTS5 is unavailable or stale.
5. Chunk primarily by Markdown headings; use page-level fallback for pages with no headings.
6. Save hash-based metadata so stale detection covers added, deleted, and modified pages.

## Indexed corpus

Index compiled KB pages under:

```text
wiki/concepts/*.md
wiki/entities/*.md
wiki/summaries/*.md
```

`wiki/index.md` is the query entrypoint, not the main evidence body. It may be read before retrieval but should not dominate search results.

## Minimum chunk fields

```yaml
chunk_record:
  chunk_id: stable hash
  kb_slug: string
  rel_path: string
  title: string
  page_type: summary | concept | entity | unknown
  status: draft | active | needs_review | deprecated | superseded | unknown
  confidence: high | medium | low | mixed | unknown
  claim_label: allowed claim label or unknown
  heading: string
  heading_level: integer
  start_line: integer
  end_line: integer
  text: string
  page_hash: sha256
  source_mtime: float
```

## Query packet requirements

A saved query output must include query, KB slug, backend, stale status, generated timestamp, evidence paths, headings, line ranges, confidence, claim label, excerpts, open gaps if any, and raw JSON for reproducibility.

## Stale policy

A retrieval result used for planning or durable synthesis must not rely on a stale index. If stale, rebuild first or explicitly mark the result as stale and bounded.
