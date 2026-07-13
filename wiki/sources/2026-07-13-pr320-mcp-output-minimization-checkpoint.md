---
title: "PR320 MCP Output Minimization Checkpoint"
category: source
tags: [mcp, chatgpt-app, private-beta, output-minimization, privacy, checkpoint]
created: 2026-07-13
updated: 2026-07-13
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[sources/2026-07-13-pr313-pr317-mcp-private-beta-live-reproof-checkpoint]]
---

# PR320 MCP Output Minimization Checkpoint

## Merged result

Application PR320 is merged into `application-os-foundation`:

| PR | Merge commit | Reviewed head |
| --- | --- | --- |
| PR320 | `3710e54f869dba1d457e43b1d33403079c7e7f4f` | `d7f590fcc8d8ede0ce799bd0b90563af1390c4ed` |

PR320 minimizes the model-visible output of the four authenticated read-only summary tools. The tools still return the existing text status content, but runtime `structuredContent` and the advertised output schema now expose only this closed envelope:

```json
{
  "kind": "mcp_readonly_summary_status_result",
  "status": "OK",
  "toolName": "application_package",
  "version": 1
}
```

The allowed status values remain unchanged:

```text
OK, STALE, NO_DATA, ONBOARDING_REQUIRED, MALFORMED, TIMEOUT, DEPENDENCY_MISSING
```

The removed `summary` field previously allowed optional aggregate metadata. After PR320, the model-visible projection no longer exposes counts, categories, timestamps, safe-ref metadata, availability metadata, capabilities, internal kinds, owner state, or nested internal model-visible data for the four summary tools.

## Preserved boundary

- The exact six-tool catalog, order, names, input schemas, OAuth scope, read-only annotations, authentication, private-beta eligibility, policy kernel, and fail-closed behavior remain unchanged.
- `search` and `fetch` remain fixed-catalog compatibility tools and are not behaviorally minimized by PR320.
- Internal read execution remains unchanged; only the final model-visible projection is minimized.
- No OAuth authorization, token exchange, client, session, redirect, metadata, Convex schema/query, provider/model call, write path, refresh token, billing, deployment, or public-launch behavior changed.

## Verification evidence

- GitHub PR: `https://github.com/panamini/neyssan/pull/320`
- GitHub checks passed: CI, Playwright Tests, MCP private-beta offline smoke contract, and Semgrep.
- Codex Review on reviewed commit `d7f590fcc8` found no major issues.
- Local implementation verification reported focused Vitest coverage for the summary normalizer, production route adapter, read-only summary executor, tools-call boundary, and credential-free MCP private-beta smoke.

## Live-proof boundary

No live ChatGPT connector re-proof was run for PR320. The historical PR313-PR317 private-beta proof remains the latest live connector proof. PR320 did not exercise `POST /oauth/token`, live `tools/list`, or live `tools/call`.

## Remaining boundary

- Provider calls, writes, refresh tokens, billing, account-link expansion, shared or production data mutation, non-beta access, and public launch remain blocked.
- The stable public catalog/submission URL decision remains the next separate MCP roadmap item before any submission rail.
