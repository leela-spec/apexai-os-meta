# Apex KB Phase 0 First Real Test Handover

## Purpose

Use a new operator-facing orchestrator chat to verify the current Phase 0 Setup implementation against the real Leela repository, then stop before deterministic corpus intelligence begins.

## Canonical inputs

Read completely from current `main`:

1. `PHASE-0-DOWNSTREAM-IMPACT-HANDOVER.md`
2. `patches/PHASE-0-SEMANTIC-DEPTH-AND-GIT-SYNC.exact-match.md`
3. `templates/start-qa-option-a-v3-example-guidance.md`
4. `.claude/skills/apex-kb/references/start-input.schema.json`
5. `apex-meta/scripts/apex_kb_start.py`
6. `apex-meta/scripts/apex_kb_control.py`
7. `apex-meta/scripts/tests/test_apex_kb_start.py`

## Test target

```yaml
apex_repository: leela-spec/apexai-os-meta
leela_repository: leela-spec/leela
source_folder: LeelaAppDevelopment
kb_destination: operator_confirmation_required
stop_after: phase_0_setup
```

## Required results

The new chat must:

- verify every proposed exact-match edit against live file text before any change;
- run the Start and control-plane tests;
- verify primary-main and linked-worktree behavior without combining worktree content;
- preserve existing local changes;
- report synchronization status without hiding failures;
- inspect and present Leela destination candidates;
- obtain operator confirmation of one destination and one complete Start configuration;
- run a no-write Start preview;
- after confirmation, create and reread only the Setup artifacts;
- stop before deterministic corpus intelligence.

## Locked interpretation

- Deterministic corpus intelligence always runs fully.
- `quick`, `standard`, and `deep` control later semantic execution only.
- Non-text policy is preserved by Setup and consumed by the deterministic corpus module.
- `analysis_only` stops after semantic analysis.
- `compiled_kb` adds compiled pages and independent acceptance.
- `query_ready` additionally builds and verifies retrieval.

## Final report

Return the runtime commit, patch verification, tests, selected Leela destination, Start preview, confirmation state, created Setup artifacts, worktree and synchronization evidence, blockers, and Phase 1 handover readiness. Then stop for the operator decision.
