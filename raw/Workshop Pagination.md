This document describes the validated workshop resume pagination system as it exists after the experience split work and the atomic-section continuity passes.

It is intentionally technical. It is written for future maintainers who need to change layout, tokens, or pagination behavior without breaking preview/print/export parity.

## Scope

### In scope

- The active workshop resume path that renders the one-column ATS-style resume.
- committedPages as the source of truth for page boundaries.
- experience splitting and continuation behavior.
- Atomic section pagination behavior for compact and long-form sections.
- Workshop page geometry and token propagation.
- Preview, print, and export parity for the workshop path.
- Browser-backed validation and debug tooling used to prove layout behavior.

### Out of scope

- DOCX internals.
- Proposal generation.
- OCR / parser ingestion logic.
- Legacy comparison pages unless explicitly referenced as contrast.
- Ad hoc temporary probe files, screenshot artifacts, and local debug scratch surfaces.

## 1. Overview

“Workshop pagination” is the active planner-driven pagination system for the workshop resume template workshop_resume_onecol_ats.

The active runtime path is:

- src/features/verbati/VerbatiResumePreview.tsx
- src/features/verbati/resume/ResumeTemplateRenderer.tsx
- src/lib/resume/resumePagination.ts
- src/features/verbati/resume/ResumeOneColAtsPage.tsx

It exists so the live preview, print route, and export path all render the same committed page breaks. The workshop path is not the same thing as the older measured/legacy pages in src/features/verbati/resume/ResumePage.tsx.

The workshop path is planner-first:

- the planner computes pages for internal placement and committedPages for rendering/export
- committedPages is the authoritative page boundary model
- the renderer and export layers consume committedPages; they should not invent new boundaries

Legacy comparison pages are still present for other layouts in ResumePage.tsx (ClassicResumePage, SwissMinimaPage, VolkRegisterPage, EditorialMagazinePage, SignalGridPage, QuirePage), but they are not the workshop pagination system.

## 2. Active Architecture

### Planner

The planner lives in src/lib/resume/resumePagination.ts.

Key entry point:

- planWorkshopResumePages({ data, template, stylePreset, debugTrace? })

Important internal helpers:

- buildPlannerMetrics(...)
- buildPlannerSections(...)
- splitExperienceEntryToFit(...)
- splitExperienceBlockAtWrapBoundary(...)

The planner converts template tokens into millimeter-based metrics, estimates section heights, then fills pages in order. It emits:

- pages: internal page plans with entries and sections
- committedPages: serialized page fragments used by preview, print, and export

### Preview renderer

The workshop preview renderer lives in src/features/verbati/resume/ResumeTemplateRenderer.tsx.

Important behavior:

- For workshop_resume_onecol_ats, it uses the planner output when committedPages are passed in.
- If committedPages is missing, it can fall back to planWorkshopResumePages(...).
- It renders each committed page inside a fixed A4 canvas shell.
- It keeps the canvas width/height stable and scales it inside the preview shell.

The active page component is src/features/verbati/resume/ResumeOneColAtsPage.tsx.

### Print path

src/pages/ResumePrintPage.tsx passes the workshop committedPages payload into ResumeTemplateRenderer.

That means print is not re-planning the workshop pages. It should render the same boundaries that were already committed for preview and export.

### Export path

The workshop export path lives in src/lib/export-renderers.ts.

Key helpers:

- getCommittedWorkshopPagesOrThrow(...)
- renderResumeStyledExportDocument(...)
- renderResumeAtsExportDocument(...)

For workshop_resume_onecol_ats, export rendering uses the committed pages directly. The parity tests assert that export boundaries match the shared planner model.

### Source of truth

committedPages is the source of truth for workshop page boundaries.

If preview, print, or export disagree, the first thing to inspect is whether they are all reading the same committedPages payload.

## 3. Section Model

The workshop section model is defined across:

- src/features/verbati/resumeLinking.ts
- src/features/verbati/cvDocumentToResumeData.ts
- src/features/verbati/resume/resume.types.ts
- src/lib/resume/resumePagination.ts

### Canonical section inventory

|Section kind|Active path representation|Atomic or splittable|Compact or long-form|Current pagination behavior|Special rules|
|---|---|---|---|---|---|
|profile|profile header block, plus contact and metadata rows|Atomic|Compact-to-mid|Whole header fragment, no split|Profile header and row spacing are token-driven; no section continuation|
|summary|summary fragment|Atomic|Long-form|Whole fragment, no split|Summary is placed as a single block after profile|
|experience|experience fragments|Splittable|Long-form|Can split within an entry and continue across pages|Only section with intra-entry split logic|
|education|education items|Atomic per item|Compact-to-mid|Whole items only|Covered by compact-tail rules|
|skills|skill items|Atomic per item|Compact|Whole items only|Covered by compact-tail rules|
|selected_projects / projects|canonical data model uses projects; workshop planner/render uses selected_projects|Atomic per item|Long-form card|Whole cards only|Has continuity protection so later sections do not outrun unfinished projects|
|languages|language items|Atomic per item|Compact|Whole items only|Covered by compact-tail rules|
|certifications|certification items|Atomic per item|Compact|Whole items only|Covered by compact-tail rules|
|achievements|text list items|Atomic per item|Compact-to-mid|Whole items only|Covered by compact-tail rules|
|affiliations|affiliation items|Atomic per item|Compact-to-mid|Whole items only|Covered by compact-tail rules|
|hobbies|hobby items|Atomic per item|Compact|Whole items only|Covered by compact-tail rules|
|additional_information|text section fragments|Atomic whole-text section|Long-form|Whole text section fragments only|Shares the text-section render path with custom|
|custom|preserved in the canonical text-section model, then represented through the same planner/render bucket as additional_information|Atomic whole-text section|Long-form|Collapsed into the additional_information planner bucket|Section title is preserved in the text item metadata|

### Canonicalization notes

- src/features/verbati/resumeLinking.ts treats projects as the canonical section type and maps the preview alias selected_projects back to projects.
- src/features/verbati/cvDocumentToResumeData.ts builds ResumeTextSection items for text sections and preserves the original sectionTitle.
- In the text-section mapping, additional_information and custom are both represented by ResumeTextSection, but the planner bucket is the same long-form text section family.

## 4. experience Pagination Logic

experience is special because it is the only workshop section that can split inside a single entry.

Relevant helpers in src/lib/resume/resumePagination.ts:

- buildPlannerExperienceEntry(...)
- splitExperienceEntryToFit(...)
- splitExperienceBlockAtWrapBoundary(...)
- estimateExperienceHeight(...)

### Fragment model

Experience entries are converted into planner fragments with:

- continued
- fragmentIndex
- sourceEntryId
- blocks

Blocks can be:

- text paragraphs
- bullets

The split logic preserves ordering and creates a tail fragment when the head part fits on the current page and the remainder can continue on the next page.

### Continued behavior

When experience continues, the renderer shows a Continued badge in the section heading and the later fragment is marked as continued. The committed page model keeps the repeated section fragments in sequence.

### Page-fill behavior

The planner attempts to fill the current page with experience content before moving on, but it will split an experience entry if needed instead of cropping it or moving the entire entry unnecessarily.

### Parity

The workshop preview, print route, and export path all rely on the same committed experience fragments. The parity tests assert that the continued fragments appear in the same order across planner, preview, print, and export.

### Current limitations

The experience split logic is still heuristic:

- it uses estimated heights rather than browser-measured heights
- it relies on text-length and wrap-boundary heuristics to decide whether a split is valid
- font-family changes can still shift the real page-fit boundary

## 5. Atomic-Section Pagination Rules

The compact and long-form non-experience sections are still planner-placed as whole items or whole text fragments.

The validated workshop branch adds local rules to improve continuation quality without redesigning the planner globally.

### Compact one-item-tail prevention

This rule family targets:

- education
- skills
- languages
- achievements
- certifications
- affiliations
- hobbies

Goal:

- avoid a page break that strands exactly one remaining item on the next page when the whole remaining section can fit cleanly there

Behavior:

- if the remaining section would be left as a visually weak one-item tail and the full remainder fits on a fresh page, the planner prefers moving the whole section to the next page

### selected_projects continuity handling

selected_projects is treated more strictly than the other atomic sections.

Goal:

- once a following section begins, the unfinished selected_projects block must not resume later

Behavior:

- the planner keeps selected_projects contiguous instead of allowing it to interleave with later sections
- this prevents a later compact section from starting before the project block is finished

### Text-section rescue

This applies to:

- additional_information
- custom

Behavior:

- the long-form text section is kept contiguous on the current or next page rather than being allowed to read as a stranded tail after other sections have started
- custom is carried through the same planner/render path as additional_information, with the section title preserved in the text item metadata

### What is still not solved globally

- There is no universal balancing system that reflows all sections for perfect visual packing.
- The planner is still local and sequential.
- Section-specific fit decisions are still heuristic.
- Font family changes can still move the real browser fit boundary even when committed pages are stable in the planner.

## 6. Margins / Geometry / Layout Tokens

The workshop path is token-driven for page geometry and typography.

### Source of truth

Workshop token resolution starts in:

- src/lib/layout/documentTokenNormalizer.ts
- src/lib/layout/documentTokens.ts
- src/lib/layout/documentTokenSerializers.ts
- src/lib/layout/documentAppearance.ts
- src/features/verbati/style.ts

The workshop template definition is:

- src/lib/layout/resumeTemplates.ts

### Final workshop margins

The active workshop template workshop_resume_onecol_ats uses:

- topMm: 17
- rightMm: 35
- bottomMm: 18
- leftMm: 18

That 18mm bottom inset is the current workshop state. It is intentionally not the older 35mm legacy margin.

### Preview/export token chain

The chain is:

1. resumeTemplates.ts defines the template geometry and preview numbers.
2. documentTokenNormalizer.ts converts template geometry into canonical document tokens.
3. documentTokenSerializers.ts exports those tokens as CSS variables.
4. documentAppearance.ts resolves font families, colors, and themed appearance.
5. style.ts exposes the resolved workshop appearance to the preview and export layers.

### What is token-driven

- page width and height
- page margins
- live area size
- section gaps
- header spacing
- body and caption font sizes
- project padding
- skill pill padding
- export and preview theme variables

### What still uses local hardcoded values

Some local values are still intentionally hardcoded in component and serializer code:

- src/features/verbati/resume/ResumeOneColAtsPage.tsx still uses a few fine-grain spacings for heading gaps, list gaps, and the Continued label presentation.
- src/features/verbati/resume/ResumeTemplateRenderer.tsx still uses a fixed page gap between preview shells.
- src/lib/layout/documentTokenSerializers.ts still contains serializer-side literal styles for preview/export decoration.
- src/lib/layout/resumeTemplates.ts still holds the authoritative template constants for preview and export geometry.

Do not change those casually. Any geometry or typography change should be treated as a token change plus a browser-backed verification change.

## 7. Typography Contract

The canonical typography roles live in src/lib/layout/documentTokens.ts:

- display
- title
- subtitle
- summary
- body
- bodySm
- label
- meta

The workshop renderer consumes the serialized CSS variables produced by src/lib/layout/documentTokenSerializers.ts, such as:

- --text-display-size
- --text-title-size
- --text-body-size
- --text-body-sm-size
- --text-caption-size
- --text-meta-size
- --font-heading-family
- --font-body-family
- --font-editorial-family

### Renderer and planner alignment

src/lib/layout/documentTokenNormalizer.ts converts the workshop template into the typography and geometry values used by the planner.

The planner then uses:

- body line heights
- body-sm line heights
- label and meta line heights
- title height adjustments
- pageHeightBudgetMm

to estimate page breaks.

### What is stable

- The token roles are stable.
- The workshop template uses the resolved font families from appearance.font.*.
- Preview and print should use the same resolved font family chain.

### What is still approximate

- Browser font metrics can still alter wrapping and page fit.
- The planner is not fully font-metric-aware.
- The same content can fit differently under different primary font families even when the token values are identical.

### Known font-family sensitivity

Use the font debug helpers when the same content fits differently across fonts.

## 8. Debugging / Validation Tools

### Browser-backed font and parity harness

File:

- scripts/run-resume-font-parity-harness.ts

What it does:

- launches headless Chromium with Playwright
- loads the live resume preview and the print route
- captures preview, print, and raster snapshots
- compares the rendered surfaces with image diffs
- writes a durable audit report under docs/audits/
- stores temporary artifacts under tmp/resume-font-parity/<timestamp> by default, or a custom directory passed with --artifact-dir

Useful CLI arguments:

- --cv-id <id>
- --cv-url <url>
- --fixture-name <fixture>
- --viewed-pdf <path>
- --artifact-dir <path>

Typical invocation:

`rtk ./node_modules/.bin/tsx scripts/run-resume-font-parity-harness.ts \ --cv-id <fixture-id> \ --artifact-dir tmp/resume-font-parity/<run-name>`

Use --cv-url if you want to target a live preview URL directly, or --fixture-name if you want the harness to select a repo fixture by name.

What it proves:

- the live browser preview and print route agree on the same typography and page fit behavior
- the returned export PDF matches what the worker actually generated
- the browser surface is not diverging from the planner for the tested fixture

What it does not prove:

- it does not eliminate all font sensitivity
- it does not prove every possible CV fixture is safe
- it does not replace planner unit tests

### Font snapshot helper

Files:

- src/lib/resume-font-debug.ts
- src/lib/__tests__/resume-font-debug.test.ts

What it does:

- reads computed font families from the live preview or print DOM
- checks primary font family resolution
- measures primary vs fallback text widths
- captures the current theme variables used by the renderer

What it proves:

- the runtime is actually using the intended heading/body/editorial font families
- CSS variables are resolved to the expected families in the browser

### Token hardcode audit

File:

- src/lib/layout/__tests__/documentTokenHardcodeAudit.test.ts

What it does:

- statically checks that active preview branches do not accumulate raw colors, raw font literals, or stray authored mm/pt literals outside the allowlist

What it proves:

- the token contract is still respected in the active preview and serializer layers

What it does not prove:

- it does not prove browser fit
- it does not prove real font metrics
- it does not replace runtime pagination tests

### Workshop pagination tests

Files:

- src/lib/resume/__tests__/resumePagination.test.ts
- src/features/verbati/resume/__tests__/ResumeTemplateRenderer.test.tsx
- src/lib/__tests__/resumeExportParity.test.ts
- src/pages/__tests__/ResumePrintPage.test.tsx

These cover:

- planner page breaks
- experience splitting
- atomic section continuity rules
- preview committed-page rendering
- export committed-page parity
- print route parity

### Temporary probes and artifacts

During audits, local-only probe surfaces and artifacts may be created, such as:

- my-app/.artifacts/
- my-app/.playwright-tmp/
- my-app/atomic-sections-probe.html
- my-app/src/debug/

These are audit tools, not product code.

Do not commit them unless a specific durable tool is being intentionally added to the repo.

## 9. Test Strategy

### Planner tests

src/lib/resume/__tests__/resumePagination.test.ts is the primary planner regression suite.

It covers:

- compact section placement
- experience splitting
- continuation ordering
- oversized entry safety
- committed page serializability

### Preview tests

src/features/verbati/resume/__tests__/ResumeTemplateRenderer.test.tsx covers:

- workshop page rendering
- preview shell scaling
- live font and palette variable injection
- committed fragment boundaries in the rendered DOM

### Export parity tests

src/lib/__tests__/resumeExportParity.test.ts covers:

- planner/export page boundary alignment
- dense continuation boundary alignment

### Print route tests

src/pages/__tests__/ResumePrintPage.test.tsx covers:

- the actual print route wiring
- workshop print rendering
- committed pages passed through the payload
- font-variable parity on the print route

### Browser-backed validation still required

Use browser-backed validation when:

- a change can alter wrapping or fit
- a change affects the live preview shell
- a change affects token values that influence page height
- a change affects font family resolution
- a change affects experience or any continuation-sensitive section

Unit tests are not enough for live-fit issues.

## 10. Known Limitations / Follow-ups

Be explicit about what is still approximate:

- The planner still estimates height; it does not measure the browser DOM in real time.
- Font family variance can still change page fit.
- Section-specific continuation rules are local and heuristic.
- The workshop system is not a global balancing engine.
- The legacy measured pages still exist as comparison/compatibility surfaces in ResumePage.tsx.

Likely follow-ups:

- token usage audit
- deeper font-metric-aware planning
- any remaining atomic-section quality cleanup
- possible section reordering / manual drag-and-drop product follow-up, if the product eventually needs it

## 11. Safe Modification Guide

If you need to change workshop pagination, start here:

1. src/lib/resume/resumePagination.ts
2. src/features/verbati/resume/ResumeTemplateRenderer.tsx
3. src/features/verbati/resume/ResumeOneColAtsPage.tsx
4. src/lib/layout/documentTokenNormalizer.ts
5. src/lib/layout/documentTokenSerializers.ts
6. src/lib/layout/documentAppearance.ts
7. src/features/verbati/style.ts

### Authoritative files

- Planner truth: src/lib/resume/resumePagination.ts
- Workshop template truth: src/lib/layout/resumeTemplates.ts
- Token normalisation truth: src/lib/layout/documentTokenNormalizer.ts
- Token serialization truth: src/lib/layout/documentTokenSerializers.ts
- Runtime preview truth: src/features/verbati/VerbatiResumePreview.tsx
- Workshop page renderer truth: src/features/verbati/resume/ResumeTemplateRenderer.tsx and src/features/verbati/resume/ResumeOneColAtsPage.tsx
- Print route truth: src/pages/ResumePrintPage.tsx
- Export parity truth: src/lib/export-renderers.ts

### Invariants to preserve

- committedPages remains the boundary source of truth.
- Preview, print, and export must keep the same committed page order.
- experience remains the only section allowed to split within a single entry.
- Atomic sections should not start a new visual continuation strategy without a concrete reason.
- Token changes must flow through the normalizer and serializers, not ad hoc component duplication.
- Font-sensitive changes must be validated in a real browser.

### Risky changes

- changing bottomMm or the template live area without re-running browser-backed parity checks
- changing font families, font weights, or line heights without re-running the font parity harness
- changing section-estimation helpers without re-checking planner and preview parity
- introducing a new pagination heuristic without confirming it does not break experience
- adding raw hardcoded styling values into active preview branches

### Safe validation checklist

- run src/lib/resume/__tests__/resumePagination.test.ts
- run src/features/verbati/resume/__tests__/ResumeTemplateRenderer.test.tsx
- run src/lib/__tests__/resumeExportParity.test.ts
- run src/pages/__tests__/ResumePrintPage.test.tsx
- run src/lib/layout/__tests__/documentTokenHardcodeAudit.test.ts if tokens or styles changed
- run scripts/run-resume-font-parity-harness.ts for browser-backed fit or font changes

### Final note

If a change only looks correct in unit tests, do not assume the workshop system is safe. For pagination and typography, the browser remains the deciding boundary.