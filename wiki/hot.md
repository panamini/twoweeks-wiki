---
title: "Hot Cache — twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-05-08
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical.
Use it to choose the next pages to read, then trust current durable pages when details matter.

## Current Focus

twoweeks is an active job application operating system centered on CV ingestion/parsing, canonical editable resume data, and contextual generation of resumes, cover letters, and proposals.
The active knowledge model favors retrieval speed for LLM agents: read this cache first, then `wiki/index.md`, then only the few canonical pages that own the topic. Proposal Forge document geometry now has a page-first canonical contract for paper width, toolbar/panel alignment, breakpoint stability, and preview/edit scrollbar ownership.

## Key Active Facts

- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names, not the current product identity.
- Parser truth should flow through structured sections, especially `currentCv.sections[*].structuredContent`, rather than legacy top-level arrays when structured sections are valid.
- Export truth is generated final PDF/DOCX output from normalized data, not the preview DOM alone.
- Local parser work should prefer `./run.sh local-fast`; `local` is not equivalent for full structured upload backend behavior.
- The wiki write path remains `rawinput/ -> raw/`, with `raw/` immutable after ingest.
- One active durable page per subject is mandatory. Update or supersede before creating anything new.
- CV style persistence now uses a metadata-only Convex patch path for style edits; style-only saves no longer send full `cvDocument` and no longer create orphan rows.
- CV Forge edit and preview now share the same 860px paper width; the compact edit-only stage was removed and mobile stays at 100%.
- CV Forge helper AI routing now defaults to `mistral-small-latest` for summary/custom and suggestion actions.
- Rich summary paper-edit parity is implemented in the shared preview renderer; full direct paper editing remains partially deferred.
- `cvforge-preview-linking` e2e assertions were stabilized around dialog heading contracts and close panel semantics to avoid brittle name matching.
- Proposal style selection now treats Style 1/2/3 as durable base styles; manual color/font/layout edits show a custom state and use named palette ids (`terre`, `cobalt`, `ink`, `sauge`, `plum`, `ochre`), with legacy palette ids read-only.
- Settings, CV Forge, and Proposal Forge expose Custom as the seventh accent option. It persists as `palette: "custom"` plus `accentHex`; `paletteOverride` remains only for named palette tokens.
- Settings has one explicit default action: `Set as default`. Clicking a style card edits that slot; clicking the button marks the active default slot. If the default badge jumps, that is a UI/state bug, not the intended model.
- Document Style 1/2/3 has multiple live boundaries: factory slots are in `document-style-slots.ts`, Settings/CV Forge read `proposalSettings.getPresets`, and Proposal Forge reads mirrored current fields from `proposalSettings.getCurrent`. Persisted Convex preset/current fields can override new factory defaults.
- The live save blocker was `proposalSettings.savePreset` collecting and replacing every `userProfiles` row for a Clerk identity. The fix is to read/write the latest indexed profile row only; if Style 2 looks wrong, inspect persisted `proposalPreset2` / `proposalFontPairId` first.
- Proposal Forge document geometry is page-first: `--proposal-paper-visual-inline-size` is the active page width authority; toolbar, compact panel, output shell, preview viewport, and edit body derive from it; preview/edit scrollbars sit at the page edge while edit text keeps a centered reading measure.
- Planner-backed Workshop resume templates now include `workshop_resume_onecol_ats` and `workshop_resume_twocol_ats`; preview, print route, and export consume `committedPages` instead of re-planning independently.
- Proposal AI routing now uses OpenAI `gpt-5.5` for generation, Qwen 3.6 Plus for most visible toolbar actions, Qwen 3.6 Flash for `fix_grammar`, with Mistral then DeepSeek fallbacks; proposal text review now renders as an inline diff overlay in `ProposalDisplay`.
- Proposal signature/closing is now resolved as structured proposal metadata (`closing`): Settings/metadata fallback > legacy parsed closing > generated defaults. The UI/print/export path consumes this structured state; the current implementation is Code-only TypeScript/Convex (no Python signature path).
- Legacy proposal drafts can still contain residual closing text artifacts; planned cleanup is needed so old saved signatures do not force edit/preview oscillation.
- Job summary/keyword match synthesis uses the Ministral/Mistral family, currently defaulting to `ministral-3-3b-instruct-2512`.
- `wiki/index.md` and `wiki/log.md` remain mandatory for every persistent wiki mutation.

## Canonical Pages To Read

- Product state: [[overview]], [[entities/twoweeks]], [[product/product-roadmap]], [[product/product-vision]]
- Parser and import truth: [[concepts/cv-parsing-pipeline]], [[concepts/cv-families]], [[tech/import-ocr-pipeline]]
- Jobs: [[product/job-library]], [[product/job-match-review]]
- Export and layout: [[tech/export-pipeline]], [[tech/preview-to-print-pipeline]], [[tech/workshop-pagination]]
- Proposal geometry and style: [[tech/proposal-forge-document-geometry]], [[tech/proposal-style-layer]], [[tech/proposal-signature-closing-layer]], [[design/document-token-contract]]
- Design system and safety: [[design/ats-safety]], [[design/document-token-contract]], [[design/motion-system]], [[design/brand-voice]]
- Local operations: [[howto/local-parser-operations]], [[tech/local-vs-remote-parser-architecture]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]], [[meta/codex-prompting-standards]]

## Recent Changes

- 2026-05-02: Added this active-memory cache, README startup guidance, and [[tasks/coffee talk]] for syncing collaborator Codex skills.
- 2026-05-02: Added [[howto/wiki-commands-and-llm-export]] for wiki commands and the `wiki/llms.txt` export proposal.
- 2026-05-02: Added an agent memory prompt to README, AGENTS.md, and the wiki commands howto.
- 2026-05-04: Updated PR4 notes: style-only save now routes through Convex metadata-only persistence path; added regression tests on profile patch and adapter behavior.
- 2026-05-04: Synced CV Forge edit/preview paper width to the canonical 860px paper, removed the compact edit-only stage, and aligned helper AI routing to `mistral-small-latest`.
- 2026-05-04: Reworked `e2e/cvforge-preview-linking.spec.ts` to use runtime-true modal heading assertions and shared close action; added localStorage preview-mode seeding (`dasti:cv-forge-workspace-mode:v1`).
- 2026-05-06: Added [[tech/proposal-style-layer]] for the proposal Style 1/2/3 custom-state and named palette contract.
- 2026-05-07: Added [[tech/proposal-forge-document-geometry]] for Proposal Forge page-first width, toolbar/panel geometry, preview/edit scroll ownership, and LLM implementation guardrails.
- 2026-05-08: Updated [[tech/proposal-style-layer]] with the real Style 1/2/3 factory, Settings/CV Forge, and Proposal Forge winning-source pipeline.
- 2026-05-08: Updated [[tech/proposal-style-layer]] with the shared Custom color pipeline for Settings, CV Forge, and Proposal Forge.
- 2026-05-08: Added [[tech/proposal-signature-closing-layer]] and started the structured signature pipeline (draft/output metadata + renderer + export propagation); UI controls remain phased.
- 2026-05-08: Added [[outputs/2026-05-08-ui-audit-proposal-polish]] as a screenshot-only audit snapshot with verified tokens and subjective polish notes.

## Open Threads

- Keep the memory gateway lightweight; do not add local `_index.md` files unless `wiki/index.md` becomes too expensive.
- Consider a future ingest manifest outside `raw/` for source hash dedupe.
- Consider read-only lint support for duplicate durable pages and stale retrieval routes.
- Close loop on `wiki/tech/proposal-signature-closing-layer.md` legacy artifact cleanup and edit-mode lock case before declaring signature migration complete.
- Test daily use of `hot.md` before building `wiki/llms.txt`.
