---
title: "Local-only ChatGPT App Manifest Draft"
category: source
tags: [mcp, chatgpt-app, manifest, local-only, safety]
created: 2026-06-11
updated: 2026-06-11
status: current
type: analysis
---

# Local-only ChatGPT App Manifest Draft

**Type** : Docs-only manifest draft
**Date** : 2026-06-11
**URL** : source locale `raw/PR29 - Local-only ChatGPT App Manifest Draft.md`

## Summary

This note defines a static draft shape for a future non-production ChatGPT App manifest while forbidding any file loadable by runtime or transport.

## Key points

- PR29 stays Plan-only and generates no manifest runtime file, no Apps SDK artifact, and no installer/SDK dependency.
- The draft is non-runnable by construction: no endpoint, transport, OAuth, auth, persistence, handlers, or UI components.
- Candidate tools are explicitly non-runnable and map to PR18/PR19 public names with safe summary-only outcomes.
- Metadata behavior is not yet implemented: `_meta` usage is intentionally omitted and listed as future gate requirements.
- All outputs are fixture- or summary-oriented with strict prohibition on private facts, raw source text, user/session identifiers, and real action verbs.
- PR27.1 remains a hard gate: review evidence is never execution permission.

## Data and safety policy

- Allowed: tool names, ref-only parameters, safe summaries, PR24/PR26 fixtures.
- Forbidden: raw CV/resume/cover letter/job text, private facts, secret values, `never_use` facts, raw arguments, transport endpoints, user/session IDs.

## Risks

- Static draft accidentally consumed as executable manifest input.
- Metadata field drift if copied into future runtime configs without PR27.1 gate validation.
- Tool visibility misalignment if default `hidden` is not preserved in future implementation.

## Touched pages

- none
