# Local Ollama Integration Runbook: Windows Host to WSL2 Hermes

**Document ID:** ALR-003  
**Date:** 2026-09-07  
**Location:** `apex-meta/orchestration/new_final_v4/learnings_and_corrections/`  
**Target Architecture Level:** Tier 2 / Host OS Bridge  

---

## 1. Context & Architecture Diagnostic

The Windows host has Ollama installed at:
`C:\Users\gehma\AppData\Local\Programs\Ollama\ollama.exe`
With active model: `qwen3.5:9b` (9.7B parameters, Q4_K_M quantization, 262k context length, tool calling supported).

**The Architectural Disconnect:**
By default, Windows Ollama binds exclusively to `127.0.0.1:11434` (Windows loopback). WSL2 runs in a lightweight Hyper-V virtual machine with its own virtual IP (`172.29.176.x`). When Hermes in WSL queries `localhost:11434` or the host gateway, the connection is refused.

---

## 2. Solution Path A: Enable Host Binding (Zero Install in WSL)

To allow Hermes in WSL2 to reach the Windows Ollama server:

### Step 1: Bind Windows Ollama to All Interfaces
In an Administrator PowerShell terminal on Windows:
```powershell
[System.Environment]::SetEnvironmentVariable('OLLAMA_HOST', '0.0.0.0:11434', 'User')
```
Restart Ollama from the Windows system tray or relaunch `ollama.exe`.

### Step 2: Open Windows Firewall for WSL Subnet
```powershell
New-NetFirewallRule -DisplayName "Ollama WSL Inbound" -Direction Inbound -LocalPort 11434 -Protocol TCP -Action Allow
```

### Step 3: Configure Hermes in WSL to Point to Windows Host Gateway
In WSL2, find the host gateway IP:
```bash
HOST_IP=$(ip route | grep default | awk '{print $3}')
```
Update `/root/.hermes/config.yaml`:
```yaml
model:
  provider: ollama
  base_url: http://172.29.176.1:11434/v1
  default: qwen3.5:9b
  max_tokens: 32768
```

---

## 3. Solution Path B: Native Ollama in WSL2 (Recommended for Maximum Speed)

Running Ollama directly inside WSL Ubuntu provides native Linux direct GPU passthrough (NVIDIA CUDA) without crossing the Hyper-V virtual switch:

### Step 1: Install Ollama in WSL2
```bash
wsl.exe -d Ubuntu -u root -e bash -c "curl -fsSL https://ollama.com/install.sh | sh"
```

### Step 2: Pull Model
```bash
wsl.exe -d Ubuntu -u root -e bash -c "ollama pull qwen3.5:9b"
```

### Step 3: Configure Hermes to Use Native Localhost
Update `/root/.hermes/config.yaml`:
```yaml
model:
  provider: ollama
  base_url: http://127.0.0.1:11434/v1
  default: qwen3.5:9b
  max_tokens: 32768
```

---

## 4. Expected Performance Gains
- **Zero API Costs**: 100% free offline execution.
- **Zero SSE Stream Timeouts**: Instant local token streaming directly to ext4 disk.
- **Inference Speed**: ~45-60 tokens/second on modern local GPUs.
- **Offline Reliability**: Autonomous workflows run completely isolated without internet access.
