---
title: "Non-production ChatGPT App Prototype Plan"
category: source
tags: [mcp, chatgpt-app, prototype, safety, plan]
created: 2026-06-11
updated: 2026-06-11
status: current
type: analysis
---

# Non-production ChatGPT App Prototype Plan

**Type** : Planning / readiness spec
**Date** : 2026-06-11
**URL** : source locale `raw/PR28 - Non-production ChatGPT App Prototype Plan.md`

## Summary

This plan defines a bounded, non-production prototype path for a future ChatGPT App integration using only existing Local MCP boundaries, with execution intentionally disabled.

## Key points

- PR28 is strictly docs-only and plan-only: no server, no ChatGPT SDK, no handlers, no remote transport, and no API routes.
- The prototype remains local-only, mock-only, non-runnable, and review-only.
- Allowed activities stay at candidate/tool-definition level (candidate tools, gates, copy, redaction fixtures, and review-state mapping).
- `PR20` and `PR27`/`PR27.1` are required review/preflight gates before any future runnable surface is allowed.
- Safe outputs are limited to non-sensitive summaries, bounded statuses, and synthetic fixture-style text.
- Forbidden outputs include real resume/cover letter/job text, private facts, raw arguments, user/session identifiers, or transport/submit/apply actions.
- `ready_for_internal_review` is explicitly not production/execution readiness.

## Guardrails introduced

- All prototype work stays in Plan boundary with `Build` and `Deploy` phases fully blocked.
- `PR28` blocks persistence, handler execution, network transport, authentication, and outbound actions.
- Visibility and review behavior inherits from PR25/PR27/PR27.1 constraints.
- Privacy redaction and copy correctness are sourced from PR24 and PR26, with no improvised text.

## Risks

- Accidentally treating documentation as executable runtime behavior.
- Promotion confusion around `ready_for_internal_review` as execution permission.
- Tool visibility widening before PR25 + PR27.1 checks.

## Touched pages

- none
