# MISTAKES

## Purpose

Accepted validated Knowledge Bank failure patterns and countermeasures.

## Entry schema

```yaml
mistake_entry:
  id:
  status: accepted | deprecated
  pattern:
  trigger_conditions:
  countermeasure:
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  review_due:
```

## Accepted mistake patterns

### M-KB-001 — Candidate-to-canon leak

```yaml
mistake_entry:
  id: M-KB-001
  status: accepted
  pattern: Candidate material is copied into scaffold or release-ready prose without visible candidate status, validator route, or promotion boundary.
  trigger_conditions:
    - high-scoring candidate is treated as accepted because it appears in a ledger
    - project learning arrives in meta and is treated as reusable truth by storage alone
    - scaffold prose references candidate evidence without promotion caution
  countermeasure: Keep candidate, evidence, accepted KB guidance, and runtime truth visibly separated; route promotions through the governed promotion path.
  evidence_refs:
    - appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
    - appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md
    - managed/knowledge/AGENT_KB_LANES.md
    - docs/LEARNING_SYSTEM.md
  scores:
    EVD: 90
    IMP: 95
    RSK: 25
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  review_due: 2026-07-25
```

### M-KB-002 — Raw project learning copied into meta KB

```yaml
mistake_entry:
  id: M-KB-002
  status: accepted
  pattern: Project-local data, raw context, or sensitive examples are copied into the Apex meta Knowledge Bank instead of being sanitized into generalized candidate learning.
  trigger_conditions:
    - project repo findings are moved into meta without redaction or generalization
    - coaching, investment, community, app, personal, or secret context appears in shared KB files
    - the meta repo is used as a cross-project memory dump
  countermeasure: Store raw project material only in the project repo; meta receives only sanitized LearningCandidate packets with owner, validator, source status, and promotion route.
  evidence_refs:
    - docs/LEARNING_SYSTEM.md
    - managed/knowledge/AGENT_KB_LANES.md
    - ApexAI_OS_Federated_Orchestration_Handover.md
  scores:
    EVD: 88
    IMP: 96
    RSK: 20
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  review_due: 2026-07-25
```

### M-KB-003 — Uncontrolled meta-to-project KB sync

```yaml
mistake_entry:
  id: M-KB-003
  status: accepted
  pattern: Meta KB improvements are copied directly into project repos as raw folders or full history instead of reviewed release-pack deltas.
  trigger_conditions:
    - full meta KB folders are pushed into a project without release selection
    - appendices or source history are copied where only a lean runtime pack is needed
    - release-back bypasses project adopt/defer/reject trace
  countermeasure: Package KB changes as reviewed meta release deltas; include only the lean base and selected appendices needed by the project.
  evidence_refs:
    - managed/knowledge/AGENT_KB_LANES.md
    - releases/meta-release-v0.1/MANIFEST.md
    - ApexAI_OS_Federated_Orchestration_Handover.md
  scores:
    EVD: 86
    IMP: 92
    RSK: 30
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  review_due: 2026-07-25
```

### M-KB-004 — Apex architecture absorbed into local KB doctrine

```yaml
mistake_entry:
  id: M-KB-004
  status: accepted
  pattern: Broad ApexAI_OS architecture doctrine is copied wholesale into this lane, causing Knowledge Bank to absorb MetaOps, process, routing, or governance authority.
  trigger_conditions:
    - MetaOps orchestration logic is stored as Knowledge Bank doctrine
    - runtime configuration, process contracts, or shared governance files are mutated through this lane
    - Apex architecture reports are pasted into scaffold files instead of represented as bounded deltas
  countermeasure: Keep this lane to KB placement, candidate routing, source manifesting, appendix architecture, and release-readiness; route orchestration to MetaOps, process law to managed processes, and governance to managed knowledge.
  evidence_refs:
    - managed/agent_kb/AGENT_KB_INDEX.md
    - managed/knowledge/AGENT_KB_LANES.md
    - PROMPTFLOW_KB_INTEGRATION_FINAL.md
  scores:
    EVD: 90
    IMP: 88
    RSK: 35
  owner: special_ops__knowledge_bank
  validator: special_ops__informatics_design
  review_due: 2026-07-25
```

## Non-promoted legacy note

If a future run recovers a missing or misnamed new-base `MISTAKES.md` from `newversions/`, compare it by H1/content identity before replacing this file. Do not use filename alone.
