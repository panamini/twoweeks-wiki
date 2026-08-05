---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-08-05
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and personalized resumes, cover letters, and proposals.

Keep two workstreams separate:

- MCP commercial launch: PR369 merged at `a3ea57da`. Two authenticated accounts passed 8/8 protected calls, seed/cleanup 4/4, recovery/deltas accepted, plus atomic concurrency/retry. Operational proof only, not commercial user value.
- Cover-letter quality: PR337 (`QUALITY-CL-4`) is ready at `977f1a29d8b9a5b3f1f67964eff61f46e5373f53`; 8 checks and exact-head Codex review are clear. Proves deterministic EN/FR prompt/finalizer integrity, not provider quality or a default-model choice.

## Key Active Facts

- Stable endpoint: `https://mcp.twoweeks.ai/mcp`.
- V19 remains the historical transport/OAuth proof; PR369 supersedes its `NO_DATA` limitation with a controlled data-bearing two-account proof.
- Current MCP surface is exactly four read-only `summarize` tools. It does not search jobs, ingest offers, create CV variants, or generate letters.
- Local MCP bootstrap: an Infisical Chrome session does not authenticate the CLI. Use project `twoweeks`, environment `dev`, CLI path `/twoweeks`, then the value-silent `run.sh` helpers and owner-scoped runtime procedure in [[howto/chatgpt-mcp-private-beta-tunnel-connector]]. Never substitute browser JWTs for the server-only Convex credential.
- Remaining MCP gates: prove onboarding from an empty account, compose a genuinely useful ChatGPT journey, then run a 3-5 user private beta.
- Recommended product demo slice: ChatGPT search or pasted offer → Job Brief → AI-proposed experience selection → human checkboxes → derived CV with provenance → existing proposal generation.
- A broad location/radius ATS provider comes second; a full editable master CV comes third.
- Public launch, write tools, provider/model calls, export, live submit/apply, refresh tokens and billing remain blocked pending separate reviewed gates.
- The public distribution surface is evolving; decide the final tool catalog before submission because approved tools are snapshot-frozen.
- `application-os-foundation` is verified at PR336 merge `80b4af7a764b37cc57b5bcb25a4f3bfc0a16a23b`.
- Luna low passed the English direct/adjacent development cells but only matched the stable control; do not promote it as a general default.
- Historical French CV-backed EVAL3D vetoes are invalid for quality inference because a canonical formal closing was counted as body content. No provider rerun is required now.
- No-CV remains a separate evidence/UX problem and is byte-locked against QUALITY-CL-4 drift. Any four-cell EN/FR CV-backed old/new comparison requires a separate exact contract and approval after merge; no provider run is automatic.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- Neyssan `main@3ef0bbdb`: Jobs→Proposal path (#378–#382) passed local desktop/mobile smoke; private-beta candidate, not public-ready. Open gates: deployed identity, account isolation, deletion safety, MCP operations. Read [[sources/2026-08-05-neyssan-post-merge-jobs-smoke-checkpoint]].
- Cloud-region decision: Twoweeks is US-first; future Convex Cloud and first production parser default to US East (N. Virginia), while parser provider selection remains benchmark-gated. Read [[strategy/us-first-cloud-region]] and [[sources/2026-07-27-us-first-cloud-region]].
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP commercial roadmap: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Cloud region / parser hosting: [[strategy/us-first-cloud-region]], [[tech/local-vs-remote-parser-architecture]], [[howto/local-parser-operations]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
