# Phase 0 Downstream Handover Update — Start Wrapper Flag Reachability

```yaml
update_id: phase-0-downstream-start-wrapper-flag-reachability
status: unresolved_pre_existing_blocker
scope: phase_0_public_start_entrypoint
introduced_by_latest_patch_pack: false
applies_to:
  - Phase 1 design and implementation
  - Phase 2 design and implementation
  - Phase 3 design and implementation
source_handover: PHASE-0-DOWNSTREAM-IMPACT-HANDOVER.md
```

## Purpose

Record a known pre-existing mismatch in the public Apex KB Start entrypoint so later-module agents do not assume the documented invocation contract is already executable end to end.

## Blocker

The newly documented `start_invocation_pattern` in:

```text
.claude/skills/apex-kb/references/script-command-contract.md
```

references these public Start flags:

```text
--allow-write
--dry-run
--strict
--json
```

The implementation status is split:

- `apex-meta/scripts/apex_kb_start.py` implements these flags.
- The public wrapper subcommand in `apex-meta/scripts/apex_kb.py` currently forwards only:
  - `--config`
  - `--repo-root`
- Therefore the four flags above are not currently reachable through the documented public command surface:

```text
python apex-meta/scripts/apex_kb.py start ...
```

## Required follow-up

Before relying on the documented Start invocation pattern, patch the `start` subparser in:

```text
apex-meta/scripts/apex_kb.py
```

so it accepts and forwards:

```text
--allow-write
--dry-run
--strict
--json
```

The follow-up must also add regression coverage proving that:

1. every documented Start flag is accepted by `apex_kb.py start`;
2. every flag reaches `apex_kb_start.py` unchanged;
3. preview mode performs no writes;
4. write mode is reachable only through explicit `--allow-write`;
5. JSON output remains available through the public Start entrypoint;
6. the skill, command contract, help output, and tests describe the same invocation surface.

## Downstream impact

### Phase 1

Do not treat Phase 0 Setup as fully callable through the public wrapper until this gap is repaired. Phase 1 may consume valid Phase 0 artifacts already produced, but its implementation plan must not assume that all documented Start modes can be launched through `apex_kb.py start`.

### Phase 2

No semantic compilation contract changes are required. The issue affects how a new controlled run is initialized, not Phase 2 packet semantics or output ownership.

### Phase 3

No retrieval or postflight contract changes are required. However, end-to-end acceptance must include the repaired public Start invocation before declaring the full lifecycle operator-ready.

## Boundary

This is a public-entrypoint reachability defect, not a request to redesign later phases. Repair it in Phase 0 or as a narrowly scoped prerequisite before the next real canary. Do not work around it by teaching agents to call `apex_kb_start.py` directly as the normal operator interface, because that would create a second public lifecycle surface and preserve the contract drift.
