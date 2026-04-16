

Fast orientation note for LLMs and engineers. This is the shortest useful map of how /proposal style persistence works in this branch, where style truth lives, and where the confirmed bugs were.

Primary long-form doc:

- 2026-04-16-proposal-style-persistence-and-saved-view-debugging.md

Authoritative runtime scope:

- my-app/
- main page: my-app/src/pages/ProposalForge.tsx
- saved list / saved-view card state: my-app/src/components/ProposalsList.tsx
- final renderer bridge: my-app/src/components/ProposalDisplay.tsx
- style/template resolver: my-app/src/lib/proposal-render-state.ts
- browser draft storage: my-app/src/lib/proposal-output-draft.ts
- server persistence: my-app/convex/createProposalPublic.ts, my-app/convex/updateProposalPublic.ts, my-app/convex/proposalsPublic.ts

## 1. One-line mental model

/proposal has two different concerns that often get confused:

- persistence truth: saved proposal metadata in Convex plus live draft/output draft in browser storage
- render truth: the resolved verbatiStyle + templateId that actually reach ProposalDisplay

Most regressions happen when UI state or stale local draft state is allowed to override persistence truth.

## 2. The pipeline at a glance

### Compose path

`compose form state -> ProposalForge page style state -> proposalRenderMetadata -> proposalPersistenceMetadata -> buildComposeSaveSnapshot() -> performProposalSave() -> createProposal / updateProposal -> Convex saved row`

Key functions:

- proposalPersistenceMetadata in ProposalForge.tsx
- buildComposeSaveSnapshot(...)
- performProposalSave(...)
- flushScheduledProposalSave(...)

### Saved reopen path

`route /proposal?view=saved&id=... -> sortedSavedProposals -> openedSavedProposal -> savedProposalRenderMetadata / selectedRenderState -> ProposalDisplay -> actual DOM fonts/layout/palette`

Key functions:

- sortedSavedProposals in ProposalForge.tsx
- openedSavedProposal
- savedProposalRenderMetadata
- resolveSavedAppearanceState(...) in ProposalsList.tsx
- selectedStoredRenderState
- selectedBaseStylePreset
- resolveProposalRenderState(...)

### Duplicate-to-draft path

`openedSavedProposal -> restore content + source brief + style state into live draft -> writeStoredProposalOutputDraft(...) -> writeStoredProposalComposeDraft(...) -> compose workspace renders via ProposalDisplay`

This path is important because it can prove:

- saved row metadata is correct
- draft rendering is correct
- saved view alone is wrong

If that happens, the bug is almost certainly reopen/render resolution, not save persistence.

## 3. Style truth hierarchy

### Persisted fields that matter

From proposal metadata:

- templateId
- verbatiStyle
- styleLinkMode
- sourceCvId
- templateBundleId

### What each field means

- verbatiStyle
    - saved visual snapshot: layout, typography, palette, optional accentHex
    - this is the most important persisted render input
- templateId
    - saved renderer/template geometry
- styleLinkMode
    - whether the proposal follows CV style or local proposal style
    - active values: inherit_cv, proposal_local
- sourceCvId
    - which CV the proposal is linked to
- templateBundleId
    - saved UI bundle selection
    - dangerous if treated as render-authoritative over verbatiStyle

### Practical authority rule

For saved proposals:

- if metadata.verbatiStyle or metadata.templateId exists, that saved snapshot should win for rendering
- CV fallback should only re-enter when the saved proposal lacks a persisted style snapshot
- bundle UI state should not silently replace persisted saved typography

## 4. Browser storage map

### Output draft

File:

- my-app/src/lib/proposal-output-draft.ts

Keys:

- dasti:proposal-output-draft:v1
- dasti:proposal-output-draft:session:v1

Carries:

- generatedProposalId
- proposalTemplateId
- proposalVerbatiStyle
- proposalStyleLinkMode
- templateBundleId
- proposalContent
- sourceComposeDraft

### Compose draft

Key:

- dasti:proposal-compose-draft:v1

Carries:

- source brief inputs
- job title / job description / tone info

Important:

- compose draft is not the canonical saved-style source
- output draft is not allowed to override a real saved row with the same id

## 5. Server persistence map

Files:

- my-app/convex/createProposalPublic.ts
- my-app/convex/updateProposalPublic.ts
- my-app/convex/proposalsPublic.ts

Canonical truth for saved proposals lives here.

What this branch verified:

- the style metadata validator/shape is correct
- save/autosave can write canonical style metadata correctly
- the server row was not the final blocker for the saved-view visual bug

## 6. The two confirmed bug boundaries

### Bug A: same-id optimistic/local draft override

Wrong boundary:

- sortedSavedProposals merge in ProposalForge.tsx

Old failure:

- stale local output draft with same proposal id could replace the queried saved row
- reopen and Duplicate to draft then used stale style metadata

Fix:

- only add optimistic saved draft when that id is not already present in merged saved proposals

### Bug B: saved-view bundle/default override

Wrong boundary:

- saved-view style resolution in ProposalsList.tsx

Old failure:

- persisted saved verbatiStyle was correct
- duplicate-to-draft could render correctly
- but saved view let bundle/default style state replace the saved typography before render

Fix:

- resolveSavedAppearanceState(...) now keeps bundle state as explicit UI state
- selectedBaseStylePreset now uses stored saved render state unless there is a real pending user override

## 7. The route-hydration bug that looked related

There was also a saved-route reopen bug:

- route-driven selection used the switching path
- that set isSwitchingProposal=true
- the main saved card could show a loading/generating state even though the row was already there

File:

- my-app/src/components/ProposalsList.tsx

Fix:

- route hydration now uses selectProposal(...) directly

This was real, but it was not the final visual-style blocker.

## 8. How to debug this fast next time

Use this order:

1. Check the saved Convex row.
    - templateId
    - metadata.verbatiStyle
    - metadata.sourceCvId
    - metadata.styleLinkMode
2. Check browser storage.
    - local output draft
    - session output draft
    - compose draft
3. Compare the same proposal id in:
    - saved view
    - duplicate-to-draft view
4. Compare:
    - raw server row
    - selected/opened saved proposal
    - saved render metadata
    - ProposalDisplay props
    - actual DOM/computed font families

Fast classification:

- server row wrong -> save/autosave/unmount bug
- server row correct, draft correct, saved view wrong -> saved-view resolver/render bug
- same-id stale local draft wins -> merge precedence bug

## 9. Trace points that matter

Trace marker:

- [proposal-style-trace]

Helper:

- my-app/src/lib/proposal-style-trace.ts

Most useful checkpoints:

- perform-proposal-save:before-write
- perform-proposal-save:after-write
- saved-merge
- saved-opened-proposal
- saved-runtime-style
- saved-render-metadata
- saved-restore-effect

Most useful fields:

- winnerSource
- winnerReason
- rawServerRow
- rawQueryRow
- rawLocalOutputDraft
- rawSessionOutputDraft
- rawComposeDraft
- resolvedRenderState

## 10. Tests that protect the branch fixes

- my-app/src/pages/__tests__/ProposalForge.saved-view.test.tsx
    - same-id stale local draft must not win over persisted saved row
- my-app/src/components/__tests__/ProposalsList.route-selection.test.tsx
    - route-driven saved reopen must not show the loading skeleton
- my-app/src/components/__tests__/ProposalsList.saved-view-typography.test.tsx
    - saved view must preserve persisted typography, not bundle defaults
- my-app/src/components/__tests__/ProposalsList.autosave.test.tsx
    - saved-view autosave must preserve style/source-CV metadata
- my-app/src/pages/__tests__/ProposalForge.save-to-library.test.tsx
    - save-to-library writes the expected style metadata
- my-app/src/pages/__tests__/ProposalForge.autosave.test.tsx
    - compose autosave keeps correct style metadata

## 11. The one thing to remember

If a saved proposal row is correct but the saved view is visually wrong, do not go back to save-path debugging first.

Check saved-view style resolution in:

- my-app/src/components/ProposalsList.tsx
- my-app/src/pages/ProposalForge.tsx
- my-app/src/lib/proposal-render-state.ts

In this branch, the real blocker was not persistence corruption. It was saved-view resolver state letting non-authoritative UI/bundle state override a correct persisted saved style snapshot.