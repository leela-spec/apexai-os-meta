## The Local No-API Workflow (Step-by-Step)

Imagine you are sitting at your computer with a browser window open (ChatGPT/Gemini) and your local terminal AI (Codex) ready to execute scripts in your repository.

### Step 1: The Browser AI Proposes the Text

You paste a file into your browser AI. It says: _"The reference on line 42 is wrong. Under `## Deployment`, you should change the text."_ You tell the Browser AI: _"Give me the **entire new content** for that section. No explanations, just the text."_

The Browser AI outputs this raw block:

Plaintext

```
Run `pip install -e .` to begin. Make sure you have admin rights and python 3.11+.
```

### Step 2: The Terminal AI Creates a "Staging File"

You copy that block (or your terminal AI grabs it). Your Terminal AI does **not** try to patch the file. It does something incredibly dumb and safe: it writes that exact text into a temporary scratchpad file in your repo called `.patch_tmp.txt`.

Now your workspace looks like this:

- `deployment.md` (Your actual file, untouched)
    
- `.patch_tmp.txt` (Contains nothing but the raw text the AI generated)
    

### Step 3: Running the "Blind" Python Script

Your Terminal AI now runs the local python script, passing it only **two fixed arguments** that never change format: the target file and the exact markdown heading.

Bash

```
python edit.py deployment.md "## Deployment"
```

## Inside the `edit.py` Script (No-API Version)

Here is the entire script. Look closely at why it **cannot crash**, no matter how messy, chaotic, or weird the AI's text in `.patch_tmp.txt` is.

Python

```
import sys
import re
import subprocess

target_file = sys.argv[1]     # "deployment.md"
heading = sys.argv[2]         # "## Deployment"
tmp_file = ".patch_tmp.txt"   # The dumb scratchpad file

# 1. Read your actual file
with open(target_file, "r") as f:
    file_content = f.read()

# 2. Read the AI's raw text dump (The script does zero parsing or thinking here)
with open(tmp_file, "r") as f:
    ai_new_text = f.read().strip()

# 3. Locate the old section block using the Markdown Heading
# This regex grabs everything from your heading until the next heading starts
pattern = rf"({re.escape(heading)}\n)(.*?)(?=\n## |\Z)"
match = re.search(pattern, file_content, re.DOTALL)

if not match:
    # If the AI hallucinated the heading name, the script safely hard-fails 
    # BEFORE touching or corrupting your actual file.
    print(f"ERROR: Heading '{heading}' not found. No files modified.")
    sys.exit(1)

old_full_block = match.group(0) # Heading + old text
new_full_block = match.group(1) + ai_new_text  # Heading + brand new AI text

# 4. SWAP THE BLOCKS (Pure string replacement)
updated_file_content = file_content.replace(old_full_block, new_full_block, 1)

# 5. Save the file
with open(target_file, "w") as f:
    f.write(updated_file_content)

# 6. Show the human exactly what changed
print("--- GIT DIFF DETECTED ---")
subprocess.run(["git", "diff", target_file])
```

## Why This Architecture Handles the Chaos

You are worried that the AI is unreliable. It is. But let’s look at what happens when the AI acts unreliable in this setup:

### Scenario A: The AI adds weird conversational text or code fences

- **What the AI outputs into `.patch_tmp.txt`:** ```text
    
    Markdown
    
    ```
    Sure, here is your updated section!
    Run `pip install -e .` to begin.
    ```
    
- **What the Python Script does:** It doesn't try to read the code fences or understand the English. It blindly copies that _entire_ mess, headings, backticks, conversational fluff and all, and pastes it right under `## Deployment`.
    
- **The Result:** The script finishes with a `Success` exit code. It **does not crash**. Your file structure is completely unbroken. You type `git diff`, see that the AI added backticks and fluff, say _"Wow, that looks stupid,"_ and type `git checkout deployment.md` to instantly wipe it out.
    

### Scenario B: The AI hallucinates a heading that doesn't exist

- **What happens:** You tell the script to look for `"## Setup Configuration"`, but your file actually says `"## System Setup"`.
    
- **What the Python Script does:** The regex `if not match:` triggers. The script prints an error message and shuts down. Your target file is **never opened for writing**. Zero corruption.
    

### The Core Realization

The reason your previous setups crashed or looped is that you were treating the AI's output like a **command** (a command to add a line, delete a line, or find a line matching a pattern). If the command syntax was off by one space, the execution engine broke.

In this setup, the script treats the AI's output as **pure raw data payload**. The script says: _"I don't care what characters are inside this temp file. I am just a dump truck. I am picking up this pile of characters and dumping it right under this specific markdown header."_

The script handles 100% of the navigation logistically. The AI handles 100% of the content generation inside its isolated box. Because their jobs never overlap, they can't break each other.