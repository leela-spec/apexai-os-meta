"""
transcript_engine.py
Deterministic Macro -> Meso -> Micro Knowledge Extraction Engine
Zero-cloud-API-token architecture: LLM calls are injected via a callable,
so the same skeleton runs against local models (Ollama, llama.cpp, LM Studio)
or remote APIs -- the engine itself makes no network calls.

Dependencies: standard library only (re, json, dataclasses, pathlib, datetime).
"""
from __future__ import annotations
import re
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Callable, Optional
from datetime import timedelta

TIMESTAMP_RE = re.compile(r"\[(\d{2}):(\d{2}):(\d{2})\]")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

VERDICTS = ("CONFIRMED", "CONTRADICTED", "MIXED", "UNVERIFIED")


def hhmmss_to_seconds(ts: str) -> int:
    m = TIMESTAMP_RE.match(f"[{ts}]") if not ts.startswith("[") else TIMESTAMP_RE.match(ts)
    if not m:
        raise ValueError(f"Invalid timestamp format: {ts!r}, expected HH:MM:SS")
    h, mi, s = map(int, m.groups())
    return h * 3600 + mi * 60 + s


def seconds_to_hhmmss(total_seconds: float) -> str:
    td = timedelta(seconds=int(total_seconds))
    h, rem = divmod(td.seconds + td.days * 86400, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


@dataclass
class SpeakerProfile:
    label: str
    name: Optional[str] = None
    credentials: Optional[str] = None
    bias_indicators: list = field(default_factory=list)


@dataclass
class MacroResult:
    core_thesis: str
    global_takeaways: list
    taxonomy_tags: list  # e.g. ["[[AI Orchestration]]", "[[Prompt Engineering]]"]
    speakers: list  # list[SpeakerProfile]

    def to_markdown(self) -> str:
        tags = " ".join(self.taxonomy_tags)
        takeaways = "\n".join(f"- {t}" for t in self.global_takeaways)
        speakers_md = "\n".join(
            f"- **{s.label}**{f' ({s.name})' if s.name else ''}: "
            f"{s.credentials or 'unspecified'}"
            + (f" — bias: {', '.join(s.bias_indicators)}" if s.bias_indicators else "")
            for s in self.speakers
        )
        return (
            f"## Macro: Executive Synthesis\n\n"
            f"**Core Thesis:** {self.core_thesis}\n\n"
            f"### Global Takeaways\n{takeaways}\n\n"
            f"### Taxonomy\n{tags}\n\n"
            f"### Speaker Ontology\n{speakers_md}\n"
        )


@dataclass
class MesoModule:
    title: str
    start_ts: str  # HH:MM:SS
    end_ts: str
    arguments: list
    protocol_steps: list
    caveats: list

    def to_markdown(self) -> str:
        args_md = "\n".join(f"- {a}" for a in self.arguments)
        steps_md = "\n".join(f"{i+1}. {s}" for i, s in enumerate(self.protocol_steps))
        caveats_md = "\n".join(f"- {c}" for c in self.caveats)
        return (
            f"### Meso Module: {self.title} `[{self.start_ts} - {self.end_ts}]`\n\n"
            f"**Arguments**\n{args_md}\n\n"
            f"**Protocol / Mechanism**\n{steps_md}\n\n"
            f"**Caveats**\n{caveats_md}\n"
        )


@dataclass
class MicroClaim:
    claim_id: str
    proposition: str
    quote: str
    timestamp: str  # HH:MM:SS
    internal_confidence: str  # "peer-reviewed" | "hypothesis" | "anecdote" | "opinion"
    verdict: str = "UNVERIFIED"
    search_query: Optional[str] = None
    external_sources: list = field(default_factory=list)
    added_context: Optional[str] = None

    def __post_init__(self):
        hhmmss_to_seconds(self.timestamp)  # validates format, raises if malformed
        if self.verdict not in VERDICTS:
            raise ValueError(f"verdict must be one of {VERDICTS}, got {self.verdict!r}")

    def to_markdown(self) -> str:
        sources_md = "\n".join(f"  - {s}" for s in self.external_sources) or "  - (none)"
        return (
            f"#### [[Claim-{self.claim_id}]]\n"
            f"> \"{self.quote}\" `[{self.timestamp}]`\n\n"
            f"- **Proposition:** {self.proposition}\n"
            f"- **Internal confidence:** {self.internal_confidence}\n"
            f"- **Search query:** {self.search_query or 'n/a'}\n"
            f"- **Sources:**\n{sources_md}\n"
            f"- **Verdict:** `[{self.verdict}]`\n"
            f"- **Added context:** {self.added_context or 'n/a'}\n"
        )


class VerificationHook:
    """
    Pluggable verification interface (KR2 automated search-verification hook).
    Inject any callable(query: str) -> list[dict] that returns web results;
    the engine stays free of hardcoded API dependencies.
    """
    def __init__(self, search_fn: Callable[[str], list]):
        self.search_fn = search_fn

    def verify(self, claim: MicroClaim) -> MicroClaim:
        if not claim.search_query:
            claim.search_query = claim.proposition
        results = self.search_fn(claim.search_query)
        claim.external_sources = [r.get("url", "") for r in results][:3]
        return claim


class KnowledgeEngine:
    def __init__(self, verification_hook: Optional[VerificationHook] = None):
        self.verification_hook = verification_hook
        self.macro: Optional[MacroResult] = None
        self.meso: list = []
        self.micro: list = []

    def set_macro(self, macro: MacroResult):
        self.macro = macro
        return self

    def add_meso_module(self, module: MesoModule):
        self.meso.append(module)
        return self

    def add_micro_claim(self, claim: MicroClaim, auto_verify: bool = False):
        if auto_verify and self.verification_hook:
            claim = self.verification_hook.verify(claim)
        self.micro.append(claim)
        return self

    def render_wiki_markdown(self, title: str) -> str:
        parts = [f"# {title}\n"]
        if self.macro:
            parts.append(self.macro.to_markdown())
        parts.append("## Meso: Modular Deep Dives\n")
        for m in self.meso:
            parts.append(m.to_markdown())
        parts.append("## Micro: Atomic Claims & Verification\n")
        for c in self.micro:
            parts.append(c.to_markdown())
        return "\n".join(parts)

    def to_json(self) -> str:
        return json.dumps({
            "macro": asdict(self.macro) if self.macro else None,
            "meso": [asdict(m) for m in self.meso],
            "micro": [asdict(c) for c in self.micro],
        }, indent=2, ensure_ascii=False)

    def write(self, out_dir: str, slug: str, title: str):
        out = Path(out_dir)
        out.mkdir(parents=True, exist_ok=True)
        (out / f"{slug}.md").write_text(self.render_wiki_markdown(title), encoding="utf-8")
        (out / f"{slug}.json").write_text(self.to_json(), encoding="utf-8")
