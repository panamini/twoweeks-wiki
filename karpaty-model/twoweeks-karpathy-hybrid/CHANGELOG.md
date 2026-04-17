# CHANGELOG

## 2026-04-17

### Added
- Hybrid `CLAUDE.md` that preserves twoweeks workflow rules and adds Karpathy behavior gates.
- Hybrid `WIKI_SCHEMA.md` that keeps discovery neutral and points behavior to `CLAUDE.md`.
- Upgraded `skills/ingest-wiki/SKILL.md` with preflight, ambiguity handling, minimal-change rules, and mode-specific verification.
- `EXAMPLES.md` with wiki-specific examples for the four Karpathy principles.
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` for portability.
- `audit/hybrid-audit-report.md` with benchmark findings and implementation notes.
- `audit/benchmark-matrix.csv` with weighted scoring.
- `scripts/validate_hybrid.py` and `scripts/score_benchmark.py` for reproducibility.
- `references/` folder containing the baseline source materials used for comparison.
- `diffs/` folder with unified diffs.

### Changed
- Reframed twoweeks from a pure mutation contract into a mutation contract plus execution discipline layer.
- Added explicit completion criteria to all operational modes.
- Added a “smallest safe change” rule to avoid unnecessary page creation or cleanup.

### Not changed
- Core twoweeks taxonomy, page frontmatter contract, retrieval order, archive model, and index/log requirements.
- Core Karpathy four-principle model.
