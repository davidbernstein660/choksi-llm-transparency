# Privacy & Transparency

Last updated: 2026-04-02

This page explains, in plain language, how this service handles data.

This is not a legal contract, terms of service, or formal privacy policy. It is a technical transparency note for friends and family so you can decide whether you are comfortable using the service.

## What This Service Is

This is a self-hosted AI chat service running on a private Mac.

It uses local models through Ollama and a web interface through Open WebUI. Public access is protected by Cloudflare Access.

## What Data Is Used

- Your approved email address is used for login through Cloudflare Access.
- Your prompts and responses are processed by the local server so the AI can answer.
- If web search is used, search queries are sent to Brave Search.
- If the AI reads a webpage, the server fetches that page directly.

## What Is Not Publicly Exposed

- Home Assistant is not exposed to the public internet.
- The raw Ollama API is not exposed to the public internet.
- The public site only exposes the web interface behind Cloudflare Access.

## What Is Stored

- Family accounts use temporary chats by default.
- That means normal family chat history should not be retained as persistent chat history.
- No known non-admin chats remain in the live database at the time of this update.
- Community chat sharing is disabled.
- Some operational logs still exist.
- Admin chats may still be stored unless temporary chat is used manually.

## Web Search Privacy

Web search in this service is server-side.

That means the search request comes from the server running this service, not directly from your device.

In practice, this means:

- Brave Search can see the search query and the VPN/proxy exit IP used by the service.
- If the AI reads a webpage, that destination website can see the VPN/proxy exit IP used by the service and the requested URL.
- Your personal device IP is not sent directly to Brave or the fetched website by these tool calls.

This service currently keeps webpage reading enabled because it improves research quality. That is a deliberate tradeoff, not an accident.

## Important Limits

- This service is private, but not anonymous.
- Cloudflare Access uses identity-based login.
- The server must see prompts in plaintext while processing them.
- Anyone with sufficient access to the host machine could inspect local files or logs.

## How To Use It Safely

- Do not paste passwords, recovery codes, banking credentials, or other highly sensitive secrets.
- Treat this like a useful private research tool, not a secure vault.
- If something would seriously harm you if exposed, do not paste it here.

## Technical Review

A much more detailed technical privacy document is available for anyone who wants to inspect the system more closely.

If you want, you are welcome to review the implementation yourself or use your own coding, security, or analysis tools to evaluate it before using the service.

Suggested links:

- [Technical Privacy Document](/privacy/technical/)
- [Source Code](https://github.com/davidbernstein660/choksi-llm-transparency)
- [Implementation Notes / Change History](/source/)
