---
title: "Hot Cache - twoweeks"
category: overview
status: current
created: 2026-05-02
updated: 2026-10-28
---

# Hot Cache

This page is the active-memory cache for LLM retrieval. It is overwrite-only and non-canonical. Use it to choose pages, then trust durable pages.

## Current Focus

twoweeks centers on CV ingestion/parsing, canonical saved profile/CV data, and
personalized resumes, cover letters, and proposals. Keep product behavior,
provider qualification, and commercial launch evidence distinct.

## Key Active Facts

- **Croissance (2026-10-17)** : cible US d'abord, nom = préavis de deux semaines ([[entities/twoweeks]]), voix [[design/brand-voice]] ; publication sociale déléguée à
  l'assistant via une file d'approbation. Essais : plafond réel ≈ 374 en prod
  (ligne campagne à 343,62 $), 8 réclamés ; le « 50 » n'est que dans le code.
  **Prix USD 8,90 en production depuis le 18 oct.** (Price live, variable prod,
  #675 fusionnée, backend déployé, Checkout vérifié). **Umami en ligne** (#676,
  id public `d6bc48fa…`). Search Console US : 449 impressions, 0 clic.
  Planificateur : **Buffer gratuit retenu**, 3 canaux connectés (LinkedIn page, X `@twoweeksai`, TikTok), semaine 1 programmée (L1–L5 + fil X1). App
  ChatGPT « In review » (scan MCP sans findings). [[strategy/growth-acquisition-plan]].
- **Lettres (2026-10-06)** : un seul chemin actif (facturé, générateur « premium »
  = nom historique, rédacteur `gpt-5.6-terra`) ; tout autre chemin est refusé.
  Carte : [[tech/letter-generation-pipeline]]. Correctif accents FR + refus clair
  `COVER_LETTER_CV_JOB_TOO_DISTANT` : fusionné (PR #640) et en production (image MCP `ca8f0a481`, 2026-10-06).
- **Production** : secrets Infisical `prod /twoweeks`, Convex prod via CLI
  `--prod`, Lightsail MCP par paliers, aucun changement sans accord du
  fondateur : [[howto/production-operations]].
- **Billing (2026-09-24)** : `BILLING_LAUNCH_MODE=enforced`, offre `twoweeks_letters_25_optimizations_50_v1` à 7,90 € ; smoke authentifié réussi, aucun achat payant soumis par un agent. [[product/billing-launch-readiness]].
- **Export documents** : relais Convex `/document-export/*` ; le serveur
  d'export Lightsail se déploie à la main (`deploy.sh`, tag `sha-<commit>`).
  [[tech/export-pipeline]].
- Stable endpoint: `https://mcp.twoweeks.ai/mcp`; MCP proof remains
  operational evidence, not commercial value proof.
- **MCP lettre (2026-10-05)** : PR #613 passe tous les appels lettre par le
  bridge signé (clé Convex prod sans `runInternalQueries`). Reste :
  prod déployée, lettres actives 20:20 UTC. Jamais de stack
  local sur le tunnel prod (`run.sh down`). [[product/chatgpt-app-sdk-roadmap]].
- **OAuth MCP prod (2026-10-05)** : CIMD ChatGPT, callback générique, gate
  lettres `0`. Bridge versionné (#618), issuer corrigé (#623), image construite
  depuis `main` via `deploy/mcp/` (#626). Ne JAMAIS patcher la Lightsail à la
  main. Reste : connexion + résumé read-only depuis un connecteur neuf ; garder `r2`. [[howto/chatgpt-mcp-private-beta-tunnel-connector]].
- **UI et copie (2026-10-28)** : skills `twoweeks-ui` et `twoweeks-i18n-copy`
  (`.claude/skills/`, PR #681) remplacent `twoweeks-app-skeleton`.
  [[design/app-ui-and-copy-skills]].
- Product truth is `twoweeks`; CVForge and ProposalForge are internal names.
- Persistent wiki mutations require `wiki/index.md`, `wiki/log.md`, and
  `wiki/hot.md`.

## Canonical Pages To Read

- Letters and production ops: [[tech/letter-generation-pipeline]], [[howto/production-operations]]
- Billing activation: [[product/billing-launch-readiness]], [[product/product-roadmap]]
- Billing history: [[archive/outputs/2026-09-16-billing-launch-current-state]], [[archive/tasks/2026-09-16-billing-launch-qualification]]
- MCP commercial roadmap: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- Product/parser/export routing: [[overview]], [[concepts/cv-parsing-pipeline]], [[tech/export-pipeline]]
- Jobs/Mistral/UI checkpoint: [[sources/2026-08-31-neyssan-jobs-mistral-ui-merge-checkpoint]], [[product/job-library]]
- Cloud region / parser hosting: [[strategy/us-first-cloud-region]], [[tech/local-vs-remote-parser-architecture]]
- App UI, tokens, nav, FR/EN/ES copy: [[design/app-ui-and-copy-skills]]
- Wiki operations: [[meta/llm-wiki-pattern]], [[meta/temporal-management]]
