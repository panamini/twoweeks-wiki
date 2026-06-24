---
title: "ChatGPT App MCP Auth And Account-Linking Architecture Checkpoint - PR87.11"
category: source
tags: [chatgpt-app, apps-sdk, mcp, auth, checkpoint, pr87-11]
created: 2026-06-24
updated: 2026-06-24
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint]], [[sources/2026-06-23-release-orchestration-staging-pr87-8-checkpoint]]
---

# ChatGPT App MCP Auth And Account-Linking Architecture Checkpoint - PR87.11

## Summary

PR252, [PR87.11: decide MCP auth architecture for ChatGPT account linking](https://github.com/panamini/neyssan/pull/252), merged the docs-only architecture checkpoint for the future ChatGPT Apps SDK MCP auth path. It records Clerk as the Twoweeks app login authority, Stytch Connected Apps as the OAuth bridge, `(issuer, subject)` account linking through server-only link records, and `twoweeks:applications:read` as the first external MCP scope, without enabling runtime OAuth or production MCP behavior.

## Key points

- PR252 merged into `application-os-foundation` as merge commit `d9b47c72dd68dd388561b6c71d50d5952742c761` on 2026-06-24 01:55:07 +0200, verified from local git and GitHub merge result.
- The head SHA before merge was `7d7008c2943986c6b4c8d56f816c9381ffd79a05`.
- The only changed files stayed `docs/decisions/2026-06-24-chatgpt-app-mcp-auth-account-linking-architecture.md` and `docs/audits/2026-06-24-mcp-app-sdk-production-gate-blocker-register.md`.
- GitHub checks were reported green: CI success, Playwright Tests success, CodeRabbit success.
- The unresolved CodeRabbit wording nit on the ADR status banner was fixed in the same branch before merge; the review thread is now resolved.
- The wiki PR251 checkpoint is pushed and `wiki/main` matches `origin/main` at `693d36696f738f00aa21c5c32629f46f1da36b50`.
- No runtime permission is granted by this checkpoint.
- Production `/mcp`, production `tools/list`, production `tools/call`, real handlers, real data, OAuth runtime, outbound/model calls, write actions, PR88, and PR89 remain blocked.
- The PR252 merge did not change any runtime app code or package/lockfile state.

## Implications

PR87.11 is now the durable architecture checkpoint for ChatGPT account linking on the MCP/App SDK track. The next MCP slice must still be a separate runtime implementation decision, not production enablement.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[product/manual-application-handoff]]
- [[hot]]
- [[index]]
