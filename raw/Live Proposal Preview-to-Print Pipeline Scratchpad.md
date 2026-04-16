

This note describes the active styled-proposal pipeline in the live local tree. It is written as an operator / LLM scratchpad, not as product documentation.

Use this note when you need to understand what is implied between the live proposal preview, the Export Styled PDF click, the export request, the worker bootstrap, /print/proposal, and the final PDF bytes returned by page.pdf().

## Active-code authority

- Treat my-app/ as the active implementation surface for proposal preview and styled proposal PDF export.
- Treat my-app/src/lib/layout/documentAppearance.ts as the live appearance authority for shared layout/document token work.
- Treat pdf-ingest/, backups, archive trees, and older proposal renderer experiments as non-authoritative unless they are being used only as historical context.
- The styled proposal path should be reasoned from the active preview-driven print route, not from the older direct HTML-string renderer path.

## Pipeline overview

The active styled proposal export path is one continuous flow:

1. ProposalForge owns the live compose/saved proposal state, the effective template id, the effective style preset, and the preview shell.
2. ProposalDisplay renders the proposal preview surface and delegates the actual page document to ProposalDocumentRenderer.
3. ProposalForge builds a ProposalPreviewPrintSource from the same resolved preview state that is currently visible.
4. exportDocumentFile posts that payload to /api/v1/document-export/proposal/pdf.
5. The export service invokes document-export-worker.ts.
6. For styled proposal PDF, the worker builds a ProposalPrintRoutePayload, launches Playwright, injects the payload into the browser, and opens /print/proposal.
7. ProposalPrintPage reads window.__DASTI_PROPOSAL_PRINT_PAYLOAD__, rebuilds the same proposal document vars, renders ProposalDocumentRenderer, waits for document.fonts.ready, and reports a ready snapshot through window.__DASTI_PROPOSAL_PRINT_STATUS__.
8. The worker captures the pre-page.pdf() print-route screenshot, then calls page.pdf() and returns the exact PDF bytes to the browser.

The core implication is simple: preview and styled PDF are supposed to be twins because both are driven by the same resolved template/style state and the same ProposalDocumentRenderer.

## Live preview path

### UI entrypoints

- my-app/src/pages/ProposalForge.tsx
- my-app/src/components/ProposalDisplay.tsx
- my-app/src/components/proposal-render/ProposalDocumentRenderer.tsx

### Preview state ownership

ProposalForge owns the source-of-truth state used by preview and by styled export:

- proposal body/content
- proposalType
- applicant/header values
- header visibility flags
- voicePreset
- effective template id
- effective style preset

There are two important resolved-state boundaries:

1. Compose preview uses the effective live template/style state derived from the current forge session.
2. Saved proposal preview uses normalized saved state, including effectiveSavedProposalTemplateId and effectiveSavedProposalStylePreset.

Styled PDF must use those effective values, not stale raw saved fields.

### Preview renderer structure

ProposalDisplay is the preview shell. It owns:

- preview zoom / fit shell behavior
- stage sizing
- wrapper chrome for workspace use
- selection of the live proposal template

ProposalDocumentRenderer owns the actual document body. It is the page renderer that turns:

- templateId
- stylePreset
- documentTypography
- header/body blocks

into the A4 document surface the user sees.

That split matters:

- ProposalDisplay is allowed to scale or frame the page for workspace viewing.
- ProposalDocumentRenderer is the document authority and must stay print-faithful.

## Style and layout resolution

### Effective template/style pair

The active preview/export contract depends on these values being identical between preview and print:

- templateId
- stylePreset.layout
- stylePreset.typography
- stylePreset.palette
- stylePreset.accentHex

In the live path, ProposalForge resolves those first, then passes them to both preview and styled export source builders.

### Proposal-specific theme vars

The print/preview document vars come from:

- buildVerbatiProposalDocumentVars(stylePreset)

Typography for the proposal document comes from:

- getProposalDocumentTypography(voicePreset, stylePreset)

Those utilities decide the body/document-level font family and other proposal document presentation details.

If the proposal looks wrong, the first questions are:

- did preview and export use the same templateId?
- did preview and export use the same resolved stylePreset?
- did ProposalDocumentRenderer receive the same document typography inputs?
- did the fonts actually materialize, or only resolve as CSS-family strings?

## Export click path

### UI action

The styled export action lives in:

- my-app/src/pages/ProposalForge.tsx
- my-app/src/lib/exportDocumentFile.ts

When the user clicks Export Styled PDF, ProposalForge chooses one of:

- exportComposeStyledProposalSource()
- exportSavedStyledProposalSource()

Both build a ProposalPreviewPrintSource, not a pre-rendered HTML string.

### Request contract

The active live contracts are defined in:

- my-app/src/lib/document-export-models.ts

Important types:

- ExportDocumentFileArgs
- ProposalPreviewPrintSource
- ProposalPrintRoutePayload

ProposalPreviewPrintSource is the styled preview-export handoff. It carries:

- kind: "proposal"
- renderSource: "preview"
- content
- proposalType
- voicePreset
- header/document fields
- templateId
- stylePreset

This is the critical boundary between preview land and export land. If parity breaks, inspect this first.

## Browser request boundary

exportDocumentFile(...) serializes the request body and posts it to:

- /api/v1/document-export/proposal/pdf

After a successful response:

- it reads the returned blob
- captures the exact bytes in debug mode through setLastCapturedDocumentExport(...)
- triggers the browser download

For styled proposal PDF, the exact returned bytes are the artifact that matters. Any audit that only replays the request is weaker than an audit that saves the actual response from the real click.

## Worker path

The active styled proposal PDF worker path lives in:

- my-app/scripts/document-export-worker.ts

For styled proposal exports:

1. The worker receives data as a ProposalPreviewPrintSource.
2. It builds a ProposalPrintRoutePayload using buildProposalPrintRoutePayload({ data }).
3. It writes debug artifacts such as worker-bootstrap.json when audit metadata is present.
4. It launches Playwright.
5. It injects the payload into the browser via window.__DASTI_PROPOSAL_PRINT_PAYLOAD__.
6. It navigates to /print/proposal.
7. It waits until window.__DASTI_PROPOSAL_PRINT_STATUS__.status becomes ready or error.
8. It saves the pre-page.pdf() screenshot.
9. It calls page.pdf({ preferCSSPageSize: true, printBackground: true, scale: 1, margin: 0 }).

This worker is not supposed to invent an export-only layout or font override. Its job is to rehydrate the preview-intent payload into the print route.

## Print route path

### Route

The active styled proposal print route is:

- /print/proposal

It is wired in:

- my-app/src/App.tsx
- my-app/src/pages/ProposalPrintPage.tsx

### Print page responsibilities

ProposalPrintPage does the following:

1. Reads window.__DASTI_PROPOSAL_PRINT_PAYLOAD__.
2. Validates it as a ProposalPrintRoutePayload.
3. Rebuilds proposal document vars using buildVerbatiProposalDocumentVars(payload.stylePreset).
4. Recomputes documentTypography using getProposalDocumentTypography(payload.voicePreset, payload.stylePreset).
5. Renders ProposalDocumentRenderer directly on a bare A4 print surface.
6. Waits for document.fonts.ready.
7. Publishes the ready/debug snapshot through window.__DASTI_PROPOSAL_PRINT_STATUS__.

Important browser globals:

- window.__DASTI_PROPOSAL_PRINT_PAYLOAD__
- window.__DASTI_PROPOSAL_PRINT_BOOTSTRAP__
- window.__DASTI_PROPOSAL_PRINT_STATUS__

The important subtlety is that the print route should render the document surface itself, not the workspace preview chrome around it.

## Final PDF generation path

Once /print/proposal reports ready, the worker captures the same surface that the print route is showing and then calls:

- page.pdf(...)

The returned PDF bytes come from Playwright’s print pipeline. They are supposed to represent the same rendered ProposalDocumentRenderer surface that was visible immediately before page.pdf().

That means the styled proposal parity chain is:

- same proposal content
- same header/document fields
- same templateId
- same stylePreset
- same voicePreset
- same proposal document vars
- same documentTypography
- same ProposalDocumentRenderer
- same font materialization
- same print-ready rendered surface

If the rasterized PDF still differs after all of that, the divergence is downstream of the print route, usually in print timing, print surface wrappers, or font readiness.

## Same-export parity contract

For a single styled proposal export run, preview and styled PDF should remain twins across these invariants:

- same selected/exported templateId
- same selected/exported stylePreset
- same content
- same proposalType
- same voicePreset
- same header fields
- same proposal document vars
- same loaded font faces
- same ProposalDocumentRenderer
- no alternate export-only style system
- no fallback renderer for styled proposal PDF

If any of those stop matching, parity is already broken before the PDF bytes are produced.

## Why proposal output can still look wrong

### 1. Preview shell scale versus document surface

ProposalDisplay may scale the document for workspace fit, while /print/proposal is a bare A4 surface. That is allowed.

The invariant is not “same outer shell”, it is:

- same internal A4 document geometry
- same document renderer
- same layout proportions inside the page

If the page seems different only because one view is a scaled workspace preview and the other is a raw A4 page, inspect the shell first.

### 2. Computed font-family strings match, but the font never materializes

CSS-family parity is weaker than real font loading parity. If preview or print misses local font-face materialization, the document can fall back while still reporting similar family strings.

Inspect:

- local font-face injection
- document.fonts
- preview debug capture
- print debug snapshot

### 3. Template role styling can look different even with the same font family

A proposal block can use the same body font family but still look different because of:

- weight
- size
- casing
- letter-spacing
- template-specific role styling

So “the font looks different” is not enough by itself. You need to separate:

- wrong family
- right family, different role styling

### 4. Wrapper chrome leaking into the print surface

If the print route includes preview-only shells, cards, frames, or workspace backgrounds, page.pdf() can capture the wrong outer surface even though the document body is correct.

That is why the pre-page.pdf() screenshot is mandatory in a serious audit.

## Debug checkpoints

When debugging a styled proposal mismatch, walk this exact chain for the same export:

1. Selected templateId and stylePreset in ProposalForge
2. Preview computed/debug snapshot from ProposalDisplay
3. Real Export Styled PDF request body from exportDocumentFile
4. Exact returned PDF bytes from that same click
5. Worker bootstrap payload in document-export-worker.ts
6. /print/proposal snapshot immediately before page.pdf()
7. Pre-page.pdf() screenshot
8. Rasterized PDF page
9. Preview vs print screenshot comparison

10. Print screenshot vs PDF raster comparison

That gives you the first real divergence boundary instead of forcing you to guess from code or payloads alone.

## Working mental model

For styled proposals, think of the live system as:

- ProposalForge resolves the visible proposal state
- ProposalDisplay previews that state
- ProposalPreviewPrintSource serializes that same state for export
- document-export-worker.ts rehydrates it into /print/proposal
- ProposalPrintPage renders the same document surface through ProposalDocumentRenderer
- Playwright prints that ready surface to PDF

If you keep that model in mind, the most important debugging question becomes:

“At what exact boundary did the same proposal stop being the same proposal?”