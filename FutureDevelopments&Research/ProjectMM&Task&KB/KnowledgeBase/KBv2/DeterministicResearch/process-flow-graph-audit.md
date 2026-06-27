# Apex Link Graph and Process-Flow Representability Audit

## 1. Verdict

- Graph useful now: partial
- Main reason: enough deterministic edges exist for the central loop and package boundaries, but many relationships are encoded as YAML/path/prose conventions rather than Markdown links.
- Recommended phase: V1.5
- Need Obsidian app: no

## 2. Plain-language explanation

A link graph is a map of which files point to which other files, processes, scripts, contracts, and outputs. For a human, it is like an index with arrows. For an LLM, it is a navigation layer: instead of rereading everything, the LLM can start at hub files, follow explicit references, and avoid guessing.

## 3. Evidence Table

| Relation type | Found? | Count in inspected sample | Example source | Example target | Useful for LLM? | Notes |
|---|---:|---:|---|---|---:|---|
| Markdown links `[text](path)` | weak/partial | not exhaustively counted | repo source snapshots | varied | medium | Not the dominant Apex graph signal. |
| Wikilinks `[[target]]` | yes, but mostly blueprint/source snapshots | search returned at least 20 files | llm-wiki / gsd / source repos | varied | medium | Useful for KB/wiki graph, less central to Apex process graph. |
| Explicit file references | yes | high | `.claude/Claude.md` | skill paths | high | Main V1 graph source. |
| YAML path references | yes | high | package manifests and SKILL contracts | references/templates/scripts | high | Must be parsed beyond Markdown-link regex. |
| Process sequence references | yes | several strong | `.claude/Claude.md`, `AnotherMetaLevelFlow.md` | core loop stages | high | Deterministic edges exist. |
| Contract dependency references | yes | high | Apex KB / Sync / Session / PreCapNextDay skill files | owns/hands_off_to/does_not_own/canonical_source | high | Main boundary map. |

## 4. Hub Files

| File | Incoming links | Outgoing links | Why it matters |
|---|---:|---:|---|
| `.claude/Claude.md` | high conceptual | high | Core loop, skill index, artifact paths, present/missing status. |
| `.claude/skills/PrecapNextDay/Skill_precap-next-day.md` | medium | high | Connects daily planning to flow packets, prompt packs, usage tracking, workflow validation, FlowRecap handoff. |
| `.claude/skills/PrecapNextDay/precap-next-day-package-manifest.md` | medium | very high | Best package-level path map. |
| `.claude/skills/apex-kb/SKILL.md` | medium | high | KB modes, data layout, ownership, handoffs. |
| `.claude/skills/apex-kb/package-manifest.md` | medium | high | KB file inventory and script path. |
| `.claude/skills/apex-sync/SKILL.md` | medium | medium | Deterministic script-backed sync boundary. |
| `.claude/skills/apex-session/SKILL.md` | medium | medium | Session/handoff/mutation boundary. |

## 5. Orphan / Weakly Connected Files

| File/concept | Reason | Suggested fix |
|---|---|---|
| `.claude/skills/flow-recap/Skill_flow-recap.md` | Referenced in `.claude/Claude.md` but marked missing there. | Add installed skill or update status/path. |
| `.claude/skills/status-merge/Skill_status-merge.md` | Referenced in `.claude/Claude.md` but marked missing there. | Add installed skill or update status/path. |
| Older `ApexDefinition&OldVersions/...` files | Rich process semantics but mostly legacy location. | Add source-manifest classification and canonical/legacy status. |
| Source snapshots under `source-knowledge/ProjectRepos/` | Many links/scripts but not canonical Apex process edges. | Keep in graph as blueprint/source nodes, not active process nodes. |

## 6. Process Flow Representation

| Flow | Deterministic edges found? | Files involved | Missing links | Recommendation |
|---|---:|---|---|---|
| PreCapWeek → PreCapNextDay → FlowRecap → status merge | partial/yes | `.claude/Claude.md`, `AnotherMetaLevelFlow.md`, PreCapNextDay skill/manifest | FlowRecap and status-merge active skill files missing by `.claude/Claude.md` index | V1.5 graph can represent as concept edges plus missing-node flags. |
| Apex KB scaffold → ingest_phase_1 → ingest_phase_2 → query/lint/audit | yes | `.claude/skills/apex-kb/SKILL.md`, package manifest, script contract | None major for package-level graph | Build as deterministic mode-sequence edges. |
| Apex Plan → Apex Sync → Apex Session handoff boundaries | partial | Apex Sync/Session installed; Apex Plan source visible in project context but not fully fetched in this pass | Need current `.claude/skills/apex-plan` files in local scan | V1.5 should parse `owns`, `hands_off_to`, `does_not_own`. |
| Prompt engineering → AI routing → workflow-process-design → PreCapNextDay | partial/yes | PromptEngineer, AIRouting, Workflow&Processes, PreCapNextDay | Some files use malformed/collapsed YAML style; path normalization needed | V1.5 should parse package interfaces and dependency interfaces. |

## 7. Script vs LLM Boundary

| Relationship | Script can detect? | LLM needed? | Reason |
|---|---:|---:|---|
| Explicit path fields | yes | no | Regex/YAML-lite extraction sufficient. |
| `owns`, `hands_off_to`, `does_not_own` | yes | no for edge existence; yes for meaning quality | Edge is deterministic; significance may need LLM. |
| Arrow sequences | yes | no | Explicit `A → B` text is parseable. |
| Whether FlowRecap semantically depends on a raw dump | partial | yes | Direct path/field edges can be detected; operational meaning needs interpretation. |
| Whether legacy files are canonical | partial | yes | Path names imply old status, but authority requires context. |
| Whether a process should be refactored | no | yes | Design judgment. |
| Whether prompt-engineering should precede PreCapNextDay | partial | yes | Dependency interfaces exist; build-order priority is design semantics. |

## 8. Recommended Graph Artifact Schema

```json
{
  "metadata": {
    "repo": "owner/name",
    "generated_at": "ISO-8601",
    "scope_roots": [],
    "extractor_version": "v1.5"
  },
  "nodes": [
    {
      "id": "path-or-concept",
      "type": "file | skill | contract | script | process | artifact | concept",
      "path": "optional/repo/path.md",
      "status": "present | missing | legacy | inferred_semantic"
    }
  ],
  "edges": [
    {
      "source": "node-id",
      "target": "node-id",
      "type": "markdown_link | wikilink | explicit_file_reference | yaml_path_reference | process_sequence | contract_dependency | owns | hands_off_to | does_not_own | script_path",
      "evidence_text": "short excerpt",
      "source_line": 0,
      "confidence": "deterministic | semantic_relationship_llm_needed"
    }
  ],
  "summaries": {
    "hub_files": [],
    "orphans": [],
    "missing_targets": [],
    "process_flows": []
  }
}
```

## 9. Final Recommendation

Build this into Phase 0 as V1.5, not V1 and not V2.

V1 would be too weak if it only counts Markdown links and wikilinks. V2 would be overbuilt if it tries semantic graph construction before the deterministic corpus layer exists.

Exact output files:

```text
apex-meta/kb/claude-skill-design/manifests/link-graph.sample.json
apex-meta/kb/claude-skill-design/manifests/graph-summary.md
apex-meta/kb/claude-skill-design/manifests/process-flow-graph-audit.md
```

Do not require Obsidian. The graph should be a deterministic repo artifact that Obsidian could later consume, not an Obsidian-specific feature.
