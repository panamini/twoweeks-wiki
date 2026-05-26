---
title: "Two Weeks Theme Palette"
category: source
tags: [design-system, palette, ui, tokens]
created: 2026-05-25
updated: 2026-05-25
status: current
type: other
related: [[design/elite-design-system]]
---

# Two Weeks Theme Palette

## Summary

Consolidated light and dark theme token proposal for the app shell/chrome layer.

## Key points

- Light mode proposed base:
  - `--bg` `#F1EEE7`
  - `--sf1` `#F6F4EF`
  - `--sf2` `#E9E5DC`
  - `--sf3` `#F8F6F2`
  - `--sfr` `#FFFDF8`
  - `--paper` `#FAF9F5`
  - `--paper-ink` `#15120F`
  - `--text` `#2D2A26`
  - `--strong` `#1A1815`
  - `--muted` `#76726B`
  - `--dim` `#A8A39A`
  - `--accent` `#D47554`
  - `--accent-soft` `rgba(212,117,84,0.12)`
- Dark mode proposed base:
  - `--bg` `#16130F`
  - `--sf1` `#1C1814`
  - `--sf2` `#251F19`
  - `--sf3` `#211C17`
  - `--sfr` `#2A2620`
  - `--paper` `#EFEADC`
  - `--paper-ink` `#1E1A17`
  - `--text` `#D8D0C2`
  - `--strong` `#F1EBDD`
  - `--muted` `#918677`
  - `--dim` `#62584C`
  - `--accent` `#D8805F`
  - `--accent-soft` `rgba(216,128,95,0.14)`
- Mapping note in source: apply this token set to existing `themes.css` / `foundation.css` names and confirm shared token usage.

## Implications

- This is a proposed consolidated set and still needs code mapping before app-wide rollout.
- This source should be treated as evidence for design token alignment discussions and visual audits.
- It is not yet a canonical durable change to the UI implementation.

## Touched pages

- [[design/elite-design-system]]
- [[design/document-token-contract]]
