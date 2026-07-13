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
- MCP / ChatGPT App SDK: PR305-PR317 are merged. The digest-based private-beta configuration is deployed, the V2 confidential connector is connected, `/oauth/token` was observed through a token-record count increase, exactly six read-only tools were listed, and one safe `application_package` summary call completed. `run.sh doctor` remains the collaborator preflight and `run.sh mcp-smoke` the credential-free public canary.

## Key Active Facts

- PR305 is private-beta proof only. Provider calls, writes, refresh tokens, billing, shared DB mutation, account-link expansion and public launch remain blocked.
- The exact redirect is `https://chatgpt.com/connector/oauth/b7v_6OncLEsg`; wildcard redirects are forbidden.
- Server configuration belongs in ignored root `.env.local` mode `600`. Use `./run.sh mcp-check`, `./run.sh mcp-private-beta`, and `./run.sh reload-env`.
- The canonical eligibility key is `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS` with lowercase SHA-256 digests. Legacy raw-subject configuration and `MCP_PRODUCTION_PRIVATE_BETA_*` aliases must not be used.
- Missing or malformed secret digest never downgrades OAuth to public client `none`; token exchange fails closed while metadata remains `client_secret_post`.
- The shared client secret is sourced from Infisical EU Cloud; collaborators authenticate individually, and the digest cannot recover the secret. The root `.env.local` is canonical; `my-app/.env.local` is for client values only.
- PR306 regression coverage proves that prerequisite, partial-retrieval, post-digest permission, and success paths do not expose the raw secret or either digest under `bash -x`.
- PR307 keeps `my-app/.env.local` Vite-only, rejects Docker-client env drift and symlinked MCP secret files, and selects native Linux host networking for cloudflared while Vite remains loopback-only.
- PR308 adds operational read-only smoke coverage only. PR309 fixes protocol compatibility and proves one existing `application_package` read without adding tools or opening provider/write/public surfaces.
- PR311 closes startup-preflight regressions for ports, local Docker, WSL2 tunnel networking, Bash special variables, and strict Vite port binding; it does not alter MCP behavior or the separate cover-letter rail.
- PR313-PR316 establish the digest-only eligibility contract and private-beta readiness checks. PR317 keeps the exact six-tool projection under CI regression coverage.
- The deployed environment now uses the digest key. A rotated Infisical secret and fresh V2 connector re-proved authenticated token exchange, six-tool discovery, and one safe read-only call without exposing private values.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- PR80B remains the safe manual application handoff while ATS authorization is pending; `provider_verified_submitted` remains unreachable.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP / ChatGPT App SDK: [[sources/2026-07-13-pr313-pr317-mcp-private-beta-live-reproof-checkpoint]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[product/chatgpt-app-sdk-roadmap]], [[sources/2026-07-13-pr311-runsh-doctor-regression-closure-checkpoint]], [[sources/2026-07-13-pr309-mcp-protocol-compatibility-checkpoint]], [[product/manual-application-handoff]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
