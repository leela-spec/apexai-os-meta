### 1. Deterministic Payload Transfer Pattern

Passing data payloads directly through references while excluding the raw payload from the LLM's context window is known as the **Claim Check Pattern** (or _Reference-Based Messaging_ / _Pass-by-Reference_).

  

```
┌─────────────────┐       1. Save Large Payload       ┌────────────────────────┐
│  Orchestration  │──────────────────────────────────►│  Local Storage / DB    │
│  / Tool Layer   │◄──────────────────────────────────│ (Disk, File, Temp-Dir) │
└────────┬────────┘    2. Return Hash & Byte Count    └────────────────────────┘
         │
         │ 3. Send Claim Check (Receipt)
         ▼
┌─────────────────┐
│ Local Model Context
│ (Receipt Only: File Path, Byte Count, SHA-256 Hash)
└─────────────────┘
```

#### Pitfalls & Mitigations in Agentic Pipelines

- **Identity Verification without Inspection**: The model cannot read the payload to verify correctness. Your tool response must supply deterministic verification metadata: byte count, SHA-256 checksum, page status code, and target CSS selectors matched.
    
      
    
- **Payload Truncation Silent Failures**: A web scraper might capture an "Access Denied" page (500 bytes) instead of a 100,000-character research response. Mitigation: Implement tool-side validation rules (e.g., minimum expected byte length thresholds or required DOM elements) before returning a "success" receipt to the model.
    
      
    
- **Provenance & Auditing**: If downstream cloud models consume the raw payload directly from storage, tag every payload file with a session ID, step index, and cryptographic hash to maintain a strict chain of custody across handoffs.
    
      
    

### 2. Context Window Sizing Budget

With large payloads handled out-of-band via claim checks, the remaining token budget is consumed strictly by system instructions, tool schemas, DOM accessibility trees, and turn receipts.

  

#### Per-Turn Token Breakdown (Executor Role)

|**Component**|**Estimate (Tokens)**|**Notes**|
|---|---|---|
|**System Prompt & Role Directives**|2,500 – 3,500|OpenClaw scaffolding, safety rules, strict execution constraints.|
|**Tool Schemas**|1,000 – 1,500|`browser` schema (~3,600 chars) + `write`/cron tool definitions.|
|**Skill Instructions**|500 – 800|Hardcoded execution runbooks.|
|**Target Task / Prompt Input**|400 – 2,600|300–2,000 words emitted to the composer.|
|**DOM Accessibility Tree Snapshot**|1,500 – 4,000|Compact UI element map returned per navigation step.|
|**Execution History (Tail)**|3,000 – 8,000|3–5 recent tool-call turns and receipts.|
|**Safety Margin / Output Reserve**|2,000|Space for next tool generation + unexpected DOM spikes.|
|**Total Operational Target**|**10,900 – 20,400**|**Sweet spot: 32K context window (32,768 tokens)**|

#### Why `--ctx-size 8192` Failed

Your prompt setup had a static footprint of ~13,500 characters (system) + ~3,600 characters (browser schema) + ~1,900 characters (skills) + task prompt = ~20,000 characters (~5,200 tokens). Adding a single accessibility tree snapshot (~2,500 tokens) pushed total input to **~7,700 tokens**, leaving virtually zero headroom for token output generation or multi-turn execution history, causing immediate `context_overflow`.

  

- **Recommendation**: Set `--ctx-size 32768`. An 8K context is too small for modern agentic tool schemas, while 64K adds unnecessary KV cache memory overhead without providing additional functional utility for single-turn execution.
    
      
    

### 3. Qwen3-8B Architecture & Tool-Calling Performance

#### Architecture Specifications

- **Base Architecture**: Dense causal decoder-only Transformer.
    
      
    
- **Parameters**: 8.2B total (6.95B non-embedding).
    
      
    
- **Layers ($N_{\text{layers}}$)**: 36.
    
      
    
- **Hidden Size**: 4096.
    
      
    
- **Query Attention Heads ($N_{\text{q\_heads}}$)**: 32.
    
      
    
- **Key/Value Heads ($N_{\text{kv\_heads}}$)**: 8 (Grouped-Query Attention with 4:1 ratio).
    
      
    
- **Head Dimension ($d_{\text{head}}$)**: 128.
    
      
    
- **Native Context**: 32,768 tokens natively. Context lengths up to 131,072 use YaRN RoPE scaling.
    
      
    

#### Quality Degradation & Model Assessment

- **RoPE / YaRN Threshold**: Within its native 32K context, no RoPE scaling factors are required.
    
      
    
- **Quantization Impact**: For `Q4_K_M`, quality remains stable up to 32K. At 64K+, precision loss in 4-bit weights combined with RoPE phase compression leads to degraded attention accuracy on long structured inputs.
    
      
    
- **Executor Suitability**: Qwen3-8B and Qwen2.5-7B/8B excel at structured JSON function calling and mechanical execution. They adhere closely to JSON schemas under constrained context conditions, outperforming similarly sized open models on function-calling reliability.
    
      
    

### 4. Key-Value (KV) Cache Memory Calculations

For a model using Grouped-Query Attention (GQA), the KV cache size per token across all layers is calculated as:

  

$$\text{Elements per token} = 2 \times N_{\text{layers}} \times N_{\text{kv\_heads}} \times d_{\text{head}}$$

$$\text{Elements per token} = 2 \times 36 \times 8 \times 128 = 73,728 \text{ elements/token}$$

#### Precision Specifications

1. **FP16 (2 bytes/element)**: $73,728 \times 2 = 147,456 \text{ bytes/token} \approx 0.140625 \text{ MiB/token}$ ($144 \text{ KiB/token}$).
    
      
    
2. **`q8_0` Quantized KV (~1.0625 bytes/element)**: $73,728 \times 1.0625 = 78,336 \text{ bytes/token} \approx 0.0747 \text{ MiB/token}$ ($76.5 \text{ KiB/token}$).
    
      
    
3. **`q4_0` Quantized KV (~0.5625 bytes/element)**: $73,728 \times 0.5625 = 41,472 \text{ bytes/token} \approx 0.0395 \text{ MiB/token}$ ($40.5 \text{ KiB/token}$).
    
      
    

#### KV Cache Memory Requirements (GiB)

|**Context Size**|**FP16 KV Cache**|**q8_0 KV Cache**|**q4_0 KV Cache**|
|---|---|---|---|
|**8,192 (8K)**|1.13 GiB (1.21 GB)|0.60 GiB (0.64 GB)|0.31 GiB (0.34 GB)|
|**16,384 (16K)**|2.25 GiB (2.42 GB)|1.19 GiB (1.28 GB)|0.63 GiB (0.68 GB)|
|**32,768 (32K)**|**4.50 GiB (4.83 GB)**|2.39 GiB (2.57 GB)|1.26 GiB (1.35 GB)|
|**65,536 (64K)**|9.00 GiB (9.66 GB)|**4.78 GiB (5.13 GB)**|2.53 GiB (2.72 GB)|
|**131,072 (128K)**|18.00 GiB (19.33 GB)|9.56 GiB (10.26 GB)|5.06 GiB (5.43 GB)|

Your calculation of ~0.14 MiB/token is accurate.

  

### 5. Hardware Fit on Intel Arc 140V (Lunar Lake)

#### Memory Availability

- **System RAM**: 31.63 GB total LPDDR5X (8533 MT/s).
    
      
    
- **WDDM Shared Memory Allocation Cap**: Under Windows 11, the WDDM driver caps integrated GPU device allocations at **~50% of total physical RAM** by default (~15.8 – 16.5 GB).
    
      
    
- **Model Weight Footprint (`Q4_K_M`)**: ~5.10 GB (~4.75 GiB).
    
      
    
- **llama.cpp Context & Compute Overhead**: ~1.00 GiB.
    
      
    
- **Net Available iGPU VRAM for KV Cache**: $\approx 16.5\text{ GB} - 5.1\text{ GB} - 1.0\text{ GB} = \mathbf{10.4\text{ GB}}\ (\approx 9.7\text{ GiB})$.
    
      
    

```
Total iGPU VRAM Limit (WDDM Shared Cap): ~16.5 GB
┌─────────────────────────┬──────────────────┬─────────────────────────────┐
│  Model Weights (Q4_K_M) │ Compute Overhead │ Free Space for KV Cache     │
│  ~5.1 GB                │ ~1.0 GB          │ ~10.4 GB (~9.7 GiB)         │
└─────────────────────────┴──────────────────┴─────────────────────────────┘
                                             ▲
                                             │
                       32K Context FP16 KV Cache (~4.8 GB): Fits comfortably
                       64K Context FP16 KV Cache (~9.7 GB): Borderline / Unstable
                       64K Context q8_0 KV Cache (~5.1 GB): Fits comfortably
```

#### Context Fit & Limits

- **32K Context at FP16**: Total VRAM required = $5.1 + 1.0 + 4.8 = \mathbf{10.9\text{ GB}}$, which fits within the 16.5 GB iGPU limit.
    
      
    
- **64K Context at FP16**: Total VRAM required = $5.1 + 1.0 + 9.7 = \mathbf{15.8\text{ GB}}$. This sits right at the WDDM allocation limit, risking driver instability or `ErrorOutOfDeviceMemory` allocation crashes under Windows.
    
      
    
- **64K Context with Quantized Cache (`q8_0`)**: Total VRAM required = $5.1 + 1.0 + 5.13 = \mathbf{11.23\text{ GB}}$, which runs safely within iGPU limits.
    
      
    

#### Quality Impact of KV Quantization

- **`q8_0` KV Cache (`--cache-type-k q8_0 --cache-type-v q8_0`)**: Negligible quality drop (<1%). Recommended for 32K/64K workloads.
    
      
    
- **`q4_0` KV Cache**: Can cause key attention accuracy drops and intermittent schema syntax errors in long contexts. If memory constraints require lower quantization, use `q8_0` for keys and `q4_0` for values (`-ctk q8_0 -ctv q4_0`).
    
      
    

### 6. Throughput & Prompt Caching

#### Performance Characteristics (Arc 140V Xe2 GPU)

- **Memory Bandwidth**: ~136 GB/s peak (LPDDR5X 8533 MT/s over 128-bit bus).
    
      
    
- **Generation Speed (Decoding)**: Bandwidth-bound. Theoretical maximum = $136\text{ GB/s} / 5.1\text{ GB weights} \approx 26.6\text{ tokens/sec}$. Expect **20 – 24 tokens/sec** in practice.
    
      
    
- **Prefill Speed (Prompt Processing)**: Compute and bandwidth-bound. Achieves **280 – 420 tokens/sec** on SYCL matrix extensions.
    
      
    

#### Prefill Scaling & Caching Impact

|**Scenario / Context Size**|**Prefill Processing Time (No Cache)**|**Effective Prefill Time (With Prompt Cache)**|
|---|---|---|
|**15,000 Tokens**|~38 – 53 seconds|**2 – 4 seconds**|
|**25,000 Tokens**|~65 – 89 seconds|**3 – 5 seconds**|
|**32,768 Tokens**|~85 – 115 seconds|**3 – 6 seconds**|

#### Prefix Caching Configuration

In multi-step execution workflows, system prompts, schemas, and early history remain identical. `llama-server` features automatic prefix caching, which reuses pre-computed KV states for matching prompt prefixes and processes only newly added tokens (e.g., the latest DOM tree snapshot).

  

To ensure efficient caching in `llama-server`:

  

- Set single-slot execution (`--parallel 1` or `-np 1`).
    
      
    
- Enable host-memory/cache reuse flags if available in your build: `--cache-reuse 256` or `--cram 512`.
    
      
    
- Structure prompts to keep static components (system prompt, schemas) at the top, appending dynamic step receipts at the end.
    
      
    

### 7. Backend Selection for Lunar Lake Arc 140V

#### Performance Comparison on Windows 11

|**Backend**|**Performance Rating**|**Stability Rating**|**Notes**|
|---|---|---|---|
|**SYCL (oneAPI / Level Zero)**|**Fastest (100%)**|**High**|Direct access to Xe2 XMX matrix cores via Intel DPCPP/Level Zero runtime.|
|**Vulkan**|Moderate (70–85%)|Low / Unstable|`VK_KHR_cooperative_matrix` driver bugs can cause GPU TDR crashes on Intel drivers `101.8509`/`101.8531`. Requires `GGML_VK_DISABLE_COOPMAT=1` as a workaround.|
|**OpenCL**|Slow (30–40%)|High|Legacy fallback lacking matrix hardware acceleration.|

#### Alternative Runtimes

- **OpenVINO**: Provides high inference performance on Intel hardware, but GGUF ecosystem compatibility and OpenClaw API integration are weaker than `llama.cpp`.
    
      
    
- **IPEX-LLM**: Offers strong PyTorch/vLLM-style optimization, but introduces higher setup complexity compared to a single `llama-server.exe` binary.
    
      
    

#### Identifying Your Current Backend

Run the following command in PowerShell:

  

PowerShell

```
.\llama-cli.exe --version
```

Inspect the startup logs:

  

- `ggml_sycl: Found 1 SYCL devices` $\$rightarrow **SYCL Backend**
    
      
    
- `ggml_vulkan: Found 1 Vulkan devices` $\$rightarrow **Vulkan Backend**
    
      
    
- `ggml_opencl: ...` $\rightarrow$ **OpenCL Backend**
    
      
    

If your build runs on Vulkan or OpenCL, replace it with a **SYCL-compiled `llama.cpp` release** for optimal performance on Lunar Lake.

  

### 8. Execution Reliability Check

#### Feasibility Verdict

Deploying Qwen3-8B Q4 as an execution-only agent is viable, provided that strict operational safeguards are enforced.

  

```
       Incoming Step Directives
                  │
                  ▼
┌───────────────────────────────────┐
│ llama-server                      │
│ (Enforces Strict JSON Grammar)    │
└─────────────────┬─────────────────┘
                  │ Valid JSON Tool Call
                  ▼
┌───────────────────────────────────┐
│ OpenClaw Execution Layer          │
│ ├─ Selector Presence Pre-Check    │
│ ├─ Retries (Max 3 Attempts)       │
│ └─ State Loop Detection           │
└─────────────────┬─────────────────┘
                  │ Success / Failure Receipt
                  ▼
┌───────────────────────────────────┐
│ Local Storage (Claim Check)       │
└───────────────────────────────────┘
```

#### Failure Modes & Safeguards

|**Failure Risk**|**Root Cause**|**Operational Mitigation**|
|---|---|---|
|**Invalid Tool JSON**|Minor model sampling variation.|Force JSON Schema output validation in `llama-server` or OpenClaw using structured outputs / GBNF grammars.|
|**Hallucinated DOM Selectors**|Complex UI trees.|Implement tool-side verification: check selector presence in the DOM before executing clicks. Return a standard error receipt if missing.|
|**Execution Loops**|Static DOM states after repeated clicks.|OpenClaw loop guard: limit identical tool calls to 3 attempts. Abort and escalate to the cloud model if unresolved.|

### 9. Operating Profiles & Execution Strategy

#### 9a. Operational Impact (Day vs. Unattended Night)

- **Power & Thermals**: Running prefill/decode passes pins the iGPU, drawing ~25–30W SoC power. On battery, this drains ~20–30% capacity per hour and increases fan noise.
    
      
    
- **System Resource Contention**: Foreground workloads will contend with desktop UI rendering and video encoding on the shared memory bus. Unattended overnight execution avoids this resource competition.
    
      
    

#### 9b. Dual Operating Profile Implementation

Set up two distinct launch configurations for `llama-server.exe`:

  

##### Daytime Configuration (`llama-daytime.cmd`)

Optimized for low resource footprint and fast UI responsiveness:

  

DOS

```
llama-server.exe ^
  --model Qwen3-8B-Q4_K_M.gguf ^
  --host 127.0.0.1 --port 8090 ^
  --ctx-size 16384 ^
  --parallel 1 ^
  --gpu-layers 999 ^
  --threads 4 --threads-batch 4 ^
  --prio -1 ^
  --jinja
```

##### Nighttime Configuration (`llama-nighttime.cmd`)

Optimized for long context batch handling during idle hours:

  

DOS

```
llama-server.exe ^
  --model Qwen3-8B-Q4_K_M.gguf ^
  --host 127.0.0.1 --port 8090 ^
  --ctx-size 32768 ^
  --cache-type-k q8_0 --cache-type-v q8_0 ^
  --parallel 1 ^
  --gpu-layers 999 ^
  --threads 8 --threads-batch 8 ^
  --prio 0 ^
  --jinja
```

##### Automated Task Management

Use Windows Task Scheduler to manage configuration switches:

  

1. **At 08:00 AM**: Task runs `taskkill /IM llama-server.exe /F` and launches `llama-daytime.cmd`.
    
      
    
2. **At 11:00 PM**: Task terminates daytime processes and launches `llama-nighttime.cmd`.