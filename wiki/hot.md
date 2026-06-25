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

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- Cover-letter quality: staging `dev:neat-starfish-33` is green for Mistral V2 with only `cover_letter_premium_prompt_v2=1`; quality repair is OFF and production full GO is not approved.
- MCP / ChatGPT App SDK: PR87.15D/PR263 is merged as local/dev runtime composition wiring after PR87.15C auth composition, PR87.15B1 lookup adapter, PR87.15B0 storage, PR87.15A verifier, PR87.14B endpoint challenge wiring, PR87.14A orchestrator, PR87.13 policy, PR87.12 fixture demo, PR87.11 architecture, and PR87.10 reachability.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR87.15D wires the PR87.15C composed verifier/lookup dependencies into the local/dev Vite MCP runtime behind explicit flags; it does not open production MCP, OAuth callback/code exchange, account-link lifecycle mutation, real Stytch calls, or real user data.
- The next MCP step is Gate87.16A: MCP Inspector local authentication smoke over loopback only, with no branch, PR, wiki mutation, production exposure, HTTPS tunnel, ChatGPT Developer Mode, live Stytch, live Convex, or real user data.
- PR87.15B1 adds `buildMcpConvexAccountLinkLookupAdapter` plus bounded lookup query `internalLookupMcpAuthPolicyAccountLinkCandidates`.
- PR87.8 remains blocked for production exposure; OAuth callback/token exchange, production MCP, real handlers, live submit/apply, billing, PR88, and PR89 require separate reviewed gates.
- PR80B must not claim provider submission. `provider_verified_submitted` remains unreachable; `user_reported_submitted` is the highest external reported state.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- MCP / ChatGPT App SDK: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint]], [[sources/2026-06-25-pr87-15c-mcp-auth-composition-checkpoint]], [[sources/2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint]], [[sources/2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint]], [[sources/2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint]], [[sources/2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
