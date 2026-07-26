---
title: "MCP Current-Head Authenticated Summary Reproof Checkpoint - V19"
category: source
type: checkpoint
created: 2026-07-15
updated: 2026-07-15
status: current
tags: [chatgpt-app, mcp, oauth, private-beta, authenticated-proof, commercial-readiness]
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# MCP Current-Head Authenticated Summary Reproof Checkpoint - V19

## Summary

`CC-20260715-mcp-current-head-authenticated-summary-reproof-v19` directly proved the current-head private-beta transport, confidential-client OAuth path, public MCP contract, and exactly one protected read-only tool call. The proof closed the transport/authentication question but did not prove commercial user value because the protected result was `NO_DATA` and the public summary projection remains status-only.

## Directly observed evidence

- Proof checkout HEAD: `0503832f5671b995b0095841104afc2e33b065ee`, clean and tied to the live head used for V19.
- Public OAuth and protected-resource metadata returned `200` for the stable endpoint `https://mcp.twoweeks.ai/mcp`.
- MCP initialization succeeded for exactly `2025-06-18` and `2025-11-25`.
- The ordered catalog contained exactly `search`, `fetch`, `twoweeks.application_package.summarize`, `twoweeks.evidence_graph.summarize`, `twoweeks.resume_variant_plan.summarize`, and `twoweeks.review_cockpit.summarize`.
- All six tools advertised `readOnlyHint=true`, `destructiveHint=false`, `openWorldHint=false`, and scope `twoweeks:applications:read`.
- The four protected summary tools advertised the minimized output contract `kind`, `status`, `toolName`, `version`, with identical required fields and `additionalProperties=false`.
- One connector reconnect was completed. The sanitized token-record count moved from `30` to `31`; no token value or private identity was captured.
- Exactly one protected call was executed: `twoweeks.application_package.summarize` with `mcp-safe-ref:application-package:latest`.
- The bounded result was `kind=mcp_readonly_summary_status_result`, `status=NO_DATA`, `toolName=twoweeks.application_package.summarize`, `version=1`.
- The result contained no `summary` and no private nested data.
- After the proof, the current-head runtime was stopped canonically and the previous private-beta runtime was restored canonically.

## What this proves

- Remote reachability, protocol negotiation, tool discovery, confidential-client OAuth, subject alignment, protected-route authorization, and one read-only invocation work together on the proven head.
- The public schema and result projector remain fail-closed and do not expose raw candidate data, credentials, private identities, or nested private results.
- The stable public endpoint can support a controlled private beta.

## What this does not prove

- No protected tool returned `OK` against a data-bearing user account.
- No end-to-end onboarding path from an empty account to useful MCP data was proven.
- No multi-user beta, sustained reliability, rate-limit behavior, refresh-token continuity, billing/entitlement flow, public directory submission, or public launch was proven.
- The current status-only projection does not yet demonstrate enough model-visible value for a commercial product.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
- [[log]]
