---
title: "ChatGPT/App SDK Roadmap"
category: product
tags: [chatgpt-app, apps-sdk, mcp, roadmap, safety]
created: 2026-06-23
updated: 2026-06-27
status: current
valid_from: 2026-06-12
type: roadmap
sources: [2026-06-27-pr87-17d-mcp-oauth-local-dev-route-adapter-checkpoint, 2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint, 2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint, 2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint, 2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint, 2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint, 2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint, 2026-06-25-pr87-15c-mcp-auth-composition-checkpoint, 2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint, 2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint, 2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint, 2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint, 2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint, 2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint, 2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint, 2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint, 2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint, 2026-06-23-release-orchestration-staging-pr87-8-checkpoint, 2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint, 2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89, 2026-06-12-non-production-apps-sdk-exploration-plan, 2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]
related: [[product/manual-application-handoff]], [[product/product-roadmap]], [[product/product-vision]], [[product/ai-product-model]]
---

# ChatGPT/App SDK Roadmap

The ChatGPT/App SDK roadmap is now a current checkpoint page, not just a future plan. The active truth is PR87.8 production-gate reconciliation after PR245, with PR88-PR89 still blocked.

## Current state

The roadmap has moved through the early MCP/App SDK phases and now sits around PR87 / production deployment gate reconciliation plus release stabilization. PR87.17D merged the local/dev-only MCP OAuth route adapter after PR87.17C1 server-only MCP OAuth login-return continuation boundary, PR87.17C0 repo-owned login-return convention, PR87.17B server-only authorization-intent storage, PR87.17A server-only MCP OAuth authorization request boundary, PR87.16 authoritative account-link lifecycle, PR87.15D local/dev runtime auth composition wiring, PR87.15C auth composition, PR87.15B1 server-only account-link lookup adapter, PR87.15B0 canonical storage/index, PR87.15A server-only Stytch bearer verifier boundary, PR87.14B local/dev-only MCP auth discovery and challenge wiring, PR87.14A auth orchestration, PR87.13 auth metadata/policy, and the PR87.12 local/dev fixture-only MCP demo. It does not open production MCP, OAuth callback/token exchange, public account-link API, real Stytch runtime integration, authorization-code issuance, token exchange, production account-link creation, real handlers, or real user data.

PR87.17D is merged. Do not rerun PR87.17D, and do not start PR88 or PR89 from this checkpoint. The next implementation PR must be chosen only after reloading this roadmap and verifying the current lowest-numbered unmerged blocker. Production MCP/OAuth/token/account-link runtime remains blocked pending a separate reviewed gate.

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
