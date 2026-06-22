---
aliases:
  - CV Forge Save / Restore Pipeline Fix
---


Date: 2026-06-07
Branch: `codex/proposal-save-sanity-docs`
Scope: active `v1` CV Forge save, import, drawer, and route paths.

## User Symptom

The broken user flow was persistence that looked correct in storage but wrong in the UI after refresh or drawer selection.

- Creating a new CV, typing, and refreshing could preserve the CV.
- Importing a parsed PDF could create a full `cv:<id>` record and compact `cvDocuments` entry, but the drawer could still omit the current CV or load another CV after refresh.
- Clicking a saved CV in the drawer could stall on `Loading CV...` while an outgoing save was pending.
- A browser probe showed the important storage facts were already true: `routeId`, active library id, compact library entry, full CV cache, and section count could all exist for the same CV id.

That made the bug a coordination failure between the active CV, route, local cache, drawer model, and async save switching path, not a simple missing localStorage write.

## Broken Invariants

These are the user-facing invariants the fix restored.

1. The current CV must appear in the drawer/library even if the compact `cvs` state is temporarily stale.
2. Importing a parsed CV must make that CV the active document and align `/cv?id=...` before the remote save promise finishes.
3. A drawer click on a saved CV must load the clicked CV immediately when the full local cache exists.
4. Switching CVs must not block forever on the outgoing remote save.
5. A background save for the outgoing CV must not update dirty/saved bookkeeping for the newly active CV.

## Active Code Path

| Area | Active files / functions | Status |
| --- | --- | --- |
| CV route page | `my-app/src/pages/CvForge.tsx` | active code |
| CV context and save/load | `my-app/src/contexts/CvLibraryContext.tsx` | active code |
| CV drawer shell | `my-app/src/pages/CvForgeCvDrawer.tsx` | active code |
| Library drawer shell | `my-app/src/pages/CvForgeLibraryDrawer.tsx` | active code |
| Shared drawer model | `my-app/src/lib/application-library.ts` | active code |
| Local full document cache | `cv:<id>` localStorage keys | active code |
| Compact CV index | `cvDocuments` localStorage key | active code |
| Current CV pointer | `dasti:cv-library-current-id:v1` localStorage key | active code |

## Root Causes

- Drawer recents were derived from alternate documents first, so the current CV could be missing from the prominent drawer region.
- `buildWorkLibraryModel(...)` only trusted the compact `cvs` array and had no active-document fallback.
- The import path could set the active CV before the route fully reflected that new id, creating a temporary `activeId` / `routeId` mismatch.
- `loadCv(...)` waited on an outgoing remote save before loading the target CV, so a slow or failing remote save could block a local drawer switch.
- `performSave(...)` updated `lastSavedRef` after saves that no longer belonged to the active CV, which made the new active CV's dirty state vulnerable to old save completions.

## Fixes Applied

- `CvForgeCvDrawer` and `CvForgeLibraryDrawer` now lift the current CV into the drawer recents/top section.
- `buildWorkLibraryModel(...)` accepts `currentCv` and merges it into the CV collection when the compact library list lags.
- `CvForge` now uses a centralized `selectCvById(...)` path for route and context selection.
- CV import/create uses a pending route transition guard so `/cv?id=...` is repaired when the imported CV becomes active while save is still pending.
- `CvLibraryContext.loadCv(...)` caches/syncs the outgoing CV locally, starts the outgoing remote save in the background, then loads the requested target CV immediately.
- `performSave(...)` only updates `lastSavedRef` when the saved document id still matches the current active CV id.

## Step-By-Step Pipeline

### New CV, Type, Refresh

1. `createNewCv(...)` creates the new document id and sets it as current.
2. The full document is cached under `cv:<id>` and the compact `cvDocuments` library index is updated.
3. `/cv?id=<id>` is selected through the same route/load path used by drawer clicks.
4. Edits update current document state and local full-cache state before relying on remote persistence.
5. After refresh, the app restores the active id and full cached document, and the drawer model includes that current document even if the compact list hydrates later.

### Import Parsed PDF, No Manual Edit, Refresh

1. The parser returns sections and metadata.
2. `importCv(...)` normalizes the parsed payload into a full CV document.
3. The parsed CV is set as current, written to `cv:<id>`, inserted into `cvDocuments`, and scheduled for save.
4. The pending route transition aligns `/cv?id=<imported-id>` once the imported CV becomes active.
5. The drawer model receives `currentCv`, so the parsed CV remains visible before and after refresh even without a later manual edit.

### Import Parsed PDF, Modify, Refresh

1. The same import pipeline writes the parsed CV locally and selects it.
2. User edits update the active document and refresh the full local cache.
3. Debounced/remote save can lag without changing which CV is current.
4. After refresh, route id, active id, compact entry, and full document cache resolve to the modified imported CV.

### Drawer Click On Saved CV

1. Drawer selection uses `selectCvById(...)`.
2. The outgoing active CV is cached locally before switching.
3. The outgoing remote save runs in the background.
4. The clicked target CV loads from full local cache or remote fallback without waiting for that outgoing remote save.
5. If the old save completes late, it cannot mark the new active CV as clean because `lastSavedRef` is guarded by active id.

## Regression Tests

Tests added or updated for the fixed invariants:

- `my-app/src/contexts/__tests__/CvLibraryContext.test.tsx`
  - `switches to a locally available cv without waiting for an outgoing remote save`
- `my-app/src/pages/__tests__/CvForge.workspace-mode.test.tsx`
  - `moves the route to an imported CV before the save promise resolves`
  - `keeps the route aligned when an imported CV becomes active while save is pending`
- `my-app/src/lib/__tests__/application-library.test.ts`
  - `includes the active current CV when the library list is stale`
- `my-app/src/pages/__tests__/ForgeRailDrawers.test.tsx`
  - current CV is visible in the library drawer.
  - current CV is visible in the CV drawer recent section.

## Verification

Targeted verification already passed on the CV fix branch:

```text
rtk npx vitest run src/contexts/__tests__/CvLibraryContext.test.tsx -t "switches to a locally available cv without waiting|auto-persists when dirty|hydrates a compact cvDocuments index|restores the active cv from full cached storage|mirrors imported CV content|restores edited full cache"

rtk npx vitest run src/pages/__tests__/CvForge.workspace-mode.test.tsx -t "keeps the route aligned when an imported CV becomes active while save is pending|moves the route to an imported CV before the save promise resolves|clears the parsing pending state after parser returns sections"

rtk npx vitest run src/lib/__tests__/application-library.test.ts src/pages/__tests__/ForgeRailDrawers.test.tsx

rtk npx tsc --noEmit
```

Result: all targeted CV persistence and drawer guard rails passed.

## Known Boundary

A broad `CvForge.workspace-mode` file run still contains unrelated pre-existing failures outside this fix pass, including older call-count assumptions and test-environment issues such as `container is not defined`. Those broad failures were not treated as proof against the targeted persistence fix because the new user-facing invariants above are covered by focused green tests.

## Practical Standard Going Forward

CV Forge should be treated as a single save/restore pipeline, not separate "new CV" and "import CV" behaviors.

For every CV source, the required sequence is:

1. create or parse the full CV document.
2. set that CV as the active current document.
3. write the full local `cv:<id>` cache.
4. upsert the compact `cvDocuments` library entry.
5. write `dasti:cv-library-current-id:v1`.
6. align `/cv?id=<id>`.
7. render drawer/library from compact docs plus the current CV fallback.
8. run remote save asynchronously without blocking local restore or drawer switching.

If any future change saves only one of those layers, the same class of bug can return.
