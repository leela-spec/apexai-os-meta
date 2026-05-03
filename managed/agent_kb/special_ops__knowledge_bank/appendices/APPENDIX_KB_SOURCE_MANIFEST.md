# APPENDIX_KB_SOURCE_MANIFEST

## Purpose

This appendix records the bounded source slice used to build and Apex-integrate the `special_ops__knowledge_bank` KB base.

## Execution lock

- **Working repo:** `leela-spec/apexai-os-meta`
- **Target root:** `managed/agent_kb/special_ops__knowledge_bank/`
- **Base-build promptflow:** `newversions/PROMPTFLOW_KB_BASE_BUILD.md`
- **Apex integration promptflow:** `PROMPTFLOW_KB_INTEGRATION_FINAL.md`
- **Execution mode:** Apex new-base integration
- **Write boundary:** only this agent KB root

## Source authority stack

|priority|source_path|source_role|read_status|use_in_this_build|
|---|---|---|---|---|
|1|`managed/agent_kb/special_ops__knowledge_bank/PROMPTFLOW_KB_INTEGRATION_FINAL.md`|integration authority|read|defines Apex target root, new-base discovery, H1 identity mapping, valid Apex delta test, and patch boundaries|
|2|`managed/agent_kb/special_ops__knowledge_bank/newversions/`|new baseline folder|read|provides newly created Knowledge Bank KB base files; H1/content identity is authoritative over filename when mismatched|
|3|`managed/agent_kb/special_ops__knowledge_bank/`|current Apex standard target|read|provides existing standard-path KB files and old Apex deltas|
|4|`managed/knowledge/AGENT_KB_LANES.md`|Apex KB lane authority|read|defines KB roots, five-file scaffold, candidate-only queue rule, runtime loading boundary, owner/validator expectations, and score scale|
|5|`docs/LEARNING_SYSTEM.md`|Apex learning boundary|read|defines project-to-meta learning write-down, candidate routing, and separation from accepted truth|
|6|`managed/agent_kb/AGENT_KB_INDEX.md`|Apex agent KB index|read|maps first-wave agent KB roots, owner/validator expectations, and companion docs|
|7|`ApexAI_OS_Federated_Orchestration_Handover.md`|architecture evidence|read|supports meta/project learning flow, project isolation, release-pack logic, and non-contamination rules|
|8|`releases/meta-release-v0.1/MANIFEST.md`|release-pack evidence|read|supports release-shaped downstream packaging rather than uncontrolled sync|
|9|`managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`|promotion packet surface|not fully reread in this pass|referenced as current governed candidate packaging surface|
|10|Historical MasterOfArts source ledgers referenced by new base|lineage evidence|preserved|kept as provenance/source lineage; not used as active target repo|

## Indexed Knowledge Bank slice

The new baseline lists this agent as owning a KB build slice centered on:

- ranked KB candidate selection
- corpus inventory and duplicate handling
- normalized idea extraction
- role and KB target mapping
- compact essence candidates
- failure and anti-drift safeguards
- improvement capture
- resilient migration / continuity process guidance

The Apex integration adds the system placement context centered on:

- `managed/agent_kb/special_ops__knowledge_bank/` as the Apex meta KB root
- `managed/knowledge/` as shared KB governance
- `managed/processes/` as process-contract host
- project-to-meta sanitized LearningCandidate flow
- meta-to-project reviewed release-pack delta flow
- raw project-data exclusion from meta KB surfaces

## New-base discovery and identity map

|physical_new_base_path|detected_h1|intended_target_file|confidence|action|
|---|---|---|---|---|
|`newversions/ESSENCE.md`|`# BEST_PRACTICES`|`BEST_PRACTICES.md`|heading_match_clear|standard path already contained same new-base body; Apex deltas patched into standard path|
|`newversions/BEST_PRACTICES.md`|`# APPENDIX_KB_SOURCE_MANIFEST`|`appendices/APPENDIX_KB_SOURCE_MANIFEST.md`|heading_match_clear|standard path already contained same new-base body; Apex integration source rows patched|
|`newversions/MISTAKES.md`|`# LEARNING_QUEUE`|`LEARNING_QUEUE.md`|heading_match_clear|standard path already contained same new-base body; Apex candidates patched|
|`newversions/LEARNING_QUEUE.md`|`# ESSENCE`|`ESSENCE.md`|heading_match_clear|standard path already contained same new-base body; Apex placement deltas patched|
|`newversions/TEMPLATES.md`|`# TEMPLATES`|`TEMPLATES.md`|path_match|Apex LearningCandidate and release-delta templates patched|
|`newversions/APPENDIX_KB_SOURCE_MANIFEST.md`|`# APPENDIX_KB_INFORMATION_RANKING_LEDGER`|`appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`|heading_match_clear|standard path already contained same new-base body; no direct Apex delta needed in this pass|
|`newversions/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md`|`# APPENDIX_KB_CANDIDATE_LEDGER`|`appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`|heading_match_clear|standard path already contained same new-base body; no direct Apex delta needed in this pass|
|`newversions/APPENDIX_KB_CANDIDATE_LEDGER.md`|`# APPENDIX_KB_ANTI_DRIFT_EVIDENCE`|`appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|heading_match_clear|standard path already contained same new-base body; no direct Apex delta needed in this pass|
|`newversions/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|missing file|`appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`|missing|standard path contains anti-drift body mapped from misnamed candidate-ledger file|
|`newversions/PROMPTFLOW_KB_BASE_BUILD.md`|promptflow artifact|non-target|non_kb_artifact|kept as provenance only|
|`newversion/`|folder absent|none|missing|no action|

## Top-ranked candidate coverage

|rank|candidate_id|covered|source_role|manifest_status|
|---|---:|---|---|---|
|1|`KB-META-OPS-001`|yes|process / staged-file protocol evidence|represented in ranking and candidate ledgers|
|2|`KB-META-OPS-023`|yes|density-gate failure evidence|represented in ranking and anti-drift ledgers|
|3|`KB-CODEX-EXECUTION-PROCESS-077`|yes|patch evidence / open-question correction|represented in candidate and anti-drift ledgers|
|4|`KB-CODEX-EXECUTION-PROCESS-031`|yes|required validation / improvement capture|represented in ranking, candidate, and template targets|
|5|`KB-META-OPS-009`|yes|typed bullet classes|represented as reusable structure signal|
|6|`KB-META-OPS-014`|yes|instruction block / cold-start viability|represented as scaffold and template input|
|7|`KB-META-OPS-025`|yes|waterfall critique|represented as mistake and adaptive-build guard|
|8|`KB-META-OPS-034`|yes|anti-drift rule|represented as anti-drift evidence|
|9|`KB-PROMPTS-WORKFLOWS-032`|yes|critical-doc blind-updater risk|represented as mistake and scaffold density guard|
|10|`KB-CODEX-EXECUTION-PROCESS-107`|yes|live-status / operating-spine preservation evidence|represented as evidence-only item|
|11|`KB-CODEX-EXECUTION-PROCESS-114`|yes|freeze / QA-hygiene evidence|represented as evidence-only item|
|12|`KB-META-OPS-004`|yes|swarm scope boundary|represented as boundary input|

## Role-fit validation

|role_dimension|finding|status|
|---|---|---|
|KB architecture|Role map assigns Knowledge Bank ownership over KB structure, layering, ownership, and cross-agent coherence.|fit|
|Lifecycle routing|Role map assigns capture, candidate, and promotion routing safeguards but with explicit non-ownership of final approval.|fit|
|Appendix architecture|Promptflow requires deep body in appendices and thin scaffold files.|fit|
|Candidate status|Ledgers classify material as candidate, strong_candidate, evidence, or safeguard rather than accepted shared truth.|fit|
|Validation partner|Role map and Apex lane index identify `special_ops__informatics_design` as the structural validator.|fit|
|Apex meta/project learning|Apex sources assign this lane placement/readiness responsibility, not final promotion approval.|fit|
|Release-pack routing|Apex sources support reviewed release-pack deltas rather than uncontrolled sync.|fit|

## Exclusion register

|excluded_source_or_class|reason|status|
|---|---|---|
|Other Special Ops agent source slices|non-target for this promptflow|excluded|
|Shared governance files outside the agent KB root|read as Apex deltas only; not mutated by this lane|excluded from writes|
|Runtime config and provider/model config|explicitly out of scope for Knowledge Bank integration|excluded|
|Raw project data|violates Apex project isolation and non-contamination boundary|excluded|
|Unindexed broad repo traversal|not justified because target promptflow plus Apex governance files were sufficient|excluded|
|Failure/postmortem source material|used as evidence and safeguards only|included as evidence, not doctrine|

## Duplication handling

- **Rule:** same-filename and exact-duplicate variants are recorded once at candidate level.
- **Applied handling:** source inventory duplicate notes are preserved as source metadata, but scaffold files point to candidate IDs and appendices rather than duplicating every variant.
- **Representative path policy:** when the inventory identifies a representative or unique path, use the ledger candidate ID as the stable citation handle in this KB base.
- **Apex policy:** repeated Apex concepts are captured only where operationally needed: boundary in `ESSENCE.md`, operating rules in `BEST_PRACTICES.md`, failure modes in `MISTAKES.md`, candidate items in `LEARNING_QUEUE.md`, and packet forms in `TEMPLATES.md`.

## Index gap register

|gap_id|gap|materiality|disposition|
|---|---|---|---|
|GAP-001|Manual local files in the previous index are not repo-accessible in this single-repo execution context.|low for this build|No stop. The top-ranked Knowledge Bank slice is represented by repo-accessible ledgers and supporting files.|
|GAP-002|Some ledger rows reference historic `AllAIBestPractice` source paths rather than current repo-relative file locations.|medium|Handled by using ledger candidate IDs and repo-accessible ledger files as the stable source surface for this KB base.|
|GAP-003|`newversions/` files include filename/H1 mismatches and missing `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` physical file.|medium|Resolved by H1/content identity mapping and standard-path verification; do not use filename alone.|
|GAP-004|Dedicated local source-notes and promotion-trace appendices are not present.|medium|Captured as `LQ-KB-008`; defer until validator decides whether shared managed knowledge surfaces are sufficient.|

## Plausibility verdict

- **Coverage:** pass. Top-ranked `special_ops__knowledge_bank` candidates are represented.
- **Apex compatibility:** pass with bounded deltas. Project-to-meta learning, release-pack readiness, and raw-project-data exclusion are represented.
- **Role fit:** pass. Source slice maps to KB lifecycle, appendices, candidate routing, and anti-sprawl safeguards.
- **Exclusion fit:** pass. Non-target slices, runtime config, and raw project data are excluded.
- **Duplication:** pass. Duplicate variants are collapsed to candidate IDs and source-ledger handles.
- **Gap risk:** pass with bounded caveat. Newversions naming mismatch is recorded; no material gap blocks standard-path use.
- **Authority risk:** pass. Evidence-only material remains evidence-only; this lane does not approve promotion or mutate shared governance.

## Build consequence

Use the standard-path files as the Apex-integrated new Knowledge Bank base. Future changes should patch only valid Apex deltas or validator-approved candidate promotions.
