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

- Direct paper editing is implemented.
- Type-specific section sheets are near completion.
- Rail Ask AI is close to structured section actions.
- Summary tone was folded into default tone; only the default-tone pass needs verification.
- Import UI is mostly complete; remaining risk is parser/import correctness and smoke polish.

## Current priority order

1. Fix CV save-size / Convex payload bug (critical behavior risk for autosave and style-only saves).
2. Run narrow browser smoke after payload fix (`desktop`, `narrow`, paper edit/rail/Ask-AI section behaviors).
3. Audit Proposal Forge and Jobs against the active app skeleton before final merge.
4. Final parity/polish pass (CV, Proposal, Jobs, Dashboard/Shell).

## Remaining PR4 tasks

1. Finish type-specific section sheets and close remaining gaps.
   - Profile, Summary, Experience, Education, chips-based Skills/Languages/Hobbies, and generic list editors.
2. Replace generic rail Ask AI with active structured module actions:
   - `generate_skills_suggestions`
   - `generate_language_suggestions`
   - achievements line-level improve action
   - `improve_experience_responsibilities`
3. Harden save-size path and add regression guardrail test.
4. Finish import review behavior (pending/weak block filtering, Accept/Edit/Delete, unresolved parser warning).
5. Complete section operations (reorder persistence, hide/show stability, delete undo).
6. Verify direct paper editing path shares typed section update flow.
7. Run browser verification for desktop, narrow desktop, mobile, Ask AI behavior, import state, and style labels.

## Source

- `raw/2026-04-30-cv-forge-pr4-remaining-tasks 1.md`
- `raw/2026-04-30-cv-forge-pr4-remaining-tasks.md` (pré-`1.md`; contenu partiellement redondant, dédupliqué sans nouvelle entrée)
