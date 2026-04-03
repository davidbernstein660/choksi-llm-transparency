# Privacy & Transparency

Last updated: 2026-04-02

This page explains, in plain language, how this service handles data.

This is not a legal contract, terms of service, or formal privacy policy. It is a technical transparency note for friends and family so you can decide whether you are comfortable using the service.

Signed-in users can open the in-app Privacy Status page from inside the app to see the current observed Open WebUI version, logging state, and last successful verification time.

## What This Service Is

This is a self-hosted AI chat service running on a private Mac.

It uses local models through Ollama and a web interface through Open WebUI. Public access is protected by Cloudflare Access.

## What Data Is Used

- Your approved email address is used for login through Cloudflare Access.
- Your prompts and responses are processed by the local server so the AI can answer.
- If web search is used, the server sends Brave Search queries through the service's VPN/proxy-backed research path. This hides the home IP from Brave, but Brave still sees the query and the VPN/proxy provider becomes part of the trust boundary.
- If the AI reads a webpage, the server fetches that page through the same VPN/proxy-backed path. The destination site can still see the requested URL and the VPN/proxy exit IP.

## What Is Not Publicly Exposed

- Home Assistant is not exposed to the public internet.
- The raw Ollama API is not exposed to the public internet.
- The public site only exposes the web interface behind Cloudflare Access.

## What Is Stored

- Family users can choose between temporary/private chats and persistent chats.
- Temporary/private chats are less likely to remain as normal saved chat history, while persistent chats may be stored locally.
- Earlier retained non-admin chats from before the current private/persistent chat model were deleted from the live database on April 2, 2026.
- New non-admin chats may exist in the live database by design when a user chooses persistent mode.
- Short-lived rollback backups can temporarily retain stored chat data within the current backup retention window.
- Community chat sharing is disabled.
- Some operational logs still exist.
- The operator's own admin-account chats may still be stored unless temporary chat is used manually. This refers to the operator's own use of the service, not automatic access to other users' chats.

## Web Search Privacy

Web search in this service is server-side.

That means the search request comes from the server running this service, not directly from your device.

In practice, this means:

- Brave Search can see the search query and the VPN/proxy exit IP used by the service.
- If the AI reads a webpage, that destination website can see the VPN/proxy exit IP used by the service and the requested URL.
- Your personal device IP is not sent directly to Brave or the fetched website by these tool calls.
- The VPN/proxy path reduces exposure of the home IP, but it does not hide the search query from Brave or remove the VPN/proxy provider from the trust chain.

This service currently keeps webpage reading enabled because it improves research quality. That is a deliberate tradeoff, not an accident.

## Important Limits

- This service is private, but not anonymous.
- Cloudflare Access uses identity-based login.
- Cloudflare is in the public browser-to-origin path for the app, not only the login step.
- The server must see prompts in plaintext while processing them.
- The public transparency site asks not to be indexed or AI-crawled, but it is still a public website and non-compliant bots can ignore those controls.
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
