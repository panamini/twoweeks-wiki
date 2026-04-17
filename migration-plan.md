# Migration plan

1. Add `WIKI_SCHEMA.md` as a neutral discovery file. Keep it short. Do not duplicate workflows.
2. Replace `CLAUDE.md` with the rewritten operational contract.
3. Replace `ingest-wiki/SKILL.md` with the mode-based version.
4. Rename `wiki/to do list/` to `wiki/tasks/` or remove it from the core retrieval surface.
5. Run lint once, fix taxonomy drift, and backfill any missing archive directories and index entries.
6. Do not attempt a full `CLAUDE.md` to `WIKI_SCHEMA.md` migration until the skill and the repo stay stable under the hybrid model.
