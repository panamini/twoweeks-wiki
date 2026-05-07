---
title: "Workshop Pagination"
category: tech
tags: [workshop, resume, pagination, preview, print, export, committed-pages]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-27-workshop-pagination, 2026-04-27-test-headless-browser-setup-workshop-preview-probe]
related: [[tech/preview-to-print-pipeline]], [[tech/export-pipeline]], [[design/document-token-contract]], [[tech/workshop-token-parity]]
---

# Workshop Pagination

Workshop pagination is the planner-driven page-boundary system for planner-backed Workshop resume templates, currently `workshop_resume_onecol_ats` and `workshop_resume_twocol_ats`. `committedPages` is the authoritative source of page breaks for preview, print, and export.

## Current state

The active path is:

- `VerbatiResumePreview.tsx`
- `ResumeTemplateRenderer.tsx`
- `resumePagination.ts`
- `ResumeOneColAtsPage.tsx`
- `ResumeTwoColAtsPage.tsx`

The planner computes internal `pages` and serialized `committedPages`. The renderer and export layers should consume committed pages rather than inventing new boundaries. Column placement for two-column Workshop remains renderer-local unless measured browser validation proves that the committed page payload must carry column metadata.

## Section rules

- `experience` is the only section allowed to split inside a single entry.
- compact sections are atomic per item.
- `selected_projects` must stay contiguous so later sections do not outrun unfinished project content.
- `additional_information` and `custom` share the long-form text-section path, with custom titles preserved in metadata.

## Geometry

The shared Workshop base uses:

- top: 17mm
- right: 35mm
- bottom: 18mm
- left: 18mm

The two-column variant adds:

- gutter: 12mm
- sidebar/main widths owned by Workshop template tokens

The 18mm bottom inset is the current workshop state, not the older 35mm legacy margin.

## Validation

Use planner tests, renderer tests, print-route tests, export parity tests, token hardcode audits, and browser-backed font parity harnesses when a change can affect wrapping, page fit, font family, or section continuation.

Browser-backed validation remains decisive for pagination and typography; unit tests alone are not enough for live-fit changes.

## Sources

- [[sources/2026-04-27-workshop-pagination]]
- [[sources/2026-04-27-test-headless-browser-setup-workshop-preview-probe]]

## Related

- [[tech/workshop-token-parity]]
- [[tech/preview-to-print-pipeline]]

