---
title: "MCP Tools Call And Schema Matcher Hardening Checkpoint - PR102/PR103"
category: source
type: checkpoint
created: 2026-06-30
updated: 2026-06-30
status: current
tags: [mcp, chatgpt-app, apps-sdk, tools-call, schema, production-gate]
---

# MCP Tools Call And Schema Matcher Hardening Checkpoint - PR102/PR103

PR291 and PR292 merged the authenticated production `tools/call` read-only boundary and follow-up schema matcher hardening into `application-os-foundation`.

This checkpoint records the compressed MCP/App SDK state after production `/mcp` moved from metadata-only `tools/list` to a validated read-only `tools/call` boundary.

## Merge facts

- PR291: <https://github.com/panamini/neyssan/pull/291>
  - Title: `PR102: add MCP tools/call read-only boundary and hardening`
  - Final head SHA: `2ba0123e83deab840e8a47d04cb661595e63579b`
  - Merge commit SHA: `1a18564865313fad679d9ae2268fb561b1cf16c8`
  - Merged at: `2026-06-30T17:22:53Z`
  - Base branch: `application-os-foundation`
- PR292: <https://github.com/panamini/neyssan/pull/292>
  - Title: `PR103: add MCP schema normalization and matcher hardening`
  - Final head SHA: `3bb75145a32d0c1ffc8871b07211a2061eb1e556`
  - Merge commit SHA: `d269069922cd3e4e183223891f1fb175a9bbe568`
  - Merged at: `2026-06-30T19:58:29Z`
  - Base branch: `application-os-foundation`

## PR102/PR103 merged state

Production `/mcp` now has:

- digest-backed bearer verification and trusted caller quota before protocol handling;
- server-only authenticated protocol envelope and decision-only production policy kernel;
- JSON-RPC `initialize`, `notifications/initialized`, and `ping`;
- authenticated metadata-only `tools/list`;
- authenticated `tools/call` for known listed read-only tools through a production boundary;
- schema normalization and matcher hardening for production tool-call argument validation.

The `tools/call` surface remains a read-only boundary. It validates method params, tool names, payload shape, and arguments before returning safe bounded results. It does not open provider submission, write effects, outbound HTTP/model calls, account-link lifecycle expansion, refresh tokens, private beta, or public launch.

## Still blocked

PR102/PR103 do not unlock provider calls, write actions, real submit/apply/export/send/download behavior, outbound HTTP/model calls, refresh tokens, production account-link lifecycle expansion, private beta, public launch, or UI changes.

## Next state

The next app PR should be PR104: private beta gate.

PR104 should gate access to the already-reviewed authenticated MCP surfaces for an explicit private-beta allowlist, while keeping public launch and all provider/write/runtime expansion blocked.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
