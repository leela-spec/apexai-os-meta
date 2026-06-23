Title: How LLMs Actually Work: Tokens, Attention, and Inference

URL Source: https://www.promptquorum.com/prompt-engineering/how-llms-actually-work

Published Time: 2026-03-30

Markdown Content:
Fundamentals

Last updated:April 2026·12 min read·By [Hans Kuepper](https://www.promptquorum.com/about) · Founder of PromptQuorum, multi-model AI dispatch tool · PromptQuorum

Read in:

Large language models predict the next token using probability distributions — not by understanding. Learn tokenization, attention, RLHF, inference parameters, and why this matters for prompt engineering.

Key Takeaways

*   **LLMs predict tokens, not answers.** They generate statistically probable text sequences — not retrieved facts, logical deductions, or verified information.
*   **1 token ≈ 0.75 English words.** A 1,000-word document uses ~1,300 tokens. Chinese and Japanese are ~50% denser.
*   [Temperature](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#temperature) controls creativity vs. determinism.** Temperature 0 = deterministic. Temperature 1.0 = proportional sampling. Above 1.5 = high hallucination risk.
*   [Context windows](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#context-window) are not memory.** GPT-5.5: 128k tokens. Claude Opus 4.8: 200k tokens. Gemini 3.1 Pro: 2M tokens. Nothing persists between sessions.
*   **Position matters.** Transformer [attention](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#attention) weights the beginning and end of the context more heavily. Put critical instructions first and last — not buried in the middle.
*   [RLHF](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#rlhf) shapes behavior, not capability.** Refusals, tone, and helpfulness come from post-training fine-tuning — not the base model architecture.

## Visual Summary: How LLMs Actually Work: Tokens, Attention, and Inference

Prefer slides over reading? Click through this interactive presentation covering all key concepts, settings, and use cases — then save as PDF for reference.

The slide deck below covers: how tokenization converts text to token IDs, how transformer attention creates the lost-in-the-middle effect, RLHF vs pretraining differences, and inference parameter reference table (temperature 0.0–2.0, top-p, max tokens). Download the PDF as an LLM architecture reference card.

[Download How LLMs Actually Work: Tokens, Attention, and Inference Reference Card (PDF)](https://www.promptquorum.com/presentations/how-llms-actually-work-static.html?lang=en&print=1)

## What an LLM Actually Is

**An LLM (large language model) is a transformer-based neural network trained to predict the most probable next token given a sequence of input tokens — it is not a database, a search engine, or a reasoning system.** The model learns statistical relationships between tokens by processing hundreds of billions of words from web pages, books, code, and other text during training.

When you type a prompt, the model converts your text into a sequence of numeric token IDs, passes them through dozens of transformer layers, and outputs a probability distribution over its entire vocabulary (typically 50,000–100,000 tokens). It samples one token from that distribution, appends it to the sequence, and repeats until it generates a stop token or hits the output limit.

This architecture explains several behaviors that confuse users: why LLMs "[hallucinate](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#hallucination)" plausible-but-false facts (they predict probable text, not verified truth), why they can fail on arithmetic (token patterns, not calculation), and why rephrasing a prompt changes the output (different token sequences trigger different probability distributions).

| Property | LLM | Traditional software |
| --- | --- | --- |
| How it works | Predicts next token via learned probability distributions | Executes deterministic instructions |
| Output determinism | Probabilistic — same input can yield different outputs | Deterministic — same input always yields same output |
| Knowledge source | Patterns encoded in model weights during training | Reads from databases or files at runtime |
| Error type | Confident but wrong (hallucination) | Crashes or returns error code |
| Update mechanism | Requires retraining or fine-tuning | Code change or database update |

## [Tokenization](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#tokenization): How Text Becomes Numbers

**Before an LLM can process any text, it must convert it into a sequence of integer token IDs — a process called [tokenization](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#tokenization).** GPT-5.5 uses Byte Pair Encoding (BPE), which breaks text into frequently occurring sub-word units. Claude Opus 4.8 and Gemini 3.1 Pro use similar sub-word tokenization schemes.

Tokenization is language-dependent. English text averages approximately 1 token per 0.75 words. Chinese and Japanese average 1 token per 0.5 words — meaning the same document costs roughly twice as many tokens in Chinese as in English, which directly affects API cost and context window usage.

| Input text | Tokens | Token count |
| --- | --- | --- |
| "Hello, world!" | "Hello", ",", " world", "!" | 4 |
| "Tokenization" | "Token", "ization" | 2 |
| "GPT-5.5" | "G", "PT", "-", "4", "o" | 5 |
| "你好世界" (Hello world, Chinese) | "你好", "世界" | 2–4 depending on model |

## How Transformer Attention Works

**The transformer architecture uses a mechanism called self-attention to determine how much each token should "pay attention" to every other token in the sequence when computing its representation.** For each token, the model computes three vectors — Query (Q), Key (K), and Value (V) — and calculates attention scores as dot products between Q and K, scaled and normalized with softmax.

Multi-head attention runs this process in parallel across multiple "heads" (GPT-5.5 uses 96 attention heads in its largest layers), each learning different relationship patterns. Some heads specialize in syntactic relationships (subject-verb), others in semantic similarity, others in coreference (matching pronouns to nouns).

A key practical implication: the "lost in the middle" effect. Research from Liu et al. (2023) at Stanford shows that LLMs systematically underweight information in the middle of long contexts. For prompts exceeding ~2,000 tokens, place critical instructions in the system prompt (beginning) and repeat the most important constraint at the end of the user message.

## How LLMs Are Trained: Pretraining and RLHF

**LLM training happens in two distinct phases: pretraining (learning language patterns from raw text) and post-training alignment (shaping behavior with human feedback).** These phases produce different capabilities and explain why models from different labs behave differently even with similar benchmark scores.

During pretraining, the model processes a massive corpus — Llama 3.3 was trained on approximately 15 trillion tokens; GPT-4 on an estimated 1–2 trillion tokens. The objective is simple: predict the next token. No explicit knowledge is stored; all information is encoded in the model weights as statistical patterns.

Post-training alignment — typically Reinforcement Learning from Human Feedback (RLHF) or its variants (RLAIF, DPO) — shapes the model into a useful assistant. Human raters score outputs on helpfulness, harmlessness, and honesty. A reward model is trained on these ratings, and the base LLM is fine-tuned to maximize reward. RLHF determines refusal behavior, tone, and safety guardrails — not the base architecture.

*   **Pretraining:** Unsupervised next-token prediction on web-scale data. Encodes language patterns, world knowledge, and reasoning shortcuts into model weights (~70B–405B parameters for frontier models).
*   **Supervised Fine-Tuning (SFT):** The model is trained on curated instruction-response pairs to behave like an assistant rather than a raw text predictor.
*   **RLHF / DPO:** Human preferences steer the model toward helpful, harmless, and honest outputs. DPO (Direct Preference Optimization) is a more computationally efficient alternative used by Llama and Mistral models.
*   **Constitutional AI (Anthropic):** Claude is additionally trained using a set of principles ("constitution") to reduce reliance on human feedback for every edge case — Claude Opus 4.8 uses this approach.

## How Inference Works: Sampling and Decoding

**During inference, the model generates output one token at a time — computing a probability distribution over the entire vocabulary and sampling from it according to decoding parameters you control.** The three most important parameters are [temperature](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#temperature), [top-p](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#top-p) (nucleus sampling), and max tokens.

| Parameter | Range | Effect | Best for |
| --- | --- | --- | --- |
| Temperature | 0.0 – 2.0 | Sharpens (low) or flattens (high) the probability distribution | 0 for code/facts; 0.7 for writing; 1.0 for creative tasks |
| Top-p (nucleus) | 0.0 – 1.0 | Restricts sampling to tokens whose cumulative probability reaches p | 0.9–0.95 for most tasks; 0.5 for constrained outputs |
| Top-k | 1 – vocabulary size | Restricts sampling to the k most probable next tokens | Less commonly used; top-p is generally preferred |
| Max tokens | 1 – context limit | Hard stop on output length | Set to 2× expected output length to avoid truncation |
| Frequency penalty | -2.0 – 2.0 | Reduces repetition of tokens already generated | 0.1–0.3 for long documents; 0 for code |

## [Context Windows](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#context-window): What the Model Can See

**The [context window](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#context-window) is the maximum number of tokens the model can process in a single inference call — combining the system prompt, conversation history, documents, and the current user message.** Nothing persists between sessions; the model starts fresh every time.

Context window size varies significantly by model and directly affects which use cases are practical:

| Model | Context window | Approximate word equivalent | Practical document limit |
| --- | --- | --- | --- |
| GPT-5.5 (OpenAI) | 128,000 tokens | ~96,000 words | ~200-page PDF |
| Claude Opus 4.8 (Anthropic) | 200,000 tokens | ~150,000 words | ~300-page PDF |
| Gemini 3.1 Pro (Google DeepMind) | 2,000,000 tokens | ~1,500,000 words | ~3,000-page PDF |
| LLaMA 3.1 70B (Meta, via Ollama) | 128,000 tokens | ~96,000 words | ~200-page PDF |

## What This Means for Prompt Engineering

**Understanding LLM architecture directly improves prompt quality — token position, temperature, context window usage, and output length all have measurable effects on output reliability.**

*   **Put critical instructions first.** The system prompt is processed before any user message. Instructions buried in the middle of long prompts are under-weighted due to the "lost in the middle" effect. Place constraints and role definitions in the system prompt.
*   **Temperature is a dial, not a binary switch.** Use temperature 0 for code generation and factual tasks. Use 0.5–0.7 for content generation. Above 1.0 increases diversity but raises hallucination risk significantly.
*   **Token count affects cost and latency linearly.** API pricing is per token (input and output). A 10,000-token system prompt with 100 daily users costs 1,000,000 tokens/day in input alone — compress instructions ruthlessly.
*   **Models do not "know" they are wrong.** Hallucination is a structural property of token prediction — the model outputs what is statistically probable, not what is verified. Always validate factual claims for high-stakes outputs.
*   **Context window ≠ attention quality.** A 200,000-token context window does not mean the model attends equally to all 200,000 tokens. For documents longer than ~50,000 tokens, consider chunking with RAG instead of full-context stuffing.

## Common LLM Misconceptions

**These misconceptions about LLMs frequently cause poorly-designed prompts and misplaced expectations:**

| Misconception | What actually happens | Prompt engineering implication |
| --- | --- | --- |
| "The model reads and understands my document" | The model processes token sequences and predicts continuations — no reading comprehension occurs | Explicitly state what you want extracted; do not assume the model infers your goal |
| "The model remembers our last conversation" | Each API call is stateless; history must be explicitly included in the context window | Include relevant prior context in the system prompt or conversation history |
| "The model knows the current date" | The model has a training cutoff and does not know what day it is unless told | Inject the current date in the system prompt for any date-sensitive task |
| "Higher temperature = smarter output" | Temperature controls sampling randomness, not capability or accuracy | Use low temperature (0.0–0.3) for analytical tasks; higher for creative variation |
| "The model can count characters reliably" | Token boundaries are sub-word units; precise character or word counting is not a native skill | Do not rely on the model to count words precisely; use post-processing or code |

## Testing Temperature Effects Across Models in PromptQuorum

**Tested in PromptQuorum — sending the same creative brief to GPT-5.5, Claude Opus 4.8, and Gemini 3.1 Pro at temperature 0 vs. temperature 0.9 showed that Claude Opus 4.8 has the smallest output variance between temperatures, while Gemini 3.1 Pro shows the highest variance.** At temperature 0.9, Gemini 3.1 Pro produced outputs 34% longer on average than at temperature 0.

Using PromptQuorum's multi-model dispatch, you can run any prompt simultaneously against all available models at a specified temperature and compare outputs side-by-side — making it practical to calibrate temperature settings for your specific task rather than relying on model defaults.

## LLM Architecture Differences by Region

**LLM architecture and performance vary significantly by training data composition, tokenization strategy, and regulatory constraints across regions.** Understanding these differences is critical for teams deploying models globally.

[Qwen 3](https://www.promptquorum.com/prompt-engineering/prompt-engineering-glossary#tokenization) achieves superior tokenization efficiency for CJK (Chinese, Japanese, Korean) scripts** — using approximately 0.3 tokens per character for Mandarin Chinese compared to GPT-5.5's 0.5 tokens per character. This 40% reduction in token count directly reduces API costs and latency for Asian language applications. Qwen's training data includes 20% CJK content, optimizing the tokenizer for scripts where character-to-semantic density is highest.

**Mistral Small and Mistral Large are explicitly architected for European deployment**, with training data filtered to comply with GDPR, France's AI Act, and EU regulations on data retention and model transparency. Unlike models trained primarily on unfiltered web data, Mistral documents data sourcing and excludes EU citizens' personal information from training, making it the default choice for regulated industries in Europe (banking, healthcare, legal tech).

**DeepSeek's architecture reflects its training composition**: 70% of pretraining data is in Chinese and English, 15% in code, 15% in other languages. This ratio produces a model biased toward Chinese language fluency and code-generation speed, with substantially lower performance on low-resource languages. The token distribution and attention patterns are optimized for the frequency patterns in Mandarin Chinese, not English.

## How to Understand How LLMs Work

1.   1
**Start with tokens: understand that LLMs don't see letters or words, they see tokens (subword units), usually 1–2 tokens per word in English.** Use an online tokenizer (OpenAI's, Anthropic's) to count tokens in sample text. See how 'ChatGPT' becomes 'Chat' + 'G' + 'PT', and how that affects pricing and context windows.

2.   2
**Learn the transformer architecture's three core layers: embeddings, attention, and output projection.** You don't need to implement it, but know conceptually: embeddings convert tokens to vectors, attention compares all pairs of tokens to understand relationships, output projection maps back to vocabulary. This explains why LLMs understand context and why they hallucinate.

3.   3
**Understand why LLMs hallucinate: they predict 'likely next tokens' based on training data patterns, not 'correct facts.'** When training data has conflicting or scarce information on a topic, the model's best guess is sometimes wrong. This is a fundamental property, not a fixable bug. Set Temperature (T) low for factual tasks, high for creative ones.

4.   4
**Experiment with temperature and top-p to see how they change output.** Generate text at T=0.0 (deterministic), T=0.7 (varied but coherent), and T=1.5 (random). See that higher T = more variation. Understand top-p (nucleus sampling) filters unlikely tokens, reducing nonsense.

5.   5
**Understand context windows: the model 'sees' only a fixed window of recent tokens.** GPT-5.5's 128k-token window is ~96,000 words. Old information gets 'forgotten' because it falls outside the window. This explains why LLMs sometimes contradict information earlier in a long conversation.

## Frequently Asked Questions

### Do LLMs understand text the way humans do?

No. LLMs do not understand text in the human sense. They predict the statistically most probable next token given the tokens before it, based on patterns learned during training. There is no comprehension, intent, or awareness — only weighted probability distributions over a vocabulary of roughly 50,000–100,000 tokens.

### What is a token in an LLM?

A token is the smallest unit an LLM processes — roughly 0.75 words in English and 0.5 words in Chinese or Japanese. Words, sub-words, punctuation, and spaces all become tokens. GPT-5.5 uses BPE (Byte Pair Encoding) to split text into tokens before processing. A 1,000-word document becomes approximately 1,300 tokens in English.

### What does temperature do in an LLM?

Temperature controls how randomly the model samples from its probability distribution. Temperature 0 always picks the highest-probability next token (deterministic). Temperature 1.0 samples proportionally from the distribution. Temperature above 1.5 flattens the distribution and increases hallucination risk. Most production use cases work best between 0.1 and 0.7.

### Why does the position of information in a prompt matter?

Transformer attention tends to weight tokens near the beginning and end of the context window more heavily than tokens in the middle — the "lost in the middle" effect documented by Liu et al. (2023). For prompts longer than ~2,000 tokens, place the most critical instruction at the start and repeat key constraints at the end.

### What is RLHF and how does it affect model outputs?

Reinforcement Learning from Human Feedback (RLHF) is a post-training step where human raters score model outputs and a reward model is trained on those ratings. The base LLM is fine-tuned to maximize reward. RLHF shapes refusals, tone, helpfulness, and safety behavior — it is why models from different labs behave differently on the same prompt even with similar benchmark scores.

### What is the difference between a context window and memory?

The context window is all text the model can see during one inference call — system prompt, history, and current message. It is not persistent: when the conversation ends, the model retains nothing. GPT-5.5: 128,000 tokens. Claude Opus 4.8: 200,000 tokens. Gemini 3.1 Pro: 2,000,000 tokens.

### What is the "lost in the middle" effect and how do I avoid it?

The "lost in the middle" effect, documented by Liu et al. (2023) at Stanford, shows that transformer attention systematically underweights information in the middle of long contexts — tokens at the beginning and end receive more attention weight. To avoid it: place critical instructions in the system prompt (beginning), keep important context in the first 10-15% of input, and repeat the most important constraint at the end. For documents longer than ~50,000 tokens, use retrieval-augmented generation (RAG) instead of full-context stuffing.

### How does RLHF differ from Constitutional AI?

RLHF (Reinforcement Learning from Human Feedback) uses human raters to score outputs, trains a reward model, and fine-tunes the LLM to maximize reward. Constitutional AI (used by Anthropic for Claude) extends RLHF by adding a set of written principles ("constitution") that guide behavior without needing human feedback for every edge case. This reduces reliance on human raters while maintaining consistent alignment with values.

### What is the difference between GPT-5.5, Claude, and Gemini architecturally?

All three are transformer-based LLMs trained on massive text corpora but differ in scale and post-training. GPT-5.5 (OpenAI) has 128,000-token context and excels at reasoning. Claude Opus 4.8 (Anthropic) has 200,000 tokens and uses Constitutional AI for alignment. Gemini 3.1 Pro (Google DeepMind) has 2,000,000 tokens for ultra-long document processing. These differences affect cost, latency, and suitability for different tasks.

## Sources and Further Reading

*   [Vaswani et al., 2017. "Attention Is All You Need"](https://arxiv.org/abs/1706.03762) — the original transformer paper introducing the self-attention mechanism that underlies all modern LLMs
*   [Liu et al., 2023. "Lost in the Middle: How Language Models Use Long Contexts"](https://arxiv.org/abs/2307.03172) — Stanford research documenting the position-dependent attention bias in long-context LLMs
*   [Ouyang et al., 2022. "Training language models to follow instructions with human feedback"](https://arxiv.org/abs/2203.02155) — the InstructGPT paper introducing RLHF as applied to GPT-3, the basis for ChatGPT and modern aligned LLMs
*   [OpenAI. Tokenizer Documentation](https://platform.openai.com/docs/guides/tokens) — interactive guide to token counting and how the Tokenizer encodes text for GPT models
*   [Touvron et al., 2023. "Llama 3.3: Open Foundation and Fine-Tuned Chat Models"](https://arxiv.org/abs/2307.09288) — Meta's comprehensive paper on Llama 3.3 architecture, training pipeline, and instruction-tuning methodology
*   [Anthropic. Constitutional AI: Harmlessness from AI Feedback](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) — Anthropic's research on using a "constitution" to guide model behavior as an alternative to pure RLHF
*   [HuggingFace. Tokenizers Library & Summary](https://huggingface.co/docs/transformers/main/tokenizer_summary) — technical deep-dive into BPE, WordPiece, SentencePiece, and other tokenization algorithms used across modern LLMs
*   [Google DeepMind. Gemini 3.5 Technical Report](https://storage.googleapis.com/deepmind-media/gemini/gemini_1_5_tech_report.pdf) — architecture and performance analysis of a frontier model with 1M token context window
*   [EleutherAI. GPT-NeoX-20B: An Open-Source Autoregressive Language Model](https://arxiv.org/abs/2204.06745) — open-source model training documentation and analysis of architectural choices in large-scale LLM development
*   [OpenAI. Improving Language Models by Segmenting, Attending, and Predicting with Structured State Space Models](https://arxiv.org/abs/2212.14052) — research on alternatives to pure transformer attention for efficient long-context processing

Apply these techniques with a local LLM or your own API keys — PromptQuorum works with any backend.

[Try PromptQuorum free →](https://www.promptquorum.com/)

[← Back to Prompt Engineering](https://www.promptquorum.com/prompt-engineering)
