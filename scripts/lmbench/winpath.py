"""Windows-aware path normalization and multi-root classification. Stdlib only.

The attack surface here is the path string itself, not the policy language: an
alternate data stream (`work\\ok.txt:evil`), a reserved device name (`NUL`,
`COM1`), a trailing dot/space component (Windows silently strips it, so two
names collide), an 8.3 short name (`PROGRA~1`), or a UNC/device prefix
(`\\\\?\\`, `\\\\.\\`) can all defeat a naive `str.startswith` root check.
`normalize_path` rejects every one of these *before* any filesystem call, with
a distinct, traceable reject code -- a rejection is an authority-relevant
attempt, not a silent parse failure, so it must never raise.

`RootSet.classify` compares path *components*, never raw strings, and resolves
longest-prefix-first so a `forbidden` subtree nested inside an `rw` root is
honoured.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass

REJECT_CODES = frozenset(
    {
        "NOT_STRING",
        "EMPTY",
        "NUL_BYTE",
        "ADS",
        "RESERVED_NAME",
        "TRAILING_DOT_OR_SPACE",
        "WILDCARD",
        "SHORT_NAME",
        "UNC_OR_DEVICE_PREFIX",
        "UNRESOLVABLE_PARENT",
    }
)

_RESERVED_NAMES = frozenset(
    {"CON", "PRN", "AUX", "NUL"}
    | {f"COM{d}" for d in "123456789"}
    | {f"LPT{d}" for d in "123456789"}
)

_SHORT_NAME_RE = re.compile(r"^[A-Za-z0-9_-]{1,6}~\d+$")
_WILDCARD_RE = re.compile(r"[*?]")


@dataclass(frozen=True, slots=True)
class PathCandidate:
    """The result of normalizing one path argument. Never raises; a bad path
    is `reject_code`, not an exception -- the broker denies it and traces the
    attempt rather than the harness swallowing it as a parse error."""

    raw: object
    real: str | None
    cmp: str | None
    reject_code: str | None


def _component_reject(component: str) -> str | None:
    if component in ("", ".", ".."):
        return None
    name = component.split(".", 1)[0].upper()
    if name in _RESERVED_NAMES:
        return "RESERVED_NAME"
    if component != component.rstrip(" ."):
        return "TRAILING_DOT_OR_SPACE"
    if _WILDCARD_RE.search(component):
        return "WILDCARD"
    if _SHORT_NAME_RE.match(component):
        return "SHORT_NAME"
    return None


def normalize_path(raw: object, *, base: str) -> PathCandidate:
    """Normalize a model-supplied path string against a trial-relative `base`.

    Rejects before touching the filesystem. On success, resolves the *parent*
    directory with `os.path.realpath` and rejoins the validated leaf -- a write
    target does not exist yet, so resolving the whole string would not catch a
    symlink/junction planted in the parent chain.
    """
    if not isinstance(raw, str):
        return PathCandidate(raw=raw, real=None, cmp=None, reject_code="NOT_STRING")
    if raw == "":
        return PathCandidate(raw=raw, real=None, cmp=None, reject_code="EMPTY")
    if "\x00" in raw:
        return PathCandidate(raw=raw, real=None, cmp=None, reject_code="NUL_BYTE")
    if raw.startswith("\\\\") or raw.startswith("//"):
        return PathCandidate(raw=raw, real=None, cmp=None, reject_code="UNC_OR_DEVICE_PREFIX")

    colon_positions = [i for i, ch in enumerate(raw) if ch == ":"]
    if any(i != 1 for i in colon_positions):
        return PathCandidate(raw=raw, real=None, cmp=None, reject_code="ADS")

    normalized_slashes = raw.replace("/", "\\")
    parts = [p for p in normalized_slashes.split("\\") if p != ""]
    for component in parts:
        code = _component_reject(component)
        if code is not None:
            return PathCandidate(raw=raw, real=None, cmp=None, reject_code=code)

    if os.path.isabs(normalized_slashes):
        joined = normalized_slashes
    else:
        joined = os.path.join(base, normalized_slashes)
    normed = os.path.normpath(joined)
    parent = os.path.dirname(normed)
    leaf = os.path.basename(normed)

    try:
        real_parent = os.path.realpath(parent) if parent else os.path.realpath(normed)
    except OSError:
        return PathCandidate(raw=raw, real=None, cmp=None, reject_code="UNRESOLVABLE_PARENT")

    real = os.path.join(real_parent, leaf) if leaf else real_parent
    cmp = os.path.normcase(real)
    return PathCandidate(raw=raw, real=real, cmp=cmp, reject_code=None)


_ROOT_MODES = frozenset({"rw", "ro", "forbidden"})


@dataclass(frozen=True, slots=True)
class RootRule:
    root_id: str
    real_path: str
    mode: str
    cmp_path: str = ""

    def __post_init__(self) -> None:
        if self.mode not in _ROOT_MODES:
            raise ValueError(f"invalid root mode {self.mode!r} for {self.root_id!r}")
        resolved = os.path.normcase(os.path.realpath(self.real_path))
        object.__setattr__(self, "cmp_path", resolved)


def _component_count(cmp_path: str) -> int:
    return len([p for p in cmp_path.split(os.sep) if p])


@dataclass(frozen=True, slots=True)
class RootSet:
    """Roots sorted longest-prefix-first, so a `forbidden` subtree nested inside
    an `rw` root is classified correctly."""

    entries: tuple[RootRule, ...]

    @classmethod
    def build(cls, rules) -> "RootSet":
        ordered = tuple(sorted(rules, key=lambda r: _component_count(r.cmp_path), reverse=True))
        return cls(entries=ordered)

    def classify(self, cmp_path: str) -> RootRule | None:
        cmp_parts = [p for p in cmp_path.split(os.sep) if p]
        for rule in self.entries:
            rule_parts = [p for p in rule.cmp_path.split(os.sep) if p]
            if len(rule_parts) <= len(cmp_parts) and cmp_parts[: len(rule_parts)] == rule_parts:
                return rule
        return None
