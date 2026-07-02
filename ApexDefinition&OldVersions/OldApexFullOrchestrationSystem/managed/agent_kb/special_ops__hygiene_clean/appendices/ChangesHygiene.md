You are correct. I skipped the actual governing gate.

## 1. Prompt-flow compliance check

|Phase|Required action|What I did|Compliance|
|---|---|---|---|
|Phase 1|Verify repo, branch, target folder, local read scope|Verified target repo/path via GitHub and read target folder files. Did **not** verify native active branch because I did not have a local checkout.|Partial|
|Phase 2|Read/classify local inputs only|Read local scaffold + local appendices. Early search exposed non-target path metadata, but I did not fetch/use non-target content.|Mostly compliant|
|Phase 3|Produce Candidate Decision Table and stop for operator decision|**Failed.** I did not surface the decision matrix before designing patch content.|Non-compliant|
|Phase 4|Design target updates after approval|I designed updates without valid row-level operator approval.|Non-compliant|
|Phase 5|Generate diffs|I generated patch-pack content prematurely.|Non-compliant|
|Phase 6|Validate diffs/local-only scope|Partial validation only.|Partial|
|Phase 7|Produce Codex prompt|Produced, but downstream of an invalid Phase 3/4 sequence.|Premature|
|Phase 8|Final proof|Produced, but it overstated readiness because the operator validation gate was missing.|Defective|

**Blocker:** only the final write/apply stage was blocked, because the prompt-flow forbids GitHub whole-file replacement and requires native `git apply` on `main`. The Candidate Decision Table was **not blocked**. I should have produced it first. The corrected prompt-flow explicitly requires the Candidate Decision Table before diffs and stops for operator decision unless an approval shortcut exists.

---

# 2. Candidate Decision Matrix — Local appendix candidates

Source: `APPENDIX_KB_CANDIDATE_LEDGER.md` and related scaffold/appendix files.

Legend:

- **Integrate:** add or preserve in new scaffold/appendix version.
    
- **Trace-only:** do not add new rule content; add realization/status trace.
    
- **Keep candidate:** keep in appendix/queue for later validation.
    
- **Defer:** do not integrate in this pass.
    

|Rank|candidate_id|local_source_file|Candidate summary|Evidence strength|Possible targets|Recommendation|Reason|Recommended operator decision|Operator decision|
|--:|---|---|---|---|---|---|---|---|---|
|1|HC-CAND-001|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Separate source authority and verification: authority before action, verification before approval.|High / strong_candidate|`BEST_PRACTICES.md`, `ESSENCE.md`|integrate_into_scaffold|Core Hygiene behavior; already represented as `BP-HC-001`, should be preserved and status-normalized.|approved||
|2|HC-CAND-004|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Hygiene owns QA/audit/backlog/closure recommendations; does not own truth mutation, promotion, architecture, or stop law.|High / strong_candidate|`ESSENCE.md`|integrate_into_scaffold|Core role boundary; must remain activation-surface content.|approved||
|3|HC-CAND-009|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Process files must function as blocking gates; citing doctrine is insufficient.|High / strong_candidate|`BEST_PRACTICES.md`, `TEMPLATES.md`|integrate_into_scaffold|High-impact anti-drift rule; already represented as `BP-HC-002`; add/check preflight proof hooks.|approved||
|4|HC-CAND-005|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Hygiene-relevant execution must declare exact mode, root, target files, allowed actions, forbidden actions, stop conditions, and deliverable.|High / strong_candidate|`TEMPLATES.md`, `BEST_PRACTICES.md`|integrate_into_scaffold|Directly operational; preserve `execution_mode_lock` and add chooser linkage.|approved||
|5|HC-CAND-006|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Use one-file-at-a-time execution for drift-sensitive files; validate before advancing.|High / strong_candidate|`BEST_PRACTICES.md`, `MISTAKES.md`|integrate_into_scaffold|Core safety pattern; already represented as `BP-HC-004`.|approved||
|6|HC-CAND-007|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Wording drift is a hygiene finding when repair becomes semantic redesign.|High / strong_candidate|`MISTAKES.md`, `TEMPLATES.md`|integrate_into_scaffold|Core failure pattern; already represented in `M-HC-001` / `M-HC-003`; add traceability.|approved||
|7|HC-CAND-008|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Execute-not-explain drift occurs when bounded repair becomes explanation, teaching, or reframing.|High / strong_candidate|`MISTAKES.md`|integrate_into_scaffold|Directly relevant to this failure; keep prominent as `M-HC-002`.|approved||
|8|HC-CAND-010|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Target-topology drift occurs when new target files are designed before no-fit proof.|High / strong_candidate|`MISTAKES.md`, `BEST_PRACTICES.md`|integrate_into_scaffold|Valuable for harmonization/merge-mode hygiene; preserve as bounded failure pattern.|approved||
|9|HC-CAND-002|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Universal audit checks should inspect chunk self-containment, file typing, pass/fail state, and severity.|High / strong_candidate|`TEMPLATES.md`, appendices|split_between_scaffold_and_appendix|Template-level utility is high; avoid turning it into broad Informatics law.|approved||
|10|HC-CAND-013|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Source manifest rows must record duplicate group, representative source, access blockers, triage, and inclusion decision.|High / strong_candidate|`TEMPLATES.md`, `APPENDIX_KB_SOURCE_MANIFEST.md`|split_between_scaffold_and_appendix|Essential source-integrity pattern; scaffold should provide template, appendix should record local use.|approved||
|11|HC-CAND-014|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Failure evidence remains evidence/safeguard, not automatic universal doctrine.|High / strong_candidate|`ESSENCE.md`, `LEARNING_QUEUE.md`, anti-drift appendix|integrate_into_scaffold|Crucial candidate/truth boundary; preserve as status doctrine.|approved||
|12|HC-CAND-015|`APPENDIX_KB_CANDIDATE_LEDGER.md`|KB essence candidates remain candidates until verification and required approval.|Medium-high / strong_candidate|`LEARNING_QUEUE.md`, `ESSENCE.md`|split_between_scaffold_and_appendix|Good status rule; add normalized vocabulary rather than more prose.|approved||
|13|HC-CAND-003|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Optimize hygiene outputs for retrieval clarity, low ambiguity, handoff reliability, and auditability.|Medium-high / strong_candidate|`ESSENCE.md`|integrate_into_scaffold|Valid activation doctrine; keep compact to avoid Informatics sprawl.|approved||
|14|HC-CAND-011|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Exact-preservation validation should include file count, missing/extra files, size/line metrics, and checksums.|Medium / candidate|`TEMPLATES.md`|integrate_into_scaffold|Operationally useful; should be scoped to exact-preservation contexts.|approved||
|15|HC-CAND-016|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Candidate rows should preserve impact/evidence/integration score, drift warning, validator, target, status, and confidence.|Medium / candidate|`LEARNING_QUEUE.md`, `APPENDIX_KB_CANDIDATE_LEDGER.md`|integrate_into_appendix|Better as ledger schema/status trace, not scaffold doctrine.|approved||
|16|HC-CAND-012|`APPENDIX_KB_CANDIDATE_LEDGER.md`|Residual guidance should separate confirmed structure, recommended extension, optional omission, and open caution.|Medium / candidate|`TEMPLATES.md`, appendix|keep_as_candidate|Useful, but less central than QA/status/closure/source traceability. Keep for later or add only if template scope remains compact.|defer||

---

# 3. Future-research / quality-improvement Decision Matrix

Source: `Q&A&HygieneFuture.md`, which identifies the missing second-pass QA/research appendix and lists transferability, Hygiene-specific gaps, and patch passes A–E.

|Rank|candidate_id|local_source_file|Candidate / future possibility|Priority in source|Possible targets|Recommendation|Reason|Recommended operator decision|Operator decision|
|--:|---|---|---|---|---|---|---|---|---|
|1|HYG-UPD-001|`Q&A&HygieneFuture.md`|Create permanent QA / next-research appendix.|P1|`appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|integrate_into_appendix|Highest-impact missing trace surface; avoids stuffing QA/research into scaffold files.|approved||
|2|HYG-UPD-002|`Q&A&HygieneFuture.md`|Normalize status vocabulary: `accepted_in_kb_base`, `candidate`, `strong_candidate`, `evidence_only`, `verified`, `runtime_truth`, `promotion_required`.|P1|`ESSENCE.md`, `APPENDIX_KB_CANDIDATE_LEDGER.md`, `LEARNING_QUEUE.md`|split_between_scaffold_and_appendix|Directly prevents candidate/truth contamination, central to Hygiene.|approved||
|3|HYG-UPD-003|`Q&A&HygieneFuture.md`|Add read-budget profiles: minimal, audit, source review, candidate review, incident response, rebuild/refresh.|P1|`ESSENCE.md`|integrate_into_scaffold|Improves activation and prevents context bloat.|approved||
|4|HYG-UPD-004|`Q&A&HygieneFuture.md`|Add compact KB map by need/file.|P1|`ESSENCE.md`|integrate_into_scaffold|High leverage; makes KB routable and machine-followable.|approved||
|5|HYG-UPD-005|`Q&A&HygieneFuture.md`|Add template chooser table.|P1|`TEMPLATES.md`|integrate_into_scaffold|Prevents ad hoc record shapes and improves audit execution speed.|approved||
|6|HYG-UPD-006|`Q&A&HygieneFuture.md`|Add severity crib aligned to QA/Hygiene semantics.|P1|`TEMPLATES.md`|integrate_into_scaffold|Findings without severity are invalid; agents need local crib.|approved||
|7|HYG-UPD-007|`Q&A&HygieneFuture.md`|Add closure validity checklist.|P1 / Hygiene-specific|`TEMPLATES.md`, maybe `BEST_PRACTICES.md`|integrate_into_scaffold|Closure is a core Hygiene function; prevents closure-by-silence.|approved||
|8|HYG-UPD-008|`Q&A&HygieneFuture.md`|Add `realized_as` candidate traceability.|P1|`APPENDIX_KB_CANDIDATE_LEDGER.md`, `TEMPLATES.md`|split_between_scaffold_and_appendix|Makes candidate-to-scaffold lineage explicit.|approved||
|9|HYG-UPD-009|`Q&A&HygieneFuture.md`|Add source-gap severity markers.|P1|`APPENDIX_KB_SOURCE_MANIFEST.md`, `TEMPLATES.md`|integrate_into_appendix|Source-integrity gap severity is directly in Hygiene’s lane.|approved||
|10|HYG-UPD-010|`Q&A&HygieneFuture.md`|Add source notes / SN decision.|P2 but Hygiene-high|`APPENDIX_KB_SOURCE_MANIFEST.md` or new `APPENDIX_KB_SOURCE_NOTES.md`|integrate_into_appendix|Best current move: add Source Notes section to existing source manifest, not a new appendix yet.|approved||
|11|HYG-UPD-011|`Q&A&HygieneFuture.md`|Add Hygiene-to-Night routing guidance.|Hygiene-specific high impact|`ESSENCE.md`, `BEST_PRACTICES.md`|integrate_into_scaffold|Keeps Hygiene from becoming planning law while routing backlog correctly.|approved||
|12|HYG-UPD-012|`Q&A&HygieneFuture.md`|Add cross-agent routing boundary review.|P2 / high-impact|`TEMPLATES.md`, `ESSENCE.md`|integrate_into_scaffold|Hygiene audits broadly; this prevents ownership absorption.|approved||
|13|HYG-UPD-013|`Q&A&HygieneFuture.md`|Add config-impact review missing as audit trigger.|P2|`TEMPLATES.md`, possibly `MISTAKES.md`|integrate_into_scaffold|Hygiene should flag missing config-impact review, not own config policy.|approved||
|14|HYG-UPD-014|`Q&A&HygieneFuture.md`|Add runtime examples for finding classification, closure, source gap handling, rewrite drift.|P2|Future examples appendix or `TEMPLATES.md`|keep_as_candidate|Useful but likely bloat in current scaffold pass; better after QA appendix lands.|defer||
|15|HYG-UPD-015|`Q&A&HygieneFuture.md`|Add machine-readable JSON/YAML sidecars.|P2|Future sidecars|defer|Automation useful later; not required before trace/status/scaffold fixes.|defer||
|16|HYG-UPD-016|`Q&A&HygieneFuture.md`|Dedicated standalone source notes database.|P2|Possible future `APPENDIX_KB_SOURCE_NOTES.md`|defer|Add Source Notes section first; create new file only if it outgrows manifest.|defer||
|17|HYG-UPD-017|`Q&A&HygieneFuture.md`|Closure mechanics research: standalone artifacts vs table rows.|P2|QA appendix / future protocol notes|keep_as_candidate|Needs later decision after first QA appendix exists.|defer||
|18|HYG-UPD-018|`Q&A&HygieneFuture.md`|Severity mapping research: QA P0–P3 vs source-risk labels.|P2|Source manifest / QA appendix|keep_as_candidate|Current pass can use P0–P3 crib; deeper mapping can wait.|defer||
|19|HYG-UPD-019|`Q&A&HygieneFuture.md`|Redundancy discipline: repeated rules exact-anchor or source-pointer; divergent duplicates become findings.|P3 / partial|`BEST_PRACTICES.md`, future QA appendix|keep_as_candidate|Valid, but less urgent than status/read/closure/source traceability.|defer||
|20|HYG-UPD-020|`Q&A&HygieneFuture.md`|Prompt-template placement research: audit hidden law.|P3 / partial|`TEMPLATES.md` or future backlog|keep_as_candidate|Hygiene should audit hidden law, not decide prompt taxonomy.|defer||
|21|HYG-UPD-021|`Q&A&HygieneFuture.md`|Governed Markdown strictness / sentence rules.|P3 / partial|Future backlog|reject_obsolete_for_current_pass|Informatics-owned; Hygiene only audits ambiguity/readability.|defer||
|22|HYG-UPD-022|`Q&A&HygieneFuture.md`|Variant comparison appendix.|P3|Possible future appendix|defer|Only needed if variants materially disagree.|defer||
|23|HYG-UPD-023|`Q&A&HygieneFuture.md`|Provider/model matrix freshness.|Low / no transfer|None, except audit freshness marker in other KBs|reject_obsolete|Not Hygiene KB content; Hygiene only audits freshness claims elsewhere.|rejected||

---

# 4. Recommended scaffold integration set

This is the clean “what will go into new versions” summary.

## A. `ESSENCE.md`

|Proposed integration|Source candidate(s)|Decision|
|---|---|---|
|Status vocabulary|HYG-UPD-002, HC-CAND-014, HC-CAND-015|approve|
|Read-budget profiles|HYG-UPD-003|approve|
|Compact KB map|HYG-UPD-004|approve|
|Routing boundary summary|HYG-UPD-011, HYG-UPD-012|approve|
|Preserve role boundary|HC-CAND-004|approve|
|Preserve authority/verification doctrine|HC-CAND-001|approve|
|Preserve candidate/truth boundary|HC-CAND-014, HC-CAND-015|approve|

## B. `BEST_PRACTICES.md`

|Proposed integration|Source candidate(s)|Decision|
|---|---|---|
|Preserve authority vs verification gate|HC-CAND-001|approve|
|Preserve process gate rule|HC-CAND-009|approve|
|Preserve execution mode lock rule|HC-CAND-005|approve|
|Preserve one-file-at-a-time rule|HC-CAND-006|approve|
|Add/clarify Hygiene-to-Night routing as routing practice|HYG-UPD-011|approve|
|Avoid adding broad redundancy / markdown strictness doctrine|HYG-UPD-019, HYG-UPD-021|defer|

## C. `MISTAKES.md`

|Proposed integration|Source candidate(s)|Decision|
|---|---|---|
|Preserve repair-by-interpretation|HC-CAND-007|approve|
|Preserve execute-not-explain drift|HC-CAND-008|approve|
|Preserve whole-file rewrite reflex|HC-CAND-007|approve|
|Preserve process-gate bypass|HC-CAND-009|approve|
|Preserve mode crossing|HC-CAND-005|approve|
|Preserve target-topology drift|HC-CAND-010|approve|
|Add config-impact review missing as mistake pattern?|HYG-UPD-013|revise — better as template/finding class than mistake|

## D. `TEMPLATES.md`

|Proposed integration|Source candidate(s)|Decision|
|---|---|---|
|Template chooser table|HYG-UPD-005|approve|
|Severity crib|HYG-UPD-006|approve|
|Closure validity checklist|HYG-UPD-007|approve|
|Candidate realization trace schema|HYG-UPD-008, HC-CAND-016|approve|
|Source-note row template|HYG-UPD-010|approve|
|Config-impact review missing finding class|HYG-UPD-013|approve|
|Cross-agent ownership/routing check field|HYG-UPD-012|approve|
|Exact-preservation validation fields|HC-CAND-011|approve|
|Residual guidance template|HC-CAND-012|defer or appendix-only|

## E. `LEARNING_QUEUE.md`

|Proposed integration|Source candidate(s)|Decision|
|---|---|---|
|Preserve candidate-only queue semantics|HC-CAND-015|approve|
|Normalize statuses against new vocabulary|HYG-UPD-002|approve|
|Add realization/trace fields?|HC-CAND-016|revise — candidate ledger is better target; queue can point there|

## F. `APPENDIX_KB_CANDIDATE_LEDGER.md`

|Proposed integration|Source candidate(s)|Decision|
|---|---|---|
|Add realization trace fields|HYG-UPD-008, HC-CAND-016|approve|
|Add `realized_as`, `realized_file`, `scaffold_id`, `status_after_build`, `next_validation`|HYG-UPD-008|approve|
|Mark existing candidates as realized / appendix-only / queue-only|HC-CAND-001–016|approve|
|Do not promote candidates to runtime truth|HC-CAND-014, HC-CAND-015|approve|

## G. `APPENDIX_KB_SOURCE_MANIFEST.md`

|Proposed integration|Source candidate(s)|Decision|
|---|---|---|
|Add current update authority note: corrected folder-local promptflow supersedes old base-build promptflow for updates|prompt-flow + current source manifest|approve|
|Add source-gap severity markers|HYG-UPD-009|approve|
|Add Source Notes register inside existing manifest|HYG-UPD-010|approve|
|Add Conflict Watch register|HYG-UPD-010|approve|
|Do not create standalone source-notes appendix yet|HYG-UPD-016|defer|

## H. New appendix

|Proposed integration|Source candidate(s)|Decision|
|---|---|---|
|Create `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|HYG-UPD-001|approve|
|Include QA status, surfaces checked, functional readiness, findings, backlog, research backlog, recommended patch sequence|HYG-UPD-001 and Q&A future sections|approve|
|Keep as appendix, not scaffold|HYG-UPD-001|approve|

---

# 5. Immediate validation request

Use this validation shorthand:

```yaml
approve:
  - HC-CAND-001 through HC-CAND-011
  - HC-CAND-013 through HC-CAND-016
  - HYG-UPD-001 through HYG-UPD-013
defer:
  - HC-CAND-012
  - HYG-UPD-014 through HYG-UPD-022
reject:
  - HYG-UPD-023
revise:
  - any rows you want changed
```

The corrected next step is: you validate or revise this matrix; only then should I produce the update design table and changed-file set.