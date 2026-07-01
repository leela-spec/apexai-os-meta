Title: Chain-of-Thought Prompting: Make AI Show Its Reasoning

URL Source: https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting

Published Time: 2026-03-26

Markdown Content:
Techniques

Last updated:May 2026·13 min read·By [Hans Kuepper](https://www.promptquorum.com/about) · Founder of PromptQuorum, multi-model AI dispatch tool · PromptQuorum

Read in:

Chain-of-thought prompting is a technique where you explicitly ask the model to show its reasoning steps instead of jumping straight to the final answer. This makes complex decisions easier to audit, debug, and improve over time.

**Chain-of-thought (CoT) prompting instructs an AI model to show its reasoning step by step before giving a final answer.** This improves accuracy on math, logic, and multi-step tasks. In 2026, frontier models like Claude Opus 4.8 and OpenAI o3 have built-in reasoning modes that automate CoT internally — but prompt-level CoT remains valuable on smaller and non-reasoning models where it's the primary way to elicit structured thinking.

1.   1
**Chain-of-thought prompting asks models to show reasoning steps before giving a final answer**, improving accuracy on math, logic, and multi-step tasks.

2.   2
Zero-shot CoT ("think step by step") works on most models. Few-shot CoT (with worked examples) is more reliable.

3.   3
In 2026, frontier models like Claude Opus 4.8 and OpenAI o3 have **built-in reasoning modes** that subsume prompt-level CoT — you don't need to say "think step by step" on these models.

4.   4
CoT increases output tokens and therefore cost. Built-in reasoning modes add separate thinking token budgets with their own billing.

5.   5
Use prompt-level CoT on non-reasoning models (Haiku, Flash, LLaMA 4) for cost-effective reasoning. Use built-in reasoning modes on frontier models for maximum accuracy.

6.   6
CoT is most valuable for math, logic, planning, and root-cause analysis. Skip it for simple classification, short answers, and quick copywriting.

Contents

1.   [Key Takeaways](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#key-takeaways)
2.   [Quick Facts](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#quick-facts)
3.   [What Is Chain-of-Thought Prompting?](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#what-is-chain-of-thought)
4.   [Why It Matters](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#why-it-matters)
5.   [When It Helps (and When It Doesn't)](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#when-it-helps)
6.   [Example: Without vs With CoT](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#example-without-vs-with)
7.   [Math Example: Revenue Calculation](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#math-example)
8.   [How to Write Effective Prompts](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#how-to-write)
9.   [Chain-of-Thought in PromptQuorum](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#in-promptquorum)
10.   [How to Use CoT Prompting](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#how-to-start)
11.   [CoT vs Built-In Reasoning Models](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#reasoning-models)
12.   [Chain-of-Thought Variants](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#cot-variants)
13.   [Model Comparison](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#model-comparison)
14.   [Related Reading](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#related-reading)
15.   [FAQ](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#faq)
16.   [Sources](https://www.promptquorum.com/prompt-engineering/chain-of-thought-prompting#sources)

## Quick Facts

1.   1
**Coined:** Wei et al. (2022), Google Brain — NeurIPS 2022 foundational paper

2.   2
**Key result:** Zero-shot CoT raised PaLM 540B accuracy from 17.7% → 78.7% on MultiArith

3.   3
**Trigger phrase:** "Let's think step by step" (zero-shot) or worked examples (few-shot)

4.   4
**2026 evolution:** Built-in reasoning modes (o3, Claude extended thinking) now automate CoT internally

5.   5
**Cost impact:** Prompt-level CoT = more output tokens; reasoning modes = separate thinking token budget

6.   6
**Best models for prompt-level CoT:** Non-reasoning models (Claude Haiku 4.5, Gemini Flash, GPT-5.5 mini, LLaMA 4 Scout)

## What Chain-of-Thought Prompting Is

**Chain-of-thought prompting asks the model to reason step by step before giving a final conclusion.** Instead of returning only "the answer," the model writes out intermediate calculations, logical steps, or explanations.

You can trigger this behavior by instructions like "think step by step," "show your reasoning," or by providing worked examples where the reasoning is explicit. The result is a trace you can read to understand how the model reached its conclusion.

## Why Chain-of-Thought Prompting Matters

**Chain-of-thought prompting matters because it makes model behavior more transparent on tasks that involve multi-step reasoning.** When you see each step, you can spot misinterpretations, missing assumptions, or arithmetic errors.

This is especially valuable in domains like analytics, planning, and troubleshooting. Instead of a single opaque output, you get a narrative that can be checked, corrected, or reused as documentation.

🔍Works with local models

Chain-of-thought works on any model with 7B+ parameters. Test it locally with [Ollama or LM Studio](https://www.promptquorum.com/local-llms).

## When Chain-of-Thought Helps (and When It Doesn't)

**Chain-of-thought prompting helps most on tasks that naturally break into clear steps, but it is not necessary for every prompt.** It shines wherever the path is as important as the destination.

Chain-of-Thought reasoning is what lets a tool-calling agent stay reliable across multi-step tasks. For a local agent stack that gives a CoT-capable model the ability to query databases and edit files, see [Local AI Agents With MCP](https://www.promptquorum.com/power-local-llm/local-ai-agents-with-mcp-2026).

Good use cases include:

*   Math and quantitative reasoning problems.
*   Multi-step logical puzzles or decision analyses.
*   Root-cause analysis, incident postmortems, and trade-off discussions.
*   Planning tasks where the sequence of actions must be explicit.

For simple classification, quick copywriting, or short factual answers, chain-of-thought often adds verbosity without much extra value. In sensitive domains, you may also want to keep reasoning internal and show only the final answer to end users.

## Example: Without vs With Chain of Thought

**The difference becomes clear when you compare a direct-answer prompt with one that explicitly asks for reasoning.** Here is a simple decision example.

Bad Prompt

"Which project should we prioritize next quarter?"

Good Prompt

"You are a product operations manager. We have three candidate projects for next quarter. Use chain-of-thought reasoning to decide which project to prioritize. 1) List the decision criteria you will use (for example revenue impact, risk, alignment with strategy). 2) Evaluate each project against these criteria step by step. 3) Make a clear recommendation and justify it in 3–5 sentences. At the end, provide a short final answer starting with `Recommendation:` on a separate line."

In the "good" version, the model explains how it chose its criteria, how each project scores, and then states a recommendation you can challenge or accept.

## How to Write Effective Chain-of-Thought Prompts

**To write effective chain-of-thought prompts, you should define the structure of the reasoning and the structure of the final answer.** Vague requests like "explain more" are less reliable than concrete instructions.

A practical pattern is:

*   Tell the model its role (for example "You are a senior data analyst.").
*   Specify that it should think step by step or use chain-of-thought.
*   Define the sections of reasoning you expect (for example assumptions, calculations, comparison, conclusion).
*   Ask for a short, clearly marked final answer at the end so you can use it quickly.

This separates the detailed reasoning from the concise output, which is helpful when you integrate the result into other tools or reports.

## Chain-of-Thought Prompting in PromptQuorum

**PromptQuorum is a multi-model AI dispatch tool where you can apply chain-of-thought prompting consistently across different models.** You write one structured chain-of-thought prompt and send it to several providers in parallel.

In PromptQuorum, you can:

*   Combine chain-of-thought instructions with reasoning-focused frameworks such as TRACE or APE so that thinking steps are explicitly labeled.
*   Compare how different models handle the same reasoning task and inspect their step-by-step traces side by side.
*   Save chain-of-thought prompts as templates for recurring analyses, incident reviews, or strategic decisions.

This turns chain-of-thought prompting from a one-off trick into a repeatable part of your decision-making process.

## How to Use Chain-of-Thought (CoT) Prompting

1.   1
**For logic, reasoning, or debugging tasks, ask the model to 'think step by step' before answering.** Instead of 'What is the bug?', ask 'Trace the execution step by step, then identify the bug.'

2.   2
**Provide a worked example showing step-by-step reasoning.** Don't just describe it—show the model what step-by-step reasoning looks like. Example: 'First, I check the function signature... Then, I trace the first call with input X...'

3.   3
**Use explicit prompts like 'Let's think step by step' or 'First, identify... Then...'** These trigger more deliberate reasoning in the model.

4.   4
**For complex problems, ask the model to trace intermediate outputs.** Example: 'Trace the execution of this function for input 5. Show the value of each variable after each line.'

5.   5
**Combine CoT with verifiable outputs: ask the model to show its work so you can audit it.** 'Explain your reasoning at each step. If you make a mistake, I should be able to spot it from your shown work.'

## Math Example: Revenue Calculation

**Without CoT, a model might give a single final answer. With CoT, the model shows calculations step by step.**

**Without CoT:**

"A customer buys 50 units at $15 each, but gets a 10% discount. What do they pay?"

Model: "$675"

**With CoT:**

"A customer buys 50 units at $15 each, but gets a 10% discount. Work through this step by step: 1) Calculate the subtotal. 2) Calculate the discount amount. 3) Subtract the discount from the subtotal to get the final price."

Model: "1) Subtotal = 50 × $15 = $750. 2) Discount = 10% of $750 = $75. 3) Final price = $750 − $75 = $675."

Both give the same answer, but the CoT version lets you see the math and catch errors (e.g., if someone miscalculates 10% of $750).

## CoT vs Built-In Reasoning Models (2026)

**In 2026, the frontier models—Claude Opus 4.8, OpenAI o3, Gemini Deep Think—have built-in reasoning modes that internalize chain-of-thought automatically.** You do not need to add "think step by step" instructions on these models.

**When to use prompt-level CoT:** Non-reasoning models (Claude Haiku 4.5, GPT-5.5 mini, Gemini Flash, Llama 4), local LLMs, or when you want to avoid the extra cost of reasoning token budgets.

**When to use built-in reasoning modes:** Maximum accuracy on frontier models, math-heavy tasks, complex analysis. These models bill reasoning tokens separately (usually higher rate than output tokens). Test your CoT prompts in [Anthropic's Console](https://docs.anthropic.com/) or [OpenAI's Playground](https://platform.openai.com/playground) before deploying to production.

| Approach | Best For | Cost | Transparency | Models |
| --- | --- | --- | --- | --- |
| Prompt-level CoT ("think step by step") | Small models, local LLMs, cost-sensitive tasks | Increases output tokens | Full: visible steps in output | Haiku, Flash, LLaMA, Qwen |
| Claude extended thinking (Opus 4.8, Sonnet 4.6) | Complex analysis, maximum accuracy | Separate thinking token budget (input rate) | Inspector trace via API | Claude Opus 4.8, Claude Sonnet 4.6 |
| OpenAI o3 | Hardest problems (math, coding, competition) | Reasoning token budget (higher tier) | Hidden reasoning, visible output | OpenAI o3 |
| Gemini Deep Think | Google Cloud integration, Gemini ecosystem | Thinking tokens separate from output | thinking_level parameter (LOW, MEDIUM, HIGH) | Gemini 3.1 Pro |
| DeepSeek R1 | Open-weights option, on-device reasoning | Visible reasoning streamed as output text | Full: inline CoT in output | DeepSeek R1 |

💡Pro Tip

If you're building for cost, use prompt-level CoT on smaller models. If you're building for accuracy on hard problems, use o3 or Claude extended thinking and let the model handle reasoning internally.

## Chain-of-Thought Variants and Extensions

**Beyond the basic "think step by step" pattern, researchers have developed several CoT variants, each optimized for different problem types.**

*   **Zero-shot CoT:** Ask "Let's think step by step" with no examples. Works on most models and is the simplest to implement. Boost: ~10–20% accuracy improvement on reasoning tasks.
*   **Few-shot CoT:** Show 2–5 worked examples where the reasoning is explicit, then ask the model to apply the same pattern to a new problem. More reliable than zero-shot but requires manual example creation. Boost: ~20–40% accuracy.
*   **Self-consistency (Wang et al., 2023):** Generate multiple CoT reasoning paths independently, then take a majority vote on the final answer. Significantly more robust to errors. Boost: ~30–50% on hard tasks.
*   **Tree of Thought (ToT):** Instead of a linear chain, explore multiple reasoning branches and prune poor ones. Use when there are many possible solution paths (planning, game-playing, creative tasks).
*   **ReAct (Reasoning + Acting):** Interleave reasoning with external actions—call APIs, search databases, or run code—and incorporate the results back into the next reasoning step. Best for real-world tasks that need live data or verification.

## Model Comparison: How Models Handle CoT Prompting (2026)

| Model | Prompt-Level CoT | Built-In Reasoning | Best Use Case | Cost (approx.) |
| --- | --- | --- | --- | --- |
| Claude Opus 4.8 | Not needed | Extended thinking (inspect trace via API) | Maximum accuracy analysis | Higher (input + output + thinking tokens) |
| Claude Sonnet 4.6 | Not needed | Extended thinking | Balanced accuracy/cost | Medium |
| Claude Haiku 4.5 | Recommended | None | Fast, cost-effective reasoning | Low |
| OpenAI o3 | Not needed | Effort levels (low, medium, high, xhigh) | Competition-level problems | Very high (reasoning token tier) |
| GPT-5.5 mini | Recommended | None | Budget-conscious deployment | Very low |
| Gemini 3.1 Pro | Works | Deep Think (thinking_level param) | Google Cloud integration | Medium-high |
| Gemini Flash | Recommended | None | Fast responses | Low |
| DeepSeek R1 | Not needed | Inline reasoning in output | Open-weights, on-device | Free (open source) |
| Llama 4 | Recommended | None | Local deployment, privacy | Self-hosted (compute-dependent) |

## Frequently Asked Questions

### Does chain-of-thought work on all models?

Chain-of-thought works on most models with 7B+ parameters, but the benefit varies. It's most effective on mid-size and smaller models (Haiku, Flash, Llama 4). On frontier models (Claude Opus 4.8, o3), built-in reasoning modes are often more efficient than prompt-level CoT.

### Does chain-of-thought increase cost?

Yes, prompt-level CoT increases the number of output tokens (since the model writes out reasoning before the final answer). Built-in reasoning modes (Claude extended thinking, OpenAI o3) use separate thinking token budgets that may have different billing rates. Test both on your use case to compare cost vs accuracy tradeoff.

### When should I use few-shot CoT instead of zero-shot?

Use zero-shot CoT first—it's simpler and works in most cases. Move to few-shot (with 2–5 examples) if zero-shot is unreliable or if your domain requires specific reasoning patterns (e.g., financial analysis with standard line-item structure).

### Can I combine chain-of-thought with structured output (JSON)?

Yes. You can ask the model to show its reasoning in plain text first, then output a JSON object with the final answer. Combine instructions: "Think step by step. Then output your result as valid JSON." This is common in production systems.

### What's the difference between chain-of-thought and tree-of-thought?

Chain-of-thought is a linear sequence: step 1 → step 2 → ... → conclusion. Tree-of-thought explores multiple branches (alternative reasoning paths) and prunes weaker ones before arriving at the answer. Tree-of-thought is more powerful but more expensive (requires multiple model calls).

### Does OpenAI o3 require chain-of-thought prompting?

No. OpenAI o3 has built-in reasoning that activates automatically. You do not need to add "think step by step" instructions. Just give o3 the problem and set the effort level (low/medium/high/xhigh) to control how much reasoning budget to spend.

### Can I audit the reasoning of built-in reasoning models?

Yes, but it depends on the model. Claude extended thinking reasoning traces are inspectable via API. OpenAI o3 reasoning is hidden by default (for competitive advantage). Gemini Deep Think reasoning is also hidden. For full auditability, use prompt-level CoT or DeepSeek R1.

### Is chain-of-thought prompting suitable for real-time applications?

Prompt-level CoT adds latency (more output tokens = slower generation). For real-time use cases, either use smaller models with minimal reasoning, or use stream endpoints to show tokens as they arrive. Built-in reasoning modes may add even more latency; benchmark your specific use case.

## Sources & Further Reading

*   Wei, J., Wang, X., Schuurmans, D., et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS 2022. arXiv:2201.11903
*   Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). "Large Language Models are Zero-Shot Reasoners." NeurIPS 2022. arXiv:2205.11916
*   Wang, X., Wei, J., Schuurmans, D., et al. (2023). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." ICLR 2023. arXiv:2203.11171
*   Anthropic. (2024). "Extended Thinking in Claude." Technical documentation on Claude Opus 4.8 and Sonnet 4.6 reasoning capabilities.
*   OpenAI. (2026). "OpenAI o3: Reasoning Models for Competition-Level Problem Solving." OpenAI documentation and research announcements.

Apply these techniques with a local LLM or your own API keys — PromptQuorum works with any backend.

[Try PromptQuorum free →](https://www.promptquorum.com/)

[← Back to Prompt Engineering](https://www.promptquorum.com/prompt-engineering)
