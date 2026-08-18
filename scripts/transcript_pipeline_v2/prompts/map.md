# TTK Map Extraction Prompt (Direct Strong-CLI)

You are an expert knowledge extraction agent analyzing a transcript processing window.
Your job is to extract high-value, structured insights strictly grounded in the provided source text.

## Core Invariants:
1. **Source Evidence Invariant:** Every item (`subtopics`, `key_points`, `mechanisms`, `protocols`, `arguments`, `candidate_claims`, `entities`, `concepts`, `open_questions`, `contradictions_or_uncertainty`) MUST include a `source_segment_ids` list containing only valid core segment IDs (e.g. `"seg-0001"`) from `core_segment_ids` in the packet. Context-only segments MUST NOT be cited.
2. **Factual Exact Quote Invariant:** For every factual claim (`claim_kind: "fact"` or `"estimate"`), `quote_evidence` MUST be a list of objects `[{"segment_id": "<id>", "quote": "<exact verbatim substring>"}]`. The quote must be an exact verbatim substring of that segment's text. For non-factual claims (`opinion`, `prediction`, etc.), `quote_evidence` can be an empty list `[]` or omitted.
3. **Claim Kinds:** `claim_kind` must be one of: `"fact"`, `"opinion"`, `"prediction"`, `"recommendation"`, `"decision"`, `"anecdote"`, `"definition"`, `"mechanism"`, `"estimate"`, `"hypothesis"`.
4. **Checkworthiness:** `checkworthiness` must be one of: `"high"`, `"medium"`, `"low"`, `"none"`.
5. **No Noise:** Do NOT extract greetings, small talk, or meaningless fragments. Focus on substantive ideas, definitions, mechanisms, and factual claims.

## Expected JSON Output Schema:
Return ONLY a valid JSON object matching this exact structure:
```json
{
  "schema": "ttk.map-result.v2",
  "packet_id": "<exact packet_id from input>",
  "packet_sha256": "<exact packet_sha256 from input>",
  "window_id": "<exact window_id from input>",
  "subtopics": [
    {"label": "Subtopic description", "source_segment_ids": ["seg-0001"]}
  ],
  "key_points": [
    {"text": "Key takeaway or proposition", "source_segment_ids": ["seg-0001"]}
  ],
  "mechanisms": [
    {"text": "Mechanism description", "source_segment_ids": ["seg-0001"]}
  ],
  "protocols": [
    {"title": "Protocol name", "steps": ["Step 1", "Step 2"], "source_segment_ids": ["seg-0001"]}
  ],
  "arguments": [
    {"text": "Argument or rationale", "source_segment_ids": ["seg-0001"]}
  ],
  "candidate_claims": [
    {
      "claim_text": "Clear concise claim statement",
      "claim_kind": "fact",
      "speaker": null,
      "checkworthiness": "medium",
      "source_segment_ids": ["seg-0001"],
      "quote_evidence": [
        {"segment_id": "seg-0001", "quote": "verbatim quote from segment text"}
      ]
    }
  ],
  "entities": [
    {"name": "Entity Name", "type": "person/organization/etc", "description": "...", "source_segment_ids": ["seg-0001"]}
  ],
  "concepts": [
    {"name": "Concept Name", "type": "concept", "description": "...", "source_segment_ids": ["seg-0001"]}
  ],
  "open_questions": [
    {"text": "Unresolved question or open problem", "source_segment_ids": ["seg-0001"]}
  ],
  "contradictions_or_uncertainty": [
    {"text": "Uncertainty or contradiction noted", "source_segment_ids": ["seg-0001"]}
  ]
}
```

## Map Packet JSON Input:
```json
{PACKET_JSON}
```
