---
aliases:
  - CVForge Live Resume Render / Interactive Preview Handoff
---


Date: 2026-04-17  
Branch state: main at d83aa783  
Scope: active code only for the live CVForge resume preview, renderer routing, preview-to-editor linking, and the recent non-Swiss ghost Projects fix.

## 1. What this system is

The live resume preview system is the CVForge runtime that:

1. reads the current canonical CvDocument
2. maps it into renderer-friendly ResumeData
3. chooses a visual renderer variant from the selected style preset
4. renders an interactive preview
5. converts preview clicks into canonical editor intents
6. routes those intents into either modal-owned or inline-owned editing surfaces
7. reflects mutations back into the same preview without a page reload

This handoff covers the active implementation on this branch. It does not treat pdf-ingest/, legacy parser code, backup files, or archive folders as architecture authority.

## 2. Runtime architecture

### Top-level ownership

- Page orchestration: my-app/src/pages/CvForge.tsx
- Preview panel wrapper and source selection: my-app/src/features/verbati/VerbatiCvPreviewPanel.tsx
- Interactive preview viewport and click-intent extraction: my-app/src/features/verbati/VerbatiResumePreview.tsx
- Style preset -> renderer routing: my-app/src/features/verbati/style.ts
- Canonical preview/editor routing metadata: my-app/src/features/verbati/resumeLinking.ts
- CV document -> renderer data mapping: my-app/src/features/verbati/cvDocumentToResumeData.ts
- Actual renderer implementations: my-app/src/features/verbati/resume/ResumePage.tsx
- Canonical editor orchestration: my-app/src/components/ProfileReviewCard.tsx
- Section-level editor behavior and modal opening: my-app/src/components/SectionEditor.tsx
- Modal shell and structured editors: my-app/src/components/structured-blocks/*.tsx

### High-level flow

`CvForge -> VerbatiCvPreviewPanel -> mapCvDocumentToResumeData(currentCv) -> VerbatiResumePreview -> ResumePage(variant selected from style preset) -> user click produces ResumeLinkIntent -> ProfileReviewCard / SectionEditor -> resolve canonical section target -> open modal or focus inline surface -> mutate currentCv -> VerbatiCvPreviewPanel remaps currentCv to ResumeData -> ResumePage rerenders`

## 3. End-to-end pipeline

### A. Canonical document source

The active source of truth is the current CvDocument in the CV library context.

- VerbatiCvPreviewPanel.tsx:56 computes activeData from currentCv
- VerbatiCvPreviewPanel.tsx:74-78 chooses between active data and sample fallback
- VerbatiCvPreviewPanel.tsx:81 defines handleRemoveSection

Important behavior:

- If a real current CV exists and preview source is "active", the preview uses mapped live data.
- Sample/mock data is fallback only.
- The recent ghost Projects bug was not caused by sample fallback. The live active path was rendering a stale optional section shell inside the real renderer.

### B. Mapping layer

my-app/src/features/verbati/cvDocumentToResumeData.ts converts the canonical document into ResumeData.

Important anchors:

- mapProjects: cvDocumentToResumeData.ts:354
- empty-projects return path: cvDocumentToResumeData.ts:356
- section ID map: cvDocumentToResumeData.ts:169
- profileSectionId, summarySectionId, sectionIdsByType: cvDocumentToResumeData.ts:958-960

This file is where section presence is normalized. If Projects is deleted, mapProjects returns []. If the preview still shows a Projects header after that, the bug is in renderer behavior or UI state, not in the mapping layer.

### C. Preview wrapper

my-app/src/features/verbati/VerbatiResumePreview.tsx owns:

- viewport and pan behavior via useDocumentPan
- preview root mounting
- click interception and intent construction
- comparison mode vs single-renderer mode
- activeTarget propagation
- forwarding onRemoveSection into the renderer

Key anchors:

- useDocumentPan: VerbatiResumePreview.tsx:136
- visible preview root marker: VerbatiResumePreview.tsx:228, :530, :582
- renderer receives activeTarget and onRemoveSection: VerbatiResumePreview.tsx:240-241, :516-517
- click lookup for preview section regions: VerbatiResumePreview.tsx:346

data-live-resume-preview="true" is the best runtime marker for the visible preview tree.

### D. Actual renderer

my-app/src/features/verbati/resume/ResumePage.tsx contains the real visual branches. This is the decisive file for “the preview still visibly shows X” bugs.

Active branch dispatch:

- swissminima: ResumePage.tsx:4522
- editorialmag: ResumePage.tsx:4536
- signalgrid: ResumePage.tsx:4562
- default ClassicResumePage: ResumePage.tsx:4589

robial does not have its own page component. It routes into ClassicResumePage.

## 4. Renderer routing

Renderer routing is split across style presets and renderer dispatch.

### Style preset -> renderer

my-app/src/features/verbati/style.ts

- route table: style.ts:82
- swiss -> swissminima: style.ts:86
- volk-register -> swissminima: style.ts:87
- two-column -> robial: style.ts:88
- editorial -> robial: style.ts:89
- modernist -> robial: style.ts:90
- quire -> robial: style.ts:91

This is why the verified live non-Swiss bug reproduced through the classic renderer path.

### Renderer component dispatch

ResumePage.tsx then resolves:

- robial -> ClassicResumePage
- editorialmag -> EditorialMagazinePage
- signalgrid -> SignalGridPage
- swissminima -> SwissMinimaPage

Implication for debugging:

- A visual bug on a non-Swiss preset usually means ClassicResumePage first, not a special robial component.
- Do not trust a style preset name to imply a matching page component exists.

## 5. Preview mapping and interaction metadata

### Canonical preview routing metadata

my-app/src/features/verbati/resumeLinking.ts is now the routing authority for preview section families and canonical editor targets.

Important anchors:

- preview aliases include contact, notes, selected_projects: resumeLinking.ts:19-21
- surface modes include modal, inline, alias: resumeLinking.ts:34
- contact alias metadata: resumeLinking.ts:84-88
- notes alias metadata: resumeLinking.ts:92-96
- projects canonical modal surface: resumeLinking.ts:142
- selected_projects alias to projects: resumeLinking.ts:148-152
- alias normalization switch: resumeLinking.ts:235-240
- preview section classification switch: resumeLinking.ts:321-324

### What aliases mean in practice

- contact is not its own canonical editor surface. It aliases to the profile modal.
- notes is also treated as profile-owned metadata.
- selected_projects is a preview alias that routes back to canonical projects.

This matters for delete controls, preview highlighting, and click routing. If a preview heading says “Selected projects”, the canonical section type is still projects.

## 6. Preview -> editor -> preview linking

### Intent production

Preview clicks originate in VerbatiResumePreview.tsx. The preview DOM exposes section/item metadata through attributes like:

- data-preview-section
- data-preview-section-id
- data-preview-item-id
- data-preview-row-id

The wrapper converts those into a ResumeLinkIntent and forwards it upstream.

### Intent orchestration

my-app/src/pages/CvForge.tsx owns the page-level linking state.

Key anchors:

- workspaceMode: CvForge.tsx:143
- resumeLinkIntent: CvForge.tsx:147
- resumeActiveTarget: CvForge.tsx:149
- link handler: CvForge.tsx:152
- inline-target mode flip from preview back to edit: CvForge.tsx:162-166

Important behavior:

- If the user is in workspace preview and clicks something that should be edited inline instead of through a modal, CvForge switches back to edit mode.
- Modal-capable surfaces stay in preview mode and rely on the hidden editor host to open the canonical modal.

### Editor-side handling

my-app/src/components/ProfileReviewCard.tsx receives resumeLinkIntent and activeTarget.

Key anchors:

- props definition with resumeLinkIntent: ProfileReviewCard.tsx:95
- intent handling guard and dedupe: ProfileReviewCard.tsx:647-684
- inline review panel ref and scroll targeting: ProfileReviewCard.tsx:637, :1368-1446

my-app/src/components/SectionEditor.tsx performs section-level routing and modal opening.

Key anchors:

- canonical section detection: SectionEditor.tsx:1459
- section delete/reorder flow: SectionEditor.tsx:1830-1836
- modal opening for education/projects: SectionEditor.tsx:2057-2061
- custom text canonicalization: SectionEditor.tsx:4243-4260
- modal initial item routing for education/projects: SectionEditor.tsx:5009-5015
- projects container dismiss button rendering: SectionEditor.tsx:5438-5443
- projects modal mount: SectionEditor.tsx:5796-5799

## 7. Canonical modal and inline surfaces

### Modal-owned surfaces

These are the authoritative modal editors for preview-linked sections:

- Profile: my-app/src/components/structured-blocks/ProfileModal.tsx
- Experience / Education: my-app/src/components/structured-blocks/ExperienceEducationModal.tsx
- Projects: my-app/src/components/structured-blocks/ProjectsModal.tsx
- Skills: my-app/src/components/structured-blocks/SkillsModal.tsx
- Languages: my-app/src/components/structured-blocks/LanguagesModal.tsx
- Achievements: my-app/src/components/structured-blocks/AchievementsModal.tsx
- Certifications / Affiliations: my-app/src/components/structured-blocks/CertificationAffiliationModal.tsx
- Hobbies: my-app/src/components/structured-blocks/HobbiesModal.tsx
- Custom / additional text: my-app/src/components/structured-blocks/TextSectionModal.tsx
- Common modal shell: my-app/src/components/structured-blocks/CvModalShell.tsx

### Inline-owned or hybrid surfaces

- ProfileReviewCard.tsx owns the larger editor shell and inline review behavior.
- SectionEditor.tsx decides whether a given section stays inline, opens a modal, or behaves as an alias to another canonical surface.

Rule of thumb:

- If you add a preview-clickable surface and it should behave like a structured block, make it modal-owned and register it in resumeLinking.ts.
- If it is an editor-only convenience surface, keep it inline and let CvForge bounce back to edit mode when clicked from preview.

## 8. Duplicate mounted tree audit

There is a hidden editor host in workspace preview mode, but not a duplicate preview renderer.

Relevant code:

- hidden host wrapper: CvForge.tsx:564
- hidden ProfileReviewCard: CvForge.tsx:565-576
- visible VerbatiCvPreviewPanel: CvForge.tsx:583-591

This hidden subtree exists so modal-capable preview clicks can still resolve into canonical editor surfaces while the user is visually in preview mode.

What it is:

- a hidden editor host

What it is not:

- a second VerbatiResumePreview
- a second ResumePage
- the source of the recent ghost Projects header

Future engineers repeatedly need this distinction. If you see duplicate editing side effects, inspect the hidden ProfileReviewCard. If you see duplicate visible resume rendering, inspect data-live-resume-preview="true" nodes instead.

## 9. Recent bug history and regression risk

### Ghost “Selected projects” header on non-Swiss preview

Verified live bug:

- deleting Projects removed the data
- preview still visibly showed the Projects header on the non-Swiss path

Actual root cause:

- cvDocumentToResumeData.ts already returned projects=[]
- VerbatiCvPreviewPanel.tsx still used the active live CV data
- the real bug lived in ResumePage.tsx, where optional Projects containers were still mounted in some renderer branches even when the list was empty

Patched renderer sites:

- classic / robial path: ResumePage.tsx:1987
- editorial magazine path: ResumePage.tsx:3622
- signal grid path: ResumePage.tsx:4380 area

Important nuance:

- The fix was local to optional Projects call sites.
- MainSection was deliberately not changed globally.
- In signalgrid, Projects shares surrounding layout with Education. Guard the Projects sub-block only. Do not blindly remove the outer shell or you can break Education rendering.

### Why previous fixes missed the bug

The prior tests mostly proved data mutation, not renderer output:

- VerbatiCvPreviewPanel.test.tsx was mocking the real resume renderer in the critical path
- workspace integration tests also mocked ResumePage in places

That allowed “green” tests while the live robial renderer still emitted the ghost heading.

## 10. Known fragile areas

### ResumePage.tsx is high-risk

This file is large and mixes:

- renderer-specific layout logic
- preview interaction metadata
- delete controls
- active target highlighting
- optional section rendering
- comparison mode support

Any change that touches section wrappers, preview data attributes, or optional section guards can create live/UI regressions without obvious TypeScript failures.

### Preview alias drift

If resumeLinking.ts and ResumePage.tsx disagree on section names, you get one of:

- preview clicks opening the wrong editor
- active highlighting on the wrong surface
- delete actions targeting a preview alias instead of canonical type
- regressions where the UI text looks correct but the routed action is wrong

### Hidden editor host confusion

Do not remove the hidden ProfileReviewCard in workspace preview mode unless you are redesigning modal orchestration end-to-end. It is easy to misclassify as dead code because it is display: none, but it is part of live preview-to-modal routing.

### Mock-heavy tests

For render-path bugs, mocked wrapper tests are insufficient. At least one real renderer test is required.

## 11. Test coverage on this branch

### Renderer regression tests

my-app/src/features/verbati/resume/__tests__/ResumePage.test.tsx

Important current coverage:

- empty Projects should not render heading in robial: ResumePage.test.tsx:406-427
- empty Projects should not render heading in editorialmag: ResumePage.test.tsx:406-423
- empty Projects should not render heading in signalgrid: ResumePage.test.tsx:406-423
- Swiss delete button still routes canonical Projects target: ResumePage.test.tsx:448-454

### Wrapper-level regression

my-app/src/features/verbati/__tests__/VerbatiResumePreview.rendering.test.tsx

This is the important new live-path wrapper check:

- uses a Robial-mapped preset with projects: []
- asserts no ghost Projects heading
- asserts exactly one visible [data-live-resume-preview="true"] root per host mode

Anchors:

- test fixture projects empty: VerbatiResumePreview.rendering.test.tsx:52
- heading absence assertion: VerbatiResumePreview.rendering.test.tsx:68
- delete button absence: VerbatiResumePreview.rendering.test.tsx:71
- visible preview root count: VerbatiResumePreview.rendering.test.tsx:74

### Preview panel mapping regression

my-app/src/features/verbati/__tests__/VerbatiCvPreviewPanel.test.tsx

This still matters, but it is not enough by itself. It proves active mapping and deletion flow, not necessarily final renderer correctness.

### Other relevant coverage

- my-app/src/features/verbati/__tests__/resumePreviewInteractionTokens.test.ts
- my-app/src/features/verbati/__tests__/cvDocumentToResumeData.test.ts
- my-app/src/pages/__tests__/CvForge.workspace-preview.integration.test.tsx
- my-app/src/components/__tests__/ProfileReviewCard.addSection.test.ts
- my-app/src/components/__tests__/ProfileReviewCard.import.test.tsx
- my-app/src/components/__tests__/SectionEditor.cv-ai.test.tsx
- my-app/src/components/__tests__/StructuredModalFocus.test.tsx
- e2e/cvforge-preview-linking.spec.ts

## 12. Manual QA checklist

Run this against a real non-Swiss preset, especially two-column.

### Preview rendering

1. Open CVForge with a real CV and active preview source.
2. Switch to a non-Swiss layout such as two-column.
3. Delete the Projects section.
4. Confirm the preview no longer shows:
    - Selected projects
    - Selected Projects
    - any empty Projects container

### Preview linking

1. Click profile/contact rows in preview.
2. Confirm they route to the profile modal, not a phantom contact editor.
3. Click Selected projects items when Projects exists.
4. Confirm the Projects modal opens on the targeted item.
5. Click inline-owned targets from workspace preview.
6. Confirm CVForge switches back to edit mode and focuses the inline surface.

### Duplicate tree sanity

1. Inspect the DOM.
2. Confirm exactly one visible node with data-live-resume-preview="true" per rendered host.
3. Ignore the hidden ProfileReviewCard host unless modal behavior is broken.

### Mutation loop

1. Edit a structured section from preview.
2. Save the modal.
3. Confirm preview updates immediately without needing a source toggle or refresh.

## 13. Safe modification guidance for future engineers and LLMs

### When adding a new preview-clickable section

Change all of these together:

1. resumeLinking.ts
    - add canonical/alias routing metadata
    - define whether the surface is modal, inline, or alias
2. ResumePage.tsx
    - add correct data-preview-* metadata
    - make sure section titles and delete controls report canonical targets
3. VerbatiResumePreview.tsx
    - only extend click parsing if the new surface shape cannot be represented with existing attributes
4. CvForge.tsx
    - make sure preview intents route correctly between workspace preview and edit mode
5. ProfileReviewCard.tsx / SectionEditor.tsx
    - open the canonical inline or modal surface
6. tests
    - add at least one real renderer test
    - add one wrapper or integration regression

### When fixing optional-section bugs

- Prefer local guards at the renderer call site.
- Do not “fix” optional empty headers by changing MainSection globally.
- Check all sibling renderer branches with the same section shape, but keep the patch narrow.

### When debugging live-vs-test mismatches

- Trust the visible product behavior over mocked tests.
- First identify the real renderer branch from style.ts.
- Then verify which ResumePage.tsx branch actually renders.
- Only after that inspect mapping and source selection.

### When touching workspace preview mode

- Preserve the hidden editor host unless you are replacing the modal-routing architecture.
- Verify both hostMode="panel" and hostMode="workspace" behaviors.

### What to treat as likely bug entry points

- ResumePage.tsx section wrappers and optional guards
- resumeLinking.ts alias tables
- VerbatiResumePreview.tsx click target extraction
- CvForge.tsx workspace mode / intent handoff
- SectionEditor.tsx canonical routing and modal open paths

## 14. Short maintenance rules

- Renderer bug: inspect ResumePage.tsx before assuming state or mapping corruption.
- Alias bug: inspect resumeLinking.ts before adding ad hoc routing in editor code.
- Modal routing bug: inspect CvForge.tsx hidden host and ProfileReviewCard.tsx intent handling.
- Delete/empty-section bug: verify canonical data is empty, then verify the renderer subtree actually unmounts.
- Test bug: add one real renderer assertion before trusting wrapper or integration mocks.