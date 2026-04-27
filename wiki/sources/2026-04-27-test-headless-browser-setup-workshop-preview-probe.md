---
title: "Headless Browser Setup for Workshop Preview Probe"
category: source
tags: [playwright, workshop, preview, probe]
created: 2026-04-27
updated: 2026-04-27
status: current
type: runbook
related: [[howto/headless-workshop-preview-probe]], [[tech/workshop-pagination]]
---

# Headless Browser Setup for Workshop Preview Probe

## Summary

Runbook for using headless Chromium and Playwright to probe the workshop preview route with seeded local storage.

## Key points

- Install Chromium with `npx playwright@latest install chromium`.
- Run the app at `http://127.0.0.1:5173`.
- Seed localStorage with workspace mode, active CV id, document list, and fixture document.
- Navigate to `/cv?id=<fixture-id>`.
- Wait for `[data-testid="resume-template-page"]`, capture screenshots, and count pages with document-page selectors.

## Implications

Creates [[howto/headless-workshop-preview-probe]] and supports [[tech/workshop-pagination]] verification.

## Touched pages

- [[howto/headless-workshop-preview-probe]]
- [[tech/workshop-pagination]]

