# Hybrid examples for real repo work

These examples adapt the twoweeks-pagecraft behavior layer to a code-bearing twoweeks repository while keeping the wiki control plane intact.

## 1. Bug fix: reproduce before changing code

### Weak behavior

> “Search is broken on duplicate scores, I updated the sorter and cleaned up some helper functions.”

Problems:

- no proof the bug was reproduced
- no proof the fix works
- unrelated helpers were changed

### Hybrid behavior

```text
Goal:
Fix duplicate-score ordering without changing unrelated ranking behavior.

Assumptions:
The owner is the ranking utility used by the search endpoint.

Smallest safe change:
Add one failing test for duplicate scores, then fix the local tie-break logic only.

Verification:
1. New test fails before the fix.
2. New test passes after the fix.
3. Existing ranking tests still pass.
```

## 2. Feature: avoid speculative architecture

### Weak behavior

> “I added a generic plugin system for exporters because we might add more formats later.”

Problems:

- abstraction added for a future that was not requested
- more code and more maintenance surface than needed

### Hybrid behavior

```text
Goal:
Add CSV export for the current report endpoint.

Assumptions:
Only CSV is required right now.

Smallest safe change:
Add one CSV formatter in the existing report module and one acceptance test.

Verification:
1. Endpoint returns CSV with the requested columns.
2. Existing JSON behavior is unchanged.
```

## 3. Repo audit: criteria instead of vibes

### Weak behavior

> “The repo looks decent, but I would refactor a lot of things.”

Problems:

- subjective
- not benchmarkable
- no next action path

### Hybrid behavior

Audit against explicit criteria:

- assumption / preflight discipline
- simplicity rules
- surgical diff discipline
- verification rules
- source roots and ownership clarity
- tests near behavior
- CI / lint / build presence
- artifact/reporting readiness

Then group findings by:

1. correctness risk
2. leverage / missing functionality
3. hygiene

## 4. Wiki mutation: control plane still matters

### Weak behavior

> “I created three new pages because the source had many interesting details.”

Problems:

- likely duplication
- retrieval surface gets worse
- more maintenance for little gain

### Hybrid behavior

```text
Goal:
Merge new source facts into the current product roadmap page.

Assumptions:
The roadmap page is still the canonical durable page.

Smallest safe change:
Reuse the source page if already present, update the existing roadmap page, and avoid creating sibling pages.

Verification:
1. Source page created or reused.
2. Roadmap page updated.
3. `wiki/index.md` and `wiki/log.md` updated.
```

## 5. Knowledge-plane repository with no application code

### Weak behavior

> “The repo is a codebase because I found some JavaScript files, so I’ll treat the Obsidian plugins as app code.”

Problems:

- hidden tooling files are misclassified as product code
- repo audit becomes misleading
- follow-up recommendations target the wrong surface

### Hybrid behavior

```text
Goal:
Audit the real code plane without confusing wiki tooling for application code.

Assumptions:
This repository may currently be knowledge-plane-only.

Smallest safe change:
Ignore Obsidian, wiki, and raw storage directories when scoring code-plane structure.

Verification:
1. The repo audit reports whether a real code plane is present.
2. Obsidian plugin files no longer count as application source.
3. The instruction-layer score still reflects the rule quality.
```
