# Patch Pack Generation SOP — Exact-Match Block Class

## Scope: which patch class this document governs

This repository has documented **two distinct patch artifact classes**, for two distinct
generator environments. Do not mix them.

| | Git-native diff class | **Exact-match block class (this document)** |
|---|---|---|
| Generator environment | Real local git clone, or a scratch git repo the generator can run `git` in | Read-only repository access only — connector/browser fetch, no git CLI, no local filesystem clone |
| Artifact shape | `git diff` output: `diff --git`, `index <old>..<new>`, hunk headers | `<file>/<old>/<new>` literal-substring blocks, no git metadata |
| Validated by | `git apply --check` in a real clone | Exact-once substring match against live file content |
| Governing doc | `AI-Git-Native-Patch-Pack-Protocol.md`, `AI-Patch-Pack-Execution-Protocol.md` | This document + `WorkingPatchInstructionFormat.md` + `patchpack.py` |

**Decide the class from the generator's actual environment, not from convenience.** If the
generating AI has real git-clone access, produce git-native diffs and follow the existing
git-native protocol — it is strictly stronger evidence (blob-anchored, `git apply --check`-proven).
Use the exact-match class only when the generator genuinely cannot run git — e.g. a GitHub-connector
or browser session with read/write file access but no git CLI. This is not a fallback of
convenience: the `apex-kb-module-first-patch-pack` that installed the control plane
(`apex-meta/scripts/apex_kb_control.py`) was correctly built this way — its own manifest recorded
`access_used_for_repository: connected_github_interface_only`, `repository_write_performed: false`.
Exact-match was the right choice for that environment, and it applied cleanly (all 50 blocks,
zero conflicts, verified against pinned baseline `c34dfbfe984668d7d88ca1e3dde6744a77f8bf2b`).

## Why this class needs its own discipline

An exact-match block has no blob anchor, no line numbers, and no diff context beyond what you
write. Its only proof of correctness is: *the `<old>` text occurs in the live file, exactly once.*
Every rule below exists to keep that one guarantee true.

## Per-file generation loop

1. **Pin the baseline.** Before writing any block, record `inspected_commit = <git rev-parse HEAD>`
   of the target repository. State it at the top of the pack. Every `<old>` block is valid **only**
   against that exact commit's file content — not "recent main," not "probably still current."

2. **Read the live file immediately before authoring the block — never from memory, a prior
   summary, or a cached excerpt.** If you read a file ten minutes ago and the operator may have
   touched it since, re-read it. (This is `WorkingPatchInstructionFormat.md` rule 2, unchanged —
   it is the single most-violated rule in this repo's own patch failure history, per
   `AI-Patch-Pack-Execution-Protocol.md`'s "later messy run" case study.)

3. **One change per block.** Never bundle two unrelated edits into one `<old>/<new>` pair. If a
   file needs five changes, write five separate `<file>/<old>/<new>` groups. This keeps each block
   independently reviewable and independently revertable.

4. **`<old>` = verbatim copy, minimal-but-unique context.**
   - Copy character-for-character, including whitespace, indentation, and blank lines. Do not
     "clean up" formatting inside `<old>` — that silently breaks the match.
   - No line numbers, no block IDs. Location is the text itself.
   - Include only as much surrounding context as needed to make the match unique in the file. If
     a target string could appear more than once, add 1–2 extra lines above/below rather than
     guessing which occurrence is meant.

5. **`<new>` = the complete replacement** for exactly that block — not a diff-style `+`/`-`
   annotation, the literal resulting text.

6. **New files are never exact-match.** A file that doesn't exist yet goes whole, verbatim, under
   `new-files/<repo-relative-path>` in the pack directory — mirrored, not patched.

7. **Group blocks into dependency-ordered modules.** Name each module by what it accomplishes
   (`M1-control-plane-and-run-state`, not `patch-01`), and state which modules it depends on. Apply
   strictly in dependency order — a later module may assume an earlier module's `<new>` text is
   already live.

8. **Emit a manifest** (`package-manifest.json`) recording: `inspected_commit`; the module list
   with dependencies; the full `existing_files_patched` and `new_files` lists; `patch_order`;
   and a `SHA-256` of every artifact in the pack **except the manifest itself** (self-hash would be
   recursive). JSON, not YAML: `patchpack.py` is stdlib-only and this repo's Python environment
   has no YAML parser installed, so the one manifest a script actually validates is JSON — a
   companion prose `package-manifest.md`/`.yaml` may still exist for human readers, but it is not
   what `patchpack.py` reads. This is what lets an executor (or `patchpack.py verify-manifest`)
   detect a corrupted or partially-transferred pack before touching a real repository.

   ```json
   {
     "inspected_commit": "<git rev-parse HEAD>",
     "modules": [{"id": "N1", "name": "phase1-coverage-gate", "depends_on": []}],
     "existing_files_patched": ["apex-meta/scripts/apex_kb_control.py"],
     "new_files": [],
     "patch_order": ["patches/N1-phase1-coverage-gate.exact-match.md"],
     "artifact_sha256": {"patches/N1-phase1-coverage-gate.exact-match.md": "<sha256>"}
   }
   ```

### Worked example (real block, from the installed control-plane pack)

```text
<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb.py</file>
<old>
    commands = {
        "control", "scaffold", "source-intake", "hash", "generate-source-payload-manifest", "source-payload-manifest",
        "payload-manifest", "preflight", "topic-sanity-check", "phase0", "ingest-phase1", "ingest-phase2", "index", "query",
        "lint", "audit", "status", "health",
        "quality", "coverage", "query-eval", "semantic-acceptance-status", "graph", "process-graph", "postflight",
    }
</old>
<new>
    commands = {
        "control", "doctor", "scaffold", "source-intake", "hash", "generate-source-payload-manifest", "source-payload-manifest",
        "payload-manifest", "preflight", "topic-sanity-check", "phase0", "ingest-phase1", "ingest-phase2", "index", "query",
        "lint", "audit", "status", "health",
        "quality", "coverage", "query-eval", "semantic-acceptance-status", "graph", "process-graph", "postflight",
    }
</new>
```

Note the full existing set is copied verbatim in `<old>` (not just the one line changing) — this
is what makes the block unique and lets a mechanical check catch drift if any other flag was added
or removed since the pin.

## Fail-closed rules (author and executor both enforce these — do not skip either side)

- If `<old>` matches **zero** times in the live target: STOP. Do not "fix it up" or guess a
  nearby variant — re-read the live file and regenerate the block from what is actually there.
- If `<old>` matches **more than once**: STOP. Add disambiguating context and regenerate; never
  apply to "the first match" or "the one that looks right."
- If the target repository's `HEAD` no longer equals the pack's `inspected_commit`: treat every
  block for files touched since that commit as **unverified** — re-fetch and re-diff those files
  specifically; do not assume compatibility.
- A block that fails any of the above is never silently skipped and never force-applied. The pack
  as a whole does not apply until every block in the current module passes.

## Tooling

- `patchpack.py` (this directory) is the generic, deterministic engine for the exact-match class:
  `check` (dry-run, exact-once verification against a real target repo + baseline-commit check),
  `apply` (atomic write, refuses unless `check` was clean), `verify-manifest` (pack-integrity
  hash check), `new-baseline` (stamps a fresh `inspected_commit` + target-file hashes for a new
  pack). Run `check` before ever running `apply`.
- For the git-native diff class, use real `git diff` / `git apply --check` per
  `AI-Git-Native-Patch-Pack-Protocol.md` — no new tooling needed; that is already git itself.
- `deterministic-markdown-patcher2` (`.claude/skills/`) remains available as an interactive,
  judgment-assisted executor for one-off exact-match edits outside a packaged multi-module patch
  run; `patchpack.py` is the batch/CI-style gate for a full pack.

## Related documents (read for the class you are not using)

- `AI-Git-Native-Patch-Pack-Protocol.md` — git-native diff class, full creation/validation process.
- `AI-Patch-Pack-Execution-Protocol.md` — git-native diff class, executor classification (A/B/C)
  and repair-first flow for stale patches.
- `WorkingPatchInstructionFormat.md` — the original short-form statement of the exact-match block
  rules this document expands and packages with tooling.
- `BestPracticeGitPatchWorkflow.md` — a git-native-class success case study; useful context, not a
  substitute for the classification rule at the top of this document.
