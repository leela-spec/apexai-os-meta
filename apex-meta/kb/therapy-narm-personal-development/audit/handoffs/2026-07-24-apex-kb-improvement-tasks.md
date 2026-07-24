# Apex KB improvement — hand-over task packets

**Purpose.** Ready-to-dispatch implementation tasks derived from the approved plan. Each packet is self-contained: exact files, precise change, acceptance test, dependency, and a **type label** so you route it to the right executor.

**Two executor types (per your token model):**
- **`[DET]` Deterministic** — mechanical code/doc/schema edits and CLI runs. **No LLM semantic drafting; cheap.** Any coding agent or a local runner can do these. Running `apex-kb` commands costs **zero model tokens**.
- **`[SEM]` Semantic** — token-expensive drafting of KB content, run by your unlimited-token agent in a separate chat. **Hard requirement (operator):** the packet the CLI emits and commits to `main` must be **100% self-sufficient** — it already contains every path, every allowed source (with the exact pointers/excerpts to use), the output schema, the exact output path, *and* best-practice authoring instructions for a full-value semantic file. **The external agent adds no information, paths, or files — it only writes the semantic prose into the pre-defined blanks.** If the external agent has to hunt for a path or a source, the packet is defective (that is a `[DET]` packet-emission bug, see **P1**).

**Two design principles (operator guardrails):**
1. **Build good KB infrastructure first; don't make self-verifying quality tests the core.** The highest-value work is making the *inputs* good — the prompt/task templates and the self-sufficient packets that produce rich semantic files (**A0/A1/A3/P1**). This is *prioritized above* verification work.
2. **Keep guardrails lightweight and deterministic.** For over a month, AI-grades-AI "quality" checks and self-verifying processes did **not** work and wasted effort. We keep *deterministic structural* gates (schema floors, pointer-resolves-to-a-real-line) because those are cheap and objective — but we **demote** LLM-based self-acceptance from a core gate to an optional, bounded check (**A4**). We do **not** remove guardrails; we just refuse to over-invest in ones that already failed.

**Realms (fixed vocabulary — never conflate):** ① Apex KB **CLI** (the `apex-kb` exe, sole authority) · ② semantic **worker** (AI filling one packet) · ③ Apex KB **skill** (`.claude/skills/apex-kb/`, the manual) · ④ Apex KB **operator agent** (new `.claude/agents/apex-kb-operator.md`).

**Priority / dependency order (revised per operator feedback):**
`B1` (fix the manual) → **`A0` (research better prompts — KEY)** → `A1` (rewrite templates) → `A2` (schema floors) → `A3` (cross-links) → **`P1` (self-sufficient packets)** → `B2`,`B3` (tell the truth) → `AG1` (operator agent) → `O1` (progress/blocker visibility) → `C1`,`C2` (query value) → `B4` (pointer-resolve guard, lightweight) → `PK1` (clean install/paths) → `S1` (11th source) → `A4` (optional bounded acceptance — **not** core) → `C3` (gated). All implementation packets are `[DET]`; only the therapy-KB re-drafted **content** (packet R2) is `[SEM]`.
**What moved up:** prompt/template optimization (A0/A1) and self-sufficient packets (P1) are now top infrastructure work. **What moved down:** LLM-based acceptance (A4) is demoted below the infrastructure and truth fixes. **Nothing was deleted** — every guardrail/quality check remains available; only A4's *priority* dropped.

**Coverage check — every high-impact item is targeted (packet → what it increases):**
| Value-increasing (build a better KB) | Trust/usability | Deterministic guardrail (kept, not over-invested) | Retrieval/agent value |
|---|---|---|---|
| **A0** research prompts · **A1** rewrite prompts · **A3** cross-links/indexing · **P1** self-sufficient packets | **B1** fix the manual · **B2** honest state · **B3** visible drift · **O1** progress/blocker visibility · **PK1** clean install/portable paths · **S1** index the 11th source | **A2** schema floors · **B4** pointers resolve to real lines · *A4 optional answerability* | **AG1** operator agent · **C1** clean/ranked query · **C2** future-agent contract · **C3** reranker (gated) |

This is the complete set — the four value-increasing infrastructure tasks (A0/A1/A3/P1) plus the operator agent (AG1) and the future-agent contract (C2) are the highest-leverage new work; guardrails are present but deliberately lightweight.

---

## GROUP B — Trust & skill (do first)

### B1 `[DET]` · realm ③ — Reconcile the Apex KB skill to the installed CLI
**Why (process→value):** today the skill's manual contradicts the machine — it documents a dead `apex_kb.py control` surface and never mentions `query`. An agent reading it can't find the KB's search feature and wanders. Fixing it makes the manual match the machine and removes the #1 drift cause.

**Files & exact changes:**
1. `.claude/skills/apex-kb/SKILL.md` — the `## Public flow` / `## Allowed actions` sections list only `start/status/continue`. Add the four missing commands with one-line each:
   - `apex-kb drive --run-root <path> [--json-output]` — run deterministic actions to the next semantic/terminal boundary.
   - `apex-kb query --run-root <path> --query "<text>" [--topic <id>] [--limit N] [--json-output]` — **search the compiled KB** (the retrieval interface).
   - `apex-kb doctor --run-root <path> [--json-output]` — read-only health probe.
   - `apex-kb update --run-root <path> [--config <yaml>] [--yes]` — controlled incremental run.
   Add a line: *"Prefer `--json-output` for machine-readable envelopes."*
2. `.claude/skills/apex-kb/package-manifest.md` — remove/replace the legacy script surface:
   - Lines 9–13 `script_paths:` block (`apex_kb.py`, `apex_kb_start.py`, `apex_kb_control.py`, `apex_kb_retrieval.py`) → replace with `installed_cli: apex-kb (entry point apex_kb.cli:main, package apex-meta/apex-kb-cli)`.
   - Lines 67–69 and 127 and 131 — delete the sentences that name `apex_kb_control.py`/`apex_kb.py` as "the executable owner"; replace with: *"The installed `apex-kb` CLI (`apex-meta/apex-kb-cli`) is the sole lifecycle authority."*
   - Any `references/*` that describe the legacy `control` command surface (e.g. `references/script-command-contract.md`, `references/acceptance-tests.md` mandatory-acceptance language) → either delete or add a top banner: *"SUPERSEDED — the installed `apex-kb` CLI is authoritative; acceptance is disabled by default."*

**Acceptance test:** `grep -rn "apex_kb.py\|apex_kb_control\|control " .claude/skills/apex-kb/` returns 0 operative references; `grep -rn "apex-kb query" .claude/skills/apex-kb/SKILL.md` returns ≥1. The skill lists all 7 commands.
**Dependency:** none. **Effort:** S.

---

### B2 `[DET]` · realm ① — Stop the postflight acceptance overclaim
**Why (process→value):** the certificate asserts `all_semantic_acceptance_pass: true` even when acceptance was never run (`acceptance_verdicts` is empty). That makes the state lie about quality. Fix it so the label is trustworthy.

**Files & exact changes:**
- `apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py` (~line 485, where `all_semantic_acceptance_pass` is forced `True` when acceptance is off). Change so that when acceptance is disabled the postflight `checks` reports `all_semantic_acceptance_pass: false` **or** a distinct value `"acceptance": "disabled"` — never a bare `true`.
- In the postflight/completion output add a boolean `semantically_accepted` (true only if an independent acceptance verdict exists) distinct from `import_accepted` (schema/citation/postflight passed). Set page/topic status language accordingly.

**Acceptance test:** run `apex-kb drive` (no `--semantic-acceptance`) on a scratch KB → postflight JSON shows `all_semantic_acceptance_pass` ≠ `true` and `semantically_accepted: false`. Extend `tests/test_product_contract.py` to assert the vacuous-pass is gone.
**Dependency:** none. **Effort:** S.

---

### B3 `[DET]` · realm ① — Portable source-drift, surfaced by `doctor`/`status`
**Why (process→value):** `doctor` reports `fresh:true` even though raw sources changed after the build, because it only compares the index to the pages, and the drift check is bound to Windows absolute paths (`C:\…`) that don't resolve elsewhere. Result: an agent trusts stale pointers. Fix makes staleness visible everywhere.

**Files & exact changes:**
- `apex-meta/apex-kb-cli/src/apex_kb/corpus/engine.py` `check_source_drift` (~line 1023): stop using `record["absolute_path"]`; resolve each source from `manifest source resolved_root + repository_path` (repo-relative), so it works on any machine. When building the inventory, store **repo-relative** paths (or store both and prefer relative).
- `apex-meta/apex-kb-cli/src/apex_kb/lifecycle.py` `status_snapshot` and `cli.py doctor`: call `check_source_drift` and include a `source_drift` block (`fresh`, `changed`, `added`, `deleted`) in `status`/`doctor` output.

**Acceptance test:** on the current repo (where `MyTherapy.md` drifted 598→456 lines), `apex-kb doctor --run-root <therapy-kb>` reports the changed/deleted sources instead of `fresh:true`. Add a test that mutates a source hash and asserts `doctor` flags it.
**Dependency:** none. **Effort:** M.

---

### B4 `[DET]` · realm ① — Canonical pointer ledger + resolve-to-real-line
**Why (process→value):** capsule and review pointer ledgers disagree (e.g. `narm-model` capsule kept lines 5583/5587 that the review ledger dropped), and the a02 "correction" re-anchored the trauma-distinction claim to non-supporting headings. Fix gives one pointer truth and forbids pointers to blank/non-existent lines.

**Files & exact changes:**
- `apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py` import validation (`_validate_citations` ~144-157; phase-1 review vs capsule ~255-312): reconcile capsule↔review pointers into one canonical set at import; reject a Phase-2 citation whose pointer is not in the reconciled ledger.
- Add a resolve check: every accepted pointer must map to a **non-empty, non-separator** line in the derived extracted text; reject with a numbered repair otherwise.

**Acceptance test:** feed a result citing a pointer that lands on a blank line / `---` → CLI rejects with repair. Existing `tests/test_semantic_integrity.py` extended.
**Dependency:** none (independent of B1–B3). **Effort:** M.

---

## ④ OPERATOR AGENT (after B1)

### AG1 `[DET]` · realm ④ — Author `.claude/agents/apex-kb-operator.md`
**Why (process→value):** replaces the "drive the CLI by hand and hope the chat agent doesn't wander" flow with a tightly-chartered operator that always runs the real commands, prefers `--json-output`, reports progress/blockers in plain language, and refuses to edit state or invent commands. Fixes the month-long drift structurally (the CLI stays authority; the agent just operates it).

**Exact file to create (ready to paste, house style = clone of `apex-sync-ops.md`):**
```markdown
---
name: apex-kb-operator
description: Use to run the Apex KB lifecycle end-to-end via the installed apex-kb CLI — start, status, continue, drive, query, doctor, update. Drives runs, reports plain-language progress/blockers, and executes one CLI-issued semantic packet when explicitly handed one. Never edits run state/manifests, never invents commands, never decides lifecycle stages (the CLI does). Not a router for other tools yet.
tools: Read, Grep, Glob, Bash
skills:
  - apex-kb
---

You are the Apex KB CLI operator, not the lifecycle authority. The installed `apex-kb` CLI is the sole authority: it decides the next legal step, validates, and writes state.

Follow the preloaded `apex-kb` contract. Run only canonical `apex-kb <command> --run-root <path>` commands, and prefer `--json-output`. Let the CLI choose the next stage; when it emits a semantic packet, either hand it to the operator's semantic executor or, only if explicitly instructed, execute exactly that one packet and write only to its declared `expected-output-path.txt`. Then run `apex-kb drive` again.

Report progress in plain language after each boundary: which topics are done, which is waiting, and whether the system is working or waiting on input. When the CLI reports a blocker, translate its reason code into {which component raised it, what it protects, the consequence of bypassing, the safe resolution}.

Never edit run-config, manifests, run-state, stage results, wiki pages, retrieval files, or sources. Never invent a command the CLI did not return. Never create branches, worktrees, or stashes. Stop and hand back on any mismatch or missing identity/evidence.
```

**Acceptance test:** spawn the agent on a scratch KB; confirm it runs `start → drive → status → query` with `--json-output`, narrates progress/blockers, and **refuses** to edit state or run a non-canonical command (drift test).
**Dependency:** B1 (so the preloaded skill is correct). **Effort:** S.
**Scope note:** lifecycle-only now. Routing (CLI vs Mermaid vs graph) is a **later, gated** packet — add a `references/tool-routing-matrix.md` the agent consults and have it *recommend*, not decide. Do not add routing in AG1.

---

## GROUP A — Make the wiki richer (this is the core value work per operator feedback)

### A0 `[DET]` · realm ① — **KEY RESEARCH STEP: design best-practice KB-authoring prompts** (learn from the other wikis / projects / internet)
**Why (process→value):** the single biggest lever on wiki quality is the *instructions the CLI gives the worker*. Today they under-specify (Part 2 of the plan). Before rewriting them (A1), study what good KB-authoring prompts actually look like, so the new templates are best-practice, not guesswork. This is the research+optimization step the operator flagged as missing.

**Inputs to study (local first, then external — do NOT send private therapy content to the internet):**
- **Local llm-wiki projects** (`source-knowledge/ProjectRepos/llm-wiki-main/`, `.../llm-wiki-skill-main/`): read their `workflows/ingest.md`, `workflows/query.md`, `WIKI_SCHEMA.md`, page templates, and `SKILL.md`. Extract concretely: how they instruct the AI to preserve *all* pointers, cross-link pages, flag contradictions, and write per-source summaries. llm-wiki-main's two-phase ingest and llm-wiki-skill-main's hierarchical dossier + per-source-summary instructions are the strongest local models.
- **OpenKB** (VectifyAI/OpenKB) and **deepwiki-open** authoring/prompt behavior — how they produce interlinked concept/entity pages with citations (public docs/repos only).
- **External best practice** (public): documentation/knowledge-authoring prompt patterns (e.g. Anthropic contextual-retrieval chunk-context idea, structured "answer + cite every source line" prompting). Cite sources + dates.

**Output (deliverable of A0):** a short `apex-meta/apex-kb-cli/docs/prompt-design-notes.md` capturing the extracted patterns + the exact new wording to drop into the Phase 1 / Phase 2 templates in A1. No code change yet — this is the design that A1 applies.
**Acceptance test:** the notes name ≥3 concrete, sourced patterns (pointer-coverage, cross-linking, per-source depth) and provide ready-to-paste template language.
**Dependency:** none. **Effort:** M. **Priority: high (core value).**

### A1 `[DET]` · realm ① — Apply the rewritten hardcoded prompts (from A0)
**Why (process→value):** the prompts tell the worker *which* sections to write but never *how much*, so it produced the thin minimum (1 pointer where 9 existed; 3 claims where ~21 existed). Applying A0's best-practice wording makes the next run thorough — and, per the self-sufficiency rule, the instructions live *inside the emitted packet* so the external agent needs nothing else.

**Files & exact changes (use A0's exact wording; the below is the floor):**
- `apex-meta/apex-kb-cli/src/apex_kb/templates/phase1-task.md` line 13 — after "Preserve versions, contradictions, uncertainty, authority, and freshness." add: *"For every source you open, record **all** material line pointers (not a token sample) and **every** distinct key claim it supports. For each locked question, answer completely and cite every supporting pointer."*
- `apex-meta/apex-kb-cli/src/apex_kb/templates/phase2-task.md` line 9 — change "citation must be non-empty" expectations to: *"Each ranked source must carry **all** pointers preserved for it in Phase 1. Enumerate **every** material key claim (not a sample). Each direct answer must cite every supporting pointer. Write Macro/Meso/Micro as substantive paragraphs (≥3 sentences each), not one-liners. Add a Related-pages section linking every related topic."* (plus any richer A0 language)
- Mirror the same wording in the injected contracts in `semantic/engine.py` (`page_value_contract` ~374-379 and the phase-1 disposition contract ~109).

**Acceptance test:** re-emit a Phase 2 packet (packet R1) and confirm the `TASK.md` now contains the coverage + related-pages language. Full validation is via A2 + the R re-run diff.
**Dependency:** A0. **Effort:** M. **Priority: high (core value).**

---

### A2 `[DET]` · realm ① — Raise schema floors so thin output is rejected
**Why (process→value):** prompts alone are soft; the schema is the hard gate. Today `minItems:1` lets one pointer/claim pass. Raising floors makes the CLI *reject* thin results with a numbered repair — richness becomes enforced.

**Files & exact changes (`apex-meta/apex-kb-cli/src/apex_kb/schemas/phase2-result.schema.json`):**
- `key_claims` (line 21): raise `minItems` to a realistic floor (e.g. `3`).
- Per-source `adaptive_ranked_sources[].citations` (line 17): keep `minItems:1` but add a validation in `semantic/engine.py` that each ranked source carries **≥ the count of pointers Phase 1 preserved for that source** (coverage check, not a fixed number).
- `open_questions` (line 23): add `"minItems": 1`.
- `phase1-result.schema.json`: give `review.pointers` and `target_answers[].citations` a `"minItems": 1` (today they have none).
- Add the coverage check to `import_phase2_result`/`import_phase1_result` so a shortfall triggers a numbered repair (reuse existing repair path).

**Acceptance test:** submit a result with 1 claim / 1 pointer where more exist → rejected with repair; a covered result passes. Extend `tests/test_semantic_integrity.py`.
**Dependency:** pairs with A1. **Effort:** S–M.

---

### A3 `[DET]` · realm ① — Add a cross-link / related-pages field (enables "indexing")
**Why (process→value):** there is **no field** linking pages today, so the wiki is 10 stand-alone files. Adding `related_pages` makes it an interlinked web the operator can navigate and the retriever can traverse.

**Files & exact changes:**
- `schemas/phase2-result.schema.json` `dossier` object — add `"related_pages": {"type": "array", "items": {"type": "object", "required": ["topic_id","relation"], "properties": {"topic_id": {"type":"string"}, "relation": {"type":"string","minLength":1}}}}` (start optional, then require `minItems:1` once workers populate it).
- `phase2-task.md` — instruct the worker to list related topics and the relationship (e.g. "narm-model ↔ narm-personal-match-map: theory feeds the match map").
- Renderer in `semantic/engine.py` (`_render_*`) — emit a `## Related pages` section with markdown links to the other concept pages.
- `retrieval/engine.py` — index the related-pages section so `query` can surface cross-links.

**Acceptance test:** rendered dossier contains a `## Related pages` section with resolvable links; `query` returns them. Add a render test.
**Dependency:** A1/A2 land first (same schema file). **Effort:** M.

---

### P1 `[DET]` · realm ① — **Make emitted packets 100% self-sufficient** (operator hard requirement)
**Why (process→value):** the external unlimited-token agent must be able to draft a full-value semantic file with **only** the committed packet — no path-hunting, no fetching sources, no guessing conventions. Today the packet lists an allow-list and a schema; it must instead be a complete, ready-to-execute brief. This is what makes the `[SEM]` step reliable and drift-free (the external agent can't wander if everything is pre-defined).

**Files & exact changes (`apex-meta/apex-kb-cli/src/apex_kb/semantic/engine.py` packet assembly + `templates/*.md`):**
- The emitted packet directory must contain, with correct absolute-and-relative paths already resolved: `TASK.md` (best-practice authoring instructions from A0/A1), `task.json` (identity), `source-allowlist.json`, `output.schema.json`, `expected-output-path.txt`, **and** the **resolved source material the worker is allowed to use** — either inlined excerpts or exact `src-id + line` pointers with the extracted-text file path — so the worker never opens anything not in the packet.
- `TASK.md` must state the *complete* authoring contract: every required section, the pointer-coverage rule, the cross-link rule, the "write only to `expected-output-path.txt`" rule, and "add nothing outside these blanks."
- Add a deterministic **packet self-check** at emit time: assert every referenced path exists and every allow-listed source resolves; refuse to emit an incomplete packet.

**Acceptance test:** emit a packet, then verify (deterministically) that a worker with **only** that packet directory — no repo access beyond it — has every path, source, schema, and instruction needed; the self-check rejects a packet with a missing/unresolved reference. Add a test that deletes one referenced source and asserts emit fails.
**Dependency:** A1 (instructions) + A3 (cross-link field in schema). **Effort:** M. **Priority: high (core value).**

### A4 `[DET]` · realm ① — Optional bounded answerability check (**demoted — NOT a core gate**)
**Why / guardrail note:** independent acceptance is off, so `query_ready` never proves a page answers its question. A *minimal* check would restore that — **but** per the operator guardrail, LLM-grades-LLM self-verification failed for a month and must **not** become the core of this update. So this is **optional and bounded**, sequenced *after* all infrastructure and truth fixes. Do the cheap deterministic guard (**B4**, pointers resolve to real lines) regardless; treat A4 as opt-in only.

**Files & exact changes:** keep the existing `--semantic-acceptance` flag opt-in (do **not** default it on unless the operator asks). If enabled, it must run in a genuinely **fresh** ② context (separate chat/agent) and record a real verdict in `acceptance_verdicts`; it must never fabricate a pass (see B2). Prefer the smallest possible check (answerable-from-page + tiny claim sample), not an elaborate rubric.
**Acceptance test:** with the flag off, `query_ready` is reachable and B2 reports `semantically_accepted:false` honestly; with the flag on, a recorded verdict is required and no vacuous pass is written.
**Dependency:** B2. **Effort:** S (kept small on purpose). **Priority: low (optional).**

---

## GROUP C — Retrieval & future-agent (after A/B)

### C1 `[DET]` · realm ① — Clean query excerpts + answer-chunk-first ranking
**Why:** query excerpts wrap matched terms in `[brackets]`, mangling displayed paths, and the atlas boilerplate header ranks #1 for broad queries. Fix makes results read cleanly and lead with the answer.
**Files:** `retrieval/engine.py` — the `snippet(...)` call (~line 369) bracket markers; bm25 column weighting (~line 370) to down-rank atlas boilerplate / up-rank dossier answer chunks.
**Acceptance test:** for each locked query, top-1 result is an answer-bearing dossier chunk; excerpts show clean paths.
**Dependency:** none. **Effort:** S.

### C2 `[DET]` · realms ① + ③ — Future-agent query contract
**Why:** the KB is currently "a folder of links" with no usage policy. A contract makes any future AI search first, budget context, and reopen raw only on drift/absence.
**Files:** extend `query` `--json-output` to include a `retrieval_policy` + `context_budget` + `answer_contract`; add the same policy to `wiki/index.md` and reference it from the skill (built on B1).
**Acceptance test:** `query` output and `wiki/index.md` both state: search-first, ≤5 answer chunks, reopen-raw-only-if-drift/absent.
**Dependency:** B1. **Effort:** M.

### C3 `[DET]` · realm ① — Local reranker over FTS5 top-K (**gated on a benchmark**)
**Why:** best-practice evidence shows reranking is the cheapest, still-local retrieval-precision upgrade (embeddings/graph are not justified here). Only adopt if it beats the FTS5 baseline on a golden set.
**Prerequisite:** build the golden-query/answer-quality benchmark (residual #13) first; adopt C3 only if it measurably wins.
**Dependency:** benchmark. **Effort:** M–L.

---

## GROUP D — Remaining value/quality items (from the audit backlog; previously omitted)

### O1 `[DET]` · realm ① — Operator-visible progress + plain-language blockers
**Why (process→value):** a direct fix for the month-long "is it working or just stuck?" confusion. `status` today only enumerates state; it never says how far along a run is or whether it is *working vs waiting on you*.
**Files & exact changes:** `lifecycle.py status_snapshot` + `cli.py status` — add a `progress` block (`topics_accepted N/5`, `current: waiting_for_semantic_packet|running|blocked|complete`) and a `blocker_explained` block that maps each reason code to `{component, invariant it protects, consequence of bypassing, safe resolution}` in plain English.
**Acceptance test:** `apex-kb status` shows `3/5 accepted, waiting on your Phase-2 draft for topic 4`; a blocked run prints a human-readable cause+fix. **Effort:** M. **Value: high (operator experience).**

### PK1 `[DET]` · realm ① — Clean-install robustness + portable stored paths
**Why (process→value):** on a fresh machine `doctor` crashed (pypdf→cryptography→`cffi`), and durable JSON stores Windows `\\` paths that break on other systems. Fixes make the tool install and run anywhere.
**Files & exact changes:** `pyproject.toml` — move `pypdf` to an optional `[project.optional-dependencies] pdf = [...]` extra (or guard the import so `doctor` degrades gracefully instead of a hard crash). In `io.py`/state writers — normalize stored paths to forward slashes (`as_posix()`), so `completion.json`/`run-state.json`/inventory are portable.
**Acceptance test:** clean-box `pip install` + `apex-kb doctor` succeed without extra system deps; `grep -c '\\\\' completion.json run-state.json` = 0 after a fresh run. **Effort:** S–M. **Value: medium (portability/trust).**

### S1 `[DET]` · realm ① — Index the 11th source (or record its exclusion)
**Why (process→value):** `Integrierte Psychologiekarte & OS.md` (62 KB) is present in raw notes but **not** in the index, with no exclusion reason — silent coverage loss.
**Files & exact changes:** either add it to the configured source folders so it is inventoried/indexed, or record an explicit `exclusion_reason` in `source-inventory.ndjson`. Decide per its relevance to the five topics.
**Acceptance test:** the source is either indexed (appears in `source-inventory.ndjson` as `included`) or carries a non-null `exclusion_reason`. **Effort:** S. **Value: medium (completeness).**

---

## THERAPY-KB RE-COMPILE (the only `[SEM]` work)

### R1 `[DET]` — Emit fresh richer packets
After A1–A3 land, run (zero model tokens): `apex-kb update --run-root <therapy-kb>` (or a fresh `start`) then `apex-kb drive --json-output` until it stops at each Phase-2 semantic boundary. This produces new packets under `runs/<run-id>/…` and an execution pack like the existing `phase2-execution-pack/`.

### R2 `[SEM]` — Hand the self-sufficient execution pack to your unlimited-token agent
Because of **P1**, each emitted packet is already complete — give it (`TASK.md`, `task.json`, `source-allowlist.json`, `output.schema.json`, `expected-output-path.txt`, plus the resolved source material) to the `apex-kb-operator` agent (AG1) in your unlimited chat. **The agent adds nothing — no paths, no files, no extra sources — it only drafts the richer dossier JSON into the declared output path.** Then `apex-kb drive` (DET) imports/validates. (Only if you explicitly opted into A4 do you also run its answerability check in a **separate fresh context**; it is not required.)
**Acceptance test:** diff old vs new `narm-model-and-core-needs.md` — ranked source #2 now carries all 9 pointers; key-claims ≥ the floor; a `## Related pages` section is present; `doctor` fresh; postflight honest. The external agent needed nothing beyond the packet.

---

*All implementation packets (B*, A*, C*, AG1, R1) are deterministic and token-free to run. Only R2 (and, if chosen, A4's acceptance pass) is semantic — route those to the unlimited-token agent. The CLI (①) remains sole authority throughout.*
