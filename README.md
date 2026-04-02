# Choksi LLM Public Transparency Site

This folder is a clean public-safe repo for the public-facing transparency site.

The intended use is:

- publish the plain-language privacy/transparency pages for friends and family
- publish the public-safe technical privacy document
- later add links to the public source code repository
- deploy the static site with Cloudflare Pages

This repo is intentionally separate from the live local LLM workspace.

## What belongs here

- homepage copy
- privacy/transparency summary copy
- public-safe technical privacy documentation
- FAQ content
- source/review instructions
- static HTML pages and shared CSS

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

## Current site files

- `index.html`
- `privacy/index.html`
- `privacy/technical/index.html`
- `faq/index.html`
- `source/index.html`
- `assets/site.css`
- `_headers`

## Intended next steps

1. Review and refine the public-safe copy in `content/`.
2. Deploy with Cloudflare Pages.
3. Add the public custom domain `choksillmservice.com`.
4. Redirect the default `*.pages.dev` hostname to the custom domain.
