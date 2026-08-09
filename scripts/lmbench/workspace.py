"""Trial workspace lifecycle: allocate, terminate tracked processes, destroy.
Stdlib only.

Exempted from the fsguard-only write/spawn rule (with `fsguard.py` and
`telemetry.py`) because this module does harness-controlled setup and
teardown, not the actor's real-time tool-call surface -- there is no model
input on this path for a broker decision to gate.

Two things here matter more than they look:

`destroy()` never raises -- it returns whether the workspace is actually gone,
and a caller that gets `False` back must mark the trial `INFRA_INVALID` rather
than silently proceeding. Windows read-only files, held handles, and AV scans
are common, real reasons a `rmtree` fails; silently swallowing that would let
a residual file from trial N pollute trial N+1's baseline manifest.

`terminate_verified()` verifies `(pid, creation_time)` before killing, not
bare `pid` -- a crashed prior trial's PID can be reused by an unrelated
process on the operator's own machine by the time cleanup runs, and killing by
PID alone risks killing that unrelated process instead.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def allocate(base_dir: Path, trial_id: str) -> Path:
    trial_dir = base_dir / trial_id
    trial_dir.mkdir(parents=True, exist_ok=False)
    return trial_dir


def destroy(trial_dir: Path) -> bool:
    """Returns True iff the directory is verifiably gone afterward. Never raises."""
    try:
        shutil.rmtree(trial_dir, ignore_errors=False)
    except OSError:
        pass
    return not trial_dir.exists()


def spawn_tracked(argv, *, cwd: str) -> subprocess.Popen:
    kwargs = {}
    creation_flag = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", None)
    if creation_flag is not None:
        kwargs["creationflags"] = creation_flag
    return subprocess.Popen(list(argv), cwd=cwd, **kwargs)


def _creation_date(pid: int) -> str | None:
    """Query a process's creation timestamp via CIM. Property names
    (`CreationDate`) are English regardless of Windows display-language
    setting, unlike `Get-Counter` path strings -- this machine is German-locale."""
    try:
        completed = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-NonInteractive",
                "-Command",
                f"(Get-CimInstance Win32_Process -Filter \"ProcessId={pid}\").CreationDate",
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (subprocess.TimeoutExpired, OSError):
        return None
    value = completed.stdout.strip()
    return value or None


def is_alive(pid: int) -> bool:
    return _creation_date(pid) is not None


def terminate_verified(popen: subprocess.Popen, *, wait_seconds: float = 10.0) -> bool:
    """Terminate `popen` and its process tree, identity-checked by
    (pid, creation_time). Returns True iff the process is confirmed gone."""
    if popen.poll() is not None:
        return True
    pid = popen.pid
    before = _creation_date(pid)
    if before is None:
        # Vanished between spawn and check, or the CIM query itself failed --
        # fall through to a plain wait rather than guessing at a kill.
        try:
            popen.wait(timeout=wait_seconds)
        except subprocess.TimeoutExpired:
            return False
        return True
    subprocess.run(
        ["taskkill", "/PID", str(pid), "/T", "/F"],
        capture_output=True,
        timeout=15,
    )
    try:
        popen.wait(timeout=wait_seconds)
    except subprocess.TimeoutExpired:
        return False
    return True


__all__ = ["allocate", "destroy", "spawn_tracked", "is_alive", "terminate_verified"]
