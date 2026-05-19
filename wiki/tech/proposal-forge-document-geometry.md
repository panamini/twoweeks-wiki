---
title: "Proposal Forge Document Geometry"
category: tech
tags: [proposal, forge, geometry, layout, document, toolbar, scrollbar, llm-note]
created: 2026-05-07
updated: 2026-05-20
status: current
valid_from: 2026-05-07
version: v1
related: [[tech/proposal-style-layer]], [[tech/preview-to-print-pipeline]], [[design/document-token-contract]], [[tech/proposal-ai-routing-and-inline-diff]]
---

# Proposal Forge Document Geometry

Canonical LLM note for how the active Proposal Forge document surface is built.
Read this before changing Proposal Forge page width, toolbar width, edit/preview scroll behavior, or workspace breakpoint geometry.

## Core thesis

Proposal Forge is **page-first**.

The visible document page is the object. Workspace chrome, toolbar, rail/panel, preview/edit body, and scrollbars derive from the page geometry. Rail collapse must not make the document feel like a different page.

The current contract is:

1. **Paper visual width** defines the workspace document width.
2. **Toolbar and panel align to that paper width** in collapsed/stacked mode.
3. **Two-pane desktop layout** is page + rail + grid gap; the rail does not resize the page.
4. **Preview and edit share the same page boundary**.
5. **Reading measure is separate from page width**; text stays comfortable and centered.
6. **Scrollbars belong to the page boundary**, not an inner reading column.

## Active code owners

Primary active files:

- `my-app/src/pages/ProposalForge.tsx`
  - workspace-level width variables
  - two-pane vs compact breakpoint
  - Proposal rail/stage grid
  - `--proposal-paper-visual-inline-size`
- `my-app/src/components/ProposalDisplay.tsx`
  - preview/edit document stage
  - page sizing via `useDocumentStageLayout`
  - edit scroll ownership
  - inline AI selection/overlay anchors
- `my-app/src/styles/product-proposal.css`
  - workspace shell geometry
  - toolbar/rail chrome
  - preview/edit scroll styling
  - document stage and editor reading-measure rules
- `my-app/src/hooks/use-document-stage-layout.ts`
  - shared measurement hook for page/stage fit calculations
  - currently unchanged by the canonical Proposal width work

Tests that lock this surface:

- `my-app/src/components/__tests__/ProposalDisplay.css.test.ts`
- `my-app/src/components/__tests__/ProposalDisplay.stage.test.tsx`
- `my-app/src/components/__tests__/ProposalDisplayFooter.css.test.ts`

## Canonical width variable

Proposal Forge has one Proposal-local width authority:

```css
--proposal-paper-visual-inline-size
```

Meaning: the visible document page width inside the Proposal Forge workspace.

In the current implementation, browser width-map audit showed:

- `--forge-page-inline-size` = `860px`
- actual rendered A4 document stage/page width = about `793.7px`

Therefore the Proposal workspace paper visual width is the rendered A4 width at the current app scale, not the legacy 860px frame/gutter width.

Do **not** reintroduce `--forge-page-inline-size` as the Proposal page width unless the design intent changes and a fresh width-map proves it.

## Width hierarchy

Use this hierarchy:

```text
--proposal-paper-visual-inline-size
  -> --proposal-workspace-stage-inline-size
  -> --proposal-workspace-output-shell-inline-size
  -> --document-viewer-shell-inline-size
  -> measured .dasti-document-stage-chassis
  -> ProposalDisplay stage/page dimensions
```

Important consequences:

- `--proposal-workspace-stage-inline-size` should derive from `--proposal-paper-visual-inline-size`.
- `--proposal-workspace-output-shell-inline-size` should derive from `--proposal-paper-visual-inline-size` when the output shell represents the page frame.
- `.dasti-doc-viewer-shell__surface`, `.dasti-proposal-sheet-frame`, `.dasti-document-shell`, `.dasti-proposal-sheet__body--document-viewer`, `.dasti-document-stage-chassis`, and `.dasti-proposal-sheet__preview-stage` must not add competing inline width authority.
- The page may shrink only when the viewport is genuinely too narrow, via `min(100%, var(--proposal-paper-visual-inline-size))` behavior.

## Breakpoint contract

The two-pane breakpoint is around `1420px`.

At and around the breakpoint:

- Expanded desktop: stage/page remains the canonical paper width; the rail sits beside it.
- Compact/stacked: rail/panel stacks above the document, but page width stays the same.
- The breakpoint changes layout ordering/presence, not document identity.

Bad behavior:

```text
1430px expanded: page 794px, toolbar/shell 860px
1410px compact: page/toolbar/panel 794px
```

This makes the document feel like it changes size when the rail collapses.

Good behavior:

```text
1430px expanded: toolbar/shell/stage/viewport/page ~793.7px
1410px compact: toolbar/shell/stage/viewport/page ~793.7px
narrow mobile: all shrink together
```

## Toolbar geometry

The workspace toolbar is part of document chrome, not a full workspace header.

Rules:

- Toolbar max width follows the paper visual width.
- It should not use the rail width, full grid width, or legacy 860px shell when the page is ~793.7px.
- In collapsed mode, the toolbar and panel should read as the same document column width.
- Toolbar controls may remain compact/intrinsic internally; only the toolbar shell aligns to paper width.
- Control metrics (height, spacing, and padding) are driven by shared app-topbar tokens from the design token contract, not local hard-coded literals.

Mental model:

```text
[ toolbar shell: paper width ]
[ page / edit surface: same paper width ]
```

## Rail / panel geometry

The Proposal rail is independent from paper sizing.

Desktop two-pane:

```text
[ paper-width stage ] + [ grid gap ] + [ rail width ]
```

Compact/stacked:

```text
[ rail/panel width = paper visual width ]
[ toolbar width = paper visual width ]
[ document width = paper visual width ]
```

Do not make the rail drive page scale. If the rail needs more internal layout, solve inside the rail.

## Preview mode scroll contract

Preview uses the document viewport as scroll boundary:

- active scroll owner: `.dasti-proposal-sheet__preview-stage`
- it has `data-document-stage="true"`
- overflow mode is controlled through `data-stage-mode="fit" | "overflow"`
- scrollbar styling is thin/narrow:
  - `scrollbar-width: thin`
  - WebKit width/height: `7px`

The scrollbar should sit at the right edge of the visible page/viewport.

Preview should not scroll on an inner text column. Preview content is rendered page content; the page/viewport owns overflow.

## Edit mode scroll contract

Edit mode must match preview scrollbar position while preserving text readability.

Current desired contract:

- outer scroll owner: `.dasti-proposal-sheet__body--document-editor`
- inner textarea: `.dasti-proposal-editor-page__textarea`
- textarea does **not** own visible scroll in workspace document edit mode
- textarea expands to content height
- outer editor body scrolls at the page boundary
- edit scrollbar styling matches preview:
  - `scrollbar-width: thin`
  - WebKit width/height: `7px`

Why this exists:

- If the textarea owns scroll, the scrollbar appears on the centered reading column, too far inside the page.
- If the text column is made full page width, line length becomes too long and quality drops.
- Therefore scroll boundary and text measure are separate concepts.

Correct structure:

```text
page / editor body scroll boundary  -------------------- scrollbar here
  centered editor inner column
    textarea / mirrored text measure  ------------------ no visible scrollbar
```

## Reading measure contract

Page width and reading measure are not the same.

- Page/paper width controls visual document identity and scroll boundary.
- Reading measure controls line length.
- The editable text column stays centered and constrained by existing measure tokens such as `--proposal-document-reading-measure-max` and editor padding variables.

Do not fix scrollbar placement by making text full paper width.

## Inline AI overlay contract

Inline AI selection and proofing overlays depend on the editable text geometry.

Important behavior:

- selection anchors are measured from the textarea
- proofing overlay receives the edit scroll top
- when scroll ownership moves outward, overlay scroll state must follow the outer editor body while the textarea remains geometrically aligned with the text

In practice:

- textarea remains the measurement element for selection geometry
- outer editor body becomes the scroll container for edge fades and scroll position
- textarea `scrollTop` should remain zero in workspace document edit mode

Regression to avoid:

- overlay or floating toolbar anchored to old/inset scroll coordinates
- mirror text drifting from the textarea
- selection toolbar following page scroll incorrectly

## Frame and surface contract

Do not reintroduce a card frame around the paper in workspace preview.

Current design wants:

```text
app/workspace canvas
  quiet document viewport / desktop
    paper page with its own subtle boundary/shadow
```

Avoid:

```text
app canvas -> output card -> framed viewer card -> paper
```

Specifically, collapsed workspace preview should not add border/background/shadow to `.dasti-proposal-sheet__body--document-viewer`.

## Verification checklist

After changing this surface, verify at minimum:

Automated:

```bash
cd my-app && npx tsc --noEmit --pretty false
npm --prefix my-app run test -- src/components/__tests__/ProposalDisplay.stage.test.tsx src/components/__tests__/ProposalDisplay.css.test.ts src/components/__tests__/ProposalDisplayFooter.css.test.ts
```

Browser geometry checks:

- just above `1420px`: toolbar, shell, viewport, page share the same visual width
- just below `1420px`: toolbar, panel, shell, viewport, page still share that width
- narrow viewport: all shrink together, no horizontal layout drift
- preview long document: scrollbar is at page/viewport right edge and thin
- edit long document: scrollbar is at same page edge and thin
- edit text measure remains centered and narrow, not full paper width
- inline AI overlay/selection mirror remains aligned with selected text

## One-prompt implementation guardrail

Use this prompt when asking an LLM to modify this area:

> Work only on active Proposal Forge document geometry. Keep the visible document page as the width authority through `--proposal-paper-visual-inline-size`. Toolbar, panel in compact mode, output shell, document shell, stage chassis, preview viewport, and edit body must derive from that page width. Rail collapse must not resize the page. Preview and edit scrollbars must align to the page right edge and use the same thin scrollbar styling. Do not make edit text full paper width; keep the centered reading measure. Do not move scroll to the outer workspace shell. Do not reintroduce a framed card around the paper. Preserve inline AI selection/proofing alignment. Verify just above and below 1420px, plus long preview/edit scroll cases, TypeScript, and focused ProposalDisplay tests.

## Common mistakes

- Treating `--forge-page-inline-size` as the Proposal document page width.
- Reusing live measured frame width as a page authority.
- Letting breakpoint changes alter the measured page width.
- Moving scroll ownership to the workspace shell instead of the document/editor boundary.
- Making the textarea full width to move the scrollbar.
- Styling only preview scrollbars and forgetting edit scrollbars.
- Adding border/background/shadow back to the collapsed document viewer body.

## See also

- [[design/document-token-contract]]
- [[tech/preview-to-print-pipeline]]
- [[tech/proposal-style-layer]]
- [[tech/proposal-ai-routing-and-inline-diff]]
