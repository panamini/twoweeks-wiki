---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-06-23
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks is an active job application operating system centered on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: PR230-PR245, PR246, PR248, and PR249 are merged. PR249 records `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`, but the 2026-06-23 root rollout attempt returned `STAGING_BLOCKED`: authorized Convex access to `dev:neat-starfish-33` was unavailable. No flags changed, no deployed smoke ran, production was untouched, quality repair remains OFF, Qwen remains legacy-only, and GPT remains unchanged.
- MCP / ChatGPT App SDK: PR87.8 returned `PR87_8_GATE_STILL_BLOCKED` with no PR needed. PR80B manual handoff is implemented and remains the safe delivery boundary; production MCP endpoints, `tools/call`, OAuth, real handlers, live submit/apply, approved-answer copy, billing, PR88, and PR89 remain blocked.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR249 local/staged evidence was clean, but deployed staging rollout is unverified until Convex access can read/apply flags and prove revision.
- PR87.8 is reviewed and still blocked for production exposure; future launch-readiness needs a separate reviewed gate.
- PR80B must not claim provider submission. `provider_verified_submitted` remains unreachable; `user_reported_submitted` is the highest external reported state.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]], [[sources/2026-06-23-cover-letter-quality-pr249-staged-internal-gate]]
- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]], [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]

## Recent Changes

- 2026-06-23: Root orchestration returned `STAGING_BLOCKED` for internal Mistral V2 rollout due Convex auth boundary and `PR87_8_GATE_STILL_BLOCKED` for MCP/App SDK; no app PR opened, no production change.
- 2026-06-23: Recorded PR249 merge and staged internal Mistral V2 gate: `COVER_LETTER_MISTRAL_V2_READY_FOR_INTERNAL_STAGING_ONLY`; production full GO remains separate, quality repair OFF, Qwen legacy-only, GPT unchanged.
