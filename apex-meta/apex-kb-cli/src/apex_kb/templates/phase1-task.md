TASK
Perform the bounded Apex KB Phase 2A semantic analysis for one topic. Read the exact deterministic evidence below, write every required analysis artifact, self-review the complete output set, then commit and push those artifacts directly to the destination repository main branch.

WRITE REPOSITORY
- Repository: {destination_repository}
- Branch: main
- Expected main commit before writing: {base_commit}

READ-ONLY SOURCE REPOSITORY
{source_repository_block}

RUN
- Run ID: {run_id}
- Configuration hash: {config_hash}
- Task ID: {task_id}
- Topic ID: {topic_id}
- Topic name: {topic_name}
- Exhaustive candidate count: {candidate_count}

READ IN THIS ORDER
{inputs}

LOCKED QUESTIONS
{questions}

WRITE ONLY
{outputs}

REQUIRED OUTPUT SHAPE
1. Write `{topic_analysis_json}` as one schema-valid `apex.kb.phase1-result.v2` object matching the committed `output.schema.json`.
2. Write `{topic_analysis_markdown}` as the durable human-readable topic analysis with Macro, Meso, Micro, direct target answers, every candidate disposition, contradictions, and uncertainties.
3. For every hash listed in `required_capsule_hashes` in `task.json`, write the corresponding JSON and Markdown source-capsule paths listed above.
4. The `source_capsules` array in the topic JSON must contain exactly the capsule objects written as JSON files. Reused capsules named by the allowlist are read-only inputs and must not be rewritten.

SEMANTIC RESULT
- Read every material candidate in full or at every relevant named section; review contextual, incidental, duplicate, irrelevant-after-review, and blocked candidates deeply enough to justify their disposition.
- Give every deterministic candidate exactly one disposition.
- Preserve current, implementation, prototype, historical, superseded, duplicate, contextual, incidental, irrelevant-after-review, and blocked distinctions.
- Preserve contradictions, uncertainty, authority, freshness, individual source value, duplicate/supersession relationships, and exact evidence pointers.
- Answer every locked question directly or record a precise unresolved state.
- Never infer source content from a filename, rank, snippet, or prior chat.
- Do not create compiled wiki pages or modify deterministic manifests, run state, retrieval, or unrelated files.

COMPLETE THE GIT ACTION
1. Confirm destination repository main still equals `{base_commit}`. If it moved, return `MAIN_MOVED` and write nothing.
2. Reread every output and validate the topic JSON against the committed output schema.
3. Confirm the changed paths are exactly the WRITE ONLY paths.
4. Commit with: `{commit_message}`
5. Push the commit directly to main. Do not create a branch, worktree, clone, or pull request.

RETURN EXACTLY
status: completed | blocked
repository: {destination_repository}
branch: main
base_commit: {base_commit}
result_commit: null when blocked; otherwise the exact resulting commit SHA
changed_paths: [] when blocked; otherwise exactly the WRITE ONLY paths
blocked_code: null | MAIN_MOVED | GITHUB_WRITE_UNAVAILABLE | SEMANTIC_INPUT_MISSING
blocked_detail: null when completed; otherwise a precise blocker detail
