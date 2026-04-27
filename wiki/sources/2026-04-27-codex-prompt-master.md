---
title: "Meta-prompt maître"
category: source
tags: [codex, prompt, agents, scope]
created: 2026-04-27
updated: 2026-04-27
status: current
type: other
related: [[meta/codex-prompting-standards]]
---

# Meta-prompt maître

## Summary

Prompt and method for rewriting weak technical prompts into strict, local, testable, regression-safe Codex execution prompts.

## Key points

- Preserve exact intent and never broaden scope.
- Convert ambiguity into explicit constraints and acceptance criteria.
- Name allowed scope, forbidden files/zones, invariants, required tests, and output format.
- Ban opportunistic refactors, redesigns, adjacent cleanups, and vague phrasing.
- Prefer narrower scope and stronger proof of non-regression when uncertain.

## Implications

Creates [[meta/codex-prompting-standards]].

## Touched pages

- [[meta/codex-prompting-standards]]
