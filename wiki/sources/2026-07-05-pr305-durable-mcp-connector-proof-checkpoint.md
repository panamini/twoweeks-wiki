---
title: "PR305 Durable MCP Connector Proof Checkpoint"
category: source
tags: [chatgpt-app, mcp, oauth, cloudflare, private-beta, smoke]
created: 2026-07-05
updated: 2026-07-10
status: current
type: checkpoint
related: [[product/chatgpt-app-sdk-roadmap]], [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
---

# PR305 Durable MCP Connector Proof Checkpoint

PR305 est mergee dans `application-os-foundation` par `f9dd477b116c48f1b223b17e1636876edf3c939f`. Elle prouve le connecteur private-beta durable a `https://mcp.twoweeks.ai/mcp` sans autoriser de lancement public.

## Proven

- Le tunnel Cloudflare nomme `neyssan-mcp-pr305-twoweeks-ai` route le hostname durable vers Vite local sur le port `5196`.
- Les metadata OAuth et protected-resource repondent `200` et annoncent exactement `client_secret_post` et la ressource MCP attendue.
- Un diagnostic live a observe directement `POST /oauth/token` en `200`.
- Le connecteur frais `twoweeks-mcp-pr305-final-0710` est connecte dans ChatGPT.
- `tools/list` expose les tools read-only `search` et `fetch`.
- Un `tools/call search` read-only a termine avec succes dans ChatGPT sans erreur de connexion.
- Les tests focalises passent `205/205`; le build TypeScript/Vite, la syntaxe shell, `mcp-check`, `reload-env`, `git diff --check` et les checks GitHub ont passe sur le head de PR `e9ddb1b6997e9bdd6c2663d3837abbd32d8c13e1`.

## Root cause

Le blocage final etait un drift de configuration locale, pas Cloudflare ni le callback ChatGPT :

- le chemin ChatGPT exigeait un client OAuth confidentiel, pas `token_endpoint_auth_method=none`;
- le secret brut ChatGPT et son digest local devaient correspondre exactement;
- le runtime actif attend `MCP_OAUTH_PRODUCTION_PRIVATE_BETA_*`, pas les anciens alias `MCP_PRODUCTION_PRIVATE_BETA_*`;
- les valeurs serveur devaient etre chargees dans `process.env` depuis la racine `.env.local`, pas seulement dans `my-app/.env.local`.

## Durable controls

- `/oauth/token` reste `client_secret_post` uniquement et fail-closed si la politique digest est absente ou malformee.
- Les redirects sont exacts; tous les wildcards sont rejetes.
- `run.sh mcp-check` impose la racine `.env.local` en mode `600`, controle la provenance des cles serveur et ne publie aucune valeur.
- `reload-env` rejoue le controle et recree la cle Clerk publique en memoire avant tout restart Vite private-beta.
- `.dockerignore` exclut les fichiers dotenv du contexte Docker.

## Boundaries

Cette preuve n'ajoute aucun provider call, write tool, refresh token, billing, account-link lifecycle expansion, mutation production/shared, raw-data logging ou lancement public. Le resultat prive des tools et les secrets ne sont pas conserves dans ce checkpoint.

## Related

- [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- [[product/chatgpt-app-sdk-roadmap]]
