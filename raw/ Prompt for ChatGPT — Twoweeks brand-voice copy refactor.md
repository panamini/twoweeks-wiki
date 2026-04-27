#

You are refactoring user-facing strings in a Next.js/React codebase to match the **Twoweeks.ai brand voice**.

## Voice rules (non-negotiable)

- **Declarative.** State facts. No apology, no "please", no "kindly", no "sorry".
- **Compressed.** Buttons 1–3 words. Tooltips ≤4 words. Empty states ≤2 lines. Errors: fact, then action.
- **Punctuation.** Periods as pause. No exclamations. No ellipses. No em-dashes in headlines (OK in body).
- **Tense.** Present. `Saved.` not `Will be saved.`
- **Numbers.** Numerals always (`2 weeks`, `0 saved`).
- **Questions.** Only on destructive confirms (`Delete this job?`).
- **Toasts.** Success = one word + period (`Saved.`). Failure = 2–3 words + period (`Import failed.`).

## IA locks

- `CV` → `resume` (user-facing).
- `proposal` → `cover letter` (vestigial; keep in code identifiers, flip in UI copy).
- Brand: `Twoweeks` (not TwoWeeks, not Proposal Forge).

## Banned words

seamlessly, effortlessly, powerful, leverage, unlock, elevate, empower, robust, comprehensive, intuitive, intelligent, smart, AI-powered, let's, hey, oops, please, kindly, sorry, "Just a sec…", "Working on it."

## Do not touch

- `aria-label` describing non-visual behavior (a11y convention wins).
- Keyboard shortcut hints.
- Clerk auth flows, legal/ToS, payment vendor copy.
- Analytics event names, internal error code constants.

## Task

I will paste an audit table in the format `file:line | current | surface | proposed | note`. For each row:

1. Apply the `proposed` string at the exact `file:line`.
2. Preserve surrounding code, types, and JSX structure.
3. Do not rename identifiers, props, or constants.
4. If a row is flagged ambiguous, skip it and list it back to me.

Output: a unified diff per file, grouped by the commit split I provide. No commentary inside the diffs.