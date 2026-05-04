# CV forge PR4 remaining tasks

Date: 2026-04-30

Scope: PR4 CV forge only. Do not start PR5. Do not touch proposal, jobs, dashboard, or `my-app/src/lib/ai/*`.

Skeleton source: `.claude/worktrees/hungry-mcnulty-1722ea/docs/UI/APP-SKELETON.html`

## Current decision

The PR4 architecture stays section-scoped:

- The CV paper is the live preview and section focus target.
- Real editing happens in the section sheet.
- The rail owns section organization, section-scoped Ask AI, style, and import entry points.
- Skills, Languages, and Hobbies are structured chip/list sections, not prose rewrite sections.

## 2026-05-01 checkpoint addendum

This document predates the current PR4 implementation pass. Treat this addendum as the current checkpoint before continuing CV Forge work.

Confirmed updated state from local implementation notes:

- Direct paper editing has been implemented. The remaining risk is page-end pagination/section rendering quality, not whether paper editing exists.
- Type-specific section sheets are close to done. Do not restart them from scratch; inspect active components and close concrete gaps only.
- Rail Ask AI is close to structured section actions. Continue wiring section-specific actions where active backend support exists instead of replacing the whole flow.
- Summary tone was removed as a separate path and tied to the default tone. Remaining gap: the live AI toolbar may still not pass the user's default tone into AI requests.
- Import UI is mostly implemented. Remaining work is parser/import correctness and polish, especially Python parsing and end-state validation.
- Section operations are mostly stable. Delete still lacks undo; DND hover/animation/paper/glass styling is polish unless behavior is unstable.
- Mobile/narrow verification has not been done.
- Proposal Forge and Jobs still need active-code audits against the app skeleton before final merge. Do not assume the old PR1-PR3 closure checks prove those pages are finished; the reset PR4 branch may include mixed implementation history.

Current priority order:

1. Fix the CV save-size / Convex payload bug first. It can break autosave and style-only saves, so it is the main non-polish risk.
2. Do a narrow CV browser smoke after the save-size fix: desktop, narrow desktop, basic paper editing, rail usability, and Ask AI behavior by section type.
3. Audit Proposal Forge and Jobs against `APP-SKELETON.html` using active code only. Record concrete repair tasks instead of relying on closed PR1-PR3 assumptions.
4. Do page-by-page final parity and polish after the core implementation is stable: CV, Proposal, Jobs, Dashboard/Shell.

Tone is probably not useful for every CV section. Keep tone as a writing hint only for prose-heavy sections if the product keeps exposing tone controls:

- Summary: useful and should be the primary tone target.
- Experience and Education prose: sometimes useful for bullet/paragraph phrasing.
- Skills, Languages, Hobbies, Certifications: not useful for names/chips. Do not send tone to structured suggestion actions unless the backend explicitly supports it.

Do not persist tone into CV metadata until the schema explicitly supports it. Current safe behavior is local UI/request state or the existing user default tone, provided live AI requests receive it intentionally.

## Remaining PR4 tasks

1. Finish type-specific section sheets.
   - Status checkpoint: close remaining gaps only; this is no longer a from-scratch task.
   - Profile: name, headline, contact fields.
   - Summary: prose editor with summary-specific AI.
   - Experience: role/company/date/bullet list editor.
   - Education: school/degree/date/details editor.
   - Skills/Languages/Hobbies: chip editors with add/remove and structured suggestions.
   - Projects/Certifications/Awards/Volunteer/References: generic list editor.
   - Custom: named rich-text body only.

2. Replace the generic rail Ask AI for typed modules with the active structured module actions.
   - Status checkpoint: continue from the current structured-action wiring; do not rebuild the whole rail AI flow without proving it is necessary.
   - Skills: use `generate_skills_suggestions`.
   - Languages: use `generate_language_suggestions`.
   - Hobbies: keep local suggestion-library behavior unless a backend action exists.
   - Achievements: use `improve_achievement_line` per item, not whole-section raw text.
   - Experience responsibilities: use `improve_experience_responsibilities` per item.

3. Add a clean Summary tone path.
   - Status checkpoint: separate Summary tone was removed and linked to the user's default tone.
   - Remaining work: confirm live AI toolbar requests actually receive the user's default tone where tone is supported.
   - If tone becomes persistent later, add it to the CV schema intentionally before writing it into `metadata`.

4. Harden save size.
   - Prevent rail AI accept flows from writing large duplicated prose into structured sections.
   - Add a guardrail test that a Skills AI suggestion append does not inflate the CV payload.
   - Investigate existing oversized profile payloads separately from PR4 UI wiring.
   - Active browser bug: `CvLibraryContext.tsx:1901` repeatedly logs `save failed Error: [CONVEX M(profiles:patch)] ... Value is too large (1.16 MiB > maximum size 1 MiB)` and then `1.17 MiB > maximum size 1 MiB`.
   - Observed call path: `ConvexStorageAdapter.save` at `StorageAdapter.ts:192`, `performSave` at `CvLibraryContext.tsx:1830`, debounced save at `CvLibraryContext.tsx:2052`, called after `CvLibraryContext.tsx:2835`, triggered from `useBoundVerbatiCvStyle.ts:66` after its debounce at `useBoundVerbatiCvStyle.ts:56`.
   - Treat this as a save-payload/root-state bug, not just an AI-output bug. Start by measuring the exact payload passed into `profiles:patch` when style changes or autosave runs.
   - Confirm whether `metadata.authoritativeResume`, `metadata.importRecoverySession.baseSectionsSnapshot`, duplicated `blocks` + `structuredContent`, or repeated style writes are pushing the profile document over Convex's 1 MiB value limit.
   - Add a regression test or diagnostic assertion that style-only changes do not write/import the full oversized CV/profile payload when no section content changed.

5. Finish import review behavior.
   - Status checkpoint: import UI is close; remaining work is parser/import correctness and polish unless active behavior proves otherwise.
   - Review banner should show only unresolved or weak import blocks.
   - Import Review sheet should support Accept/Edit/Delete against active CV state.
   - Export should keep warning when parser URL is unresolved or import review is pending.

6. Complete section operations.
   - Keep reorder persisted and keyboard-accessible.
   - Keep hide/show stable without focus jumps.
   - Add delete undo.
   - Treat DND hover animation and section surface styling as polish unless behavior is unstable.
   - Add browser-backed checks for all three operations on a disposable CV fixture.

7. Harden direct paper editing.
   - Status checkpoint: direct paper editing has been implemented.
   - Verify it shares the same typed section update paths as the sheets to avoid duplicate editors.
   - Improve pagination and section display at page ends where the rendered page currently degrades.

8. Browser verification still needed.
   - Desktop and narrow desktop: rail remains usable beside the paper.
   - Mobile: rail stacks below the paper intentionally.
   - Ask AI: structured sections show add/dismiss suggestions, prose sections show preview-before-apply.
   - Import: pending state appears and parser URL failure is not treated as success.
   - Style: labels match rendered font mappings.

## Known environment boundary

The local browser still warns:

`[structuredUpload] Parser URL unresolved. Ensure start-parser-service.sh has populated .parser-tunnel-url.`

Do not treat live PDF import as verified until parser config is available.
