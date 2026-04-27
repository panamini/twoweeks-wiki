---
title: "Repo Test System Note"
category: source
tags: [tests, vitest, playwright, jsdom]
created: 2026-04-27
updated: 2026-04-27
status: current
type: other
related: [[tech/repo-testing-system]]
---

# Repo Test System Note

## Summary

Short audit of the app's test system: primarily Vitest + JSDOM + Testing Library, with lighter Playwright coverage.

## Key points

- `npm run test` runs Vitest in `my-app`.
- Tests are hybrid: central `src/__tests__` plus colocation near hooks, components, pages, contexts, and Convex parsing code.
- Coverage is strongest around CV logic, hooks/providers, UI flows, and async handoff/persistence behavior.
- Mocks focus on Convex, Clerk, fetch, localStorage, and browser runtime APIs.
- Weakest visible area is product E2E coverage, not the quality of existing unit/behavior tests.

## Implications

Creates [[tech/repo-testing-system]].

## Touched pages

- [[tech/repo-testing-system]]
