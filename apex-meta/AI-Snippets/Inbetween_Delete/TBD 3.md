# Handover to the next AI

## The actual task

Find **one existing, established, preferably free program or script** that accepts a transcript or Markdown/text file and automatically turns it into a structured, searchable knowledge base.

The desired experience is:

```
transcript.md → run one program/command → knowledge base
```

The system itself should automatically:

- Read the complete transcript.
- Identify topics.
- Extract important statements, claims, procedures, recommendations, qualifications, limitations, and uncertainties.
- Group related statements.
- Preserve links to the exact source passages and timestamps when available.
- Produce something searchable and reusable, such as a graph, database, structured Markdown collection, JSON, or another real knowledge-base format.

This is a **general transcript-ingestion problem**. The Long COVID interview is only the initial use case. Do not turn the investigation into a medical-NLP project.

## What “one solution” means

The user wants a ready-made application, CLI, repository, or single packaged script that already performs the complete transformation.

Internal implementation details are acceptable, but the user should not have to assemble or operate:

- One tool for sentence splitting.
- Another for entity recognition.
- Another for relationships.
- Another for topic detection.
- Another database.
- Custom rules or training data.

A solution using multiple internal components qualifies only if they are already packaged behind one command or application.

## Required research approach

Search the web for existing transcript/document-to-knowledge-base tools.

For every candidate, verify using its official documentation, repository, research paper, and credible independent evidence where available:

- It accepts Markdown, text, or equivalent documents.
- It processes the complete document automatically.
- It extracts actual knowledge—not merely embeddings or text chunks.
- It creates topics, entities, statements, relationships, notes, or graph records.
- Its output is inspectable and linked to the original text.
- It is usable now rather than only described in a research paper.
- Whether it is free/==open==-source and can run locally.
- What installation and execution actually require.
- Whether it needs an API key, paid model, local LLM, GPU, manual annotation, schema design, or training.
- Its documented limitations and hallucination risks.

Prefer tools with evidence of real adoption and maintenance. Do not treat GitHub stars or marketing copy as proof of reliability.

## Required answer format

Keep the response short.

1. Start with the single best answer:
    
    > “The closest existing one-command solution is **X**.”
    
2. Show exactly how it is used:
    
    ```
    Input: transcript.md
    Command or action: ...
    Output: ...
    ```
    
3. Show a small realistic example of the resulting knowledge-base record or files.
    
4. State plainly:
    
    - What it extracts automatically.
    - What it does not extract.
    - Whether it uses generative AI.
    - Whether hallucinations are possible.
    - Whether every result retains its source passage.
    - Whether it is genuinely free.
5. Mention at most two alternatives, and only if the recommended system has an important deficiency.
    

Do not respond with a proposed architecture, eight-stage pipeline, collection of NLP libraries, or long methodological explanation.

## Excluded or previously unsuccessful answers

Do not recommend these as the primary answer:

- TTK or another system created in the user’s own repositories.
- Taguette, QualCoder, or manual annotation software.
- A workflow requiring the user to read and label the complete transcript.
- cTAKES, spaCy, CoreNLP, ==Open==IE, MedCAT, Bio-YODIE, GATE rules, or separate databases that the user must assemble.
- Microsoft GraphRAG unless it can be demonstrated as the best practical one-command end-to-end answer and its real requirements are explained succinctly.
- A generic vector database that merely divides the transcript into chunks.
- A RAG chatbot that retrieves passages but does not create organized knowledge records.
- A custom pipeline proposed by the answering AI.
- Another transcription solution.

## Important distinction

The requested output is not merely:

```
chunk → embedding → vector database
```

That only creates semantic search over transcript fragments.

The requested output is closer to:

```
Topic: Orthostatic testing

Statement:
A ten-minute active stand test can help identify an abnormal
heart-rate response.

Type: procedure/diagnostic claim
Qualification: medication may affect the result
Source: exact quotation
Timestamp: 01:42:18–01:42:31
Related statements: [...]
```

The application does not need to prove that a statement is scientifically true. It must accurately capture and organize what the source says, while maintaining traceability.

## Why the previous AI failed

The previous AI repeatedly answered a different question:

- It designed pipelines instead of finding one usable program.
- It decomposed the task into many technical stages the user would have to integrate.
- It confused deterministic storage with automatic knowledge extraction.
- It recommended manual coding software.
- It focused excessively on transcription after being told to assume the transcript already exists.
- It over-specialized the general problem into medical information extraction.
- It presented component libraries as though they constituted a usable end-to-end product.
- It reintroduced TTK despite explicit instructions not to rely on it.
- It produced large amounts of technical information before giving a direct recommendation.
- Even after identifying the correct question, it answered with eight stages and several separate tools.

The next AI must not design a solution first. It must search for and verify whether a **complete existing solution** already performs:

```
one document in → organized knowledge base out
```

If no credible tool satisfies that requirement, say so directly and identify the closest existing solution—without disguising a custom multi-tool pipeline as a finished product.