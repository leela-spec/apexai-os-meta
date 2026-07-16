You are designing a fix to the `apex-kb` skill at `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\`. This is a knowledge-base compiler skill. Do NOT write code — produce a design/plan. Read the files named below before designing.

## The incident that motivates this

An executor was asked to build/extend a KB for the "Leela" app. It misread the request and locked the topic as "Dealer App" (a subject that does not exist anywhere in the local material). It never confirmed that interpretation with the operator. It then registered 1,084 files as sources, ran the full deterministic Phase 0 corpus pass, committed and pushed artifacts — ~22 minutes and a large token budget — before "discovering" a self-created blocker (a literal search for "dealer" returned nothing). No semantic analysis or wiki pages were produced. The operator's verdict: the real failure was that the opening intent-capture Q&A did not rigorously establish and CONFIRM what the operator actually wanted, what the KB is about, and which process/mode fits — and there was no explicit approval gate before expensive work.

## What already exists in the skill (read these)

- `SKILL.md` — contains: (1) an "Execution-surface router" (asks ONE question: can the executor run Python in a live worktree → terminal_backed vs connector_only vs unsupported); (2) a "capability_precheck" YAML (terminal/python/git/evaluator supported?); (3) "Step 0 — Topic interview" which says to ask "which important questions future AIs must answer" and lock query IDs + vocabulary (phrases/aliases/supporting_terms/negative_terms/ambiguous_terms) in `manifests/topic-registry.json`; (4) a just-added "Step 0.5 — Topic-scope sanity check"; (5) an `owned_lifecycle` list containing an `operator_gate` step; (6) a "Failure behavior" YAML block including a new `topic_vocabulary_mismatches_kb_scope_evidence` entry.
- `references/semantic-value-contract.md` — "Topic registry v2" section (target_queries schema, vocabulary), truthful states (analysis_complete_unvalidated / partial / compiled_unvalidated / query_ready), output tiers, and a just-added "Topic-lock mismatch is not a source-access blocker" section.
- `references/script-command-contract.md` — table of deterministic CLI subcommands, including the just-added `topic-sanity-check`.
- `examples/powershell-commands.md` and `examples/lifecycle-runbook.md` — operator-facing command sequences.
- A deterministic CLI exists: `apex-meta/scripts/apex_kb.py`. It already has `cmd_topic_sanity_check` (a cheap read-only check: compares a topic's registry phrases/aliases against the KB root's own path components, sibling registry topics, and a bounded filename scan; excludes the KB's own generated output and kb-schema/README as circular; a single generic word never counts). It is generic — nothing subject-specific is hardcoded.

## The operator's framing of the real fix (design to THIS)

The skill needs a well-organized front-end with three things it currently lacks as a coherent, enforced unit: **(1) intent capture via Q&A, (2) mode/process selection, (3) target lockdown + explicit operator approval before any expensive/irreversible step.** The Q&A must be GENERIC — it elicits from the operator what THIS KB is about and what to look for; it must never hardcode a subject, app name, or wording. Every KB has a different subject, so the intake must be conversational and operator-validated, not pattern-matched. The topic-sanity-check should be re-anchored as a _validation input to the operator approval read-back_, not the primary safeguard — the primary safeguard is the operator confirming the read-back.

## Design requirements

1. A structured but lightweight **intake protocol** that runs before scaffold/source-intake/Phase 0 on every run (new KB or extending one). Define the required "slots" it must fill from operator answers (candidates: operator intent / job-to-be-done; KB identity — one-line "this KB is about X"; where the real source material lives + what's out of scope; success definition / what query_ready means here; output tier; execution route; corpus breadth default = narrow). Keep it generic and non-bureaucratic — guard hard against overengineering; the operator hates bloat.
2. A first-class, operator-confirmed **intent-record artifact** (propose path + minimal schema; consider folding into an existing `log/run-profile.md` that executors already create ad hoc, vs a new `manifests/run-intent.md`). It must carry an explicit `operator_confirmed` signal and the operator's confirmation, and must be auditable.
3. An explicit **target-lockdown read-back + approval gate**: the skill reads its whole understanding back to the operator in one compact summary and requires an explicit yes before any scaffold/intake/Phase 0. Design how this is enforced on BOTH the terminal_backed route AND the connector_only route (no Python on connector route).
4. Show how the existing pieces fold in without duplication: execution-surface router, capability_precheck, Step 0 topic interview, the `operator_gate` lifecycle step, and `topic-sanity-check` (re-anchored). Prefer restructuring/renaming existing sections over bolting on parallel ones.
5. Anti-hardcoding: state explicitly how the design guarantees no subject/app-specific literal ever enters the skill or scripts.

## Deliverable

A concrete design: the intake protocol steps and required slots; the intent-record artifact path + schema + confirmation field; exactly where in `SKILL.md` sections are added/restructured (name them) and what each says at a high level; how the approval gate is worded and enforced per route; how topic-sanity-check is repositioned; and a short "what we explicitly do NOT do (overengineering guard)" list. Name the specific files to edit. Do not write final prose or code — outline what each change contains.

I have enough to produce the design. Returning it directly (not writing a report file), per the task instructions.

---

# Design: Intake / mode-selection / target-lockdown front-end for `apex-kb`

## 1. Root cause the design fixes

The incident happened because the skill's front-end (execution-surface router → capability_precheck → Step 0 topic interview → Step 0.5 sanity check) is a sequence of _independent_ checks with **no single point where the executor's whole understanding is confirmed by the operator before expensive/irreversible work**. Step 0 "locks" a topic from a possibly-misread request; nothing forces that lock to be read back and approved; `source_intake`/`phase0`/commit can all run before anyone notices the topic is wrong. The fix is to weld the three missing things — **intent capture, mode selection, target lockdown + explicit approval** — into one enforced gate that owns everything before `scaffold --allow-write`.

## 2. Intake protocol — steps and required slots

A single conversational pass (not a form). The executor may fill every slot from one operator message; it only asks follow-ups for slots left genuinely unresolved. Runs on **every** run — new KB or extending one.

Required slots (each stored verbatim-ish in the intent record):

|Slot|What it captures|Default / source|
|---|---|---|
|`mode`|new KB vs extending an existing KB|asked / inferred, confirmed|
|`operator_intent`|job-to-be-done, in the operator's words|operator answer|
|`kb_identity`|one line: "this KB is about X"|operator answer, echoed back|
|`source_locus`|where the real material lives + what is explicitly out of scope|operator answer|
|`success_definition`|what `query_ready` (or the chosen tier) means _for this KB_|operator answer|
|`output_tier`|one of the existing `output_tiers`|operator choice|
|`execution_route`|terminal_backed / connector_only / unsupported|**reuses the existing Execution-surface router + `capability_precheck`** — not a new question|
|`corpus_breadth`|narrow (default) or broad|**default narrow**; broad requires a recorded reason|
|`topic_slugs`|the registry topics this run will build|from Step 0 topic interview|

Slots are described in SKILL.md **by role only** — no example subject, app name, or wording ever appears.

## 3. Intent-record artifact

**Recommendation: one first-class artifact at `manifests/run-intent.md`**, and **fold the ad-hoc `log/run-profile.md` into it** (delete the `log/run-profile.md` reference in SKILL.md line 214 — the broad-corpus reason moves into `broad_breadth_reason`). `manifests/` is canonical/auditable; `log/` is ephemeral. One artifact, not two.

Minimal YAML-frontmatter schema (markdown body optional for narrative):

```
run_id:kb_root:kb_slug:mode: new_kb | extend_kboperator_intent:kb_identity:            # "this KB is about X"source_locus:out_of_scope:success_definition:output_tier:execution_route:corpus_breadth: narrow            # defaultbroad_breadth_reason:             # required only when broadtopic_slugs: []topic_sanity_check:               # validation input, per topic  <topic-slug>: { verdict: scope_evidence_found|scope_evidence_absent, recommendation: , source: terminal|manual }operator_confirmed: false         # flips true only after read-back approvaloperator_confirmation_quote:      # the operator's actual affirmative, verbatimconfirmed_at:
```

`operator_confirmed: true` **plus** a non-empty `operator_confirmation_quote` is the only signal downstream steps accept. Absent/`false` ⇒ scaffold-write/intake/phase0 must not run.

**Connector-route path exception:** the connector route currently prohibits manifest writes. `run-intent.md` is operator-authored markdown, not a machine-maintained manifest, so add a one-sentence carve-out allowing it as a complete whole-file write on the connector route (same latitude the route already grants `log/semantic-runs/.../*.json`). This keeps a single canonical path rather than forking to a `log/` copy.

## 4. Target-lockdown read-back + approval gate

After slots are filled and Step 0 topic interview + topic-sanity-check have run, the executor emits **one compact read-back** (≈8 lines) summarizing: kb_identity, mode, source_locus + out_of_scope, output_tier, execution_route, corpus_breadth, the topic_slugs, and **the topic-sanity-check verdict per topic**. It ends with an explicit ask: "Reply to confirm before I scaffold / intake sources / run Phase 0."

Enforcement per route:

- **terminal_backed:** hard precondition. `topic-sanity-check` (read-only) is run and its verdict embedded in the read-back. No `scaffold --allow-write`, `source-intake`, or `phase0 --allow-write` executes until `run-intent.md` carries `operator_confirmed: true`. If the sanity verdict is `scope_evidence_absent`, the read-back must surface it prominently, but the **gate is the operator's confirmation**, not the verdict.
- **connector_only:** no Python, so the read-back is authored in chat, `topic-sanity-check`'s **manual equivalent** is performed (registry strong terms vs KB path + sibling topics + light filename sample, excluding self-authored `kb-schema.md`/`README.md`), and the verdict is recorded in `run-intent.md` (whole-file write). Same rule: no source selection / Phase-1 writing until the operator confirms in chat and the record shows `operator_confirmed: true`.

Confirmation is a plain affirmative recorded verbatim — deliberately **no new approval-phrase machinery** (the existing `approve ingest` phrase stays scoped to the Phase 2 gate; this intake gate is distinct and earlier).

## 5. How existing pieces fold in (restructure, don't bolt on)

- **Execution-surface router** (SKILL.md §"Execution-surface router") — kept; add one sentence stating its answer is the `execution_route` slot of the intake record. No new question.
- **`capability_precheck`** (§"Capability precheck…") — kept; referenced as the mechanism that fills `execution_route`/route feasibility. Not duplicated.
- **Procedure › Step 0 topic interview + Step 0.5 sanity check** — **restructured into one "Step 0 — Intake and intent lock"** with sub-steps: 0a intake Q&A (slots) → 0b topic interview (existing content, unchanged intent) → 0c `topic-sanity-check` **repositioned as a validation input to the read-back** → 0d read-back + approval gate that writes `run-intent.md`. The old Step 0.5 stop-behavior text is retained but re-anchored: mismatch is _surfaced in the read-back_, and the operator's confirmation is the primary safeguard.
- **`owned_lifecycle`** (SKILL.md §"Operating contract") — prepend two entries `intake_and_intent_lock` and `operator_intent_gate` **before** `scaffold`; **rename the existing `operator_gate` → `operator_phase2_gate`** so the two gates (early intent gate vs Phase 2 wiki gate) are unambiguous.
- **`topic-sanity-check`** — repositioned everywhere from "the primary Step 0.5 safeguard" to "a read-only validation input that pre-populates the read-back." Its `scope_evidence_absent` verdict no longer stands alone as the gate; it flags the read-back. Update the `topic_vocabulary_mismatches_kb_scope_evidence` failure entry and the semantic-value-contract "Topic-lock mismatch…" section to say the operator read-back approval is the enforcement point, with sanity-check as its input.

## 6. Anti-hardcoding guarantees

- Every slot value originates from operator answers at runtime and lives in `run-intent.md` (data), never in SKILL.md or the script (instructions).
- SKILL.md describes slots and the read-back **by role**, using placeholders (`<kb_identity>`, `<topic-slug>`) only — no example subject/app names in normative text.
- `topic-sanity-check` is already generic (compares registry-supplied terms to the KB's _own_ path/siblings/filenames, excludes self-authored output, a single generic word never counts) — confirmed at `apex_kb.py:683-849`. No subject literal is added.
- The gate keys on the presence of `operator_confirmed`/`operator_confirmation_quote`, never on matching any particular string.

## 7. What we explicitly do NOT do (overengineering guard)

- No new script or CLI subcommand — reuse `topic-sanity-check` and existing scaffold/intake/phase0.
- No multi-screen questionnaire; one conversational pass, all slots fillable from a single operator message.
- No second artifact — `log/run-profile.md` is folded into `manifests/run-intent.md`, not kept alongside it.
- No approval-phrase enum or new gate DSL; a plain affirmative, recorded verbatim.
- No gating of read-only work — `query`, `retrieve`, `lint`, `audit`, `status`, `health` on an already-confirmed KB do not re-trigger intake.
- No re-running the gate on every command within a run once `operator_confirmed: true` for that `run_id`.
- No blocking on `supporting`-priority ambiguity or on a lone weak `supporting_term`.
- No auto-widening to full-corpus "to see" — breadth stays narrow unless `broad_breadth_reason` is recorded and confirmed.

## 8. Files to edit

- `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\SKILL.md` — restructure Procedure Step 0/0.5 into "Step 0 — Intake and intent lock"; add `intake_and_intent_lock` + `operator_intent_gate` to `owned_lifecycle` and rename `operator_gate`→`operator_phase2_gate`; add `manifests/run-intent.md` to `canonical_paths`; remove the `log/run-profile.md` reference; re-anchor the `topic_vocabulary_mismatches_kb_scope_evidence` failure entry; add one connector-route carve-out sentence for `run-intent.md`.
- `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\semantic-value-contract.md` — reposition the "Topic-lock mismatch is not a source-access blocker" section (sanity-check = input to read-back; approval = enforcement); add the `run-intent.md` schema near "Topic registry v2".
- `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\script-command-contract.md` — update the `topic-sanity-check` row to state its verdict feeds the operator read-back, not a standalone stop.
- `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\examples\powershell-commands.md` — insert the read-back/approval step and `run-intent.md` write ahead of scaffold-write/intake/phase0.
- `C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\examples\lifecycle-runbook.md` — extend "A. Prepare" with the intake pass, read-back, and gate.

### Critical Files for Implementation

- `C:\GitDev\apexai-os-meta.claude\skills\apex-kb\SKILL.md`
- `C:\GitDev\apexai-os-meta.claude\skills\apex-kb\references\semantic-value-contract.md`
- `C:\GitDev\apexai-os-meta.claude\skills\apex-kb\references\script-command-contract.md`
- `C:\GitDev\apexai-os-meta.claude\skills\apex-kb\examples\lifecycle-runbook.md`
- `C:\GitDev\apexai-os-meta.claude\skills\apex-kb\examples\powershell-commands.md`

Note on scope: no code changes are required — `apex_kb.py`'s `cmd_topic_sanity_check` (lines 683–849) is already generic and read-only and needs no modification; the fix is entirely doctrine/restructuring plus one new operator-authored artifact.