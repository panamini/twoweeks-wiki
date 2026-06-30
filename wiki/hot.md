---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-06-30
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: staging `dev:neat-starfish-33` is green for Mistral V2 with only `cover_letter_premium_prompt_v2=1`; quality repair is OFF and production full GO is not approved.
- MCP / ChatGPT App SDK: PR99/PR285, PR99.1/PR286, PR99.2/PR287, PR99.3/PR288, PR100/PR289, PR101/PR290, PR102/PR291, and PR103/PR292 are merged after PR94 ownerless pre-auth creation, PR95 owner binding, PR96 authorization-code issuance, PR96.1 redirect URI normalization, PR97 code redemption, and PR98 access-token issuance. Production `/mcp` can verify digest-backed bearer tokens, apply trusted caller quota, process JSON-RPC `initialize`/`notifications/initialized`/`ping`, expose authenticated metadata-only `tools/list`, and accept validated read-only `tools/call`; provider calls, write actions, refresh tokens, account-link lifecycle expansion, private beta, and public launch remain blocked.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR87.17D remains local/dev only behind `LOCAL_MCP_DEV_OAUTH_AUTHORIZATION=1`.
- PR94 connects production `/oauth/authorize` to ownerless pre-auth intent creation.
- PR95 binds production login-return continuation to the authenticated owner.
- PR96 consumes owner-bound authorization intent and issues digest-backed short-lived authorization codes.
- PR96.1 canonicalizes production OAuth redirect URI allowlist entries and preserves invalid raw entries fail-closed.
- PR98 issues bearer access tokens from valid authorization-code token requests, persists only token digests, consumes the authorization code atomically with token digest persistence, adds expired access-token cleanup, filters OIDC identity scopes from the token response, and hardens storage/PKCE/scope/clock-skew proofs.
- PR99 validates production `/mcp` bearer access tokens against digest-backed storage and returns authenticated-MCP-blocked without executing MCP.
- PR99.1 hardens bearer verification with pre-lookup quota, storage-side time trust, `401 invalid_token` binding failures, and production authorization-server metadata.
- PR99.2 keys `/mcp` bearer-verification quota from the trusted socket address instead of caller-controlled forwarding headers.
- PR99.3 canonicalizes trusted `/mcp` bearer quota caller keys and fails closed when the route lacks a trusted remote address.
- PR100 adds the authenticated MCP protocol/session envelope boundary for `initialize`, `notifications/initialized`, and `ping`.
- PR101 adds the production MCP policy kernel and authenticated metadata-only `tools/list`.
- PR102 adds the authenticated production `tools/call` read-only boundary plus hardening.
- PR103 adds schema normalization and matcher hardening for production MCP tool-call validation.
- Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, PR98, PR99, PR99.1, PR99.2, PR99.3, PR100, PR101, PR102, or PR103.
- The next narrow app PR should be PR104 private beta gate.
- PR80B remains the safe manual application handoff path while ATS authorization is pending; `provider_verified_submitted` remains unreachable.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[sources/2026-06-30-pr102-pr103-mcp-tools-call-schema-hardening-checkpoint]], [[sources/2026-06-30-pr101-mcp-policy-kernel-tools-list-checkpoint]], [[sources/2026-06-30-pr99-2-mcp-bearer-quota-trusted-caller-checkpoint]], [[sources/2026-06-30-pr99-1-mcp-bearer-verification-hardening-bug-list]], [[sources/2026-06-29-pr98-mcp-oauth-access-token-issuance-checkpoint]], [[sources/2026-06-29-pr96-1-mcp-oauth-redirect-uri-normalization-checkpoint]], [[sources/2026-06-28-pr96-mcp-oauth-production-authorization-code-checkpoint]], [[sources/2026-06-27-pr94-mcp-oauth-production-authorize-preauth-checkpoint]], [[sources/2026-06-27-pr89-pr93-mcp-oauth-production-gate-route-shell-checkpoint]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
