---
title: "Voice Card and UI Copy Audits"
category: source
tags: [brand, voice, ui-copy, audit]
created: 2026-04-27
updated: 2026-04-27
status: current
type: analysis
related: [[design/brand-voice]]
---

# Voice Card and UI Copy Audits

## Summary

Merged voice card plus detailed UI copy audits for Sidebar, JobsPage, CvForge, ProfileReviewCard, and VerbatiCvPreviewPanel.

## Key points

- Canonical visible nouns should be `resume` and `cover letter`; internal identifiers can remain `cv` or proposal-specific.
- UI copy should compress labels, tooltips, empty states, and toasts while preserving accessibility labels where convention matters.
- Debug/dev surfaces are excluded from user-facing copy cleanup.
- Major recurring fixes: remove ellipses, avoid verb padding, use `Try again.` only when retry is safe, and standardize toasts.
- ProfileReviewCard and preview surfaces are the heaviest remaining copy-cleanup clusters.

## Implications

Updates [[design/brand-voice]] and provides source evidence for future copy refactors.

## Touched pages

- [[design/brand-voice]]

