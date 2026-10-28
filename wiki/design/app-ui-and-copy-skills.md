---
title: "App UI and copy skills"
category: design
status: current
created: 2026-10-28
updated: 2026-10-28
valid_from: 2026-10-28
tags: [ui, design-system, i18n, copy, skills, agents]
related: [[design/brand-voice]], [[design/locale-typography-rules]], [[design/motion-system]], [[design/elite-design-system]], [[strategy/language-localization]]
---

# App UI and copy skills

Two agent skills in the neyssan repo are the working guide for the twoweeks.ai
app interface and for its FR/EN/ES wording. Claude Code reads them from
`.claude/skills/`, Codex from `.agents/skills/` (relative symlinks to the same
files). They point to the source files that own each value instead of copying
values, so the code stays the truth.

## Current state

- Added on branch `claude/twoweeks-skills`, commit `e9f5477e2` (based on
  `origin/main` `91efe598e`), 2026-10-28. Not merged yet: until it is, the
  files exist only on that branch.
- **`twoweeks-ui`** — `.claude/skills/twoweeks-ui/SKILL.md`. Authority order,
  map of source files (`App.tsx`, `Sidebar.tsx`, `foundation.css`,
  `themes.css`, `product.css`, `src/components/ui`), routes, nav rail and the
  phone tab bar (≤599px), token names, z-index ladder, breakpoints, theming
  (light/dark/system, `pal-*` accents), primitives, and a checklist to verify
  a UI change (tokens, strings in the three languages, 375px, no overlap with
  the tab bar).
- **`twoweeks-i18n-copy`** — `.claude/skills/twoweeks-i18n-copy/SKILL.md`.
  Where each kind of string lives (`ui-messages.ts`, landing `locales.mjs`
  and its rebuild, marketing JSON, Chrome extension, Clerk), register (FR
  *vous*, ES *tú*), glossary, naming decisions, known inconsistencies.
- The `twoweeks-app-skeleton` skill (April–May 2026) is removed and
  superseded: it pointed to a deleted worktree and to the static
  `APP-SKELETON.html` refonte mock-up. Its source summary is archived:
  [[archive/sources/2026-04-30-two-weeks-app-skeleton-skill]].

## Details

Naming decisions of 2026-10-28 (detail and reasons in `twoweeks-i18n-copy`;
implemented on a separate branch):

- `/career` nav: Parcours / Career / Trayectoria (was Profil / Profile / Perfil).
- Settings account tab: Compte / Account / Cuenta (was Profil / Profile / Perfil).
- Settings voice tab: Ton d'écriture / Writing tone / Tono de escritura.
- Job action that archives a job: Pas pour moi / Not for me / No me interesa.
- Landing ES hero: always «carta de presentación» for the cover letter.
- Rule: never use the same label for two different destinations.

Drift noted while writing the skills (not fixed here):

- [[design/brand-voice]] asks for Title Case section headers and names
  *resume* as the canonical noun; the app uses sentence case and *CV* in
  navigation.
- In the repo, `docs/UI/*`, `docs/ui-claude/UI/*` and
  `my-app/DESIGN_SYSTEM.md` describe the spring 2026 design and are
  historical.

## Sources

- neyssan code at `origin/main` `91efe598e` (2026-10-28): `my-app/src/App.tsx`,
  `my-app/src/components/Sidebar.tsx`, `my-app/src/styles/foundation.css`,
  `my-app/src/styles/product.css`, `my-app/src/lib/i18n/ui-messages.ts`,
  `my-app/landing-brand-journey/locales.mjs`.

## Related

- [[design/brand-voice]] · [[design/locale-typography-rules]] ·
  [[design/motion-system]] · [[design/elite-design-system]] ·
  [[strategy/language-localization]]
