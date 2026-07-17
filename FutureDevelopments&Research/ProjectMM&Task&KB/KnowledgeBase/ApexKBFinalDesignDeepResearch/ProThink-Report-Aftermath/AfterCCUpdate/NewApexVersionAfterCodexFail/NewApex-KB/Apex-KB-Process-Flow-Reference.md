# Apex KB Control-Plane — Micro-Step Process Flow Reference

Grounded directly in `apex-meta/scripts/apex_kb_control.py` (function names and line numbers as of
commit `f3d6ec4d`). Every "What message" cell is the literal string the code actually emits, not a
paraphrase. Route shown is `terminal_backed` (Codex CLI); the `connector_only` variant is noted
where it diverges (semantic stages 8/9, 11/12, 14/15).

**Legend for "Who":** Operator = you. Orchestrator AI = the AI running the CLI (Codex). Semantic
Executor = the AI that drafts Phase 1/2 content (browser GPT or the orchestrator itself).
Independent Evaluator = a *separate*, clean-context AI session for acceptance. Script = pure
deterministic code, no AI judgment at all.

---

## Step 0a — Intake Q&A

| Field | Detail |
|---|---|
| How | Prose conversation in chat — **not a script.** There is no hardcoded welcome-message string anywhere in the codebase (verified: zero grep hits). |
| Who | Orchestrator AI asks; Operator answers. |
| Where | Chat only. Instructed by `SKILL.md:222-262` ("Step 0 — Intake and intent lock"), sub-step 0a. |
| What value | Operator's free-text answers: intent, KB identity, source locus, success definition, topics. |
| What message | No fixed script output — the Orchestrator AI composes the questions itself, per `SKILL.md` prose. **This is the step an AI can silently skip.** |
| Feeds into | Step 1 (`control init` flags). |

## Step 0b — Topic registry authored

| Field | Detail |
|---|---|
| How | File write (by LLM or operator), not a CLI command. |
| Who | Orchestrator AI or Operator. |
| Where | `manifests/topic-registry.json` inside the KB root. |
| What value | Topic slugs, names, `phrases`/`aliases`/`supporting_terms`, target queries. |
| What message | None — just a file on disk. `control init` reads it via `_topic_states()`. |
| Feeds into | Step 1 (`control init` requires this file to exist for any tier beyond `source_only`; `apex_kb_control.py:546-547`). |

---

## Step 1 — `control init`

| Field | Detail |
|---|---|
| How | CLI command. |
| Who | Orchestrator AI runs it; values come from Step 0a's answers. |
| Where | `apex_kb_control.py:1780` `control_init()`. |
| Exact command | `python apex-meta/scripts/apex_kb.py --kb-root <path> --allow-write --json control init --run-id <id> --mode compile --operator-intent "<...>" --kb-identity "<...>" --source-locus "<...>" --success-definition "<...>" --output-tier <tier> --output-tier-rationale "<...>" --execution-route terminal_backed --topic-slug <slug> --target-repository "<repo>"` |
| What value | Every Step 0a answer, as named flags — no free JSON blob. |
| What message | Writes `manifests/run-intent.md` (schema: `run-intent.schema.json`) + `manifests/run-state.json` (schema: `run-state.schema.json`). Returns `stage-result` with `operator_action`: *"python apex-meta/scripts/apex_kb.py --kb-root <path> --json control next"* (`apex_kb_control.py:1831`). |
| Feeds into | Step 2 (`scaffold`, the first stage in `GLOBAL_STAGE_ORDER`). |

## Step 2 — `control run` → `scaffold`

| Field | Detail |
|---|---|
| How | CLI command, deterministic — no AI judgment. |
| Who | Orchestrator AI issues the command; a **Script** does the work. |
| Where | `apex_kb_control.py:1665-1670`, delegates to existing `cmd_scaffold` in `apex_kb.py`. |
| Exact command | `python apex-meta/scripts/apex_kb.py --kb-root <path> --allow-write --json control run` |
| What value | Nothing new — uses `run-state.json`'s recorded config. |
| What message | Creates the KB skeleton (`raw/`, `manifests/`, `ingest-analysis/`, `wiki/`, etc.). Marks stage `scaffold` complete. |
| Feeds into | Step 3 (`intent_lock`). |

## Step 3 — `control run` → `intent_lock` (the readback)

| Field | Detail |
|---|---|
| How | CLI command; the readback text itself is Script-rendered from the stored intent, not freshly composed by the AI. |
| Who | Orchestrator AI issues the command. |
| Where | `apex_kb_control.py:2009-2024` → `prepare_intent_readback()` at `apex_kb_control.py:1855`. |
| Exact command | Same `control run` call as Step 2 (the stage machine advances automatically). |
| What value | The stored `run-intent.md` fields + a topic-sanity-check verdict per topic (`_run_topic_sanity()`, line 1837). |
| What message | Writes `log/runs/<run-id>/operator-readback.md`. Status `needs_operator`; `operator_action`: *"control confirm --confirmation-quote '\<operator affirmative\>'"* (`apex_kb_control.py:2019`). |
| Feeds into | Step 4. **This is the fixed pause point** — nothing after it runs until the operator explicitly answers. |

## Step 4 — `control confirm`

| Field | Detail |
|---|---|
| How | CLI command carrying the operator's own words. |
| Who | Operator supplies the quote; Orchestrator AI types the command. |
| Where | `apex_kb_control.py:1877` `control_confirm()`. |
| Exact command | `python apex-meta/scripts/apex_kb.py --kb-root <path> --allow-write --json control confirm --confirmation-quote "<verbatim operator yes>"` |
| What value | The operator's literal affirmative sentence — never inferred, never defaulted. |
| What message | Writes the quote + timestamp into both `run-intent.md` and `run-state.json`. Marks `intent_lock` complete. `operator_action`: *"control run"* (line 1932). |
| Feeds into | Step 5 (`preflight`) — and every stage from here on is now gated: `guard_direct_command` (`apex_kb_control.py:2321`) blocks direct legacy commands from this point forward because `manifests/run-state.json` now exists. |

## Step 5 — `control run` → `preflight`

| Field | Detail |
|---|---|
| How | CLI command, deterministic. |
| Who | Orchestrator AI issues it; Script executes. |
| Where | `apex_kb_control.py:1671-1676`, delegates to existing `cmd_preflight`. |
| What value | KB root path, existing manifests. |
| What message | Structural checks only (kb-schema exists, source-manifest exists, etc.). Blocks with `preflight_failed` + the raw check dict if anything's missing. |
| Feeds into | Step 6. |

## Step 6 — `control run` → `source_intake`

| Field | Detail |
|---|---|
| How | CLI command, deterministic. |
| Who | Script. |
| Where | `apex_kb_control.py:1677-1719`. |
| What value | `source_roots` / `source_inputs` recorded in the intent at Step 1. |
| What message | Calls existing `cmd_source_intake` per source, then `cmd_generate_source_payload_manifest`. Records fingerprints on `source-manifest.json`/`source-payload-manifest.json` against the `phase0` stage — if either file changes later, `phase0` gets invalidated automatically. |
| Feeds into | Step 7. |

## Step 7 — `control run` → `phase0`

| Field | Detail |
|---|---|
| How | CLI command, deterministic. |
| Who | Script. |
| Where | `apex_kb_control.py:1720-1736`, delegates to existing `cmd_phase0`. |
| What value | Topic registry + source manifest. |
| What message | Produces `topic-source-rankings.json` + one work-pack per topic. Blocks with `phase0_output_missing` if any topic's work pack didn't materialize. Fingerprints the rankings/work-packs against `phase1:<slug>`. |
| Feeds into | Step 8, once per topic. |

---

## Step 8 — `control run` → `phase1:<topic>` (packet emission)

| Field | Detail |
|---|---|
| How | CLI command — but the *output* is a packet, not a completed action. This is where the flow hands off to an LLM. |
| Who | Orchestrator AI issues the command; a **Script** renders the packet (no drafting happens here). |
| Where | `apex_kb_control.py:2025-2049` → `build_packet()` (line 1322) → `_phase1_packet()` (~line 1132). |
| What value | The topic's work pack, the registry entry, `semantic-contract/phase1-analysis-template.md`. |
| What message | Writes `log/runs/<run-id>/packets/phase1-<topic>.json` **and** `.md`. Status `needs_semantic_executor`. `operator_action` / `short_trigger`: *"Execute the Apex KB packet at log/runs/\<run-id\>/packets/phase1-\<topic\>.md; write only the declared outputs; return the completion response exactly."* (`apex_kb_control.py:1188`) |
| Feeds into | Step 9. This exact one-line trigger is what the Operator relays — never the packet's full contents. |

## Step 9 — Semantic Executor drafts Phase 1

| Field | Detail |
|---|---|
| How | The Operator pastes Step 8's one-line trigger into the Semantic Executor's chat (or, on `connector_only`, the executor fetches the `.md` packet itself via its git connector). |
| Who | **Semantic Executor** (browser GPT, or the same Orchestrator AI acting in that role). |
| Where | Outside the CLI entirely — a chat session with repo file read/write. |
| What value | Everything the packet names: work pack, template, registry entry. |
| What message | Writes `ingest-analysis/<topic>.analysis.md` + `log/semantic-runs/<run-id>/topics/<topic>.json` — **the exact paths the packet named, nothing else** (enforced next step). |
| Feeds into | Step 10. |

## Step 10 — `control reconcile` (validates Phase 1 output)

| Field | Detail |
|---|---|
| How | CLI command, fully deterministic — this is the "no thinking, just check" step you asked for. |
| Who | Orchestrator AI issues it; Script validates. |
| Where | `apex_kb_control.py:2076` → `reconcile_semantic_outputs()` → `_phase1_validation()` (this session's own code: exact path, no placeholders, `phase_2_ready: true`, ledger schema, candidate dispositions, **and** the new coverage gate — `opened`/`ranked` sources, blocked as `phase1_source_coverage_below_floor` if under 0.6). |
| Exact command | `python apex-meta/scripts/apex_kb.py --kb-root <path> --allow-write --json control reconcile` |
| What value | The file(s) the Semantic Executor just wrote. |
| What message | `ok` → advances state, records fingerprints for `phase2:<topic>`. Any failure → a specific reason code (never a vague "looks wrong"). |
| Feeds into | Step 11. |

## Step 11 — `control run` → `phase2:<topic>` (packet emission)

| Field | Detail |
|---|---|
| How | Same shape as Step 8. |
| Who | Orchestrator AI issues it; Script renders. |
| Where | `_phase2_packet()` (~line 1202). |
| What value | The validated Phase 1 output + registry page decisions. |
| What message | Writes `packets/phase2-<topic>.json`/`.md`. `short_trigger`: *"Execute the Apex KB packet at .../phase2-\<topic\>.md; write only the declared outputs; return the completion response exactly."* (line 1262) |
| Feeds into | Step 12. |

## Step 12 — Semantic Executor drafts Phase 2

| Field | Detail |
|---|---|
| How | Same relay mechanism as Step 9. |
| Who | Semantic Executor. |
| Where | Chat + repo write. |
| What value | Validated Phase 1 analysis, the wiki-page template, registry. |
| What message | Writes the compiled `wiki/summaries/<topic>.md` (and any concept/entity pages named in the packet). |
| Feeds into | Step 13. |

## Step 13 — `control reconcile` (validates Phase 2 output)

| Field | Detail |
|---|---|
| How | CLI command, deterministic. |
| Who | Script. |
| Where | `_phase2_validation()` (~line 1423): exact output path, unauthorized-write check against the packet's allowlist, and `_quality_page_metrics()` (existing structural quality gate — headings, claim counts, thin-M/M/M). |
| What message | `ok` → fingerprints the page for `semantic_acceptance:<topic>`. |
| Feeds into | Step 14 (only if the output tier is `compiled_minimal`/`compiled_full`/`query_ready`). |

## Step 14 — `control run` → `semantic_acceptance:<topic>` (packet emission)

| Field | Detail |
|---|---|
| How | Same packet shape, one more time. |
| Who | Orchestrator AI issues it; Script renders. |
| Where | `_acceptance_packet()` (~line 1265). |
| What value | The compiled wiki page(s) + target queries + resolved evidence — **not** the drafting rationale (per doctrine: acceptance must not see how the page was written). |
| What message | Writes `packets/semantic_acceptance-<topic>.json`/`.md`. `short_trigger`: *"Execute the Apex KB packet at .../semantic_acceptance-\<topic\>.md; write only the declared output; return the completion response exactly."* (line 1314) |
| Feeds into | Step 15. |

## Step 15 — Independent Evaluator runs acceptance

| Field | Detail |
|---|---|
| How | Relayed the same one-line-trigger way — but **must be a fresh, clean context**, never the same session that drafted the page. |
| Who | **Independent Evaluator** (explicitly not the Semantic Executor — this is a named, separate role). |
| Where | A new chat session. |
| What value | Only the packet's contents — no memory of how Phase 1/2 were drafted. |
| What message | Writes `audit/semantic-acceptance/<run-id>/<topic>.json`, schema `semantic-acceptance.schema.json`: `query_results` (each `answerable`/`partial`/`not_answerable`/`blocked`), `claim_reviews` (each `supported`/`partially_supported`/`contradicted`/`unresolvable`), and one final `verdict`. |
| Feeds into | Step 16. |

## Step 16 — `control reconcile` (the mandatory acceptance gate)

| Field | Detail |
|---|---|
| How | CLI command, deterministic, zero exceptions. |
| Who | Script. |
| Where | `_acceptance_validation()` (~line 1464): schema-valid, `run_id`/`topic_slug` match, every query `answerable`, every claim `supported`, **and** `verdict == "semantic_pass"` — all four, or it's blocked. |
| What message | Nothing short of `semantic_pass` on every query and claim advances the state. This is the fix for the original incident's core failure ("the gate never became mandatory"). |
| Feeds into | Step 17 (only for `query_ready` tier) or Step 18 (`complete`, for lower tiers). |

## Step 17 — `control run` → `postflight`

| Field | Detail |
|---|---|
| How | CLI command, deterministic. |
| Who | Script, delegates to existing `cmd_postflight`. |
| Where | `apex_kb_control.py:1737-1742`. |
| What message | Runs the existing 7-stage deterministic completion aggregate (lint, quality, retrieval freshness, etc.). Blocks unless it reports `pass`/`ok`. |
| Feeds into | Step 18. |

## Step 18 — `control run` → `complete`

| Field | Detail |
|---|---|
| How | CLI command. |
| Who | Script. |
| Where | `apex_kb_control.py:1999-2003`. |
| What message | Final `stage-result` with `status: ok`, `next_stage: null`. Run is done. |
| Feeds into | Nothing — terminal state. |

---

## Ancillary steps (available at any point, not part of the linear sequence)

| Command | Who | What it does |
|---|---|---|
| `control status` / `control next` | Orchestrator AI, any time | Read-only. Reports current stage + the exact next command, without executing anything (`control_status`/`control_next`, both call `derive_next_result()`). |
| `control git-state` | Orchestrator AI | Read-only Git/worktree classifier — branch, ahead/behind, dirty/conflicted counts. Never mutates. Blocks the stage machine if a merge/rebase/conflict is in progress. |
| `control doctor` | Orchestrator AI or you, any time | Read-only self-check of the **skill package itself** (schemas parse, docs agree, tests discoverable) — not tied to any run. |

---

## The one gap this table makes visible

**Step 0a has no "Script" row.** Every other step either *is* a script action or is a script that
renders/validates something. Step 0a is pure prose-instruction compliance — nothing forces the
Orchestrator AI to run it, or to call `control init` (Step 1) at all, before reaching for old
direct commands. `guard_direct_command` only starts blocking those old commands **after**
`manifests/run-state.json` exists (i.e., after Step 1 has already happened once). For a brand-new
KB, that file doesn't exist yet — so an AI that skips straight to `scaffold`/`phase0`/etc. the
old way is never stopped. That is almost certainly what you are watching happen right now.
