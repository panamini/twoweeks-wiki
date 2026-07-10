---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-07-10
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: staging `dev:neat-starfish-33` is green for Mistral V2 with only `cover_letter_premium_prompt_v2=1`; quality repair is OFF and production full GO is not approved.
- MCP / ChatGPT App SDK: PR305 is merged as `f9dd477b116c48f1b223b17e1636876edf3c939f`; follow-up PR306 is merged as `23c2cca9c09ba22c522242305545390dbc1bbea1`. The shared OAuth secret is sourced from Infisical EU Cloud project `twoweeks`, `dev` environment, key `MCP_OAUTH_PRODUCTION_CLIENT_SECRET`; `.infisical.json` contains only non-secret binding. `./run.sh mcp-secret-sync` stores only the SHA-256 digest in root `.env.local` mode `600`, prints no values, and suppresses `xtrace` before env loading and sensitive handling. One-time rotation and connector `twoweeks-mcp-infisical-0710` are proven; the connector uses confidential OAuth `client_secret_post`, lists `search` and `fetch`, and completed safe read-only `search` and `fetch` calls. Direct `/oauth/token` was not separately captured in the current Vite log, so the claim is behavioral rather than a direct network capture.

## Key Active Facts

- PR305 is private-beta proof only. Provider calls, writes, refresh tokens, billing, shared DB mutation, account-link expansion and public launch remain blocked.
- The exact redirect is `https://chatgpt.com/connector/oauth/b7v_6OncLEsg`; wildcard redirects are forbidden.
- Server configuration belongs in ignored root `.env.local` mode `600`. Use `./run.sh mcp-check`, `./run.sh mcp-private-beta`, and `./run.sh reload-env`.
- The active key family is `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_*`; legacy `MCP_PRODUCTION_PRIVATE_BETA_*` aliases are invalid.
- Missing or malformed secret digest never downgrades OAuth to public client `none`; token exchange fails closed while metadata remains `client_secret_post`.
- The shared client secret is sourced from Infisical EU Cloud; collaborators authenticate individually, and the digest cannot recover the secret. The root `.env.local` is canonical; `my-app/.env.local` is for client values only.
- PR306 regression coverage proves that prerequisite, partial-retrieval, post-digest permission, and success paths do not expose the raw secret or either digest under `bash -x`.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR80B remains the safe manual application handoff while ATS authorization is pending; `provider_verified_submitted` remains unreachable.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP / ChatGPT App SDK: [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[sources/2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]], [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
