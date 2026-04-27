

## A 2026 Product Motion & Animation Audit

---

## 0. Executive design verdict

Most "AI app" motion systems in 2026 are still cosplaying as 2022 — gradient shimmers, sparkle icons, three-dot loaders pretending to think. Twoweeks.ai should refuse all of that. The brand promise is _finality_. The motion system must therefore be a system about **stopping**, not a system about movement.

The point of Twoweeks.ai's motion is to make four things legible:

1. **The app understood you** (a proof, not a flourish).
2. **The AI is doing real work** (stage text, not vibes).
3. **The thing changed** (a diff, not a swoosh).
4. **You can stop now** (settle, then silence).

Everything else — most things you see in modern AI products — should be cut.

---

## 1. Motion thesis

> **The point thinks. The document changes. The interface proves it. Then everything settles.**

This thesis already does most of the work. Three small refinements:

- **The point thinks** — only the period is allowed to breathe. Nothing else loops.
- **The document changes** — motion happens _to content_, not _around content_. We don't decorate, we mutate.
- **The interface proves it** — every AI moment ends in a visible artifact (a diff, a stage log, a highlighted region). No invisible work.
- **Then everything settles** — the resting state is the loudest state. Motion is the exception; stillness is the brand.

Operating rule: **every animation must name the user uncertainty it resolves.** If it can't, cut it.

---

## 2. Motion principles (7)

### 2.1 Stillness is the default

**Explanation.** Resting UI does not move, breathe, pulse, or shimmer. Looping animation is reserved for one element only: the brand period during AI work. **Why it fits.** Twoweeks.ai is anti-corporate-energy. Calm is the product. **Example.** Sidebar items have no idle animation. The active rail does not pulse. **Avoid.** Idle gradient sweeps, "alive" cards, hover parallax, animated illustrations.

### 2.2 Motion follows causality

**Explanation.** Animation only fires in response to a user action or a state change the user must notice. No ambient motion. **Why it fits.** The brand voice is declarative. Motion is the same — a sentence, not a song. **Example.** Saving a field flashes the saved state once. It does not pulse afterward. **Avoid.** Periodic re-animations, attention-grabbing loops, "look at me" idle states.

### 2.3 Proof over performance

**Explanation.** When the AI works, we show _what it's doing_ (reading role, matching profile, writing draft) and _what changed_ (diff highlights, region flash). We never show vague activity. **Why it fits.** Trust is earned with receipts. The brand refuses theater. **Example.** Generation streams stage text + the actual draft, not a loader. **Avoid.** Indeterminate spinners, shimmer placeholders during real AI work, opaque progress bars.

### 2.4 One ambient loop, ever

**Explanation.** The terracotta period is the _only_ element permitted an infinite loop, and only during active AI work. When the AI is idle, the period is solid. **Why it fits.** A single, recognizable thinking signal becomes brand. Multiple loaders become noise. **Example.** During generation: `two weeks•` (animated dot). At rest: `two weeks.` (solid). **Avoid.** Spinners next to the dot, progress bars co-existing with the dot, secondary "thinking" indicators.

### 2.5 Speed is a feature, not a transition

**Explanation.** Most transitions are 120–200ms. Anything above 320ms must justify itself (panel slides, modal appearance, brand moments). Route transitions are essentially zero. **Why it fits.** "Finish. Faster." cannot be the tagline of an app with 600ms page fades. **Example.** Tab switches: 140ms. Modal: 220ms. Route change: 80ms crossfade or instant. **Avoid.** Cinematic transitions, staggered card waterfalls, hero animations on navigation.

### 2.6 Content earns motion; chrome doesn't

**Explanation.** Editor regions, generated text, diffs, score changes, parsed CV blocks — these animate when they change, because the user needs to _see_ the change. Buttons, sidebars, tabs, headers — these snap. **Why it fits.** The product is about the document. The chrome is scaffolding. **Example.** A regenerated paragraph fades in over 200ms with a 1.2s terracotta underline. The "Generate" button does not bounce. **Avoid.** Animated icons, hover scale on chrome, button press depth.

### 2.7 Ending is louder than starting

**Explanation.** The settle — the moment work completes — gets the most expressive motion in the system. Entrances are quiet; completions are clear. **Why it fits.** "Two weeks. Period." The brand is about endings. **Example.** When a draft finishes: stage text collapses, period turns solid, "Done." appears, document gets a single 600ms terracotta border-pulse. **Avoid.** Confetti, success modals, celebratory sounds, checkmark animations with overshoot.

---

## 3. Logo motion system

The logo has four expressions and one rule: **only the period moves, and only when there is real work.**

```
Expanded:  two weeks.    ← resting (solid period)
Collapsed: tw.           ← resting (solid period)
Thinking:  two weeks•    ← AI working (period breathes)
Done:      two weeks.    ← AI just finished (period settles, brief glow)
```

### 3.1 Full logo (`two weeks.`) — header, marketing

- **At rest.** Solid terracotta period. Zero motion.
- **On page load.** No entrance animation. Logo is present, immediately. (Entrance animations on logos signal startup energy. We don't.)
- **During AI work anywhere in app.** Period transitions to _breathing_ state — opacity oscillates between `1.0` and `0.55` on a `2400ms` cycle, easing `cubic-bezier(0.4, 0, 0.6, 1)`. Color does not change. Size does not change.
- **On AI completion.** Period briefly scales `1.0 → 1.08 → 1.0` over 480ms (the "settle"), then stays solid.

### 3.2 Collapsed logo (`tw.`) — collapsed sidebar, app icon

- Same rules as full logo. The period still breathes during work.
- The collapsed form is the one that appears in the favicon / app icon / OS dock. **The breathing dot is what makes the icon feel alive without being childish.** This is your single most valuable brand-motion asset. Protect it.

### 3.3 App icon (favicon / PWA icon / dock)

- Static `tw.` at all times.
- Do **not** animate the favicon. Browser tab animation is a 2014 SaaS tic and creates visual noise across the user's entire OS.
- Exception: PWA installed-app icon may use a static frame with the period in _thinking_ opacity (~0.7) to signal "this app does background work." Test this. Cut if unclear.

### 3.4 Why the dot, not the `II` pause motif

- The `II` is a strong campaign mark but a weak UI signal. It reads as "paused," which is the opposite of "thinking."
- The dot is already present in the wordmark, in the URL (`twoweeks.ai`), and in the brand thesis ("Two weeks. Period."). It is the most overdetermined element you have. Use it.
- Reserve `II` for marketing surfaces, billboards, merch, and the "two weeks notice" metaphor. Keep it out of the product UI.

### 3.5 Avoiding AI-loader clichés

- The dot **does not** spin, orbit, pulse with multiple dots, or generate trailing dots.
- It **does not** change color (terracotta only).
- It **does not** become a spinner during long operations. Long operations get stage text instead. The dot just keeps breathing.
- It **does not** appear next to other loading indicators. If the dot is breathing, no spinner is permitted in the same view.

---

## 4. Motion tokens

Realistic values. Use these.

```css
:root {
  /* Durations */
  --motion-duration-instant:  0ms;
  --motion-duration-micro:    80ms;   /* state flips: hover, focus, press */
  --motion-duration-fast:     140ms;  /* small UI: tabs, dropdown items */
  --motion-duration-normal:   200ms;  /* most transitions */
  --motion-duration-medium:   320ms;  /* drawers, popovers */
  --motion-duration-panel:    420ms;  /* modals, side panels */
  --motion-duration-settle:   480ms;  /* completion / done state */
  --motion-duration-reveal:   600ms;  /* changed-region highlight */
  --motion-duration-brand:    2400ms; /* breathing period (one full cycle) */

  /* Easings */
  --motion-ease-linear:    cubic-bezier(0, 0, 1, 1);
  --motion-ease-standard:  cubic-bezier(0.2, 0, 0, 1);    /* default */
  --motion-ease-enter:     cubic-bezier(0, 0, 0, 1);      /* decelerate in */
  --motion-ease-exit:      cubic-bezier(0.4, 0, 1, 1);    /* accelerate out */
  --motion-ease-emphasized: cubic-bezier(0.2, 0, 0, 1.2); /* settle, with gentle overshoot */
  --motion-ease-breathe:   cubic-bezier(0.4, 0, 0.6, 1);  /* breathing dot only */

  /* Delays */
  --motion-delay-none:    0ms;
  --motion-delay-nudge:   40ms;   /* sequential reveals */
  --motion-delay-stage:   120ms;  /* stage text appearance */

  /* Stagger */
  --motion-stagger-tight:  20ms;  /* list items entering */
  --motion-stagger-normal: 40ms;
  --motion-stagger-loose:  80ms;  /* parsed CV blocks */
  /* Stagger never applied to >8 items. After 8, all remaining items appear together. */

  /* Translation */
  --motion-translate-xs: 2px;
  --motion-translate-sm: 4px;
  --motion-translate-md: 8px;
  --motion-translate-lg: 16px;  /* drawers, sheets */
  --motion-translate-xl: 24px;  /* mobile bottom sheets */

  /* Scale */
  --motion-scale-press:    0.98;
  --motion-scale-rest:     1.00;
  --motion-scale-emphasis: 1.02;
  --motion-scale-settle:   1.08; /* period settle only */

  /* Opacity */
  --motion-opacity-ghost:    0;
  --motion-opacity-faint:    0.32;
  --motion-opacity-breathe-low:  0.55;
  --motion-opacity-breathe-high: 1.00;
  --motion-opacity-rest:     1.00;

  /* Blur — used sparingly, never on text */
  --motion-blur-none: 0px;
  --motion-blur-sm:   4px;   /* modal backdrop only */
  --motion-blur-md:   12px;  /* never on content; backdrop only */
}

/* Reduced motion fallbacks */
@media (prefers-reduced-motion: reduce) {
  :root {
    --motion-duration-micro:  0ms;
    --motion-duration-fast:   0ms;
    --motion-duration-normal: 0ms;
    --motion-duration-medium: 0ms;
    --motion-duration-panel:  0ms;
    --motion-duration-settle: 0ms;
    --motion-duration-reveal: 0ms;
    --motion-duration-brand:  0ms; /* dot becomes static */
  }
}
```

**Rules of thumb:**

- Default any new transition to `--motion-duration-normal` + `--motion-ease-standard`. Reach for other tokens only with cause.
- Never compose more than two animated properties on the same element simultaneously (e.g. `opacity` + `transform` is fine; adding `filter` is not).
- Never animate `width`, `height`, `top`, `left`, `margin`, or `padding`. Use `transform` and `clip-path`.

---

## 5. UI motion primitives

Each primitive does one thing. Composition happens in the flow specs.

### 5.1 `fade`

- **Use.** Content swaps, modal backdrops, toast appearance.
- **Timing.** 140–200ms.
- **Easing.** `--motion-ease-standard`.
- **Properties.** `opacity` only.
- **A11y.** Reduced motion → instant.
- **Don't.** Fade route transitions over 100ms. Fade text content while it streams.

### 5.2 `translate`

- **Use.** Drawers, side sheets, mobile nav.
- **Timing.** 320–420ms.
- **Easing.** `--motion-ease-enter` for in, `--motion-ease-exit` for out.
- **Properties.** `transform: translate3d()` only.
- **Distance.** Drawer = full width. Toast slide-in = `--motion-translate-md`.
- **Don't.** Translate buttons, cards, or chrome on idle.

### 5.3 `scale`

- **Use.** Press states, period settle.
- **Timing.** 80ms (press) or 480ms (settle).
- **Easing.** `--motion-ease-standard` or `--motion-ease-emphasized`.
- **Properties.** `transform: scale()`.
- **Don't.** Scale icons on hover. Scale cards on hover. Scale anything ambiently.

### 5.4 `reveal`

- **Use.** Drawer contents, accordion, evidence expansion.
- **Timing.** 320ms.
- **Easing.** `--motion-ease-enter`.
- **Properties.** `clip-path: inset()` + `opacity`. Avoid `height: auto` animation.
- **Don't.** Use for >300px of content (jarring). Stage instead.

### 5.5 `collapse`

- Reverse of `reveal`. `--motion-ease-exit`. Slightly faster, 240ms — collapse should feel decisive.

### 5.6 `highlight-flash`

- **Use.** Field saved, single-line edits accepted.
- **Timing.** 600ms total — 80ms ramp up, 520ms ramp down.
- **Properties.** `background-color` from terracotta-50 → transparent.
- **Don't.** Use on more than one element at a time. Use for region-level changes (use `updated-region-flash` instead).

### 5.7 `active-rail`

- **Use.** Sidebar selected state, tab indicator.
- **Behavior.** A 2px terracotta bar that _moves_ between active items, not appears/disappears.
- **Timing.** 200ms.
- **Easing.** `--motion-ease-standard`.
- **Properties.** `transform: translateY()` of a single rail element.
- **Don't.** Pulse the rail. Re-animate on route reload.

### 5.8 `breathing-dot`

- **Use.** The brand period during AI work. Nowhere else.
- **Timing.** 2400ms loop, infinite while AI active.
- **Easing.** `--motion-ease-breathe`.
- **Properties.** `opacity` only. From 1.0 → 0.55 → 1.0.
- **A11y.** Reduced motion → static dot at opacity 0.85, plus stage text carries the work signal.

### 5.9 `progress-step`

- **Use.** AI stage text ("Reading role", "Matching profile", "Writing draft").
- **Behavior.** Each completed step receives a faint terracotta tick; the active step is full opacity; pending steps are at 0.32 opacity.
- **Timing.** 200ms transition between states.
- **Don't.** Animate the tick (no checkmark draw-on). Just state-flip.

### 5.10 `updated-region-flash`

- **Use.** A paragraph or document region just changed (post-generation, post-edit).
- **Behavior.** A 1px terracotta left-border + faint terracotta background (alpha 0.06) for 1200ms, then fades over 600ms.
- **Don't.** Pulse. Repeat. Apply to >3 regions simultaneously.

### 5.11 `diff-reveal`

- **Use.** AI proposed edits in editor, before accept/reject.
- **Behavior.** Insertions: terracotta underline + slight background. Deletions: strikethrough at 0.5 opacity. Replacements: old text fades out (200ms), new text fades in (200ms, +40ms delay). No reflow during the swap — measure first.
- **Don't.** Animate every word. Animate per block.

### 5.12 `success-settle`

- **Use.** Generation done, export complete.
- **Behavior.** Stage text collapses to "Done.", period scales 1.0 → 1.08 → 1.0 (480ms), region gets one updated-region-flash.
- **Don't.** Add sound. Add modal. Add icon.

### 5.13 `error-contour`

- **Use.** Validation, AI failure, network error.
- **Behavior.** A 1px terracotta-700 border appears around the affected region (140ms), inline error text appears below (fade-in, 200ms, 40ms delay).
- **Don't.** Shake. Use red. Use icons that reinforce panic.

### 5.14 `skeleton-to-content`

- **Use.** _Only_ for true unknowns — initial document load, jobs list first fetch. Not for AI generation (stage text instead).
- **Behavior.** Skeleton blocks at neutral-100 (no shimmer). On content arrival: skeleton opacity → 0 (140ms), content opacity 0 → 1 (200ms, 40ms delay). No layout shift.
- **Don't.** Shimmer. Pulse. Use during AI work.

---

## 6. Flow specs

### 6.1 App shell

**Route transitions.** 80ms crossfade max, or instant. Routes feel like tabs, not pages. No hero transitions, no shared element morphs.

**Sidebar collapse/expand.** 320ms `--motion-ease-standard`. Width animates via `transform: translateX()` on contents inside a fixed-width container, not the container's `width`. Logo crossfades `two weeks.` ↔ `tw.` in 140ms during the collapse.

**Header logo.** Static unless AI is working anywhere in app → period breathes. Single source of truth for "is the app thinking right now."

**Nav active state.** `active-rail` primitive. Rail slides between items in 200ms. No fade in/out.

**Mobile nav.** Bottom sheet slides up 420ms with `--motion-ease-enter`. Backdrop fades in 200ms with `blur-sm`. Dismiss = 240ms exit.

### 6.2 AI thinking

The defining flow. Get this right; the brand stands.

```
User clicks "Generate"
  ↓ (0ms)
Button enters disabled state (opacity 0.5, 80ms)
  ↓
Period starts breathing (2400ms loop begins)
  ↓ (120ms)
Stage 1 text appears: "Reading role"           ← fade-in, 200ms
  ↓ (~600ms, real)
Stage 1 receives tick, Stage 2 appears: "Matching profile"
  ↓
Stage 2 receives tick, Stage 3 appears: "Writing draft"
  ↓ (text begins streaming)
Generated text streams into document — chunked, ~3-5 word groups, no per-character animation
  ↓ (stream ends)
success-settle:
  - Period: scale 1 → 1.08 → 1 (480ms)
  - Stage text collapses to "Done." (140ms fade-out of stages, 40ms delay, "Done." fades in 200ms)
  - Generated region: updated-region-flash (1200ms hold, 600ms fade)
  ↓ (~2000ms after settle starts)
"Done." disappears, period stops breathing, returns solid
```

**Failure.**

- Period stops breathing within 80ms.
- Stage text replaced with `error-contour` text: "Couldn't finish. Try again." (no exclamation, no apology theater).
- Generated region (if partial) remains; user can keep or discard.

**Cancel.**

- User clicks Stop. Period stops within 80ms. Stage text shows "Stopped." for 1200ms then fades. Partial output remains.

### 6.3 CV import / parsing

**Upload.** File appears in drop zone with 140ms fade. No bounce. No "drag here" animation while idle.

**Accepted.** Filename appears, period begins breathing (parsing is AI work).

**Parsing stages.** Same `progress-step` pattern: "Reading file", "Extracting sections", "Identifying experience", "Done."

**Block reveal.** Parsed blocks (Experience, Education, Skills) reveal with `--motion-stagger-loose` (80ms between blocks), max 8 staggered. Each block fades in + translates up `--motion-translate-sm`. 200ms each.

**Uncertain blocks.** Block carries an `error-contour` style border (warning variant — same terracotta but at 1px, no fill). On hover, an inline "Review" label appears (140ms).

**Reassignment motion.** When user drags a block to a new section: 200ms `transform`, `--motion-ease-standard`. Block flashes `updated-region-flash` once it lands.

### 6.4 Editor ↔ preview

**Hover editor section.** No motion in the editor. The corresponding preview section gets a 1px terracotta left-border (140ms fade-in). Reverses on hover-out.

**Click preview section.** Editor scrolls to corresponding section. Use native `scrollIntoView({behavior: 'smooth'})` capped at ~400ms — or instant if reduced motion. Target section gets a 600ms `updated-region-flash` (subtler variant, 0.04 alpha).

**Changed field update.** When the user edits a field, the corresponding preview region shows `updated-region-flash` 200ms after typing stops (debounced).

**Active section sync.** Editor scroll position drives a faint terracotta marker in the preview's right gutter. The marker translates, doesn't fade. 80ms updates, throttled.

### 6.5 Jobs / match score

**Import job.** Job card slides in from right `--motion-translate-md`, 320ms.

**Refresh match.** Period breathes. Score number animates from old value to new value — but only if change is ≥3 points. Smaller changes flip instantly. Counter animation: 600ms, `--motion-ease-emphasized`, no easing overshoot on the number itself.

**Matched / partial / missing rows.** Rows reveal with stagger (40ms, max 8). Status indicator (filled / half / outline circle) appears with 140ms fade. **No checkmark draw animations.**

**Evidence expansion.** `reveal` primitive, 320ms. Inside content fades in with 80ms delay.

**Score comparison (optional).** When score changes meaningfully, an inline `+4` or `−2` chip appears next to the new score for 2400ms then fades. Terracotta for positive, neutral gray for negative. **No green for up, red for down — that's stock-ticker grammar, wrong brand.**

### 6.6 Proposal generation

**First draft.** Same as AI thinking flow (§6.2).

**Tone change.** User selects a different tone. Period breathes. The diff-reveal primitive shows changes: deletions strike through, insertions underline. Settle: 480ms.

**Replace / Insert / Keep.** Three actions on each AI suggestion. Selecting one: chosen text gets `updated-region-flash`, suggestion chrome collapses (240ms `collapse`). No celebration.

**Diff preview.** When toggled, all changes reveal simultaneously (no stagger — staggering diffs implies hierarchy that isn't there). 200ms fade.

**Undo.** Reverses with same primitives, slightly faster (140ms vs 200ms). Undo should feel instant, not animated.

### 6.7 Export

**Preparing export.** Period breathes. Stage text: "Checking layout", "Embedding fonts", "Generating PDF".

**Ready.** `success-settle`. "Done." appears next to a download button that _was already there_ — don't reveal a new button. The button changes from disabled to active state (opacity 0.5 → 1.0, 200ms).

**Failure.** `error-contour` on the export panel. Inline message. Retry available immediately, no modal.

---

## 7. State grammar

|State|Visual treatment|Motion treatment|Duration|Loop?|A11y note|
|---|---|---|---|---|---|
|idle|Default styles|None|—|No|—|
|hover|Slight bg shift (alpha 0.04)|Background only, no transform|80ms|No|Must have non-color affordance|
|pressed|Bg shift + scale 0.98|scale + opacity|80ms|No|Keyboard activation matches|
|focused|2px terracotta ring, offset 2px|Ring fades in|140ms|No|Must be visible w/o color (use offset)|
|selected|Terracotta active rail or fill|Rail translates between items|200ms|No|aria-selected required|
|loading|Skeleton blocks (no shimmer)|skeleton-to-content|200ms|No|aria-busy on container|
|thinking|Stage text + breathing period|breathing-dot + stage transitions|2400ms|Yes¹|aria-live="polite" on stage region|
|streaming|Text appears in chunks|Chunked fade-in, no per-char animation|200ms/chunk|No|aria-live="polite", chunk announcements throttled|
|saving|Inline "Saving…" text, no spinner|Text fade only|200ms|No|aria-live="polite"|
|saved|Inline "Saved" + highlight-flash|highlight-flash on changed field|600ms|No|aria-live="polite", once|
|warning|Terracotta-warning border (no fill)|error-contour (warning variant)|140ms|No|role="status"|
|error|Terracotta-error border + inline text|error-contour|140ms|No|role="alert"|
|done|"Done." + settle|success-settle|480ms|No|aria-live="polite"|
|disabled|0.4 opacity, no pointer events|Opacity transition only|80ms|No|aria-disabled, not just visual|
|empty|Static illustration-free message|None on entry|—|No|—|
|offline|Subtle banner above content|Slide-down from top, 200ms|200ms|No|role="status", persistent until online|

¹ The breathing period is the only allowed loop. Reduced motion → static.

---

## 8. AI animation rulebook

**Banned.**

- Sparkles, stars, glints.
- Magic-wand cursors or icons.
- Rainbow / iridescent gradients.
- Generic three-dot loaders (`...`).
- Spinning circles of any kind during AI work.
- Animated robot/bot avatars.
- "Typing" indicators with bouncing dots.
- Per-character text reveals (cargo-culted from terminal aesthetics, slow to read).
- Confetti, fireworks, balloons.
- Sound effects.

**Required.**

1. **Breathing period.** The single ambient signal that AI is working. Anywhere in the app. One per app, never more.
    
2. **Stage text.** Every AI operation longer than 800ms displays its stages. Stages are short, declarative, lowercase-feeling: "Reading role", "Matching profile", "Writing draft". Never "Thinking…" or "AI is processing your request…".
    
3. **Source-reading proof.** When AI reads a document the user provided (CV, job posting), highlight the source sections being processed in real time, even subtly — a faint terracotta left-border traveling down the source. This is the most underused move in 2026 AI UX, and it builds trust faster than any other animation.
    
4. **Chunked text reveal.** Generated text appears in 3–5 word chunks, not character by character. Each chunk fades in over 80ms. The cursor (if any) is a 1px terracotta caret, not a blinking block. Reduced motion → text appears in paragraph chunks, no per-chunk animation.
    
5. **Diff-based proof.** When AI edits existing content (tone change, refinement), show the diff. Don't just replace silently. The diff _is_ the animation.
    
6. **Final settle.** Every AI operation ends in `success-settle` or `error-contour`. There is no third option. No "AI returned a partial result with caveats" mystery state.
    
7. **User control moments.** A "Stop" button is visible during any AI operation > 1.5s. Stopping is instant; the breathing period stops within 80ms. The brand is about agency.
    

---

## 9. Accessibility & performance rules

### Accessibility

- **`prefers-reduced-motion: reduce`** is honored everywhere. All durations except `--motion-duration-brand` collapse to 0; the brand period becomes static. Functional state changes still occur — they just don't animate.
- **No infinite decorative loops.** The breathing period is the only loop, and it is functional (signals work-in-progress), not decorative. Even so, it must be paused when the work completes.
- **No motion blocks comprehension.** Stage text uses `aria-live="polite"`, not `assertive`. Screen readers announce stages without interrupting the user.
- **Keyboard focus.** Focus rings are 2px solid terracotta with 2px offset. Visible on every theme. Focus _appears_ (140ms) but never animates _position_ — focus jumps are instant.
- **Streaming text accessibility.** Throttle `aria-live` updates to once per ~1500ms during streaming. Never announce per-chunk.
- **Color is never the only signal.** Errors have border + text. Warnings have border + label. Status is never communicated by color alone.
- **Motion-triggered seizure risk.** No flashes >3/sec. The breathing dot at 2400ms cycle is well under threshold.

### Performance

- **Animate `transform` and `opacity` only.** Anything else triggers layout/paint and is forbidden in motion primitives. `clip-path` is allowed for `reveal` (compositor-friendly in modern browsers).
- **No `width` / `height` animation.** Use scale or clip-path.
- **`will-change` discipline.** Apply only to elements actively animating; remove on completion. Never blanket `will-change: transform` across many elements.
- **Backdrop-filter blur** (modal backdrops) is the only filter allowed in motion. Cap at `--motion-blur-sm` (4px). Never blur content.
- **No JS-driven animation for the breathing dot.** CSS keyframes only. The dot must keep breathing if the main thread is busy.
- **Stagger caps.** No stagger sequence runs longer than 320ms total. After 8 items, remaining items appear together.
- **Mobile.** All durations respect the same tokens. Mobile transforms use `translate3d` to ensure GPU compositing. Bottom sheets on iOS Safari use `transform`, not `bottom` animation.
- **Streaming text** must batch DOM updates with `requestAnimationFrame`. Not per-token writes.
- **Page transitions** never block input. The next view is interactive immediately; outgoing view fades on its own.

---

## 10. Visual examples

### Logo states

```
Expanded:  two weeks.     ← rest
Collapsed: tw.            ← rest
Thinking:  two weeks•     ← AI active
Done:      two weeks.     ← settle, then rest
```

### AI generation flow (visible state)

```
[ User clicks Generate ]

two weeks•                ← period begins breathing

Reading role
Matching profile
Writing draft
  └─ Drafting cover letter for Senior PM role at Acme...
     [streaming chunks of generated text appear in document]

Done.                     ← stages collapse to "Done."
two weeks.                ← period settles, returns solid
```

### Job match score change

```
Before:   Match 71
After:    Match 75 +4     ← +4 chip in terracotta, fades after 2.4s
```

### Updated region (after AI edit)

```
┃ The candidate has six years of experience leading        ← terracotta left-border (1px)
┃ cross-functional teams, with a focus on...                  background alpha 0.06
                                                              fades over 600ms after 1200ms hold
```

### Sidebar (active rail)

```
  Inbox
┃ Jobs           ← rail (terracotta, 2px)
  Documents
  Settings
```

Rail moves between items in 200ms. Items themselves don't animate.

### Empty state

```
No documents yet.

Import your CV.    [ Import ]
```

No illustration. No animated empty-state mascot. Plain text, one CTA.

---

## 11. Implementation-ready output

### 11.1 Executive design verdict

Build a motion system about _stopping_, not _moving_. Stillness is the brand. The breathing period is the only ambient loop. Everything else is causal, fast, and ends in proof.

### 11.2 Motion thesis

The point thinks. The document changes. The interface proves it. Then everything settles.

### 11.3 Core brand animation

The terracotta period transitions between solid (rest) and breathing (work) states. Single source of truth across the app for "AI is doing something." Settle on completion. Static under reduced-motion.

### 11.4 Token system

See §4. Six duration tokens, six easings, careful scale/translate/opacity sets, full reduced-motion fallback. Stick to these — every off-token duration is technical debt.

### 11.5 Component primitives

14 primitives in §5. The most important ones to ship correctly: `breathing-dot`, `progress-step`, `updated-region-flash`, `diff-reveal`, `success-settle`, `active-rail`.

### 11.6 Flow specs

Detailed in §6. The AI thinking flow is the centerpiece — get §6.2 right and 70% of the brand is delivered.

### 11.7 Accessibility rules

Reduced motion collapses everything but kills the brand dot loop. `aria-live` for stages, throttled for streaming. Focus visible always, no animated focus position. Color is never the sole signal.

### 11.8 Performance rules

Transform + opacity only. CSS keyframes for the brand loop. Capped staggers. No layout-triggering properties. Streaming text via rAF batching.

### 11.9 Implementation order

See §12.

### 11.10 What to cut

- Any spinner. Replace with stage text or breathing period.
- Per-character text reveals.
- Hover scale / lift on cards and buttons.
- Route transitions over 100ms.
- Animated icons (the only allowed icon "motion" is state change, not animation).
- Skeleton shimmer.
- Idle background gradients.
- Animated empty-state illustrations.
- Toast slide + bounce. Slide only.
- Confetti and any success theater.
- Tab indicator fade-in/out (replace with translating rail).
- Any green/red color signaling for changes (stay in the terracotta + neutral system).

### 11.11 Final MVP motion checklist

- [ ] Reduced-motion media query implemented and tested.
- [ ] Motion tokens shipped as CSS variables.
- [ ] `breathing-dot` works as one global signal.
- [ ] Stage text component with `aria-live="polite"`.
- [ ] `updated-region-flash` shipped.
- [ ] `active-rail` for nav.
- [ ] `success-settle` for AI completion.
- [ ] `error-contour` for AI failure.
- [ ] All transitions audited against duration tokens (no off-token values).
- [ ] No animated `width`/`height`/`top`/`left` anywhere in the codebase.

---

## 12. Build this first

Ten pieces. In order. Ship nothing else until these are correct.

1. **Motion tokens as CSS variables**, including the `prefers-reduced-motion` overrides. Everything depends on this. Half a day.
2. **Breathing period component** (`breathing-dot`) with a single global "AI active" state. Every AI surface in the app subscribes to this one signal. The brand stands or falls here.
3. **Stage text component** — declarative, lowercase tone, `aria-live="polite"`, `progress-step` styling.
4. **`success-settle` primitive** — the most expressive moment in the app. Period scale 1 → 1.08 → 1, "Done." reveal, `updated-region-flash` on the affected region.
5. **`updated-region-flash`** — used everywhere content changes (AI generation, edits, score updates).
6. **`active-rail` for sidebar/tabs** — translating terracotta bar, 200ms. Replaces all fade-based active indicators.
7. **`error-contour`** — terracotta border + inline text, no shake, no icons of panic.
8. **Chunked text streaming** with throttled `aria-live` and a 1px terracotta caret. Replaces every "AI is typing" indicator.
9. **Drawer / modal motion** — translate + opacity, 320–420ms, with backdrop blur capped at 4px. Replaces any custom modal animation already shipped.
10. **Logo collapse transition** (`two weeks.` ↔ `tw.`) — 140ms crossfade, period stays put across both forms.

Everything else in this document is real, but it's the next sprint. These ten are the floor. With them in place, Twoweeks.ai will already feel calmer, faster, and more credible than ~95% of AI products shipping in 2026.