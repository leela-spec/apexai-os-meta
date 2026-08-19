# Research prompt — local LLM context sizing and agentic browser-control feasibility

Copy everything below the line into Perplexity / ChatGPT / Gemini.

---

I am running a local LLM as a bounded "executor" agent that drives a real, signed-in Chrome tab through an agent framework. I need a reality check on context-window sizing, memory cost, and speed on my specific hardware, plus a check on whether one architectural assumption in my design is wrong.

Please be concrete and quantitative. Where you are uncertain or where the answer depends on backend/build specifics, say so explicitly rather than guessing. Cite sources for architecture numbers and any benchmark figures.

## My hardware

- Laptop: HP OmniBook X Flip 16-as0xxx
- CPU: Intel Core Ultra 7 258V ("Lunar Lake"), 8 cores (4+4), 2.20 GHz base / 4.8 GHz max, AVX2 + AVX-VNNI (no AVX-512)
- iGPU: Intel Arc 140V, 64 compute units (Xe2), max 1950 MHz, reported device memory 16.5 GB (shared, not dedicated)
- RAM: 31.63 GB LPDDR5/DDR5, 8533 MT/s, 8 channels (memory is shared between CPU and iGPU)
- OS: Windows 11 Pro
- Geekbench 6 CPU: 2759 single / 10942 multi
- Geekbench 6 OpenCL (GPU): 30999
- Geekbench 7 GPU (OpenCL): 21309
- No discrete GPU, no NVIDIA/CUDA

## My current software stack

- Model: **Qwen3-8B**, GGUF, **Q4_K_M** quantization
- Runtime: **llama.cpp** `llama-server.exe`, launched as:
  `llama-server.exe --model Qwen3-8B-Q4_K_M.gguf --host 127.0.0.1 --port 8090 --ctx-size 8192 --parallel 1 --gpu-layers 999 --jinja --reasoning-budget 128`
- All layers offloaded to the iGPU (`--gpu-layers 999`). I am not certain whether this build uses the SYCL, Vulkan, or OpenCL backend — please tell me how to determine this and which is currently fastest on Lunar Lake / Arc 140V.
- Agent framework: OpenClaw (Node-based). The model is exposed a `browser` tool and a `write` tool. The browser tool's JSON schema alone is ~3,600 characters (54 properties).
- Currently `--ctx-size 8192` and the agent's `contextTokens` is 8192. This was a conservative smoke-test default, not a considered choice.

## What the system actually has to do

The local model is **not** a planner or an author. A larger cloud model writes the prompts and evaluates the results. The local model's entire job is bounded execution:

1. Take a pre-written prompt (typically 300–2,000 words) from a file.
2. Drive a signed-in Chrome tab at Perplexity, ChatGPT, or Gemini: select an exact mode (e.g. Perplexity "Learn step by step"), select an exact web model (e.g. Claude Sonnet 5), select a reasoning mode, verifying each selection by re-reading the page.
3. Type the prompt into the composer, verify the inserted text matches, submit.
4. Wait for generation to finish (can be many minutes for Deep Research).
5. Capture the full response **verbatim** — these can be very long; the platform page-sharing cap is around 120,000 characters.
6. Write the captured text to a specified file path and report a receipt with byte/character counts.

Later I also want it to do small deterministic file edits and move larger blocks of text between files.

Every UI interaction step involves an accessibility-tree snapshot of the page being returned to the model so it can find and verify elements.

## The specific problem I hit

At `--ctx-size 8192`, the very first real attempt failed **before the model did anything**, with `context_overflow` at the precheck stage. The system prompt was 13,505 characters, plus the browser tool schema (~3,600 chars), plus skills text (~1,900 chars), plus the turn prompt. It never got to the browser task.

## The architectural question I think I may have gotten wrong

Currently, capturing the response works like this: the browser tool's `snapshot` action returns the page text **as a tool result into the model's context**, and then the model must re-emit those same characters as an argument to a `write` tool call to save them. So the model is acting as the data pipe for the payload — it has to "retype" everything it captures, autoregressively.

My instinct is that this is simply the wrong design: copy-paste should be a **mechanical** operation, not something that consumes context and generation time. I believe I should instead have my own orchestration layer (which already shells out to the framework's CLI for other things) perform the extraction and file write deterministically — the model just says "the response is complete, capture it", and gets back a byte count and hash for its receipt, never seeing the payload.

Please tell me whether that reasoning is correct, and what the standard/best-practice pattern is for this in agentic systems. Is there a well-known name for this pattern? Are there pitfalls (e.g. verification, provenance, the model needing to confirm the right content was captured)?

## Questions

1. **Is my architectural instinct correct** — that large payload transfer (page capture, file copy, big text moves) should bypass the model's context entirely via deterministic tool-side operations, rather than being routed through the model as tool-result-in / tool-argument-out? What are the standard patterns and their tradeoffs?

2. **If payload transfer is made deterministic**, what context window does the *remaining* work realistically need — multi-step UI navigation with repeated accessibility-tree snapshots, plus a 300–2,000 word prompt the model must emit into a composer? Give a realistic token budget breakdown per turn, and tell me whether 16K / 32K / 64K is the right target.

3. **Qwen3-8B specifics**: What is its native maximum context length, and at what point does it require RoPE scaling / YaRN? Does quality degrade materially at longer contexts for a Q4_K_M quant? Is Qwen3-8B a sensible choice for reliable, repetitive tool-calling and UI automation, or is there a materially better small open model for structured tool-use at this size in 2026?

4. **KV cache memory cost**: For Qwen3-8B (please confirm the architecture: layer count, number of KV heads, head dimension, GQA grouping), compute the KV cache size per token and the total at 8K / 16K / 32K / 64K / 128K, for fp16 KV and for q8_0 and q4_0 KV quantization. My own estimate is roughly 0.14 MiB/token at fp16, giving ~4.6 GiB at 32K and ~9.2 GiB at 64K — please verify or correct this.

5. **Will it fit on my hardware?** With ~5 GiB of Q4_K_M weights plus KV cache plus compute buffers, against an Arc 140V drawing from 31.63 GB of shared system memory (reported 16.5 GB device memory): what is the practical maximum context I can run fully GPU-offloaded? Are there Windows/Intel-specific allocation limits on shared-memory iGPUs I will hit before exhausting system RAM? Does going to 64K force me to KV-quantize, and what does `--cache-type-k` / `--cache-type-v` cost in quality?

6. **Speed — the thing I actually care about**: On an Arc 140V with an 8B Q4_K_M model, what prompt-processing (prefill) and token-generation throughput should I realistically expect? Specifically: if a turn carries a 15,000–25,000 token context, how long does prefill take, and how much does that grow at 32K vs 64K? Does llama.cpp prompt caching help across the many sequential tool-call round-trips within a single task (where the prefix is stable and only the tail grows)? What flags should I use to exploit that?

7. **Backend choice**: For Intel Lunar Lake / Arc 140V on Windows, which llama.cpp backend is currently fastest and most stable for this workload — SYCL, Vulkan, or OpenCL? Are there specific build flags or an alternative runtime (Intel IPEX-LLM, OpenVINO, etc.) that would materially outperform stock llama.cpp here? How do I check which backend my current build is using?

8. **Reality check on the whole approach**: Is an 8B Q4 model running on an integrated GPU a realistic choice for reliable, repeated, multi-step browser UI automation where correctness matters (selecting the right mode, verifying the right text was inserted before submitting)? Or is the practical failure mode going to be reasoning reliability rather than context or memory? If the latter, what would you change?

Please answer each numbered question directly, and flag clearly anywhere my premises are wrong.