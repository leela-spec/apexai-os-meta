Target confirmed. Two candidates stand out — [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) and [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB). Here's the breakdown for benchmark comparison against your scripts.[

---

## Top Candidates

## 1. AsyncFuncAI/deepwiki-open ⭐ ~15,500+

The clear leader. [deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open) is an open-source, AI-powered wiki generator for GitHub/GitLab/Bitbucket repos. It is the open-source clone of Devin's DeepWiki (by Cognition AI).[[sourceforge](https://sourceforge.net/projects/deepwiki-open.mirror/)]

**Pipeline steps:**

1. Clone repo → analyze structure and component relationships[[medium](https://medium.com/@sjng/deepwiki-why-i-open-sourced-an-ai-powered-wiki-generator-b67b624e4679)]
    
2. Embed codebase with OpenAI embeddings + Google Gemini context[[medium](https://medium.com/@sjng/deepwiki-why-i-open-sourced-an-ai-powered-wiki-generator-b67b624e4679)]
    
3. RAG retrieval → generate structured markdown wiki pages[[deepwiki](https://deepwiki.com/d-bui/deepwiki-open)]
    
4. Auto-generate Mermaid architecture/data-flow diagrams[[medium](https://medium.com/@sjng/deepwiki-why-i-open-sourced-an-ai-powered-wiki-generator-b67b624e4679)]
    
5. Expose interactive "Ask" Q&A over the wiki via MCP server[[github](https://github.com/mcp/cognitionai/deepwiki)]
    

**Key measurables:** 15,500+ stars, MIT license, Docker one-command start, supports 7 LLM providers (Gemini, OpenAI, Ollama, Mistral, Claude, DeepSeek, OpenRouter).[[ai-heartland](https://ai-heartland.com/tool/deepwiki-open/)]

---

## 2. VectifyAI/OpenKB ⭐ newer, lower stars

[OpenKB](https://github.com/VectifyAI/OpenKB) implements Karpathy's "LLM Wiki" pattern — compiles raw docs/sessions into a structured, interlinked wiki. More document-input focused vs. code-repo focused. Smaller community but tighter concept match if your process is about prompt/session wikis rather than code repos.[[pageindex](https://pageindex.ai/blog/introducing-openkb)]

---

## Process Comparison Matrix

|Dimension|deepwiki-open|OpenKB|Your Space scripts|
|---|---|---|---|
|Input|Code repo URL|Raw docs/files|Prompt templates + MD files [[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/06ff114f-e422-4941-b9ee-79ae3d7a57be/PromptTemplate.md?AWSAccessKeyId=ASIA2F3EMEYE47XFTX3S&Signature=0B2RpOOxzVqqWm3XQn%2BAn%2Fn1jHg%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDkaCXVzLWVhc3QtMSJHMEUCIQDFCGu2kL8mAiVZswoHw%2BCZwFnrDewRXuInbo7Oli4YBAIgMO9UKKAz0ABBnVCoyJUPZzamkPEK6qDVKZ0VRbLVNMQq8wQIARABGgw2OTk3NTMzMDk3MDUiDAP5JfJmpCZiAurdqyrQBAQmV2gjYvLPCkw1A9jh2hgHZnIWfMALHYsX22sz2f%2BeFDnXxBxwB9sJfxk4sX2mdX8IE9dDQ11c7xrTRqTj7h8oN%2BV2l2QoVzclUeyGfR1caSePHHfVnepQXLLLkGZWb2FQ6txIFaYrqevsiDj62bQab9r9qX10czwFdOgj%2FCiwVPFRRsi4mhLynVgfWKLsLjeugXpCcu%2FEJTAhLuKkucGURhJE5KN9X6SKKyHnR7vnz%2FhC3qHUi7gOpLN6B3npDgnTDtfVPhMZN952WEzdv4YPSsjDZXhQD8UVurKUOhH%2B9l%2BKqV5M%2BnYWASutKG%2FVht%2FLSPcuQ8%2BFf9pCO2YvPFNQGI47RxqU4xczig8NRj3FvGBNj7RMzRwZtj%2FLaD6X0d9OqgdQeFkaQq7O%2FnUc25Ri1%2B%2BivvyhD4haa7pVtLKOXgJYg3GsUxgWYnv0R2WlquQSDHQ75LVYt3Vidvjp7%2FbGif0gF%2FHhmQxgAwhhqhrQ26s0s44pPIL1RBuWC%2FJ6na1IAHNPX3kL6PMjhXMxSibyOgDZ7U408OLH76opzQJUjKQtmb74Bi5JPJDbb0%2FSIQ%2BNS8%2BIretUMh8YURIPHlE91F17R0%2FMZg9Thc8Ppiqjhs6%2Bt2iABB7X4ESmCSlwv%2F48i0dukhoDayeqKyU1l8mZiFNg6FagjANeaDb3Vn44fRwmOX92%2FopJ2jDJ4YA7HtcvUB20JRO8ZhB%2FClF88s12zc5wWaQFjQ5yxvo5QcC%2FZ4W9Z8fq%2BaiiLX9Nk42Qv%2BzWaO4kL5Vr%2BtK1wK39AZEw3LmM0wY6mAHDAheb%2Bzgr9BWqxvSd38fr%2BVBrzWL3usoFbbDS0vTuaPwznlR6F01WGFbzZ%2FXB15SA1EDVEDT7FtIA9CCXePV4oH146pshV0ZbyTz29Ogn7TWxBX%2F1%2BsRyd%2FheUV%2B4mP2q9N%2FENZS3V6b3o6ivVZvybXb%2FmUsj5b%2F0eRtDkZui7jztYc1%2FWO1dC6%2BwRhZWD5Yzk89c943FWQ%3D%3D&Expires=1784883887)]|
|Wiki generation|RAG + multi-LLM|Karpathy pattern CLI|Manual iterative [[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/aa046ba6-c1f9-405f-bff9-ef8283c0313e/IterativeProcess.md?AWSAccessKeyId=ASIA2F3EMEYE47XFTX3S&Signature=eYu8krvh6s%2Ba0zc24Ya9I9DQQQQ%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDkaCXVzLWVhc3QtMSJHMEUCIQDFCGu2kL8mAiVZswoHw%2BCZwFnrDewRXuInbo7Oli4YBAIgMO9UKKAz0ABBnVCoyJUPZzamkPEK6qDVKZ0VRbLVNMQq8wQIARABGgw2OTk3NTMzMDk3MDUiDAP5JfJmpCZiAurdqyrQBAQmV2gjYvLPCkw1A9jh2hgHZnIWfMALHYsX22sz2f%2BeFDnXxBxwB9sJfxk4sX2mdX8IE9dDQ11c7xrTRqTj7h8oN%2BV2l2QoVzclUeyGfR1caSePHHfVnepQXLLLkGZWb2FQ6txIFaYrqevsiDj62bQab9r9qX10czwFdOgj%2FCiwVPFRRsi4mhLynVgfWKLsLjeugXpCcu%2FEJTAhLuKkucGURhJE5KN9X6SKKyHnR7vnz%2FhC3qHUi7gOpLN6B3npDgnTDtfVPhMZN952WEzdv4YPSsjDZXhQD8UVurKUOhH%2B9l%2BKqV5M%2BnYWASutKG%2FVht%2FLSPcuQ8%2BFf9pCO2YvPFNQGI47RxqU4xczig8NRj3FvGBNj7RMzRwZtj%2FLaD6X0d9OqgdQeFkaQq7O%2FnUc25Ri1%2B%2BivvyhD4haa7pVtLKOXgJYg3GsUxgWYnv0R2WlquQSDHQ75LVYt3Vidvjp7%2FbGif0gF%2FHhmQxgAwhhqhrQ26s0s44pPIL1RBuWC%2FJ6na1IAHNPX3kL6PMjhXMxSibyOgDZ7U408OLH76opzQJUjKQtmb74Bi5JPJDbb0%2FSIQ%2BNS8%2BIretUMh8YURIPHlE91F17R0%2FMZg9Thc8Ppiqjhs6%2Bt2iABB7X4ESmCSlwv%2F48i0dukhoDayeqKyU1l8mZiFNg6FagjANeaDb3Vn44fRwmOX92%2FopJ2jDJ4YA7HtcvUB20JRO8ZhB%2FClF88s12zc5wWaQFjQ5yxvo5QcC%2FZ4W9Z8fq%2BaiiLX9Nk42Qv%2BzWaO4kL5Vr%2BtK1wK39AZEw3LmM0wY6mAHDAheb%2Bzgr9BWqxvSd38fr%2BVBrzWL3usoFbbDS0vTuaPwznlR6F01WGFbzZ%2FXB15SA1EDVEDT7FtIA9CCXePV4oH146pshV0ZbyTz29Ogn7TWxBX%2F1%2BsRyd%2FheUV%2B4mP2q9N%2FENZS3V6b3o6ivVZvybXb%2FmUsj5b%2F0eRtDkZui7jztYc1%2FWO1dC6%2BwRhZWD5Yzk89c943FWQ%3D%3D&Expires=1784883887)]|
|Diagram output|Mermaid auto|None listed|None|
|Q&A layer|MCP server, 3 tools|PageIndex RAG|N/A|
|Validation step|Implicit (RAG retrieval)|N/A|Explicit (list_files + cite) [[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/8dfe57a8-2a61-438c-8cbd-507b0f1d0879/MASTER_HANDOVER_learnings_and_rankings.md?AWSAccessKeyId=ASIA2F3EMEYE47XFTX3S&Signature=LLEv97aUqyYWfgqa%2FeTG8X%2FwCd0%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDkaCXVzLWVhc3QtMSJHMEUCIQDFCGu2kL8mAiVZswoHw%2BCZwFnrDewRXuInbo7Oli4YBAIgMO9UKKAz0ABBnVCoyJUPZzamkPEK6qDVKZ0VRbLVNMQq8wQIARABGgw2OTk3NTMzMDk3MDUiDAP5JfJmpCZiAurdqyrQBAQmV2gjYvLPCkw1A9jh2hgHZnIWfMALHYsX22sz2f%2BeFDnXxBxwB9sJfxk4sX2mdX8IE9dDQ11c7xrTRqTj7h8oN%2BV2l2QoVzclUeyGfR1caSePHHfVnepQXLLLkGZWb2FQ6txIFaYrqevsiDj62bQab9r9qX10czwFdOgj%2FCiwVPFRRsi4mhLynVgfWKLsLjeugXpCcu%2FEJTAhLuKkucGURhJE5KN9X6SKKyHnR7vnz%2FhC3qHUi7gOpLN6B3npDgnTDtfVPhMZN952WEzdv4YPSsjDZXhQD8UVurKUOhH%2B9l%2BKqV5M%2BnYWASutKG%2FVht%2FLSPcuQ8%2BFf9pCO2YvPFNQGI47RxqU4xczig8NRj3FvGBNj7RMzRwZtj%2FLaD6X0d9OqgdQeFkaQq7O%2FnUc25Ri1%2B%2BivvyhD4haa7pVtLKOXgJYg3GsUxgWYnv0R2WlquQSDHQ75LVYt3Vidvjp7%2FbGif0gF%2FHhmQxgAwhhqhrQ26s0s44pPIL1RBuWC%2FJ6na1IAHNPX3kL6PMjhXMxSibyOgDZ7U408OLH76opzQJUjKQtmb74Bi5JPJDbb0%2FSIQ%2BNS8%2BIretUMh8YURIPHlE91F17R0%2FMZg9Thc8Ppiqjhs6%2Bt2iABB7X4ESmCSlwv%2F48i0dukhoDayeqKyU1l8mZiFNg6FagjANeaDb3Vn44fRwmOX92%2FopJ2jDJ4YA7HtcvUB20JRO8ZhB%2FClF88s12zc5wWaQFjQ5yxvo5QcC%2FZ4W9Z8fq%2BaiiLX9Nk42Qv%2BzWaO4kL5Vr%2BtK1wK39AZEw3LmM0wY6mAHDAheb%2Bzgr9BWqxvSd38fr%2BVBrzWL3usoFbbDS0vTuaPwznlR6F01WGFbzZ%2FXB15SA1EDVEDT7FtIA9CCXePV4oH146pshV0ZbyTz29Ogn7TWxBX%2F1%2BsRyd%2FheUV%2B4mP2q9N%2FENZS3V6b3o6ivVZvybXb%2FmUsj5b%2F0eRtDkZui7jztYc1%2FWO1dC6%2BwRhZWD5Yzk89c943FWQ%3D%3D&Expires=1784883887)]|
|Patch/update process|Git-native re-index|Re-run CLI|Patch pack workflow [[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/a0da7961-d34c-4156-854e-525cb17b8073/AgentMode-GitNative-PatchPack-Process.okf.md?AWSAccessKeyId=ASIA2F3EMEYE47XFTX3S&Signature=DMPz9inxewg%2FrOl8oHHJlF5EaDM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDkaCXVzLWVhc3QtMSJHMEUCIQDFCGu2kL8mAiVZswoHw%2BCZwFnrDewRXuInbo7Oli4YBAIgMO9UKKAz0ABBnVCoyJUPZzamkPEK6qDVKZ0VRbLVNMQq8wQIARABGgw2OTk3NTMzMDk3MDUiDAP5JfJmpCZiAurdqyrQBAQmV2gjYvLPCkw1A9jh2hgHZnIWfMALHYsX22sz2f%2BeFDnXxBxwB9sJfxk4sX2mdX8IE9dDQ11c7xrTRqTj7h8oN%2BV2l2QoVzclUeyGfR1caSePHHfVnepQXLLLkGZWb2FQ6txIFaYrqevsiDj62bQab9r9qX10czwFdOgj%2FCiwVPFRRsi4mhLynVgfWKLsLjeugXpCcu%2FEJTAhLuKkucGURhJE5KN9X6SKKyHnR7vnz%2FhC3qHUi7gOpLN6B3npDgnTDtfVPhMZN952WEzdv4YPSsjDZXhQD8UVurKUOhH%2B9l%2BKqV5M%2BnYWASutKG%2FVht%2FLSPcuQ8%2BFf9pCO2YvPFNQGI47RxqU4xczig8NRj3FvGBNj7RMzRwZtj%2FLaD6X0d9OqgdQeFkaQq7O%2FnUc25Ri1%2B%2BivvyhD4haa7pVtLKOXgJYg3GsUxgWYnv0R2WlquQSDHQ75LVYt3Vidvjp7%2FbGif0gF%2FHhmQxgAwhhqhrQ26s0s44pPIL1RBuWC%2FJ6na1IAHNPX3kL6PMjhXMxSibyOgDZ7U408OLH76opzQJUjKQtmb74Bi5JPJDbb0%2FSIQ%2BNS8%2BIretUMh8YURIPHlE91F17R0%2FMZg9Thc8Ppiqjhs6%2Bt2iABB7X4ESmCSlwv%2F48i0dukhoDayeqKyU1l8mZiFNg6FagjANeaDb3Vn44fRwmOX92%2FopJ2jDJ4YA7HtcvUB20JRO8ZhB%2FClF88s12zc5wWaQFjQ5yxvo5QcC%2FZ4W9Z8fq%2BaiiLX9Nk42Qv%2BzWaO4kL5Vr%2BtK1wK39AZEw3LmM0wY6mAHDAheb%2Bzgr9BWqxvSd38fr%2BVBrzWL3usoFbbDS0vTuaPwznlR6F01WGFbzZ%2FXB15SA1EDVEDT7FtIA9CCXePV4oH146pshV0ZbyTz29Ogn7TWxBX%2F1%2BsRyd%2FheUV%2B4mP2q9N%2FENZS3V6b3o6ivVZvybXb%2FmUsj5b%2F0eRtDkZui7jztYc1%2FWO1dC6%2BwRhZWD5Yzk89c943FWQ%3D%3D&Expires=1784883887)]|
|Token/limit handling|Chunked embeddings|Chunked PDFs|Manual 5k char cap [[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bf26939d-29f7-4641-a6f4-56b0c9f8c83e/8dfe57a8-2a61-438c-8cbd-507b0f1d0879/MASTER_HANDOVER_learnings_and_rankings.md?AWSAccessKeyId=ASIA2F3EMEYE47XFTX3S&Signature=LLEv97aUqyYWfgqa%2FeTG8X%2FwCd0%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEDkaCXVzLWVhc3QtMSJHMEUCIQDFCGu2kL8mAiVZswoHw%2BCZwFnrDewRXuInbo7Oli4YBAIgMO9UKKAz0ABBnVCoyJUPZzamkPEK6qDVKZ0VRbLVNMQq8wQIARABGgw2OTk3NTMzMDk3MDUiDAP5JfJmpCZiAurdqyrQBAQmV2gjYvLPCkw1A9jh2hgHZnIWfMALHYsX22sz2f%2BeFDnXxBxwB9sJfxk4sX2mdX8IE9dDQ11c7xrTRqTj7h8oN%2BV2l2QoVzclUeyGfR1caSePHHfVnepQXLLLkGZWb2FQ6txIFaYrqevsiDj62bQab9r9qX10czwFdOgj%2FCiwVPFRRsi4mhLynVgfWKLsLjeugXpCcu%2FEJTAhLuKkucGURhJE5KN9X6SKKyHnR7vnz%2FhC3qHUi7gOpLN6B3npDgnTDtfVPhMZN952WEzdv4YPSsjDZXhQD8UVurKUOhH%2B9l%2BKqV5M%2BnYWASutKG%2FVht%2FLSPcuQ8%2BFf9pCO2YvPFNQGI47RxqU4xczig8NRj3FvGBNj7RMzRwZtj%2FLaD6X0d9OqgdQeFkaQq7O%2FnUc25Ri1%2B%2BivvyhD4haa7pVtLKOXgJYg3GsUxgWYnv0R2WlquQSDHQ75LVYt3Vidvjp7%2FbGif0gF%2FHhmQxgAwhhqhrQ26s0s44pPIL1RBuWC%2FJ6na1IAHNPX3kL6PMjhXMxSibyOgDZ7U408OLH76opzQJUjKQtmb74Bi5JPJDbb0%2FSIQ%2BNS8%2BIretUMh8YURIPHlE91F17R0%2FMZg9Thc8Ppiqjhs6%2Bt2iABB7X4ESmCSlwv%2F48i0dukhoDayeqKyU1l8mZiFNg6FagjANeaDb3Vn44fRwmOX92%2FopJ2jDJ4YA7HtcvUB20JRO8ZhB%2FClF88s12zc5wWaQFjQ5yxvo5QcC%2FZ4W9Z8fq%2BaiiLX9Nk42Qv%2BzWaO4kL5Vr%2BtK1wK39AZEw3LmM0wY6mAHDAheb%2Bzgr9BWqxvSd38fr%2BVBrzWL3usoFbbDS0vTuaPwznlR6F01WGFbzZ%2FXB15SA1EDVEDT7FtIA9CCXePV4oH146pshV0ZbyTz29Ogn7TWxBX%2F1%2BsRyd%2FheUV%2B4mP2q9N%2FENZS3V6b3o6ivVZvybXb%2FmUsj5b%2F0eRtDkZui7jztYc1%2FWO1dC6%2BwRhZWD5Yzk89c943FWQ%3D%3D&Expires=1784883887)]|

---

## What to Compare Against

For your benchmark, deepwiki-open's pipeline is the most direct reference:[[deepwiki](https://deepwiki.com/d-bui/deepwiki-open)]

- Their **chunking + embedding** step is the equivalent of your token-limit guards
    
- Their **RAG retrieval before generation** maps to your "SEARCH summaries first, then generate" rule
  
- Their **MCP server exposure** (`read_wiki_structure`, `read_wiki_contents`, `ask_question`) is the productized version of what your iterative prompt templates are doing manually[[github](https://github.com/mcp/cognitionai/deepwiki)]
    

The gap in your current scripts vs. deepwiki-open: no auto-diagram generation, no embedding layer, and no reusable query API — everything is prompt-driven and human-validated. That's not a flaw given your space constraints, but it's the delta to be aware of.