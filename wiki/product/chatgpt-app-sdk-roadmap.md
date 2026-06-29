---
title: "ChatGPT/App SDK Roadmap"
category: product
tags: [chatgpt-app, apps-sdk, mcp, roadmap, safety]
created: 2026-06-23
updated: 2026-06-29
status: current
valid_from: 2026-06-12
type: roadmap
sources: [2026-06-29-pr98-mcp-oauth-access-token-issuance-checkpoint, 2026-06-29-pr96-1-mcp-oauth-redirect-uri-normalization-checkpoint, 2026-06-28-pr96-mcp-oauth-production-authorization-code-checkpoint, 2026-06-27-pr94-mcp-oauth-production-authorize-preauth-checkpoint, 2026-06-27-pr89-pr93-mcp-oauth-production-gate-route-shell-checkpoint, 2026-06-27-pr87-17d-mcp-oauth-local-dev-route-adapter-checkpoint, 2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint, 2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint, 2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint, 2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint, 2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint, 2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint, 2026-06-25-pr87-15c-mcp-auth-composition-checkpoint, 2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint, 2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint, 2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint, 2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint, 2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint, 2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint, 2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint, 2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint, 2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint, 2026-06-23-release-orchestration-staging-pr87-8-checkpoint, 2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint, 2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89, 2026-06-12-non-production-apps-sdk-exploration-plan, 2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]
related: [[product/manual-application-handoff]], [[product/product-roadmap]], [[product/product-vision]], [[product/ai-product-model]]
---

# ChatGPT/App SDK Roadmap

The ChatGPT/App SDK roadmap is now a current checkpoint page, not just a future plan. The active truth is PR98 production OAuth access-token issuance after PR94 ownerless pre-auth creation, PR95 owner-bound login-return continuation, PR96 authorization-code issuance, PR96.1 redirect URI allowlist normalization, and PR97 code redemption.

## Current state

The roadmap has moved through PR87.17D local/dev-only MCP OAuth route wiring and then through PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, and PR98 production OAuth preparation. PR89 added the controlled production activation boundary. PR90 added bounded operational status. PR92 added the production route preflight with `MCP_OAUTH_PRODUCTION_ROUTE_WIRING=1` and activation dependency readiness. PR93 added guarded inert production route shells for `/oauth/authorize`, `/oauth/callback`, and `/mcp`. PR94 connected production `/oauth/authorize` to existing ownerless pre-auth intent creation. PR95 bound production login-return continuation to the authenticated owner. PR96 issues short-lived digest-backed OAuth authorization codes and redirects the browser back to the validated OAuth client with `code` and original `state`. PR96.1 canonicalizes production redirect URI allowlist entries and keeps invalid raw entries fail-closed. PR97 validates authorization-code token requests without token issuance. PR98 issues bearer access tokens from valid authorization-code token requests, stores only access-token digests, atomically consumes codes with token digest persistence, filters OIDC identity scopes from access-token responses, and hardens expiry, PKCE, scope, and clock-skew proofs.

PR98 is merged. Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, or PR98, and do not create PR88 retroactively. The next narrow implementation PR is PR99 production MCP bearer-token verification boundary: validate `Authorization: Bearer <access_token>` against digest-backed access-token storage for `/mcp` requests while keeping MCP execution, `tools/list`, `tools/call`, provider calls, refresh tokens, account-link lifecycle, private beta, and public launch blocked unless a later reviewed PR explicitly opens them.

PR80B manual handoff is already implemented as the safe delivery path while ATS authorization is pending, but live submit/apply remains blocked.

The 2026-06-23 root orchestration checkpoint returned `PR87_8_GATE_STILL_BLOCKED` without requiring a corrective PR. Runtime MCP production endpoints, production `tools/list`, production `tools/call`, OAuth, real handlers, outbound HTTP/model calls, live submit/apply, approved-answer copy, `provider_verified_submitted`, production billing, PR88, and PR89 remain blocked.

The PR245 reference is a shared branch/readiness checkpoint only. It does not move cover-letter prompt work into this roadmap, and it does not make MCP/App SDK launch work part of PR246.

## Workstream boundary

This page owns Twoweeks MCP, ChatGPT App SDK, Apps SDK readiness, production gates, manual handoff routing, launch blockers, and release sequencing.

It does not own cover-letter prompt V2, Mistral factuality tightening, premium provenance/finalization, Qwen premium behavior, or quality repair. Those belong to [[tasks/2026-06-22-cover-letter-quality-production-roadmap]].

## Details

| Range | Current truth | Boundary |
| --- | --- | --- |
| PR41-PR52 | Merged foundation for non-production ChatGPT/MCP demo | local demo / fixtures |
| PR53-PR64 | Merged auth, consent, privacy, and read-only real integration | no write actions |
| PR65-PR67 | Merged component / UI experience | read-only review UX |
| PR68-PR75 | Merged artifact generation, approval, revision, and export | human approval required |
| PR76-PR80 | Merged write-action foundations and manual handoff path | live submit/apply still blocked |
| PR80B | Implemented safe manual handoff while ATS authorization is pending | provider-verified submission unreachable |
| PR81-PR85 | Merged production-readiness hardening | launch still blocked |
| PR86-PR87 | Merged governance / production gate checkpoints | BLOCKED_PRODUCTION_GATE |
| PR87.8 | Gate reconciled as still blocked after PR245 | no corrective PR opened |
| PR87.10-PR87.17D | Local/dev MCP reachability, auth architecture checkpoint, fixture-only demo, pure auth-policy boundary, auth request orchestrator boundary, local/dev auth discovery/challenge endpoint wiring, server-only Stytch bearer verifier boundary, canonical account-link storage/index contract, server-only account-link lookup adapter, deterministic auth composition boundary, local/dev runtime composition wiring, authoritative server-only account-link lifecycle, MCP OAuth authorization request boundary, MCP OAuth authorization-intent storage, MCP OAuth login-return convention, MCP OAuth login-return continuation boundary, and local/dev-only MCP OAuth route adapter merged | local/dev, storage, lookup, composition, local runtime wiring, internal lifecycle, authorization-request boundary, authorization-intent storage, login-return convention, route-independent continuation boundary, and `LOCAL_MCP_DEV_OAUTH_AUTHORIZATION=1` route adapter only; production MCP/OAuth/token/account-link runtime, real Stytch runtime calls, public account-link API, authorization-code issuance, token exchange, production account-link creation, real handlers, and launch surfaces still blocked |
| PR89-PR98 | Production activation gate, operational status, route preflight, guarded production route shells, production `/oauth/authorize` ownerless pre-auth intent creation, production login-return owner binding, production OAuth authorization-code issuance, redirect URI allowlist normalization, authorization-code redemption, and access-token issuance merged | `/oauth/authorize` may create ownerless pre-auth intents; login return may bind the authenticated owner and issue a short-lived digest-backed authorization code; production redirect allowlists are canonicalized with invalid entries fail-closed; `/oauth/token` may issue digest-backed bearer access tokens for valid authorization-code token requests; production `/mcp` bearer-token verification, MCP execution, provider calls, consent UI, refresh tokens, production account-link lifecycle, `tools/list`, and `tools/call` remain blocked |
| PR88-PR89 | Private beta / public launch | blocked |

Forbidden production surfaces stay blocked unless a later reviewed decision opens them: production endpoints, production `tools/list`, production `tools/call`, OAuth, real handlers, real user data, outbound HTTP, LLM/model calls, export/download/send/submit/apply, production behavior, approved answer copy, and PR80-live.

## Remaining checklist

### PR87.8 - Production gate reconciliation

- [x] Reconcile the production gate after PR245 without changing cover-letter PR246 work.
- [x] Confirm the current blocked surfaces are still blocked: runtime endpoints, tool listing/calls, OAuth, real handlers, outbound HTTP, LLM/model calls, export/download/send/submit/apply, approved answer copy, and PR80-live.
- [x] Confirm PR80B manual handoff remains implemented and is still the only application-delivery path while ATS authorization is pending.
- [x] Document which PR87 blockers are still real after the merged governance/status gates.
- [ ] Decide whether a later MCP/App SDK PR should remain reconciliation-only or become a separately approved launch-readiness slice.

### PR88 - Private beta, blocked

- [ ] Do not start until PR87.8 confirms the production gate is open.
- [ ] Keep private beta copy, approved-answer behavior, and production user data blocked until separately reviewed.
- [ ] Require a launch-readiness review before any production ChatGPT/App SDK exposure.

### PR89 - Public launch, blocked

- [ ] Do not start until private beta has a reviewed success signal.
- [ ] Do not open runtime, billing/entitlements, OAuth, provider submission, or public App SDK behavior by assumption.
- [ ] Treat public launch as a separate release decision, not as a continuation of cover-letter quality work.

## Sources

- [[sources/2026-06-29-pr98-mcp-oauth-access-token-issuance-checkpoint]]
- [[sources/2026-06-29-pr96-1-mcp-oauth-redirect-uri-normalization-checkpoint]]
- [[sources/2026-06-27-pr94-mcp-oauth-production-authorize-preauth-checkpoint]]
- [[sources/2026-06-28-pr96-mcp-oauth-production-authorization-code-checkpoint]]
- [[sources/2026-06-27-pr89-pr93-mcp-oauth-production-gate-route-shell-checkpoint]]
- [[sources/2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint]]
- [[sources/2026-06-27-pr87-17d-mcp-oauth-local-dev-route-adapter-checkpoint]]
- [[sources/2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint]]
- [[sources/2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint]]
- [[sources/2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint]]
- [[sources/2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint]]
- [[sources/2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint]]
- [[sources/2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint]]
- [[sources/2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint]]
- [[sources/2026-06-25-pr87-15c-mcp-auth-composition-checkpoint]]
- [[sources/2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint]]
- [[sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint]]
- [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]]
- [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint]]
- [[sources/2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint]]
- [[sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint]]
- [[sources/2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint]]
- [[sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint]]
- [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]]
- [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
- [[sources/2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89]]
- [[sources/2026-06-12-non-production-apps-sdk-exploration-plan]]
- [[sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]]

## Related

- [[product/manual-application-handoff]]
- [[product/product-roadmap]]
- [[product/product-vision]]
- [[product/ai-product-model]]
