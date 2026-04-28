---
title: "AI Consistency P0 — Editor AI Baseline"
category: product
tags: [ai, editor, rulebook, telemetry, job-context, baseline]
created: 2026-04-28
updated: 2026-04-28
status: current
valid_from: 2026-04-28
valid_until:
superseded_by:
horizon: present
version: v1
related: [[product/product-roadmap]], [[product/ai-product-model]], [[product/kpis]]
---

# AI Consistency P0 — Editor AI Baseline

## Status

- P0 implementation is merged.
- Closure audit is still pending.
- This document is a merged-baseline snapshot, not a full audit.

## Problem

The original editor AI behavior was fragmented across surfaces:

- toolbar and backend action drift
- risky rewrites auto-applying
- custom Ask AI auto-applying
- duplicated diff cards
- no shared apply contract
- no telemetry lifecycle
- no job-context contract for tailoring

That made the product feel inconsistent even when individual flows worked.

## Merged PRs

### PR #42 — Editor AI action contract

- canonical action IDs
- frontend rulebook
- backend mirror / validator
- structured `transformEditorSelection` result
- apply mode explicit in backend result

### PR #43 — Preview and undo flow

- shared `AiSuggestionCard`
- shared apply / undo helper
- risky / custom actions preview first
- low-risk actions inline with Undo

### PR #44 — Metadata-only telemetry

Events:

- `ai_started`
- `ai_completed`
- `ai_failed`
- `ai_accepted`
- `ai_discarded`
- `ai_undone`

Privacy rule:

- no selected text
- no generated text
- no prompts
- no CV / proposal / job content

### PR #45 — Job-aware tailoring

- canonical `tailor_to_job`
- high-risk
- `preview_required`
- compact job context required
- hidden without context
- backend rejects missing / insufficient context before model call
- no raw job text passed
- variants deferred as `[]`

## Current Editor AI Contract

Canonical actions:

```ts
fix_grammar
shorten
rewrite
clarify
strengthen
expand
custom
tailor_to_job
```

Apply modes:

```ts
inline_replace_with_undo
preview_required
```

Result shape:

```ts
{
  kind: "text",
  actionId,
  text,
  applyMode,
  outputMode,
  variants
}
```

Interpretation:

- `inline_replace_with_undo` is for low-risk edits that can apply immediately and be reverted.
- `preview_required` is for higher-risk or user-controlled edits that must wait for Accept.
- `variants` stay empty in the merged baseline.

## Deferred Work

1. Post-P0 closure audit
2. Playwright roundtrip stabilization
3. Skeleton-based AI suggestion UI polish
4. CV job-context Tailor
5. `Insert below` / `Keep both`
6. Variants

## Known Caveats

- Broad TypeScript build debt existed before this pass and remains unresolved.
- PR #45 was merged with a documented waiver because the required Playwright check failed on an unrelated roundtrip timeout.
- The failing spec was `e2e/proposal-workspace-roundtrip.spec.ts`.
- The timeout was waiting for `Switch CV. Attached CV: Operations Associate — Alex Martin`.

## Design Principle

AI should be controlled, reversible, context-bounded, and quiet.

No AI cockpit.
No hidden destructive behavior.

The backend declares the contract.
The frontend applies the contract.
The user stays in control.
