# Plan: Realize the Apex KB Final Architecture Research Export

## Context

Two linked research documents now sit in `apexai-os-meta` under
`FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/ProThink-Report/`:

- `Apex KB Final Architecture — Research Export.md` — the executive summary.
- `Apex_KB_Final_Architecture_Deep_Research_Report.md` — the full 3,245-line decision-ready
  report (Target Lock, lifecycle/value scoring, module-by-module strategy, and a
  **Final File and Script Implementation Plan** with an exact target tree, a per-file
  disposition matrix, per-file design records, a 12-step implementation dependency order,
  and a migration strategy).

The report's core finding: the live `rank_topic_sources()` in `apex-meta/scripts/apex_kb.py`
does line-level substring counting and silently truncates to the top 30 files, so semantic
review already operates on a candidate set that may have lost sources. The report's fix is a
full architecture: exhaustive deterministic topic maps, hash-keyed source capsules, a durable
per-concept source atlas, four-layer acceptance, dependency-aware incremental maintenance, and
a modular `apex_kb_runtime/` package — replacing today's single-file `apex_kb.py`/`apex_kb_retrieval.py`
plus a package of overlapping reference/template/schema files under `.claude/skills/apex-kb/`.

Rather than implementing this directly in this session, the operator wants to hand the heavy
authoring work to a GPT-5.6 heavy-thinking-mode session (via ChatGPT/Codex, outside this tool),
because the report's own orchestration design already assumes a Codex/ChatGPT-web split: Codex
runs deterministic work and Git operations, ChatGPT web reads evidence and authors artifacts,
Codex imports and validates. This plan sets up that handoff: get the report onto `main` so an
external GitHub-connected session can read it authoritatively, produce a prompt that makes
GPT-5.6 emit one patch file per target file (batched safely), then pull those patches back into
the repo and apply them here.

Confirmed with the operator:
- The commit to `main` will include everything currently pending in the research folder (the
  two ProThink-Report files, the `FINAL-DEEP-RESEARCH-PROMPT.md` → `FINAL-ProThinking-RESEARCH-PROMPT.md`
  rename, and the three files that show as modified — those three appear to be CRLF/LF
  normalization noise only, not content changes, but will be committed as-is rather than
  cherry-picked).
- Patch generation will be **batched by the report's 12-step implementation dependency order**
  (fixtures → schemas → inventory → extraction → topic maps → semantic contracts →
  dossiers/atlas → acceptance → impact/incremental → retrieval → orchestration/profiles →
  package cleanup), not one mega-prompt for all 80+ files at once. Each batch is its own
  prompt → patch set → pull/apply/verify cycle.

## Step 1 — This plan

Recorded here. No code or repo changes yet.

## Step 2 — Commit and push the research export to `main`

Working tree state (`apexai-os-meta`, already on `main`, in sync with `origin/main`):

```
 M  01-CURRENT-APEX-KB-FAILURE-ANALYSIS.md
 M  04-Apex-KB-Current-Research-Index.md
 M  05-Apex_KB_Current_Research_Index.machine-readable.yaml.md
 D  FINAL-DEEP-RESEARCH-PROMPT.md
 ?? FINAL-ProThinking-RESEARCH-PROMPT.md
 ?? ProThink-Report/   (contains both report files)
```

Actions:
1. `git add` the entire `FutureDevelopments&Research/.../ApexKBFinalDesignDeepResearch/` folder
   (covers the modifications, the deletion/rename, and the new `ProThink-Report/` directory).
2. Commit with a message describing this as landing the Apex KB final-architecture research
   export and renaming the deep-research prompt file.
3. Push to `origin main`.

**This is a push to a shared branch — confirm with the operator immediately before running
`git push`, per the standing safety rule, even though the direction has been set in this plan.**

Record the resulting commit hash; it becomes the `research_start_commit`-equivalent anchor
that every batch prompt in Step 3 will cite, so GPT-5.6 reads the report from a fixed, known
`main` state rather than a moving target.

## Step 3 — Author the GPT-5.6 handoff prompts (one per implementation-dependency-order unit)

Create a new prompt file per batch (e.g. under a new
`.../ApexKBFinalDesignDeepResearch/ProThink-Report/patch-prompts/` folder), named after the
report's own 12 units, e.g. `01-fixtures-and-baseline.md`, `02-schemas-and-references.md`,
`03-inventory.md`, `04-extraction.md`, `05-topic-maps.md`, `06-semantic-capsules-and-templates.md`,
`07-dossier-and-atlas.md`, `08-acceptance.md`, `09-impact-and-incremental.md`,
`10-retrieval.md`, `11-orchestration-and-profiles.md`, `12-package-cleanup.md`.

Each prompt file must:

1. **Pin evidence**: state the exact `main` commit hash from Step 2, the two report file paths,
   and instruct GPT-5.6 to treat the deep-research report as binding architecture (not to
   re-derive it) while reading current file contents from `main` directly via GitHub for ground
   truth of "what exists today."
2. **Scope to one unit only**: name the specific target paths for that unit, pulled from the
   report's "Final target tree", "Current package disposition matrix", and the three design-record
   tables (`Control-plane file design records`, `Schemas and templates`,
   `Runtime and test design records`, `KB-instance artifact design records`) — quoting the
   relevant rows so GPT-5.6 doesn't have to re-search the whole 3,245-line report per file.
3. **Require one patch file per target file**: unified diff / `git apply`-compatible format,
   one file per patch, named after the target path (slashes → some safe separator), output as
   a downloadable bundle. New files are a diff against `/dev/null`; removed files (e.g. the
   deprecated `lifecycle-state-machine.md`) are a diff to `/dev/null` plus the migration note
   the report requires before removal.
4. **Carry forward the report's hard constraints** so GPT-5.6 doesn't improvise beyond the
   architecture: no candidate truncation, no duplicated schema ownership, preserve public CLI
   command names/flags in `apex_kb.py`/`apex_kb_retrieval.py`, don't invent files outside the
   final tree, follow the disposition column (`keep`/`change`/`add`/`merge`/`remove`/`configurable`)
   exactly for each listed path.
5. **State the batch's own completion evidence**, copied from the report's
   "Implementation dependency order" table row for that unit, so GPT-5.6 knows what "done" means
   for this batch specifically (e.g. unit 5's evidence is "candidate beyond rank 30 retained; no
   top-N loss; direct reasons visible").
6. **Require a manifest** at the end of each batch's output: list of patch files produced, the
   target path each corresponds to, and any target file the batch intentionally left untouched
   with a reason (so nothing silently drops off the list between batches).

Draft all 12 prompt files in this step; only unit 1's prompt needs to be handed off immediately,
since later units depend on earlier ones landing first (per the dependency order).

## Step 4 — Run externally, then pull and apply

This step is manual/external and repeats per batch:

1. Operator runs the batch prompt in GPT-5.6 heavy-thinking mode (outside this tool, since this
   session cannot invoke that model directly).
2. Operator brings the resulting patch bundle back (e.g. saves it into
   `patch-prompts/<unit>/incoming/`).
3. In this tool: review each patch's target path against the report's disposition table before
   applying (no blind `git apply -p0` on everything), apply with `git apply` (or manual
   placement for brand-new files where a clean patch context doesn't exist yet, e.g. the first
   files in a new `apex_kb_runtime/` package).
4. Run the batch's fixtures/tests named in the report (`apex-meta/tests/apex_kb/...` once it
   exists) and the batch's stated completion evidence.
5. Commit the applied batch locally; confirm with the operator before pushing to `main` again
   (same push-confirmation rule as Step 2).
6. Move to the next unit's prompt only after the current unit's completion evidence passes.

## Verification

- After Step 2's push: `git log --oneline -3` and `git status` on `main` should show a clean
  tree with the new commit, and the two report files should be fetchable from `origin/main` by
  path (this is what makes them visible to a GitHub-connected GPT-5.6 session).
- After each Step 4 apply cycle: `git apply --check` before applying for real; run whatever
  automated tests exist for that unit; spot-check that no file outside the unit's declared scope
  changed (`git diff --stat`).
- Before advancing dependency units, confirm the current unit's "observable completion evidence"
  cell from the report's implementation-dependency-order table is actually satisfied, not just
  that patches applied cleanly.