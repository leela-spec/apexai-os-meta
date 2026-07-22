# Apex KB bounded Phase 2 compiler task

Run ID: `{run_id}`  
Config hash: `{config_hash}`  
Task ID: `{task_id}`  
Topic: `{topic_name}` (`{topic_id}`)  
Candidate count to preserve in the atlas: `{candidate_count}`

Compile an answer-bearing Macro/Meso/Micro dossier at `{dossier}`. Macro explains why the topic matters for the operator's outcome; Meso explains what the relevant models, patterns, distinctions, and relationships are; Micro explains how to recognize, choose, and apply practices safely. Every locked answer, material key claim, and citation must be non-empty. Preserve every locked query ID and question verbatim. Cite only topic candidates reviewed in Phase 1, using source IDs and exact pointers preserved by that review. Use only this topic's validated Phase 1 analysis and the source capsules listed in this packet. Do not read another topic's Phase 1 analysis. Preserve only evidence states actually supported by the sources; do not manufacture enum coverage.

Include page purpose, an adaptive ranked source set, routes by locked question, source boundaries, contradictions or tensions, uncertainty and open questions, raw-source reopen triggers, and material evolution. The application creates `{atlas}` deterministically from Phase 1; do not submit or copy the atlas.

Return readable, indented structured JSON; the application renders the Markdown pages deterministically. Write only to:

`{incoming}`

Do not mutate manifests, run state, indexes, retrieval, or sources. After writing this result, the outer executor must run `apex-kb drive` again, report concise progress, and continue to the next topic without asking for approval. The application remains the sole authority that selects the next lifecycle stage.
