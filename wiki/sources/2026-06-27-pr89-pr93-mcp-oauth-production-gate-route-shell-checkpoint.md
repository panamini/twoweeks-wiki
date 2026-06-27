---
title: "MCP OAuth Production Gate And Route Shell Checkpoint - PR89-PR93"
category: source
type: checkpoint
created: 2026-06-27
updated: 2026-06-27
status: current
tags: [mcp, chatgpt-app, apps-sdk, auth, oauth, production-gate, route-adapter, checkpoint]
---

# MCP OAuth Production Gate And Route Shell Checkpoint - PR89-PR93

PR274, PR275, PR276, and PR277 moved the MCP OAuth production rail from local/dev-only route wiring to guarded production route shells behind explicit production gates.

This checkpoint supersedes the PR87.17D local/dev-only state for production gating, but it does not unlock real OAuth execution.

## Merge facts

- PR274: <https://github.com/panamini/neyssan/pull/274>
  - Title: `PR89: controlled MCP OAuth production activation boundary`
  - Final merged head SHA: `7f2e0f52cc2d934f2094317cbbebcf60efb3cd8e`
  - Merge commit SHA: `a1b7c01c05a5a2288a3ae6ab97cd5320844252f8`
  - Merged at: `2026-06-27T03:39:08Z`
- PR275: <https://github.com/panamini/neyssan/pull/275>
  - Title: `PR90: production OAuth operational status`
  - Final merged head SHA: `50c0bc940d6a0c05254a51993542039b6ce18ab5`
  - Merge commit SHA: `eb703b7ebc2c8cd8149adb9fb3705cb7aee56f34`
  - Merged at: `2026-06-27T03:45:58Z`
- PR276: <https://github.com/panamini/neyssan/pull/276>
  - Title: `PR92: add production MCP OAuth route preflight boundary`
  - Final merged head SHA: `010f4b6184f45be47709cfa51050240fe71ee893`
  - Merge commit SHA: `d8eafac75fb3b7cbf53ff9732a5815bb85d5fa38`
  - Merged at: `2026-06-27T05:18:05Z`
- PR277: <https://github.com/panamini/neyssan/pull/277>
  - Title: `PR93: wire production MCP OAuth routes behind preflight boundary`
  - Final merged head SHA: `6a5b64c69983a2985a9d146d12057c24d5d89011`
  - Merge commit SHA: `d63f3144dee5260a7d350f3dfde85e00fd4c9046`
  - Merged at: `2026-06-27T06:03:01Z`

## Implementation summary

PR89 added the controlled production activation boundary.

PR90 added the bounded operational status view for production OAuth activation.

PR92 added the production route preflight boundary with the explicit `MCP_OAUTH_PRODUCTION_ROUTE_WIRING=1` exposure flag. The preflight was hardened before PR93 merge so `ready_to_wire` also requires activation dependency ports to be available by shape.

PR93 added guarded inert production route shells for:

- `/oauth/authorize`
- `/oauth/callback`
- `/mcp`

The route shells are fail-closed unless the production preflight returns `ready_to_wire`, and even then they return guarded inert responses instead of running OAuth.

## Validation evidence

- Focused production route/preflight tests passed.
- Related PR89/PR90/PR92/local-dev MCP OAuth suite passed.
- TypeScript `tsc --noEmit` passed.
- Changed-file ESLint passed, including test files with `--no-ignore`.
- `git diff --check` passed.
- Fallow audit reported no introduced issues in changed files.
- CodeRabbit, Qodo, Codex review, and Semgrep passed on PR93 final head.
- GitHub Actions `js-tests` and Playwright jobs failed before runner startup with `runner_id: 0` and no steps, matching external runner/billing/spending-limit availability rather than an app regression.

## Non-permissions

PR89-PR93 do not call Stytch or another provider, run consent, accept authorization codes, issue authorization codes, exchange tokens, create account links, persist tokens, read real user data through production MCP, expose `tools/list`, expose `tools/call`, deploy hosted MCP, change schema, change package manifests, or change lockfiles.

The production route shells exist structurally only as guarded inert handlers.

## Next state

Do not rerun PR89, PR90, PR92, or PR93.

Do not create a PR88 retroactively.

The next narrow implementation PR should be PR94: connect production `/oauth/authorize` to existing pre-auth intent creation behind PR92/PR93 gates. PR94 should reuse PR87.17A authorization request projection, PR87.17C3 pre-auth intent storage, and the existing continuation handle/login-return convention.

PR94 must not call providers, run consent, bind owners, issue authorization codes, exchange tokens, create account links, persist tokens, expose production `tools/list`, or expose production `tools/call`.

PR95 should be the separate production login-return / owner-binding continuation using the existing PR87.17C4 owner-binding logic.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
