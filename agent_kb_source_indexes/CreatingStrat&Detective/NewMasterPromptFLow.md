# Prompt Flow Package — Meta Heads KB Update, One By One

Use this as the new clean flow. Start with **Meta Strategy**, then repeat for **Meta Detective**.

## 0. Operator Setup

```
# Operator Setup — Meta Heads KB UpdateWe are working only in:- repo: `leela-spec/MasterOfArts`- branch: `main` unless explicitly changed by the operatorDo not write to Apex AI.Do not access or patch an Apex AI repo.Do not run a two-repo workflow.Current goal:Update/create a solid KB and compact seed for two meta heads, one by one:1. `meta_strategy`2. `meta_detective`Current target paths in MasterOfArts:- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/`- `OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md`- `OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md`Working method:Create a temporary mirror/staging packet inside MasterOfArts first. The staging packet must mirror the real final target paths exactly, but it must not replace final files until the audit and file-by-file patch plan passes.Recommended staging root:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/`Inside it, mirror the final target tree:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/``OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/``OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md``OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md`Hard boundaries:- No Special Ops KB creation.- No Alfred KB changes.- No Meta Ops KB changes unless only used as source/context.- No domain masters.- No runtime config changes.- No `openclaw.json` changes.- No broad architecture rewrite.- No Apex AI writes.
```

---

## 1. Master Controller Prompt

```
# Meta Heads KB Controller — MasterOfArts OnlyYou are operating as a careful KB update controller inside the private repo `leela-spec/MasterOfArts`.## MissionCreate or update a solid, source-grounded KB and compact seed for exactly two meta heads:1. `meta_strategy`2. `meta_detective`We do them one by one.## Current work modeThis is not a two-repo task.You must work only in `leela-spec/MasterOfArts`.Do not write to Apex AI.Do not mention Apex AI as a current write target.Do not create instructions that assume Apex AI access.Only after this packet is complete may a separate later migration copy the final packet to another repo.## Target filesFor `meta_strategy`:- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/ESSENCE.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/BEST_PRACTICES.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/MISTAKES.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/TEMPLATES.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/LEARNING_QUEUE.md`- `OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md`For `meta_detective`:- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/ESSENCE.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/BEST_PRACTICES.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/MISTAKES.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/TEMPLATES.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/LEARNING_QUEUE.md`- `OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md`## Staging packetBefore touching the real target files, create or update this staging packet:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/`Required staging files:- `README.md`- `SOURCE_READ_LOG.md`- `CURRENT_STATE_AUDIT.md`- `ROLE_BOUNDARY_MATRIX.md`- `PATCH_BACKLOG.md`- `VALIDATION_REPORT.md`Required staging mirror:- `mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/`- `mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/`- `mirror/OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md`- `mirror/OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md`The staging mirror must contain the proposed final versions of the exact target files.## KB scaffold ruleEach meta-head KB folder uses exactly:1. `ESSENCE.md`2. `BEST_PRACTICES.md`3. `MISTAKES.md`4. `TEMPLATES.md`5. `LEARNING_QUEUE.md`No `AGENT_CARD.md`.No `SOURCE_MANIFEST.md` unless the repo already requires it for this exact folder.No `COVERAGE_AUDIT.md` unless the repo already requires it for this exact folder.No `DOCTRINE.md`, `ROLE_BOUNDARIES.md`, `ROUTING_CONTRACT.md`, `HANDOFF_SCHEMA.md`, or `WORKFLOW_PLAYBOOK.md` unless already present and explicitly required by the current repo convention.If such extension files already exist, do not delete them automatically. Mark them in the audit as:- canonical- extension- stale- duplicate- needs human decision## Source authority rulesUse this hierarchy:1. Current final-system files under `OpenClaw/07_finalopenclawsystem/managed/`2. Current final-system docs under `OpenClaw/07_finalopenclawsystem/docs/`3. Current user/system entrypoints under `OpenClaw/07_finalopenclawsystem/user/`4. Binding lock / decision / governance files under `NewFinals/NextLevel2/`, as evidence only5. Resource-screening ledgers, as evidence and source-routing support6. Old prompts, old drafts, failure logs, and research files, as evidence onlyDo not turn source/staging material into runtime truth.Do not copy raw source dumps into KB files.Do not promote unvalidated claims into accepted KB files.Put unvalidated but useful material in `LEARNING_QUEUE.md`.## Role boundaries`meta_strategy` owns:- option framing- scenario comparison- timing logic- leverage analysis- recommendation packets- tradeoff framing- decision-structure clarity`meta_strategy` does not own:- execution control- patch application- direct promotion- operator override- config authority- adversarial validation`meta_detective` owns:- adversarial validation- contradiction surfacing- plausibility checks- authority checks- drift detection- escalation recommendation`meta_detective` does not own:- primary execution- patch application- generic cleanup- orchestration control- direct promotion- strategy ownershipShared boundary:- Strategy proposes and frames.- Detective challenges and validates.- Neither silently mutates truth.- Neither bypasses promotion rules.- Neither patches config.## Process phasesRun the phases in order:1. Scope and source lock2. Current-state audit3. Role-boundary audit4. Staging mirror creation5. Single-agent KB synthesis6. Single-agent seed synthesis7. Red-team validation8. One-file-at-a-time final patch plan9. Apply only approved final patches10. Final verification reportStop after each phase with a compact checkpoint.Do not ask for confirmation unless a hard blocker exists.
```

---

# 2. Phase Prompts

## Phase 1 — Scope and Source Lock

```
# Phase 1 — Scope And Source LockTask:Lock scope before writing anything.Rules:- Do not patch final target files.- Do not create the final KB files yet.- You may create/update only the staging packet under:  `OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/`Inspect these current final-system files first:- `OpenClaw/07_finalopenclawsystem/managed/agents/AGENT_INDEX.md`- `OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md`- `OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/AGENT_KB_INDEX.md`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/`- `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/`- `OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md`- `OpenClaw/07_finalopenclawsystem/managed/knowledge/AGENT_KB_LANES.md`- `OpenClaw/07_finalopenclawsystem/managed/knowledge/OVERLAP_VALIDATION_MATRIX.md`- `OpenClaw/07_finalopenclawsystem/managed/processes/AGENT_HANDOFF_CONTRACTS.md`- `OpenClaw/07_finalopenclawsystem/managed/processes/HOLDING_ORCHESTRATION_FLOW.md`Then inspect source/staging evidence only as needed:- `OpenClaw/07_finalopenclawsystem/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md`- `OpenClaw/07_finalopenclawsystem/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md`- `OpenClaw/07_finalopenclawsystem/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md`- `OpenClaw/07_finalopenclawsystem/NewFinals/ResourceScreeningLedgers/OPEN_QUESTIONS_AND_BLOCKERS.md`- relevant role/decision/lock files under `NewFinals/NextLevel2/`Output:1. `SCOPE_LOCK`   - repo   - branch   - exact target agents   - exact target files   - explicit non-goals2. `SOURCE_READ_LOG`   - path   - exists yes/no   - read mode: full / partial / skipped / blocked   - role: final-system / governance / process / staging-evidence / failure-evidence   - notes3. `BLOCKERS`   - missing files   - inaccessible files   - ambiguous repo state   - convention conflicts4. `NEXT_PHASE_DECISION`   - proceed / stop   - reason
```

---

## Phase 2 — Current-State Audit

```
# Phase 2 — Current-State AuditTask:Audit the exact current state of the target files before synthesis.Rules:- Do not patch final target files.- Read every current target file fully.- If a target file is missing, mark it as `missing_create_needed`.- If a target folder exists but lacks scaffold files, mark the exact missing files.- Do not assume the old prompt’s eight-file scaffold.Audit exactly:For `meta_strategy`:- `managed/agent_kb/meta_strategy/ESSENCE.md`- `managed/agent_kb/meta_strategy/BEST_PRACTICES.md`- `managed/agent_kb/meta_strategy/MISTAKES.md`- `managed/agent_kb/meta_strategy/TEMPLATES.md`- `managed/agent_kb/meta_strategy/LEARNING_QUEUE.md`- `managed/agents/meta_strategy.md`For `meta_detective`:- `managed/agent_kb/meta_detective/ESSENCE.md`- `managed/agent_kb/meta_detective/BEST_PRACTICES.md`- `managed/agent_kb/meta_detective/MISTAKES.md`- `managed/agent_kb/meta_detective/TEMPLATES.md`- `managed/agent_kb/meta_detective/LEARNING_QUEUE.md`- `managed/agents/meta_detective.md`Output:1. `FILE_INVENTORY`   - path   - exists yes/no   - current size   - current status: accepted / candidate / empty / stale / malformed / missing   - inferred owner   - inferred validator2. `CONTENT_DIAGNOSIS`   - path   - useful existing content   - stale content   - overpromoted claims   - missing doctrine   - missing source posture   - missing role boundary   - candidate/canon leakage3. `PATCH_NEED_CLASSIFICATION`   - keep as-is   - light patch   - full rewrite   - create missing   - move to learning queue   - human decision needed4. `NEXT_PHASE_DECISION`
```

---

## Phase 3 — Role-Boundary Audit

```
# Phase 3 — Meta Strategy / Meta Detective Boundary AuditTask:Prevent role collapse before generating new KB content.Rules:- Keep `meta_strategy` and `meta_detective` sharply distinct.- Strategy frames options and recommendations.- Detective validates, challenges, blocks, or escalates.- Do not let Detective become a generic cleanup agent.- Do not let Strategy become an executor or validation authority.Output:1. `ROLE_BOUNDARY_MATRIX`| Capability | meta_strategy | meta_detective | Shared? | Boundary rule ||---|---|---|---|---|Must cover:- option framing- scenario comparison- timing- leverage- recommendation packet- source authority verification- contradiction detection- drift detection- validation gates- escalation- patch application- promotion authority- config authority- operator override2. `HANDOFF_RULES`   - strategy asks detective for audit   - detective escalates strategic ambiguity   - joint decision memo boundaries3. `FAILURE_MODES_TO_PREVENT`   - role collapse   - self-promotion   - generic advice   - source laundering   - candidate/canon mixing   - stale prompt residue   - cross-agent contamination4. `ACCEPTANCE_CRITERIA`   - what must be true before writing final target files
```

---

# 3. Agent-Specific Synthesis Prompts

## 3A. Meta Strategy — KB First

```
# Meta Strategy KB SynthesisWork on one agent only:`meta_strategy`Do not write or modify `meta_detective` files except as source/context for validator relationship.Target KB folder:`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/`Required files:1. `ESSENCE.md`2. `BEST_PRACTICES.md`3. `MISTAKES.md`4. `TEMPLATES.md`5. `LEARNING_QUEUE.md`Write first to staging mirror only:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/`Meta Strategy identity:- strategic option framing- timing logic- leverage analysis- scenario comparison- recommendation packets- decision-quality improvement- architecture/tradeoff framingMeta Strategy must not:- execute changes- apply patches- validate itself- override operator constraints- mutate config- promote its own candidates- become Meta Ops- become Meta DetectiveFile requirements:## ESSENCE.mdMust contain:- purpose- agent boundary- owns- does not own- read when- core constraints- validator relationship- evidence/status block## BEST_PRACTICES.mdMust contain:- durable practices for framing options- decision packet structure- tradeoff analysis rules- reversibility and dependency surfacing- when to request Detective review- anti-drift practices## MISTAKES.mdMust contain:- known failure modes- how strategy drifts into execution- how strategy overgeneralizes- how strategy hides assumptions- how strategy ignores source authority- correction pattern for each mistake## TEMPLATES.mdMust contain:- option comparison memo- recommendation packet- strategy-to-detective audit request- strategic ambiguity escalation- joint decision memo draft## LEARNING_QUEUE.mdMust contain:- candidate-only entries- no accepted doctrine- no proof of promotion- fields:  - candidate_id  - claim  - source_basis  - why_candidate  - validation_needed  - validator  - promotion_target  - statusOutput:1. full staged file bodies2. source basis table3. candidate/canon separation check4. role-boundary check5. open questions6. recommended one-file final patch order
```

---

## 3B. Meta Strategy — Seed First/Second Pass

```
# Meta Strategy Seed SynthesisWork on exactly one file:`OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md`Write first to staging mirror:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md`Seed purpose:Compact activation spec only.Do not put rich doctrine into the seed.Do not put long examples into the seed.Do not put learning queue content into the seed.Do not cite staging files as runtime truth.Required compact seed sections:1. `# Meta Strategy`2. `## Purpose`3. `## Owns`4. `## Does Not Own`5. `## Activation Triggers`6. `## Inputs`7. `## Outputs`8. `## Handoff Partners`9. `## Validation Partner`10. `## KB Pointer`11. `## Failure Safeguards`12. `## Boundary Note`Must include:- validation partner: `meta_detective`- KB pointer: `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/`- clear non-executor boundary- no direct promotion authority- no config authorityOutput:1. staged final seed body2. compactness check3. rich-doctrine exclusion check4. validator check5. final patch readiness verdict
```

---

## 3C. Meta Detective — KB First

```
# Meta Detective KB SynthesisWork on one agent only:`meta_detective`Do not write or modify `meta_strategy` files except as source/context for strategy/detective handoff.Target KB folder:`OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/`Required files:1. `ESSENCE.md`2. `BEST_PRACTICES.md`3. `MISTAKES.md`4. `TEMPLATES.md`5. `LEARNING_QUEUE.md`Write first to staging mirror only:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/`Meta Detective identity:- adversarial validation- authority checks- contradiction detection- drift detection- plausibility pressure- source/candidate/canon separation pressure- stop/hold/escalation recommendationsMeta Detective must not:- execute patches- rewrite the artifact under review silently- own generic cleanup- become Hygiene Clean- become Meta Ops- own strategy- promote its own findings- mutate configFile requirements:## ESSENCE.mdMust contain:- purpose- agent boundary- owns- does not own- read when- core constraints- validator relationship- evidence/status block## BEST_PRACTICES.mdMust contain:- validation method- source authority check- contradiction check- drift check- evidence quality check- stop/hold/escalation practice- when to route structural issues to Hygiene Clean## MISTAKES.mdMust contain:- known failure modes- becoming executor- silent rewriting- overblocking without evidence- treating suspicion as proof- confusing cleanup with validation- correction pattern for each mistake## TEMPLATES.mdMust contain:- detective audit report- contradiction register- source authority challenge- drift finding- stop/hold/escalation memo- detective-to-strategy ambiguity escalation- joint decision memo review## LEARNING_QUEUE.mdMust contain:- candidate-only entries- no accepted doctrine- no proof of promotion- fields:  - candidate_id  - claim  - source_basis  - why_candidate  - validation_needed  - validator  - promotion_target  - statusOutput:1. full staged file bodies2. source basis table3. candidate/canon separation check4. role-boundary check5. open questions6. recommended one-file final patch order
```

---

## 3D. Meta Detective — Seed First/Second Pass

```
# Meta Detective Seed SynthesisWork on exactly one file:`OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md`Write first to staging mirror:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md`Seed purpose:Compact activation spec only.Do not put rich doctrine into the seed.Do not put long examples into the seed.Do not put learning queue content into the seed.Do not cite staging files as runtime truth.Required compact seed sections:1. `# Meta Detective`2. `## Purpose`3. `## Owns`4. `## Does Not Own`5. `## Activation Triggers`6. `## Inputs`7. `## Outputs`8. `## Handoff Partners`9. `## Validation Partner`10. `## KB Pointer`11. `## Failure Safeguards`12. `## Boundary Note`Must include:- validation partner: `special_ops__hygiene_clean`- KB pointer: `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/`- clear adversarial-validation boundary- non-executor boundary- no direct promotion authority- no config authorityOutput:1. staged final seed body2. compactness check3. rich-doctrine exclusion check4. validator check5. final patch readiness verdict
```

---

# 4. Red-Team Validation Prompt

Run this after each single-agent staged packet.

```
# Red-Team Validation — One Agent OnlyValidate the staged packet for:Agent:`[meta_strategy OR meta_detective]`Staging root:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/`Rules:- Do not patch final target files.- Compare staged files against current final target files.- Validate one agent only.- Do not let source/staging material become runtime truth.- Do not allow candidate material into accepted files.- Do not allow accepted doctrine into `LEARNING_QUEUE.md`.Checks:1. `SCAFFOLD_CHECK`   - exactly five KB files   - no extra required files invented   - seed is separate from KB2. `ROLE_BOUNDARY_CHECK`   - owns / does-not-own correct   - no Strategy/Detective collapse   - no Meta Ops contamination   - no Hygiene Clean contamination3. `CANDIDATE_CANON_CHECK`   - accepted files contain only validated doctrine   - learning queue is candidate-only   - no self-promotion4. `SOURCE_AUTHORITY_CHECK`   - final-system files outrank staging files   - evidence-only sources not treated as canon   - contradictions preserved or routed5. `PATCH_SAFETY_CHECK`   - every final patch target is exact   - no config mutation   - no unrelated files touched   - no Apex AI references as current write target6. `QUALITY_CHECK`   - dense, operational, specific   - no generic AI advice   - useful without rereading all source files   - examples/templates are actionable   - known failure modes are concreteOutput:1. `PASS_FAIL_SUMMARY`2. `CRITICAL_DEFECTS`3. `SERIOUS_DEFECTS`4. `MINOR_FIXES`5. `REQUIRED_REPAIRS`6. `PATCH_READINESS_VERDICT`If critical defects exist, do not proceed to final patching.
```

---

# 5. One-File Final Patch Prompt

Use only after the staged mirror passes validation.

```
# One-File Final Patch — MasterOfArtsPatch exactly one final target file.Repo:`leela-spec/MasterOfArts`Branch:`main` unless operator specified otherwise.Target file:`[EXACT_PATH]`Staged source file:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/mirror/[EXACT_PATH]`Rules:1. Read the current final target file.2. Read the staged source file.3. Produce the minimal exact patch needed.4. Patch only this file.5. Do not touch any other file.6. Do not patch Apex AI.7. Do not patch config.8. Do not patch source/staging except the staging packet itself if recording status.9. Preserve useful existing content if it does not conflict.10. Fetch/read back the patched file after writing.11. Verify the final content matches the intended staged content or explain any deliberate difference.Output:1. `TARGET_FILE`2. `OPERATION`   - create / replace / update3. `WHY_THIS_PATCH`4. `SOURCE_BASIS`5. `PATCH_APPLIED`6. `POST_PATCH_VERIFICATION`7. `REMAINING_RISK`8. `NEXT_FILE_TO_PATCH`Stop after this one file.
```

---

# 6. Recommended Patch Order

## Meta Strategy

```
1. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/ESSENCE.md2. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/BEST_PRACTICES.md3. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/MISTAKES.md4. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/TEMPLATES.md5. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/LEARNING_QUEUE.md6. OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md
```

## Meta Detective

```
1. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/ESSENCE.md2. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/BEST_PRACTICES.md3. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/MISTAKES.md4. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/TEMPLATES.md5. OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/LEARNING_QUEUE.md6. OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md
```

---

# 7. Final Verification Prompt

```
# Final Verification — Meta Heads KB UpdateVerify the completed MasterOfArts update.Scope:- `meta_strategy`- `meta_detective`Final target files:- all five KB files for `meta_strategy`- seed file for `meta_strategy`- all five KB files for `meta_detective`- seed file for `meta_detective`Rules:- Do not patch unless a critical verification defect is found.- Do not inspect or modify Apex AI.- Do not add other agents.- Do not rewrite broad architecture.- Verify current repo state only.Output:1. `FINAL_FILE_INVENTORY`| Path | Exists | Status | Owner | Validator | Notes ||---|---:|---|---|---|---|2. `SCAFFOLD_VERIFICATION`   - five KB files per agent   - compact seed per agent   - KB pointer present in seed   - validator present in seed3. `BOUNDARY_VERIFICATION`   - Strategy remains recommendation-only   - Detective remains validation-only   - no execution ownership drift   - no promotion authority drift   - no config authority drift4. `CANDIDATE_CANON_VERIFICATION`   - accepted doctrine files contain accepted content only   - `LEARNING_QUEUE.md` candidate-only   - no candidate material promoted without validation5. `SOURCE_POSTURE_VERIFICATION`   - final-system files used as highest authority   - staging/source material used only as evidence   - contradictions not silently smoothed over6. `PATCH_SUMMARY`   - files created   - files updated   - files untouched   - blocked files   - remaining open questions7. `APEX_HANDOFF_PACKET`   - exact list of final files that can later be copied or patched into Apex AI   - no Apex write performed   - notes for future cross-repo migration
```

---

## Practical starting command for the next chat

Paste this first:

```
Run Phase 1 — Scope And Source Lock for the Meta Heads KB update.Use only `leela-spec/MasterOfArts`.Do not patch Apex AI.Do not patch final target files yet.Create or update only the staging packet under:`OpenClaw/07_finalopenclawsystem/NewFinals/MetaHeadsKBUpdateState/`We will update agents one by one:1. `meta_strategy`2. `meta_detective`Start by inspecting the current managed files and producing `SCOPE_LOCK`, `SOURCE_READ_LOG`, `BLOCKERS`, a
```