# Choksi LLM Public Transparency Site

This folder is a clean public-safe repo scaffold for the future public-facing transparency site.

The intended use is:

- publish the plain-language privacy/transparency pages for friends and family
- publish the public-safe technical privacy document
- later add links to the public source code repository
- eventually deploy the static site with Cloudflare Pages

This repo is intentionally separate from the live local LLM workspace.

## What belongs here

- homepage copy
- privacy/transparency summary copy
- public-safe technical privacy documentation
- FAQ content
- source/review instructions
- static site assets and templates later

## What must not be published here

- secrets
- tokens
- database files
- backups
- LaunchAgent files
- raw logs
- exact local filesystem paths
- operator-only maintenance notes
- anything copied directly from the live machine without review

## Current structure

- `content/homepage.md`
- `content/privacy-summary.md`
- `content/privacy-technical.md`
- `content/faq.md`
- `content/source-review.md`

## Relationship to local-only docs

The internal operator document lives outside this repo at:

- [Privacy.local.md](/Users/llmservice/Desktop/llmservice/Privacy.local.md)

That file is intentionally more candid and more operational. It should not be published verbatim.

## Intended next steps

1. Review and refine the public-safe copy in `content/`.
2. Create a simple static site shell.
3. Publish this repo to GitHub.
4. Deploy with Cloudflare Pages.
5. Add a public custom domain such as `choksillmservice.com`.
