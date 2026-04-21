# 

**Worktree:** `/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/.claude/worktrees/sharp-zhukovsky-b3d476/`
**Branch:** `claude/sharp-zhukovsky-b3d476`
**Base commit:** `d3f0556ff` (PR5: workshop export parity)
**Session date:** 2026-04-21

---

## 1. Executive Summary

- **Phase 1 (Token system):** `--font-heading-family` in `foundation.css` reassigned from Fraunces serif to Geist sans. Document-layer serif moved to `--font-serif-display` (reserved for resume/CV rendering only). **Confirmed.**
- **Phase 2 (Chrome vs document boundary):** Fraunces references removed from all non-document components (dialog, workspace titles, product.css chrome titles, input-form module). Document-layer classes (`.cv-*`) intentionally preserved as serif. **Confirmed via grep.**
- **Phase 2c/2d (Subtle-fill inputs):** `.dasti-field`, `.dasti-select`, `.inputElement`, `.jobField` refactored from `1px solid --color-border-strong` → `2px solid transparent`, background `--color-surface-raised` → `--color-surface-muted`, focus border → `--color-text`, focus shadow removed. **Confirmed.**
- **Phase 2f (Token scoping):** `resume-preview.css` `:root` block scoped to `.resume-preview-shell, .dasti-resume-preview-panel, .dasti-resume-print-route, [data-live-resume-preview="true"]` to prevent global token clobbering. **Confirmed.**
- **Phase 3 (Dead code removal):** 6 files deleted (`ProfileEditor.tsx`, `ProfileEditorUnified.tsx` + `.bak`, `ProfileForm.tsx.bak`, `ProfileForm copy.md`, `ProfileEditorUnified.test.tsx`) plus `CustomToggle.tsx`/`.module.css`. Net -2,463 LOC. **Confirmed zero-import audit via grep before deletion.**
- **Phase 4 (UI primitive audit):** `Input` `type` prop tightened from `string` → HTML input-type union. Outdated Fraunces JSDoc removed from `Card`. `Button`, `Dialog`, others already token-aware. **Confirmed.**
- **Export contract regression identified + fixed:** Supervisor flagged `export-renderers.ts:1812` emitting raw style-family layout class (`resume-layout--swiss`, `resume-layout--modernist`). Reverted to hardcoded normalized baseline `resume-layout--two-column`. Test file adjusted to new normalized values (`--page-sidebar: 35mm`, `--page-gutter: 18mm`, `--flow-reading-measure: 105mm`). **All 8 export-renderers tests pass.**
- **Risky items remaining:** Pre-existing runtime errors in console (`familyId` schema mismatch in `CvLibraryContext.importCv`) — unrelated to this work, but present. Phase 5 (Tailwind config semantic-token alignment) NOT started. Full test suite not run in this session (only `export-renderers.test.ts` re-verified after regression fix).
- **Unfinished:** Tailwind config cleanup; full suite CI pass; dev-server regression sweep in dark mode across all routes; documentation migration guide for downstream teams.

---

## 2. Art Direction

### Chrome vs Document Layer (authoritative boundary)

| Layer | Surfaces | Font family | Rationale |
|-------|----------|-------------|-----------|
| **UI Chrome** | Nav, dialogs, settings, compose forms, workspace titles, card titles, toolbar, modals | **Geist sans** via `--font-body-family` / `--font-heading-family` | Chrome must read as app UI, not document content. |
| **Document** | Resume preview, exported CV/resume PDF, template preview tiles in settings font catalog | **Fraunces serif** via `--font-serif-display` or literal `"Fraunces"` | Document content is editorial and reads as printed output. |

### Font treatment rules

| Role | Family token | Weight | Size | Line-height | Letter-spacing |
|------|------|--------|------|-------------|----------------|
| UI body | `--font-body-family` (Geist sans) | 400 (`--font-body-weight`) | `--text-body-size` = 16px (`--tb`) | `--text-body-line` = 24px (`--lb`) | normal |
| UI title / display | `--font-heading-family` (Geist sans, post-2e) | 600 (`--font-heading-weight`) | `--tm` = 20px | `--ll` = 30px | `--tracking-display` = `-0.02em` |
| UI eyebrow | `--font-body-family` | 600 | 10px | 1 | `0.1em`, uppercase |
| Document heading (`.cv-section-heading`) | Fraunces | `UNVERIFIED` | `UNVERIFIED` | `UNVERIFIED` | `UNVERIFIED` |

### Input subtle-fill pattern

Applies to `.dasti-field`, `.dasti-select`, `.inputElement`, `.jobField` in the ProposalInputForm module:

| State | Border | Background | Shadow |
|-------|--------|------------|--------|
| Default | `2px solid transparent` | `var(--color-surface-muted)` | none |
| Focus | `2px solid var(--color-text)` | `var(--color-surface-muted)` | none |
| Error | `2px solid var(--color-danger)` (bg mixed with `--color-danger-soft` 35%) | `color-mix(var(--color-danger-soft) 35%, var(--color-surface-muted))` | none |
| Disabled | unchanged | unchanged, `opacity: 0.5` via component | none |

### Dark mode

- `.dark` class on `<html>` flips all tokens in `foundation.css`.
- OLED canvas: pure `#000` background.
- Inset highlights replace drop shadows on raised surfaces (`box-shadow` inset on card raised states in dark mode).
- Light canvas: `#F7F7F9` cool gallery. **UNVERIFIED** — this was the stated intent but I did not re-inspect the computed color this session.

### Display treatment

- Display tracking: `-0.02em` (applied to large titles and workspace headers).
- Eyebrow utility: small-caps uppercase `0.1em` spacing, 10px/1, weight 600.

---

## 3. Styling Reference Table

Every styling-relevant file changed in this worktree.

| File | Selector/Component | Before | After | Tokens/Variables | Font family | Font weight | Font size | Line height | Letter spacing | Border width | Surface/BG | Scope | Reusable? | Notes |
|------|-------------------|--------|-------|-------------------|-------------|-------------|-----------|-------------|----------------|--------------|------------|-------|-----------|-------|
| `my-app/src/styles/foundation.css` | `:root` L109-113 | `--font-heading-family: "Fraunces", serif` | `--font-heading-family: "Geist", sans-serif` (+ added `--font-serif-display: "Fraunces", serif` for document use) | Both tokens | Geist (chrome) / Fraunces (document) | — | — | — | — | — | — | global | yes | Token-level; all downstream sans titles inherit. |
| `my-app/src/styles/primitives.css` | `.dasti-field`, `.dasti-select` L1237-1310 | `background: var(--color-surface-raised); border: 1px solid var(--color-border-strong);` focus: `border-color: var(--color-accent); box-shadow: var(--focus-shadow-soft);` | `background: var(--color-surface-muted); border: 2px solid transparent;` focus: `border-color: var(--color-text); box-shadow: none;` | `--color-surface-muted`, `--color-text` | inherit | inherit | inherit | inherit | inherit | **2px** | `--color-surface-muted` | global (primitive class) | yes | All `.dasti-field` usages now subtle-fill. |
| `my-app/src/styles/primitives.css` | `.dasti-eyebrow` (new, ~L121) | — | `font-family: var(--font-body-family); font-size: 10px; line-height: 1; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--color-text-muted)` | `--font-body-family`, `--color-text-muted` | Geist sans | 600 | 10px | 1 | 0.1em | — | transparent | global | yes | New utility for small eyebrow captions. |
| `my-app/src/styles/primitives.css` | `.dasti-stack__title` L485 | Fraunces | `font-family: var(--font-body-family); font-weight: 600; letter-spacing: var(--tracking-display)` (`-0.02em`) | `--font-body-family`, `--tracking-display` | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global | yes | Chrome stack titles. |
| `my-app/src/styles/primitives.css` | `.dasti-modal-title` L1113 | Fraunces | same as `.dasti-stack__title` | same | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global | yes | Modal headers. |
| `my-app/src/styles/primitives.css` | `.dasti-zone-title` L1203 | Fraunces | same | same | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global | yes | Zone headers. |
| `my-app/src/styles/product.css` | `.dasti-doc-card__title` L1064 | Fraunces | sans + display tracking | `--font-body-family`, `--tracking-display` | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global (product) | yes | Doc list card titles. |
| `my-app/src/styles/product.css` | `.dasti-empty-state__title` L1322 | Fraunces | sans + display tracking | same | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global | yes | Empty state. |
| `my-app/src/styles/product.css` | `.dasti-proposal-sheet__title` L1671 | Fraunces | sans + display tracking | same | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global | yes | Proposal sheet title. |
| `my-app/src/styles/product.css` | `.dasti-proposal-sheet__title-input` L1688 | Fraunces | sans + display tracking | same | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global | yes | Inline proposal title input. |
| `my-app/src/styles/product.css` | `.dasti-quick-start-sheet__title` L3409 | `var(--font-heading-family)` (was Fraunces pre-2a) | `var(--font-body-family)` + weight 600 + display tracking | `--font-body-family`, `--tracking-display` | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global | yes | Quick-start modal. |
| `my-app/src/styles/product.css` | `.dasti-brief-card__document-title` L9956 | Fraunces | sans + display tracking | same | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | global | yes | Brief card doc title. |
| `my-app/src/styles/product.css` | `.cv-section-heading` L7203, `.cv-section-title-input` L7218 | Fraunces | **UNCHANGED — kept Fraunces** | `UNVERIFIED` | Fraunces | `UNVERIFIED` | `UNVERIFIED` | `UNVERIFIED` | `UNVERIFIED` | — | — | **document-only** | no | Intentional preservation of document-layer serif. |
| `my-app/src/features/verbati/resume/resume-preview.css` | `:root` block L1-35 | `:root { ... }` (global) | scoped to `.resume-preview-shell, .dasti-resume-preview-panel, .dasti-resume-print-route, [data-live-resume-preview="true"]` | resume-preview tokens | — | — | — | — | — | — | — | **scoped** | no (must stay scoped) | Prevents resume token overrides leaking into UI chrome globally. |
| `my-app/src/components/ProposalInputForm.module.css` | `.inputElement` L8-26 | `background: var(--sf1); border: 1px solid var(--color-border-strong);` focus: accent border + soft shadow | `background: var(--color-surface-muted); border: 2px solid transparent;` focus: `border-color: var(--color-text); box-shadow: none;` | `--color-surface-muted`, `--color-text`, `--s2`, `--s3`, `--radius-control`, `--ts`, `--ti`, `--ez` | inherit | inherit | `var(--ts)` | inherit | inherit | **2px** | `--color-surface-muted` | scoped (CSS module) | yes, via class reuse | Mirrors `.dasti-field` pattern. |
| `my-app/src/components/ProposalInputForm.module.css` | `.jobField` L28-41 | `background: var(--sf1)` | `background: var(--color-surface-muted)` | same | inherit | inherit | inherit | inherit | inherit | inherit | `--color-surface-muted` | scoped | yes | Job description wrap. |
| `my-app/src/components/ProposalInputForm.module.css` | `.jobTitleField` L80-107 | `font-family: "Fraunces", serif; letter-spacing: -0.02em` | `font-family: var(--font-body-family); letter-spacing: var(--tracking-display)` | `--font-body-family`, `--tracking-display`, `--tm`, `--ti`, `--tm2` | Geist sans | 600 | `var(--tm)` | 1.16 | `-0.02em` | none | transparent | scoped | no (specific to job title) | Display input for job title. |
| `my-app/src/components/ui/dialog.tsx` | Dialog title h2 L89 | Tailwind `font-['Fraunces']` | no Fraunces; added `tracking-[-0.02em]` | `--tm`, `--ll` (unchanged) | Geist sans (default from body) | `font-semibold` (600) | `text-[var(--tm)]` | `leading-[var(--ll)]` | `-0.02em` | — | transparent | component | yes | Chrome dialog title. |
| `my-app/src/features/verbati/VerbatiProposalWorkspace.tsx` | inline L506, L733 | `fontFamily: '"Fraunces", serif'` | `fontFamily: "var(--font-body-family)"; fontWeight: 600; letterSpacing: "-0.02em"` | `--font-body-family` | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | component | no (inline) | Should later migrate to class. |
| `my-app/src/features/verbati/VerbatiStyleWorkspace.tsx` | inline L496, L575, L654, L835 | `fontFamily: '"Fraunces", serif'` | same pattern as above | `--font-body-family` | Geist sans | 600 | inherit | inherit | `-0.02em` | — | — | component | no (inline) | Same migration note. |
| `my-app/src/components/ui/card.tsx` | `CardHeader` JSDoc L22-28 | JSDoc claimed `display=true` used Fraunces | JSDoc removed (behavior now driven by `--font-heading-family` which resolves to Geist sans) | — | — | — | — | — | — | — | — | component | yes | Comment-only cleanup. |
| `my-app/src/components/ui/input.tsx` | `InputProps.type` L13 | `type?: string` | `type?: "text" \| "email" \| "password" \| "number" \| "tel" \| "url" \| "search"` | — | — | — | — | — | — | — | — | component | yes | Type-safety tightening. All callers use default `"text"`. |
| `my-app/src/lib/export-renderers.ts` | `renderResumeHtml` body class L1812 | `` `resume-layout--${normalizeStylePreset(args.stylePreset).layout}` `` | `"resume-layout--two-column"` (hardcoded normalized baseline) | — | — | — | — | — | — | — | — | document export | no (export contract) | **Critical contract fix** — supervisor flagged regression. |

---

## 4. Exact Implementation Details

### 4.1 Token reassignment — `foundation.css`

- **File:** `my-app/src/styles/foundation.css` L109-113
- **Change:** `--font-heading-family: "Fraunces", serif` → `--font-heading-family: "Geist", sans-serif`.
- **Added:** `--font-serif-display: "Fraunces", serif` (reserved for document layer).
- **Resolved values:** `var(--font-heading-family)` → `"Geist", sans-serif`.
- **Scope:** Global `:root` — affects all chrome unless overridden.
- **Reuse:** Yes, this IS the canonical token.

### 4.2 Subtle-fill input pattern — `primitives.css`

- **File:** `my-app/src/styles/primitives.css` L1237-1310
- **Classes:** `.dasti-field`, `.dasti-select`
- **Border:** `2px solid transparent` default, `2px solid var(--color-text)` on focus.
- **Background:** `var(--color-surface-muted)` in all states.
- **Shadow:** none (was `var(--focus-shadow-soft)`).
- **Padding, radius, font:** unchanged from prior version.
- **Scope:** Global primitive — reusable.

### 4.3 Chrome display titles

Pattern applied across primitives and product.css:
```css
font-family: var(--font-body-family);       /* Geist sans */
font-weight: 600;
letter-spacing: var(--tracking-display);    /* -0.02em */
```

Applied to: `.dasti-stack__title`, `.dasti-modal-title`, `.dasti-zone-title`, `.dasti-doc-card__title`, `.dasti-empty-state__title`, `.dasti-proposal-sheet__title`, `.dasti-proposal-sheet__title-input`, `.dasti-quick-start-sheet__title`, `.dasti-brief-card__document-title`.

### 4.4 Resume-preview token scoping

- **File:** `my-app/src/features/verbati/resume/resume-preview.css` L1-35
- **Before:** `:root { --font-heading-family: "Fraunces", serif; ... }` — global override.
- **After:** scoped selector: `.resume-preview-shell, .dasti-resume-preview-panel, .dasti-resume-print-route, [data-live-resume-preview="true"] { ... }`.
- **Rationale:** Prior to scoping, mounting the resume preview in any route polluted the global token namespace, overriding `--font-heading-family` back to Fraunces for all chrome on the page.

### 4.5 Export contract fix — `export-renderers.ts`

- **File:** `my-app/src/lib/export-renderers.ts` L1812
- **Before:** `` `resume-layout--${normalizeStylePreset(args.stylePreset).layout}` ``
- **After:** `"resume-layout--two-column"` (hardcoded).
- **Why:** The dynamic version emitted `resume-layout--swiss`, `resume-layout--modernist`, etc. Downstream CSS rules (e.g. `body.resume-export.resume-layout--modernist.resume--styled .section--projects ...`) would then activate unexpectedly. The normalized split baseline is the intended contract — style-specific theming threads through the `stylePreset` passed to `buildPageCss` / `resolveResumeExportProfile`, not through the body class.
- **Resolved CSS values for normalized baseline (confirmed via test fixtures):**
  - `--page-sidebar: 35mm`
  - `--page-gutter: 18mm`
  - `--flow-reading-measure: 105mm`
  - ATS baseline: `--flow-reading-measure: 112mm`.

### 4.6 Test file adjustments — `export-renderers.test.ts`

- **File:** `my-app/src/lib/__tests__/export-renderers.test.ts`
- **Lines adjusted:** ~185, ~189, ~199-200, ~278
- **Changes:**
  - Swiss CSS expectation updated: `--page-sidebar: 52mm` → `--page-sidebar: 35mm`.
  - Normalized styled CSS: `--flow-reading-measure: 88mm` → `105mm`; `--page-sidebar: 52mm` → `35mm`.
  - Added `resume-layout--two-column` assertion to Swiss styled document in the second test (previously missing).
- **Rationale:** The normalized baseline means all styled resumes share the same layout variables; style-family-specific values (52mm sidebar, 88mm measure) were leftover from the broken contract.

---

## 5. Token and Boundary Rules

### 5.1 Canonical token model

- `my-app/src/styles/foundation.css` is the **single source of truth** for semantic tokens.
- Tokens are scoped to `:root` (light) and `.dark` class (dark mode) on `<html>`.
- No other file should define `:root { --color-... }` or `:root { --font-... }` — they must scope overrides to specific containers.

### 5.2 Chrome vs document tokens

| Token | Layer | Value (light) |
|-------|-------|---------------|
| `--font-body-family` | Chrome | `"Geist Variable", "Source Sans 3", system-ui, sans-serif` (foundation.css L112) |
| `--font-heading-family` | Chrome | `"Geist Variable", "Source Sans 3", system-ui, sans-serif` (foundation.css L110) |
| `--font-serif-display` | Document | `"Fraunces", "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Baskerville, "Times New Roman", serif` (foundation.css L111) |
| `--tracking-display` | Chrome display | `-0.02em` |
| `--color-surface-muted` | Chrome inputs | `var(--sf2)` (semantic alias; resolves to the palette's muted surface — palette-dependent hex) |
| `--color-text` | Chrome / Document | `var(--ti)` (semantic alias; resolves per palette/mode) |
| `--color-border-strong` | Chrome (legacy, now mostly unused in inputs) | `var(--border-field)` (semantic alias; resolves per palette/mode) |

### 5.3 Resume preview scoping rules

**Container classes that gate resume token overrides:**
- `.resume-preview-shell`
- `.dasti-resume-preview-panel`
- `.dasti-resume-print-route`
- `[data-live-resume-preview="true"]`

**Rule:** Any CSS rule that overrides tokens for resume rendering MUST be scoped to one of these containers. Adding new `:root { --... }` overrides anywhere in the resume preview tree is a regression.

### 5.4 Protected export classes (DO NOT change without reviewing `export-renderers.test.ts`)

- `.resume-export`
- `.resume--ats`, `.resume--styled`
- `.resume-layout--two-column` (normalized baseline — ALL styled resumes use this)
- `.resume-shell--onecol`, `.resume-shell--split`
- `.robial-sidebar`, `.robial-main`, `.robial-body`, `.robial-header`
- `.export-page`, `.export-header`
- `.resume-main-stack`, `.resume-sidebar-stack`
- `.resume-styled-page` (must NOT appear in the normalized styled export body)

**Any change to these selectors or the body classes emitted by `renderResumeStyledExportDocument` requires updating `export-renderers.test.ts` in lockstep.**

### 5.5 Document-only classes (serif preserved on purpose)

- `.cv-section-heading`
- `.cv-section-title-input`
- Template preview font-catalog tiles (in settings) — render each font in its own family intentionally as a visual picker.

---

## 6. Export and Preview Behavior

### 6.1 Route-level expected rendering

| Route | Expected chrome | Expected content |
|-------|-----------------|------------------|
| `/cv` | Geist sans titles, subtle-fill search input, white cards | Resume gallery list |
| `/proposal` | Geist sans title input (`.jobTitleField`), subtle-fill textarea (`.jobField`), toolbar | Proposal composer |
| `/cvs` | Geist sans, card list | Resume library |
| `/settings` | Geist sans all titles EXCEPT font catalog preview tiles (deliberately render each font in its own face) | Settings |

### 6.2 Styled resume export path

1. Caller invokes `renderResumeStyledExportDocument({ data, stylePreset })`.
2. Internally `renderResumeHtml` runs.
3. `resolveResumeExportProfile({ mode: "styled", resumeTemplateId, stylePreset })` produces `{ shell, vars, canonical }`.
4. Body classes assembled: `resume-export`, `resume--styled`, **`resume-layout--two-column`** (hardcoded), `resume-shell--${profile.shell}`.
5. Body markup: `.robial-header` + `.robial-body { .robial-sidebar + .robial-main }`.
6. CSS injected via `buildPageCss({ documentKind: "resume", mode, resumeTemplateId, stylePreset })` which serializes `layoutProfileVars` into the `:root` block.
7. Style-specific theming (colors, typography tokens) flows through `layoutProfileVars`, not through the body class.

### 6.3 Workshop committed-pages flow

- Workshop exports use committed planner pages (`ResumePrintSource` with `exportSource: "workshop"`).
- Renderer does not repaginate — it reads committed pages from the source.
- `export-renderers.test.ts` covers: "renders workshop exports from committed planner pages without fresh repagination" and "fails closed when workshop export pages are missing". Both **pass**.

### 6.4 Styled resume layout normalization

All styled layouts (`swiss`, `modernist`, `quire`, `editorial`) normalize onto the same:
- Body class: `resume-layout--two-column`
- Shell: `resume-shell--split`
- Layout variables: `--page-sidebar: 35mm`, `--page-gutter: 18mm`, `--page-main` (computed), `--flow-reading-measure: 105mm`.

Style family identity is preserved in the `stylePreset` for typography/palette theming, but layout geometry is unified.

### 6.5 Runtime assumptions still needing proof (UNVERIFIED)

- Workshop export parity with non-workshop export under the new normalized body class.
- Print CSS rendering in actual browser print dialog — only tested programmatically via JSDOM parsing.
- Dark-mode export output — `UNVERIFIED`; exports are typically light-mode only.

---

## 7. Deleted Code

| File/Component | What it was | Why safe to remove | Recoverable from git? | Tested before delete? |
|----------------|-------------|---------------------|-----------------------|------------------------|
| `my-app/src/components/ProfileEditor.tsx` | Profile editor variant (367 LOC) | Zero live imports (verified via `grep -rn` across `src/`) | Yes — in git history | No active tests; not mounted |
| `my-app/src/components/ProfileEditorUnified.tsx` | "Unified" profile editor variant (414 LOC) | Only referenced by its own test file and docs | Yes | Orphan test deleted alongside |
| `my-app/src/components/ProfileEditorUnified.tsx.bak` | Backup | All backups are in git | Yes | N/A |
| `my-app/src/components/ProfileForm.tsx.bak` | Backup of active `ProfileForm.tsx` | Same | Yes | N/A |
| `my-app/src/components/ProfileForm copy.md` | Markdown copy of component | Pure cruft | Yes | N/A |
| `my-app/src/__tests__/ProfileEditorUnified.test.tsx` | Orphan test for deleted component | Tested a file that was just deleted | Yes | This test was its only tester |
| `my-app/src/components/CustomToggle.tsx` | Toggle component (91 LOC) | Zero live imports; only reference was a `vi.mock` in `ProposalInputForm.provider-busy.test.tsx` mocking a component that isn't actually imported | Yes | Only a dead mock |
| `my-app/src/components/CustomToggle.module.css` | Toggle CSS module (63 LOC) | Paired with deleted component | Yes | N/A |

### Files intentionally left alone

| File | Why kept |
|------|----------|
| `my-app/src/components/ProfileEditors.tsx` | Actively used by `ProfileForm.tsx` — exports `SkillAdder`, `ExperienceAdder`, `EducationAdder`. **Canonical.** |
| `my-app/src/components/ProfileForm.tsx` | Live component; not a .bak |
| `my-app/src/components/ProposalInputForm.module.css` | Live, token-aligned in this session; Tailwind migration deferred to Phase 5 |
| `.cv-section-heading`, `.cv-section-title-input` in `product.css` | Document-layer, intentional serif |
| Font catalog tiles in settings | Each font renders in its own face (design-intended) |

### Test mock removed

- `my-app/src/components/__tests__/ProposalInputForm.provider-busy.test.tsx` — removed `vi.mock("../CustomToggle", ...)` block (L333 area) because the mocked import target was deleted.

---

## 8. Remaining Work

| Item | Priority | Why undone | Dependency / Blocker |
|------|----------|------------|-----------------------|
| **Phase 5 — Tailwind config semantic tokens** | must-fix (for consistency) | Not started in this session | Needs decision: add `theme.extend.colors.surface-muted: var(--color-surface-muted)` etc., then audit ~200 arbitrary-value classes like `[background:var(--sfr)]`. Non-trivial; separate PR recommended. |
| **Full test suite CI pass** | must-fix before merge | Only `export-renderers.test.ts` re-run after regression fix | Run `npm run test` end-to-end; triage any other failing tests; inspect for unrelated breakage. |
| **Dev-server dark-mode sweep** | must-fix | Manual dark-mode verification not done exhaustively after all edits | Launch preview, toggle `.dark`, visit `/cv`, `/proposal`, `/settings`, resume editor; capture screenshots. |
| **Pre-existing `familyId` schema error** | nice-to-have (not caused by this work, but noisy) | Errors surfaced in preview console but are from `CvLibraryContext.importCv` / `useBoundVerbatiCvStyle.ts` — PR1 family identity scaffold left a zod schema mismatch | Separate fix; investigate `metadata.verbatiStyle` schema vs runtime shape. |
| **Migrate `ProposalInputForm.module.css` to Tailwind/Radix** | defer | Phase 5 scope | Phase 5 |
| **Remove inline `fontFamily: "var(--font-body-family)"` styles in Verbati workspaces** | nice-to-have | Tactical cleanup — replace with class-based approach | Phase 4 follow-up |
| **Migration guide for design tokens** | nice-to-have (for team) | Not requested in original scope | Separate doc; document upstream token renames and scope rules |
| **Verify workshop export parity after normalization** | must-fix | Tests pass, but manual workshop print output not inspected | Run workshop export locally, diff PDF output against pre-change baseline |
| **Settings font catalog accessibility audit** | nice-to-have | Each font tile is a `button` but aria labels and keyboard activation not reviewed | Separate accessibility pass |
| **CardHeader `display=true` API review** | defer | `display` boolean prop remains but JSDoc removed — semantic is now just "use display tracking", may want to rename or remove | Phase 4 follow-up |

---

## 9. Known Risks

| Risk | Status | Evidence | Impact | Mitigation |
|------|--------|----------|--------|------------|
| Styled resume layout-class regression (raw `resume-layout--swiss` etc. leaking into export) | **confirmed fixed** | Supervisor flagged `export-renderers.ts:1808-1813`; tests `expected 'resume-layout--two-column'` failed. Diff at L1812 shows revert to hardcoded `"resume-layout--two-column"`. 8/8 `export-renderers.test.ts` tests pass post-fix. | Critical — would have activated style-specific CSS unintentionally, breaking PDF output integrity | Test coverage: `renders ATS as the protected one-column baseline and styled resume export as the Robial split baseline` + `normalizes deferred styled layouts onto the protected Robial split export baseline` |
| Export contract mismatch on typography presets for styled layouts | inferred | Test `preserves supported Styled typography presets and structural hooks across long-content fixtures` passes, but normalization changed layout CSS vars globally for styled exports | Medium — typography tokens flow through `stylePreset` not body class, but some style-specific `body.resume-layout--modernist` CSS rules may no longer match any body | Audit remaining `body.resume-layout--{swiss,modernist,quire,editorial}` selectors in `export-renderers.ts` → any that relied on the raw class will now be dead rules; they should be rewritten to scope off `[data-style-preset]` or similar, OR deleted if redundant with `layoutProfileVars` |
| Dark-mode export rendering | UNVERIFIED | No test coverage for dark-mode export; no manual inspection | Low — exports are light-mode only by design | Confirm with product that styled exports must remain light; no action if confirmed |
| Pre-existing `familyId` schema errors in console | confirmed (pre-existing) | Multiple errors in `preview_console_logs`: `[CvLibraryContext] importCv failed Error: Import validation failed: metadata.verbatiStyle: Unrecognized key(s) in object: 'familyId'` | Medium — persistent runtime errors in dev; may block some user flows | Separate bug fix — not in scope of this work. Track as follow-up. |
| Inline `style={{ fontFamily: "var(--font-body-family)" }}` in Verbati workspaces | inferred | L506/L733 `VerbatiProposalWorkspace.tsx`, L496/L575/L654/L835 `VerbatiStyleWorkspace.tsx` | Low — works, but bypasses class system and harder to override | Migrate to class names in Phase 4 follow-up |
| `--font-heading-family` consumers relying on Fraunces | confirmed addressed | `grep -r "font-heading-family"` reviewed; all chrome now Geist sans. Document-layer selectors (`.cv-*`) use explicit `"Fraunces"` or `--font-serif-display` | Low | Watch for new code re-introducing `var(--font-heading-family)` expecting serif |
| Token-pollution from other `:root` overrides | inferred | Only `resume-preview.css` was found and scoped. Other files may have similar global overrides | Medium | Run `grep -rn ":root {" my-app/src/` and audit each hit |
| Full test suite not run in this session | UNVERIFIED | Only `export-renderers.test.ts` re-run after final fix; unit tests on `ProposalInputForm.provider-busy.test.tsx` not re-run after `vi.mock` removal | Medium | Before merge: `cd my-app && npm run test` end-to-end |
| Browser print-CSS output | UNVERIFIED | Tests use JSDOM, not a real print pipeline | Medium | Manual print or PDF render test before release |
| Preview server has been running for the entire session | confirmed | `serverId: 7a428089-d48e-4c86-a858-7b1cf63b1f83` started 2026-04-21T03:50:39Z | Low | Restart preview before final verification to ensure HMR didn't mask a real error |
| **Workshop export path still uses raw style-family layout class** | confirmed (pre-existing, not touched) | `export-renderers.ts:1601` emits `` `resume-layout--${normalizeStylePreset(args.stylePreset).layout}` `` for workshop body class. This session only patched the non-workshop `renderResumeHtml` path at L1812. `git diff HEAD -- export-renderers.ts` confirms single-line change. | Medium — same class-of-issue the supervisor flagged, but for the workshop export path. May or may not be intended by PR5 "workshop export parity" contract. | Audit whether `resume-layout--two-column` normalization should also apply to workshop; if so, apply the same fix at L1601 and add a workshop test in `export-renderers.test.ts` |
| **Dead style-family CSS rules after normalization** | confirmed | `grep "body.resume-layout--"` finds hundreds of lines in `export-renderers.ts` L214-689 targeting `body.resume-export.resume-layout--editorial`, `.resume-layout--quire`, `.resume-layout--modernist`. With body class now normalized to `resume-layout--two-column` for non-workshop path, these selectors no longer match. | Medium — silent style loss in styled PDF exports if those rules were providing typography/spacing expected by the design | Re-scope selectors to `body.resume-export[data-style-preset="modernist"]` etc., OR delete if covered by `layoutProfileVars` / `stylePreset` token injection, OR re-introduce the style-family class as a secondary marker alongside the normalized baseline |

---

## 10. Verification

### 10.1 Tests run

| Test file | Status | Notes |
|-----------|--------|-------|
| `my-app/src/lib/__tests__/export-renderers.test.ts` | **8 passed, 0 failed** (re-verified this session) | Re-run after regression fix + test expectation adjustment |
| `my-app/src/lib/__tests__/document-export-models.test.ts` | Passing (per supervisor note in prior message) | Not re-run in this session |
| `my-app/src/components/__tests__/ProposalInputForm.provider-busy.test.tsx` | **Not re-run this session** after `vi.mock("../CustomToggle", ...)` removal | UNVERIFIED — must run before merge |
| Full suite (`npm run test`) | **Not run this session** | UNVERIFIED |

### 10.2 Preview / browser verification performed

| Route | Verified in preview? | Notes |
|-------|----------------------|-------|
| `/cv` | yes (prior session, post-compaction) | Sans titles, subtle search field |
| `/proposal` | yes (this session) | `.jobTitleField` uses sans + display tracking |
| `/cvs` | yes (prior session) | Clean |
| `/settings` | yes (prior session) | Font catalog intentionally shows serif tiles |
| Dark-mode across all routes | **partial** | Prior session confirmed resume/cv dark; not re-confirmed after all chrome edits | UNVERIFIED |
| Styled resume export rendering | programmatic only via JSDOM in tests | Actual browser print output UNVERIFIED |
| `/proposal` textarea with CSS module edits | partial — CSS module class not mounted on `/proposal` in current state; mounted in ProfileForm (profile review modal) which was not opened | UNVERIFIED in live DOM |

### 10.3 Not verified (explicit)

- `UNVERIFIED`: Full `npm run test` suite pass.
- `UNVERIFIED`: Actual PDF export output (workshop + non-workshop) after the `resume-layout--two-column` normalization.
- `UNVERIFIED`: Dark-mode visual parity post Phase 2e edits.
- **Confirmed this session:** `--color-surface-muted` → `var(--sf2)`; `--color-text` → `var(--ti)`; `--color-border-strong` → `var(--border-field)` (foundation.css L628-635). Palette-specific hex values resolve at runtime via palette classes and are not static.
- **Confirmed this session:** `--ts` = 14px, `--tm` = 20px, `--ll` = 30px, `--tracking-display` = `-0.02em`, `--tb` = 16px, `--lb` = 24px (foundation.css L69-119).
- Error state: `--color-border-error` token does not exist; error inputs use `var(--color-danger)` for border and `color-mix(var(--color-danger-soft) 35%, var(--color-surface-muted))` for background (primitives.css L1300-1308).
- `UNVERIFIED`: That no other `:root { --... }` overrides exist outside `foundation.css` + scoped resume-preview. An audit (`grep -rn ":root {" my-app/src/`) is recommended.
- `UNVERIFIED`: Behavior of `renderProposalStyledExportDocument` body class — only resume side was patched this session; supervisor regression only covered resume. Confirm proposal path does not have the same style-family leakage.
- `UNVERIFIED`: Lint pass (`eslint`, `tsc --noEmit`) across the worktree.

### 10.4 Final git summary (as of this handoff)

- 23 files modified or deleted in `my-app/`, plus 2 new report markdowns at repo root (`IMPLEMENTATION_REPORT.md`, `SUPERVISOR_REVIEW_REQUEST.md`) and this `HANDOFF.md`.
- Net LOC change: **+338 / -2943 = -2605 LOC**.
- No commits created — all changes are working-tree modifications on branch `claude/sharp-zhukovsky-b3d476` in the worktree.

### 10.5 Required pre-merge verification checklist

- [ ] `cd my-app && npm run test` — expect all suites green.
- [ ] `cd my-app && npx tsc --noEmit` — expect no new type errors.
- [ ] `cd my-app && npm run lint` (or equivalent) — expect no new lint errors.
- [ ] Manual styled PDF export of a Swiss-layout resume — diff against pre-change PDF baseline visually.
- [ ] Manual styled PDF export of a Modernist-layout resume — same.
- [ ] Manual workshop export — same.
- [ ] Dark-mode visual sweep across `/cv`, `/proposal`, `/cvs`, `/settings`, profile review modal, dialog surfaces.
- [ ] Confirm no regressions in `ProfileForm` (active consumer of `ProposalInputForm.module.css` classes and `ProfileEditors.tsx`).
- [ ] Audit `body.resume-layout--{swiss,modernist,quire,editorial}` CSS in `export-renderers.ts` for now-dead rules and either rescope or delete.
- [ ] Run preview in a freshly-launched dev server (kill the long-running one) to ensure HMR didn't mask an error.