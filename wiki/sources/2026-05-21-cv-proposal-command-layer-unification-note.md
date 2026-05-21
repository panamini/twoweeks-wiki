---
title: "Command Layer Unification Note — CV & Proposal Toolbars"
category: source
date: 2026-05-21
status: current
tags: [ui, command-layer, toolbar-density, ask-handle, zoom, proposal-forge, cv-forge]
---

# Command Layer Unification Note — CV & Proposal Toolbars

## Why this was done
- CV Forge toolbar was not following Proposal Forge density and width behavior at low zoom.
- CV Ask handle positioning had CV-specific offsets/branching and jumped across narrow-width breakpoints.
- We needed one stable command-layer behavior to avoid parallel logic divergence and regressions.

## Canonical decision
1. Shared command-layer geometry remains source of truth for both surfaces:
   - toolbar width/placement
   - toolbar density mode (`wide`, `medium`, `compact`, `ultraCompact`)
   - toolbar sticky/normal y (`commandLayerY`)
   - Ask x/y placement
2. Proposal and CV consume the same helper + density logic:
   - Proposal keeps `Edit/Preview`, `Heading`, `Design`, `Templates`, `Draft`.
   - CV keeps `Edit/Preview`, `Sections`, `Design`, `Templates`.
3. Paper-based visual controls must not be remapped by viewport changes:
   - zoom remains user intent value (e.g. `0.30`, `1.00`, `2.00`)
   - viewport collapse changes only layout, never `zoom` value or conversion scale.
4. Ask handle stays icon-only and paper-side:
   - always outside the toolbar
   - shared y anchor with toolbar (`commandLayerY`)
   - horizontal clamp to paper/canvas gutter with minimal drift.
5. No hardcoded one-off CSS offset fixes or per-view hacks; behavior is shared via helper outputs and existing tokens.

## Quality bar for future toolbar work
- Do not add duplicate CV-only toolbar density or Ask placement branches.
- Keep density transitions tied to actual computed natural/available widths and zoom thresholds from the shared helper.
- Keep icon size and padding changes data-driven by density tokens.
- Keep command-layer sticky state in one source; toolbar + Ask must always move together.
- If a regression is seen in Ask/toolbar across width/zoom, first verify:
  1) toolbar density mode
  2) `commandLayerY` calculation
  3) paper rect + canvas rect anchors
  4) shared helper outputs (before adding surface-level CSS tweaks).
- For any future fixes, prefer helper-level changes over component-level exceptions.
