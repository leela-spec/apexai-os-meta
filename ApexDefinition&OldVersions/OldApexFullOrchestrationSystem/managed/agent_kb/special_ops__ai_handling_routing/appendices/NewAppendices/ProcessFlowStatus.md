## Stage-0 finding: source + scaffold readiness

**Verdict:** We have enough to design the patch-flow, but not enough to claim the final AI Handling/Routing KB is holistic yet.

The current managed promptflow already locks the right repo and target root: it says all execution stays inside `leela-spec/MasterOfArts`, writes only into `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__ai_handling_routing/`, and targets the scaffold files `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, and `LEARNING_QUEUE.md` plus appendices. It also already has the right architecture model: **thin scaffold, deep appendices**, with appendices holding evidence, ranking, candidate ledgers, and anti-drift material.

The current scaffold is not empty or broken. `ESSENCE.md` already defines the agent as owning advisory model/tool selection, source-authority routing, ambiguity/escalation posture, handoff readiness, repo-execution-vs-chat routing, fallback paths, and current-verification warnings for provider/model claims. It also correctly excludes runtime config mutation, provider-policy authority, all-agent orchestration authority, QA severity authority, and accepted-truth promotion.

The issue is **under-integration**, not absence. The current source manifest admits that no current provider-pricing, live benchmark, or runtime-config source was used, and treats that as non-blocking only because the KB is advisory and must mark those claims as `needs_current_verification`. Your uploaded index ranks a broader AIHR source pack than the current managed manifest currently reflects, especially the `Research Agent API Calls Performance & Cost.md` source and many informatics / promptflow / Codex / failure evidence sources.

## Files I would ask you to upload or confirm

### P0 — upload now if available

|Priority|File|Why it matters|Current status|
|--:|---|---|---|
|P0|`Research Agent API Calls Performance & Cost.md`|Primary AIHR source in your uploaded index; needed for model/tool/provider routing, cost-quality boundaries, freshness rules, and model-selection handoff shape.|Referenced by source inventory as unique/high-value, but I have not seen the full file content in the current AIHR appendix set.|
|P0|`OpenClaw Model Routing.md`|Direct OpenClaw-specific model routing source; likely more important for this agent than generic prompt/workflow material.|Listed in repo research packet as AI handling/routing source, not present in current AIHR source manifest.|
|P0|`AI_Useage.md`|Likely operational usage doctrine for AI handling; should be screened for scaffold rules and examples.|Listed as AI handling/routing source, not present in current AIHR source manifest.|
|P0|`AI_Handling_Process_Gem.md`|Likely direct process rules for the AI handling lane.|Listed as AI handling/routing source, not present in current AIHR source manifest.|

### P1 — upload if you want the KB to be stronger than the current source manifest

These are already represented in your uploaded index and/or repo ledgers, but should be attached if the exact local versions differ from repo versions:

|Priority|File group|Why|
|--:|---|---|
|P1|`AUDIT_CHECKLIST_GPT.md`, `FILE_TAXONOMY_GPT.md`, `INFORMATION_DESIGN_CANON_GPT.md`, `TERMINOLOGY_GPT.md`, `FILE_TAXONOMY_Perp.md`|Not AIHR doctrine directly, but high-impact for decision-card shape, routing-table discipline, status vocabulary, machine-readability, and audit coverage.|
|P1|`WorkflowResearchClaude.md`, `Promptflow.md`, `GPT&OPENCLOUD_PROMPT_FLOW_ANALYSIS.md`, `ChatHandover&PromptFlow.md`|Needed for promptflow/handoff/process patch semantics, especially preventing the prior failure mode of vague prompt-flow instructions.|
|P1|`CODEX_GIT_EXECUTION_ESSENCE.md`, `CODEX_RESILIENT_MIGRATION_PROCESS.md`, `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md`, `Improvement_Capture_Rule.md`|Needed because AIHR must route repo work correctly even if it does not execute it.|
|P1|`FailureAnalysis.md`, `SYSTEM_AUDIT.md`, `2ndTrybutalsoBad.md`, `prob - prompt design & process failure.md`, relevant `.diff` files|Needed as anti-drift / failure evidence, not as direct doctrine.|

## What should be patched before “final KB” status

The current cross-agent gap analysis already names the strongest missing AIHR improvements:

|Rank|Patch target|Recommendation|
|--:|---|---|
|1|`appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`|Create it. This gives durable readiness status, missing database candidates, research backlog, attach pack, and closure state. The gap analysis ranks this as P1.|
|2|`appendices/APPENDIX_KB_SOURCE_NOTES.md`|Create it. AIHR depends on knowing each source’s authority scope, non-authority scope, freshness sensitivity, and routing use.|
|3|`appendices/APPENDIX_KB_ROUTING_EXAMPLES.md`|Create it with worked examples: browser-chat answer, current provider claim, repo write, config-impact stop, source conflict, and repaired handoff.|
|4|`appendices/APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`|Create it, but without stale provider rankings unless freshly verified. It should compare browser chat, deep research, web verification, repo connector write, Codex-style execution, manual review, QA/audit, and specialist handoff.|
|5|`appendices/APPENDIX_KB_MACHINE_READABLE_INDEX.md`|Create Markdown-first. YAML/JSON can come later as generated sidecars if automation needs it.|
|6|`ESSENCE.md`|Patch in status vocabulary, read-budget profiles, stronger KB map, and currentness policy.|
|7|`TEMPLATES.md`|Patch in a `choose_template_when` table. Current templates are useful, but chooser logic is missing. The existing templates already include routing, source authority, model/tool fit, repo execution, specialist handoff, and config-impact stop cards.|
|8|`LEARNING_QUEUE.md`|Add explicit candidate lanes for provider/currentness research, prompt-template ownership boundary, source notes, and mode/tool taxonomy.|

## Prompt-flow Q&A — recommended defaults

### A. Scope and write boundaries

**Q1. Should the patch-flow modify only `special_ops__ai_handling_routing`, or can it touch shared managed rules?**  
**Recommendation:** Only modify `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__ai_handling_routing/**` in this pass. Cross-agent/shared rules become follow-up research notes, not writes.

**Q2. Should the patch-flow write to `main` directly or produce a branch/PR?**  
**Recommendation:** Patch through a branch/PR, but the promptflow itself should be main-targeted and exact-path. Avoid hidden “candidate branch changed but main unchanged” confusion.

**Q3. Should the KB remain advisory or become runtime authority?**  
**Recommendation:** Advisory only. It may recommend routing, source authority, handoff shape, current-verification requirements, and stop conditions. It must not mutate `openclaw.json`, model registry, runtime config, provider policy, or permissions. Existing best practices already enforce manual review for config-impacting recommendations.

### B. Integration posture

**Q4. Should high-impact ideas go directly into scaffold or appendices first?**  
**Recommendation:** Both, but by compression level.  
**Scaffold:** compact rules, state names, read paths, chooser tables, anti-failure rules.  
**Appendices:** evidence, detailed source notes, examples, source conflicts, mode comparisons, candidate ledgers.

**Q5. Should “accepted” mean runtime truth?**  
**Recommendation:** No. Patch vocabulary to distinguish:

- `accepted_in_kb_base`
    
- `candidate`
    
- `needs_validation`
    
- `deferred`
    
- `runtime_authority_not_granted`
    

The current quality analysis already flagged that “accepted” language can blur KB-base acceptance vs runtime truth, so this is a high-value patch.

**Q6. Should model/provider recommendations be embedded now?**  
**Recommendation:** No direct rankings unless the full source is attached and current provider data is freshly verified. But we should absolutely add the **research lane, model/tool fit card rules, freshness windows, official-source requirement, and handoff to cost/performance analysis** now.

### C. Patch sequencing

**Q7. What should the patch-flow do first?**  
**Recommendation:** First create/update appendices in this order:

1. `APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`
    
2. `APPENDIX_KB_SOURCE_NOTES.md`
    
3. `APPENDIX_KB_ROUTING_EXAMPLES.md`
    
4. `APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md`
    
5. `APPENDIX_KB_MACHINE_READABLE_INDEX.md`
    

Then patch scaffold:

6. `ESSENCE.md`
    
7. `TEMPLATES.md`
    
8. `BEST_PRACTICES.md`
    
9. `MISTAKES.md`
    
10. `LEARNING_QUEUE.md`
    
11. `PROMPTFLOW_KB_BASE_BUILD.md`
    

**Q8. Should the existing appendix files be replaced?**  
**Recommendation:** No. Patch and extend them. The existing manifest/candidate/anti-drift/ranking files are structurally useful; the problem is missing layers and under-integration, not wholesale failure.

**Q9. Should old factory-output files under `docs/kb4agents/...` be used?**  
**Recommendation:** Use only as evidence/candidate material. They contain useful concepts like dispatcher identity, clarification, authority declaration, and handoff discipline, but they are provisional and weaker than the managed scaffold.

### D. Final ledger structure

**Q10. What should the information ledger contain?**  
**Recommendation:** Three ledgers, exactly matching your requested output:

1. **Integrate into scaffold now:** compact rules, state enums, chooser logic, hard stops, read-budget profiles, status vocabulary.
    
2. **Integrate into appendices now:** source notes, examples, mode/tool comparison, machine-readable index, QA/research plan, evidence packets.
    
3. **Move/additional sources to folder:** direct AIHR source files, provider-cost/performance source, OpenClaw model-routing files, current verification source pack.
    

## My recommended next move

Upload the P0 files if you have them:

1. `Research Agent API Calls Performance & Cost.md`
    
2. `OpenClaw Model Routing.md`
    
3. `AI_Useage.md`
    
4. `AI_Handling_Process_Gem.md`
    

Then I’ll build the full **information ledger** in the three-part form you requested and turn it into a concrete promptflow for patching the scaffold and appendix files.