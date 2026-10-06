---
title: "Opérations de production (secrets, Convex, Lightsail, paliers)"
category: howto
status: current
created: 2026-10-06
updated: 2026-10-06
tags: [production, infisical, convex, lightsail, mcp, runbook]
related: ["[[tech/letter-generation-pipeline]]", "[[howto/local-parser-operations]]", "[[howto/chatgpt-mcp-private-beta-tunnel-connector]]", "[[tech/export-pipeline]]"]
---

# Opérations de production

Mode d'emploi court pour savoir **où sont les choses** et **comment on change la production sans la casser**. Aucune valeur secrète n'est écrite ici : seulement des noms et des emplacements.

> **Règle : aucun changement de production (Lightsail, Convex, Infisical, DNS, ChatGPT) sans accord explicite du fondateur.** Lire est toujours permis ; écrire demande un « oui » donné dans la conversation, pour cette action précise.

## Current state

### Où sont les secrets

- **Infisical EU** (`https://eu.infisical.com`), projet `twoweeks`, environnements `prod` et `dev`, chemin `/twoweeks`. La CLI se connecte séparément du navigateur : `infisical login --domain=https://eu.infisical.com`, voir [[howto/local-parser-operations]].
- Noms utiles (jamais les valeurs) : `OPENAI_API_KEY`, `MISTRAL_API_KEY`, `CONVEX_AUTH_TOKEN`, `CONVEX_DEPLOY_KEY` (dev, listé dans [[howto/local-parser-operations]]) et, côté production, la clé de déploiement `CONVEX_deploy_key_PROD` (nom indiqué par le fondateur, SUPPOSÉ : non relu dans Infisical pour cette page).
- Ne jamais utiliser `infisical secrets get --plain` dans un terminal enregistré ni copier une valeur dans le wiki, une PR, un log ou un fichier suivi par Git.

### Convex production

- La clé `CONVEX_deploy_key_PROD` **déploie** le code mais n'a **pas** le droit `deployment:env:view` (indiqué par le fondateur ; SUPPOSÉ : non retesté).
- Pour lire ou écrire les variables, utiliser la **CLI Convex connectée** depuis `my-app` :

  ```bash
  cd my-app
  npx convex env get BILLING_LAUNCH_MODE --prod
  npx convex env set NOM_DE_LA_VARIABLE <valeur> --prod   # écriture : accord du fondateur requis
  ```

  VÉRIFIÉ le 2026-10-06 : `env get … --prod` fonctionne avec la session CLI connectée (lecture de variables non secrètes). Éviter `env list --prod`, qui affiche aussi les valeurs secrètes ; lire les noms un par un.
- Les fonctions Convex et Cloudflare Pages se déploient seules à la fusion ; le serveur MCP et le worker PDF **ne** se déploient **pas** seuls.

### Serveur MCP (`mcp.twoweeks.ai`, Lightsail)

- Hôte `3.220.205.193`, accès `ssh -i ~/.ssh/twoweeks-lightsail ubuntu@3.220.205.193` (VÉRIFIÉ : utilisateur `ubuntu`, groupe `docker`, `sudo` sans mot de passe).
- Docker Compose dans `/opt/twoweeks/mcp` : services `mcp`, `gateway` (nginx), `cloudflared`. `.env` (ne contient que `MCP_IMAGE_TAG` et les deux `VITE_*`) et `secrets/mcp.env` appartiennent à root : toujours `sudo`, ne jamais les afficher en entier.
- Procédure exacte de déploiement et de retour arrière : `deploy/mcp/README.md` du dépôt (section « Deploy a release »). Ne jamais corriger un fichier dans le conteneur : reconstruire l'image depuis Git. Ne jamais lancer `./run.sh down` ni une pile locale sur le tunnel de production.
- Le parser / export a son propre serveur et son propre déploiement : [[tech/export-pipeline]].
- Où vivent les variables des lettres : tableau dans [[tech/letter-generation-pipeline]].

### Deux principes simples

- **Lancement par paliers** : on ne change pas dix choses d'un coup. Chaque palier a quatre temps : *sauvegarde*, *changement*, *vérification*, *retour arrière prêt*. On ne passe au palier suivant que si le précédent est vérifié. Si une vérification échoue, on revient en arrière d'abord, on enquête ensuite.
- **Idempotence** : une opération peut être rejouée sans effet double. Exemple concret : une même approbation ou un même `clientRunId` donne la **même** lettre et **un seul** débit, même si l'utilisateur ou ChatGPT réessaie ([[tech/letter-generation-pipeline]]). Les scripts et les procédures sont écrits pour pouvoir être relancés sans casse.

## Details

### Paliers locaux (poste de développement)

1. `./run.sh bootstrap` : prépare la configuration locale (Clerk du frontend, depuis Infisical `dev`).
2. `./run.sh doctor <profil>` : contrôle sans rien démarrer (`local-fast` ou `mcp-private-beta`). Doit finir en `PASS`.
3. `./run.sh local-fast` (application complète : parser local, frontend, Convex local) ou `./run.sh mcp-private-beta` (pile MCP locale + tunnel nommé).

Voir [[howto/local-parser-operations]] et [[howto/chatgpt-mcp-private-beta-tunnel-connector]]. Un simple serveur Vite n'est pas l'application complète.

### Paliers de production (serveur MCP et lettres)

Historique réel du 2026-10-05 : image, puis lettres, puis outils de boucle (voir `wiki/log.md`).

| Palier | Quoi | Sauvegarde | Changement | Vérification | Retour arrière |
| --- | --- | --- | --- | --- | --- |
| **A — image** | nouvelle version du serveur MCP construite depuis un commit exact | copies horodatées `.env.bak-<UTC>`, `compose.yaml.bak-<UTC>`, `secrets/mcp.env.bak-<UTC>`, et noter l'ancien `MCP_IMAGE_TAG` | `git archive` du SHA complet → `releases/<SHA>` → `docker build` sur l'hôte → `MCP_IMAGE_TAG=<SHA>` → `docker compose up -d mcp` | conteneur `healthy`, métadonnées 200, `/mcp` anonyme 401, `/oauth/authorize` CIMD → 303 `/sign-in`, `./run.sh mcp-smoke --origin https://mcp.twoweeks.ai --letters`, logs sans erreur | remettre l'ancien `MCP_IMAGE_TAG`, `docker compose up -d mcp` |
| **B — variables lettres** | `BILLING_LAUNCH_MODE`, `PREMIUM_COVER_LETTER_BOUNDED_REQUESTS`, `COVER_LETTER_PREMIUM_WRITER_MODEL`, `OPENAI_API_KEY`, `MCP_LETTER_GENERATION_ENABLED` dans `secrets/mcp.env` (ajouter une ligne, sans réécrire le fichier) et le gate côté Convex prod | sauvegarde de `secrets/mcp.env` ; noter la valeur Convex actuelle (`env get`) | `npx convex env set … --prod` puis `sudo docker compose up -d --force-recreate mcp` | `mcp-smoke --letters` (scope lettres annoncé) ; une lettre d'essai avec un compte de test | remettre `MCP_LETTER_GENERATION_ENABLED=0` (Convex puis `mcp.env`), recréer le conteneur |
| **C — outils de boucle** | `MCP_LETTER_LOOP_TOOLS_ENABLED=1` dans `mcp.env` (ouvre `twoweeks.letter.get` et `twoweeks.job.add`) | sauvegarde de `secrets/mcp.env` | ajouter la ligne, recréer le conteneur ; attendre au moins une heure après la mise en ligne du nouveau texte de consentement, car les jetons durent ≤ 1 h et ne sont pas rafraîchis (commentaire `my-app/src/modules/local-mcp/mcpLetterTools.ts:53-55`) | `tools/list` montre les deux outils ; `mcp-smoke --letters` | remettre la ligne à `0`, recréer le conteneur |

Les noms des variables et leur rôle exact : [[tech/letter-generation-pipeline]]. SUPPOSÉ : l'ordre et le délai d'une heure du palier C sont ceux du déploiement du 2026-10-05, pas une règle automatique.

### Lire la production sans rien changer

- Variables Convex : `npx convex env get <NOM> --prod` (un nom à la fois).
- Noms de `mcp.env` : `ssh … 'sudo sed "s/=.*//" /opt/twoweeks/mcp/secrets/mcp.env | sort'` (affiche uniquement les noms).
- État du conteneur : `ssh … 'cd /opt/twoweeks/mcp && sudo docker compose ps'`.

## Sources

`deploy/mcp/README.md` et `deploy/mcp/compose.yaml` du dépôt ; lectures seules sur Convex prod et la Lightsail le 2026-10-06 ; `run.sh` (`bootstrap`, `doctor`, `local-fast`, `mcp-private-beta`, `mcp-smoke`) ; `wiki/log.md` du 2026-10-05.

## Related

[[tech/letter-generation-pipeline]] · [[howto/local-parser-operations]] · [[howto/chatgpt-mcp-private-beta-tunnel-connector]] · [[tech/export-pipeline]] · [[product/billing-launch-readiness]]
