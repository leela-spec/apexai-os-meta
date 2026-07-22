# NARM personal-development KB — Phase 2 execution pack

Run root: `C:\GitDev\apexai-os-meta\apex-meta\kb\therapy-narm-personal-development`

Run all five topic prompts in numeric order in one uninterrupted agent task. Topic 1 is a corrected `a02` attempt; topics 2–5 are first attempts. For each topic:

1. Run `apex-kb drive --run-root <run-root> --json-output` and confirm the active packet has the expected topic ID.
2. Read every file in that active packet directory: `TASK.md`, `task.json`, `source-allowlist.json`, `output.schema.json`, and `expected-output-path.txt`.
3. Read only the Phase 1 analysis and source capsules listed in that packet. Never read another topic's Phase 1 analysis while drafting the current topic.
4. Write readable, indented JSON only to `expected-output-path.txt`'s declared path.
5. Run `apex-kb drive` again. If validation requests repair, repair only the newly generated numbered packet/result.
6. Verify the rendered dossier and deterministic source atlas, commit only this topic's lifecycle/result/page artifacts, and push `main`.
7. Report concise progress and immediately continue with the next numbered prompt without asking for approval.

After topic 5, keep running `apex-kb drive` until the lifecycle reaches `query_ready`. Verify retrieval health and commit/push the final deterministic artifacts with message `Finalize NARM personal development KB run`.

Safety: source notes are pointer-only and must never be copied, edited, deleted, moved, or staged. Do not create branches, worktrees, stashes, or pull requests. Do not stage unrelated dirty files.
