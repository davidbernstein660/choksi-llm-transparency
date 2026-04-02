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

Family users can now choose between temporary/private chats and persistent chats.

If a family user uses temporary/private mode, that chat should not persist as normal saved chat history. If a family user chooses persistent mode, that chat may be stored locally. Known older non-admin chats were removed from the live database.

## Can I share chats publicly from inside the app?

No.

Community sharing is disabled in the current configuration.

## Are admin chats stored?

The operator's own admin-account chats can be, unless temporary chat is used manually. This refers to the operator's own use of the service, not automatic access to other users' chats.

## How does web search work?

Web search is server-side.

The backend sends Brave search requests and page fetch requests. Your browser does not contact Brave or the fetched site directly for those tool calls.

## Who sees web searches?

Brave can see the search query and the VPN/proxy exit IP used by the service. If a webpage is fetched, that website can also see the VPN/proxy exit IP and the requested URL. The VPN/proxy path helps hide the home IP, but it does not hide the query from Brave or remove the VPN/proxy provider from the trust chain.

## Why keep webpage fetching enabled?

Because it improves research quality. Search-only mode would reduce privacy disclosure to third-party sites, but it would also noticeably weaken the model's ability to read and summarize source pages.

## Can I inspect the code?

Yes. That is the goal.

When the source code repo is published, users should be able to inspect the implementation themselves or use their own tools or agents to review it.
