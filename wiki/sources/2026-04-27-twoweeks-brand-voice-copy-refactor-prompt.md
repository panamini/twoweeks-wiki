---
title: "Prompt for Twoweeks Brand-Voice Copy Refactor"
category: source
tags: [brand, voice, prompt, copy-refactor]
created: 2026-04-27
updated: 2026-04-27
status: current
type: other
related: [[design/brand-voice]], [[meta/codex-prompting-standards]]
---

# Prompt for Twoweeks Brand-Voice Copy Refactor

## Summary

Execution prompt for applying Twoweeks voice rules to user-facing strings in a React/Next.js codebase from an audit table.

## Key points

- Preserve code identifiers and structure; apply only approved string changes.
- Skip flagged-ambiguous rows and report them back.
- Do not touch aria labels that describe non-visual behavior, keyboard hints, auth/legal/payment vendor copy, analytics names, or internal constants.
- Enforces declarative compressed copy, period rhythm, present tense, numeric digits, and noun locks.

## Implications

Supports [[design/brand-voice]] and [[meta/codex-prompting-standards]].

## Touched pages

- [[design/brand-voice]]
- [[meta/codex-prompting-standards]]
