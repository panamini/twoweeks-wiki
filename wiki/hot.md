---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-07-13
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: staging `dev:neat-starfish-33` is green for Mistral V2 with only `cover_letter_premium_prompt_v2=1`; quality repair is OFF and production full GO is not approved.
- MCP / ChatGPT App SDK: PR322 selected the stable MCP public catalog/submission URL `https://mcp.twoweeks.ai/mcp` and added a fail-closed launch-readiness evidence bit. Public launch remains blocked; OAuth/auth/tool catalog/runtime reachability unchanged.

## Key Active Facts

- PR322 selected the stable MCP catalog/submission URL `https://mcp.twoweeks.ai/mcp` and added a fail-closed launch-readiness evidence bit. Public launch remains blocked.
- PR305 is connected in ChatGPT as a private/development connector; `tools/list` and one safe read-only `tools/call search` are live-proven. This does not authorize provider calls, writes, refresh tokens, billing, production/shared DB mutation, account-link expansion, or public launch.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR87.17C2 adds the docs-only pre-auth ownership decision and browser-storage policy, records `TWO_PHASE_PREAUTH_INTENT_REQUIRED`, and keeps route/runtime/provider/token/code/account-link behavior blocked until later slices.
- PR87.17C0 defines `mcp_oauth_return`, preserves `/cv` fallback, allows only the fixed local/dev MCP OAuth continuation path with `mcp_oauth_intent`, and adds resolver/SignInPage tests only.
- PR87.17B adds server-only authorization-intent storage with digest-only handles and one-time consume behavior; neither PR87.17B nor PR87.17C0 opens production MCP, OAuth callback/code exchange, consent UI, token persistence, public account-link API, endpoint/Vite lifecycle wiring, real Stytch/Clerk network calls, or real user data.
- PR87.15B1 adds `buildMcpConvexAccountLinkLookupAdapter` plus bounded lookup query `internalLookupMcpAuthPolicyAccountLinkCandidates`.
- PR87.8 remains blocked for production exposure; OAuth callback/token exchange, production MCP, real handlers, live submit/apply, billing, PR88, and PR89 require separate reviewed gates.
- PR80B must not claim provider submission. `provider_verified_submitted` remains unreachable; `user_reported_submitted` is the highest external reported state.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- MCP / ChatGPT App SDK: [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[product/chatgpt-app-sdk-roadmap]], [[sources/2026-07-13-pr322-mcp-public-catalog-url-checkpoint]], [[product/manual-application-handoff]], [[sources/2026-06-26-pr87-17c2-mcp-oauth-preauth-ownership-checkpoint]], [[sources/2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint]], [[sources/2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint]], [[sources/2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint]], [[sources/2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint]], [[sources/2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint]], [[sources/2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint]], [[sources/2026-06-25-pr87-15c-mcp-auth-composition-checkpoint]], [[sources/2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint]], [[sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint]], [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]], [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
