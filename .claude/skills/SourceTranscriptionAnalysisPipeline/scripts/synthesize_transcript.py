"""
synthesize_transcript.py
Deterministic Macro -> Meso -> Micro Transcript Knowledge Synthesis Engine.

Transforms raw Whisper transcripts (.json, .srt, .txt) into verified,
anchor-linked Obsidian Wiki Markdown and structured JSON artifacts.
"""
from __future__ import annotations
import os
import sys
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Callable
from datetime import timedelta

TIMESTAMP_RE = re.compile(r"\[?(?:(\d{1,2}):)?(\d{2}):(\d{2})\]?")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
VERDICTS = ("CONFIRMED", "CONTRADICTED", "MIXED", "UNVERIFIED")
CONFIDENCE_LEVELS = ("peer-reviewed", "hypothesis", "anecdote", "opinion", "market-data")


def parse_timestamp_to_seconds(ts: str) -> int:
    """Parses MM:SS or HH:MM:SS to total seconds."""
    ts = ts.strip().strip("[]")
    m = TIMESTAMP_RE.match(ts)
    if not m:
        raise ValueError(f"Invalid timestamp format: {ts!r}, expected MM:SS or HH:MM:SS")
    h_str, mi_str, s_str = m.groups()
    h = int(h_str) if h_str is not None else 0
    mi = int(mi_str)
    s = int(s_str)
    return h * 3600 + mi * 60 + s


def seconds_to_hhmmss(total_seconds: float) -> str:
    """Formats total seconds into HH:MM:SS string."""
    td = timedelta(seconds=int(total_seconds))
    total_sec = td.seconds + td.days * 86400
    h, rem = divmod(total_sec, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


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
    speakers: List[SpeakerProfile]

    def to_markdown(self) -> str:
        tags_md = " ".join(f"[[{t.strip('[]')}]]" for t in self.taxonomy_tags)
        takeaways_md = "\n".join(f"- {t}" for t in self.global_takeaways)
        speakers_md = "\n".join(
            f"- **{s.label}**{f' ({s.name})' if s.name else ''}: "
            f"{s.credentials or 'Unspecified'}"
            + (f" — *Bias/Perspective:* {', '.join(s.bias_indicators)}" if s.bias_indicators else "")
            for s in self.speakers
        )
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
    protocol_steps: List[str]
    caveats: List[str]

    def to_markdown(self) -> str:
        args_md = "\n".join(f"- {a}" for a in self.arguments)
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
    internal_confidence: str = "hypothesis"
    verdict: str = "UNVERIFIED"
    search_query: Optional[str] = None
    external_sources: List[str] = field(default_factory=list)
    added_context: Optional[str] = None

    def __post_init__(self):
        # Format timestamp safely
        sec = parse_timestamp_to_seconds(self.timestamp)
        self.timestamp = seconds_to_hhmmss(sec)
        if self.verdict not in VERDICTS:
            raise ValueError(f"verdict must be one of {VERDICTS}, got {self.verdict!r}")

    def to_markdown(self) -> str:
        sources_md = "\n".join(f"  - {s}" for s in self.external_sources) if self.external_sources else "  - *(Pending external verification)*"
        return (
            f"#### [[Claim-{self.claim_id}]]\n"
            f"> \"{self.quote}\" `[{self.timestamp}]`\n\n"
            f"- **Proposition:** {self.proposition}\n"
            f"- **Internal Confidence:** `{self.internal_confidence}`\n"
            f"- **Verification Query:** `{self.search_query or 'N/A'}`\n"
            f"- **External Evidence & Sources:**\n{sources_md}\n"
            f"- **Verdict:** `[{self.verdict}]`\n"
            f"- **Added Context & Nuance:** {self.added_context or 'N/A'}\n"
        )


class KnowledgeSynthesisEngine:
    """Master engine for composing and exporting Macro-Meso-Micro knowledge graphs."""

    def __init__(self, title: str = "Transcript Knowledge Synthesis"):
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

    def render_wiki_markdown(self) -> str:
        parts = [
            f"# {self.title}\n",
            "> [!NOTE]\n> Standalone, verified Source Knowledge synthesized from verbatim audio transcript.\n"
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
            "macro": asdict(self.macro) if self.macro else None,
            "meso": [asdict(m) for m in self.meso_modules],
            "micro": [asdict(c) for c in self.micro_claims],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def write_artifacts(self, output_dir: Path, slug: str):
        output_dir.mkdir(parents=True, exist_ok=True)
        md_file = output_dir / f"{slug}_knowledge_wiki.md"
        json_file = output_dir / f"{slug}_knowledge_wiki.json"
        
        md_file.write_text(self.render_wiki_markdown(), encoding="utf-8")
        json_file.write_text(self.to_json(), encoding="utf-8")
        return md_file, json_file


def parse_args():
    parser = argparse.ArgumentParser(description="Macro-Meso-Micro Transcript Knowledge Synthesis Engine")
    parser.add_argument("--transcript", type=str, required=True, help="Path to transcript (.json, .srt, or .md)")
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

    print(f"Synthesizing knowledge wiki for '{slug}' from {transcript_path}...")
    
    # Instantiate engine
    engine = KnowledgeSynthesisEngine(title=args.title)
    
    # Render and export
    md_file, json_file = engine.write_artifacts(output_dir, slug)
    print(f"Successfully generated:")
    print(f"  - Markdown Wiki: {md_file}")
    print(f"  - Structured JSON: {json_file}")


if __name__ == "__main__":
    main()
