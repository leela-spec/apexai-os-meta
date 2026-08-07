# FEE — Upstream Change Gate Batch (DRAFT)

```yaml
status: "items 1 and 3 approved and applied 2026-08-07; items 2/4/5/6 unchanged"
authority:
  state: candidate
  operator_validation: partially_requested
scope: "six additive changes to files FEE does not own"
rule: "each item is independently approvable; none is applied as part of implementation"
```

Every item below is **additive**. None removes or rewrites an existing rule. Each is listed with what it unblocks, so partial approval is meaningful.

---

## Item 1 — Prompt-body location (BLOCKS live execution) — **APPROVED AND APPLIED 2026-08-07**

**Target:** `.claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md` (+ the agent wrapper's output note)

**Problem it fixes.** `flow_prompt_pack` carries only `final_copy_paste_prompt_ref`, a bare string, and the body schema is owned by PromptEngineer. No on-disk location for a materialized body is defined anywhere. Per finding **F2**, zero bodies exist under `artifacts/` and no `prompt-packs/` directory has ever been written. M1's core job — resolve every `*_ref` to concrete content — has no target.

**Change.** Define the body location:

```
artifacts/flow-packets/<YYYYMMDD>/prompt-packs/bodies/<packet_id>.md
```

- One file per prompt packet. Body content only, honouring the existing `copy_boundary: copy_prompt_body_only` and `metadata_outside_prompt_body: true` rules.
- `PrecapNextDay.output_requirements.filesystem_write_required` stays `false` for the *pack*; this adds an optional-but-required-for-FEE body write.
- FEE behaviour when absent: write `unresolved-refs.md`, exit 3, **no silent default** — identical posture to the existing `provider_unspecified → HALT` rule.

**Unblocks:** live execution of any non-skipped flow. **Does not block:** the skip path, the validator paths, or the capture loop.

**Reversal trigger:** PrecapNextDay adopts a different body-materialization mechanism.

**Applied.** `flow-prompt-pack-contract.md` gained a `prompt_body_materialization` section (additive) plus a `note` on `prompt_packet_reference.prompt_packet_path_or_slot`; `.claude/agents/apex-precap-next-day.md`'s Output list gained the body-path line. M1 can now be implemented against a real target.

---

## Item 2 — Local adjudication surface class (only if M5 is ever built)

**Target:** `.claude/skills/AIRouting/references/AI-surface-inventory-contract.md`

**Change.** Add the surface class exactly as drafted in `02-meso-module-design.md` D-S3 — `local_adjudication_surface`, `cost_class: zero_marginal_cost`, `forbidden_uses: [primary_flow_reasoning, review_lens, prompt_authoring, routing_decision]`.

**Status: deferred, not requested.** M5 is deferred by operator decision (plan §4 B3). This item is queued only so the dependency is visible; **do not approve it now** — approving a surface class for a module that does not exist is drift.

**Unblocks:** nothing currently planned.

---

## Item 3 — FEE as a permitted step-4 actor — **APPROVED AND APPLIED 2026-08-07**

**Target:** `.claude/skills/weekly-orchestrator/SKILL.md:32`

**Current (live authority, per finding F1):**
```yaml
operator_execution: {agent: none_operator_human_step, gate: G3, trigger: "operator returns evidence or skip signal"}
```

**Change.** One line. The actor may be FEE; **G3 is unchanged and stays `required: always`**:
```yaml
operator_execution: {agent: none_operator_human_step_or_fee, gate: G3, trigger: "operator returns evidence or skip signal"}
```

**What this does not do.** It does not automate G3, does not change the trigger, does not change what step 5 receives, and does not make FEE an orchestration system. D-M7 stands: FEE changes who *performs* step 4, never who *approves* it.

**Unblocks:** FEE running as a sanctioned actor rather than an undeclared one.

**Applied.** `weekly-orchestrator/SKILL.md:32` now reads `agent: none_operator_human_step_or_fee`; `gate: G3` and its trigger are unchanged.

---

## Item 4 — Record FEE as an execution substrate, not a third system

**Target:** `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md` + `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`

**Change.** Record FEE as an **execution substrate for step 4 of the Weekly Orchestrator** — explicitly *not* a peer orchestration system, and **not** added to the index as one.

**Why it matters more than it looks.** Per finding **B9**, `"orchestration system"` has no standalone glossary entry; it is defined only inside **APEX OS** as *"two separate orchestration systems — Weekly Orchestrator and Multi-Agent Orchestration."* The boundary D-M0 protects is itself informally defined, which makes the explicit disclaimer load-bearing rather than ceremonial.

**Unblocks:** honest documentation. No code depends on it.

---

## Item 5 — Four candidate glossary entries

**Target:** `apex-meta/GLOSSARY.md` and/or `apex-meta/orchestration/GLOSSARY.md`

**Change.** Add **flow**, **sprint**, **surface class**, **capture** — the four terms FEE depends on most, none of which has an entry in either glossary today. They exist only schematically inside contracts.

Per the glossary's own change rule, each enters as `candidate` and becomes canonical only after Detective review + operator confirmation. Proposed definitions should be lifted from the owning contracts rather than invented:

| Term | Source of truth |
|---|---|
| flow | `PrecapNextDay/references/flow-packet-contract.md` (F1–F4 fixed daily flows) |
| sprint | same (`sprint_policy`, `sprint_count` 0–3, `flow_sprint_block`) |
| surface class | `AIRouting/SKILL.md` `surface_class_policy.abstract_surface_classes` |
| capture | gate `G3 (capture)`; `canonical_capture_home: raw_flow_dump \| FlowRecap` |

**Unblocks:** nothing. Low priority, real.

---

## Item 6 — WITHDRAWN (D-I2 amendment not needed)

A sixth item was drafted to narrow D-I2's stdlib-only rule and permit PyYAML in M1. **It is withdrawn.**

Evidence that settled it: `scripts/orchestration_check.py`, the repo's live validator for this artifact family, parses these files with `re` + `json` + `pathlib` and no YAML parser at all; PyYAML/jsonschema/pytest are absent from this environment; and a construct scan of every input artifact found **zero** block scalars, anchors, or non-empty flow collections. See corrected finding **F5** in `05-preflight-findings.md`.

**D-I2 stands as locked. No gate is required to begin Phase 1.**

---

## Recommended approval order

| Order | Item | Blocks |
|---|---|---|
| 1 | **3** (FEE as step-4 actor) | sanctioned operation |
| 2 | **1** (prompt-body path) | live execution of non-skipped flows |
| 3 | **4**, **5** (documentation, glossary) | nothing |
| — | **2** (surface class) | **do not approve — M5 is deferred** |
| — | **6** | **withdrawn — not needed** |

**Nothing in this batch blocks the start of Phase 1.** The skip path (F4), the validator/halt paths (F6), and the capture loop all run against real artifacts today with no gate and no install.

**Not proposed, deliberately:** any change to `handoff-schema.md`, the seven other stage agents, downstream skills, `apex-plan`/`apex-sync`/`apex-session`, the review wiring, or any gate definition. Also not proposed: adding `Perplexity` to the `provider_target` enum (plan §4 B10 — deferred), and any numeric spend ceiling (plan §4 B12 — the subscription path has no metered spend to cap).
