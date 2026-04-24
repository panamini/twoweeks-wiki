

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