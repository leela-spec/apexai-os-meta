# Semantic mainline and browser prompt contract

## Purpose and scope

This file locks the simplest selected repository transport for Apex KB semantic work and the construction rules for the generated browser prompts.

It corrects one narrow design error: CLI implementation branch safety was copied into the generated-KB semantic workflow. These are different concerns.

- **CLI implementation work** remains on the locked Apex KB implementation branch and follows `02-LIVE-STATE-AND-BRANCH-SAFETY.md`.
- **Generated KB artifacts** are written to the configured destination repository and committed directly to that repository's `main` branch.

This file supersedes any older orchestration text that proposes a semantic branch, semantic worktree, semantic pull request, semantic clone, or per-run branch. It does not remove the implementation-branch rules used to develop the CLI itself.

## Locked semantic transport

```yaml
semantic_transport:
  destination_ref: main
  deterministic_publication: direct_commit_and_push_to_main
  browser_semantic_publication: direct_commit_and_push_to_main
  local_continuation: git_pull_ff_only_origin_main
  forbidden_fallbacks:
    - create_semantic_branch
    - create_semantic_worktree
    - create_semantic_clone
    - open_semantic_pull_request
    - split_write_commit_push_into_operator_steps
```

The repository is the durable handoff surface. `main` is the one place every participant reads and writes.

## Direct-main lifecycle

1. The local CLI completes deterministic corpus intelligence in the configured destination repository.
2. The CLI commits and pushes the deterministic run artifacts directly to destination `main`.
3. The CLI records the resulting `main` commit as the semantic task's `base_commit`.
4. The CLI generates one complete Phase 2A browser prompt containing the repository, `main`, `base_commit`, exact inputs, exact outputs, semantic contract, commit instruction, and return format.
5. The browser worker reads the exact evidence, writes only the required analysis artifacts, commits them, and pushes directly to `main` in the same run.
6. The local CLI runs the equivalent of `git pull --ff-only origin main`, validates the expected artifacts, and generates the Phase 2B prompt.
7. The Phase 2B browser worker writes the dossier and source atlas, commits them, and pushes directly to `main`.
8. The local CLI pulls `main`, validates the outputs, and enters Phase 3.

There are no separate operator stages for write, commit, or push.

## Minimal validation only

The semantic round trip has three required checks:

1. **Base commit:** before writing, the browser worker confirms destination `main` still equals the prompt's `base_commit`. If it moved, return `MAIN_MOVED` and write nothing.
2. **Changed paths:** the semantic commit changes only the exact output paths listed by the prompt.
3. **Artifact contract:** after pulling `main`, the CLI validates run ID, configuration hash, topic ID, required files, and semantic content/schema rules already owned by the application.

Do not add branch creation, worktree management, clone classification, pull-request handling, multi-branch ancestry logic, a new state database, or a separate publication workflow. If direct writes are unavailable because the execution surface is read-only or `main` rejects the push, return the exact blocker. Do not invent a branch fallback.

## Internal-name translation

Preserve current code names until a separate migration is justified:

| Operator phase | Current internal task name |
|---|---|
| Phase 2A semantic analysis | `phase1` |
| Phase 2B dossier/source-atlas compilation | `phase2` |
| Phase 3 independent evaluation | `acceptance` |

The transport correction does not require a terminology rewrite.

## Prompt research findings

The browser templates below apply current official prompt guidance:

- OpenAI recommends putting instructions first, separating instructions from context, being specific about the desired outcome, and showing the exact output format.
- OpenAI's current model guidance recommends lean prompts, stating each instruction once, exposing only relevant tools/context, defining autonomy and approval boundaries, and specifying goal, evidence, success criteria, and output format.
- OpenAI Academy guidance recommends the simple structure: task, helpful context, and ideal output. GPT-5-class models can handle one coherent multi-step request, so commit and push belong inside the same semantic prompt.
- OpenAI's GitHub documentation confirms that repository access depends on the enabled GitHub surface. The generated prompt therefore names the required write action explicitly and returns `GITHUB_WRITE_UNAVAILABLE` when the chat has read-only access. It must not compensate by creating a branch.

Primary sources:

- https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api
- https://developers.openai.com/api/docs/guides/latest-model
- https://academy.openai.com/en/public/clubs/work-users-ynjqu/resources/prompting
- https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt-deep-research
- https://docs.github.com/en/pull-requests/reference/branches

## Prompt-construction rules

Every generated semantic prompt must be complete and executable without chat memory.

1. State the task and product outcome first.
2. Include one repository, one ref (`main`), one exact `base_commit`, one run, one topic, and one semantic phase.
3. List exact inputs in read order. Do not tell the worker to search the repository broadly when deterministic artifacts already name the evidence.
4. List exact output paths. The list is also the complete Git changed-path allowlist.
5. State the semantic requirements positively and once. Avoid repeated warnings and process commentary.
6. Authorize the complete intended action: read, write, self-review, commit, and push directly to `main`.
7. Define the three blockers: `MAIN_MOVED`, `GITHUB_WRITE_UNAVAILABLE`, and `SEMANTIC_INPUT_MISSING`.
8. Require one structured completion response with the resulting commit and changed paths.
9. Do not ask the worker to choose the next stage, create new topics, redesign the workflow, or recommend infrastructure.
10. Test the exact generated prompt on the real Leela Skill Tree workflow. A template or synthetic import alone is not proof.

## Canonical Phase 2A browser prompt template

The CLI fills every value. A runtime prompt containing an unresolved placeholder is invalid.

```text
TASK
Perform the bounded Apex KB Phase 2A semantic analysis for one topic. Read the exact deterministic evidence below, write the required analysis artifacts, then commit and push those artifacts directly to the destination repository's main branch.

REPOSITORY
- Repository: <DESTINATION_REPOSITORY>
- Branch: main
- Expected main commit before writing: <BASE_COMMIT>

RUN
- Run ID: <RUN_ID>
- Configuration hash: <CONFIG_HASH>
- Topic ID: <TOPIC_ID>
- Topic name: <TOPIC_NAME>

READ IN THIS ORDER
<EXACT_PHASE2A_INPUT_PATHS>

LOCKED QUESTIONS
<EXACT_TARGET_QUESTIONS_WITH_REQUIREMENTS>

WRITE ONLY
<EXACT_PHASE2A_OUTPUT_PATHS>

SEMANTIC RESULT
- Read every material candidate in full or at every relevant named section.
- Give every deterministic candidate exactly one disposition.
- Preserve current, implementation, prototype, historical, superseded, duplicate, contextual, incidental, irrelevant-after-review, and blocked distinctions.
- Preserve contradictions, uncertainty, authority, freshness, individual source value, and exact evidence pointers.
- Answer every locked question directly or record a precise unresolved state.
- Never infer source content from a filename, rank, snippet, or prior chat.
- Do not create compiled wiki pages or modify deterministic manifests, run state, retrieval, or unrelated files.

COMPLETE THE GIT ACTION
1. Confirm repository main still equals <BASE_COMMIT>. If not, return MAIN_MOVED and write nothing.
2. Reread every output.
3. Confirm the changed paths are exactly the WRITE ONLY paths.
4. Commit with: <EXACT_COMMIT_MESSAGE>
5. Push the commit directly to main. Do not create a branch, worktree, clone, or pull request.

RETURN EXACTLY
status: completed | blocked
repository: <DESTINATION_REPOSITORY>
branch: main
base_commit: <BASE_COMMIT>
result_commit: <RESULT_COMMIT_OR_NULL>
changed_paths:
  - <PATH>
blocked_code: null | MAIN_MOVED | GITHUB_WRITE_UNAVAILABLE | SEMANTIC_INPUT_MISSING
blocked_detail: null | <DETAIL>
```

## Canonical Phase 2B browser prompt template

```text
TASK
Compile the bounded Apex KB Phase 2B dossier and source atlas for one topic from the validated Phase 2A artifacts, then commit and push the compiled pages directly to the destination repository's main branch.

REPOSITORY
- Repository: <DESTINATION_REPOSITORY>
- Branch: main
- Expected main commit before writing: <PHASE2A_COMMIT>

RUN
- Run ID: <RUN_ID>
- Configuration hash: <CONFIG_HASH>
- Topic ID: <TOPIC_ID>
- Topic name: <TOPIC_NAME>

READ IN THIS ORDER
<EXACT_PHASE2B_INPUT_PATHS>

WRITE ONLY
<EXACT_PHASE2B_OUTPUT_PATHS>

COMPILED RESULT
- Compile only from validated Phase 2A analysis and source capsules named above.
- Produce distinct Macro, Meso, and Micro value: why the topic matters, what it is, and how it works.
- Answer every locked critical and routine question directly or preserve a precise unresolved state.
- Preserve present, proposed, historical, contradicted, and uncertain states.
- Preserve every deterministic candidate exactly once in the source atlas with its disposition, individual value, freshness/authority assessment, duplicate or supersession relationship, and exact pointers.
- Do not rediscover the corpus or modify deterministic manifests, run state, retrieval, acceptance, or unrelated files.

COMPLETE THE GIT ACTION
1. Confirm repository main still equals <PHASE2A_COMMIT>. If not, return MAIN_MOVED and write nothing.
2. Reread every output.
3. Confirm the changed paths are exactly the WRITE ONLY paths.
4. Commit with: <EXACT_COMMIT_MESSAGE>
5. Push the commit directly to main. Do not create a branch, worktree, clone, or pull request.

RETURN EXACTLY
status: completed | blocked
repository: <DESTINATION_REPOSITORY>
branch: main
base_commit: <PHASE2A_COMMIT>
result_commit: <RESULT_COMMIT_OR_NULL>
changed_paths:
  - <PATH>
blocked_code: null | MAIN_MOVED | GITHUB_WRITE_UNAVAILABLE | SEMANTIC_INPUT_MISSING
blocked_detail: null | <DETAIL>
```

## Next implementation iteration

```yaml
task_id: phase2a-direct-main-patch
mode: patch_authoring
repository: leela-spec/apexai-os-meta
branch: codex/apex-kb-cli-phase0-integration
expected_start_commit: resolve_current_branch_head_before_work
product_outcome: >-
  Replace the local incoming-JSON Phase 2A transport with one generated browser prompt
  and one direct-main pull-and-validate continuation, without changing Phase 0, Phase 2B,
  acceptance, retrieval, updates, or the state architecture.
must_read:
  - apex-meta/apex-kb-cli/orchestration/05-SEMANTIC-MAINLINE-AND-PROMPT-CONTRACT.md
  - apex-meta/apex-kb-cli/src/apex_kb/config.py
  - apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py
  - apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py
  - apex-meta/apex-kb-cli/src/apex_kb/templates/phase1-task.md
  - apex-meta/apex-kb-cli/src/apex_kb/schemas/semantic-task.schema.json
  - apex-meta/apex-kb-cli/tests/test_lifecycle.py
  - apex-meta/apex-kb-cli/tests/test_product_contract.py
allowed_patch_paths:
  - the smallest existing files required by the proven code boundary
  - at most one new small Git helper module when reuse is not realistic
required_behavior:
  - deterministic artifacts are committed and pushed to destination main
  - generated Phase 2A prompt contains no unresolved placeholders
  - browser result is a direct commit to destination main
  - local continuation uses a simple fast-forward-only pull of main
  - validation is limited to base commit, changed paths, and existing semantic contract
forbidden_scope:
  - semantic_branches
  - semantic_worktrees
  - semantic_clones
  - semantic_pull_requests
  - phase_0_changes
  - phase_2b_implementation
  - acceptance_changes
  - retrieval_changes
  - update_changes
  - new_state_database
  - provider_adapter_framework
return_contract:
  - exact-match patch pack
  - complete content for any approved new file
  - patch manifest
  - focused test additions
  - exact Leela Phase 2A canary procedure
  - apex.kb.orchestration-result.v1 envelope
```
