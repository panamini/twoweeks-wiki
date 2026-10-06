---
title: "Neyssan Jobs, Mistral and UI Merge Checkpoint"
category: source
status: current
created: 2026-08-31
updated: 2026-08-31
type: checkpoint
tags: [neyssan, jobs, mistral, ui, merge]
related: [[product/job-library]], [[concepts/cv-parsing-pipeline]], [[product/product-roadmap]]
---

# Neyssan Jobs, Mistral and UI Merge Checkpoint

On 2026-08-31, three independently reviewed changesets were squash-merged into `main`:

| PR | Merged commit | Delivered boundary |
| --- | --- | --- |
| #420 | `f30522427cf5f864ca930a06d8c78b3672eac08a` | Jobs list read-model projections, bounded selective proposal/shadow fallbacks, and durable proposal-link migration gating |
| #419 | `fbe29ec8782f3f301c7c42e7af6cbc51ebe75c92` | Selective Mistral/canonical-resume trust and export hardening without porting the older broad parser branches |
| #421 | `cab56d6873c2dd32f988a48899e035e61f519fce` | Reconciled v1 UI remediation, localized recovery, guarded preview/query intent, semantic tokens, and restrained motion |

## Durable product facts

- Projection-ready Jobs use their materialized list fields and avoid proposal/shadow table reads on the normal ready path.
- Legacy Jobs retain bounded fallback reads. Proposal and current-shadow fallbacks are selected by linked profile before per-Job quotas, preventing one visible Job from starving another.
- The proposal-link phase records durable completion only on its actual final page. The Jobs projection phase verifies that state server-side instead of trusting caller input.
- The backfill remains resumable and idempotent, but it was **not executed** during this changeset.
- Trusted structured resume sections remain authoritative through normalization, hydration, mapping, and export. Numeric education ranges, repeated education details, and supported secondary sections are preserved by focused regressions.
- The UI remediation covers active v1 routes and shared semantic contracts. It explicitly excludes template geometry/fonts, parser paths, Convex contracts, auth, billing, export behavior, StyleForge, and a Templates gallery redesign.

## Verification boundary

Each changeset received focused tests and final Codex review before merge. This checkpoint proves reviewed code integration only. It does not prove a new production deployment, live parser/provider quality, migration execution, or a completed private-beta smoke.

## Remaining PR hygiene

- #418 is superseded by #421 and should not be merged independently.
- #387 and #389 are older broad Mistral branches; #419 is the selective replacement, so they should not be merged wholesale.
- #396 remains separate draft runtime-budget work.
- #385 is an older conflicting post-merge contact-recovery slice and requires fresh validation against current `main` before any decision.
- #405 and #383 are independent documentation/developer-environment changes, not missing parts of this merge train.
