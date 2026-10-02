## Mission 1 — Karakeep evidence sync

This implements **US-03: Media & Document Custody** and feeds the existing **US-04/US-05 evidence process**.

### Process

```
Real research in Karakeep
        ↓
Select bookmarks tagged “macro”
        ↓
Download PDFs, archived HTML, and transcript JSON
        ↓
Store files in data/inbox/research/
        ↓
Record Karakeep identity, URL, timestamps, and SHA-256
        ↓
Existing evidence pipeline verifies structured claims
        ↓
Valid grounded claims enter the Action/Watch Register
```

### Input

Real data from your running Karakeep instance:

- Karakeep server URL
    
- Karakeep API key
    
- Bookmarks tagged `macro`
    
- Ideally several realistic examples:
    
    - one PDF
    - one archived webpage
    - one transcript JSON with timestamps
    - optionally one bookmark containing structured claims

### Transformation

The connector will:

1. Call the real Karakeep REST API.
2. Reject authentication failures and unexpected response formats.
3. Download supported evidence without altering its contents.
4. Calculate SHA-256 hashes in Python.
5. Preserve the external identity as:

```
karakeep:entries:<bookmark-id>
```

6. Avoid downloading or processing the same evidence repeatedly.
7. Pass compatible transcript-and-claim packages to the existing grounding process.

Raw PDFs or webpages will be placed into evidence custody, but they will not magically become investment claims. A claim only enters the register after the existing grounding rules can verify it against source material.

### Output

- Original evidence files under `data/inbox/research/`
- Provenance metadata and hashes
- Idempotency receipts
- Verified claims and watch items in the existing register, when adequate structured evidence is present
- A CLI result showing discovered, downloaded, skipped, processed, and rejected items

### Expected value

- No more manual downloading from Karakeep
- Traceable evidence lineage
- Duplicate-safe weekly processing
- Fail-closed behavior when Karakeep changes its API
- No invented data or mock production service

---

## Mission 2 — Telegram weekly digest

This implements **US-11: Hermes Telegram Digest** using the outputs already produced by **US-07 through US-10**.

### Process

```
Existing weekly quantitative pipeline
        ↓
Pre-computed report.md
        ↓
Deterministic section extraction
        ↓
Message shortened to Telegram’s limit
        ↓
Telegram Bot API
        ↓
Private operator chat or topic
```

### Input

Real pipeline output:

```
data/exports/snapshots/YYYY-MM-DD/report.md
```

Real Telegram configuration:

- Bot token
- Private chat ID
- Optional topic/thread ID

### Transformation

Python will copy and format these already-computed sections:

- Executive Macro Stance
- Regime Scaler
- Active Contradictions
- Priority Batch 1 Order Tickets

It will not recalculate:

- risk budgets
- position sizes
- portfolio weights
- share quantities
- limit prices

The message will remain below 4,000 characters. Telegram formatting failures and rejected API responses will be reported instead of silently ignored.

### Output

A private Telegram message containing the most important weekly operating information, including the reminder that order tickets require manual broker entry.

### Expected value

- The operator receives the weekly decision summary without opening files manually.
- The message contains the same figures as `report.md`.
- No LLM arithmetic or automated trading is introduced.
- Full reports remain the authoritative audit record.

## Real data I need from you

Please create `C:\GitDev\Investment\.env` locally—do not paste secrets into this chat—with:

```
KARAKEEP_URL=http://127.0.0.1:3000
KARAKEEP_API_KEY=<your-real-key>

TELEGRAM_BOT_TOKEN=<your-real-bot-token>
TELEGRAM_CHAT_ID=<your-private-chat-id>
TELEGRAM_THREAD_ID=<optional-topic-id>
```

Also add at least one real Karakeep bookmark tagged `macro`, preferably with a PDF or transcript attachment.

Tell me once the `.env` and sample bookmark are ready. I will then inspect the real API response safely, finalize the design against that real data, implement the two flows, and—with your approval—send one clearly labelled test Telegram digest.

Web previewWebsiteOpen

Open in

1:44 PM

okay lets start from the beginning:

- give me details on what kind of sources I should hand you Our infrastructure should be able to automatically scan for posts, videos, articles, and emails. In the last four weeks, we already created a flow on how to filter Web.de, which is a German email service provider, and a Google email. And, for example, I think it was Hermes or some other pipeline that understands, that checks the incoming mails. Then we have YouTube channels that post videos, and we might have also web pages that post articles that are important to watch. We don't want to over-engineer things right now. So give me a list of things that we will be adding. And yeah.
- Regarding your input list, I'm not 100% sure on what I'm going to provide. I can provide a PDF, a web page, a transcript, or a bookmark. What I don't understand is the KaraKeep server URL, KaraKeep API, bookmarks. What is that? So yeah, I need you to guide me through the process. Maybe we can do that through a different agent. Give me a handover to do all of that, and update surgically the project management for me doing that next, so that all agents are informed of these next steps.

Show more

1:49 PM

Worked for 1m 54s

We are building a controlled research-intake process: approved emails, YouTube channels, websites, PDFs, and manual bookmarks enter one evidence inbox. Karakeep stores the sources; Activepieces detects new items; Hermes later interprets them; IPOS remains responsible for deterministic investment decisions.

Important reality check: the Web.de/Gmail flow exists as a detailed plan, but it is not deployed. Activepieces and Karakeep are currently not reachable; Hermes and OpenProject are reachable.

## 1. What Karakeep means

Karakeep is your private research library.

A Karakeep “bookmark” can be:

- a webpage
- a PDF
- a YouTube URL
- an email attachment
- a text note
- an archived copy of an article

The terms mean:

- **Karakeep server URL:** the local address where Karakeep opens, expected to be `http://127.0.0.1:3000`.
- **API key:** a password-like token created inside Karakeep settings. It lets approved automation read your library. Never paste it into chat or commit it to Git.
- **Bookmark:** one stored research item with a title, URL or file, tags, notes, and a unique ID.
- **Tag:** a label such as `macro`, `rates`, `portfolio`, or `ipos-inbox`.

Karakeep is not currently running at the expected address, so deployment and initial configuration must happen before live synchronization.

## 2. Sources to add

### A. Email sources — US-EMAIL-01 and US-EMAIL-02

Please identify:

- approved Web.de senders
- approved Gmail senders
- newsletter domains
- subject patterns that indicate relevant mail
- whether attachments should be retained
- whether video and article links should be extracted

Examples:

|Source|What you provide|
|---|---|
|Analyst newsletter|Sender address and one representative email|
|Bank research|Sender domain and one PDF attachment|
|Market alert|Sender and recognizable subject prefix|
|YouTube notification|Sender and example notification|
|General newsletter|Sender plus examples of relevant and irrelevant messages|

Recommended filtering:

- Gmail: create a label named `IPOS/Research`.
- Web.de: create a folder named `IPOS Research`.
- Existing email rules place approved messages into those locations.
- Activepieces only scans the label/folder—not the complete mailbox.

This is more private and reliable than asking an AI to inspect every incoming email.

### B. YouTube sources — US-VIDEO-01

Please provide:

- channel URLs
- optionally specific playlists
- whether every video matters or only videos matching keywords
- preferred lookback period

Examples:

- central-bank channels
- macro analysts
- market-cycle researchers
- asset-specific analysts
- company investor-relations channels

Recommended first scope:

- 3–5 channels
- new videos going forward
- at most the last 30 days of history
- use YouTube’s RSS feed for detection
- store the URL in Karakeep
- transcribe only videos that pass the explicit source/keyword filter

### C. Websites and articles

Please provide:

- website homepage
- relevant section or category URL
- RSS/Atom feed if known
- relevant topics or keywords
- whether the site requires login or subscription

Recommended first scope:

- 3–5 public websites
- RSS feeds wherever available
- no paywall bypassing
- no custom scraping unless a valuable site has no supported feed
- archive the article URL and readable content in Karakeep

### D. PDFs

Please provide:

- one or two representative PDFs
- original publisher or download URL
- expected document type, such as outlook, whitepaper, earnings report, or policy publication

Initially, PDFs can be uploaded manually or captured from approved emails. Automatic extraction can follow once custody and duplicate handling are proven.

### E. Manual bookmarks

You should also be able to send an individual webpage to Karakeep from a browser extension or its web interface.

Recommended initial tags:

- `ipos-inbox`
- `macro`
- `rates`
- `equity`
- `credit`
- `commodities`
- `watch`

Manual capture remains useful for one-off research that does not belong to a monitored feed.

## 3. Recommended minimal architecture

This follows the existing project user stories without over-engineering:

```
Web.de folder ──────┐
Gmail label ────────┤
YouTube RSS ────────┤
Website RSS ────────┼─→ Activepieces ─→ Karakeep
Manual PDF/URL ─────┘                         │
                                             ▼
                                  Evidence ID + original source
                                             │
                                             ▼
                             Transcript/claim processing when applicable
                                             │
                                             ▼
                               Action/Watch Register and Hermes
```

Responsibilities:

- **Activepieces:** detects and routes approved incoming items.
- **Karakeep:** stores, searches, tags, and identifies evidence.
- **Hermes:** summarizes and evaluates relevance.
- **IPOS:** computes numeric policy, portfolio effects, and order tickets.
- **Operator:** reviews decisions and manually executes any broker action.

## 4. Implementation sequence

### Step 1 — Source inventory

Create a small allowlist containing:

- source name
- source type
- email sender, channel URL, or website feed
- topics
- priority
- attachments required
- processing rule

Output: an approved source registry and sample pack.

### Step 2 — Deploy and verify Karakeep

- Start Karakeep inside the existing WSL2 Docker environment.
- Open its web interface.
- Create the operator account.
- Generate an API key.
- Add one webpage, one PDF, and one YouTube URL manually.
- Confirm search, tags, duplicate behavior, and retained content.

Output: a functioning evidence library.

### Step 3 — Connect deterministic discovery

- Gmail label → Activepieces
- Web.de IMAP folder → Activepieces
- YouTube channel RSS → Activepieces
- Website RSS → Activepieces
- Activepieces → Karakeep

Output: approved new sources automatically enter Karakeep exactly once.

### Step 4 — Connect Karakeep to IPOS

- Query new items tagged `macro` or `ipos-inbox`.
- Export their source metadata and supported files.
- Calculate hashes.
- Preserve `karakeep:entries:<id>`.
- Process timestamped transcripts and grounded claims when available.

Output: traceable evidence available to the existing IPOS register.

### Step 5 — End-to-end validation

Test one realistic example from each class:

1. Web.de email with an article link
2. Gmail research email with a PDF
3. New YouTube video
4. New RSS article
5. Manually added bookmark
6. Duplicate delivery
7. Invalid mailbox authentication
8. Karakeep temporarily unavailable

Pass criteria:

- each valid item is stored once
- duplicates do not create duplicate actions
- failures are visible
- original source identity is retained
- no LLM invents numeric data
- no source recommendation becomes an automatic trade

## 5. What I need from you initially

Do not provide passwords yet. Prepare this simple list:

```
WEB.DE:
- Approved senders:
- Example relevant email:
- Example irrelevant email:

GMAIL:
- Approved senders:
- Existing labels:
- Example relevant email:

YOUTUBE:
- Channel URLs:
- Keywords, if any:

WEBSITES:
- Website or article-section URLs:

PDFS:
- One or two sample documents:

LOOKBACK:
- Recommended: last 30 days plus all new items
```

Files can be copied into a temporary intake folder later. Email credentials and API keys will remain in the relevant product’s secret store, not in the repository or chat.

## 6. Proposed handover and project-management update

I propose creating:

- `HANDOVER_RESEARCH_INTAKE_BOOTSTRAP.md`
    
- A new “Research Intake Bootstrap” work package in OpenProject
    
- Four child tasks:
    
    1. **Operator Source Inventory & Sample Pack**
    2. **Deploy and Validate Karakeep**
    3. **Configure Web.de, Gmail, YouTube, and RSS Intake**
    4. **Validate Karakeep-to-IPOS Evidence Sync**

I will also update `PROJECT_STATE.md` to correct the current status:

- Email intake: planned, not deployed
- Karakeep: planned, not currently reachable
- Activepieces: planned, not currently reachable
- Hermes: reachable
- Next operator action: provide the source inventory and representative samples

This matches the existing [user stories](C:/GitDev/Investment/05_blueprint/research/2026-08-28-modular-rebuild/08_USER_STORIES_AND_INTEGRATION_WORKFLOWS.md) and replaces the premature assumption that live Karakeep synchronization is ready.

If you approve this intake-first design, I’ll write the handover and update OpenProject and `PROJECT_STATE.md` accordingly.

Web previewWebsiteOpen

Open in

1:51 PM

do that, but build heavily on the already created plans for that. we do not need to reinvent things. but the handover should be very mindful not to confuse rpevious settings and envrionemtn with our updated new architecture. what is that project state file? In what kind of a (sub)project are you going to create the tasks in openproject.

sadly your sequence is still very hard for me to undestand. it is very superficial and does nnot give me a real feleling of what the actual value is that each output will produce for me as a investment practitioner

furhter we already tested several sources in the past (video to transcript to insights) find them. they should have commits and folders on this machine or repo. (they should be 1-2months old) we can use them as input for that pipeline I guess?

2:09 PM

Worked for 6m 23s

Created the intake handover and updated the repository’s living status:

- [Research Intake Bootstrap handover (line 1)](C:/GitDev/Investment/HANDOVER_RESEARCH_INTAKE_BOOTSTRAP.md:1)
- [Updated PROJECT_STATE.md (line 1)](C:/GitDev/Investment/PROJECT_STATE.md:1)

The handover builds directly on M04, M05, M07, M08, M09, M19, WF-07, and the existing user stories. It explicitly rejects stale branch, Docker, filesystem, port, and runtime assumptions.

### Practitioner value

The process now has seven concrete outputs:

1. **Source mandate** — defines which analysts, channels, newsletters, and sites deserve attention.
2. **Research queue** — removes irrelevant and duplicate material.
3. **Evidence record** — keeps the original source searchable and auditable.
4. **Media package** — converts long videos into timestamped transcripts and chart frames.
5. **Research card** — states the thesis, evidence, affected assets, and invalidation condition.
6. **Portfolio relevance result** — classifies evidence as `NO_IMPACT`, `WATCH`, `REVIEW`, or `HIGH_PRIORITY_REVIEW`.
7. **Weekly decision context** — combines unresolved research with holdings, macro stance, risk diagnostics, and precomputed order tickets.

This is meant to answer: _What arrived? What exactly was said? What could it affect? Does it require attention?_

### Existing sources found

The handover reuses these committed tests:

- IMF July 2026 outlook video: real yt-dlp → FFmpeg → WhisperX → PySceneDetect execution, including timestamped transcript and reviewed frames.
- German Markus Koch investment video: complete German transcript-to-knowledge test.
- Elliott Prechter market-structure video.
- Market Cycles Report from August 17, 2026.
- Ralph Adolphs long-form lecture as a non-investment control, proving the system need not force every source into portfolio relevance.

The larger four-source pipeline is under:

`C:\GitDev\apexai-os-meta\artifacts\transcript_pipeline_v2`

It passed the August 18 four-source regression and English/German end-to-end tests. These are now specified as the initial acceptance corpus, so we do not need to reinvent or request another video collection.

### What PROJECT_STATE.md is

It is the repository’s short living index for new sessions. It tells agents:

- what is already complete;
- what the current execution frontier is;
- which handover is authoritative;
- where the important files are.

It does not replace OpenProject. OpenProject manages ownership and delivery; `PROJECT_STATE.md` keeps repository sessions oriented.

### OpenProject placement

The tasks should be created in the existing private OpenProject project that already owns the M01–M19 IPOS modular-rebuild work. They should not go into:

- community OpenProject;
- a demo project;
- a generic infrastructure project;
- a newly invented project.

The proposed parent is:

`IPOS — Research Intake & Evidence Operations`

with RI-01 through RI-07 as children. Existing M04/M05/M07/M08/M09/M19 work packages should be linked or updated rather than duplicated.

I have not created the OpenProject work packages yet. The private instance is reachable, but its browser tab is signed out and currently displays an invalid-password/temporary-lock warning. Please sign in to the private OpenProject tab yourself, then tell me to continue; I will inspect the existing hierarchy and prepare the exact work-package changes for final confirmation before submission.

Repository QA after the documentation changes reports `ALL REQUIRED TESTS PASSED`.