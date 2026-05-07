I inspected the repo to ground this plan. Key findings:

- Frontend lives in `my-app/` (Vite + React + TS).
- Token system already exists: `my-app/src/styles/foundation.css` (DASTI v1) defines `--bg, --sf1/sf2/sf3/sfr, --ti, --tm2, --tg2, --ac, --am, --as, --ap, --fr, --border-soft/field/strong, --radius-1..4, --radius-pill, --sha/shb/shc, --ok/er/wa`, palettes in `themes.css`, and product-scoped CSS in `product-*.css`.
- Pages: `DashboardPage.tsx, JobsPage.tsx, DocumentsPage.tsx, TemplatesPage.tsx, SettingsPage.tsx, CvForge.tsx, ProposalForge.tsx`. Component dirs: `components/{cv-editor, jobs, onboarding, proposal, header, ui, ...}`. `CommandPalette.tsx` exists at `components/CommandPalette.tsx`.
- `tailwind.config.js` is near-empty (Tailwind not the primary styling layer); CSS variables are the contract.

The plan below maps the audit onto these real surfaces. Where I'm not certain a class name exists, I mark it `[verify]`.

---

# Twoweeks UI Quality Gap — Full Implementation Plan

## 1. Executive summary

The product looks 65/100. The single biggest gap is that **light mode and dark mode are not the same product** — light mode (landing, onboarding, templates, settings) is editorial and confident; dark mode (dashboard, documents, CV/proposal editor app shell) is flat, low-elevation, and over-saturated with brand orange. Secondary gap: brand accent is over-used as both CTA color and status color, so nothing wins visually.

What must be fixed first: **token semantics**. The DASTI tokens (`--sf1/2/3/r`, `--ti`, `--ac/am`, `--border-*`, `--radius-*`, `--shb`) exist but are applied unevenly across product-scoped CSS. Normalize their meaning, then re-thread them through the dark app shell, document/job cards, and right rails. After that, fix density (Documents grid, KPI row, Verdict rail) and chip semantics.

What must NOT change: routing, data flow, editor logic, CV/proposal renderers, export pipeline, auth, the brand palette (`--ac/am` Terre/clay), the editorial serif on documents.

Target quality bar: **80/100**. App shell parity light↔dark, single-CTA-per-view discipline, definition-list right rails, dense Documents grid with real previews, visible focus rings, status colors decoupled from brand orange.

## 2. Core design diagnosis

|Topic|Current problem|Why it hurts|Target behavior|Implementation direction|
|---|---|---|---|---|
|Accent semantics|`--ac/--am` used for CTA, status pills (Probably skip), section bullets, active nav, brand chips|Primary action invisible|One CTA per view; status uses `--wa/--ok/--er`; bullets use `--tg3`|Re-map class usages, not the tokens|
|Light/dark parity|Different paddings, type ratios, accent intensity per mode|Brand cliff between onboarding and app|Theme = swap `--bg/--sf*/--ti/--ac` only|Audit `.dark` overrides, remove mode-specific paddings|
|Dark surface hierarchy|Cards on `--sf2` only — no second elevation|Dashboard reads as a slab|3 elevations: page `--bg`, card `--sf2`, raised `--sfr` + 1px hairline|Apply existing `--sfr` to the Next-Best-Action card and toolbars|
|Typography hierarchy|H1 sits next to similarly-weighted serif body|Hero collapses|Larger weight delta, sans for app body, serif scoped to letter|Tighten `--type-h1`, scope serif via `.document-paper`|
|App vs document type|Serif appears in app chrome|Reading effort, weak hierarchy|App: sans (Inter/Geist). Document: serif (Baskerville/Fraunces)|Restrict `--font-document` to `.document-paper` containers|
|Verdict rail structure|Skills/Seniority/Location/Gap labels and values share weight, ragged wrap|Looks unfinished|2-col definition list, fixed label column|Build `.verdict-grid` in `product-jobs.css`|
|Card density|Documents cards 240px tall, 2 lines of text|Looks like skeletons|140–160px, status+type inline, `…` menu|Edit `[document card component]` in `DocumentsPage.tsx`|
|Pills/chips|Pills carry company, location, source, status equal weight|Visual noise|Pills = status only; meta = text row|Replace pill stack with text·dot·text row|
|Radius|Inputs ~10, buttons ~12, cards ~16, pills 999, mixed|Hand-picked feel|Map components to `--radius-1/2/3/pill` strictly|Sweep usages|
|Focus|Not verified; likely missing on custom controls|a11y risk|Visible 2px ring via `--fr`, `:focus-visible` only|Add global `:focus-visible` rule in `base.css`|
|Sidebar active|Color-only state|a11y, low affordance|Background `--sf2` block + thin accent stripe|Edit nav component|
|Template/style previews|Empty rectangles labelled "Style 1"|Style is hidden|Real mini-letter preview|Render miniature component|
|Onboarding progress|6 quiet bars, "Step 3 of 6" disconnected|Unclear status|Labeled bars, larger active state, count adjacent|Edit `components/onboarding/...`|
|Command palette|Default highlight on "Replay onboarding"; mixed kbd format|Risky default, scattered|No default highlight; consistent `<kbd>` chips|Edit `CommandPalette.tsx`|

## 3. Design system contract

### Colors

- **Page bg**: `--bg` (light `#FAF9F5`, dark `#0D0D0D`)
- **Surfaces**:
    - `--sf1` sidebar chrome
    - `--sf2` cards/panels (default elevation)
    - `--sfr` raised (Next-Best-Action card, toolbars, popovers, modals)
    - `--sf3` subtle hover/input fill
- **Foreground**:
    - `--ti` primary
    - `--tm2` secondary (~64% in light, ~58% in dark)
    - `--tg3` tertiary/labels
- **Borders**: `--border-soft` (default), `--border-field` (inputs), `--border-strong` (dividers/selected)
- **Accent**: `--ac` (interactive ink), `--am` (CTA fill), `--am-soft` (active pill fill), `--ap`/`--as` (washes)
- **Status**: `--ok/--okb/--okt`, `--wa/--wab/--wat`, `--er/--erb/--ert` — use these for "Probably skip", "Strong match", "Drafting", etc.
- **Dark mode** must use only `.dark` overrides on the same tokens. No new dark-only padding/radius.

### Typography

- **App body**: existing app sans (Inter or Geist — `[verify in foundation.css @font-face / --font-app]`).
- **Document body**: serif (Baskerville/Fraunces) — applied only inside `.document-paper`, `.letter`, `.resume-page`.
- **Scale (recommended ranges; pick from existing `--ds-*` if present)**:
    - H1 32–40 / line-height 1.1 / weight 600
    - H2 22–24 / 1.2 / 600
    - Card title 15–16 / 1.3 / 600
    - Body 14–15 / 1.55 / 400
    - Small 12–13 / 1.5 / 400
    - Label 11 / 1.2 / 500 / uppercase / `letter-spacing: 0.06em`
    - Metadata 12 / 1.4 / 400 / `--tm2`
    - KPI numbers 36–48 / 1 / 600 / `font-variant-numeric: tabular-nums`
- **Letter-spacing**: only on labels (caps).
- **Tabular nums**: KPI row, dates, counts.

### Spacing

- Page padding (desktop): 24–32px.
- Section gap: 32px.
- Card padding: 20–24px.
- Compact card (Documents grid, KPI tiles): 16px.
- Grid gap: 16px.
- Right rail width: 320–360px; rail padding: 20px.
- Vertical rhythm: 8/12/16/24/32 (use existing DASTI scale `--s1..s8` `[verify]`).

### Radius

- `--radius-1` (8): chips, segmented controls, status pills small.
- `--radius-2` (12): buttons, inputs, segmented tabs.
- `--radius-3` (16): cards, modals, drawers, command palette.
- `--radius-4` (20): hero/raised cards (Next Best Action) — optional.
- `--radius-pill` (999): status pills, brand pills.

### Borders & shadows

- **Light card**: `1px solid var(--border-soft)` + `--sha` or no shadow.
- **Light raised**: `--shb` + 1px `--border-soft`.
- **Dark card**: `1px solid var(--border-soft)` (which is `rgba(218,217,211,0.08)` in dark) + no shadow.
- **Dark raised**: same hairline + inner highlight `inset 0 1px 0 rgba(255,255,255,0.04)`.
- **Paper shadow** (proposal preview, light): `--document-paper-shadow`.
- **Forbidden**: black drop shadows in dark mode, gradient borders, double-stroke borders, glow effects.

### Focus states

- Global `:focus-visible` ring: `outline: 2px solid var(--fr); outline-offset: 2px; border-radius: inherit;`
- Never `outline: none` without replacement.
- Active state must include a non-color affordance (background, weight, stripe).

### Pills/chips

- **Pills allowed only for status** (Probably skip, Strong, Saved, Active, Drafting, Sent, Ready, Needs review).
- Replace metadata pills (company, location, source) with a text row: `Deloitte Legal · Ghent, ME · From LinkedIn ↗`.
- **Status color map**:
    - Saved/Active/Done → `--ok*`
    - Drafting/Needs review/Probably skip → `--wa*`
    - Failed/Error → `--er*`
    - Brand chips (`Will / International / Legal` taxonomy) → `--ap`/`--as` neutral, not full brand fill.
- **Dark chip rules**: fill `color-mix(in oklch, var(--accent) 14%, transparent)`, ink `color-mix(... 70%, var(--ti))` — not full saturation.

## 4. Token proposal

Most tokens already exist. Net-new are marked **(NEW)**. Values shown match what the repo already declares; ranges given where the repo doesn't define them.

|Token|Light|Dark|Usage|Components|Notes|
|---|---|---|---|---|---|
|`--bg`|`#FAF9F5`|`#0D0D0D`|Page canvas|App shell|Existing|
|`--sf1`|`#F8F7F3`|`#0E0E0E`|Sidebar chrome|Sidebar|Existing|
|`--sf2`|`#F0EEE6`|`#1A1918`|Default card|Cards, panels|Existing|
|`--sf3`|`#F5F4EF`|`#161616`|Hover/input fill|Inputs|Existing|
|`--sfr`|`#FFFFFF`|`#222120`|Raised|Next-Best-Action, toolbars, modals|Existing — extend usage|
|`--ti`|`#0F0C08`|`#DAD9D3`|Primary fg|Headings|Existing|
|`--tm2`|`rgba(15,12,8,.64)`|`#95948D`|Secondary fg|Body|Existing|
|`--tg3`|`#7E7D79`|`#6E6D69`|Tertiary/labels|Captions|Existing|
|`--border-soft`|`rgba(15,12,8,.08)`|`rgba(218,217,211,.08)`|Default border|Cards, dividers|Existing|
|`--border-field`|`rgba(15,12,8,.06)`|`rgba(218,217,211,.06)`|Inputs|Controls|Existing|
|`--border-strong`|`rgba(15,12,8,.14)`|`#504F4C`|Selected/dividers|Active borders|Existing|
|`--ac`|`#A84E2E`|`#A15A42`|Accent ink|Brand text, focused borders|Existing|
|`--am`|`#D97757`|`#D47554`|CTA fill|Primary buttons|Existing|
|`--am-soft`|`#EBBCAF`|`rgba(212,117,84,.20)`|Active pill|Pills|Existing|
|`--ok/--okb/--okt`|as repo|as repo|Success|Saved, Active, Strong|Existing|
|`--wa/--wab/--wat`|as repo|as repo|Warning|Drafting, Probably skip, Needs review|Existing — extend usage|
|`--er/--erb/--ert`|as repo|as repo|Danger|Errors only|Existing|
|`--fr`|`#D97757`|`#D47554`|Focus ring|All interactive|Existing|
|`--radius-1`|8|8|Chips/inputs small|—|Existing|
|`--radius-2`|12|12|Buttons/inputs|—|Existing|
|`--radius-3`|16|16|Cards/modals|—|Existing|
|`--radius-pill`|999|999|Pills|—|Existing|
|`--sha/--shb/--shc`|as repo|none in dark|Card shadows|Light cards only|Existing|
|`--shadow-card-dark` **(NEW)**|—|`inset 0 1px 0 rgba(255,255,255,0.04)`|Dark inner highlight|Cards|Add to `.dark` block|
|`--document-paper-shadow`|repo value|repo value|Letter paper|Proposal preview|Existing|
|`--card-pad-x` **(NEW)**|24px|24px|Card horizontal pad|All cards|Add token|
|`--card-pad-y` **(NEW)**|20px|20px|Card vertical pad|All cards|Add token|
|`--card-pad-compact` **(NEW)**|16px|16px|Documents grid cards|Compact cards|Add token|
|`--grid-gap` **(NEW)**|16px|16px|Card grids|Documents/Templates|Add token|
|`--rail-width` **(NEW)**|320px|320px|Right rail|Job/CV/Proposal|Add token|
|`--font-app` **(NEW alias)**|existing app sans|same|App body|App chrome|Alias to current value `[verify name]`|
|`--font-document` **(NEW alias)**|existing serif|same|Letters/CV|Document scope|Alias|
|`--type-h1` **(NEW)**|clamp(28px,3vw,40px)/1.1/600|same|Hero headings|Page H1|Pick from existing `--ds-*` if present|
|`--type-h2` **(NEW)**|22px/1.2/600|same|Section H2|—|—|
|`--type-body` **(NEW)**|14–15px/1.55/400|same|Body|—|—|
|`--type-small` **(NEW)**|12–13px/1.5/400|same|Metadata|—|—|
|`--type-label` **(NEW)**|11px/1.2/500/0.06em uppercase|same|Section labels|—|—|
|`--kpi-numerals` **(NEW)**|36–48px/1/600 tabular|same|Dashboard KPIs|KPI tiles|Set `font-variant-numeric: tabular-nums`|

Repo verification needed before merging new tokens: confirm whether `--ds-h1/-h2/-body` (or similar) already exist in `foundation.css`/`ds-v2.css` and **alias** rather than duplicate.

## 5. Component-by-component implementation plan

### 5.1 Global theme/tokens

**Current issue:** Tokens exist but are unevenly applied; no compact spacing tokens; no global `:focus-visible`. **Target:** Single source of truth in `foundation.css` with all tokens from §4 declared once and inherited by `.dark`. **Steps:**

1. Audit `foundation.css` for duplicate/legacy tokens. Add `--card-pad-x/y`, `--card-pad-compact`, `--grid-gap`, `--rail-width`, `--shadow-card-dark`, `--type-*` if missing.
2. Verify `--font-app` and `--font-document` exist; add aliases if not.
3. Add a global `*:focus-visible` rule in `base.css` using `--fr`. **Files:** `my-app/src/styles/foundation.css`, `my-app/src/styles/base.css`, `my-app/src/styles/themes.css`. **CSS:** new tokens listed above. **JSX:** none. **Acceptance:**

- `:root` and `.dark` both declare every new token.
- `:focus-visible` ring appears on every focused control (sample 5 controls with keyboard).
- `git grep` shows no hardcoded `#FFFFFF`, `#0D0D0D`, `8px`/`16px` radius literals introduced. **Regression risks:** existing components that hardcode colors will look unchanged (acceptable); any component overriding `outline: none` without replacement will break focus — log them.

### 5.2 App shell

**Current issue:** Light/dark cliff between onboarding and authenticated app. **Target:** Same paddings, same radii, same gap rhythm in both modes. **Steps:**

1. Search `App.tsx` and the layout wrapper for mode-specific paddings/widths.
2. Replace any `dark:p-*` / mode-conditional class with token-driven value.
3. Standardize page padding to a single `--page-pad-x/y` derived constant. **Files:** `my-app/src/App.tsx`, layout component `[verify: components/header/* or components/AppShell*]`. **Acceptance:** screenshot diff between light & dark dashboard shows only color changes, no geometry change. **Regression risks:** sidebar width changes if hardcoded.

### 5.3 Sidebar navigation

**Current issue:** Active state is color-only on icon. **Target:** Active item shows a `--sf2` rounded-square background **and** a 2px `--ac` left stripe; tooltip on hover shows label. **Steps:**

1. Locate sidebar component `[verify: components/header/Sidebar.tsx or similar —` grep -r "nav" components/header`]`.
2. Add active class with `background: var(--sidebar-active-bg)` (already exists) + `box-shadow: inset 2px 0 0 var(--ac)`.
3. Add `aria-label` and a `Tooltip` (existing UI primitive `[verify components/ui/Tooltip*]`). **CSS:** `--sidebar-active-bg`, `--sidebar-active-stripe` already declared in `foundation.css` — extend usage. **Acceptance:** active item visible without color (test by toggling grayscale dev tool). **Regression:** keyboard tab order must remain.

### 5.4 Dashboard / Next Best Action

**Current issue:** Card flat with the rest of the page in dark mode; over-uses brand orange. **Target:** Raised card on `--sfr` with hairline border + `--shb` (light) / inner highlight (dark); single CTA "Review match" in `--am` fill, secondary "Open draft" in outlined neutral; "2 watch-outs" pill remapped to `--wa*`; "CV ready" → `--ok*`. **Steps:**

1. Open `pages/DashboardPage.tsx`. Locate Next-Best-Action block.
2. Apply `class="card card--raised"` with rules `background: var(--sfr); border: 1px solid var(--border-soft); box-shadow: var(--shb);` (dark: drop shadow, add inner highlight).
3. Re-class status pills using existing tone tokens (`--wa-bg/--wa-ink` or `--okb/--okt`).
4. Demote secondary CTA to outlined. **Files:** `pages/DashboardPage.tsx`, `styles/product.css` (or component-scoped CSS). **Acceptance:** in dark mode the NBA card is visibly raised vs neighbours; only one filled brand button visible; pills no longer brand-orange.

### 5.5 Dashboard KPI row

**Current issue:** Big numbers not tabular-aligned, "(30d)" stacked under label, columns variable width. **Target:** Three equal columns; numbers in tabular nums; `(30d)` inline as small caps suffix. **Steps:**

1. Apply `font-variant-numeric: tabular-nums; font-feature-settings: 'tnum'` to KPI numerals.
2. `display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--grid-gap);`
3. Move "(30d)" into the label as a small span. **Files:** `pages/DashboardPage.tsx`, `styles/product.css`.

### 5.6 Dashboard quick actions / recent activity

**Current issue:** Two equal-elevation cards with no scanning rhythm. **Target:** Quick-actions card slightly compressed; recent-activity rows have date right-aligned with tabular nums and a dot indicator. **Steps:** restyle list items, no logic changes.

### 5.7 Job detail page header

**Current issue:** 5 stacked pills below H1 (company, location, source, status). **Target:** Text meta row + single right-aligned status pill.

- `H1` → company · location · source ↗ → spacer → status pill. **Steps:**

1. Open Jobs detail component `[verify: components/jobs/JobDetail*.tsx or pages/JobsPage.tsx]`.
2. Replace pills with a flex row of small text (`--type-small`, `--tm2`); keep one pill for status.
3. Source link (LinkedIn) becomes inline `<a>` with external-link icon. **Acceptance:** only one pill visible in the header area.

### 5.8 Job detail right verdict rail

**Current issue:** Skills/Seniority/Location/Gap labels and values share weight, ragged wrap. **Target:** 2-column definition list with fixed label column. **CSS:**

```
.verdict-grid { display: grid; grid-template-columns: 88px 1fr; row-gap: 12px; column-gap: 16px; }
.verdict-grid dt { font: var(--type-label); color: var(--tg3); text-transform: uppercase; letter-spacing: .06em; }
.verdict-grid dd { font: var(--type-body); color: var(--ti); }
```

**Files:** `styles/product-jobs.css`, jobs detail JSX. **Acceptance:** every row aligns at the same x; labels in caps; no orphaned wraps.

### 5.9 Proposal editor preview frame

**Current issue:** Paper edge blends into app bg in light mode; rail surface identical. **Target:** App bg drops to warm `#F5F1EC` (or `--sf2`) in editor; paper stays `#FFFFFF` with `--border-soft` + `--document-paper-shadow`; rail uses `--bg`/`--sf1` with hairline left divider. **Steps:**

1. Inside `pages/ProposalForge.tsx` (or its container), set the editor area background to `--sf2`.
2. Apply paper shadow class `[verify: .document-paper or .proposal-paper in product-proposal.css]`.
3. Right rail: `border-left: 1px solid var(--border-soft); background: transparent;`. **Acceptance:** clear paper-on-desk impression.

### 5.10 Documents grid cards

**Current issue:** ~240px cards with empty zones; "Actions" full button; type chip equals title weight. **Target:**

- Card height ~140–160px.
- Top row: type label (caps `--type-label`) + `…` icon button (24px hit area).
- Title 15px/600.
- 2-line excerpt clamped, `--tm2`.
- Footer row: updated date (tabular) + status pill. **Steps:**

1. Open `pages/DocumentsPage.tsx`. Find document card subcomponent.
2. Replace `<button>Actions</button>` with `IconButton` (`…`) opening menu.
3. Apply `--card-pad-compact` and clamp via `-webkit-line-clamp: 2`.
4. Re-class status pills with tone tokens. **Acceptance:** 5 columns visible at desktop with no card whitespace > 30%.

### 5.11 Template/style preview cards

**Current issue:** Empty rectangles labeled "Style 1/2/3"; selection ring competes with brand CTA. **Target:** Render a real miniature letter inside each preview using the actual font pair; selected state = 2px `--ac` border + corner check. **Steps:**

1. Locate preview component `[verify: components/onboarding/StylePicker* and pages/TemplatesPage.tsx]`.
2. Build a small preview that reuses the same letter primitive at scale ~0.4 with sample text.
3. Replace full-saturation ring with thin border + check icon. **Acceptance:** font choice readable from the picker.

### 5.12 Onboarding progress indicator

**Current issue:** Six quiet bars; "Step 3 of 6" footer disconnected. **Target:** Labeled segmented progress; completed segments tinted; current segment higher contrast; count adjacent. **Steps:** edit `components/onboarding/StepIndicator*` `[verify]`. **Acceptance:** keyboard nav between steps possible; progress visible at a glance.

### 5.13 CV editor tabs

**Current issue:** `Sections / Ask / Style` active state same contrast as inactive in dark mode. **Target:** Active tab has heavier weight + 2px bottom border `--ac`; inactive `--tm2`. **Steps:** locate tabs in `pages/CvForge.tsx` or `components/cv-editor/*`. Apply tab classes.

### 5.14 CV editor drawers

**Current issue:** Drawer fills full pane for 3 fields; mostly empty. **Target:** Auto-size drawer to content; min-width 360px, max-width 480px; sticky footer with Save/Cancel. **Steps:** edit drawer container `[verify components/cv-editor/SectionDrawer* or similar]`.

### 5.15 Settings document style panel

**Current issue:** Font specimens huge; color picker tiny and unlabeled. **Target:** Specimens ~56px with mini paired preview; swatches 32px with names (Brick / Ink / Cobalt / Forest / Plum / Ochre) and check on selected. **Files:** `pages/SettingsPage.tsx`, `styles/product-settings.css`.

### 5.16 Command palette

**Current issue:** Default highlight on "Replay onboarding"; mixed kbd format; "Replay onboarding" surfaced by default. **Target:** No default highlight (or focus only the input); shortcuts wrapped in `<kbd>` with consistent format (`⌘⇧T`, `G → J`); destructive/utility actions only after search. **Files:** `components/CommandPalette.tsx`. **Acceptance:** Enter on a fresh open does nothing destructive; `<kbd>` chips visually consistent.

### 5.17 Global focus states

**Current issue:** Likely missing/inconsistent. **Target:** Single global `:focus-visible` rule in `base.css`; component-specific overrides only when shape requires it. **CSS:**

```
:where(button, a, [role=button], input, select, textarea, [tabindex]):focus-visible {
  outline: 2px solid var(--fr);
  outline-offset: 2px;
}
```

**Acceptance:** Tab through Dashboard, Jobs, CV editor — every focused element shows a ring.

### 5.18 Light/dark parity QA

**Steps:** Side-by-side screenshots of every route in both modes; diff geometry only. Treat color differences as acceptable, geometry differences as bugs.

## 6. Issue-to-fix mapping

|#|Issue|Severity|Component|Root cause|Fix type|Phase|Acceptance|
|---|---|---|---|---|---|---|---|
|1|Accent overuse|High|Dashboard, Jobs, Documents, Sidebar|Same `--ac/--am` for CTA + status + bullets + active|Token semantics + CSS sweep|2,4,5,6|Only one filled brand button per view; status pills no longer orange|
|2|No dark elevation system|High|Dashboard, Documents|`--sfr` underused in dark|CSS|2,4|NBA card visibly raised in dark|
|3|Type scale lacks contrast|High|Dashboard, Jobs|H1 too close to body|Typography|3|H1 ≥ 2× body weight*size impression|
|4|Verdict rail weak|High|Jobs detail|No grid structure|Component|5|2-col definition list aligned|
|5|Inconsistent radius|Medium|Global|Per-component literals|Token sweep|2|Only `--radius-1/2/3/pill` used|
|6|Focus states missing|High (a11y)|Global|`outline: none` overrides|CSS|2|Visible ring on every focusable|
|7|KPI tabular nums missing|Medium|Dashboard|No `tabular-nums`|CSS|4|Numbers vertically aligned across columns|
|8|Editor frame contrast|Medium|Proposal|App bg matches paper|CSS|8|Paper visible against bg|
|9|Pill inflation|Medium|Jobs/Proposal headers|Pill used for metadata|Component|5,8|One status pill per header|
|10|Sidebar active state|Medium (a11y)|Sidebar|Color-only|Component|9|Visible at grayscale|
|11|Light/dark cliff|High|App shell|Mode-specific paddings|CSS|2,10|Geometry parity|
|12|Documents cards empty|High|Documents|Over-padded, empty|Component|6|Compact 140–160px cards|
|13|Onboarding progress quiet|Medium|Onboarding|Low contrast bars|Component|7|Labeled progress|
|14|Template previews fake|Medium|Templates/Onboarding|Empty rects|Component|7|Real font preview rendered|
|15|CV tabs unclear|Medium|CV editor|Identical pill states|CSS|8|Active tab visibly stronger|
|16|Doc style picker imbalance|Medium|Settings|Specimens huge, colors tiny|Layout|7|Balanced specimen/swatch sizes|
|17|CV drawers oversized|Low/Med|CV editor|No max-width|Layout|8|Drawer sized to content|
|18|Brand drop landing→app|Medium|App shell|Logo + signature moves not ported|Component|7|Same logo lockup, dot punctuation token|
|19|Dark pill saturation|Low|Dashboard, Proposal|Solid accent fill|CSS|4,8|Subtle tint, not solid|
|20|Command palette polish|Low|CommandPalette|Default highlight + mixed kbd|Component|9|No destructive default; consistent kbd|

## 7. Phased execution plan

### Phase 0 — Repo discovery & baseline

- **Goal:** capture baseline screenshots and confirm file paths.
- **Inspect:** `foundation.css, ds-v2.css, themes.css, base.css, primitives.css, product*.css, App.tsx, pages/*, components/header, components/onboarding, components/cv-editor, components/CommandPalette.tsx`.
- **Tasks:** screenshot every route in light and dark at 1440×900; commit baselines under `docs/UI/baselines/<date>/`.
- **Forbidden:** any code change.
- **Acceptance:** baseline folder exists.
- **Build:** `pnpm -C my-app dev` running.

### Phase 1 — Token normalization

- **Goal:** declare missing tokens, alias type tokens, no visual change yet.
- **Files:** `foundation.css`, `base.css`, `themes.css`.
- **Tasks:** add `--card-pad-x/y/compact, --grid-gap, --rail-width, --shadow-card-dark, --type-h1/h2/body/small/label, --kpi-numerals`; add `--font-app/--font-document` aliases.
- **Forbidden:** changing existing token values; removing tokens.
- **Acceptance:** `pnpm -C my-app build` green; no UI diff.

### Phase 2 — Global surfaces, radius, borders, shadows, focus

- **Goal:** apply `--sfr` to raised surfaces in dark; sweep radii to scale; global focus.
- **Tasks:** add `:focus-visible` rule; add `.card`/`.card--raised` utilities (or apply to existing); replace any hardcoded radius literals in `product*.css`.
- **Forbidden:** component refactors; layout changes.
- **Acceptance:** focus rings on every focusable; dark NBA card visibly elevated.

### Phase 3 — Typography

- **Goal:** scope serif to documents; tighten H1; tabular nums on KPI.
- **Tasks:** restrict `--font-document` to `.document-paper`/`.letter`/`.resume-page`; set app body to `--font-app`; apply `--type-h1/h2`.
- **Forbidden:** changing letter rendering, changing CV/proposal export typography.
- **Acceptance:** dashboard H1 visibly larger; CV/proposal preview unchanged.

### Phase 4 — Dashboard dark-mode polish

- **Goal:** elevation, status remap, KPI alignment.
- **Tasks:** §5.4–5.6.
- **Acceptance:** only one filled brand CTA on dashboard; KPIs aligned.

### Phase 5 — Job detail header & verdict rail

- **Goal:** §5.7–5.8.
- **Acceptance:** definition-list rail; single status pill in header.

### Phase 6 — Documents grid density

- **Goal:** §5.10.
- **Acceptance:** 5 cards per row at desktop, no skeleton feel.

### Phase 7 — Templates, onboarding, settings

- **Goal:** §5.11, 5.12, 5.15, 5.18.
- **Acceptance:** onboarding step labels visible; template previews render real letter; settings doc-style picker balanced.

### Phase 8 — CV/proposal editor consistency

- **Goal:** §5.9, 5.13, 5.14, 5.16 (chip saturation in proposal).
- **Acceptance:** editor frames consistent; tabs and drawers correctly sized.

### Phase 9 — Command palette & sidebar active

- **Goal:** §5.3, 5.16.
- **Acceptance:** command palette has no destructive default; sidebar active visible at grayscale.

### Phase 10 — Final QA & regression pass

- **Goal:** screenshot diff vs Phase 0 baselines; record findings.
- **Tasks:** run `pnpm -C my-app build`, `pnpm -C my-app test`, Playwright smoke if present (`playwright.config.ts` exists).
- **Acceptance:** all routes load, no console errors, geometry parity light↔dark.

For every phase: capture before/after screenshots of the affected routes only.

## 8. Codex/GPT implementation prompts

> The same preamble applies to every phase prompt:
> 
> "You are working on the twoweeks repo at `my-app/`. Inspect the repo before editing. Do NOT invent files, classes, or tokens. Do NOT redesign. Do NOT refactor unrelated code. Do NOT change routing, data loading, editor logic, CV/proposal renderers, export, or auth. Use only the existing token system in `my-app/src/styles/foundation.css`, `themes.css`, `base.css`, plus tokens added in Phase 1. After implementing, report tests honestly, give a concise diff summary, and list any items you skipped or are uncertain about."

### Phase 0 prompt

- **Context:** baseline capture before UI fixes.
- **Goal:** screenshot every route in light & dark at 1440×900 and save under `docs/UI/baselines/<YYYY-MM-DD>/`.
- **Scope:** read-only.
- **Do not change:** anything.
- **Required work:** start dev server, navigate to `/dashboard, /jobs, /jobs/:id, /proposal, /documents, /templates, /settings?tab=docstyle, /cv?id=...`, toggle dark via command palette ("Toggle light or dark"), capture.
- **Acceptance:** folder contains `<route>__light.png` and `<route>__dark.png` per route.
- **Tests/build:** `pnpm -C my-app dev`.
- **Output:** list of files captured + any routes that errored.

### Phase 1 prompt

- **Context:** add missing tokens.
- **Goal:** declare all `Phase 1` tokens from §4 in `foundation.css` (`:root` and `.dark`), `base.css` for global focus, no visual change.
- **Scope:** `my-app/src/styles/foundation.css`, `base.css`, `themes.css`.
- **Do not change:** values of existing tokens; component CSS.
- **Required work:** verify whether `--ds-h1/-h2/-body` exist; if so, alias `--type-h1/h2/body` to them rather than redefining. Add `--card-pad-x/y/compact, --grid-gap, --rail-width, --shadow-card-dark, --kpi-numerals, --font-app, --font-document`. Add a `:focus-visible` rule in `base.css` keyed off `--fr`.
- **Acceptance:** `pnpm -C my-app build` green; visual diff vs Phase 0 = none.
- **Tests:** `pnpm -C my-app build && pnpm -C my-app test`.
- **Output:** diff summary; list of pre-existing tokens you aliased to vs new tokens added.

### Phase 2 prompt

- **Context:** apply tokens to global surfaces, radii, borders, shadows; enforce focus.
- **Goal:** dark cards in `pages/DashboardPage.tsx` and `pages/DocumentsPage.tsx` use `--sfr` for raised tiles; radii unified to `--radius-1/2/3/pill`; global `:focus-visible` ring visible.
- **Scope:** `styles/product*.css`, page CSS scopes for Dashboard/Documents only.
- **Do not change:** layout, copy, component structure, JSX (CSS-only).
- **Required work:** sweep `border-radius: <px>` literals → tokens; replace dark card flat `--sf2` on the Next-Best-Action card with `--sfr` + hairline; add `--shadow-card-dark` inset highlight in `.dark`.
- **Acceptance:** keyboard tab on dashboard shows ring on every interactive; NBA card raised in dark mode; no radius literal remains in touched files.
- **Tests:** build + visual diff (manual).
- **Output:** list of files edited, count of radius literals replaced.

### Phase 3 prompt

- **Context:** typography hierarchy.
- **Goal:** scope serif to documents; apply `--type-h1/h2/body` to dashboard and jobs; add tabular nums to KPI numerals.
- **Scope:** `styles/product.css, product-jobs.css`, `pages/DashboardPage.tsx`/`JobsPage.tsx` only for class swaps.
- **Do not change:** `.document-paper`, `.resume-page`, `.letter`, proposal preview CSS.
- **Required work:** ensure app body uses `--font-app`; serif fonts only inside `[class*="document-paper"], .resume-page, .letter`.
- **Acceptance:** dashboard H1 visibly larger; KPI numerals vertically aligned column-to-column; CV/proposal preview unchanged in screenshots.
- **Output:** screenshots of `/dashboard` and `/jobs/:id` before/after.

### Phase 4 prompt

- **Context:** dashboard dark-mode polish.
- **Goal:** §5.4–5.6 implemented.
- **Scope:** `pages/DashboardPage.tsx` + scoped CSS.
- **Required work:** primary CTA uses `--am`; secondary outlined; pills remapped to `--wa*`/`--ok*`; KPI grid `repeat(3, 1fr)` with tabular nums.
- **Acceptance:** only one filled brand button on the page; "2 watch-outs" pill uses warning tone; "CV ready" uses success tone.
- **Output:** before/after screenshots.

### Phase 5 prompt

- **Context:** Job detail header + Verdict rail.
- **Goal:** §5.7–5.8.
- **Scope:** Jobs detail component + `product-jobs.css`.
- **Required work:** replace metadata pill stack with text row + single status pill; build `.verdict-grid` 2-col DL.
- **Acceptance:** one pill in header; rail labels in caps `--tg3`, values in `--ti`, all aligned.

### Phase 6 prompt

- **Context:** Documents grid density.
- **Goal:** §5.10.
- **Scope:** `pages/DocumentsPage.tsx` + scoped CSS.
- **Required work:** card height 140–160px; `…` icon button replacing "Actions"; `-webkit-line-clamp: 2` excerpt; status pill in footer; `--card-pad-compact`.
- **Acceptance:** 5 cards/row at 1440px; no card has > 30% empty area.

### Phase 7 prompt

- **Context:** Templates, onboarding, settings polish.
- **Goal:** §5.11, 5.12, 5.15, 5.18.
- **Scope:** `pages/TemplatesPage.tsx, SettingsPage.tsx, components/onboarding/*`.
- **Required work:** real letter mini-preview in template/style cards; labeled segmented progress; balanced specimen/swatch in settings; reuse landing logo lockup if available.
- **Acceptance:** template font choice readable from preview; onboarding step labels visible.

### Phase 8 prompt

- **Context:** Editor consistency.
- **Goal:** §5.9, 5.13, 5.14, dark-mode chip saturation.
- **Scope:** `pages/ProposalForge.tsx, CvForge.tsx, components/cv-editor/*, styles/product-proposal.css, product-cv.css`.
- **Required work:** editor app bg `--sf2` while paper stays raised; tabs active state with bottom border; drawer max-width 480px with sticky footer; dark pills use `color-mix` tints.
- **Acceptance:** paper visible against bg; tabs unambiguous; drawers compact.

### Phase 9 prompt

- **Context:** Command palette + Sidebar.
- **Goal:** §5.3, 5.16.
- **Scope:** `components/CommandPalette.tsx`, sidebar component.
- **Required work:** no default highlight on "Replay onboarding"; consistent `<kbd>` chips; sidebar active = `--sf2` block + 2px `--ac` left stripe + tooltip.
- **Acceptance:** Enter on fresh palette open does nothing destructive; sidebar active visible in grayscale.

### Phase 10 prompt

- **Context:** Final QA.
- **Goal:** regression sweep.
- **Required work:** run `pnpm -C my-app build`, `pnpm -C my-app test`, Playwright smoke; capture screenshots of every route light/dark; diff against Phase 0 baselines.
- **Output:** report listing any geometry deltas (must be intentional only) and console errors.

## 9. QA checklist

|Surface|Pass condition|Fail condition|Screenshot|
|---|---|---|---|
|Dashboard light|Single brand CTA, KPI tabular, raised NBA card|Multiple filled brand buttons, ragged KPIs|Yes|
|Dashboard dark|NBA card visibly elevated; pills not full-orange|Flat slab; brand-orange status pills|Yes|
|Documents light|5 dense cards/row, status footer|Skeleton-feel cards|Yes|
|Documents dark|Same geometry as light, only colors differ|Different paddings|Yes|
|Job detail light|Definition-list rail; one header pill|Pill stack; ragged rail|Yes|
|Job detail dark|Same|Same|Yes|
|Proposal editor light|Paper raised on warm bg|Paper merges into bg|Yes|
|Proposal editor dark|Paper readable, rail divider visible|Paper too dark or rail invisible|Yes|
|CV editor light|Tabs unambiguous, drawer auto-sized|Active tab unclear|Yes|
|CV editor dark|Same|Same|Yes|
|Onboarding light|Labeled progress + active emphasized|Quiet bars only|Yes|
|Onboarding dark|Same|Same|Yes|
|Templates light|Real font preview readable|"Style 1" empty rects|Yes|
|Templates dark|Same|Same|Yes|
|Settings docstyle|Balanced specimen/swatch|Huge fonts, tiny dots|Yes|
|Command palette|No default destructive highlight; consistent kbd|"Replay onboarding" pre-highlighted|Yes|
|Sidebar active|Visible in grayscale|Color-only|Yes|
|Keyboard focus|Ring visible on every focusable|Missing on any|Yes (animated)|
|Mobile (≤768)|App shell readable, no horizontal scroll|Horizontal scroll|Optional|

## 10. Non-regression rules

Must not change:

- React Router routes; URL shapes (`/jobs/:id`, `/cv?id=...`, `/proposal`, etc.).
- Data loading: Convex/queries, fetch hooks.
- Editor behavior: Remirror config, undo/redo, AI toolbar logic.
- CV rendering output (`ResumePrintPage.tsx`, `.resume-page` print CSS).
- Proposal rendering output (`ProposalPrintPage.tsx`, `.document-paper` print/export CSS).
- Export pipeline (PDF, DOCX) — touch nothing in `services/`, `adapters/`, or print pages.
- Auth/session (Clerk).
- Brand identity: Terre/clay palette; current logo lockup; existing fonts.
- Existing token values (only add or alias).
- No new runtime dependency unless absolutely required (none expected).
- No global Tailwind config changes.

## 11. Final execution recommendation

- **Run first:** Phase 0 (baseline) immediately, then Phase 1 (tokens) as it unblocks everything and has zero visual diff.
- **Combinable:** Phase 1 + Phase 2 (tokens + global surfaces/focus) can land in one PR safely. Phase 5 + Phase 6 can be combined (Jobs + Documents) since they touch different files. Phase 9's two scopes (palette + sidebar) can ship together.
- **Must not combine:** Phase 3 (typography) must ship alone — broad surface area for regression. Phase 8 (editor) must ship alone — highest blast radius for CV/proposal output regressions. Phase 4 must not be merged with Phase 5 (both touch dashboard/jobs surface tokens; cleaner to verify independently).
- **Highest visual ROI:** Phase 4 (Dashboard dark-mode polish) — it's the surface users see first after login.
- **Highest regression risk:** Phase 8 (editor) — proposal/CV print and export pipelines are downstream. Treat with extra screenshot diff and a full export smoke test.
- **Screenshots to give Codex/GPT before any phase:** Phase 0 baselines for the routes that phase touches, plus the corresponding rows of §9 QA. For Phase 4, hand over Dashboard light + dark. For Phase 5, Job detail. Etc. Do not give a phase screenshots from unrelated routes — it invites scope creep.