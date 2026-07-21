# Apex KB bounded semantic task

Run ID: `{run_id}`  
Config hash: `{config_hash}`  
Task ID: `{task_id}`  
Topic: `{topic}`

## Locked target questions

{questions}

Read `task.json`, `source-allowlist.json`, and `output.schema.json` before opening sources. Read only allowlisted sources. Preserve contradictions and uncertainty. Do not update configuration, manifest, state, stage results, source files, or any path not explicitly allowed.

Write exactly one JSON result to:

`{incoming}`

Stop instead of improvising when an identity value, source, or required output is unavailable.
