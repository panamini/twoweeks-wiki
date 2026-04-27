---
title: "Motion System Implementation Hardening"
category: source
tags: [motion, implementation, tokens, pr-plan]
created: 2026-04-27
updated: 2026-04-27
status: current
type: spec
related: [[design/motion-system]]
---

# Motion System Implementation Hardening

## Summary

Hardening pass that converts the motion-system audit into implementation-ready PR scopes and resolves token, concurrency, and validation risks.

## Key points

- Add canonical `--motion-*` tokens in `foundation.css` and alias legacy duration/easing tokens rather than deleting them.
- Global AI activity should be a counter, not a boolean, so concurrent operations do not race the breathing dot.
- PR1 covers canonical tokens, reduced motion, `useAiActivity`, `BreathingDot`, `StageText`, and proposal generation only.
- PR2 adds settle, region flash, error contour, active rail, score tweening, and selected integrations.
- PR3 adds streaming text, diff reveal, editor/preview sync, overlay token migration, and a lint rule against animated layout properties.

## Implications

Provides the implementation plan for [[design/motion-system]].

## Touched pages

- [[design/motion-system]]

