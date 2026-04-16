

This note is for fast orientation. It describes the active verbati style system as it exists in the repo today, with emphasis on CV styling, proposal styling, runtime inheritance, renderer/token plumbing, and the class families that matter when tracing output.

Non-authoritative by default:

- pdf-ingest/
- archived or backup trees
- ProposalForgeNext.tsx
- generic app-shell theme tokens that are not passed into the document token pipeline

## What Is The Render Authority

metadata.verbatiStyle is the persisted visual source of truth for document rendering.

- On CVs, metadata.verbatiStyle is read from the CV document and canonicalized through getVerbatiStyleFromCv() and resolveVerbatiStyle() in my-app/src/features/verbati/style.ts.
- On proposals, runtime may temporarily follow an attached CV style, but the rendered metadata still resolves to a concrete verbatiStyle snapshot before preview/export/save.
- templateId is not the full style authority. It owns proposal geometry and layout-template structure, not typography/palette/accent appearance.
- Workspace preview state is not persisted state. Runtime detachment and live preview logic can sit in component state without creating a second persisted style system.

The current proposal inheritance MVP is:

- attached proposal follows CV style at runtime
- first direct proposal style edit detaches to local custom
- explicit save/apply/save-draft paths persist the resulting verbatiStyle

## Mental Model

There are two linked concerns:

- Layout/template geometry:
    - VerbatiStylePreset.layout picks the structural family
    - getProposalTwinTemplateId() maps layout to the proposal twin template
    - proposal templates control document geometry and renderer structure
- Appearance:
    - VerbatiStylePreset.typography, palette, and optional accentHex control appearance
    - documentAppearance.ts resolves these into canonical preview/export tokens
    - those tokens become CSS vars consumed by the actual renderers

Useful rule of thumb:

- layout chooses the structural branch
- templateId chooses the proposal renderer template within that branch
- verbatiStyle chooses how the document looks inside that structure

VerbatiStylePreset today is:

`type VerbatiStylePreset = { layout: VerbatiLayoutPreset; typography: VerbatiTypographyPreset; palette: VerbatiPalettePreset; accentHex?: string; };`

Canonicalization matters:

- legacy layout aliases are normalized in resolveVerbatiStyle()
- typography aliases are normalized through resolveVerbatiFontPairId()
- custom accents are normalized through normalizeVerbatiAccentHex()
- comparisons should happen on canonicalized values, not raw UI input

## Pipeline

### CV path

Persisted CV metadata flows like this:

cv.metadata.verbatiStyle  
-> getVerbatiStyleFromCv()  
-> resolveVerbatiStyle()  
-> useBoundVerbatiCvStyle()  
-> preview/export consumers

Important details:

- useBoundVerbatiCvStyle.ts keeps a local stylePreset state for the CV workspace.
- Before persistence, it canonicalizes through canonicalizeVisualStyle() and writes back metadata.verbatiStyle.
- That preserves one persisted visual authority even though the workspace is interactive.

### Proposal path

Proposal runtime currently resolves style from multiple inputs, but only one resolved style wins for rendering.

The active runtime precedence is expressed by resolveProposalStyle() in my-app/src/features/verbati/styleState.ts:

`if (hasUserEditedStyle && workspaceStyle) return { style: workspaceStyle, source: "custom" }; if (!hasUserEditedStyle && isCvAttached && cvStyle) return { style: cvStyle, source: "cv" }; if (metadataStyle) return { style: metadataStyle, source: "default" | "custom" }; return { style: DEFAULT_VERBATI_STYLE, source: "default" };`

In ProposalForge.tsx, the practical flow is:

- base proposal style state is assembled from stored draft metadata and local proposal settings
- palette/custom accent overrides are folded into proposalMetadataStyle
- attached CV style comes from activeCvProposalStylePreset
- runtime resolution happens through resolveProposalStyle(...)
- effectiveProposalStylePreset becomes the active proposal style
- proposalRenderMetadata.verbatiStyle is serialized from that resolved style
- ProposalDisplay receives the resolved stylePreset and templateId
- ProposalDocumentRenderer turns that into final document DOM and CSS vars

Important warning:

- styleLinkMode is a runtime/persistence hint, not the render authority by itself
- the actual render authority is still the resolved verbatiStyle snapshot passed down into the proposal renderer

### Theme/token path

The style preset reaches the renderer through the document token pipeline:

VerbatiStylePreset  
-> documentAppearance.ts  
-> canonical preview/export appearance tokens  
-> serializer helpers  
-> CSS custom properties on the document root  
-> DOM classes in the renderer

Active touchpoints:

- buildVerbatiThemeVars() for resume preview surfaces
- buildVerbatiProposalDocumentVars() for proposal document surfaces
- serializeVerbatiThemeVars() / serializeProposalDocumentThemeVars() for appearance vars
- normalizeProposalPreviewTokens() plus serializeProposalPreviewVars() / serializeProposalRuntimeVars() / serializeProposalMeasurementRuntimeVars() inside ProposalDocumentRenderer.tsx

This is why preview/export/print parity depends on shared token intent rather than ad hoc DOM styling.

## Classes And Surfaces

Treat class families as ownership markers.

### Document classes

These classes represent actual document structure or the document viewer shell:

- .dasti-proposal-document*
    - actual proposal document DOM inside ProposalDocumentRenderer.tsx
    - examples: .dasti-proposal-document__page, .dasti-proposal-document__body, .dasti-proposal-document__rail
- .dasti-proposal-sheet*
    - proposal sheet/viewer shell and editor-preview framing in ProposalDisplay.tsx
    - examples: .dasti-proposal-sheet__preview-stage, .dasti-proposal-sheet__preview-page, .dasti-proposal-sheet__controls
- .dasti-document-shell and .dasti-document-rail
    - generic document viewer shell/rail surfaces shared across document display flows

Interpretation:

- .dasti-proposal-document* means document content layer
- .dasti-proposal-sheet* means proposal-specific viewer/editor shell
- .dasti-document-* means shared document-stage infrastructure

### Workspace and control classes

These classes are workspace chrome, not the persisted document:

- .dasti-compose-toolbar*
    - proposal workspace toolbar and status chips
- .dasti-artifact-inspector*
    - style inspector / bundle / palette / typography controls
- proposal workbench shell classes in ProposalForge.tsx
    - examples: .dasti-workbench-top-left-slot--proposal
    - .dasti-proposal-workbench-left-stack
    - .dasti-proposal-compose-column--workspace
    - .dasti-proposal-output-shell--workspace

Do not confuse these with document styling. They control the editing workspace around the artifact, not the artifact’s persisted appearance.

## Files To Read First

- my-app/src/features/verbati/style.ts
    - primary style authority helpers: defaults, canonicalization, alias normalization, layout-to-renderer/template mapping, equality, and CSS-var builders.
- my-app/src/lib/layout/documentAppearance.ts
    - token plumbing for preview/export appearance; this is where palette/accent/typography become canonical document tokens.
- my-app/src/pages/ProposalForge.tsx
    - active proposal runtime owner; resolves attached CV style, local draft style, detachment behavior, and the metadata passed to rendering/persistence.
- my-app/src/components/ProposalDisplay.tsx
    - bridge between proposal runtime state and the document renderer; resolves final stylePreset + templateId for display mode/edit mode.
- my-app/src/components/proposal-render/ProposalDocumentRenderer.tsx
    - final proposal document DOM and CSS-var application; the best file for understanding which classes are real document structure.

Secondary context files:

- my-app/src/features/verbati/styleState.ts
    - pure helpers for canonicalization, diffs, and proposal runtime style resolution.
- my-app/src/features/verbati/useBoundVerbatiCvStyle.ts
    - CV workspace persistence boundary for metadata.verbatiStyle.
- my-app/src/lib/proposal-render-state.ts
    - smaller resolver for stylePreset + templateId pairing used by display-level consumers.
- my-app/src/lib/proposal-output-draft.ts
    - proposal draft persistence shape and normalization for proposalVerbatiStyle, proposalStyleLinkMode, and related workspace output state.

## Major Things To Understand

- Canonicalization happens before comparison and persistence.
    - resolveVerbatiStyle(), serializeVerbatiStyle(), and canonicalizeVisualStyle() are the stabilizers.
- Proposal templates and verbatiStyle are linked but not identical responsibilities.
    - template controls proposal geometry
    - verbatiStyle controls appearance and layout family choice
- Proposal style inheritance is runtime workspace logic, not a second persisted style authority.
    - attached CV style can temporarily win at runtime
    - once the proposal is directly edited, local custom style wins
    - persistence still resolves to an explicit style snapshot
- Renderer parity matters.
    - preview/export/print are meant to share resolved token intent
    - if a change bypasses token serializers and styles DOM directly, parity risk goes up

Two common misunderstandings to avoid:

- Mistake: templateId alone tells you how the proposal should look.
    - Reality: it only tells you the structural proposal template; appearance still comes from the resolved style pipeline.
- Mistake: current workspace preview state is the same thing as persisted document state.
    - Reality: ProposalForge can hold transient runtime state that has not yet become the persisted verbatiStyle.

## Weaknesses / Future Improvements

- Proposal style resolution is still spread across several layers.
    - ProposalForge, styleState.ts, ProposalDisplay, and proposal-render-state.ts all participate, which increases onboarding cost.
- Proposal runtime detachment relies on multiple signals.
    - hasUserEditedStyle, proposalWorkspaceStyle, proposalStyleLinkMode, and persisted draft metadata all interact.
- Style docs are local-only right now.
    - docs/plans/ is mostly gitignored in this repo, so scratchpads like this are easy to lose unless the ignore rules are intentionally widened.
- Legacy layout aliases still exist in the active style resolver.
    - that is pragmatic for compatibility, but it makes the real layout set less obvious to new readers.
- Class ownership is understandable but dispersed.
    - workspace shell, viewer shell, and document classes are defined across page components, renderer components, and CSS/tests rather than one obvious map.

If improving later, keep the constraints:

- do not introduce a second token system
- do not move render authority away from metadata.verbatiStyle
- prefer consolidating resolution helpers over adding another style layer