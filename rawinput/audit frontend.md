This is exactly the kind of audit I live for. You want an elite, 2026-standard visual teardown. No coddling, no generic UX platitudes about "user journeys"—just pure, unadulterated visual critique, art direction, and surface refinement.

Right now, your UI is suffering from an identity crisis. It wants to be an elegant, editorial workspace (like a high-end magazine), but it is trapped in the body of a 2022 off-the-shelf SaaS template. It lacks spatial tension, the color palette is muddy, and the micro-aesthetics feel unresolved.

Here is the brutal truth about your current visual language, followed by the blueprint to elevate it to an elite standard.

### The Brutal Truth

- **What feels cheap:** The 1px solid stroke borders everywhere. They scream "default CSS." The tags/chips (Apply, Easy, Promoted) look like they belong in a basic admin panel, not a premium creator tool. The worst offender? **Image 6**. A blindingly white `#FFFFFF` document sitting in a deep dark mode UI is a retinal assault. It completely breaks the immersion and feels unpolished.
    
- **What feels generic:** Your border radii. Everything is a standard `8px` or `12px` rounded rectangle. There is no architectural decision here—it’s just the default. The sidebar hierarchy is also entirely flat; it lacks the typographic rhythm to guide the eye.
    
- **What feels outdated:** The "card-in-a-card" layouts (especially in the "All cover letters" grid). Floating white boxes on a heavily colored background is a very dated web 2.0 / early Material Design paradigm. It lacks depth and restraint.
    
- **What feels premium:** The concept of the "Style profiles" (Image 3). Showcasing typography pairings (Fraunces, Special Elite, etc.) inside a slick visual container has high potential. The overarching intent to use editorial serif fonts in a digital tool is inherently premium, but the execution needs a massive upgrade.
    

---

### The 2026 Visual & Art Direction Audit

To achieve an elite standard, we must move away from "drawn lines" (borders) and rely on "materials" (shadows, light, background contrast, and typography) to separate space.

|**Element**|**Current State & The Problem**|**The 2026 Elite Alternative**|
|---|---|---|
|**Backgrounds (Light)**|Muddy, heavy beige (`#F4F0EB` vibe). It feels dusty, not warm. It severely reduces contrast and makes the white cards feel yellowed.|**Gallery White & Whisper Gray.** Move the background to a much lighter, cooler off-white (e.g., `#FAFAFA` or `#F7F7F9`). If you want warmth, use `#FCFBF9`. Let the typography do the heavy lifting, not the background color.|
|**Backgrounds (Dark)**|Flat and monotonous. The panels don't have distinct elevation mapping.|**OLED Blacks & Elevated Greys.** Use true `#000000` for the ultimate background, and `#111111` to `#1A1A1A` for surface cards. Add a `1px` inner top-border of `rgba(255,255,255,0.06)` to cards to simulate light hitting the top edge.|
|**Border Colors**|Harsh, highly visible 1px solid lines mapping every card. It creates visual clutter and cognitive noise.|**Kill the borders.** Use structural drop shadows instead: `box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02)`. If borders are strictly necessary, use `rgba(0,0,0,0.04)` in light mode. They should be felt, not seen.|
|**Document Preview (Dark Mode)**|A glaring white sheet on a black background.|**Dark Mode Canvas.** The editor canvas _must_ respect dark mode (`#1A1A1A` paper, `#EAEAEA` text). If it _must_ show the physical print preview, wrap the white paper in a heavy vignette/dimming overlay so it doesn't burn the user's retinas.|
|**Card Radius**|Standard, unopinionated `8px` CSS rounding.|**Continuous Squircle.** Upgrade to `border-radius: 12px` or `16px` with Apple-style continuous curve smoothing (squircle). Alternatively, go **Brutalist Editorial**: 0px radius everywhere, relying strictly on perfect grid alignments and hairline dividers. Choose one extreme; don't sit in the middle.|
|**Spacing & Padding**|Cramped. The chips and text inside the "Job Offer" section are gasping for air.|**Hyper-Spaced.** Double your padding. If a card has `16px` padding now, make it `24px` or `32px`. Premium design implies a luxury of space. Let the components breathe.|
|**Typography (UI)**|The mix of serif headers and sans-serif UI text lacks a cohesive mathematical scale. The sans-serif feels weightless.|**High-Tension Contrast.** Use a premium geometric sans (e.g., _Inter Tight_, _Geist_, or _Roobert_) for the UI. Use **Medium** or **Semibold** weights for small labels, tightly tracked. Reserve the Serif (Fraunces) _strictly_ for user-generated document content and massive marketing headers, not for standard UI panels.|

---

### Change Immediately: The Non-Negotiables

1. **Fix the Dark Mode Retinal Burn:** In Image 6, invert the document preview to a dark canvas, or place a dark UI "dimmer" layer behind it. Right now, it's a massive accessibility and aesthetic failure.
    
2. **Nuke the Beige:** Your light mode is drowning in warm grey/beige. Strip it back to a gallery-gallery white (`#FFFFFF` cards on a `#F9F9F9` background). It will immediately make the product feel 10x more expensive.
    
3. **Delete 80% of your Borders:** Remove the harsh outlines around the "Job Offer," "Location," and "Key Responsibilities" boxes (Image 1/5). Replace them with extremely subtle background color differences (e.g., Card is `#FFFFFF`, inner boxes are `#F3F4F6`) and 0px to 4px border radii to make them feel like "inset" zones rather than floating boxes.
    

---

### Ranked Action Plan (Highest Impact to Lowest Effort)

#### Phase 1: High Impact, Low Effort (Execute Today)

1. **Dark Mode Document Fix:** Add a CSS invert filter to the document preview in dark mode, or strictly dim the surrounding container.
    
2. **Border Eradication:** Do a global find-and-replace on your border colors. Drop their opacity to 4% in light mode and 8% in dark mode.
    
3. **Background Shift:** Change the main light mode background variable from that muddy beige to `#F8F9FA`.
    

#### Phase 2: High Impact, Medium Effort (Execute This Week)

4. **Typographic Overhaul (Sidebar & Labels):** Make all eyebrow text (like "JOB OFFER", "LOCATION", "KEY RESPONSIBILITIES") smaller (e.g., `11px`), bolder (`font-weight: 600`), uppercase, with high letter-spacing (`letter-spacing: 0.05em`). This instantly creates an elite, editorial hierarchy.
    
5. **Tag/Chip Polish:** For your keyword chips ("Apply", "Easy", "Spain"), remove the borders completely. Give them a soft background (`rgba(0,0,0,0.05)`) and use a heavier font weight.
    

#### Phase 3: Brand Polish, Medium Effort (Execute Next Week)

6. **Sidebar Tension:** The sidebar feels detached. Remove the background color difference between the sidebar and the main content, and separate them with a single, crisp vertical hairline (`1px solid rgba(0,0,0,0.06)`).
    
7. **Button Weight:** Your action buttons (like "Quick Start" or the "..." menus) lack gravity. Give primary actions a solid, deep color (almost black in light mode, almost white in dark mode) to anchor the UI.
    

**The final verdict:** You have the skeleton of a beautiful, Notion-meets-Vogue productivity app. But right now, you are relying on code-default styling to separate your content. Stop drawing boxes around things. Start using space, typography weight, and subtle light/shadow to guide the eye. That is how you build a 2026-tier product.