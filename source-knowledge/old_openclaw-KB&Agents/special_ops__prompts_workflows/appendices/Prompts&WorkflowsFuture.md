I’ll compare the informatics-design gap report against the current `special_ops__prompts_workflows` KB surface, then separate: shared improvements, lane-specific improvements, and items that should not transfer.

The informatics report’s strongest transferable themes are already visible: source-note/database layer, QA permanence, machine-readable sidecars, examples, and a next-research plan. I’m checking the Prompts Workflows repo surface now so the recommendations are not inferred only by analogy.

Received app response

Thought for 50s

Yes. Most informatics-design gaps are also applicable to `special_ops__prompts_workflows`, but several must be translated because this KB lane owns **prompt/workflow construction**, not information-design governance.

The attached informatics report identifies the main reusable improvement families: source-note/SN database, machine-readable sidecars, permanent QA report, optional source-conflict report, variant-comparison appendix, runtime examples, and a `QA_AND_NEXT_RESEARCH_PLAN` appendix.

## Executive verdict

|Finding|Applies to Prompts Workflows?|Priority|Notes|
|---|---|---|---|
|`APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|**Yes**|**P1**|Highest-value next file. Same logic as informatics: permanent QA + research backlog + attach-pack guidance.|
|`APPENDIX_KB_SOURCE_NOTES.md` / SN database|**Yes**|**P1**|I found no exact `SOURCE_NOTES` / SN file for this lane. Prompts Workflows would benefit from source notes because prompt/workflow evidence is especially variant-heavy.|
|JSON/YAML sidecars|**Yes**|**P2**|Useful for machine querying ledgers and templates. Not needed for runtime correctness, but high leverage later.|
|`APPENDIX_KB_QA_REPORT.md`|**Yes**|**P1**|Current fetch-back verification exists in chat, but not as a durable target-folder artifact.|
|`APPENDIX_KB_EXAMPLES.md`|**Yes, stronger than informatics**|**P1**|This lane especially needs before/after prompt, handoff, promptflow, and recovery examples.|
|Source conflict report|**Already exists**|Done|Prompts Workflows already needed and got one, unlike informatics. Source manifest points to `SOURCE_CONFLICT_REPORT.md` as the conflict-handling appendix.|
|Variant-comparison appendix|**Yes**|**P2**|More relevant here than informatics because there are multiple workflow/prompt research variants.|
|Research backlog|**Already partially present**|Partial|`LEARNING_QUEUE.md` already contains deferred prompt-design ranking, workflow variants, promptflow/handoff sources, and deeper failure-file mining candidates.|

## Current Prompts Workflows KB status

|Dimension|Status|Assessment|
|---|---|---|
|**Core KB base**|**Strong**|Scaffold + appendices are complete and source-grounded.|
|**Appendix-first architecture**|**Strong**|Source manifest, ranking, candidate, anti-drift, and conflict report exist.|
|**Source provenance**|**Strong**|Source manifest records indexed source set, coverage checks, duplication handling, gap risk, and material-gap disposition.|
|**Open research handling**|**Good**|Learning queue already captures four deferred lanes: prompt-design variants, workflow variants, promptflow/handoff files, and deeper failure evidence.|
|**Permanent QA artifact**|**Missing**|Verification exists from the run, but no durable appendix stores it.|
|**Examples / regression cases**|**Missing**|Templates exist, but applied examples are not yet stored.|
|**Machine-query database readiness**|**Medium**|Markdown ledgers are usable; JSON/YAML sidecars would improve later automation.|
|**Cross-agent reusability**|**High potential**|Several improvements should become a shared KB-base convention across all Special Ops KBs.|

## Transfer analysis from informatics-design gaps

### 1. Source notes / SN database

**Applicability:** Yes, high impact.

For Prompts Workflows, source notes should not duplicate the source manifest. They should explain **how each source should be used in future prompt/workflow construction**.

Recommended file:

```
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_SOURCE_NOTES.md
```

Recommended columns:

|Column|Why|
|---|---|
|`source_id`|Links to source manifest.|
|`source_path`|Direct provenance.|
|`use_as`|doctrine / template / evidence / example / conflict source.|
|`strongest_reusable_pattern`|What future prompts should reuse.|
|`do_not_overuse_as`|Prevents template-as-governance drift.|
|`known_overlap`|Avoids duplicate variants.|
|`best_runtime_pointer`|Which scaffold/template should cite it.|

**Impact:** High. This would help future agents avoid reopening the whole prompt/workflow corpus.

### 2. Machine-readable sidecars

**Applicability:** Yes, but not first.

Recommended sidecars:

```
appendices/APPENDIX_KB_SOURCE_MANIFEST.yamlappendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.yamlappendices/APPENDIX_KB_CANDIDATE_LEDGER.yamlappendices/APPENDIX_KB_TEMPLATE_CATALOG.yaml
```

For Prompts Workflows, the most valuable sidecar is not just source/ranking/candidate; it is a **template catalog sidecar** because this agent owns reusable prompt bodies.

**Impact:** Medium/high for automation, medium for current human use.

### 3. Permanent QA report

**Applicability:** Yes, high impact.

Recommended file:

```
appendices/APPENDIX_KB_QA_REPORT.md
```

Minimum sections:

|Section|Content|
|---|---|
|`Promptflow Compliance`|Repo boundary, target root, appendices-first, ESSENCE-last.|
|`Fetch-back Verification`|Files verified and final SHAs.|
|`Changed-file Set`|Target-only confirmation.|
|`Boundary Drift Check`|No config/governance/QA/promotion authority claimed.|
|`Known Residual Gaps`|Links to learning queue and source manifest gaps.|
|`Next QA Trigger`|When to rerun.|

**Impact:** High because the current verification exists in conversation state, not as a durable KB artifact.

### 4. Source conflict report

**Applicability:** Already handled.

Prompts Workflows already has a real conflict report because this KB had actual tensions:

|Conflict|Resolution|
|---|---|
|Patch-before-rewrite vs full-final-body/live-edit|Contextual: patch stable local defects; use full body/live edit when diff transport is fragile.|
|Stop-after-step vs multi-file promptflow|Treat closed promptflow as bounded execution unit.|
|Template usefulness vs governance authority|Templates are construction aids, not authority surfaces.|

This is a Prompts Workflows strength relative to the informatics run.

### 5. Runtime examples

**Applicability:** Yes, stronger than informatics.

Recommended file:

```
appendices/APPENDIX_KB_EXAMPLES.md
```

High-value examples:

|Example class|Example|
|---|---|
|Bad prompt → bounded prompt|Vague “improve this” converted into target/source/output/stop contract.|
|Bad handoff → clean handoff|Long chat summary converted into settled decisions, authority stack, next job, risks.|
|Fragile diff → live-edit contract|Markdown patch failure converted into one-file live edit.|
|Promptflow skeleton|Source lock → manifest → ranking → scaffold → fetch-back verification.|
|Out-of-mode capture|Adjacent improvement captured but not applied.|

**Impact:** Very high. This KB is a prompt/workflow agent; examples are not decorative here, they are core training material.

### 6. Variant comparison appendix

**Applicability:** Yes.

Recommended file:

```
appendices/APPENDIX_KB_VARIANT_COMPARISON.md
```

Why: The source manifest already records deferred workflow and prompt-design variants. The learning queue says additional workflow variants may add phrasing but appear convergent, and it warns not to promote duplicate wording.

Recommended comparison axes:

|Axis|Reason|
|---|---|
|`rule_overlap`|Avoid duplicate doctrine.|
|`unique_pattern`|Identify real new value.|
|`misuse_risk`|Prompts can become governance accidentally.|
|`template_candidate`|Extract only reusable structures.|
|`promotion_decision`|accepted / candidate / reject / appendix only.|

**Impact:** Medium/high. Useful before mining more prompt-design and workflow variants.

## Research questions: shared vs lane-specific

### Common across all Special Ops KBs

|Question|Applies to all?|Owner|
|---|---|---|
|Should every KB base have `QA_AND_NEXT_RESEARCH_PLAN.md`?|**Yes**|Meta Ops / Knowledge Bank|
|Should every KB base have `SOURCE_NOTES.md`?|**Yes**|Knowledge Bank|
|Should Markdown ledgers get YAML/JSON mirrors?|**Yes**|Informatics Design + Knowledge Bank|
|Should every KB base have an attach-pack definition?|**Yes**|Knowledge Bank|
|Should every KB base include examples?|Mostly yes|Agent-specific|
|Should every KB base have a conflict report?|Conditional|Agent-specific|

### Specific to Prompts Workflows

|Research question|Priority|Why|
|---|---|---|
|When does a prompt template become system knowledge instead of workflow tooling?|**P1**|This is the core governance-risk question for this lane.|
|What is the formal decision tree for patch vs full-body vs live-edit?|**P1**|Already identified as a real conflict; should be operationalized.|
|What is the maximum safe promptflow file set before decomposition is required?|**P1**|Resolves one-artifact-per-step vs closed-file-set execution.|
|What belongs in promptflow skeletons vs Codex execution preflights?|**P2**|Prevents mixing planning and execution.|
|Which prompt/workflow variants add new value versus duplicate phrasing?|**P2**|Needed before deeper source mining.|
|Should prompt templates have frontmatter metadata?|**P2**|Useful, but schema should not become bureaucracy.|
|What regression examples best detect prompt drift?|**P1**|Needed for `APPENDIX_KB_EXAMPLES.md`.|

### Informatics questions that should **not** transfer directly

|Informatics question|Prompts Workflows handling|
|---|---|
|Sentence-level Markdown strictness|Consume the future decision; do not own it.|
|Global file-type declaration rules|Consume or template them; do not define global schema.|
|Taxonomy/terminology governance|Reference informatics-design outputs; do not duplicate ownership.|
|Audit severity model|Route to QA/Hygiene; do not define locally.|

## High-impact improvement package for `special_ops__prompts_workflows`

### Recommended next patch set

|Order|File|Purpose|Priority|
|---|---|---|---|
|1|`appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|Permanent status, readiness, next research, attach packs, patch candidates.|**P1**|
|2|`appendices/APPENDIX_KB_SOURCE_NOTES.md`|Source-by-source use guidance and anti-overuse boundaries.|**P1**|
|3|`appendices/APPENDIX_KB_EXAMPLES.md`|Applied before/after prompt, handoff, promptflow, and recovery examples.|**P1**|
|4|`appendices/APPENDIX_KB_VARIANT_COMPARISON.md`|Compare duplicate/variant prompt and workflow research before deeper promotion.|**P2**|
|5|`appendices/APPENDIX_KB_QA_REPORT.md`|Separate durable QA report if not merged into QA/research plan.|**P2**|
|6|YAML sidecars|Machine-readable source/ranking/candidate/template catalogs.|**P2**|

### Best single next file

Create:

```
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
```

Recommended sections:

|Section|Contents|
|---|---|
|`QA Status`|Promptflow compliance, fetch-back, target-only writes, conflict report existence.|
|`Functional Readiness`|Score scaffold and appendices.|
|`Transfer From Informatics Gap Report`|Which gaps apply, modified, rejected.|
|`Prompts-Workflows-Specific Gaps`|Examples, variant comparison, patch/live-edit decision tree.|
|`Common KB Improvements`|Source notes, sidecars, QA, attach pack.|
|`Research Backlog`|Ranked P1/P2 questions.|
|`Next Patch Candidates`|Exact optional appendix files.|
|`Recommended Attach Pack`|Runtime pack vs rebuild/audit pack.|

## Common high-impact improvement pattern

The same higher-order improvement is visible for both KBs:

> The KB bases are already functional. The next improvement is not more doctrine; it is **durable meta-structure around the KB**: QA trace, source notes, examples, sidecars, attach packs, and ranked research backlog.

For `special_ops__prompts_workflows`, the most important added twist is this:

> Because this lane produces prompts and workflows, the examples/regression layer is not optional polish. It is the closest thing to a behavioral test suite.