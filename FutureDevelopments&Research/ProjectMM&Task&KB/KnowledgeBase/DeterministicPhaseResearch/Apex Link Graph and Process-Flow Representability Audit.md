# Apex Link Graph and Process-Flow Representability Audit

## 1. Verdict

- **Graph useful now:** **partial**
- **Main reason:** Apex already has strong deterministic graph signals, but not mostly as Markdown links. The useful edges are mainly in `.claude/Claude.md`, skill manifests, YAML-style path fields, `owns`, `hands_off_to`, `does_not_own`, `canonical_source`, `supporting_files`, and explicit process sequences.
- **Recommended phase:** **V1.5**
- **Need Obsidian app:** **no**

Important constraint: I did **not** have a local Windows checkout to run a whole-repo regex crawler. I executed this as a read-only repo/project audit through available repository/project file access, without Codex and without write/PR/issue/comment flows. So the edge counts below are **inspected-sample counts**, not exhaustive local crawl counts.

Downloadable artifact files:

- link-graph.sample.json
- graph-summary.md
    
    ```
    # Apex Link Graph Summary## Verdict- Graph useful now: partial- Main reason: deterministic process and package edges exist, but they are mostly encoded as YAML/path fields and prose sequence blocks rather than dense Markdown links or wikilinks.- Recommended extraction phase: V1.5- Need Obsidian app: no## SummaryThe current repo can already produce a useful file graph for LLM navigation if the extractor supports:- explicit path strings,- package manifest `file_list` / `supporting_files`,- `canonical_source`, `script_path`, `hands_off_to`, `owns`, `does_not_own`,- explicit arrow/sequence text,- skill index entries in `.claude/Claude.md`.A pure Obsidian-style parser that only reads `[text](path)` and `[[wikilinks]]` would undercount the graph heavily.## Strong hubs| Hub | Why ||---|---|| `.claude/Claude.md` | Defines core loop, skill index, artifact paths, present/missing skill status. || `.claude/skills/PrecapNextDay/Skill_precap-next-day.md` | Defines daily plan outputs, flow packets, prompt packs, dependency interfaces, FlowRecap handoff. || `.claude/skills/PrecapNextDay/precap-next-day-package-manifest.md` | Dense package file index with many explicit paths. || `.claude/skills/apex-kb/SKILL.md` | Defines KB modes, data layout, ownership, boundaries, handoffs to plan/session/sync. || `.claude/skills/apex-kb/package-manifest.md` | Dense KB file inventory and runtime script reference. || `.claude/skills/apex-sync/SKILL.md` | Script-backed deterministic sync boundary. || `.claude/skills/apex-session/SKILL.md` | Session mutation and handoff boundary. |## Weak spots- `FlowRecap` and `status-merge/APSU` are represented in loop/index references but are marked missing in the current `.claude/Claude.md` skill index.- Many support paths are relative and would require path normalization.- Wikilinks exist in repo/source snapshots, but not as the main Apex process graph mechanism.- Markdown links appear less important than YAML-ish path references and package manifests.## V1.5 output setRecommended files:```textapex-meta/kb/claude-skill-design/manifests/link-graph.sample.jsonapex-meta/kb/claude-skill-design/manifests/graph-summary.mdapex-meta/kb/claude-skill-design/manifests/process-flow-graph-audit.md```
    ```
    
- process-flow-graph-audit.md
    
    ```
    # Apex Link Graph and Process-Flow Representability Audit## 1. Verdict- Graph useful now: partial- Main reason: enough deterministic edges exist for the central loop and package boundaries, but many relationships are encoded as YAML/path/prose conventions rather than Markdown links.- Recommended phase: V1.5- Need Obsidian app: no## 2. Plain-language explanationA link graph is a map of which files point to which other files, processes, scripts, contracts, and outputs. For a human, it is like an index with arrows. For an LLM, it is a navigation layer: instead of rereading everything, the LLM can start at hub files, follow explicit references, and avoid guessing.## 3. Evidence Table| Relation type | Found? | Count in inspected sample | Example source | Example target | Useful for LLM? | Notes ||---|---:|---:|---|---|---:|---|| Markdown links `[text](path)` | weak/partial | not exhaustively counted | repo source snapshots | varied | medium | Not the dominant Apex graph signal. || Wikilinks `[[target]]` | yes, but mostly blueprint/source snapshots | search returned at least 20 files | llm-wiki / gsd / source repos | varied | medium | Useful for KB/wiki graph, less central to Apex process graph. || Explicit file references | yes | high | `.claude/Claude.md` | skill paths | high | Main V1 graph source. || YAML path references | yes | high | package manifests and SKILL contracts | references/templates/scripts | high | Must be parsed beyond Markdown-link regex. || Process sequence references | yes | several strong | `.claude/Claude.md`, `AnotherMetaLevelFlow.md` | core loop stages | high | Deterministic edges exist. || Contract dependency references | yes | high | Apex KB / Sync / Session / PreCapNextDay skill files | owns/hands_off_to/does_not_own/canonical_source | high | Main boundary map. |## 4. Hub Files| File | Incoming links | Outgoing links | Why it matters ||---|---:|---:|---|| `.claude/Claude.md` | high conceptual | high | Core loop, skill index, artifact paths, present/missing status. || `.claude/skills/PrecapNextDay/Skill_precap-next-day.md` | medium | high | Connects daily planning to flow packets, prompt packs, usage tracking, workflow validation, FlowRecap handoff. || `.claude/skills/PrecapNextDay/precap-next-day-package-manifest.md` | medium | very high | Best package-level path map. || `.claude/skills/apex-kb/SKILL.md` | medium | high | KB modes, data layout, ownership, handoffs. || `.claude/skills/apex-kb/package-manifest.md` | medium | high | KB file inventory and script path. || `.claude/skills/apex-sync/SKILL.md` | medium | medium | Deterministic script-backed sync boundary. || `.claude/skills/apex-session/SKILL.md` | medium | medium | Session/handoff/mutation boundary. |## 5. Orphan / Weakly Connected Files| File/concept | Reason | Suggested fix ||---|---|---|| `.claude/skills/flow-recap/Skill_flow-recap.md` | Referenced in `.claude/Claude.md` but marked missing there. | Add installed skill or update status/path. || `.claude/skills/status-merge/Skill_status-merge.md` | Referenced in `.claude/Claude.md` but marked missing there. | Add installed skill or update status/path. || Older `ApexDefinition&OldVersions/...` files | Rich process semantics but mostly legacy location. | Add source-manifest classification and canonical/legacy status. || Source snapshots under `source-knowledge/ProjectRepos/` | Many links/scripts but not canonical Apex process edges. | Keep in graph as blueprint/source nodes, not active process nodes. |## 6. Process Flow Representation| Flow | Deterministic edges found? | Files involved | Missing links | Recommendation ||---|---:|---|---|---|| PreCapWeek → PreCapNextDay → FlowRecap → status merge | partial/yes | `.claude/Claude.md`, `AnotherMetaLevelFlow.md`, PreCapNextDay skill/manifest | FlowRecap and status-merge active skill files missing by `.claude/Claude.md` index | V1.5 graph can represent as concept edges plus missing-node flags. || Apex KB scaffold → ingest_phase_1 → ingest_phase_2 → query/lint/audit | yes | `.claude/skills/apex-kb/SKILL.md`, package manifest, script contract | None major for package-level graph | Build as deterministic mode-sequence edges. || Apex Plan → Apex Sync → Apex Session handoff boundaries | partial | Apex Sync/Session installed; Apex Plan source visible in project context but not fully fetched in this pass | Need current `.claude/skills/apex-plan` files in local scan | V1.5 should parse `owns`, `hands_off_to`, `does_not_own`. || Prompt engineering → AI routing → workflow-process-design → PreCapNextDay | partial/yes | PromptEngineer, AIRouting, Workflow&Processes, PreCapNextDay | Some files use malformed/collapsed YAML style; path normalization needed | V1.5 should parse package interfaces and dependency interfaces. |## 7. Script vs LLM Boundary| Relationship | Script can detect? | LLM needed? | Reason ||---|---:|---:|---|| Explicit path fields | yes | no | Regex/YAML-lite extraction sufficient. || `owns`, `hands_off_to`, `does_not_own` | yes | no for edge existence; yes for meaning quality | Edge is deterministic; significance may need LLM. || Arrow sequences | yes | no | Explicit `A → B` text is parseable. || Whether FlowRecap semantically depends on a raw dump | partial | yes | Direct path/field edges can be detected; operational meaning needs interpretation. || Whether legacy files are canonical | partial | yes | Path names imply old status, but authority requires context. || Whether a process should be refactored | no | yes | Design judgment. || Whether prompt-engineering should precede PreCapNextDay | partial | yes | Dependency interfaces exist; build-order priority is design semantics. |## 8. Recommended Graph Artifact Schema```json{  "metadata": {    "repo": "owner/name",    "generated_at": "ISO-8601",    "scope_roots": [],    "extractor_version": "v1.5"  },  "nodes": [    {      "id": "path-or-concept",      "type": "file | skill | contract | script | process | artifact | concept",      "path": "optional/repo/path.md",      "status": "present | missing | legacy | inferred_semantic"    }  ],  "edges": [    {      "source": "node-id",      "target": "node-id",      "type": "markdown_link | wikilink | explicit_file_reference | yaml_path_reference | process_sequence | contract_dependency | owns | hands_off_to | does_not_own | script_path",      "evidence_text": "short excerpt",      "source_line": 0,      "confidence": "deterministic | semantic_relationship_llm_needed"    }  ],  "summaries": {    "hub_files": [],    "orphans": [],    "missing_targets": [],    "process_flows": []  }}```## 9. Final RecommendationBuild this into Phase 0 as V1.5, not V1 and not V2.V1 would be too weak if it only counts Markdown links and wikilinks. V2 would be overbuilt if it tries semantic graph construction before the deterministic corpus layer exists.Exact output files:```textapex-meta/kb/claude-skill-design/manifests/link-graph.sample.jsonapex-meta/kb/claude-skill-design/manifests/graph-summary.mdapex-meta/kb/claude-skill-design/manifests/process-flow-graph-audit.md```Do not require Obsidian. The graph should be a deterministic repo artifact that Obsidian could later consume, not an Obsidian-specific feature.
    ```
    

---

## 2. Plain-language explanation

A link graph is a map of which files, processes, contracts, scripts, and outputs point to each other.

For a human, it is like a structured index with arrows. For an LLM, it is more important: it prevents blind reading. Instead of asking the LLM to inspect everything, the graph says:

```
Start here → this file owns the loopThen read this skill → it produces this artifactThen follow this manifest → it points to contracts/templates/scriptsStop here → this relationship is only semantic and needs LLM interpretation
```

For Apex, the graph should **not** be an Obsidian visual graph. It should be a deterministic Phase 0 repo artifact.

---

## 3. Evidence Table

|Relation type|Found?|Count|Example source|Example target|Useful for LLM?|Notes|
|---|---|---|---|---|---|---|
|Markdown links `[text](path)`|Weak/partial|Not exhaustively counted|source/blueprint files|varied|Medium|Not the dominant Apex signal.|
|Wikilinks `[[target]]`|Yes, mostly in blueprint/source snapshots|Search returned at least 20 files|LLM-Wiki / GSD / source repos|varied|Medium|Useful for KB/wiki graph, less central to Apex process graph.|
|Explicit file references|Yes|High in inspected files|`.claude/Claude.md`|`.claude/skills/PrecapNextDay/Skill_precap-next-day.md`|High|Main V1 graph source. `.claude/Claude.md` contains a skill index with paths and statuses.|
|YAML path references|Yes|High|PreCapNextDay manifest|references/templates/examples|High|PreCapNextDay manifest has dense file-list path references.|
|Process sequence references|Yes|Several strong|`.claude/Claude.md`, `AnotherMetaLevelFlow.md`|PreCapWeek → PreCapNextDay → FlowRecap → APSU/status-merge|High|Core loop is explicit in both current control file and architecture spec.|
|Contract dependency references|Yes|High|Apex KB / Sync / Session / PreCapNextDay skills|`owns`, `hands_off_to`, `does_not_own`, `script_path`|High|Apex KB, Sync, Session expose machine-readable ownership/boundary fields.|

---

## 4. Hub Files

|File|Incoming links|Outgoing links|Why it matters|
|---|---|---|---|
|`.claude/Claude.md`|High conceptual|High|Defines Apex identity, core loop, skill index, skill paths, artifact paths, missing/present status.|
|`.claude/skills/PrecapNextDay/Skill_precap-next-day.md`|Medium|High|Defines daily plan, flow packets, prompt packs, dependency interfaces, FlowRecap handoff, and boundary against status merge.|
|`.claude/skills/PrecapNextDay/precap-next-day-package-manifest.md`|Medium|Very high|Best package-level file graph: entrypoint, references, templates, examples, handoff examples.|
|`.claude/skills/apex-kb/SKILL.md`|Medium|High|Defines KB modes, data layout, ownership, handoffs to Apex Plan/Session/Sync, and source policy.|
|`.claude/skills/apex-kb/package-manifest.md`|Medium|High|Defines package inventory, runtime script path, source trace, required KB paths.|
|`.claude/skills/apex-sync/SKILL.md`|Medium|Medium|Defines deterministic read-side sync and script boundary via `scripts/apex_sync.py`.|
|`.claude/skills/apex-session/SKILL.md`|Medium|Medium|Defines session mutation, handoff artifacts, status enum, raw-source preservation, and non-script boundary.|

---

## 5. Orphan / Weakly Connected Files

|File / concept|Reason|Suggested fix|
|---|---|---|
|`.claude/skills/flow-recap/Skill_flow-recap.md`|Referenced in `.claude/Claude.md` but marked `missing`.|Install or update the FlowRecap package; otherwise keep as a missing graph node.|
|`.claude/skills/status-merge/Skill_status-merge.md`|Referenced in `.claude/Claude.md` but marked `missing`.|Install or update status-merge/APSU package; otherwise keep as missing graph node.|
|Legacy architecture files under `ApexDefinition&OldVersions/...`|Semantically rich but not clearly canonical.|Add `legacy|
|Source snapshots under `source-knowledge/ProjectRepos/`|Many links/scripts, but not active Apex process files.|Include as blueprint/source nodes, not active process-owner nodes.|
|PromptEngineer / AIRouting / Workflow&Processes packages|They contain useful dependency edges but some formatting is collapsed or nonstandard.|V1.5 parser should be YAML-lite tolerant, not strict-YAML-only.|

---

## 6. Process Flow Representation

|Flow|Deterministic edges found?|Files involved|Missing links|Recommendation|
|---|---|---|---|---|
|**PreCapWeek → PreCapNextDay → FlowRecap → status merge**|**Partial / yes**|`.claude/Claude.md`, `AnotherMetaLevelFlow.md`, PreCapNextDay skill/manifest|FlowRecap and status-merge are referenced but marked missing in `.claude/Claude.md`.|Represent as deterministic concept/process edges plus missing-file flags.|
|**Apex KB scaffold → ingest_phase_1 → ingest_phase_2 → query/lint/audit**|**Yes**|`.claude/skills/apex-kb/SKILL.md`, package manifest, script contract path|No major package-level gap.|Build as deterministic mode-sequence edges.|
|**Apex Plan → Apex Sync → Apex Session handoff boundaries**|**Partial**|Apex Sync and Apex Session installed; Apex KB hands off to plan/session/sync|Need full current Apex Plan package scan.|Parse `owns`, `hands_off_to`, `does_not_own`, script boundaries.|
|**Prompt engineering → AI routing → workflow-process-design → PreCapNextDay**|**Partial / yes**|PromptEngineer, AIRouting, Workflow&Processes, PreCapNextDay|Some package files use collapsed YAML/code-fence formatting.|V1.5 parser should extract dependencies from both formatted YAML and prose-like YAML blocks.|

---

## 7. Script vs LLM Boundary

|Relationship|Script can detect?|LLM needed?|Reason|
|---|---|---|---|
|Explicit file paths|Yes|No|Regex/YAML-lite extraction is enough.|
|Markdown links / wikilinks|Yes|No|Standard extraction.|
|`supporting_files.path`, `script_path`, `canonical_source`|Yes|No|Deterministic path fields.|
|`owns`, `hands_off_to`, `does_not_own`|Yes|No for edge existence; yes for quality interpretation|Edge exists deterministically; significance can need interpretation.|
|Arrow sequences|Yes|No|Explicit `A → B → C` or numbered loop is parseable.|
|“PreCapNextDay depends on prompt-engineering quality”|Partial|Yes|Some dependency interfaces are explicit, but build-order significance is semantic.|
|“Legacy file should be canonicalized”|No|Yes|Requires design judgment.|
|“FlowRecap should create exactly X status delta semantics”|Partial|Yes|Edge can be detected; operational interpretation needs LLM.|

---

## 8. Recommended Graph Artifact Schema

```
{  "metadata": {    "repo": "owner/name",    "generated_at": "ISO-8601",    "scope_roots": [],    "extractor_version": "v1.5"  },  "nodes": [    {      "id": "path-or-concept",      "type": "file | skill | contract | script | process | artifact | concept",      "path": "optional/repo/path.md",      "status": "present | missing | legacy | inferred_semantic"    }  ],  "edges": [    {      "source": "node-id",      "target": "node-id",      "type": "markdown_link | wikilink | explicit_file_reference | yaml_path_reference | process_sequence | contract_dependency | owns | hands_off_to | does_not_own | script_path",      "evidence_text": "short excerpt",      "source_line": 0,      "confidence": "deterministic | semantic_relationship_llm_needed"    }  ],  "summaries": {    "hub_files": [],    "orphans": [],    "missing_targets": [],    "process_flows": []  }}
```

---

## 9. Final Recommendation

Build this into **Phase 0** as **V1.5**.

**Why not V1:** A V1 parser that only counts Markdown links and wikilinks would miss the main Apex graph. The main graph is in YAML/path fields, manifests, and contract/boundary fields.

**Why not V2:** A semantic graph is premature. First create deterministic graph artifacts that the LLM can read.

Exact repo outputs should be:

```
apex-meta/kb/claude-skill-design/manifests/link-graph.sample.jsonapex-meta/kb/claude-skill-design/manifests/graph-summary.mdapex-meta/kb/claude-skill-design/manifests/process-flow-graph-audit.md
```

The extractor should support:

```
v1_5_extractors:  markdown_links: true  wikilinks: true  explicit_file_paths: true  yaml_lite_path_fields: true  package_manifest_file_list: true  supporting_files: true  canonical_source: true  script_path: true  owns_hands_off_to_does_not_own: true  arrow_sequences: true  missing_target_detection: true
```

This aligns with the skill-package design direction that machine-readable path references and manifests are first-class navigation aids, not merely prose decoration.