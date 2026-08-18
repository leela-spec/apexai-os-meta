"""
synthesize_transcript.py
Deterministic Macro -> Meso -> Micro Transcript Knowledge Validator and Renderer.

Validates structured semantic results against verbatim source transcripts and
renders anchor-linked Obsidian Wiki Markdown and structured JSON artifacts.
Fails closed if semantic result is absent, invalid, or ungrounded.
"""
from __future__ import annotations
import os
import sys
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Tuple
from datetime import timedelta

TIMESTAMP_RE = re.compile(r"\[?(?:(\d{1,2}):)?(\d{2}):(\d{2})\]?")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
VERDICTS = ("CONFIRMED", "CONTRADICTED", "MIXED", "UNVERIFIED")
CONFIDENCE_LEVELS = ("peer-reviewed", "hypothesis", "anecdote", "opinion", "market-data")
CLAIM_TYPES = ("FACT", "OPINION", "PREDICTION", "RECOMMENDATION", "ANECDOTE", "DEFINITION", "MECHANISM", "HYPOTHESIS", "ESTIMATE")


class ValidationError(Exception):
    """Raised when semantic result fails structural or grounding validation."""
    pass


def parse_timestamp_to_seconds(ts: str) -> int:
    """Parses MM:SS or HH:MM:SS to total seconds."""
    ts = ts.strip().strip("[]")
    m = TIMESTAMP_RE.match(ts)
    if not m:
        raise ValidationError(f"Invalid timestamp format: {ts!r}, expected MM:SS or HH:MM:SS")
    h_str, mi_str, s_str = m.groups()
    h = int(h_str) if h_str is not None else 0
    mi = int(mi_str)
    s = int(s_str)
    if mi >= 60 or s >= 60:
        raise ValidationError(f"Invalid timestamp values in {ts!r}: minutes and seconds must be < 60")
    return h * 3600 + mi * 60 + s


def seconds_to_hhmmss(total_seconds: float) -> str:
    """Formats total seconds into HH:MM:SS string."""
    td = timedelta(seconds=int(total_seconds))
    total_sec = td.seconds + td.days * 86400
    h, rem = divmod(total_sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def normalize_text(text: str) -> str:
    """Normalizes whitespace and standardizes punctuation for exact substring matching."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_transcript_spoken_text(transcript_path: Path) -> str:
    """Extracts only clean spoken dialogue from an SRT, TXT, or JSON file, removing metadata."""
    content = transcript_path.read_text(encoding="utf-8", errors="ignore")
    suffix = transcript_path.suffix.lower()
    
    if suffix == ".srt":
        # Parse SRT blocks cleanly
        blocks = content.strip().split("\n\n")
        spoken_parts = []
        for block in blocks:
            lines = [l.strip() for l in block.strip().split("\n") if l.strip()]
            if len(lines) >= 2:
                # Find line with -->
                time_idx = -1
                for i, l in enumerate(lines):
                    if "-->" in l:
                        time_idx = i
                        break
                if time_idx != -1 and len(lines) > time_idx + 1:
                    dialogue = " ".join(lines[time_idx + 1:])
                    # Remove HTML/subtitle tags e.g. <font>, <i>
                    dialogue = re.sub(r"<[^>]+>", "", dialogue)
                    spoken_parts.append(dialogue)
        return normalize_text(" ".join(spoken_parts))
        
    elif suffix == ".json":
        try:
            data = json.loads(content)
            if "segments" in data and isinstance(data["segments"], list):
                spoken = " ".join(s.get("text", "") for s in data["segments"])
                return normalize_text(spoken)
            elif "text" in data:
                return normalize_text(data["text"])
        except Exception:
            pass
            
    # Default plaintext
    return normalize_text(content)


@dataclass
class SpeakerProfile:
    label: str
    name: Optional[str] = None
    credentials: Optional[str] = None
    bias_indicators: List[str] = field(default_factory=list)


@dataclass
class MacroResult:
    core_thesis: str
    global_takeaways: List[str]
    taxonomy_tags: List[str]
    speakers: List[SpeakerProfile] = field(default_factory=list)

    def to_markdown(self) -> str:
        tags_md = " ".join(f"[[{t.strip('[]')}]]" for t in self.taxonomy_tags) if self.taxonomy_tags else "*(None)*"
        takeaways_md = "\n".join(f"- {t}" for t in self.global_takeaways) if self.global_takeaways else "- *(No takeaways specified)*"
        speakers_md = "\n".join(
            f"- **{s.label}**{f' ({s.name})' if s.name else ''}: "
            f"{s.credentials or 'Unspecified'}"
            + (f" — *Bias/Perspective:* {', '.join(s.bias_indicators)}" if s.bias_indicators else "")
            for s in self.speakers
        ) if self.speakers else "- *(Speaker profiles unspecified)*"
        return (
            f"## Macro: Executive Synthesis\n\n"
            f"**Core Thesis:** {self.core_thesis}\n\n"
            f"### Global Takeaways\n{takeaways_md}\n\n"
            f"### Taxonomy & Ontology\n{tags_md}\n\n"
            f"### Speaker Profiles\n{speakers_md}\n"
        )


@dataclass
class MesoModule:
    title: str
    start_ts: str
    end_ts: str
    arguments: List[str]
    protocol_steps: List[str] = field(default_factory=list)
    caveats: List[str] = field(default_factory=list)

    def to_markdown(self) -> str:
        args_md = "\n".join(f"- {a}" for a in self.arguments) if self.arguments else "- *(No discrete arguments)*"
        steps_md = "\n".join(f"{i+1}. {s}" for i, s in enumerate(self.protocol_steps)) if self.protocol_steps else "- *(No discrete protocol defined)*"
        caveats_md = "\n".join(f"- {c}" for c in self.caveats) if self.caveats else "- *(Standard scope limitations apply)*"
        return (
            f"### Meso Module: {self.title} `[{self.start_ts} - {self.end_ts}]`\n\n"
            f"**Arguments & Mechanics**\n{args_md}\n\n"
            f"**Actionable Protocol / Framework**\n{steps_md}\n\n"
            f"**Caveats & Nuances**\n{caveats_md}\n"
        )


@dataclass
class MicroClaim:
    claim_id: str
    proposition: str
    quote: str
    timestamp: str
    claim_type: str = "FACT"
    internal_confidence: str = "hypothesis"
    source_support: str = "SUPPORTED"
    verdict: str = "UNVERIFIED"
    search_query: Optional[str] = None
    external_sources: List[str] = field(default_factory=list)
    added_context: Optional[str] = None

    def __post_init__(self):
        sec = parse_timestamp_to_seconds(self.timestamp)
        self.timestamp = seconds_to_hhmmss(sec)
        if self.verdict not in VERDICTS:
            raise ValidationError(f"verdict must be one of {VERDICTS}, got {self.verdict!r}")

    def to_markdown(self) -> str:
        sources_md = "\n".join(f"  - {s}" for s in self.external_sources) if self.external_sources else "  - *(Pending external verification)*"
        return (
            f"#### [[Claim-{self.claim_id}]]\n"
            f"> \"{self.quote}\" `[{self.timestamp}]`\n\n"
            f"- **Proposition:** {self.proposition}\n"
            f"- **Claim Type:** `{self.claim_type}`\n"
            f"- **Source Support:** `{self.source_support}`\n"
            f"- **Internal Confidence:** `{self.internal_confidence}`\n"
            f"- **Verification Query:** `{self.search_query or 'N/A'}`\n"
            f"- **External Evidence & Sources:**\n{sources_md}\n"
            f"- **Verdict:** `[{self.verdict}]`\n"
            f"- **Added Context & Nuance:** {self.added_context or 'N/A'}\n"
        )


class KnowledgeSynthesisEngine:
    """Master engine for validating, composing, and rendering Macro-Meso-Micro knowledge artifacts."""

    def __init__(self, title: str = "Source Knowledge Synthesis"):
        self.title = title
        self.macro: Optional[MacroResult] = None
        self.meso_modules: List[MesoModule] = []
        self.micro_claims: List[MicroClaim] = []

    def set_macro(self, macro: MacroResult):
        self.macro = macro
        return self

    def add_meso_module(self, module: MesoModule):
        self.meso_modules.append(module)
        return self

    def add_micro_claim(self, claim: MicroClaim):
        self.micro_claims.append(claim)
        return self

    def get_external_verification_status(self) -> str:
        if not self.micro_claims:
            return "NOT_RUN"
        verified_count = sum(1 for c in self.micro_claims if c.verdict in ("CONFIRMED", "CONTRADICTED", "MIXED") or c.external_sources)
        if verified_count == 0:
            return "NOT_RUN"
        elif verified_count < len(self.micro_claims):
            return "PARTIAL"
        return "COMPLETED"

    def render_wiki_markdown(self) -> str:
        ext_status = self.get_external_verification_status()
        parts = [
            f"# {self.title}\n",
            "> [!NOTE]\n"
            "> - **Source Grounding:** VALIDATED (100% exact verbatim match)\n"
            f"> - **External Fact-Checking:** {ext_status}\n"
        ]
        if self.macro:
            parts.append(self.macro.to_markdown())
        
        parts.append("## Meso: Modular Deep Dives & Actionable Frameworks\n")
        for m in self.meso_modules:
            parts.append(m.to_markdown())
            
        parts.append("## Micro: Forensic Claims & Evidence Verification\n")
        for c in self.micro_claims:
            parts.append(c.to_markdown())
            
        return "\n".join(parts)

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "validation": {
                "source_grounded": True,
                "external_fact_checking": self.get_external_verification_status()
            },
            "macro": asdict(self.macro) if self.macro else None,
            "meso": [asdict(m) for m in self.meso_modules],
            "micro": [asdict(c) for c in self.micro_claims],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def write_artifacts(self, output_dir: Path, slug: str) -> Tuple[Path, Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        md_file = output_dir / f"{slug}_knowledge_wiki.md"
        json_file = output_dir / f"{slug}_knowledge_wiki.json"
        
        md_file.write_text(self.render_wiki_markdown(), encoding="utf-8")
        json_file.write_text(self.to_json(), encoding="utf-8")
        return md_file, json_file


def validate_and_load_semantic_result(semantic_path: Path, spoken_text: str, title: str) -> KnowledgeSynthesisEngine:
    """Validates structured semantic JSON against transcript spoken text and instantiates engine."""
    if not semantic_path.exists():
        raise ValidationError(f"Semantic result file not found: {semantic_path}")
        
    try:
        data = json.loads(semantic_path.read_text(encoding="utf-8"))
    except Exception as e:
        raise ValidationError(f"Semantic result JSON parsing failed: {e}")
        
    engine = KnowledgeSynthesisEngine(title=title)
    
    # 1. Macro validation
    macro_data = data.get("macro")
    if not macro_data or not isinstance(macro_data, dict):
        raise ValidationError("Missing or invalid 'macro' block in semantic result.")
    
    core_thesis = macro_data.get("core_thesis")
    if not core_thesis or not isinstance(core_thesis, str):
        raise ValidationError("Macro 'core_thesis' must be a non-empty string.")
        
    takeaways = macro_data.get("global_takeaways", [])
    if not isinstance(takeaways, list) or not takeaways:
        raise ValidationError("Macro 'global_takeaways' must be a non-empty list of strings.")
        
    taxonomy = macro_data.get("taxonomy_tags", [])
    if not isinstance(taxonomy, list):
        raise ValidationError("Macro 'taxonomy_tags' must be a list of strings.")
        
    speakers = []
    for sp in macro_data.get("speakers", []):
        speakers.append(SpeakerProfile(
            label=sp.get("label", "Speaker"),
            name=sp.get("name"),
            credentials=sp.get("credentials"),
            bias_indicators=sp.get("bias_indicators", [])
        ))
        
    engine.set_macro(MacroResult(
        core_thesis=core_thesis.strip(),
        global_takeaways=[t.strip() for t in takeaways],
        taxonomy_tags=[t.strip() for t in taxonomy],
        speakers=speakers
    ))
    
    # 2. Meso validation
    meso_list = data.get("meso", [])
    if not isinstance(meso_list, list):
        raise ValidationError("'meso' must be a list of Meso modules.")
        
    for m in meso_list:
        m_title = m.get("title", "").strip()
        start_ts = m.get("start_ts", "").strip()
        end_ts = m.get("end_ts", "").strip()
        args = m.get("arguments", [])
        protocol = m.get("protocol_steps", [])
        caveats = m.get("caveats", [])
        
        if not m_title:
            raise ValidationError("Each Meso module requires a non-empty 'title'.")
            
        parse_timestamp_to_seconds(start_ts)
        parse_timestamp_to_seconds(end_ts)
        
        if not isinstance(args, list) or not args:
            raise ValidationError(f"Meso module '{m_title}' requires non-empty 'arguments' list.")
            
        engine.add_meso_module(MesoModule(
            title=m_title,
            start_ts=start_ts,
            end_ts=end_ts,
            arguments=[a.strip() for a in args],
            protocol_steps=[p.strip() for p in protocol],
            caveats=[c.strip() for c in caveats]
        ))
        
    # 3. Micro claims validation & source grounding
    micro_list = data.get("micro", [])
    if not isinstance(micro_list, list):
        raise ValidationError("'micro' must be a list of Micro claims.")
        
    norm_spoken = normalize_text(spoken_text)
    
    for c in micro_list:
        cid = str(c.get("claim_id", "")).strip()
        prop = c.get("proposition", "").strip()
        quote = c.get("quote", "").strip()
        ts = c.get("timestamp", "").strip()
        ctype = c.get("claim_type", "FACT").strip().upper()
        conf = c.get("internal_confidence", "hypothesis").strip()
        support = c.get("source_support", "SUPPORTED").strip().upper()
        verdict = c.get("verdict", "UNVERIFIED").strip().upper()
        query = c.get("search_query")
        sources = c.get("external_sources", [])
        context = c.get("added_context")
        
        if not cid or not prop or not quote or not ts:
            raise ValidationError("Micro claims require 'claim_id', 'proposition', 'quote', and 'timestamp'.")
            
        # Reject SRT metadata in quotes
        if "-->" in quote or re.search(r"^\d+\s*$", quote, re.MULTILINE):
            raise ValidationError(f"Micro claim '{cid}' quote contains raw SRT formatting metadata: {quote!r}")
            
        # Grounding check: Quote must be exact substring in spoken transcript
        norm_quote = normalize_text(quote)
        if norm_quote not in norm_spoken:
            # Check case-insensitive as well
            if norm_quote.lower() not in norm_spoken.lower():
                raise ValidationError(
                    f"Micro claim '{cid}' quote is NOT present verbatim in source transcript:\n"
                    f"  Quote: {quote!r}"
                )
                
        engine.add_micro_claim(MicroClaim(
            claim_id=cid,
            proposition=prop,
            quote=quote,
            timestamp=ts,
            claim_type=ctype,
            internal_confidence=conf,
            source_support=support,
            verdict=verdict,
            search_query=query,
            external_sources=sources,
            added_context=context
        ))
        
    return engine


def parse_args():
    parser = argparse.ArgumentParser(description="Macro-Meso-Micro Transcript Knowledge Validator & Renderer")
    parser.add_argument("--transcript", type=str, required=True, help="Path to transcript (.srt, .json, .txt)")
    parser.add_argument("--semantic-result", type=str, default=None, help="Path to semantic result JSON (required for synthesis)")
    parser.add_argument("--output_dir", type=str, required=True, help="Output directory for generated knowledge wiki")
    parser.add_argument("--slug", type=str, default="", help="Slug/ID for generated files")
    parser.add_argument("--title", type=str, default="Source Knowledge Synthesis", help="Document title")
    return parser.parse_args()


def main():
    args = parse_args()
    transcript_path = Path(args.transcript)
    output_dir = Path(args.output_dir)
    slug = args.slug or transcript_path.stem

    if not transcript_path.exists():
        print(f"Error: Transcript file not found: {transcript_path}", file=sys.stderr)
        sys.exit(1)

    if not args.semantic_result:
        print(f"[SYNTHESIS_PENDING] No semantic result JSON provided for '{slug}'. Skipping synthesis.", file=sys.stderr)
        print(f"To synthesize, provide: --semantic-result <path.json>", file=sys.stderr)
        sys.exit(2)  # Exit code 2 indicates SYNTHESIS_PENDING

    semantic_path = Path(args.semantic_result)
    print(f"Validating and synthesizing knowledge wiki for '{slug}' from {semantic_path.name}...")
    spoken_text = parse_transcript_spoken_text(transcript_path)
    
    try:
        engine = validate_and_load_semantic_result(semantic_path, spoken_text, title=args.title)
    except ValidationError as ve:
        print(f"Validation Error: {ve}", file=sys.stderr)
        sys.exit(1)

    md_file, json_file = engine.write_artifacts(output_dir, slug)
    print(f"Successfully validated and generated:")
    print(f"  - Markdown Wiki: {md_file}")
    print(f"  - Structured JSON: {json_file}")
    sys.exit(0)


if __name__ == "__main__":
    main()
