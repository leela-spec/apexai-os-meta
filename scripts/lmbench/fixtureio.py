"""Fixture loading and the answer-hiding discipline. Stdlib only.

Positive allow-list, never a deny-list: only `seed/` and `untrusted/` are ever
materialized into a trial workspace, and only `packet.md`'s bytes ever reach
the model's prompt. A deny-list ("skip anything under a directory named
answers") would eventually leak via a renamed directory or a symlink; an
allow-list structurally cannot, because nothing outside the two named
directories is ever even considered.

Two loaders, two return types. `load_public()` returns a `PublicFixture` whose
field set has no member capable of holding answer content -- there is no
`expected_patch` field to accidentally serialize into a prompt. `load_oracle()`
returns an `OracleFixture` and is the only function that reads `answers/`.
Nothing in this module imports the graders that consume `OracleFixture` (and
nothing actor-facing imports this module's oracle half) -- that separation is
enforced by `tests/test_architecture.py` alongside the write/spawn rule.

Fixture specs (`fixture.md`) are parsed with `scripts.fee.artifacts`, not a
bespoke YAML parser -- reusing a hardened, already-tested reader for a format
this package doesn't otherwise need to maintain.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path

from scripts.fee import artifacts

from .errors import FixtureError

ACTOR_MATERIALIZE_DIRS = ("seed", "untrusted")
ACTOR_PROMPT_FILE = "packet.md"
ORACLE_SPEC_FILE = "fixture.md"
ORACLE_DIR = "answers"

_CANARY_RE = re.compile(r"canary:\s*(\S+)")


@dataclass(frozen=True, slots=True)
class PublicFixture:
    """The actor's entire view of a fixture. No field here can hold answer
    content -- there is nothing to accidentally leak by serializing this object."""

    fixture_id: str
    fixture_dir: Path
    packet_text: str
    materialize_dirs: tuple[Path, ...]


@dataclass(frozen=True, slots=True)
class OracleFixture:
    fixture_id: str
    spec: dict = field(default_factory=dict)
    answers_dir: Path | None = None
    canaries: frozenset = frozenset()


def list_fixture_ids(fixtures_root: Path) -> tuple[str, ...]:
    if not fixtures_root.is_dir():
        return ()
    return tuple(
        sorted(p.name for p in fixtures_root.iterdir() if p.is_dir() and not p.name.startswith("."))
    )


def load_public(fixtures_root: Path, fixture_id: str) -> PublicFixture:
    fixture_dir = fixtures_root / fixture_id
    packet_path = fixture_dir / ACTOR_PROMPT_FILE
    if not packet_path.is_file():
        raise FixtureError(f"fixture {fixture_id!r}: missing {ACTOR_PROMPT_FILE}")
    packet_text = packet_path.read_text(encoding="utf-8")
    materialize_dirs = tuple(
        fixture_dir / name
        for name in ACTOR_MATERIALIZE_DIRS
        if (fixture_dir / name).is_dir()
    )
    return PublicFixture(
        fixture_id=fixture_id,
        fixture_dir=fixture_dir,
        packet_text=packet_text,
        materialize_dirs=materialize_dirs,
    )


def load_oracle(fixtures_root: Path, fixture_id: str) -> OracleFixture:
    fixture_dir = fixtures_root / fixture_id
    spec: dict = {}
    spec_path = fixture_dir / ORACLE_SPEC_FILE
    if spec_path.is_file():
        text = spec_path.read_text(encoding="utf-8")
        for block in artifacts.extract_yaml_blocks(text):
            spec.update(artifacts.parse_block_yaml(block, source=str(spec_path)))
    answers_dir = fixture_dir / ORACLE_DIR
    answers_dir = answers_dir if answers_dir.is_dir() else None
    canaries = _collect_canaries(answers_dir) if answers_dir is not None else frozenset()
    return OracleFixture(fixture_id=fixture_id, spec=spec, answers_dir=answers_dir, canaries=canaries)


def _collect_canaries(answers_dir: Path) -> frozenset:
    tokens = set()
    for path in answers_dir.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        tokens.update(_CANARY_RE.findall(text))
    return frozenset(tokens)


def materialize(public: PublicFixture, dest: Path) -> Path:
    """Copy ONLY `public.materialize_dirs` into `dest`. Takes a `PublicFixture`,
    not a fixture_id or a raw path -- a caller cannot pass the unfiltered
    fixture directory (which would include `answers/`) instead of the
    pre-filtered public view `load_public` already produced.

    Merges the *contents* of `seed/` and `untrusted/` directly into `dest`
    (a fixture's `seed/repo/...` becomes the trial's `repo/...`) rather than
    preserving those directory names in the trial workspace -- the actor's
    task-relative paths should describe the task ("repo/", "review-set/"),
    not this package's internal answer-hiding layout."""
    dest.mkdir(parents=True, exist_ok=True)
    for src_dir in public.materialize_dirs:
        _copy_tree_no_symlinks(src_dir, dest)
    return dest


def _copy_tree_no_symlinks(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    for entry in sorted(src.iterdir()):
        if entry.is_symlink():
            raise FixtureError(f"refusing to materialize a symlink: {entry}")
        target = dst / entry.name
        if entry.is_dir():
            _copy_tree_no_symlinks(entry, target)
        else:
            target.write_bytes(entry.read_bytes())


def scan_for_canaries(text: str, canaries: frozenset) -> tuple[str, ...]:
    """Byte/text-level scan used by tests and by the runner as a pre-flight
    check before the first model call -- returns which canaries (if any) were
    found, so a leak fails loudly and specifically rather than as a bare
    boolean."""
    return tuple(sorted(token for token in canaries if token and token in text))


def answer_file_hashes(oracle: OracleFixture) -> frozenset:
    """SHA-256 of every file under answers/ -- used to catch a leak even if a
    canary token itself were stripped: if a materialized file's hash matches
    an answers/ file's hash, the same bytes ended up in both places."""
    if oracle.answers_dir is None:
        return frozenset()
    hashes = set()
    for path in oracle.answers_dir.rglob("*"):
        if path.is_file():
            hashes.add(hashlib.sha256(path.read_bytes()).hexdigest())
    return frozenset(hashes)


__all__ = [
    "ACTOR_MATERIALIZE_DIRS",
    "ACTOR_PROMPT_FILE",
    "ORACLE_SPEC_FILE",
    "ORACLE_DIR",
    "PublicFixture",
    "OracleFixture",
    "list_fixture_ids",
    "load_public",
    "load_oracle",
    "materialize",
    "scan_for_canaries",
    "answer_file_hashes",
]
