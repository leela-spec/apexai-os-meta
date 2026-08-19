## Executive conclusion

Your core architecture is sound, and the repo handover already implements the same authority boundary: APEX/cloud reasoning owns planning, authoring, evaluation, routing, and scheduling; Qwen is a bounded executor operating validated requests and returning deterministic evidence.

For this machine and workload, my recommendation is:

|Decision|Recommendation|
|---|---|
|**Minimum context**|**32K remains the correct floor**|
|**Daytime profile**|**32K**, FP16 KV initially|
|**Browser-heavy / overnight profile**|**64K + q8_0 KV + YaRN factor 2**|
|**128K**|**Not warranted** for this executor|
|**Model**|**Keep Qwen3-8B Q4_K_M** for now|
|**Thinking**|**Turn it off** for this executor after acceptance testing|
|**Windows backend**|**Vulkan first**, A/B-test current SYCL|
|**OpenCL**|Do not use for this machine|
|**OpenVINO**|Worth a controlled benchmark, especially for prefill|
|**IPEX-LLM**|Do not build new production work on it; Intel archived it|
|**Large responses/transcripts**|Keep entirely outside model context|
|**Pre-written prompt bytes**|Ideally also transfer file→composer deterministically|
|**Most important reliability risk**|UI-state / accessibility-tree interpretation, not raw compute|

Your uploaded benchmarks confirm the essential hardware assumptions: Core Ultra 7 258V, 31.63 GB unified memory, Arc 140V, 64 compute units, 1950 MHz, and a reported 16.5 GB GPU memory window. The Geekbench 6 results are 2759/10942 CPU and 30999 OpenCL GPU. Your Geekbench 7 capture actually reports **21,327**, not 21,309, and the captured OS says Windows 11 Home rather than Pro; neither discrepancy changes the conclusions.

---

# 1. Deterministic payload transfer

**Yes. This is the right architecture.**

There isn't one universally agreed agent-specific name. The closest standard architectural terms are:

- **control-plane / data-plane separation**
    
- **out-of-band payload transfer**
    
- **pass-by-reference / artifact handles**
    
- and, when hashes identify the bytes, **content-addressed artifacts**
    

The LLM should operate on a small **control-plane envelope**:

```text
artifact_id
source
destination
byte_count
character_count
sha256
mime_type
capture_timestamp
execution_id
status
```

The orchestration/tool layer moves the actual bytes.

### Important limitation of hashes

A SHA-256 proves:

> "These are the same bytes."

It does **not** prove:

> "These were the correct bytes to capture."

So a robust receipt should bind the digest to provenance:

**Capture identity:** provider, URL/hostname, frozen tab/conversation identifier, response identifier if the provider exposes one.

**Capture conditions:** generation-complete state, exact response container, start/end boundaries, encoding/MIME type.

**Execution identity:** job ID, tool version/hash, timestamp, source path, destination path.

**Integrity:** source hash, stored-file hash, byte/character counts, atomic-write success.

**Independent verification:** another deterministic component should be able to recompute the digest and compare it to the receipt.

If somebody needs to determine whether the captured answer is _semantically the right answer_, that belongs to the cloud reasoning/evaluation model, not Qwen.

### One thing I would change in Workflow 1

You say the 300–2,000-word prompt is already authored, immutable, and stored in a file, yet Qwen has to receive it and emit it into the browser.

That is another payload transfer.

Your own architecture principle suggests:

```text
Qwen:
"Call insert_prompt_file(path=X, sha256=Y, target=composer-Z)."

Tool:
reads file bytes
inserts exact bytes
re-reads composer deterministically
compares bytes/hash
returns {characters, bytes, sha256, match:true}
```

Then Qwen never sees the prompt body either.

That simultaneously:

1. saves perhaps 400–3,000 context tokens;
    
2. eliminates transcription/copy errors;
    
3. makes "prompt exactly as authored" cryptographically testable;
    
4. makes a smaller context substantially safer.
    

I would strongly prefer this over having an 8B model reproduce immutable text.

---

# 2. Context sizing: 32K vs 64K vs 128K

The 8K failure is unsurprising.

OpenClaw explicitly counts system prompts, conversation history, tool calls/results, tool JSON schemas and provider wrappers. Its own diagnostic examples approximate text at roughly four characters per token. ([docs.openclaw.ai](https://docs.openclaw.ai/concepts/context "Context - OpenClaw"))

Your known fixed material alone is:

|Component|Characters|Approx tokens|
|---|--:|--:|
|System prompt|13,505|~3,375|
|Browser schema|3,600|~900|
|Skills text|1,900|~475|
|**Known subtotal**|**19,005**|**~4,750**|

And that excludes other schemas, OpenClaw framing, provider/chat-template wrappers and the actual user turn. The repo confirms the executor is still configured at 8,192 tokens today.

### Realistic browser-turn budget

I would plan roughly:

|Contributor|Typical|Heavy|
|---|--:|--:|
|Fixed OpenClaw/system/tool bootstrap|6–8K|8–10K|
|Immutable prompt, **if Qwen sees it**|0.4–3K|~3K|
|Current accessibility snapshot|1–3K|~4K|
|Recent snapshot/tool-result history|2–5K|6–10K|
|Tool calls + short receipts/status|0.5–1.5K|2K|
|Recent assistant messages|0.5–1K|2K|
|**Working total**|**10–20K**|**25–31K**|

Those snapshot values are workload estimates, not a documented constant. OpenClaw confirms that tool outputs and schemas accumulate in context and provides pruning specifically because tool output can become the dominant source of context growth. ([OpenClaw](https://docs.openclaw.ai/concepts/context "Context - OpenClaw"))

### Verdict

**32K:** sufficient, but under your _current_ browser workflow I would call it **adequate rather than luxurious**. A badly scoped page plus several retained accessibility snapshots can push it uncomfortably close to the ceiling.

**64K:** genuinely useful for the browser executor. It is not needed because Qwen must understand 64K of meaningful prose; it is useful as **operational slack** against UI/tool-result variability. This is the size I would choose for the unattended/high-headroom profile.

**128K:** no. Once page/document payloads are out-of-band, I see no credible reason for this executor to carry 128K. It costs memory, YaRN extrapolation and increasingly expensive attention without giving your bounded state machine much benefit.

### Cron/media workflow

Workflow 2 itself has very modest context requirements. Paths, hashes, exit codes, byte counts and state enums are tiny. If transcripts and cloud-model outputs remain out-of-band, **Workflow 2 is not a reason to exceed 32K at all**.

### OpenClaw-specific trap

OpenClaw compaction is summarization-based; session pruning merely removes/shortens old tool results. ([OpenClaw](https://docs.openclaw.ai/concepts/session-pruning "Session pruning - OpenClaw"))

That matters because **local-Qwen-authored compaction would violate your architecture rule**. OpenClaw can assign compaction to another model, but its documented fallback can still involve model summarization. ([OpenClaw](https://docs.openclaw.ai/compaction?utm_source=chatgpt.com "Compaction - OpenClaw"))

For this executor I prefer:

**bounded execution session → deterministic tool-result pruning → finish → new execution session**

rather than relying on Qwen to summarize its own old context.

---

# 3. Qwen3-8B specifics

Qwen's official figures are:

- **8.2B parameters**
    
- **36 layers**
    
- **32 query heads**
    
- **8 KV heads**
    
- **128 head dimension**
    
- **32,768-token native context**
    
- validated to **131,072 using YaRN**. ([Hugging Face](https://huggingface.co/Qwen/Qwen3-8B "Qwen/Qwen3-8B · Hugging Face"))
    

There is a confusing `max_position_embeddings = 40960` in the model config. That does **not** mean its native trained context is 40,960. Qwen explicitly says native context is 32,768 and explains the 40,960 setting as an allocation convention involving 32K output plus an 8K typical prompt. ([Hugging Face](https://huggingface.co/Qwen/Qwen3-8B "Qwen/Qwen3-8B · Hugging Face"))

### 64K

Use YaRN factor **2**.

Qwen specifically recommends factor 2 when a workload typically reaches ~65,536 tokens. For llama.cpp, their documented syntax is effectively:

```powershell
--ctx-size 65536 `
--rope-scaling yarn `
--rope-scale 2 `
--yarn-orig-ctx 32768
```

Qwen's 128K example uses factor 4. ([Hugging Face](https://huggingface.co/Qwen/Qwen3-8B "Qwen/Qwen3-8B · Hugging Face"))

### Does long context reduce quality?

Somewhat, potentially.

Qwen warns that the commonly implemented form is **static YaRN**, so enabling it can degrade performance at short contexts. It explicitly recommends **not enabling YaRN when average context remains ≤32,768**. ([Hugging Face](https://huggingface.co/Qwen/Qwen3-8B "Qwen/Qwen3-8B · Hugging Face"))

That argues strongly for your two-profile idea:

- **32K daytime:** native RoPE, no YaRN.
    
- **64K high-headroom:** YaRN ×2.
    

### Does Q4_K_M specifically make long context bad?

I found no primary evidence that Q4_K_M introduces a special long-context cliff unique to Qwen3-8B. Quantization adds its normal approximation error; YaRN/extrapolation is the more important context-length change.

### Is Qwen3-8B sensible for this job in 2026?

**Yes. I would not replace it yet.**

Qwen explicitly supports external-tool integration in both thinking and non-thinking modes. ([Hugging Face](https://huggingface.co/Qwen/Qwen3-8B "Qwen/Qwen3-8B · Hugging Face"))

Qwen3.5-9B is newer, but I would **not automatically migrate this executor to it**. There have been multiple 2026 llama.cpp reports involving Qwen3.5 tool calls getting emitted inside reasoning/XML instead of parsed tool calls, plus cache-reuse/reprocessing issues. One report specifically says disabling thinking made repeated tool calls work correctly. ([GitHub](https://github.com/ggml-org/llama.cpp/issues/20837?utm_source=chatgpt.com "Eval bug: Qwen3.5 9B often prints tool calls in XML and stops when thinking is enabled - tool calls inside thinking block · Issue #20837 · ggml-org/llama.cpp · GitHub"))

For a mechanical executor, boring reliability is more valuable than newer benchmark capability.

So:

**Qwen3-8B stays incumbent until another model beats it on your actual executor acceptance suite.**

---

# 4. KV-cache memory

Your estimate was basically correct.

Architecture:

[  
36\ layers \times 8\ KVheads \times 128\ dimensions  
]

For both K and V:

[  
36 \times 8 \times 128 \times 2  
=73,728\ scalar\ values/token  
]

With FP16 at 2 bytes:

[  
147,456\ bytes/token  
=0.140625\ MiB/token  
]

The architecture values are from Qwen's official model card/config. ([Hugging Face](https://huggingface.co/Qwen/Qwen3-8B "Qwen/Qwen3-8B · Hugging Face"))

llama.cpp supports FP16, q8_0, q4_0 and other KV types through `--cache-type-k` and `--cache-type-v`. ([GitHub](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md "llama.cpp/tools/server/README.md at master · ggml-org/llama.cpp · GitHub"))

### Exact theoretical KV size

These figures exclude small alignment/allocator/runtime overhead.

|Context|FP16|q8_0|q4_0|
|--:|--:|--:|--:|
|**8K**|**1.125 GiB**|**0.598 GiB**|**0.316 GiB**|
|**16K**|**2.250 GiB**|**1.195 GiB**|**0.633 GiB**|
|**32K**|**4.500 GiB**|**2.391 GiB**|**1.266 GiB**|
|**64K**|**9.000 GiB**|**4.781 GiB**|**2.531 GiB**|
|**128K**|**18.000 GiB**|**9.563 GiB**|**5.063 GiB**|

So your approximately 4.6/9.2 GiB numbers were only slightly high.

The official Q4_K_M GGUF is **5.03 GB on disk**, or about 4.68 GiB. ([Hugging Face](https://huggingface.co/Qwen/Qwen3-8B-GGUF/tree/main?utm_source=chatgpt.com "Qwen/Qwen3-8B-GGUF at main"))

Thus the rough **weights + KV alone** picture is:

|Profile|Weights|KV|Subtotal before compute/driver|
|---|--:|--:|--:|
|32K FP16|~4.68 GiB|4.50|**~9.18 GiB**|
|32K q8|~4.68|2.39|**~7.07 GiB**|
|64K FP16|~4.68|9.00|**~13.68 GiB**|
|64K q8|~4.68|4.78|**~9.46 GiB**|
|128K FP16|~4.68|18.00|**~22.68 GiB**|
|128K q8|~4.68|9.56|**~14.24 GiB**|

Those subtotals are why **64K/q8 is attractive** on this machine.

---

# 5. Hardware fit

Your Arc reports a 16.5 GB GPU-memory window while sharing the same physical 31.63 GB system memory pool.

Intel now exposes a **Shared GPU Memory Override** for Core Ultra Series 2 iGPUs on sufficiently recent Intel Graphics Software/drivers. Intel says the default is 57% of RAM, the maximum depends on installed system memory, unused GPU allowance remains usable by the system, and changing it requires a reboot. ([Intel](https://www.intel.com/content/www/us/en/support/articles/000101789/graphics.html "Shared GPU Memory Override Feature and Requirements"))

### Practical context limits

**32K FP16:** comfortably plausible fully offloaded. Around 9.2 GiB for weights+KV leaves several GiB for compute buffers, backend allocations, display, driver, etc.

**64K FP16:** theoretically fits inside 16.5 GB, but I would **not call it operationally safe**. At ~13.7 GiB before compute buffers you're entering the area where backend-specific allocation behavior matters.

There are actual Arc 140V/258V llama.cpp OOM reports with both Vulkan and SYCL despite UMA, so “system RAM exists” is not the same as “every GPU allocation will succeed.” ([GitHub](https://github.com/ggml-org/llama.cpp/issues/18946?utm_source=chatgpt.com "Misc. bug: \"ErrorOutOfDeviceMemory\" - Critical Out of Device Memory Errors and Memory Accounting Failures in llama.cpp (Vulkan Backend and SYCL Backend) with Intel 258v APU Processor. · Issue #18946 · ggml-org/llama.cpp · GitHub"))

**64K q8:** ~9.5 GiB before buffers. Much healthier.

So:

> **64K does not mathematically force KV quantization, but on your current 16.5-GB GPU window I would use q8_0 KV for production reliability.**

**128K:** unattractive. FP16 KV alone is 18 GiB. q8 gives ~14.2 GiB weights+KV before buffers. q4 makes it memory-feasible but trades away reliability for a context length your executor does not need.

### q8_0 vs q4_0 quality

Use **q8_0 first**.

I would not promise “zero quality loss”: llama.cpp has had backend/model-specific KV-quant regressions. Therefore KV quantization belongs in your executor acceptance matrix, especially for exact tool calling.

For your use case:

1. FP16 baseline.
    
2. q8_0 K + q8_0 V.
    
3. compare hundreds of fixed tool-call trajectories.
    
4. only consider q4 if memory actually demands it.
    

---

# 6. Throughput

There is no good controlled primary benchmark I found for the **exact combination**:

> Qwen3-8B Q4_K_M + Arc 140V + Windows + your current llama.cpp build.

So the following must be treated as **planning estimates**, not measured results.

We do have extremely relevant upstream llama.cpp submissions from the exact Core Ultra 7 258V/Arc 140V class.

On native Windows Vulkan, a 6.74B Llama-2 Q4_0 benchmark reported:

- **~572–574 tok/s pp512**
    
- **~23–24 tok/s generation**. ([GitHub](https://github.com/ggml-org/llama.cpp/discussions/10879 "Performance of llama.cpp with Vulkan · ggml-org llama.cpp · Discussion #10879 · GitHub"))
    

On the same processor under Linux SYCL, another run reported:

- **535.6 tok/s pp512**
    
- **24.6 tok/s generation** without FA. ([GitHub](https://github.com/ggml-org/llama.cpp/discussions/23313?utm_source=chatgpt.com "Performance of llama.cpp on Intel GPU with SYCL backend · ggml-org llama.cpp · Discussion #23313 · GitHub"))
    

Qwen3-8B is larger and its Q4_K_M file is ~5.03 GB rather than the benchmark model's 3.56 GiB, so I would budget roughly:

**Generation:** **~18–22 tok/s**

**Short/medium prefill:** **~400–500 tok/s**

Again, those are extrapolations from same-chip llama.cpp data, not a Qwen3 benchmark.

### Long cold prefill

`pp512` does not capture the increasing attention work of a 15K–64K prompt.

My operational planning ranges would therefore be:

|Cold input|Planning range|
|--:|--:|
|**15K tokens**|~45–90 sec|
|**25K**|~75–150 sec|
|**32K**|~1.5–3 min|
|**64K**|~3–6+ min|

Actual measurement could land outside those ranges depending heavily on backend, Flash Attention, KV type, batch/ubatch and current driver/build.

### But your actual agent loop should be much faster

`llama-server` has prompt caching **enabled by default**. If request B shares request A's prefix, it can reuse the existing KV and process only the changed suffix. ([GitHub](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md "llama.cpp/tools/server/README.md at master · ggml-org/llama.cpp · GitHub"))

That matches your workload extremely well:

```text
stable system prompt
stable tool schemas
stable prior conversation
+ one new accessibility snapshot
+ one new tool result
```

So after the first turn, you should **not** continually pay a 20K-token full prefill.

Keep:

```text
--parallel 1
--cache-prompt
```

`--cache-prompt` is already the default, but stating it explicitly documents intent.

I would initially leave:

```text
--cache-reuse 0
```

because ordinary common-prefix caching already solves your primary case. `--cache-reuse` adds chunk/KV-shift reuse and is a separate mechanism. ([GitHub](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md "llama.cpp/tools/server/README.md at master · ggml-org/llama.cpp · GitHub"))

Also keep the prefix byte-stable: don't inject changing timestamps/job IDs near the beginning of the prompt if they can instead live toward the tail.

---

# 7. Backend choice

## My ordering for this machine

### **1. Vulkan — current default recommendation**

For Windows specifically, the strongest directly relevant upstream measurement I found is Arc 140V native Windows Vulkan at ~574 pp512 / 24 tg128. The startup log also makes backend detection very obvious:

```text
ggml_vulkan: ... Arc 140V ...
load_backend: loaded Vulkan backend ... ggml-vulkan.dll
```

([GitHub](https://github.com/ggml-org/llama.cpp/discussions/10879 "Performance of llama.cpp with Vulkan · ggml-org llama.cpp · Discussion #10879 · GitHub"))

Vulkan is also simpler operationally than installing Intel's complete oneAPI/SYCL environment.

### **2. SYCL — definitely worth a controlled A/B**

llama.cpp's SYCL backend is explicitly designed for Intel GPUs and officially lists integrated Arc GPUs in **Lunar Lake** as supported. ([GitHub](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/SYCL.md?utm_source=chatgpt.com "llama.cpp/docs/backend/SYCL.md at master · ggml-org/llama.cpp · GitHub"))

Same-chip SYCL generation has reached ~25 t/s in upstream testing. ([GitHub](https://github.com/ggml-org/llama.cpp/discussions/23313?utm_source=chatgpt.com "Performance of llama.cpp on Intel GPU with SYCL backend · ggml-org llama.cpp · Discussion #23313 · GitHub"))

So I would benchmark rather than philosophize:

```powershell
llama-bench.exe -m Qwen3-8B-Q4_K_M.gguf -ngl 999
```

on a current Vulkan build and current SYCL build, same driver, same power mode.

Whichever wins your **Qwen3 tool-use acceptance + long-context test** becomes production.

### **3. OpenVINO — interesting experiment**

On the same Core Ultra 7 258V submission, llama.cpp OpenVINO delivered **1306 pp512**, versus ~529 Vulkan, although token generation was lower at **18.1 t/s**. ([GitHub](https://github.com/ggml-org/llama.cpp/discussions/10879 "Performance of llama.cpp with Vulkan · ggml-org llama.cpp · Discussion #10879 · GitHub"))

That is highly interesting for _your_ workload because browser agents are often **prefill-heavy and output-light**.

But llama.cpp itself still labels OpenVINO's performance, memory optimization, accuracy validation, quantization and broader model coverage as work in progress. Q4_K_M is supported and Lunar Lake is specifically being validated. ([GitHub](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/OPENVINO.md "llama.cpp/docs/backend/OPENVINO.md at master · ggml-org/llama.cpp · GitHub"))

So OpenVINO deserves an **experiment**, not an architecture migration yet.

### **OpenCL — no**

llama.cpp says its OpenCL backend was designed first for Qualcomm Adreno; Intel GPUs without SYCL can run it, but performance is **not optimal**. ([GitHub](https://github.com/ggml-org/llama.cpp/blob/master/docs/backend/OPENCL.md?utm_source=chatgpt.com "llama.cpp/docs/backend/OPENCL.md at master · ggml-org/llama.cpp · GitHub"))

You have SYCL and Vulkan. Don't use OpenCL for Qwen.

### **IPEX-LLM — no new investment**

Intel archived IPEX-LLM on **January 28, 2026**, says no further development/support is guaranteed, and explicitly notes known security issues. ([GitHub](https://github.com/intel/ipex-llm "GitHub - intel/ipex-llm: Accelerate local LLM inference and finetuning (LLaMA, Mistral, ChatGLM, Qwen, DeepSeek, Mixtral, Gemma, Phi, MiniCPM, Qwen-VL, MiniCPM-V, etc.) on Intel XPU (e.g., local PC with iGPU and NPU, discrete GPU such as Arc, Flex and Max); seamlessly integrate with llama.cpp, Ollama, HuggingFace, LangChain, LlamaIndex, vLLM, DeepSpeed, Axolotl, etc. · GitHub"))

That removes it from my production shortlist.

## How to identify your current backend

The easiest test is simply restart `llama-server` and inspect the first startup lines.

**Vulkan:**

```text
ggml_vulkan:
loaded Vulkan backend
ggml-vulkan.dll
```

**SYCL:**

expect SYCL/Level-Zero device initialization and an Intel Arc device.

You can also run:

```powershell
.\llama-server.exe --list-devices
```

Current llama.cpp exposes `--list-devices` specifically for this. ([GitHub](https://github.com/ggml-org/llama.cpp/issues/18063?utm_source=chatgpt.com "Misc. bug: llama-server fail with 'Failed to read connection' when 'stream: false' · Issue #18063 · ggml-org/llama.cpp · GitHub"))

And the downloaded binary filename is a clue: Qwen's docs note that Windows llama.cpp release packages are backend-specific. ([Qwen](https://qwen.readthedocs.io/en/latest/run_locally/llama.cpp.html "llama.cpp - Qwen"))

---

# 8. Reliability reality check

**Yes: an 8B Q4 model on this iGPU is realistic for the bounded job you describe.**

But one premise needs semantic precision.

If Qwen reads an accessibility tree and chooses which control corresponds to “Claude Sonnet 5,” it is still doing **model inference over semantics**. It isn't a literal deterministic automaton.

The architecture becomes safe because Qwen does **not own the decision authority**:

```text
Cloud/validated request:
expected setting = Claude Sonnet 5

Qwen:
identify candidate UI control

deterministic guard:
only allowed tab/tool/action

Qwen clicks

tool/Qwen:
re-read UI state

guard:
expected state must equal declared state
else STOP
```

That is entirely consistent with your design.

### Risk ranking

I would rank failures roughly:

**1. UI-state ambiguity / provider UI changes — highest.** Labels move, controls hide, popovers change, accessibility trees change.

**2. Stale observations.** Qwen uses a node/reference from a snapshot taken before an async UI transition.

**3. Tool-call format/schema errors.** Especially multi-turn arguments and reference IDs.

**4. False verification.** The model thinks a selection succeeded because a nearby label matches.

**5. Context accumulation.** Repeated snapshots grow until precheck/compaction problems appear.

**6. Backend/quantization regressions.** Particularly after llama.cpp or graphics-driver upgrades.

**7. Raw model intelligence — lower than the above**, because the task has been deliberately constrained.

The correct reliability mechanism is therefore **not a smarter local model**. It is the state-machine/guard architecture you are already building:

- closed-world requests;
    
- allowlisted actions;
    
- exact expected values;
    
- re-snapshot after every consequential mutation;
    
- bounded retries;
    
- fail closed on ambiguity;
    
- idempotent deterministic wrappers;
    
- frozen tab/provider identity;
    
- receipts;
    
- no autonomous recovery invention.
    

That matches the current repo design closely.

### One runtime flag I would change

Your current command has:

```text
--reasoning-budget 128
```

Current llama.cpp has an explicit:

```text
--reasoning off
```

and a reasoning budget of `0` means immediate end. ([GitHub](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md "llama.cpp/tools/server/README.md at master · ggml-org/llama.cpp · GitHub"))

Given your architecture, I would acceptance-test:

```powershell
--reasoning off
```

If your Qwen/OpenClaw tool parser behaves correctly, that is semantically cleaner than allocating 128 reasoning tokens to an agent prohibited from reasoning.

---

# 9. Day/night profiles

## 9a. Laptop impact

### Idle laptop, plugged in

This is a good overnight workload.

The weights remain resident, but when there is no inference the server does little GPU computation. During a job, inference will heavily use the iGPU and shared memory subsystem, after which load falls again.

### Laptop actively used

The important contention is **unified memory bandwidth**.

The CPU, iGPU, browser, display compositor and Qwen are all using the same physical memory subsystem. So active Qwen inference can noticeably affect:

- Chrome/UI smoothness;
    
- video/GPU applications;
    
- anything bandwidth-intensive;
    
- thermal headroom;
    
- battery drain.
    

That is another reason I prefer **32K day / 64K night** rather than simply leaving 64K FP16 resident everywhere.

And I would not schedule long unattended inference on battery.

## 9b. Practical Windows arrangement

I would use **one server, two launch profiles**, not two simultaneously running llama servers.

Two concurrent servers would duplicate model/cache allocations from the same unified-memory pool.

### Day

Conceptually:

```powershell
llama-server.exe `
  --model Qwen3-8B-Q4_K_M.gguf `
  --host 127.0.0.1 `
  --port 8090 `
  --ctx-size 32768 `
  --parallel 1 `
  --gpu-layers 999 `
  --jinja `
  --reasoning off
```

Start with FP16 KV.

### Night

```powershell
llama-server.exe `
  --model Qwen3-8B-Q4_K_M.gguf `
  --host 127.0.0.1 `
  --port 8090 `
  --ctx-size 65536 `
  --parallel 1 `
  --gpu-layers 999 `
  --jinja `
  --reasoning off `
  --rope-scaling yarn `
  --rope-scale 2 `
  --yarn-orig-ctx 32768 `
  --cache-type-k q8_0 `
  --cache-type-v q8_0
```

The YaRN flags are supported by current llama.cpp and the factor-2 choice follows Qwen's recommendation for a typical 65,536-token application. ([GitHub](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md "llama.cpp/tools/server/README.md at master · ggml-org/llama.cpp · GitHub"))

### Scheduling pattern

Windows Task Scheduler is perfectly reasonable:

```text
Evening task
  stop day llama-server
  wait for :8090 to close
  start night profile
  health-check :8090

Morning task
  stop night server
  wait for :8090 to close
  start day profile
  health-check :8090
```

Keep **the same host/port/model alias** so OpenClaw does not care which resource profile is active.

OpenClaw Cron itself is also more capable than your premise suggests: its current documentation supports deterministic command/script cron payloads **without starting a model-backed turn at all**. ([OpenClaw](https://docs.openclaw.ai/automation/cron-jobs?utm_source=chatgpt.com "Scheduled tasks - OpenClaw"))

That means Workflow 2 can be made even stronger:

```text
Cron
 ↓
deterministic website checker/downloader
 ↓
deterministic Whisper invocation
 ↓
cloud-model handoff
 ↓
deterministic validator
```

Qwen may not need to participate in several of those steps **at all**.

That is preferable wherever the step really is just “run this exact command and check its typed result.”

---

# Final architecture recommendation

I would lock the near-term design this way:

```text
                         CLOUD REASONING
             plan / author / judge / validate semantics
                              │
                              ▼
                    frozen execution request
                              │
                     paths + hashes + enums
                              │
                              ▼
                ┌─────────────────────────┐
                │ Qwen3-8B Q4_K_M         │
                │ bounded UI executor     │
                │ no thinking / planning  │
                └─────────────────────────┘
                    │                  │
           small observations      declared calls
                    │                  │
                    ▼                  ▼
              accessibility       deterministic tools
              state only          / data plane
                                       │
               ┌───────────────────────┼─────────────────┐
               ▼                       ▼                 ▼
        prompt file→UI         response→artifact   transcript→cloud
        hash verified          hash verified       by reference
```

And specifically:

**32K native Qwen context** is the production floor and the right daytime setting.

**64K + YaRN ×2 + q8 KV** is justified as the high-headroom/browser-heavy profile on this hardware.

**128K is not justified.**

**Vulkan is the first Windows backend I would run**, with SYCL immediately A/B-tested and OpenVINO tested experimentally for its potentially much faster prefill.

**Qwen3-8B should remain the incumbent** until a challenger wins a fixed acceptance suite measuring exact multi-step tool-call success, not generic reasoning benchmarks.

Most importantly, I would extend your out-of-band rule one step further and **stop making Qwen copy immutable 300–2,000-word prompts at all**. Once that is deterministic too, the executor becomes smaller, faster and materially easier to prove correct.