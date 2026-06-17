I extracted the workflow-bearing files from `C:\GitDev\OpenClaw\OpenClaw\07_finalopenclawsystem`. The core incorporated workflow surfaces are these:

**Core Workflow Files**
- [PROCESS_BLUEPRINT_SYSTEM.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/docs/PROCESS_BLUEPRINT_SYSTEM.md)  
  Map of where process authority lives: operating spine, bootstrap, session export, night planning, QA, promotion, routing.

- [PROJECT_ROUTING.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/docs/PROJECT_ROUTING.md)  
  Companion routing examples: keep-local vs delegate, specialist handoff checklist, first-wave routing examples.

- [HOLDING_ORCHESTRATION_FLOW.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/processes/HOLDING_ORCHESTRATION_FLOW.md)  
  Intake, thresholding, agent activation, validation bands, output routing, promotion/hygiene handling.

- [AGENT_HANDOFF_CONTRACTS.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/processes/AGENT_HANDOFF_CONTRACTS.md)  
  Durable handoff workflow: packet schema, EVD/IMP/RSK scoring, state semantics, validators, stop conditions.

- [DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md)  
  Deep-research-to-patchspec routine: scope lock, source alignment, patch plan, diff safety, executor handoff, validation checklist.

- [BOOTSTRAP.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/rituals/BOOTSTRAP.md)  
  Startup routine: verify repo, environment, Python, governing files, agent routing files, KB placement files.

- [CHECKLISTS.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/rituals/CHECKLISTS.md)  
  Lightweight recurring checks: foundation, environment, safety, interface, trace, escalation, promotion.

- [HEARTBEAT.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/rituals/HEARTBEAT.md)  
  Maintenance routine: script-first heartbeat, one active foreground flow, memory maintenance, routing of continuity signals.

- [SESSION_EXPORT_PROTOCOL.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/rituals/SESSION_EXPORT_PROTOCOL.md)  
  End-of-session trace workflow: required export sections, operative delta, findings, promotion candidates, next actions.

- [NIGHT_PLANNING_PROTOCOL.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/rituals/NIGHT_PLANNING_PROTOCOL.md)  
  Cross-session planning ritual: synthesize session exports, project state, hygiene findings, promotion queue, operator/cloud plans.

**Governance Workflows**
- [PROMOTION_PROTOCOL.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/rules/PROMOTION_PROTOCOL.md)  
  Truth-change workflow: promotion packet, verification gates, approval, application trace, KB promotion routing.

- [QA_HYGIENE_PROTOCOL.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/rules/QA_HYGIENE_PROTOCOL.md)  
  QA workflow: finding classes, severity model, required checks, routing, closure rules.

- [PROJECT_INTERFACE_CONTRACT.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/rules/PROJECT_INTERFACE_CONTRACT.md)  
  Project entry workflow: required project control surfaces, validation-first traversal, interface/state/truth separation.

- [AGENT_KB_LANES.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/knowledge/AGENT_KB_LANES.md)  
  KB placement workflow: lane model, five-file scaffold, runtime loading boundaries, candidate-only learning queues.

- [KB_STARTING_SOURCE_MAP.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_STARTING_SOURCE_MAP.md)  
  Source-routing workflow: source classes, authority order, evidence-only staging, final-system patch targets.

- [KB_PROMOTION_LEDGER_TEMPLATE.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md)  
  KB promotion packet template: candidate packaging, scoring, overlap checks, source/candidate/canon separation.

**Promptflow / Routine Templates**
- [PROMPTFLOW_KB_BASE_BUILD.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_KB_BASE_BUILD.md)  
  Build sequence for the Prompts Workflows KB: repo lock, source authority, appendices first, scaffold generation, quality gates.

- [PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/PROMPTFLOW_CONSTANT_FRAME_CONTROLLED_KB_INTEGRATION.md)  
  Constant-frame KB integration workflow: frame block, atomic task payload, gate check, HALT/CLARIFY signals, artifact order.

- [TEMPLATES.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md)  
  Accepted reusable workflow templates: one-file live edit, research preflight, bounded repo execution, promptflow stage-gate, clean handoff.

- [PROMPTFLOW_KB_BASE_BUILD.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/PROMPTFLOW_KB_BASE_BUILD.md)  
  Hygiene Clean KB build routine: source manifest, ranking ledger, candidate ledger, anti-drift appendix, scaffold verification.

**Secondary / Working Workflow Artifacts**
- [ZERO_DRIFT_DIFF_APPLICATION_PROCESS_GUIDE_V5.yaml](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/docs/working/ZERO_DRIFT_DIFF_APPLICATION_PROCESS_GUIDE_V5.yaml)  
  Working diff-application process guide.

- [META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_EXECUTION_PLAN.md)  
  Working execution plan for watchdog QA/hygiene.

- [META_DETECTIVE_WATCHDOG_QA_HYGIENE_PER_TARGET_DIFF_HANDOVER.md](C:/GitDev/OpenClaw/OpenClaw/07_finalopenclawsystem/docs/working/META_DETECTIVE_WATCHDOG_QA_HYGIENE_PER_TARGET_DIFF_HANDOVER.md)  
  Per-target diff handover workflow artifact.

I would treat the `managed/processes`, `managed/rules`, `managed/rituals`, and `managed/knowledge` files as the truly incorporated workflow layer. The `docs/working` and many `appendices/` files are useful execution evidence or source material, but less canonical unless routed through the managed files above.