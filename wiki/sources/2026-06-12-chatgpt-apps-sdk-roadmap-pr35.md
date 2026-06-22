---
title: "ChatGPT Apps SDK Roadmap PR33-PR40"
category: source
tags: [mcp, chatgpt-app, apps-sdk, roadmap, planning]
created: 2026-06-12
updated: 2026-06-12
status: current
type: analysis
---

# ChatGPT Apps SDK Roadmap PR33-PR40

**Type**: staged planning artifact
**Date**: 2026-06-12
**URL**: source locale `raw/Roadmap.md`

## Summary

This staged roadmap formalizes a conservative PR ordering from PR33 through PR40 around Apps SDK readiness, where documentation and safety gates come before any implementation.

## Key points

- PR33 (prototype scaffold golden fixtures) is identified as the most immediate next step.
- PR34 (snapshot/regression guard) is potentially foldable into PR33 if coverage is complete.
- PR36 is defined as a docs-only MCP server architecture decision.
- PR37 and PR38 focus on data/privacy and tool contract mapping before implementation.
- PR39 captures integration threat model, and PR40 is the first explicit dependency/approval checkpoint for runtime work.
- PR35 keeps explicit constraints against dependency installs, runtime handlers, transports, auth, connector setup, UI, persistence, deployment, and submission.

## Open questions

- Which owner team signs each safety gate in the follow-on PR sequence?
- Which PR from PR33-PR39 can be safely collapsed without reducing safety evidence?

## Touched pages

- none
