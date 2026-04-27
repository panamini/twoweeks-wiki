---
title: "Workshop Token Parity"
category: tech
tags: [workshop, tokens, typography, planner, renderer, parity]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-27-workshop-token-audit, 2026-04-27-typography-token-audit-table]
related: [[tech/workshop-pagination]], [[design/document-token-contract]], [[tech/preview-to-print-pipeline]]
---

# Workshop Token Parity

Workshop preview and planner parity is still partly dependent on duplicated literals and incomplete typography-token integration.

## Current state

The active boundary is verified: preview, planner, print, and export all use the workshop committed-page model. The remaining risk is not path ownership; it is whether the planner and renderer use the same typography and spacing contracts.

## Known mismatches

- planner uses `headerSummaryWidthMm`; active renderer does not receive that runtime var
- planner consumes density size adjustments; preview ignores them
- canonical bullet padding exists, preview hardcodes `4.5mm`, and export expects a var that is not populated in the same contract
- preview hardcodes project inner gap while planner uses canonical `projectGapMm`
- section and experience heading numbers are duplicated between renderer and planner
- preview uses legacy font alias fallbacks while export uses canonical font var names
- renderer uses undefined `--text-label-*` vars while the serializer emits caption variables

## Safest next cleanup

The narrowest high-value pass is to centralize duplicated workshop section and experience heading constants shared by `ResumeOneColAtsPage.tsx` and `resumePagination.ts`, without changing numeric values.

Targets:

- section-title reduction `0.95mm`
- experience heading size `+0.2mm`
- experience heading line-height `1.25`
- keep the `0.5mm` planner fit safety adjacent to the same workshop sizing contract

## What not to do casually

- do not retune planner heuristics while centralizing constants
- do not change font families or line heights without browser-backed parity checks
- do not clean serializer aliases before proving no non-workshop consumers depend on them

## Sources

- [[sources/2026-04-27-workshop-token-audit]]
- [[sources/2026-04-27-typography-token-audit-table]]

## Related

- [[tech/workshop-pagination]]
- [[design/document-token-contract]]

