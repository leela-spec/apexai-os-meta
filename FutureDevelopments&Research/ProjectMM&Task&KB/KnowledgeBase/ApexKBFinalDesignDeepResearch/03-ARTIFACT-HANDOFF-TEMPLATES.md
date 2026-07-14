# Artifact and Handoff Templates

These are illustrative research interfaces for Deep Research to test, correct, simplify, expand, or reject. They show possible value-bearing relationships and must not be treated as finalized schemas, field contracts, filenames, or implementation commitments. Every retained field and artifact requires an identified consumer, demonstrated value, and relevant micro-design evidence.

## Artifact chain

| Stage | Artifact | Owner | Canonical status | Primary consumer |
|---|---|---|---|---|
| Target | `manifests/corpus-scope.json` | Operator | canonical input | inventory |
| Target | `manifests/topic-registry.json` | Operator + LLM | canonical input | Phase 0, semantic compiler, acceptance |
| Custody | `manifests/source-inventory.ndjson` | deterministic | regenerable evidence map | all later stages |
| Corpus intelligence | `manifests/phase0/structure-map.ndjson` | deterministic | derived | term/topic mapping |
| Corpus intelligence | `manifests/phase0/term-postings.ndjson` | deterministic | derived | topic mapping |
| Corpus intelligence | `manifests/phase0/duplicate-map.json` | deterministic | derived | topic mapping/source reuse |
| Corpus intelligence | `manifests/phase0/topic-maps/<topic>.json` | deterministic | derived authoritative candidate set | semantic compiler |
| Corpus intelligence | `manifests/phase0/topic-maps/<topic>.md` | deterministic | derived compact projection | LLM navigation |
| Corpus intelligence | `manifests/phase0/phase0-navigation-report.md` | deterministic | derived | operator and batch planning |
| Semantic | `ingest-analysis/sources/<hash>.analysis.md` | LLM | canonical semantic record | topic analyses/pages |
| Semantic | `ingest-analysis/topics/<topic>.analysis.md` | LLM | canonical semantic record | Phase 2 and acceptance |
| Compiled | `wiki/concepts/<topic>.md` | LLM | derived durable knowledge | queries and agents |
| Compiled | `wiki/summaries/<topic>-source-atlas.md` | LLM | derived durable navigation | queries, audits, future updates |
| Acceptance | `audit/semantic-acceptance/<run>/<topic>.json` | independent LLM + deterministic validation | canonical verdict record | status/postflight |
| Retrieval | `wiki/index.md`, `derived/search/*` | deterministic | derived | queries |
| Query | `outputs/queries/<timestamp>-<slug>.md` | LLM + deterministic evidence packet | reusable output | operator/agents/promotion |

## 1. Corpus scope

Purpose: make “whole corpus” testable and prevent silent omission or recursive indexing of KB outputs.

```json
{
  "schema": "apex.kb.corpus-scope.design-candidate",
  "source_roots": ["LeelaAppDevelopment"],
  "exclusions": [
    {
      "path": "LeelaAppDevelopment/LeelaApp-Index-KB-Wiki",
      "reason": "generated_kb_output"
    }
  ],
  "follow_pointer_only_sources": true,
  "formats": {
    "text": "index_full_text",
    "pdf": "extract_if_capable_else_blocked_visible",
    "image": "inventory_only_unless_visual_semantic_route"
  },
  "lifecycle_hint_rules": [
    {
      "path_glob": "**/Upgrades/**",
      "hint": "current_or_update_candidate",
      "authority": "hint_only"
    },
    {
      "path_glob": "**/Prototyp Spark/**",
      "hint": "prototype_candidate",
      "authority": "hint_only"
    }
  ]
}
```

Validation:

- Every file below a source root is present in inventory or matched by one exclusion.
- No exclusion is implicit.
- Path rules emit hints and the matching rule ID; they never declare semantic authority.

## 2. Topic registry

Purpose: combine future-AI questions with deterministic concept vocabulary.

```json
{
  "schema": "apex.kb.topic-registry.design-candidate",
  "topics": [
    {
      "topic_id": "skill-tree",
      "name": "Skill Tree",
      "primary_phrases": ["skill tree", "skilltree"],
      "aliases": ["spatial skill tree"],
      "supporting_terms": ["epic", "block", "chunk", "path"],
      "negative_or_ambiguous_terms": ["tree"],
      "target_queries": [
        {
          "query_id": "skill-tree-current-definition",
          "priority": "critical",
          "question": "What is the current Skill Tree and what does it own?",
          "answer_requirements": [
            "current definition",
            "Epic/Block/Chunk hierarchy",
            "ownership boundary",
            "current versus prototype distinction"
          ]
        },
        {
          "query_id": "skill-tree-source-coverage",
          "priority": "critical",
          "question": "Which files cover Skill Tree, how current are they, and what does each add?",
          "answer_requirements": [
            "every deterministic candidate",
            "individual source snapshot",
            "freshness and authority assessment",
            "duplicate/supersession relationship",
            "exact pointers"
          ]
        }
      ],
      "expected_pages": {
        "dossier": "wiki/concepts/skill-tree.md",
        "source_atlas": "wiki/summaries/skill-tree-source-atlas.md"
      }
    }
  ]
}
```

Validation:

- Primary phrases and aliases drive strong matches.
- Supporting terms require co-occurrence or structural context; they cannot independently flood the map.
- Broad topics include a source-coverage question, not only domain-answer questions.

## 3. Source inventory row

Purpose: stable source identity and deterministic extraction visibility.

```json
{
  "source_id": "src-sha256-prefix-or-stable-path-id",
  "path": "LeelaAppDevelopment/Upgrades/.../Skill Tree Update N4 v1.md",
  "bytes": 48219,
  "sha256": "...",
  "extension": ".md",
  "mime_or_format": "markdown",
  "extraction_status": "full_text",
  "line_count": 812,
  "filesystem_modified_utc": "2026-06-12T10:24:00Z",
  "git_last_change": {
    "commit": "abc123",
    "date": "2026-06-11",
    "status": "available"
  },
  "scope_status": "included",
  "lifecycle_hints": [
    {"rule_id": "updates-path", "hint": "current_or_update_candidate"}
  ]
}
```

Validation:

- Repeated generation is deterministic except explicitly volatile timestamp fields, which should be omitted or isolated.
- Unsupported files have `extraction_status` such as `blocked_parser_unavailable`; they remain in inventory.

## 4. Structure record

Purpose: give term and topic mapping stable section/line addresses.

```json
{
  "source_id": "src-...",
  "path": ".../Skill Tree Update N4 v1.md",
  "title": "Skill Tree Update N4 v1",
  "frontmatter_keys": ["title", "status"],
  "sections": [
    {
      "section_id": "s-004",
      "level": 2,
      "heading": "Epic, Block, and Chunk hierarchy",
      "heading_line": 118,
      "start_line": 118,
      "end_line": 203
    }
  ],
  "links": [
    {
      "type": "repository_path",
      "target": "LeelaAppDevelopment/MVP, User Stories & Flows/...",
      "line": 221
    }
  ],
  "parser_warnings": []
}
```

## 5. Term posting

Purpose: answer “where and how strongly does this exact configured phrase appear?” without opening files.

```json
{
  "topic_id": "skill-tree",
  "term": "skill tree",
  "normalized_term": "skill tree",
  "source_id": "src-...",
  "field": "heading",
  "count": 4,
  "pointers": [
    {"section_id": "s-004", "line": 118, "snippet": "Epic, Block, and Chunk hierarchy"}
  ],
  "match_kind": "exact_phrase"
}
```

Field enum should distinguish at least:

```text
path | filename | frontmatter_title | h1 | heading | body | link_text | link_target
```

## 6. Duplicate and version family

Purpose: save reads while retaining all documentary paths and possible evolution.

```json
{
  "exact_duplicates": [
    {
      "sha256": "...",
      "representative_source_id": "src-a",
      "member_source_ids": ["src-a", "src-b"]
    }
  ],
  "possible_version_families": [
    {
      "family_id": "skill-tree-update-night4",
      "member_source_ids": ["src-c", "src-d"],
      "signals": ["normalized_filename", "shared_title_tokens"],
      "semantic_supersession_status": "llm_review_required"
    }
  ]
}
```

## 7. Exhaustive topic-map row

Purpose: preserve every deterministic candidate and make ranking inspectable.

```json
{
  "topic_id": "skill-tree",
  "source_id": "src-...",
  "path": ".../Skill Tree Update N4 v1.md",
  "candidate_class": "direct",
  "signals": {
    "path_exact": 1,
    "filename_exact": 1,
    "title_exact": 1,
    "h1_exact": 0,
    "heading_exact_count": 4,
    "body_exact_count": 31,
    "alias_count": 2,
    "supporting_term_count": 18,
    "incoming_link_count": 3,
    "outgoing_link_count": 5
  },
  "best_pointers": ["s-004:118-203", "s-008:311-367"],
  "duplicate": {"status": "unique", "representative": null},
  "date_evidence": {"git_last_change": "2026-06-11"},
  "lifecycle_hints": ["current_or_update_candidate"],
  "sort_vector": [1, 1, 1, 4, 31, 3],
  "semantic_status": "not_evaluated"
}
```

Rules:

- The machine map is exhaustive for configured vocabulary and graph inclusion rules.
- A compact Markdown view may show prioritized groups but links to totals and omitted row counts.
- `sort_vector` is documented; an opaque total score is not the only explanation.

## 8. Compact topic navigation view

Purpose: minimize LLM startup context without hiding candidates.

```markdown
# Topic Map — Skill Tree

## Coverage

- In-scope files: 405
- Deterministic candidates: 130
- Unique content hashes: 92
- Direct/title/path/heading candidates: 24
- Dense contextual candidates: 38
- Linked/incidental candidates: 31
- Exact duplicate paths: 37
- Blocked extraction: 2

## Read first

| Source | Why surfaced | Best sections | Lifecycle hint | Duplicate status |
|---|---|---|---|---|
| `.../Skill Tree Update N4 v1.md` | filename + title + 4 headings | `118–203`, `311–367` | current/update candidate | unique |

## Then classify

- Contextual contract sources: 18 — see machine map filter `candidate_class=contextual`.
- Historical/prototype candidates: 29 — lifecycle hints require semantic confirmation.
- Duplicate paths: 37 — read representatives only; retain all paths in the atlas.
- Complete candidate artifact: `topic-maps/skill-tree.json`.
```

## 9. Populated Phase 0 navigation report

Purpose: operator-level overview and semantic batch plan. It is deleted from the mandatory path if it cannot add more value than the compact topic views.

Required sections:

```markdown
# Phase 0 Navigation Report

## Corpus coverage and extraction blockers
## Duplicate and version-family overview
## Topic coverage table
## Read-first source families by topic
## Cross-topic high-value sources
## Likely current/prototype/historical source groups (hints only)
## Recommended semantic batches and reusable source opportunities
## Unresolved deterministic ambiguities
```

## 10. Reusable source capsule

Purpose: compile a unique source once and reuse its evidence across topics.

```markdown
---
source_id: src-...
source_hash: sha256:...
semantic_contract_version: "design-candidate"
read_mode: complete
reviewed_spans: ["1-812"]
authority_assessment: current_specification
authority_confidence: medium
---

# Source Capsule — Skill Tree Update N4 v1

## Source identity and limitations

## One-sentence snapshot

This file defines ...

## Material knowledge by section

| Pointer | Snapshot | Reusable claims/concepts | Current/proposed status |
|---|---|---|---|

## Contradictions, supersession, and dependencies

## Topic contributions

| Topic | Questions supported | Individual value |
|---|---|---|

## Exact evidence pointers
```

Capsule invalidation requires at least source hash or semantic-contract change. Topic-specific value remains in topic analysis so one capsule does not become a giant all-purpose file.

## 11. Topic analysis and candidate disposition

Purpose: join the exhaustive deterministic map to semantic meaning and page architecture.

```markdown
# Topic Analysis — Skill Tree

## Target questions and coverage

| Query ID | Status | Answer evidence | Gap/next source |
|---|---|---|---|

## Candidate dispositions

| Source ID/path | Review mode | Semantic role | One-sentence snapshot | Individual value | Freshness/authority | Duplicate/version relation | Evidence pointers | Destination |
|---|---|---|---|---|---|---|---|---|
| src-a | full | core_current | Defines current hierarchy and handoff | highest | current specification, medium confidence | unique | §... | dossier + atlas |
| src-b | duplicate_representative | duplicate | Exact copy of src-a | path visibility only | same content | duplicate of src-a | hash | atlas |
| src-c | targeted | prototype | Spatial prototype interaction ideas | historical comparison | prototype, high confidence | possible family ... | §... | dossier prototype section + atlas |
| src-d | incidental | incidental | Mentions Skill Tree only as route destination | low | unknown | unique | line ... | atlas only |

## Contradiction and evolution map
## Page architecture decision
## Completion blockers
```

Candidate rules:

- Every topic-map candidate appears exactly once.
- `incidental` and `irrelevant_after_review` are valid, evidence-based outcomes.
- Exact duplicate paths do not require duplicate reads.
- A core/current readable source cannot remain `unopened` at completion.

## 12. Concept dossier

Purpose: answer routine concept questions directly and compactly.

```markdown
---
title: Skill Tree
page_type: concept
topic_id: skill-tree
target_query_ids: [...]
source_atlas: wiki/summaries/skill-tree-source-atlas.md
status: active
---

# Skill Tree

## Direct current-state answer

## Macro

What the concept is, why it exists, and its system boundary.

## Meso

Hierarchy, workflows, ownership, contracts, interconnections, and lifecycle.

## Micro

Fields, states, formulas, permissions, examples, edge cases, and precise pointers.

## Current implementation versus target specification
## Prototype and historical evolution
## Contradictions and unresolved decisions
## Related concepts and routes
## Key evidence pointers
```

The dossier should not repeat the full source atlas, long claim arrays, or frontmatter source lists. It links to the atlas and uses inline evidence pointers where claims are made.

## 13. Concept source atlas

Purpose: let a future AI understand the entire documentary landscape without rerunning corpus analysis.

```markdown
---
title: Skill Tree Source Atlas
page_type: summary
topic_id: skill-tree
candidate_count: 130
unique_content_count: 92
---

# Skill Tree Source Atlas

## How to use this atlas
## Source authority and evolution summary
## Core current sources
## Supporting and cross-feature sources
## Prototype and historical sources
## Duplicate and supersession families
## Incidental or rejected candidates
## Blocked/unreadable sources

| Source | Date/version evidence | Role | Read mode | Individual content snapshot | Individual value | Freshness/authority | Relationships | Exact relevant pointers |
|---|---|---|---|---|---|---|---|---|
```

Atlas acceptance:

- Candidate count reconciles with the deterministic topic map.
- Every candidate has one row or a lossless grouped duplicate representation that lists every path.
- “Freshness” distinguishes observed dates/path hints from LLM semantic judgment.
- Evidence sources are separated from incidental/unread/blocked sources.

## 14. Semantic acceptance record

```json
{
  "schema": "apex.kb.semantic-acceptance.design-candidate",
  "run_id": "...",
  "topic_id": "skill-tree",
  "contract_version": "...",
  "page_only_queries": [
    {
      "query_id": "skill-tree-current-definition",
      "verdict": "answerable",
      "answer": "...",
      "page_pointers": ["wiki/concepts/skill-tree.md#direct-current-state-answer"],
      "missing_requirements": []
    }
  ],
  "claim_entailment": [
    {
      "claim_pointer": "wiki/concepts/skill-tree.md#micro:C004",
      "verdict": "supported",
      "source_pointer": "src-a:118-137"
    }
  ],
  "atlas_coverage": {
    "topic_map_candidates": 130,
    "atlas_candidates": 130,
    "missing_ids": [],
    "duplicate_path_loss": []
  },
  "verdict": "semantic_pass"
}
```

## 15. Retrieval chunk

```json
{
  "chunk_id": "stable-hash",
  "rel_path": "wiki/concepts/skill-tree.md",
  "topic_id": "skill-tree",
  "heading": "Micro",
  "start_line": 82,
  "end_line": 146,
  "text": "...",
  "page_hash": "...",
  "source_type": "concept_dossier"
}
```

Source-atlas tables may need row-aware chunking or subsection grouping so retrieval can answer “which source covers X?” without returning an entire huge atlas.

## 16. Query packet

```markdown
# KB Query Output

## Question and direct answer
## Evidence pages and sections
## Source-atlas routes
## Contradictions and confidence
## Raw-source reopen status
## Retrieval backend and freshness
```

Routine queries should report `raw_source_reopen_status: not_required`. Reopen is valid for verification, unresolved conflict, or genuinely unavailable compiled detail—not for knowledge that was readable during compilation.

## 17. Incremental impact record

```json
{
  "changed_source_ids": ["src-a"],
  "change_reason": "hash_changed",
  "affected_topics": ["skill-tree", "path"],
  "capsules_to_refresh": ["sha256-old -> sha256-new"],
  "pages_to_reaccept": [
    "wiki/concepts/skill-tree.md",
    "wiki/summaries/skill-tree-source-atlas.md"
  ],
  "unaffected_topics": ["stats"]
}
```

## 18. Module Output Record

Use this as a research-output checklist, not a final storage schema:

```yaml
module_id:
target_contribution:
current_behavior:
current_mismatch:
evidence_status:
focused_questions: []
sources_read: []
llm_wiki_mechanisms_consulted: []
claude_micro_design_sources_consulted: []
final_strategy:
submodules: []
inputs: []
outputs: []
consumers: []
interconnections: []
implementation_order: []
tests_and_fixtures: []
configuration_effects: []
remaining_unverified_facts: []
```

## 19. File and Script Design Record

For every affected current or proposed file, script, template, workflow, reference, hook, manifest, or generated artifact, provide:

```yaml
repository_relative_path:
artifact_type:
purpose:
owner:
status: canonical | generated | derived | temporary
current_behavior:
current_mismatch:
final_responsibilities: []
non_responsibilities: []
inputs: []
outputs: []
consumers: []
required_sections_or_interfaces: []
control_flow: []
deterministic_semantic_boundary:
relationships: []
progressive_disclosure_behavior:
micro_design_evidence: []
migration_behavior:
tests_and_fixtures: []
failure_behavior:
token_and_maintenance_cost:
risks: []
disposition:
rationale:
```

This record is implementation guidance. It must not contain the complete replacement file or finished code.

## 20. Configuration Axis Record

```yaml
axis_id:
purpose:
allowed_values: []
default:
activation_criteria:
dependencies: []
effect_on_outputs: []
effect_on_cost:
effect_on_completeness:
incompatible_combinations: []
operator_decision_needed:
```

Configuration controls execution scope inside one complete architecture. It does not create separate product versions.

## 21. Source-Access Evidence Record

```yaml
repository_identity:
route_attempts: []
selected_route:
evidence_mode: full_repository_evidence | project_source_repository_snapshot | architecture_research_without_apex_implementation
current_main_commit:
available_sources: []
unavailable_sources: []
snapshot_limitations: []
unverified_implementation_facts: []
```

## 22. Browser Semantic Task-Packet Design Record

```yaml
save_batch_id:
concept_or_source_group:
input_artifacts: []
whole_files_to_read: []
semantic_outputs_expected: []
allowed_write_scope: []
completion_definition:
actual_model_or_mode:
blocked_or_partial_behavior:
next_deterministic_actions: []
```

A save batch is a coherent, context-aware completed Apex KB unit, not an arbitrary partial draft.

## Interface value test

For every proposed artifact, field, instruction, gate, evaluator, or handoff, Deep Research must identify:

1. which downstream consumer reads it;
2. which demonstrated failure it prevents or which repeat work it removes;
3. whether it can be derived instead of authored by the LLM;
4. whether it duplicates information elsewhere;
5. whether omission would make a product decision or truthful state ambiguous;
6. which LLM-Wiki mechanism supports the pattern;
7. which Claude skill/orchestration source supports its micro design;
8. its recurring token, compute, and maintenance cost.

Items that fail this test should not be mandatory. Durable source maps and source atlases require lossless candidate reconciliation, blocked-source visibility, exact pointers, and future-AI usability; they are core product outputs rather than optional reports.
