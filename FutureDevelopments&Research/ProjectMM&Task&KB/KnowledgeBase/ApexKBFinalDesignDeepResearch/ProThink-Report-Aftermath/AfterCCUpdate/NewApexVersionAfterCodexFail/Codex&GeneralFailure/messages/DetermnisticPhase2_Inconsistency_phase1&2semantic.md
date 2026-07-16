You were right to question it: `incomplete_artifact` does not mean the Phase 2 wiki pages or acceptance work are absent. It means the nine new acceptance JSON files do not use the field names required by the current deterministic validator.

What is confirmed on `origin/main`:

|Report claim|Actual result|
|---|---|
|9 Phase 1 analyses and ledgers exist|Yes|
|16 reported Phase 2 pages exist|Yes|
|9 new semantic-acceptance files exist|Yes|
|Every new artifact records 3 target-query results, all `answerable`|Yes|
|Every artifact declares `semantic_pass`|Yes|
|Current Apex validator accepts them|No|

The direct reason is a contract mismatch:

|New files use|Validator requires|
|---|---|
|`semantic_run_id`|`run_id`|
|`review_mode`|`evaluator_context`|
|query `verdict: "answerable"`|query `result: "answerable"`|
|`material_claim_verifications`|`claim_reviews`|
|claim `supported: true`|claim `result: "supported"`|
|no per-query `page_pointers`|`page_pointers` required|

The new files follow the example embedded in [semantic-value-contract.md](C:\\GitDev\\apexai-os-meta.claude\\skills\\apex-kb\\references\\semantic-value-contract.md), while the deterministic validator and [semantic-acceptance.schema.json](C:\\GitDev\\apexai-os-meta.claude\\skills\\apex-kb\\references\\semantic-acceptance.schema.json) still require the older schema. This is an Apex KB contract/runtime inconsistency, not evidence that the browser chat failed to create the nine records.

There are also three genuine Phase 2 route mistakes:

|Topic|Registry expected|Page actually created|
|---|---|---|
|sequencing|`wiki/summaries/sequencing.md`|`wiki/summaries/sequencing-and-play.md`|
|stats|`wiki/summaries/stats.md`|`wiki/summaries/stats-and-metrics.md`|
|feature interconnections|`wiki/summaries/feature-interconnections-user-flows.md`|`wiki/summaries/cross-feature-interconnections.md`|

Those three route mismatches are real and correctly appear as `target_query_route_missing`.

The Phase 1 report is also only partly structurally valid. Its nine ledgers exist, but none conforms to the current [semantic-run-ledger.schema.json](C:\\GitDev\\apexai-os-meta.claude\\skills\\apex-kb\\references\\semantic-run-ledger.schema.json):

- All nine lack `run_id`, `page_decisions`, and `candidate_dispositions`.
- They use `semantic_run_id` instead of `run_id`.
- Their source entries use `read` rather than `read_status` and omit required authority/availability/query-use fields.
- `user-stories` additionally lacks the required `sources` array.
- Several candidate dispositions use non-contract values such as `promote_tunable`, `embed_as_proposal`, and `defer_future`.

Finally, the deterministic quality run found 10 page repair candidates, but only three belong to the new nine-topic Phase 2 run: the three route mismatches above. The other candidates are older legacy pages with obsolete query IDs or thin sections; they should not be attributed to this latest Phase 2 report.

So the truthful state is:

- Semantic files: created and internally self-reported as passed.
- Deterministic acceptance: blocked by incompatible acceptance/ledger schemas and three page-route mismatches.
- Postflight: rebuilt `wiki/index.md` and retrieval successfully; retrieval is now fresh.
- `query_ready`: cannot be claimed.w