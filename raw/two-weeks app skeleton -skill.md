---
name: twoweeks-app-skeleton
description: Use when planning, implementing, or reviewing the twoweeks.ai app refonte against APP-SKELETON.html, especially PR-sized work on navigation, dashboard, Proposal forge, Jobs, CV forge, Documents, Templates, Settings, Sign-in, Safe-send, Import review, command palette, or onboarding.
skill:
frontend:
---

# Twoweeks App Skeleton

Use this skill for any frontend refactor work that must match the twoweeks app skeleton.

## Authority Order

1. `docs/UI/APP-SKELETON.html` in the active refonte worktree is the visual and interaction contract.
2. `docs/UI/SKELETON-AUDIT.md` explains the product decisions behind the skeleton.
3. `docs/UI/REFONTE-AUDIT.md` defines PR-sized implementation contracts.
4. `docs/UI/FEATURES-KEEP-VS-REMOVE.md` defines feature survival, restore, remove, and defer decisions.
5. Current active code decides implementation details, imports, data shape, and verification scope.

When these conflict, do not silently merge them. Use the conflict rules below, then flag anything unresolved.

## Required Sources

Read the exact current files before implementation:

- `.claude/worktrees/hungry-mcnulty-1722ea/docs/UI/APP-SKELETON.html`
- `.claude/worktrees/hungry-mcnulty-1722ea/docs/UI/SKELETON-AUDIT.md`
- `.claude/worktrees/hungry-mcnulty-1722ea/docs/UI/REFONTE-AUDIT.md`
- `.claude/worktrees/hungry-mcnulty-1722ea/docs/UI/FEATURES-KEEP-VS-REMOVE.md`

If a later session moves these files into `docs/UI/`, prefer the active repo copy and mention the path used.

## Skeleton Conflict Rules

- Quick Start appears twice in the HTML. Implement one Quick Start, using the version with `Capture jobs` as step 3.
- Theme is Light/Dark only. Do not add System mode unless the docs are explicitly changed.
- Numeric match percentages are not user-facing. Use verdict labels instead.
- Onboarding has 6 steps. Implement counters and state as 6, not 5.
- Safe-send is required from the Share menu in both forges. If the row count differs between docs and HTML, keep the HTML row semantics and flag the mismatch before merge.
- Treat `Application package` as a soft display concept, not a primary nav item or data model, unless explicitly requested.
- Do not copy inline styles or literal colors from the static HTML into app code. Translate them to existing DS primitives and tokens.

## Implementation Workflow

1. Identify the active route/component path before editing.
2. Compare the target surface against `APP-SKELETON.html`.
3. Preserve all KEEP items for the touched surface.
4. Restore any RESTORE items assigned to that PR.
5. Remove only items explicitly listed for that PR, or ask before deleting.
6. Use DS primitives before custom markup: `Button`, `Input`, `Card`, `Pill`, `Toast`, `Dialog`, `Sheet`, `Menu`, `AiSuggestionCard`, `AiStageList`, `DiffBlock`, `FloatingAiToolbar`.
7. Keep AI library files under `my-app/src/lib/ai/*` untouched.
8. Run the narrowest relevant tests first, then browser verification for rendered UI changes.

## PR Boundaries

- Shell/dashboard work owns app grid, collapsed sidebar, mixed recents, topbar context, command palette, Dashboard, Quick Start, Next Best Action, onboarding entry.
- Proposal work owns Proposal forge split, document stage, proposal rail, share menu, safe-send trigger, floating toolbar verification, export/history preservation.
- Jobs work owns split list/detail, filters, favorites, verdict labels, inline match panel, paste URL/capture entry points.
- CV work owns CV forge split, rail tabs, section organizer, section editor sheets, import review, ATS badge, per-document style, section-scoped Ask AI.
- Documents/templates/settings/auth work owns unified Documents, Templates, Settings inner nav, Document style simplification, sign-in.
- Final parity work owns drift cleanup against `APP-SKELETON.html`.

## Reporting

In final responses, state:

- which skeleton source path was used
- which PR contract was touched
- what changed
- what was verified
- any skeleton/doc conflict still unresolved
