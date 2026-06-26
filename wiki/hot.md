---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-06-27
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: staging `dev:neat-starfish-33` is green for Mistral V2 with only `cover_letter_premium_prompt_v2=1`; quality repair is OFF and production full GO is not approved.
- MCP / ChatGPT App SDK: PR87.17D/PR273 is merged as the local/dev-only MCP OAuth route adapter behind `LOCAL_MCP_DEV_OAUTH_AUTHORIZATION=1` after PR87.17C1/PR269 login-return continuation boundary, PR87.17C0/PR268 login-return convention, PR87.17B/PR267 authorization-intent storage, PR87.17A/PR265 authorization request boundary, PR87.16 account-link lifecycle, PR87.15D runtime composition wiring, PR87.15C auth composition, PR87.15B1 lookup adapter, PR87.15B0 storage, PR87.15A verifier, PR87.14B endpoint challenge wiring, PR87.14A orchestrator, PR87.13 policy, PR87.12 fixture demo, PR87.11 architecture, and PR87.10 reachability.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR87.17D wires the local/dev OAuth route flow: ChatGPT OAuth request -> PR265 validation -> PR271 pre-auth storage -> PR268 Clerk login return -> PR272 owner binding -> PR267 owner-bound intent -> PR269 continuation.
- PR87.17D remains local/dev only behind `LOCAL_MCP_DEV_OAUTH_AUTHORIZATION=1`; it does not open production MCP/OAuth, add Stytch runtime integration, issue OAuth codes, exchange tokens, create production account links, persist sensitive OAuth request data in browser storage, unlock PR88, or unlock PR89.
- PR87.17C1 adds the server-only login-return continuation boundary with `prepareMcpOAuthLoginReturnContinuation` and `resumeMcpOAuthAuthorizationAfterLoginReturn`, digest-only PR267-style ports, one-time owner-bound resume behavior, and no provider/token/code/account-link/production behavior.
- PR87.17C0 defines `mcp_oauth_return`, preserves `/cv` fallback, allows only the fixed local/dev MCP OAuth continuation path with `mcp_oauth_intent`, and adds resolver/SignInPage tests only.
- PR87.17B adds server-only authorization-intent storage with digest-only handles and one-time consume behavior; neither PR87.17B nor PR87.17C0 opens production MCP, OAuth callback/code exchange, consent UI, token persistence, public account-link API, endpoint/Vite lifecycle wiring, real Stytch/Clerk network calls, or real user data.
- Do not rerun PR87.17D. Do not start PR88 or PR89 from this checkpoint; choose the next implementation PR only after reloading the roadmap and verifying the current lowest-numbered unmerged blocker.
- PR87.15B1 adds `buildMcpConvexAccountLinkLookupAdapter` plus bounded lookup query `internalLookupMcpAuthPolicyAccountLinkCandidates`.
- PR87.8 remains blocked for production exposure; OAuth callback/token exchange, production MCP, real handlers, live submit/apply, billing, PR88, and PR89 require separate reviewed gates.
- PR80B must not claim provider submission. `provider_verified_submitted` remains unreachable; `user_reported_submitted` is the highest external reported state.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-27-pr87-17d-mcp-oauth-local-dev-route-adapter-checkpoint]], [[sources/2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint]], [[sources/2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint]], [[sources/2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint]], [[sources/2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint]], [[sources/2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint]], [[sources/2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint]], [[sources/2026-06-25-pr87-15c-mcp-auth-composition-checkpoint]], [[sources/2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint]], [[sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint]], [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]], [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
