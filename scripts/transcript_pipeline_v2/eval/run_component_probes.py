"""
Run real component identity probes for Checkpoint C.
Probes candidate environments and models without simulation,
writing honest PASS, BLOCKED, or NOT_INSTALLED receipts.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts" / "transcript_pipeline_v2"))

from receipt import write_atomic_receipt, utc_now_iso


def run_component_probes():
    corrective_root = REPO_ROOT / "artifacts" / "transcript_pipeline_v2" / "corrective-run"
    install_receipts = corrective_root / "receipts" / "install"
    smoke_receipts = corrective_root / "receipts" / "smoke"
    install_receipts.mkdir(parents=True, exist_ok=True)
    smoke_receipts.mkdir(parents=True, exist_ok=True)

    print("=== Checkpoint C: Real Component Identity & Probe Smokes ===")

    # 1. Probe faster-whisper
    try:
        import faster_whisper
        import ctranslate2
        from faster_whisper import WhisperModel
        
        t0 = time.time()
        model = WhisperModel("base", device="cpu", compute_type="int8")
        load_time = time.time() - t0

        write_atomic_receipt(install_receipts / "asr_faster_whisper.json", {
            "schema": "ttk.receipt.v2",
            "component_id": "asr_faster_whisper",
            "package": "faster-whisper",
            "version": faster_whisper.__version__,
            "ctranslate2_version": ctranslate2.__version__,
            "status": "PASS",
            "device": "cpu",
            "compute_type": "int8",
            "installed_at": utc_now_iso()
        })
        write_atomic_receipt(smoke_receipts / "asr_faster_whisper.json", {
            "schema": "ttk.receipt.v2",
            "component_id": "asr_faster_whisper",
            "status": "PASS",
            "smoke_test": "load_base_model_cpu_int8",
            "load_time_seconds": round(load_time, 4),
            "evaluated_at": utc_now_iso()
        })
        print(f"[ASR_FASTER_WHISPER] Status: PASS (v{faster_whisper.__version__}, loaded in {load_time:.2f}s)")
    except Exception as e:
        print(f"[ASR_FASTER_WHISPER] Status: FAIL ({e})")

    # 2. Probe remaining candidate packages
    probes = [
        ("asr_parakeet", "nemo", "BLOCKED_DEPENDENCY", "NeMo/PyTorch CUDA ecosystem not installed on Windows Intel Arc environment"),
        ("align_whisperx", "whisperx", "BLOCKED_DEPENDENCY", "WhisperX / PyTorch audio stack not installed"),
        ("preextract_gliner2", "gliner2", "NOT_INSTALLED", "gliner2 package not installed in environment"),
        ("map_langextract", "langextract", "NOT_INSTALLED", "langextract package not installed in environment"),
        ("support_mdeberta", "transformers", "NOT_INSTALLED", "transformers/torch package not installed in environment"),
        ("support_hhem", "transformers", "NOT_INSTALLED", "transformers/torch package not installed in environment"),
        ("reduce_docetl", "docetl", "BLOCKED_FOR_TRIAL1", "docetl package not installed; Trial-1 uses agent/subagent semantic transport"),
        ("eval_deepeval", "deepeval", "NOT_INSTALLED", "deepeval package not installed in environment"),
        ("baseline_fabric", "fabric", "BLOCKED_FOR_TRIAL1", "fabric CLI binary not installed"),
        ("baseline_open_notebook", "open_notebook", "BLOCKED_FOR_TRIAL1", "open-notebook UI environment not installed")
    ]

    import importlib.metadata

    for cid, pkg_name, blocked_status, reason in probes:
        try:
            ver = importlib.metadata.version(pkg_name)
            status = "PASS"
            msg = f"Installed v{ver}"
        except importlib.metadata.PackageNotFoundError:
            status = blocked_status
            msg = reason

        write_atomic_receipt(install_receipts / f"{cid}.json", {
            "schema": "ttk.receipt.v2",
            "component_id": cid,
            "package": pkg_name,
            "status": status,
            "reason": msg,
            "installed_at": utc_now_iso()
        })
        write_atomic_receipt(smoke_receipts / f"{cid}.json", {
            "schema": "ttk.receipt.v2",
            "component_id": cid,
            "status": status,
            "reason": msg,
            "evaluated_at": utc_now_iso()
        })
        print(f"[{cid.upper()}] Status: {status} ({msg})")


if __name__ == "__main__":
    run_component_probes()
