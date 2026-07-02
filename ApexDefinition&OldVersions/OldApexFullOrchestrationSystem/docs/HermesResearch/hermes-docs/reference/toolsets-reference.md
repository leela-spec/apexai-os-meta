Title: Toolsets Reference | Hermes Agent

URL Source: https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference

Published Time: Fri, 29 May 2026 12:35:12 GMT

Markdown Content:
`browser``browser_back`, `browser_cdp`, `browser_click`, `browser_console`, `browser_dialog`, `browser_get_images`, `browser_navigate`, `browser_press`, `browser_scroll`, `browser_snapshot`, `browser_type`, `browser_vision`, `web_search`Core browser automation. Includes `web_search` as a fallback for quick lookups. `browser_cdp` and `browser_dialog` are gated at runtime — registered only when a CDP endpoint is reachable at session start (via `/browser connect`, `browser.cdp_url` config, Browserbase, or Camofox). `browser_dialog` works together with the `pending_dialogs` and `frame_tree` fields that `browser_snapshot` adds when a CDP supervisor is attached.
`clarify``clarify`Ask the user a question when the agent needs clarification.
`code_execution``execute_code`Run Python scripts that call Hermes tools programmatically.
`cronjob``cronjob`Schedule and manage recurring tasks.
`debugging`composite (`file` + `terminal` + `web`)Debug bundle — file, process/terminal, web extract/search.
`delegation``delegate_task`Spawn isolated subagent instances for parallel work.
`discord``discord`Core Discord text/embed/DM actions (gateway-only). Active on the `hermes-discord` toolset.
`discord_admin``discord_admin`Discord moderation (bans, role changes, channel management). Active on the `hermes-discord` toolset; requires the bot to hold the relevant Discord permissions.
`feishu_doc``feishu_doc_read`Read Feishu/Lark document content. Used by the Feishu document-comment intelligent-reply handler.
`feishu_drive``feishu_drive_add_comment`, `feishu_drive_list_comments`, `feishu_drive_list_comment_replies`, `feishu_drive_reply_comment`Feishu/Lark drive comment operations. Scoped to the comment agent; not exposed on `hermes-cli` or other messaging toolsets.
`file``patch`, `read_file`, `search_files`, `write_file`File reading, writing, searching, and editing.
`homeassistant``ha_call_service`, `ha_get_state`, `ha_list_entities`, `ha_list_services`Smart home control via Home Assistant. Only available when `HASS_TOKEN` is set.
`computer_use``computer_use`Background macOS desktop control via cua-driver — does not steal cursor/focus. Works with any tool-capable model. macOS only; requires `cua-driver` on `$PATH`.
`image_gen``image_generate`Text-to-image generation via FAL.ai (with opt-in OpenAI / xAI backends).
`video_gen``video_generate`Text-to-video and image-to-video via plugin-registered backends (xAI Grok-Imagine, FAL.ai Veo 3.1 / Pixverse v6 / Kling O3). Pass `image_url` to animate an image; omit it for text-to-video.
`kanban``kanban_block`, `kanban_comment`, `kanban_complete`, `kanban_create`, `kanban_heartbeat`, `kanban_link`, `kanban_list`, `kanban_show`, `kanban_unblock`Multi-agent coordination tools. Registered for dispatcher-spawned task workers (`HERMES_KANBAN_TASK`) and for profiles that explicitly enable the `kanban` toolset. Workers mark tasks done, block, heartbeat, comment, and create/link follow-up tasks; orchestrator profiles additionally get board-routing tools like list/unblock.
`memory``memory`Persistent cross-session memory management.
`messaging``send_message`Send messages to other platforms (Telegram, Discord, etc.) from within a session.
`moa``mixture_of_agents`Multi-model consensus via Mixture of Agents.
`safe``image_generate`, `vision_analyze`, `web_extract`, `web_search` (via `includes`)Read-only research + media generation. No file writes, no terminal, no code execution.
`search``web_search`Web search only (without extract).
`session_search``session_search`Search past conversation sessions.
`skills``skill_manage`, `skill_view`, `skills_list`Skill CRUD and browsing.
`spotify``spotify_albums`, `spotify_devices`, `spotify_library`, `spotify_playback`, `spotify_playlists`, `spotify_queue`, `spotify_search`Native Spotify control (playback, queue, search, playlists, albums, library). Registered by the bundled `spotify` plugin.
`terminal``process`, `terminal`Shell command execution and background process management.
`todo``todo`Task list management within a session.
`tts``text_to_speech`Text-to-speech audio generation.
`vision``vision_analyze`Image analysis via vision-capable models.
`video``video_analyze`Video analysis and understanding tools (opt-in, not in the default toolset — add explicitly via `--toolsets`).
`web``web_extract`, `web_search`Web search and page content extraction.
`x_search``x_search`Search X (Twitter) posts and threads via xAI's built-in `x_search` Responses tool. Off by default; opt in via `hermes tools`. Schema only registered when xAI credentials (SuperGrok OAuth or `XAI_API_KEY`) are configured.
`yuanbao``yb_query_group_info`, `yb_query_group_members`, `yb_search_sticker`, `yb_send_dm`, `yb_send_sticker`Yuanbao DM/group actions and sticker search. Registered only on `hermes-yuanbao`.
