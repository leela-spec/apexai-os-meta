---
name: apex-kb
description: >
  Use this skill when the operator asks to scaffold, intake sources, hash sources,
  run deterministic corpus intelligence, perform two-phase ingest, compile wiki
  pages, query, retrieve, lint, audit, or maintain a durable Apex knowledge base
  under apex-meta/kb/<kb-slug>/. Produces source-preserving KB artifacts,
  Phase 1 ingest analysis, operator-gated Phase 2 wiki pages, deterministic
  indexes, local retrieval outputs, query packets, lint reports, and audit flags.
  Does not plan projects, mutate task/session/sync state, rank next tasks,
  rebuild task registries, contact external services, or write outside the KB root.
---

# Apex KB

## Operating contract

```yaml
package_name: apex-kb
primary_role: durable_source_preserving_knowledge_base_compiler
data_root_template: apex-meta/kb/<kb-slug>/
one_kb_root_per_invocation: true
required_global_argument: --kb-root apex-meta/kb/<kb-slug>/

owned_lifecycle:
  - scaffold
  - source_intake
  - deterministic_corpus_intelligence
  - ingest_phase_1_analysis
  - operator_gate
  - ingest_phase_2_wiki_compile
  - deterministic_index_validation
  - local_retrieval
  - query_packet_generation
  - lint_audit_maintenance

canonical_paths:
  - raw/
  - kb-schema.md
  - manifests/source-manifest.json
  - ingest-analysis/
  - wiki/
  - audit/
  - log/

derived_paths:
  - manifests/phase0/
  - derived/search/
  - outputs/queries/

approval_gate:
  phrase: approve ingest
  required_before:
    - wiki_page_generation
    - manifest_semantic_updates
    - audit_items_from_semantic_claims

boundary:
  must_not_mutate:
    - apex-plan files
    - apex-sync files
    - apex-session files
    - PreCap artifacts
    - FlowRecap artifacts
    - APSU/status-merge artifacts
    - personal orchestration state
```

## File navigation

Read supporting files only when needed:

| Need | File |
|---|---|
| Data layout, canonical/derived rules, page and manifest constraints | `references/kb-contract.md` |
| Python command surface and write policy | `references/script-command-contract.md` |
| Ingest, query, lint, audit behavior | `references/ingest-query-lint-audit-rules.md` |
| Retrieval engine rules | `references/retrieval-contract.md` |
| State transitions and gates | `references/lifecycle-state-machine.md` |
| Acceptance checks | `references/acceptance-tests.md` |
| Phase 1 analysis shape | `templates/ingest-analysis-template.md` |
| Phase 2 wiki page shape | `templates/wiki-page-templates.md` |
| Query packet shape | `templates/query-output-template.md` |
| Starter KB schema | `templates/kb-schema-template.md` |
| Starter source manifest | `templates/source-manifest-template.json` |
| Local commands | `examples/powershell-commands.md` |
| Operator runbook | `examples/lifecycle-runbook.md` |

## Procedure

1. Resolve exactly one `--kb-root`. Never hardcode `claude-skill-design`; treat it only as a possible test KB slug.
2. Run deterministic checks through `apex-meta/scripts/apex_kb.py` for scaffold, hash, source-intake, preflight, phase0, index, lint, audit, status, and health.
3. Preserve source custody before semantic work: raw source, durable pointer, storage mode, source hash or no-hash reason, source manifest entry.
4. Run Phase 0 before LLM ingest when corpus navigation is needed. Phase 0 may create only deterministic artifacts under `manifests/phase0/`.
5. In Phase 1, create source-grounded semantic analysis under `ingest-analysis/` and halt. Do not generate wiki pages yet.
6. Proceed to Phase 2 only after the operator provides the exact phrase `approve ingest`. In normal mode this must be a separate operator turn after Phase 1 exists.
7. In Phase 2, draft or update `wiki/summaries/`, `wiki/concepts/`, `wiki/entities/`, audit items, and semantic index sections. Every claim needs source pointers, confidence, and claim labels.
8. Rebuild deterministic index sections and retrieval indexes after wiki updates. Use `apex_kb_retrieval.py` for `build-index`, `stale`, `query`, `export`, and `clear-index`.
9. Answer queries index-first. Read `wiki/index.md`, retrieve the smallest sufficient page set, synthesize from compiled wiki pages, and save query packets when reuse is useful.
10. Keep lint/audit maintenance read-only unless the operator explicitly asks for a deterministic write inside the KB root.

## Deterministic versus LLM ownership

```yaml
python_owns:
  - scaffold_structure
  - file_hashing
  - source_manifest_shape
  - source_storage_mode_recording
  - corpus_profile
  - heading_link_frontmatter_maps
  - keyword_hit_maps
  - deterministic_index_sections
  - frontmatter_validation
  - link_orphan_stale_checks
  - retrieval_index_build_query_export
  - audit_file_listing

llm_owns:
  - relevance_judgment
  - source_summary
  - concept_extraction
  - entity_synthesis
  - contradiction_interpretation
  - phase_1_analysis
  - phase_2_wiki_drafting
  - query_answer_synthesis
  - knowledge_gap_framing
```

## Failure behavior

```yaml
source_access_precheck_failed:
  behavior: stop
  output_only: SOURCE_ACCESS_PRECHECK_FAILED

missing_kb_root:
  behavior: route_to_scaffold_or_request_existing_root

missing_source:
  behavior: stop
  rule: never infer source contents from filename, title, memory, or summary

phase2_without_approval:
  behavior: stop_after_phase1
  required_phrase: approve ingest

stale_retrieval_index:
  behavior: report_stale_and_rebuild_before_reliance

contradiction_detected:
  behavior: expose_as_contradiction_or_audit_item

request_mutates_plan_sync_session:
  behavior: refuse_in_apex_kb_and_handoff_read_only_evidence_packet
```

## Completion gate

The skill is complete only when the requested mode has produced the correct artifact, source custody is preserved, deterministic/semantic ownership was respected, no outside-KB mutation occurred, confidence and claim labels are not conflated, and unresolved contradictions/open questions remain visible.
