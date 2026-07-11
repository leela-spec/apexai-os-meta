[RESEARCH_BLOCK v1.0]
TRIGGER: task is synthesis, analysis, or knowledge output (not file write)

FORMAT:
```
# RESEARCH: {TOPIC}
# SCOPE: {bounded question only}
# FORMAT: [bullets | table | numbered | prose]
# DEPTH: [surface | standard | exhaustive]
---
{output — format as specified, nothing else}
```

RULES:
- No preamble before block
- No "here is what I found" text
- No recommendations unless OUTPUT_TYPE includes "recommendations"
- If depth=exhaustive and content exceeds limit: use SPLIT_SIGNAL
- Cite sources inline as [SOURCE: name/url] not footnotes
