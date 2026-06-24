---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-06-24
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks is an active job application operating system centered on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: PR230-PR245, PR246, PR248, and PR249 are merged. After stale function-spec sync and cleanup of 28 old invalid `proposalHandoffs`, Convex staging `dev:neat-starfish-33` returned `COVER_LETTER_MISTRAL_V2_STAGING_GREEN`. Only `cover_letter_premium_prompt_v2=1` is enabled on staging; aliases are unset, quality repair is OFF, Qwen stayed legacy-only in the control route, GPT stayed on GPT, and production full GO remains not approved.
- MCP / ChatGPT App SDK: PR87.10 is merged as a test-only reachability proof for the local/dev endpoint. PR87.8 remains blocked for production exposure. PR80B manual handoff is implemented and remains the safe delivery boundary; production MCP endpoints, `tools/call`, OAuth, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- `dev:neat-starfish-33` now has the synced function spec including `mistral-medium-latest` and `qwen3.7-max`; the staging smoke matrix passed 8/8.
- PR87.10 added test-only local MCP dev endpoint reachability proof; PR87.8 is still blocked for production exposure; future launch-readiness needs a separate reviewed gate.
- PR80B must not claim provider submission. `provider_verified_submitted` remains unreachable; `user_reported_submitted` is the highest external reported state.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]], [[sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]]
- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]], [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]

## Recent Changes

- 2026-06-24: Recorded `MCP_DEV_ENDPOINT_PR87_10_TEST_ONLY_REACHABILITY`: PR251 merged as a one-file test-only checkpoint for the local/dev MCP endpoint; focused endpoint tests and the broader local-MCP suite passed; production MCP, OAuth, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.
- 2026-06-24: Recorded `COVER_LETTER_MISTRAL_V2_STAGING_GREEN`: staging function spec synced after stale `proposalHandoffs` cleanup; canonical Mistral V2 flag enabled only on `dev:neat-starfish-33`; 8/8 staging smoke passed; production and quality repair remain not approved/off.
- 2026-06-23: Recorded PR249 merge and staged internal Mistral V2 gate: `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`; production full GO remains separate, quality repair OFF, Qwen legacy-only, GPT unchanged.
