---
title: "Convex Environment Sync"
category: howto
status: current
created: 2026-09-28
updated: 2026-09-28
tags: [convex, infisical, env, deploy, production, runbook]
related: [[howto/local-parser-operations]], [[howto/cloudflare-zero-trust-tunnel]], [[tech/import-ocr-pipeline]]
---

# Convex Environment Sync

Procédure pour que chaque variable d'environnement lue par le serveur Convex soit présente en production, à chaque déploiement. Aucune valeur de secret ne figure ici (repo public) : uniquement des noms et la procédure.

## Current state

- **Source de vérité** : Infisical, environnement `prod`, chemin `/twoweeks` (domaine EU). Le project id est dans `my-app/package.json` du repo Neyssan.
- **Consommateur** : le déploiement Convex de production.
- **Inventaire** : `my-app/scripts/convex-env/manifest.mjs` (Neyssan) liste chaque variable lue par `my-app/convex/`. Le test `my-app/scripts/__tests__/convex-env-manifest.test.ts` échoue si le code Convex lit une variable absente du manifeste : une nouvelle variable ne peut plus être oubliée.
- **Déploiement** : `npm run deploy:prod` (depuis `my-app/`) injecte les secrets Infisical, ajoute sur Convex les variables manquantes, puis lance `npx convex deploy`.
- Runbook détaillé côté code : `docs/runbooks/convex-environment.md` (Neyssan PR #509).

## Details

### Commandes (depuis `my-app/`, sur `main` à jour)

| But | Commande |
|---|---|
| Déployer la prod (sync des variables manquantes puis deploy) | `npm run deploy:prod` |
| Voir les différences sans rien changer | `infisical run … -- npm run convex:env:check` |
| Ajouter seulement les variables manquantes | `infisical run … -- npm run convex:env:sync` |
| Remplacer aussi les valeurs différentes | `infisical run … -- node scripts/convex-env-sync.mjs --prod --apply --overwrite` |

`infisical run …` = `infisical run --projectId=<id> --env=prod --path=/twoweeks --domain=https://eu.infisical.com --`.

Le script n'affiche jamais de valeur ; les valeurs passent à `npx convex env set` par stdin. Par défaut il **ajoute** seulement ; une valeur différente est signalée `UPDATE?` sans être touchée (sauf `--overwrite`).

Codes de sortie : `1` = une variable `core` manque à la fois dans Infisical et sur Convex (`deploy:prod` s'arrête) ; `2` = impossible de lire les variables Convex (droits de la clé) — le deploy continue et affiche la raison.

### Types de variables

- `core` : une fonctionnalité prod casse sans elle (auth Clerk, fournisseurs IA, import CV, billing Stripe, recherche d'offres JobsPipe).
- `feature` : interrupteur, désactivé si absent. Ex. `ENABLE_SEMANTIC_JOB_MATCH_V4=true` active l'analyse de compatibilité offre/CV ; sans elle la page offre affiche « analyse non disponible dans cet environnement » et l'adaptation du CV à l'offre peut échouer.
- `config` : surcharge optionnelle (modèle, URL, réglage) avec défaut dans le code.
- `local` : tests, debug, parser local ou fourni par Convex ; jamais synchronisé.

### Identifiants

`deploy:prod` exporte `CONVEX_DEPLOY_KEY` depuis le secret Infisical `CONVEX_deploy_key_PROD`. Si le sync signale qu'il ne peut pas lire les variables (`deployment:env:view`), soit lancer `npx convex login` une fois, soit créer dans le dashboard Convex une clé de déploiement prod avec les droits variables d'environnement et la ranger dans Infisical sous le même nom.

### La CI ne déploie pas Convex

Cloudflare Pages construit le frontend à chaque merge sur `main`. Les fonctions et le schéma Convex ne sont **pas** déployés par la CI. Après un merge touchant `my-app/convex/`, lancer `npm run deploy:prod`, sinon le nouveau frontend appelle un ancien backend et l'utilisateur voit `Server Error`.

### Import CV (`structuredUpload`)

Convex n'appelle pas Mistral OCR directement : il transmet le fichier au service parser à `CONVEX_PARSER_URL` (derrière Cloudflare Access : `CF_ACCESS_CLIENT_ID`, `CF_ACCESS_CLIENT_SECRET`, ticket signé par `OCR_BILLING_TICKET_SECRET`). Le parser exécute Mistral OCR avec **sa propre** `MISTRAL_API_KEY`. Si toutes ces variables sont présentes sur Convex et que l'import échoue encore, le parser est arrêté, injoignable, ou n'a pas sa clé : vérifier son hôte et les logs Convex de `structuredUpload`.

### Constat 2026-09-28 (prod)

Présentes sur Convex prod : toutes les variables d'import CV, `MISTRAL_API_KEY`, `OPENAI_API_KEY`, `JOBSPIPE_API_KEY`, Stripe, Clerk. Absentes : `ENABLE_SEMANTIC_JOB_MATCH_V4` (analyse de compatibilité désactivée) et `CLERK_WEBHOOK_SECRET` (classée `core` dans le manifeste).

## Sources

- Neyssan PR #509 (manifeste, script de sync, `deploy:prod`, runbook `docs/runbooks/convex-environment.md`).
- Liste des noms de variables du dashboard Convex prod, 2026-09-28.

## Related

- [[howto/local-parser-operations]]
- [[howto/cloudflare-zero-trust-tunnel]]
- [[tech/import-ocr-pipeline]]
