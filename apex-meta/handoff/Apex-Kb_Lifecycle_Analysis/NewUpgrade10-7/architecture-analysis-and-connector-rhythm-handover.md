# Handover — Apex KB Architecture Analysis + Connector-Native Compile Rhythm (Research & Patch Commission)

> **You are the researcher/implementer.** Your job is to (1) research the design questions below,
> (2) author patch files **against current `main`**, and (3) produce a verification plan. You do **not**
> get to declare the work done — a separate controller (the operator + a terminal-backed Claude Code
> session) verifies your patches afterward. Do not self-certify. If a recommendation below is not marked
> ✅ verified, treat it as a hypothesis to confirm, not a fact.

---

## 0. Role & boundaries

- **Validator/implementer separation is deliberate.** The analysis in this file was produced and
  validated by a prior session; you implement; the controller verifies. Keep these three roles distinct.
- **No self-grading.** "I wrote the patch and it looks right" is not evidence. The controller runs the
  deterministic checks in §9 and reviews `git diff`.
- **Author patches against CURRENT `main`, not a snapshot.** See §6 — the previous patch pack was built
  on a stale baseline; one patch failed to apply and *would have deleted working code*. Diff the live
  files first, every time.

---

## 1. Complete validated analysis (macro / meso / micro)

### Measured surface (facts, counted this session)
- **Skill docs:** 18 files, **1,995 lines**. `SKILL.md` + everything under `references/` = **1,239 lines
  (62%)**. Largest files: `templates/wiki-page-templates.md` (341), `references/acceptance-tests.md`
  (253), `SKILL.md` (221).
- **Scripts:** `apex-meta/scripts/apex_kb.py` (2,313 lines) + `apex-meta/scripts/apex_kb_retrieval.py`
  (802 lines) = **3,115 lines**, **26 subcommands** (25 functionally distinct; `coverage` aliases
  `quality`). Standard-library only, no network, no shell-out, default dry-run, writes require
  `--allow-write`.

### The decisive lens — a connector-only LLM (ChatGPT-style browser chat + git connector, no terminal)
- It can **read and write files** via the git connector and **nothing else**. **Zero of the 26
  subcommands** are runnable by it. No postflight, no `quality`, no `lint`, no `index`, no retrieval.
- Therefore **~1,100 of the 1,995 doc lines are non-actionable** for that executor (all of
  `script-command-contract.md`, `retrieval-contract.md`, `acceptance-tests.md`, both `*-lint-spec.md`,
  `lifecycle-state-machine.md`, `examples/powershell-commands.md`). Its real job is ~4 steps: read
  sources → draft Phase 1 analysis → draft Phase 2 pages to the value contract → write them + emit a
  `compiled_unvalidated` handoff.
- **Core defect:** the skill does **not partition by capability**. The recent patch added a capability
  *precheck* (record what you can do) and a completion-state *cap* (don't overclaim) — both correct — but
  it does **not branch the procedure**. The least-capable executor faces the same 2,000-line maze as the
  most-capable one and must infer for itself that more than half of it doesn't apply. This is the single
  biggest followability problem and is exactly the operator's stated concern.

### Macro — mostly VALIDATED
- ✅ **Two-plane split** (deterministic Python plane vs semantic LLM plane) is sound and is genuine best
  practice; cleanly declared in `SKILL.md` (`python_owns` / `llm_owns`).
- ✅ **Source-preserving custody** (canonical vs derived; indexes are rebuildable, never sole truth) is
  sound.
- ✅ **Target now realized for a terminal executor.** The quality gate rebuilt this session catches the
  thin-but-structurally-complete pages that caused the original failure (validated — see §2).
- ⚠️ **Weakness:** the architecture is implicitly terminal-executor-centric. Connector-only is a bolt-on
  (a state cap), not a first-class execution path.

### Meso — coherent but over-represented
- ⚠️ The lifecycle is stated **three times**: the `SKILL.md` 12-step procedure, the `operator_flow` A–D
  block, and the 12-state `references/lifecycle-state-machine.md`. The state machine is "deprecated"
  only *by reference* in `package-manifest.md` — **the file itself has no in-file deprecation banner** and
  reads as authoritative.
- ⚠️ **Duplication:** the Phase 2 page-value contract appears in ~4 files (`kb-contract.md`,
  `wiki-page-templates.md`, `ingest-query-lint-audit-rules.md`, `SKILL.md`); the boundary/no-mutation
  clause in ~4; the phase-gate policy in ~3. Redundant, **not contradictory** post-patch — but it
  inflates reading cost, which is what hurts a connector LLM most.
- ⚠️ **5 named output tiers** add classification load (R04 already flagged this).

### Micro — quality gate fixed; CLI footguns remain (terminal-only impact)
- ✅ `quality` / `coverage` is now reason-coded and was validated this session against the 6 R02
  reference pages (see §2).
- ⚠️ CLI footguns that bite a *terminal* executor (irrelevant to a connector executor, which can't run
  the CLI at all): **silent dry-run** (forget `--allow-write` → success-looking output, zero writes);
  **aliases** (`quality`/`coverage`, `graph`/`process-graph`, three names for the payload-manifest
  command); **flag-placement magic** (`normalize_global_flag_placement` silently relocates a hard-coded
  flag set only); three similar `lint*` commands; non-obvious args (`--analysis` is a filename under
  `ingest-analysis/`, not a path; `--approval-phrase` must match the gate; `--confirm-clear-index` is a
  token, empty = no-op).

### Best-practice scorecard
✅ progressive disclosure (nav table) · ✅ determinism/semantics split · ✅ executable acceptance tests ·
✅ source grounding · ❌ single-authority (duplication remains) · ❌ capability-based routing · ~ naming
clarity.

### Connector-native rhythm — viability hypothesis (confirm/refine; do not assume)
- **Viable — per-file self-validation.** A connector LLM can re-read each page immediately after writing
  it and check it against the exact reason-codes the quality engine now emits (`single_claim_summary`,
  `single_claim_concept_thin`, `thin_macro_meso_micro`, `concept_micro_not_evidenced`,
  `claim_pointer_coverage_below_100_percent`, `placeholder_text`, `missing_source_refs`,
  `missing_phase2_value_sections`, `no_query_routes`, `summary_source_breadth_below_profile`). These are
  all *readable* properties — no Python required.
- **Viable — the rhythm itself.** One page per commit, small writes, is exactly what the connector's
  technical limits favor. The original max-run already worked in that rhythm — it just lacked a per-file
  "definition of done." Keep the rhythm, add the gate at each step, sized to one page per context window.
- **Not viable — deterministic certification.** Hashes, the machine quality result, retrieval freshness,
  and the retrieval index stay terminal-only. A connector run caps at `compiled_unvalidated` and hands
  off (already enforced by the patch).

### Load-bearing design principle (operator-confirmed) — this governs the whole rhythm design
> **The connector LLM is trusted to CREATE wholly new files or perform COMPLETE whole-file rewrites
> only. The moment anything requires an in-place update/mutation of an existing file — appending to
> `wiki/index.md`'s machine section, the retrieval index, hash ledgers, or any partial edit — that is
> Python/terminal work, never the connector LLM's.**

This is not a limitation to route around; it is the design. It **removes the fragile
hand-maintained-index path entirely**: the connector never touches the index; a later terminal
`apex_kb.py index` regenerates it deterministically. It is the concrete, testable form of the
determinism/semantics split — **LLM owns whole-artifact semantic authoring; Python owns all mutation and
derivation.** Every rhythm-design decision you make must respect it.

---

## 2. Already done this session — DO NOT redo

- **7 markdown/YAML patches applied** to the skill (from an external draft pack, reconciled against live
  `main`): `SKILL.md` (capability precheck + state cap + completion gate), `script-command-contract.md`
  (postflight evidence contract), `package-manifest.md` (lifecycle-authority clause),
  `acceptance-tests.md` (Phase 2 thin-page regression fixtures), `ingest-query-lint-audit-rules.md`
  (Phase 2 acceptance & repair loop), `kb-schema-template.md` (fixed the contradictory
  `ingest_phase_2_requires_phrase` field).
- **`apex-meta/scripts/apex_kb.py` quality engine rebuilt and validated.** The draft patch failed
  `git apply` and was built on a stale stub of `quality_report`; it was **hand-merged** onto current
  `main` instead. During the merge, **5 real bugs in the draft were caught and fixed**:
  1. section extraction matched only `##` headings, but Macro/Meso/Micro use `###` → all sub-layer word
     counts were 0 → `thin_macro_meso_micro` fired on every page;
  2. ranked-source regex matched only `source_id:`/`source_path:`, but real pages use plain `source:` →
     ranked-source count was always 0;
  3. a universal per-page-type narrative word floor (180/140/90) flagged even the two R02-validated
     *passing* pages — this is the "universal word threshold" R02 explicitly rejected; removed;
  4. single-claim rule was `== 0`, but R02's rule for summaries is `< 2` (the actual root-cause pattern);
  5. missing `CONCEPT_MICRO_NOT_EVIDENCED` rule and the narrow-entity concise exception.
  The result was validated against all 6 R02 reference pages and behaves exactly as R02's manual analysis
  predicted (thin pages flagged with correct reason codes; the strong summary, valid narrow entity, and
  strong multi-source concept pass clean).
- **Two handover items had NO patches in the pack and remain OPEN** (see `patch-plan-handover.md` §5
  items #6 and #9):
  - **#6** — `references/lifecycle-state-machine.md` still has 12 states and **no in-file deprecation
    banner** (only referenced as deprecated from `package-manifest.md`).
  - **#9** — `examples/lifecycle-runbook.md` is **not marked example-only**.

---

## 3. Central research commission — the connector-native compile rhythm

Design a **per-file `create-or-full-rewrite → self-validate` loop** for a connector-only LLM, under the
load-bearing principle in §1 (whole-file authoring only; all in-place updates/mutations = Python).

Deliverables for this section:
1. **The per-page "definition of done" checklist** — derived directly from the quality reason-codes in
   §1 so that what the LLM self-checks at authoring time is the *same standard* the terminal `quality`
   gate enforces later. (Goal: a page that passes the connector self-check should pass terminal
   `quality --strict`. Verify this equivalence.)
2. **Where the instruction lives** — the smallest, best-placed home in `SKILL.md` (or a single new
   short reference) so a connector LLM reaches it early and does not have to read the deterministic half.
   Prefer editing existing structure over adding a new file.
3. **Context-window sizing** — how to instruct the LLM to compile **one page per context window**:
   read the source slice + the contract + the checklist, author the whole page, self-validate, write,
   commit, then move on. Make explicit that it must **not** batch many pages into one pass (the original
   failure mode).
4. **The mutation boundary, stated in the instruction itself** — "you create new files or fully rewrite
   a file you own; you never partially edit an existing file, never append to `wiki/index.md`, never
   touch derived indexes; those are regenerated by a terminal `apex_kb.py index` / retrieval build after
   handoff." Include the `compiled_unvalidated` cap + handoff packet contents.
5. **Answer the viability question explicitly** — confirm or refine the §1 hypothesis with reasoning,
   and state any case where the whole-file-only rule is insufficient (e.g. a KB that has no terminal
   executor available at all — what is the truthful terminal state then?).

Open sub-questions to resolve in your design note:
- What is the authoritative source of the per-page checklist — is it hand-maintained in `SKILL.md`, or
  generated from the `apex_kb.py` reason-code list so the two can't drift? (Drift here re-creates the
  original "docs say one thing, code does another" failure.)
- Should there be a machine-checkable **connector compile manifest** (a small file the connector writes
  listing the pages it authored + its self-check verdict per page) so the terminal controller can diff
  self-claimed vs actually-measured quality? Weigh this against the anti-over-engineering rule in §6.
- How does a connector run declare "I could not run any deterministic step" so the state truthfully caps
  at `compiled_unvalidated` without the LLM having to read the whole deterministic contract to discover
  that?

---

## 4. Implementation options — research, decide, and JUSTIFY each

Each option must be justified against the deletion rule ("keep/add only when it prevents a named observed
failure, is executable or directly controls an executable transition, and isn't already authoritative
elsewhere"). **Net effect across all adopted options must REDUCE the effective surface, not grow it.**

- **(a) Capability-first entry router in `SKILL.md`.** A short block at the very top: "If you cannot run
  terminal Python (e.g. connector-only chat), your entire role is X, read only files Y, produce only
  artifacts Z, cap state at `compiled_unvalidated`, hand off." Highest impact for the operator's stated
  concern; small text addition that removes a large *effective* navigation cost. Recommended — confirm.
- **(b) Finish consolidation / de-duplication + in-file deprecation banner.** Add the missing in-file
  deprecation banner to `lifecycle-state-machine.md` (open item #6) and mark `lifecycle-runbook.md`
  example-only (open item #9); define the Phase 2 page-value contract **once** (canonically in
  `kb-contract.md`) and have the other 3 files reference it rather than restate it. Pure surface
  reduction.
- **(c) CLI footgun fixes** (terminal-executor ergonomics) — e.g. make a missing-`--allow-write` write
  attempt emit a loud "dry-run: no writes performed" banner; document the aliases in one place. Small,
  optional; does not touch the connector path.
- **(d) Optional aggregate `postflight` command** — one command that runs index + retrieval build +
  stale + lint --strict + quality --strict + status and emits the single evidence packet. Collapses 6
  invocations into 1 for the terminal executor. Optional per R01/R05; only if it reduces error surface
  without becoming a workflow engine inside `apex_kb.py`.

---

## 5. All open questions

Carry forward the still-open operator decisions from `patch-plan-handover.md` §8 (Phase 1→2 policy
confirmation, target-query authority, semantic-partial handling, threshold calibration, pointer-minimum
granularity, reviewer-escalation threshold, pointer-only custody, Phase 1 persistence), **plus** the new
rhythm-design questions:
- per-page checklist authority (hand-maintained vs generated from reason-codes — see §3);
- whether to add a connector compile manifest (§3);
- context-window sizing rule (§3);
- for options (a)–(d): which are adopted, and the justification for each.

---

## 6. Constraints / must-not

- No page-value **score**, no new **roles**, no new **lifecycle document**.
- **Keep** the determinism/semantics split; **keep** source-manifest / payload-manifest architecture,
  canonical-vs-derived distinction, retrieval backend (`apex_kb_retrieval.py`), and existing wiki pages —
  do not touch these as part of a *process* patch.
- **Connector LLM creates whole files or does full rewrites only. All in-place updates/mutations (index,
  hashes, partial edits, `wiki/index.md` machine section) are Python/terminal.** This is the governing
  rule (§1).
- **Author every patch against CURRENT `main`.** The previous pack used a stale baseline: `002-apex_kb.py`
  failed `git apply` outright and its `quality_report` rewrite would have silently deleted fields the live
  code depends on (`unmanifested_source_refs`, `manifest_sources_without_pages`). Before writing any
  patch, read the live target file and diff against it. Prefer patches that a terminal Claude Code session
  applies with `Edit` (unique-match) + `git diff` as proof, over hand-authored line-numbered diffs.
- Net effect must **reduce** the effective instruction surface, especially for the connector executor.

---

## 7. Deliverables you (the next chat) must produce

1. **A design note** answering the §3 viability question and the §5 open questions, with reasoning.
2. **Patch files authored against current `main`**, scoped to the files in §8, each with a one-line
   rationale tied to a named failure or a §4 option.
3. **A verification plan** the controller can run (the §9 checks, plus any new fixture your rhythm needs
   in `acceptance-tests.md`).

---

## 8. Files in scope / out of scope

**In scope** (carry forward `patch-plan-handover.md` §5, minus what's already done in §2):
- `.claude/skills/apex-kb/SKILL.md` — capability router (option a), rhythm instruction (§3).
- `.claude/skills/apex-kb/references/lifecycle-state-machine.md` — in-file deprecation banner (open #6).
- `.claude/skills/apex-kb/examples/lifecycle-runbook.md` — mark example-only (open #9).
- `.claude/skills/apex-kb/references/kb-contract.md` **/** `ingest-query-lint-audit-rules.md` **/**
  `templates/wiki-page-templates.md` — de-duplicate the page-value contract to one canonical home
  (option b). Confirm with operator before editing `kb-contract.md`/`wiki-page-templates.md` (they were
  deferred to a "second wave" in the prior handover).
- `apex-meta/scripts/apex_kb.py` — only if option (c) or (d) is adopted.
- `.claude/skills/apex-kb/references/acceptance-tests.md` — any new fixture for the rhythm.

**Out of scope** (carry forward `patch-plan-handover.md` §6): `apex_kb_retrieval.py`, the retrieval
backend, existing wiki pages under `apex-meta/kb/.../wiki/`, `query-eval-pack.json` content, graph
behavior, and everything under the repo's excluded backup/recovery/source-knowledge dirs.

---

## 9. Verification the controller will run (design your patches to pass these)

- `python -m py_compile apex-meta/scripts/apex_kb.py` (if the script is touched).
- `quality --strict --json` and `lint --strict --json` against a scratch KB (reuse the
  `acceptance-tests.md` smoke-KB pattern; do not invent a new harness).
- The `acceptance-tests.md` fixtures end-to-end, including any fixture you add.
- **Equivalence check for the rhythm:** a page authored to pass your connector self-check must also pass
  terminal `quality --strict` — demonstrate this on at least one authored page.
- `git diff` reviewed file-by-file. No self-declared completion without it.
- A **connector-simulation dry-read**: confirm that following only the connector path in `SKILL.md`
  (reading only the files the router permits) is sufficient to produce a contract-compliant page — i.e.
  the router genuinely lets the connector LLM ignore the deterministic half.
