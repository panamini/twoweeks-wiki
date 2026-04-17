# Skills Howto

This repository ships two reusable skills.

Use them as workflow overlays, not as business logic by themselves.
They tell Codex how to operate on the repo with the twoweeks discipline.

## [$ingest-wiki](/Users/pana/.codex/skills/ingest-wiki/SKILL.md)

File:
- `SKILL.md`
- `skills/ingest-wiki/SKILL.md`

Use it when the task is about the knowledge plane:
- ingest files from `rawinput/`
- update or repair wiki pages
- run a wiki lint / health check
- save an answer or audit into `wiki/outputs/`

What it does:
- reads the wiki control files first
- prefers updating canonical pages over creating duplicates
- requires a short preflight on non-trivial work
- forces verification after ingest, direct-update, lint, and save-output work

Use this skill when the request is mainly about:
- `wiki/`
- `rawinput/`
- `raw/`
- `wiki/index.md`
- `wiki/log.md`

## [$apply-hybrid-code-layer](/Users/pana/.codex/skills/apply-hybrid-code-layer/SKILL.md)

File:
- `skills/apply-hybrid-code-layer/SKILL.md`

Use it when the task is about the code plane:
- audit a real code repository
- fix a bug
- add a feature
- refactor with verification
- benchmark or compare before/after behavior
- save an implementation or audit report

What it does:
- starts from manifests, tests, CI, and the smallest owning module
- requires a preflight before non-trivial code work
- pushes toward the smallest safe change
- requires concrete verification instead of unverified claims

Use this skill when the request is mainly about:
- source code
- tests
- CI / lint / build
- performance measurement
- implementation reports

## Which one to use

Use [$ingest-wiki](/Users/pana/.codex/skills/ingest-wiki/SKILL.md) for wiki mutations.

Use [$apply-hybrid-code-layer](/Users/pana/.codex/skills/apply-hybrid-code-layer/SKILL.md) for code work.

If a task touches both:
- use [$ingest-wiki](/Users/pana/.codex/skills/ingest-wiki/SKILL.md) for the durable knowledge update
- use [$apply-hybrid-code-layer](/Users/pana/.codex/skills/apply-hybrid-code-layer/SKILL.md) for the code analysis or implementation part

## Important limit

These skills provide operating method, not automatic project knowledge.

They work best when the repo also has local context such as:
- `README.md`
- `WIKI_SCHEMA.md`
- `CLAUDE.md`
- tests
- manifests
- wiki `tech/` or `product/` pages

Without local context, the skill still improves behavior, but it cannot invent the missing source of truth.
