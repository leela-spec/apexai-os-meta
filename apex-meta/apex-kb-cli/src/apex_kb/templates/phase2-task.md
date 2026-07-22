# Apex KB bounded Phase 2 compiler task

Run ID: `{run_id}`  
Config hash: `{config_hash}`  
Task ID: `{task_id}`  
Topic: `{topic_name}` (`{topic_id}`)  
Candidate count to preserve in the atlas: `{candidate_count}`

Compile an answer-bearing Macro/Meso/Micro dossier at `{dossier}` and a complete source atlas at `{atlas}`. Macro, Meso, Micro, every locked answer, every material key claim, and every citation must be non-empty. Preserve every locked query ID and question verbatim. Cite only topic candidates reviewed in Phase 1, using source IDs and exact pointers preserved by that review. Use only validated Phase 1 analysis and reusable source capsules. Preserve present, proposed, historical, open, and contradicted states. The atlas must contain every deterministic candidate exactly once, including incidental, duplicate, historical, generated, blocked, and irrelevant-after-review dispositions.

Return structured JSON; the application renders the Markdown pages deterministically. Write only to:

`{incoming}`

Do not mutate manifests, run state, indexes, retrieval, or sources. Do not select the next lifecycle stage.
