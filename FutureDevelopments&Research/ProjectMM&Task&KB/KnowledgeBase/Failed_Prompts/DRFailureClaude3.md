The honest answer is: I identified the failure modes correctly each time. Then I fixed them with more structure — which is itself the failure mode.[PromptDesignFailures-5.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/b48fcfbd-9cf2-4df4-9f6c-d87c47992942/PromptDesignFailures-5.md?AWSAccessKeyId=ASIA2F3EMEYEWZFWJLI3&Signature=tumoyKiH7FsP6Jal%2Bqrbcv%2BEdhc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIGVg%2BMitL8e8U7ewm9%2Fec5pIt8LtUiA9FnxijWKUB4MSAiEApsN3%2BmI%2FHwctqQX2RUgzhxWrL101NjLauKTUBnOzjD8q8wQIaBABGgw2OTk3NTMzMDk3MDUiDBtYwni%2BkS0dCDnhgirQBFUOz7eNHDlot64komEMJiqRw8cVIdzYj27SbbO3QHnMUvE9tMv9iTs0pzw2Ny8mJFFnY3wqZdNX9Z36BJGzfLT2a9fYYHQFWYblTzbP9vp%2FIDWbE%2Fsqv9xoEVxZeys26j1aRAVzmHLSlhHF3A1wvtGvW9lUtkITLYn0%2FjSz3h%2FpsNX75ga5H405HmkkZz0SybLZLiqgpQzbRDlx2k2XLZCfcjGeJuC3vkqZ36nUEIL1RvGFAwu6aXMCsXX2msZfVkFIp9DTukC72wcn7xZ4kQF8bpveFYKe8RJT%2BQ0eomc1Cw%2BMzB5dfaarSEAkQD7AsHnR09nRXUG%2BNohOPip2buda8JVRk7koYDmnkpe%2F%2FRirZoYDFm2oVu%2FapkYeiZJ3V7hvNo5fshWF5P1GOTymVk5rUe9yJhmFAwViIJOpKgn1rN%2FmplLcot1WqfNRFwRpvN9YsiASwAhjVpMSLEXInlRAu2Hxt4%2FINpjfJOJiDPk192K4rkWvGOI70%2BQYE2n45NAw2tis6XJpONi3%2BY94etqYxEHHiyr2VQ0byJy7C8BzcU8EA5fOlTQNEtVx%2Br9rqC6415XDexABRFkcPlU8FSs8V8vyoPmQlpLRsmH3eqr%2BO%2BEzQX66Z7Ez3ikT7PuY6PAhRYa0zV7SX5HCWTrAMNFwkTm8TykOc35S0hm5DKXM0dBcRnzxDuid%2B%2F9dTePR8Id1L7oFmG9kUWShimhREzZJpcr%2FVQ1VI7WxOpUNscGQ17VtI2LewWDx%2BzABDQP0L3FXRDPzzSBrla2%2FeCJNbo4wi5%2F60QY6mAHyZQ1dQb4FnCjqe5RhLM%2F4Hs%2BGZzagKd%2FbjbOVLd1wKdA9f%2FZoQs%2B5SB9D4TtEZgqKkELS678gEDrjsHBwQl1BrXZh9AIRBwTc6wsZ4WN5Z%2B4RI2CTMdcv4%2BpI4QGOxD%2BbqcUdN5%2B43CMHSU33DljNo6ZBpkZMXmZnzKKyOH15s1rLL%2B0fyDR3rwtGNaX6d%2Bz%2FASKAzgPcXQ%3D%3D&Expires=1782488414)

---

## What Actually Happened

Every iteration followed the same loop:

1. Diagnose: "the model ignored constraint X"
    
2. Fix: "add stronger enforcement for X"
    
3. Result: the enforcement machinery became the new failure
    

The post-mortem (PE-04) explicitly states that A consumed B's budget because of structural overhead. My response to that was to add XML isolation tags, tiered web query logic, VM01–VM10 validation markers, and a phase split — all of which are structural overhead. I read the diagnosis and prescribed the disease.[PromptDesignFailures-5.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/b48fcfbd-9cf2-4df4-9f6c-d87c47992942/PromptDesignFailures-5.md?AWSAccessKeyId=ASIA2F3EMEYEWZFWJLI3&Signature=tumoyKiH7FsP6Jal%2Bqrbcv%2BEdhc%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIGVg%2BMitL8e8U7ewm9%2Fec5pIt8LtUiA9FnxijWKUB4MSAiEApsN3%2BmI%2FHwctqQX2RUgzhxWrL101NjLauKTUBnOzjD8q8wQIaBABGgw2OTk3NTMzMDk3MDUiDBtYwni%2BkS0dCDnhgirQBFUOz7eNHDlot64komEMJiqRw8cVIdzYj27SbbO3QHnMUvE9tMv9iTs0pzw2Ny8mJFFnY3wqZdNX9Z36BJGzfLT2a9fYYHQFWYblTzbP9vp%2FIDWbE%2Fsqv9xoEVxZeys26j1aRAVzmHLSlhHF3A1wvtGvW9lUtkITLYn0%2FjSz3h%2FpsNX75ga5H405HmkkZz0SybLZLiqgpQzbRDlx2k2XLZCfcjGeJuC3vkqZ36nUEIL1RvGFAwu6aXMCsXX2msZfVkFIp9DTukC72wcn7xZ4kQF8bpveFYKe8RJT%2BQ0eomc1Cw%2BMzB5dfaarSEAkQD7AsHnR09nRXUG%2BNohOPip2buda8JVRk7koYDmnkpe%2F%2FRirZoYDFm2oVu%2FapkYeiZJ3V7hvNo5fshWF5P1GOTymVk5rUe9yJhmFAwViIJOpKgn1rN%2FmplLcot1WqfNRFwRpvN9YsiASwAhjVpMSLEXInlRAu2Hxt4%2FINpjfJOJiDPk192K4rkWvGOI70%2BQYE2n45NAw2tis6XJpONi3%2BY94etqYxEHHiyr2VQ0byJy7C8BzcU8EA5fOlTQNEtVx%2Br9rqC6415XDexABRFkcPlU8FSs8V8vyoPmQlpLRsmH3eqr%2BO%2BEzQX66Z7Ez3ikT7PuY6PAhRYa0zV7SX5HCWTrAMNFwkTm8TykOc35S0hm5DKXM0dBcRnzxDuid%2B%2F9dTePR8Id1L7oFmG9kUWShimhREzZJpcr%2FVQ1VI7WxOpUNscGQ17VtI2LewWDx%2BzABDQP0L3FXRDPzzSBrla2%2FeCJNbo4wi5%2F60QY6mAHyZQ1dQb4FnCjqe5RhLM%2F4Hs%2BGZzagKd%2FbjbOVLd1wKdA9f%2FZoQs%2B5SB9D4TtEZgqKkELS678gEDrjsHBwQl1BrXZh9AIRBwTc6wsZ4WN5Z%2B4RI2CTMdcv4%2BpI4QGOxD%2BbqcUdN5%2B43CMHSU33DljNo6ZBpkZMXmZnzKKyOH15s1rLL%2B0fyDR3rwtGNaX6d%2Bz%2FASKAzgPcXQ%3D%3D&Expires=1782488414)

---

## The Actual Pattern You're Watching

|Iteration|New mechanism added|Outcome|
|---|---|---|

|Iteration|New mechanism added|Outcome|
|---|---|---|
|v1–v3|Contamination guard preamble|Model acknowledged it, ignored it during output|
|v4 (file:5)|Tagging system, BUDGETEXCEEDED flag, compute weights|Identified as improvement, untested|
|My revision|XML tags, phase split, tiered queries, VM markers|Blocked execution, added overhead|
|Working prompt|None of the above|Ran successfully|

The working prompt you shared is structurally **simpler** than v1. It has more _content_ (14 deliverables, detailed YAML field specs, contamination table) but far less _enforcement machinery_.[Anotehr-failed-DRPromptdesign4-4.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/e460bc0d-eaa1-4748-810a-71e8694c6485/Anotehr-failed-DRPromptdesign4-4.md?AWSAccessKeyId=ASIA2F3EMEYEWZFWJLI3&Signature=6%2FBtgm1s1Zewd7jP1dYspGlG7i8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIGVg%2BMitL8e8U7ewm9%2Fec5pIt8LtUiA9FnxijWKUB4MSAiEApsN3%2BmI%2FHwctqQX2RUgzhxWrL101NjLauKTUBnOzjD8q8wQIaBABGgw2OTk3NTMzMDk3MDUiDBtYwni%2BkS0dCDnhgirQBFUOz7eNHDlot64komEMJiqRw8cVIdzYj27SbbO3QHnMUvE9tMv9iTs0pzw2Ny8mJFFnY3wqZdNX9Z36BJGzfLT2a9fYYHQFWYblTzbP9vp%2FIDWbE%2Fsqv9xoEVxZeys26j1aRAVzmHLSlhHF3A1wvtGvW9lUtkITLYn0%2FjSz3h%2FpsNX75ga5H405HmkkZz0SybLZLiqgpQzbRDlx2k2XLZCfcjGeJuC3vkqZ36nUEIL1RvGFAwu6aXMCsXX2msZfVkFIp9DTukC72wcn7xZ4kQF8bpveFYKe8RJT%2BQ0eomc1Cw%2BMzB5dfaarSEAkQD7AsHnR09nRXUG%2BNohOPip2buda8JVRk7koYDmnkpe%2F%2FRirZoYDFm2oVu%2FapkYeiZJ3V7hvNo5fshWF5P1GOTymVk5rUe9yJhmFAwViIJOpKgn1rN%2FmplLcot1WqfNRFwRpvN9YsiASwAhjVpMSLEXInlRAu2Hxt4%2FINpjfJOJiDPk192K4rkWvGOI70%2BQYE2n45NAw2tis6XJpONi3%2BY94etqYxEHHiyr2VQ0byJy7C8BzcU8EA5fOlTQNEtVx%2Br9rqC6415XDexABRFkcPlU8FSs8V8vyoPmQlpLRsmH3eqr%2BO%2BEzQX66Z7Ez3ikT7PuY6PAhRYa0zV7SX5HCWTrAMNFwkTm8TykOc35S0hm5DKXM0dBcRnzxDuid%2B%2F9dTePR8Id1L7oFmG9kUWShimhREzZJpcr%2FVQ1VI7WxOpUNscGQ17VtI2LewWDx%2BzABDQP0L3FXRDPzzSBrla2%2FeCJNbo4wi5%2F60QY6mAHyZQ1dQb4FnCjqe5RhLM%2F4Hs%2BGZzagKd%2FbjbOVLd1wKdA9f%2FZoQs%2B5SB9D4TtEZgqKkELS678gEDrjsHBwQl1BrXZh9AIRBwTc6wsZ4WN5Z%2B4RI2CTMdcv4%2BpI4QGOxD%2BbqcUdN5%2B43CMHSU33DljNo6ZBpkZMXmZnzKKyOH15s1rLL%2B0fyDR3rwtGNaX6d%2Bz%2FASKAzgPcXQ%3D%3D&Expires=1782488414)

---

## What I Should Have Done

Instead of redesigning your prompt, I should have said:

> "Your prompt structure is already correct based on the working pattern. Apply the 4 surgical fixes as literal text swaps — don't restructure."

The four fixes from the feedback were:

- Escape the backticks → swap for XML tags in the patch _content_ only
    
- Fix the scope contradiction → one sentence rewrite in §0.2
    
- Reduce token exhaustion → add a compute weight note, not a phase split
    
- Tier the web queries → add "Critical first" as a single line, not a full tier system
    

None of those required a rewrite. I rewrote anyway. That's the real failure.