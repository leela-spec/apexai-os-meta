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
- **The subject repo's `scripts/check_instruction_integrity.py`** independently reinvents the same
  idea for a different rule family: it enforces that every `agents/*.md`-style rule file declares a
  `paths:` key (so it loads on match, not on every turn), checks citation resolution, rule
  placement, and rule-destination consistency. It is wired into `scripts/gates.py` and its own
  sabotage self-test (`sabotage_audit.py`, scenario `I5`) proves the enforcement actually fires, not
  just that the check exists.

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
| `trade_off` (bake-off 4-phase structure, decision-matrix fields) | **A, built 2026-11-03** | `GS-12`/`GS-13` state, in the imperative, "reject a bake-off that skips or reorders the four phases" and "reject a decision record that omits any mandatory field" — `okf_validator.py` had no check for either (confirmed by reading it in full before building). Closed by `tools/check_decision_bakeoff_shape.py`: a standalone structural checker, self-tested against 4 synthetic fixtures (good/bad bake-off, good/bad decision matrix), all passing. Scope caveat, found while sanity-running it against this corpus's own real files: it is meant for authored bake-off/decision *records*, not the spec files that define the rubric — running it against `bake-off.md`/`governance-schemas.md` themselves produces expected false positives, since those files discuss the shape without being an instance of it. Not yet wired into `okf_validator.py` or any CI — kept standalone deliberately, to avoid editing a production validator without having traced every one of its call sites in one sitting. |
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
| `agents/index.md`'s own placement rule (`paths:` key required, listed in `ALLOWED_RULE_FILES`) | **A** | Already built and self-tested (`check_instruction_integrity.py`, sabotage scenario `I5`). |
| `agents/data-plane.md`: "do not add a new storage engine, auth flow, sync layer, outbox, or multi-device behavior" | **B** | Partially gateable as a path/import allowlist: no new file under a storage-adjacent path, no new dependency matching a denylist (`sqflite`, `hive`, a second auth package), without an explicit SSOT-D exception citation in the same diff. Imperfect — a determined rewrite could still dodge it — but catches the lazy case. |
| `agents/sequencing.md`: "reuse Wave A typed IDs, do not recreate parallel domain objects" | **C, weak B** | A near-duplicate-class/type-name detector against the existing domain module is a weak proxy at best; true "is this a parallel object" requires semantic judgment. |
| `agents/gates.md`'s own meta-rule: re-measure tier timings when a gate changes; correct a stale guarantee comment in the same commit | **C** | Needs semantic linkage between a code change and a specific comment's claim; not mechanically checkable without that link being named structurally (e.g., a comment ID a gate could grep for — not present today). |

## 4. What to build next, ranked by cost ÷ value

1. ~~`GS-12`/`GS-13` structural checks~~ — **built 2026-11-03**: `tools/check_decision_bakeoff_shape.py`, standalone, self-tested. See §3.1's corrected row.
2. ~~Wire `check_vendor_drift.py` into `scripts/gates.py`~~ — **built 2026-11-03**, operator-authorized after this file flagged the CI-silent-skip caveat. Added as a fast-tier gate (`exposure: ("docs/apex/",)`); full canary (`--full`, triggered because the change touched `gates.py` itself) ran 16/16 GREEN. The caveat stands and is documented inline in `gates.py`: exit 0 covers both "in sync" and "meta repo absent," so GREEN there means "nothing to compare" in a clone without `apexai-os-meta`, not "verified in sync" — state that distinction whenever this gate's evidence is reported.
3. ~~A "gate-green-but-uncommitted" nudge~~ — **built 2026-11-03**: `.claude/hooks/stop-uncommitted-nudge.py`, a Claude Code `Stop` hook, advisory only (prints AGENTS.md §7's own text back; does not auto-commit, since "is this actually verified" stays a judgment call). Claude-only for now, same vendor-lock caveat as the `verification_scope` hook.
4. **Still open**: the same nudge pattern for Gemini CLI / Codex CLI equivalents of `Stop` (unconfirmed whether either has one — not found in this sweep's research, flagged rather than guessed).
4. ~~The `_generated/` hand-edit gate~~ — **removed from this list.** It looked like row 1's twin
   (repo names the gap, looks bounded) until `scripts/gates.py`'s own removal comment was checked:
   the gate existed and was deliberately retired per `SSOT-D-052`/`SSOT-D-058`. Rebuilding it would
   reverse an accepted decision without authorization. Kept here, struck through, as the record of
   almost building the wrong thing — see §3.2's corrected row.
5. Everything marked **C** in §3.1-§3.3 — explicitly not recommended. Building a brittle proxy check
   for a judgment call produces false confidence worse than no check at all; a hook that intercepts
   the specific *action* (as done for `verification_scope`) is the better lever where one applies.

## 5. Sources

- `specs/governance-schemas.md` (this corpus) — `GS-01` through `GS-22`, read in full for this sweep.
- `specs/execution-modes/{task-specification,bake-off,patch-discipline,handover,iterative-execution}.md` (this corpus) — read in full.
- `tools/okf_validator.py` (this corpus) — read for actual (not declared) coverage.
- `Leela-Cloud-2026/AGENTS.md` — read in full, including §7 (missed on an earlier pass on the same repo — see `docs/audits/2026-11-03-agent-adherence-inter-feature-runtime-reliability/README.md`).
- `Leela-Cloud-2026/agents/{index,data-plane,sequencing,gates,repo-layout}.md` — read in full.
- `Leela-Cloud-2026/scripts/check_instruction_integrity.py`, `scripts/gates.py` — read for actual coverage.
