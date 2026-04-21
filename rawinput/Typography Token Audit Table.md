

| Family | Source of truth | Serialized to runtime vars | Used in active workshop renderer | Reflected in planner metrics | If not, planner fallback |
|---|---|---|---|---|---|
| Body font family | `appearance.font.body.family` from `buildVerbatiThemeVars` via preview appearance in [style.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/style.ts#L263) and [documentAppearance.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentAppearance.ts#L550) | Yes: `--body-font`, `--font-body-family` in [documentTokenSerializers.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenSerializers.ts#L1076) and [documentAppearance.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentAppearance.ts#L550) | Yes: page root uses `var(--body-font, var(--font-body-family))` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L709) | No | Generic chars-per-line heuristic from width and line-height only in [resumePagination.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/resume/resumePagination.ts#L528) |
| Body font size | `flow.type.body.sizePt` from `normalizeResumePreviewTokens` in [documentTokenNormalizer.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenNormalizer.ts#L373) | Yes: `--text-body-size` in [documentTokenSerializers.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenSerializers.ts#L152) | Yes: body paragraphs use `var(--text-body-size)` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L111) and [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L274) | Partially | Converted to line height only via `resolveTextLineHeightMm`; width model ignores actual font width in [resumePagination.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/resume/resumePagination.ts#L543) |
| Body line-height | `flow.type.body.lineHeight` in [documentTokenNormalizer.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenNormalizer.ts#L375) | Yes: `--text-body-line` in [documentTokenSerializers.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenSerializers.ts#L161) | Yes in body blocks in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L112) | Yes | N/A |
| Body letter-spacing | Canonical field exists as `flow.type.body.resolvedTrackingEm` in [documentTokens.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokens.ts#L8), but resume preview normalizer does not set it | No for resume preview. Only proposal serializer emits letter-spacing in [documentTokenSerializers.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenSerializers.ts#L596) | No body letter-spacing token use in workshop renderer | No | None. Completely unmodeled |
| Heading font family | `appearance.font.heading.family` from theme in [documentAppearance.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentAppearance.ts#L550) | Yes: `--heading-font`, `--font-heading-family` in [documentTokenSerializers.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenSerializers.ts#L1070) | Yes: headings use `var(--heading-font, var(--font-heading-family))` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L42) and [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L331) | No | Generic line-height and chars-per-line heuristic only |
| Heading font size | `flow.type.title.sizePt` in [documentTokenNormalizer.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenNormalizer.ts#L369) | Yes: `--text-title-size` in [documentTokenSerializers.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenSerializers.ts#L137) | Yes, but often with hard-coded offsets like `calc(var(--text-title-size) - 0.95mm)` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L43) | Partially | Planner uses title size only to derive a synthetic section header height in [resumePagination.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/resume/resumePagination.ts#L569) |
| Heading line-height | `flow.type.title.lineHeight` in [documentTokenNormalizer.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenNormalizer.ts#L371) | Yes: `--text-title-line` in [documentTokenSerializers.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenSerializers.ts#L146) | Mostly no. Workshop section heading uses hard-coded `1.1`, role heading uses hard-coded `1.25` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L44) and [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L333) | Partially | Planner uses token line-height for section title, but uses hard-coded experience heading line-height multiplier in [resumePagination.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/resume/resumePagination.ts#L573) |
| Heading letter-spacing | Decorative source exists for export appearance in [documentAppearance.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentAppearance.ts#L302) | Not for active workshop preview headings | Renderer hard-codes `0.08em` for section heads and continued labels in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L46) | No | None |
| Heading text-transform | Decorative source exists for export appearance in [documentTokens.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokens.ts#L232) | Not for active workshop preview headings | Renderer hard-codes `uppercase` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L45) | No | None |
| Meta font size | Canonical `flow.type.meta.sizePt` exists and is set in [documentTokenNormalizer.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenNormalizer.ts#L385) | No dedicated preview var for meta size | No. Workshop renderer uses `--text-body-sm-size` for experience meta and metadata values in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L347) | Partially | Planner also uses `bodySmLineHeightMm` for meta rows in [resumePagination.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/resume/resumePagination.ts#L698) |
| Meta line-height | Canonical `flow.type.meta.lineHeight` exists and is set in [documentTokenNormalizer.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenNormalizer.ts#L386) | No dedicated preview var | No. Renderer uses `--text-body-sm-line` | No | `bodySmLineHeightMm` |
| Meta letter-spacing | Decorative source exists only in export decor (`metaLabelLetterSpacing`) in [documentAppearance.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentAppearance.ts#L304) | Not for active workshop preview meta rows | Renderer hard-codes `0.08em` for labels and none for meta values | No | None |
| Skill/tag font family | No workshop skill-specific typography token source; inherits body/root font | No skill-specific font var | No explicit chip font family set; inherits page body font in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L416) | No | Body font inheritance outside planner model |
| Skill/tag font size | Renderer uses `--text-body-sm-size` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L422) | Yes, via body-sm vars | Yes | Partially | Planner estimates skill text with `bodySmLineHeightMm` only in [resumePagination.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/resume/resumePagination.ts#L1424) |
| Skill/tag chip padding | Source of truth should be `flow.component.skill.padInlineMm/padBlockMm` from [documentTokenNormalizer.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenNormalizer.ts#L423) | Not serialized as workshop preview vars | Renderer ignores token and hard-codes `padding: 1.2mm 2.6mm`, `minHeight: 8mm` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L418) | Partially | Planner uses only `skillPadBlockMm` and `skillGapMm`, not inline pad or min height, in [resumePagination.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/resume/resumePagination.ts#L633) |
| Skill/tag wrapping behavior | No token source | No | Renderer uses `display:flex`, `flex-wrap:wrap`, hard-coded gap in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L653) | No real wrap model | Planner treats each skill like independent text-height entries, not true wrapped chips |

B. Typography Values Used By Renderer But Not Planner

Renderer uses, planner does not model:
- Body font family changes via `--body-font` / `--font-body-family`
- Heading font family changes via `--heading-font` / `--font-heading-family`
- All letter-spacing used in workshop page:
  - section heading `0.08em`
  - continued label `0.08em`
  - metadata label `0.08em`
- All heading text transforms:
  - `uppercase` for section titles
  - `uppercase` for continued badges
  - `uppercase` for metadata labels
- Hard-coded heading line heights:
  - section heading `1.1`
  - experience role heading `1.25`
- Hard-coded heading size offsets:
  - `calc(var(--text-title-size) - 0.95mm)`
  - `calc(var(--text-body-size) + 0.2mm)` for role headings
- Meta rows rendered with `bodySm` typography instead of canonical `meta`
- Skill chips:
  - hard-coded `padding: 1.2mm 2.6mm`
  - hard-coded `minHeight: 8mm`
  - hard-coded wrap behavior with `flex-wrap: wrap`
  - hard-coded outer gap `1.6mm`

Two additional concrete inconsistencies:
- The workshop renderer references `--text-label-size` and `--text-label-line` in [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L55) and [ResumeOneColAtsPage.tsx](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/features/verbati/resume/ResumeOneColAtsPage.tsx#L245), but the preview serializer only emits `--text-caption-size` and `--text-caption-line` in [documentTokenSerializers.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/layout/documentTokenSerializers.ts#L182).
- The canonical token model includes `flow.type.meta`, but neither the active workshop preview serializer nor the workshop page uses dedicated meta typography on this path.

C. Acceptable Natural Variation Or Planner Mismatch?

This is a real planner/render mismatch, not just acceptable natural variation.

Why:
- Some variation from different font families is inherently expected.
- But the active workshop planner is not actually font-metric aware. It derives heights from token size/line-height and a generic width heuristic in [resumePagination.ts](/Volumes/video/kay/app/pouraurelien/save/implementation_UI/neyssan/my-app/src/lib/resume/resumePagination.ts#L528).
- The active workshop renderer does use the real font families and several hard-coded typographic treatments that affect wrapping and line count.
- Letter-spacing, text-transform, family width differences, chip inline padding, and chip wrapping are not reflected in planner metrics.
- The planner therefore cannot fully predict font-driven reflow on this path.

So the inconsistency you see across fonts is not just “fonts are different”; it is partly caused by missing typography-token integration.

D. Exact Next Bug To Fix

Single next bug:
- The active workshop planner does not use the same typography contract as the active workshop renderer.

Most exact narrow fix target:
- Align workshop renderer and planner around a shared preview typography contract for section-label/meta/chip text, starting with:
  1. stop using undefined `--text-label-*` vars on the renderer, and
  2. either serialize/use canonical meta and label vars consistently, or make planner and renderer both use the same body-sm/caption roles explicitly.

If you want the highest-value follow-up after this audit, it is:
- make workshop section labels, continued badges, metadata labels, and skill chips consume serialized canonical typography vars, then update planner metrics to use those same roles instead of generic `bodySm` plus heuristics.

Confirmed bottom line:
- This is `2. real planner/render mismatch caused by missing typography-token integration`, not merely acceptable natural variation.