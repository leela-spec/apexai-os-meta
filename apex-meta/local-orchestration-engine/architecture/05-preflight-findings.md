# FEE — Phase 0 Pre-flight Findings

```yaml
status: "findings — executed 2026-07-30 against the live repo"
authority:
  state: candidate
  basis: "real reads of live artifacts and contracts; no file outside this package written"
supersedes: nothing
amends:
  - "01-macro-architecture-decision.md — trace authority citation (F1)"
  - "03-micro-implementation-map.md — pack path resolution (F3), D-I2 scope (F5)"
```

Executed per the evidence standard the Weekly Orchestrator package sets for itself: actual attempt, actual result, honest verdict. Every claim below is a real read, not a walkthrough.

---

## F1 · Step-trace authority — RESOLVED, favorably

**Finding.** The live contract for step 4 is **`.claude/skills/weekly-orchestrator/SKILL.md:32`**:

```yaml
operator_execution: {agent: none_operator_human_step, gate: G3, trigger: "operator returns evidence or skip signal"}
```

`apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md` does self-mark as historical, but its disclaimer is **scoped**: it describes *"the 2026-07-11/12 configuration in which weekly routing absorbed Plan/Sync wrappers and a main-thread state write."* Step 4 involves none of Plan, Sync, Session, or a state write. Its row is unaffected, and it agrees with the live contract.

**Consequence.** The step-4 seam is safe to build on. **Cite `weekly-orchestrator/SKILL.md:32` as authority, not the trace file.** All four FEE architecture files should have their "the locked trace" citations updated. This is also precisely the field the §7 gate batch amends (`agent: none_operator_human_step` → actor may be FEE, G3 unchanged).

---

## F2 · No prompt body exists anywhere as live data — the §3 blocker, confirmed harder than stated

**Finding.** A repo-wide search for `prompt_body|final_copy_paste_prompt` (excluding vendored `source-knowledge/`) returns **91 files, of which zero are under `artifacts/`.** Every hit is a contract, template, skill reference, or archived version.

`artifacts/flow-packets/` contains, in total:

```
.gitkeep
20260713/flow_packet-20260713-F1.md
20260713/flow_packet-20260713-F3.md
20260713/normalized-raw-flow-dump-F3.md
```

**There is no `prompt-packs/` directory anywhere under `artifacts/`.** It has never been written.

**Consequence.** The plan's §3 blocker is real and total. M1 has no bodies to resolve and no pack to resolve them from. Gate-batch item 1 remains the Phase 1 blocker.

---

## F3 · The live flow packet declares its own pack path — follow the ref, don't construct it

**Finding.** `artifacts/flow-packets/20260713/flow_packet-20260713-F1.md:85-89`:

```yaml
prompt_pack_ref:
  flow_prompt_pack_path: artifacts/flow-packets/20260713/prompt-packs/flow_prompt_pack-20260713-F1.md
  prompt_pack_status: not_needed_for_skipped_flow
  prompt_pack_authority: references/flow-prompt-pack-contract.md
```

The live convention is `prompt-packs/flow_prompt_pack-<YYYYMMDD>-<flow_id>.md`. The `apex-precap-next-day` agent wrapper describes `prompt-packs/<flow_id>.md`. **These disagree.**

**Consequence — resolves the discrepancy at zero cost.** M1 must resolve the pack by **reading `flow_packet.prompt_pack_ref.flow_prompt_pack_path`**, never by constructing a path from convention. The packet tells you where its pack is; believe it. This is strictly more robust than either convention and makes the disagreement moot.

M1 must also honour `prompt_pack_status` — `not_needed_for_skipped_flow` is a valid, non-error state.

---

## F4 · The skip path is a complete vertical slice available today — and it is D-I5-compatible

**Finding.** The only live flow packets are a **planned skip** and an **already-normalized flow**:

| Packet | State |
|---|---|
| `flow_packet-20260713-F1.md` | `flow_status: skipped` · `sprint_policy: skipped` · `sprint_count: 0` · `sprints: []` · `prompt_pack_status: not_needed_for_skipped_flow` |
| `flow_packet-20260713-F3.md` | already has `normalized-raw-flow-dump-F3.md` |

F1 carries a **filled `skipped_flow_marker_template`** inline (`marker_id`, `flow_id`, `execution_day`, `skip_status: planned_skip`, `skip_reason`, `carry_forward_policy`, `next_review_point`) and a `FlowRecap_handoff_block` with `skipped_flow_marker_allowed: true`, `required_operator_completion_marker: skipped`.

**Consequence.** FEE's first real end-to-end run should be the **skip path**, against real 20260713/F1 data: read packet → detect `flow_status: skipped` → emit `skipped_flow_marker` → hand to step 5. This exercises M1 → M6 → M8 completely with **zero network, zero browser, zero model, and no prompt bodies required.**

**This does not violate D-I5.** D-I5 rejected a *vertical slice first* on the criterion *"V3 injection test must pass before any real untrusted text exists."* The skip path involves **no captured content at all**, so no untrusted text exists to contain. The criterion is satisfied vacuously, not bypassed. M8's contract already anticipates this: `emits_instead_when_no_evidence: skipped_flow_marker`.

---

## F5 · D-I2 holds unamended — M1 stays stdlib-only

> **This finding was initially recorded backwards.** The first pass recommended amending D-I2 to permit PyYAML in M1, reasoning from `apex-kb-cli/pyproject.toml`'s declared dependencies. That was the wrong precedent: those dependencies are not installed here, and the tooling that actually reads these artifacts is deliberately stdlib-only. Corrected below. Gate-batch item 6 is **withdrawn**.

**Finding.** Live artifacts are **markdown documents containing fenced YAML blocks and pipe tables** — not YAML files.

- `flow_packet-20260713-F1.md` / `-F3.md` — **5 fenced YAML blocks each**, under markdown headings.
- `F1..F4-flow-prompt-pack.md` — **3 fenced YAML blocks each**, plus a markdown pipe table carrying the sprint sequences (`| Sprint | Sprint goal | Prompt packet ref/placeholders | Provider/surface hint | Capture hint |`).

**The repo already solves this stdlib-only.** `scripts/orchestration_check.py` — the live validator for this artifact family — imports exactly `argparse`, `hashlib`, `json`, `re`, `sys`, `pathlib`. No YAML parser. It does **targeted extraction**, not general parsing.

**Environment check (executed).** Store Python 3.12.10. `click 8.4.2` present. **PyYAML, jsonschema, and pytest all absent.** So the PyYAML path would require installing into Store Python's redirected `site-packages` — the hazard already flagged — to gain nothing the stdlib cannot do here.

**Construct scan (executed, then corrected by implementation).** The first scan covered four input artifacts plus the pack template and found zero block scalars, anchors, or non-empty flow collections. **That file set was too small.** Building the reader and running it over the full 55-file artifact/example/template family surfaced two constructs the scan had missed, both in `normalized-raw-flow-dump-F3.md`:

- a flow **sequence**: `source_refs: [artifacts/flow-packets/20260713/flow_packet-20260713-F3.md]`
- a flow **mapping**: `authority: {state: candidate, basis_digest: null, verification_ref: null}` — the standard inline authority block, the same shape as `weekly-orchestrator/SKILL.md:32`

Both are scalar-only and therefore unambiguous, so both were added to the subset; **nested** flow collections remain rejected. Neither file is an M1 input (the normalized dump is step-5 output), but the correction matters because the inline `authority` block can appear in any artifact.

**This is the safety property earning its place.** In both cases the reader raised `UnsupportedConstruct` naming file, line, and the offending token — it did not guess. A parser that had guessed would have silently mis-shaped an authority block.

**Decision. D-I2 stands as locked: M1, M6, and M8 are stdlib-only.** M1 gets a strict-subset block-YAML reader supporting exactly what these artifacts use — nested block maps, block sequences, empty flow sequences, bare and quoted scalars, `null`, booleans, comments, blank lines — plus a pipe-table reader.

The safety property that answers the hand-rolled-parser objection: **the reader raises `UnsupportedConstruct` on anything outside the subset rather than guessing.** A loud failure on an unexpected construct is honest; a silent misparse is not. That inverts the original objection — the risk of a subset parser is silent misreading, and an explicit allowlist eliminates exactly that.

**Implemented and measured** (`scripts/fee/artifacts.py`, stdlib-only, two-pass tokenize-then-build):

| Check | Result |
|---|---|
| Artifacts + examples + templates parsed | **53 / 55** |
| Remaining 2 failures | Template files with intentionally repeated top-level blocks (`raw-flow-dump-template.md`, `FlowRecap-handoff.md`). Correct behaviour — `load_artifact` refuses to silently overwrite a duplicate key. Neither is an M1 input; callers needing repeats use `extract_yaml_blocks` directly |
| Negative guards raising the right exception type | **13 / 13** — block scalars, folded scalars, anchors, aliases, nested flow seq/map, malformed flow mapping, tab indentation, bare-dash blocks, garbage lines, unterminated quotes, duplicate keys, seq-where-map-expected |
| Supported forms round-tripping | **16 / 16** — incl. quoted scalars containing `: ` and `,`, `#`-bearing paths (`../handoff/F.md#F1`), trailing-comment stripping, and sequences of mappings |

**Consequence: zero installs for Phases 1–4, and no gate needed to start.**

---

## F6 · The only existing pack would halt compile immediately — and that is correct

**Finding.** `.claude/skills/PrecapNextDay/examples/apex-only-template-example/prompts/F1-flow-prompt-pack.md` — one of the four example packs, and the closest thing to a real pack in the repo:

```yaml
generation_mode: degraded_generic_prompt_mode
pack_status: operator_review_recommended
validation_status: operator_review_recommended
```

All three sprints carry `provider_unspecified` as the provider hint, and all three prompt packet refs are literal placeholders (`placeholder_prompt_packet_F1_S1_repo_scan`). Its own review flag says so: *"Prompt packets are placeholders until prompt-engineering dependency is applied."*

**Consequence.** Against the only pack that exists, M1 would fire **three** of its halt/degrade rules at once:

| Rule | Fires |
|---|---|
| `primary_surface_class: provider_unspecified → HALT, ask operator` | yes, all sprints |
| `generation_mode: degraded_generic_prompt_mode → plan.confidence = low` | yes |
| `pack_status` review-recommended → `requires_pre_run_review = true` | yes |
| `unresolved_refs` (new, §3) | yes, all packets |

**This reorders Phase 1 verification honestly.** V1 (*"assert every ref resolves"*) **cannot pass against live data today** — no pack with resolvable refs exists, so V1 needs a synthetic fixture until PrecapNextDay produces a real pack. What **can** pass today, against real artifacts, is **V6** (`provider_unspecified` halt), the new **`unresolved_refs` halt**, and **V5** (degraded pack).

The halt paths are therefore the *common* case right now, not the edge case. Phase 1's stated standalone value — *"validates packs and surfaces routing gaps before any execution exists"* — turns out to be the only thing that runs against current data. **FEE's first delivered value is as a pack validator that tells the operator exactly why their packs are not yet executable.** The build order anticipated this correctly.

---

## Revised Phase 1 order

1. **Skip path, real data** (F4) — `plan` + `emit` against 20260713/F1 → `skipped_flow_marker`. Full M1→M6→M8 slice, no blockers.
2. **Validator / halt paths, real data** (F6) — V6 + `unresolved_refs` + V5 against the example pack.
3. **Fixture pack** — synthetic pack with resolvable refs so V1/V2 can assert hash stability.
4. **Capture loop** (plan B7) — `next` / `capture`, clipboard-driven.

**None of steps 1–4 needs an upstream gate, a dependency install, or a contract amendment.** Only live execution of a non-skipped flow needs gate-batch item 1.

---

## Gate batch, updated

**Plan §7 items 1–5 stand unchanged. Nothing added.** The D-I2 amendment floated in the first pass is withdrawn per corrected F5 — stdlib-only holds, so no gate is required to begin.

Queued as documentation corrections *inside this package* (no external gate — the package is `candidate` and untracked): update the four "locked trace" citations to `weekly-orchestrator/SKILL.md:32` per F1.

---

## Phase 0 status

| Item | Status |
|---|---|
| 0.1 Trace authority | **resolved** (F1) |
| 0.2 Volatile claims re-verification | **pending — gates Phase 5, not Phase 1** |
| 0.3 Live inputs + body existence | **resolved** (F2, F3, F4, F6) |
| 0.4 Gate batch draft | **in progress** — 6 items identified |
