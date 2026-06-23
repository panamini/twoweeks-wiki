---
title: "ChatGPT/App SDK Roadmap PR41-PR89"
category: source
tags: [chatgpt-app, apps-sdk, mcp, roadmap, safety]
created: 2026-06-12
updated: 2026-06-12
status: current
type: roadmap
related: [[product/chatgpt-app-sdk-roadmap]], [[product/manual-application-handoff]], [[sources/2026-06-12-non-production-apps-sdk-exploration-plan]]
---

# ChatGPT/App SDK Roadmap PR41-PR89

## Summary

This staged roadmap extends the ChatGPT/App SDK planning chain through PR41-PR89 with a strict one-PR-at-a-time execution model for safe, reviewable, user-approved job application workflows.

## Key points

- PR41 creates the agent implementation contract before any code work continues.
- PR42-PR52 cover package-only setup, descriptor tests, a disabled skeleton, simulated list/call behavior, and a local non-production demo.
- PR53-PR64 establish auth, consent, redacted audit, retention, privacy tests, and read-only real-data summaries.
- PR65-PR75 define UI/component policy, artifact preview, human approval, revision loops, and export/download.
- PR76-PR80 cover write-action foundations, controlled egress, controlled send, dry-run submit/apply, and one live integration only when explicitly approved.
- PR80B is inserted as the safe manual handoff path while ATS authorization remains pending.
- PR81-PR89 cover limits, secrets, observability, tenancy, billing, security review, deployment, beta, and launch gates.

## Implications

- This roadmap is planning-only unless the specific PR allows runtime behavior.
- Forbidden surfaces remain blocked until a PR explicitly opens them.
- The roadmap should be read together with [[product/manual-application-handoff]] for the PR80B boundary.

## Touched pages

- [[product/chatgpt-app-sdk-roadmap]]
- [[product/manual-application-handoff]]
- [[sources/2026-06-12-non-production-apps-sdk-exploration-plan]]
