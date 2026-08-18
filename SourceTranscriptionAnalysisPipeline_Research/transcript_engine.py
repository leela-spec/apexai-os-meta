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
from typing import Callable, Optional, List, Dict
from datetime import timedelta

TIMESTAMP_RE = re.compile(r"\[?(?:(\d{1,2}):)?(\d{2}):(\d{2})\]?")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

VERDICTS = ("CONFIRMED", "CONTRADICTED", "MIXED", "UNVERIFIED")
SOURCE_SUPPORTS = ("SUPPORTED", "PARTIAL", "AMBIGUOUS", "UNSUPPORTED")
CLAIM_TYPES = ("FACT", "OPINION", "PREDICTION", "RECOMMENDATION", "ANECDOTE", "DEFINITION", "MECHANISM", "HYPOTHESIS", "ESTIMATE")
CONFIDENCE_LEVELS = ("peer-reviewed", "hypothesis", "anecdote", "opinion", "market-data")


class GroundingError(Exception):
    """Raised when quote grounding or structural validation fails."""
    pass


def hhmmss_to_seconds(ts: str) -> int:
    ts = ts.strip().strip("[]")
    m = TIMESTAMP_RE.match(ts)
    if not m:
        raise ValueError(f"Invalid timestamp format: {ts!r}, expected MM:SS or HH:MM:SS")
    h_str, mi_str, s_str = m.groups()
    h = int(h_str) if h_str is not None else 0
    mi = int(mi_str)
    s = int(s_str)
    if mi >= 60 or s >= 60:
        raise ValueError(f"Invalid timestamp values in {ts!r}: minutes and seconds must be < 60")
    return h * 3600 + mi * 60 + s


def seconds_to_hhmmss(total_seconds: float) -> str:
    td = timedelta(seconds=int(total_seconds))
    h, rem = divmod(td.seconds + td.days * 86400, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_srt_spoken_text(srt_path: Path) -> str:
    """Deterministically extracts only spoken text from SRT, stripping indexes, timestamps, and tags."""
    if not srt_path.exists():
        return ""
    content = srt_path.read_text(encoding="utf-8", errors="ignore")
    blocks = content.strip().split("\n\n")
    spoken_parts = []
    for block in blocks:
        lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
        if len(lines) >= 2:
            time_idx = -1
            for i, l in enumerate(lines):
                if "-->" in l:
                    time_idx = i
                    break
            if time_idx != -1 and len(lines) > time_idx + 1:
                dialogue = " ".join(lines[time_idx + 1:])
                dialogue = re.sub(r"<[^>]+>", "", dialogue)
                spoken_parts.append(dialogue)
    return normalize_text(" ".join(spoken_parts))


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
    speakers: list = field(default_factory=list)  # list[SpeakerProfile]

    def to_markdown(self) -> str:
        tags = " ".join(self.taxonomy_tags) if self.taxonomy_tags else "*(None)*"
        takeaways = "\n".join(f"- {t}" for t in self.global_takeaways) if self.global_takeaways else "- *(None)*"
        speakers_md = "\n".join(
            f"- **{s.label}**{f' ({s.name})' if s.name else ''}: "
            f"{s.credentials or 'unspecified'}"
            + (f" — bias: {', '.join(s.bias_indicators)}" if s.bias_indicators else "")
            for s in self.speakers
        ) if self.speakers else "- *(Unspecified)*"
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
    start_ts: str  # HH:MM:SS or MM:SS
    end_ts: str
    arguments: list
    protocol_steps: list = field(default_factory=list)
    caveats: list = field(default_factory=list)

    def to_markdown(self) -> str:
        args_md = "\n".join(f"- {a}" for a in self.arguments) if self.arguments else "- *(No arguments)*"
        steps_md = "\n".join(f"{i+1}. {s}" for i, s in enumerate(self.protocol_steps)) if self.protocol_steps else "- *(No discrete protocol steps defined)*"
        caveats_md = "\n".join(f"- {c}" for c in self.caveats) if self.caveats else "- *(Standard scope limitations)*"
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
    timestamp: str  # HH:MM:SS or MM:SS
    claim_type: str = "FACT"
    internal_confidence: str = "hypothesis"
    source_support: str = "SUPPORTED"
    verdict: str = "UNVERIFIED"
    source_segment_ids: list = field(default_factory=list)
    source_start: str = ""
    source_end: str = ""
    search_query: Optional[str] = None
    external_sources: list = field(default_factory=list)
    added_context: Optional[str] = None

    def __post_init__(self):
        sec = hhmmss_to_seconds(self.timestamp)
        self.timestamp = seconds_to_hhmmss(sec)
        if self.verdict not in VERDICTS:
            raise ValueError(f"verdict must be one of {VERDICTS}, got {self.verdict!r}")
        if self.claim_type not in CLAIM_TYPES:
            raise ValueError(f"claim_type must be one of {CLAIM_TYPES}, got {self.claim_type!r}")
        if self.source_support not in SOURCE_SUPPORTS:
            raise ValueError(f"source_support must be one of {SOURCE_SUPPORTS}, got {self.source_support!r}")

    def to_markdown(self) -> str:
        sources_md = "\n".join(f"  - {s}" for s in self.external_sources) or "  - (none)"
        return (
            f"#### [[Claim-{self.claim_id}]]\n"
            f"> \"{self.quote}\" `[{self.timestamp}]`\n\n"
            f"- **Proposition:** {self.proposition}\n"
            f"- **Claim Type:** `{self.claim_type}`\n"
            f"- **Source Support:** `{self.source_support}`\n"
            f"- **Internal confidence:** {self.internal_confidence}\n"
            f"- **Search query:** {self.search_query or 'n/a'}\n"
            f"- **Sources:**\n{sources_md}\n"
            f"- **Verdict:** `[{self.verdict}]`\n"
            f"- **Added context:** {self.added_context or 'n/a'}\n"
        )


class VerificationHook:
    """
    Pluggable verification interface.
    Inject any callable(query: str) -> list[dict] that returns web results;
    Setting URLs leaves external_verdict = UNVERIFIED unless an evaluator confirms/contradicts.
    """
    def __init__(self, search_fn: Callable[[str], list]):
        self.search_fn = search_fn

    def verify(self, claim: MicroClaim) -> MicroClaim:
        if not claim.search_query:
            claim.search_query = claim.proposition
        results = self.search_fn(claim.search_query)
        claim.external_sources = [r.get("url", "") for r in results if r.get("url")][:3]
        # Strict rule: URL retrieval alone leaves verdict as UNVERIFIED
        claim.verdict = "UNVERIFIED"
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

    @classmethod
    def from_semantic_result(cls, data: dict, spoken_text: Optional[str] = None) -> KnowledgeEngine:
        """Instantiates and strictly validates a KnowledgeEngine from structured dictionary data."""
        engine = cls()
        
        # 1. Macro
        macro_dict = data.get("macro")
        if not macro_dict or not isinstance(macro_dict, dict):
            raise GroundingError("Missing or invalid 'macro' block.")
            
        speakers = []
        for sp in macro_dict.get("speakers", []):
            speakers.append(SpeakerProfile(
                label=sp.get("label", "Speaker"),
                name=sp.get("name"),
                credentials=sp.get("credentials"),
                bias_indicators=sp.get("bias_indicators", [])
            ))
            
        engine.set_macro(MacroResult(
            core_thesis=macro_dict.get("core_thesis", "").strip(),
            global_takeaways=[t.strip() for t in macro_dict.get("global_takeaways", [])],
            taxonomy_tags=[t.strip() for t in macro_dict.get("taxonomy_tags", [])],
            speakers=speakers
        ))
        
        # 2. Meso
        for m in data.get("meso", []):
            engine.add_meso_module(MesoModule(
                title=m.get("title", "").strip(),
                start_ts=m.get("start_ts", "").strip(),
                end_ts=m.get("end_ts", "").strip(),
                arguments=[a.strip() for a in m.get("arguments", [])],
                protocol_steps=[p.strip() for p in m.get("protocol_steps", [])],
                caveats=[c.strip() for c in m.get("caveats", [])]
            ))
            
        # 3. Micro
        norm_spoken = normalize_text(spoken_text) if spoken_text else None
        for c in data.get("micro", []):
            quote = c.get("quote", "").strip()
            cid = str(c.get("claim_id", "")).strip()
            
            # Reject raw SRT formatting metadata
            if "-->" in quote or re.search(r"^\d+\s*$", quote, re.MULTILINE):
                raise GroundingError(f"Claim '{cid}' quote contains raw SRT formatting metadata: {quote!r}")
                
            # Exact verbatim grounding check if spoken_text supplied
            if norm_spoken is not None:
                norm_quote = normalize_text(quote)
                if norm_quote not in norm_spoken and norm_quote.lower() not in norm_spoken.lower():
                    raise GroundingError(f"Claim '{cid}' quote is NOT present verbatim in source transcript: {quote!r}")
                    
            engine.add_micro_claim(MicroClaim(
                claim_id=cid,
                proposition=c.get("proposition", "").strip(),
                quote=quote,
                timestamp=c.get("timestamp", "").strip(),
                claim_type=c.get("claim_type", "FACT").strip().upper(),
                internal_confidence=c.get("internal_confidence", "hypothesis").strip(),
                source_support=c.get("source_support", "SUPPORTED").strip().upper(),
                verdict=c.get("verdict", "UNVERIFIED").strip().upper(),
                source_segment_ids=c.get("source_segment_ids", []),
                source_start=c.get("source_start", ""),
                source_end=c.get("source_end", ""),
                search_query=c.get("search_query"),
                external_sources=c.get("external_sources", []),
                added_context=c.get("added_context")
            ))
            
        return engine

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
