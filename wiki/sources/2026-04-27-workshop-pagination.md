---
title: "Workshop Pagination"
category: source
tags: [workshop, pagination, resume, print, export]
created: 2026-04-27
updated: 2026-04-27
status: current
type: spec
related: [[tech/workshop-pagination]]
---

# Workshop Pagination

## Summary

Technical reference for the validated workshop resume pagination system after experience split and atomic-section continuity passes.

## Key points

- `committedPages` is the source of truth for workshop page boundaries.
- Preview, print, and export should consume committed pages and not re-plan independently.
- `experience` is the only section allowed to split within an entry.
- Atomic sections have continuity and one-item-tail safeguards.
- Workshop geometry currently uses 17/35/18/18mm margins.
- Browser-backed validation remains required for font, wrapping, and page-fit changes.

## Implications

Creates [[tech/workshop-pagination]] and connects to [[tech/preview-to-print-pipeline]].

## Touched pages

- [[tech/workshop-pagination]]
- [[tech/preview-to-print-pipeline]]

