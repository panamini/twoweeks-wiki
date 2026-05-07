---
title: "CV Forge PR4 remaining tasks"
category: source
tags: [cv-forge, parser, sections, ai, import]
created: 2026-04-30
updated: 2026-05-04
status: current
type: scratchpad
related: [[product/product-roadmap]], [[concepts/cv-parsing-pipeline]], [[tech/workshop-pagination]], [[tech/local-vs-remote-parser-architecture]]
---

# CV Forge PR4 remaining tasks

This source captures the current PR4 continuation notes and implementation risks.

## Scope note

- PR4 scope: CV forge only. No broad PR5 work.
- Keep existing module boundaries; avoid mixing with proposal/jobs/dashboard.

## Confirmed implemented state

- Summary-rich paper editing parity is implemented in the shared preview renderer; full direct paper editing for every structured section remains a follow-up.
- CV Forge edit and preview now share the same 860px paper width; the compact edit-only stage was removed and mobile collapses to 100%.
- CV Forge helper AI routing now defaults to `mistral-small-latest` for summary/custom and suggestion actions.
- Type-specific section sheets are near completion.
- Rail Ask AI is close to structured section actions.
- Summary tone was folded into default tone; only the default-tone pass needs verification.
- Import UI is mostly complete; remaining risk is parser/import correctness and smoke polish.
- `e2e/cvforge-preview-linking.spec.ts` now uses stable, runtime-aligned dialog selectors and close-button handling for preview-linking assertions.

## Verification notes

- Cross-browser run status: Chromium passing; Firefox/WebKit checks are blocked locally by missing browser executables.

## Current priority order

1. Reconfirm cross-breakpoint Proposal visual QA (`desktop`, `tablet`, `mobile`) in both themes, then freeze styles.
2. Run narrow browser smoke only if the Proposal pass exposes a regression.
3. Audit Proposal Forge and Jobs against the active app skeleton before final merge.
4. Final parity/polish pass (Proposal, Jobs, Dashboard/Shell, and any residual CV drift).

## Remaining PR4 tasks

1. Finish type-specific section sheets and close remaining gaps.
   - Profile, Summary, Experience, Education, chips-based Skills/Languages/Hobbies, and generic list editors.
2. Replace generic rail Ask AI with active structured module actions:
   - `generate_skills_suggestions`
   - `generate_language_suggestions`
   - achievements line-level improve action
   - `improve_experience_responsibilities`
3. Hardened: metadata-only style persistence now uses a metadata patch path; regression guardrail exists (convex + adapter tests). ✅ 2026-05-04
4. Finish import review behavior (pending/weak block filtering, Accept/Edit/Delete, unresolved parser warning).
5. Complete section operations (reorder persistence, hide/show stability, delete undo).
6. Verify the remaining full direct paper editing path (beyond summary-rich parity) shares typed section update flow.
7. Run browser verification for desktop, narrow desktop, mobile, Ask AI behavior, import state, and style labels if any drift remains.
8. Validate preview-linking sheet flow in `cvforge-preview-linking` (`/cv`) with stable section/modal assertions (dialog heading + close panel locator).

## Source

- `raw/2026-04-30-cv-forge-pr4-remaining-tasks 1.md`
- `raw/2026-04-30-cv-forge-pr4-remaining-tasks.md` (pré-`1.md`; contenu partiellement redondant, dédupliqué sans nouvelle entrée)
