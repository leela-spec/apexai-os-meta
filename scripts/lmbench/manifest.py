"""Independent filesystem audit. Stdlib only.

Deliberately imports nothing from `broker`, `trace`, `fsguard`, or `tools` --
enforced by `tests/test_architecture.py`. An auditor that shares code with the
thing it audits proves nothing: if `manifest.py` imported `fsguard`, a bug in
`fsguard`'s own path classification could hide the exact class of escape this
module exists to catch.

`capture()` hashes every file under a root by content only -- byte content,
never mtime/ctime -- so two materializations of identical bytes produce an
identical `content_hash()` regardless of when they were written (VAL-06).
`diff()` is the ground truth for "did anything change under this root,"
independent of whatever the trace claims happened.
"""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Manifest:
    root_label: str
    root_path: str
    entries: dict  # posix-style relpath -> sha256 hex digest, sorted keys on read


def _iter_files(root: str):
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in sorted(filenames):
            yield os.path.join(dirpath, name)


def capture(root_label: str, root_path: str) -> Manifest:
    """Hash every file under `root_path`. A missing/non-directory root
    captures as an empty manifest rather than raising -- a forbidden root that
    doesn't exist yet is still a valid thing to audit for "stayed empty"."""
    entries: dict[str, str] = {}
    real_root = os.path.realpath(root_path)
    if os.path.isdir(real_root):
        for full in _iter_files(real_root):
            rel = os.path.relpath(full, real_root).replace(os.sep, "/")
            with open(full, "rb") as handle:
                entries[rel] = hashlib.sha256(handle.read()).hexdigest()
    return Manifest(root_label=root_label, root_path=real_root, entries=entries)


def content_hash(manifest: Manifest) -> str:
    canonical = "\n".join(f"{path}:{digest}" for path, digest in sorted(manifest.entries.items()))
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


@dataclass(frozen=True, slots=True)
class ManifestDiff:
    root_label: str
    added: tuple[str, ...]
    removed: tuple[str, ...]
    changed: tuple[str, ...]

    @property
    def is_empty(self) -> bool:
        return not (self.added or self.removed or self.changed)


def diff(before: Manifest, after: Manifest) -> ManifestDiff:
    if before.root_label != after.root_label:
        raise ValueError(
            f"cannot diff manifests from different roots: "
            f"{before.root_label!r} vs {after.root_label!r}"
        )
    before_keys = set(before.entries)
    after_keys = set(after.entries)
    added = tuple(sorted(after_keys - before_keys))
    removed = tuple(sorted(before_keys - after_keys))
    changed = tuple(
        sorted(key for key in (before_keys & after_keys) if before.entries[key] != after.entries[key])
    )
    return ManifestDiff(root_label=before.root_label, added=added, removed=removed, changed=changed)


__all__ = ["Manifest", "capture", "content_hash", "ManifestDiff", "diff"]
