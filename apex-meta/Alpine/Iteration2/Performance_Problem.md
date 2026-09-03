### The Diagnostic Breakdown: Architectural Premise vs. Reality

We just captured live telemetry from both the **individual containers** and the **Windows NT kernel host** while the stack was running.

Here is what is happening and why your laptop is experiencing mouse lag, delayed clicks, and frozen window frames:

---

### 1. The Container Layer Is Actually Lean (~1.4 GB Total)

We queried the internal container metrics directly from the Docker Engine. The 7 services themselves are using:

text

ki-basis-nginx            Memory:     3.1 MB

ki-basis-valkey           Memory:     5.6 MB

ki-basis-firefly          Memory:     9.7 MB

ki-basis-postgres         Memory:    49.2 MB

ki-basis-hermes           Memory:   206.4 MB

ki-basis-paperless        Memory:   244.6 MB

ki-basis-openproject      Memory:   891.9 MB

------------------------------------------------

Total Container Memory:             ~1,410 MB (~1.4 GB)

The services inside the engine are behaving as designed and consuming only **~1.4 GB** combined.

---

### 2. So Why Is the Laptop Freezing? (The Four Compounding Factors)

The presumption was that a 1.4 GB container stack would have a negligible impact on a 32 GB machine. However, running it inside **Docker Desktop on Windows** triggers a cascade of host-level bottlenecks:

#### Cause A: Docker Desktop Host App Overhead (Electron + GPU)

Docker Desktop on Windows is not just a container runner—it is a heavy **Electron desktop application**. Live telemetry shows Docker Desktop launched **5 separate Windows host processes** (`Docker Desktop.exe` PID 6556, 12120, 15912, 16924, 23472) plus 2 `com.docker.backend.exe` processes. These processes attach hardware-accelerated GPU hooks into the Windows display subsystem, competing directly with your screen compositor.

#### Cause B: DWM (Desktop Window Manager) Starvation

- **Live `dwm.exe` state:** **756.5 MB Private Memory** (Normal is ~50–100 MB).
- **The effect:** `dwm.exe` is the master process responsible for rendering your mouse cursor, window close (`X`) buttons, taskbar, and animations. When Docker Desktop’s virtual display/GPU hooks interact with Windows, DWM balloons to 750+ MB. When DWM struggles, the **exact symptoms are mouse cursor skipping/stuttering and window close buttons not responding**.

#### Cause C: Windows Kernel "Memory Compression" Thrashing

- **Live Memory Compression:** **1,999.3 MB (2.0 GB)**!
- **The effect:** When Docker Desktop and Hyper-V request their dynamic memory block, the host memory pressure crosses the Windows aggressive threshold. Windows starts actively compressing 2.0 GB of RAM in the background. Every time you switch windows, open a folder, or click a browser tab, your CPU has to synchronously decompress pages, producing a 2–4 second input freeze.

#### Cause D: OpenProject Dominance

Inside the stack, **OpenProject alone takes 892 MB (63% of the entire stack)** due to the Ruby on Rails Puma multi-process cluster and background workers. When Puma spawns threads inside the VM, it triggers Hyper-V vCPU scheduling interrupts.

---

### 3. Concrete Solutions to Eliminate the Drag

To return your laptop to a responsive state while keeping the stack operational, we can apply three targeted adjustments:

|Measure|What It Does|Expected Relief|
|---|---|---|
|**1. Run Docker Headless (Kill Docker Desktop GUI)**|Keep the Docker engine daemon running in the background, but close the heavy 5-process Electron GUI (`Docker Desktop.exe`).|Frees GPU contexts and stops DWM compositor stutter immediately.|
|**2. Cap OpenProject Puma Workers (`OPENPROJECT_WEB_WORKERS=1`)**|Cuts OpenProject's memory usage from ~900 MB down to ~400 MB.|Reduces VM memory pressure and stops Windows Memory Compression.|
|**3. Hard Resource Limits in `compose.yaml`**|Put strict `deploy.resources.limits` (e.g. max 1.5 GB for OpenProject, 512 MB for Paperless).|Prevents containers from triggering Hyper-V dynamic memory ballooning.|

---

### Immediate Next Step

To test this right now and get immediate relief on your desktop:

1. Would you like to **gracefully stop the stack and Docker Desktop GUI** to verify that your mouse and window responsiveness instantly return to 100%?
2. Or would you like to **apply the lightweight single-worker and headless configuration** so it runs in the background without freezing Windows?