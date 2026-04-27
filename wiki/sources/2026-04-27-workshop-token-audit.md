---
title: "Workshop Token Audit"
category: source
tags: [workshop, tokens, planner, renderer, audit]
created: 2026-04-27
updated: 2026-04-27
status: current
type: analysis
related: [[tech/workshop-token-parity]], [[design/document-token-contract]]
---

# Workshop Token Audit

## Summary

Audit of active workshop preview/planner/export boundaries, token usage, hardcoded values, mismatches, stale metadata, and safest cleanup sequence.

## Key points

- The active workshop code boundary is verified and covered by relevant tests.
- Some authoritative template fields are ignored by active renderers or only partially reflected in planner metrics.
- Preview/planner parity depends on duplicated literals for section title reduction and experience heading metrics.
- Canonical bullet padding, project gap, header summary width, density adjustments, and font-var names remain mismatch points.
- Safest cleanup is to centralize duplicated workshop section/experience heading constants without changing numeric values.

## Implications

Creates [[tech/workshop-token-parity]].

## Touched pages

- [[tech/workshop-token-parity]]
- [[design/document-token-contract]]

