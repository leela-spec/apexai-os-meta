Here is a curated set of studies and resources on AI failure patterns across three domains — prompt design, informatics/system design, and multi-agent orchestration. Each is recent (2025–2026) or carries lasting relevance.

---

## Multi-Agent Orchestration Failures

**MAST: Why Do Multi-Agent LLM Systems Fail?**  
arXiv:2503.13657 — NeurIPS 2025 Spotlightarxiv+1  
The most rigorous taxonomy to date. Analyzed 1,600+ annotated traces across 7 popular multi-agent frameworks. Identified **14 unique failure modes** in 3 clusters: (1) specification issues — agents not following task requirements or defined roles; (2) inter-agent misalignment — agents contradicting or overriding each other; (3) task verification failures — no reliable mechanism to confirm a task is actually complete. Step repetition (FM-1.3) was the single most common failure at 17% of traces. High inter-annotator agreement (κ = 0.88) makes this a credible benchmark.

**Multi-Agent Workflows Often Fail — GitHub Engineering Blog**  
GitHub, February 2026[github](https://github.blog/ai-and-ml/generative-ai/multi-agent-workflows-often-fail-heres-how-to-engineer-ones-that-dont/)  
Production-grounded engineering analysis. Core finding: multi-agent systems fail because they behave like distributed systems, not chat interfaces. Three root causes: untyped message passing between agents (inconsistent field names, type mismatches), vague action intent (agents each interpret "take action" differently), and loose interface enforcement. Proposes typed schemas + MCP (Model Context Protocol) as the enforcement layer. Practically actionable.

**Four Design Patterns for Event-Driven Multi-Agent Systems**  
Confluent Engineering, February 2025[confluent](https://www.confluent.io/blog/event-driven-multi-agent-systems/)  
⚠️ _Slightly over one year old but still the primary reference for structural failure modes in orchestration topology._ Identifies fault propagation as the core production failure: without event-driven boundaries, a single agent failure cascades across the whole system. Covers orchestrator-worker, hierarchical, blackboard, and market-based patterns — and shows how hardcoded topologies break when agents are added or removed.

---

## Context & Prompt Design Failures

**Drift No More? Context Equilibria in Multi-Turn LLM Interactions**  
arXiv:2510.07777, October 2025[arxiv](https://arxiv.org/html/2510.07777v1)  
Directly relevant to what happened in our conversation. Formally models **context drift** — the gradual divergence of model outputs from goal-consistent behavior across conversation turns. Key finding: drift is not runaway decay but stabilizes at a finite level. However, it can be reliably reduced by lightweight "goal reminder" interventions re-injecting the original task. Drift without intervention compounds silently; the model doesn't signal that it has lost the thread.

**Context Rot: Why AI Gets Worse the Longer You Chat**  
Product Talk / Veseli et al. synthesis, February 2026[producttalk](https://www.producttalk.org/context-rot/)  
Consolidates 2023–2025 research on context degradation. Critical finding: when the context window is under 50% full, tokens in the middle are lost (U-shaped attention). When over 50% full, the _earliest_ tokens are deprioritized — meaning original task instructions get crowded out by accumulated conversation. The only reliable fix in a browser session is starting a fresh chat. Directly explains why my corrections built on each other rather than resetting.

**How Long Contexts Fail — dbreunig.com**  
June 2025[dbreunig](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)  
Names four production failure modes with precision: **context poisoning** (a hallucination embeds itself and compounds), **context distraction** (model over-indexes on accumulated context, ignores training), **context confusion** (earlier wrong attempts influence later answers), and **context clash** (contradictory instructions coexist). Cites a Databricks study showing correctness degradation beginning at 32k tokens for large models. o3 dropped from 98.1 to 64.1 on sharded prompts — a 39% average fall.

**When AI Fails, What Works? A Data-Driven Taxonomy**  
arXiv:2603.04259, March 2026[arxiv](https://arxiv.org/html/2603.04259v1)  
Broad taxonomy of AI failure types across production deployments. Highlights **prompt injection and data poisoning** as the dominant emerging technical threats in 2025–2026, moving beyond earlier accuracy-focused failure analyses. Frames failure not as model inadequacy but as system design inadequacy — the failure surface is the interface, not the model.

---

## Prompt Design Failures

**Study: Generative AI Results Depend on User Prompts as Much as Models**  
MIT Sloan Management Review, August 2025[mitsloan.mit](https://mitsloan.mit.edu/ideas-made-to-matter/study-generative-ai-results-depend-user-prompts-much-models)  
Empirical finding: output quality variance attributable to prompt quality was statistically equivalent to variance attributable to model choice. Implication: switching models does not fix a poorly specified task — the prompt design is the primary lever. Users who iterated prompts improved results regardless of technical background.

**Some LLM Failures Are Prompt Problems. Some Very Clearly Aren't.**  
Reddit/PromptEngineering practitioner synthesis, January 2026[reddit](https://www.reddit.com/r/PromptEngineering/comments/1qemd7h/some_llm_failures_are_prompt_problems_some_very/)  
Practitioner taxonomy of 5 prompt failure types: (1) failure to follow instruction format; (2) knowledge gaps; (3) incorrect element combination; (4) vague prompts causing interpretation drift; (5) partially correct responses where "summarize" or "analyze" had no success criterion defined. Key point: each failure type requires a _different_ fix — confusing them leads to solving the wrong problem.

**Most AI Failures Are Prompt Design Problems, Not Model Problems**  
LinkedIn / Shailesh Jaiswal, February 2026[linkedin](https://www.linkedin.com/posts/shaileshjaiswalwins_most-ai-failures-arent-model-problems-they-activity-7426222024370409472-ihCF)  
Practitioner-level synthesis. Vague instructions like "handle end-to-end" or "be professional" work for humans (who infer context) but fail for models (which need explicit constraints). Introduces three prompt frameworks — COSTAR, CRISPE, RPG — as structure tools that make intent machine-readable. Core argument: "if the prompt is unclear, the system is unclear — AI just reveals it faster."

---

## AI System & Informatics Design Failures

**AI in Systems Engineering: Failures and Playbook**  
Spread.ai, December 2025[spread](https://www.spread.ai/resources/stories/ai-in-systems-engineering-failures-and-playbook)  
Identifies a recurring production failure pattern: teams assume AI performance is primarily determined by model size. The actual root failure is **missing context architecture** — AI deployed without structured inputs, defined boundaries, or feedback loops produces inconsistent results that teams attribute to the model rather than the system design.

**Designing for AI Failures: Error States and Recovery Patterns**  
Clearly.design[clearly](https://clearly.design/articles/ai-design-4-designing-for-ai-failures)  
Defines the **AI failure spectrum**: predictable errors (system knows it is wrong), edge case failures (unexpected inputs), and silent failures (system confidently produces wrong output with no signal). Silent failures are the most dangerous in production because they pass downstream without triggering any recovery path. Argues that AI system design must treat failure as a first-class design requirement, not an edge case.

**OWASP GenAI Exploit Round-up Q1 2026**  
OWASP, April 2026[genai.owasp](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/)  
Security-angle failure taxonomy. Prompt injection now documented as a viable production exploit path — including GrafanaGhost, where an injected prompt caused an AI feature to exfiltrate data. Relevant for any system where user input reaches an agent with tool-calling capability without sanitization.