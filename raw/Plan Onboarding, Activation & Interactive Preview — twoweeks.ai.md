---
aliases:
  - "Plan: Onboarding"
  - Activation & Interactive Preview — twoweeks.ai
---


## Context

Parser is functional (Cycle 1 item 1 ✅). The wiki product-roadmap defines remaining Cycle 1 (P0) items:
- Quick-start guided path
- First-run onboarding system
- Preview ↔ editor interactive linking

User is asking which of the three open items to prioritize and whether to fortify brand voice first or build onboarding first.

---

## Audit Findings

### App current state (dasti)
- **No onboarding exists** — first-time users land directly in CVForge with an auto-generated placeholder CV
- **No quick-start funnel** — cold traffic hits the full editor immediately (sub-optimal conversion)
- **No preview ↔ editor interaction** — live preview (Verbati) renders in real time but has no bidirectional click behavior
- **Brand voice: complete** — the brand bible is fully specified (staccato, corporate noir, 4 copy rules, microcopy examples, anti-IA rule). **No need to fortify before building** — apply it directly

### What the wiki says to do (P0 cycle)
1. ~~Parser cleanup~~ ✅ done
2. Quick-start guided path
3. Preview ↔ editor linking
4. First-run onboarding system (listed as P1, depends on quick-start path)

---

## Order Recommendation

**The interactive preview ↔ editor linking should come first.**

Why:
- It is the single "wow" moment that makes the editor feel like a premium 2026 tool (Figma/Notion-class interaction)
- It is the strongest retention and conversion signal inside the editor
- It makes the quick-start path's payoff ("see your resume live, click it to edit") credible
- It can be shipped in isolation, no dependency on funnel or onboarding
- The wiki explicitly lists it as P0, on par with quick-start

Then quick-start path, then first-run onboarding layer.

**Brand voice: don't touch it first.** It is already solid. Write the onboarding microcopy directly using the brand bible rules.

---

## Three Workstreams (in execution order)

### 1. Interactive Preview ↔ Editor Linking (do first)
**What**: When user clicks a section in the Verbati live preview → CVForge editor focuses that section and opens the edit modal. When user hovers/edits a section in editor → the corresponding block in preview highlights.

**Why it's elite 2026 UX**: Bidirectional spatial awareness. The preview is no longer read-only chrome — it becomes an input surface. This reduces cognitive load ("where do I edit this?") and creates a tactile loop that is deeply satisfying and builds trust in the product.

**Scope**:
- Click on profile block in preview → scroll to + highlight Profile section in editor
- Click on an experience block → open the relevant experience entry edit modal
- Click on skills/education → focus those sections
- Editor section active state → send highlight signal to preview (already partially exists via style binding)

**Files involved**:
- `src/pages/CvForge.tsx` — orchestrates editor + preview, holds workspace state
- `src/features/verbati/VerbatiCvPreviewPanel.tsx` — live preview panel
- `src/features/verbati/VerbatiResumePreview.tsx` — renders sections, needs click handlers
- `src/components/cv-editor/` — editor sections, need scroll-to-section + open-modal API

**Technical approach**:
- Add `data-section-id` attributes to preview section wrappers
- Lift a `focusSection(sectionId)` callback from CvForge down into preview panel
- In editor: expose `scrollToSection(id)` + `openModal(sectionId)` refs
- Use a shared `activeSectionId` state in CvForge to sync both directions
- Cursor: pointer on preview sections; subtle hover highlight (2px left border or opacity lift)

---

### 2. Quick-Start Guided Path (do second)
**What**: Before landing in the full editor, new/cold users go through a short 3-step flow:
1. "What do you want to create?" (Resume / Cover Letter)
2. Import CV (PDF/text/LinkedIn) OR Start fresh
3. Tone calibration (Auto / Natural / Formal / Warm) → "Generate first draft" CTA
→ lands in CVForge editor with real content

**Why**: Kills the blank-slate conversion problem. User arrives in editor with *their* data already there, editor feels immediately legible. Time to First Draft ↓.

**Scope**:
- Triggered only on first session (no CV content yet / fresh account)
- 3 screens max, no modal tour
- Microcopy in brand voice: "Drop your CV. We'll handle the rest." / "What are you building today?" / "Finish it."
- Skip option always visible ("Go straight to editor →")
- After completion: lands in CVForge with content already parsed/populated

**Files involved**:
- New component: `src/components/onboarding/QuickStartFlow.tsx` (3-step wizard, stateless screens)
- `src/App.tsx` — gate logic (check `hasMeaningfulCvContent()` from CvLibraryContext, if false + first visit → show quick-start)
- `src/contexts/CvLibraryContext.tsx` — `hasMeaningfulCvContent()` already exists, reuse it
- `src/lib/` or `localStorage` — track `onboarding:quick-start-completed` flag

---

### 3. First-Run Onboarding System (do third, after quick-start)
**What**: A stack of complementary light layers, NOT a tooltip tour:
- **Session checklist** (5 steps): import resume → add job → generate first draft → improve one section → export (dismissible, shown in sidebar or floating card)
- **Contextual nudges**: one-liners at key moments ("Click any section to edit" / "Select text to rewrite with AI")
- **1-2 spotlight moments**: only for: (a) first IA rewrite action, (b) first export
- **Empty-state education**: sections with no content teach the next action inline

**Microcopy examples** (brand bible applied):
- Checklist header: "Five things. Then you're done."
- Empty experience state: "Nothing here yet. Add your last role."
- First IA action spotlight: "Try it. Select any sentence."
- After export: "Done. Go outside."

**Files involved**:
- New component: `src/components/onboarding/FirstRunChecklist.tsx`
- New component: `src/components/onboarding/ContextualNudge.tsx`
- Empty state updates in `src/components/cv-editor/` sections
- `src/contexts/CvLibraryContext.tsx` — track checklist completion state

---

## Brand Voice Verdict

**Solid. Do not rewrite before building.**

The brand bible covers:
- Staccato sentence rules ✓
- Corporate noir humor tone ✓
- Specific microcopy examples (placeholder, empty state, button, success, error) ✓
- Anti-IA copy rule ✓
- Copy dos/don'ts table ✓

Apply it directly when writing onboarding microcopy. The only risk is inconsistency *across* surfaces — enforce the rules during implementation (short phrases, direct verbs, no AI announcements, dry > friendly).

---

## 2026 Elite UI/UX Principles (what this plan delivers)

| Principle | Delivered by |
|-----------|-------------|
| Bidirectional spatial UI (preview = input surface) | Workstream 1 |
| Zero-to-value < 60 seconds | Workstream 2 |
| Progressive disclosure (teach at the moment of need) | Workstream 3 |
| Empty states as active teachers | Workstream 3 |
| No tooltip tours (2023 pattern, now anti-pattern) | Workstreams 2+3 |
| Micro-delight on key actions (first draft, first export) | Workstream 3 spotlights |
| Job-aware AI (tone calibration as UX gate) | Workstream 2 step 3 |

---

## KPIs (what moves after shipping)
- Time to First Draft ↓ (quick-start path)
- Visitor → First Draft Rate ↑ (quick-start path)
- Paywall Conversion ↑ (quick-start drives intent)
- D7 Retention ↑ (interactive preview creates stickiness)
- Export Initiation Rate ↑ (checklist completion drives it)

---

## What is NOT in scope here
- Import recovery layer (parser UX confidence scoring) — next cycle
- Template switcher — next cycle
- Document health/quality layer — next cycle
- Jobs as first-class object — next cycle

---

## Verification
- Start dev server: `cd my-app && npm run dev`
- Test interactive preview: click experience section in preview → editor scrolls to that section + modal opens
- Test quick-start: clear localStorage, sign in fresh → quick-start flow appears → complete it → land in editor with data
- Test checklist: fresh user → checklist visible → complete each step → checklist dismisses
- Regression check: existing CVForge editor, proposal flow, style presets all still functional