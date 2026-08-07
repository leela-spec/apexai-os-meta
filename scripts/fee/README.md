# FEE — Flow Execution Engine

An execution substrate for **step 4** of the Weekly Orchestrator loop. **Not an orchestration system** (D-M0) — APEX OS has exactly two, and FEE is a substrate for one stage of one of them.

Live authority for the seam it fills, `.claude/skills/weekly-orchestrator/SKILL.md:32`:

```yaml
operator_execution: {agent: none_operator_human_step, gate: G3, trigger: "operator returns evidence or skip signal"}
```

FEE replaces the **actor** at that step. It never touches G3.

## Status

`authority.state: candidate` · Phase 1 + Phase 3 implemented and tested · **no live provider contact has ever occurred**.

## Install

None. Stdlib only, Python 3.10+ (D-I2). No PyYAML, no Node, no Playwright, no local model, no Docker.

## Commands

```bash
python -m scripts.fee plan    --day 20260713 --flow F1     # compile + freeze. No network.
python -m scripts.fee status  --day 20260713               # loop position for the day
python -m scripts.fee next    --day 20260713 --flow F1     # next step; body -> clipboard
python -m scripts.fee capture --day 20260713 --flow F1     # file the reply from the clipboard
python -m scripts.fee emit    --day 20260713 --flow F1     # emit step 5's input
```

`next`/`capture` accept `--lane auto_lane|operator_lane`. `capture` accepts `--file X`, `--stdin`, or `--skip REASON`. `next` accepts `--print-body` when you would rather not use the clipboard.

Exit codes: `0` clean · `2` needs operator · `3` plan invalid · `4` hash mismatch.

### The two-command loop

```bash
python -m scripts.fee next    --day 20260801 --flow F2 --lane operator_lane
#   paste into the provider, copy the reply
python -m scripts.fee capture --day 20260801 --flow F2 --lane operator_lane
```

Position comes from the ledger's `turn_captured` events, so `next` and resume can never disagree.

## Lanes

Only Claude has a vendor-sanctioned automation channel, so only the Claude lane can run unattended. Everything else is an **assisted** worklist — FEE prepares and files it; the operator executes it. No detection avoidance is implemented, and none will be.

| Lane | Contents | Runs |
|---|---|---|
| `auto_lane` | `provider_target: Claude` on an automatable surface class | unattended (Phase 5) |
| `operator_lane` | ChatGPT · Gemini · `deep_research_surface` · agent/code surfaces | operator present |

`provider_unspecified`, `OpenRouter_later`, and `supplemental_api_low_cost` **halt** rather than defaulting.

## Modules

| File | Module | Role |
|---|---|---|
| `artifacts.py` | M1 (input) | strict-subset reader for markdown + fenced YAML + pipe tables |
| `compile.py` | **M1** | resolve refs, freeze the plan, hash it, partition lanes |
| `ledger.py` | **M6** | append-only JSONL; closed event enum; hashes and paths only |
| `capture.py` | M4 (assisted) | the two-command clipboard loop |
| `emit.py` | **M8** | `skipped_flow_marker` today; evidence bundle in Phase 2 |
| `paths.py` | — | write-surface resolution; refuses refs that escape the repo root |

Not built, by decision: **M5** (local adjudicator — deferred; `stop_reason`/heuristics cover it), **M7** (executor bridge — nothing to depend on yet), **M2/M3** (Phase 5).

## Two properties worth knowing

**The plan is frozen before anything runs.** Every prompt body, provider, order, and follow-up is resolved at compile time and hashed. `declared_follow_ups` is a closed list. Nothing captured later can add a step — there is no field for it to land in. Tamper with the frozen plan and every downstream command exits 4.

**Captured content is data forever.** It is written verbatim, hashed, and never parsed for instructions, paths, commands, providers, or next steps. `tests/test_fee.py::TestInjectionContainment` is a permanent fixture, not a one-time check.

## Tests

```bash
python -m unittest discover -s scripts/fee/tests -t . -v
```

32 tests, stdlib `unittest` (pytest is not installed in this environment). Mapping to the verification plan in `apex-meta/local-orchestration-engine/architecture/03-micro-implementation-map.md` §6:

| Test | Asserts | Status |
|---|---|---|
| V1 | identical inputs reproduce an identical `plan_hash`; M1 imports no network module | pass |
| V2 | injected step, edited body, swapped provider, tampered lane, added follow-up all detected; `compiled_at` excluded by design | pass |
| V3 | a hostile capture is stored verbatim and changes nothing — no new step, no lane change, no authority advance, no write outside the artifact family, no body in the ledger | pass |
| V4 | a captured turn is never re-offered; position advances | pass |
| V5 | degraded pack → `plan_confidence: low` + `requires_pre_run_review` | pass |
| V6 | `provider_unspecified` halts with exit 3 and commits no plan | pass |
| V11 | Claude → `auto_lane`; ChatGPT/Gemini → `operator_lane`; deep research never auto | pass |
| V7 | downstream acceptance by `apex-evidence-normalize` | **Phase 2, not run** |
| V8 · V9 · V10 | failure-class policy · live single flow · nightly harness | **not run** |

V6 and the live-artifact reader guard run against **real repo artifacts**, not fixtures.

## Known blocker

`flow_prompt_pack` carries only `final_copy_paste_prompt_ref`; **no prompt body exists on disk anywhere**, and `artifacts/.../prompt-packs/` has never been written. Executable flows therefore halt with an `unresolved_ref` report naming the expected path. The skip path, the validator paths, and the capture loop all work today regardless.

Closing it needs gate-batch item 1 — see `apex-meta/local-orchestration-engine/architecture/06-gate-batch-draft.md`.
