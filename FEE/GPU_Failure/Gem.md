This is a **known hardware/driver/backend interaction issue** on Intel Lunar Lake (Arc 140V) and Arrow Lake platforms running `llama.cpp` over Vulkan.

  

Below is the detailed breakdown of the issue, root causes, backend comparisons, ranked mitigations, and diagnostic steps.

  

## Quick Check: How to Check Your `llama-server` Version

Before applying fixes, check your build version using either:

  

1. **CLI Flag:** Run `llama-server.exe --version` in your terminal.
    
      
    
2. **Startup Log Header:** Look at the first 5–10 lines of stdout when launching `llama-server.exe`. It outputs a line similar to:
    
      
    
    Plaintext
    
    ```
    build: 8252 (a241b0b) or version: 8322 (40c550d)
    ```
    

_Please record the build number and commit hash when testing or reporting upstream._

  

## 1. Is this a known issue?

**Yes.** This behavior is documented in multiple upstream GitHub issues across `ggerganov/llama.cpp` involving **Intel Arc GPUs (Xe2 / Lunar Lake Core Ultra 7 258V)** and the **Vulkan backend**:

  

- **GitHub Issue [#18946](https://github.com/ggml-org/llama.cpp/issues/18946)**: _"Critical Out of Device Memory Errors and Memory Accounting Failures in llama.cpp (Vulkan Backend and SYCL Backend) with Intel 258v APU Processor"_
    
      
    - Specifically tracks systematic instability, fence timeouts (`vk::Device::getFenceStatus: ErrorDeviceLost`), and UMA memory accounting desynchronization on Intel Core Ultra 7 258V / Arc 140V.
        
          
        
- **GitHub Issue [#19327](https://github.com/ggml-org/llama.cpp/issues/19327)**: _"Vulkan backend crashes on Intel Arrow Lake / Lunar Lake iGPU"_
    
      
    - Identifies driver job timeouts and UMA memory buffer crashes when processing larger prompt/context sequences on Intel iGPUs.
        
          
        
- **GitHub Issue [#20201](https://github.com/ggml-org/llama.cpp/issues/20201)**: _"Intel iGPU + Vulkan - crashes"_
    
      
    - Confirms context-dependent crashes on Intel Arc iGPUs during Vulkan execution.
        
          
        

## 2. Root Cause Hypotheses Assessment

Based on the failure logs and known Intel Lunar Lake driver characteristics:

  

### Primary Root Cause A: Windows TDR (Timeout Detection & Recovery) Trigger

- **Likelihood:** **Very High**
    
      
    
- **Mechanism:** On turn 2, when prompt caching reuses existing KV slots and appends thousands of new context tokens (`n_tokens = 2048` on top of ~8k tokens), `llama.cpp` submits heavy Vulkan compute command buffers. Because iGPUs share system memory bandwidth, long prompt-eval dispatches stall the execution pipeline. If a single GPU queue execution takes longer than Windows' default TDR threshold (~2 seconds), Windows assumes the GPU is hung, resets the graphics driver context, and immediately returns `vk::Device::getFenceStatus: ErrorDeviceLost`.
    
      
    

### Primary Root Cause B: UMA Dynamic Memory Management Bug in Intel's Vulkan Driver

- **Likelihood:** **Very High**
    
      
    
- **Mechanism:** Lunar Lake uses standard LPDDR5X as unified memory (UMA). When `--gpu-layers 999` is set, `llama.cpp`'s Vulkan allocator requests device-local dynamic buffers. Intel’s Windows Vulkan driver (ICD) contains known memory desynchronization bugs when updating existing descriptor sets across continuous session turns without a complete device re-initialization. Reusing cached slots ("LCP similarity match") appends data into pre-allocated Vulkan memory buffers, triggering driver-level buffer corruption and context invalidation.
    
      
    

### Contributing Factor: Vulkan Graph Batching

- **Likelihood:** **High**
    
      
    
- `ggml-vulkan` historically batches up to 100 graph nodes per queue submission. On Intel UMA platforms, monolithically batched command buffers overload the driver scheduler, precipitating fence polling timeouts.
    
      
    

## 3. Is this specific to Vulkan? (Vulkan vs. SYCL)

**Vulkan is the primary trigger for this specific fence crash, but Intel Arc APUs have platform-level caveats.**

  

- **Vulkan:** Vulkan is a cross-platform API. Intel's Vulkan ICD on Windows is notoriously prone to timeout crashes under continuous LLM compute workloads, especially when handling dynamic UMA memory allocation across sequence turns.
    
      
    
- **SYCL (via Intel oneAPI / Level Zero):** SYCL is Intel’s **native compute backend** for Arc GPUs. It interacts directly with Intel's Level Zero driver interface rather than the Vulkan KHR fence queue.
    
      
    - **Stability:** SYCL generally bypasses `vk::Device` fence timeout crashes entirely.
        
          
        
    - **Performance:** On Arc 140V (Xe2), SYCL builds compiled with Intel DPCPP utilize XMX matrix instructions directly, offering superior tokens-per-second performance compared to Vulkan.
        
          
        
    - **Caveat:** Earlier driver builds for Lunar Lake had memory allocation bugs under SYCL as well (as noted in Issue #18946), but recent Intel driver updates + SYCL builds are significantly more stable than Vulkan on Arc hardware.
        
          
        

## 4. Concrete Mitigations (Ranked from Least to Most Disruptive)

### Option 1: Limit Vulkan Queue Submission Batching (Environment Variable)

`llama.cpp` added environment variables to restrict how many execution graph nodes are bundled into a single Vulkan dispatch.

  

- **Action:** Set the environment variable before launching `llama-server`:
    
      
    
    DOS
    
    ```
    set GGML_VK_MAX_NODES_PER_SUBMIT=1
    ```
    
- _Why it helps:_ Prevents single long-running dispatches from holding the iGPU queue, directly preventing Windows TDR timeouts during turn 2 context evaluations.
    
      
    

### Option 2: Reduce Micro-Batch Size (`-ub`)

By default, `llama-server` evaluates prompts in chunks of 512 tokens (`--ubatch-size 512`). On iGPUs, evaluating 512 tokens at 8K context causes huge execution delays per step.

  

- **Action:** Pass `--ubatch-size 128` (or `-ub 128`) in your launch command:
    
      
    
    DOS
    
    ```
    llama-server.exe --model Qwen3-8B-Q4_K_M.gguf --host 127.0.0.1 --port 8090 --ctx-size 32768 --ubatch-size 128 --parallel 1 --gpu-layers 999 --jinja --reasoning-budget 128
    ```
    
- _Why it helps:_ Breaks context evaluation into smaller dispatches, letting the GPU yield to the OS and preventing driver reset timeouts.
    
      
    

### Option 3: Update Intel Arc Drivers & Adjust BIOS VRAM Allocation

- **Driver Update:** Ensure you are running the latest Intel Graphics Driver for Lunar Lake (Arc 140V).
    
      
    
- **BIOS / Driver VRAM Override:** In BIOS or Intel Arc Control, set the dedicated/pre-allocated memory from **Auto** to a fixed size (e.g., 16 GB). Issue #18946 noted that dynamic UMA allocation in "Auto" mode frequently triggers memory accounting crashes.
    
      
    

### Option 4: Switch Backend from Vulkan to SYCL

Instead of using a Vulkan binary build of `llama.cpp`, switch to a **SYCL build** (`llama-server` built with Intel oneAPI / SYCL).

  

- **Action:** Download or build the `llama.cpp` release tagged with `sycl` support (e.g., `llama-bXXXX-bin-win-sycl-x64.zip`).
    
      
    
- _Why it helps:_ Bypasses the Vulkan driver stack completely and uses Intel's Level Zero compute interface.
    
      
    

### Option 5: Reduce Initial Pre-Allocated Context Size (`--ctx-size`)

Setting `--ctx-size 32768` forces the Vulkan backend to allocate massive KV cache structures upfront in shared RAM.

  

- **Action:** Lower `--ctx-size` to `16384` or `12288` if your agent workload permits it.
    
      
    

### Option 6: Adjust Windows TDR Registry Delay (Diagnostic Workaround)

If the crash is caused purely by Windows timing out the long GPU execution turn:

  

1. Open `regedit` and navigate to: `HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers`
    
      
    
2. Create/edit a `DWORD (32-bit)` value named `TdrDelay` and set value to `10` (decimal, representing 10 seconds timeout instead of 2).
    
      
    
3. Reboot Windows.
    
      
    

## 5. Gathering Diagnostic Information

If the issue persists, collect deeper diagnostics to confirm the exact failing operation:

  

### 1. Check Windows Event Logs for TDR

After a crash, open **Windows Event Viewer** -> `Windows Logs` -> `System`.

  

- Search for **Source: Display** or **Event ID 4101** (_"Display driver igfxba stopped responding and has successfully recovered."_).
    
      
    
- If present, it confirms Windows TDR killed the Vulkan device due to execution length.
    
      
    

### 2. Enable `llama.cpp` Vulkan Debug Flags

Set these environment variables in your terminal prior to running `llama-server.exe`:

  

DOS

```
:: Forces synchronous checking after each op to pinpoint the exact failing shader kernel
set GGML_VULKAN_CHECK_RESULTS=1

:: Enables verbose output from the Vulkan allocator
set GGML_VULKAN_DEBUG=1
```

### 3. Capture Vulkan Loader Debug Output

To view memory allocation calls and Vulkan driver communication:

  

DOS

```
set VK_LOADER_DEBUG=all
llama-server.exe ... > vulkan_debug.log 2>&1
```

## Recommended Next Step

Start by trying **Option 1** (`set GGML_VK_MAX_NODES_PER_SUBMIT=1`) and **Option 2** (`--ubatch-size 128`). These two changes address the prompt-cache/TDR crash without requiring driver reinstalls or binary changes.