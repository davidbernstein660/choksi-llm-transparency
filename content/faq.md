# FAQ

## Is this a legal privacy policy?

No.

This is a technical transparency note for friends and family. It is not a legal contract, terms of service, or formal privacy policy.

## Is this service anonymous?

No.

Access is controlled through Cloudflare Access with approved email addresses and one-time PIN. That means access is identity-based.

## Does the server see my prompts?

Yes, during processing.

The local host has to process the prompt in plaintext in order to run the model and produce a response.

## Are family chats stored?

Family accounts use enforced temporary chats by default, so new family chats should not persist as normal saved chat history.

## Are admin chats stored?

They can be, unless temporary chat is used manually.

## How does web search work?

Web search is server-side.

The backend sends Brave search requests and page fetch requests. Your browser does not contact Brave or the fetched site directly for those tool calls.

## Who sees web searches?

Brave can see the search query and the server's public IP. If a webpage is fetched, that website can also see the server's public IP and the requested URL.

## Why keep webpage fetching enabled?

Because it improves research quality. Search-only mode would reduce privacy disclosure to third-party sites, but it would also noticeably weaken the model's ability to read and summarize source pages.

## Can I inspect the code?

Yes. That is the goal.

When the source code repo is published, users should be able to inspect the implementation themselves or use their own tools or agents to review it.
