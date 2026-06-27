```
# Codex Task — Apex Markdown Link Graph and Process-Flow Representability Audit## 0. MissionAudit whether the Apex repo contains enough explicit Markdown links, wikilinks, file references, contract references, manifest references, and process-flow references to build a useful Obsidian-style / file-reference graph before LLM semantic ingest.This is **not** an Obsidian app task.  This is **not** a visual graph task.  This is **not** semantic ingest.  This is a deterministic local repo analysis task.The output must answer:```textCan the relationships between PreCapWeek, PreCapNextDay, FlowRecap, status merge,Apex KB, Apex Sync, Apex Session, contracts, templates, scripts, and manifests berepresented as a file graph that helps the LLM navigate the repo?
```

Do not create wiki pages.  
Do not run Apex KB Phase 1 semantic ingest.  
Do not use GitHub connector writes, PRs, issues, comments, reviewers, assignees, or external sharing.  
Work only in the local repo file tree.

---

## 1. Start

```
cd C:\GitDev\apexai-os-metagit status --short
```

Report dirty files, but continue unless they conflict with these paths:

```
.claude/skills/apex-meta/kb/apex-meta/scripts/apex-meta/processes/source-knowledge/ProjectRepos/
```

---

## 2. Target areas

Inspect these areas if present:

```
.claude/skills/apex-meta/kb/claude-skill-design/apex-meta/kb/apex-meta/scripts/apex-meta/processes/source-knowledge/ProjectRepos/
```

Prioritize these concepts:

```
priority_concepts:  - PreCapWeek  - PreCapNextDay  - FlowRecap  - status-merge  - AllProjectStatusPacketUpdate  - APSU  - Apex KB  - apex-kb  - Apex Sync  - apex-sync  - Apex Session  - apex-session  - prompt-engineering  - ai-routing-and-usage-tracking  - workflow-process-design  - ingest-analysis  - source-manifest  - script-command-contract  - kb-contract  - flow-packet  - prompt-pack
```

---

## 3. Extract deterministic graph signals only

Extract these relation types:

```
relation_types:  markdown_links:    pattern: "[text](path)"  wikilinks:    pattern: "[[target]] or [[target|alias]]"  explicit_file_references:    examples:      - ".claude/skills/apex-kb/SKILL.md"      - "references/kb-contract.md"      - "apex-meta/scripts/apex_kb.py"  yaml_path_references:    examples:      - package_path      - script_path      - canonical_rules      - supporting_files.path      - canonical_source      - source_trace      - package_manifest.file_list.path  process_sequence_references:    examples:      - "PreCapWeek → PreCapNextDay → FlowRecap"      - "Phase 0 → Phase 1 → Phase 2"      - "Apex Plan → Apex Sync → Apex Session"  contract_dependency_references:    examples:      - read_when      - canonical_source      - hands_off_to      - hands_off_to_apex_sync      - hands_off_to_apex_session      - owns      - does_not_own      - source_trace
```

Strict rule:

```
Do not invent edges because concepts sound related.Only count an edge as deterministic if it appears as:- Markdown link- wikilink- explicit path reference- YAML path field- package manifest reference- supporting_files reference- owns / does_not_own / hands_off_to relation- canonical_source relation- read_when relation- explicit arrow / sequence in textAnything else must be marked:semantic relationship — LLM needed
```

---

## 4. Build graph artifacts

Create these files:

```
apex-meta/kb/claude-skill-design/manifests/link-graph.sample.jsonapex-meta/kb/claude-skill-design/manifests/graph-summary.mdapex-meta/kb/claude-skill-design/manifests/process-flow-graph-audit.md
```

Create the manifests directory if missing.

Do not modify any other files.

---

## 5. Required JSON shape for `link-graph.sample.json`

Use this minimal schema:

```
{  "graph_metadata": {    "schema_version": "0.1",    "generated_at": "YYYY-MM-DDTHH:MM:SSZ",    "repo_root": "C:/GitDev/apexai-os-meta",    "scope": [      ".claude/skills/",      "apex-meta/kb/",      "apex-meta/scripts/",      "apex-meta/processes/",      "source-knowledge/ProjectRepos/"    ],    "edge_policy": "deterministic_explicit_edges_only"  },  "nodes": [    {      "id": "normalized/repo/path.md",      "path": "normalized/repo/path.md",      "node_type": "skill | contract | template | manifest | script | process | source | unknown",      "priority_concepts": ["apex-kb", "source-manifest"]    }  ],  "edges": [    {      "source": "normalized/source/path.md",      "target": "normalized/target/path.md or concept:PreCapWeek",      "relation_type": "markdown_link | wikilink | explicit_file_reference | yaml_path_reference | process_sequence | contract_dependency",      "relation_key": "supporting_files.path | canonical_source | owns | hands_off_to | read_when | explicit_arrow | null",      "raw_text": "short raw evidence excerpt",      "deterministic": true,      "confidence": "high | medium | low"    }  ],  "semantic_candidates": [    {      "source": "normalized/source/path.md",      "target": "concept:SomeConcept",      "reason": "Mentioned in prose but no explicit edge syntax.",      "requires_llm": true    }  ],  "summary": {    "node_count": 0,    "edge_count": 0,    "semantic_candidate_count": 0,    "orphan_count": 0,    "hub_count": 0  }}
```

Path normalization rules:

```
path_normalization:  use_forward_slashes: true  remove_repo_root_prefix: true  preserve_relative_paths_when_target_unresolved: true  unresolved_targets_prefix: "unresolved:"  concept_targets_prefix: "concept:"
```

---

## 6. Required analysis questions

Answer these in `process-flow-graph-audit.md`:

1. Do the files already contain enough explicit links to build a useful graph?
2. Are the relationships mostly implicit in prose instead of explicit Markdown/file references?
3. Which files are graph hubs?
4. Which files are orphans?
5. Which process flows are representable as deterministic edges?
6. Which relationships require LLM semantic interpretation and cannot be safely inferred by script?
7. Should Apex add explicit links/frontmatter to improve future graph quality?
8. Would this graph help Phase 1 LLM semantic ingest?
9. Should graph extraction be V1, V1.5, or V2?

---

## 7. Required Markdown output structure

Use this exact structure in:

```
apex-meta/kb/claude-skill-design/manifests/process-flow-graph-audit.md
```

```
# Apex Link Graph and Process-Flow Representability Audit## 1. Verdict- Graph useful now: yes/no/partial- Main reason:- Recommended phase: V1 / V1.5 / V2- Need Obsidian app: no## 2. Plain-language explanationExplain what a link graph is in non-programmer terms.## 3. Evidence Table| Relation type | Found? | Count | Example source | Example target | Useful for LLM? | Notes |## 4. Hub Files| File | Incoming links | Outgoing links | Why it matters |## 5. Orphan / Weakly Connected Files| File | Reason | Suggested fix |## 6. Process Flow Representation| Flow | Deterministic edges found? | Files involved | Missing links | Recommendation |Include these flows:- PreCapWeek → PreCapNextDay → FlowRecap → status merge- Apex KB scaffold → ingest_phase_1 → ingest_phase_2 → query/lint/audit- Apex Plan → Apex Sync → Apex Session handoff boundaries- Prompt engineering → AI routing → workflow-process-design → PreCapNextDay## 7. Script vs LLM Boundary| Relationship | Script can detect? | LLM needed? | Reason |## 8. Recommended Graph Artifact SchemaShow a minimal JSON schema for `link-graph.json`.## 9. Final RecommendationState whether this should be built into Phase 0 and what exact output files it should produce.
```

Use this exact structure in:

```
apex-meta/kb/claude-skill-design/manifests/graph-summary.md
```

```
# Apex Graph Summary## Counts| Metric | Count |## Top Hubs| File | Incoming | Outgoing |## Top Orphans| File | Reason |## Strongest Deterministic Flows| Flow | Evidence |## Weakest / Missing Edges| Missing relationship | Suggested explicit link/frontmatter fix |## Codex NotesShort notes on how the graph was extracted and where extraction was uncertain.
```

---

## 8. Implementation guidance

Use deterministic parsing. A simple script is acceptable.

Preferred approach:

```
implementation:  language: "Python or Node; choose what is already easiest in the repo"  allowed:    - recursive file scan    - regex extraction for Markdown links    - regex extraction for wikilinks    - regex/path heuristics for explicit file references    - YAML/frontmatter parsing if safe    - simple line-based extraction for owns/hands_off_to/read_when/canonical_source  not_allowed:    - LLM semantic interpretation    - wiki generation    - external APIs    - GitHub connector writes    - Obsidian app dependency
```

Suggested extraction targets:

```
*.md*.markdown*.yml*.yaml*.json*.py*.ps1*.sh*.txt
```

Only include scripts as graph nodes if they are explicitly referenced or match priority package paths.

---

## 9. Completion report

After writing the three artifacts, print:

```
# Completion Report## Files written| Path | Status |## Counts| Metric | Count |## Verdict- Graph useful now:- Recommended graph phase:- Main blocker:## Important caveatState clearly that the graph contains only deterministic explicit edges and does not represent all semantic relationships in Ap
```