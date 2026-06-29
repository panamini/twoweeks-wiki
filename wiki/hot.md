---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-06-29
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: staging `dev:neat-starfish-33` is green for Mistral V2 with only `cover_letter_premium_prompt_v2=1`; quality repair is OFF and production full GO is not approved.
- MCP / ChatGPT App SDK: PR98/PR284 is merged as production OAuth access-token issuance after PR94 ownerless pre-auth creation, PR95 owner binding, PR96 authorization-code issuance, PR96.1 redirect URI normalization, and PR97 code redemption. Production `/mcp`, bearer-token verification, `tools/list`, `tools/call`, provider calls, refresh tokens, account-link lifecycle, private beta, and public launch remain blocked.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR87.17D remains local/dev only behind `LOCAL_MCP_DEV_OAUTH_AUTHORIZATION=1`.
- PR94 connects production `/oauth/authorize` to ownerless pre-auth intent creation.
- PR95 binds production login-return continuation to the authenticated owner.
- PR96 consumes owner-bound authorization intent and issues digest-backed short-lived authorization codes.
- PR96.1 canonicalizes production OAuth redirect URI allowlist entries and preserves invalid raw entries fail-closed.
- PR98 issues bearer access tokens from valid authorization-code token requests, persists only token digests, consumes the authorization code atomically with token digest persistence, adds expired access-token cleanup, filters OIDC identity scopes from the token response, and hardens storage/PKCE/scope/clock-skew proofs.
- Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, or PR98.
- The next narrow app PR should be PR99 production MCP bearer-token verification boundary: validate access tokens for `/mcp` requests while keeping MCP execution, `tools/list`, `tools/call`, provider calls, refresh tokens, account-link lifecycle, private beta, and public launch blocked.
- PR80B remains the safe manual application handoff path while ATS authorization is pending; `provider_verified_submitted` remains unreachable.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[sources/2026-06-29-pr98-mcp-oauth-access-token-issuance-checkpoint]], [[sources/2026-06-29-pr96-1-mcp-oauth-redirect-uri-normalization-checkpoint]], [[sources/2026-06-28-pr96-mcp-oauth-production-authorization-code-checkpoint]], [[sources/2026-06-27-pr94-mcp-oauth-production-authorize-preauth-checkpoint]], [[sources/2026-06-27-pr89-pr93-mcp-oauth-production-gate-route-shell-checkpoint]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
