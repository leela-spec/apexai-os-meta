# apex-kb Command-Driven Orchestration — Plan

Status: PLAN ONLY. No skill/script files have been modified by this document. Every recommendation
below is evidenced against the actual Codex transcript (`CodexProblems/messages/001-013`,
`fragments/001`, `DetermnisticPhase2_Inconsistency_phase1&2semantic.md`) and the
`claude-code-orchestration-design` KB. Where your own draft (`New aPex-kb orga.md`) conflicts with
that evidence, I say so explicitly and recommend the evidenced alternative — see §4.

---

## 1. What actually broke (failure clusters, with transcript citations)

| # | Cluster | Evidence | Process step |
|---|---|---|---|
| A | **Structural gates pass, semantic value near-zero** — 9 topics "completed" from only 4 of 405 ranked sources; one Phase 1 analysis reused across many topics; pages hit minimum claim-count thresholds with thin one-sentence layers. Codex's own diagnosis: *"the process can now satisfy deterministic shape checks, but those checks do not establish that the pages carry enough domain knowledge... knowingly analyzed only 4 of 405 files and deferred the canonical Path, Rhythm, Sequencing, Stats, and Epic sources"* (msg 011). | msg 005, 011 | Phase 1 / Phase 2 semantic |
| B | **Worktree/branch state confusion** — local checkout didn't match a claimed "semantic build completed" report; remote was ahead; untracked local pilot files blocked a normal pull; long internal reasoning to reconcile it (msg 006, 9m39s work block in msg 009). This is your standing complaint (`New aPex-kb orga.md`: *"ths work tree issue comes up everytime... ai dont knwo what to do about it"*) — now transcript-confirmed, not just a feeling. | msg 006, 007, 009 | Deterministic run / git |
| C | **Multi-AI handoff channel is not durable** — the plan to "send a diagnostic prompt to the original chat and wait" failed outright: *"No matching Codex task or open browser chat exists. The available ChatGPT browser session is signed out."* (msg 013). The handoff depended on a specific chat session staying alive; it didn't. | msg 013 | Handoff between AIs |
| D | **Long internal deliberation before/instead of execution** — multi-paragraph internal narration in msg 006 and 011 (git-state reasoning, hypothesis-testing) before any file touches disk; matches your complaint that the orchestrating AI "is thinking an insane amount." | msg 006, 011 | All steps |
| E | **The skill's own reference doc contradicts its own validator** — `semantic-value-contract.md`'s embedded acceptance-artifact example uses `semantic_run_id`, `review_mode`, `verdict`, `material_claim_verifications`, `supported: true`; the actual `semantic-acceptance.schema.json` + validator require `run_id`, `evaluator_context`, `result`, `claim_reviews`, `result: "supported"`, `page_pointers`. The executor followed the doc faithfully and still failed validation. This is a pure **single-owner-schema violation** (two files defining the same shape, one stale) — a KB-documented anti-pattern (see §2). | fragment `DetermnisticPhase2_Inconsistency...` | Validation |
| F | **Registry-vs-output filename drift** — topic registry says `sequencing.md`, executor wrote `sequencing-and-play.md` (and 2 more mismatches); the deterministic validator correctly flags these, but nothing *prevented* them. | fragment `DetermnisticPhase2_Inconsistency...` | Phase 2 → validation |
| G | **Phase 1 ledger schema drift** — all 9 ledgers use `semantic_run_id` not `run_id`, `read` not `read_status`, invalid disposition values (`promote_tunable`, `embed_as_proposal`, `defer_future` instead of the 4-value enum), missing `page_decisions`/`candidate_dispositions`. Same root cause as E. | fragment `DetermnisticPhase2_Inconsistency...` | Phase 1 |

**Severity ranking:** A (product is worthless without it) > B+C (process cannot even complete a run reliably) > E+G (silent, 100%-reproducible validator failures) > D (symptom of B, not independent) > F (cosmetic once E/G are fixed).

---

## 2. What the orchestration-design KB says to do about it (cited, not invented)

- **Single-owner schema.** *"Each schema is defined in EXACTLY ONE file... Triple definition was found... Cost: ~800 redundant tokens per load."* Every other file references it as `canonical_source: <owning-file-path>`, never redefines it. → **Directly fixes Clusters E and G.** (`wiki/summaries/prompt-pack-and-artifact-contract-design.md`)
- **Deterministic-then-inference ordering.** *"Run deterministic checks before inference-based validation so LLM judgment is spent only on genuinely ambiguous or semantic rules."* (`wiki/concepts/deterministic-script-boundary.md`)
- **File state over chat state.** *"A claim of completion... is only trustworthy once it is anchored to a written artifact that can be fetched back and inspected... Chat continuity is explicitly insufficient for high-risk work; any workflow claiming completion from conversational memory alone should be treated as non-compliant."* → **Directly fixes Cluster C** — and directly contradicts the copy-paste-relay design in your own draft (see §4). (`wiki/concepts/file-state-over-chat-state.md`)
- **Low-token / standard handoff packet.** Required fields: settled state, source priority/authority, non-redo list, exact next job, risks, explicit success condition — never a menu of options, never reconstructed from memory. (`wiki/concepts/standard-handoff-packet.md`, `low-token-handoff-design.md`)
- **Stop condition as context saver.** HALT/CLARIFY must be an explicit visible field, name the single next required action, and exist specifically to stop *momentum errors* (continuing to burn tokens on a wrong assumption) — this is your Dealer-App-type failure and Cluster A's "kept going on 4/405 files" failure, same mechanism. (`wiki/concepts/stop-condition-as-context-saver.md`)
- **Progressive disclosure / thin scaffold, deep appendices.** Keep the orchestrator's own instructions small; push heavy schemas/templates into `references/`/`scripts/`, loaded only on demand. (`wiki/summaries/skill-package-design-contract.md`, `token-efficient-information-design.md`)
- **"Do not use LLM grading or page_value_score production"** for quality/coverage — already apex-kb's own rule; Cluster A shows it needs a *deterministic* teeth, not just a stated principle. (`ingest-analysis/max-run-20260709/05-failure-analysis-and-operator-feedback.md`, claim P1-FAIL-005)

---

## 3. Proposed architecture: one driver script, file-based handoffs, zero freeform orchestration

### Actors (confirmed, not assumed)
- **Orchestrator = Codex CLI.** Has repo access, runs Python/git, is the only one who touches `apex_kb.py`/the new driver.
- **Operator = you.** Answers the Q&A once per run; relays exactly one fixed trigger line to the executor; confirms the read-back.
- **Executor = ChatGPT-browser-with-git-connector.** Per your own transcript (msg 001, 003, 010: *"it does not have local access, only git conector"*), it already reads/writes repo files directly — it is **not** a plain chat needing pasted instructions. This changes the design from what your draft assumed.

### The one rule that fixes Cluster B, C, and D at once
**The orchestrator never improvises a git/apex_kb.py command sequence, and the operator never pastes packet content.** Everything reduces to:
1. Codex runs one driver subcommand → the driver deterministically decides what happens (including all git state) and writes exactly one of a fixed set of outcomes to a file.
2. If the next step is semantic (Phase 1/2), the driver writes a **self-contained instructions file into the repo**. The operator's entire job is one fixed sentence to the executor: *"Read `<path>` in the leela repo and execute it exactly; write your outputs to the paths it specifies; then read them back and reply 'done'."* No packet text is ever pasted by hand.
3. Codex validates the executor's file output deterministically (existence, schema, coverage ratio) — never by trusting the executor's chat-report prose.

### New component: `apex_kb_orchestrator.py` (new script, alongside the existing `apex_kb.py`)

A thin wrapper — it does not reimplement Phase 0/1/2, it sequences the *existing* `apex_kb.py`/`apex_kb_retrieval.py` subcommands with **zero freeform flags**, all derived from one input file.

```
apex_kb_orchestrator.py --kb-root <path> <stage>

stages (fixed, in this order — Codex only ever picks the stage name, never the flags inside it):
  intake        -> runs the existing Step 0 intake Q&A; writes/updates manifests/run-intent.md
  preflight     -> deterministic report + RECOMMENDATION (see §3.2); writes manifests/preflight-report.md
  sync          -> the ONLY place git happens; see §3.3
  phase0        -> calls apex_kb.py phase0 with args taken only from run-intent.md
  emit-phase1   --topic <slug>   -> writes outputs/prompts/phase1-packet-<slug>.md (file, not chat text)
  check-phase1  --topic <slug>   -> deterministic validation of what the executor wrote back (see §3.4)
  emit-phase2   --topic <slug>   -> writes outputs/prompts/phase2-packet-<slug>.md
  check-phase2  --topic <slug>   -> deterministic validation + coverage-ratio + acceptance gate (see §3.5)
  postflight    -> existing apex_kb.py postflight, unchanged
```

Every stage prints one JSON object: `{"stage": ..., "status": "ok|blocked|needs_operator", "next_stage": ..., "artifact": <path or null>, "reason": <fixed code or null>}`. Codex's entire job across a run is: read that JSON, run the `next_stage` it names, repeat. **No stage ever asks Codex to reason about what to do next — the JSON says it.**

### 3.1 Intake — extends what already exists, does not replace it
`run-intent.md` already exists from the prior Step-0 intent-lock work (this session, apex-kb SKILL.md). Per the single-owner-schema rule, **this plan does not invent a second intake file** — `intake` just becomes a scripted stage that fills the same schema, so it is machine-checkable instead of prose-checkable.

### 3.2 Preflight — deterministic report, not LLM prose
Real template (script-generated, every value computed, no field hand-written):

```markdown
# Preflight Report — <topic-slug> — <run_id>

## Deterministic facts
- corpus_root: <path>                     (from run-intent.md)
- files_discovered: <N>                   (os.walk count)
- ranked_sources_for_topic: <N>           (from topic-source-rankings.json)
- ranked_sources_above_elbow_cut: <N>     (work-pack elbow-cut count)
- kb_scope_evidence: <found|absent>       (topic-sanity-check verdict, reused as-is)

## Recommendation (rule-based, not opinion)
- output_tier: <compiled_minimal|compiled_full>   because: ranked_sources_above_elbow_cut <= 8 -> compiled_minimal is achievable in one pass
- corpus_breadth: narrow                          because: default; broad requires operator override (existing rule)
- execution_route: connector_only                 because: capability_precheck reports terminal_execution: unsupported

## Operator decision required
Reply with one of: `approve` | `override: <field>=<value>` | `stop`
```

No paragraph of this is authored per-run by an LLM — every line is `f"{value} because: {rule_name}"` from a fixed rule table. This directly answers your draft's *"all options... listed with a recommendation and the reasoning why"* — but as script output, so it cannot drift or ramble.

### 3.3 `sync` — the ONLY place git logic lives (fixes Cluster B)
Deterministic decision tree, fixed enum output, **never** freeform reasoning about branches:

```
git fetch origin
case:
  local == remote                        -> {"status": "ok", "action": "none"}
  local behind, no local changes         -> git pull --ff-only            -> {"status": "ok", "action": "pulled"}
  local behind, untracked-only changes   -> {"status": "needs_operator", "reason": "untracked_overlap",
                                              "action_required": "stash_or_remove: [<paths>]"}
  local behind, tracked local changes    -> {"status": "needs_operator", "reason": "tracked_divergence",
                                              "action_required": "operator_must_choose: keep_local | keep_remote"}
  local ahead                            -> git push                     -> {"status": "ok", "action": "pushed"}
```
Five outcomes, fixed text, no prose. This is the exact decision msg 006 spent an entire long paragraph reasoning through live — it becomes a table lookup.

### 3.4 `check-phase1` — deterministic-then-inference, in that order (fixes Cluster A partially)
1. **Deterministic pass (script, always runs first):** file exists at the exact registry-required path (fixes Cluster F); required headings present; no placeholder text; frontmatter schema-valid against the **single-owner** schema file (fixes E/G); `source_count` in frontmatter matches the number of `### <source_id> - authority:` blocks actually present (catches "claims 9 topics but only touched 4 files" *mechanically*, per-topic).
2. **Coverage-ratio gate (new, deterministic, directly targets Cluster A):**
   ```
   coverage_ratio = sources_with_a_written_record / sources_in_work_pack_above_elbow_cut
   if coverage_ratio < 0.6:  status = "blocked", reason = "insufficient_source_coverage",
                              detail = f"{opened}/{ranked} ranked sources actually analyzed"
   ```
   This is the mechanical fix for *"knowingly analyzed only 4 of 405 files"* — it cannot be satisfied by writing thinner content faster; it requires actually opening more of the ranked sources.
3. Only if both pass does the stage report `"status": "ok"` — an LLM never self-grades this.

### 3.5 `check-phase2` — adds the mandatory acceptance gate (fixes the msg-011 finding directly)
Codex's own diagnosis: *"the same failure was already documented... but its independent query/entailment gate never became mandatory in the connector-only path."* Fix, stated as a hard rule with no exception clause:

> **No run may report `compiled_unvalidated` in its final chat message unless
> `audit/semantic-acceptance/<run-id>/<topic-slug>.json` exists and its `verdict` field
> reads `semantic_pass`.** `check-phase2` checks this file's existence and verdict field
> *deterministically* before allowing the stage to report `"status": "ok"`. If the file is
> absent, status is `"needs_operator"` with `reason: "acceptance_artifact_missing"` — the
> run is not "probably fine," it is blocked.

### 3.6 The file-based handoff packet (fixes Cluster C)

`outputs/prompts/phase1-packet-<topic-slug>.md` — real template, fields filled only from `run-intent.md` + `topic-registry.json` + the work-pack, never freehand:

```markdown
---
packet_type: phase1_instructions
run_id: <run_id>
topic_slug: <topic-slug>
required_output_path: ingest-analysis/<topic-slug>.analysis.md   # exact, enforced (fixes Cluster F)
template_ref: semantic-contract/phase1-analysis-template.md      # canonical_source, never inlined (single-owner rule)
work_pack_ref: manifests/phase0/work-packs/<topic-slug>.md
stop_condition: "HALT if the required raw source cannot be opened; do not infer content."
success_condition: "File written at required_output_path, reread, coverage >= 60% of the
  work pack's elbow-cut source list actually opened and recorded."
---

# Phase 1 Instructions — <topic-slug>

Read `template_ref` and `work_pack_ref` in full before writing anything.
Write your single output file at exactly `required_output_path` — no other path is valid.
When done, reply in chat with only: "done: <required_output_path>" — no summary, no report text.
The orchestrator will read the file back itself; a chat description is not evidence of completion.
```

The operator's one-line trigger to the executor never changes shape run to run:
> *"Read `outputs/prompts/phase1-packet-<topic-slug>.md` in the leela repo (git connector) and
> execute it exactly. Reply only 'done: <path>' when finished."*

This is the direct fix for Cluster C: if the executor's chat session dies mid-run, the operator opens **any** new session with git-connector access and repeats the exact same trigger line pointing at the same file — nothing is lost, because nothing that matters was ever *in* the chat.

---

## 4. Where your draft (`New aPex-kb orga.md`) is right, and where I disagree (per your explicit "don't be a pushover" instruction)

| Your idea | Verdict | Why |
|---|---|---|
| Q&A collects KB folder, index folder, preflight depth, KB type, intent | **Keep** | Matches the existing Step-0 intent-lock design (`run-intent.md`) already built; just needs to become script-filled, not prose-filled. |
| "Full instructions pre-run template... options with recommendation and reasoning" | **Keep, but script-generated** | See §3.2 — real template above, computed not written. |
| Orchestrator "pastes the script/command/template/message to the operator in chat" for the operator to relay to the executor | **Reject as the primary mechanism** | Directly contradicts the transcript's own failure (Cluster C: the relay depended on a chat session that vanished) and the KB's explicit rule that chat continuity is *"insufficient for high-risk work... any workflow claiming completion from conversational memory alone should be treated as non-compliant."* Your executor already has file read/write via git connector (msg 001/003/010) — pasting text through chat is strictly worse than pointing it at a file it can already read itself. Replace with the one-line trigger + file packet in §3.6. |
| "make the AI only execute commands, not think" | **Keep as the design's central goal** — but the mechanism is the fixed-stage-JSON driver (§3), not merely an instruction telling the AI to think less (an instruction alone did not work here — msg 006/011 show the AI narrating extensively *despite* being told to be deterministic). | Deterministic-script-boundary: mechanical decisions must be made by a script, not requested of an LLM by prose. |
| Worktree confusion "comes up every time" | **Confirmed, root-caused, fixed** | §3.3 — five fixed outcomes replace the freeform git reasoning that produced the 9m39s deliberation block in msg 009. |
| Codex vs GPT-browser: "otherwise apex-kb will run into repo problems as templates aren't accessible" | **Confirmed correct concern; solved by packaging, not by giving GPT-browser scripts** | See §5 — GPT-browser never runs scripts; it only ever needs the *contents of one file* (the packet), which it already fetches via its own git connector. Nothing needs duplicating into a separate "GPT skill" beyond a short instruction card telling it how to read/interpret a packet file — see §5. |

---

## 5. Packaging: Codex skill vs GPT-browser skill (your explicit requirement)

- **Codex skill package** = the existing `apex-kb` skill folder, plus the new `apex_kb_orchestrator.py` inside `scripts/`. Nothing changes about portability here — it already assumes local repo + Python access.
- **GPT-browser skill package** = intentionally tiny. It does **not** need any script, template copy, or repo-specific content baked in, because every run-specific detail already lives in the packet file the driver writes (§3.6) and the executor fetches live via its git connector. The GPT-browser skill only needs one short, generic instruction card (not per-run content):
  > "When given a path like `outputs/prompts/phase1-packet-*.md` or `phase2-packet-*.md` in a
  > repository you have git-connector access to: read that file in full, read every file it
  > references under `template_ref`/`work_pack_ref`, do exactly what it says, write your output
  > at exactly the path it names, then reply with only `done: <path>`. Never invent an output
  > path. Never report completion without having written and reread the file."

  This card is the *entire* GPT-browser "skill" — it is subject-agnostic, repo-agnostic, and never needs updating when the apex-kb templates change (because it never embeds them; it always fetches `template_ref` fresh). This satisfies "universally applicable... not saved with repo access issues" directly: the repo-specific material never leaves the repo.

---

## 6. Ranking table

Scored 1–10 (10 = best/highest). Weighted composite = `0.30*Impact + 0.20*Evidence + 0.20*(11-Risk) + 0.15*(11-TokenCost) + 0.15*Resilience`.

| # | Option | Impact | Evidence | Risk | Token Cost (build+run) | Resilience | **Weighted** | Verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Extend existing `run-intent.md` intake, script-filled | 9 | 8 | 2 | 3 | 8 | **8.6** | ✅ Keep |
| 2 | Deterministic preflight + rule-based recommendation report | 8 | 7 | 2 | 3 | 8 | **8.1** | ✅ Keep |
| 3 | `apex_kb_orchestrator.py` driver, fixed-stage JSON | 9 | 9 | 4 | 6 | 9 | **7.8** | ✅ Keep (core of the plan) |
| 4 | Deterministic `sync` stage (5-outcome git decision tree) | 9 | 9 | 5 | 5 | 9 | **7.7** | ✅ Keep |
| 5 | File-based handoff packet + fixed one-line operator trigger | 9 | 9 | 3 | 4 | 10 | **8.6** | ✅ Keep — highest-confidence fix for the worst channel failure |
| 6 | Coverage-ratio gate (≥60% of ranked sources actually opened) | 9 | 9 | 4 | 5 | 8 | **7.8** | ✅ Keep — directly targets Cluster A |
| 7 | Mandatory, deterministically-checked semantic-acceptance gate | 9 | 8 | 3 | 4 | 9 | **8.3** | ✅ Keep |
| 8 | Single-owner schema fix (delete drifted inline examples) | 8 | 10 | 1 | 2 | 9 | **8.9** | ✅ Keep — do this one first, it's pure upside |
| 9 | Enforce registry `expected_page` as literal required path | 6 | 8 | 1 | 1 | 8 | **7.4** | ✅ Keep — cheap, mechanical |
| 10 | Deterministic-then-inference ordering enforced structurally | 7 | 7 | 2 | 3 | 8 | **7.5** | ✅ Keep |
| 11 | Tiny, generic GPT-browser instruction card (no embedded templates) | 8 | 6 | 3 | 5 | 7 | **6.9** | ✅ Keep |
| 12 | Chat-paste relay of full packet text (your draft's original mechanism) | 3 | 2 | 7 | 6 | 2 | **2.7** | ❌ Reject — replaced by #5 |
| 13 | Reusing one Phase-1 analysis across many topics to save effort | 2 | 9 | 9 | 1 | 1 | **2.0** | ❌ Reject — this *is* the value-hollowing bug; #6 prevents recurrence |
| 14 | LLM self-graded "page value score" | 2 | 8 | 8 | 4 | 2 | **2.6** | ❌ Reject — already against apex-kb's own existing rule; keep it rejected |

**Read this as:** items 1, 5, 8 are the highest-leverage, lowest-risk starting points (do these regardless of anything else). Items 3/4/6/7 are the substantive engineering (the actual driver script + gates) and should be built together since they share the JSON-stage contract. Item 11 is nearly free once 3-7 exist.

---

## 7. Suggested build order (not yet executed)

1. **Single-owner schema fix** (#8, #9) — same-session, mechanical, zero design risk. Fixes Clusters E, F, G outright.
2. **`apex_kb_orchestrator.py` skeleton** with stages `intake`, `preflight`, `sync` (#1, #2, #3, #4) — this alone kills Clusters B and D, and is testable with unit tests exactly like the existing `apex_kb.py` suite.
3. **`emit-phase1`/`check-phase1`/`emit-phase2`/`check-phase2`** (#5, #6, #7, #10) — this is where Cluster A and C actually get fixed; needs the coverage-ratio and acceptance-gate logic designed carefully against real work-pack data before trusting it.
4. **GPT-browser instruction card** (#11) — trivial once the packet format is stable.

I have **not** touched any file to build this yet. Tell me which stages to implement first, or if you want changes to the ranking/weights before we start.
