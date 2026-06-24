---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-06-25
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks is an active job application operating system centered on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: PR230-PR245, PR246, PR248, and PR249 are merged. After stale function-spec sync and cleanup of 28 old invalid `proposalHandoffs`, Convex staging `dev:neat-starfish-33` returned `COVER_LETTER_MISTRAL_V2_STAGING_GREEN`. Only `cover_letter_premium_prompt_v2=1` is enabled on staging; aliases are unset, quality repair is OFF, Qwen stayed legacy-only in the control route, GPT stayed on GPT, and production full GO remains not approved.
- MCP / ChatGPT App SDK: PR87.15A is merged as a server-only Stytch bearer verifier boundary after PR87.14B local/dev-only auth discovery/challenge wiring, PR87.14A auth orchestration, PR87.13 auth metadata/policy, PR87.12 fixture-only local/dev demo, PR87.11 auth/account-linking architecture, and PR87.10 reachability. PR87.8 remains blocked for production exposure. PR80B manual handoff is implemented and remains the safe delivery boundary; production MCP endpoints, production `tools/list`/`tools/call`, runtime verifier wiring, real Stytch/OAuth runtime calls, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- `dev:neat-starfish-33` now has the synced function spec including `mistral-medium-latest` and `qwen3.7-max`; the staging smoke matrix passed 8/8.
- PR87.15A adds the server-only Stytch bearer verifier boundary; PR87.8 is still blocked for production exposure; runtime verifier wiring, OAuth callback/token exchange, production MCP, and future launch-readiness need separate reviewed gates.
- PR80B must not claim provider submission. `provider_verified_submitted` remains unreachable; `user_reported_submitted` is the highest external reported state.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]], [[sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]]
- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]], [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint]], [[sources/2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint]], [[sources/2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint]], [[sources/2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint]], [[sources/2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint]], [[sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]

## Recent Changes

- 2026-06-25: Recorded `MCP_STYTCH_BEARER_VERIFIER_PR87_15A_CHECKPOINT`: PR257 merged the server-only Stytch bearer verifier boundary; CodeRabbit fixes landed in head `00172f63a8a49d28756150e611a5371d615f2de3`; focused verifier tests passed 38/38 and full local-MCP suite passed 59 files / 1377 tests; CodeRabbit, `js-tests`, and `test` were green; `npm run build` remained red only on inherited Convex `_generated` baseline; production MCP, runtime verifier wiring, real Stytch/OAuth runtime calls, OAuth callback/token exchange, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.
- 2026-06-24: Recorded `MCP_AUTH_DEV_ENDPOINT_WIRING_PR87_14B_CHECKPOINT`: PR256 merged local/dev-only MCP auth discovery and challenge endpoint wiring; focused endpoint tests passed 22/22 and full local-MCP suite passed 58 files / 1339 tests; CodeRabbit, `js-tests`, and `test` were green; `npm run build` remained red only on inherited Convex `_generated` baseline; production MCP, real Stytch/OAuth runtime, OAuth callback/token exchange, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.
- 2026-06-24: Recorded `MCP_AUTH_REQUEST_ORCHESTRATOR_PR87_14A_CHECKPOINT`: PR255 merged the local-MCP auth request orchestrator boundary; focused orchestrator tests passed 41/41 and full local-MCP suite passed 58 files / 1331 tests; GitHub CI, Playwright Tests, and CodeRabbit were green; runtime endpoint wiring, production MCP, OAuth, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remained blocked at that checkpoint.
- 2026-06-24: Recorded `MCP_AUTH_POLICY_BOUNDARY_PR87_13_CHECKPOINT`: PR254 merged pure MCP auth metadata and policy boundary; focused boundary tests passed 89/89 and full local-MCP suite passed 57 files / 1290 tests; CodeRabbit reported no actionable comments; docstring coverage stayed advisory; runtime auth wiring, production MCP, OAuth, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.
- 2026-06-24: Recorded `MCP_DEV_FIXTURE_DEMO_PR87_12_CHECKPOINT`: PR253 merged fixture-only local/dev MCP demo; focused endpoint tests passed 17/17 and full local-MCP suite passed 56 files / 1201 tests; MCP Inspector was unavailable and live ChatGPT smoke was not run; production MCP, OAuth, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.
- 2026-06-24: Recorded `MCP_DEV_ENDPOINT_PR87_10_TEST_ONLY_REACHABILITY`: PR251 merged as a one-file test-only checkpoint for the local/dev MCP endpoint; focused endpoint tests and the broader local-MCP suite passed; production MCP, OAuth, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.
- 2026-06-24: Recorded `MCP_AUTH_ACCOUNT_LINKING_PR87_11_CHECKPOINT`: PR252 merged as a docs-only auth/account-linking checkpoint; Clerk remains app login authority, Stytch Connected Apps is the OAuth bridge, `(issuer, subject)` account linking is documented, `twoweeks:applications:read` is the first external scope, and runtime OAuth / production MCP remain blocked.
- 2026-06-24: Recorded `COVER_LETTER_MISTRAL_V2_STAGING_GREEN`: staging function spec synced after stale `proposalHandoffs` cleanup; canonical Mistral V2 flag enabled only on `dev:neat-starfish-33`; 8/8 staging smoke passed; production and quality repair remain not approved/off.
- 2026-06-23: Recorded PR249 merge and staged internal Mistral V2 gate: `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`; production full GO remains separate, quality repair OFF, Qwen legacy-only, GPT unchanged.
