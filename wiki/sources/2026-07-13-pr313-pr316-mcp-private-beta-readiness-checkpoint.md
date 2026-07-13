---
title: "PR313-PR316 MCP Private-beta Readiness Checkpoint"
category: source
tags: [mcp, chatgpt-app, private-beta, subject-digest, smoke, checkpoint]
created: 2026-07-13
updated: 2026-07-13
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# PR313-PR316 MCP Private-beta Readiness Checkpoint

## Merged result

Application PR313 through PR316 are merged into `application-os-foundation`:

| PR | Merge commit | Reviewed head |
| --- | --- | --- |
| PR313 | `d091c066edceaa60ba4e92dd0e215a913aa1d2a3` | `894ee870c24433b3636f9cfe6841a29a694e085b` |
| PR314 | `ccbba0a4a655af942b21c8e9144c432df79cbb38` | `85b8b201f2cae99b09007013398d3c7983220b03` |
| PR315 | `14e5abcdc880ef9ed020fe34e3d5f586819381c4` | `8f58c4637b81e45c6d5d8dec75bd9a2b7ff142e3` |
| PR316 | `bbd96b5cbaa3f7a24908ed51b001183b62119001` | `0c63c234f004ac4fbd853eb6aebf328ebf6bc758` |

PR316's merge commit is the current target for this checkpoint. The merged runtime contract uses `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS` as the canonical private-beta eligibility key. Its values must be lowercase SHA-256 digests. Legacy raw-subject configuration must not be recommended or treated as a fallback.

## Fresh public smoke

A fresh credential-free `./run.sh mcp-smoke` passed after all four merges. It verified:

- authorization-server metadata;
- protected-resource metadata;
- MCP `2025-06-18` and `2025-11-25` negotiation;
- the exact six-tool inventory;
- unauthenticated `tools/call` failure remains fail-closed;
- malformed-token failure remains fail-closed.

The smoke used no credential and proves only the public boundary.

## Readiness boundary

- **NOT DONE:** migrate the deployed private-beta environment to `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS` and deploy that configuration. The merged PR314 source contract is not evidence that its digest configuration is live.
- **NOT DONE:** obtain fresh authenticated ChatGPT `tools/list` and `tools/call` proof after the digest migration and deployment.
- No real subject, digest, token, authorization code, secret, email, user identifier, private data, or live OAuth query is recorded in this checkpoint.
- Provider calls, writes, refresh tokens, billing, account-link expansion, shared or production data mutation, non-beta access, and public launch remain blocked.
