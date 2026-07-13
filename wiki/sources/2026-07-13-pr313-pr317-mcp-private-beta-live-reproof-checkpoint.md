---
title: "PR313-PR317 MCP Private-beta Live Reproof Checkpoint"
category: source
tags: [mcp, chatgpt-app, private-beta, subject-digest, oauth, live-proof, checkpoint]
created: 2026-07-13
updated: 2026-07-13
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# PR313-PR317 MCP Private-beta Live Reproof Checkpoint

## Merged result

Application PR313 through PR317 are merged into `application-os-foundation`:

| PR | Merge commit | Reviewed head |
| --- | --- | --- |
| PR313 | `d091c066edceaa60ba4e92dd0e215a913aa1d2a3` | `894ee870c24433b3636f9cfe6841a29a694e085b` |
| PR314 | `ccbba0a4a655af942b21c8e9144c432df79cbb38` | `85b8b201f2cae99b09007013398d3c7983220b03` |
| PR315 | `14e5abcdc880ef9ed020fe34e3d5f586819381c4` | `8f58c4637b81e45c6d5d8dec75bd9a2b7ff142e3` |
| PR316 | `bbd96b5cbaa3f7a24908ed51b001183b62119001` | `0c63c234f004ac4fbd853eb6aebf328ebf6bc758` |
| PR317 | `0ddcfeccef1a0f803c12b227692b85e848e1561b` | `e18e74f40d0ceb9e90f56596374f713f5d6b756f` |

PR317's merge commit is the current target for this checkpoint. The merged runtime contract uses `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS` as the canonical private-beta eligibility key. Its values must be lowercase SHA-256 digests. Legacy raw-subject configuration must not be recommended or treated as a fallback. PR317 keeps the exact six-tool public projection under focused CI coverage without changing the tool catalog or execution permissions.

## Fresh public smoke

A fresh credential-free `./run.sh mcp-smoke` passed after the digest migration and PR317 merge. It verified:

- authorization-server metadata;
- protected-resource metadata;
- MCP `2025-06-18` and `2025-11-25` negotiation;
- the exact six-tool inventory;
- unauthenticated `tools/call` failure remains fail-closed;
- malformed-token failure remains fail-closed.

The smoke used no credential and proves only the public boundary.

## Authenticated live reproof

- The private-beta environment was migrated to `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_SUBJECT_DIGESTS`; no raw subject is part of the documented runtime contract.
- The confidential OAuth client secret was rotated in Infisical and synchronized value-silently into the local runtime digest configuration.
- A fresh connector, `twoweeks-mcp-final-v2-0713`, reached connected state after the migration.
- Targeted storage evidence showed the OAuth token-record count increase from 7 to 8 during that fresh connection, proving that `/oauth/token` completed without recording any token value.
- ChatGPT listed exactly the six existing read-only tools.
- One safe `twoweeks.application_package.summarize` call completed with `status=no_data_available`, schema `mcp_application_package_summary_result`, and version `1`; no private package content was recorded.
- The user confirmed removal of the earlier connector that held the superseded credential.

## Remaining boundary

- No real subject, digest, token, authorization code, secret, email, user identifier, private data, or live OAuth query is recorded in this checkpoint.
- Provider calls, writes, refresh tokens, billing, account-link expansion, shared or production data mutation, non-beta access, and public launch remain blocked.
- Output minimization and the public catalog/submission URL decision remain separate follow-up work.
