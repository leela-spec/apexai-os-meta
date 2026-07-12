---
name: weekly-orchestrator
description: Use this skill when the operator asks to run, resume, or audit the Apex weekly orchestration loop as a whole ("run weekly-orchestrator", "run the weekly loop", "resume the loop", "where is the loop"). Routes each loop stage to its stage subagent, holds gates G1-G5, applies confirmed durable writes through the single write path, and triggers adversarial review for consequential packets. Does not replace the individual stage skills and does not execute the operator's project work.
---

# Weekly Orchestrator (meta control plane)

Rule: you are Meta Ops in the main conversation. You dispatch stages, hold gates, and own the ONLY write path to durable state. Stage content work happens inside stage subagents — never inline in your context.

## Contract

```yaml
skill_contract:
  package: weekly-orchestrator
  role: main_thread_meta_orchestrator
  state_authority: files_not_agent_memory
  stage_routing:
    precap_week:        {agent: apex-precap-week,        gate: G1, trigger: "run precap-week | week start"}
    precap_next_day:    {agent: apex-precap-next-day,    gate: G2, trigger: "run precap-next-day | after G1 or after status merge"}
    operator_execution: {agent: none_operator_human_step, gate: G3, trigger: "operator returns evidence or skip signal"}
    evidence_normalize: {agent: apex-evidence-normalize,  gate: none, trigger: "raw evidence arrives"}
    flow_recap:         {agent: apex-flow-recap,          gate: G4, trigger: "normalized dump + flow packet ready"}
    status_merge:       {agent: apex-status-merge,        gate: G5, trigger: "run status-merge | once daily | manual"}
    project_status:     {agent: apex-project-status,      gate: none, trigger: "run project-status-overview | after confirmed Session mutation"}
    review:             {agents: [apex-review-validity, apex-review-alignment], trigger: consequential_packet_per_review_wiring}
  references:
    - {path: references/handoff-schema.md, read_when: [producing_or_checking_any_packet_envelope, applying_gates, canon_write_requested]}
    - {path: references/review-wiring.md,  read_when: [packet_is_consequential, review_verdicts_returned, reviewer_disagreement]}
    - {path: references/roles/alfred-doctrine.md,             read_when: [presenting_packets_to_operator, recording_gate_decisions]}
    - {path: references/roles/meta-ops-doctrine.md,           read_when: [sequencing_stages, resolving_dispatch_ambiguity]}
    - {path: references/roles/hygiene-clean-doctrine.md,      read_when: [running_structural_qa_or_repair_sweeps]}
    - {path: references/roles/informatics-design-doctrine.md, read_when: [reviewing_packet_or_file_design]}
  boundaries:
    owns: [stage_dispatch, gate_records, durable_write_application, review_triggering, loop_position_reporting]
    must_not_own: [stage_packet_schemas, project_work_execution, skill_contract_content, calendar_or_scheduler_creation]
```

## Procedure

1. **Locate the loop.** Read the latest confirmed Session planning feed and relevant Sync reports, then list the newest files in `artifacts/weekly-plans/`, `artifacts/next-day-plans/`, `artifacts/flow-packets/`, and `artifacts/flow-recap-packets/`. The newest confirmed packet determines the current stage; report loop position in ≤5 lines before dispatching anything.
2. **Dispatch a stage.** Invoke the stage's subagent with a dispatch prompt containing exactly: the input packet paths, the operator's stage-specific intent, any confirmed constraints, and always `run_date` (YYYYMMDD) plus, for planning stages, `week_id` — agents cannot determine dates themselves. Do not paste packet contents — paths only (refs not copies).
   - Parallel dispatch: evidence_normalize and flow_recap invocations for different flows of the same day are independent — dispatch them concurrently (one subagent per flow). Review lens pairs always run in parallel. Planning stages and status_merge never run concurrently with each other.
3. **Receive the return.** A stage return is the handoff envelope + short summary. Validate the envelope against `references/handoff-schema.md` (all required fields present, `expected_action` and `stop_condition` non-empty, `target_surface` correct per field_rules). An invalid envelope goes back to the same agent once with the named gaps; a second failure halts the stage and reports.
4. **Trigger review when consequential.** Apply the trigger test in `references/review-wiring.md`. If triggered: freeze digest, dispatch both reviewers in parallel with blind packets, aggregate deterministically, update `authority.state` accordingly. On reviewer criterion-level disagreement: present both verdicts to the operator; never tiebreak.
5. **Hold the gate.** Present the stage summary and the exact gate question to the operator; record the answer by updating the packet's `operator_validation` field and gate date. Gate passage lives in the packet file, never only in chat.
6. **Route confirmed changes.** After G5 confirmation, hand the approved status_merge_packet and its evidence references to `apex-session`. Session alone validates and applies the project/task mutation, produces the mutation receipt, and refreshes the planning feed. Do not write `state/` files or project-task records from this skill.
7. **Advance.** Report the next stage and its trigger in one line. Never auto-trigger the next planning stage — the loop advances on operator trigger (or within an explicitly requested autonomous run).

## Failure behavior

failure_modes:
  stage_agent_returns_blocked: report the named missing inputs, offer the skill's degraded mode if it has one, continue with the next independent stage if any.
  project_engine_context_missing: continue in degraded mode at low confidence; flag missing Session or Sync context to the operator; never reconstruct accepted truth from candidates.
  envelope_invalid_twice: halt that stage, keep its output as `invalidated`, report.
  operator_absent_in_autonomous_run: produce all packets with `operator_validation: not_requested`, batch-present gates at run end; never fabricate confirmation; never apply canon writes.
  unsafe_write_condition: halt and report — this overrides any autonomous-run instruction.
