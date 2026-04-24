Both artifacts below. Save the voice card, then the audit table is your calibration reference.

---

## 1. Merged voice card — save as `~/.claude/brand/twoweeks-voice.md`

```markdown
# Twoweeks.ai — Brand Voice Card

## Identity
- Archetype: anti-corporate productivity coach
- Lineage: Linear × 37signals × anti-work movement
- Register: declarative, compressed, leisure-forward
- Thesis: the work is done. Time > ambition.

## Rhythm
- Poster/marketing: all-caps two-word panel heads with terminal periods ("FIND SIGNAL.")
- UI body: Conventional Title Case; periods as pause, not as decoration
- 2–3 supporting lines max, 4 words each max
- Never 4-line bodies — waters it down

## Capitalization
- Title Case for UI labels and nav
- ALL CAPS only in marketing surfaces (posters, hero, value labels)
- Sentence case for multi-sentence body copy

## Punctuation
- Heavy period rhythm
- No exclamations. No ellipses. No em-dashes in headlines.
- Commas only when required for clarity

## Tense & Person
- Present tense. No future promises. "Saved." not "Will be saved."
- Second person implied, rarely stated. "Paste the URL" not "You can paste the URL."

## Numbers
- Numerals always. `2 weeks`, `23 jobs`, `0 saved`. Never spell out.

## Questions
- Zero. The brand declares. The only exception: destructive confirms ("Delete this job?").

## Stance
- Anti-corporate, pro-Friday-afternoon
- User is capable; the tool is invisible
- Declarative over coaching

## UI Surface Rules

### Buttons
- 1–3 words. Verb-first.
- No period.
- `Save job`, `Attach resume`, `Draft cover letter`.

### Section headers
- 1–2 words, Title Case.
- `Jobs`. `Brief`. `Match`. `Resumes`.

### Empty states
- Two lines max. Line 1 declarative fact. Line 2 action.
- `No jobs. Import one.`

### Tooltips
- 4 words max. No period.
- `Attach a resume`. `Collapse sidebar`.

### Placeholders
- Mirror the field. No hints. No e.g.
- `Paste job URL`. `Job title`.

### Toasts
- Success: one word. `Saved.` `Done.`
- Failure: two–three words. `Import failed.` `Save failed.`

### Errors
- State the fact. No apology. No cause unless fixable.
- `Job not found.` not `We couldn't find that job.`

### Loading
- `Loading` alone is fine. Avoid `Just a sec...`, `Working on it.`

### Confirms (destructive only)
- Question form allowed here.
- `Delete this job?` `Discard draft?`

## Allowed Words
Jobs, Brief, Match, Resume, Draft, Saved, Done, Open, Close, Attach, Detach, Import, Paste, Pick, Skip, Keep, Drop, Archive, Duplicate, Default, Missing, Matched, Weak, Partial, Strong.

## Banned Words
- Hype: seamlessly, effortlessly, powerful, leverage, unlock, elevate, empower, robust, comprehensive, intuitive, intelligent, smart, AI-powered, cutting-edge, best-in-class.
- Coach-voice: let's, hey, oops, uh oh, whoops, yay, hooray, you got this, we get you.
- Corporate filler: please, kindly, sorry (except real apology for real failure).
- Constructions: "not X, just Y", "Zero fluff", "Real impact", "Powerful under the hood".
- "Zero X" — max once per campaign. Not in UI.

## Voice Calibration Examples

- `Click here to attach a resume` → `Attach resume`
- `No jobs yet. Get started by importing your first one!` → `No jobs. Import one.`
- `Oops! Something went wrong. Please try again.` → `Something broke. Try again.`
- `Successfully saved your changes` → `Saved.`
- `Are you sure you want to delete this job?` → `Delete this job?`
- `e.g. https://linkedin.com/jobs/...` → `Paste job URL`
- `Loading your jobs, please wait...` → `Loading jobs`
- `You haven't selected a resume yet` → `No resume attached`
- `Generate a cover letter with AI` → `Draft cover letter`

## Do Not Touch
- Clerk-owned auth flows
- Legal, ToS, privacy
- Payment copy from vendor
- aria-labels describing non-visual behavior (screen-reader convention wins over voice)
- Analytics event names
- Keyboard shortcut hints
```

---

## 2. Sidebar audit table — calibration reference

Source: `my-app/src/components/Sidebar.tsx`. Surface type, current, proposed. Rationale where non-obvious.

|file:line|current|surface|proposed|note|
|---|---|---|---|---|
|Sidebar.tsx:172|`Untitled Resume`|fallback-label|`Untitled resume`|sentence case for fallback phrasings reads less corporate|
|Sidebar.tsx:173|`Untitled Resume {n}`|fallback-label|`Untitled resume {n}`|same|
|Sidebar.tsx:251|`Delete {title}`|aria-label|keep|aria convention wins|
|Sidebar.tsx:258–259|`Confirm delete {title}`|aria/title|keep|aria convention|
|Sidebar.tsx:275–276|`Cancel delete {title}`|aria/title|keep|aria convention|
|Sidebar.tsx:290–291|`Delete {title}`|aria/title|keep|aria convention|
|Sidebar.tsx:313|`All {label} ({count}) →`|nav-link|`All {label} ({count})`|arrow is visual noise; link affordance is sufficient|
|Sidebar.tsx:753|`Untitled Resume`|fallback-label|`Untitled resume`|matches above|
|Sidebar.tsx:764|`Untitled Resume`|fallback-label|`Untitled resume`||
|Sidebar.tsx:915|`Cover Letter` (base)|fallback-base|`Cover letter`|sentence case for fallback|
|Sidebar.tsx:922|`Untitled Cover Letter`|fallback-label|`Untitled cover letter`||
|Sidebar.tsx:931|`Untitled Cover Letter`|fallback-label|`Untitled cover letter`||
|Sidebar.tsx:799|`Saved proposal`|optimistic-title|`Saved cover letter`|"proposal" is vestigial; product language is cover letter|
|Sidebar.tsx:1016–1017|`Expand sidebar` / `Collapse sidebar`|title/aria|keep|accurate, brand-compatible|
|Sidebar.tsx:1024|`Primary sidebar`|nav aria-label|keep|aria convention|
|Sidebar.tsx:1026|`Quick Start`|rail label|`Quick start`|Title Case inflated for a two-word action; sentence case fits better|
|Sidebar.tsx:1033, 1047|`Resumes`|rail label|keep|correct|
|Sidebar.tsx:1057, 1066|`Cover letters`|rail label|keep|correct|
|Sidebar.tsx:1079|`Quick Start`|section aria|`Quick start`|match visible label|
|Sidebar.tsx:1094|`Quick Start`|button text|`Quick start`||
|Sidebar.tsx:1099|`Resumes`|section label|keep||
|Sidebar.tsx:1101|`New Resume` (renders as `+ New Resume`)|button|`New resume` (renders as `+ New resume`)|sentence case for sidebar actions|
|Sidebar.tsx:1102|`Resumes`|all-label|keep||
|Sidebar.tsx:1110|`Cover letters`|section label|keep||
|Sidebar.tsx:1112|`New Cover Letter` → `+ New Cover Letter`|button|`New cover letter` → `+ New cover letter`||
|Sidebar.tsx:1113|`Cover letters`|all-label|keep||
|Sidebar.tsx:1133|`Open account menu` / `Sign in`|aria|keep|accurate|
|Sidebar.tsx:1134|`Account` / `Sign in`|tooltip|keep|one word each, on brand|
|Sidebar.tsx:1151|`Account` (fallback for username)|display name|`You`|softer than generic "Account" as a name; matches leisure-forward tone. Alternative: keep `Account` if `You` feels too casual for you|
|Sidebar.tsx:1155|`Loading`|status|keep||
|Sidebar.tsx:1157|`Signed in`|status|keep||
|Sidebar.tsx:1158|`Guest`|status|keep||
|Sidebar.tsx:1169–1170|`Settings`|tooltip/aria|keep||
|Sidebar.tsx:1181, 1183|`Switch to light mode` / `Switch to dark mode`|tooltip/aria|`Light mode` / `Dark mode`|tooltip rule: 4 words max, no verb padding|

### Flagged-ambiguous

1. **`All resumes (N) →` arrow removal.** Losing the arrow costs a visual affordance. Confirm it — if you like the arrow visually, keep it. Voice rule says no decorative punctuation in nav, but arrows-as-UI are common. Your call.
2. **`Account` → `You` for signed-in display name fallback.** `You` is warmer but less literal. If it reads weird when someone has no first name set, revert.
3. **`Saved proposal` → `Saved cover letter`.** Depends on whether you're migrating product language away from "proposal" app-wide, or if "proposal" stays a valid term elsewhere. This flags the broader question: is it `Cover letters` or `Proposals` in your product? Pick one.

### What stays the same

- All aria-labels describing destructive confirms (convention wins).
- `Resumes`, `Cover letters`, `Settings`, `Account`, `Loading`, `Signed in`, `Guest`.
- `Expand sidebar` / `Collapse sidebar`.

### Summary

- 10 changes proposed. 0 breaking. All copy-only.
- Theme: strip Title Case inflation from two-word actions (`Quick Start` → `Quick start`, `New Resume` → `New resume`), collapse vestigial "proposal" language, trim tooltip verbs.
- One product question to settle: **Proposals vs Cover letters.** That's not voice, that's IA. Decide before sweeping the rest of the app or you'll do this twice.

---

## Next action

1. Save the voice card.
2. Decide: `Cover letters` vs `Proposals` as canonical product term. This affects every page.
3. Run the application-brief prompt (from my prior message) against **JobsPage** next — it's the largest surface and the highest-impact page for voice.

Want me to produce the JobsPage audit table next, or settle the `Cover letters`/`Proposals` IA question first?