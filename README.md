# twoweeks-wiki

Knowledge base and hybrid operating overlay for the [twoweeks](https://twoweeks.ai) project.

## Start here

1. Read `WIKI_SCHEMA.md` for neutral discovery.
2. Read `AGENTS.md` or `CLAUDE.md` for write-time mutation and verification rules.
3. For wiki work, read `wiki/overview.md`, `wiki/index.md`, and recent `wiki/log.md` entries.
4. For code work, start from the nearest manifest, tests, CI/lint config, and owning module.
5. Check `rawinput/` when ingest or repo-health work is relevant.

Do not read the entire repository blindly.
Start from the owning path.

## Repository shape

This repository is knowledge-plane-first today:

- `wiki/`, `rawinput/`, and `raw/` hold durable knowledge and ingest state.
- `WIKI_SCHEMA.md`, `AGENTS.md`, and `CLAUDE.md` define discovery and write-time behavior.
- `SKILL.md` and `skills/` expose the reusable wiki and code-layer workflows.
- `SKILLS_HOWTO.md` explains what each shipped skill is for.

The hybrid overlay also includes code-plane rules so the same discipline applies if application code is added here or mounted into the same workspace later.

## Structure

```text
twoweeks-wiki/
├── WIKI_SCHEMA.md
├── CLAUDE.md
├── AGENTS.md
├── IMPLEMENTATION_RULES.md
├── README.md
├── SKILL.md
├── skills/
│   ├── ingest-wiki/
│   │   └── SKILL.md
│   └── apply-hybrid-code-layer/
│       └── SKILL.md
├── scripts/
│   ├── audit_code_repo.py
│   ├── score_code_repo.py
│   └── validate_overlay.py
├── audit/
│   └── code-benchmark-criteria.csv
├── rawinput/
├── raw/
│   └── assets/
└── wiki/
    ├── overview.md
    ├── index.md
    ├── log.md
    ├── timeline.md
    ├── entities/
    ├── concepts/
    ├── design/
    ├── product/
    ├── strategy/
    ├── tech/
    ├── howto/
    ├── meta/
    ├── sources/
    ├── outputs/
    ├── tasks/
    └── archive/
```

Optional code plane:

- source roots such as `src/`, `app/`, `lib/`, `packages/`, `services/`
- test roots such as `tests/` or `__tests__/`
- manifests such as `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`
- CI config such as `.github/workflows/`

## For humans

- Drop new sources in `rawinput/` and use the ingest workflow to merge them into the wiki.
- Use `skills/apply-hybrid-code-layer/SKILL.md` and `IMPLEMENTATION_RULES.md` when the task touches real source code.
- Read `SKILLS_HOWTO.md` if you want the quick “which skill should I use?” version.
- Run `python3 scripts/validate_overlay.py` to validate the overlay files.
- Run the audit and score scripts when you want a repo-quality snapshot of the current instruction layer and any mounted code plane.
