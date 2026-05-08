---
title: "Proposal Style Layer"
category: tech
tags: [proposal, style, tokens, palette, llm-note]
created: 2026-05-06
updated: 2026-05-08
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

There are three different Style 1/2/3 surfaces. They share the user-facing identity, but they do not all read the same field.

### Factory/native document slots

Factory slots live in `my-app/src/lib/document-style-slots.ts`.

- Style 1: `geist-baskervville`, `ink`, `workshop_resume_onecol_ats`
- Style 2: `quiet-editorial`, `ink`, `workshop_resume_twocol_ats`
- Style 3: `ledger-sans`, `ink`, `workshop_resume_twocol_ats`

These are defaults only. If Convex returns a persisted `proposalPresetN`, Settings and CV Forge hydrate from that saved slot first and only use the factory slot for missing fields.

### Settings and CV Forge winner

Settings reads `proposalSettings.getPresets`.

- `presetN === null`: slot source is factory/native.
- `presetN !== null`: slot source is settings/persisted.
- Saved `fontPairId`, `paletteOverride`, `accentHex`, `verbatiStyle`, and signature fields win over factory values.

CV Forge reads the same preset query. Selecting Style N applies the hydrated slot and records metadata with `verbatiStyleSlotSource: "settings"` only when the server returned a persisted preset for that slot. Otherwise it records `factory`.

If the live UI shows an old font such as `studio-grotesk` / Parisienne-Cormorant for Style 2, the first boundary to inspect is the persisted Convex preset/current settings, not the factory slot file.

## Default Model

There is one explicit default action in the Settings UI: `Set as default`.

- Clicking a style card edits that slot's contents.
- Clicking `Set as default` marks that slot as the active default slot.
- The active default is what new documents should start from when no more specific document style exists.
- The active badge should stay attached to the chosen default slot; it should not move just because another slot was edited.

Current live code stores that choice as `proposalActivePresetSlot` and mirrors the active slot into legacy current proposal fields for Proposal Forge compatibility.

The design intent is:

- Settings slot content = font, color, layout, signature, and related defaults for Style 1/2/3.
- Active default slot = the selected default bucket for new documents.
- Existing CV/proposal documents keep their own captured style until the user explicitly re-applies or resets style.

If the badge appears to jump between slots while editing, that is a UI/state bug. The intended model is not “the last edited slot becomes default”; it is “the user chooses a slot, then optionally marks it as default.”

### Proposal Forge winner

Proposal Forge primarily reads `proposalSettings.getCurrent`, not the three preset slots. `savePreset` and `setActivePreset` mirror the active slot into legacy current fields such as `proposalFontPairId` and `proposalVerbatiStyle` so older proposal flows keep working.

That means Proposal Forge can still show an old active style even after factory defaults change if `proposalFontPairId` or `proposalVerbatiStyle.typography` is persisted with an old value.

Proposal bundle defaults remain proposal-safe:

- Style 1 / `swiss_serif` -> `terre`
- Style 2 / `magazine_editorial` -> `cobalt`
- Style 3 / `grid_mono` -> `ink`

Reverse-matching a visual style back to a bundle is only a legacy fallback when no stored `templateBundleId` exists.
Once a proposal has a stored bundle id, that id is the selected base style.

## Live Boundary Note

Problem cause, goal, and fix path for the live Style 1/2/3 bug:

- Goal: keep the shared factory Style 1/2/3 defaults visible in Settings/CV Forge, while still letting saved Convex presets win.
- Cause: `proposalSettings.savePreset` was collecting every `userProfiles` row for a Clerk identity and replacing all of them, which hit Convex's 16 MB read limit and blocked the save. That made Settings look unsaved even when the UI patch was correct.
- What changed: the active profile read/write path now uses the latest indexed `userProfiles` row only, so Settings can persist the slot payload and mirror the active slot without fan-out reads.
- What to inspect if Style 2 still looks wrong: persisted `proposalPreset2`, `proposalFontPairId`, `proposalVerbatiStyle.typography`, or other current fields, not the factory slot file.
- Native Style 2 default remains `quiet-editorial` with the Workshop two-column CV template; Parisienne/Cormorant is a persisted value, not the factory default.

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
