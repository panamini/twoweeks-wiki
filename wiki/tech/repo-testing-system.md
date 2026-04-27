---
title: "Repo Testing System"
category: tech
tags: [tests, vitest, playwright, jsdom, qa]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-27-repo-test-system-note]
related: [[tech/import-ocr-pipeline]], [[tech/workshop-pagination]]
---

# Repo Testing System

The application test base is primarily Vitest in `my-app`, backed by JSDOM and Testing Library. Playwright exists but product E2E coverage is still light.

## Current state

The main command is `npm run test`, which runs `vitest --run --exclude pdf-ingest/*`. Tests live both centrally in `src/__tests__` and near domains such as hooks, components, pages, contexts, and Convex parsing logic.

## Coverage shape

The strongest coverage is around:

- CV business logic and data normalization
- hooks and providers
- important UI flows
- async behavior such as polling, local persistence, and state handoff
- parsing canonicalization and import recovery logic

The suite relies on targeted mocks for `convex/react`, Clerk, `fetch`, `localStorage`, and browser runtime APIs. `src/setupTests.ts` and `src/test/setup.ts` are required reading before test changes.

## Style

Tests should prefer observable behavior and accessible queries (`getByRole`, `findByRole`, `getByLabelText`) over snapshots or DOM-structure assertions. Mocks and timers should be cleaned explicitly.

## Gap

The main visible weakness is not unit-test quality; it is thin product E2E coverage. Playwright is present, but current E2E examples are not yet broad product coverage.

## Sources

- [[sources/2026-04-27-repo-test-system-note]]

## Related

- [[tech/workshop-pagination]]

