# DS v2 + AI Primitives — Implementation Plan for Codex

> **Audience:** Codex (implementer).
> **Rule:** Implement exactly as specified. Do NOT improvise tokens, sizes, easings, copy, or component APIs. If a value is not in this doc, ask before guessing.
> **Source of truth tokens:** `my-app/src/styles/foundation.css`. Never introduce new tokens — use existing ones.
> **Voice:** sentence case, period-terminated, no emoji, no exclamation marks (except the literal `!` icon glyph in danger toast).

---

## 0. Scope

This plan ships the v2 primitives layer and the AI interaction primitives required by the upcoming "Premium AI" refonte (preview → accept/discard, no auto-apply on Rewrite/Strengthen/Ask).

Deliverables:
1. **A.** Token contract + Stylelint guardrails.
2. **B.** Primitives v2: `Button`, `IconButton`, `Input`, `Textarea`, `Card`, `Pill`, `StatusBadge`, `Toast`, `Dialog`, `Skeleton`.
3. **C.** AI primitives: `AiStageList`, `AiSuggestionCard` (3 modes), `FloatingAiToolbar` (refactor), `AskAiInput`, `UndoToast`, `DiffBlock`.
4. **D.** Storybook (Ladle) entries for every primitive.
5. **E.** Migration of existing usages within Library/Forge files where mechanical (not full page refonte — that's a later PR).

NOT in scope: ProposalForge / JobsPage refonte, sidebar redesign, command palette, route splitting.

---

## 1. Token contract (READ FIRST)

**Always use `var(--token)`. Never literal hex/rgb/px-from-air.** Stylelint will block them (see §11).

### 1.1 Color tokens (semantic, light + dark via `.dark`)

| Use | Token | Light | Dark |
|---|---|---|---|
| Canvas | `--bg` | `#FAF9F5` | `#0D0D0D` |
| Sidebar / panel | `--sf1` | `#F8F7F3` | `#0E0E0E` |
| Muted surface / stage | `--sf2` | `#F0EEE6` | `#1A1918` |
| Raised (cards, popovers, dialogs, toolbars) | `--sfr` | `#FFFFFF` | `#222120` |
| Document paper | `--paper` | `#FAF9F5` | `#E8E5DB` |
| Primary text | `--ti` | `#0F0C08` | `#DAD9D3` |
| Muted text | `--tm2` | `rgba(15,12,8,0.64)` | `#95948D` |
| Subtle text / disabled | `--tg2` | `rgba(15,12,8,0.60)` | `#6E6D69` |
| Border soft (cards) | `--border-soft` | `rgba(15,12,8,0.08)` | `rgba(218,217,211,0.08)` |
| Border field | `--border-field` | `rgba(15,12,8,0.06)` | `rgba(218,217,211,0.06)` |
| Border strong (controls, dividers) | `--border-strong` | `rgba(15,12,8,0.14)` | `#504F4C` |
| Accent (primary action) | `--ac` | `#A84E2E` | `#A15A42` |
| Accent hover / overline / CTA | `--am` | `#D97757` | `#D47554` |
| Accent wash | `--ap` | `rgba(168,78,46,0.10)` | `rgba(212,117,84,0.14)` |
| Accent soft | `--as` | `rgba(168,78,46,0.16)` | `rgba(212,117,84,0.20)` |
| Focus ring | `--fr` | `#D97757` | `#D47554` |
| Ink on filled accent | `--color-on-accent` | `#FAF9F5` | `#0E0E0E` |
| Success | `--ok` / `--okb` (soft bg) / `--okt` (ink) |  |  |
| Danger | `--er` / `--erb` / `--ert` |  |  |
| Warning | `--wa` / `--wab` / `--wat` |  |  |
| Shadow sm/md/lg | `--sha` / `--shb` / `--shc` |  |  |

### 1.2 Spacing — 4-based

`--s1=4` `--s2=8` `--s3=12` `--s4=16` `--s5=24` `--s6=32` `--s7=40` `--s8=64` `--s9=80`
Aliases: `--space-1..9`.

### 1.3 Radius

`--radius-1=8` (`--rx`, inline chips) · `--radius-2=12` (`--rs`, controls) · `--radius-3=16` (`--rm`, cards) · `--radius-4=20` (`--rl`, panels) · `--radius-pill=999` (`--rp`).

### 1.4 Control heights

`--hs=32` (sm) · `--hm=40` (md) · `--hb=44` (lg) · `--hdr=54` (header).

### 1.5 Type scale

Sizes: `--tx=12` `--ts=14` `--tb=16` `--tm=20` `--tl=26` `--tx2=32`.
Lines: `--lx=16` `--ls=20` `--lb=24` `--ll=30` `--lx2=40`.
Families: `--font-body-family`, `--font-serif-display`, `--font-mono-family`.
Weights: body 400, label/heading 600, **never 500**.
Tracking: `--tracking-display=-0.02em`, `--tracking-tight=-0.01em`, `--tracking-wide=0.14em` (overline UPPERCASE).

### 1.6 Motion

Durations: `--dur-1=80` `--dur-2=160` `--dur-3=240` `--dur-4=320` `--dur-5=480`.
Easings: `--ez` (= `--ease-standard`), `--ease-enter`, `--ease-exit`, `--ease-emphasis`.
Press scale: `--motion-press-scale=0.96`.

Use the **canonical motion-tokens** from `motion-tokens.css` for new animations:
- `--motion-duration-micro=80` `--motion-duration-fast=140` `--motion-duration-normal=200` `--motion-duration-medium=320` `--motion-duration-panel=420` `--motion-duration-settle=480` `--motion-duration-reveal=600` `--motion-duration-brand=2400`
- `--motion-ease-standard` `--motion-ease-enter` `--motion-ease-exit` `--motion-ease-emphasized` `--motion-ease-breathe`

> Codex: import `motion-tokens.css` in `src/styles/foundation.css` if not already imported. Verify with `grep motion-duration src/styles/foundation.css`.

### 1.7 Z-index

`--z-sticky=100` `--z-popover=400` `--z-modal=800` `--z-toast=900` `--z-tooltip=1000`.

### 1.8 Frost (overlays)

`backdrop-filter: blur(var(--frost-blur)) saturate(var(--frost-saturate))` with `background: var(--frost-surface)`.

---

## 2. File map

```
my-app/src/
├── styles/
│   ├── foundation.css            (existing — verify motion-tokens import)
│   ├── primitives.css            (PURGE legacy classes; keep only tokens-driven utilities)
│   └── ds-v2.css                 (NEW — primitives v2 layer; @layer components)
├── components/
│   ├── ui/                       (REFACTOR existing files in place)
│   │   ├── button.tsx
│   │   ├── icon-button.tsx       (NEW)
│   │   ├── input.tsx
│   │   ├── textarea.tsx          (NEW)
│   │   ├── card.tsx
│   │   ├── pill.tsx              (NEW)
│   │   ├── status-badge.tsx      (NEW)
│   │   ├── toast.tsx
│   │   ├── dialog.tsx
│   │   ├── skeleton.tsx
│   │   └── index.ts              (NEW — public re-exports)
│   ├── ai/                       (NEW directory)
│   │   ├── AiStageList.tsx
│   │   ├── AiSuggestionCard.tsx
│   │   ├── DiffBlock.tsx
│   │   ├── FloatingAiToolbar.tsx (MOVE from components/ — refactor + split)
│   │   ├── AskAiInput.tsx
│   │   ├── UndoToast.tsx
│   │   └── index.ts              (NEW)
│   └── FloatingAiToolbar.tsx     (DELETE after migrating imports)
└── lib/
    └── motion.ts                 (NEW — typed motion presets)
```

Stories (Ladle) — one per primitive:
```
my-app/.ladle/
└── stories/
    ├── button.stories.tsx
    ├── input.stories.tsx
    ├── card.stories.tsx
    ├── pill.stories.tsx
    ├── toast.stories.tsx
    ├── dialog.stories.tsx
    ├── ai-stage-list.stories.tsx
    ├── ai-suggestion-card.stories.tsx
    ├── floating-ai-toolbar.stories.tsx
    └── ask-ai-input.stories.tsx
```

> If Ladle isn't installed: `pnpm add -D @ladle/react`. Add script `"ladle": "ladle serve"` to `my-app/package.json`.

---

## 3. CSS layer — `ds-v2.css`

Codex: create `my-app/src/styles/ds-v2.css` with the exact rules below. Import it in `src/index.css` AFTER `foundation.css` and BEFORE `primitives.css`. Use `@layer components`.

```css
@layer components {

/* ---------- Button ---------- */
.ds-btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  border: 1px solid transparent; border-radius: var(--radius-2);
  font-family: inherit; font-weight: var(--font-label-weight); cursor: pointer;
  white-space: nowrap; line-height: 1; user-select: none;
  transition:
    background-color var(--dur-2) var(--ez),
    border-color    var(--dur-2) var(--ez),
    color           var(--dur-2) var(--ez),
    transform       var(--dur-2) var(--ez),
    box-shadow      var(--dur-2) var(--ez),
    opacity         var(--dur-2) var(--ez);
}
.ds-btn:hover:not(:disabled) { transform: translateY(-1px); }
.ds-btn:active:not(:disabled) { transform: scale(var(--motion-press-scale)); transition-duration: var(--dur-1); }
.ds-btn:focus-visible { outline: 2px solid var(--fr); outline-offset: 2px; }
.ds-btn:disabled { opacity: 0.42; cursor: not-allowed; transform: none !important; }

.ds-btn--sm { height: var(--hs); padding: 0 var(--s3); font-size: var(--tx); }
.ds-btn--md { height: var(--hm); padding: 0 var(--s4); font-size: var(--ts); }
.ds-btn--lg { height: var(--hb); padding: 0 var(--s5); font-size: var(--tb); }

.ds-btn--primary   { background: var(--ac); color: var(--color-on-accent); box-shadow: var(--sha); }
.ds-btn--primary:hover:not(:disabled)   { background: var(--am); box-shadow: var(--shb); }

.ds-btn--secondary { background: var(--sfr); color: var(--ti); border-color: var(--border-strong); box-shadow: var(--sha); }
.ds-btn--secondary:hover:not(:disabled) { background: var(--sf2); }

.ds-btn--ghost     { background: transparent; color: var(--tm2); }
.ds-btn--ghost:hover:not(:disabled) { background: var(--sf2); color: var(--ti); }

.ds-btn--accent    { background: var(--ap); color: var(--ti); }
.ds-btn--accent:hover:not(:disabled) { background: var(--as); }

.ds-btn--danger    { background: var(--erb); color: var(--ert); }
.ds-btn--danger:hover:not(:disabled) { background: var(--er); color: #fff; }

.ds-btn--success   { background: var(--okb); color: var(--okt); }
.ds-btn--success:hover:not(:disabled) { background: var(--ok); color: #fff; }

.ds-btn--pill { border-radius: var(--radius-pill); }

/* Loading: replace label by "<verb><period-pulse>" — handled in TSX, no spinner CSS */
.ds-btn__period {
  display: inline-block; margin-left: 1px;
  animation: ds-period-pulse 1800ms cubic-bezier(0.45, 0, 0.55, 1) infinite;
}
@keyframes ds-period-pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%      { opacity: 0.2; transform: scale(0.6); }
}
@media (prefers-reduced-motion: reduce) {
  .ds-btn__period { animation: none; opacity: 1; }
}

/* ---------- IconButton ---------- */
.ds-icon-btn {
  width: var(--hs); height: var(--hs);
  display: inline-flex; align-items: center; justify-content: center;
  border: 1px solid var(--border-soft); border-radius: var(--radius-2);
  background: var(--sfr); color: var(--tg2); cursor: pointer;
  box-shadow: var(--sha);
  transition: background-color var(--dur-2) var(--ez), color var(--dur-2) var(--ez), border-color var(--dur-2) var(--ez), transform var(--dur-2) var(--ez);
}
.ds-icon-btn:hover { background: var(--sf2); border-color: var(--border-strong); color: var(--ti); transform: translateY(-1px); }
.ds-icon-btn:active { transform: scale(var(--motion-press-scale)); transition-duration: var(--dur-1); }
.ds-icon-btn:focus-visible { outline: 2px solid var(--fr); outline-offset: 2px; }
.ds-icon-btn--ghost { border-color: transparent; box-shadow: none; background: transparent; }

/* ---------- Input / Textarea ---------- */
.ds-field {
  width: 100%; min-height: var(--hm); padding: 0 var(--s3);
  border: 1px solid var(--border-strong); border-radius: var(--radius-2);
  background: var(--sfr); color: var(--ti);
  font-family: inherit; font-size: var(--ts); line-height: var(--ls);
  outline: none;
  transition: border-color var(--dur-2) var(--ez), box-shadow var(--dur-2) var(--ez);
}
.ds-field::placeholder { color: var(--tg2); }
.ds-field:hover:not(:disabled):not(:focus) { border-color: var(--border-contrast, var(--border-strong)); }
.ds-field:focus { border-color: var(--fr); box-shadow: 0 0 0 2px color-mix(in srgb, var(--fr) 18%, transparent); }
.ds-field--error { border-color: var(--er); box-shadow: 0 0 0 2px color-mix(in srgb, var(--er) 18%, transparent); }
.ds-field:disabled { opacity: 0.5; cursor: not-allowed; background: var(--sf2); }
.ds-field--textarea { min-height: 80px; padding: var(--s2) var(--s3); resize: vertical; }

.ds-field-label { font-size: var(--ts); font-weight: var(--font-label-weight); color: var(--ti); }
.ds-field-hint  { font-size: var(--tx); color: var(--tg2); }
.ds-field-error { font-size: var(--tx); color: var(--er); }

/* ---------- Card ---------- */
.ds-card {
  border: 1px solid var(--border-soft); border-radius: var(--radius-3);
  background: var(--sfr); padding: var(--s4);
  box-shadow: var(--sha);
  display: grid; gap: var(--s2);
  transition: border-color var(--dur-2) var(--ez), box-shadow var(--dur-2) var(--ez), transform var(--dur-2) var(--ez);
}
.ds-card[data-interactive="true"]:hover { transform: translateY(-1px); box-shadow: var(--shb); border-color: var(--border-strong); }
.ds-card--muted    { background: var(--sf1); }
.ds-card--elevated { box-shadow: var(--shb); }
.ds-card__title { font-size: var(--ts); font-weight: var(--font-label-weight); color: var(--ti); }
.ds-card__body  { font-size: 13px; color: var(--tm2); line-height: var(--ls); }
.ds-card__footer{ display: flex; align-items: center; justify-content: space-between; padding-top: var(--s1); }

/* ---------- Pill ---------- */
.ds-pill {
  display: inline-flex; align-items: center; height: 28px; padding: 0 var(--s3);
  border-radius: var(--radius-pill); font-size: var(--tx); font-weight: var(--font-label-weight);
  white-space: nowrap; border: 1px solid transparent;
}
.ds-pill--neutral { background: var(--sf2); color: var(--tm2); }
.ds-pill--accent  { background: var(--ap); color: var(--am); }
.ds-pill--success { background: var(--okb); color: var(--okt); }
.ds-pill--warning { background: var(--wab); color: var(--wat); }
.ds-pill--danger  { background: var(--erb); color: var(--ert); }

/* ---------- StatusBadge (with dot) ---------- */
.ds-status {
  display: inline-flex; align-items: center; gap: var(--s2); height: var(--hs); padding: 0 var(--s3);
  border-radius: var(--radius-1); font-size: 13px; font-weight: var(--font-label-weight);
}
.ds-status__dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

/* ---------- Toast ---------- */
.ds-toast-region {
  position: fixed; bottom: var(--s5); right: var(--s5);
  display: flex; flex-direction: column-reverse; gap: var(--s2); align-items: flex-end;
  z-index: var(--z-toast); pointer-events: none;
}
.ds-toast {
  display: flex; align-items: flex-start; gap: var(--s3);
  padding: var(--s3) var(--s4); border-radius: var(--radius-3);
  border: 1px solid var(--border-strong);
  background: var(--sfr); color: var(--ti);
  box-shadow: var(--shb);
  min-width: 220px; max-width: 360px; pointer-events: all;
  transform: translateY(12px) scale(0.97); opacity: 0;
  transition: transform 320ms var(--motion-ease-enter), opacity 280ms var(--motion-ease-enter);
}
.ds-toast[data-state="open"]    { transform: translateY(0) scale(1); opacity: 1; }
.ds-toast[data-state="closing"] { transform: translateY(6px) scale(0.98); opacity: 0;
  transition: transform 160ms var(--motion-ease-exit), opacity 140ms var(--motion-ease-exit); }
.ds-toast__icon { width: 18px; height: 18px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 700; flex-shrink: 0; margin-top: 1px; }
.ds-toast__title { font-size: var(--ts); font-weight: var(--font-label-weight); line-height: var(--ls); }
.ds-toast__desc  { font-size: var(--tx); color: var(--tm2); margin-top: 1px; line-height: 18px; }
.ds-toast--neutral .ds-toast__icon { background: var(--sf2); color: var(--tg2); }
.ds-toast--success { background: var(--okb); border-color: color-mix(in srgb, var(--ok) 26%, transparent); }
.ds-toast--success .ds-toast__icon { background: var(--ok); color: #fff; }
.ds-toast--success .ds-toast__title { color: var(--okt); }
.ds-toast--danger  { background: var(--erb); border-color: color-mix(in srgb, var(--er) 26%, transparent); }
.ds-toast--danger  .ds-toast__icon { background: var(--er); color: #fff; }
.ds-toast--danger  .ds-toast__title { color: var(--ert); }
@media (prefers-reduced-motion: reduce) {
  .ds-toast, .ds-toast[data-state] { transition: none; transform: none; }
}

/* ---------- Dialog ---------- */
.ds-dialog-overlay {
  position: fixed; inset: 0; z-index: var(--z-modal);
  background: color-mix(in srgb, var(--ti) 28%, transparent);
  backdrop-filter: blur(var(--frost-blur)) saturate(var(--frost-saturate));
  opacity: 0; transition: opacity var(--dur-3) var(--motion-ease-enter);
}
.ds-dialog-overlay[data-state="open"] { opacity: 1; }
.ds-dialog {
  position: fixed; left: 50%; top: 50%; z-index: calc(var(--z-modal) + 1);
  width: min(560px, calc(100vw - var(--s5)));
  background: var(--sfr); color: var(--ti);
  border: 1px solid var(--border-soft); border-radius: var(--radius-4);
  box-shadow: var(--shc); padding: var(--s5);
  transform: translate(-50%, -50%) translateY(10px) scale(0.96); filter: blur(10px); opacity: 0;
  transition: transform 220ms var(--motion-ease-emphasized), filter 220ms var(--motion-ease-emphasized), opacity 220ms var(--motion-ease-emphasized);
}
.ds-dialog[data-state="open"] { transform: translate(-50%, -50%) translateY(0) scale(1); filter: blur(0); opacity: 1; }
.ds-dialog__title { font-size: var(--tm); line-height: var(--ll); font-weight: var(--font-heading-weight); letter-spacing: var(--tracking-tight); }
.ds-dialog__body  { margin-top: var(--s3); font-size: var(--ts); color: var(--tm2); line-height: var(--ls); }
.ds-dialog__footer{ display: flex; gap: var(--s2); justify-content: flex-end; margin-top: var(--s5); }

/* ---------- Skeleton ---------- */
.ds-skeleton {
  background: linear-gradient(90deg, var(--sf2) 0%, var(--sf1) 50%, var(--sf2) 100%);
  background-size: 200% 100%;
  animation: ds-skeleton-shift 1400ms linear infinite;
  border-radius: var(--radius-1);
}
@keyframes ds-skeleton-shift { from { background-position: 200% 0; } to { background-position: -200% 0; } }
@media (prefers-reduced-motion: reduce) { .ds-skeleton { animation: none; } }

/* ---------- AI Stage List (motion sketch 03) ---------- */
.ds-ai-stage { display: grid; gap: var(--s1); }
.ds-ai-stage__header { display: flex; align-items: baseline; gap: var(--s2); margin-bottom: var(--s4); font-size: var(--ts); font-weight: var(--font-label-weight); }
.ds-ai-stage__period { display: inline-block; width: 5px; height: 5px; border-radius: 50%; background: var(--ac); vertical-align: middle; }
.ds-ai-stage__period[data-thinking="true"] { animation: tw-breathe var(--motion-duration-brand) var(--motion-ease-breathe) infinite; }
.ds-ai-stage__item { display: flex; align-items: center; gap: var(--s2); height: 30px;
  transition: opacity var(--motion-duration-medium) var(--motion-ease-standard), color var(--motion-duration-medium) var(--motion-ease-standard); }
.ds-ai-stage__dot  { width: 5px; height: 5px; border-radius: 50%; flex-shrink: 0;
  transition: background-color var(--motion-duration-medium) var(--motion-ease-standard), opacity var(--motion-duration-medium) var(--motion-ease-standard); }
.ds-ai-stage__text { font-size: 13px;
  transition: color var(--motion-duration-medium) var(--motion-ease-standard); }
.ds-ai-stage__item[data-state="pending"] .ds-ai-stage__dot  { background: var(--tg2); opacity: 0.3; }
.ds-ai-stage__item[data-state="pending"] .ds-ai-stage__text { color: var(--tm2); opacity: 0.35; }
.ds-ai-stage__item[data-state="active"]  .ds-ai-stage__dot  { background: var(--ac); opacity: 1; }
.ds-ai-stage__item[data-state="active"]  .ds-ai-stage__text { color: var(--ti); font-weight: var(--font-label-weight); }
.ds-ai-stage__item[data-state="done"]    .ds-ai-stage__dot  { background: var(--tg2); opacity: 0.55; }
.ds-ai-stage__item[data-state="done"]    .ds-ai-stage__text { color: var(--tg2); }
.ds-ai-stage__item[data-state="error"]   .ds-ai-stage__dot  { background: var(--er); opacity: 1; }
.ds-ai-stage__item[data-state="error"]   .ds-ai-stage__text { color: var(--ti); font-weight: var(--font-label-weight); }

/* ---------- AI Suggestion Card ---------- */
.ds-ai-card {
  border: 1px solid var(--border-strong); border-radius: var(--radius-3);
  background: var(--sfr); box-shadow: var(--shb);
  display: grid; gap: var(--s3); padding: var(--s4);
  opacity: 0; transform: translateY(4px);
  transition: opacity var(--motion-duration-medium) var(--motion-ease-enter),
              transform var(--motion-duration-medium) var(--motion-ease-enter);
}
.ds-ai-card[data-state="open"]    { opacity: 1; transform: translateY(0); }
.ds-ai-card[data-state="closing"] { opacity: 0; transform: translateY(2px);
  transition-duration: var(--motion-duration-fast);
  transition-timing-function: var(--motion-ease-exit); }
.ds-ai-card--compact { padding: var(--s3); border-radius: var(--radius-2); gap: var(--s2); }
.ds-ai-card__overline { font-size: 10px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--am); font-weight: var(--font-label-weight); }
.ds-ai-card__title    { font-size: var(--ts); font-weight: var(--font-label-weight); color: var(--ti); }
.ds-ai-card__body     { font-size: 13px; line-height: var(--lb); color: var(--tm2); }
.ds-ai-card__footer   { display: flex; gap: var(--s2); justify-content: flex-end; align-items: center; }
.ds-ai-card__loading  { font-size: var(--tx); color: var(--tg2); }
.ds-ai-card__error    { font-size: var(--tx); color: var(--er); }

/* ---------- Diff Block (motion sketch 05) ---------- */
.ds-diff-block { font-size: 13px; line-height: 22px; color: var(--tm2); margin-bottom: var(--s3); position: relative; }
.ds-diff-block--removed {
  background: var(--erb); color: var(--ert);
  text-decoration: line-through; text-decoration-color: var(--er);
  border-radius: 3px; padding: 3px 4px;
  animation: ds-block-in 280ms var(--motion-ease-enter) both;
}
.ds-diff-block--added {
  background: var(--okb); color: var(--okt);
  border-radius: 3px; padding: 3px 4px;
  animation: ds-block-in 280ms var(--motion-ease-enter) both;
}
.ds-diff-block__old { background: var(--erb); color: var(--ert); text-decoration: line-through; text-decoration-color: var(--er); border-radius: 3px; padding: 1px 3px; margin-right: 4px; }
.ds-diff-block__new { background: var(--ap); color: var(--ti); border-radius: 3px; padding: 1px 3px;
  animation: ds-block-in 280ms 80ms var(--motion-ease-enter) both; }
@keyframes ds-block-in { from { opacity: 0; transform: translateY(3px); } to { opacity: 1; transform: translateY(0); } }
@media (prefers-reduced-motion: reduce) {
  .ds-diff-block--removed, .ds-diff-block--added, .ds-diff-block__new { animation: none; }
}

/* ---------- Floating AI Toolbar ---------- */
.ds-ai-toolbar {
  position: absolute; z-index: var(--z-popover);
  display: inline-flex; align-items: center; gap: var(--s1);
  height: 36px; padding: 0 var(--s2);
  background: var(--sfr); color: var(--ti);
  border: 1px solid var(--border-strong); border-radius: var(--radius-pill);
  box-shadow: var(--shb);
  opacity: 0; transform: translateY(4px);
  transition: opacity var(--motion-duration-fast) var(--motion-ease-enter),
              transform var(--motion-duration-fast) var(--motion-ease-enter);
}
.ds-ai-toolbar[data-state="open"]    { opacity: 1; transform: translateY(0); }
.ds-ai-toolbar[data-state="closing"] { opacity: 0; transform: translateY(2px);
  transition-duration: var(--motion-duration-micro); transition-timing-function: var(--motion-ease-exit); }
.ds-ai-toolbar__btn {
  height: 28px; padding: 0 var(--s3); border: none; background: transparent;
  color: var(--ti); font: inherit; font-size: var(--tx); font-weight: var(--font-label-weight);
  border-radius: var(--radius-1); cursor: pointer;
  transition: background-color var(--dur-2) var(--ez);
}
.ds-ai-toolbar__btn:hover:not(:disabled) { background: var(--sf2); }
.ds-ai-toolbar__btn[aria-pressed="true"] { background: var(--ap); color: var(--am); }
.ds-ai-toolbar__btn:disabled { opacity: 0.42; cursor: not-allowed; }
.ds-ai-toolbar__divider { width: 1px; height: 20px; background: var(--border-strong); margin: 0 var(--s1); }

/* ---------- Ask AI Input (expandable inside toolbar) ---------- */
.ds-ask-ai {
  display: inline-flex; align-items: center; gap: var(--s2);
  height: 32px; padding: 0 var(--s2);
  background: var(--sf2); border-radius: var(--radius-1);
  width: 240px;
  transition: width var(--motion-duration-medium) var(--motion-ease-emphasized);
}
.ds-ask-ai__input {
  flex: 1; height: 100%; min-width: 0; padding: 0;
  background: transparent; border: none; outline: none; color: var(--ti);
  font: inherit; font-size: var(--ts);
}
.ds-ask-ai__input::placeholder { color: var(--tg2); }
.ds-ask-ai[data-loading="true"] .ds-ask-ai__input { color: var(--tm2); }

}
```

---

## 4. Component contracts (TypeScript)

### 4.1 Button — `components/ui/button.tsx`

```ts
export type ButtonSize = "sm" | "md" | "lg";
export type ButtonVariant =
  | "primary" | "secondary" | "ghost" | "accent" | "danger" | "success";

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  size?: ButtonSize;          // default "md"
  variant?: ButtonVariant;    // default "primary"
  loading?: boolean;          // when true, label becomes `${children}<period-pulse>` and disabled
  loadingLabel?: string;      // optional override e.g. "Generating"
  pill?: boolean;             // radius pill
  iconLeft?: React.ReactNode;
  iconRight?: React.ReactNode;
  asChild?: boolean;          // optional Radix-slot pattern (only if you already use @radix-ui/react-slot)
}
```

**Rendering rules:**
- Class root: `ds-btn`, plus `ds-btn--{size}`, `ds-btn--{variant}`, `ds-btn--pill` if `pill`.
- When `loading=true`: render `<span>{loadingLabel ?? children}</span><span class="ds-btn__period" aria-hidden="true">.</span>` and apply `disabled` and `aria-busy="true"`.
- When `disabled`: real `disabled` attribute + remove all hover transforms (handled in CSS).
- Type defaults to `button` (no implicit form submits).
- Focus visible: native (CSS handles it).
- Icons: 16×16, render before/after text with `gap: 6px`. Use Phosphor regular weight via `lib/icons.tsx`.

**Forbidden:** spinners, dots, icons-as-loading-state. Only the period pulse.

### 4.2 IconButton — `components/ui/icon-button.tsx`

```ts
export interface IconButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "default" | "ghost"; // default "default"
  label: string;                 // REQUIRED — used as aria-label and tooltip title
  children: React.ReactNode;     // icon node, 16×16
}
```

Class root: `ds-icon-btn`, add `ds-icon-btn--ghost` for ghost. `aria-label={label}` mandatory.

### 4.3 Input / Textarea — `components/ui/input.tsx`, `components/ui/textarea.tsx`

```ts
export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  hint?: string;
  error?: string;       // when set, applies error border + replaces hint
  id?: string;
}
export interface TextareaProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {
  label?: string;
  hint?: string;
  error?: string;
  id?: string;
}
```

**Rendering:**
- Wrap in `<div class="grid gap-1.5">` (or inline style `display:grid; gap:6px`).
- `<label class="ds-field-label" htmlFor={id}>` if `label`.
- `<input class="ds-field" aria-invalid={!!error} aria-describedby={describedBy}>` (or `<textarea class="ds-field ds-field--textarea">`).
- Bottom slot: error text (`.ds-field-error`) if `error`, else hint (`.ds-field-hint`) if `hint`.
- Auto-generate id with `useId()` if not provided.

### 4.4 Card — `components/ui/card.tsx`

```ts
export interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: "default" | "muted" | "elevated"; // default "default"
  interactive?: boolean;                       // hover lift
  asChild?: boolean;
}
export const CardTitle:  React.FC<React.HTMLAttributes<HTMLDivElement>>;
export const CardBody:   React.FC<React.HTMLAttributes<HTMLDivElement>>;
export const CardFooter: React.FC<React.HTMLAttributes<HTMLDivElement>>;
```

Root: `ds-card` + variant. `data-interactive={interactive}`. `CardTitle` → `.ds-card__title`, `CardBody` → `.ds-card__body`, `CardFooter` → `.ds-card__footer`.

### 4.5 Pill / StatusBadge — `components/ui/pill.tsx`, `components/ui/status-badge.tsx`

```ts
export type PillTone = "neutral" | "accent" | "success" | "warning" | "danger";
export interface PillProps extends React.HTMLAttributes<HTMLSpanElement> {
  tone?: PillTone; // default "neutral"
}

export interface StatusBadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  tone?: PillTone;
  dot?: boolean;     // default true
  pulsing?: boolean; // breathe the dot — only allowed for "Generating" state
}
```

For `StatusBadge` colors: same backgrounds/inks as pill. Dot color = ink color. When `pulsing`, apply `animation: tw-breathe var(--motion-duration-brand) var(--motion-ease-breathe) infinite` on dot.

### 4.6 Toast — `components/ui/toast.tsx`

API:
```ts
type ToastTone = "neutral" | "success" | "danger";
interface ToastInput {
  title: string;
  description?: string;
  tone?: ToastTone;        // default "neutral"
  durationMs?: number;     // default 4000
  action?: { label: string; onClick: () => void }; // optional inline action (used by UndoToast)
}
export const toast = {
  show(t: ToastInput): string;        // returns id
  dismiss(id: string): void;
};
export const ToastProvider: React.FC<{ children: React.ReactNode }>;
```

**Rules:**
- One region only, mounted by `ToastProvider`, `class="ds-toast-region"`.
- Stack direction: `column-reverse` (newest at bottom, visually at top of stack since `flex-direction: column-reverse` flips).
- Auto-dismiss after `durationMs`, **unless** `action` is present → durationMs default 6000 and a hover/focus pause.
- Pause auto-dismiss while pointer hovers a toast or it has focus.
- Reduced motion: instant in/out (CSS handles).

Icon glyphs: neutral `·`, success `✓`, danger `!`. No emoji.

### 4.7 Dialog — `components/ui/dialog.tsx`

Use Radix-style imperative API (or keep your existing one — verify). Required parts: `Dialog.Root`, `Dialog.Trigger`, `Dialog.Content` (+ `Title`, `Description`, `Footer`).
- Overlay class `ds-dialog-overlay`, content class `ds-dialog`.
- Sizes: small (max-w 420), default (560), large (720). Add `size?: "sm" | "md" | "lg"` prop on `Content`.
- Esc and overlay-click close (default).
- Focus trap and return-focus: keep current Radix behavior.

### 4.8 Skeleton — `components/ui/skeleton.tsx`

```ts
export interface SkeletonProps extends React.HTMLAttributes<HTMLDivElement> {
  width?: number | string;  // default "100%"
  height?: number | string; // default 12
  radius?: "1" | "2" | "3" | "pill"; // default "1"
}
```
Renders `<div class="ds-skeleton" style={...}>`. Width/height accept px numbers (auto append `px`) or string.

### 4.9 `index.ts` re-exports

```ts
export { Button } from "./button";
export { IconButton } from "./icon-button";
export { Input } from "./input";
export { Textarea } from "./textarea";
export { Card, CardTitle, CardBody, CardFooter } from "./card";
export { Pill } from "./pill";
export { StatusBadge } from "./status-badge";
export { Skeleton } from "./skeleton";
export { ToastProvider, toast } from "./toast";
export { Dialog } from "./dialog";
```

---

## 5. AI primitives — `components/ai/`

### 5.1 `AiStageList.tsx`

```ts
export type AiStageState = "pending" | "active" | "done" | "error";
export interface AiStage { id: string; label: string; }
export interface AiStageListProps {
  title: string;            // e.g. "Generating"
  stages: AiStage[];        // ordered
  currentIndex: number;     // 0..stages.length, stages.length means "all done"
  errorIndex?: number | null; // when set, that index is "error", everything after is "pending"
}
```

**Rendering rules (from motion sketch 03):**
- Header: `<div class="ds-ai-stage__header">{title}<span class="ds-ai-stage__period" data-thinking={thinking} /></div>`.
- `thinking = errorIndex == null && currentIndex < stages.length` (period pulses while work in progress, stops when done or errored).
- Each stage renders `<div class="ds-ai-stage__item" data-state={state}>` with state computed:
  - `state = "error"` if `errorIndex === i`
  - `state = "done"` if `i < currentIndex && errorIndex == null`
  - `state = "active"` if `i === currentIndex && errorIndex == null && i < stages.length`
  - else `"pending"`
- Stage labels are passed in. Default labels for proposal: `["Reading role", "Matching profile", "Writing draft", "Done."]`.
- The final stage when reached uses `data-state="active"` styling with `ti` color (no separate `done-final` state needed since `currentIndex === stages.length-1` makes it active).

**Forbidden:** per-stage spinners, color other than terracotta on active, animation other than the header period.

### 5.2 `AiSuggestionCard.tsx`

```ts
export type AiSuggestionMode = "default" | "compact" | "list";
export type AiSuggestionState = "loading" | "ready" | "error";
export type AiSuggestionAction = "rewrite" | "shorten" | "fix" | "ask" | "strengthen";

export interface AiSuggestionCardProps {
  mode?: AiSuggestionMode;          // default "default"
  state: AiSuggestionState;
  action: AiSuggestionAction;       // drives overline label
  before?: React.ReactNode;         // ignored when state="loading"
  after?: React.ReactNode;          // the suggested replacement / addition
  errorMessage?: string;            // when state="error"
  onAccept: () => void;
  onDiscard: () => void;
  onRetry?: () => void;             // when state="error"
}
```

**Overline label per action:**
| `action` | overline |
|---|---|
| `rewrite` | `AI · REWRITE` |
| `shorten` | `AI · SHORTEN` |
| `fix` | `AI · FIX` |
| `ask` | `AI · ASK` |
| `strengthen` | `AI · STRENGTHEN` |

(Sentence-case body text but overline is uppercase per token rules.)

**Layout (default mode):**
```
.ds-ai-card[data-state="open"]
  .ds-ai-card__overline    ← "AI · REWRITE"
  .ds-ai-card__title       ← "Suggested rewrite" (or computed)
  [diff area]              ← see "diff area" below
  .ds-ai-card__footer
    <Button variant="ghost"  size="sm" onClick={onDiscard}>Discard</Button>
    <Button variant="primary" size="sm" onClick={onAccept}>Accept</Button>
```

**Diff area:**
- If `before` AND `after`: render `DiffBlock mode="replace"` with both.
- If only `after` (additive): render `DiffBlock mode="add"`.
- If only `before` with `after=null`: `mode="remove"`.

**State variants:**
- `state="loading"`: instead of diff area, show `<div class="ds-ai-card__loading">Reading<span class="ds-btn__period">.</span></div>`. Hide footer accept/discard. Show only `<Button variant="ghost" size="sm" onClick={onDiscard}>Cancel</Button>`.
- `state="error"`: replace diff area with `<div class="ds-ai-card__error">{errorMessage ?? "Couldn't finish."}</div>`. Footer: `<Button variant="ghost" size="sm" onClick={onDiscard}>Dismiss</Button>` + `<Button variant="secondary" size="sm" onClick={onRetry}>Try again</Button>` (only if `onRetry`).

**`mode="compact"`:** add `ds-ai-card--compact`, hide overline, smaller padding. Use inside small editors / sidebar rails.
**`mode="list"`:** render `before/after` as `<ul>` with `DiffBlock` per bullet (added/removed/replaced). Use in Experience modal / bullets.

**Lifecycle:**
- Mount with `data-state="closing"`, then on next animation frame set `data-state="open"`. Same enter pattern as toast.
- On accept/discard, set `data-state="closing"` and call parent handler after `var(--motion-duration-fast)` (140ms).

### 5.3 `DiffBlock.tsx`

```ts
export type DiffMode = "add" | "remove" | "replace";
export interface DiffBlockProps {
  mode: DiffMode;
  before?: React.ReactNode; // required for "remove" and "replace"
  after?: React.ReactNode;  // required for "add" and "replace"
}
```

Rendering uses `.ds-diff-block`, `.ds-diff-block--added`, `.ds-diff-block--removed`, `.ds-diff-block__old`, `.ds-diff-block__new`. **No per-character animation. Block-level only.**

### 5.4 `FloatingAiToolbar.tsx` (refactor)

> Codex: the existing 24.5K monolith at `my-app/src/components/FloatingAiToolbar.tsx` must be REWRITTEN to this contract, then **moved** to `my-app/src/components/ai/FloatingAiToolbar.tsx`. Update all imports. Delete the old file.

```ts
export type AiToolbarAction = "rewrite" | "shorten" | "fix" | "ask";
export interface FloatingAiToolbarProps {
  /** anchor rect in viewport coords; toolbar positions itself above it */
  anchorRect: DOMRect | null;
  /** whether to render at all */
  open: boolean;
  /** action currently running, if any (disables others, shows period on label) */
  busyAction?: AiToolbarAction | null;
  onAction: (action: AiToolbarAction, askText?: string) => void;
  onClose: () => void;
}
```

**Rules:**
- **Maximum 4 visible actions:** Rewrite, Shorten, Fix, Ask. No more. No menu.
- Order in DOM: Rewrite | Shorten | Fix | divider | Ask.
- "Ask" toggles an inline `AskAiInput` that expands the toolbar width; on Enter, calls `onAction("ask", text)`. Esc closes the input only (not the toolbar).
- Position: `top = anchorRect.top - 36 - 8` (8px gap above selection); horizontally centered on `anchorRect`. If clipped at viewport top, position below: `top = anchorRect.bottom + 8`.
- Render in a portal at `document.body`, `position: absolute` with explicit `top/left/transform: translateX(-50%)`.
- `data-state="open" | "closing"` mirrors `open` prop with the 140ms exit before unmount.
- While `busyAction` is set: that button shows label + period pulse and `aria-busy="true"`; other buttons get `disabled`.
- Click outside → `onClose()`. Selection lost → `onClose()`.
- Reduced motion: respect via existing CSS rules.

**No icons in toolbar buttons.** Text labels only — sentence case.

### 5.5 `AskAiInput.tsx`

```ts
export interface AskAiInputProps {
  loading?: boolean;
  placeholder?: string; // default "Ask the document…"
  onSubmit: (text: string) => void;
  onCancel: () => void;
}
```

Renders `.ds-ask-ai` containing `<input class="ds-ask-ai__input">`. Enter → `onSubmit`. Esc → `onCancel`. Empty Enter → noop.
While `loading=true`, replace placeholder with `Asking.` (period uses `.ds-btn__period` span).

### 5.6 `UndoToast.tsx`

A thin wrapper over `toast.show` that emits a toast with `action: { label: "Undo", onClick }` and `tone: "neutral"`, `durationMs: 6000`. Use after Accept on a suggestion.

```ts
export function showUndoToast(opts: { title: string; onUndo: () => void }): void;
```

Default title for accepted rewrite: `"Change applied."`.

### 5.7 `components/ai/index.ts`

Re-export every component above.

---

## 6. Motion utilities — `lib/motion.ts`

```ts
export const motion = {
  duration: { micro: 80, fast: 140, normal: 200, medium: 320, panel: 420, settle: 480, reveal: 600 },
  ease: {
    standard:  "cubic-bezier(0.2, 0, 0, 1)",
    enter:     "cubic-bezier(0, 0, 0, 1)",
    exit:      "cubic-bezier(0.4, 0, 1, 1)",
    emphasized:"cubic-bezier(0.2, 0, 0, 1.2)",
    breathe:   "cubic-bezier(0.4, 0, 0.6, 1)",
  },
} as const;

export function prefersReducedMotion(): boolean {
  return typeof window !== "undefined" &&
    window.matchMedia?.("(prefers-reduced-motion: reduce)").matches === true;
}
```

Use only in TS where CSS variables can't be referenced (e.g., `setTimeout` durations matching CSS).

---

## 7. Voice / copy reference (use verbatim)

| Surface | Copy |
|---|---|
| Save success toast | `Saved.` |
| Generate done toast | `Draft ready.` (desc: `Your proposal has been generated.`) |
| Export done toast | `Export ready.` (desc: `PDF is ready to download.`) |
| Generic error toast | `Couldn't finish.` (desc: contextual or `Check your connection and try again.`) |
| AI applied undo toast | `Change applied.` (action: `Undo`) |
| AI loading inline | `Reading.` / `Asking.` (verb + period pulse) |
| Stage labels (proposal) | `Reading role`, `Matching profile`, `Writing draft`, `Done.` |
| Stage labels (CV section) | `Reading section`, `Refining`, `Done.` |
| Toolbar buttons | `Rewrite`, `Shorten`, `Fix`, `Ask` |
| Suggestion card primary | `Accept` |
| Suggestion card secondary | `Discard` |
| Suggestion card retry | `Try again` |
| Empty state cover letter | `No drafts yet.` |
| Empty state CVs | `No CVs yet.` |

**No emoji. No Title Case. No exclamation marks. Period at the end of declarative status lines.**

---

## 8. Storybook (Ladle) entries

For every primitive, create one story file with:
1. Default story.
2. One story per variant.
3. One story per state (loading, error, disabled, focused) where applicable.
4. One story for dark mode (wrap in `<div class="dark">`).
5. One story for `prefers-reduced-motion` simulated by setting `data-rm="true"` on root and a small CSS override in the story.

Acceptance: `pnpm ladle serve` runs without errors, every story renders.

---

## 9. Migration checklist (mechanical)

After primitives v2 is in:

1. **Replace imports** repo-wide:
   - `import { Button } from "@/components/ui/button"` — keep, but ensure it resolves to the v2 file.
   - `import FloatingAiToolbar from "@/components/FloatingAiToolbar"` → `import { FloatingAiToolbar } from "@/components/ai"`.
2. **Replace ad-hoc CSS** in pages where it's a 1-to-1 swap with a v2 class. Do NOT refactor pages structurally — that's later PRs.
3. **Delete** `components/FloatingAiToolbar.tsx`, `components/ProfileEditorUnified.tsx.bak`, `components/ProfileForm.tsx.bak`, `components/ProfileForm copy.md`, `pages/proposainputform.bak`, `src/COLORPALETTE.HTML`, `src/COLORPALETTE2.HTML` (Codex: confirm with `git status` before deleting).

---

## 10. Acceptance criteria (per task)

Each PR must satisfy ALL items below.

### A. Tokens contract & guardrails
- [ ] `motion-tokens.css` imported from `foundation.css`.
- [ ] Stylelint config in §11 added to `my-app/.stylelintrc.json`.
- [ ] `pnpm lint:css` script added; CI green.

### B. Primitives v2
- [ ] All primitive class names match §3 exactly.
- [ ] Each primitive has a Storybook story file under §8.
- [ ] Visual regression Playwright test takes screenshots of each story; baseline checked in.
- [ ] Reduced-motion: every animation either zero-duration or removed under the media query.
- [ ] Dark mode: every primitive renders correctly with `<body class="dark">`.
- [ ] Focus ring: 2px `var(--fr)` outline + 2px offset on every interactive primitive.
- [ ] `pnpm tsc --noEmit` passes.
- [ ] `pnpm test` passes.

### C. AI primitives
- [ ] `AiStageList`: state matrix tested (pending/active/done/error) — unit tests assert exactly one `data-state="active"` while running, zero when errored.
- [ ] `AiSuggestionCard`: enter animation 320ms, exit 140ms (verified by jest-fake-timer test or Playwright).
- [ ] `FloatingAiToolbar`: positions correctly above selection; falls back below when clipped (Playwright test).
- [ ] `FloatingAiToolbar`: only 4 actions rendered (assert by query selectors).
- [ ] `FloatingAiToolbar`: `Ask` expands width and accepts text; Enter submits, Esc closes input only.
- [ ] No `Rewrite/Strengthen/Ask` action triggers an auto-apply — handlers receive the action and parent renders a `AiSuggestionCard`. Test asserts no document mutation when `onAction` is called by the toolbar.
- [ ] `UndoToast.showUndoToast` shows a toast with action `Undo`, durationMs 6000, pause on hover.

### D. Migration
- [ ] Old `FloatingAiToolbar.tsx` deleted.
- [ ] No file imports `components/FloatingAiToolbar` anymore.
- [ ] `.bak`, COLORPALETTE\*.HTML, `proposainputform.bak`, `ProfileForm copy.md` removed.
- [ ] `pnpm build` green.

---

## 11. Stylelint guardrails — `my-app/.stylelintrc.json`

Codex: install `stylelint`, `stylelint-config-standard`, `stylelint-declaration-strict-value`. Add this config:

```json
{
  "extends": ["stylelint-config-standard"],
  "plugins": ["stylelint-declaration-strict-value"],
  "rules": {
    "scale-unlimited/declaration-strict-value": [
      ["/color$/", "background-color", "background", "border-color", "fill", "stroke", "box-shadow", "border-radius", "padding", "padding-top", "padding-right", "padding-bottom", "padding-left", "margin", "margin-top", "margin-right", "margin-bottom", "margin-left", "gap", "row-gap", "column-gap", "font-size", "line-height", "font-family", "transition-duration", "animation-duration", "transition-timing-function", "animation-timing-function", "z-index"],
      {
        "ignoreValues": [
          "0", "0px", "auto", "inherit", "initial", "unset", "currentColor", "transparent", "none",
          "/^var\\(--/", "/^calc\\(/", "/^color-mix\\(/"
        ],
        "disableFix": true,
        "severity": "error"
      }
    ],
    "color-no-hex": [true, { "ignoreFiles": ["**/foundation.css", "**/themes.css", "**/colors_and_type.css"] }],
    "selector-class-pattern": null,
    "no-descending-specificity": null
  },
  "ignoreFiles": ["**/dist/**", "**/build/**", "**/node_modules/**", "**/*.bak", "**/*.bak.css"]
}
```

Add to `package.json` scripts: `"lint:css": "stylelint 'src/**/*.css'"`.

CI: run `lint:css` in the existing GitHub Actions workflow before build.

---

## 12. Definition of Done (whole effort)

1. `pnpm tsc --noEmit && pnpm test && pnpm lint:css && pnpm build` all green locally and in CI.
2. Every primitive in §4 and AI primitive in §5 exists with the exact API.
3. Storybook serves with every story listed in §8.
4. No file in `src/` contains hardcoded color hex outside `foundation.css`/`themes.css` (verified by Stylelint).
5. `FloatingAiToolbar` lives at `components/ai/FloatingAiToolbar.tsx`; old path 404s; old file deleted.
6. Voice/copy strings match §7 exactly.
7. Reduced-motion fully respected (verified by one Playwright run with `--reduced-motion=reduce`).

---

## 13. Order of work (PR sequence)

Each PR title is the literal commit subject Codex must use.

| PR | Title | Files touched |
|---|---|---|
| **DS-1** | `chore(styles): import motion-tokens + stylelint guardrails` | `src/styles/foundation.css`, `.stylelintrc.json`, `package.json`, CI workflow |
| **DS-2** | `feat(ds-v2): primitives layer (button, input, card, pill, status, toast, dialog, skeleton)` | `src/styles/ds-v2.css`, `src/index.css`, `src/components/ui/*` |
| **DS-3** | `feat(ai): AiStageList + DiffBlock + AiSuggestionCard` | `src/components/ai/{AiStageList,DiffBlock,AiSuggestionCard,index}.tsx`, stories |
| **DS-4** | `refactor(ai): rewrite FloatingAiToolbar (4 actions, ask input, no auto-apply)` | `src/components/ai/FloatingAiToolbar.tsx`, `src/components/ai/AskAiInput.tsx`, delete old `src/components/FloatingAiToolbar.tsx`, fix imports |
| **DS-5** | `feat(ai): UndoToast helper + integrate with toast provider` | `src/components/ai/UndoToast.tsx`, `src/components/ui/toast.tsx` (action support) |
| **DS-6** | `chore: remove .bak files, COLORPALETTE htmls, dead duplicates` | repo root + `src/` cleanups |
| **DS-7** | `test(ds-v2): playwright visual baselines + a11y smoke` | `e2e/ds-v2.spec.ts`, screenshots |

Dependencies: DS-1 → DS-2 → (DS-3, DS-4) → DS-5 → DS-6 → DS-7.

---

## 14. Hard rules (Codex must not violate)

1. **No new tokens.** If a value is missing, stop and ask.
2. **No emoji, no Title Case, no exclamation marks** in UI strings.
3. **No spinners.** Period pulse only.
4. **No icons in `FloatingAiToolbar` buttons.** Text only.
5. **No auto-apply** for Rewrite / Strengthen / Ask. Toolbar emits action; parent shows `AiSuggestionCard`.
6. **No idle decorative animation** anywhere except the brand period (header dot in `AiStageList`, button-loading period).
7. **Block-level diff animation only.** No per-character.
8. **Maximum 4 actions** in `FloatingAiToolbar`.
9. **One toast region** in the whole app, mounted once at root.
10. **No literal hex/rgb** outside token files. Stylelint will fail the build.
11. Don't touch `ProposalForge.tsx`, `JobsPage.tsx`, `CvForge.tsx`, `SettingsPage.tsx` structurally in these PRs. Only import-path migrations.
12. Reduced-motion: every animation must have a `@media (prefers-reduced-motion: reduce)` neutralization.

---

## 15. Quick check before committing each PR

```
pnpm tsc --noEmit
pnpm test --run
pnpm lint:css
pnpm build
pnpm ladle build   # only after DS-2
```

All must exit 0. If any fails, fix before commit. No `--no-verify`.
