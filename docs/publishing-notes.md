# Publishing Notes

This file is for preparing the public transparency repo for GitHub and Cloudflare Pages.

## Current Status

- Content drafts exist in `content/`
- Static HTML pages are generated from `content/` into `public/`
- A Git repository has been initialized in this folder
- A public GitHub remote exists for this folder
- A Cloudflare Git-connected static-assets project already exists
- The custom domain `choksillmservice.com` already points at this site

## Pre-Publish Checklist

- confirm no secrets exist in this folder
- confirm no local absolute filesystem paths remain
- confirm no operator-only backup or maintenance details remain
- confirm wording stays clearly non-legal and non-contractual
- confirm the technical doc remains candid about limitations

## Next Cloudflare Setup Step

Confirm the existing Git-connected Cloudflare static-assets project is using:

- production branch: `main`
- build command: `python3 scripts/build_site.py`
- deploy command: `npx wrangler deploy`
- custom domain: `choksillmservice.com`

The repository includes a `wrangler.jsonc` file that points the deploy to `./public`.

## Local Update Flow

Whenever content in `content/` changes:

1. run `python3 scripts/build_site.py`
2. review the generated output in `public/`
3. commit both the source changes and the regenerated output
