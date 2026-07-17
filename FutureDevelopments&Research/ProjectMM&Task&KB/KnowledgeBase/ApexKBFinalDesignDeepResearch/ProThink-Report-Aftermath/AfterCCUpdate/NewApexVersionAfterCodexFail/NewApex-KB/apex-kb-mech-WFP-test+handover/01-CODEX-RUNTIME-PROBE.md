# Codex Task - Apex KB v2 Runtime Probe

Use this task as the first child-chat handoff.

```text
ROLE
You are the read-only deterministic runtime probe for an Apex KB mechanistic workflow test.

REPOSITORY
- Repository: leela-spec/apexai-os-meta
- Branch: main
- Required pack commit: 4fddeab59a8e4d63a8efa347ec9b3d28f33f43c1
- Pack root: FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/ProThink-Report-Aftermath/AfterCCUpdate/NewApexVersionAfterCodexFail/NewApex-KB/apex-kb-mechanistic-workflow-pack

MISSION
Determine whether the mechanistic v2 pack is merely stored as a research package or is installed into the live Apex KB skill/runtime and executable.

READ COMPLETELY
1. <pack-root>/README.md
2. <pack-root>/IMPLEMENTATION-CHANGE-MANIFEST.okf.yaml
3. <pack-root>/.claude/skills/apex-kb/SKILL.md
4. .claude/skills/apex-kb/SKILL.md
5. apex-meta/scripts/apex_kb.py
6. apex-meta/scripts/apex_kb_control.py
7. Live schemas/templates named by the implementation-change manifest

READ-ONLY CHECKS
- Confirm HEAD and whether it contains commit 4fddeab59a8e4d63a8efa347ec9b3d28f33f43c1.
- Compare the nested pack files with the live skill/runtime files.
- Run safe help or doctor commands only when available.
- Check whether these operator aliases truly exist and dispatch:
  - start
  - continue
  - status
  - repair
- Check whether live runtime supports:
  - run-config.okf.json v2
  - read-only preflight-config
  - run-manifest.json with reproducible config_hash
  - Phase 0 exhaustive field-separated ranking without top-N truncation
  - phase0-stats.json and phase0-stats.okf.md
  - generated Phase 1/2 instruction files
  - prompt_template_path, instruction_file_path, and batch_guide_path in semantic packets
- Do not create, edit, delete, commit, stash, reset, pull, or push anything.

VERDICT RULE
Return exactly one verdict:
- LIVE_CLI_READY: all required v2 surfaces are installed and demonstrated.
- PACK_ONLY_NOT_IMPLEMENTED: the pack exists but one or more required live runtime changes are absent.
- BLOCKED: repository or runtime access prevents a reliable determination.

RETURN
Return one YAML envelope and nothing after it:

schema: apex.kb.child-result.v1
run_id: pre-run
executor_role: codex_deterministic
task_id: runtime-probe-v2
status: complete | blocked | failed
reason_code: LIVE_CLI_READY | PACK_ONLY_NOT_IMPLEMENTED | BLOCKED
evidence:
  head_sha: ""
  pack_present: true | false
  live_skill_matches_pack: true | false
  aliases:
    start: demonstrated | absent | unverified
    continue: demonstrated | absent | unverified
    status: demonstrated | absent | unverified
    repair: demonstrated | absent | unverified
  v2_capabilities:
    run_config: demonstrated | absent | unverified
    read_only_preflight: demonstrated | absent | unverified
    manifest_hash_lock: demonstrated | absent | unverified
    exhaustive_phase0: demonstrated | absent | unverified
    phase0_stats: demonstrated | absent | unverified
    generated_semantic_instructions: demonstrated | absent | unverified
  commands_executed: []
  files_read: []
  missing_or_mismatched_files: []
recommended_mode: live_cli | protocol_simulation | blocked
next_action: Return this envelope to the orchestrator chat. Do not patch the runtime.
```
