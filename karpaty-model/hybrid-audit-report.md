# Hybrid Audit Report

## Scope

I treated **your project** as the uploaded twoweeks wiki contract, because that is the project material available in this session.

That means this audit is about the **instruction / orchestration layer**, not about application source code or model weights.
So the relevant question is:

> Which project provides the stronger operating layer for an agent that needs to mutate, audit, and preserve knowledge while behaving like a careful senior engineer?

## Executive conclusion

Karpathy does **not** beat twoweeks on repository structure, ingest workflow, or knowledge governance.

Karpathy **does** beat twoweeks on the behavioral layer:

1. ambiguity handling
2. anti-bloat / simplicity pressure
3. surgical-scope discipline
4. verifiable completion criteria
5. example-driven onboarding
6. portable packaging as a reusable plugin/skill

The right move is **not** to replace twoweeks with Karpathy.
The right move is to **add Karpathy as a behavior shim on top of twoweeks**.

That is what this hybrid package implements.

## Layer-by-layer verdict

### Layers where twoweeks is stronger

- **Knowledge architecture**
  - clear durable/support page split
  - explicit retrieval order
  - archive vs active separation

- **Mutation governance**
  - strong rules for create/update/supersede
  - mandatory `wiki/index.md` and `wiki/log.md`
  - raw/source/output separation

- **Operational coverage**
  - ingest
  - direct-update
  - lint
  - save-output

### Layers where Karpathy is stronger

- **Assumption management**
  - explicitly surfaces confusion instead of silently picking a path

- **Complexity control**
  - forces minimum viable change and rejects speculative abstractions

- **Scope containment**
  - “touch only what you must” maps directly to smaller diffs and fewer accidental regressions

- **Verification discipline**
  - pushes every task toward a clear success condition

- **Training / onboarding**
  - examples file teaches the expected behavior through contrast

- **Portability**
  - plugin packaging makes the behavior layer easier to reuse across repos

## Missing functionality in the original twoweeks project

These were the most valuable missing pieces:

1. **Ambiguity gate**
   - The original system tells the agent how to mutate the wiki, but not how to handle uncertainty before it mutates.

2. **Minimality gate**
   - The original system prefers simplicity at a structural level, but it does not enforce a hard anti-bloat behavior layer.

3. **Surgical-diff rule**
   - The original system repairs references and updates control files, but it does not explicitly forbid drive-by rewrites.

4. **Mode-specific verification**
   - The original system has workflows, but Karpathy adds a stronger “done means verified” discipline.

5. **Examples package**
   - The original system lacks a concrete examples file showing good vs bad behavior.

6. **Portable plugin metadata**
   - The original system is repo-local; Karpathy’s repo is packaged for easier reuse.

## Benchmark method

Scoring model:

- score each criterion from **1 to 5**
- apply the weight from `benchmark-matrix.csv`
- compute weighted totals on a 100-point scale

Interpretation:

- **1** = absent
- **3** = adequate
- **5** = strong / explicit / reusable

## Weighted totals

See `audit/benchmark-summary.json`.

Headline result:

- **twoweeks baseline:** structurally excellent, behaviorally incomplete
- **Karpathy baseline:** behaviorally excellent, structurally thin
- **hybrid target:** strongest combined profile

## What changed in the hybrid

### 1. Added a behavior layer to `CLAUDE.md`
I inserted explicit rules for:

- think before mutating
- simplicity first
- surgical changes
- goal-driven execution

### 2. Added preflight to the skill
The upgraded skill now requires:

```text
Goal:
Assumptions:
Smallest safe change:
Verification:
```

before non-trivial writes.

### 3. Added mode-specific verification
Each mode now has explicit completion checks instead of ending at “changes were made”.

### 4. Added wiki-specific examples
The new `EXAMPLES.md` translates the Karpathy principles into:

- page creation decisions
- ingest decisions
- lint reporting
- save-output discipline

### 5. Added portability metadata
The hybrid now includes `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.

### 6. Preserved the twoweeks control plane
I did **not** remove or weaken:

- page frontmatter contract
- category router
- ingest/direct-update/lint/save-output modes
- retrieval order
- archive model
- index/log requirements

## Recommended usage

Use this hybrid when you want an agent that:

- preserves a stable knowledge base
- avoids over-creation of pages
- explains ambiguities before mutating
- verifies completion instead of stopping early
- behaves more like a careful senior engineer than a fast speculative generator

## Validation

I added scripts to validate the package shape and recompute the benchmark.
See:

- `scripts/validate_hybrid.py`
- `scripts/score_benchmark.py`
- `audit/validation-output.txt`
- `audit/benchmark-summary.json`
