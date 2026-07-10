# Apex KB Phase 2 Minimal Value Contract — Macro/Meso Change Plan

## 1. Current Scope

Target package:

```text
.claude/skills/apex-kb/
```

Runtime scripts referenced by the package:

```text
apex-meta/scripts/apex_kb.py
apex-meta/scripts/apex_kb_retrieval.py
```

The package manifest identifies the Apex KB package role, runtime script paths, dry-run/write policy, and the file inventory that defines the package surface. It also lists the core reference, template, and example files under `.claude/skills/apex-kb/`.

This plan does **not** rewrite wiki pages, patch scripts, patch retrieval, or touch `apex-kb2`.

---

## 2. Corrected Macro Architecture

### 2.1 Main change

Apex KB Phase 2 must move from:

```yaml
old_contract:
  type: structural_page_contract
  passes_if:
    - frontmatter exists
    - source_refs exist
    - confidence exists
    - claim_label exists
    - page has correct folder/path
```

to:

```yaml
new_contract:
  type: adaptive_page_value_contract
  passes_if:
    - page reduces future reading cost
    - page preserves an adaptive ranked source set
    - page contains macro / meso / micro synthesis
    - page carries source-grounded claims with source pointers
    - page routes future questions
    - page names uncertainty and raw-source reopen triggers
```

The current skill already says Phase 2 drafts or updates summaries, concepts, entities, audit items, and semantic index sections, and that every claim needs source pointers, confidence, and claim labels. The patch should **strengthen that existing Phase 2 behavior**, not redesign the lifecycle.

### 2.2 Adaptive ranked source set

The previous “2–5 most relevant sources” simplification is rejected.

Correct model:

```yaml
ranked_source_set:
  status: required
  implementation_level: macro_and_meso_contract
  rule: >
    The ranked source set must be proportional to KB size, topic breadth,
    and source diversity. It may be short for narrow pages and large for broad
    synthesis pages.
  must_include:
    - source_id_or_path
    - rank_or_priority_tier
    - why_relevant
    - claim_or_section_supported
    - source_pointer
    - reopen_raw_source_when
  not_required:
    - fixed source count
    - separate source cluster map
```

Source count guidance:

```yaml
source_count_guidance:
  narrow_entity_or_single_source_concept:
    expected: "1-3 highly relevant sources may be enough"
  normal_concept_or_summary:
    expected: "all materially relevant sources from Phase 1 should be carried"
  broad_architecture_or_process_concept:
    expected: "include every source family that materially changes the synthesis"
  very_large_kb:
    expected: "rank by tiers instead of arbitrary caps"
```

### 2.3 Source cluster map

```yaml
source_cluster_map:
  status: drop_from_required_patch
  reason: >
    Useful, but it risks becoming a second bureaucracy layer beside the ranked
    source set.
  future_development:
    - "Add optional source-family / source-cluster summaries for very large KBs."
    - "Derive candidate clusters from Phase 0 / source manifest / file paths where possible."
    - "Do not require it on every page."
```

### 2.4 Macro / meso / micro synthesis

```yaml
macro_meso_micro:
  status: required
  reason: >
    It gives future LLMs the different abstraction levels needed for routing,
    synthesis, and detail recovery.
  page_level_meaning:
    macro: "Why this page matters in the KB and which larger decision area it supports."
    meso: "Main mechanisms, relationships, process rules, or conceptual structure."
    micro: "Specific claims, source pointers, examples, commands, fields, or edge cases."
```

This should not become a huge schema. It should become one required section or compact subsection in Phase 2 templates.

### 2.5 Relationships and crosslinks

```yaml
relationships_and_crosslinks:
  status: merge
  merge_into:
    - route_by_question
    - related_pages
    - next_reads
  deterministic_script_role:
    validates:
      - dead wikilinks
      - orphan pages
      - index freshness
    does_not_validate:
      - semantic relationship quality
      - whether a link is the right next read
      - whether a concept should be connected
```

The deterministic lint currently checks frontmatter, paths, wikilinks, orphan pages, and index staleness; it does not perform semantic relationship judgment. So the LLM must still decide meaningful relationship/crosslink routing, while Python can validate mechanical link health.

### 2.6 Contradictions, open questions, and raw source reading

```yaml
uncertainty_layer:
  status: merged_required_section
  merged_items:
    - contradictions_or_tensions
    - open_questions
    - raw_source_reading_path
  section_name: "Uncertainty / Raw Source Triggers"
  purpose: >
    Tell future models when compiled pages are enough and when raw evidence must
    be reopened.
```

### 2.7 Route by question

```yaml
route_by_question:
  status: required
  reason: >
    Query routing is the core value of a compiled KB. Pages should tell future
    models which questions should start there.
  minimum:
    - likely_question
    - why_this_page
    - next_reads
    - raw_source_needed: yes | no | conditional
```

The retrieval contract already states that compiled KB pages are the indexed corpus, while `wiki/index.md` is the query entrypoint and should not dominate search results. The page-value contract should make those compiled pages route-useful.

---

## 3. Meso Change Logic by File

## 3.1 `.claude/skills/apex-kb/SKILL.md`

### Macro role

Skill entrypoint and operator-facing lifecycle contract.

It already defines the full lifecycle and Phase 2 position. It also preserves the no-mutation boundary for Plan, Sync, Session, PreCap, FlowRecap, APSU/status-merge, and personal orchestration.

### Meso change

Add a concise Phase 2 value instruction to the existing procedure.

```yaml
change_needed: yes
change_size: small
section_to_change:
  - "## Procedure"
  - "Phase 2 step"
behavior_to_create:
  - "Phase 2 must create page-value, not shell pages."
  - "Every page must preserve adaptive ranked source set, macro/meso/micro, claims, routing, and raw-source triggers."
behavior_to_avoid:
  - "Do not expand SKILL.md into the full template."
  - "Do not redefine lifecycle."
  - "Do not mention a fixed number of ranked sources."
```

---

## 3.2 `.claude/skills/apex-kb/package-manifest.md`

### Macro role

Package inventory, runtime scope, canonical script references.

The manifest lists the package path, script paths, runtime policy, inventory, canonical runtime KB paths, canonical/derived split, scope exclusions, and executability note.

### Meso change

No immediate content change required for Phase 2 value contract.

```yaml
change_needed: no
reason: >
  This file is inventory and scope. The Phase 2 value contract belongs in
  SKILL.md, kb-contract.md, ingest rules, and templates.
future_optional_change:
  - "Add note that wiki-page-templates.md now owns the Phase 2 page-value contract."
behavior_to_avoid:
  - "Do not turn package-manifest into a policy file."
```

---

## 3.3 `.claude/skills/apex-kb/references/kb-contract.md`

### Macro role

Canonical data root, source custody, page contract, and boundary contract.

Current page contract is frontmatter-focused: title, page_type, kb_slug, source_refs, timestamps, confidence, claim_label, and status.

### Meso change

Add a **Page Value Contract** after the current frontmatter contract.

```yaml
change_needed: yes
change_size: medium
section_to_change:
  - "## Page contract"
new_meso_layer:
  - "Frontmatter contract remains structural."
  - "Page value contract becomes semantic/LLM-owned."
  - "Phase 2 pages must reduce future reading cost."
required_concepts_to_add:
  - adaptive_ranked_source_set
  - macro_meso_micro
  - key_claims_with_source_pointers
  - route_by_question
  - uncertainty_raw_source_triggers
invalid_patterns_to_name:
  - frontmatter_only_value
  - generic_yaml_pattern_shell
  - source_refs_without_source_reason
  - fixed_source_count_cap
behavior_to_avoid:
  - "Do not add 20 required frontmatter fields."
  - "Do not put semantic value fields in frontmatter."
```

---

## 3.4 `.claude/skills/apex-kb/references/script-command-contract.md`

### Macro role

CLI command contract and write policy for deterministic scripts.

It says `ingest-phase2` does not script-write pages; the LLM drafts pages, while Python owns deterministic commands.

### Meso change

No immediate change.

```yaml
change_needed: no
reason: >
  The current patch should not add deterministic semantic scoring or script-level
  page-value enforcement.
future_optional_change:
  - "If a later mechanical shell-page detector is added, document it here."
behavior_to_avoid:
  - "Do not add Python semantic quality scoring."
  - "Do not modify CLI contract for this patch."
```

---

## 3.5 `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`

### Macro role

Operational rules for ingest, query, lint, and audit.

Current Phase 2 rule is too broad: it allows compiled pages, semantic manifest updates, deterministic index updates, audit items, and logs, while preserving contradictions and low-confidence claims.

### Meso change

Strengthen Phase 2 rules and semantic review flags.

```yaml
change_needed: yes
change_size: medium
section_to_change:
  - "### Phase 2"
  - "Semantic review flags"
new_phase2_rule:
  - "Phase 2 output must not be shell pages."
  - "Every page must include adaptive ranked source set."
  - "Every page must include macro/meso/micro synthesis."
  - "Every page must route likely questions."
  - "Every page must identify raw-source reopen triggers."
semantic_review_flags_to_add:
  - missing_ranked_source_set
  - fixed_source_cap_used_when_more_sources_matter
  - missing_macro_meso_micro
  - source_refs_without_relevance_explanation
  - route_by_question_missing
  - raw_source_trigger_missing
behavior_to_avoid:
  - "Do not make lint semantic if script is not changed."
  - "Keep these as LLM/audit review flags unless a future deterministic detector is added."
```

---

## 3.6 `.claude/skills/apex-kb/references/retrieval-contract.md`

### Macro role

Retrieval and search-index contract.

It defines compiled wiki pages as indexed corpus and makes `wiki/index.md` the query entrypoint, not the evidence body. It also defines query packet requirements including evidence paths, headings, line ranges, confidence, claim labels, excerpts, and open gaps.

### Meso change

Small optional clarification, not required in first patch.

```yaml
change_needed: optional
change_size: small
possible_section_to_change:
  - "## Indexed corpus"
  - "## Query packet requirements"
clarification_to_add:
  - "Retrieval quality depends on Phase 2 pages containing routeable headings and source-grounded claims."
  - "Ranked source sets and route-by-question sections improve retrieval/query synthesis but are authored in wiki templates."
behavior_to_avoid:
  - "Do not patch retrieval engine."
  - "Do not add new backend requirements."
  - "Do not require vector search."
```

Recommendation: leave unchanged in first implementation unless the next micro patch targets this file.

---

## 3.7 `.claude/skills/apex-kb/references/lifecycle-state-machine.md`

### Macro role

Lifecycle state transitions and gates.

Current S6 says Phase 2 creates compiled wiki pages with source pointers, confidence, claim labels, contradictions, and questions.

### Meso change

Small change recommended.

```yaml
change_needed: yes
change_size: small
section_to_change:
  - "S6_phase2_ready"
meso_update:
  - "S6 goal should say compiled wiki pages must have page-value contract, not only source pointers/confidence/claim labels."
  - "Add adaptive ranked source set and macro/meso/micro to S6 goal or outputs."
behavior_to_create:
  - "Lifecycle state machine records the value contract at the correct phase."
behavior_to_avoid:
  - "Do not split lifecycle into more states."
  - "Do not add another gate."
```

---

## 3.8 `.claude/skills/apex-kb/references/acceptance-tests.md`

### Macro role

Smoke and acceptance criteria.

The current wiki/retrieval test creates one very small concept page and then verifies index/retrieval behavior. That accepts the failure pattern.

### Meso change

Replace the weak compiled-page fixture with a page-value fixture.

```yaml
change_needed: yes
change_size: medium
section_to_change:
  - "## Wiki/index/retrieval"
meso_update:
  - "Test fixture concept page must include adaptive ranked source set."
  - "Test fixture must include macro/meso/micro."
  - "Test fixture must include key claims."
  - "Test fixture must include route-by-question."
  - "Test fixture must include uncertainty/raw-source trigger."
  - "Add negative acceptance language: frontmatter plus one YAML block is not acceptable Phase 2 output."
behavior_to_avoid:
  - "Do not make test huge."
  - "Do not require script to fail shell page yet."
  - "Do not patch Python in this step."
```

---

## 3.9 `.claude/skills/apex-kb/references/knowledge-promotion-rules.md`

### Macro role

Prevents raw source, candidate, accepted doctrine, and runtime truth from collapsing. It defines knowledge states and promotion gates.

### Meso change

Small clarification recommended.

```yaml
change_needed: yes
change_size: small
section_to_change:
  - "## State model"
  - "## Promotion gate"
meso_update:
  - "Clarify that Phase 2 pages can promote Phase 1 candidates into accepted_doctrine only when source-grounded and page-value conditions are met."
  - "Add page_value_contract as a requirement for candidate_to_accepted_doctrine when the target form is a wiki page."
behavior_to_create:
  - "Thin YAML pages do not accidentally become accepted doctrine."
behavior_to_avoid:
  - "Do not redefine runtime_truth."
  - "Do not add operator decisions that must be inferred."
```

---

## 3.10 `.claude/skills/apex-kb/references/repo-execution-router-lint-spec.md`

### Macro role

Future deterministic lint spec for repo execution handovers. It is explicitly `spec_only_not_executable`.

### Meso change

No Phase 2 value-contract change.

```yaml
change_needed: no
reason: >
  This file concerns repo execution handover safety, not wiki page value.
future_optional_change:
  - "None for Phase 2 page contract."
behavior_to_avoid:
  - "Do not mix repo execution routing with wiki synthesis quality."
```

---

## 3.11 `.claude/skills/apex-kb/references/historical-path-authority-lint-spec.md`

### Macro role

Future deterministic lint spec that prevents historical paths from being treated as current authority. It is also spec-only.

### Meso change

No Phase 2 value-contract change.

```yaml
change_needed: no
reason: >
  Useful Apex KB integrity rule, but unrelated to the current shell-page failure.
future_optional_change:
  - "If Phase 2 pages cite historical paths, page templates may reference this file as a review concern."
behavior_to_avoid:
  - "Do not combine historical-path lint with page-value contract."
```

---

## 3.12 `.claude/skills/apex-kb/templates/ingest-analysis-template.md`

### Macro role

Phase 1 semantic payload that Phase 2 consumes.

It already includes source identity, source summary, extraction candidates, concept/entity candidates, key claims, contradictions/open questions, and proposed Phase 2 changes.

### Meso change

Strengthen proposed Phase 2 outputs so Phase 2 receives the right payload.

```yaml
change_needed: yes
change_size: medium
section_to_change:
  - "## 8. Proposed Phase 2 Changes"
meso_update:
  - "Add adaptive ranked_source_set field to proposed summaries/concepts/entities."
  - "Add macro_meso_micro_notes or level_specific_value field."
  - "Add key_claim_ids_to_carry."
  - "Add route_questions."
  - "Add raw_source_reopen_triggers."
  - "Drop source_cluster_map from required fields."
behavior_to_create:
  - "Phase 1 hands Phase 2 enough source-routing material."
  - "Phase 2 does not collapse rich Phase 1 analysis into generic YAML."
behavior_to_avoid:
  - "Do not add massive concept/entity matrices."
  - "Do not force fixed source counts."
```

---

## 3.13 `.claude/skills/apex-kb/templates/wiki-page-templates.md`

### Macro role

Main Phase 2 page-generation contract.

Current template has correct frontmatter, but body sections allow low-value pages: summary pages can be `Core Summary`, `What This Adds`, `Key Claims`, `Contradictions`, `Open Questions`; concept pages can be `Definition`, `Operating Rules`, `Relationships`, `Evidence`, `Contradictions and Open Questions`; entity pages can be `Identity`, `Source-Grounded Summary`, `Known Relationships`, `Evidence`, `Open Questions`.

### Meso change

This is the central file to patch.

```yaml
change_needed: yes
change_size: large_relative_to_other_files
sections_to_change:
  - "Shared frontmatter"
  - "Summary page"
  - "Concept page"
  - "Entity page"
new_shared_contract:
  - "Phase 2 page-value contract."
  - "Adaptive ranked source set required."
  - "Macro / meso / micro required."
  - "Shell-page anti-patterns named."
summary_page_meso_sections:
  - Core Summary
  - Ranked Source Set
  - Macro / Meso / Micro
  - Key Claims
  - Routes Here
  - Uncertainty / Raw Source Triggers
concept_page_meso_sections:
  - Definition
  - Ranked Source Set
  - Macro / Meso / Micro
  - Key Claims
  - Use / Do Not Use
  - Routes Here
  - Uncertainty / Raw Source Triggers
entity_page_meso_sections:
  - Identity
  - Ranked Source Set
  - Macro / Meso / Micro
  - Role and Boundaries
  - Key Claims
  - Routes Here
  - Uncertainty / Raw Source Triggers
index_page_meso_sections_to_add_if_template_exists_or_future_add:
  - KB Purpose
  - Read First
  - Route by Question
  - Ranked Source Families / Ranked Source Set
  - Macro / Meso / Micro KB Map
  - Open Risks
  - Auto-Generated Page Catalog
behavior_to_avoid:
  - "No fixed 2-5 source cap."
  - "No source_cluster_map required section."
  - "No page_value_score."
  - "No 20+ field schema."
```

---

## 3.14 `.claude/skills/apex-kb/templates/query-output-template.md`

### Macro role

Template for saved query outputs.

It already includes evidence pages, source refs, citations, gaps/open questions, and reuse notes.

### Meso change

Small optional change.

```yaml
change_needed: optional
change_size: small
section_to_change:
  - "## Evidence Pages"
  - "## Gaps / Open Questions"
meso_update:
  - "Allow query packets to record which Phase 2 route questions were used."
  - "Allow query packets to record whether raw-source reopen was triggered."
behavior_to_create:
  - "Query outputs benefit from route-by-question and raw-source trigger logic."
behavior_to_avoid:
  - "Do not make query packets part of Phase 2 page template."
```

Recommendation: not required for first patch.

---

## 3.15 `.claude/skills/apex-kb/templates/kb-schema-template.md`

### Macro role

Starter KB-local schema: authority levels, taxonomy, language policy, operator-review policy.

It currently defines top-level taxonomy entries including source custody, lifecycle, concepts, entities, summaries, contradictions, and open questions.

### Meso change

Small recommended change.

```yaml
change_needed: yes
change_size: small
section_to_change:
  - "kb_concept_taxonomy_top_level"
  - "kb_operator_review_policy"
meso_update:
  - "Add source_routing or ranked_sources as taxonomy concept."
  - "Add macro_meso_micro as synthesis policy."
  - "Add page_value_contract reference under operator review policy."
behavior_to_create:
  - "New KBs know that ranked source sets and macro/meso/micro are core KB concepts."
behavior_to_avoid:
  - "Do not make KB schema domain-specific."
```

---

## 3.16 `.claude/skills/apex-kb/templates/source-manifest-template.json`

### Macro role

Starter source custody manifest.

It records source ID, type, storage mode, paths, hashes, ingest status, generated pages, and review flags.

### Meso change

No immediate change.

```yaml
change_needed: no
reason: >
  Ranked source sets are authored in Phase 1/Phase 2 pages, not in the raw source
  custody manifest.
future_optional_change:
  - "If source-payload-manifest work continues, keep it as a companion manifest, not here."
behavior_to_avoid:
  - "Do not overload source-manifest with semantic ranking."
```

---

## 3.17 `.claude/skills/apex-kb/examples/powershell-commands.md`

### Macro role

Operator examples for local command execution.

### Meso change

Optional after contract patch.

```yaml
change_needed: optional_later
reason: >
  If examples include Phase 2 or acceptance-like wiki fixtures, update them after
  wiki-page-templates.md and acceptance-tests.md are patched.
meso_update:
  - "Ensure examples do not show shell-page wiki fixtures."
  - "Ensure examples do not imply fixed source count."
behavior_to_avoid:
  - "Do not update examples before the contract files are settled."
```

---

## 3.18 `.claude/skills/apex-kb/examples/lifecycle-runbook.md`

### Macro role

Operator lifecycle runbook.

### Meso change

Optional after contract patch.

```yaml
change_needed: optional_later
reason: >
  Runbook should reflect Phase 2 value expectations, but it is not the contract source.
meso_update:
  - "Add note that Phase 2 approval means page-value compile, not file-count compile."
  - "Add stop condition if pages are shells."
behavior_to_avoid:
  - "Do not turn runbook into a second template."
```

---

## 3.19 `apex-meta/scripts/apex_kb.py`

### Macro role

Deterministic lifecycle helper.

It currently owns deterministic checks such as frontmatter, paths, wikilinks, orphan pages, and index freshness.

### Meso change

No script change in this phase.

```yaml
change_needed: no_current_patch
reason: >
  The current change is LLM/template contract design, not deterministic script behavior.
future_possible_change:
  - "Add lightweight mechanical shell-page warning only after template contract is merged."
allowed_future_mechanical_checks:
  - "missing required headings"
  - "frontmatter plus body below minimal line threshold"
  - "no Ranked Source Set heading"
  - "no Macro / Meso / Micro heading"
  - "no Routes Here heading"
not_allowed_future_checks:
  - "semantic quality scoring"
  - "LLM-like relevance judgment"
  - "page_value_score"
behavior_to_avoid_now:
  - "Do not modify Python."
```

---

## 3.20 `apex-meta/scripts/apex_kb_retrieval.py`

### Macro role

Derived retrieval index builder/query tool.

The retrieval contract says retrieval indexes are rebuildable and never canonical, and that retrieval should use JSON/NDJSON plus SQLite FTS5/BM25 when available.

### Meso change

No script change.

```yaml
change_needed: no
reason: >
  The retrieval engine should benefit from better compiled pages naturally. It does
  not need a patch to understand the new contract.
future_possible_change:
  - "Boost headings like Ranked Source Set, Macro / Meso / Micro, Key Claims, Routes Here in retrieval if needed."
behavior_to_avoid:
  - "Do not patch retrieval before the page contract exists."
  - "Do not add vector retrieval."
```

---

## 4. Prioritized Macro/Meso Patch Waves

### Wave 1 — Core Phase 2 value contract

```yaml
wave_1:
  purpose: "Stop shell pages at the LLM/template contract layer."
  files:
    - ".claude/skills/apex-kb/SKILL.md"
    - ".claude/skills/apex-kb/references/kb-contract.md"
    - ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"
    - ".claude/skills/apex-kb/templates/wiki-page-templates.md"
    - ".claude/skills/apex-kb/templates/ingest-analysis-template.md"
    - ".claude/skills/apex-kb/references/acceptance-tests.md"
  must_include:
    - adaptive_ranked_source_set
    - macro_meso_micro
    - key_claims
    - route_by_question
    - uncertainty_raw_source_triggers
  must_exclude:
    - fixed_source_count
    - source_cluster_map_required
    - page_value_score
    - Python semantic scoring
```

### Wave 2 — Lifecycle/schema alignment

```yaml
wave_2:
  purpose: "Make surrounding contracts reflect the new Phase 2 value contract."
  files:
    - ".claude/skills/apex-kb/references/lifecycle-state-machine.md"
    - ".claude/skills/apex-kb/references/knowledge-promotion-rules.md"
    - ".claude/skills/apex-kb/templates/kb-schema-template.md"
  changes:
    - "S6_phase2_ready mentions page-value contract."
    - "Promotion rules prevent shell pages becoming accepted doctrine."
    - "New KB schema includes source routing and macro/meso/micro synthesis policy."
```

### Wave 3 — Optional examples/query alignment

```yaml
wave_3:
  purpose: "Make examples and query outputs reflect the new contract."
  files:
    - ".claude/skills/apex-kb/templates/query-output-template.md"
    - ".claude/skills/apex-kb/examples/powershell-commands.md"
    - ".claude/skills/apex-kb/examples/lifecycle-runbook.md"
  changes:
    - "Query outputs may record route question and raw-source trigger."
    - "Examples do not show shell pages."
    - "Runbook clarifies Phase 2 approval means value compile, not file-count compile."
```

### Wave 4 — Future deterministic support

```yaml
wave_4_future_only:
  purpose: "Optional mechanical shell-page lint after templates stabilize."
  files:
    - "apex-meta/scripts/apex_kb.py"
    - ".claude/skills/apex-kb/references/script-command-contract.md"
  allowed:
    - missing_heading_warning
    - frontmatter_plus_tiny_body_warning
    - missing_ranked_source_set_heading_warning
    - missing_macro_meso_micro_heading_warning
    - missing_routes_here_heading_warning
  forbidden:
    - semantic quality score
    - source relevance judgment
    - fixed ranked source count
```

---

## 5. Final Decision Matrix

|item|final decision|implementation level|
|---|---|---|
|ranked source set|**Keep and upgrade**|Required, adaptive, proportional to KB/topic breadth|
|source cluster map|**Drop from required patch**|Future optional large-KB feature|
|macro / meso / micro|**Keep**|Required synthesis section|
|relationships / crosslinks|**Merge**|Route-by-question, next reads, related pages|
|contradictions|**Merge**|Uncertainty / raw-source triggers|
|open questions|**Merge**|Uncertainty / raw-source triggers|
|route by question|**Keep**|Required|
|raw source reading path|**Merge**|Raw-source reopen triggers|
|future LLM use|**Merge**|Covered by macro/meso/micro and route-by-question|
|page value score|**Drop**|Too gameable|
|broad concept minimum source count|**Drop as fixed rule**|Replace with adaptive ranked source set|
|shell page lint|**Future only**|Mechanical warning after template contract|
|information density threshold|**Drop as numeric threshold**|Replace with required value sections|

## 6. Next Step

The next chat should not patch everything. It should take **one file** and produce the **micro-level exact patch** for that file only.

Recommended first file:

```text
.claude/skills/apex-kb/templates/wiki-page-templates.md
```

Reason: it is the central Phase 2 behavior surface. Once that file is correct, the other files can align around it.