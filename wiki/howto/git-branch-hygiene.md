---
title: "Git Branch Hygiene"
category: howto
tags: [git, workflow, branches]
created: 2026-04-27
updated: 2026-04-27
status: current
version: v1
sources: [2026-04-27-git-good-habit-skill]
related: [[meta/llm-wiki-pattern]]
---

# Git Branch Hygiene

For a new implementation task, start from a fresh updated `main` branch before creating a short descriptive task branch.

## Procedure

```bash
git switch main
git pull --ff-only origin main
git switch -c short-descriptive-branch-name
```

## Notes

This is a branch-start habit, not a rule for ongoing wiki ingest sessions. Do not use it to overwrite uncommitted local work.

## Sources

- [[sources/2026-04-27-git-good-habit-skill]]

