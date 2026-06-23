---
title: "Twoweeks MCP / ChatGPT App SDK Roadmap Checkpoint"
category: source
tags: [chatgpt-app, apps-sdk, mcp, checkpoint, roadmap]
created: 2026-06-23
updated: 2026-06-23
status: current
type: analysis
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89]], [[sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]]
---

# Twoweeks MCP / ChatGPT App SDK Roadmap Checkpoint

## Summary

This checkpoint captures the current roadmap truth for the MCP / ChatGPT App SDK track: PR245 is clean, the roadmap has progressed into PR87 production-gate reconciliation, PR80B manual handoff is already represented, and PR88-PR89 remain blocked.

## Key points

- Current known base is `application-os-foundation` at `2ceb98d071b51e87a368dc3d01f33d7ce147f724`.
- PR245 hardened GPT premium cover-letter finalization and the post-merge flags-off smoke is clean.
- Current feature posture is: small internal Mistral V2 canary only, quality repair off, full production not yet.
- The actual roadmap position is around PR87 production deployment gate reconciliation plus release stabilization and post-PR245 canary planning.
- PR41-PR52, PR53-PR64, PR65-PR67, PR68-PR75, PR76-PR80, and PR81-PR85 are treated as merged in the ledger path summarized by the checkpoint.
- PR86-PR87 are merged as governance/status gates, but the production gate is still blocked.
- PR80-live submit/apply remains blocked, approved answer copy remains blocked, and production billing / entitlements remain blocked.
- PR88 and PR89 remain blocked pending production gate reconciliation and launch readiness.
- The next narrow checkpoint is PR87.8 production gate reconciliation after PR245.

## Implications

- The older early-roadmap view is no longer the current truth surface.
- Manual handoff exists as a current boundary, but live submit/apply still does not.
- Any future launch work has to start by reconciling PR87 blockers and not by jumping to PR88 or PR89.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[product/manual-application-handoff]]
- [[sources/2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89]]
- [[sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]]
