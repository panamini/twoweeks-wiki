---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-08-14
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
- Infisical local contract: project `twoweeks`, environment `dev`, path `/twoweeks` holds the Convex bindings and the OpenAI Agent Proxy mapping. Launch proxied agents with `infisical secrets agent-proxy run ... -- codex`; `OPENAI_API_KEY_INFISICAL` is the placeholder for source secret `OPENAI_API_KEY`, while Mistral stays separate. Browser login does not authenticate the CLI; see [[howto/local-parser-operations]].
- Remaining MCP gates: prove onboarding from an empty account, compose a genuinely useful ChatGPT journey, then run a 3-5 user private beta.
- Recommended product demo slice: ChatGPT search or pasted offer → Job Brief → AI-proposed experience selection → human checkboxes → derived CV with provenance → existing proposal generation.
- A broad location/radius ATS provider comes second; a full editable master CV comes third.
- Public launch, write tools, provider/model calls, export, live submit/apply, refresh tokens and billing remain blocked pending separate reviewed gates.
- Historical French CV-backed EVAL3D vetoes are invalid for quality inference because a canonical formal closing was counted as body content. No provider rerun is required now.
- No-CV remains a separate evidence/UX problem and is byte-locked against QUALITY-CL-4 drift. Any four-cell EN/FR CV-backed old/new comparison requires a separate exact contract and approval after merge; no provider run is automatic.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- Neyssan `main@3ef0bbdb`: Jobs→Proposal path (#378–#382) passed local desktop/mobile smoke; private-beta candidate, not public-ready. Open gates: deployed identity, account isolation, deletion safety, MCP operations. Read [[sources/2026-08-05-neyssan-post-merge-jobs-smoke-checkpoint]].
- Neyssan auth/production checkpoint (2026-08-14): #408/#409 are merged and `main@a1bfbd42` is the code reference; Cloudflare Production deploys that SHA on `twoweeks.ai` and `beta.twoweeks.ai`, but still carries a Clerk `pk_test` key for `accounts.dev`. Convex Production `prod:giddy-basilisk-88` now has the #408 deletion functions/tables. A synthetic Clerk Production user exists, but no deletion canary ran and Convex rollback history is unavailable on the current plan. Keep the two-domain Access confinement and defer beta expansion. Read [[sources/2026-08-14-neyssan-auth-production-transition-checkpoint]].
- Cloud-region decision: Twoweeks is US-first; future Convex Cloud and first production parser default to US East (N. Virginia), while parser provider selection remains benchmark-gated. Read [[strategy/us-first-cloud-region]] and [[sources/2026-07-27-us-first-cloud-region]].
- AWS industrialisation is security-first and threshold-driven. The stateless Lightsail beta requires measured capacity, SLOs, observability, automated rollback and closed identity/data-safety gates before broader launch. Read [[tech/aws-production-industrialization]].
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP commercial roadmap: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Cloud region / parser hosting / scale: [[strategy/us-first-cloud-region]], [[tech/aws-production-industrialization]], [[tech/local-vs-remote-parser-architecture]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
