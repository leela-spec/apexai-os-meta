# Apex KB independent semantic acceptance task

Run ID: `{run_id}`  
Config hash: `{config_hash}`  
Task ID: `{task_id}`  
Topic ID: `{topic_id}`  
Drafting context ID that must not be reused: `{drafting_context_id}`

Evaluate only the compiled pages first:

{pages}

Test page-only answerability for every critical and routine target question exactly once, then check a non-empty contract-defined sample of material claims against the supplied topic-scoped resolved evidence capsules. Page pointers must resolve under the compiled page paths in this packet; evidence pointers must resolve under its supplied capsule paths. Preserve contradictions and uncertainty. A semantic pass requires every critical/routine question to be answerable without reopening readable raw sources and every sampled material claim to be supported.

The application can verify only that the returned evaluator context ID differs from the drafting context ID. The operator or execution environment must provide a genuinely independent fresh evaluator context; a renamed ID in the drafting context is not independent acceptance.

Write one schema-valid result only to:

`{incoming}`

Do not improve the pages, lower the gate, or select the next lifecycle stage.
