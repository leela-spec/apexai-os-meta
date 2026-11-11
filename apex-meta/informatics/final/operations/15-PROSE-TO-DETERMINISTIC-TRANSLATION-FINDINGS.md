---
type: Evidence
id: EVIDENCE-PROSE-TO-DETERMINISTIC-TRANSLATION-v1.0
title: Prose-to-deterministic translation findings — which contract rules can become gates, tests, or linters instead of prose
description: A rule-by-rule sweep of the global carrier, its nested specs, a subject repo's AGENTS.md, and its nested agent modules, classifying each rule by whether it can be checked deterministically instead of relying on an agent reading and remembering prose.
status: current_truth
tags: [evidence, deterministic-enforcement, gates, okf-validator, prose-vs-gates]
---

# Prose-to-deterministic translation findings

## 0. The thesis this answers

Prose instructions are not as reliable as a deterministic check — a gate, a test, a linter, a hook,
anything that runs the same way regardless of session length or model attention — for any rule
where a violation is observable in an artifact or a command's exit code. This is not a theory about
one rule in one repo; it is a claim about the whole instruction corpus (the global carrier, its
nested execution-mode specs, a subject repo's `AGENTS.md`, and that repo's nested `agents/*.md`
modules), and it should be checked against all four layers, not asserted from one incident.

This file does that sweep for one subject repo (`Leela-Cloud-2026`) against this corpus's four
layers, and separates what is **general** — true of any agent, any repo, because it is about the
corpus itself or about a pattern that generalizes — from what is **repo-specific** — true only
because of one repo's own file layout and tooling.

## 1. What already exists — the pattern is proven, not novel

This corpus already has two mature, working examples of exactly this translation, which is why §3's
catalog recommends more of it rather than inventing the idea:

- **`tools/okf_validator.py`** already enforces, deterministically, a subset of the governance
  schemas in `specs/governance-schemas.md`: frontmatter presence and parsing (`GS-07`), the root
  index's `okf_version` declaration (`GS-06`), link integrity inside a governed index
  (part of `GS-06`'s family), and a sentence-length advisory (the `WP-14`/`GS` relationship in
  §5 of that file). It classifies findings into `OKF_ERROR` / `APEX_PROFILE_ERROR` /
  `ADVISORY_WARNING` — a severity model worth reusing rather than reinventing per repo.
- **The subject repo's `scripts/check_instruction_integrity.py` (Claude-Code-specific lane)**
  implements a separate validator for Claude Code modular rules: it enforces that every
  `agents/*.md`-style rule file declares a `paths:` key (so Claude Code injects it lazily on
  glob match), checks citation resolution, rule placement, and rule-destination consistency.
  **Cross-agent scope limit:** `.claude/rules/*.md` `paths:` YAML frontmatter, `PreToolUse`
  hooks, and `Stop` hooks are **Claude Code-only mechanics** (verified against official Claude
  Code docs vs. OpenAI Codex CLI's hierarchical `AGENTS.md` / `AGENTS.override.md` and Google
  Gemini CLI's hierarchical `GEMINI.md` + eager `@path` imports). Codex CLI and Gemini CLI do
  not load rules via `paths:` frontmatter globs. It is wired into `scripts/gates.py`, and its own
  sabotage self-test (`sabotage_audit.py`, scenario `I5`) proves the enforcement fires inside Claude
  Code workflows.

Both predate this sweep. The catalog below asks, for every remaining prose rule: does this pattern
apply here too, and has anyone actually built it, or only declared that it should exist?

## 2. Method

Four layers, read in full for this sweep (not sampled):
- **General, top**: the global carrier (`apex_contract`, 23 tags).
- **General, nested**: `specs/execution-modes/{task-specification,bake-off,patch-discipline,handover,iterative-execution}.md` (the `ref=` targets `<align>`/`<trade_off>`/`<editing>`/`<handover>`/`<iterative>` open) and `specs/governance-schemas.md` (`GS-01`-`GS-22`).
- **Repo, top**: `Leela-Cloud-2026/AGENTS.md` (all 230 lines — an earlier pass on the same repo stopped at line 150 and missed §7; this sweep reads to the end on principle, since that omission is itself evidence for §3's finding about attention position).
- **Repo, nested**: `agents/{index,data-plane,sequencing,gates,repo-layout}.md`.

## 3. Classification

- **A — already deterministic, built and wired.** A check exists, runs automatically, and a
  sabotage/self-test proves it fires.
- **B — declared, or feasible, but not built.** The rule's violation is observable in an artifact
  (a file, a diff, a table's shape, a path), so a check *could* exist, but none does yet, or one is
  declared as a requirement (`governance-schemas.md` frequently states "reject a record that
  omits X" as if authoritative) with no evidence any validator actually enforces it.
- **C — requires judgment, not worth forcing.** The violation is a live reasoning or scope decision
  (was this the *right* amount of reuse, was this redraft actually a misread) that a static check
  cannot evaluate without re-deriving the judgment itself. Hooks can still intercept the *action*
  (as the subject repo's `flutter test` bypass hook does) even when the *correctness* of the
  decision stays a C.

### 3.1 Global carrier (`apex_contract`) — general, applies beyond this repo

| Tag | Class | Finding |
|---|---|---|
| `schemas` (`patch_intent.v1`) | **A** | Already fully deterministic: a JSON Schema plus a validating patcher skill. The most mature example in the whole corpus — cite this as the target shape for everything else in this table. |
| `authoring` (imperative+trigger, flat YAML, bracket lists) | **A** (partial) | `okf_validator.py` already checks flat-YAML frontmatter and parse errors. It does not check that a rule's *body* is phrased as `WHEN/IF...THEN`, only that the file's frontmatter parses — the imperative-phrasing half of this rule is still **B**. |
| `current_truth` (no retired component names in live rules) | **B** | Trivially gateable: a denylist of retired identifiers, grepped against every governed rule file outside a changelog. Not built in this corpus or the subject repo. Cheap, high value — a one-file script. |
| `surgical` / `editing` (never regenerate a file in full; `git mv` not rewrite) | **B** | `governance-schemas.md GS-02` already declares this as P0 ("never generate or apply full-file rewrites"), but no validator in this corpus checks it. A diff-shape heuristic (percentage of a file's lines replaced in one change) is a workable proxy, not perfect, but better than nothing. |
| `trade_off` (bake-off 4-phase structure, decision-matrix fields) | **A, built, wired, and real-world tested 2026-11-03** | `GS-12`/`GS-13` state, in the imperative, "reject a bake-off that skips or reorders the four phases" and "reject a decision record that omits any mandatory field" — `okf_validator.py` had no check for either (confirmed by reading it in full before building). Closed by `tools/check_decision_bakeoff_shape.py`. **Synthetic fixtures alone passed on the first try and would have shipped a broken checker** — the operator rejected that as insufficient and asked for a real decision in the corpus instead. Run against `research/02-deep-reasoning/02-new-rules-discovery-and-qa-bakeoff.md` — this project's own real architectural decision record (file-ownership, ID renumbering, XML-vs-Markdown routing; real `Option A/B/C`, real `Grounding:`, real `(I/E/R)` tags) — the first pass found two real bugs the synthetic fixtures never would have: (1) the file's frontmatter tags it `bake-off` *and* `decision-matrix` loosely/colloquially, so the word-presence heuristic misclassified it as a bake-off and failed it against `GS-13`'s phase/column requirements it was never written to satisfy; (2) the heading reads "Decision **Matrices**" (plural) and the original regex only matched the singular, missing the real decision-matrix content entirely. Both are fixed: bake-off detection now requires structural evidence (a comparison table or a phase marker), not the word alone; decision-matrix detection also matches on structural evidence (an `Option X (...)` header near a `Grounding:` label), not just the literal phrase. Re-run after the fix: correctly classified as a decision matrix, zero findings — a true pass, not silence from misdetection. **Separately, real-world testing surfaced a finding more valuable than a bug**: `Leela-Cloud-2026/docs/ssot/decisions/DECISION-SHEET-06-path-seam-and-allocation-origin.md`, a real, already-resolved product decision in a downstream repo, uses a narrative "Version A/B/C" convention with no `Option` keyword and no `(I/E/R)` tags at all — the checker does not recognize it as a decision matrix, and should not be forced to; this is evidence that `GS-12`'s schema, while followed in this corpus's own meta-work, has not propagated into at least one downstream repo's actual decision-making practice. **Scoping decision (2026-11-03): GS-12/GS-13 stay apex-meta-only.** `okf_validator.py` is never invoked against any downstream repo's bundles today (confirmed: `Leela-Cloud-2026` only documents the tool's existence under its vendored `docs/apex/`, has no CI call site, and runs no validator against its own `docs/ssot/decisions/`) — so wiring the checker into `okf_validator.py`'s own bundle walk scopes it to this corpus by construction, no extra path-gate needed. The downstream propagation gap (`DECISION-SHEET-06` and whatever else in that repo predates `GS-12`) is a separate problem for that repo's own operator to decide whether to retrofit — not fixed here, not this checker's job. **Wired 2026-11-03**: `okf_validator.py`'s per-file loop now calls `check_decision_bakeoff_shape.looks_like_bakeoff`/`looks_like_decision_matrix` and folds its findings into the same `APEX_PROFILE_ERROR` severity class, so every `okf_validator.py --target` run gets GS-12/GS-13 coverage automatically — no separate invocation needed. Wiring it into the real `research/02-deep-reasoning` bundle (not a synthetic fixture) found a **third** real bug past the two above: the bare-phrase branch of `looks_like_decision_matrix` (`"decision matri"` anywhere in text) false-positived on two unrelated files in the same bundle — `REVIEW-REQUEST.md`, which only *names* the real decision file in a table cell, and `07-candidate-always-on-block.md`, which discusses a past "Option C" choice in retrospective prose — neither is a decision matrix being authored in that file. Fixed by requiring the phrase appear in a heading line (`^#{1,6}\s.*decision matri`), not anywhere in prose; the structural branches (`Option X` near `Grounding:`, `\| question \|`) are unchanged since they were already specific enough. Re-run after the fix: both false positives gone, the real fixture still clean, and the full bundle surfaced one genuine new finding — `06-how-the-routing-actually-works.md` has real `Option A/B/C` sections, `Grounding`, and a `Recommendation`, but no `(I/E/R)` tags, which is GS-12 doing its job on content never checked against it before. Not CI-wired (no CI pipeline exists in this repo to wire into) — "automatic" here means every `okf_validator.py` invocation, which is how this corpus's validation already runs. |
| `handover` (5-component report: Observation/Logic Chain/Caveats/Conclusion/Verification Method) | **B** | Same shape-check pattern as `trade_off`: are the five headers present, in order, each non-empty. Checks presence, not substance — still catches the common failure of a handover silently dropping "Verification Method." Not built. |
| `pointers` (`ref=` only when needed, never restate; `WP-23`) | **B** | A near-duplicate-content detector (N-gram overlap above a threshold between two governed files) would catch the exact failure class `AGENTS.md` itself names ("two copies drifted within six hours"). Not built in either repo. |
| `align` (six-field restatement before non-trivial work) | **B, weak** | Checkable only if the restatement is itself committed as an artifact (a plan file, a PR description) — most restatements happen in conversation and leave no artifact, so this degrades toward **C** in practice unless the carrier requires the restatement to be written to disk first. |
| `ground` (state the command behind a count/zero/percentage claim) | **B** | A lightweight linter: flag a sentence containing a bare number, "X files", "zero", or a percentage with no adjacent code-fenced command or citation within N lines. Same family as the sentence-length `ADVISORY_WARNING` already in `okf_validator.py` — same severity model, new rule. |
| `target`, `product_first`, `scope`, `reuse`, `context`, `recovery`, `stop_repairing`, `new_machinery`, `detour`, `method`, `sync`, `hold_position`, `communication` | **C** | Each is a live scope/judgment/reasoning-quality call. A hook can still intercept a specific *action* that violates one of these in a specific repo (as `scope` does for the subject repo below), but the general tag itself does not reduce to a file-shape check. Not worth building machinery here; this is where a hook earns its keep over a gate, if anything does. |

### 3.2 Subject repo, top (`AGENTS.md`) — repo-specific

| Rule | Class | Finding |
|---|---|---|
| §5 Gates (`--since`/`--full`, exposure, widen on catch) | **A** | Already built: `scripts/gates.py` itself implements exactly the documented selection logic. |
| `instruction_contract.verification_scope` (no direct `flutter test`/`analyze`) | **A** | Built this session: `scripts/check_gate_runner_bypass.py` + a Claude Code `PreToolUse` adapter. Proven live. Vendor-locked by construction (see `docs/audits/.../README.md` §5 in the subject repo for the hook-vs-wrapper trade-off already written up there). |
| §7 standing authorization ("commit and push a verified unit, do not ask") | **B — the real gap, and the one this sweep exists because of** | The rule is not ambiguous; it is correctly worded and pre-authorized. It sits at line 206 of a 230-line file — well past `governance-schemas.md`'s own `GS-03` "Top-Loaded Attention Primacy" horizon ("front-load critical P0 invariants... before attention density decays"). Two separate sessions on this repo (the executing agent on #206-#210, and this orchestrating session on its first pass) both failed to act on it, and the second failure was not a wording problem — it was never having read that far. **Class B**: a session-start or pre-commit check comparing "files touched since the last green gate run" against "files with no new commit" is buildable and would have caught this without anyone needing to re-read line 206. Not built yet. |
| `docs/ssot/_generated/` must never be hand-edited | **C — deliberately absent, not a gap** | Corrected after checking `scripts/gates.py`'s own history comment before building anything: a `generate_ssot_views --check` gate existed and was deliberately *removed* once `SSOT-D-052` untracked the status-view subtree (making the comparison vacuous) and `check_ssot_contracts` absorbed materialization-drift ownership (`RI-006`). `AGENTS.md`'s "no gate polices those trees" reads as an open gap on first pass, but it is an **accepted cost per two named decisions**, not an unbuilt check — rebuilding it would reverse `SSOT-D-052`/`SSOT-D-058` without operator authorization. Left as **C** precisely because the earlier draft of this table called it a clean **B** build before checking `gates.py`'s own removal rationale — the correction is itself evidence for this file's method: read the live artifact before classifying it, not the rule text alone. |
| `docs/apex/` must be edited at the master (`apexai-os-meta`), never locally | **A, but the checker is unwired** | `check_vendor_drift.py` exists and reports `in sync`/`SKIPPED` — but `agents/gates.md`'s own inventory table lists it as "nothing, and documented as nothing," the one checker whose silence is indistinguishable from success. This is a **third class worth naming**: a checker that exists but is not registered as a gate, distinct from "no checker exists" (the `_generated/` case above) and from "no checker was ever built" (most of §3.1's B rows). |
| Authority tiers, recency, "surface conflicts, don't pick a side" (§2) | **C** | Requires semantic understanding of which artifact actually settles a conflict. Not gateable. |

### 3.3 Subject repo, nested (`agents/*.md`) — repo-specific

| Rule | Class | Finding |
|---|---|---|
| `agents/index.md`'s own placement rule (`paths:` key required in Claude Code, listed in `ALLOWED_RULE_FILES`) | **A (Claude Code only)** | Already built and self-tested (`check_instruction_integrity.py`, sabotage scenario `I5`). Ignored by Codex CLI (uses hierarchical `AGENTS.md`) and Gemini CLI (uses hierarchical `GEMINI.md` + eager `@path`), so portable cross-agent modules cannot rely on `paths:` globs for routing. |
| `agents/data-plane.md`: "do not add a new storage engine, auth flow, sync layer, outbox, or multi-device behavior" | **B** | Partially gateable as a path/import allowlist: no new file under a storage-adjacent path, no new dependency matching a denylist (`sqflite`, `hive`, a second auth package), without an explicit SSOT-D exception citation in the same diff. Imperfect — a determined rewrite could still dodge it — but catches the lazy case. |
| `agents/sequencing.md`: "reuse Wave A typed IDs, do not recreate parallel domain objects" | **C, weak B** | A near-duplicate-class/type-name detector against the existing domain module is a weak proxy at best; true "is this a parallel object" requires semantic judgment. |
| `agents/gates.md`'s own meta-rule: re-measure tier timings when a gate changes; correct a stale guarantee comment in the same commit | **C** | Needs semantic linkage between a code change and a specific comment's claim; not mechanically checkable without that link being named structurally (e.g., a comment ID a gate could grep for — not present today). |

## 4. What to build next, ranked by cost ÷ value

1. ~~`GS-12`/`GS-13` structural checks~~ — **built, broken, fixed, and wired into `okf_validator.py`, 2026-11-03**: `tools/check_decision_bakeoff_shape.py`. Self-test alone (synthetic fixtures) passed and was not sufficient evidence — validated against a real decision record in this corpus, a real one in a downstream repo, and then the full bundle it was wired into, which together found and fixed three real detection bugs (two before wiring, one surfaced only by wiring it into a whole bundle instead of one fixture). GS-12/GS-13 scoped to this corpus deliberately — the downstream propagation gap (`DECISION-SHEET-06`) is that repo's own problem to raise. See §3.1's corrected row for the full account.
2. ~~Wire `check_vendor_drift.py` into `scripts/gates.py`~~ — **built 2026-11-03**, operator-authorized after this file flagged the CI-silent-skip caveat. Added as a fast-tier gate (`exposure: ("docs/apex/",)`); full canary (`--full`, triggered because the change touched `gates.py` itself) ran 16/16 GREEN. The caveat stands and is documented inline in `gates.py`: exit 0 covers both "in sync" and "meta repo absent," so GREEN there means "nothing to compare" in a clone without `apexai-os-meta`, not "verified in sync" — state that distinction whenever this gate's evidence is reported.
3. ~~A "gate-green-but-uncommitted" nudge~~ — **built 2026-11-03**: `.claude/hooks/stop-uncommitted-nudge.py`, a Claude Code `Stop` hook, advisory only (prints AGENTS.md §7's own text back; does not auto-commit, since "is this actually verified" stays a judgment call). Claude-only for now, same vendor-lock caveat as the `verification_scope` hook.
4. **Still open — Cross-agent harness limits & upfront vs. post-hoc gating (2026-11-11 finding)**: `.claude/rules/*.md` `paths:` globs and `PreToolUse`/`Stop` hooks protect only Claude Code runs (`§1`, `§3.3`). Codex CLI (`AGENTS.md` hierarchy) and Gemini CLI (`GEMINI.md` + `@path`) lack `paths:` lazy-glob activation and our repo has no verified cross-harness hook parity for them. Moreover, post-hoc linters, `Stop` hooks, and validators only inspect artifacts *after* an agent writes them; they do not steer reasoning from token 1. Cross-agent upstream alignment belongs in a **two-phase pre-action planning gate** in Layer 1 (`<align>` + `<pointers>`): list every matched `when=`/`ref=` target in the pre-action plan and open it *before* editing or finalizing output, while skipping refs on trivial `Route 0` typos/lookups. That mechanism is portable prose planning rather than a deterministic runtime guarantee; it requires Stage 2 / `EVAL-APEX-JIT-GATE-V3` read-trace proof across harnesses.
4. ~~The `_generated/` hand-edit gate~~ — **removed from this list.** It looked like row 1's twin
   (repo names the gap, looks bounded) until `scripts/gates.py`'s own removal comment was checked:
   the gate existed and was deliberately retired per `SSOT-D-052`/`SSOT-D-058`. Rebuilding it would
   reverse an accepted decision without authorization. Kept here, struck through, as the record of
   almost building the wrong thing — see §3.2's corrected row.
5. Everything marked **C** in §3.1-§3.3 — explicitly not recommended. Building a brittle proxy check
   for a judgment call produces false confidence worse than no check at all; a hook that intercepts
   the specific *action* (as done for `verification_scope`) is the better lever where one applies.
6. ~~Fix the 4 `WP-23` violations `check_governed_markdown_duplicates.py` found~~ — **done
   2026-11-03, but the tool's suggested direction was backwards and had to be corrected before
   acting on it.** The detector was first run with `--owner specs/execution-modes.md
   specs/execution-modes/patch-discipline.md`, which reported "retain the block in
   execution-modes.md." Checking `git log` before editing anything (the discipline this whole
   project keeps re-learning) showed the opposite: `specs/execution-modes/{bake-off,patch-
   discipline,handover,iterative-execution}.md` were created 2026-10-26 specifically "to execute
   the `DEC-16` adapter split," *after* `execution-modes.md`'s last full-content commit
   (2026-10-23) — they are the newer, canonical split files; `execution-modes.md` is the pre-split
   monolith that was never trimmed down to a router. Re-running with the corrected direction found
   **15 duplicate blocks across 4 adapters, not 4 across 1** — the original scope undersold the
   real extent of the incomplete split. Fixed: all four `execution-modes.md` adapter sections now
   point to their canonical file instead of restating it, keeping the heading/anchor intact so the
   file's own `<execution_dispatch>` `IF`-routing still resolves. One self-inflicted bug caught
   immediately after: the pointer wording for Adapter 2 contained the literal phrase "comparison
   matrix," which tripped this project's own `GS-13` checker into flagging `execution-modes.md` as
   an incomplete bake-off record; reworded, reverified clean. Four trigger-line duplicates remain
   by design — the one-sentence `EM-0X [P... ] Conditional ... Trigger` line is the inline summary
   this corpus's own `<pointers>` pattern calls for at the dispatch point; removing it would break
   the documented just-in-time design, not fix a drift risk. **This is the fifth time in this
   project that a plausible first answer was wrong until checked against a live artifact** — see
   §3 "the meta-lesson" in `operations/16`.

## 5. Sources

- `specs/governance-schemas.md` (this corpus) — `GS-01` through `GS-22`, read in full for this sweep.
- `specs/execution-modes/{task-specification,bake-off,patch-discipline,handover,iterative-execution}.md` (this corpus) — read in full.
- `tools/okf_validator.py` (this corpus) — read for actual (not declared) coverage.
- `Leela-Cloud-2026/AGENTS.md` — read in full, including §7 (missed on an earlier pass on the same repo — see `docs/audits/2026-11-03-agent-adherence-inter-feature-runtime-reliability/README.md`).
- `Leela-Cloud-2026/agents/{index,data-plane,sequencing,gates,repo-layout}.md` — read in full.
- `Leela-Cloud-2026/scripts/check_instruction_integrity.py`, `scripts/gates.py` — read for actual coverage.
- **External harness docs (verified 2026-11-11):** Anthropic Claude Code memory & `.claude/rules/` `paths:` frontmatter docs; OpenAI Codex CLI hierarchical `AGENTS.md` / `AGENTS.override.md` discovery docs; Google Gemini CLI `GEMINI.md` & `@path/to/file.md` import docs; Plan-and-Execute two-phase decomposition literature (Anthropic *Effective Context Engineering for AI Agents*; Gloaguen et al. 2026, *Evaluating AGENTS.md*).
