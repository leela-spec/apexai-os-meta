**Source Ledger for Deterministic‑Markdown‑Patcher**

This ledger lists the files provided by the user for this project.  Each entry
captures only the filename and a description inferred from the filename.  Since
the actual file contents are not available in this environment, the ledger
indicates which sections would need to be extracted later when the files
become accessible.  The ledger also classifies each source into one of several
categories (e.g., skill package rules, patching architecture, deterministic
scripts, templates/examples, failure analysis, research results or
obsolete/superseded) based solely on the filename.  Additional notes
indicate whether content should **not** be copied directly into the final
deliverables.

| source_name | source_type | expected_use | read_priority | sections_to_extract | do_not_copy_notes |
| --- | --- | --- | --- | --- | --- |
| **Claude_Skill_Package_BestPractice_Handover.md** | skill_package_rules | Guidance on structuring SKILL.md files; defines mandatory sections and best practices for Claude skill packages. | 1 | Title, section ordering guidelines, front‑matter requirements, procedure length, failure modes guidelines. | Do not copy the examples verbatim; summarise rules in your own words. |
| **Claude_Skill_PromptFlow_Design_Guidance_v1.md** | skill_package_rules | Additional design guidance for building prompt flows and integrating them into skill packages. | 1 | Key design principles, prompt flow structure, integration tips. | Avoid copying any proprietary examples; extract only high‑level design principles. |
| **FailureAnalysis_FBClaude.md** | failure_analysis | Analysis of previous failures when using Claude for patching tasks. | 1 | Headings summarising failure modes, root causes, and recovery strategies. | Summarise failure modes without reusing internal data. |
| **FailureAnalysis_FB_Claude.md** | failure_analysis | Another failure analysis document for Claude patching. | 1 | Top failure modes and corrective measures. | Do not reproduce raw test data; extract lessons learned. |
| **FailureAnalysis_FB_Claude2.md** | failure_analysis | Continuation of the failure analysis series. | 1 | Additional failure modes and recommendations. | Same caution as above. |
| **FinalResearchReport_gem.md** | patching_architecture | Research report on patching processes (gem variant). | 2 | Key conclusions about deterministic patching processes, recommended action categories, and sample workflows. | Focus on principles and recommended steps; avoid copying any copyrighted content. |
| **FinalResearchReport_GPT.md** | patching_architecture | Research report on patching processes (GPT variant). | 2 | Similar to above; extract differences between models and process recommendations. | Summarise the actionable insights; omit large narrative sections. |
| **FinalResearchReport_CC.md** | patching_architecture | Research report on patching processes (CC variant). | 2 | Extract common patterns across the research reports. | Do not duplicate any code or examples verbatim. |
| **Patch Process Analysis.txt** | patching_architecture | Plain text analysis of the patch process. | 2 | Identify key rules (e.g., no multi‑match replacements, live extraction only). | Only quote deterministic rules; omit context. |
| **ClaudePatchRedesign.md** | patching_architecture | Document proposing a redesign of the Claude patching process. | 2 | Extract final architecture diagram and accompanying rules. | Summarise design; no diagrams. |
| **Patchingpaths_various.md** | patching_architecture | A collection of patching path experiments. | 2 | Extract list of valid patch paths and decision factors. | Avoid copying raw logs. |
| **Patchingpaths_various_AIProbSolution.md** | patching_architecture | AI‑assisted solutions to patching paths. | 2 | Extract success patterns and pitfalls. | Do not copy AI answers. |
| **FirstClaudePatchReport.okf.md** | existing_process_and_scripts | An earlier report of the first Claude patch execution. | 3 | Extract any process steps or scripts referenced. | Do not reuse the report’s wording; summarise the procedure. |
| **ClaudeCode‑Deterministic‑StubRepair‑Process.okf.md** | existing_process_and_scripts | Detailed stub repair process for deterministic code fixes. | 3 | Extract algorithm for stub repair, including invocation patterns. | Avoid copying code samples; abstract the steps. |
| **stub_repair_toolkit.py** | deterministic_scripts | Python toolkit used for stub repair. | 3 | Review functions to inspire deterministic patch executor; identify error handling patterns. | Do not reuse code directly; reimplement logic where appropriate. |
| **CompleteFirstChatHistoryWithPatchClaudeCode.md** | existing_process_and_scripts | A comprehensive chat history of the first patching task. | 3 | Extract insights about interactive steps and user interaction patterns. | Do not replicate conversation text. |
| **SKILL.md** | existing_process_and_scripts | Existing skill file (possibly outdated) used as reference. | 3 | Extract section structure and content flow for comparison. | Do not reuse the content; use as a structural reference only. |
| **DetermnisticTools_sed_awk_perl.md** | deterministic_scripts | Guide on deterministic command‑line tools (sed, awk, perl). | 4 | Extract command patterns that ensure deterministic replacements. | Do not include command outputs or examples verbatim. |
| **DetermnisticTools_sed_awk_perl2.md** | deterministic_scripts | Follow‑up guide on deterministic tools. | 4 | Additional command patterns and best practices. | Same caution as above. |
| **ClaudeSetupGeneral.md** | deterministic_scripts | General setup instructions for Claude in patching environments. | 4 | Extract environment prerequisites and configuration steps. | Summarise only the high‑level setup; omit specifics like API keys. |