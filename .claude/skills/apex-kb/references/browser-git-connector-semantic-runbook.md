# Browser Git Connector Semantic Runbook

## Capability boundary

Use this route only when complete repository-file reads and reliable whole-file writes are available but terminal execution is not. Account-level Skills are optional. A terminal-backed control executor must first render the exact run-specific packet under `log/runs/<run-id>/packets/`. The packet, its input fingerprints, and the repository-local `semantic-contract/` files are authority; chat prose is not. If no packet exists, stop with `needs_terminal_executor: semantic_packet_missing`. Never run or claim scaffold, intake, hashing, manifest mutation, Phase 0 regeneration, index/retrieval rebuild, lint, quality, postflight, or deterministic validation from this route.

## Startup target lock

1. Read the packet Markdown and JSON named by the one-line trigger, then read every `exact_input_files` entry completely or by the exact section mode permitted by the packet.
2. Verify the packet's `run_id`, `stage`, `topic_id`, exact output paths, write allowlist, stop conditions, and input fingerprints before writing.
3. Confirm stable target-query IDs, priorities, answer requirements, and expected page routes from the packet inputs. If a compiled topic has no target queries, stop semantic drafting and report `partial: missing_target_queries`.

## One-topic packet execution

1. Write only the packet's `allowed_writes`; never create a path merely because it appeared in chat or a prior run.
2. Use Phase 0 rankings only to nominate candidates. Prefer canonical specifications; then implementation evidence for current-state questions; current contracts/updates; user stories and examples; then historical or proposed material.
3. Open the complete source or every relevant section needed for the locked questions. Never infer from filenames, snippets, rankings, or prior summaries.
4. Update the exact topic ledger after every source and before context ends. Distinguish `unopened`, `targeted`, `complete`, and `blocked`; distinguish candidate, reviewed, and materially used.
5. Continue source reading while a known readable source can answer an unresolved critical/routine query.
6. For Phase 1, write the exact topic analysis and ledger with query linkage and explicit concept/entity dispositions. For Phase 2, write only pages declared by the registry or Phase 1 analysis. For semantic acceptance, write only the independent verdict artifact.
7. Read every `required_readback` file in full and check every packet `success_conditions` item before returning the exact `completion_response`.
8. Classify reopen triggers as `evidence_unavailable`, `evidence_conflict`, `future_change`, or `readable_unopened`; the last blocks completion for critical/routine queries.
9. Stop on every packet stop condition. Report truthful partial state when connector reliability, context, or evidence access prevents completion; never widen the write set or self-certify acceptance.

## Interrupted-context recovery prompt

```text
Resume one Apex KB semantic stage from repository files only. Read `manifests/run-state.json`, then open the packet referenced by its current stage under `log/runs/<run-id>/packets/`. Verify the packet input fingerprints and read only its exact inputs. Treat the ledger as navigation, not evidence. Reopen every source whose exact passage is needed before making a claim. Continue from the first unresolved critical/routine query, write only packet-allowed paths, perform every required readback, and return the packet completion response exactly. Do not certify your own output or perform deterministic work.
```

## Clean-context page-only evaluator prompt

```text
Evaluate one topic without drafting context. Read its target queries and compiled pages first. For each query, answer only from compiled pages, cite the exact page section, and return answerable, partial, not_answerable, or blocked. Then identify any answer requirement absent from the pages. Do not inspect raw sources until the page-only verdicts are fixed. Afterward inspect only the resolved evidence passages supplied for verification. Return reason-coded repairs and a semantic verdict. No numeric score, file-count proxy, or self-report may establish a pass.
```

## Claim-entailment evaluator prompt

```text
Independently select at least two material claims from each page, or all claims when fewer exist. Compare each claim with its resolved source passage. Return supported, partially_supported, contradicted, or unresolvable, with page and source pointers. A semantic pass requires all sampled material claims to be supported.
```

## Deterministic handoff

Return the packet's exact completion response after required readback. The terminal-backed executor then runs `control reconcile`, which validates exact paths, schemas, packet fingerprints, custody, independent acceptance, and the next legal transition from repository files. Connector execution stops at `compiled_unvalidated`; only a terminal-backed `control run` may execute postflight and promote the run to `query_ready`.
