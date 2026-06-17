## Executive verdict

**Yes.** Most of the Informatics Design and AI Handling/Routing gaps are also relevant to `special_ops__hygiene_clean`, but with different priority and translation.

The Hygiene Clean KB is already functional as a compact KB base, but it is missing a **second-pass quality/research appendix** comparable to what AI Handling/Routing received. The highest-impact improvement is not more doctrine. It is **traceability, status precision, QA reporting, and machine-readable audit structure**.

Source basis: Informatics Design validation/future-research report ; AI Handling/Routing validation/future-research report ; QA/Hygiene governing protocol .

---

# 1. Transferability matrix

|Finding / gap from other KBs|Transfer to Hygiene Clean?|Priority|Translation for Hygiene Clean|
|---|---|---|---|
|**Dedicated QA / next-research appendix**|Yes|**P1**|Create `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md` or `APPENDIX_KB_QUALITY_IMPROVEMENT_ANALYSIS.md`.|
|**Status vocabulary precision**|Yes|**P1**|Distinguish `accepted_in_kb_base`, `candidate`, `evidence_only`, `verified`, `runtime_truth`, and `promotion_required`.|
|**Read-budget profiles**|Yes|**P1**|Add “minimal / audit / rebuild / incident-response” read profiles to `ESSENCE.md`.|
|**Compact KB map**|Yes|**P1**|Add one table showing which file to read for activation, rule lookup, failure lookup, template use, provenance, ranking, evidence, and candidates.|
|**Template chooser table**|Yes|**P1**|Add “use this template when…” table to `TEMPLATES.md`. Especially important because Hygiene has multiple audit/finding/closure templates.|
|**Source-gap severity markers**|Yes|**P1**|Add `P0–P3` severity to source gaps in `APPENDIX_KB_SOURCE_MANIFEST.md`, aligned with QA/Hygiene severity semantics.|
|**`realized_as` links from candidates to scaffold IDs**|Yes|**P1**|Candidate rows should say whether each candidate became `BP-HC-*`, `M-HC-*`, template block, queue entry, or appendix-only evidence.|
|**Machine-readable JSON/YAML sidecars**|Yes, but defer|P2|Useful for later automation, not needed before QA report + status traceability.|
|**Dedicated source notes / SN database**|Yes|P2|Hygiene would benefit more than Informatics because it audits source integrity.|
|**Runtime examples**|Yes|P2|Add examples for finding classification, closure, source gap handling, and rewrite-drift detection.|
|**Variant comparison appendix**|Partial|P3|Less important unless Gemini/Perplexity/source variants materially disagree on hygiene doctrine.|
|**Prompt-template placement research**|Partial|P3|Mostly belongs to Prompts/Workflows, but Hygiene should audit when prompt templates become hidden law.|
|**Governed Markdown sentence strictness**|Partial|P3|Hygiene should validate readability/auditability, not own hard numeric sentence law.|
|**Provider/model matrix freshness**|No / mostly not|Low|AI Handling/Routing-specific; Hygiene only audits whether routing sources are current, not which model is best.|
|**Config-impact review packet pattern**|Yes, as audit trigger|P2|Hygiene should check whether config-impact review exists when changes touch config/provider/runtime policy.|

---

# 2. Common high-impact improvements across all three KBs

These should become a **shared Special Ops KB quality standard**, not just one-off improvements.

## A. Status vocabulary normalization

**Problem:** The current KBs use terms like `strong_candidate`, `candidate`, “accepted practices,” and “accepted scaffold” in ways that are understandable but could blur into runtime truth.

**High-impact fix:** Add a shared status vocabulary.

|Status|Meaning|
|---|---|
|`accepted_in_kb_base`|Included in scaffold as current KB operating guidance, but not necessarily global runtime law.|
|`candidate`|Stored for future validation.|
|`strong_candidate`|High-priority candidate, still not truth.|
|`evidence_only`|May support a rule, but is not itself a rule.|
|`verified`|Checked against required evidence.|
|`runtime_truth`|Accepted by governing promotion/config/managed-law path.|
|`promotion_required`|Cannot become truth without promotion route.|

**Hygiene-specific value:** Very high. Hygiene’s whole purpose is preventing candidate/truth contamination.

---

## B. Read-budget profiles

**Problem:** The scaffold/appendix split is good, but a cold agent still needs to know which files to load for each mode.

**Add to `ESSENCE.md`:**

|Read mode|Attach / read|
|---|---|
|`cold_start_minimal`|`ESSENCE.md`, then `BEST_PRACTICES.md` only if action is needed|
|`audit_run`|`ESSENCE.md`, `TEMPLATES.md`, `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|
|`source_review`|`APPENDIX_KB_SOURCE_MANIFEST.md`, `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`|
|`candidate_review`|`LEARNING_QUEUE.md`, `APPENDIX_KB_CANDIDATE_LEDGER.md`|
|`incident_response`|`MISTAKES.md`, `TEMPLATES.md`, `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`, `QA_HYGIENE_PROTOCOL.md`|
|`rebuild_or_refresh`|all appendices plus `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`|

**Hygiene-specific value:** Very high. It prevents context bloat while making audit depth available.

---

## C. Compact KB map

**Problem:** The files are clear individually, but the KB lacks a one-screen dependency map.

**Add to `ESSENCE.md`:**

|Need|File|
|---|---|
|Activate agent|`ESSENCE.md`|
|Apply hygiene rule|`BEST_PRACTICES.md`|
|Recognize failure pattern|`MISTAKES.md`|
|Write audit/finding/closure|`TEMPLATES.md`|
|Add future candidate|`LEARNING_QUEUE.md`|
|Check source provenance|`APPENDIX_KB_SOURCE_MANIFEST.md`|
|Check why information was selected|`APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`|
|Check candidate status|`APPENDIX_KB_CANDIDATE_LEDGER.md`|
|Check postmortem/evidence basis|`APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|
|Validate severity/routing/closure law|`QA_HYGIENE_PROTOCOL.md`|

**Hygiene-specific value:** Very high. This KB is itself a routing/audit surface.

---

## D. Template chooser table

**Problem:** `TEMPLATES.md` has several templates, but no fast chooser.

**Add:**

|Situation|Use template|
|---|---|
|Need to audit a target surface|`hygiene_audit_record`|
|Found a structural problem|`finding_record`|
|Closing or downgrading a finding|`closure_record`|
|Before risky patch/cleanup|`execution_mode_lock`|
|Adding or reviewing source|`source_manifest_row`|
|Ranking new extracted info|`information_ranking_row`|
|Preserving postmortem support|`evidence_note`|
|Two sources conflict|`source_conflict_report`|

**Hygiene-specific value:** Very high. It reduces execution friction and prevents agents from inventing local record shapes.

---

## E. `realized_as` traceability

**Problem:** Candidate ledgers say what each candidate targets, but not exactly where it landed.

**Add to `APPENDIX_KB_CANDIDATE_LEDGER.md`:**

```
realization:  realized_as:  realized_file:  scaffold_id:  appendix_pointer:  status_after_build:
```

Example:

|Candidate|Realized as|
|---|---|
|`HC-CAND-001` source authority / verification gate|`BP-HC-001` in `BEST_PRACTICES.md`|
|`HC-CAND-007` wording drift|`M-HC-001` / `M-HC-003` in `MISTAKES.md`|
|`HC-CAND-013` source manifest row|`source_manifest_row` in `TEMPLATES.md`|

**Hygiene-specific value:** Very high. This is exactly the kind of traceability Hygiene should model.

---

# 3. Hygiene-specific gaps not fully covered by the other two KBs

These are not merely transferred findings. They are specific to `special_ops__hygiene_clean`.

## A. Missing permanent QA report appendix

The Informatics report explicitly identifies that fetch-back verification happened, but no permanent QA report exists inside the KB folder. That same gap applies to Hygiene Clean.

**Create:**

```
appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
```

or

```
appendices/APPENDIX_KB_QUALITY_IMPROVEMENT_ANALYSIS.md
```

**Recommended sections:**

|Section|Content|
|---|---|
|`QA Header`|repo, branch, target root, generated_at, input window|
|`Surfaces checked`|5 scaffold files + 4 appendices|
|`Promptflow compliance`|appendix-first, ESSENCE-last, source-index-first, no Apex write|
|`Functional readiness scores`|activation, role boundary, source provenance, templates, evidence, candidate handling|
|`Findings`|P0–P3 findings, or explicit `finding_count: 0`|
|`Hygiene backlog`|non-blocking improvements|
|`Research backlog`|unresolved future questions|
|`Recommended patch sequence`|one-file-at-a-time sequence|

This aligns with the QA/Hygiene Protocol, which requires QA artifacts to declare identity, target scope, input window, finding count, highest severity, bounded findings, holds/escalations, backlog, and verification notes.

---

## B. Missing explicit severity model inside Hygiene KB templates

The current `TEMPLATES.md` includes severity fields, but the KB should explicitly tie them to the governing QA/Hygiene severity semantics.

**Patch target:** `TEMPLATES.md`

Add a compact severity crib:

|Severity|Hygiene meaning|
|---|---|
|`P0`|cannot safely continue without hold/escalation|
|`P1`|continue only in bounded degraded mode or after remediation|
|`P2`|material hygiene debt; backlog with due path|
|`P3`|low-risk cleanup or bounded deferment|

**Why:** QA/Hygiene Protocol says findings without explicit severity are invalid and P0/P1 cannot remain only in backlog.

---

## C. Missing closure-quality checklist

The Hygiene KB has closure templates, but should include a **closure validity checklist** because closure is a core Hygiene function.

**Patch target:** `TEMPLATES.md` or `BEST_PRACTICES.md`

Add:

|Closure check|Pass condition|
|---|---|
|Action completed|Required action was completed or explicitly reclassified|
|Evidence attached|Closure evidence references are present|
|Severity respected|P0/P1 routing was not bypassed|
|Residual risk visible|Residual P2/P3 debt is not hidden|
|No closure by silence|Later prose omission is not treated as closure|
|Downgrade reason|Any downgrade has explicit reason|

This mirrors the governing closure rules in QA/Hygiene Protocol, which says findings may not be closed by silence, later prose omission, or unreasoned downgrade.

---

## D. Missing “Hygiene-to-Night” routing guidance

This is high impact because Hygiene findings often become backlog and sequencing work. The Night Planning Protocol explicitly has an “Infrastructure and hygiene lane” for missing interfaces, stale state, broken pointers/dependencies, authority leakage, structural-risk backlog, and hygiene holds.

**Patch target:** `BEST_PRACTICES.md` or `ESSENCE.md`

Add:

|Finding outcome|Route|
|---|---|
|P0/P1 hold or escalation|`ESCALATION_EXCEPTION_BLOCK.md`|
|promotion integrity issue|`PROMOTION_PROTOCOL.md`|
|non-blocking hygiene backlog|`NIGHT_PLANNING_PROTOCOL.md`|
|state recommendation|bounded state recommendation, no direct mutation|
|ordinary cleanup|hygiene backlog / batch cleanup|

**Why:** This keeps Hygiene from becoming stop law, promotion law, or planning law while still routing consequences correctly.

---

## E. Missing explicit source-note/SN decision

The Informatics report searched for a dedicated `SOURCE_NOTES` / SN database and did not find one; it identified `SOURCE_INVENTORY_LEDGER.md`, `MASTER_IDEA_LEDGER.md`, `KB_RANKINGS_BY_AGENT.md`, and `APPENDIX_KB_SOURCE_MANIFEST.md` as closest equivalents.

For Hygiene, this matters more than for Informatics because Hygiene audits source gaps and source integrity.

**Recommendation:** Add either:

```
appendices/APPENDIX_KB_SOURCE_NOTES.md
```

or add a **Source Notes section** to `APPENDIX_KB_SOURCE_MANIFEST.md`.

**Minimum fields:**

```
source_note:  source_id:  source_path:  note_type: access_gap | duplicate | representative_choice | authority_caution | deferred_source | conflict_watch  note:  severity: P0 | P1 | P2 | P3  follow_up:
```

---

# 4. Items from Informatics Design that should transfer only partially

## A. Governed Markdown strictness

Informatics asks whether sentence-level rules should remain guidance or become stricter. That is relevant, but Hygiene should not own the final rule.

**Hygiene role:** audit whether a file is readable, self-contained, and unambiguous.

**Not Hygiene role:** define universal sentence-length or sentence-count law.

**Recommended Hygiene candidate:** “Flag hard numeric style rules as provisional unless promoted by Informatics Design + Meta Ops.”

---

## B. Prompt-template placement

Informatics asks whether prompt templates are governed file types, operational support assets, or prompts-workflows concerns.

**Hygiene role:** detect when prompt templates become hidden runtime law.

**Not Hygiene role:** decide final prompt-template taxonomy.

**Recommended Hygiene candidate:** “If a prompt template controls durable execution, require explicit authority/status classification.”

---

## C. Redundancy discipline

Informatics asks how much repetition between scaffold and appendices is useful before it becomes contradiction risk.

**Hygiene role:** audit contradictory or stale redundancy.

**Not Hygiene role:** own the design theory of redundancy.

**Recommended Hygiene candidate:** “Repeated rules must either be exact anchors or point to the source section; divergent duplicate wording becomes P2 unless it affects authority, then P1.”

---

# 5. Items from AI Handling/Routing that should transfer only partially

## A. Provider/model matrix freshness

This is **not** a Hygiene KB responsibility.

**Hygiene transfer:** check whether any routing KB claims depend on current provider/model facts and whether those facts have freshness markers.

**Do not transfer:** model recommendations, provider rankings, config policy.

---

## B. Config-impact review packet pattern

This is relevant to Hygiene as an audit trigger.

**Hygiene transfer:** add a template/finding class for “config-impact review missing.”

**Do not transfer:** ownership of config edits or provider policy.

---

## C. Cross-agent routing boundary review

Relevant.

**Hygiene transfer:** add a recurring audit check: “Does this finding belong to Hygiene, Routing, Informatics, Meta Detective, Promotion, or Escalation?”

**High-impact because:** Hygiene can easily absorb too much if it audits everything but fails to route ownership.

---

# 6. Proposed high-impact patch set for Hygiene Clean KB

## Patch pass A — `ESSENCE.md`

**Goal:** improve activation without adding bloat.

Add:

1. `Status vocabulary`
2. `Read-budget profiles`
3. `Compact KB map`
4. `Routing boundary summary`

**Impact:** Very high  
**Risk:** Low  
**Reason:** Single-file, compact navigation improvement.

---

## Patch pass B — `TEMPLATES.md`

**Goal:** improve execution utility.

Add:

1. Template chooser table
2. Severity crib
3. Closure validity checklist
4. `realized_as` candidate trace schema
5. Source-note row template

**Impact:** Very high  
**Risk:** Low/Medium  
**Reason:** More template content, but still bounded and appropriate.

---

## Patch pass C — `APPENDIX_KB_CANDIDATE_LEDGER.md`

**Goal:** improve traceability.

Add:

1. `realized_as`
2. `realized_file`
3. `scaffold_id`
4. `status_after_build`
5. `next_validation`

**Impact:** High  
**Risk:** Low  
**Reason:** Makes candidate-to-scaffold lineage explicit.

---

## Patch pass D — `APPENDIX_KB_SOURCE_MANIFEST.md`

**Goal:** improve source auditability.

Add:

1. Source-gap severity markers
2. Source-note register
3. Conflict-watch register
4. Representative-source decision field

**Impact:** High  
**Risk:** Low  
**Reason:** Directly aligned to Hygiene role.

---

## Patch pass E — new appendix

Create:

```
appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
```

**Include:**

|Section|Contents|
|---|---|
|`QA Status`|promptflow compliance, changed-file set, fetch-back state|
|`Functional Readiness`|scores for each scaffold and appendix|
|`Findings`|explicit `finding_count`; P0–P3 if present|
|`Hygiene Backlog`|non-blocking improvements|
|`Common Improvements From Other KBs`|shared cross-agent improvements|
|`Hygiene-Specific Improvements`|closure, severity, source notes, Night routing|
|`Research Backlog`|unresolved questions ranked by impact|
|`Recommended Patch Sequence`|A–E sequence above|

**Impact:** Very high  
**Risk:** Low  
**Reason:** Separate trace artifact; does not contaminate scaffolds.

---

# 7. Research backlog for Hygiene Clean

## P1 — High-impact research / decision questions

1. **Status semantics:** What exact status terms should all Special Ops KBs share?
2. **QA report standard:** Should every KB base build end with a permanent QA appendix?
3. **Candidate realization:** Should every candidate ledger require `realized_as` links?
4. **Source notes:** Should every KB maintain `APPENDIX_KB_SOURCE_NOTES.md`, or should source notes remain inside source manifests?
5. **Read-budget profiles:** Should all agent KBs use identical read-budget labels?

## P2 — Medium-impact research

6. **JSON/YAML sidecars:** Which ledgers deserve machine-readable mirrors first?
7. **Runtime examples:** How many examples are enough before examples become appendix bloat?
8. **Closure mechanics:** Should closure records be standalone artifacts or table rows inside QA reports?
9. **Cross-agent boundary checks:** How should Hygiene route findings that belong to Informatics, Routing, Meta Detective, Escalation, or Promotion?
10. **Severity mapping:** Should KB-source gaps use QA/Hygiene P0–P3, or separate source-risk labels?

## P3 — Defer

11. **Full variant comparison:** Only needed if source variants disagree materially.
12. **Strict sentence rules:** Informatics-owned; Hygiene should only audit readability and ambiguity.
13. **Prompt-template taxonomy:** Prompts/Workflows-owned; Hygiene audits hidden authority.

---

# 8. Common improvement standard for all Special Ops KBs

Use this as a shared acceptance upgrade:

|Requirement|Applies to all KBs?|Hygiene-specific importance|
|---|---|---|
|`ESSENCE.md` has read-budget profiles|Yes|High|
|`ESSENCE.md` has compact KB map|Yes|High|
|`TEMPLATES.md` has chooser table|Yes|Very high|
|Source manifest has gap severity|Yes|Very high|
|Candidate ledger has `realized_as` links|Yes|Very high|
|QA / quality appendix exists|Yes|Very high|
|Source notes / SN decision recorded|Yes|Very high|
|Machine-readable sidecar considered|Yes|Medium|
|Runtime examples appendix considered|Yes|Medium|
|No source conflict report unless needed|Yes|Medium|

---

## Final recommendation

**Create one new Hygiene appendix first:**

```
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
```

Then patch, in order:

1. `ESSENCE.md` — status vocabulary, read-budget profiles, compact KB map.
2. `TEMPLATES.md` — chooser table, severity crib, closure checklist, source-note row.
3. `APPENDIX_KB_CANDIDATE_LEDGER.md` — `realized_as` traceability.
4. `APPENDIX_KB_SOURCE_MANIFEST.md` — source-gap severity and source-note register.

This gives the Hygiene KB the same maturity improvements identified for Informatics and AI Handling/Routing, but translated into its core job: **source integrity, drift detection, severity, routing, and closure discipline.**