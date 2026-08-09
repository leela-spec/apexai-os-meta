"""The sole write/delete/rename/spawn choke point. Stdlib only.

Every other module in this package is banned (by `tests/test_architecture.py`,
a source-scan over every `.py` file) from calling `open(..., "w"/"a"/"x")`,
`os.remove`, `os.rename`, `shutil.rmtree`, or `subprocess.*` -- except
`workspace.py` and `telemetry.py`, which do harness-controlled setup/teardown/
sampling rather than dispatching the actor's real-time tool calls, and
`trace.py`, which only ever appends to its own fixed trial-trace file, never
to a model-supplied path.

`FsGuard` does not trust the broker's decision on faith: it holds its own
`RootSet` and re-classifies every path itself at open time. If that
re-classification disagrees with what the broker already decided -- a
directory junction swapped in between decision and open, say -- this raises
`InfraInvalid` rather than silently proceeding. That closes the TOCTOU window
and means "the broker logged a denial but the tool ran anyway" has no code
path: a tool implementation only ever receives the broker's *resolved* path,
and every resolved path is re-checked here regardless.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Sequence

from .errors import InfraInvalid
from .winpath import RootSet


class FsGuard:
    def __init__(self, roots: RootSet):
        self._roots = roots

    def _classify_or_raise(self, path: str, *, need_write: bool) -> None:
        cmp = os.path.normcase(os.path.realpath(path))
        rule = self._roots.classify(cmp)
        if rule is None or rule.mode == "forbidden":
            raise InfraInvalid(f"fsguard: path not accessible: {path}")
        if need_write and rule.mode != "rw":
            raise InfraInvalid(f"fsguard: path not writable: {path}")

    def read_text(self, path: str) -> str:
        self._classify_or_raise(path, need_write=False)
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read()

    def write_text(self, path: str, content: str) -> None:
        self._classify_or_raise(path, need_write=True)
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)

    def delete(self, path: str) -> None:
        self._classify_or_raise(path, need_write=True)
        os.remove(path)

    def list_dir(self, path: str) -> list[str]:
        self._classify_or_raise(path, need_write=False)
        return sorted(os.listdir(path))

    def run_argv(
        self, argv: Sequence[str], *, cwd: str, timeout: float = 60.0
    ) -> subprocess.CompletedProcess:
        """Never a command string -- always argv, always `shell=False`. There
        is no shell metacharacter interpretation for the actor to exploit, and
        `cmd.exe`/`powershell.exe`/`mklink` are never allowlisted as argv[0]
        prefixes, so the actor has no way to create a link or invoke a shell
        even if it discovers `run_command`."""
        return subprocess.run(
            list(argv),
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            shell=False,
        )


__all__ = ["FsGuard"]
