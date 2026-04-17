# Implementation rules

This file translates the hybrid contract into a direct checklist for real code work.
Apply it only when a real code plane exists in this repository or is mounted into the same workspace.

## Preflight

Before non-trivial code changes, write:

```text
Goal:
Assumptions:
Smallest safe change:
Verification:
```

## Do this

- start from the nearest test, bug report, failing case, or entrypoint
- change the smallest owning module first
- keep new APIs narrower than your first instinct
- reuse existing patterns before introducing a new abstraction
- report exact verification commands and outcomes
- update the nearest relevant docs when public behavior changes

## Do not do this

- do not create extension points for hypothetical future use
- do not reformat unrelated files while fixing a bug
- do not silently replace user-authored comments with generic summaries
- do not claim success without a passing check, test, or measurement
- do not mix refactors with behavior changes unless the task explicitly requires both

## By task type

### Bug fix

1. reproduce
2. make the repro fail reliably
3. fix the smallest owning path
4. rerun the repro and nearby tests
5. report why the bug existed and why the fix is sufficient

### Feature

1. define acceptance behavior
2. add the smallest relevant coverage
3. implement the minimal path
4. verify the requested behavior and nearby regressions
5. report follow-ups separately from the delivered scope

### Refactor

1. define preserved behavior
2. lock it with tests if coverage is missing
3. refactor in small steps
4. verify external behavior stayed the same
5. report any debt intentionally left in place

### Performance

1. define the metric
2. record baseline
3. optimize the hottest proven path
4. record after-state
5. report environment, commands, and deltas

## Benchmark dimensions

Judge changes by these questions:

- **clarity** — is the owning path easier to understand afterward?
- **scope** — does every changed line trace back to the request?
- **verification** — is there a concrete proof the change works?
- **simplicity** — did the change avoid speculative complexity?
- **fit** — does it match existing repo conventions instead of inventing new ones?

## Reporting template

```markdown
## Change summary
- files changed
- minimal intent of each change

## Verification
- command / check
- observed result

## Risks / follow-ups
- unresolved edge cases
- deferred improvements not included in this diff
```
