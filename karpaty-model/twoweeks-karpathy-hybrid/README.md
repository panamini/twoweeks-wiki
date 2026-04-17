# twoweeks-karpathy-hybrid

A reference project that merges the **twoweeks wiki operating model** with the **Karpathy execution layer**.

## What this project is

This package is built from two source systems:

- **twoweeks**: strong at durable knowledge architecture, ingest/lint/save-output workflows, index/log discipline, and retrieval order
- **forrestchang/andrej-karpathy-skills**: strong at behavioral execution — think before coding, simplicity first, surgical changes, and goal-driven verification

The hybrid keeps the twoweeks control plane and adds the Karpathy behavior shim.

## Why this merge works

The two source projects solve different problems:

| Layer | twoweeks | Karpathy repo | Hybrid result |
| --- | --- | --- | --- |
| Discovery/schema | Strong | Minimal | Strong |
| Mutation workflow | Strong | Minimal | Strong |
| Ambiguity handling | Weak | Strong | Strong |
| Simplicity guardrails | Weak | Strong | Strong |
| Surgical diffs | Medium | Strong | Strong |
| Verification loop | Medium | Strong | Strong |
| Examples/onboarding | Minimal | Strong | Strong |
| Plugin portability | Minimal | Strong | Strong |

## Delivered files

- `CLAUDE.md` — merged operating contract
- `WIKI_SCHEMA.md` — neutral discovery contract
- `skills/ingest-wiki/SKILL.md` — upgraded skill with explicit preflight and verification
- `EXAMPLES.md` — hybrid examples adapted to wiki mutations
- `.claude-plugin/` — plugin metadata for portability
- `audit/` — benchmark matrix, audit report, validation output
- `references/` — preserved baseline files from both source projects
- `diffs/` — text diffs from twoweeks baseline to the hybrid

## Quick recommendation

Use the hybrid if your goal is not just “store project knowledge,” but “operate on project knowledge like a careful senior engineer.”
