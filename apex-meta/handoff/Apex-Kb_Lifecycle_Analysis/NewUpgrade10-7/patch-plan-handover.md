# Patch-Plan Handover — Apex KB Lifecycle Fix (Validated)

> Do not add process, roles, or scoring beyond what's listed here. If a
> recommendation below lacks a ✅ verified tag, treat it as unverified and
> confirm with the operator before including it in the patch plan.

This handover was produced by validating R01–R05 against the live repository
at `C:\GitDev\apexai-os-meta`. It supersedes R01–R05 wherever they disagree
with what the repo actually shows. It is not the patch plan — the next chat
writes that.

---

## 1. Path correction (apply before using any report)

R01–R05 cite KB artifact paths (log files, wiki pages, `query-eval-pack.json`)
as if they were relative to the repo root. They are actually relative to
`apex-meta/kb/claude-code-orchestration-design/`. Example:

- Report says: `wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md`
- Actual path: `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md`

All content at the corrected paths matches what the reports describe (see §2).
This is a citation-format issue, not a content error — but the next chat
should use corrected paths, not the reports' literal strings.

## 2. Verified evidence (✅) the patch plan may build on

✅ **`is_shell_page_candidate` / `cmd_quality` logic in `apex-meta/scripts/apex_kb.py`**
matches R01/R02/R04 exactly: thresholds `SHELL_PAGE_MIN_WORDS=40`,
`SHELL_PAGE_MIN_CHARS=200` (line ~1704); shell status requires low density
**AND** (no `source_refs` OR missing `Key Claims` OR missing `Macro / Meso /
Micro`) (line 1714–1726); `--strict` fails only on `phase2_repair_candidates`
or `shell_page_candidates` (line 1793–1798). This is the exact false-negative
path R02 describes: a page with all headings, `source_refs`, one generic
claim, and file-level-only pointers is not flagged.

✅ **`extract_source_refs`** (line 1666) collapses `source_refs` to bare
identifier strings, losing structured pointer detail — confirmed exactly as
R01/R02 state. No claim-level pointer parsing exists in the current code.

✅ **Root-cause log evidence is real and directly supports R01/R02/R04's
central claims.** Read in full:
`apex-meta/kb/claude-code-orchestration-design/log/max-run-20260709-phase2-quality-failure-root-cause.md`
and `...execution-audit.md`. Confirmed: quality command was never run after
generation; 37 commits ahead of baseline; one unrelated out-of-KB-root file
in the diff window; `source-payload-manifest.json` was empty; no deterministic
postflight ran; the `claude-code-mechanism-decision-model.md` example page has
one-sentence macro/meso/micro layers and one claim with a file-level pointer.
The "smoking gun" quote R01/R04 rely on ("This max-run intentionally writes
smaller pages, but every Phase 2 page includes the mandatory headings.") is a
real, exact quote from `phase2-value-contract.md`.

✅ **`outputs/queries/evals/query-eval-pack.json` (at the corrected KB path)
has `"queries": []`** — confirmed empty, exactly as R03 claims. The query-based
blind-review gate cannot run until this is populated.

✅ **`kb-contract.md` requirements** (Micro must be anchored by source
pointers; every claim needs pointer/confidence/label; Routes Here needs
question routes; uncertainty items need pointer + handling) — confirmed
verbatim in `.claude/skills/apex-kb/references/kb-contract.md`.

✅ **Script policy** (`network_access: forbidden`, `default_mode: dry_run`,
`shell_out: forbidden`, writes require `--allow-write`) — confirmed verbatim
in `script-command-contract.md` and `package-manifest.md`. Supports R01's
"scripts are local, no-network, dry-run by default" claim.

✅ **`lifecycle-state-machine.md` has 4 macro states (A–D)** — confirmed.
**S6_phase2_ready advances directly to S7_index_validation** with no bounded
handover or semantic-acceptance state in between — confirmed, supports R01's
and R03's claim that semantic acceptance is structurally absent from the
current state machine.

✅ **A real contradiction exists in the Phase 1→2 gate policy**, but it is
narrower than R04 states it. `SKILL.md` and
`references/ingest-query-lint-audit-rules.md` **agree** with each other:
continuous-by-default, `approve ingest` is only an *optional resume phrase*
for stop modes. The actual contradiction is in
`.claude/skills/apex-kb/templates/kb-schema-template.md` line 26:
`ingest_phase_2_requires_phrase: "approve ingest"` — this field implies the
phrase is mandatory, conflicting with the continuous-by-default policy stated
everywhere else. **Fix target: `templates/kb-schema-template.md`, not
`ingest-query-lint-audit-rules.md`** (R04 misattributed this file as a source
of the contradiction; it isn't one).

✅ **Acceptance-tests.md fixtures F01/F02 exist as R02 describes**: a shell
page fixture with `source_refs: []` and body "Nothing much here." (used in
the v3-repair-smoke block), and a "Retrieval" concept-page fixture containing
literal placeholder text (`<pointer>`, `<High-level retrieval summary.>`,
etc.) in the wiki/index/retrieval smoke block. Neither reproduces a
heading-complete-but-thin page — confirmed gap, matches R02's finding.
Note: the `#v3-repair-shell-page` / `#retrieval-page` anchors R02 cites are
not literal heading IDs in the file — cite by section name, not anchor, in
the patch plan.

## 3. Unverified or contradicted claims — do not carry into the patch plan without operator confirmation

⚠️ **State count is imprecise.** R01 says "eleven detailed states"; R04 says
`current_named_lifecycle_states: 11`. Direct count of
`lifecycle-state-machine.md` gives **12** named states (S0, S1, S2, S2b, S3,
S4, S5, S6, S7, S8, S9, S10). Immaterial to the recommended fix (both reports
agree the count should shrink to ~6), but do not repeat "eleven" as a
verified fact.

⚠️ **R03's semantic verdicts on 4 of its 5 sampled pages were not
independently re-verified** (`production-agent-readiness-and-risk-model.md`,
`source-preserving-kb-compile.md`, `claude-code-subagents.md`,
`failure-analysis-and-feedback-loop.md`). Per this validation's scope,
subjective semantic judgments were explicitly out of bounds — only R03's
verdict on `claude-code-mechanism-decision-model.md` was cross-checked
against the root-cause log's own characterization, and it matches. Treat
R03's other four page verdicts as plausible but not independently confirmed.

⚠️ **`apex_kb_retrieval.py` internals (index building, stale detection,
command dispatch) were not inspected.** R01's S09 claims about this file are
unverified. This file is explicitly out of scope for the patch per R05 and
R01 (`likely_no_change_required_for_process_model`) — leave it untouched
regardless.

⚠️ **`lifecycle-runbook.md` content was not read in this pass** — only
confirmed to exist. R04's characterization of it ("repeats output tiers and
execution sequence") is unverified.

## 4. R05 recommendations without direct verified evidence

- Adding `authority_class` / `deprecated` markers to `package-manifest.md` —
  no root-cause or execution-audit finding ties package-manifest ambiguity to
  the actual max-run failure. R04 itself scores this lowest of its table
  (impact 83, the lowest impact score in R04 §16). Treat as optional, not
  mandatory.
- Everything else in R05's "Mandatory Changes" (§1–7 of P05.md) traces to a
  verified root-cause or execution-audit finding per §2 above.

## 5. Exact files the patch plan may touch

1. `.claude/skills/apex-kb/SKILL.md` — lifecycle authority, capability
   routing, evidence fields, semantic gate, completion classes.
2. `apex-meta/scripts/apex_kb.py` — reason-coded quality measurements
   (`extract_source_refs`, `is_shell_page_candidate`, `quality_report`,
   `cmd_quality`) per R02's verified change map.
3. `.claude/skills/apex-kb/references/script-command-contract.md` — quality
   result schema, postflight packet contract, exit semantics.
4. `.claude/skills/apex-kb/references/acceptance-tests.md` — add a
   heading-complete-thin fixture and a strong-pass fixture; cite by section
   name, not anchor.
5. `.claude/skills/apex-kb/package-manifest.md` — authority-class markers
   (optional; see §4).
6. `.claude/skills/apex-kb/references/lifecycle-state-machine.md` — deprecate
   as lifecycle authority (verified: no semantic-acceptance state, S6→S7 has
   no bounded handover).
7. `.claude/skills/apex-kb/templates/kb-schema-template.md` — fix the
   `ingest_phase_2_requires_phrase` field to match the continuous-by-default
   policy (verified contradiction; corrected file target — see §2).
8. `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md` —
   merge unique content per R04, but do not treat it as a source of the
   Phase 1→2 contradiction (it isn't one — see §2).
9. `.claude/skills/apex-kb/examples/lifecycle-runbook.md` — mark
   example-only per R04 (content not independently verified, but the
   "mark non-authoritative" action itself carries no risk).

## 6. Files the patch plan must not touch

- `.claude/skills/apex-kb/references/kb-contract.md` and
  `.claude/skills/apex-kb/templates/wiki-page-templates.md` — R05 explicitly
  defers these to a second wave; R02 recommends changes to them but R05's
  synthesis (not a factual claim) overrides for the first patch. Confirm with
  operator before including.
- `apex-meta/scripts/apex_kb_retrieval.py` — out of scope per all reports;
  not independently inspected in this validation either.
- `outputs/queries/evals/query-eval-pack.json` and existing wiki pages under
  `apex-meta/kb/claude-code-orchestration-design/wiki/` — content, not
  process; do not regenerate as part of this process patch.
- Any file under `.repair-backups/`, `_recovery_backup_before_apex_package_restore/`,
  `_restore_staging_apex_packages/`, `_verification/`, `_reports/`,
  `validation-reports/`, `source-knowledge/` — excluded by root `.claude/CLAUDE.md`.

## 7. Smallest viable process changes that survived validation

1. Cap connector-only writes at `compiled_unvalidated` / external `partial` —
   directly evidenced by execution-audit F4/F8.
2. One mandatory deterministic postflight evidence packet (index, retrieval
   build, stale, lint --strict, quality --strict, status) — directly
   evidenced by execution-audit F4 (no postflight ran) and root-cause RC1.
3. Strengthen `is_shell_page_candidate`/`quality_report` with per-section
   word counts, key-claim count, claim-pointer coverage, pointer-specificity
   — directly evidenced by the verified code walkthrough in §2 and root-cause
   RC2/RC3.
4. One bounded clean-context semantic acceptance gate (query trial + 2–3
   material claim checks) before `query_ready` — directly evidenced by the
   confirmed absence of any semantic-acceptance state in
   `lifecycle-state-machine.md` and the empty `query-eval-pack.json`.
5. Fix the `kb-schema-template.md` phrase-requirement contradiction (§2).
6. One lifecycle authority (`SKILL.md`) — evidenced by the real (but
   narrower-than-reported) Phase 1→2 gate contradiction in §2.

## 8. Open operator decisions (unchanged from R05, still open)

1. Phase 1→2 policy: continuous-by-default (already the stated policy in
   `SKILL.md`/`ingest-query-lint-audit-rules.md`) vs. mandatory separate
   approval — decide whether to also fix `kb-schema-template.md` to match.
2. Target-query authority: Phase 1 author, operator, or populated
   query-eval pack.
3. Semantic-partial handling: exclude from query-ready retrieval, or include
   with `needs_review`.
4. Threshold calibration for section/claim-count candidate rules.
5. Minimum acceptable source-pointer granularity (line/span, section,
   heading, quote hash) when stable lines are unavailable.
6. Reviewer escalation threshold: which page classes need a different model
   or operator instead of a clean same-model invocation.
7. Whether to include `kb-contract.md` / `wiki-page-templates.md` in this
   patch wave or defer them (§6).
8. Whether to add `package-manifest.md` authority-class markers now or treat
   as optional cleanup (§4).

## 9. Deviations from the original validation instructions

- The handover's request for "exact files it must not touch" is populated
  from R05's own list plus the repo's root `.claude/CLAUDE.md` exclusions —
  no additional files were added on this validator's own judgment.
- Per the original task's boundary, this validator did not design the patch
  plan, execute code changes, or write to any file other than this one.
