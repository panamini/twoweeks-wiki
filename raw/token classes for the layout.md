# ADR: Canonical Document Token Contract

## Decision

Adopt a single internal token contract with four ownership classes:

- geometry
- flow
- appearance
- runtime

## Reasoning

- Preview, export CSS, and DOCX need one source of truth without breaking existing output surfaces.
- Runtime fit and measurement helpers must remain local to preview.
- Proposal voice overlays affect layout behavior and therefore belong to flow, not appearance.

## Locked Shapes

- geometry.page.liveArea.widthMm
- geometry.page.liveArea.heightMm
- flow.type.<role>.resolvedTrackingEm

## Additional Rules

- appearance.decor is non-structural. It may hold renderer-safe visual recipes such as borders, radii, gradients, and shadows, but it may not own spacing, sizing, reading measure, or anything intended to change pagination.
- style.ts delegates to the canonical appearance resolver. It remains a style selection/input module, not an independent theme authority.
- Primary font choice comes from canonical appearance.font.*. Serializer-level fallback stacks are allowed only as platform literals and may not override canonical font selection.
- Serializer-required platform literals such as transparent, currentColor, DOCX-safe keywords, and generic font-family tails remain allowed when they serve platform compatibility rather than design authorship.

## Consequences

- Existing output var names stay stable.
- DOCX moves from fixed constants to canonical token resolution.
- Runtime vars remain excluded from persisted/exported canonical snapshots.