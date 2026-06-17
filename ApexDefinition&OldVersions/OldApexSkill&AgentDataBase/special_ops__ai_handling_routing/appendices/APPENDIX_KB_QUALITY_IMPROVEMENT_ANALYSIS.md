---
class: trace
role: AUDIT
surface: agent_kb_appendix
quality: reliable
scope: agent
purpose: verify KB-base quality and identify high-value improvements for compact, unambiguous, interconnected use
dependencies: ESSENCE.md | BEST_PRACTICES.md | MISTAKES.md | TEMPLATES.md | LEARNING_QUEUE.md | APPENDIX_KB_SOURCE_MANIFEST.md | APPENDIX_KB_INFORMATION_RANKING_LEDGER.md | APPENDIX_KB_CANDIDATE_LEDGER.md | APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
status: improvement_analysis
owner: special_ops__ai_handling_routing
validator: meta_ops
---

# APPENDIX_KB_QUALITY_IMPROVEMENT_ANALYSIS

## Purpose

- **Decision:** This audit verifies the KB base after scaffold and appendix construction.
- **Constraint:** This file is an improvement analysis, not an applied rewrite and not accepted runtime authority.
- **Constraint:** Recommendations below should be applied only through a later bounded patch pass.

## Scope

- **Covers:** the five scaffold files and four appendices for `special_ops__ai_handling_routing`.
- **Covers:** compactness, plausibility, source coverage, interconnectedness, status clarity, and token efficiency.
- **Does not cover:** live model/provider benchmarking, runtime config, provider policy, or all-agent orchestration authority.

## Overall verdict

- **Verdict:** quality pass.
- **Confidence:** high for structural validity and advisory-boundary correctness.
- **Efficiency rating:** good now; can be improved by adding one compact cross-file map and tightening status language.
- **Plausibility rating:** high; source choices fit AI routing, source authority, handoff, and repo-execution boundaries.
- **Informatics-design rating:** good; files are function-separated and mostly self-contained.
- **Main risk:** some scaffold entries are labeled `accepted` while candidate/provenance language elsewhere says promotion is still governed; this is not a blocker, but a future patch should make `accepted_in_kb_base` distinct from `accepted_runtime_truth`.

## File-by-file audit

| file | current function | quality finding | efficiency finding | improvement priority |
|---|---|---|---|---|
| `ESSENCE.md` | activation boundary and compressed doctrine | strong boundary; clear owns/does-not-own split | compact and skimmable | P2 |
| `BEST_PRACTICES.md` | compact accepted practices | useful practices with evidence and appendix refs | somewhat repetitive schema/owner/validator fields per entry | P2 |
| `MISTAKES.md` | reusable failure patterns | strong countermeasure mapping | acceptable length; could use a top mini-index | P2 |
| `TEMPLATES.md` | reusable routing cards | high utility; best immediate operational value | strongest file for reuse; could add one `choose_template_when` table | P2 |
| `LEARNING_QUEUE.md` | candidate-only future improvements | correct candidate boundary | efficient; only three entries | P3 |
| `APPENDIX_KB_SOURCE_MANIFEST.md` | source coverage and plausibility | strong source trace and gap-risk disclosure | some ledger references are represented rather than fully materialized | P2 |
| `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` | information-unit mapping | strong information design; clear target mapping | table is dense but appropriate | P2 |
| `APPENDIX_KB_CANDIDATE_LEDGER.md` | candidate provenance | useful promotion/defer separation | good; could cross-link candidate IDs to scaffold IDs more explicitly | P2 |
| `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` | detailed failure evidence | high-value anti-drift body | slightly overlaps with `MISTAKES.md`, but acceptable because scaffold vs evidence roles differ | P3 |

## Strengths found

- **Boundary strength:** The KB repeatedly preserves the advisory lane boundary and blocks runtime config authority drift.
- **Source authority:** The source manifest and best-practice scaffold keep source authority as a pre-step gate rather than a post-hoc note.
- **Failure coverage:** The anti-drift appendix and mistakes scaffold cover the highest-risk routing failures: scope drift, source-authority blur, verification theater, path drift, premature handoff, stale provider claims, and config overreach.
- **Interconnection:** The scaffold files point into appendices, and appendices point back into scaffold targets.
- **Token posture:** Scaffold files are readable without loading all appendices.
- **Template value:** `TEMPLATES.md` is immediately reusable and lowers routing ambiguity.

## Weaknesses / improvement opportunities

### QI-001 — Add a one-page KB map

- **Finding:** The system has enough cross-links, but no single dependency map showing which file to read first and which appendix backs each scaffold file.
- **Impact:** Future agents may over-read appendices or miss the intended activation path.
- **Recommendation:** Add a compact `KB_MAP.md` or a short `## KB Map` section in `ESSENCE.md`.
- **Preferred patch:** Add to `ESSENCE.md`, not a new file, unless this KB grows further.
- **Target shape:** 5-row table: `need -> first file -> supporting appendix -> stop condition`.
- **Priority:** P2.

### QI-002 — Normalize status vocabulary

- **Finding:** The KB uses `accepted`, `promoted_to_scaffold`, `candidate`, `needs_validation`, `deferred`, and `kb_base_built`. These are mostly clear but not defined in one place.
- **Impact:** Future agents may confuse KB-base acceptance with governed runtime truth or promotion completion.
- **Recommendation:** Add a compact status vocabulary block to `ESSENCE.md` or `LEARNING_QUEUE.md`.
- **Preferred definitions:**
  - `accepted_in_kb_base`: usable as this agent's advisory KB scaffold.
  - `candidate`: captured but not validated.
  - `needs_validation`: useful but requires evidence/review before operational use.
  - `deferred`: intentionally not actionable now.
  - `runtime_authority`: not granted by this KB.
- **Priority:** P1.

### QI-003 — Add explicit read-budget profiles

- **Finding:** The KB is token-efficient, but it lacks a formal read-budget profile.
- **Impact:** Limited-context agents may load too much detail.
- **Recommendation:** Add a small section to `ESSENCE.md`:
  - `10-second route`: `ESSENCE.md` only.
  - `normal route`: `ESSENCE.md` + relevant `TEMPLATES.md` section.
  - `risk route`: add `MISTAKES.md`.
  - `audit route`: add relevant appendix.
- **Priority:** P2.

### QI-004 — Add template chooser table

- **Finding:** `TEMPLATES.md` has strong templates but no initial chooser.
- **Impact:** Agents may scan all templates when one table would suffice.
- **Recommendation:** Add a top-level `Template chooser` table before template details.
- **Target shape:** `situation -> template -> required fields -> fail action`.
- **Priority:** P2.

### QI-005 — Add source-gap severity markers

- **Finding:** The source manifest correctly notes gaps around live provider/pricing/model benchmark evidence.
- **Impact:** Future agents need to know whether that gap blocks general routing or only provider-specific recommendation.
- **Recommendation:** Convert gap notes into severity labels:
  - `blocking_for_provider_specific_recommendation`
  - `non_blocking_for_generic_routing_doctrine`
  - `manual_review_required_for_config_effect`
- **Priority:** P2.

### QI-006 — Link candidate IDs to applied scaffold IDs

- **Finding:** Candidate ledger statuses say `promoted_to_scaffold_as_template` or similar, but do not list exact scaffold IDs.
- **Impact:** Traceability is adequate but can be sharper.
- **Recommendation:** Add a column `realized_as` with exact IDs such as `AIHR-TPL-001`, `AIHR-BP-004`, or `AIHR-MISTAKE-008`.
- **Priority:** P2.

### QI-007 — Reduce repeated owner/validator metadata in scaffold entries

- **Finding:** Repeating owner and validator inside every entry improves local interpretability but costs tokens.
- **Impact:** Token overhead is minor now, but it scales poorly.
- **Recommendation:** Add a file-level default owner/validator and allow entries to omit repeated owner/validator unless they differ.
- **Caution:** Do not remove evidence refs or appendix refs; those are load-bearing.
- **Priority:** P3 now; P2 if file grows.

### QI-008 — Add a compact anti-overreach block to each scaffold

- **Finding:** The boundary is strongest in `ESSENCE.md` and appendices, but future partial retrieval may surface only `BEST_PRACTICES.md`, `MISTAKES.md`, or `TEMPLATES.md`.
- **Impact:** Partial retrieval could lose the advisory-only boundary.
- **Recommendation:** Add a one-line boundary note near the top of each scaffold: `This file is advisory and does not authorize config, provider-policy, or runtime authority changes.`
- **Priority:** P2.

## Recommended patch plan

### Patch pass A — highest value, lowest risk

- **Target:** `ESSENCE.md` only.
- **Actions:**
  - add status vocabulary
  - add read-budget profiles
  - refine KB map table
- **Expected benefit:** strongest token-efficiency and ambiguity reduction from one file.
- **Risk:** low.

### Patch pass B — template navigability

- **Target:** `TEMPLATES.md` only.
- **Actions:**
  - add template chooser table
  - add one-line advisory boundary note
- **Expected benefit:** faster use and fewer wrong-template scans.
- **Risk:** low.

### Patch pass C — traceability polish

- **Target:** `APPENDIX_KB_CANDIDATE_LEDGER.md` and `APPENDIX_KB_SOURCE_MANIFEST.md`.
- **Actions:**
  - add `realized_as` column to candidate ledger
  - add source-gap severity labels to manifest
- **Expected benefit:** better auditability and clearer non-blocking vs blocking gaps.
- **Risk:** medium because table rewrites are more error-prone than small inserts.

### Patch pass D — scale optimization if files grow

- **Target:** `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`.
- **Actions:**
  - move repeated owner/validator/review defaults to file level
  - keep per-entry evidence and appendix refs
- **Expected benefit:** token savings at scale.
- **Risk:** medium; apply only if entries expand substantially.

## Proposed minimal additions

### ESSENCE.md insertion candidate

```md
## Status vocabulary

- `accepted_in_kb_base`: usable as this agent's advisory KB scaffold.
- `candidate`: captured but not validated.
- `needs_validation`: promising but not operationally accepted.
- `deferred`: intentionally not actionable now.
- `runtime_authority`: not granted by this KB.
```

### ESSENCE.md read-budget candidate

```md
## Read-budget profiles

| Profile | Load | Use when |
|---|---|---|
| `10_second_route` | `ESSENCE.md` | quick advisory boundary or route-state check |
| `normal_route` | `ESSENCE.md` + relevant `TEMPLATES.md` section | building a routing/handoff card |
| `risk_route` | add `MISTAKES.md` | route may drift or overreach |
| `audit_route` | add relevant appendix | source/evidence trace is needed |
```

### TEMPLATES.md chooser candidate

```md
## Template chooser

| Situation | Template | Fail action |
|---|---|---|
| route selection unclear | `AIHR-TPL-001` | mark `needs_input` or `manual_review` |
| source conflict possible | `AIHR-TPL-002` | escalate if primary sources conflict |
| model/tool choice needed | `AIHR-TPL-003` | mark current claims `needs_current_verification` |
| repo mutation possible | `AIHR-TPL-004` | stop unless repo/mode/path are exact |
| delegation needed | `AIHR-TPL-005` | reject incomplete handoff |
| config impact possible | `AIHR-TPL-006` | stop for review |
```

## Do-not-change findings

- **Do not:** merge appendices into scaffold files.
- **Do not:** add live model/provider rankings without current verification.
- **Do not:** turn this KB into runtime config authority.
- **Do not:** create a broad all-agent routing canon here.
- **Do not:** remove appendix evidence refs from scaffold entries.

## Final recommendation

- **Recommendation:** Keep the current KB base as valid.
- **Recommendation:** Apply Patch pass A next if the goal is maximum value per token.
- **Recommendation:** Apply Patch pass B next if operators are actively using routing templates.
- **Recommendation:** Defer Patch pass D until the scaffold files grow enough for repeated owner/validator metadata to matter.
