---
title: "Non-production Apps SDK Exploration Plan"
category: source
tags: [mcp, chatgpt-app, apps-sdk, plan, safety, readiness]
created: 2026-06-12
updated: 2026-06-12
status: current
type: analysis
---

# Non-production Apps SDK Exploration Plan

**Type**: planning-only exploration
**Date**: 2026-06-12
**URL**: source locale `raw/PR35 - Non-production Apps SDK Exploration Plan.md`

## Summary

PR35 defines the narrow, safe next step for Apps SDK exploration and keeps execution blocked in Plan-only mode.

## Key points

- Keeps the `OpenAI Apps SDK` integration direction explicit for future work while confirming no runtime build path is allowed in PR35.
- Reiterates blocked surfaces: package installs, MCP SDK installation, MCP server creation, `/mcp`, `tools/list`, `tools/call`, OAuth, connector setup, transport exposure, UI/widget implementation, persistence, deployment, and production submission.
- Reinforces that local fixtures, read-only envelopes, and policy mapping are valid for planning only and not equivalent to protocol execution.
- Maps PR18-PR34 boundary work to the current state and calls out a minimal safe next implementation step: a docs-only MCP server architecture decision.
- Defines required safety gates before any implementation PR: architecture, transport, auth/OAuth, data policy, handler policy, approval/audit, UI/resource policy, threat model, privacy review, and explicit maintainer approvals.

## Implications

- PR35 does not create or approve Apps SDK runtime integration.
- `ready_for_internal_review` remains evidence of planning quality and not execution permission.
- Future PR sequencing and blocked runtime boundaries are now documented for PR planning only.

## Touched pages

- none
