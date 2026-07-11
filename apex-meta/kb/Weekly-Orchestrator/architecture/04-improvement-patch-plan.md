# Weekly Orchestrator — Improvement & Testing Patch Plan

Status: plan only — no patch below is applied. Execution: deterministic executor per patch card (exact find/replace where given), wave order mandatory, validation gate after each wave.

---

## PART A — Whole-orchestration-flow plan

### A1. Test evidence this plan is built on (executed live, 2026-07-11)

```yaml
behavioral_tests:
  T1_apex-evidence-normalize:
    dispatch: synthetic F3 raw notes, no flow_packet on disk, run_date passed in dispatch
    result: pass — full envelope, correct unmatched_flow uncertainty, refused interpretation, envelope+4-line return
    cost: {subagent_tokens: 22887, tool_uses: 4}
    output: artifacts/flow-packets/20260711/normalized-raw-flow-dump-F3.md
  T2_apex-precap-week:
    dispatch: G1 bootstrap, empty state file, operator intent + calendar constraints, week-id passed
    result: pass — correct degraded/bootstrap behavior, all assumptions flagged, envelope complete
    cost: {subagent_tokens: 36749, tool_uses: 9}
    output: artifacts/weekly-plans/weekly_plan_packet-20260711-2026-W29.md
  static_sweeps:
    dangling_old_entrypoint_refs_in_live_packages: 17 lines across 14 files (list in Wave 2)
    index_v3_staleness: {md: 6 old-path hits, yaml: 4, jsonl: 1, new_surface_coverage: 0}
    preload_budget: all stage skill entrypoints 5.5–9.7 KB, agent defs 2.0–2.8 KB — within the ≤5000-token skill cap
```

### A2. Defects and improvements by dimension

```yaml
d1_agent_orchestration_efficiency:
  found:
    - no parallel-dispatch rule: F1–F4 normalize/recap stages are independent per flow but the orchestrator contract is silent, forcing serial habit
    - no model/effort tiering: every stage inherits the session model; evidence-normalize and project-status are mechanical stages
    - dispatch date dependency implicit: stage agents have no shell — run_date/week_id must come from the dispatch prompt, currently unwritten
  keep: refs-not-copies dispatch, envelope+capped-summary returns (proven by T1/T2 token costs)
d2_handover_contracts:
  found:
    - target_surface ambiguity (proven twice): both test agents set it to their own output path; schema means "durable surface this packet proposes to affect"
    - envelope lacks version field and gate field (self-description gap for forward migration and audit)
  keep: authority object, gate primitive, stop_condition discipline (both tests populated them correctly)
d3_micro_informatics_standards:
  found:
    - 02-meso-file-map.md contains "was <old filename>" changelog comments — violates the operator law: no changelog narrative in working files
    - PromptEngineer/SKILL.md contract YAML squashed onto single lines (index gap G09) — parses as prose, defeats machine readability
    - agent bodies mix typed labels (Constraint:/Stop:) with untyped prose bullets — inconsistent with the function-typed-label standard
d4_file_placement:
  found:
    - all runtime files are in correct locations (agents/, skills/, architecture/) — no moves required
    - 17 dangling references to pre-rename entrypoint filenames inside LIVE skill packages (break read_when navigation)
    - Weekly-Orchestrator index v3 (all 3 formats) cites old paths and indexes none of the new surfaces
    - 2 test artifacts from T1/T2 pollute the pre-first-cycle artifact families
  leave_untouched: provenance surfaces (operator-output-design steps 2–6, patch-packs, old-apex KBs, SmallSkills) — historical records keep old paths by design
```

### A3. Wave order and validation gates

```yaml
waves:
  wave_1_contract_corrections: {patches: [P01, P02, P03..P10], gate: rerun T1+T2 dispatches; expect target_surface none/state-path respectively; envelope_version present}
  wave_2_file_placement:       {patches: [P11..P24, P25], gate: repo grep for 6 old entrypoint filenames over .claude/skills + indexes returns 0 live hits}
  wave_3_informatics:          {patches: [P26, P27, P28], gate: rerun frontmatter/path/draft-language lint script — ALL CHECKS PASS; yaml.safe_load parses P27 block}
  wave_4_record_and_cleanup:   {patches: [P29, P30], gate: architecture package internally consistent; artifact families clean}
rollback: each wave is one commit; a failed gate reverts only its wave.
```

---

## PART B — Individual patches per file

### Wave 1 — contract corrections

**P01 — `.claude/skills/weekly-orchestrator/references/handoff-schema.md`**
- Intent: kill the proven target_surface ambiguity; add envelope self-description; make date sourcing explicit.
- Changes:
  1. Envelope: add `envelope_version: 1` as first field; add `gate: G1 | G2 | G3 | G4 | G5 | review | none` after `packet_type`.
  2. Replace the `target_surface` comment line with: `target_surface: <durable_state_path_this_packet_proposes_to_change_or_none>   # NEVER the packet's own storage path; only state/ or .claude/kb/ paths qualify; none for plans, dumps, overviews, verdicts`.
  3. Add under field_rules: `Rule: dates, week ids, and packet_id date segments always come from the orchestrator dispatch prompt; stage agents never infer the current date.`
  4. Add under field_rules: `Rule: correct target_surface per packet_type — weekly_plan_packet/next_day_plan/flow_packet/normalized_raw_flow_dump/skipped_flow_marker/all_project_status_packet/review_verdict: none; flow_recap_packet: state/apex-project-status.md (via status-merge only); status_merge_packet: state/apex-project-status.md.`

**P02 — `.claude/skills/weekly-orchestrator/SKILL.md`**
- Intent: efficiency rules the tests showed are missing.
- Changes:
  1. Procedure step 2, append: `The dispatch prompt MUST include run_date (YYYYMMDD) and, for planning stages, week_id — agents cannot determine dates themselves.`
  2. New procedure step 2b: `Parallel dispatch: evidence_normalize and flow_recap invocations for different flows of the same day are independent — dispatch them concurrently (one subagent per flow). Review lens pairs always run in parallel. Planning stages and status_merge never run concurrently with each other.`
  3. Procedure step 3, append to envelope validation: `including target_surface correctness per handoff-schema field_rules`.

**P03 — `.claude/agents/apex-precap-week.md`** — set `target_surface: none` in the envelope-fields instruction line; add `Rule: run_date and week_id come from the dispatch prompt — never infer dates.`; convert the three Boundaries bullets to typed labels (`Constraint:` ×2, `Stop:` unchanged).

**P04 — `.claude/agents/apex-precap-next-day.md`** — same three changes (target_surface: none; date rule; typed labels), plus: `Constraint: represent F1–F4 so each flow's packet is independently dispatchable for parallel downstream normalize/recap.`

**P05 — `.claude/agents/apex-evidence-normalize.md`** — envelope instruction: `target_surface: none` (replace the current self-path example); date rule; typed labels.

**P06 — `.claude/agents/apex-flow-recap.md`** — keep `target_surface: state/apex-project-status.md (via status-merge only)` (already correct); add date rule; typed labels.

**P07 — `.claude/agents/apex-status-merge.md`** — target_surface already correct; add date rule; typed labels.

**P08 — `.claude/agents/apex-project-status.md`** — envelope instruction: `target_surface: none`; date rule; typed labels.

**P09 — `.claude/agents/apex-review-validity.md`** — add to return block: `envelope_version: 1` and `gate: review`; add `Constraint: basis_digest_ref and subject path come from the dispatch prompt only.`

**P10 — `.claude/agents/apex-review-alignment.md`** — same as P09 for the alignment lens.

Optional (operator decision, not blocking): P03a/P05a/P08a add `model: sonnet` to apex-evidence-normalize and apex-project-status frontmatter (mechanical stages; T1 shows low tool-use complexity). Default if undecided: leave `inherit`.

### Wave 2 — file placement (dangling live references)

Deterministic rule for P11–P24: in each file, replace the old entrypoint filename with `SKILL.md` in the cited path; content otherwise untouched.

| patch | file | line | old → new |
|---|---|---|---|
| P11 | .claude/skills/AIRouting/ai-routing-card-template.md | 128 | `AIRouting/ai-routing-and-usage-tracking-SKILL.md` → `AIRouting/SKILL.md` |
| P12 | .claude/skills/flow-recap/references/flow-recap-packet-contract.md | 80 | `PrecapNextDay/Skill_precap-next-day.md` → `PrecapNextDay/SKILL.md` |
| P13 | .claude/skills/model-usage-log/package-manifest.md | 130 | `AIRouting/ai-routing-and-usage-tracking-SKILL.md` → `AIRouting/SKILL.md` |
| P14 | .claude/skills/model-usage-log/references/model-usage-delta-contract.md | 72 | same as P13 |
| P15 | .claude/skills/PrecapNextDay/precap-next-day-package-manifest.md | 17 | `Skill_precap-next-day.md` → `SKILL.md` |
| P16 | .claude/skills/PrecapNextDay/templates/precap-next-day-brief-template.md | 109 | same as P15 |
| P17 | .claude/skills/PrecapWeek/weekly-command-brief-template.md | 129 | `Skill_Precap-Week.md` → `SKILL.md` |
| P18 | .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md | 133,135,136 | all three skill paths → `<package>/SKILL.md` |
| P19 | .claude/skills/ProjectStatus/project-status-overview-template.md | 113 | `project-status-overview_SKILL_v3.md` → `SKILL.md` |
| P20 | .claude/skills/raw-flow-dump-normalize/examples/apex-minimal-raw-flow-dump-example.md | 32 | `Skill_precap-next-day.md` → `SKILL.md` |
| P21 | .claude/skills/raw-flow-dump-normalize/package-manifest.md | 20 | same |
| P22 | .claude/skills/raw-flow-dump-normalize/references/raw-flow-dump-contract.md | 21 | same |
| P23 | .claude/skills/status-merge/package-manifest.md + references/next-precaphandoff-context-contract.md + references/status-merge-packet-contract.md | 143 / 87 / 93 | `project-status-overview_SKILL_v3.md` → `SKILL.md` |
| P24 | .claude/skills/PrecapNextDay/references/* + remaining in-package hits from the same grep | per grep | same rule, applied by the deterministic sweep, re-grep to zero |

**P25 — `apex-meta/kb/Weekly-Orchestrator/indexes/APEX_Weekly_Orchestration_Index_v3.{md,yaml,jsonl}`**
- Intent: index reflects the live execution surface.
- Changes: (a) apply the same path rule to the 6/4/1 stale hits; (b) add records for `.claude/agents/` (8 files, authority live_domain_authority, loop_stage per stage), `.claude/skills/weekly-orchestrator/` (rank alongside root control file), `apex-meta/kb/Weekly-Orchestrator/architecture/` (authority accepted_design_rationale, freshness current), `apex-meta/GLOSSARY.md`; (c) update `inspected_head` to the current commit; (d) note in §0 that the fable-orchestrator initiative's weekly-loop portion is now realized. Alternative (deferred, larger): full v4 regeneration — not required for correctness.

### Wave 3 — micro informatics standards

**P26 — `apex-meta/kb/Weekly-Orchestrator/architecture/02-meso-file-map.md`**
- Intent: comply with the no-changelog-narrative law.
- Change: delete the four `# was ...` / `; frontmatter repaired` / `; wrapper fence removed` / `; header stripped` comments in the skill-layer block and the parenthetical rename notes — the map states only the current surface. (Rename evidence already lives in git history and 03's verification record.)

**P27 — `.claude/skills/PromptEngineer/SKILL.md`**
- Intent: restore machine readability of the contract block (G09).
- Change: reflow the single-line `skill_contract:` blob (line 11) into properly indented multi-line YAML inside a ` ```yaml ` fence; token-for-token same keys/values, no semantic change. Validation: `yaml.safe_load` parses; key set identical before/after.

**P28 — all 8 `.claude/agents/*.md` (rolled into Wave 1 P03–P10 edits)**
- Intent: one consistent typed-label grammar (`Rule:`, `Constraint:`, `Stop:`, `Do not:`) for every normative line; prose kept only for role narration. No new obligations introduced — relabeling only.

### Wave 4 — record and cleanup

**P29 — `apex-meta/kb/Weekly-Orchestrator/architecture/03-execution-trace-verification.md`**
- Change: append `## 5. Live stage-agent behavioral tests` with the T1/T2 records from A1 (dispatch, result, cost, output path) and the target_surface finding that produced P01.

**P30 — artifact cleanup**
- Change: delete the two test artifacts `artifacts/flow-packets/20260711/normalized-raw-flow-dump-F3.md` and `artifacts/weekly-plans/weekly_plan_packet-20260711-2026-W29.md` (test dispatches, not cycle output), leaving families pristine for the first real cycle. Executed via plain `git rm` in the wave-4 commit.

---

## Execution contract

```yaml
apply_rules:
  order: wave_1 -> wave_2 -> wave_3 -> wave_4, one commit per wave, gate before next wave
  executor: deterministic exact-match replacement per card; a failed exact match halts that card only and reports
  never: rewrite whole files, touch provenance surfaces, change skill schema semantics outside P01's listed lines
post_plan_validation:
  - rerun lint script (frontmatter, path refs, draft language) — must pass
  - rerun T1 + T2 — envelopes must show corrected target_surface and envelope_version
  - grep old entrypoint filenames over .claude/skills + Weekly-Orchestrator indexes — 0 hits
```
