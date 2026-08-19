# Vulkan device-lost crash on Intel Arc 140V — analysis and fix plan

Written 2026-08-11. Synthesizes two independent AI research reports (`Claude.md`, `Gem.md`) against this machine's actual state, so a future session can continue with zero re-derivation. If you're picking this up cold: read this file only, don't re-read the two source reports unless you need a direct quote — everything load-bearing from both is already pulled out below.

## Problem statement

Running `llama-server` (Qwen3-8B, `llama.cpp`, **Vulkan** backend) on this laptop's Intel Arc 140V iGPU crashes reproducibly, in the same shape, every time:

- Turn 1 of any fresh session always succeeds.
- Turn 2 of the *same* session reliably crashes as cumulative context grows.
- Confirmed **four separate times** on 2026-08-11, with and without the model's own thinking/reasoning mode enabled — so it is not caused by that toggle.
- Exact error: `ggml_vulkan: device lost on Vulkan0` → `getFenceStatus at ggml-vulkan.cpp:2603` → `vk::Device::getFenceStatus: ErrorDeviceLost`, surfaced to the caller as `FailoverError: decode() failed: ...` (also seen once as `got exception: ...` and once as a generic `network connection error` after the server had already died).

Real example from logs:
```
[[turn 1 — succeeds]]
prompt eval time = 37830.80 ms / 5587 tokens (147.68 tok/s)
eval time = 19661.29 ms / 150 tokens (7.63 tok/s)
slot release: task 0 | n_tokens = 5736

[[turn 2 — reuses cached context via slot/LCP similarity, then dies]]
slot get_available: selected slot by LCP similarity, f_sim_best = 0.555, f_keep = 0.997
slot launch_slot: task 153 | processing task
prompt processing, n_tokens = 2048, progress = 0.75, t = 13.94s / 146.97 tok/s
ggml_vulkan: device lost on Vulkan0
srv update_slots: decode() failed: vk::Device::getFenceStatus: ErrorDeviceLost
slot release: task 153 | n_tokens = 9812
```

Launch command in use:
```
llama-server.exe --model Qwen3-8B-Q4_K_M.gguf --host 127.0.0.1 --port 8090 --ctx-size 32768 --parallel 1 --gpu-layers 999 --jinja --reasoning-budget 128
```

## This machine's confirmed facts (checked 2026-08-11, read-only)

- **Driver: `32.0.101.8626`, dated 2026-03-11.** This is *newer* than both driver builds named in Claude.md's closest-matching upstream report (#20554: `101.8509` WHQL, `101.8531` non-WHQL) and newer than the older `101.7026` build reported to avoid the bug. Since #20554 was closed `not_planned` — meaning no code/driver fix ever shipped for it — a newer driver still crashing the same way is expected, not a contradiction.
- **`matrix cores: KHR_coopmat` activation status: UNCONFIRMED.** This is the single fastest yes/no test for Claude.md's leading hypothesis, and it has *not* been checked yet — `llama-server`'s device-identification startup banner (normally `ggml_vulkan: 0 = Intel(R) Arc(TM) 140V GPU ... matrix cores: ...`) is not present in any existing `.err.log`/`.out.log` file; those only captured per-request timing and the crash itself. **First action for the next session**: relaunch with fuller logging captured (redirect both stdout and stderr from the very first line, don't rely on the current redirection setup) and grep for `matrix cores`.
- `llama-server.exe --version` / build number: **not yet captured.** Both reports ask for this explicitly (behavior has shifted between builds in adjacent upstream threads). Run it and record the output before making other changes.

## Synthesis of the two research reports

**Where they agree:**
- This is a real, documented, *unresolved* upstream problem area for Intel Arc/Xe2 iGPUs + Vulkan + sustained compute, not a one-off local misconfiguration.
- The proximate mechanism is a driver-level timeout/reset (Windows TDR family of behavior) killing the GPU context mid-dispatch.
- `GGML_VK_DISABLE_COOPMAT=1` and switching to the SYCL backend are both worth trying, in that order.
- No known llama.cpp version pin fixes this — the fix, if any, lives in Intel's driver or in avoiding the triggering code path, not in a specific `llama.cpp` release.
- Windows TDR delay registry changes are diagnostic only, not a real fix.

**Where they genuinely disagree — do not silently pick one, test both:**

| Point | Claude.md | Gem.md |
|---|---|---|
| Primary named upstream issue | [#20554](https://github.com/ggml-org/llama.cpp/issues/20554) — `KHR_cooperative_matrix` causes TDR on **this exact GPU model** (Arc 140V) | [#18946](https://github.com/ggml-org/llama.cpp/issues/18946) — out-of-device-memory + fence timeouts + UMA memory accounting desync, also named for **this exact CPU** (Core Ultra 7 258V) |
| Root cause ranking | `KHR_coopmat` pipeline bug is "most likely," ranked above generic TDR | Splits likelihood across TDR-from-large-dispatch **and** a separate UMA memory-accounting bug, both "very high" |
| `--ctx-size` reduction | Low priority — device-lost is triggered by per-dispatch compute volume, not allocated buffer size; the referenced issues crashed at *smaller* ctx-size than ours | Worth trying — smaller upfront KV-cache allocation directly reduces UMA memory pressure, which is one of its two named root causes |
| Batch-size flags | Not mentioned | `--ubatch-size 128` (down from default 512) and `GGML_VK_MAX_NODES_PER_SUBMIT=1` — both aimed at shrinking per-dispatch size so single GPU submissions don't stall long enough to trigger TDR |

**The two reports cite two different GitHub issues for two different (if related) bugs on this same hardware.** Treat this as evidence there may be more than one problem stacked here, not one root cause with one fix. Don't stop at the first mitigation that seems to help without confirming it actually addresses the mechanism you think it does (see "confirms success" column below).

## CONFIRMED FIX (tested 2026-08-11, same day)

`GGML_VK_DISABLE_COOPMAT=1` **stops the crash.** Tested directly: same task, same session-reuse pattern that had crashed four times today at ~9,800–10,300 cumulative tokens now ran a session past **12,762 tokens across two tasks with no device-lost error** (`llama-server --version` for this build: `10333 (08659901c)`, Clang 20.1.8 — this build's default verbosity does not print the Vulkan device/`matrix cores` banner at all, so that specific diagnostic from step 1 below could not be captured; not worth pursuing further now that the fix is confirmed empirically).

The only failure in the confirmed-fix run was an unrelated client-side CLI timeout (480s) — generation speed with coopmat disabled is slower (~5 tok/s vs ~7–8 tok/s with coopmat on), so give it a longer timeout, not a shorter one. That's the real tradeoff of this fix: a real, working, crash-free session that just needs a proportionally longer request timeout.

**Recommended standing config**: set `GGML_VK_DISABLE_COOPMAT=1` in the `llama-server` launch environment permanently, and raise agent/request timeouts to account for the ~30-40% generation slowdown. Steps 3-8 below are no longer necessary to pursue unless this fix later proves insufficient under heavier real workloads (e.g. much longer sessions, more turns) — treat them as a fallback list, not a required next-step queue.

## Ordered action plan

Cheapest / least disruptive first. Each step names what to check to know if it actually worked, not just whether the crash happened to not recur once (turn-2-only crashes mean you need to reach turn 2 to trust a negative result).

1. **Capture the missing diagnostics first, no config change yet.** Relaunch exactly as today but with clean, fully-captured stdout+stderr from process start. Run `llama-server.exe --version` separately. Record: build number, and whether the startup banner shows `matrix cores: KHR_coopmat` or `matrix cores: none`. This resolves the biggest open unknown and tells you which report's primary hypothesis is even in play on this machine.
2. **`GGML_VK_DISABLE_COOPMAT=1`** (set as an environment variable before launching `llama-server.exe`). Confirms via the now-visible log line changing to `matrix cores: none`. This is the single most directly-evidenced fix for this exact GPU model (Claude.md / #20554). Test through at least 2 full turns to actually exercise the failure point.
3. **`--ubatch-size 128`** (down from the default 512). Gem.md's mitigation for the "one dispatch too large, stalls the queue, driver resets it" mechanism. Cheap, no rebuild, test independently of step 2 so you know which one (if either) is doing the work.
4. **`GGML_VK_MAX_NODES_PER_SUBMIT=1`.** Same mechanism as step 3, different lever — test independently, not stacked with step 3 on the first pass, so results are attributable.
5. **Partial GPU offload** — reduce `--gpu-layers` from `999` to a partial value. Both reports list this as a useful diagnostic (less GPU compute/memory pressure per turn should push the crash point later or eliminate it) even if it's not the final config you want (it will be slower).
6. **`--ctx-size` reduction** (e.g. `16384`) — the two reports disagree on whether this matters. Worth one deliberate, isolated test specifically because they disagree; don't trust either claim without checking it yourself on this hardware.
7. **Switch to a SYCL build of `llama-server`** (Intel oneAPI/Level Zero backend instead of Vulkan). Both reports agree this sidesteps the Vulkan-specific bug(s) by construction. Correctly sequenced last: requires installing Intel's oneAPI runtime, a new dependency, and re-benchmarking speed (mixed evidence in Claude.md on whether SYCL is faster or slower than Vulkan on this GPU family — test, don't assume).
8. **Windows TDR delay registry change** — listed last deliberately. Claude.md reports this was tried against the *exact same bug* (#20554) and did not prevent the crash, only delayed it while freezing the machine for the longer timeout window first. Gem.md lists it without that caveat. Treat it as diagnostic-only (useful to confirm TDR is really the kill mechanism via Event Viewer, per the diagnostics section below) — do not expect it to be a real fix.

## What NOT to do

- Don't chase a specific "known-good" `llama.cpp` version expecting a resolution — #20554 was closed `not_planned`, meaning no code fix shipped upstream for that bug. A version pin might dodge an unrelated regression but won't fix this.
- Don't assume `--ctx-size` is either definitely irrelevant or definitely helpful — the two reports disagree; step 6 above exists to settle it empirically for this exact machine.
- Don't rely on the TDR registry delay as a fix (see step 8) — it's confirmed not to work against the closest-matching bug.
- Don't stack multiple mitigations on the first test pass — you'll get a false "it's fixed" signal you can't attribute to anything, and won't know what to actually keep.

## Diagnostics, if the whole ordered list doesn't resolve it

- Windows Event Viewer → System log → look for `Display`/`igfxba`/`TdrTerminated` events at the crash timestamp. Confirms whether Windows TDR is really the kill mechanism, independent of the app.
- Build with `-DGGML_VULKAN_VALIDATE=ON` (referenced in a third, less-central issue, #22034) to get a more specific Vulkan validation error than the generic `ErrorDeviceLost` fence timeout.
- `VK_LOADER_DEBUG=all` with output redirected to a file, to see the Vulkan loader's own view of driver communication around the crash.
- If none of the above resolves it: file a **new** upstream GitHub issue, explicitly referencing #20554, #18946, and #19327, with this machine's driver version (`32.0.101.8626`), the `--version` build output from step 1, and which mitigations were tried and their exact results. This combination (dense model, Windows, Lunar Lake, session-based turn-2-specific crash) isn't cleanly covered by any single existing thread — a well-documented new report would be genuinely useful upstream, not just for us.

## Source material

- `FEE/GPU_Failure/Claude.md` — full original report, GPU-140V-specific issue #20554 as primary evidence.
- `FEE/GPU_Failure/Gem.md` — full original report, CPU-258V-specific issue #18946 as primary evidence, plus #19327 and #20201.
