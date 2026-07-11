# Previous Run and Signal Comparison

## Inputs

- Previous output: `apex-meta/kb/old-apex-full-orchestration-agent-kb`
- Authoritative corpus: `ApexDefinition&OldVersions/OldApexFullOrchestrationSystem`
- Corrected output: `apex-meta/kb/old-apex-full-orchestration-agent-kb-v2`

## Previous Run Findings

- The previous KB had 2 manifest sources and no source-payload manifest.
- Previous status reported stale retrieval.
- Previous quality reported 16 repair candidates across 18 wiki pages.
- Previous lint reported 73 issues, including missing frontmatter fields, missing canonical directories, orphan pages, and missing Phase 2 value sections.
- Previous pages were structurally present but under-indexed the full old-system corpus.

## Signal-Word Reassessment

Phase 0 scanned 418 source files. The highest raw terms included `agent`, `source`, `file`, `evidence`, and `ops`, while `https`, `com`, and repository/vendor names were high-frequency noise. The v2 topic registry therefore uses semantic clusters rather than blindly copying the previous run’s signal words:

1. Agent architecture: agent, role, skill, foundation, overlap, routing, handoff, validator.
2. Resilient workflows: workflow, macro, meso, micro, iteration, orchestration, sequence, coordination.
3. Failure evidence: failure, mistake, audit, log, research, drift, recovery, validation.

## Highest-Impact Conflict Ranking

1. Final-system truth versus mirror/staging material — highest risk because it can canonize obsolete behavior.
2. Role authority versus operational state — high risk because it can grant permissions that the current state does not allow.
3. Builder versus verifier responsibility — high risk because self-review can promote defects.
4. Conservative single-flow doctrine versus historical swarm experiments — high architectural risk because concurrency assumptions change routing and safety.
5. Source custody versus copied or summarized evidence — high epistemic risk because claims become impossible to recheck.

Each conflict is preserved in `wiki/audit/high-impact-conflict-register.md` with authority, risk, and disposition requirements.
