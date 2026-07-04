---
title: "ChatGPT/App SDK Roadmap"
category: product
tags: [chatgpt-app, apps-sdk, mcp, roadmap, safety]
created: 2026-06-23
updated: 2026-07-04
status: current
valid_from: 2026-06-12
type: roadmap
sources: [2026-07-04-pr304-live-mcp-connector-smoke-checkpoint, 2026-07-02-pr302-pr303-mcp-stage3-readside-materialization-checkpoint, 2026-07-01-pr301-mcp-readiness-diagnostics-checkpoint, 2026-07-01-pr300-mcp-tools-call-synthetic-metadata-cleanup-checkpoint, 2026-07-01-pr107-pr108-mcp-summary-status-launch-readiness-checkpoint, 2026-07-01-pr106-mcp-readonly-summary-execution-checkpoint, 2026-06-30-pr102-pr103-mcp-tools-call-schema-hardening-checkpoint, 2026-06-30-pr101-mcp-policy-kernel-tools-list-checkpoint, 2026-06-30-pr99-2-mcp-bearer-quota-trusted-caller-checkpoint, 2026-06-30-pr99-1-mcp-bearer-verification-hardening-bug-list, 2026-06-29-pr98-mcp-oauth-access-token-issuance-checkpoint, 2026-06-29-pr96-1-mcp-oauth-redirect-uri-normalization-checkpoint, 2026-06-28-pr96-mcp-oauth-production-authorization-code-checkpoint, 2026-06-27-pr94-mcp-oauth-production-authorize-preauth-checkpoint, 2026-06-27-pr89-pr93-mcp-oauth-production-gate-route-shell-checkpoint, 2026-06-27-pr87-17d-mcp-oauth-local-dev-route-adapter-checkpoint, 2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint, 2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint, 2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint, 2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint, 2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint, 2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint, 2026-06-25-pr87-15c-mcp-auth-composition-checkpoint, 2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint, 2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint, 2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint, 2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint, 2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint, 2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint, 2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint, 2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint, 2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint, 2026-06-23-release-orchestration-staging-pr87-8-checkpoint, 2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint, 2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89, 2026-06-12-non-production-apps-sdk-exploration-plan, 2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]
related: [[product/manual-application-handoff]], [[product/product-roadmap]], [[product/product-vision]], [[product/ai-product-model]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# ChatGPT/App SDK Roadmap

The ChatGPT/App SDK roadmap is now a current checkpoint page, not just a future plan. The active truth is merged PR304 live private-beta connector smoke after PR303 post-merge proof for PR302 Stage 3 MCP read-side materialization, PR301 diagnostic-only launch-readiness evidence, PR300 stale synthetic `tools/call` metadata cleanup review, PR108 launch-readiness summary evidence hardening, PR107 read-only summary status normalization, PR106 read-only summary execution, PR105 launch-readiness/public-launch blocking, PR104 private beta gating, PR103 schema normalization and matcher hardening, PR102 authenticated `tools/call` read-only boundary, PR101 production MCP policy kernel plus authenticated metadata-only `tools/list`, PR100 authenticated protocol/session envelope, and the PR99 bearer verification hardening chain.

## Current state

The roadmap has moved through PR87.17D local/dev-only MCP OAuth route wiring and then through PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, PR98, PR99, PR99.1, PR99.2, PR99.3, PR100, PR101, PR102, PR103, PR104, PR105, PR295, PR106, PR107, PR108, PR300, PR301, PR302, PR303, and PR304 production OAuth/MCP preparation. PR89 added the controlled production activation boundary. PR90 added bounded operational status. PR92 added the production route preflight with `MCP_OAUTH_PRODUCTION_ROUTE_WIRING=1` and activation dependency readiness. PR93 added guarded inert production route shells for `/oauth/authorize`, `/oauth/callback`, and `/mcp`. PR94 connected production `/oauth/authorize` to existing ownerless pre-auth intent creation. PR95 bound production login-return continuation to the authenticated owner. PR96 issues short-lived digest-backed OAuth authorization codes and redirects the browser back to the validated OAuth client with `code` and original `state`. PR96.1 canonicalizes production redirect URI allowlist entries and keeps invalid raw entries fail-closed. PR97 validates authorization-code token requests without token issuance. PR98 issues bearer access tokens from valid authorization-code token requests, stores only access-token digests, atomically consumes codes with token digest persistence, filters OIDC identity scopes from access-token responses, and hardens expiry, PKCE, scope, and clock-skew proofs. PR99 validates production `/mcp` bearer access tokens against digest-backed storage and returns an authenticated-MCP-blocked response without executing MCP. PR99.1 adds pre-lookup bearer quota, storage-side time trust, binding failures as invalid tokens, and authorization-server metadata. PR99.2 fixes the bearer-verification quota caller boundary so `/mcp` uses the trusted socket address instead of caller-controlled forwarding headers. PR99.3 canonicalizes trusted caller keys and fails closed when trusted remote address is missing. PR100 adds the authenticated MCP JSON-RPC protocol/session envelope. PR101 adds a decision-only production policy kernel and authenticated metadata-only `tools/list`. PR102 adds authenticated production `tools/call` read-only boundary and hardening. PR103 adds schema normalization and matcher hardening for production MCP tool-call validation. PR104 adds deterministic private beta eligibility gating after auth/quota/envelope and before policy dispatch. PR105 adds the launch-readiness/public-launch blocking boundary. PR295 fixes the PR105 runtime wiring so the default Vite production route reads launch-readiness env and treats `publicLaunchRequested` as a fail-closed public-launch block before evidence completeness. PR106 replaces the PR102 synthetic production `tools/call` result for the four summary tools with gated Convex read-only summary execution. PR107 wraps those real read-only summary results in explicit status envelopes. PR108 makes launch-readiness evidence require PR106/PR107 summary review flags before it can be considered complete. PR300 removes stale PR102 synthetic `tools/call` result metadata from the active boundary so read-only output ownership stays with PR106 execution and PR107 status normalization. PR301 adds diagnostic-only launch-readiness evidence for the PR300 cleanup review; malformed non-boolean evidence fails closed, but missing or false diagnostic evidence is not part of readiness completeness. PR302 materializes safe Stage 3 MCP read-side `applicationContexts` and `applicationPackages` from proposal saves/updates and cleans stale packages/contexts when source jobs, profiles, ownership, or proposals become invalid. PR303 records post-merge proof and adds a focused cleanup regression without widening runtime behavior. PR304 proves the private-beta ChatGPT connector path through an ephemeral Cloudflare quick tunnel: OAuth metadata and MCP `tools/list` were reachable, ChatGPT completed OAuth, and `twoweeks.application_package.summarize` returned real read-side data with `status=available` and `count=1`.

PR304 is merged. Do not rerun PR89, PR90, PR92, PR93, PR94, PR95, PR96, PR96.1, PR97, PR98, PR99, PR99.1, PR99.2, PR99.3, PR100, PR101, PR102, PR103, PR104, PR105, PR295, PR106, PR107, PR108, PR300, PR301, PR302, PR303, or PR304, and do not create PR88 retroactively. Provider calls, write actions, refresh tokens, account-link lifecycle expansion, and public launch remain blocked unless a later reviewed PR explicitly opens them.

PR80B manual handoff is already implemented as the safe delivery path while ATS authorization is pending, but live submit/apply remains blocked.

The 2026-06-23 root orchestration checkpoint returned `PR87_8_GATE_STILL_BLOCKED` without requiring a corrective PR. MCP execution beyond the reviewed protocol, metadata, read-only tool-call surfaces, and reviewed local/private-beta connector smoke remains blocked; provider calls, outbound HTTP/model calls, live submit/apply, approved-answer copy, `provider_verified_submitted`, production billing, PR88, non-beta access, and public launch remain blocked.

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
| PR89-PR303 | Production activation gate, operational status, route preflight, guarded production route shells, production `/oauth/authorize` ownerless pre-auth intent creation, production login-return owner binding, production OAuth authorization-code issuance, redirect URI allowlist normalization, authorization-code redemption, access-token issuance, production `/mcp` bearer-token verification, bearer-verification hardening, authenticated protocol/session envelope, policy kernel, metadata-only `tools/list`, read-only `tools/call`, schema matcher hardening, private beta gate, launch-readiness boundary, read-only summary execution, summary status normalization, summary-aware launch-readiness evidence hardening, stale synthetic tools-call metadata cleanup, diagnostic-only cleanup-review evidence, Stage 3 read-side materialization, and post-merge proof merged | `/oauth/authorize` may create ownerless pre-auth intents; login return may bind the authenticated owner and issue a short-lived digest-backed authorization code; production redirect allowlists are canonicalized with invalid entries fail-closed; `/oauth/token` may issue digest-backed bearer access tokens for valid authorization-code token requests; production `/mcp` may verify digest-backed bearer tokens, apply trusted quota, process JSON-RPC `initialize`/`notifications/initialized`/`ping`, expose authenticated metadata-only `tools/list`, accept validated read-only `tools/call`, execute four gated Convex read-only summary queries behind safe-ref validation, return explicit summary statuses, gate access through private beta eligibility, and block public-launch-shaped requests through launch readiness evidence that includes summary execution/status review flags; stale PR102 synthetic `tools/call` result metadata is removed from the active boundary; the PR300 cleanup review can be recorded as optional diagnostic evidence without becoming a completeness gate; proposal save/update/delete paths may materialize safe read-side application context/package metadata for MCP summaries; provider calls, write actions, consent UI, refresh tokens, production account-link lifecycle expansion, and public launch remain blocked |
| PR304 | Live connector smoke | merged as `d158768d28e418aeca5e176e504b8cf79fb1a8c1`; local/private-beta proof through an ephemeral Cloudflare quick tunnel and real ChatGPT connector; OAuth/MCP handshake, `tools/list`, and read-only `application_package` summary reached real read-side data; not a durable production deployment or public launch |
| PR99.1 | MCP bearer verification hardening | caller quota before digest lookup, storage-time trust at route proof boundary, binding failures challenged as invalid tokens, and authorization-server metadata for OAuth discovery; no MCP execution or tool exposure |
| PR99.2 | MCP bearer quota trusted caller boundary | `/mcp` bearer-verification quota uses trusted socket address instead of forwarding headers; next follow-up is canonicalization/fail-closed remote-address hardening |
| PR99.3 | MCP bearer quota caller-key hardening | trusted remote address forms are canonicalized before quota keying and missing trusted remote address fails closed |
| PR100 | Authenticated MCP protocol envelope boundary | minimal JSON-RPC is parsed after bearer verification; `initialize`, `notifications/initialized`, and `ping` are supported without tools execution |
| PR101 | MCP policy kernel plus `tools/list` metadata boundary | decision-only policy kernel and separate metadata projection expose authenticated metadata-only `tools/list`; no tool execution |
| PR102 | `tools/call` read-only boundary plus hardening | merged; known listed read-only tools can be validated through production `tools/call` without provider/write execution |
| PR103 | Schema normalization and matcher hardening | merged; production MCP tool-call argument validation hardened |
| PR104 | Private beta gate | merged; authenticated MCP surfaces require explicit private-beta eligibility before policy dispatch |
| PR105 | Launch readiness/public launch block | merged; public launch remains blocked and PR295 wires the default Vite route to the env-backed readiness config |
| PR106 | Read-only summary execution | merged; four existing summary tools call matching Convex internal summary queries only after auth/quota/beta/readiness/policy/tools-call validation, with safe-ref/result guards and no provider/write/model/outbound behavior |
| PR107 | Read-only summary status normalization | merged; PR106 executor results are wrapped in a strict status envelope for OK, stale, no-data, onboarding, malformed, timeout, and missing-dependency states |
| PR108 | Launch-readiness summary evidence hardening | merged; launch evidence cannot be complete unless PR106 summary execution and PR107 summary status normalization are explicitly reviewed |
| PR300 | Tools-call synthetic metadata cleanup | merged; stale PR102 synthetic result kind/type/builder/status/phase metadata removed from the active boundary while PR106/PR107 remain the real read-only output and status owners |
| PR301 | Launch-readiness cleanup diagnostic evidence | merged; optional strict boolean evidence records PR300 cleanup review without becoming part of readiness completeness |
| PR302 | Stage 3 MCP read-side materialization | merged; proposal save/update/delete paths materialize and reconcile safe context/package rows for MCP summaries without raw CV/job/proposal text |
| PR303 | Stage 3 MCP post-merge proof | merged; proof-only audit and focused regression for owner-profile deletion cleanup, with no runtime permission expansion |

Forbidden runtime and launch surfaces stay blocked unless a later reviewed decision opens them: MCP execution beyond reviewed protocol/metadata/read-only tool-call surfaces, provider calls, real handlers with write effects, real user-data mutation, outbound HTTP, LLM/model calls, export/download/send/submit/apply, approved answer copy, PR80-live, non-beta/public access, and public launch.

## Remaining checklist

### Completed PR99.3-PR105 compressed MCP protocol, metadata, beta, and launch-readiness chain

- [x] PR99.3 canonicalized trusted socket address forms before `/mcp` bearer-verification quota keying.
- [x] PR99.3 fails closed when production `/mcp` bearer verification lacks a trusted remote address.
- [x] PR100 parses minimal JSON-RPC after bearer verification succeeds and supports `initialize`, `notifications/initialized`, and `ping`.
- [x] PR101 centralizes production MCP method eligibility in a decision-only policy kernel.
- [x] PR101 exposes authenticated metadata-only `tools/list`.
- [x] PR102 adds authenticated production `tools/call` read-only boundary plus hardening.
- [x] PR103 adds schema normalization and matcher hardening for production MCP tool-call validation.
- [x] PR104 gates authenticated MCP access behind deterministic private-beta eligibility.
- [x] PR105 adds a launch-readiness boundary that keeps public launch blocked.
- [x] PR295 wires launch-readiness env into the default Vite production MCP route and makes `publicLaunchRequested` block before evidence completeness checks.
- [x] PR106 replaces PR102 synthetic `tools/call` output with gated real read-only summary execution for the four existing summary tools.
- [x] PR107 adds an execution-result freshness/status boundary for PR106's four real read-only summary tools.
- [x] PR108 hardens launch-readiness evidence so PR106/PR107 summary surfaces must be reviewed before evidence is complete.
- [x] PR300 removes stale PR102 synthetic `tools/call` result metadata from the active boundary after PR106/PR107 took ownership of real read-only output and status normalization.
- [x] PR301 adds diagnostic-only launch-readiness evidence for PR300 cleanup review without making that evidence part of completeness.
- [x] PR302 materializes safe Stage 3 MCP read-side application context/package metadata from proposal flows and cleans stale derived rows.
- [x] PR303 records post-merge proof and adds a cleanup regression without changing runtime permissions.
- [x] PR304 is merged: local/private-beta connector smoke passed through ChatGPT and an ephemeral Cloudflare quick tunnel, but public launch and durable deployment remain blocked.
- [x] Provider calls, write actions, refresh tokens, account-link lifecycle expansion, public launch, and UI changes remain blocked.

### Next guarded MCP step

- [ ] Choose the next narrow app-code safety or metadata refinement only after reloading the live roadmap and application code.
- [ ] Only expand real execution behind PR101 policy, PR103 schema validation, PR104 private beta eligibility, PR105 launch-readiness blocking, PR106 safe-ref/query-result guards, PR107 status normalization, and PR108 launch evidence hardening.
- [ ] Keep provider submit/apply, write actions, outbound HTTP/model calls, billing/entitlements, account-link lifecycle expansion, and public launch blocked unless separately approved.

## Sources

- [[sources/2026-07-04-pr304-live-mcp-connector-smoke-checkpoint]]
- [[sources/2026-07-01-pr107-pr108-mcp-summary-status-launch-readiness-checkpoint]]
- [[sources/2026-07-02-pr302-pr303-mcp-stage3-readside-materialization-checkpoint]]
- [[sources/2026-07-01-pr301-mcp-readiness-diagnostics-checkpoint]]
- [[sources/2026-07-01-pr300-mcp-tools-call-synthetic-metadata-cleanup-checkpoint]]
- [[sources/2026-06-30-pr102-pr103-mcp-tools-call-schema-hardening-checkpoint]]
- [[sources/2026-07-01-pr106-mcp-readonly-summary-execution-checkpoint]]
- [[sources/2026-06-30-pr101-mcp-policy-kernel-tools-list-checkpoint]]
- [[sources/2026-06-30-pr99-2-mcp-bearer-quota-trusted-caller-checkpoint]]
- [[sources/2026-06-30-pr99-1-mcp-bearer-verification-hardening-bug-list]]
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
