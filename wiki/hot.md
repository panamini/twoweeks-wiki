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

- Cover-letter quality: PR310 deterministic replay and PR312 multilingual policy shadow are merged in `application-os-foundation@3f3fb3a4`. Production and replay share the same deterministic preparation/finalization path; policy remains shadow-only, quality repair is OFF, and production full GO is not approved.
- MCP / ChatGPT App SDK: PR305-PR316 are merged; PR316 is current at `application-os-foundation@bbd96b5c`. The credential-free public smoke is green for both supported protocols and six read-only tools. Digest deployment migration and post-migration authenticated ChatGPT proof are not done.

## Key Active Facts

- PR305 is private-beta proof only. Provider calls, writes, refresh tokens, billing, shared DB mutation, account-link expansion and public launch remain blocked.
- The exact redirect is `https://chatgpt.com/connector/oauth/b7v_6OncLEsg`; wildcard redirects are forbidden.
- Server configuration belongs in ignored root `.env.local` mode `600`. Use `./run.sh mcp-check`, `./run.sh mcp-private-beta`, and `./run.sh reload-env`.
- The canonical eligibility key is `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS` with lowercase SHA-256 digests. Legacy raw-subject configuration and `MCP_PRODUCTION_PRIVATE_BETA_*` aliases must not be used.
- Missing or malformed secret digest never downgrades OAuth to public client `none`; token exchange fails closed while metadata remains `client_secret_post`.
- The shared client secret is sourced from Infisical EU Cloud; collaborators authenticate individually, and the digest cannot recover the secret. The root `.env.local` is canonical; `my-app/.env.local` is for client values only.
- PR306-PR311 are merged operational and protocol history; no step opened provider, write, or public surfaces.
- PR313-PR316 merge the digest-based source contract. The public canary does not prove PR314 configuration deployment or post-migration authenticated tools.
- Cover-letter replay currently has two English authored-synthetic fixtures and no French replay fixture. The policy baseline is 84 records / 70 plans / 14 rejections, with 13 distant non-English plans still unanchored; matrix hash `b447e3568abe93f4f42b3419894bb19720583f89f7f60e364ceea2aa22e20260`.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR80B remains the safe manual application handoff while ATS authorization is pending; `provider_verified_submitted` remains unreachable.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP / ChatGPT App SDK: [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[sources/2026-07-13-pr313-pr316-mcp-private-beta-readiness-checkpoint]], [[sources/2026-07-13-pr311-runsh-doctor-regression-closure-checkpoint]], [[sources/2026-07-13-pr309-mcp-protocol-compatibility-checkpoint]], [[sources/2026-07-12-pr308-mcp-private-beta-operational-smoke-checkpoint]], [[sources/2026-07-12-pr307-runsh-collaborator-portability-checkpoint]], [[sources/2026-07-05-pr305-durable-mcp-connector-proof-checkpoint]], [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
