

## Status

- Active

- Date: 2026-04-18

## Intent

- Keep Quick Start as an app-shell content-pane state, not a modal and not a page-owned overlay.

- Keep cover-letter cold start as an intentional `/proposal` entry state, not the default proposal shell.

- Share one semantic choice-card primitive across resume and cover-letter start flows.

## Top-Level Ownership

- `src/App.tsx`

- Owns whether Quick Start is open.

- Reads transient router state through `readQuickStartRouteState(location.state)`.

- When `quickStartRouteState.isOpen` is true, it renders `QuickStartFlow` in place of the routed content pane.

- Sidebar and topbar remain visible because Quick Start is an app-shell workspace state.

## Route-State Contract

- `src/lib/quick-start-routing.ts`

- Defines the transient app-shell Quick Start state:

- `createType`

- `resumeMode`

- `returnTarget`

- `createQuickStartLocationState(...)` opens Quick Start.

- `clearQuickStartLocationState(...)` closes Quick Start.

- No storage is involved.

## Quick Start Flow

- `src/components/onboarding/QuickStartFlow.tsx`

- App-shell launcher flow.

- State 1:

- `What are you starting?`

- `Resume`

- `Cover letter`

- State 2 for resume:

- `Bring in your resume.`

- `Upload PDF or image`

- `Start fresh`

- Resume import keeps the trusted Mistral import path and existing `importCv` semantics.

- Cover-letter selection hands off to `/proposal` with:

- proposal workspace reset token

- transient `proposalEntryIntent: "cover-letter-start"`

## Proposal Cold Start

- `src/pages/ProposalForge.tsx`

- Owns whether the inline cover-letter start session is active.

- Shows the cover-letter start only when all intentional cold-start conditions are true:

- compose view

- `proposalEntryIntent === "cover-letter-start"`

- no handoff

- no attached CV

- no meaningful compose/output draft

- While active, it replaces the normal proposal content pane area and hides the empty result shell.

- Rewind from the root cover-letter start state navigates back into app-shell Quick Start through `createQuickStartLocationState(...)`.

## Cover-Letter Start Surface

- `src/components/CoverLetterStartSurface.tsx`

- Centered two-step guided sheet inside the proposal content pane.

- Root state:

- `Bring in the job`

- `Bring in your resume`

- Job child state:

- `Capture the role`

- `Paste job offer`

- Resume child state:

- `Use a resume`

- `Import a resume`

- Back behavior:

- child state -> root state

- root state -> app-shell Quick Start when entered from `cover-letter-start`

## Shared Choice Primitive

- `src/components/onboarding/QuickStartChoiceCard.tsx`

- Semantic shared product primitive for primary Quick Start actions.

- `src/styles/product.css`

- Shared class family:

- `.dasti-quick-start-choice`

- `.dasti-quick-start-choice__button`

- `.dasti-quick-start-choice__body`

- `.dasti-quick-start-choice__title`

- `.dasti-quick-start-choice__hint`

- `.dasti-quick-start-choice__meta`

- `.dasti-quick-start-choice__expanded`

- Built from existing tokens for spacing, radius, typography, surface, and interaction color.

- Used across:

- Quick Start root cards

- resume child cards

- cover-letter root cards

- cover-letter child cards

## Width and Layout

- Current shared sheet width is owned by `--quick-start-sheet-inline-size` in `src/styles/product.css`.

- Cards are always `width: 100%` inside that shared sheet.

- The start sheets are centered via the shared Quick Start pane/frame structure.

- Proposal cold-start explicitly overrides the normal compact desktop left-anchor rule so the centered sheet remains centered.

## Non-Goals

- No new storage.

- No new parser path.

- No changes to trusted import contract.

- No modal/backdrop system for Quick Start.