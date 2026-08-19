---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-08-19
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
- Infisical local: project `twoweeks`, environnement `dev`, chemin `/twoweeks`. Launch proxy: `infisical secrets agent-proxy run ... -- codex`; voir [[howto/local-parser-operations]].
- Remaining MCP gates: prove onboarding from an empty account, compose a genuinely useful ChatGPT journey, then run a 3-5 user private beta.
- Recommended product demo slice: ChatGPT search or pasted offer → Job Brief → AI-proposed experience selection → human checkboxes → derived CV with provenance → existing proposal generation.
- A broad location/radius ATS provider comes second; a full editable master CV comes third.
- Public launch, write tools, provider/model calls, export, live submit/apply, refresh tokens and billing remain blocked pending separate reviewed gates.
- Historical French EVAL3D vetoes are invalid because a formal closing was counted as body content. No-CV remains separate and locked; any provider rerun requires its own approved contract.
- Product truth is `twoweeks`; CVForge and ProposalForge are internal module names.
- Neyssan production checkpoint (2026-08-19): `origin/main`, Cloudflare Pages Production et Convex Production sont alignés sur `83872148`; Clerk Production et l’issuer `clerk.twoweeks.ai` restent alignés, le canary de suppression est passé et les deux domaines sont anonymement confinés par Access. Restent le smoke des deux identités autorisées, l’isolation A/B et l’exercice du repli coordonné vers `966890d9`; l’image parser `83872148` est publiée mais Lightsail reste sur `408e428`. Read [[sources/2026-08-14-neyssan-auth-production-transition-checkpoint]].
- Twoweeks is US-first; future Convex Cloud and parser default to US East, provider benchmark-gated. AWS industrialisation remains security-first and threshold-driven. Read [[strategy/us-first-cloud-region]] and [[tech/aws-production-industrialization]].
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and usually `wiki/hot.md`.

## Canonical Pages To Read

- MCP commercial roadmap: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- Cover-letter quality: [[tasks/2026-06-22-cover-letter-quality-production-roadmap]], [[sources/2026-06-24-cover-letter-mistral-v2-staging-green]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Cloud region / parser hosting / scale: [[strategy/us-first-cloud-region]], [[tech/aws-production-industrialization]], [[tech/local-vs-remote-parser-architecture]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
