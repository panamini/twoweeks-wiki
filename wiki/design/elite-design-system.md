---
title: "Elite Design System"
category: design
tags: [design-system, chrome, document-layer, tokens, ui, export]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-21-2026-elite-design-system-implementation-handoff, 2026-04-27-claude-light-mode-palette]
related: [[design/document-token-contract]], [[design/brand-voice]], [[design/logo-system]], [[tech/export-pipeline]]
---

# Elite Design System

The active design-system boundary is chrome vs document: application chrome uses Geist sans and quiet surfaces; resume/document rendering may preserve Fraunces or document-specific typography.

## Current state

The confirmed implementation direction is:

- `foundation.css` owns semantic tokens
- UI chrome headings use Geist sans
- document-layer selectors preserve document typography intentionally
- resume preview token overrides must be scoped to resume containers, never global `:root`
- subtle-fill inputs use muted surfaces, transparent 2px default borders, and text-color focus borders
- styled resume exports normalize layout geometry through protected export classes, not style-family body classes

## Boundary rules

| Layer | Surfaces | Font rule |
| --- | --- | --- |
| UI chrome | nav, dialogs, settings, compose forms, workspace titles, cards, toolbar | Geist sans via body/heading tokens |
| Document | resume preview, PDF export, template font catalog | document family via `--font-serif-display` or resolved document appearance |

## Open risks

- workshop export may still emit raw style-family layout classes
- dead style-family CSS selectors may remain after normalized body-class changes
- full test suite, dark-mode sweep, real PDF output, and fresh dev-server verification were not completed in the handoff
- Tailwind semantic token alignment remains a follow-up

## Sources

- [[sources/2026-04-21-2026-elite-design-system-implementation-handoff]]
- [[sources/2026-04-27-claude-light-mode-palette]]

## Related

- [[design/document-token-contract]]
- [[tech/export-pipeline]]

