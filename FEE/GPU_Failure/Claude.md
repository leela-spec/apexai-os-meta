## Direct Answer

Your exact symptom — Vulkan `device lost` / `getFenceStatus: ErrorDeviceLost` on an Intel Arc 140V, appearing as workload accumulates within a session — matches a documented, GPU-driver-level bug: **GitHub issue #20554**, filed for the same GPU (Arc 140V) on Windows 11 with the same failure mode. The most likely fix requiring zero code changes is setting `GGML_VK_DISABLE_COOPMAT=1` as an environment variable before launching `llama-server.exe`. Test that first.

## Q1: Is this a known issue?

Yes, partially matched, with caveats.

**Closest match — [#20554](https://github.com/ggml-org/llama.cpp/issues/20554)** "Vulkan/Intel bug: VK_KHR_cooperative_matrix causes GPU TDR on Intel Arc 140V (101.8509) with llama.cpp Vulkan backend." Same exact GPU model as yours. Reporter: TDR (driver reset) occurs during Vulkan compute dispatch on Arc 140V with drivers 101.8509 (WHQL) or 101.8531 (non-WHQL). The server dies silently when the driver recovers from the reset — matching your "process just dies, next session's turn 1 works again" pattern[20554].

- **Cause identified in the thread**: combination of `matrix cores: KHR_coopmat` (a Vulkan cooperative-matrix extension llama.cpp uses on GPUs that advertise it) and the newest Intel drivers.
- **Workaround confirmed by the reporter**: `$env:GGML_VK_DISABLE_COOPMAT = "1"` before launch — this disables the coopmat code path (you'll see `matrix cores: none` in startup logs instead of `KHR_coopmat`), and the TDR/device-lost stops occurring.
- **Alternate workaround**: roll back to the older Lenovo OEM driver 101.7026, which doesn't trigger it.
- Status: closed as `not_planned` due to inactivity (stale-bot), **not because it was fixed upstream** — it's an open, unresolved driver/backend interaction, cross-referenced to [Intel GPU Community Issue Tracker #1330](https://github.com/IGCIT/Intel-GPU-Community-Issue-Tracker-IGCIT/issues/1330)[20554].

**Related but not identical — [#19327](https://github.com/ggml-org/llama.cpp/issues/19327)**, Arrow Lake iGPU (not Xe2/Lunar Lake) on Linux. Root cause there was traced by a contributor to the Linux `xe` kernel driver's hardcoded 10-second job timeout (`CONFIG_DRM_XE_JOB_TIMEOUT_MAX`), specifically hit by `MUL_MAT_ID` operations on MoE models with many experts[19327]. **This doesn't directly apply to you**: you're on Windows (different driver stack entirely — WDDM/TDR, not the Linux `xe` KMD), and Qwen3-8B is a dense model, not MoE, so the expert-count-triggered timeout mechanism in that thread isn't your mechanism. It's evidence of the general pattern (Intel iGPU + Vulkan + sustained compute → driver-enforced timeout kills the device) but not a literal match.

**Also related — [#22034](https://github.com/ggml-org/llama.cpp/issues/22034)**, Intel Arc B580 (discrete, not iGPU) `getFenceStatus` device-lost, but reproduced only with specific tiny batch sizes (`-b 32 -ub 32`) in `llama-bench`, unrelated to your batch config. Confirms `getFenceStatus`/`ErrorDeviceLost` is a recurring generic symptom across several distinct Intel Vulkan bugs, not one single root cause[22034].

**No exact issue exists yet for "crashes specifically on turn 2 of a multi-turn session with slot/prompt-cache reuse on Lunar Lake."** That specific framing (session-level, slot-reuse-triggered) does not appear as a filed, resolved issue. Treat that framing as your own hypothesis, not confirmed fact.

## Q2: Root cause assessment

Ranked by evidence strength, not by your listed order:

| Hypothesis | Assessment |
|---|---|
| Driver-level TDR on Xe2/Arc 140V triggered by `KHR_coopmat` pipeline | **Most likely.** Directly documented for your exact GPU in #20554[20554]. Explains why it's reproducible: turn 2 does more cumulative Vulkan compute work than turn 1 (larger prompt reprocessing + KV state), pushing a coopmat-path dispatch over whatever threshold triggers the driver bug. |
| Windows TDR killing a too-long single dispatch | **Plausible contributing mechanism**, but likely downstream of the coopmat bug rather than a separate root cause — the coopmat pipeline is what's producing the pathological dispatch in the first place. Not "just" TDR being too strict; #20554's reporter tried raising `TdrDelay` to 60s and the driver still crashed after that longer window, meaning the workload itself is stalling the GPU, not merely running long under a tight timeout. |
| Vulkan resource/descriptor leak across slot reuse ("LCP similarity" cache reuse) | **Not supported by evidence found.** No filed issue attributes device-lost specifically to llama-server's slot/prompt-cache reuse logic. Your logs show turn 2 reprocessing ~2048 tokens fresh (not full slot hit) before the crash — consistent with "more compute work hits the driver bug," not with a leak from reuse logic per se. |
< br>
| Shared-memory/UMA allocator instability specific to iGPUs | **Unconfirmed as a distinct cause.** iGPU UMA does show up in other Intel-Vulkan threads (Arrow Lake #19327) but as a secondary factor, not as the primary reported cause for Arc 140V.

**Bottom line on root cause**: current best evidence points to a driver bug in Intel's cooperative-matrix (`KHR_coopmat`) Vulkan implementation on Xe2, triggered once compute load crosses some threshold — which lines up with "first turn always small enough to survive, second turn's added compute crosses the line." This is a hypothesis with direct supporting evidence, not proven causation for your specific case — you haven't yet confirmed `matrix cores: KHR_coopmat` appears in your own startup log.

## Q3: Vulkan vs SYCL vs OpenCL for Arc/Xe2

No unconditional "SYCL is more stable" claim holds up under scrutiny; evidence is mixed and workload-dependent. [reddit](https://www.reddit.com/r/IntelArc/comments/1enunga/llamacpp_benchmarks_of_llama318b_on_arc_a770/)

- On Xe2/Lunar Lake specifically, one user report (mid-2026) found Vulkan on Arrow Lake iGPU essentially unusable (~0.5–4 t/s) while SYCL delivered 4–12 t/s and was the only usable path.[2]
- Conversely, a detailed benchmark on Arc B70 (discrete, post-driver-update) found Vulkan *faster* than SYCL at every concurrency level after a Mesa 26.1 update — the opposite of what held true months earlier. [reddit](https://www.reddit.com/r/LocalLLaMA/comments/1abb5cx/sycl_for_intel_arc_support_almost_here/)
- On older Arc A770, SYCL crushed Vulkan on prompt processing (870 vs 140 t/s) but was roughly tied or slightly behind on generation speed. [reddit](https://www.reddit.com/r/IntelArc/comments/1enunga/llamacpp_benchmarks_of_llama318b_on_arc_a770/)
- SYCL requires installing Intel's oneAPI runtime — an extra dependency your current setup doesn't have.

**Practically for you**: SYCL is worth testing as a fallback specifically *because* it uses a completely different code path than the buggy `KHR_coopmat` Vulkan pipeline implicated in #20554 — it would sidestep that specific bug by construction, not because SYCL is generically "more stable." If SYCL also crashes, that would argue against the coopmat/Vulkan-specific hypothesis and toward a lower-level driver/thermal/TDR issue affecting both backends.

## Q4: Concrete mitigations, ordered least → most disruptive

1. **Set `GGML_VK_DISABLE_COOPMAT=1` as an environment variable, relaunch, confirm log shows `matrix cores: none`.** This is the single most directly evidenced fix for your exact hardware, per #20554[20554]. Zero cost besides a possible performance drop.
2. **Check your current Intel Arc driver version.** If you're on 101.8509 or 101.8531 (the versions implicated), that itself is diagnostic information worth reporting back. Rolling back to something like Lenovo's 101.7026 worked for the original reporter, but you're on an HP, so an HP-branded equivalent-vintage driver (not the Lenovo package itself) would be the analogous move — check HP's support site for driver history around that timeframe.
3. **Run `llama-server.exe --version`** and report the build number/commit hash — this is requested explicitly because both #20554 and #22034 pin their reports to specific build numbers (8317, 8827), and behavior has shifted between builds in adjacent threads.
4. **Try disabling prompt-cache/slot reuse** as a diagnostic (not because reuse is confirmed as the cause, but to rule it out): pass `--no-slot-reuse` type flags if your build supports them, or force `--parallel 1` with no cache-prompt reuse, and see if crash still occurs at similar cumulative token counts. If it does, that rules out slot-reuse logic as the trigger and further implicates raw compute-volume-triggered driver TDR.
5. **Reduce `--gpu-layers` from 999 to partial offload** as a compute-load-reduction test — if the coopmat/TDR hypothesis is right, less GPU compute work per turn should push the crash point further out or eliminate it, which is diagnostically useful even if not your final config.
6. **`--ctx-size` reduction is unlikely to matter** — device-lost/TDR in the referenced issues is triggered by per-dispatch compute volume, not by allocated buffer size; the crashes in #20554/#19327 occurred with much smaller ctx-size than yours. Low priority to test.
7. **Disabling Windows TDR delay entirely** was tried by the #20554 reporter (raised to 60s) and did **not** prevent the crash — it just delayed it and froze the laptop for 60 seconds first. Do not rely on this as a fix; it's diagnostic-only and the evidence says it won't work anyway.
8. **No specific "known-good" llama.cpp build/version is documented as fixing this upstream** — #20554 was closed `not_planned`, meaning no code fix shipped. Don't chase a version pin expecting resolution; the fix (if any) lives in Intel's driver, not llama.cpp's codebase.

## Q5: Better diagnostics if none of the above works

- **Confirm coopmat is actually active** first: your startup log line `ggml_vulkan: 0 = Intel(R) Arc(TM) 140V GPU ... matrix cores: KHR_coopmat` (as shown in #20554) versus `matrix cores: none` after the env-var fix. This single line is the fastest yes/no test for the leading hypothesis.
- **Vulkan validation layers**: build with `-DGGML_VULKAN_VALIDATE=ON` as done in #22034, which surfaces `vkGetFenceStatus(): Returned error VK_ERROR_DEVICE_LOST` with more context around which dispatch triggered it[22034].
- **Windows Event Viewer** → check for `nvlddmkm`/`igfx`/`TdrTerminated` or Display driver crash events under System log around the crash timestamp — Windows TDR recoveries are logged there independent of the app.
- **Intel Graphics Command Center** or `intel_gpu_top`-equivalent monitoring during turn 2 to watch for a compute utilization spike right before the crash — would corroborate the "compute volume crosses a threshold" hypothesis.
- File a **new** GitHub issue if none of the above resolves it, explicitly referencing #20554 and #19327, with your `--version` output, driver version, and whether `GGML_VK_DISABLE_COOPMAT=1` changed anything — this is currently missing data upstream and would be genuinely useful to the maintainers, since your case (dense model, session-based, Windows, Lunar Lake) isn't exactly covered by either existing thread.