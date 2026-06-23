---
title: "Cover Letter Quality Production Roadmap — Updated Checklist"
category: source
tags: [cover-letter, quality, roadmap, checklist, proposals]
created: 2026-06-23
updated: 2026-06-23
status: current
type: analysis
related: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[outputs/2026-05-26-proposal-language-generation-hardening]]
---

# Cover Letter Quality Production Roadmap — Updated Checklist

## Summary

This updated checklist supersedes the earlier PR1-PR4-open roadmap state with the post-PR245 reality: the baseline is merged, Mistral V2 expansion is on hold, quality repair stays off, and PR246 is the next implementation step.

## Key points

- PR230 premium provenance finalization, PR231 legacy prompt routing, PR232 premium prompt V2, PR233 bounded `qualityShadow` repair, and PR245 GPT premium finalization hardening are done.
- Post-PR245 flags-off smoke is clean for GPT premium, Mistral medium/large with V2 off, No-CV Mistral, and Qwen legacy.
- First Mistral V2 internal canary found unsupported expansion in `standardizing component usage and versioning`.
- The active decision is `NO-GO / HOLD` for Mistral V2 canary expansion and `NO-GO` for full production.
- PR246 is the next step: Mistral V2 factuality tightening.
- Quality repair remains off by default and stays outside the current canary path.

## Implications

- The earlier plan is no longer the live execution state; it should be read as history.
- The current work is tightening factuality and holding expansion, not broadening rollout.
- Any production release now requires a separate decision after PR246 outcomes are known.

## Touched pages

- [[tasks/2026-06-22-cover-letter-quality-production-roadmap]]
- [[outputs/2026-05-26-proposal-language-generation-hardening]]
