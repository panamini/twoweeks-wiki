---
title: "MCP Stage 3 Read-side Materialization Checkpoint - PR302/PR303"
category: source
type: checkpoint
created: 2026-07-02
updated: 2026-07-02
status: current
tags: [mcp, chatgpt-app, apps-sdk, read-side, application-package, production-gate]
---

# MCP Stage 3 Read-side Materialization Checkpoint - PR302/PR303

PR302 merged Stage 3 MCP read-side materialization for safe application package summaries. PR303 then merged the post-merge proof record and a focused cleanup regression.

This checkpoint records the merged state without opening any blocked runtime or launch surface.

## Merge facts

- PR302: <https://github.com/panamini/neyssan/pull/302>
  - Title: `Add MCP Stage 3 read-side materialization`
  - Final head SHA: `2ced854ff64d2707c73b97e827297f2d2fe3306b`
  - Merge commit SHA: `262444e5ea4ed24e493fd93599452ddb56a0c317`
  - Merged at: `2026-07-02T17:44:20Z`
  - Base branch: `application-os-foundation`
- PR303: <https://github.com/panamini/neyssan/pull/303>
  - Title: `Post-merge Stage 3 MCP proof`
  - Final head SHA: `303b1859b99d0d50aaed963085d69502e87ffb12`
  - Merge commit SHA: `f63d35dc6f8ae765d9afb004991e2a2aeb6c5679`
  - Merged at: `2026-07-02T18:47:48Z`
  - Base branch: `application-os-foundation`

## Merged state

Proposal save/update paths can now best-effort materialize safe Stage 3 MCP read-side rows:

- `applicationContexts`
- `applicationPackages`

The materialized package is safe metadata and hashes only. It is designed for read-only MCP summaries and does not expose raw CV, profile, job, proposal, provider output, prompt, secret, file bytes, emails, Clerk ids, or private storage ids through the MCP summary surface.

PR302 also reconciles stale deterministic derived rows when a proposal's source job/profile/ownership becomes invalid or when a proposal is deleted. Orphan contexts are removed only when no remaining package, run, or artifact references them.

PR303 adds a repo-local proof audit and a focused regression for the owner-profile deletion cleanup case. It is proof-only and does not change production permissions.

## Still blocked

PR302 and PR303 do not unlock provider calls, write actions beyond existing proposal persistence, outbound HTTP/model calls, refresh tokens, account-link lifecycle expansion, production/shared database access, public launch, UI changes, export/download/send/submit/apply, approved-answer copy, billing/entitlements, or schema/dependency expansion.

## Verification recorded

PR302:

- Focused materialization tests passed locally before merge.
- Related MCP/ref/summary and proposal compatibility tests passed.
- TypeScript check passed.
- `git diff --check` passed.
- GitHub checks passed: CI `js-tests`, Playwright `test`, Semgrep.
- Review-bot findings were addressed before merge.

PR303:

- Exact post-merge proof PR changed only the audit note and one focused regression test.
- Local TypeScript and diff checks passed; local Vitest collection was blocked in the isolated worktree because ignored Convex generated bindings were absent and generation requires deployment configuration.
- GitHub checks passed on latest head: CI `js-tests`, Playwright `test`, Semgrep.
- CodeRabbit full review completed.
- Qodo updated review to latest head with no new findings after the doc portability fix.
- Codex Review found no major issues on latest head `303b1859b9`.

## Next state

The next MCP/App SDK app-code slice should remain narrow and preserve the PR101 policy kernel, PR103 schema validation, PR104 private beta gate, PR105 launch-readiness blocking, PR106 safe-ref/query-result guards, PR107 status normalization, PR108 launch evidence hardening, PR300 stale synthetic metadata cleanup, PR301 diagnostic-only evidence boundary, and PR302 read-side materialization cleanup guarantees.

Provider calls, write actions, refresh tokens, production account-link lifecycle expansion, billing/entitlements, and public launch remain blocked.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
