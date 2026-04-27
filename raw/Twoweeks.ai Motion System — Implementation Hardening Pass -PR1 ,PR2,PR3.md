

## 1. Executive verdict

**Needs hardening.** The audit is design-ready but not implementation-ready. Three concrete blockers:

1. It introduces a new `--motion-duration-*` namespace while `foundation.css` already ships `--duration-*`, `--dur-1..5`, and `--motion-*-duration`. Shipping the audit verbatim creates a third parallel namespace.
2. "Single global `isAiActive`" is under-specified — multiple concurrent AI ops (parse + generate + score refresh) will race the breathing period on/off.
3. Several rules are too absolute for the existing codebase ("never animate width", "no route transition", "favicon thinking variant"). Some need softening.

Hardening produces a 2-PR plan: PR1 ships tokens + breathing dot + stage text + AI activity hook with one real integration (proposal generation). PR2 wires the rest.

---

## 2. Token integration plan

**Recommended strategy: hybrid — add new canonical tokens, alias the legacy names to them, do not delete legacy.**

Rationale:

- Adding a separate `motion.css` fragments the source of truth — keep tokens in `foundation.css`.
- Replacing legacy tokens breaks every component currently consuming `--duration-fast` / `--motion-hover-duration`.
- Aliasing new → old loses semantic clarity (the new names _are_ the system).
- Aliasing old → new keeps callers working while migrating mentally to the new vocabulary.

**Canonical names going forward** (audit's `--motion-*` namespace):

```
--motion-duration-{instant,micro,fast,normal,medium,panel,settle,reveal,brand}
--motion-ease-{linear,standard,enter,exit,emphasized,breathe}
--motion-delay-{none,nudge,stage}
--motion-stagger-{tight,normal,loose}
--motion-translate-{xs,sm,md,lg,xl}
--motion-scale-{press,rest,emphasis,settle}
--motion-opacity-{ghost,faint,breathe-low,breathe-high,rest}
```

**Legacy aliases to retain** (one-line each, in `foundation.css`):

```css
--duration-fast:                 var(--motion-duration-fast);
--duration-normal:               var(--motion-duration-normal);
--duration-slow:                 var(--motion-duration-medium);
--ease-standard:                 var(--motion-ease-standard);
--ease-enter:                    var(--motion-ease-enter);
--ease-exit:                     var(--motion-ease-exit);
--dur-1:                         var(--motion-duration-micro);
--dur-2:                         var(--motion-duration-fast);
--dur-3:                         var(--motion-duration-normal);
--dur-4:                         var(--motion-duration-medium);
--dur-5:                         var(--motion-duration-panel);
--motion-hover-duration:         var(--motion-duration-micro);
--motion-press-duration:         var(--motion-duration-micro);
--motion-focus-duration:         var(--motion-duration-fast);
--motion-overlay-enter-duration: var(--motion-duration-panel);
--motion-overlay-exit-duration:  var(--motion-duration-medium);
--motion-panel-duration:         var(--motion-duration-panel);
```

Proposal-specific motion tokens stay untouched in PR1 — migrate in PR2.

The `prefers-reduced-motion` block sets the new canonical durations to `0ms`; aliases inherit automatically. One source of truth for reduced motion.

---

## 3. Component mapping

|Product area|Component / file pattern|Motion primitive|Trigger state|Notes|
|---|---|---|---|---|
|App shell sidebar|`components/AppShell/Sidebar*`|`active-rail`, `translate`|nav change, collapse|Rail translates; do **not** animate `width` of container — use fixed track + content `translateX`.|
|Header logo (full)|`components/Brand/Logo`|`breathing-dot` (period span)|`isAiActive` true|Single subscriber to global signal.|
|Collapsed logo|same component, `data-collapsed`|`breathing-dot` + `fade` crossfade|sidebar collapse|140ms crossfade between `two weeks.` and `tw.`|
|AI generation status|`components/Ai/StageText` (new)|`progress-step`, `fade`|per-stage transition|`aria-live="polite"`, throttled.|
|Proposal generation|`features/proposal/*`|`breathing-dot`, `progress-step`, `success-settle`, `updated-region-flash`|mutation state|Centerpiece for PR1.|
|CV import/parsing|`features/cv/Import*`|`progress-step`, stagger `fade+translate-sm`|parse mutation|Stagger cap 8 blocks.|
|Editor ↔ preview sync|`features/editor/*`, `features/preview/*`|`updated-region-flash`, gutter marker `translate`|debounced edit|200ms debounce after typing stops.|
|Document preview updates|`features/preview/Region`|`updated-region-flash`|content diff|Max 3 concurrent flashes.|
|Jobs match refresh|`features/jobs/MatchScore`|counter tween, `+N` chip fade|score delta ≥ 3|Skip tween for <3 delta.|
|Requirements rows|`features/jobs/Requirement*`|stagger `fade+translate-sm`|list mount|Cap 8, rest snap.|
|Export flow|`features/export/*`|`progress-step`, `success-settle`, `error-contour`|export mutation|Reuse stage text.|
|Modals / drawers / dropdowns|`components/ui/{Modal,Drawer,Popover}`|`translate` + `fade`, backdrop `fade`|open/close|Backdrop `blur-sm` cap 4px.|
|Toasts|`components/ui/Toast`|`translate` slide-in|append|Slide only, no bounce.|

---

## 4. State ownership

- **Global `isAiActive`**: derived, not stored. Live in a small `useAiActivity()` hook backed by a Zustand/Jotai store _or_ a Convex-derived selector that counts in-flight AI mutations. Do not duplicate per-feature boolean state.
- **Granularity**: a single global counter (`activeOperations: number`) is correct for the breathing dot (the dot answers "is _something_ thinking?"). Stage text lives per-operation and is owned by the calling feature.
- **Concurrent ops**: increment on start, decrement on settle/error/cancel. Dot breathes while `count > 0`. `success-settle` fires on the operation that just finished — not on the global counter.
- **How the logo knows**: subscribes to `useAiActivity().isActive`. One subscriber, top of `AppShell`.
- **Avoiding "breathes forever"**: every increment must be paired with a decrement in `finally`. Hook owns a hard timeout (default 60s per op) that auto-decrements with a console warning. On unmount of the originating component, decrement.
- **Cleanup**: `useEffect` return path decrements; `AbortController` cancels pending ops; route change decrements all ops registered to that route's component tree.
- **Derive from existing state**: prefer `useMutation().isPending` or Convex query `status === "pending"` over standalone booleans. The activity hook is a _roll-up_ of these — feed mutation states into it, don't shadow them.

---

## 5. First PR scope

**Title**: `feat(motion): introduce canonical motion tokens, breathing dot, stage text`

**Files to add**:

- `my-app/src/styles/motion.css` — _no_, fold into `foundation.css` (keep one source). Skip.
- `my-app/src/components/brand/BreathingDot.tsx`
- `my-app/src/components/ai/StageText.tsx`
- `my-app/src/hooks/useAiActivity.ts`
- `my-app/src/hooks/useReducedMotion.ts`
- Test files mirroring above.

**Files to modify**:

- `my-app/src/styles/foundation.css` — add new motion token block + reduced-motion override + legacy aliases.
- `my-app/src/components/brand/Logo.tsx` (or equivalent) — render period as `<BreathingDot />`.
- `features/proposal/*` generation entry point — wrap mutation with `useAiActivity().track(...)`, render `<StageText />`.

**Primitives implemented**: `breathing-dot`, `progress-step` (stage text styling only), reduced-motion plumbing.

**Real integration**: proposal generation only.

**Tests**:

- Unit: `useAiActivity` increment/decrement/timeout cleanup.
- Unit: `BreathingDot` static under reduced-motion.
- Unit: `StageText` `aria-live="polite"`, throttled announcements.
- CSS smoke: token resolution snapshot.

**Explicit non-goals**:

- No `active-rail`, no `updated-region-flash`, no `success-settle`, no `error-contour`, no diff-reveal in PR1.
- No CV/Jobs/Export wiring.
- No legacy token deletion.
- No favicon work.
- No route transition changes.

---

## 6. Second PR scope

**Title**: `feat(motion): settle, region flash, error contour, active rail`

- Add `success-settle`, `updated-region-flash`, `error-contour`, `active-rail` primitives.
- Wire CV parsing, jobs match refresh, export flow, sidebar/tab rail.
- Migrate proposal-specific motion tokens to canonical tokens, retire shadow tokens.
- Add Playwright reduced-motion test + visual diffs for the four new primitives.

PR3 (out of scope here) would handle chunked text streaming and modal/drawer migration.

---

## 7. Implementation details

**CSS class names** (BEM-ish, prefixed):

- `.tw-breathing-dot` (+ `[data-active="true"]`)
- `.tw-stage-text`, `.tw-stage-step[data-state="pending|active|done"]`
- `.tw-region-flash` (PR2)
- `.tw-active-rail` (PR2)

**Data attributes** (state, not classes — easier to test):

- `[data-ai-active]` on `<html>` or `AppShell` root, written by `useAiActivity`.
- `[data-motion-reduced]` on `<html>` for JS-side conditionals (mirrors media query).
- `[data-state]` on stage steps.

**React components**:

- `<BreathingDot solid={boolean} />` — pure CSS keyframe; `solid` forces resting.
- `<StageText stages={Stage[]} activeIndex={number} done={boolean} />`.
- `<AiActivityProvider />` (context) wrapping `AppShell`.

**Hooks**:

- `useAiActivity()` → `{ isActive, count, track<T>(promise, opts?) }`.
- `useReducedMotion()` → `boolean`, subscribes to `matchMedia('(prefers-reduced-motion: reduce)')`.

**Reduced-motion helper**: single `useReducedMotion()` hook + CSS media query. Components that have a non-CSS animation (none in PR1) read the hook; CSS-only animations rely on the token override.

**`aria-live` behavior**:

- Stage container: `aria-live="polite"` `aria-atomic="false"`.
- Throttle announcements to ≥1500ms apart (StageText internal).
- Breathing dot: `aria-hidden="true"` — purely decorative; the real signal is stage text.

**Cleanup behavior**:

- `useAiActivity.track()` returns a disposer; cleanup runs in `finally`.
- 60s safety timeout per op with `console.warn` (dev only).
- Route unmount drains pending ops via `AbortController`.

**No layout-thrash rules**:

- Lint rule (PR2): forbid CSS `transition`/`animation` properties on `width|height|top|left|right|bottom|margin|padding`. Document as ESLint custom rule or stylelint plugin.
- Use `transform` + `opacity` + `clip-path` only.
- `will-change` set inline only while animating; cleared on `animationend`.

---

## 8. Corrections to the audit

|Audit rule|Verdict|Reasoning / replacement|
|---|---|---|
|"Never animate width/height/top/left"|**Soften** → "Don't animate in PR1; keep allowed for sidebar collapse if already implemented that way until PR2 migration." Hard ban becomes a lint rule in PR2.||
|"Single global `isAiActive`"|**Soften** → global _counter_, not boolean. Stage text remains per-operation.||
|"No progress bar"|**Keep** for AI work; **soften** for export — a determinate progress bar is fine when bytes are real (PDF render).||
|"No shimmer"|**Keep**.||
|"No route transition"|**Soften** → "≤100ms crossfade or instant." Audit already says this; don't ban outright.||
|"Collapsed favicon animated period (PWA only)"|**Remove**. Audit hedges; remove entirely. Favicon stays static, no exceptions. Aligns with hard constraint.||
|"Score counter tween only if delta ≥3"|**Keep** but lower threshold to 2 — feels arbitrary at 3 and many real deltas are small.||
|"Chunked text reveal 3–5 words"|**Soften** → "chunk by server stream boundaries; do not introduce client-side re-chunking." Reduces complexity.||
|"Source-reading proof" (traveling border on source doc)|**Replace with safer rule** → defer to PR3. Real-time source highlighting is non-trivial and risks layout thrash.||
|"Period scale 1.08 on settle"|**Keep**, but ensure `transform-origin` is centered on the glyph baseline; otherwise it visually jumps.||
|"Stop button stops dot within 80ms"|**Keep**, but require the underlying mutation to actually abort — visual stop without real abort is theater.||

---

## 9. Test plan

**Unit** (Vitest + RTL):

- `useAiActivity`: `track()` increments/decrements; rejection still decrements; timeout decrements with warn; multiple concurrent tracks roll up correctly.
- `BreathingDot`: renders static element under `prefers-reduced-motion: reduce` (mock `matchMedia`).
- `StageText`: `aria-live="polite"`, announcement throttle, step `data-state` flips.
- `Logo`: subscribes to activity, period gets `data-active="true"` when count>0.

**CSS / token tests**:

- Snapshot a computed-style probe: `getComputedStyle(document.documentElement).getPropertyValue('--motion-duration-normal')` returns `200ms`; under reduced-motion returns `0ms`.
- Legacy alias resolution: `--duration-fast` resolves to same value as `--motion-duration-fast`.

**Playwright** (PR1 minimal, expand in PR2):

- Trigger proposal generation → assert `[data-ai-active]` present on root → assert stage text node exists → wait for completion → assert `[data-ai-active]` absent.
- Same flow under `page.emulateMedia({ reducedMotion: 'reduce' })`: dot static, completion still observable.

**Accessibility**:

- axe scan on AppShell with dot active: no violations.
- Screen-reader manual pass: stages announce politely, do not interrupt typing.

**Regression**:

- Visual diff of header, sidebar, proposal screen pre/post PR1 — should be pixel-identical at rest.
- Existing component tests must not change.

**Manual QA checklist**:

- [ ] Dot solid at rest in light + dark theme.
- [ ] Dot breathes during proposal generation.
- [ ] Dot stops within 200ms of completion or error.
- [ ] Two concurrent generations → dot stays breathing through both, stops only when both finish.
- [ ] `prefers-reduced-motion: reduce` → dot static, stages still update.
- [ ] No console warnings about leaked operations after happy path.
- [ ] Existing pages render unchanged.

---

## 10. Acceptance criteria (PR1)

1. `foundation.css` exports the canonical `--motion-*` tokens and reduced-motion overrides; legacy aliases resolve to the new tokens; no existing token is removed.
2. `useAiActivity` hook exposes `{ isActive, count, track }`; `track()` is the only public mutation path; cleanup verified by tests.
3. `<BreathingDot />` is a CSS-keyframe component, `aria-hidden`, becomes static under reduced motion, and is mounted inside the existing logo without changing logo layout (visual-diff identical at rest).
4. `<StageText />` renders an ordered list of stages, marks one active, has `aria-live="polite"`, and throttles announcements to ≥1500ms.
5. Proposal generation flow drives the dot via `useAiActivity().track()` and renders `<StageText />` for its stages — no other feature is touched.
6. All new code passes typecheck, lint, and unit tests; Playwright smoke for proposal generation passes in normal and reduced-motion modes.
7. No favicon changes. No route-transition changes. No deletion of existing motion tokens. No animated `width/height/top/left` introduced.
8. PR description lists every legacy token aliased and which canonical token it maps to.

---

## 11. Final Codex prompt (PR1)

```
# Context
You are working on Twoweeks.ai, a Next.js + TypeScript app located under
`my-app/`. Design tokens live in `my-app/src/styles/foundation.css` and
`my-app/src/styles/themes.css`. The repo already ships legacy motion tokens
(`--duration-fast/normal/slow`, `--ease-standard/enter/exit`, `--dur-1..5`,
`--motion-hover-duration`, `--motion-press-duration`, `--motion-focus-duration`,
`--motion-overlay-enter-duration`, `--motion-overlay-exit-duration`,
`--motion-panel-duration`, plus proposal-specific motion tokens). They are in
use across components and MUST keep working.

The brand motion thesis: "The point thinks. The document changes. The
interface proves it. Then everything settles." The terracotta period in the
`two weeks.` logo is the only animated brand element. No spinners, sparkles,
shimmer, confetti.

# Goal
Land the foundation of the motion system: canonical tokens, a single global
"AI is working" signal, the breathing-dot logo behavior, and stage text — wired
into proposal generation only.

# Scope
1. Extend `my-app/src/styles/foundation.css` with the canonical
   `--motion-duration-*`, `--motion-ease-*`, `--motion-delay-*`,
   `--motion-stagger-*`, `--motion-translate-*`, `--motion-scale-*`, and
   `--motion-opacity-*` token sets exactly as defined in section 4 of the
   motion audit.
2. Add `@media (prefers-reduced-motion: reduce)` overrides setting all
   canonical durations (including `--motion-duration-brand`) to `0ms`.
3. Add legacy aliases so existing tokens resolve to canonical tokens:
     --duration-fast        → --motion-duration-fast
     --duration-normal      → --motion-duration-normal
     --duration-slow        → --motion-duration-medium
     --ease-standard/enter/exit → corresponding --motion-ease-*
     --dur-1..5             → micro / fast / normal / medium / panel
     --motion-hover-duration   → --motion-duration-micro
     --motion-press-duration   → --motion-duration-micro
     --motion-focus-duration   → --motion-duration-fast
     --motion-overlay-enter-duration → --motion-duration-panel
     --motion-overlay-exit-duration  → --motion-duration-medium
     --motion-panel-duration   → --motion-duration-panel
4. Add `my-app/src/hooks/useReducedMotion.ts` — `matchMedia` subscription
   returning a boolean.
5. Add `my-app/src/hooks/useAiActivity.ts` — context + provider exposing
   `{ isActive, count, track<T>(promise, opts?: { timeoutMs?: number }) }`.
   Implementation notes:
     - internal counter; isActive = count > 0
     - track() increments before awaiting, decrements in finally
     - default 60s safety timeout that decrements with console.warn (dev)
     - exports `<AiActivityProvider />`; mount it inside the existing AppShell
     - write `data-ai-active` on `document.documentElement` whenever isActive flips
6. Add `my-app/src/components/brand/BreathingDot.tsx`:
     - renders a span with class `tw-breathing-dot`
     - reads `useAiActivity().isActive`
     - `aria-hidden="true"`
     - CSS keyframe `breathe` animates `opacity` 1 → 0.55 → 1 over
       `var(--motion-duration-brand)` with `var(--motion-ease-breathe)`
     - keyframe runs only when `[data-active="true"]`
     - reduced-motion: keyframe collapses to static via the token override
7. Replace the period glyph in the existing logo component with
   `<BreathingDot />`. Visual-diff at rest must be identical.
8. Add `my-app/src/components/ai/StageText.tsx`:
     - props: `{ stages: { id: string; label: string }[]; activeIndex: number; done?: boolean }`
     - container has `aria-live="polite"` `aria-atomic="false"`
     - each step has `data-state="pending" | "active" | "done"`
     - announcements throttled to ≥1500ms
     - styling: pending opacity 0.32, active 1.0, done 1.0 with terracotta tick
       (use existing terracotta token; no checkmark draw animation)
9. Wire proposal generation:
     - locate the proposal generation entry mutation
     - wrap the mutation promise in `useAiActivity().track(...)`
     - render `<StageText />` adjacent to the existing generation surface
     - do NOT change any generation, parsing, scoring, or export logic

# Do NOT change
- Any existing motion token VALUE (only ADD canonical tokens + ALIAS legacy).
- Any feature in CV import, Jobs, editor/preview, export, modals, toasts,
  sidebar rail, route transitions, or favicon.
- Any business logic in proposal generation.
- The `themes.css` file beyond what is strictly required (ideally untouched).
- framer-motion is not to be added.

# Constraints
- CSS keyframes only for the breathing dot. No JS-driven RAF loop.
- Animate `transform` and `opacity` only. No `width/height/top/left/margin/padding`.
- Honor `prefers-reduced-motion: reduce` everywhere.
- No favicon changes. No new route transitions. No new modals.
- Every `track()` call MUST decrement in `finally`. No leaked operations.
- TypeScript strict; no `any`.

# Acceptance criteria
1. `pnpm typecheck` passes.
2. `pnpm lint` passes.
3. `pnpm test` passes; new tests cover useAiActivity (increment/decrement/
   timeout/concurrent), BreathingDot (static under reduced-motion), and
   StageText (aria-live, throttle, data-state).
4. Playwright: proposal generation flips `[data-ai-active]` on then off;
   passes under both normal and `reducedMotion: 'reduce'` emulation.
5. Visual diff of header/sidebar/proposal screen at rest is unchanged.
6. Legacy tokens still resolve (computed style probe in test).
7. PR description enumerates every alias added and the canonical token it
   points to.

# Required validation commands
cd my-app && pnpm install
cd my-app && pnpm typecheck
cd my-app && pnpm lint
cd my-app && pnpm test
cd my-app && pnpm exec playwright test motion

# Required output format
- A single PR diff against the current branch.
- A PR body containing:
    ## Summary
    - 3 bullets describing what shipped.
    ## Token alias map
    - table of legacy → canonical.
    ## Test plan
    - markdown checklist matching Acceptance criteria 1–7.
    ## Non-goals
    - bullets matching the "Do NOT change" list.
```



# PR2 Codex prompt — revised

```
# Context
Twoweeks.ai motion system, PR2. PR1 already shipped canonical `--motion-*`
tokens with legacy aliases in `my-app/src/styles/foundation.css`,
`useReducedMotion`, `useAiActivity` + `<AiActivityProvider />`,
`<BreathingDot />` (mounted in the logo), and `<StageText />` wired into
proposal generation. The brand thesis is unchanged: only the terracotta period
animates ambiently; everything else is causal, fast, and ends in proof.

# Goal
Add four motion primitives — success-settle, updated-region-flash,
error-contour, active-rail — and wire them into proposal completion + failure,
jobs match refresh, CV parsing errors, and the sidebar/tab navigation. Begin
migrating proposal-specific motion tokens to canonical tokens.

# Pre-resolved decisions (do not deviate)
A. Period ref: refactor `<BreathingDot />` to `forwardRef<HTMLSpanElement>`.
   Update `Logo` to forward a ref through to the dot. `<SuccessSettle>`
   receives that ref via `targetRef`. No imperative handle pattern.
B. generationId: the proposal mutation does not currently return a stable id.
   Generate one client-side at mutation start: `crypto.randomUUID()`. Store
   it alongside the in-flight op; pass to `<RegionFlash flashKey={...} />`
   on completion. The id changes per generation, which is the trigger.
C. ActiveRail first paint: instant placement on mount (no transition on the
   first measurement); animate only on subsequent activeId changes.
   Implement by setting `transition: none` for the first layout effect, then
   enabling the 200ms transition on the next frame (`requestAnimationFrame`).
D. Match score direction: HIGHER is always better in this product. Positive
   delta = terracotta chip (`+N`), negative delta = neutral gray chip (`−N`).
   Never green/red. If a future surface inverts this, it must pass an
   explicit `direction="lower-is-better"` prop — out of scope for this PR.

# Scope
1. `my-app/src/components/motion/SuccessSettle.tsx`:
     - props: `{ play: boolean; targetRef: RefObject<HTMLElement>; children?: ReactNode }`
     - on `play` rising edge: applies class `tw-success-settle` to targetRef
       which runs a one-shot keyframe `scale 1 → 1.08 → 1` over
       `var(--motion-duration-settle)` with `var(--motion-ease-emphasized)`
     - removes class on `animationend`; clears `will-change`
     - renders an optional "Done." label adjacent (fade in 200ms, hold,
       fade out 1200ms)
     - reduced motion: no scale, "Done." still appears

2. `my-app/src/components/motion/RegionFlash.tsx`:
     - props: `{ flashKey: string | number; children: ReactNode; alpha?: 'normal' | 'subtle' }`
     - on flashKey change: sets `data-flash="true"` for 1800ms then clears
     - module-level counter caps concurrent flashes at 3; over-cap calls are no-ops
     - on HMR: export a `__resetFlashCounterForTests()` and also reset on
       `import.meta.hot?.dispose` if available
     - CSS class `tw-region-flash` paints 1px terracotta left-border + alpha 0.06 bg
       (subtle variant uses 0.04); fades over `--motion-duration-reveal` after a
       1200ms hold (use `--motion-flash-hold` token)

3. `my-app/src/components/motion/ErrorContour.tsx`:
     - props: `{ message: string; variant?: 'error' | 'warning' }`
     - renders a wrapping element with class `tw-error-contour` +
       `data-variant="error|warning"`
     - 1px border (terracotta-700 for error, terracotta-base for warning, no fill)
     - inline message with `role="alert"` (error) or `role="status"` (warning)
     - border fade-in 140ms; message fade-in 200ms with 40ms delay
     - NO shake, NO icon

4. `my-app/src/components/nav/ActiveRail.tsx`:
     - props: `{ activeId: string; orientation?: 'vertical' | 'horizontal' }`
     - finds element with `[data-rail-target="<activeId>"]` inside the rail's
       `parentElement`
     - measures via `getBoundingClientRect` relative to container
     - sets `transform: translateY(...)` (or X) and height/width to match target
     - First measurement: apply with `transition: none`, then re-enable
       transition on next `requestAnimationFrame`. Subsequent activeId
       changes use the 200ms transition with `var(--motion-ease-standard)`.
     - `ResizeObserver` on container re-measures (re-measure during sidebar
       collapse must not trigger a transition jump; treat any measurement
       caused by container resize as instant — same `transition: none` then
       re-enable pattern)
     - reduced motion: transition collapses to 0ms

5. `my-app/src/hooks/useFlashOnChange.ts`:
     - signature: `(value: unknown, debounceMs?: number) => number`
     - returns an incrementing counter that bumps when value changes
       (Object.is comparison) after a 200ms debounce
     - cleanup on unmount

6. `my-app/src/hooks/useTweenedNumber.ts` (helper for match score):
     - signature: `(target: number, opts: { durationMs: number; easing: string }) => number`
     - rAF-driven; cancels prior animation on new target; cancels on unmount
     - if `Math.abs(target - prev) < threshold` (caller passes), snaps
       (the score component, not the hook, owns the threshold)
     - reduced motion: snaps immediately

7. Extend `my-app/src/styles/foundation.css`:
     - add `--motion-flash-hold: 1200ms`
     - add `.tw-region-flash` rules + keyframe `regionFlashFade`
     - add `.tw-error-contour` rules (variants via `data-variant`)
     - add `.tw-active-rail` rules (absolutely positioned, transition transform)
     - add `.tw-success-settle` rules + keyframe `successSettle`
     - reduced-motion block: zero out new durations / animations

8. Wire integrations:
     - `<BreathingDot />` becomes `forwardRef`. Logo forwards a ref to the
       period span (decision A).
     - Proposal generation surface: at mutation start, generate
       `generationId = crypto.randomUUID()` and stash on the in-flight op
       (decision B). On completion, mount `<SuccessSettle play={done}
       targetRef={periodRef} />` and wrap the generated region in
       `<RegionFlash flashKey={generationId} />`. On error, render
       `<ErrorContour message="Couldn't finish. Try again." />` in place of
       stages.
     - Jobs match score component: HIGHER is better (decision D). When
       `Math.abs(delta) >= 2`, tween via `useTweenedNumber` over 600ms with
       `--motion-ease-emphasized`. Render `+N` (terracotta) or `−N` (neutral
       gray) chip that fades in 200ms and out after 2400ms. Delta < 2 snaps,
       no chip.
     - Sidebar + primary tab strip: replace fade-based active indicators
       with a single `<ActiveRail activeId={...} />` per nav. Add
       `data-rail-target` to each nav item. Remove prior fade CSS. Verify
       behavior during sidebar collapse — rail must not animate-jump while
       the container is resizing (decision C / ResizeObserver path).
     - CV parsing failure: render `<ErrorContour />`. Uncertain blocks:
       render with `<ErrorContour variant="warning" />` border styling (no
       message — border-only is acceptable for warnings on blocks).

9. Migrate proposal-specific motion tokens to alias canonical tokens. Do
   not delete; do not change effective values.

# Do NOT change
- Token VALUES (only add new ones + alias proposal tokens to canonical).
- Generation, parsing, scoring, or export business logic.
- favicon, route transitions, modals, drawers, toasts, editor↔preview sync,
  chunked text streaming.
- The PR1 hooks (`useAiActivity`, `useReducedMotion`).
- `<StageText />` and `<AiActivityProvider />` behavior.
- themes.css unless strictly required.

# Constraints
- CSS keyframes / transitions only. No framer-motion. The only JS-driven
  animation is the rAF score-counter tween via `useTweenedNumber` and the
  ActiveRail measurement loop.
- Animate `transform` and `opacity` only. No `width/height/top/left/margin/
  padding` transitions. ActiveRail sets height/width once per measurement,
  not via transition.
- Honor `prefers-reduced-motion: reduce` everywhere.
- `will-change` set inline only while animating; cleared on `animationend`.
- No green/red. Terracotta + neutral only.
- TypeScript strict; no `any`.
- Concurrent-flash cap is global. Provide HMR reset.
- All rAF loops cancel on unmount and on new input (no leaked frames).

# Acceptance criteria
1. `pnpm typecheck`, `pnpm lint`, `pnpm test`,
   `pnpm exec playwright test motion` all pass.
2. Proposal completion plays settle exactly once per generation; region
   flashes for 1800ms total. generationId changes per run.
3. Proposal failure renders `role="alert"` text via ErrorContour.
4. Match score: delta ≥ 2 tweens 600ms; delta < 2 snaps; chip never green/red;
   higher = terracotta, lower = neutral gray.
5. Sidebar + tab strip use ActiveRail. Rail's transform changes on nav.
   First paint is instant (no transition). Sidebar collapse does not cause
   the rail to animate-jump.
6. CV parsing surfaces ErrorContour on failure; uncertain blocks use warning
   variant border.
7. Proposal-specific motion tokens resolve to canonical tokens (computed-
   style probe in test).
8. Under `prefers-reduced-motion: reduce`: all new transitions collapse to
   0ms; state changes still observable (chip appears, error announced,
   "Done." renders).
9. No animated width/height/top/left/margin/padding introduced. Confirm in
   PR description.
10. Visual diff at rest is identical on every modified surface.
11. No leaked rAF frames or timers (verified by unmount tests on
    SuccessSettle, RegionFlash, ActiveRail, useTweenedNumber,
    useFlashOnChange).

# Required validation commands
cd my-app && pnpm install
cd my-app && pnpm typecheck
cd my-app && pnpm lint
cd my-app && pnpm test
cd my-app && pnpm exec playwright test motion

# Required output format
- Single PR diff against the current branch.
- PR body containing:
    ## Summary
    - 4 bullets: settle, flash, error-contour, active-rail.
    ## Pre-resolved decisions
    - restate A/B/C/D and how each was implemented.
    ## Integrations
    - table: surface → primitive → trigger.
    ## Token migration
    - table: proposal-specific token → canonical token it now aliases.
    ## Test plan
    - markdown checklist matching Acceptance criteria 1–11.
    ## No layout-thrash audit
    - explicit confirmation no width/height/top/left/margin/padding was
      added to any transition or animation.
    ## Non-goals
    - bullets matching the "Do NOT change" list.
```

# PR3 — Streaming, Modals, Diff-Reveal, Editor↔Preview Sync

## Context

PR1: tokens + breathing dot + stage text + activity hook.  
PR2: settle, region flash, error contour, active rail + integrations.  
PR3 picks up the remaining audit items that meaningfully affect the user's mental model: how generated text appears, how proposed edits are reviewed, how the editor and preview stay in sync, and how overlays open/close. Also lands the lint rule that locks the no-layout-thrash invariant in place.

## Goal

Ship chunked text streaming with a terracotta caret, a `diff-reveal` primitive for AI-proposed edits, the editor↔preview gutter marker + debounced flash, and migrate modal/drawer/toast motion onto canonical tokens. Lock the system in with a stylelint rule banning animated layout properties.

## Scope

### Files to add

- `my-app/src/components/ai/StreamingText.tsx` — renders streamed text in chunks. Accepts a stream (`AsyncIterable<string>` or a controlled `chunks: string[]` prop). Each chunk fades in 80ms; a 1px terracotta caret blinks at the tail (CSS-only, opacity keyframe, no shape change). On stream end, caret removes. `aria-live="polite"` on the wrapper, throttled to ≥1500ms via `useThrottledAnnouncer`.
- `my-app/src/components/motion/DiffReveal.tsx` — wraps a region containing `{ before, after }` segments. Insertions: terracotta underline + faint terracotta bg. Deletions: strikethrough at 0.5 opacity. Replacements: `before` fades out 200ms, `after` fades in 200ms with 40ms delay, with the _measured_ outgoing height pinned during the swap to prevent reflow. Accept-all reveals all changes simultaneously (no stagger).
- `my-app/src/components/editor/PreviewGutterMarker.tsx` — a 2px terracotta marker in the preview's right gutter. Subscribes to a shared scroll/active-section signal via a new context. Translates (no fade), 80ms transition, throttled via `requestAnimationFrame`.
- `my-app/src/context/EditorSyncContext.tsx` — exposes `{ activeSectionId, setActiveSectionId, hoveredEditorSectionId, setHoveredEditorSectionId }`. Editor writes; preview reads. Replaces any ad-hoc prop drilling for hover sync.
- `my-app/src/hooks/useThrottledAnnouncer.ts` — utility for `aria-live` throttling, extracted from PR1's StageText (StageText migrates to use it). Public signature: `(message: string | null, minIntervalMs?: number) => void` writing to a hidden live-region the hook owns.
- `my-app/src/hooks/useStreamChunks.ts` — adapts an `AsyncIterable<string>` (server stream) into a React state of accumulated chunks. Cancels on unmount via `AbortController`. Batches updates with `requestAnimationFrame`.
- `tools/stylelint/no-animated-layout-properties.js` — custom stylelint rule.
- Test files mirroring each.

### Files to modify

- `my-app/src/styles/foundation.css` — add `.tw-streaming-caret`, `.tw-diff-insert`, `.tw-diff-delete`, `.tw-diff-replace`, `.tw-gutter-marker`. Add `--motion-caret-blink: 1000ms`. Migrate modal/drawer/toast classes to canonical tokens (alias-only — values unchanged).
- Modal / Drawer / Popover components (`components/ui/{Modal,Drawer,Popover,Toast}`) — replace any literal duration/easing values with `var(--motion-*)`. Backdrop blur capped at `--motion-blur-sm`. Toast slide is slide-only (no bounce — verify and remove any overshoot easing).
- Proposal generation streaming surface — replace whatever currently renders generated text with `<StreamingText />`. The completion settle from PR2 still fires.
- Proposal "tone change" / "refine" flow — render proposed edits via `<DiffReveal />`. Accept/Reject/Insert actions emit `updated-region-flash` (PR2 primitive) on the affected region.
- Editor and Preview shells — wrap with `<EditorSyncContext.Provider />`. Editor section hover writes `hoveredEditorSectionId`; Preview reads it and applies the existing 1px terracotta left-border (140ms) on the matching region. Editor scroll position drives `activeSectionId`; Preview gutter marker reflects it.
- `StageText.tsx` — refactor to consume `useThrottledAnnouncer` instead of its inline throttle (no behavior change; deduplicates logic).
- `package.json` + `.stylelintrc` — register the custom rule and turn it on at `error` level for `my-app/src/**/*.css` and styled JSX/CSS-in-JS template literals if applicable.

### Primitives implemented

`streaming-text` (with caret), `diff-reveal`, `gutter-marker`. Modal/drawer/toast become token-compliant rather than visually changed.

### Real product integrations

1. Proposal generation streaming → `<StreamingText />`.
2. Proposal tone change / refinement → `<DiffReveal />` + region flash on accept.
3. Editor↔preview hover sync → context + existing border treatment.
4. Editor↔preview scroll sync → `<PreviewGutterMarker />`.
5. Modals, drawers, popovers, toasts → token migration only.

### Tests

- Unit: `useStreamChunks` accumulates chunks across rAF batches, aborts on unmount, surfaces stream errors.
- Unit: `useThrottledAnnouncer` writes at most once per interval, coalesces rapid writes to the latest message.
- Unit: `StreamingText` renders chunks, caret present mid-stream, caret removed on stream end, `aria-live` polite + throttled.
- Unit: `DiffReveal` pins height during replacement (mock `getBoundingClientRect`), no reflow during swap, accept-all renders all changes without stagger.
- Unit: `PreviewGutterMarker` translates on `activeSectionId` change, throttled to one update per frame, no fade.
- Unit: `EditorSyncContext` updates propagate; default values do not crash consumers outside provider (graceful no-op).
- CSS: stylelint rule blocks `transition: width 200ms` / `animation: ... height` / `top` / `left` / `margin` / `padding`; allows `transform` and `opacity`. Self-test fixtures.
- Playwright: streaming surface — assert text grows in chunks, caret visible mid-stream, gone after. Diff-reveal — accept inserts new text and triggers region flash. Editor hover → preview border appears. Scroll editor → gutter marker translates. Modal open/close uses canonical durations (computed style probe). All under `reducedMotion: 'reduce'` — text appears in larger paragraph chunks, no caret blink, gutter marker snaps.
- Regression: visual diff at rest for every modal/drawer/toast surface.

### Explicit non-goals

- No deletion of legacy aliases yet (separate cleanup PR after migration is verified in production).
- No change to the proposal generation API contract or stream format.
- No reordering or restructuring of editor/preview DOM beyond adding the provider and the gutter marker mount point.
- No source-reading proof animation (parked permanently).
- No favicon, no route transitions.
- No new features in editor, jobs, CV, or export.
- No mass refactor of one-off transitions in chrome — the lint rule will surface them; fix in a follow-up sweep.

## Acceptance criteria

1. Streaming text renders in chunks (server stream boundaries, not client re-chunking) with a 1px terracotta caret that appears mid-stream and disappears at stream end. `aria-live="polite"`, throttled to ≥1500ms.
2. Diff-reveal pins outgoing height during replacement; no measurable layout shift during the swap (Playwright `cls` probe stays at 0 across the diff). Accept-all reveals all changes simultaneously, no stagger.
3. Editor hover writes to context; preview reflects via the existing 1px terracotta border within 140ms. Hover-out reverses.
4. Editor scroll updates `activeSectionId`; preview gutter marker translates within one frame, throttled, no fade.
5. Modal, drawer, popover, and toast components consume canonical motion tokens; computed-style probes confirm. No visual diff at rest. Toast has zero overshoot.
6. Stylelint rule errors on any new `transition` or `animation` declaration touching `width|height|top|left|right|bottom|margin|padding`. Existing offenders, if any, are listed in the PR body with follow-up issues filed (not fixed in this PR).
7. Under `prefers-reduced-motion: reduce`: chunks render without caret blink in larger groupings; diff swap is instant (no fade); gutter marker snaps; modal/drawer transitions collapse to 0ms; state remains observable.
8. PR1 + PR2 behavior is unchanged. Breathing dot, stage text, settle, region flash, error contour, active rail all still work.
9. `pnpm typecheck`, `pnpm lint`, `pnpm stylelint`, `pnpm test`, `pnpm exec playwright test motion` all pass.
10. No leaked rAF frames, abort controllers, or timers — verified by unmount tests on `useStreamChunks`, `StreamingText`, `DiffReveal`, `PreviewGutterMarker`.

## Final Codex prompt (PR3)

```
# ContextTwoweeks.ai motion system, PR3. Already shipped:- PR1: canonical `--motion-*` tokens + legacy aliases, `useReducedMotion`,  `useAiActivity` + `<AiActivityProvider />`, `<BreathingDot />` (in Logo,  forwardRef), `<StageText />` (proposal generation).- PR2: `<SuccessSettle />`, `<RegionFlash />`, `<ErrorContour />`,  `<ActiveRail />`, `useTweenedNumber`, `useFlashOnChange`. Wired into  proposal completion/failure, jobs match score, CV parsing errors,  sidebar + tab navigation. Proposal-specific tokens aliased to canonical.This PR adds streaming text, diff-reveal, editor↔preview sync, modal/drawer/toast token migration, and a stylelint rule that locks the no-animated-layout-properties invariant.# Pre-resolved decisions (do not deviate)A. Chunk source: chunks come from the server stream — DO NOT re-chunk on the   client. `<StreamingText />` accepts either an `AsyncIterable<string>` or   a controlled `chunks: string[]` prop (caller's choice).B. Caret: 1px solid terracotta vertical bar, height matching the line-box,   opacity keyframe between 1.0 and 0.4 over `--motion-caret-blink`   (1000ms). No shape morph. Removed entirely on stream end (no fade-out   needed; the caret is functional, not decorative).C. DiffReveal anti-reflow: measure outgoing element via   `getBoundingClientRect().height` BEFORE removing it, set the wrapper's   `min-height` to that pinned value, perform the swap, release `min-height`   on the next rAF after the incoming element settles.D. Editor↔preview sync state: lives in a new `EditorSyncContext`, NOT in   `useAiActivity` or any global store. Editor is the only writer for   hover/scroll; preview is the only reader. Default context value is a   no-op shape so consumers outside the provider don't crash.E. Stylelint rule scope: the rule fires on `transition-property`,   `transition` shorthand, `animation-name`, `animation` shorthand, and   `@keyframes` blocks. Banned properties: `width`, `height`, `top`,   `left`, `right`, `bottom`, `margin`, `margin-*`, `padding`, `padding-*`,   `inset`, `inset-*`. Allowed: `transform`, `opacity`, `clip-path`,   `filter` (cap on backdrop blur enforced separately by review).F. Existing layout-property offenders: do NOT fix in this PR. Run the rule,   list every violation in the PR body, file follow-up issues. PR3 only   prevents NEW violations.# Scope1. `my-app/src/hooks/useThrottledAnnouncer.ts`:     - signature: `(message: string | null, minIntervalMs?: number) => void`       (default 1500)     - hook owns a hidden `aria-live="polite" aria-atomic="false"` element       appended to body once     - coalesces rapid writes to the latest message     - cleanup on unmount (removes the live region if it was the last user)2. Refactor `<StageText />` to consume `useThrottledAnnouncer`. No external   behavior change.3. `my-app/src/hooks/useStreamChunks.ts`:     - signature: `(stream: AsyncIterable<string> | null) => { chunks:       string[]; done: boolean; error: Error | null }`     - batches state updates with `requestAnimationFrame`     - cancels via `AbortController` on unmount or stream change     - surfaces stream errors4. `my-app/src/components/ai/StreamingText.tsx`:     - props: `{ stream?: AsyncIterable<string>; chunks?: string[];       done?: boolean }` — exactly one of `stream` or `chunks` required     - renders accumulated chunks; each new chunk wrapped in a span that       fades in 80ms via CSS class `tw-stream-chunk`     - 1px terracotta caret appended at the tail while not done       (decision B); removed when done     - wrapper has `aria-live="polite"`; uses `useThrottledAnnouncer` to       announce the latest accumulated text at ≥1500ms intervals     - reduced motion: chunks appear without fade; caret static (no blink);       announcer interval unchanged5. `my-app/src/components/motion/DiffReveal.tsx`:     - props: `{ segments: Array<{ kind: 'unchanged' | 'insert' | 'delete' |       'replace'; before?: string; after?: string }>; mode: 'preview' |       'accepted' }`     - `preview` mode: insertions show with `.tw-diff-insert` underline +       faint bg; deletions with `.tw-diff-delete` strikethrough + 0.5       opacity; replacements show both stacked (or inline per segment),       awaiting accept     - `accept` transition: when `mode` flips to `accepted`, perform the       replacement swap per decision C: pin height, fade out before       (200ms), fade in after (200ms, 40ms delay), release height on next       rAF after settle     - all changes reveal simultaneously on accept-all (no stagger)     - reduced motion: swap is instant, no fade, height pin still applied       to prevent flash6. `my-app/src/context/EditorSyncContext.tsx`:     - exposes `{ activeSectionId: string | null; setActiveSectionId;        hoveredEditorSectionId: string | null; setHoveredEditorSectionId }`     - default value is no-op shape; consumers outside provider get       `null` reads and silently-ignored writes (no throw)     - `useEditorSync()` selector hook7. `my-app/src/components/editor/PreviewGutterMarker.tsx`:     - reads `activeSectionId` from `useEditorSync`     - finds `[data-preview-section="<id>"]` within the preview container     - sets `transform: translateY(<measured offset>)` on the marker     - 80ms `transition: transform var(--motion-duration-micro)       var(--motion-ease-standard)`     - throttled to one update per `requestAnimationFrame`     - `ResizeObserver` on preview container re-measures     - reduced motion: transition collapses to 0ms (snaps)     - aria-hidden (purely visual)8. Wire integrations:     - Proposal generation: replace whatever currently renders the       streaming generated text with `<StreamingText />`. PR2's       `<SuccessSettle />` still fires on completion.     - Proposal tone change / refine: render proposed edits via       `<DiffReveal mode="preview" />`. On accept, transition to       `mode="accepted"` AND emit a `<RegionFlash />` (PR2) on the       affected region.     - Editor + Preview shells: wrap the closest common ancestor with       `<EditorSyncContext.Provider />`. Editor section onMouseEnter/Leave       writes `hoveredEditorSectionId`; Preview reads it and applies the       existing 1px terracotta left-border (140ms) on the matching region.     - Editor scroll: update `activeSectionId` (debounce 80ms or use       IntersectionObserver — pick one; document the choice). Preview       mounts `<PreviewGutterMarker />`.     - Modals, drawers, popovers, toasts in `components/ui/`: replace       literal duration/easing values with `var(--motion-*)` tokens.       Backdrop blur cap: `var(--motion-blur-sm)`. Toast: confirm slide-only       (remove any overshoot easing if present).9. `tools/stylelint/no-animated-layout-properties.js`:     - implements the rule per decision E     - includes self-test fixtures under `tools/stylelint/__tests__/`     - register in `.stylelintrc`; level: `error`     - `pnpm stylelint` script wired in `package.json`     - run the rule, capture all current violations, paste verbatim into       PR body under "Existing offenders (follow-up)". Do NOT fix them       (decision F). File one GitHub issue per offender file (or a single       umbrella issue with the list).10. Extend `my-app/src/styles/foundation.css`:     - add `--motion-caret-blink: 1000ms`     - add `.tw-stream-chunk` (opacity fade-in 80ms)     - add `.tw-streaming-caret` (1px terracotta bar, opacity keyframe)     - add `.tw-diff-insert`, `.tw-diff-delete`, `.tw-diff-replace`     - add `.tw-gutter-marker` (2px terracotta, transition transform)     - reduced-motion block: zero out new durations and the caret blink# Do NOT change- Token VALUES (only ADD new + ALIAS existing).- Generation/parsing/scoring/export business logic.- The proposal generation API contract or server stream format.- favicon, route transitions.- Editor/Preview DOM structure beyond adding provider + gutter mount point.- PR1/PR2 components' external behavior (StageText refactor is  internal-only).- themes.css unless strictly required.- Existing layout-property offenders (decision F).# Constraints- CSS keyframes / transitions only. No framer-motion. JS animation limited  to `useStreamChunks` (rAF batching), `PreviewGutterMarker` (rAF throttle),  and `DiffReveal` height pinning.- Animate `transform` and `opacity` only. The new stylelint rule MUST pass  on every file this PR adds or modifies.- Honor `prefers-reduced-motion: reduce` everywhere.- All AbortControllers, ResizeObservers, rAF handles, and timers cancel on  unmount.- TypeScript strict; no `any`.- `aria-live` regions are throttled. Never `assertive`.# Acceptance criteria1. `pnpm typecheck`, `pnpm lint`, `pnpm stylelint`, `pnpm test`,   `pnpm exec playwright test motion` all pass.2. Streaming text renders chunks from server boundaries (decision A) with   1px terracotta caret (decision B); caret gone at stream end.3. DiffReveal swap pins height (decision C); Playwright CLS probe stays   at 0 during accept transition.4. Editor hover writes context; preview border appears within 140ms.   Hover-out reverses.5. Editor scroll updates activeSectionId; gutter marker translates within   one frame; throttled; no fade.6. Modal, drawer, popover, toast use canonical tokens (computed-style   probe). No visual diff at rest. Toast has no overshoot.7. Stylelint rule errors on banned properties in `transition`/`animation`/   `@keyframes` (decision E); existing offenders listed in PR body   (decision F); zero NEW violations introduced.8. Reduced motion: chunks render without caret blink; diff swap instant   (still height-pinned); gutter marker snaps; overlay transitions 0ms;   all state changes still observable.9. PR1 + PR2 behavior unchanged: breathing dot, stage text, settle, region   flash, error contour, active rail still work.10. No leaked rAF frames, abort controllers, ResizeObservers, or timers    (verified by unmount tests).11. Visual diff at rest is identical for every modal/drawer/popover/toast.# Required validation commandscd my-app && pnpm installcd my-app && pnpm typecheckcd my-app && pnpm lintcd my-app && pnpm stylelintcd my-app && pnpm testcd my-app && pnpm exec playwright test motion# Required output format- Single PR diff against the current branch.- PR body containing:    ## Summary    - 4 bullets: streaming text, diff-reveal, editor↔preview sync,      overlay token migration + lint rule.    ## Pre-resolved decisions    - restate A/B/C/D/E/F and how each was implemented.    ## Integrations    - table: surface → primitive → trigger.    ## Existing offenders (follow-up)    - verbatim stylelint output for any pre-existing layout-property      animations; one issue link per file or an umbrella issue link.    ## Test plan    - markdown checklist matching Acceptance criteria 1–11.    ## No layout-thrash audit    - explicit confirmation no NEW transition or animation touches      width/height/top/left/right/bottom/margin/padding/inset.    ## Non-goals    - bullets matching the "Do NOT change" list.
```

After PR3 ships and bakes in production, the natural follow-ups are: (a) sweep the existing layout-property offenders surfaced by the stylelint rule, and (b) retire legacy token aliases (`--duration-*`, `--dur-1..5`, `--motion-*-duration`) once usage hits zero. Both are cleanup PRs, not motion PRs.