---
title: "Codex Prompting Standards"
category: meta
tags: [codex, prompts, agents, execution, scope]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-27-codex-prompt-master, 2026-04-27-ui-design-audit-prompt, 2026-04-27-twoweeks-brand-voice-copy-refactor-prompt]
related: [[meta/llm-wiki-pattern]], [[design/brand-voice]]
---

# Codex Prompting Standards

Codex execution prompts should be strict, local, testable, and explicit about both scope and non-regression proof.

## Current state

A good Codex prompt closes bad plausible interpretations. It should answer:

1. exact objective
2. allowed modification scope
3. forbidden zones
4. invariants to preserve
5. verification method
6. expected output format

## Required shape

- context
- goal
- scope
- do not change
- required work
- constraints
- acceptance criteria
- required output

## Rules

- preserve the user's exact intent
- never broaden scope
- convert vague language into testable constraints
- ban opportunistic refactors, redesigns, adjacent cleanups, and unrelated improvements
- require targeted tests or checks
- prefer a narrower scope and stronger non-regression proof when uncertain

## Design audit prompts

High-stakes UI audits should separate objective craft issues, accessibility risks, UX risks, and subjective taste. They should judge only what is visible, label inferred claims, and return concrete token/system-level fixes rather than generic taste advice.

## Sources

- [[sources/2026-04-27-codex-prompt-master]]
- [[sources/2026-04-27-ui-design-audit-prompt]]
- [[sources/2026-04-27-twoweeks-brand-voice-copy-refactor-prompt]]

