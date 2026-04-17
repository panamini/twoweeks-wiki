---
name: apply-hybrid-code-layer
description: >
  Code-aware execution layer for the twoweeks hybrid repository. Use this skill for
  repo-audit, implement, benchmark, and save-output work on real codebases. It applies
  twoweeks-pagecraft behavior discipline to manifests, source code, tests, CI, and reports,
  while staying compatible with the twoweeks wiki control plane.
license: MIT
---

# apply-hybrid-code-layer

Use this skill when the request is about real code structure, tests, implementation rules,
performance work, or benchmarkable repo audits.
Only apply it when a real code plane exists in this repository or is mounted into the same workspace.

## 1. Pick the mode

Choose the first matching mode:

- `repo-audit`
  - user asks for an audit, compare, benchmark, gap analysis, or senior review of the code repo
- `implement`
  - user asks to fix a bug, add a feature, refactor, or apply the hybrid layer to code changes
- `benchmark`
  - user asks for a measurable before/after comparison, performance study, or criteria scoring
- `save-output`
  - user asks to preserve the current report or change summary

## 2. Read sequence

Read in this order:

1. `WIKI_SCHEMA.md` if present
2. `AGENTS.md` and/or `CLAUDE.md`
3. root `README.md`
4. build / dependency manifests
5. tests and test config nearest the behavior
6. CI / lint / formatting config
7. the smallest source module that owns the behavior
8. callers only if needed
9. relevant `wiki/tech/`, `wiki/howto/`, or `wiki/product/` pages when they clarify intent

Do not load the whole repository unless the task genuinely requires it.

## 3. Mandatory preflight

Before non-trivial work, state:

```text
Goal:
Assumptions:
Smallest safe change:
Verification:
```

Rules:

- if multiple interpretations exist, present them briefly instead of picking silently
- if a simpler approach exists, say so
- if uncertainty is material, choose the safer narrow interpretation or ask
- do not continue with hidden confusion

## 4. Global rules

- prefer the smallest owning module
- do not invent abstractions for one call site
- do not do drive-by refactors
- preserve existing style unless a broader migration is requested
- remove only dead code created by your own change
- match the existing test framework and CI conventions
- every changed line should trace back to the request
- for non-trivial work, report files changed and verification results

## 5. repo-audit mode

### 5.1 Inventory

Identify:

- manifests and primary language(s)
- source roots and likely entrypoints
- test roots and test framework(s)
- CI / lint / format configuration
- architecture documents or wiki tech pages
- obvious gaps between rules and implementation

### 5.2 Score against criteria

Use `audit/code-benchmark-criteria.csv`.

Score at least:

- ambiguity / preflight discipline
- simplicity guardrails
- surgical diff discipline
- verification discipline
- source roots and ownership clarity
- tests near behavior
- CI / lint / build coverage
- repeatable audit and reporting artifacts

### 5.3 Report

Group findings by:

1. correctness risk
2. leverage / missing functionality
3. maintenance hygiene

For each finding, recommend the smallest safe fix.

## 6. implement mode

### 6.1 Bug fix

1. reproduce with a failing test or harness
2. make the smallest owning code change
3. rerun the failing case
4. rerun nearby tests
5. report the root cause and why the fix is sufficient

### 6.2 Feature

1. define acceptance behavior
2. add the smallest relevant coverage
3. implement the narrowest path
4. verify behavior and nearby regressions
5. separate future ideas from delivered scope

### 6.3 Refactor

1. state preserved behavior
2. lock it with tests if needed
3. refactor in small steps
4. verify no behavior drift
5. report debt that remains intentionally untouched

## 7. benchmark mode

Only claim improvements you can measure.

Record:

- metric
- baseline command / environment
- after-state command / environment
- before and after values
- limits of the measurement

Good examples:

- failing tests before / passing tests after
- latency before / after on the same command
- file count or diff size before / after for simplification work
- coverage before / after when adding tests

## 8. save-output mode

If the knowledge plane exists, prefer saving to `wiki/outputs/` using the output contract.
If the repo has no wiki, save under `audit/` or `reports/` with a stable date-stamped filename.

Verify:

1. artifact exists
2. path is linked from the nearest navigation surface when one exists
3. the report states commands, evidence, and unresolved risks

## 9. Quality bar

A good result should show:

- explicit assumptions instead of hidden guesses
- smaller, cleaner diffs
- tests or measurements near the changed behavior
- no speculative architecture
- no unverified claims
- a report that another engineer could follow without rereading the whole repo
