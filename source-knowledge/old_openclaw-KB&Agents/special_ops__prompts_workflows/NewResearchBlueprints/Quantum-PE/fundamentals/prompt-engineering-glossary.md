Title: Prompt Engineering Glossary: 500 Key Terms

URL Source: https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary

Published Time: 2026-03-28

Markdown Content:
Fundamentals

Last updated:March 2026·12 min read·By [Hans Kuepper](https://www.promptquorum.com/about) · Founder of PromptQuorum, multi-model AI dispatch tool · PromptQuorum

Read in:

Concise definitions of the 500 most important prompt engineering terms — from tokens and context windows to agent orchestration, RAG, and evaluation metrics.

## Top 20 Most Important AI & Prompt Engineering Terms (2026)

Master the essential terminology of artificial intelligence and prompt engineering. These 20 core concepts form the foundation of working with LLMs, from fundamental architectures to advanced optimization techniques. Whether you're building AI agents, implementing RAG systems, or optimizing prompt performance, understanding these terms will accelerate your expertise across all areas of AI development and deployment.

*   ### [RAG (Retrieval-Augmented Generation) Connecting LLMs to external knowledge bases so they answer based on real data, not training memory.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-rag-retrieval-augmented-generation)
*   ### [Chain-of-Thought (CoT) Asking the model to show its reasoning step-by-step before giving the final answer, improving accuracy on complex problems.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-chain-of-thought-prompting)
*   ### [AI Agent An autonomous AI system that plans tasks, calls tools, and iterates until reaching a goal without human intervention.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-ai-agent)
*   ### [Prompt Injection An attack where untrusted user input tricks an LLM into ignoring its original instructions.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-prompt-injection)
*   ### [Few-Shot Prompting Providing 2–5 examples of the desired behavior in the prompt so the model learns the pattern.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-few-shot-prompting)
*   ### [Fine-Tuning Retraining a model on task-specific data to improve its performance on that exact task.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-fine-tuning)
*   ### [Embeddings Converting text or images into numerical vectors that capture meaning, enabling semantic search and similarity.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-embeddings)
*   ### [Vector Database A specialized database that stores and retrieves embeddings by similarity, enabling fast semantic search at scale.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-vector-database)
*   ### [Hallucination When an LLM generates confident-sounding but false information, fabricating facts or citations.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-hallucination)
*   ### [Context Window The maximum number of tokens an LLM can process in a single request (e.g., GPT-4o: 128k tokens).](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-context-window)
*   ### [Temperature A setting controlling randomness: low (0.0) = predictable, high (1.0) = creative/chaotic.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-temperature-and-top-p)
*   ### [Zero-Shot Prompting Asking the model to perform a task without any examples — the baseline approach.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-zero-shot-prompting)
*   ### [Tool Calling Enabling an LLM to call external APIs, run code, or trigger actions based on its reasoning.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-tool-calling)
*   ### [Guardrails Safety systems that filter harmful inputs and outputs, preventing misuse or unwanted behavior.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-guardrails)
*   ### [LLM Evaluation Measuring model quality using benchmarks, human ratings, or automated metrics like BLEU or ROUGE.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-llm-evaluation)
*   ### [Prompt Engineering The art of writing precise instructions to get accurate, useful answers from AI models.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-prompt-engineering)
*   ### [Multi-Agent Systems Multiple independent AI agents working in parallel or sequence to solve complex problems collaboratively.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-multi-agent-systems)
*   ### [Context Engineering Structuring the context window strategically to prioritize important information and reduce noise.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-context-engineering)
*   ### [Latency The time delay between sending a prompt and receiving the complete response (e.g., 800ms for GPT-4o).](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-latency)
*   ### [Cost Optimization Techniques like model selection, prompt caching, and batch processing to reduce API spending.](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-cost-optimization)

## Commonly Confused AI Terms

Quick reference for 10 term pairs that are frequently misunderstood or used interchangeably.

| Category | Term A | Term B | Key Difference |
| --- | --- | --- | --- |
| Prompting Technique | Zero-shot | Few-shot | Zero-shot: ask without examples (faster, cheaper). Few-shot: provide 2–5 examples (more accurate for specific formats or domains). |
| Reasoning | Chain-of-Thought | Tree-of-Thought | CoT: single linear reasoning path. ToT: explores multiple branches, evaluates paths. ToT costs 2–3× more tokens but handles harder problems. |
| Knowledge Architecture | RAG | Fine-tuning | RAG: retrieves current data at inference time — no retraining. Fine-tuning: adjusts model weights permanently — expensive, requires labeled data. |
| Security | Prompt injection | Jailbreak | Injection: structural attack — user input overrides system instructions. Jailbreak: behavioral attack — crafted phrasing bypasses safety guardrails. |
| Sampling Parameters | Temperature | Top-p | Temperature: scales all token probabilities (0 = deterministic, 1+ = creative). Top-p: samples only from the smallest set of tokens covering probability p. Use one at a time. |
| Memory | Short-term memory | Long-term memory | Short-term: active conversation context (tokens in window). Long-term: persistent store across sessions (vector DB or key-value). Agents need both. |
| Alignment | Guardrail | RLHF | Guardrail: runtime policy enforcement (filter, validate, block) — no retraining. RLHF: training-time alignment via human feedback — rewires model behavior permanently. |
| Agent Behavior | Tool calling | Agentic | Tool calling: single function invocation per turn. Agentic: autonomous loop — decide → call tool → observe → decide — until goal is achieved. |
| Output Quality | Hallucination | Confabulation | Synonymous in practice. Both describe confident, plausible-sounding but false model output. "Hallucination" is more common in US/tech; "confabulation" in academic/EU contexts. |
| Prompt Architecture | System prompt | User prompt | System: persistent instructions (role, rules, format) — set once per conversation. User: specific task per turn. System controls behavior; user specifies request. |

Level

Domain

## Learning Paths

Curated term sequences — follow a path to build expertise in one area.

## Most Important Prompt Engineering Terms in 2026

The 10 terms that matter most for AI practitioners building production systems in 2026 — ranked by industry adoption and search demand.

1.   1[Agentic RAG](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-agentic-rag)

Agents that retrieve + reason autonomously are the dominant production AI pattern in 2026. 
2.   2[LangGraph](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-langgraph)

Stateful multi-agent orchestration framework adopted by most production teams. 
3.   3[Context engineering](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-context-engineering)

What "prompt engineering" is called when managing multi-turn agents and memory. 
4.   4
5.   5[LLM-as-a-Judge](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-llm-as-a-judge)

Scalable eval method replacing human raters in most CI/CD AI testing pipelines. 
6.   6[Grounding](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-grounding)

Mandatory for compliance-sensitive AI (finance, legal, medical) post-2025 regulations. 
7.   7
8.   8[Prompt Injection](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-prompt-injection)

Top security vulnerability for AI systems — most production teams now test for this. 
9.   9[Vector database](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-vector-database)

Core infrastructure component for every RAG and long-term memory implementation. 
10.   10

Jump to section

[A](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-agent)[B](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-bias)[C](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-context-window)[D](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-drift)[E](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-executor-agent)[F](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-few-shot-prompting)[G](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-grounding)[H](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-hallucination)I[J](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-jailbreak)K[L](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-llm-large-language-model)[M](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-multi-agent-system)N[O](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-open-weights)[P](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-prompt)Q[R](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-role-prompting)[S](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-system-prompt)[T](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-token)U[V](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-vram)[W](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-win-rate)X Y[Z](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#term-zero-shot-prompting)

Key Takeaways

*   500 terms organized into 6 sections: Core Concepts, Agents, Safety, Evaluation, Advanced Techniques, and Metrics & Production
*   Each term includes a practical definition and 1–3 primary source citations for E-E-A-T validation
*   Covers foundational techniques (CoT, RAG, few-shot) through 2026 agentic patterns (multi-agent, handoff, GraphRAG)
*   Search filter to find terms by name and jump navigation to quickly locate relevant sections
*   FAQPage schema + DefinedTermSet schema for answer extraction by Google, Claude, Perplexity, and other AI engines

**This glossary covers the 500 most important terms in prompt engineering, from foundational concepts to agent orchestration and evaluation frameworks.** Each entry includes a concise practical definition written for developers and AI practitioners, plus a primary reference link for deeper reading.

Terms are organized into six groups: Core Prompting Concepts, Agents & Orchestration, Safety & Alignment, Evaluation & Testing, Advanced Techniques, and Metrics & Production. Use the searchable tables as a quick reference or follow the links for implementation details.

## Core Prompting Concepts

### Prompt

Prompt Engineering Foundations

Any text instruction, question, or example you give an AI model to steer its output toward a specific goal; quality is bounded by how clearly the prompt defines role, task, context, format, and constraints.

[Wikipedia](https://en.wikipedia.org/wiki/Prompt_engineering), [PromptingGuide Basics](https://www.promptingguide.ai/introduction/basics), [LearnPrompting Prompt](https://learnprompting.org/vocabulary/prompt)

### LLM (Large Language Model)

Prompt Engineering Foundations

Neural network trained on massive text corpora to predict and generate human-like language from prompts; examples include GPT-5.5, Claude, Gemini, and others used for chat, coding, and reasoning.

[PromptingGuide LLM](https://www.promptingguide.ai/introduction/llms), [AWS Guide](https://aws.amazon.com/what-is/large-language-model/), [ClipboardAI Glossary](https://www.clipboard-ai.com/blog/ai-glossary)

### Context window

Prompt Engineering Foundations RAG Mastery

[Maximum number of tokens the model can consider at once](https://www.promptquorum.com/prompt-engineering/context-windows-explained-why-ai-forgets), including system prompt, conversation history, and retrieved documents; exceeding this truncates or ignores older context. PromptQuorum manages context window optimization across models with different limits (Claude 200K, GPT-4 128K, Gemini 1M) automatically within your workflow.

[Wikipedia](https://en.wikipedia.org/wiki/Prompt_engineering), [Firecrawl Context Engineering](https://www.firecrawl.dev/blog/context-engineering), [PromptingGuide Settings](https://www.promptingguide.ai/introduction/settings)

### Hallucination

Prompt Engineering Foundations Fine-tuning & Alignment Safety & Security

Confident-sounding but factually incorrect or fabricated output from an LLM, often caused by missing context, ambiguous prompts, or over-generalization beyond training data.

[Zendesk Glossary](https://www.zendesk.com/blog/generative-ai-glossary/), [LearnPrompting](https://learnprompting.org/docs/hallucinations), [Infomineo Best Practices](https://infomineo.com/artificial-intelligence/prompt-engineering-techniques-examples-best-practices-guide/)

### Grounding

RAG Mastery

Supplying the model with authoritative, task-specific data (documents, database results, web pages) inside the prompt so answers rely on real sources instead of model memory alone.

[PromptingGuide RAG](https://www.promptingguide.ai/techniques/rag), [AWS RAG Guide](https://aws.amazon.com/what-is/retrieval-augmented-generation/), [CoherePath Glossary](https://coherepath.org/coherepath/ai-prompting-glossary/)

### Fine-tuning

Fine-tuning & Alignment

Retraining model weights on domain-specific data to specialize the model for a particular task, writing style, or vocabulary. Fine-tuning requires datasets, training runs, and computational resources, but results in a customized model. Techniques include LoRA (efficient), QLoRA (quantized), and full backpropagation (resource-intensive).

[Anthropic – Fine-tuning guide](https://docs.anthropic.com/en/docs/build-with-claude/fine-tuning), [OpenAI – Fine-tuning API](https://platform.openai.com/docs/guides/fine-tuning), [IBM – RAG vs fine-tuning](https://www.ibm.com/think/topics/rag-vs-fine-tuning-vs-prompt-engineering)

### VRAM

GPU memory required for model inference and fine-tuning. Example: LLaMA 3.1 70B needs ~40GB VRAM for full precision, ~16–20GB in 4-bit quantization, ~8GB for the 8B variant. VRAM availability determines which models can run locally on consumer or enterprise hardware.

[NVIDIA – GPU memory](https://www.nvidia.com/en-us/geforce/graphics-cards/), [Ollama – Hardware guide](https://ollama.ai/), [HuggingFace – Model cards](https://huggingface.co/models)

### Context engineering

Discipline of deciding *what* fills the context window (system prompt, memory, retrieved docs, tool outputs, history), not just *how* the instructions are written; crucial for agents and RAG.

[Firecrawl Blog](https://www.firecrawl.dev/blog/context-engineering), [PromptingGuide Settings](https://www.promptingguide.ai/introduction/settings), [KeepMyPrompts 2026](https://www.keepmyprompts.com/blog/en/prompt-engineering-guide-2026)

![Image 1: Core prompt engineering concepts: zero-shot, few-shot, chain-of-thought, and system prompts illustrated with example structures.](https://www.promptquorum.com/images/glossary-prompting-taxonomy-en.svg)

Core prompt engineering concepts: zero-shot, few-shot, chain-of-thought, and system prompts illustrated with example structures.

## Agents & Orchestration

![Image 2: LLM agent orchestration overview: tool use, ReAct loops, planner-executor patterns and multi-agent coordination.](https://www.promptquorum.com/images/glossary-agent-diagram-en.svg)

LLM agent orchestration overview: tool use, ReAct loops, planner-executor patterns and multi-agent coordination.

## Safety & Alignment

![Image 3: LLM safety and alignment glossary: RLHF, constitutional AI, jailbreak defenses and red-teaming workflows.](https://www.promptquorum.com/images/glossary-alignment-terms-en.svg)

LLM safety and alignment glossary: RLHF, constitutional AI, jailbreak defenses and red-teaming workflows.

## Evaluation & Testing

## Advanced Techniques

## Metrics & Production

### ROUGE

Evaluation & Production

Family of recall-oriented metrics (ROUGE-N, ROUGE-L, etc.) that measure overlap of n-grams or longest common subsequences between generated and reference texts; commonly used for summarization evaluation.

[Medium – LLM evaluation metrics](https://medium.com/data-science-in-your-pocket/llm-evaluation-metrics-explained-af14f26536d2), [Codecademy – Evaluation](https://www.codecademy.com/article/llm-evaluation-metrics-benchmarks-best-practices)

### Perplexity

Measure of how well a probability model predicts a sample; lower perplexity indicates the model is less "surprised" by the text; useful for intrinsic evaluation of language modeling quality.

[Medium – LLM metrics](https://medium.com/data-science-in-your-pocket/llm-evaluation-metrics-explained-af14f26536d2), [Lamatic – Evaluation guide](https://labs.lamatic.ai/p/llm-evaluation-metrics/)

### Human-in-the-Loop (HITL) Evaluation

Evaluation workflow incorporating human review or annotation at key points to validate or correct model/agent outputs, especially for high-stakes or subjective quality dimensions.

[Microsoft – Responsible AI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/responsible-use), [Anthropic – Human feedback](https://www.anthropic.com/safety)

### Constitutional AI (extended)

Alignment approach where models self-critique and revise outputs against a written set of principles; can be applied at inference time in agents for ongoing safety.

[Anthropic – Constitutional AI](https://www.anthropic.com/news/constitutional-ai), [OpenAI – Safety](https://platform.openai.com/docs/guides/safety-best-practices)

### Context Engineering (advanced)

Strategic curation and modular management of everything entering the context window—including dynamic memory, retrieved chunks, tool results, and compressed history—for optimal agent performance.

[Firecrawl – Context engineering](https://www.firecrawl.dev/blog/context-engineering), [AIPromptLibrary – Advanced 2026](https://www.aipromptlibrary.app/blog/advanced-prompt-engineering-techniques), [KeepMyPrompts – Guide](https://www.keepmyprompts.com/blog/en/prompt-engineering-guide-2026)

## Frequently Asked Questions

### What is prompt engineering in simple terms?

Prompt engineering is the discipline of designing and iterating prompts so language models produce useful, predictable, and safe outputs. It involves structuring instructions, adding context, and choosing techniques like few-shot or chain-of-thought to improve reliability and quality.

### What is the difference between zero-shot and few-shot prompting?

Zero-shot prompting asks the model to perform a task using only instructions, without any examples—best for common tasks where the model's prior training already covers the pattern. Few-shot prompting includes a small number of input-output examples in the prompt so the model can infer the desired pattern, format, or style before handling the real query. Few-shot typically produces higher quality on complex or uncommon tasks.

### What does RAG stand for in AI?

RAG stands for Retrieval-Augmented Generation. It's an architecture where relevant documents are retrieved from a knowledge base and injected into the prompt so the model answers based on current, grounded data rather than relying on training data alone. This reduces hallucinations and ensures answers are based on real, up-to-date information.

### What is the difference between prompt engineering and fine-tuning?

Prompt engineering is the discipline of designing and iterating prompts to steer model outputs without changing the model itself. Fine-tuning, by contrast, modifies the model's weights by training it on task-specific data. Prompt engineering is faster, cheaper, and easier to iterate on, while fine-tuning can achieve better results on specialized tasks but requires more data and computational resources.

### What is a context window in AI?

A context window is the maximum number of tokens the model can consider at once, including system prompt, conversation history, and retrieved documents. When context limits are exceeded, older or middle parts of the context are truncated or ignored. Understanding context window size is crucial for managing costs and latencies, as longer contexts are more expensive and slower to process.

Apply these techniques with a local LLM or your own API keys — PromptQuorum works with any backend.

[Try PromptQuorum free →](https://www.promptquorum.com/)

[← Back to Prompt Engineering](https://www.promptquorum.com/prompt-engineering)
