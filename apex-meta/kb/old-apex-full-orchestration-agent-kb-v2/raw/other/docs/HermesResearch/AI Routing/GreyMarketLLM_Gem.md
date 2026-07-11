What you are describing is a highly specific, rapidly growing phenomenon in the AI engineering space often referred to as **"API Pooling"**, **"LLM Relays,"** or **"Gray-Market LLM Routers."** You are entirely correct that it functions similarly to legitimate aggregators like OpenRouter, but it operates with drastically different economic, technical, and risk dimensions.

Here is the breakdown of how these services manage to offer tokens at roughly 1% to 5% of official market rates, what is happening under the hood, and the major caveats you need to keep in mind for a training or development workflow.

## 1. How the Arbitrage Works (The "1%" Price Secret)

The deep discounts you are seeing (often sold on platforms like Taobao, Xianyu, or specialized developer forums) rely on a mix of legitimate structural cost advantages and highly aggressive gray-market pooling strategies:

- **Legitimate Domestic Price Wars:** Right now, major Chinese tech infrastructure providers (like Xiaomi, DeepSeek, Alibaba, and Bytedance) are engaged in a massive permanent price war. For instance, Xiaomi recently slashed its MiMo-V2.5 API costs by up to 99%, bringing costs down to fractions of a cent per million tokens due to custom inference optimizations (like SGLang HiCache architectures). Legit domestic tokens are natively incredibly cheap.
    
- **Subscription Slicing (The "Max Account" Loophole):** For Western models like GPT or Claude, proxy operators buy premium flat-rate team or enterprise subscription accounts (which allow high or quasi-unlimited token usage for a fixed monthly fee). The operator builds an API gateway in front of these accounts, splits the capacity into tiny token streams, and resells them to thousands of developers.
    
- **Credit & Promotion Abuse:** Operators use botnets or automated scripts to bulk-register accounts using educational (.edu) emails or stolen credentials to harvest free tier credits and API tokens, funneling them into a single endpoint pool.
    

## 2. Technical Mechanics: What is an LLM Relay?

An **LLM Relay** or **Reverse Proxy** acts as an intermediary gateway between your local environment and the target models.

Instead of pointing your base URL to `api.openai.com`, you point your application to a custom proxy endpoint (e.g., a local or gray-market server running gateway tools like One-API or specialized routing scripts).

```
[Your System / Training Script]
          │
          ▼ (OpenAI-Compatible API Format)
[Gray-Market Proxy Gateway]
          │
          ├───► Pool A: Exploited Flat-rate Accounts (GPT/Claude)
          ├───► Pool B: Subsidized Chinese Domestic APIs (DeepSeek/Qwen)
          └───► Pool C: Compromised/Shared API Keys
```

### The Reliability Problem ("Model Laundering")

You noted that they sometimes do not accurately show the real models. This is a common practice known as **Model Laundering** or **Faking Upstreams**.

Because high-end frontier models cost more to route, dishonest proxy operators will intercept your prompt to a high-end model and silently redirect it to a much cheaper, smaller model (or a heavily quantized local model) that has been system-prompted to pretend it is the requested model. If you are using these tokens to train an AI system, calculate embeddings, or generate high-fidelity synthetic datasets, **this will completely pollute your training data** without you realizing it.

## 3. Risks & Hidden Dimensions to Watch For

If you are looking at these channels strictly to save money on intensive token pipelines, you need to weigh the severe trade-offs against the cost savings:

- **Data Harvesting & Privacy Violations:** This is the most critical risk. These proxy operators do not just make money from selling you cheap tokens; they actively **log and package your prompt-response datasets**. Your training data, intellectual property, and proprietary system behavior are systematically sold to third parties or used to train domestic models.
    
- **High Latency and Request Dropping:** Because these pools rely on shared rate limits, your training scripts will frequently hit severe bottlenecks, sudden `429 Too Many Requests` errors, or arbitrary context window cutoffs when a specific account in the pool gets banned.
    
- **Security Risks in Open-Source Tooling:** The cybersecurity space has seen an influx of compromised npm and PyPI packages that silently install backdoors to turn standard Linux servers into unauthorized relay nodes for these Chinese proxy networks. If you deploy open-source proxy wrappers, audit them closely.
    

## 4. Legitimate, Safe Alternatives for Cheap Tokens

If your goal is purely to access massive volumes of compute/tokens cheaply without risking data poisoning or security issues, consider these legal and stable alternatives:

- **Native OpenRouter with Chinese Frontier Models:** Instead of using gray-market proxies for Western models, use a clean aggregator like OpenRouter to access official, native Chinese models like **DeepSeek-V3** or **MiMo-V2.5-Pro**. Because of the structural price cuts mentioned earlier, these models naturally cost a tiny fraction of Western equivalents (often under $0.50 per million tokens) while remaining entirely reliable, fully benchmarked, and safe from proxy tampering.
    
- **Local Infrastructure (Ollama / OpenClaw):** If you are running long-term background processing, agents, or pipeline training, look into self-hosting highly capable open-weights models (like Llama 3/4 or Qwen-2.5-72B) on local hardware or dedicated cloud instances (e.g., RunPod or Vast.ai). While there is an upfront hardware or rental cost, the marginal cost per token drops to exactly $0, with zero data privacy leakage.
    

Are you looking to use these cheap tokens primarily for generating synthetic training datasets, or are you running a high-volume multi-agent orchestration workflow?