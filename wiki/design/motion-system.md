---
title: "Motion System"
category: design
tags: [motion, animation, ai, accessibility, brand]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-27-twoweeks-motion-system, 2026-04-27-motion-system-implementation-hardening]
related: [[design/brand-voice]], [[design/logo-system]], [[product/ai-product-model]]
---

# Motion System

Twoweeks motion is a system about stopping, not movement. Stillness is the default; motion exists only to prove that work happened and then settle.

## Current state

The motion thesis is:

`The point thinks. The document changes. The interface proves it. Then everything settles.`

Only the terracotta period in the logo may loop, and only while real AI work is active. Everything else must be causal, fast, and tied to user uncertainty.

## Principles

- stillness is the default
- motion follows causality
- proof over performance
- one ambient loop, ever
- speed is a feature, not a transition
- content earns motion; chrome does not
- ending is louder than starting

## Required primitives

- `breathing-dot`
- `progress-step`
- `updated-region-flash`
- `diff-reveal`
- `success-settle`
- `error-contour`
- `active-rail`
- `skeleton-to-content` only for true unknown loading, never AI work

## Implementation order

The hardened plan splits implementation into narrow PRs:

1. canonical motion tokens, legacy aliases, reduced-motion fallback, `useAiActivity`, `BreathingDot`, `StageText`, proposal-generation integration
2. `success-settle`, `RegionFlash`, `ErrorContour`, `ActiveRail`, jobs score motion, CV parsing warnings, sidebar/tab rail
3. streaming text, diff reveal, editor/preview sync, overlay token migration, stylelint rule against animated layout properties

## Constraints

- no spinners, sparkles, shimmer, confetti, robot avatars, or per-character text reveal
- no green/red score movement grammar; use terracotta and neutral
- no animated `width`, `height`, `top`, `left`, `margin`, or `padding`
- `prefers-reduced-motion` must preserve state changes while removing motion
- stage text, not vague loaders, carries AI progress

## Sources

- [[sources/2026-04-27-twoweeks-motion-system]]
- [[sources/2026-04-27-motion-system-implementation-hardening]]

## Related

- [[design/logo-system]]
- [[design/brand-voice]]

