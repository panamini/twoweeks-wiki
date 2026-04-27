---
title: "Typography Token Audit Table"
category: source
tags: [typography, tokens, workshop, planner, renderer]
created: 2026-04-27
updated: 2026-04-27
status: current
type: analysis
related: [[tech/workshop-token-parity]], [[design/document-token-contract]]
---

# Typography Token Audit Table

## Summary

Typography-focused audit showing where the active workshop renderer and planner do not share one complete type contract.

## Key points

- Body and heading font families are used by renderer but not modeled by planner.
- Letter-spacing, text-transform, heading line-height offsets, meta roles, and skill-chip wrapping are not fully modeled.
- Renderer references `--text-label-*` vars that the preview serializer does not emit.
- Canonical `flow.type.meta` exists, but active workshop preview does not use dedicated meta typography.
- The observed mismatch is real planner/render drift caused by missing typography-token integration, not merely natural font variation.

## Implications

Updates [[tech/workshop-token-parity]].

## Touched pages

- [[tech/workshop-token-parity]]
- [[design/document-token-contract]]

