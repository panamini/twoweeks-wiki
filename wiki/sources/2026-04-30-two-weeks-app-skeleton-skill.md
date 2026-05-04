---
title: "Twoweeks app skeleton skill source"
category: source
tags: [app, skeleton, front-end, skill]
created: 2026-04-30
updated: 2026-05-04
status: current
type: skill
related: [[tech/local-vs-remote-parser-architecture]], [[tasks/kanban]], [[meta/codex-prompting-standards]]
---

# Two-Weeks App Skeleton skill source

This source captures the working contract for the `twoweeks-app-skeleton` SKILL helper and its expected precedence.

## Key points

- Core contract priority: `APP-SKELETON.html` and its adjacent reframe documents.
- PR boundaries matter: route work is split by PR domain (shell/dashboard, proposal, jobs, CV, docs/settings).
- Conflicts resolve with explicit rules:
  - Quick Start has one implementation path with a consistent 6-step onboarding flow.
  - Theme remains Light/Dark unless docs explicitly change.
  - Match percentages are not user-facing; verdict labels preferred.
- Preserve existing behavior in `my-app/src/lib/ai/*` unless the PR explicitly requires changes.

## Required workflow

1. Read skeleton and audit docs before implementation.
2. Compare target surface and preserve KEEP/RESTORE items.
3. Apply smallest PR-scoped patch.
4. Run narrow tests first, then UI verification for changed surfaces.

## Source

- `raw/two-weeks app skeleton -skill.md`
