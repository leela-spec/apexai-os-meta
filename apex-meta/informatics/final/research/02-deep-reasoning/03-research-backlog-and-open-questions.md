---
type: Reference
id: DR-RESEARCH-BACKLOG-v1.0
title: Informatics Research Backlog & Open Questions
description: Prioritized backlog of deeper research questions, empirical benchmark ideas, and deferred improvements surfaced during the Apex Informatics compression pass but deliberately kept outside its patch scope.
status: current
tags: [research, backlog, open-questions, benchmarks]
---

# Informatics Research Backlog & Open Questions

**Bottom line:** eight items deferred. `RBL-01` is the only one that could change the suite's
architecture; the rest are measurement, hygiene, or scope questions that do not block this pass.

Deferral is deliberate under `AD-18` (zero-speculation scope boundary) and `AD-13` (evidence
proportionality) — each item below is a real question, not a hedge, and none of them had to be
answered to apply the current patches safely.

---

## `RBL-01` — Does single-gate JIT isolation actually hold in production routing?

`[P1 | I90/E45/R25]`

- **Problem statement:** The entire dedup policy in [01](01-system-wide-overlap-and-token-audit.md)
  rests on the premise that an agent loads exactly one module per task. That premise is asserted by
  the router's design and *simulated* by `test_cis_01`–`cis_05`, which parse the gate attributes and
  check which module a synthetic task string resolves to. No measurement exists of what a real agent
  loads on a real multi-domain task.
- **Why it matters:** If real tasks routinely trip two or three gates — "write a new specification
  file" plausibly trips `writing_or_documentation` *and* `file_creation_or_structure` — then the
  retained `CROSS_LINK` rule restatements are not insurance but pure interference cost, and
  Option B in Q1 becomes correct after all.
- **Initial hypothesis:** Multi-gate activation is common for authoring tasks and rare for patch,
  drift, and schema tasks. If so, `WP` and `FA` could share more aggressively than `AD`, `EM`, `GS`.
- **Suggested method:** Instrument a set of ~30 representative operator task strings drawn from
  session history; record which gates each trips under the current attribute grammar. No model
  inference required — the gate conditions are string-matchable.
- **Linked rules:** `WP-23`, `WP-18`, `FA-03`, the `<informatics>` dispatch gates.

---

## `RBL-02` — Are the plane token orientations calibrated to 2026 practice?

`[P2 | I72/E60/R15]`

- **Problem statement:** `FA` §2 orients the Control Plane at ~2,000 tokens and Scoped Instructions
  at ~1,500. Current published convention for always-on agent instruction files is materially
  tighter — root `CLAUDE.md` under ~100 lines, some practitioners at 50–60, with `AGENTS.md` under
  ~150 ([A Complete Guide To AGENTS.md](https://www.aihero.dev/a-complete-guide-to-agents-md)).
- **Why it matters:** The orientations are what `WP-18` and `FA` use to decide when a file must be
  decomposed. If they are 2× loose, the suite will tolerate files that measurably degrade routing.
- **Initial hypothesis:** The ~2,000 figure is defensible for a *router that dispatches* (which does
  more work than a plain rules file) but loose for scoped rule files.
- **Why it was not changed in this pass:** Changing a numeric orientation on the strength of blog
  convention, with no repo-specific incident behind it, is cargo-culting — exactly what `WP-20`
  (no default-behavior rules) and `AD-25` (pre-addition gate) exist to prevent.
- **Suggested method:** Measure the repo's own always-on surfaces (`AGENTS.md`, `.claude/CLAUDE.md`,
  `.claude/rules/*.md`) against both figures; look for a dated incident where size caused a miss.
- **Linked rules:** `FA-12`, `WP-18`, `GS-14`, `AD-26`.

---

## `RBL-03` — Universal root-instruction consolidation of `WP-02` / `WP-03` / `WP-05`

`[P2 | I75/E55/R30]`

- **Problem statement:** `writing-profile.md` §5 currently carries a speculative note proposing that
  Single Command, Imperative Verbs, and Active Voice be collapsed into one ultra-compact P0
  directive *inside the always-on root surface only*, while remaining separate here.
- **Why it matters:** It is a real token-saving idea for the Control Plane, but it is roadmap
  content sitting inside a live specification, which `FA-01` (current-truth separation) forbids.
- **Resolution applied:** relocated here by this pass; the live note is removed.
- **Suggested method:** Draft the consolidated single directive, A/B it against the three separate
  rules on a prose-authoring task set, and measure whether the collapsed form loses any of the three
  behaviors.
- **Linked rules:** `WP-02`, `WP-03`, `WP-05`, `FA-01`, `WP-18`.

---

## `RBL-04` — Empirical directive ceiling per file

`[P2 | I70/E50/R20]`

- **Problem statement:** `WP-18` orients at ~30–50 active directives per standalone file, with
  `GS-15` defining what counts. `anti-drift-rules.md` carries 28 rules plus 6 not-to-dos = 34, inside
  the band but with no evidence that 34 is better or worse than 20 or 50 for this file's job.
- **Why it matters:** The ceiling drives decomposition decisions across the whole suite and is
  currently a convention rather than a measurement.
- **Initial hypothesis:** Compliance degrades with directive *count* sub-linearly until a threshold,
  then sharply — consistent with the interference effect in
  [Instruction Stacking Collapse](https://arxiv.org/pdf/2608.02639), which reports ~12% of
  satisfiable instruction pairs failing beyond their solo rates.
- **Suggested method:** Construct compliance probes for the `AD` rule set at 10 / 20 / 34 / 50
  directives and measure per-rule adherence as count rises.
- **Linked rules:** `WP-18`, `GS-14`, `GS-15`, `AD-26`.

---

## `RBL-05` — Absolute `file:///c:/GitDev/...` URLs in traceability sections

`[P2 | I68/E95/R10]`

- **Problem statement:** `AD-27` and the traceability sections of `WP`, `FA`, `GS` use absolute
  Windows `file:///c:/GitDev/apexai-os-meta/...` URLs. These resolve only on this machine and this
  checkout path; they break for any other clone, any CI runner, and any Linux agent working in
  `/root/workspaces/`.
- **Why it matters:** `APEX-LINK-INTEGRITY` only validates *relative* links in the root index, so
  the validator cannot see this class of breakage at all.
- **Why it was not fixed in this pass:** it is a mechanical sweep across four files that is
  independent of the compression work, and bundling it would blur the patch ledger.
- **Suggested method:** Convert to repository-relative links; extend `APEX-LINK-INTEGRITY` to flag
  absolute `file://` URLs in any governed concept file.
- **Linked rules:** `AD-27`, `WP-24`, `GS-20`, `FA-05`.

---

## `RBL-06` — Should the validator enforce in-body rule-ID uniqueness?

`[P2 | I78/E90/R12]`

- **Problem statement:** `okf_validator.py` enforces frontmatter `id:` uniqueness bundle-wide
  (`APEX-UNIQUE-DURABLE-ID`) but is blind to in-body durable rule IDs (`WP-01`, `FA-04`, …). Defect
  **D1** — `FA-04` assigned to two unrelated rules — existed through a full green validator run and
  185 passing tests.
- **Why it matters:** `WP-15` makes durable IDs the stable cross-reference mechanism for the entire
  suite. An unenforced uniqueness invariant is a convention, not a guarantee.
- **Resolution partially applied:** this pass adds a pytest-level duplicate-ID invariant test
  (Iteration 4). Promoting it into `okf_validator.py` as an `APEX_PROFILE_ERROR` would extend the
  guarantee to every bundle in the repo, not just this one.
- **Suggested method:** Add an `APEX-UNIQUE-RULE-ID` diagnostic; run it across all OKF bundles and
  count pre-existing violations before deciding error-vs-advisory severity (`AD-16`).
- **Linked rules:** `WP-15`, `FA-07`, `GS-08`, `GS-20`, `GS-21`.

---

## `RBL-07` — Plaintext credentials in a tracked repository file

`[P1 | I92/E100/R20]`

- **Problem statement:** `apex-meta/AI-Snippets/Orga/2Dos Ai Instructions.md` lines 66-69 contain a
  plaintext password and an API token for the OpenProject instance, in a git-tracked file.
- **Why it matters:** Secrets in version control remain recoverable from history after deletion;
  rotation is required, not just removal.
- **Why it is here and not patched:** entirely outside this pass's target, and credential handling
  is the operator's decision, not an incidental cleanup.
- **Suggested method:** Rotate the OpenProject credential first, then purge the lines; decide
  separately whether history rewriting is warranted.
- **Linked rules:** none — flagged for operator action.

---

## `RBL-08` — Does the suite need an adversarial "instruction conflict" gate?

`[P3 | I65/E55/R25]`

- **Problem statement:** Defects **D2** and **D9** were both *contradictions between two copies of
  the same contract*, and both survived every existing gate. The invariant tests added in Iteration 4
  catch structural duplication but not semantic divergence between a spec and the artifact it
  describes.
- **Why it matters:** R2 identifies contradiction as the failure mode that degrades compliance
  sharply, and this bundle produced two instances of it inside one authoring cycle.
- **Initial hypothesis:** A narrow check — "every JSON/YAML block in a spec that names an upstream
  source file must match that file" — would have caught **D9** mechanically.
- **Counter-consideration (`AD-25`):** ordinary use nearly surfaced this already; the inline copy was
  found by reading the file during an audit. Build the gate only if a second instance appears.
- **Suggested method:** Grep governed specs for fenced blocks adjacent to an upstream-source
  citation; count how many such pairs exist repo-wide before deciding whether a gate is justified.
- **Linked rules:** `GS-01`, `GS-09`, `GS-21`, `AD-25`, `WP-23`.
