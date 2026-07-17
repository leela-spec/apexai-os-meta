---
okf_schema: apex.okf.ui-message.v1
message_id: apex-kb.welcome.v2
render_policy: verbatim
next_expected_artifact: manifests/run-config.okf.json
validation_schema: .claude/skills/apex-kb/references/run-config.schema.json
---

# Hey nerd — what should Apex KB build?

Apex KB will first save your choices, then run a read-only preflight, show one compact readback, and wait for confirmation. After confirmation, those choices are locked and every later script reads the same manifest.

## Process value

1. **Configure:** you define the source, target KB folder, primary topic, questions, and options.
2. **Preflight:** scripts check paths, overlap, capabilities, and whether the topic vocabulary is usable. No sources are copied and no analysis runs yet.
3. **Lock:** after your confirmation, the configuration receives a SHA-256 fingerprint. Later stages stop if it changes.
4. **Phase 0:** scripts inventory files, extract titles/headings/dates/duplicates, rank every topic candidate with visible reasons, and produce statistics.
5. **Phase 1:** an AI analyzes only one bounded source batch at a time against locked questions.
6. **Phase 2:** an AI compiles the validated Phase 1 findings into durable wiki pages.
7. **Acceptance:** a separate context verifies that the pages answer the locked questions and that sampled claims are supported.

## Fields to provide

### 1. `paths.source_roots`
Folders containing the real source material.
- Choose the smallest roots that contain the subject.
- Do not point at the future KB output folder.

### 2. `paths.kb_root`
The new permanent Apex KB target folder.
- Recommended: `apex-meta/kb/<kb-slug>`.
- The script creates and owns generated KB artifacts only inside this root.

### 3. `kb.slug`, `kb.title`, `kb.identity`
Stable machine name, human name, and one-sentence subject definition.
- The slug must be lowercase kebab-case.
- The identity prevents a topic being inferred from filenames or chat memory.

### 4. `intent.operator_intent`
What you want the KB to make possible.
- Describe the job, not the implementation.
- Example: “Future AIs must understand the current architecture, its history, and where every important source discusses it.”

### 5. `intent.success_definition`
What must be true when the run is finished.
- Name the questions, source visibility, and query behavior you expect.

### 6. `topic`
The one primary topic for this standard build run.
- Provide a name, strong phrases/aliases, and priority questions.
- Additional topics are intentionally not auto-created. They belong in another run or the future existing-KB update workflow.

### 7. `source_handling.storage_mode`
- `pointer_only` — recommended when sources already live safely in a repository; avoids copying large corpora.
- `copy_into_kb` — choose when the KB must custody independent source copies.
- `snapshot_copy` — choose when a reproducible point-in-time copy is required.

### 8. `phase0.profile`
- `quick` — basic inventory and structure; use only for a small, well-known corpus.
- `standard` — recommended default; inventory, structure, field-separated ranking, duplicates, dates when available, work pack, and statistics.
- `deep` — adds expensive format extraction or process-graph signals where configured; use for large or highly versioned corpora.

### 9. `phase0.graph_signals`
- `off` — recommended default when links/process references are not central.
- `links_only` — include Markdown/wiki links as candidate signals.
- `full_process_edges` — include configured YAML/path/process edges; use only when those relationships materially improve discovery.

### 10. `outputs.tier`
- `analysis_only` — stop after validated Phase 1.
- `compiled_full` — produce and semantically accept durable pages; deterministic retrieval may remain pending.
- `query_ready` — recommended final product; includes semantic acceptance, postflight, and fresh retrieval.

### 11. `paths.explicit_exclusions`
Every intentionally omitted folder, with a reason.
- Generated output, dependencies, caches, and known irrelevant archives should be explicit.

### 12. `execution.route`
- `terminal_backed` — recommended; scripts execute and validate locally.
- `connector_only` — semantic writing only; cannot claim deterministic validation or query readiness.

## Exact input format

Save the following JSON as `manifests/run-config.okf.json`, replacing every example value. Do not add unrecognized fields.

```json
{
  "schema": "apex.kb.run-config.v2",
  "schema_version": "2",
  "config_revision": 1,
  "run_kind": "new_kb",
  "kb": {
    "slug": "replace-with-kb-slug",
    "title": "Replace with human-readable KB title",
    "identity": "This KB explains ..."
  },
  "paths": {
    "source_roots": [
      "repository-relative/or/absolute/source-folder"
    ],
    "kb_root": "apex-meta/kb/replace-with-kb-slug",
    "explicit_exclusions": [
      {
        "path": "path/to/exclude",
        "reason": "generated_output_or_out_of_scope"
      }
    ]
  },
  "intent": {
    "operator_intent": "What this KB must make possible for future users or AIs.",
    "success_definition": "What a successful final KB must answer or support."
  },
  "topic": {
    "topic_id": "primary-topic",
    "name": "Primary Topic",
    "topic_intent": "What must be understood about this topic.",
    "phrases": [
      "strong exact phrase"
    ],
    "aliases": [],
    "supporting_terms": [],
    "ambiguous_terms": [],
    "negative_terms": [],
    "priority_questions": [
      {
        "query_id": "primary-topic-definition",
        "question": "What is the current definition and scope of the topic?",
        "priority": "critical",
        "answer_requirements": [
          "definition",
          "scope",
          "current versus proposed distinction"
        ]
      }
    ]
  },
  "source_handling": {
    "storage_mode": "pointer_only",
    "follow_symlinks": false,
    "duplicate_policy": "representative_plus_all_paths"
  },
  "phase0": {
    "profile": "standard",
    "git_dates": "when_available",
    "graph_signals": "off",
    "non_text_policy": "inventory_and_report"
  },
  "outputs": {
    "tier": "query_ready",
    "phase1_batching": "bounded",
    "phase2_topology": "minimum_useful"
  },
  "execution": {
    "route": "terminal_backed",
    "show_success_validation_details": false,
    "fail_closed": true
  }
}
```

Then run:

```text
/apex-kb start --config manifests/run-config.okf.json
```
