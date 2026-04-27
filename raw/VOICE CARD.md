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

Have enough. Here's the JobsPage audit. Source: `my-app/src/pages/JobsPage.tsx`.

---

## JobsPage audit table

| file:line    | current                                                                                                  | surface               | proposed                                 | note                                                                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------- | --------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| :559, :1702  | `Jobs`                                                                                                   | page-title (h1)       | keep                                     | on brand                                                                                                                          |
| :1703–1706   | `Reopen opportunities, review trust, and launch document work without turning the workspace into a CRM.` | page-subtitle         | `Saved jobs. Review. Act.`               | 24 words → 4. Declarative. Removes the clever-but-wordy CRM line. If that joke is a brand hill, alt: `Saved jobs. No CRM energy.` |
| :1675        | `Loading…`                                                                                               | status-msg            | `Loading`                                | voice rule: no ellipsis                                                                                                           |
| :1677        | `Sign in to view jobs.`                                                                                  | auth-status           | `Sign in to see jobs.`                   | period ok (full sentence). "view" → "see" is warmer, less corporate                                                               |
| :1718        | `Loading jobs…`                                                                                          | loading               | `Loading jobs`                           | no ellipsis                                                                                                                       |
| :1751–1752   | `Search jobs`                                                                                            | placeholder / aria    | keep                                     | on brand                                                                                                                          |
| :1766–1769   | `Recent activity` / `Oldest first` / `Title` / `Company`                                                 | select-options        | keep                                     | correct                                                                                                                           |
| :1774        | `{n} jobs`                                                                                               | count                 | keep                                     | numerals, no fluff                                                                                                                |
| :1775        | `{n} of {total}`                                                                                         | count                 | keep                                     |                                                                                                                                   |
| :1793, :1809 | `Active` / `Archived`                                                                                    | filter-chip           | keep                                     |                                                                                                                                   |
| :1829        | `All tiers`                                                                                              | filter-chip           | keep                                     |                                                                                                                                   |
| :1847–1848   | `Match —` / `Match Strong` / `Match Partial` / `Match Weak`                                              | filter-chip           | keep                                     | correct                                                                                                                           |
| :1862        | `Has docs`                                                                                               | filter-chip           | keep                                     |                                                                                                                                   |
| :1876        | `Needs review`                                                                                           | filter-chip           | keep                                     |                                                                                                                                   |
| :1888        | `Favorites`                                                                                              | filter-chip           | keep                                     |                                                                                                                                   |
| :1897–1899   | `No archived jobs` / `No jobs match this search`                                                         | empty-state-title     | keep / keep                              | both on brand                                                                                                                     |
| :1902–1904   | `Archived jobs will appear here after you archive them.`                                                 | empty-subtitle        | `Archive a job to see it here.`          | flip passive → declarative                                                                                                        |
| :1902–1904   | `Try a broader query or reset the trust filter.`                                                         | empty-subtitle        | `Try a wider search.`                    | 9 words → 4. "trust filter" is internal language                                                                                  |
| :1911        | `Untitled job`                                                                                           | fallback-title        | `Untitled job`                           | sentence case, keep                                                                                                               |
| :1912        | `Unknown company`                                                                                        | fallback-company      | keep                                     |                                                                                                                                   |
| :667         | `Location unavailable`                                                                                   | fallback-location     | keep                                     |                                                                                                                                   |
| :1919        | `Recent`                                                                                                 | date fallback         | keep                                     |                                                                                                                                   |
| :1948        | `Sample`                                                                                                 | badge                 | keep                                     |                                                                                                                                   |
| :1953        | `Favorite`                                                                                               | badge                 | keep                                     |                                                                                                                                   |
| :1973        | `Last activity {date}`                                                                                   | meta                  | keep                                     |                                                                                                                                   |
| :1977–1978   | `Needs review`                                                                                           | aria/title            | keep                                     |                                                                                                                                   |
| :1992        | `Remove {title} from favorites`                                                                          | aria-label            | keep                                     | aria convention                                                                                                                   |
| :1993        | `Mark {title} as favorite`                                                                               | aria-label            | keep                                     | aria convention                                                                                                                   |
| :1997        | `Remove from favorites`                                                                                  | tooltip               | keep                                     | 3 words, on brand                                                                                                                 |
| :1998        | `Mark favorite`                                                                                          | tooltip               | keep                                     | 2 words                                                                                                                           |
| :2032        | `Remove attached resume`                                                                                 | aria-label            | keep                                     |                                                                                                                                   |
| :2033        | `Open resume picker`                                                                                     | aria-label            | `Attach resume`                          | shorter, matches visible chip label                                                                                               |
| :2072        | `Attached resume: {name}`                                                                                | aria-label            | keep                                     | accurate                                                                                                                          |
| :2073, :2092 | `Attach a resume`                                                                                        | aria-label            | `Attach resume`                          | drop the article, 4→2 words                                                                                                       |
| :2084        | `Attach CV`                                                                                              | chip-label            | `Attach resume`                          | product uses "resume" everywhere else — standardize. "CV" survives only in CvForge's name                                         |
| :2100–2101   | `No local resumes found yet. Create or import one in CvForge.`                                           | empty-state (popover) | `No resumes yet. Create one in CvForge.` | 11 → 7 words. Drops "local" jargon                                                                                                |
| :2119        | `Attach {title}`                                                                                         | aria-label            | keep                                     |                                                                                                                                   |
| :2153        | `More actions for {title}`                                                                               | aria-label            | keep                                     | aria convention                                                                                                                   |
| :2173        | `Actions for {title}`                                                                                    | aria-label (menu)     | keep                                     | aria convention                                                                                                                   |
| :2190        | `Open source`                                                                                            | menu-item             | keep                                     |                                                                                                                                   |
| :2206        | `Archive`                                                                                                | menu-item             | keep                                     |                                                                                                                                   |
| :2222        | `Duplicate`                                                                                              | menu-item             | keep                                     |                                                                                                                                   |
| :2240        | `Restore`                                                                                                | menu-item             | keep                                     |                                                                                                                                   |
| :2260        | `Confirm delete`                                                                                         | menu-item             | `Confirm`                                | inside a 2-button confirm flow, "Confirm" alone is enough — the sibling is `Cancel`                                               |
| :2277        | `Cancel`                                                                                                 | menu-item             | keep                                     |                                                                                                                                   |
| :2296        | `Delete permanently`                                                                                     | menu-item             | `Delete forever`                         | "forever" is stronger, shorter, and less corporate than "permanently". Stays unambiguous                                          |
| :2322        | `Loading job…`                                                                                           | empty-state           | `Loading job`                            | no ellipsis                                                                                                                       |
| :2327        | `Job unavailable`                                                                                        | empty-state-title     | keep                                     |                                                                                                                                   |
| :2330–2331   | `This job could not be loaded. Open another job from the list to continue.`                              | empty-state-subtitle  | `Could not load this job. Open another.` | 14 → 7 words                                                                                                                      |
| :2348        | `Back to jobs`                                                                                           | button                | keep                                     |                                                                                                                                   |
| :2355        | `Untitled job`                                                                                           | fallback-title        | `Untitled job`                           |                                                                                                                                   |
| :2358        | `Sample`                                                                                                 | badge                 | keep                                     |                                                                                                                                   |
| :2363        | `Favorite`                                                                                               | badge                 | keep                                     |                                                                                                                                   |
| :2369        | `Unknown company`                                                                                        | fallback              | keep                                     |                                                                                                                                   |
| :2391        | `Remove job from favorites`                                                                              | aria-label            | keep                                     |                                                                                                                                   |
| :2392        | `Mark job as favorite`                                                                                   | aria-label            | keep                                     |                                                                                                                                   |
| :2396        | `Remove from favorites`                                                                                  | tooltip               | keep                                     |                                                                                                                                   |
| :2397        | `Mark favorite`                                                                                          | tooltip               | keep                                     |                                                                                                                                   |
| :2444        | `Generate cover letter`                                                                                  | next-step-action      | keep                                     | matches canonical product term                                                                                                    |
| :2446        | `Open resume with this job`                                                                              | next-step-action      | keep                                     | already landed per prior spec                                                                                                     |
| :2447        | `Add to favorites`                                                                                       | next-step-action      | `Mark favorite`                          | consistency with row tooltip; shorter                                                                                             |
| :1608        | `Archive failed`                                                                                         | toast-title           | keep                                     | 2 words, on brand                                                                                                                 |
| :1610        | `Could not archive this job.`                                                                            | toast-description     | `Try again.`                             | voice rule: no apology, fixable hint only. If the retry is not available, drop this line entirely                                 |
| :1625        | `Restore failed`                                                                                         | toast-title           | keep                                     |                                                                                                                                   |
| :1627        | `Could not restore this job.`                                                                            | toast-description     | `Try again.`                             |                                                                                                                                   |
| :1641        | `Delete failed`                                                                                          | toast-title           | keep                                     |                                                                                                                                   |
| :1643        | `Could not delete this job.`                                                                             | toast-description     | `Try again.`                             |                                                                                                                                   |
| :1664        | `Duplicate failed`                                                                                       | toast-title           | keep                                     |                                                                                                                                   |
| :1666        | `Could not duplicate this job.`                                                                          | toast-description     | `Try again.`                             |                                                                                                                                   |
| :1346        | `error.message` fallback                                                                                 | toast                 | keep                                     | dynamic, can't standardize without context                                                                                        |
| :1381        | `Could not detach the resume.`                                                                           | toast fallback        | `Detach failed. Try again.`              | standardize to the two-word-title + short-action pattern                                                                          |
| :1424        | `Could not update favorite.`                                                                             | toast fallback        | `Favorite update failed.`                | 3 words                                                                                                                           |

### Debug / dev surfaces (do not touch)

- `:271, :292, :300, :313–340, :471–531, :484–520` — all behind `isJobsMatchInputDebugEnabled`. Leave as-is.

### Flagged-ambiguous (decide before sweep)

1. **`Saved jobs. Review. Act.` vs keeping the CRM joke.** The original subtitle is distinctive. My proposal is brand-correct but colder. If the subtitle is load-bearing brand personality, alt: `Saved jobs. Not a CRM.` — keeps the joke, kills 80% of the words.
2. **`Attach CV` → `Attach resume`.** If you're keeping "CV" as the user-facing term in CvForge's brand (it's the page name), then mixed vocabulary is fine and you'd keep `Attach CV` here. Pick one word app-wide: resume OR CV. Don't mix.
3. **`Delete forever` vs `Delete permanently`.** "forever" is more Twoweeks. "permanently" is more legalese. If users associate permanently with accounting-grade certainty, keep it. Low-stakes call.
4. **Error descriptions uniformly → `Try again.`** This assumes retry will work. If some failures are not retry-safe (e.g., already-archived), `Try again.` is wrong. Audit the mutations. If retry safe across the board → sweep. If not → keep specific descriptions only for non-retryable cases.

### Summary

- ~20 meaningful changes.
- ~35 items kept as-is (already on brand).
- Three theme moves: ellipsis removal, article/preposition trim, error-description collapse to `Try again.`.
- One IA question to settle before sweep: **Resume vs CV as the app-wide noun.** Same class of decision as `Cover letters` vs `Proposals`. Pick one.

---

## Your next action

1. Decide: **Resume or CV** as the single noun. My vote: `Resume` (stronger, shorter, no acronym). Leave `CvForge` as a product-name holdover if you don't want to rename the page.
2. Decide: subtitle tone — clean declarative (`Saved jobs. Review. Act.`) or keep the CRM joke (`Saved jobs. Not a CRM.`).
3. Apply the approved table as one commit: `chore(jobs): apply Twoweeks voice to JobsPage copy`. No logic changes, copy only.
4. Next page to audit: **CvForge**, where the Resume/CV decision will cascade heaviest. Or the match/next-step blocks since those are high-traffic read surfaces.

Which next — CvForge, 



---

## CvForge audit — `my-app/src/pages/CvForge.tsx`

### Resume/CV IA decision — cascades heaviest here

CvForge already tilts hard toward **resume** in visible copy (aria-labels, tooltips, export filenames, status strings). Only one visible string says `CV`: the export-guard toast on line 384. Internal identifiers (`CvForge`, `cv-*` classes, `currentCv`, `cvId`, context) stay as `cv` — that is not brand-facing.

**Recommendation: lock `resume` as the canonical user-facing noun app-wide.** `CV` stays as internal code, filename, component name, and URL path (if routed `/cv`). This audit assumes that decision. If you reverse it, the flipped items are the bottom 3 rows of the table.

---

### Audit table

|file:line|current|surface|proposed|note|
|---|---|---|---|---|
|CvForge.tsx:73–75|`Style 1` / `Style 2` / `Style 3`|preset-slot default label|keep|correct: Title Case + numerals, on brand|
|CvForge.tsx:366|`ATS Ready`|status label|keep|2-word Title Case, on brand|
|CvForge.tsx:366|`Standard Export`|status label|`Standard export`|sentence case — `Export` as noun inflates it; `Standard export` is the parallel to `ATS Ready`|
|CvForge.tsx:368|`Trusted Mistral v3`|status description|`Mistral v3` or keep|`Trusted` is adjective-as-value-claim; vendor-name-only is cleaner. Flagged — keep if "Trusted" is a feature flag the user should recognize|
|CvForge.tsx:369|`Not ATS-verified`|status description|keep|declarative fact, 2 words, on brand|
|CvForge.tsx:384|`Open or create a CV before exporting`|toast (warning)|`Open a resume first.`|current: 8 words, CV+resume collision, trails without period. Proposed: 4 words, single noun, terminal period, declarative. Fact-stating|
|CvForge.tsx:451|`Resume - Editable`|export filename|keep|filename convention, already on brand|
|CvForge.tsx:453|`Resume - ATS`|export filename|keep||
|CvForge.tsx:454|`Resume - Styled`|export filename|keep||
|CvForge.tsx:488|`Exported ${filename}`|toast (success)|`Exported.`|success toast rule: one word. Filename is already in the download; announcing it bloats the toast. Flagged — keep verbose if user relies on the toast to confirm _which_ file (unlikely since there is only one download)|
|CvForge.tsx:491|`Resume export failed`|toast (error)|`Export failed.`|failure rule: 2–3 words. `Resume` is implied by context (user just clicked export on a resume). Terminal period|
|CvForge.tsx:539|`Open saved resume styles`|aria-label|keep|aria convention; accurate|
|CvForge.tsx:540|`Open resume style controls`|aria-label|keep|aria convention|
|CvForge.tsx:542|`Saved styles`|toolbar tooltip|keep|2 words, no period, on brand|
|CvForge.tsx:543|`Style controls`|toolbar tooltip|keep|2 words, on brand|
|CvForge.tsx:578|`Saved resume styles`|menu aria-label|keep|aria convention|
|CvForge.tsx:604|`No saved style`|slot empty state|keep|3 words, declarative, on brand|
|CvForge.tsx:660|`Open resume preview`|aria-label|keep|aria convention|
|CvForge.tsx:662|`Switch to preview`|toolbar tooltip|`Preview`|tooltip rule: 4 words max, no verb padding. `Preview` alone is the paired action label to `Edit`|
|CvForge.tsx:673|`Back to resume editing`|aria-label|`Open resume edit`|aria should state the action, not the navigation. The button doesn't "go back" — it switches workspace mode|
|CvForge.tsx:675|`Back to edit`|toolbar tooltip|`Edit`|parallel to the `Preview` proposal above. One word each|
|CvForge.tsx:684|`More export formats`|menu label (passed to ResumeExportControl)|keep|accurate, 3 words|

---

### Theme moves

1. **Drop "Switch to" / "Back to" verb padding** on toolbar tooltips → single-noun labels (`Edit`, `Preview`). Matches the sidebar-mode compression already in the voice card.
2. **Filename-stuffed success toast** → one-word `Exported.` per toast rule.
3. **Error toasts to 2-word form** — `Export failed.` not `Resume export failed`.
4. **Status description sentence-case** — `Standard export` not `Standard Export`.

### Flagged-ambiguous

1. **`Trusted Mistral v3`** — if `Trusted` is user-meaningful (i.e., a different badge from `Standard Export` that the user should recognize as quality assurance), keep it. If it's just marketing, drop to `Mistral v3`. Voice card leans drop, but this is a data-meaning call, not a copy call.
2. **`Exported ${filename}` → `Exported.`** — reversible only if you have user research showing people read the toast for filename confirmation. My default recommendation: drop. Filename already lands on the filesystem; toast is ceremonial.
3. **`Resume/CV` IA** — if reversed (canonical = `CV`), only these flip:
    - line 384 stays `Open or create a CV before exporting` → `Open a CV first.`
    - Aria labels and filenames flip `resume` → `CV`.
    - Voice-card banned/allowed lists would swap `Resume` → `CV`. Not recommended — `Resume` is the US/global-search canonical; `CV` is EU/academic. Given Twoweeks.ai targets job-seekers, `Resume` wins.

### Stats

- User-facing strings audited: **22**
- Proposed changes: **7** (1 toast, 2 tooltips, 1 aria-label, 1 status description, 2 toast messages)
- Kept as-is: **15** (mostly aria-labels, preset slot defaults, export filenames, already-compliant labels)

### Count reality

CvForge is the thinnest page in the audit chain because the CV editing surface lives in `ProfileReviewCard` and `VerbatiCvPreviewPanel` — those are where the bulk of resume-page copy lives (field labels, section titles, inline affordances). The JobsPage/Sidebar pattern of ~20-change-per-page will not repeat until we hit those two.

### Suggested commit

```
chore(cv): apply Twoweeks voice to CvForge page chrome

- Toast copy: compress warning + error + success to 1–4 words, terminal period
- Tooltips: drop verb padding (`Switch to preview` → `Preview`)
- Status description: sentence case (`Standard export`)
- Preserve all aria-labels (screen-reader convention wins per voice card)
```

### Next audit targets (in order of bang-per-buck)

1. **`ProfileReviewCard.tsx`** — biggest resume-surface copy landmine. Field labels, section headers, inline prompts, add/remove affordances. This is where Resume/CV IA decision will show its full cascade.
2. **`VerbatiCvPreviewPanel.tsx`** — preview chrome, export buttons, style switcher copy.
3. **Job-detail blocks** — `MatchReadBlock.tsx` + `NextStepBlock.tsx` (both short, high-visibility).
4. **FirstRunPanel + ProposalInputForm** — empty states and the largest user-facing form in the app.

Lock the Resume/CV IA call and I'll start on `ProfileReviewCard`.

----
3197 lines — the big one. Let me extract user-facing strings systematically.

Voice card saved. ProfileReviewCard is the big one — 3,197 lines, ~60 distinct user-facing strings. Audit below, grouped by surface cluster for scannability.

---

## ProfileReviewCard audit — `my-app/src/components/ProfileReviewCard.tsx`

### Resume/CV IA — heaviest offender in the app

This file says `CV` **8 times in user-visible copy** (toasts, dialog title, button label, empty-state title, empty-state body). Per the locked decision (`resume` = canonical user-facing noun), every one of these flips. Internal identifiers (`currentCv`, `cvId`, `.cv-*` classes, `CvForge` component name, `cv-library` context) remain unchanged.

### Cover letter vs proposal — second IA fix

The empty-state subtitle and the import-review summary both say `proposals` ("before generating proposals"). Per locked decision: canonical term is `cover letter`. Both flip.

### Debug surface exclusion

Lines 460–625 (`ImportRuntimeDebugControls`, `importModeLabel`, copy-JSON buttons) render only when `DEBUG_CV_EDITOR` is true. Not user-facing → excluded from brand audit. Leave as-is.

---

### Audit table — visible copy

|file:line|current|surface|proposed|note|
|---|---|---|---|---|
|**Section catalog labels** (lines 777–879)|||||
|:803, :809, :815, :821, :827, :833, :839, :845|`Summary` / `Experience` / `Achievements` / `Education` / `Skills` / `Languages` / `Projects` / `Certifications`|section label|keep|standard resume nouns, 1-word Title Case, on brand|
|:863|`Affiliations`|section label|keep||
|:864|`Memberships and associations`|description|`Memberships and groups`|3 words, drops "and" chain|
|:871|`Hobbies`|section label|keep||
|:872|`Interests and personal activities`|description|`Interests and activities`|drop "personal" — redundant with "interests"|
|:855|`Additional Information` (constant)|section label|keep|standard resume heading|
|:856|`Extra details and references`|description|`Extras and references`|compress|
|:879|`Add your own`|custom section label|keep|3 words, verb-first, on brand|
|:880|`Create a custom titled section`|description|`Custom section title`|placeholder rule: mirror the field, drop "create a"|
|**Review / recovery labels** (lines 1110–1120)|||||
|:1111|`Review flagged fields again`|button label|`Review again`|2 words suffices once user's done a first review|
|:1112|`Review flagged fields`|button label|`Review flags`|2 words; `flags` matches pill vernacular|
|:1114|`Close recovery workspace`|button label|`Close recovery`|drop "workspace" — redundant|
|:1116|`Reopen recovery workspace`|button label|`Reopen recovery`|same|
|:1117|`Resume recovery review`|button label|`Open recovery`|`Resume` verb collides with `resume` noun; `review` trails. Action is "open the recovery panel"|
|:1120|`Review import changes`|button label|`Review import`|drop "changes" — implicit|
|**Rename dialog** (lines 2427–2429)|||||
|:2427|`Rename CV`|dialog title|`Rename resume`|IA flip|
|:2428|`e.g. Jane Doe — Product Manager`|placeholder|`Jane Doe — Product Manager`|placeholder rule: mirror the field, no `e.g.`|
|:2429|`Save title`|button|`Save`|1-word verb, button rule; `title` implicit from dialog|
|**Inline import review** (lines 2483–2553)|||||
|:2483|`Import review` (eyebrow)|eyebrow label|keep|2 words, Title Case, on brand|
|:2486|`Clean flagged parser noise here before generating proposals.`|section subtitle|`Clean flagged fields before drafting.`|5 words. Drops "parser noise" (engineer-speak), drops "proposals" (vestigial), declarative. `drafting` = cover-letter-agnostic verb|
|:2497|`Review acknowledged`|status chip|keep|2 words, on brand|
|:2498|`Review required before export`|status chip|`Review required`|2 words; `before export` obvious from context|
|:2505|`Open import review`|aria-label|keep|aria convention|
|:2506|`Close import review`|aria-label|keep|aria convention|
|:2552, :2627|`Discard recovery`|button|keep|2 words, verb-first, on brand|
|**Recovery resume banner** (lines 2595–2599)|||||
|:2595|`Import recovery`|eyebrow|keep|on brand|
|:2598|`Recovery review saved — reopen ${N} reviewed item${s}`|banner title|`Recovery saved. Reopen ${N} reviewed.`|4 words + count. Drops em-dash (brand forbids em-dash in headlines), period rhythm, drops second `item(s)`|
|:2599|`Import review incomplete — ${N} item${s} pending`|banner title|`Review incomplete. ${N} pending.`|same treatment; drops redundant `item(s)`|
|:2632|`Dismiss recovery banner`|aria-label|keep|aria convention|
|**Empty state (no CV loaded)** (lines 2717–2762)|||||
|:2717|`Import your existing CV or start from scratch.`|empty-state title|`No resume. Import or start fresh.`|6 words across 2 clauses. IA flip (CV→resume). `start from scratch` → `start fresh` (3 words → 2)|
|:2720|`Bring in an existing resume, begin a clean draft, or open one from the library before generating proposals.`|empty-state subtitle|`Paste a file. Draft from zero. Open library.`|8 words, 3 sentences, period rhythm. Drops "proposals". Drops "before generating" (purpose-stating, banned coaching)|
|:2735|`Import CV`|button label|`Import resume`|IA flip|
|:2754|`Start from scratch`|button|`Start fresh`|compress; parallels title|
|:2761|`Open library`|button|keep|2 words, verb-first, on brand|
|**Toolbar** (lines 2805–2951)|||||
|:2802|`Organize sections`|aria-label + button|keep|2 words, verb-first, on brand|
|:2805|`MOVE. HIDE.`|toolbar tooltip (organize mode)|keep|marketing-rhythm all-caps + period, on brand — rare in UI but deliberate|
|:2819|`Reset to recommended/default order`|button|`Reset order`|2 words; "recommended/default" is implementation detail|
|:2832, :2843|`Manage sections`|aria-label + label|keep|on brand|
|:2861|`Add sections`|menu heading|keep|on brand|
|:2898|`Remove optional sections`|menu heading|`Remove sections`|drop "optional" — only removable sections appear in this group|
|:2914|`Remove ${sectionLabel}`|menu item|keep|verb-first, dynamic|
|:2930|`Remove all optional sections`|menu item|`Remove all`|2 words; `sections` implicit from menu heading|
|:2941|`All optional sections are already configured.`|menu empty state|`All sections added.`|3 words, fact-stating, matches `:2949`|
|:2949|`All sections added.`|toolbar hint|keep|on brand|
|**Empty section states** (lines 3070–3110)|||||
|:3070|`No sections yet — add one below`|empty state|`No sections. Add one below.`|period rhythm, drop em-dash|
|:3106|`All editable sections are hidden from the live preview.`|empty state line 1|`All sections hidden.`|3 words, fact-stating. `editable` implicit in this context; `live preview` obvious|
|:3109|`Open Organize sections to show them again.`|empty state line 2|`Open organize to show them.`|5 words; `Organize` is a known UI noun in this page|
|**Drag handle** (line 2180)|||||
|:2180|`Drag ${section.title}`|aria-label|keep|aria convention, dynamic|
|**Debug surface aria-labels** (lines 511–618)|||||
|:511, :595, :606, :618|`Import runtime debug` / `Copy normalized JSON` / `Copy raw parser JSON` / `Copy raw text`|aria-label|keep|DEBUG_CV_EDITOR gated — not user-facing|
|**Toasts** (see separate cluster below)|||||

---

### Toast audit (all via `pushToast()`, lines 1332–2417)

Current toasts are a mix of instructive sentences, declarative fragments, and inconsistent periods. Voice rule: **success = 1 word, failure = 2–3 words, terminal period on both**.

|file:line|current|proposed|note|
|---|---|---|---|
|:1389|`Failed to clear recovery`|`Clear failed.`|2 words, terminal period|
|:1514|`Review the flagged fields before exporting this CV.`|`Review flags first.`|3 words; drops "this CV" (IA flip + implicit)|
|:1530|`CV title updated`|`Renamed.`|1-word success, IA flip dissolved|
|:1538|`No importable sections were found`|`Nothing to import.`|3 words, fact-stating|
|:1573|`Failed to import CV`|`Import failed.`|2 words, IA flip dissolved|
|:1677|`Failed to apply reviewed import`|`Apply failed.`|2 words|
|:1879|`Import cancelled`|`Cancelled.`|1-word success; `import` obvious from context|
|:1884|`Recovery cleared`|`Cleared.`|1-word success|
|:2252|`Choose a section type to add`|`Pick a section.`|3 words; no "type", no coaching verb|
|:2273|`Section "${type}" already exists`|`"${type}" exists.`|2 words + token|
|:2285|`Section name is required`|`Name required.`|2 words|
|:2298|`Section "${requestedTitle}" already exists`|`"${requestedTitle}" exists.`|same as 2273|
|:2332|`Section type "${type}" is not available`|`"${type}" unavailable.`|2 words + token|
|:2342|`Failed to create section`|`Create failed.`|2 words|
|:2355|`${newSection.title||option.label} added`|
|:2361|`Failed to add section`|`Add failed.`|2 words|
|:2370, :2379|`No added sections to remove`|`Nothing to remove.`|3 words|
|:2384|`Core sections must remain in the CV`|`Core sections are required.`|4 words. IA flip; drops prescriptive "must remain". If we want tighter: `Required section.` (2 words)|
|:2391|`Added sections removed`|`Removed.`|1-word success|
|:2397|`Choose a section to remove`|`Pick a section.`|mirrors :2252|
|:2406|`Section not found`|keep|3 words, declarative, on brand|
|:2417|`${removedLabel} removed`|keep|dynamic + 1-word success tag|

---

### Theme moves

1. **CV → resume, 8 sites.** Biggest single cascade in the file; all in live UI (toasts, dialog title, button, empty states). Not touching internal symbols.
2. **"proposals" → dropped or replaced by `drafting` / `cover letter`** at 2 sites (empty-state subtitle, inline-review summary).
3. **Toast compression to 1–3 words with terminal period.** 17 toasts rewritten; average drops from 5.8 → 2.3 words.
4. **Empty-state subtitle radical compression.** 20-word paragraph → 8-word 3-sentence block. Matches voice-card rule (2–3 supporting lines, 4 words each max).
5. **Drop redundant compound nouns.** `recovery workspace` → `recovery`. `optional sections` → `sections`. `live preview` → dropped (implicit). Saves ~30 words across the file.
6. **Em-dash in UI body titles → period rhythm.** Two recovery banner lines + one empty state. Brand allows em-dash in example strings (the placeholder `Jane Doe — Product Manager` keeps it) but not in UI headlines.

### Flagged-ambiguous

1. **`Core sections are required.`** vs **`Required section.`** (line 2384) — the longer form explains _why_ the removal was blocked (it's a core section). The shorter is more on-brand but less helpful when users hit it the first time. Recommendation: keep `Core sections are required.` — error-as-teaching exception.
2. **`Drafting`** as verb in the inline-review subtitle (line 2486) — I used it as a cover-letter-agnostic verb covering both cover letter and export. If you want explicit IA, swap to `before drafting a cover letter.` (6 words, still compliant).
3. **`Start fresh`** vs **`Start from scratch`** (line 2754) — I compressed. `From scratch` has a slightly punchier, anti-corporate-coach feel that might be worth keeping. Flip-a-coin call.
4. **`Open recovery`** (line 1117) — I proposed replacing `Resume recovery review` because `Resume` (verb) collides with `resume` (noun). If the recovery flow has a "first-time" vs "reopen" distinction, we need two labels, not one. Needs a data-meaning check.

### Stats

- User-facing strings audited: **~62**
- Proposed changes: **~42** (17 toasts, 8 IA flips, 3 empty-state rewrites, 6 compressions, 8 misc)
- Kept as-is: **~20** (section labels, aria-labels, on-brand buttons, dynamic tokens, debug surfaces)

### Suggested commit plan

This page is too big for a single commit. Split:

```
chore(cv): IA flip CV → resume across ProfileReviewCard visible copy   (~8 strings)
chore(cv): compress ProfileReviewCard toasts to brand voice             (~17 strings)
chore(cv): rewrite ProfileReviewCard empty states + inline review       (~10 strings)
chore(cv): compress ProfileReviewCard toolbar + menu labels             (~7 strings)
```

Each commit is mechanical and independently revertable. The IA flip commit should land first — it's the most controversial if we get the IA call wrong, and it's cheapest to reverse.

### Next audit targets

1. **`VerbatiCvPreviewPanel.tsx`** — the other half of the resume-editing workspace. Preview chrome + style switcher strings. Will finish the CvForge cluster.
2. **Job-detail blocks** — `MatchReadBlock.tsx` + `NextStepBlock.tsx`. Short files, high visibility (every open job shows them).
3. **`FirstRunPanel.tsx`** — onboarding copy; biggest first-impression lever.
4. **`ProposalInputForm.tsx`** — largest form in the app, mixed proposal/cover-letter vestigial language.

Ready for VerbatiCvPreviewPanel when you are.

---
## VerbatiCvPreviewPanel audit — `my-app/src/features/verbati/VerbatiCvPreviewPanel.tsx`

490 lines, ~18 user-facing strings. Thin file but dense with CV/resume collisions in aria-labels and tooltips — this is the second-heaviest IA cascade in the app.

### Resume/CV IA — 13 sites

Every occurrence of `CV` or `Active CV` or `Sample CV` in user-visible or screen-reader copy flips to lowercase `resume`. No internal symbols touched (`currentCv`, `CvDocument`, `cvDocumentOverride`, `isActivePreview`, `hasCurrentCv` all stay).

`Verbati` is an internal feature name (design system / preview engine); never shown to end users except via this `Verbati sample CV` tooltip. I'm treating it as not-for-users and dropping it from the tooltip entirely.

---

### Audit table

|file:line|current|surface|proposed|note|
|---|---|---|---|---|
|:235|`Previous style`|fallback label|keep|2 words, on brand|
|:242|`Next style`|fallback label|keep|on brand|
|:262|`Switch resume styles`|group aria-label|keep|aria convention, accurate|
|:275|`Show previous resume style: ${previousBundleLabel}`|button aria-label|`Previous style: ${previousBundleLabel}`|`Show` is verb padding; aria still describes the action via button role|
|:276|`${previousBundleLabel}`|toolbar tooltip|keep|dynamic bundle name|
|:284|`Show next resume style: ${nextBundleLabel}`|button aria-label|`Next style: ${nextBundleLabel}`|same pattern|
|:285|`${nextBundleLabel}`|toolbar tooltip|keep|dynamic|
|:310|`Switch to sample preview`|aria-label|`Show sample resume`|drops "Switch to" verb padding; IA flip|
|:312|`Switch to active CV preview`|aria-label|`Show your resume`|drops "Switch to"; IA flip; `your` is the only second-person in the file — justifies the disambiguation from the sample|
|:313|`Active CV preview unavailable`|aria-label (disabled)|`Resume unavailable`|IA flip, drops "active preview"|
|:317|`Preview the sample CV`|title tooltip|`Sample resume`|2 words, drops verb, IA flip|
|:319|`Preview the active CV`|title tooltip|`Your resume`|2 words, parallel to above|
|:320|`Active CV preview unavailable`|title tooltip|`Unavailable`|1 word; context ("preview") is redundant with the surface|
|:341|`Previewing active CV`|aria-label|`Your resume`|same pattern|
|:343|`Previewing sample CV`|aria-label|`Sample resume`|same pattern|
|:344|`Previewing sample CV because the active CV is unavailable`|aria-label|`Sample resume. Your resume is unavailable.`|6 words across 2 sentences; period rhythm; drops "because" coaching|
|:348|`currentCv?.title ?? "Active CV"`|title fallback|`currentCv?.title ?? "Your resume"`|IA flip|
|:349|`Verbati sample CV`|title|`Sample resume`|drops `Verbati` (internal name), IA flip|
|:354|`currentCv?.title ?? "Active CV"`|chip label|`currentCv?.title ?? "Your resume"`|IA flip; matches :348|
|:354|`Sample CV`|chip label|`Sample resume`|IA flip|
|:374–375|`The active CV is still too sparse for a faithful render. Add enough profile, summary, or experience content to stabilize the live preview.`|warning block|`Resume too sparse. Add profile, summary, or experience.`|7 words; 2 sentences; drops "faithful render" + "stabilize" (corporate filler); IA flip. Action is implicit in the list|

---

### Theme moves

1. **Drop "Switch to" / "Preview the" / "Show" verb padding** on aria-labels and tooltips. The buttons are already buttons — aria role does the work. One-noun or two-word labels match voice card.
2. **CV → resume across 13 surfaces** — tooltips, aria-labels, chip labels, fallback titles.
3. **Collapse 25-word sparse-resume warning → 7-word declarative block.** Drops "faithful render", "stabilize", "live preview" — all corporate filler or redundant context.
4. **Drop internal brand name `Verbati` from user-visible tooltip.** Product-design artifact leaking into user copy.
5. **`Your resume` vs `Active resume`** — the one site of second-person in the file. Justified here because `active` is internal-state vocabulary (active vs sample) that means nothing to the user; `your` is the direct counterpoint to `sample`.

### Flagged-ambiguous

1. **`Your resume` vs `Active resume`** — voice card rarely uses second person. The user/sample disambiguation is real though, and `Your resume` reads more natural than `Current resume`. Flipping to `Current resume` if you want to stay away from second person everywhere. My call: `Your resume` wins here precisely because of the sample-vs-real distinction.
2. **`Verbati sample CV` → `Sample resume`** — if `Verbati` is a user-facing brand (e.g., shows up in docs / marketing / onboarding), we should keep it. My read is it's an internal feature name. Confirm before shipping.
3. **Button cycle aria-labels** (`:275`, `:284`) — `Previous style: ${label}` vs `Previous: ${label}` (one word shorter). Accessibility convention favors the more descriptive form when the bundle label alone could be ambiguous. Keep `style`.

### Stats

- User-facing strings audited: **~19**
- Proposed changes: **~16** (13 IA flips, 2 verb-padding drops, 1 sparse-resume rewrite)
- Kept as-is: **3** (fallback labels, group aria-label, dynamic bundle names)

### Suggested commit

```
chore(cv): apply Twoweeks voice to VerbatiCvPreviewPanel

- IA flip: CV → resume across 13 aria-labels, tooltips, chip labels
- Drop verb padding (Switch to / Preview the / Show) from aria/tooltips
- Collapse sparse-resume warning from 25 → 7 words
- Drop internal "Verbati" name from user-visible sample tooltip
```

---

### CvForge cluster — status

With this, the CvForge page cluster is complete at the page-chrome level:

|File|Audited|Change count|
|---|---|---|
|`CvForge.tsx`|✓|~7|
|`ProfileReviewCard.tsx`|✓|~42|
|`VerbatiCvPreviewPanel.tsx`|✓|~16|

Deeper surfaces still to audit inside the resume editor (lower-urgency, higher-volume):

- `VerbatiResumePreview.tsx` (preview chrome on the rendered resume)
- Section sub-components (`SummarySection`, `ExperienceSection`, etc. — field labels, add/remove affordances)
- `ImportWarningBanner.tsx`, `ImportRecoveryPanel.tsx` (banner copy)
- `StructuredUploadButton.tsx` (the `Import CV` entry point)
- `CvRenameDialog.tsx` (the rename dialog we flipped in ProfileReviewCard)
- `ResumeExportControl.tsx` (export menu + formats)
- `EmbeddedStyleInspector.tsx` (style picker labels)

### Recommended next audit targets — job-detail cluster

High visibility, short files, single-commit each:

1. **`MatchReadBlock.tsx`** — match explanation shown on every open job
2. **`NextStepBlock.tsx`** — cohort/common-steps block below match
3. **`FirstRunPanel.tsx`** — onboarding empty state, biggest first-impression lever
4. **`ProposalBriefCard.tsx`** — job brief card (vestigial "proposal" terminology likely)

Ready for MatchReadBlock when you are.

---
