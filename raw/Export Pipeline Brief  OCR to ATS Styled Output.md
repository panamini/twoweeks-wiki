

## Purpose

This note explains the current document pipeline end to end so an LLM or developer can understand, in one pass, how the system works from OCR input to final export output.

This system now supports:

- Resume ATS PDF
- Resume Styled PDF
- Proposal ATS PDF
- Proposal Styled PDF
- Proposal DOCX

It is designed to be:

- **source-of-truth driven**
- **ATS-ready**
- **direct-download**
- **Robial-grid-governed for export geometry**
- **separate from preview DOM rendering**

---

## One-glance architecture

User file / CV / proposal input  
        ↓  
Structured upload / parser pipeline  
        ↓  
Parser service OCR + CV parsing  
        ↓  
Normalized app data / current CV / proposal state  
        ↓  
Export source builders  
        ↓  
Unified export client  
        ↓  
Parser export endpoints  
        ↓  
Node export worker  
        ↓  
PDF or DOCX file  
        ↓  
Direct browser download

---

## Core system idea

There are **two different rendering worlds**:

### 1. App preview world

Used for on-screen editing and preview.

Examples:

- CvForge preview
- ProposalForge preview
- style cycling
- zoom / viewport fit
- preview shell UI

### 2. Export world

Used for final downloadable files.

Examples:

- ATS PDF
- Styled PDF
- Proposal DOCX

These two worlds may share:

- normalized content
- style tokens
- layout intent
- typography/palette settings

They must **not** share:

- mounted preview DOM as export source
- viewport scaling wrappers
- screenshot-based export
- preview-only geometry logic

---

## Source of truth

### Content source of truth

Exports are built from **normalized data objects**, not from the visible preview DOM.

Primary export contracts:

- `ResumePrintSource`
- `ProposalPrintSource`

### Visual source of truth

Visual styling comes from:

- resolved `stylePreset`
- shared style/layout tokens
- Robial grid contract for export geometry

---

## ATS-ready meaning

“ATS-ready” here means:

- real text PDF, not image PDF
- selectable text
- searchable text
- stable reading order
- conservative layout
- semantic structure
- no screenshot/canvas flattening
- no critical information hidden only in decorative elements

ATS exports may still use the shared Robial page geometry, but they simplify:

- ornament
- density
- decorative chrome

---

## OCR / CV ingestion pipeline

## High-level flow

Uploaded resume / PDF  
        ↓  
Structured upload UI  
        ↓  
Parser service  
        ↓  
OCR / parsing path  
        ↓  
Normalized CV data  
        ↓  
Stored or active CV model in app  
        ↓  
Export source builder  
        ↓  
Export endpoints  
        ↓  
PDF output

## Practical interpretation

The system uses the parser service as the main backend for:

- OCR
- CV parsing
- export file generation

The app then uses the normalized result for:

- preview
- proposal personalization
- export

This means the final export should reflect normalized CV/proposal state, not a screenshot of the preview.

---

## Export pipeline

## Frontend trigger layer

UI entrypoints include:

- Resume export controls
- Proposal export controls
- CvForge export actions
- ProposalForge export actions

Key frontend files:

- `my-app/src/components/ResumeExportControl.tsx`
- `my-app/src/components/ProposalExportActions.tsx`
- `my-app/src/pages/CvForge.tsx`
- `my-app/src/pages/ProposalForge.tsx`

These trigger the unified export client instead of using legacy screenshot export.

---

## Unified export client

Main client:

- `my-app/src/lib/exportDocumentFile.ts`

Role:

- receives export intent from UI
- sends normalized export payload to parser service
- receives returned file as blob
- triggers direct browser download

The browser does **not** use `window.print()` for the final UX.

---

## Export source builders

Main model builder file:

- `my-app/src/lib/document-export-models.ts`

Role:

- convert current app state into export-safe normalized objects
- keep exports independent from live preview DOM

Main builders:

- `buildResumeExportSource(...)`
- `buildProposalExportSource(...)`

These produce:

- `ResumePrintSource`
- `ProposalPrintSource`

---

## Backend export endpoints

Parser service files:

- `cv_parser_service/main.py`
- `cv_parser_service/document_export.py`

Role:

- receive normalized export payloads
- validate request
- call worker/render path
- return direct-download file responses

Export endpoints include patterns like:

- resume PDF
- proposal PDF
- proposal DOCX

---

## Worker layer

Worker file:

- `my-app/scripts/document-export-worker.ts`

Role:

- receive normalized export payload
- render export-only document
- generate final file

Outputs:

- PDF
- DOCX

---

## Renderer layer

Renderer file:

- `my-app/src/lib/export-renderers.ts`

Role:

- define export-only renderers
- no preview shell
- no toolbar
- no zoom wrapper
- no viewport-fit logic
- no mounted preview dependency

Main export renderers:

- `ResumeAtsExportDocument`
- `ResumeStyledExportDocument`
- `ProposalAtsExportDocument`
- `ProposalStyledExportDocument`

Proposal DOCX builder also lives in the export rendering/builder layer.

---

## PDF generation path

For the new direct-download PDF path, the worker uses a real document rendering path and produces:

- real PDF bytes
- direct-download response
- selectable/searchable text

This is different from the old screenshot path.

### Legacy path

Legacy screenshot helper:

- `my-app/src/lib/document-export.ts`

That file used raster-style DOM export and is now legacy, not the final export architecture.

---

## DOCX generation path

Proposal DOCX is built from:

- `ProposalPrintSource`

It is:

- direct-download
- structurally faithful
- editable
- conservative in layout
- not derived from preview DOM
- not derived from HTML scraping

DOCX prioritizes:

- document structure
- editability
- clean office-document behavior

over:

- pixel-perfect preview parity

---

## Grid and page geometry

## Robial is the export geometry source of truth

Shared file:

- `my-app/src/lib/layout/robialGrid.ts`

Skill/reference doc:

- `docs/skills/robial-17-18-modular-grid.md`

Robial governs export page geometry only:

- page rhythm
- margins
- columns
- gutters
- modular spacing

Canonical geometry:

- margins: top `17mm`, right `35mm`, bottom `35mm`, left `17mm`
- body: sidebar `35mm`, gutter `18mm`, main `105mm`

### Responsibility split

- **Robial** = geometry
- **stylePreset** = typography, palette, emphasis, ornament

`stylePreset` must not control:

- margins
- columns
- gutter widths
- page rhythm

---

## Styled vs ATS output

## ATS

Purpose:

- machine-readable
- text-first
- conservative
- semantically stable

Still uses:

- normalized source data
- Robial export geometry

Reduces:

- decorative complexity
- density
- visual ornament

## Styled

Purpose:

- preserve layout feel and visual identity
- keep style preset influence
- maintain direct-download export

Uses:

- normalized source data
- Robial export geometry
- style preset for typography/palette/ornament

Does **not** use:

- preview shell DOM as export source

---

## Runtime and boot modes

Primary dev commands:

- `./run.sh local`
- `./run.sh local-convex`
- `./run.sh tunnel`
- `./run.sh down`
- `./run.sh reset`
- `./run.sh status`
- `./run.sh logs`

### `./run.sh local`

- local parser
- image runtime
- working export runtime
- no workspace mount by default
- normal online/default Convex

### `./run.sh local-convex`

- local parser
- image runtime
- local Convex too
- advanced backend-dev mode

### `./run.sh tunnel`

- tunnel / edge workflow
- parser accessible through `parser.dasti.ai`
- same validated export-capable runtime shape

### `./run.sh down`

- normal stop

### `./run.sh reset`

- stronger cleanup
- non-destructive

Important rule:  
normal modes should not default to the bad parser workspace-mount runtime shape.

---

## Why some exports were easy and PDFs were harder

Simple exports such as JSON/Markdown are mostly:

- structured data transformation
- direct file creation
- no heavy rendering runtime

The new PDF path required more because it needed:

- export-only rendering
- file-generation worker
- browser-grade PDF generation/runtime
- runtime dependencies in the parser image

That is why the export/runtime work was more complex than the simple data-download buttons.

---

## Main files to know

## Frontend

- `my-app/src/pages/CvForge.tsx`
- `my-app/src/pages/ProposalForge.tsx`
- `my-app/src/components/ResumeExportControl.tsx`
- `my-app/src/components/ProposalExportActions.tsx`
- `my-app/src/lib/exportDocumentFile.ts`
- `my-app/src/lib/document-export-models.ts`
- `my-app/src/lib/export-renderers.ts`
- `my-app/src/lib/layout/robialGrid.ts`

## Backend

- `cv_parser_service/main.py`
- `cv_parser_service/document_export.py`

## Worker / runtime

- `my-app/scripts/document-export-worker.ts`

## Preview-only files that are not final export source

- `my-app/src/features/verbati/VerbatiResumePreview.tsx`
- `my-app/src/features/verbati/resume/ResumePage.tsx`
- `my-app/src/components/ProposalDisplay.tsx`
- `my-app/src/components/proposal-render/ProposalDocumentRenderer.tsx`

## Legacy export path

- `my-app/src/lib/document-export.ts`

---

## Action map

## OCR / parsing action

- parser service receives uploaded source
- OCR / parse stage builds normalized CV data

## App-state action

- app stores or uses normalized CV/proposal state
- preview renders from state
- export builders also read from state

## Export action

- user clicks export button
- frontend builds normalized export payload
- unified export client sends payload to backend
- parser endpoint calls worker
- worker generates file
- backend returns file
- browser downloads it

---

## Mental model for an LLM

Use this system understanding:

Preview is not export.  
DOM is not source of truth.  
Normalized data is source of truth.  
Robial governs export geometry.  
stylePreset governs styling only.  
Parser service owns direct-download export backend.  
Worker produces PDF/DOCX.  
Legacy screenshot export is no longer the final architecture.

---

## Short operational summary

When debugging:

1. check whether the issue is preview-only or export-only
2. check whether normalized export data is correct
3. check parser endpoint
4. check worker/runtime
5. check Robial geometry
6. check stylePreset influence
7. do not assume preview DOM is the export source

---

## Current project state

The system is now intended to provide:

- stable source-of-truth exports
- ATS-ready PDFs
- styled direct-download PDFs
- proposal DOCX output
- clean local and tunnel workflows
- shared export geometry via Robial

Remaining work is primarily:

- layout fidelity polish
- Docker/runtime slimming
- further visual alignment between preview and styled export