# Technical Privacy Document

Last updated: 2026-04-02

This document is the public-safe technical privacy reference for `Choksi LLM`.

It is intentionally detailed, but it is still not a legal contract, terms of service, or formal privacy policy. It is a technical explanation of how the service is currently designed and what privacy tradeoffs exist.

## Purpose

This document exists so that technical users can evaluate the service before using it.

It is written to be inspectable by:

- humans
- security-minded friends and family
- coding tools
- analysis agents

## High-Level Architecture

Current high-level design:

- Public web entrypoint: `https://llm.choksillmservice.com`
- Public authentication: Cloudflare Access with approved email addresses and one-time PIN
- Web application: Open WebUI
- Inference runtime: Ollama running local models
- Primary models:
  - `qwen3.5:27b`
  - `qwen3.5:35b-a3b`
- Family-facing research tools:
  - built-in web search
  - built-in URL/page fetch

Important privacy truth:

- This service is more private than a typical cloud chatbot.
- It is not anonymous.
- It is not end-to-end encrypted from the host operator.
- The inference host must see prompts in plaintext in order to generate responses.

## Identity and Access

To use the public service, a user must:

1. visit the public hostname
2. enter an approved email address
3. receive a one-time PIN by email
4. complete Cloudflare Access authentication

Current behavior:

- Open WebUI uses the Cloudflare-authenticated email as the in-app identity
- users do not share one common chat account
- family access is individually authenticated through Cloudflare Access

This means:

- access is identity-based
- it is not anonymous access
- Cloudflare can see which approved identity authenticated

## Prompt and Response Processing

When a user sends a message:

1. the browser sends the message to Open WebUI
2. Open WebUI processes the request
3. Open WebUI sends the model request to Ollama
4. Ollama runs the local model
5. the response is returned through Open WebUI to the browser

This means prompt and response content is visible in plaintext during processing to:

- the user's browser
- the Open WebUI backend
- the Ollama runtime

Temporary chat does not change this runtime fact. Temporary chat reduces storage after the fact. It does not prevent the server from seeing the prompt while processing it.

## Web Search and URL Fetch

If a research preset uses web search:

- search queries are sent to Brave Search
- if the model chooses to read a page, the backend fetches that page directly

How that works in practice:

1. the user sends a prompt
2. Open WebUI decides whether to call `search_web`
3. Open WebUI sends the Brave API request from the server
4. if needed, Open WebUI sends the `fetch_url` request from the server too
5. the user browser does not contact Brave or the destination site directly for those tool calls

This means the origin of search and fetch traffic is:

- the host running this service
- a shared Nord VPN/proxy exit IP used for the research tool path

This means the origin is not:

- the individual user's device IP
- Cloudflare's public edge
- the home IP of the host network

What Brave can potentially see:

- the search query text
- the VPN/proxy exit IP used by the service
- the Brave API key used by the service
- request timing and normal API metadata

What destination websites can potentially see:

- the VPN/proxy exit IP used by the service
- the URL that was fetched
- metadata associated with a backend request

Current design choice:

- `fetch_url` is intentionally retained because it improves research quality
- search-only mode would be more private, but would also noticeably reduce the model's ability to read and summarize sources

## Storage and Retention

Current retention behavior:

- family users are assigned to a group with enforced temporary chat
- new non-admin users default into that family privacy group automatically
- new family chats should not persist as normal stored chat history
- no known non-admin chats remain in the live database at the time of this update
- admin chats are not automatically temporary

Known limits:

- admin chats may still be stored unless temporary chat is used manually
- older admin history may still exist
- backups may still contain older admin chat data

Older family chats that existed before enforced temporary mode were purged from the live database, the later residual non-admin chat was also removed, and the backup database snapshots known to contain family chat history were deleted.

## Logging

The service still produces operational metadata such as:

- service start and stop events
- request paths
- status codes
- tunnel events
- login-related metadata
- model runtime timing and load information

Current observed normal-operation behavior:

- ordinary Open WebUI logs are metadata-oriented rather than prompt-body logging
- ordinary Ollama logs are metadata-oriented rather than prompt-body logging
- ordinary cloudflared logs are metadata-oriented rather than prompt-body logging

Open WebUI also contains an upstream audit logging system that could capture request and response bodies if enabled.

Current intended runtime state:

- `GLOBAL_LOG_LEVEL=INFO`
- `AUDIT_LOG_LEVEL=NONE`
- audit log file output disabled

That means prompt-body logging is not intentionally enabled in the current normal request path.

Important nuance:

- this is not a cryptographic guarantee that prompt text could never appear in any log under every bug, failure mode, or future update

## Current Privacy Controls

Current important controls include:

- Open WebUI is not directly exposed on the LAN
- raw Ollama is not publicly exposed
- Home Assistant is not publicly exposed
- Cloudflare Access protects the public app
- community sharing is disabled
- admin chat access to other users is disabled in the normal app path
- admin analytics derived from chat history are disabled
- family users use enforced temporary chats
- dangerous family-facing tools such as shell access and code execution are not enabled

## Important Limitations

### This is not anonymous

Cloudflare Access is identity-based. The service operator and Cloudflare both know which approved account authenticated.

### This is not operator-proof encryption

The host running the model must process prompts in plaintext during inference.

### Search is an external disclosure surface

Web search sends user intent outside the local machine.

### Page fetch is an additional external disclosure surface

If `fetch_url` is used, third-party websites are contacted directly by the backend.

### Host trust still matters

Anyone with sufficient host-level access could inspect local files, logs, or stored state.

## How To Review The Implementation

When the source code for this deployment is published, technical reviewers should inspect:

- Open WebUI runtime configuration
- any backend override files
- model and tool configuration
- logging configuration
- privacy-related documentation and change history

In particular, reviewers should confirm:

- web search is server-side
- audit-body logging is disabled
- dangerous tool execution is not exposed to family-facing users
- public exposure is limited to the intended web app path

## Safe Usage Guidance

Users should not treat this service like a secure vault.

Do not paste:

- passwords
- recovery codes
- banking credentials
- highly sensitive personal secrets
- anything that would cause serious harm if exposed

## Future Privacy Improvements

Likely next steps include:

- outbound privacy for searches and page fetches, such as a VPN or other private egress layer
- possible migration to a self-hosted search backend such as SearXNG
- stronger backup retention and deletion policy
- more public source publication and review guidance
- possible future dedicated VPN egress only if reliability later outweighs the privacy benefit of shared exits

## Change Log

### 2026-04-02

- Created the first public-safe technical privacy document.
- Documented the identity-based Cloudflare Access flow.
- Documented the server-side Brave search and URL fetch flow.
- Documented the current logging posture and audit logging status.
- Documented the current family temporary-chat privacy posture.
- Recorded that `fetch_url` is intentionally retained for research quality despite the added privacy tradeoff.
- Documented that search and URL fetch egress now use a shared Nord VPN/proxy exit rather than the home IP.
- Documented that new non-admin users default into the family privacy group with enforced temporary chat.
- Documented that community sharing is disabled in the live configuration.
- Documented that no known non-admin chats remain in the live database after the later cleanup pass.
