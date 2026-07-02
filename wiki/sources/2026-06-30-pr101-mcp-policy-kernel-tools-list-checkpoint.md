---
title: "MCP Policy Kernel And Tools List Metadata Checkpoint - PR101"
category: source
type: checkpoint
created: 2026-06-30
updated: 2026-06-30
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, production-gate, tools-list, policy]
---

# MCP Policy Kernel And Tools List Metadata Checkpoint - PR101

PR290 merged PR101 into `application-os-foundation` after the PR99.3 quota caller-key hardening and PR100 authenticated MCP protocol envelope boundary.

This checkpoint records the compressed MCP/App SDK state after production `/mcp` moved from authenticated protocol shell to policy-governed metadata-only `tools/list`.

## Merge facts

- PR288: <https://github.com/panamini/neyssan/pull/288>
  - Title: `PR99.3: harden MCP bearer quota caller key canonicalization`
  - Final head SHA: `68561c89bd8f587febdefb6cfd6a1363421cba57`
  - Merge commit SHA: `f1b233b0069b12872ea25ffc7c3594eba956ffdf`
  - Merged at: `2026-06-30T12:17:08Z`
- PR289: <https://github.com/panamini/neyssan/pull/289>
  - Title: `PR100: add authenticated MCP protocol and session envelope boundary`
  - Final head SHA: `6b928f83df30279743b253886cf656979b82fade`
  - Merge commit SHA: `dc02d692a47be673ade48ba5a1de1842807532da`
  - Merged at: `2026-06-30T14:23:16Z`
- PR290: <https://github.com/panamini/neyssan/pull/290>
  - Title: `PR101: add MCP policy kernel and tools/list metadata boundary`
  - Final head SHA: `367e52fa795a4432a1d121736ede3b57f8a41725`
  - Merge commit SHA: `44c70ddcad5f4bcf36e5076ec0a7c67a0facf395`
  - Merged at: `2026-06-30T16:11:31Z`
  - Base branch: `application-os-foundation`

## PR101 merged state

Production `/mcp` now has:

- digest-backed bearer verification and trusted caller quota before protocol handling;
- a server-only authenticated protocol envelope extracted from the route adapter;
- a decision-only production MCP policy kernel;
- a separate production tools-list projection layer;
- JSON-RPC `initialize`, `notifications/initialized`, and `ping`;
- authenticated metadata-only `tools/list`.

The `tools/list` surface is intentionally inert. It exposes read-only metadata and does not expose raw tokens, token digests, authorization codes, owner IDs, account-link IDs, storage IDs, provider IDs, executable handlers, functions, network endpoints, or secrets.

## Still blocked

PR101 does not unlock `tools/call`, MCP execution, provider calls, outbound HTTP/model calls, real user-data access, write actions, send/submit/apply/export/download, refresh tokens, production account-link lifecycle expansion, private beta, public launch, or UI changes.

## Next state

The next app PR should be PR102: `tools/call` read-only boundary plus hardening.

PR102 may introduce authenticated `tools/call` for known listed tools only if it remains strictly read-only, schema-validated, bounded, audited, and disconnected from provider submission, write actions, network/model calls, private beta, and public launch.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
