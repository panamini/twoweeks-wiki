---
title: "Proposal Generation Truth Planner"
category: source
tags: [proposal, ai, safety, truth, benchmark]
created: 2026-05-25
updated: 2026-05-25
status: current
type: scratchpad
related: [[product/ai-product-model]], [[tech/proposal-ai-routing-and-inline-diff]], [[tech/repo-testing-system]]
---

# Proposal Generation Truth Planner

## Summary

This source defines a typed `ProposalTruthPlanV1` contract that limits what can be safely claimed before proposal drafting. It is intended as a shadow layer: plan first, writer second.

## Key points

- Safety backbone should remain:
  - draft -> detect unsafe claims -> constrained repair -> verifier -> fallback/fail-closed.
- The next layer is a semantic truth plan with no prompt rewriting:
  - `candidate + job inputs -> truth plan -> writer -> verifier`.
- `ProposalTruthPlanV1` should be deterministic in phase 1 (no live model calls).
- Writing mode must stay narrow: `normal`, `adjacent_only`, `no_context_safe`.
- `writerPolicy` exists in the schema but is shadow-only until phase 3.
- Direct candidate claims must be linked to source-backed `factIds`.
- `factIds: []` is only allowed for soft role/job-surface claims.
- Example fixture targets: weak SEO, no-context sales assistant, strong frontend, adjacent admin.
- Phase 1 scope is strict:
  - add typed planner + deterministic implementation + harness + tests,
  - do not change final production output,
  - do not change routing, prompts, UI, or live model calls.
- Key open question before phase 3:
  - whether `application-adjacent-admin` is `normal` or `adjacent_only`.

## Implications

- `harness` output should expose both the planned contract and final findings to support traceability.
- This source should drive next regression work for proposal truth safety, not production writer behavior yet.
- Existing proposal safety layers should remain unchanged until plan writer integration is explicitly enabled.

## Touched pages

- [[product/ai-product-model]]
- [[tech/proposal-ai-routing-and-inline-diff]]
- [[tech/repo-testing-system]]
