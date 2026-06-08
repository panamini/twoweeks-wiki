1. Find screenshot of component or screen I want on mobbin, Pinterest, dribbble and save it.
    
2. Ask ChatGPT pro to make JSON style guide 1:1 pixel perfect conducting several iterations minimum of 3 over the screenshot until perfection.
    
3. Provide screenshot and style guide json to AI with tech stack I.e. React Native with nativewind and expo etc.
    
4. Describe what you want the components in the screenshot to do i.e. buttons etc.
    
5. Repeat multiple times.
    

Here is one of the prompts I actually use for reference you can try out that’s given me good results:

# Pixel-Perfect UI Component Cloning Prompt (Zero-Deviation)

## Objective

Clone the provided screenshot as a **fully functional UI component** representing an **agent workflow** with **absolute 1:1 fidelity**. The final output must be visually, structurally, and behaviorally indistinguishable from the original screenshot.

The screenshot is the **Single Source of Truth (SSOT)**. No creative interpretation, stylistic adjustment, approximation, or optimization is permitted.

---

## Core Constraints (Non-Negotiable)

- Deviation tolerance: **0px**
    
- No inferred design patterns, defaults, or conventions
    
- No added, removed, resized, or re-styled elements
    
- No font, icon, spacing, or color substitution unless verified by pixel measurement
    
- The reconstructed component must overlay perfectly on the original with **no visible difference**
    

---

## Mandatory Two-Pass Workflow

### Pass 1 — Visual Decomposition & Measurement (No UI Output)

Before generating any UI, perform a full analytical breakdown of the screenshot.

#### Required Outputs:

1. **Hierarchical Element Tree**
    
    - Parent → child relationships
        
    - Z-index / stacking order
        
2. **Bounding Boxes**
    
    - Exact width & height (px)
        
    - Absolute x/y positioning
        
3. **Spacing Metrics**
    
    - Padding and margin for every side (px)
        
    - Inter-element gaps (px)
        
4. **Typography Analysis**
    
    - Font family (or closest metric match if unknown)
        
    - Font weight (numeric)
        
    - Font size (px)
        
    - Line height (px)
        
    - Letter spacing
        
    - Text color (HEX/RGBA)
        
5. **Color System**
    
    - Backgrounds, borders, text, dividers
        
    - Gradients (direction, stops, opacity)
        
    - Overlays and transparency layers
        
6. **Borders & Radius**
    
    - Border width (px)
        
    - Border color
        
    - Corner radius (px)
        
7. **Shadows & Depth**
    
    - Offset X/Y (px)
        
    - Blur radius
        
    - Spread
        
    - Opacity
        
8. **Icons & Glyphs**
    
    - Icon type and shape
        
    - Stroke width
        
    - Fill/stroke color
        
    - Exact size (px)
        
    - Position relative to text and containers
        
9. **Connectivity & Flow**
    
    - Lines, arrows, node connections
        
    - Stroke width, color, curvature, endpoints
        
10. **Opacity & Layering**
    
    - Alpha values
        
    - Elevation hierarchy
        

> If a value is not explicitly visible, infer it **only by pixel measurement**, never by convention or best practice.

---

### Pass 2 — Exact Reconstruction

Using **only** the measured values from Pass 1, reconstruct the component.

#### Reconstruction Rules:

- Use absolute pixel units for all dimensions
    
- Preserve exact layout hierarchy and ordering
    
- Lock fonts, icons, and glyph metrics precisely
    
- Reproduce all interaction states if visible (hover, active, focus)
    
- No responsiveness unless explicitly shown in the screenshot
    
- No auto-layout guessing (e.g., no `space-between` assumptions)
    

---

## Font & Icon Accuracy Enforcement

- Fonts must match glyph width, weight, and optical size
    
- If the exact font cannot be identified, use the closest metric-compatible substitute with identical character widths
    
- Icons must match stroke cap, joins, weight, and alignment exactly
    
- No “similar” or “close enough” substitutions allowed
    

---

## Deterministic Layout Rules

- Fixed positioning where visible
    
- Explicit grid tracks only if a grid is visually present
    
- No adaptive or fluid behavior unless proven by the image
    

---

## Validation & Correction Loop (Required)

After reconstruction:

1. Overlay the generated component directly on top of the original screenshot
    
2. Compare using difference or opacity blending
    
3. Identify **any** visual mismatch (even sub-pixel)
    
4. Correct and repeat until no differences remain
    

---

## Final Success Criteria

The output is considered correct **only if**:

- Overlay comparison shows zero visible difference
    
- All visual, structural, and functional aspects match exactly
    
- The component is indistinguishable from the original at 100% scale
    

---

## Prohibited Actions

- Creative enhancement
    
- Design “cleanup”
    
- Modernization
    
- Accessibility adjustments unless visible
    
- Performance or responsiveness optimization
    

---

## End Goal

Produce a UI component that, when placed over the original screenshot, is **visually indistinguishable at the pixel level**, with perfect alignment, typography, color, spacing, depth, and connectivity.