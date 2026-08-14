---
title: "Neyssan — checkpoint identité, bêta et transition production"
category: source
tags: [neyssan, clerk, convex, cloudflare, beta, production, security, deletion]
created: 2026-08-14
updated: 2026-08-14
status: current
type: checkpoint
related:
  - "[[tech/aws-production-industrialization]]"
  - "[[strategy/us-first-cloud-region]]"
  - "[[product/product-roadmap]]"
---

# Neyssan — checkpoint identité, bêta et transition production

Ce checkpoint distingue le code fusionné, le déploiement Edge, le backend Convex réellement live et la configuration d’identité. Il ne constitue pas une autorisation de lancement public.

## Résumé exécutif

- Le code de suppression de compte est fusionné dans `main` via #408 et son parcours Settings via #409; le point de code de référence déployé est `main@a1bfbd42f7cfa3e639532683c0a59224c668fa02`.
- Cloudflare Pages Production est configuré pour construire `my-app` avec `npx convex codegen --typecheck disable && npm run build`; le déploiement Production `a1bfbd42` après bascule d’identité est réussi et sert les alias `twoweeks.ai` et `beta.twoweeks.ai`. Le déploiement Edge précédent `8c973ff` fournit un rollback identifiable.
- La configuration Cloudflare Production utilise désormais la clé publique Clerk `pk_live` liée à `clerk.twoweeks.ai`; la destination Convex est `prod:giddy-basilisk-88`.
- Convex Production a ensuite été déployé depuis une archive propre de ce SHA avec `CONVEX_DEPLOYMENT=prod:giddy-basilisk-88 npx convex deploy --yes --typecheck disable --cmd 'npm run build'`; le build `tsc -b && vite build` et le déploiement ont réussi. La fonction `accountDeletion`, la table `accountDeletionTombstones`, les tables de fichiers `documentAssetReferences` et `documentAssetUploadIntents`, ainsi que l’index `by_clerk_id`, sont désormais observés dans l’environnement live.
- Le compte synthétique `porphyre2025+clerk_test@gmail.com` existe dans Clerk Production. Le smoke est actuellement arrêté sur l’écran de code email après reconnexion; aucun canary de suppression n’a donc été lancé.
- Aucune suppression de compte réelle ou synthétique n’a été lancée. Aucune donnée n’a été supprimée. La rotation des secrets reste différée à la gate finale pré-production; les noms/valeurs ne sont pas consignés ici.

## Chronologie bornée

1. **Frontière d’autorisation Convex (CS-P0-1)** : code fusionné via #407; les preuves anonyme/A/B ont été acceptées pour le code actif. Une vérification ultérieure a montré qu’il ne faut pas déduire de cette acceptation que chaque merge ultérieur est déjà déployé sur Convex Production.
2. **Suppression de compte (CS-P0-2, #408)** : ajout du tombstone persistant, de la purge rejouable et des garde-fous d’écriture tardive; fusion validée après corrections de revue.
3. **Settings (#409)** : parcours frontend connecté aux bindings Convex générés; le correctif Cloudflare a supprimé le shim typé et a fait passer le build Production/preview, les tests ciblés et les checks CI observés.
4. **Canary humainement piloté** : l’invitation a été retrouvée dans Gmail Spam puis acceptée dans le flux Clerk; la page d’inscription exigeait un username sans `+`. Le compte a été créé dans Clerk Production; l’application est ensuite restée sur l’identité Dev configurée.
5. **Contrôle live** : l’application fonctionnait, mais le menu Clerk affichait `Development mode` et le dashboard affichait des données de l’environnement Dev. Ce résultat est une preuve de fonctionnement Dev, pas une preuve d’isolation Production.
6. **Déploiement Convex Production (2026-08-14)** : depuis une archive propre de `origin/main@a1bfbd42f7cfa3e639532683c0a59224c668fa02`, codegen et `npm run build` ont réussi, puis la commande `npx convex deploy --yes --typecheck disable --cmd 'npm run build'` a publié les fonctions sur `https://giddy-basilisk-88.convex.cloud`. `accountDeletionTombstones`, `documentAssetReferences`, `documentAssetUploadIntents` et leurs index observés sont visibles après le déploiement.
7. **Alignement identité (2026-08-14)** : l’issuer Convex Production est maintenant `https://clerk.twoweeks.ai`, confirmé dans le dashboard Convex et par les métadonnées OpenID publiques Clerk. La clé Cloudflare `VITE_CLERK_PUBLISHABLE_KEY` est passée à `pk_live` puis a été publiée avec un build réussi sur `a1bfbd42`. Le smoke attend une reconnexion par code email.

## Audit sécurité et changesets réalisés

- L’audit initial sécurité/industrialisation a réconcilié le comptage à **six classes P0** : profils unclaimed, gateway/jobs publics, routes IA publiques, polling IDOR, suppression de compte et export public. Les classes ont été traitées séparément; elles ne doivent pas être recomptées comme cinq.
- **CS-P0-1** a borné l’autorisation Convex sur le code actif : identité requise pour les API publiques, propriété A/B pour lecture/modification/lancement/polling, suppression des accès unclaimed et gateway worker interne après vérification d’usage. Les tests anonyme/A/B ont été ajoutés et acceptés au niveau code.
- **CS-P0-2 / #408** a implémenté la suppression applicative avec tombstone persistant, purge paginée/rejouable, Clerk en dernier, webhook signé réutilisant l’orchestrateur et reçu opaque `_id` Convex. Le backend correspondant est maintenant déployé sur Convex Production; l’issuer Production est aligné, mais le canary réel reste volontairement non exécuté jusqu’à la fin du smoke authentifié.
- **#409** a connecté Settings au backend avec les bindings Convex générés; le shim typé Cloudflare a été retiré et le build Production observé est passé.
- Le confinement Cloudflare de la bêta est conservé. Aucun élargissement de cohorte n’est autorisé avant les preuves A/B sur l’identité et le backend réellement déployés.
- L’exposition de secrets vue pendant le dry-run n’est pas traitée comme une permission de publier des valeurs : noms seulement, rotation/révocation différée à la gate finale pré-production, et aucune valeur ne figure dans ce wiki.
- Les bugs non bloquants restants sont volontairement différés pendant cette bêta. La course résiduelle d’upload simultané à une suppression est une limitation connue; elle n’est ni corrigée ni traitée comme une fuite d’autorisation. Aucun élargissement de bêta ni lancement public n’en découle.

## Faits confirmés, inférences et non-vérifiable

### Faits confirmés

- Dans Cloudflare Pages Production : `CONVEX_DEPLOYMENT` pointe vers `prod:giddy-basilisk-88`; `VITE_CONVEX_URL` pointe vers l’URL Convex `giddy-basilisk-88`; `VITE_CLERK_PUBLISHABLE_KEY` est de type `pk_live` et lié à `clerk.twoweeks.ai`.
- Dans Convex Production, l’issuer d’authentification est `https://clerk.twoweeks.ai` et le template JWT `convex` est présent dans Clerk Production.
- Cloudflare Access répond anonymement par un blocage sur `twoweeks.ai` et `beta.twoweeks.ai`; la liste d’accès observée contient deux identités sur chaque domaine. Leurs adresses ne sont pas recopiées ici.
- Le dernier déploiement Cloudflare Pages Production correspondant à `main@a1bfbd42` est réussi sur les deux alias; le déploiement Edge précédent `8c973ff` est le rollback identifié. Le smoke autorisé de `twoweeks.ai` ouvre le dashboard; `beta.twoweeks.ai` demande une session Access distincte et n’a pas été marqué smoke-vert ici.
- Clerk Production contient exactement un compte synthétique identifié par son adresse de test; il attend le code email de reconnexion avant le smoke complet.
- Le domaine Clerk personnalisé `twoweeks.ai` a été vérifié côté DNS et SSL.
- Le Google OAuth Clerk Production n’est pas configuré : le bouton Google aboutit à `Missing required parameter: client_id`. Aucun secret OAuth n’a été affiché ni écrit dans le wiki.
- Le parcours email/invitation a créé le compte Clerk Production; le smoke frontend a affiché le dashboard avec la clé `pk_live`, puis a été interrompu pour renouveler la session après l’alignement Convex. Le parcours Google n’est pas une preuve valide pour la Production.
- Le site et le dashboard sont accessibles depuis Chrome avec l’identité Dev synthétique; aucune action de suppression ou d’écriture destructive n’a été effectuée pendant ce contrôle.

### Inférences contrôlées

- La bascule `pk_live` et l’issuer Convex sont maintenant alignés; une session antérieure peut rester invalide jusqu’à reconnexion, d’où le smoke par code email.
- Les anciennes données Dev ne sont pas utilisées comme preuve de Production; aucune migration ni copie de données n’a été réalisée.

### Non vérifiable dans ce checkpoint

- La version précédente exacte du backend Convex et un rollback opérateur sûr restent non vérifiables : l’historique de versions n’est pas exposé par le plan Convex courant. Le SHA déployé est toutefois prouvé par l’archive source, la commande et les artefacts observés.
- La seconde adresse autorisée est confirmée par l’utilisateur, mais son ouverture de session live n’est pas vérifiée dans ce checkpoint.
- La purge de bout en bout sur Convex Production et la preuve d’effacement des fichiers.

## Gates restantes

Avant une vraie production :

1. saisir le code email du compte synthétique et terminer le smoke frontend sur `twoweeks.ai` puis `beta.twoweeks.ai`;
2. refaire les tests anonyme/A/B : profils, jobs, historique, suppression, polling et absence d’accès public unclaimed;
3. identifier une procédure de rollback Convex coordonnée (frontend/backend); l’issuer peut revenir à `casual-gorilla-68.clerk.accounts.dev`, tandis que le rollback Edge est `8c973ff`;
4. exécuter le canary de suppression uniquement sur le compte synthétique Production;
5. traiter la rotation/révocation des secrets et le contrôle des logs à la gate finale pré-production;
6. conserver le confinement Cloudflare actuel et ne pas élargir la bêta avant ces preuves.

Les travaux ECS/SQS/multi-AZ/IaC, migration de région, extension Chrome et supply-chain avancée restent hors de ce checkpoint et ne sont pas des prérequis ajoutés à cette tâche.

## Actions non effectuées

- aucune modification de code;
- variables d’authentification alignées : Convex `CLERK_JWT_ISSUER_DOMAIN=https://clerk.twoweeks.ai` et Cloudflare `VITE_CLERK_PUBLISHABLE_KEY` de type `pk_live`; aucun secret privé affiché;
- déploiement Convex Production effectué depuis `main@a1bfbd42f7cfa3e639532683c0a59224c668fa02` avec build réussi; historique de rollback précédent non exposé;
- aucune suppression de données;
- aucun changement d’infrastructure.
