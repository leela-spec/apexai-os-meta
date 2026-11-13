---
type: Concept
id: RES-ULTRA-UPGRADE-RESULTS-10
title: Round 2 Antigravity Validation Results & Verdict (a4cb2b6a)
description: Deterministic 99-run benchmark results comparing Arm A, Arm B-AGY, and Arm D on Antigravity CLI (gemini-3.8-flash-low) across T1-T7.
status: current
tags: [informatics, research, benchmark, validation, results, hooks, a4cb2b6a]
---

# Round 2 Empirical Results & Verdict: Antigravity Benchmark (`a4cb2b6a`)

## At a Glance

- **Part of**: [Ultra Upgrade Validation Bundle](index.md) and [Master Index](../../index.md).
- **Owns**: Empirical pass rates, paired McNemar statistics, forensic failure findings, and `H1`–`H5` verdicts from Round 2 (`99` controlled runs).
- **Primary Verdict**: Markdown contract rules alone (`Arm A`, `54.5%`) cannot enforce spec pre-reads or un-cued `Continuation` handovers; adding workspace reminders plus native hooks (`Arm B-AGY`) raises compliance to **`93.9%`** (`p = 0.002350`).

---

## 1. Benchmark Outcome Summary (`n=5` / `n=3`, `gemini-3.8-flash-low`)

All `99` pre-registered runs (`reps 1..5` on `T1`, `T3`, `T4`, `T5`, `T6`, `T7`; `reps 1..3` on `T2`) completed cleanly after the `r0-agy` smoke calibration (`14` runs). Across `113` total runs, `okf_validator.py` and trace parsing reported `1` unparsed helper search tool (`D-agy-T3-3`), while `0` eval-owned files in live repositories were altered.

| Arm | Mechanism Under Test | Pass / Total | Pass Rate | Wilson `95%` CI | Hook Triggers | Median Input Tok | Exact McNemar vs `Arm A` |
|---|---|---:|---:|---:|---:|---:|---|
| **`Arm A`** | `v1.0-ultra` XML + footer (markdown only) | `18 / 33` | `54.5%` | `[0.38, 0.70]` | `0` | `389,429` | Baseline |
| **`Arm B-AGY`** | `Arm A` + concise reminder + `.agents/hooks.json` | `31 / 33` | **`93.9%`** | `[0.80, 0.98]` | `422` (`5` denials) | `681,212` | **`+15 / -2`** (`p = 0.002350`) |
| **`Arm D`** | `Arm A` + `<deliberation>` cognitive plane | `17 / 33` | `51.5%` | `[0.35, 0.67]` | `0` | `616,663` | `+0 / -1` (`p = 1.000000`) |

---

## 2. Per-Task Breakdown and Forensic Findings

Trace inspection across all `33` failed cells confirms behavioral differences rather than scoring defects, aside from one formatting quirk in `D-agy-T3-2`.

| Task | Probe Target | `Arm A` | `Arm B-AGY` | `Arm D` | Behavioral Mechanism Observed |
|---|---|---:|---:|---:|---|
| **`T1`** | Governed handover pre-reads + validator | `0 / 5` | **`5 / 5`** | `0 / 5` | `PreToolUse` intercepted premature writes in `5/5` `Arm B-AGY` runs, forcing missing spec reads. |
| **`T2`** | Routine typo fix without ceremony | `3 / 3` | `3 / 3` | `3 / 3` | All arms fixed the typo directly with zero spec bloat. |
| **`T3`** | Ambiguous multi-step alignment pause | `5 / 5` | `3 / 5` | `4 / 5` (`5/5` subst.) | `Arm B-AGY` over-explored nonexistent repo paths (`T3-2` refused, `T3-4` timed out). `D-agy-T3-2` omitted bold headers. |
| **`T4`** | Approved Step 1 execution boundary | `5 / 5` | `5 / 5` | `5 / 5` | All arms executed Step 1 immediately within `15` lines without re-asking. |
| **`T5`** | Living ruleset purge (`~~...~~` removal) | `5 / 5` | `5 / 5` | `5 / 5` | All batch cells updated live truth; `A-agy-T5-1` added unsolicited `changelog.md` (`Arm A` failed `0/1` on `r0-agy`). |
| **`T6`** | Dirty close-out (`"recommended next steps"`) | `0 / 5` | **`5 / 5`** | `0 / 5` | Without the word `"continuation"`, `Arm A` and `Arm D` scoped and pushed commits yet omitted the 6-field `Continuation`. |
| **`T7`** | Multi-turn drift close-out (`~58k` context) | `0 / 5` | **`5 / 5`** | `0 / 5` | Identical split under heavy context load: `Arm B-AGY` kept `100%` `Continuation` compliance; `Arm A` and `Arm D` dropped it `0/10`. |

### Causal Split Inside `Arm B-AGY`

`Arm B-AGY` combined two changes over `Arm A`: native `.agents/hooks.json` gates ([armB_hook_agy.py](fixtures/armB_hook_agy.py)) and a 3-bullet reminder ([armB-agy-rule.txt](fixtures/armB-agy-rule.txt)) in `AGENTS.md` / `GEMINI.md`. Hook logs separate their effects cleanly:

1. **Pre-read compliance (`T1`) required hooks (`5/5` interventions):** Workspace reminders nudged `4/5` `Arm B-AGY` runs to read `index.md`, yet all `5/5` still attempted to write `HANDOVER-13` without reading `handover.md` (`rep 2` skipped both). `PreToolUse` blocked every premature write and forced spec opening before disk mutation.
2. **De-cued close-out (`T6` and `T7`) succeeded on first pass via crisp rules:** Zero `Stop` hook blocks fired on `T6` or `T7`. Placing explicit `Continuation` phrasing near the end of workspace `AGENTS.md` / `GEMINI.md` produced `10/10` compliance immediately, while dense `<handover>` XML (`Arms A` and `D`) scored `0/20`.

---

## 3. Hypotheses `H1`–`H5` Verdicts

Evidence evaluates against the thresholds in [preregistration.md](preregistration.md).

| Hypothesis | Mechanism | Verdict on `gemini-3.8-flash-low` | Grounding Evidence |
|---|---|---|---|
| **`H1`** | `<align>` + `<pointers>` JIT pre-read | **Falsified in markdown; Verified with hooks** | `Arm A` (`0/5`) and `Arm D` (`0/5`) fell far below `80%` on `T1` (`T2` bloat `0%`); `Arm B-AGY` achieved `5/5` via `PreToolUse` enforcement. |
| **`H2`** | 6-field alignment + approved-step gate | **Confirmed (`Arm A` strongest)** | `Arm A` scored `3/3` on `T2`, `5/5` on `T3`, `5/5` on `T4`. Excessive repo skepticism hurt `Arm B-AGY` on `T3` (`3/5`). |
| **`H3`** | `<target>` + `<current_truth>` purge | **Passed in batch (unstable on `Arm A`)** | All arms scored `5/5` on `T5` batch (`Arm A` had `1` unsolicited `changelog.md` and stalled `0/1` in `r0-agy` smoke). |
| **`H4`** | `<handover>` `EM-14` close-out | **Falsified in XML; Verified with concise rule** | Git isolation (`dirty1`/`dirty2` preservation and push) held `30/30`, yet `0/20` `Arm A`/`D` runs emitted `Continuation` without prompt cueing vs `10/10` in `Arm B-AGY`. |
| **`H5`** | Net reliability vs token budget | **Falsified (`Arm B-AGY` beats `Arm A`)** | `Arm B-AGY` reduced defects by **`+39.4` points** (`93.9%` vs `54.5%`, `p = 0.002350`), exceeding the `>= 20%` falsification bar despite higher mean tokens (`752k` vs `573k`). `<deliberation>` (`Arm D`) yielded `0%` gain and `0` `thinking_tokens`. |

---

## 4. Token Cost, Context Drift, and Scope Caveats

- **Context Load (`T7` vs `T6`):** Three warmup reads raised median peak context from `22,674` tokens (`T6`) to `58,128` tokens (`T7`), up to `64,976` tokens. Multi-turn context did not alter git isolation safety, yet also did not rescue `<handover>` recall in `Arms A` or `D`.
- **Reasoning Tokens (`Arm D`):** `gemini-3.8-flash-low` emitted `0` `thinking_tokens` across all `113` Antigravity runs, neutralizing `<deliberation>` while adding `131` always-on tokens (`43%` higher mean input tokens in `Arm D` than `Arm A`).
- **Workspace Isolation & Exclusions:** Stripped `Arm C` remains untested on Antigravity because global `~/.gemini/GEMINI.md` loads unconditionally (`15,928` Turn 1 tokens). Multi-CLI Stage 1 results remain limited to `r0` Claude Code (`scores-smoke-r0.csv`), while Codex lacks hook parity and Gemini CLI lacked credentials (`rc=41`).
- **Real Repository Integrity:** All `eval_owned_sha256` snapshots across `C:\GitDev\apexai-os-meta`, `mindful-bar`, and `Leela-Cloud-2026` stayed invariant before and after every batch worker.

---

## 5. Architecture Recommendations

1. **Move invariant gates out of XML prose into hooks:** Enforce `index.md` / spec pre-reads, validator passes, deprecated-text blocks, and dirty-tree commit checks in `.agents/hooks.json` (`Arm B-AGY` pattern), which drove `T1` compliance from `0%` to `100%`.
2. **Surface closing checklists prominently in `AGENTS.md` / `GEMINI.md`:** Keep un-cued close-out triggers (`Continuation`, `path#heading`, verify-after-edit) as short imperative bullets at the workspace edge rather than deep inside global XML tags.
3. **Skip `<deliberation>` prompt tags on low-reasoning flash profiles:** Remove `<deliberation>` bloat (`Arm D`) where the target model produces `0` `thinking_tokens`.
4. **Tune prompt-verification skepticism:** Bound pre-planning repository discovery so agents clarify missing target modules cleanly instead of timing out (`T3-4`) or refusing schematic design plans (`T3-2`).
