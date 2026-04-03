# Source Code and Technical Review

This service is intended to be inspectable.

The goal is not to ask users to trust high-level claims blindly. Technical users should be able to review the implementation for themselves.

## What This Page Is For

This page is meant to direct reviewers to:

- the public source code repository
- the technical privacy document
- implementation notes and change history

## What Reviewers Should Look For

Technical reviewers should check:

- what is publicly exposed
- how authentication is handled
- how prompts are processed
- how web search is performed
- what gets logged
- what gets stored
- whether the in-app Privacy Status page matches the public docs
- which tools are enabled or disabled

## Key Questions To Ask

- Is the raw model API exposed publicly?
- Is Home Assistant exposed publicly?
- Are public users separated by individual identity?
- Which Open WebUI version is currently running?
- Does the in-app Privacy Status page match the written documentation?
- Is prompt-body logging intentionally enabled?
- How are web searches originated?
- Which third parties can see search or fetch traffic?
- Are dangerous tools such as shell access exposed to family-facing users?

## Public Links

- [Source code repository](https://github.com/davidbernstein660/choksi-llm-transparency)
- [Technical privacy document](/privacy/technical/)
- [Privacy/transparency summary page](/privacy/)
- [Access the app](https://llm.choksillmservice.com)

## Review Philosophy

If you are a technical user, you should feel free to:

- inspect the code yourself
- inspect the documentation yourself
- use your own coding or analysis agents to review the implementation
- decide not to use the service if the tradeoffs are not acceptable to you
