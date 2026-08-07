---
title: "Flow Execution Engine — Decision Ledger"
purpose: >
  Every FEE architecture decision in one scannable table: options considered, ranking, the single
  criterion that decided it, and what would reverse it. Plus the cross-cutting risk register and
  the strength-materialization analysis.
created: 2026-07-28
status: "proposal — candidate"
reads_with: [01-macro-architecture-decision.md, 02-meso-module-design.md, 03-micro-implementation-map.md]
---

# Flow Execution Engine — Decision Ledger

Rankings are `1` = chosen. "Reversal trigger" is the specific observation that should reopen the
decision — recorded so a future session can challenge a choice on evidence rather than re-litigate it
on taste.

## Macro decisions

| ID | Decision | Options (ranked) | Deciding criterion | Reversal trigger |
|---|---|---|---|---|
| D-M0 | System name | 1 Flow Execution Engine · 2 keep "local orchestration engine" | GLOSSARY pins "orchestration system" to two; a third would be term-drift | Operator prefers the folder name as canonical |
| D-M1 | AI tier allocation | 1 scarcity-asymmetry · 2 local-first · 3 Claude-Code-first · 4 API-first | Repo already forbids API-as-daily-engine and treats subscription cost as non-binding | Subscription flat-rate pricing ends |
| D-M2 | What combines | 1 step-4 attach only · 2 full runtime replacement · 3 parallel track | Seven of eight stages are locked and dry-run-verified; only step 4 has a human actor | A locked stage fails in practice |
| D-M3 | Workflow language | 1 consume `flow_prompt_pack` · 2 new DSL · 3 LangGraph/Temporal · 4 LLM improvises | The pack already contains provider + ordered prompts + capture hints — it *is* the work order | `flow_prompt_pack` proves insufficient for a real flow |
| D-M4 | Control flow | 1 deterministic + typed LLM edges · 2 LLM agent loop · 3 pure determinism · 4 Claude Code driver | Mechanism ladder: don't escalate without demonstrated need | Completion detection proves unsolvable without a loop |
| D-M5 | Local LLM scope | 1 toolless adjudicator/narrator · 2 narrow tool allowlist · 3 full agent | Toolless is strictly stronger at zero cost | — (no upside identified) |
| D-M6 | Trust boundary | 1 frozen plan + quarantine · 2 injection filtering · 3 sandbox-only containment | Structural impossibility beats probabilistic detection | — (containment ≠ integrity, unchanged) |
| D-M7 | G3 gate | 1 unchanged human gate · 2 auto-pass on high confidence | `handoff-schema.md` `required: always`; only human checkpoint before canon | Operator explicitly re-authorizes after V9 evidence |
| D-M8 | Multi-Agent link | 1 inert handoff packet only · 2 FEE invokes it · 3 no link | Repo law: no automatic cross-activation, full stop | — (law, not preference) |
| D-M9 | Worker platform | 1 Odysseus AI as *executor* · 2 OpenClaw (unknown) · 3 Hermes as notifier · 4 Odysseus as *orchestrator* | Odysseus's agent loop is the rejected D-M4 shape; its container + local backends are genuinely good | Q1 research shows OpenClaw already does this |

## Meso decisions

| ID | Decision | Options (ranked) | Deciding criterion | Reversal trigger |
|---|---|---|---|---|
| D-S1 | Compile phase | 1 separate + frozen · 2 lazy per sprint · 3 none | Enumerable action set before network contact | — |
| D-S2 | Surface indirection | 1 broker · 2 self-registering adapters · 3 hard-coded | Pacing must be global per account, not per adapter | — |
| D-S3 | Local surface class | 1 add `local_adjudication_surface` (additive) · 2 reuse `provider_unspecified` · 3 no class | Honest routing + `forbidden_uses` encodes D-M5 in contract | `AIRouting` owner rejects the addition |
| D-S4 | Browser channels | 1 split by risk bucket · 2 uniform Playwright · 3 private HTTP endpoints | Real ToS asymmetry; concentrate effort where risk exists | Claude's sanctioned channel is withdrawn |
| D-S5 | Local model size | 1 7–8B structured · 2 13–14B · 3 27–32B (`whichllm` pick) · 4 platform default | Shared 32GB pool: a big model competes with the browser fleet for capability M5 never uses | Narration quality measurably fails at 7–8B |
| D-S6 | Turn granularity | 1 per-turn atomic · 2 per-sprint · 3 per-flow | A browser turn is the real cost + quota unit | — |
| D-S7 | Ledger format | 1 append-only JSONL · 2 SQLite · 3 mutable JSON | Crash-safety with the simplest mechanism; greppable; small | Run volume outgrows flat files |
| D-S8 | Output shape | 1 dump-shaped bundle · 2 freeform notes · 3 finished dump (skip step 5) | Engine has the structure for free; step 5 owns `normalized_raw_flow_dump` | — (ownership, not preference) |
| D-S9 | Concurrency | 1 serial/account + parallel across · 2 full parallel · 3 permanent serial · 4 per-sprint parallel | Per-account serialization is the cheapest, strongest detection-avoidance measure | Memory or ban evidence forces tighter caps |
| D-S10 | Token discipline | 1 bodies on disk, refs only · 2 inline into envelopes | Keeps expensive reasoning output out of metered contexts entirely | — |

## Micro decisions

| ID | Decision | Options (ranked) | Deciding criterion | Reversal trigger |
|---|---|---|---|---|
| D-I1 | Code location | 1 `scripts/fee/` · 2 separate repo · 3 `.claude/` | Beside `apex_sync.py`; `.claude/` implies Claude-Code semantics FEE lacks | FEE used outside APEX OS |
| D-I2 | Dependencies | 1 M1/M6/M8 stdlib-only, deps confined to M3/M5 · 2 deps anywhere | Plan, ledger, and output stay auditable and unbreakable by dep failure | — |
| D-I3 | Dry-run default | 1 default true · 2 opt-in flag · 3 none | Matches `apex_sync.py --dry-run false`; free session pre-flight | — |
| D-I4 | Write surface | 1 `execution/` inside `flow-packets/<day>/` · 2 new top-level family | Live write-permission matrix allows own-family writes | — |
| D-I5 | Build order | 1 compile → adjudicator → 1 low-risk adapter → emit → live · 2 vertical slice first | V3 injection test must pass before any real untrusted text exists | — |

---

## Cross-cutting risk register

| Risk | Severity | Likelihood | Control | Residual |
|---|---|---|---|---|
| Prompt injection from captured content reaching execution | **critical** | moderate (adversarial content is common on the open web) | D-M6 frozen plan + quarantine; V3 permanent fixture; M5 has no action fields | Low — structurally closed, not filtered |
| Account suspension (ChatGPT/Gemini) | high | real, accepted by operator (Q4) | D-S4 risk buckets; D-S9 per-account serialization; M9 `account_flagged` halts and never retries | Accepted. Blast radius limited to one provider lane |
| Account suspension (Claude) | high | low | D-S4 sanctioned channel | Low |
| Plausible-but-wrong engine narrative reaching canon | high | moderate | D-M7 G3 intact; `authority.state: candidate`; step 5 independent normalization; existing dual-lens review downstream | Low — four independent checks |
| Web UI change breaking adapters | medium | **high** (certain over time) | D-S4 (sanctioned channel immune for Claude); adapter interface isolates breakage to one file; M9 degrades per provider | Moderate. Ongoing maintenance cost — accept explicitly |
| Local model misclassification | medium | moderate | M5 heuristic fallback → `confidence: low` → `operator_review_recommended: true` | Low — downstream contract already handles it |
| Memory exhaustion (model + browsers on one 32GB pool) | medium | moderate | D-S5 small model; D-S9 browser cap 2–3 | Low |
| Silent scope creep into a third orchestration system | medium | moderate (organizational, not technical) | D-M0 naming; D-M8 inert bridge; §5 of micro map caps changes at three files | Moderate — needs discipline, not code |
| Engine claims success on a failed flow | high | low | `completion_state` is evidence-derived, never engine-asserted; M5 forbidden from deciding completion | Low |

---

## Where this materializes existing strengths

The user's brief asked for a "strength-materializing" architecture. Named explicitly, because these
are the reasons the design is cheap rather than merely correct:

1. **`flow_prompt_pack` was already an executable work order.** The single largest finding. Provider
   targets, copy-paste-ready bodies, sprint ordering, bounded follow-ups, and capture hints already
   exist in machine-readable form. FEE needs **zero** new workflow language — the hardest part of this
   system was built months ago for a human executor and works unchanged for a machine one.

2. **`AIRouting`'s abstract surface classes were built for exactly this.**
   `stable_surface_classes_only`, `final_model_mapping_status: todo_later`, and the
   `subscription_frontier_*` / `deep_research_surface` / `code_agent_surface` taxonomy are precisely
   the indirection a multi-provider executor needs. One additive class is the entire delta.

3. **The locked trace already had a human-shaped hole.** Step 4 is the only stage whose actor is
   `operator (human)`. The architecture didn't need a seam carved into it — it shipped with one.

4. **`raw-flow-dump-normalize` was designed for messy heterogeneous input.** "Chat fragments,
   artifact references" are named source types. Machine output is *easier* for it than human notes,
   and `model_usage_notes` is a field the engine fills better than a human ever could.

5. **Files-as-state was already invariant #1.** FEE's resumability requirement is the repo's existing
   doctrine, so the ledger needed no new philosophy — only a new file.

6. **The mechanism ladder already forbade over-engineering.** "Escalate only when the lower rung
   demonstrably cannot carry the work" is what makes the deterministic-first design (D-M4)
   *native* rather than a preference imposed from outside.

7. **`apex_sync.py` set the deterministic-compute precedent.** Stdlib-only, dry-run-first, `--json`.
   FEE's CLI inherits a convention the operator already knows.

8. **Gate and authority fields already exist.** `operator_validation`, `authority.state`,
   `lifecycle_stage`, `basis_digest` — FEE needs no new permission model, only correct use of the one
   in place.

---

## The three genuine tensions this design does not paper over

1. **ToS risk is real and accepted, not solved.** D-S4 and D-S9 reduce it materially and confine its
   blast radius, but automating ChatGPT/Gemini web UIs remains outside consumer terms. The design's
   honest position: concentrate the risk in the *replaceable* providers, keep the operator's most
   important provider (Claude) on a sanctioned path, and never retry after a flag.

2. **Adapter maintenance is a permanent tax.** Web UIs change. The Claude lane is insulated by the
   sanctioned channel; the others will break periodically. This is accepted operating cost, not a
   defect — but it should be budgeted for, not discovered.

3. **A different-family review judge is now newly affordable, and deliberately not taken.**
   `ARCHITECTURE.md` §4 records that both review lenses are Claude-family and names a different-family
   judge as the escalation path, ruled out in July 2026 on "no external calls." FEE's adapters would
   make it cheap. It is still the wrong first move: the review path is APEX OS's most
   safety-critical surface and the last place to introduce a fragile, injection-exposed component.
   Precondition for revisiting: operator re-authorization **plus** a simulation showing the
   Claude-family limitation actually biting.
