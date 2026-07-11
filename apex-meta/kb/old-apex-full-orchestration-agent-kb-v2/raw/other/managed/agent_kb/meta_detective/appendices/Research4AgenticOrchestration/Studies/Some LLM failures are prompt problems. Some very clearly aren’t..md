# Some LLM failures are prompt problems. Some very clearly aren’t.

[

General Discussion

](https://www.reddit.com/r/PromptEngineering/?f=flair_name%3A%22General%20Discussion%22)

I've been getting kinda peeved at the same shit whenever AI/LLMs come up. As it is threads about whether they’re useful, dangerous, overrated, whatever, are already beaten to death but everything "wrong" with AI is just amalgamated into one big blob of bullshit. Then people argue past each other because they’re not even talking about the same problem.

_I’ll preface by saying I'm not technical. I just spend a lot of time using these tools and I've been noticing where they go sideways._

After a while, these are the main buckets I've grouped the failures into. I know this isn’t a formal classification, just the way I’ve been bucketing AI failures from daily use.

**1) When it doesn’t follow instructions**

Specific formats, order, constraints, tone, etc. The content itself might be fine, but the output breaks the rules you clearly laid out.  
That feels more like a control problem than an intelligence problem. The model “knows” the stuff, it just doesn’t execute cleanly.

**2) When it genuinely doesn’t know the info**

Sometimes the data just isn’t there. Too new, too niche, or not part of the training data. Instead of saying it doesn't know, it guesses. People usually label this as hallucinating.

**3) When it mixes things together wrong**

All the main components are there, but the final output is off. This usually shows up when it has to summarize multiple sources or when it's doing multi-step reasoning. Each piece might be accurate on its own, but the combined conclusion doesn't really make sense.

**4) When the question is vague**

This happens if the prompt wasn't specific enough, and the model wasn't able to figure out what you actually wanted. It still has to return something, so it just picks an interpretation. It's pretty obvious when these happen and I usually end up opening a new chat and starting over with a clearer brief.

**5) When the answer is kinda right but not what you wanted**

I'll ask it to “summarize” or “analyze” or "suggest" without defining what good looks like. The output isn’t technically wrong, it’s just not really usable for what I wanted. I'll generally follow up to these outputs with hard numbers or more detailed instructions, like "give me a 2 para summary" or "from a xx standpoint evaluate this article". This is the one I hit most when using ChatGPT for writing or analysis.

These obviously overlap in real life, but separating them helped me reason about fixes. In my experience, prompts can help a lot with 1 and 5, barely at all with 2, and only sometimes with 3 and 4.

When something says “these models are unreliable,” it's usually pointing at one of these. But people respond as if all five are the same issue, which leads to bad takes and weird overgeneralizations.

Some of these improve a lot with clearer prompts.  
Some don't change no matter how carefully you phrase the prompt.  
Some are more about human ambiguity/subjectiveness than actual model quality.  
Some are about forcing an answer when maybe there shouldn’t be one.

Lumping all of them together makes it easy to either overtrust or completely dismiss the model/tech, depending on your bias.

**Anyone else classifying how these models "break" in everyday use? Would love to hear how you see it and if I've missed anything.**