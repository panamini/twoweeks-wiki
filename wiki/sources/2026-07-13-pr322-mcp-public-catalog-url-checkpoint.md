---
title: "MCP Public Catalog URL Decision Checkpoint - PR322"
category: source
type: checkpoint
created: 2026-07-13
updated: 2026-07-13
status: current
tags: [chatgpt-app, apps-sdk, mcp, launch-readiness, checkpoint, public-url]
---

# MCP Public Catalog URL Decision Checkpoint - PR322

PR322, [Decide MCP public catalog URL](https://github.com/panamini/neyssan/pull/322), merged the stable MCP catalog/submission URL decision into `application-os-foundation`.

## Merge facts

- PR: <https://github.com/panamini/neyssan/pull/322>
- Title: `Decide MCP public catalog URL`
- Final merged head SHA: `c9057e313a7997419ac0911504dc502aed379370`
- Merge commit SHA: `783d86f4473b7f00b6ef4f44a33188287d53c69b`
- Merged at: `2026-07-13T19:11:01Z`
- Base after merge: `origin/application-os-foundation` at `783d86f4473b7f00b6ef4f44a33188287d53c69b`
- Stable MCP catalog/submission URL selected: `https://mcp.twoweeks.ai/mcp`
- Runtime effect: fail-closed launch-readiness evidence bit added for public catalog/submission URL review; public launch remains blocked; OAuth/auth/tool catalog/runtime reachability unchanged; no provider/model calls; no live ChatGPT connector reproof.
- QUALITY-EVAL-2C remains separate and is not part of this checkpoint.

## Behavior recorded

PR322 records the stable public MCP catalog/submission URL decision and keeps the checkpoint on the evidence side of the launch gate. It does not widen OAuth, auth, tool catalog, runtime, or provider/model behavior.

## Non-permissions

PR322 does not add or reprove a public launch, provider calls, model calls, OAuth behavior, auth behavior, tool catalog reachability, runtime behavior, account-link changes, or credential changes.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[hot]]
- [[index]]
- [[log]]
