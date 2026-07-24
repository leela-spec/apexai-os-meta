# Apex KB bounded Phase 1 semantic task

Run ID: `{run_id}`  
Config hash: `{config_hash}`  
Task ID: `{task_id}`  
Topic: `{topic_name}` (`{topic_id}`)  
Exhaustive candidate count: `{candidate_count}`

## Locked target questions

{questions}

Read `task.json`, `source-allowlist.json`, and `output.schema.json` before opening evidence. Phase 0 rank is navigation only. Give every candidate source exactly one semantic disposition. Open every material source in full or at all relevant sections, or reuse an unchanged content-hash capsule. Preserve versions, contradictions, uncertainty, authority, and freshness. Never represent an unopened source as evidence.

Coverage requirements (be thorough, not minimal): for every source you open, record **all** material line pointers it supports — not a representative sample — and **every** distinct key claim it establishes. Answer each locked target question completely, and cite **every** supporting pointer for each answer. Do not drop pointers or claims that later phases will need; Phase 2 can only cite what this review preserves.

Write one schema-valid JSON result only to:

`{incoming}`

Do not write manifests, run state, stage results, wiki pages, retrieval files, or source files. Stop instead of improvising if identity, evidence, or an allowed output is unavailable.
