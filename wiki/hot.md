---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-07-06
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: staging `dev:neat-starfish-33` is green for Mistral V2 with only `cover_letter_premium_prompt_v2=1`; quality repair is OFF and production full GO is not approved.
- MCP / ChatGPT App SDK: PR99/PR285 through PR108/PR299, PR300, PR301, PR302, PR303, and PR304 are merged after PR94 ownerless pre-auth creation, PR95 owner binding, PR96 authorization-code issuance, PR96.1 redirect URI normalization, PR97 code redemption, and PR98 access-token issuance. PR304 proves the local/private-beta connector boundary through an ephemeral Cloudflare quick tunnel and real ChatGPT connector. PR305 is draft/proof-only for durable `https://mcp.twoweeks.ai/mcp`: the route/OAuth/token/MCP/read-side ladder passes directly through the named Cloudflare tunnel, local Clerk sign-in rendered after `VITE_CLERK_PUBLISHABLE_KEY` was loaded, stale Clerk `__session` owner-binding recovery was fixed in `fb17e6cc6171f3e54baa805c39eb5e34728f5b0a`, and the latest ChatGPT UI attempt returned to ChatGPT callback with safe query keys `code,state` but never called `/oauth/token`; classify the remaining activation as `BLOCKED_CHATGPT_UI`. Production `/mcp` can verify digest-backed bearer tokens, apply trusted caller quota, process JSON-RPC `initialize`/`notifications/initialized`/`ping`, expose authenticated metadata-only `tools/list`, accept validated read-only `tools/call`, execute four gated Convex read-only summary queries behind safe-ref/result guards, return explicit read-only summary statuses, require private-beta eligibility, and block public-launch-shaped traffic through launch readiness evidence that includes PR106/PR107 summary review flags; PR300 removes stale PR102 synthetic `tools/call` result metadata from the active boundary; PR301 adds optional diagnostic-only cleanup-review evidence that is not a completeness gate; PR302 materializes safe Stage 3 read-side `applicationContexts` and `applicationPackages` from proposal save/update/delete flows; PR303 records post-merge proof and a cleanup regression; provider calls, write actions, refresh tokens, account-link lifecycle expansion, and public launch remain blocked.

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
- PR104 adds deterministic private-beta eligibility gating after auth/quota/envelope and before policy dispatch.
- PR105 adds launch-readiness/public-launch blocking, and PR295 wires launch-readiness env into the default Vite production route so `publicLaunchRequested` fails closed before evidence completeness.
- PR106 replaces PR102 synthetic production `tools/call` output with gated read-only summary execution for the four existing summary tools.
- PR107 wraps PR106 executor results in a strict post-execution summary status envelope: `OK`, `STALE`, `NO_DATA`, `ONBOARDING_REQUIRED`, `MALFORMED`, `TIMEOUT`, or `DEPENDENCY_MISSING`.
- PR108 hardens launch-readiness evidence so PR106 read-only summary execution and PR107 summary status normalization must be explicitly reviewed before readiness evidence can be complete.
- PR300 removes stale PR102 synthetic production `tools/call` result kind/type/builder/status/phase metadata from the active boundary; PR106/PR107 remain the output/status owners.
- PR301 adds strict optional launch-readiness evidence for PR300 cleanup review; false or missing evidence remains diagnostic-only and does not affect completeness.
- PR302 materializes safe Stage 3 MCP read-side context/package rows from proposal save/update paths and reconciles stale rows on invalid jobs/profiles and proposal deletion without exposing raw CV/job/proposal text.
- PR303 is proof-only: it adds a post-merge audit note plus a regression for owner-profile deletion cleanup, and grants no runtime or production permission.
- PR304 is merged as `d158768d28e418aeca5e176e504b8cf79fb1a8c1`: private-beta ChatGPT connector smoke passed through `https://are-effort-skirts-hints.trycloudflare.com`, but that trycloudflare URL is ephemeral and not a durable production deployment.
- PR305 is draft/proof-only: durable `mcp.twoweeks.ai` route/OAuth/token/MCP/read-side proof passes; local Clerk sign-in now renders with `VITE_CLERK_PUBLISHABLE_KEY`; stale Clerk `__session` owner-binding retry is fixed in `fb17e6cc6171f3e54baa805c39eb5e34728f5b0a`; final ChatGPT UI activation is blocked after callback before `/oauth/token`, so use ChatGPT/OpenAI-side diagnostics instead of wildcard redirects or repeated connector recreation.
- Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, PR98, PR99, PR99.1, PR99.2, PR99.3, PR100, PR101, PR102, PR103, PR104, PR105, PR295, PR106, PR107, PR108, PR300, PR301, PR302, or PR303.
- The next guarded MCP app PR must preserve PR101 policy, PR103 schema validation, PR104 private beta eligibility, PR105 launch-readiness blocking, PR106 safe-ref/query-result guards, PR107 status normalization, PR108 launch evidence hardening, PR300 stale synthetic metadata cleanup, PR301 diagnostic-only cleanup-review evidence, and PR302 read-side materialization cleanup guarantees.
- PR80B remains the safe manual application handoff path while ATS authorization is pending; `provider_verified_submitted` remains unreachable.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[sources/2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]], [[sources/2026-07-04-pr304-live-mcp-connector-smoke-checkpoint]], [[sources/2026-07-02-pr302-pr303-mcp-stage3-readside-materialization-checkpoint]], [[sources/2026-07-01-pr301-mcp-readiness-diagnostics-checkpoint]], [[sources/2026-07-01-pr300-mcp-tools-call-synthetic-metadata-cleanup-checkpoint]], [[sources/2026-07-01-pr107-pr108-mcp-summary-status-launch-readiness-checkpoint]], [[sources/2026-07-01-pr106-mcp-readonly-summary-execution-checkpoint]], [[sources/2026-06-30-pr102-pr103-mcp-tools-call-schema-hardening-checkpoint]], [[sources/2026-06-30-pr101-mcp-policy-kernel-tools-list-checkpoint]], [[sources/2026-06-30-pr99-2-mcp-bearer-quota-trusted-caller-checkpoint]], [[sources/2026-06-30-pr99-1-mcp-bearer-verification-hardening-bug-list]], [[sources/2026-06-29-pr98-mcp-oauth-access-token-issuance-checkpoint]], [[sources/2026-06-29-pr96-1-mcp-oauth-redirect-uri-normalization-checkpoint]], [[sources/2026-06-28-pr96-mcp-oauth-production-authorization-code-checkpoint]], [[sources/2026-06-27-pr94-mcp-oauth-production-authorize-preauth-checkpoint]], [[sources/2026-06-27-pr89-pr93-mcp-oauth-production-gate-route-shell-checkpoint]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
