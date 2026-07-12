---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-07-12
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: staging `dev:neat-starfish-33` is green for Mistral V2 with only `cover_letter_premium_prompt_v2=1`; quality repair is OFF and production full GO is not approved.
- MCP / ChatGPT App SDK: PR305 is merged as `f9dd477b116c48f1b223b17e1636876edf3c939f`; PR306 is merged as `23c2cca9c09ba22c522242305545390dbc1bbea1`; PR307 is merged as `736c6193966006e91a7bbbad5ff4b60898dd45fb`. The shared OAuth secret remains in Infisical EU Cloud and local synchronization remains digest-only and `xtrace`-safe. The confidential private connector lists `search` and `fetch` and completed safe read-only calls. `./run.sh doctor [local-fast|mcp-private-beta]` is now the collaborator preflight across macOS/Linux/WSL2. The next guarded slice is PR308 operational stabilization; PR309 authenticated read-only user-data work remains blocked until PR308 and a separate approved contract.

## Key Active Facts

- PR305 is private-beta proof only. Provider calls, writes, refresh tokens, billing, shared DB mutation, account-link expansion and public launch remain blocked.
- The exact redirect is `https://chatgpt.com/connector/oauth/b7v_6OncLEsg`; wildcard redirects are forbidden.
- Server configuration belongs in ignored root `.env.local` mode `600`. Use `./run.sh mcp-check`, `./run.sh mcp-private-beta`, and `./run.sh reload-env`.
- The active key family is `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_*`; legacy `MCP_PRODUCTION_PRIVATE_BETA_*` aliases are invalid.
- Missing or malformed secret digest never downgrades OAuth to public client `none`; token exchange fails closed while metadata remains `client_secret_post`.
- The shared client secret is sourced from Infisical EU Cloud; collaborators authenticate individually, and the digest cannot recover the secret. The root `.env.local` is canonical; `my-app/.env.local` is for client values only.
- PR306 regression coverage proves that prerequisite, partial-retrieval, post-digest permission, and success paths do not expose the raw secret or either digest under `bash -x`.
- PR307 keeps `my-app/.env.local` Vite-only, rejects Docker-client env drift and symlinked MCP secret files, and selects native Linux host networking for cloudflared while Vite remains loopback-only.
- PR308 may add operational read-only smoke coverage only. PR309 must name one existing safe read-side capability and remain separately approved; neither step opens provider/write/public surfaces.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR80B remains the safe manual application handoff while ATS authorization is pending; `provider_verified_submitted` remains unreachable.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP / ChatGPT App SDK: [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[sources/2026-07-12-pr307-runsh-collaborator-portability-checkpoint]], [[sources/2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]], [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
