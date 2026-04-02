# Publishing Notes

This file is for preparing the public transparency repo for GitHub and Cloudflare Pages.

## Current Status

- Content drafts exist in `content/`
- Static HTML pages and shared CSS now exist in `public/`
- A Git repository has been initialized in this folder
- A public GitHub remote exists for this folder
- No Cloudflare project has been created yet

## Pre-Publish Checklist

- confirm no secrets exist in this folder
- confirm no local absolute filesystem paths remain
- confirm no operator-only backup or maintenance details remain
- confirm wording stays clearly non-legal and non-contractual
- confirm the technical doc remains candid about limitations

## Next Cloudflare Setup Step

Create a Git-connected Cloudflare static-assets project connected to the public GitHub repo with:

- production branch: `main`
- build command: `exit 0`
- deploy command: `npx wrangler deploy`
- custom domain: `choksillmservice.com`

The repository includes a `wrangler.jsonc` file that points the deploy to `./public`.
