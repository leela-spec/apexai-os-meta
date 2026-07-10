**sed, awk, and perl are not Python libraries — they are free, open-source command-line programs**, and all three cost nothing and require no license or subscription.

## What They Actually Are

|Tool|Type|License|Cost|
|---|---|---|---|
|**sed**|Standalone CLI program (GNU implementation, part of GNU coreutils/textutils)|GPLv3+|Free [](https://qiita.com/y-vectorfield/items/bb92067cfbf16514301a)|
|**awk**|Standalone CLI program (GNU version called `gawk`)|GPLv3+|Free [](https://qiita.com/y-vectorfield/items/bb92067cfbf16514301a)|
|**perl**|A full programming language with its own interpreter, used here via `perl -i` for one-line file edits|GPL or Artistic License (your choice)|Free|

They are not something you `pip install` or `import` in Python — they are separate programs you call from a terminal/shell, and Python's `subprocess` module (or a shell script, or Claude Code itself) can invoke them, but they exist entirely independently of Python.

## Where to Get Them (Already Installed on Most Systems)

|OS|Availability|
|---|---|

|OS|Availability|
|---|---|
|**Linux**|Pre-installed by default on virtually every distro [](https://unix.stackexchange.com/questions/123144/which-is-the-most-portable-of-sed-awk-perl-and-sh)|
|**macOS**|Pre-installed, but it's the older BSD version of sed/awk, not GNU; install the GNU versions via Homebrew if you want GNU-specific syntax: `brew install gnu-sed` and `brew install gawk` [](https://qiita.com/y-vectorfield/items/bb92067cfbf16514301a)|
|**Windows**|Not built-in natively, but free to add via WSL2 (`sudo apt-get install perl`), Git Bash, Cygwin, or just using Perl alone since it's cross-platform and often pre-installed|

## Practical Note for Your Setup

Since you're on macOS-adjacent tooling in a coding environment (Claude Code, VS Code), you likely already have Perl and BSD sed/awk available with zero install step, and gawk/gnu-sed are a single free Homebrew command away if you hit BSD-syntax quirks. Portability ranking from actual sysadmin consensus: awk is most universally available, then sed, then perl — though perl is praised for being the most consistent across platforms once installed, since BSD and GNU versions of sed/awk have real syntax differences.

Bottom line: there is no cost, no account, no API key, and no rate limit — these are decades-old free Unix utilities, and using them for KB file patches means the "AI cost" collapses to just the few tokens needed to generate the one-line command.