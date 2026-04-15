es — the three token classes were:

## 1. Geometry tokens

These define the **hard page/frame math**.

They cover things like:

- page size
- page margins
- printable area
- sidebar width
- gutter width
- main column width
- Robial step units like `17mm`, `18mm`, `8.5mm`

Think:

**the fixed grid and page skeleton**

---

## 2. Flow tokens

These define **how content moves inside the frame**.

They cover things like:

- font sizes
- line heights
- paragraph spacing
- section spacing
- entry-head spacing
- list spacing
- metadata gaps
- chip/tag metrics
- keep-with-next / break behavior
- block cadence
- column/content rhythm

Think:

**content rhythm, wrapping, spacing, and pagination behavior**

---

## 3. Appearance tokens

These define **how it looks without changing layout behavior**.

They cover things like:

- heading/body font family choice
- ink color
- accent color
- rule color
- background / paper tone
- sidebar / rail tint
- border color
- emphasis tone
- restrained tracking
- tag fill / surface styling

Think:

**visual identity only**

---

## The important rule

### Geometry

should control the **grid/frame**

### Flow

should control the **content rhythm and structure inside the frame**

### Appearance

should control the **style/look**

---

## In your export case

### Geometry tokens

for:

- Robial page math
- export-safe grid
- allowed column families

### Flow tokens

for:

- one-column ATS rhythm
- styled spacing cadence
- hierarchy spacing
- wrap/page-break behavior

### Appearance tokens

for:

- selected font feel
- palette
- rule/rail treatment
- layout/template identity cues

---

## The key invariant

What I told you before was basically:

- **Geometry = where things can live**
- **Flow = how text/content behaves there**
- **Appearance = how it visually reads**

And the classic safety rule was:

> appearance should never secretly change geometry or flow

That was the clean model.