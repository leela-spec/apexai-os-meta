# DeepWiki

This is a large answer. I'll work through each required section systematically, citing exact file locations throughout.

Section 1: Process-by-Process Audit Table  
Process Existence class Closest repo artifact Exact file path(s) What exists concretely What is missing Recommended build target Reuse source Confidence  
goal_to_verified_artifact_loop close_process_exemplar subagent-driven-development + requesting-code-review optional-skills/software-development/subagent-driven-development/SKILL.md, skills/software-development/requesting-code-review/SKILL.md plan→implement→spec-review→quality-review→final-review loop; static scan→tests→independent reviewer→auto-fix loop No single skill unifying goal intake, artifact type selection, verification criteria, and learning capture into one named process new_skill Copy gate taxonomy from subagent-driven-development/references/gates-taxonomy.md High  
intake_goal_contract_source_map_diverge_synthesize_skeleton_fill_verify_revise_learn absent_content None — Nothing Entire process new_skill Adapt phases from research-paper-writing/SKILL.md Phase 0–6 High  
skeleton_first_artifact_creation close_process_exemplar plan skill + research-paper-writing writing workflow skills/software-development/plan/SKILL.md lines 115–180, skills/research/research-paper-writing/SKILL.md lines 853–870 Plan skill creates skeleton before execution; research-paper-writing has contribution→Figure 1→abstract→intro→methods checklist No standalone skeleton-first skill for general (non-code, non-paper) artifacts new_skill Copy plan document structure from plan/SKILL.md lines 115–180 High  
source_and_constraint_mapping close_process_exemplar research-paper-writing Phase 0 + Phase 2 skills/research/research-paper-writing/SKILL.md lines 92–180, 356–430 Step 0.4 "Identify the Contribution" (What/Why/So What); Step 2.1 "Map Claims to Experiments" table No standalone source/constraint mapping skill for general artifacts new_skill Copy claims-to-experiments table pattern from lines 356–370 High  
divergent_generation_then_convergent_synthesis close_process_exemplar Autoreason loop in research-paper-writing skills/research/research-paper-writing/SKILL.md lines 740–774, skills/research/research-paper-writing/references/autoreason-methodology.md lines 58–100 Critic→Author B→Synthesizer→Judge Panel (3 blind CoT judges, Borda count), k=2 convergence No standalone diverge/converge skill for general artifacts; Autoreason is ML-paper-specific new_skill Copy Autoreason architecture from autoreason-methodology.md lines 58–100 High  
decision_memo_generation close_process_exemplar one-three-one-rule optional skill + kanban-orchestrator example optional-skills/communication/one-three-one-rule/SKILL.md, skills/devops/kanban-orchestrator/SKILL.md lines 103–116 1-3-1 format: problem→3 options→recommendation→DoD→implementation plan; kanban-orchestrator has "draft decision memo" as a Kanban task type No standalone decision memo skill with structured output format new_skill Copy 1-3-1 structure from one-three-one-rule/SKILL.md High  
chain_of_verification_gate close_process_exemplar requesting-code-review skills/software-development/requesting-code-review/SKILL.md lines 30–230 8-step pipeline: diff→static scan→baseline tests→self-review checklist→independent reviewer subagent→evaluate→auto-fix loop→commit Specific to code; no general-purpose chain-of-verification for documents, plans, or decisions new_skill Copy gate structure from requesting-code-review/SKILL.md Steps 1–8 High  
self_refine_draft_loop close_process_exemplar Autoreason loop + two-pass refinement in research-paper-writing skills/research/research-paper-writing/SKILL.md lines 707–774, 871–890 Autoreason loop (Critic→Author→Synthesizer→Judge); two-pass refinement (per-section then global); auto-fix loop in requesting-code-review No standalone self-refine skill for general artifacts new_skill Copy two-pass refinement prompt from lines 882–889 High  
reflexion_learning_loop close_process_exemplar agent/background_review.py agent/background_review.py lines 45–148 After every turn: forked agent reviews conversation, updates MEMORY.md and skill files; _SKILL_REVIEW_PROMPT explicitly says "most sessions produce at least one skill update" Automatic and invisible; no structured "reflexion document" output; no explicit loop that feeds learning back into the next task's context primitive_only for automatic; new_skill for structured output Copy review prompt signals from background_review.py lines 55–70 High  
plan_and_solve close_process_exemplar plan skill + subagent-driven-development skills/software-development/plan/SKILL.md lines 314–325, optional-skills/software-development/subagent-driven-development/SKILL.md Plan skill explicitly hands off to subagent-driven-development: "Plan complete and saved. Ready to execute using subagent-driven-development" Two separate skills; no single "plan-and-solve" skill that unifies them; no decision logic for when to plan vs. execute directly adapt_existing_skill Combine plan + subagent-driven-development handoff Medium  
chain_of_draft_token_efficient_reasoning absent_content None — Nothing — not mentioned anywhere in skills, docs, or tools Entire process new_skill No existing exemplar High  
double_diamond absent_content None — Zero matches in entire repo Entire framework new_skill No existing exemplar High  
design_sprint absent_content None — Zero matches in entire repo Entire framework new_skill No existing exemplar High  
scrum_sprint_ceremonies absent_content None — Zero matches in entire repo Entire framework new_skill_plus_cron No existing exemplar High  
pdca absent_content None — Zero matches in entire repo Entire framework new_skill_plus_cron No existing exemplar High  
dmaic absent_content None — Zero matches in entire repo Entire framework new_skill No existing exemplar High  
crisp_dm absent_content None — Zero matches in entire repo Entire framework new_skill_plus_kanban_graph No existing exemplar High  
nist_ai_rmf_govern_map_measure_manage absent_content None — Zero matches in entire repo Entire framework new_skill No existing exemplar High  
systems_engineering_lifecycle absent_content None — Zero matches in entire repo Entire framework new_skill_plus_kanban_graph No existing exemplar High  
weekly_review_ritual primitive_only automate-with-cron.md Pattern 2 website/docs/guides/automate-with-cron.md lines 79–104 Cron supports 0 9 * * 1; "Weekly Report" cron example searches web and formats digest No procedural steps for reviewing accomplishments, in-progress work, blockers, lessons learned; no template for weekly review output new_skill_plus_cron Copy cron pattern from automate-with-cron.md lines 79–104 High  
daily_planning_ritual primitive_only daily-briefing-bot.md website/docs/guides/daily-briefing-bot.md lines 1–90 Cron supports 0 8 * * *; morning briefing pattern with web search + summarization + delivery No procedural steps for reviewing yesterday, setting today's priorities, allocating focus; no planning packet template new_skill_plus_cron Copy self-contained prompt pattern from daily-briefing-bot.md lines 119–139 High  
precap_week absent_content None — Zero matches in entire repo Entire concept new_skill_plus_cron No existing exemplar High  
precap_next_day absent_content None — Zero matches in entire repo Entire concept new_skill_plus_cron No existing exemplar High  
flow_recap absent_content None — Zero matches in entire repo Entire concept new_skill No existing exemplar High  
session_recap partially_present research-paper-writing session startup protocol skills/research/research-paper-writing/SKILL.md lines 2219–2227 Session startup protocol: todo→memory→git log→ps aux→report status; background review captures learnings No structured session recap document (what was attempted, completed, decisions made, open threads, next actions) new_skill Copy session startup protocol from lines 2219–2227 and invert it into a recap High  
project_status_packet absent_content None — Kanban task completion summaries exist (summary + metadata fields) but no aggregation skill No skill that queries Kanban DB + memory + session history and synthesizes into a structured status report new_skill_plus_cron Copy kanban_complete metadata shapes from kanban-worker/SKILL.md lines 34–101 High  
operator_briefing_packet primitive_only daily-briefing-bot.md + automation-templates.md website/docs/guides/daily-briefing-bot.md, website/docs/guides/automation-templates.md lines 476–490 Delivery mechanism (cron→messaging platform) exists; "Morning briefing" and "Weekly AI digest" cron examples exist No skill defining a specific briefing packet format (context, priorities, decisions needed, status summary, blockers) new_skill_plus_cron Copy self-contained prompt structure from daily-briefing-bot.md lines 119–139 High  
structured_learning_capture_document primitive_only agent/background_review.py agent/background_review.py lines 45–148 Background review automatically writes to MEMORY.md and skill files after every turn No skill that generates a structured "learning capture document" as a standalone artifact (insights, patterns, anti-patterns, references) new_skill Copy signal taxonomy from _SKILL_REVIEW_PROMPT lines 55–70 High  
post_task_retrospective absent_content None — Background review is an automatic micro-retrospective but writes to MEMORY.md/skills, not a retrospective document No "what went well / what didn't / what to change" artifact skill new_skill No existing exemplar High  
orchestrator_worker_fan_out_fan_in exact_process kanban-orchestrator/SKILL.md skills/devops/kanban-orchestrator/SKILL.md lines 58–150 Full 5-step decomposition playbook: profile discovery → goal understanding → task graph sketching → task creation with parent links → completion with metadata; explicit "Fan-out + fan-in" named pattern with code examples Nothing — this is complete no_build_needed — High  
planner_implementer_reviewer_pipeline exact_process kanban-orchestrator/SKILL.md + kanban-tutorial.md Story 3 skills/devops/kanban-orchestrator/SKILL.md lines 156–158, website/docs/user-guide/features/kanban-tutorial.md lines 144–228 "Pipeline with gates: planner → implementer → reviewer" explicitly named; full three-agent choreography with retry shown in Story 3; review-required block pattern in kanban-worker Nothing — this is complete no_build_needed — High  
research_synthesis_review_pipeline exact_process kanban-orchestrator/SKILL.md + research-paper-writing/SKILL.md skills/devops/kanban-orchestrator/SKILL.md lines 152–154, skills/research/research-paper-writing/SKILL.md lines 233–355 "Fan-out + fan-in (research → synthesize)" named pattern; full iterative literature search (breadth-first then depth); delegate_task parallel research pattern in delegation-patterns.md Nothing for the Kanban/delegation version; research-paper-writing is ML-specific no_build_needed for orchestration pattern; adapt_existing_skill for general research synthesis — High  
group_chat_review absent_content None — Nothing Entire concept new_plugin_or_tool No existing exemplar High  
debate_quorum_agents close_process_exemplar tools/mixture_of_agents_tool.py + Autoreason Judge Panel tools/mixture_of_agents_tool.py lines 1–30, skills/research/research-paper-writing/SKILL.md lines 740–755 MoA: parallel reference models + aggregator synthesis; Autoreason Judge Panel: 3 blind CoT judges, Borda count ranking No standalone "debate" or "quorum" skill; MoA requires OPENROUTER_API_KEY; Judge Panel is embedded in research-paper-writing adapt_existing_skill Extract Judge Panel from autoreason-methodology.md Medium  
human_in_loop_review_gate exact_process kanban-worker/SKILL.md + kanban-orchestrator/SKILL.md skills/devops/kanban-worker/SKILL.md lines 51–69, skills/devops/kanban-orchestrator/SKILL.md lines 162 review-required block pattern with comment→block→unblock→respawn cycle; full code example; "Human-in-the-loop: Any task can kanban_block()" Nothing — this is complete no_build_needed — High  
handoff_with_guardrails exact_process kanban-worker/SKILL.md + kanban-tutorial.md skills/devops/kanban-worker/SKILL.md lines 34–127, website/docs/user-guide/features/kanban-tutorial.md lines 284–295 Structured handoff shapes (coding, research, review tasks); created_cards verification gate; phantom ID detection; prose-scan advisory warnings Nothing — this is complete no_build_needed — High  
context_packet_execution_packet partially_present SOUL.md + MEMORY.md + kanban worker_context agent/prompt_builder.py (KANBAN_GUIDANCE), skills/research/research-paper-writing/SKILL.md lines 783–807 SOUL.md + MEMORY.md + USER.md + AGENTS.md provide context injection; kanban worker_context (from kanban_show()) is an execution packet; research-paper-writing has context/ directory pattern No standalone skill for authoring context packets or execution packets as reusable artifacts new_skill Copy context/ directory pattern from research-paper-writing lines 800–807 Medium  
product_creation_pipeline_goal_research_brainstorm_skeleton_draft_review_refine_final close_process_exemplar research-paper-writing/SKILL.md skills/research/research-paper-writing/SKILL.md lines 19–44 (pipeline diagram), Phase 0–7 Full ML paper pipeline: Setup→Lit Review→Experiment Design→Execution→Analysis→Drafting→Self-Review→Submission; iterative loop diagram ML-specific; no generic product creation pipeline for documents, products, or non-research artifacts adapt_existing_skill Copy phase structure and pipeline diagram from research-paper-writing High  
learning_loop_kanban_workflow_execute_retro_skill_update_next_cycle partially_present agent/background_review.py + agent/curator.py agent/background_review.py, agent/curator.py Background review fires after every turn; curator manages skill lifecycle; skill_manage tool allows agent-authored updates No Kanban workflow that explicitly encodes execute→retro→skill-update→next-cycle as a recurring durable graph new_kanban_graph_spec Use kanban-orchestrator decomposition playbook Medium  
tree_of_thoughts absent_content None — Zero matches in skills/docs; delegate_task batch mode approximates parallel branches but has no scoring/pruning No structured ToT algorithm new_plugin_or_tool No existing exemplar High  
graph_of_thoughts absent_content None — Zero matches anywhere in repo Entire concept new_plugin_or_tool No existing exemplar High  
branch_generation_scoring_pruning_selection absent_content None — Autoreason has convergence (k=2 wins) but it's not a tree/graph traversal with explicit pruning No branch/prune/select algorithm new_plugin_or_tool No existing exemplar High  
Section 2: Exemplar Extraction  
process_exemplar:  
source_name: "research-paper-writing"  
file_path: "skills/research/research-paper-writing/SKILL.md"  
why_it_matters: >  
The most complete process skill in the entire repo. Contains a full  
multi-phase pipeline with iterative loops, a named refinement algorithm  
(Autoreason), session startup protocol, cron monitoring pattern, context  
management strategy, and structured handoff format. It is the only bundled  
skill that implements Self-Refine, Reflexion, and Chain-of-Verification  
as concrete procedural steps.  
reusable_patterns:  
- trigger_wording: >  
"Use this skill when: Starting a new research paper / Designing and  
running experiments / Writing or revising any section / Preparing for  
submission / Responding to reviews"  
(lines 49–59) — trigger list covers multiple entry points, not just one  
- section_structure: >  
Phase 0: Setup → Phase 1: Literature Review → Phase 2: Experiment Design  
→ Phase 3: Execution & Monitoring → Phase 4: Analysis → Phase 5: Drafting  
→ Phase 6: Self-Review → Phase 7: Submission. Each phase has numbered  
steps (Step N.M) with concrete commands, checklists, and decision tables.  
- procedure_style: >  
Numbered steps with bash/python code blocks, decision tables  
(Situation → Action), checklists with [ ] checkboxes, and explicit  
"When to stop" criteria. Every step names its goal in bold.  
- validation_style: >  
Autoreason loop: Critic→Author B→Synthesizer→Judge Panel (3 blind CoT  
judges, Borda count). Two-pass refinement: per-section then global.  
LaTeX Quality Checklist appended to every refinement prompt.  
Citation Verification: mandatory 5-step process per citation.  
- output_format: >  
Structured report format (lines 2273–2284): ## Experiment: /  
Status / results table / Key finding / Next step. Experiment log  
(experiment_log.md) as bridge between results and prose.  
- pitfall_format: >  
Table format: Issue → Solution (lines 2327–2342). Also inline  
"Failure Modes" table: Failure → Detection → Fix (lines 764–773).  
- example_format: >  
Code blocks with exact commands, expected output, and "why" comments.  
Concrete numbers (k=2 convergence, temperature 0.8 authors / 0.3 judges).  
- handoff_format: >  
experiment_log.md as structured bridge document (lines 666–703):  
Contribution / Experiments Run (each with claim tested, setup, key result,  
result files, figures, surprising findings) / Failed Experiments / Open Questions.  
- acceptance_criteria_style: >  
Goal-mode cards: "Acceptance: every page translated, no English left,  
links intact." (kanban-orchestrator lines 188–190). Explicit, verifiable,  
binary-checkable criteria.  
can_be_template_for:  
- "product_creation_pipeline (adapt phases for non-ML artifacts)"  
- "skeleton_first_artifact_creation (adapt writing workflow checklist)"  
- "self_refine_draft_loop (extract Autoreason loop)"  
- "divergent_generation_then_convergent_synthesis (extract Autoreason architecture)"  
- "session_recap (invert session startup protocol)"  
- "structured_learning_capture_document (adapt experiment_log.md structure)"  
limitations:  
- "ML/LaTeX-specific in many sections (citations, venues, LaTeX checklist)"  
- "Requires terminal + files toolsets; not suitable for pure-reasoning profiles"  
- "Very long (~2400 lines); must be split into references/ for adaptation"

process_exemplar:  
source_name: "kanban-orchestrator"  
file_path: "skills/devops/kanban-orchestrator/SKILL.md"  
why_it_matters: >  
The definitive reference for multi-profile orchestration. Contains the  
complete decomposition playbook, anti-temptation rules, named patterns  
(fan-out + fan-in, pipeline with gates, same-profile queue, human-in-the-loop),  
goal-mode cards, and stuck worker recovery. This is the process content  
for all multi-agent workflows.  
reusable_patterns:  
- trigger_wording: >  
"Create Kanban tasks when any of these are true: Multiple specialists  
needed / Work should survive a crash / User might want to interject /  
Multiple subtasks can run in parallel / Review/iteration expected /  
Audit trail matters." (lines 35–43) — decision criteria, not just triggers  
- section_structure: >  
Anti-temptation rules → Decomposition playbook (Step 0–5) → Common  
patterns → Pitfalls → Goal-mode cards → Recovering stuck workers  
- procedure_style: >  
Numbered steps with Python code blocks showing exact kanban_create()  
calls with placeholder profile names. Step 2 explicitly says "draft  
the graph out loud before creating anything."  
- validation_style: >  
Hallucination warnings on phantom card IDs; created_cards verification  
gate; profile discovery as Step 0 (fail-fast before planning)  
- output_format: >  
kanban_complete(summary=..., metadata={task_graph: {...}}) with  
explicit task_graph metadata showing assignees and parent links  
- pitfall_format: >  
Bold pitfall name + explanation + fix. E.g., "Inventing profile names  
that don't exist. The dispatcher silently fails..." (lines 164–180)  
- example_format: >  
Full Python code blocks with placeholder profile names and comments  
explaining which profile type each placeholder represents  
- handoff_format: >  
kanban_complete(summary="decomposed into T1-T4: ...", metadata={task_graph: {...}})  
— machine-readable graph structure for downstream orchestrators  
- acceptance_criteria_style: >  
goal_mode=True cards: body treated as acceptance criteria by judge.  
"Write the body as explicit acceptance criteria — the judge is only  
as good as the goal text." (lines 204–205)  
can_be_template_for:  
- "product_creation_pipeline (as Kanban graph spec)"  
- "learning_loop_kanban_workflow"  
- "weekly_review_ritual (as recurring Kanban card)"  
- "precap_week / precap_next_day (as Kanban pipeline)"  
limitations:  
- "Requires kanban environment; not useful for single-session workflows"  
- "Profile names are placeholders; user must substitute actual profile names"  
- "No content for what each specialist profile should actually do"

process_exemplar:  
source_name: "kanban-worker"  
file_path: "skills/devops/kanban-worker/SKILL.md"  
why_it_matters: >  
Defines the worker execution contract: handoff shapes, block reasons,  
heartbeat patterns, retry diagnostics, tenant isolation, and the  
review-required block pattern. This is the process content for every  
worker in a multi-agent pipeline.  
reusable_patterns:  
- trigger_wording: >  
Auto-loaded for every dispatched worker; no explicit trigger needed  
- section_structure: >  
Workspace handling → Tenant isolation → Good summary + metadata shapes  
→ Claiming cards → Block reasons → Heartbeats → Retry scenarios →  
Notification routing → Do NOT list → Pitfalls → CLI fallback  
- procedure_style: >  
Concrete Python code blocks for each handoff type (coding, review-required,  
research, review task). "Shape metadata so downstream parsers can use it  
without re-reading your prose."  
- validation_style: >  
created_cards verification gate; phantom ID detection; prose-scan advisory  
- output_format: >  
kanban_complete(summary="...", metadata={changed_files, tests_run,  
decisions}) for coding; kanban_comment + kanban_block for review-required  
- pitfall_format: >  
Bold pitfall name + mechanism + consequence. E.g., "Task state can change  
between dispatch and your startup."  
- handoff_format: >  
Structured metadata shapes for each task type (coding, research, review)  
with exact field names and types  
- acceptance_criteria_style: >  
Block reason: "one sentence naming the specific decision you need"  
can_be_template_for:  
- "handoff_with_guardrails"  
- "human_in_loop_review_gate"  
- "context_packet_execution_packet (worker_context as execution packet)"  
limitations:  
- "Kanban-environment-only; not applicable to delegate_task or cron workflows"

process_exemplar:  
source_name: "requesting-code-review"  
file_path: "skills/software-development/requesting-code-review/SKILL.md"  
why_it_matters: >  
The most complete verification pipeline in the repo. 8-step process:  
diff → static scan → baseline tests → self-review checklist → independent  
reviewer subagent → evaluate → auto-fix loop (max 2 cycles) → commit.  
Implements chain-of-verification as concrete procedural steps with  
fail-closed rules and exact delegate_task prompts.  
reusable_patterns:  
- trigger_wording: >  
"Use when: After implementing a feature or bug fix, before git commit  
or git push / When user says 'commit', 'push', 'ship', 'done', 'verify',  
or 'review before merge' / After completing a task with 2+ file edits"  
- section_structure: >  
Step 1 (get diff) → Step 2 (static scan) → Step 3 (baseline tests) →  
Step 4 (self-review checklist) → Step 5 (independent reviewer subagent) →  
Step 6 (evaluate results) → Step 7 (auto-fix loop) → Step 8 (commit)  
- procedure_style: >  
Numbered steps with exact bash commands and Python delegate_task calls.  
Fail-closed rules stated explicitly: "security_concerns non-empty →  
passed must be false"  
- validation_style: >  
Independent reviewer gets ONLY the diff (no shared context with implementer).  
Returns structured JSON: {passed, security_concerns, logic_errors,  
suggestions, summary}. Fail-closed: unparseable response = fail.  
- output_format: >  
VERIFICATION FAILED block with categorized findings; [verified] commit prefix  
- pitfall_format: >  
Bulleted list: "Empty diff — check git status" / "Large diff (>15k chars)  
— split by file" / "delegate_task returns non-JSON — retry once, then FAIL"  
- example_format: >  
Full delegate_task prompt with XML-tagged sections for static scan results  
and code changes; exact JSON response schema  
- handoff_format: >  
git commit -m "[verified] " as the handoff signal  
- acceptance_criteria_style: >  
Binary: passed=true only when BOTH security_concerns AND logic_errors are empty  
can_be_template_for:  
- "chain_of_verification_gate (generalize from code to any artifact)"  
- "goal_to_verified_artifact_loop (use as verification phase)"  
- "product_creation_pipeline (use as review/verify phase)"  
limitations:  
- "Code-specific (git diff, static scan patterns, test frameworks)"  
- "Requires terminal toolset"  
- "Max 2 auto-fix cycles hardcoded"

process_exemplar:  
source_name: "plan"  
file_path: "skills/software-development/plan/SKILL.md"  
why_it_matters: >  
Defines plan-before-execute behavior with concrete output format. Saves  
to .hermes/plans/. Includes writing process (6 steps), plan document  
structure (header + task structure), and execution handoff to  
subagent-driven-development. The "plan mode" concept is directly  
applicable to any skeleton-first artifact creation.  
reusable_patterns:  
- trigger_wording: >  
"Use this skill when the user wants a plan instead of execution."  
Description: "Plan mode: write an actionable markdown plan to  
.hermes/plans/, no execution."  
- section_structure: >  
Core behavior → Output requirements → Save location → Interaction style →  
Writing the Plan Well → Overview → When a Full Implementation Plan Helps →  
Bite-Sized Task Granularity → Plan Document Structure → Writing Process →  
Principles → Common Mistakes → Execution Handoff  
- procedure_style: >  
6-step writing process: Understand Requirements → Explore Codebase →  
Design Approach → Write Tasks → Add Complete Details → Review the Plan.  
Each step has concrete actions.  
- validation_style: >  
Review checklist (lines 237–244): Tasks sequential and logical / Each  
task bite-sized (2-5 min) / File paths exact / Code examples complete /  
Commands exact with expected output / No missing context / DRY, YAGNI, TDD  
- output_format: >  
Markdown plan at .hermes/plans/YYYY-MM-DD_HHMMSS-.md with:  
Goal / Current context / Proposed approach / Step-by-step plan /  
Files likely to change / Tests / Risks, tradeoffs, open questions  
- pitfall_format: >  
"Vague Tasks" / "Incomplete Code" / "Missing Verification" / "Missing  
File Paths" — each with Bad/Good example  
- handoff_format: >  
"Plan complete and saved. Ready to execute using subagent-driven-development"  
- acceptance_criteria_style: >  
"A good plan makes implementation obvious. If someone has to guess,  
the plan is incomplete."  
can_be_template_for:  
- "skeleton_first_artifact_creation"  
- "weekly_review_ritual (as planning document)"  
- "daily_planning_ritual (as planning document)"  
- "flow_recap (invert: recap instead of plan)"  
limitations:  
- "Code-focused (file paths, tests, git commits)"  
- "Single-session; no Kanban integration"

process_exemplar:  
source_name: "subagent-driven-development"  
file_path: "optional-skills/software-development/subagent-driven-development/SKILL.md"  
why_it_matters: >  
The most complete implementation of a multi-gate verification loop using  
delegate_task. Per-task workflow: implementer → spec-compliance reviewer →  
quality reviewer → fix loop → mark complete. Final integration reviewer  
after all tasks. Explicitly documents gate taxonomy via references/gates-taxonomy.md.  
reusable_patterns:  
- trigger_wording: >  
"Use when: You have an implementation plan / Tasks are mostly independent /  
Quality and spec compliance are important / You want automated review  
between tasks"  
- section_structure: >  
Overview → When to Use → The Process (1. Read plan → 2. Per-task workflow  
→ 3. Final review → 4. Verify and commit) → Task Granularity → Red Flags →  
Handling Issues → Efficiency Notes → Integration with Other Skills → Example  
- procedure_style: >  
Per-task: dispatch implementer → dispatch spec reviewer → dispatch quality  
reviewer → mark complete. Each step has exact delegate_task call with  
goal, context, and toolsets.  
- validation_style: >  
Two-stage review: spec compliance (PASS/FAIL with specific gaps) then  
code quality (APPROVED/REQUEST_CHANGES with Critical/Important/Minor).  
"Never skip reviews." "Spec compliance FIRST, code quality SECOND."  
- output_format: >  
todo list tracking task status; final integration review verdict  
- pitfall_format: >  
"Red Flags — Never Do These" section with 12 explicit anti-patterns  
- handoff_format: >  
todo(status="completed") after both reviews pass; final git commit  
- acceptance_criteria_style: >  
Spec reviewer checks: "All requirements from spec implemented? / File  
paths match spec? / Function signatures match spec? / Nothing extra added?"  
can_be_template_for:  
- "goal_to_verified_artifact_loop"  
- "product_creation_pipeline (as execution phase)"  
- "chain_of_verification_gate (generalize from code)"  
limitations:  
- "Code-specific (git, tests, file paths)"  
- "delegate_task-based; not durable across sessions"

process_exemplar:  
source_name: "daily-briefing-bot"  
file_path: "website/docs/guides/daily-briefing-bot.md"  
why_it_matters: >  
The only official example of a recurring operator-facing output process.  
Documents the self-contained prompt pattern (critical for cron), parallel  
delegation for multi-topic briefings, persona-baked prompts, weekday-only  
scheduling, and twice-daily (morning + evening) patterns.  
reusable_patterns:  
- trigger_wording: >  
"Every morning at 8am..." / "0 8 * * *" / "0 8 * * 1-5" (weekdays only)  
- section_structure: >  
What We're Building → Prerequisites → Step 1: Test Manually → Step 2:  
Create Cron Job → Step 3: Customize → Step 4: Manage Jobs → Going Further  
- procedure_style: >  
Test manually first, then automate. "The Golden Rule: Self-Contained Prompts"  
— cron jobs run in completely fresh sessions with no memory of previous  
conversations.  
- validation_style: >  
Test with /cron run <job_id> before waiting for schedule  
- output_format: >  
"☀️ Your AI Briefing — [Date] / numbered stories / headline + 2-sentence  
summary + source URL / --- / N stories • Sources searched: N"  
- pitfall_format: >  
"Bad prompt: 'Do my usual morning briefing.' / Good prompt: [specific,  
self-contained prompt with what to search, how many articles, format, tone]"  
- example_format: >  
Full cron prompt examples with exact format instructions baked in  
- handoff_format: >  
Delivery to Telegram/Discord/local file  
- acceptance_criteria_style: >  
N/A — output is delivered, not verified  
can_be_template_for:  
- "operator_briefing_packet"  
- "daily_planning_ritual (morning trigger)"  
- "weekly_review_ritual (Monday trigger)"  
- "flow_recap (evening trigger)"  
- "project_status_packet (scheduled delivery)"  
limitations:  
- "Cron-only; no Kanban integration"  
- "No structured output format beyond the example"  
- "No memory of previous runs (fresh session each time)"

process_exemplar:  
source_name: "autoreason-methodology"  
file_path: "skills/research/research-paper-writing/references/autoreason-methodology.md"  
why_it_matters: >  
Complete reference for the Autoreason iterative refinement algorithm.  
Decision tree for strategy selection, architecture diagram, role definitions,  
configuration parameters, failure modes, and scope constraint design.  
This is the most complete implementation of Self-Refine + Reflexion in the repo.  
reusable_patterns:  
- trigger_wording: >  
Decision tree: "Is the task objectively verifiable? → YES: use autoreason  
if model fails first attempt. NO: What model tier? → Mid-tier: autoreason  
(sweet spot). Frontier + unconstrained: single pass."  
- section_structure: >  
Strategy Selection Guide (decision tree + comparison table + failure modes)  
→ The Autoreason Loop (architecture + roles + configuration) → Scope  
Constraints → Failure Modes → Prompts  
- procedure_style: >  
Architecture diagram (ASCII) + role table (Role / Input / Output / Key Rule)  
+ configuration table (parameter / value / rationale)  
- validation_style: >  
Judge Panel: 3 blind CoT judges, Borda count ranking, conservative tiebreak  
(incumbent wins ties), k=2 consecutive wins for convergence  
- output_format: >  
Winner of each pass becomes new incumbent; final incumbent is the output  
- pitfall_format: >  
Failure modes table: Failure → Detection → Fix (no convergence / synthesis  
drift / degradation below single pass / overfitting / broken judges)  
- handoff_format: >  
N/A — output is the refined artifact  
- acceptance_criteria_style: >  
"A wins k=2 consecutive passes → done"  
can_be_template_for:  
- "self_refine_draft_loop"  
- "divergent_generation_then_convergent_synthesis"  
- "debate_quorum_agents"  
- "chain_of_verification_gate (judge panel as verifier)"  
limitations:  
- "Compute-intensive (~6 LLM calls per iteration)"  
- "Requires scope constraints for frontier models"  
- "Embedded in research-paper-writing; not a standalone skill"  
Section 3: Build Recommendation  
build_plan:

phase_1_core_process_skills:  
goal: >  
Author the universal synthesis and verification processes that apply  
across all artifact types. These are the highest-leverage skills because  
they are reused by every other process.  
skills_to_create:  
- skill_name: "output-creation-loop"  
purpose: >  
Universal goal-to-verified-artifact process: intake → source/constraint  
map → skeleton → fill → verify → revise → learn. Covers any artifact  
type (document, plan, code, decision memo, briefing).  
based_on_existing_artifact: >  
research-paper-writing Phase 0–6 structure; subagent-driven-development  
per-task workflow; requesting-code-review verification pipeline  
why_first: >  
All other process skills are specializations of this loop. Author this  
first so all downstream skills can reference it.  
likely_category: "apex-process"  
related_skills: ["plan", "requesting-code-review", "subagent-driven-development"]  
must_include_sections:  
- "When to Use"  
- "Inputs (goal, artifact type, constraints, sources)"  
- "Procedure (intake → source map → skeleton → fill → verify → revise → learn)"  
- "Decision Rules (when to iterate vs. ship)"  
- "Output Format (artifact + verification record)"  
- "Verification (acceptance criteria checklist)"  
- "Pitfalls"  
- "Examples"

```
  - skill_name: "skeleton-first-artifact"  
    purpose: >  
      Skeleton-first creation for any artifact: define structure before  
      filling content. Saves skeleton to .hermes/plans/ or .hermes/artifacts/.  
      Covers documents, plans, briefings, reports, decision memos.  
    based_on_existing_artifact: >  
      plan/SKILL.md plan document structure (lines 115–180); research-paper-writing  
      writing workflow checklist (lines 853–870)  
    why_first: >  
      Referenced by output-creation-loop, product-creation-pipeline, and  
      all operating-cycle skills.  
    likely_category: "apex-process"  
    related_skills: ["plan", "output-creation-loop"]  
    must_include_sections:  
      - "When to Use"  
      - "Inputs"  
      - "Procedure (define artifact type → identify sections → draft skeleton → validate structure → fill)"  
      - "Decision Rules"  
      - "Output Format"  
      - "Verification"  
      - "Pitfalls"  
      - "Examples"  

  - skill_name: "goal-recheck-validation"  
    purpose: >  
      Chain-of-verification gate for any artifact: multi-step verification  
      pipeline (self-check → independent reviewer → acceptance criteria check →  
      auto-fix loop). Generalizes requesting-code-review to non-code artifacts.  
    based_on_existing_artifact: >  
      requesting-code-review/SKILL.md Steps 1–8; subagent-driven-development  
      spec-compliance + quality review gates; references/gates-taxonomy.md  
    why_first: >  
      Used as the verification phase in output-creation-loop and all  
      product-creation pipelines.  
    likely_category: "apex-process"  
    related_skills: ["requesting-code-review", "subagent-driven-development"]  
    must_include_sections:  
      - "When to Use"  
      - "Inputs (artifact, acceptance criteria, reviewer profile)"  
      - "Procedure (self-check → independent reviewer → evaluate → fix loop)"  
      - "Decision Rules (pass/fail criteria, max fix cycles)"  
      - "Output Format (verification record)"  
      - "Verification"  
      - "Pitfalls"  
      - "Examples"  

  - skill_name: "diverge-synthesize"  
    purpose: >  
      Divergent generation then convergent synthesis for any artifact.  
      Extracts the Autoreason loop from research-paper-writing into a  
      standalone reusable skill: Critic→Author B→Synthesizer→Judge Panel.  
    based_on_existing_artifact: >  
      skills/research/research-paper-writing/references/autoreason-methodology.md  
      lines 58–100; SKILL.md lines 740–774  
    why_first: >  
      Referenced by self-refine-draft-loop and product-creation-pipeline.  
    likely_category: "apex-process"  
    related_skills: ["output-creation-loop"]  
    must_include_sections:  
      - "When to Use (strategy selection decision tree)"  
      - "Inputs"  
      - "Procedure (Critic→Author B→Synthesizer→Judge Panel)"  
      - "Decision Rules (k=2 convergence, scope constraints)"  
      - "Output Format"  
      - "Verification"  
      - "Pitfalls (failure modes table)"  
      - "Examples"  
```

phase_2_operating_cycle_skills:  
goal: >  
Author the personal operating system skills: weekly review, daily planning,  
flow recap, project status, operator briefing, and learning capture.  
Each pairs with a cron trigger.  
skills_to_create:  
- skill_name: "weekly-review"  
purpose: >  
Weekly review ritual: what was accomplished, what's in progress,  
what's planned next week, blockers, lessons learned. Triggered by  
Monday 9am cron. Delivers to operator's messaging platform.  
based_on_existing_artifact: >  
automate-with-cron.md Pattern 2 (Weekly Report, lines 79–104);  
daily-briefing-bot.md self-contained prompt pattern (lines 119–139);  
research-paper-writing session startup protocol (lines 2219–2227)  
likely_category: "apex-operating-cycle"  
related_skills: ["daily-planning", "project-status-packet", "flow-recap"]  
must_include_sections:  
- "When to Use"  
- "Inputs (Kanban board state, memory, session history)"  
- "Procedure (query board → review accomplishments → assess in-progress → plan next week → capture lessons)"  
- "Decision Rules"  
- "Output Format (structured weekly review document)"  
- "Verification"  
- "Pitfalls"  
- "Cron Translation (0 9 * * 1)"  
- "Examples"

```
  - skill_name: "daily-planning"  
    purpose: >  
      Daily planning ritual: review yesterday's outcomes, set today's  
      priorities, allocate focus, identify blockers. Triggered by weekday  
      8am cron.  
    based_on_existing_artifact: >  
      daily-briefing-bot.md (lines 1–90); automation-templates.md Morning  
      briefing (lines 476–490); research-paper-writing session startup  
      protocol (lines 2219–2227)  
    likely_category: "apex-operating-cycle"  
    related_skills: ["weekly-review", "flow-recap", "operator-briefing"]  
    must_include_sections:  
      - "When to Use"  
      - "Inputs"  
      - "Procedure"  
      - "Decision Rules"  
      - "Output Format (daily planning packet)"  
      - "Verification"  
      - "Pitfalls"  
      - "Cron Translation (0 8 * * 1-5)"  
      - "Examples"  

  - skill_name: "flow-recap"  
    purpose: >  
      Session/flow recap: what was attempted, what was completed, decisions  
      made, open threads, next actions. Triggered at session end or by  
      evening cron.  
    based_on_existing_artifact: >  
      daily-briefing-bot.md twice-daily pattern (lines 184–191);  
      research-paper-writing session startup protocol (inverted);  
      kanban-worker handoff shapes (lines 34–101)  
    likely_category: "apex-operating-cycle"  
    related_skills: ["daily-planning", "learning-capture"]  
    must_include_sections:  
      - "When to Use"  
      - "Inputs"  
      - "Procedure"  
      - "Decision Rules"  
      - "Output Format (flow recap document)"  
      - "Verification"  
      - "Pitfalls"  
      - "Cron Translation (0 18 * * 1-5)"  
      - "Examples"  

  - skill_name: "project-status-packet"  
    purpose: >  
      Aggregates Kanban task summaries, memory entries, and session history  
      into a structured project status report. Triggered by weekly cron or  
      on-demand.  
    based_on_existing_artifact: >  
      kanban-worker handoff shapes (lines 34–101); research-paper-writing  
      report format (lines 2273–2284); automation-templates.md Weekly AI  
      digest (lines 309–327)  
    likely_category: "apex-operating-cycle"  
    related_skills: ["weekly-review", "operator-briefing"]  
    must_include_sections:  
      - "When to Use"  
      - "Inputs (project name, Kanban board, date range)"  
      - "Procedure (query board → aggregate summaries → query memory → synthesize)"  
      - "Decision Rules"  
      - "Output Format (status packet: summary / in-progress / completed / blocked / next actions)"  
      - "Verification"  
      - "Pitfalls"  
      - "Cron Translation"  
      - "Kanban Translation"  
      - "Examples"  

  - skill_name: "operator-briefing"  
    purpose: >  
      Structured briefing packet for the operator: context, priorities,  
      decisions needed, status summary, blockers. Delivered to messaging  
      platform.  
    based_on_existing_artifact: >  
      daily-briefing-bot.md (lines 1–90); automation-templates.md Morning  
      briefing (lines 476–490); kanban-worker block reason pattern (lines 129–143)  
    likely_category: "apex-operating-cycle"  
    related_skills: ["daily-planning", "project-status-packet"]  
    must_include_sections:  
      - "When to Use"  
      - "Inputs"  
      - "Procedure"  
      - "Decision Rules"
```

# GPT Conclusion
Yes — **this answer finally answers your real question**.

# The important conclusion

The repo agent confirms:

> **Almost none of your specific synthesis / planning / recap / process frameworks exist as reusable Hermes process skills.**

What exists are mostly **strong exemplars** you can copy from:

|Your desired process type|Repo status|
|---|---|
|Goal → skeleton → fill → verify → revise → learn|**Not present as one skill**|
|Skeleton-first artifact creation|**Close exemplar only**|
|Source/constraint mapping|**Close exemplar only**|
|Diverge → synthesize|**Close exemplar only**|
|Chain-of-verification for general artifacts|**Close exemplar only**|
|Weekly review / daily planning / flow recap|**Not present as actual process skills**|
|Project status packet / operator briefing|**Not present as actual process skills**|
|Double Diamond, Design Sprint, PDCA, DMAIC, CRISP-DM, NIST AI RMF|**Absent content**|
|Orchestrator-worker fan-out/fan-in|**Already present**|
|Planner → implementer → reviewer|**Already present**|
|Human-in-loop review gate|**Already present**|
|Handoff with guardrails|**Already present**|
|Tree/Graph of Thoughts|**Absent; likely tool/plugin if formal**|

The repo agent explicitly classifies your core “intake → goal contract → source map → diverge → synthesize → skeleton → fill → verify → revise → learn” process as **absent content** and recommends a new skill. It classifies skeleton-first, source mapping, divergent synthesis, decision memo, and chain-of-verification as only **close process exemplars**, not ready-made general skills.

# What this means practically

You should **not** think of this as “build 40 independent skills.”

The best architecture is a **composable process-skill library**:

## Layer 1 — Core process kernel

These are the highest-leverage skills. Everything else depends on them.

|Skill|Function|
|---|---|
|`output-creation-loop`|Master loop for serious artifacts.|
|`skeleton-first-artifact`|Structure before content.|
|`goal-recheck-validation`|General verification gate.|
|`diverge-synthesize`|Generalized Autoreason / divergent-convergent loop.|
|`source-constraint-map`|Inputs, evidence, constraints, assumptions.|

The agent’s build plan agrees: the first phase should author universal synthesis and verification skills because they will be reused by every other process. It names `output-creation-loop`, `skeleton-first-artifact`, `goal-recheck-validation`, and `diverge-synthesize` as Phase 1.

## Layer 2 — Operating-cycle skills

These are your personal operating system rituals.

|Skill|Function|
|---|---|
|`weekly-review`|Weekly accomplishment / blocker / next-week review.|
|`daily-planning`|Daily priorities and session framing.|
|`flow-recap`|End-of-session recap.|
|`project-status-packet`|Aggregates Kanban + memory + session history.|
|`operator-briefing`|Human-facing status / decision packet.|
|`learning-capture`|Structured learning document, not just hidden memory update.|

The repo agent confirms that weekly review, daily planning, flow recap, project status packet, operator briefing, and structured learning capture do **not** exist as procedural skills; they need custom authoring, usually paired with Cron later.

## Layer 3 — Orchestration templates

Here you do **not** rebuild Kanban. You encode your specific task graphs.

|Graph / template|Build target|
|---|---|
|Product creation pipeline|Skill + Kanban graph spec|
|Execute → retro → skill update → next cycle|Kanban graph spec|
|PreCapWeek → PreCapNextDay → FlowRecap → ProjectStatusUpdate|Skill + Cron + Kanban graph|
|Research fan-out → synthesize → verify|Mostly adapt existing Kanban/orchestrator pattern|

The repo already contains the orchestration mechanics: fan-out/fan-in, planner→implementer→reviewer, human review gates, and structured handoffs. The missing part is your specific recurring graph content.

## Layer 4 — Optional framework skills

Only after the core is stable:

|Framework|Build later as|
|---|---|
|Double Diamond|`SKILL.md`|
|Design Sprint|`SKILL.md` + optional cron/kanban schedule|
|Scrum|`SKILL.md` + cron ceremonies|
|PDCA|`SKILL.md` + cron/kanban loop|
|DMAIC|`SKILL.md`|
|CRISP-DM|`SKILL.md` + Kanban graph|
|NIST AI RMF|`SKILL.md`|
|Systems Engineering|`SKILL.md` + Kanban graph|

The repo agent found zero matches for these frameworks and classified them as absent content.

---

# My correction to the repo agent’s build plan

The repo agent’s answer is good, but I would slightly adjust the build order.

## Don’t start with `diverge-synthesize`

The repo agent includes `diverge-synthesize` in Phase 1, based on Autoreason. That is powerful, but it is expensive and complex: the extracted Autoreason pattern uses Critic → Author B → Synthesizer → Judge Panel, with multiple judge calls and convergence rules. The answer itself notes it is compute-intensive and embedded in `research-paper-writing`, not standalone.

So I would make `diverge-synthesize` **Phase 1b**, not the first thing.

## Build the first three skills first

Start with:

1. `output-creation-loop`
2. `skeleton-first-artifact`
3. `goal-recheck-validation`

These three are enough to improve almost every other workflow.

Then add:

4. `source-constraint-map`
5. `diverge-synthesize`

Then the operating-cycle skills.