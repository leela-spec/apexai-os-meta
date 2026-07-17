# Apex KB Lean-Funnel Leela Execution Handover (v2 — supersedes the corpus-map handover)

## 0. Why this document replaces `APEX_KB_FULL_CORPUS_EXECUTION_HANDOVER.md`

That handover's Phase 1 ("install Bundle 1: exhaustive corpus map") instructed building a `corpus-map`
command that writes one `topic-source-map.json` containing every scanned source under every topic,
plus a mandatory per-candidate source-atlas disposition for all of them. **That is not a hypothetical
risk — it already happened.** The artifact sits right now at:

```text
C:\GitDev\worktrees\leela-full-corpus-kb\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\manifests\phase0\topic-source-map.json
```

**8,895,030 bytes.** A read-only diagnostic audit of that exact run found: all 197–264 sources
appended to every one of ~10 topics regardless of signal, headings duplicated once per topic (43,100+
duplicate heading objects), and a Skill Tree topic that reviewed 197 candidates to retain **5** useful
sources — with 192 ledger entries reading "does not directly support a final material claim." The
combined map was ~2.3M estimated tokens before any canonical source was even opened. This is the
overload that broke the prior semantic runs. Do not rebuild it.

The root confusion in the old approach: it conflated *"we deterministically considered every
source"* (custody — fine to be exhaustive, costs nothing) with *"the LLM must semantically account for
every source"* (review — expensive, and the thing that overloads). The corpus-map/mandatory-atlas
design made every matched candidate an LLM writing obligation. The lean funnel below keeps the first
half (nothing is ever silently dropped) and fixes the second (the LLM only ever reads a small,
concentrated, gap-justified set).

**The lean funnel is already built, tested, and on `origin/main` of `apexai-os-meta` as of commit
`26f54f90`** ("Sharpen Apex KB Phase 0 into a lean deterministic funnel"). This handover assumes that
commit exists; verify it (Section 2) before doing anything else. There is no "Bundle 1/2/3 install
phase" anymore — skip straight to running it.

## 1. Mission and completion target

One chat (terminal-backed, e.g. Codex or Claude Code with Python execution) runs the Leela product
corpus through the lean Apex KB funnel and delegates semantic compilation to a browser-connected
high-reasoning LLM session, exactly as the prior handover's Git/Codex/ChatGPT-web split intended — only
the deterministic engine and the semantic input shape have changed.

The build is complete only when:

- Every scoped source is deterministically inventoried, including non-text/unreadable ones (visible,
  never silently dropped).
- Every locked topic has an **exhaustive** ranking (`topic-source-rankings.json`) — no top-N
  truncation — with every candidate's tier and reasons inspectable.
- Every locked topic has a **bounded work pack** (`work-packs/<topic-slug>.md`) that concentrates the
  exhaustive ranking without discarding anything (held-back sources stay visible in custody).
- Every critical and routine target question is answerable from compiled wiki pages, using material
  sources actually read from the work pack — pulling further sources only while a target question
  remains genuinely unresolved (continue-by-gap, never a fixed read count).
- Independent, clean-context page-only and claim-entailment evaluation passes (two layers — there is
  no third "atlas completeness" gate to satisfy).
- Deterministic postflight passes with fresh retrieval.
- The finished work is merged and pushed to `leela-spec/leela` `main`.

Do not substitute file counts, headings, self-review, a reconstructed full-candidate atlas, or the
existing canary's acceptance records for this target.

## 2. Verified starting state (re-verify — this document is a snapshot)

### Repositories and commits

- Apex implementation repository: `C:\GitDev\apexai-os-meta`
- Apex `origin/main` at handover time: `26f54f90` ("Sharpen Apex KB Phase 0 into a lean deterministic
  funnel") — **re-run `git -C C:\GitDev\apexai-os-meta fetch origin && git -C C:\GitDev\apexai-os-meta
  log --oneline -1 origin/main` and confirm this commit or a later one is present before proceeding.**
  If it is not present, stop: the lean funnel (tiered ranking, work packs, L1 facts) is not there yet
  and running Phase 0 will not behave as this document describes.
- Leela repository: `C:\GitDev\leela`
- Leela `origin/main` at handover time: `793461e` ("Merge origin/main into main")
- The primary worktrees of **both** repos are dirty right now (Leela has pending
  folder-comparison-report deletions and untracked new content; Apex's primary worktree carries
  unrelated in-progress work). **Do not update, clean, reset, commit to, or reuse either primary
  worktree for this run.**
- Existing isolated worktrees from the prior attempt are **stale** — they predate commit `26f54f90` on
  the Apex side and contain the old bloated `topic-source-map.json`/`corpus-map` artifacts on the
  Leela side:
  - `C:\GitDev\worktrees\apex-kb-corpus-map` (at `b5dca52c`), `apex-kb-corpus-map-clean` (at
    `0936170b`) — both predate the lean funnel. Do not reuse; create a fresh Apex worktree from current
    `origin/main`.
  - `C:\GitDev\worktrees\leela-full-corpus-kb`, `leela-manual-browser-full`,
    `leela-manual-semantic-test` — all contain the old failed run's derived artifacts. Do not reuse
    their `manifests/phase0/` output; either create a fresh Leela worktree, or reuse
    `leela-full-corpus-kb`'s branch **only** after deleting its entire `manifests/phase0/` directory
    (it is 100% derived/rebuildable — see `package-manifest.md`'s canonical-vs-derived split) and
    regenerating it with the new `phase0`.

Create fresh isolated worktrees:

```powershell
git -C C:\GitDev\apexai-os-meta fetch origin
git -C C:\GitDev\apexai-os-meta worktree add C:\GitDev\worktrees\apex-kb-lean-funnel -b codex/apex-kb-lean-funnel origin/main

git -C C:\GitDev\leela fetch origin
git -C C:\GitDev\leela worktree add C:\GitDev\worktrees\leela-lean-funnel -b codex/leela-lean-funnel origin/main
```

### Current Leela KB

```text
C:\GitDev\worktrees\leela-lean-funnel\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki
```

(If continuing from `leela-full-corpus-kb` instead, delete its `manifests/phase0/` directory first —
see above.)

The prior remote `origin/main` state for this KB does not pass a fresh deterministic check (stale
source-payload/index state per the old handover's own verification). Treat any inherited wiki/ledger
content as reusable draft material only, not an accepted result.

### Source corpus and priority folders — reconfirm during Phase 2's Q&A, do not blindly re-adopt

The source root and priority-folder table below are **carried over from the prior handover as a
starting proposal**, not a locked decision. Time has passed; folder contents may have changed. Phase 2
below requires walking the operator through confirming or revising this table before it is used.

```text
C:\Quasi Desktop\Leela New 26\Obsidian Leela New 01-26
```

| Priority (prior run) | Folder | Files | Markdown | Other text | Binary/other |
|---|---|---:|---:|---:|---:|
| newest | `Upgrades\Night4\Updates new` | 11 | 9 | 0 | 2 |
| newest | `New Leela Data` | 80 | 35 | 8 | 37 |
| newest | `MVP, User Stories & Flows` | 8 | 4 | 4 | 0 |
| second | `Prototyp Spark\Wireframes  & Specs` | 70 | 58 | 0 | 12 |
| supporting | `02_Interconnections` | 3 | 3 | 0 | 0 |
| supporting | `Concepts` | 11 | 10 | 1 | 0 |
| historical/general | `01_Features` | 14 | 14 | 0 | 0 |

The prior run also named ten specific priority files requiring complete reads regardless of
deterministic score. Reconfirm this list still applies in Phase 2 rather than assuming it.

Proposed locked topics (also to be reconfirmed, not assumed, in Phase 2):

1. Epic as the creator package and upstream content/data container.
2. Skill Tree.
3. Path.
4. Sequence and sequencing.
5. Rhythm.
6. Stats.
7. Algorithm.
8. Feature interconnections and end-to-end user flows.
9. User stories, personas, permissions, and acceptance criteria.
10. How a creator creates an Epic and its content — highest priority.

## 3. Does the `apex-kb` skill need to live inside the Leela repo? **No.**

Verified directly, not assumed:

- `apex_kb.py`'s `repository_semantic_contract_dir()` resolves its assets path as
  `Path(__file__).resolve().parents[2] / ".claude" / "skills" / "apex-kb" / "assets" / ...` — i.e.
  **relative to where the script itself lives**, never relative to `--kb-root`. Scaffold already
  copies the repository-local semantic contract into the KB (Leela's KB already has its own
  `semantic-contract/` folder from a prior scaffold run — confirmed present at
  `LeelaAppDevelopment\LeelaApp-Index-KB-Wiki\semantic-contract\`). Cross-repo invocation with
  `--kb-root` pointing into a different repository entirely is the intended, already-working pattern —
  the prior handover already ran this way successfully (405 manifest entries, 264 Phase 0 files
  scanned against the current remote KB).
- **13 other knowledge bases** inside `apexai-os-meta` (`apex-meta/kb/therapy`,
  `apex-meta/kb/claude-code-orchestration-design`, `apex-meta/kb/lika-verein-taxes-accounting`, and 10
  more) depend on `.claude/skills/apex-kb/` and `apex-meta/scripts/` staying together at the Apex
  repo's own root. Moving either into the Leela repo would break all of them and would also break the
  `parents[2]` assumption above unless *both* moved together in lockstep — which is unnecessary
  destructive work for a pattern that already works today.

**Do not move, copy, or duplicate the skill folder or runtime scripts into the Leela repo.** Invoke
`apex_kb.py` from the Apex worktree with `--kb-root` pointing into the Leela worktree, exactly as
below. The only thing that legitimately lives inside the Leela KB is the repository-local
`semantic-contract/` copy that `scaffold` already produces there — that is by design (it lets a
connector/browser session that can only read inside the Leela repo still see the authoritative
contract without crossing repos).

## 4. Phase-by-phase execution

### Phase 0 — Capability and authority gate

Read, from files rather than memory:

- `C:\GitDev\worktrees\apex-kb-lean-funnel\.claude\skills\apex-kb\SKILL.md`
- Its `references/semantic-value-contract.md` (now documents the L1–L5 funnel and the work pack as the
  semantic input), `references/topic-registry-v2.schema.json` (vocabulary fields), and
  `references/topic-work-pack.schema.json`.
- The Leela repository-local `semantic-contract/` and `HANDOVER_LLM_PHASES.md` from the fresh Leela
  worktree.
- This handover.

```powershell
$APEX = 'C:\GitDev\worktrees\apex-kb-lean-funnel'
$KB   = 'C:\GitDev\worktrees\leela-lean-funnel\LeelaAppDevelopment\LeelaApp-Index-KB-Wiki'

python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --json health
python "$APEX\apex-meta\scripts\apex_kb_retrieval.py" --kb-root $KB --json health
git -C C:\GitDev\worktrees\leela-lean-funnel status --short --branch
gh auth status
python -m unittest discover -s "$APEX\apex-meta\scripts\tests" -p "test_*.py"
```

The last command must show all tests passing (29 at handover time) before you trust the engine
against real Leela data.

Browser gate (unchanged from the prior handover):

1. Open ChatGPT (or the equivalent connector) in the terminal-backed executor's browser tooling.
2. If signed out, ask the operator to sign in and report readiness — a genuine blocker.
3. Verify a high-reasoning mode not labeled `Pro`; prefer the highest visible `Thinking`/`Extended`/
   `Heavy` option. Do not use Pro or Deep Research.
4. Verify the Git connector can read `leela-spec/leela` and a named working branch, or confirm a
   reliable upload/complete-file-return fallback.
5. Record the exact visible mode and connector result. Do not invent a model name.

### Phase 1 — Full Q&A / Target Lock (do this before any scan; do not skip)

**This is the step the operator explicitly asked to have added.** Do not silently re-adopt the Section
2 folder/topic table. Before scaffolding or running Phase 0, walk the operator through each decision
below as an options-with-tradeoffs conversation (offer 2–4 concrete choices with their consequences,
the way you would present a design decision to a colleague — not an open-ended "what do you want?").
Record the outcome directly in `manifests/topic-registry.json` and (if needed)
`manifests/analysis-config.json`.

For **each** of the ten proposed topics:

1. **Confirm or revise the topic itself.** Present the proposed topic name/slug and ask: still
   relevant, renamed, merged with another, split, or dropped? Use `references/semantic-value-contract.md`'s
   topic registry v2 section as the schema reference.
2. **Lock target queries.** For each topic, ask what critical/routine questions a future AI must be
   able to answer, with answer requirements and expected page route. Offer the prior run's implied
   questions (e.g. from `HANDOVER_LLM_PHASES.md` or existing wiki pages) as a starting draft the
   operator can accept, edit, or replace — never invent requirements silently.
3. **Lock vocabulary**, explaining what each field actually does (this is new since the prior handover
   — the old `keywords`-only field is still read as `supporting_terms` for compatibility, but the
   richer fields materially change ranking quality):
   - `phrases`/`aliases` — strong, multi-word or alternate-name signals; a match in a filename, H1, or
     heading is *never* suppressed by a negative term. Ask: what are the unambiguous ways this topic's
     name actually appears in Leela's files?
   - `supporting_terms` — weaker single-word signals that only count as `body_strong` with
     co-occurrence or multi-section spread.
   - `negative_terms`/`ambiguous_terms` — terms that must NOT alone justify a body-only match (e.g. the
     prior corpus had "tree" collide between "Skill Tree" and unrelated "family tree"/generic usage —
     ask the operator which terms in their vocabulary are similarly overloaded).
   - Explain the consequence directly: getting vocabulary right here is what keeps the exhaustive
     ranking's `body_strong`/`body_weak` tiers precise; it does not affect completeness (nothing is
     ever dropped outright — see Section 5) but it does affect what lands in the concentrated work
     pack versus `held_in_custody`.
4. **Offer the `manifests/analysis-config.json` choice** as one decision, not per-topic noise: default
   is every signal on `auto` (activates only when the corpus profile shows material for it — e.g.
   freshness only engages if Git history or frontmatter dates exist). Ask only whether the operator
   wants to force anything `on`/`off` (e.g. force `reference_graph: on` given Leela's heavy internal
   cross-linking, since `auto` requires link density ≥0.3 to self-activate and Leela's linking style is
   unverified at handover time).
5. **Reconfirm the seven priority folders and ten priority-file list** from Section 2: still accurate?
   Any folders renamed, merged, archived, or newly added since the prior run?

Only after this conversation is complete, write `manifests/corpus-scope.json` (roots/exclusions) and
the finalized `manifests/topic-registry.json`, and proceed to Phase 2.

### Phase 2 — Lock scope and source custody

```powershell
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --allow-write --json generate-source-payload-manifest --group-map "$KB\manifests\source-group-map.json"
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --json preflight
```

Compare all scoped external files against the repository source and raw copies by relative path and
SHA-256 (the exact-duplicate detection now built into Phase 0 will also surface this — see Section 5 —
but do the custody-level intake check first). Intake only missing or intentionally changed files. Do
not run `Materialize-ApexKBCorpus.ps1` (fixed external inventory, destructive cleanup, unnecessary
here — same exclusion as the prior handover).

### Phase 3 — Run the lean deterministic funnel

If reusing `leela-full-corpus-kb`'s branch instead of a fresh worktree, **delete
`manifests/phase0/` entirely first** — every file in it (including the old `topic-source-map.json`,
`corpus-map` outputs, and `duplicate-and-version-families.json`) is legacy from the removed
corpus-map mechanism and is not regenerated or read by the current code.

```powershell
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --allow-write --json phase0
```

This single command now produces everything the old three-command sequence (`phase0` + `graph` +
`corpus-map`) used to attempt, without the exhaustive-map explosion:

- `manifests/phase0/source-facts.json` — one row per scanned file (including non-text/unreadable),
  with section spans, freshness (Git-or-mtime), and exact-duplicate group size.
- `manifests/phase0/topic-source-rankings.json` — one exhaustive, tiered entry per topic. **No
  top-N cutoff**; a topic with 100+ signal-bearing files keeps all of them, each with a `why` object
  (which field matched) and at least one line/section pointer.
- `manifests/phase0/work-packs/<topic-slug>.{md,json}` — the bounded, concentrated semantic input per
  topic: filename/H1/heading tiers in full, plus an elbow-cut portion of the body tiers, duplicates
  collapsed to one representative, and a disclosure footer stating exactly how many sources were held
  back and why (`held_in_custody_count`, `zero_signal_custody_count`) with a pointer back to the full
  ranking file.
- `manifests/phase0/corpus-profile.md` — now also reports `optional_signal_availability` (which
  signals auto-activated and why), `normalized_text_duplicate_groups`, and `version_family_candidates`.

Before semantic delegation, verify:

- `source_file_count` in the JSON result equals the scoped file count; `blocked_file_counts` accounts
  for every non-text/unreadable file (never silently absent).
- For each locked topic, `candidate_count` in `topic-source-rankings.json` shows no suspicious round
  number (a real corpus should not land on exactly 30, 50, or any other suspicious cutoff — if it does,
  something regressed).
- `held_in_custody` + `zero_signal_custody` for each topic account for every scanned source not in
  `candidates` for that topic (test `test_custody_accounts_for_every_scanned_source` proves this holds
  on synthetic fixtures; spot-check it on the real corpus too).
- Each work pack's `disclosure` block reconciles with its topic's ranking file (same test coverage as
  above, `test_workpack_disclosure_reconciles_with_rankings`).

Commit and push this deterministic setup as the first Leela save batch.

### Phase 4 — Delegate semantic compilation through the browser-connected LLM

Same Codex/ChatGPT-web (or equivalent) ownership split as the prior handover: the terminal-backed
executor owns local execution, deterministic artifacts, Git commits and pushes; the browser session
owns source interpretation, Phase 1 semantic analysis, Phase 2 wiki synthesis, and fresh-context
semantic evaluation. What changed is **what gets handed over**:

For each topic batch, provide only:

- Repository, branch, exact commit.
- The repository-local semantic contract.
- The topic registry entry (target queries + vocabulary).
- **The topic's work pack** (`work-packs/<topic-slug>.md`) — not the full ranking file, and never the
  raw corpus.
- Existing source capsules/analyses valid for this run.
- The required output paths.

The semantic session must read the actual sources through the connector for anything in the work
pack's concentrated set. If, after reading the concentrated set, a critical or routine target question
remains unresolved, it may pull the next source named in `held_in_custody` (visible in the full
`topic-source-rankings.json`, referenced by the work pack's `disclosure.rankings_ref`) — this is the
continue-by-gap rule, and it is the *only* valid reason to read beyond the work pack. It must never
read the full exhaustive ranking file wholesale, and it must never be asked to produce a disposition
for every candidate — that mandatory-atlas obligation from the old handover is gone.

Required semantic outputs per topic (narrower than the old handover — no source atlas requirement):

- Phase 1 source analyses for every materially used source/hash.
- The per-topic semantic ledger (existing schema, unchanged), covering sources actually reviewed.
- One Macro/Meso/Micro dossier in `wiki/summaries/` (or `concepts/`/`entities/` per the existing page
  topology rules) with target questions answered, key claims with exact evidence pointers, and
  material sources only in its Adaptive Ranked Source Set.

After each topic batch: reread every written file, pull/capture the complete files, validate
JSON/Markdown structure and changed-path scope, run `quality --strict` for structural wiring, commit
and push the coherent batch.

### Phase 5 — Independent semantic acceptance

Unchanged in spirit from the prior handover, narrower in scope. A fresh session, same verified
high-reasoning mode, receives compiled pages and target questions first, without drafting rationale.

For every topic: answer every critical/routine query from compiled pages only
(`answerable`/`partial`/`not_answerable`/`blocked` with exact page pointers); independently sample at
least two material claims per page and verify against resolved source passages; write the
semantic-acceptance artifact.

`semantic_pass` requires: every critical/routine query answerable; every sampled material claim
supported. It does **not** require candidate/atlas one-to-one coverage or a full documentary-landscape
review — that was the old handover's Bundle 2 requirement, and it is exactly the mechanism that forced
every one of 197 candidates through review. Repair only reason-coded failures; reevaluate the affected
topic in a fresh context.

### Phase 6 — Deterministic completion and retrieval proof

```powershell
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --json semantic-acceptance-status
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --allow-write --json index
python "$APEX\apex-meta\scripts\apex_kb_retrieval.py" --kb-root $KB --allow-write --json build-index
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --strict --json lint
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --strict --json quality
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --json query-eval
python "$APEX\apex-meta\scripts\apex_kb_retrieval.py" --kb-root $KB --json stale
python "$APEX\apex-meta\scripts\apex_kb.py" --kb-root $KB --allow-write --json postflight
```

Run compiled-first retrieval tests for every locked target query, including the known prior failures
for Path, Rhythm, Sequence, Stats, Epic schema, and creator flows. Retrieval must return answer-bearing
sections, not only uncertainty notices.

### Phase 7 — Git completion

- Verify the Leela diff contains only scoped source/index corrections, Apex KB artifacts (the new
  lean-funnel Phase 0 outputs, not the old corpus-map ones), semantic outputs, derived retrieval
  outputs, audits, and this handover if intentionally retained.
- Rebase the working branch on current `origin/main`; merge; push `origin/main`.
- Report: exact Apex commit, Leela commit, browser mode used, topics completed, per-topic candidate
  count / concentrated-work-pack count / held-in-custody count (the new completion evidence — no
  atlas-row count), semantic verdicts, retrieval verdicts, and any genuinely blocked source formats.

Only report `query_ready` when semantic acceptance, deterministic postflight, and retrieval freshness
all pass.

## 5. What changed vs. the old handover, at a glance

| Old (corpus-map / Bundle 1-2-3) | New (lean funnel, already on `origin/main`) |
|---|---|
| `corpus-map` command, `topic-source-map.json` (8.9 MB, all sources × all topics) | `phase0` writes exhaustive-but-per-topic `topic-source-rankings.json`; no combined all-topic blob |
| Flat substring counting, top-30 cutoff on the *old* `phase0` ranking path | Tiered field-separated ranking (filename/H1/heading/body_strong/body_weak), **no cutoff at all** on the exhaustive set |
| Mandatory disposition for every candidate (source atlas, Bundle 2) | Concentration is a disclosed, elbow-cut selection into a bounded work pack; held-back sources stay visible in custody, never forced through semantic review |
| Semantic session reads the full candidate map | Semantic session reads only `work-packs/<topic>.md`, pulling `held_in_custody` sources one at a time only while a target question is unresolved |
| 4th acceptance layer: atlas completeness/faithfulness | Two acceptance layers only (page-only answerability, claim entailment) — unchanged from the existing schema, which never had a third layer |
| No numeric size gate anywhere | No numeric size gate either — concentration is by evidence tier + elbow cut, never a fixed file count or byte limit |

## 6. Stop conditions (unchanged)

Stop only for:

- The browser session cannot be authenticated or no non-Pro high-reasoning mode is available.
- The connector and upload/complete-file fallback both cannot provide reliable source reads and
  whole-file outputs.
- A required source cannot be read and no equivalent readable copy exists.
- Source identity or hashes cannot be reconciled safely.
- A deterministic or semantic gate exposes an unresolved target-integrity failure.

Do not stop for unrelated dirty files, incidental warnings, optional tools, or the need to continue
with the next `held_in_custody` source when a target question is genuinely still open.
