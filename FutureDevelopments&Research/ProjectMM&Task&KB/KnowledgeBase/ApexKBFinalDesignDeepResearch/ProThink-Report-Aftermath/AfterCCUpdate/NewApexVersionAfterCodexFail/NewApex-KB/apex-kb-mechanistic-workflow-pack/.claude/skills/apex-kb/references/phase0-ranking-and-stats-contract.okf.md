---
okf_schema: apex.okf.contract.v1
contract_id: apex-kb.phase0-ranking-and-stats.v2
status: final
script_owner: apex-meta/scripts/apex_kb.py
control_owner: apex-meta/scripts/apex_kb_control.py
---

# Phase 0 Ranking and Statistics Contract

## Purpose

Phase 0 creates complete, inspectable corpus intelligence before any semantic AI work. It never declares semantic relevance, authority, or truth.

## Exact script ownership

The existing Phase 0 implementation remains behind the single control plane. The implementation must upgrade the existing `cmd_phase0` / topic-ranking path rather than create a competing lifecycle orchestrator.

Required deterministic functions:

```yaml
functions:
  inventory_sources:
    output: manifests/source-inventory.ndjson
  extract_source_facts:
    output: manifests/phase0/source-facts.json
  extract_structure:
    outputs: [manifests/phase0/heading-map.json, manifests/phase0/link-map.json]
  detect_duplicates_and_version_families:
    output: manifests/phase0/duplicate-map.json
  rank_topic_sources:
    output: manifests/phase0/topic-source-rankings.json
  build_topic_work_pack:
    output: manifests/phase0/work-packs/<topic>.json
  build_phase0_stats:
    outputs: [manifests/phase0/phase0-stats.json, manifests/phase0/phase0-stats.okf.md]
```

## Ranking inputs

- Locked run manifest and configuration hash.
- Topic registry: phrases, aliases, supporting terms, ambiguous terms, negative terms, and locked target questions.
- Source inventory and extraction status.
- Path, filename, frontmatter title, H1, headings, body sections, links, dates, lifecycle hints, and duplicate/version evidence.

## Inspectable signal vector

Every candidate row preserves the signals separately:

```yaml
signals:
  path_phrase_match: {strength: strong}
  filename_phrase_match: {strength: strong}
  frontmatter_title_match: {strength: strong}
  h1_phrase_match: {strength: strong}
  heading_phrase_match: {strength: strong}
  body_phrase_match: {strength: medium}
  alias_match: {strength: configured}
  supporting_term_cooccurrence: {strength: weak}
  ambiguous_term_with_required_cooccurrence: {strength: medium}
  link_or_process_edge: {strength: optional_context}
  filesystem_date: {strength: hint_only}
  git_last_change_date: {strength: hint_only}
  lifecycle_path_rule: {strength: hint_only}
  exact_duplicate: {strength: routing_control}
  possible_version_family: {strength: review_hint}
```

## Ordering

1. Exact path/filename/title/H1 phrase matches.
2. Exact heading phrase matches.
3. Strong body phrase/alias matches.
4. Supporting-term matches only with configured co-occurrence.
5. Linked/contextual candidates.
6. Duplicate paths attach to their representative rather than consume another read.

Do not collapse these into one unexplained score. A stable sort vector may be emitted, but the component values and pointers remain visible.

## Date and authority rule

A newer date may improve read order but never proves correctness or authority. The output must call dates `freshness_hints`, not authority decisions.

## Completeness rules

- No top-N truncation in the canonical machine ranking.
- Every in-scope file is inventoried, explicitly excluded, or visibly blocked/unreadable.
- Every candidate includes at least one exact reason and pointer.
- The bounded work pack is a projection; the full candidate set remains available.

## Required statistics

```yaml
corpus:
  total_files: integer
  included_files: integer
  excluded_files: integer
  unreadable_or_unsupported: integer
  total_bytes: integer
  file_count_by_extension: object
  heading_count_total: integer
  heading_count_by_level: object
  exact_duplicate_groups: integer
  possible_version_families: integer
topics:
  - topic_id: string
    candidate_count_total: integer
    filename_or_title_matches: integer
    h1_matches: integer
    heading_matches: integer
    body_strong_matches: integer
    body_weak_matches: integer
    linked_contextual_matches: integer
    duplicate_paths_collapsed: integer
    concentrated_work_pack_count: integer
    held_in_custody_count: integer
    zero_signal_custody_count: integer
    locked_question_count: integer
    questions_without_candidate_evidence: array
```

## Downstream use

The semantic executor does not interpret the full Phase 0 report. The instruction generator consumes it and emits only:

- exact locked questions;
- the bounded source batch;
- why each source was surfaced;
- unresolved evidence gaps;
- exact output and validation requirements.
