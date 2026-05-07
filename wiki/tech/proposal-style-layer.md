---
title: "Proposal Style Layer"
category: tech
tags: [proposal, style, tokens, palette, llm-note]
created: 2026-05-06
updated: 2026-05-06
status: current
valid_from: 2026-05-06
version: v1
related: [[design/document-token-contract]], [[tech/export-pipeline]], [[tech/preview-to-print-pipeline]]
---

# Proposal Style Layer

Scratchpad LLM note for how proposal styles work and how agents should use them.

## Mental Model

Proposal style has two layers:

- **Base style**: the durable user-facing choice, shown as Style 1 / Style 2 / Style 3.
- **Custom edits**: color, font, or layout changes made after choosing a base style.

The base style should stay selected after custom edits. If a user picks Style 3 and changes the font or color, the UI should show `Style 3 · Custom`, not jump to Style 1 because another style happens to share that font.

## Palette Contract

Active palette ids are named product tokens:

| UI color | Palette id | Purpose |
| --- | --- | --- |
| Terre | `terre` | Style 1 default / warm brand accent |
| Cobalt | `cobalt` | Style 2 default / sharper editorial accent |
| Ink | `ink` | Style 3 default / technical neutral accent |
| Sage | `sauge` | alternate calm accent |
| Plum | `plum` | alternate expressive accent |
| Ochre | `ochre` | alternate warm accent |

Legacy ids remain readable for old saved proposals and resumes: `ocre`, `pierre`, `bordeaux`, `encre`.
Do not expose those legacy ids as new palette choices.

## Base Style Mapping

Proposal bundle defaults:

- Style 1 / `swiss_serif` -> `terre`
- Style 2 / `magazine_editorial` -> `cobalt`
- Style 3 / `grid_mono` -> `ink`

Reverse-matching a visual style back to a bundle is only a legacy fallback when no stored `templateBundleId` exists.
Once a proposal has a stored bundle id, that id is the selected base style.

## User Flow

Use this behavior in proposal style UIs:

- Selecting a style applies that bundle's original color, font, and layout.
- Editing color/font/layout preserves the selected base bundle id.
- If the current style differs from the selected bundle defaults, show `Style N · Custom`.
- Show a small reset action next to the style selector only while customized.
- Reset restores the selected bundle defaults and clears the custom state.

## Implementation Pointers

Primary code entrypoints:

- `my-app/src/lib/layout/documentAppearance.ts` owns active and legacy palette metadata.
- `my-app/src/lib/proposal-style-display.ts` exposes proposal palette options for controls.
- `my-app/src/lib/proposal-template-bundles.ts` owns Style 1 / 2 / 3 bundle defaults.
- `my-app/src/components/proposal/ProposalRail.tsx` owns the visible style controls.
- `my-app/src/pages/ProposalForge.tsx` commits proposal-local style changes and preserves/reset bundle identity.

## Verification

Minimum checks after changing this layer:

- `rtk npx vitest run src/components/proposal/__tests__/ProposalRail.style.test.tsx`
- `rtk npx vitest run src/pages/__tests__/ProposalForge.draft-heading-hydration.test.tsx`
- `rtk npx vitest run src/lib/__tests__/proposal-output-draft.test.ts src/lib/__tests__/proposal-template-bundles.test.ts`
- `rtk npx vitest run src/lib/__tests__/proposal-style-choice.test.ts src/lib/__tests__/proposal-render-state.test.ts`
- `rtk npx tsc --noEmit`

