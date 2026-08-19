---
title: "Neyssan — checkpoint identité, bêta et transition production"
category: source
tags: [neyssan, clerk, convex, cloudflare, beta, production, security, deletion]
created: 2026-08-14
updated: 2026-08-19
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

- Le code de suppression de compte est fusionné via #408 et son parcours Settings via #409. Après les correctifs #411–#414, le point de code actuellement aligné entre `origin/main`, Cloudflare Pages Production et Convex Production est `main@83872148d91263591d4cb9025cd39fbe60acfef4`.
- Cloudflare Pages Production construit `my-app` avec le codegen Convex puis `npm run build`; le déploiement du SHA `83872148` est réussi et sert les alias `twoweeks.ai` et `beta.twoweeks.ai`. Le déploiement Pages immédiatement précédent correspond à `5de4e349`.
- La configuration Cloudflare Production utilise désormais la clé publique Clerk `pk_live` liée à `clerk.twoweeks.ai`; la destination Convex est `prod:giddy-basilisk-88`.
- Convex Production a été déployé depuis un worktree propre du même SHA `83872148` avec `CONVEX_DEPLOYMENT=prod:giddy-basilisk-88 npx convex deploy --yes --typecheck disable --cmd 'npm run build'`; le build `tsc -b && vite build` et le déploiement ont réussi. Les fonctions actives de profils, Jobs, propositions, génération et suppression de compte sont observées dans l’environnement live.
- Le compte synthétique `porphyre2025+clerk_test@gmail.com` a servi au canary Production puis a été supprimé; aucun compte réel n’a été ciblé.
- Le canary de suppression est passé : `accountDeletionTombstones` est `state=purged`, `phase=complete`, avec 41 lots traités; `deleteClerkUser` et `markClerkDeletionComplete` sont en succès. La rotation des secrets reste différée à la gate finale pré-production; les noms/valeurs ne sont pas consignés ici.

## Chronologie bornée

1. **Frontière d’autorisation Convex (CS-P0-1)** : code fusionné via #407; les preuves anonyme/A/B ont été acceptées pour le code actif. Une vérification ultérieure a montré qu’il ne faut pas déduire de cette acceptation que chaque merge ultérieur est déjà déployé sur Convex Production.
2. **Suppression de compte (CS-P0-2, #408)** : ajout du tombstone persistant, de la purge rejouable et des garde-fous d’écriture tardive; fusion validée après corrections de revue.
3. **Settings (#409)** : parcours frontend connecté aux bindings Convex générés; le correctif Cloudflare a supprimé le shim typé et a fait passer le build Production/preview, les tests ciblés et les checks CI observés.
4. **Canary humainement piloté** : l’invitation a été retrouvée dans Gmail Spam puis acceptée dans le flux Clerk; la page d’inscription exigeait un username sans `+`. Le compte a été créé dans Clerk Production; l’application est ensuite restée sur l’identité Dev configurée.
5. **Contrôle live** : l’application fonctionnait, mais le menu Clerk affichait `Development mode` et le dashboard affichait des données de l’environnement Dev. Ce résultat est une preuve de fonctionnement Dev, pas une preuve d’isolation Production.
6. **Déploiement Convex Production (2026-08-14)** : depuis une archive propre de `origin/main@a1bfbd42f7cfa3e639532683c0a59224c668fa02`, codegen et `npm run build` ont réussi, puis la commande `npx convex deploy --yes --typecheck disable --cmd 'npm run build'` a publié les fonctions sur `https://giddy-basilisk-88.convex.cloud`. `accountDeletionTombstones`, `documentAssetReferences`, `documentAssetUploadIntents` et leurs index observés sont visibles après le déploiement.
7. **Alignement identité et rebuild (2026-08-14)** : l’issuer Convex Production est `https://clerk.twoweeks.ai`, confirmé dans le dashboard Convex. La clé Cloudflare `VITE_CLERK_PUBLISHABLE_KEY` est de type `pk_live`; le rebuild `a7b4be50` a régénéré les bindings après le déploiement Convex.
8. **Canary suppression (2026-08-14)** : le compte synthétique a demandé la suppression après code Clerk; la purge paginée a terminé en `purged`/`complete`, puis Clerk a été supprimé en dernier. L’ancien client affiche désormais le garde `Account deletion is in progress`, preuve qu’il ne peut plus lire les données applicatives.

## Audit sécurité et changesets réalisés

- L’audit initial sécurité/industrialisation a réconcilié le comptage à **six classes P0** : profils unclaimed, gateway/jobs publics, routes IA publiques, polling IDOR, suppression de compte et export public. Les classes ont été traitées séparément; elles ne doivent pas être recomptées comme cinq.
- **CS-P0-1** a borné l’autorisation Convex sur le code actif : identité requise pour les API publiques, propriété A/B pour lecture/modification/lancement/polling, suppression des accès unclaimed et gateway worker interne après vérification d’usage. Les tests anonyme/A/B ont été ajoutés et acceptés au niveau code.
- **CS-P0-2 / #408** a implémenté la suppression applicative avec tombstone persistant, purge paginée/rejouable, Clerk en dernier, webhook signé réutilisant l’orchestrateur et reçu opaque `_id` Convex. Le backend est déployé sur Convex Production et le canary synthétique est passé; aucune suppression réelle n’a été effectuée.
- **#409** a connecté Settings au backend avec les bindings Convex générés; le shim typé Cloudflare a été retiré et le build Production observé est passé.
- Le confinement Cloudflare de la bêta est conservé. Aucun élargissement de cohorte n’est autorisé avant les preuves A/B sur l’identité et le backend réellement déployés.
- L’exposition de secrets vue pendant le dry-run n’est pas traitée comme une permission de publier des valeurs : noms seulement, rotation/révocation différée à la gate finale pré-production, et aucune valeur ne figure dans ce wiki.
- Les bugs non bloquants restants sont volontairement différés pendant cette bêta. La course résiduelle d’upload simultané à une suppression est une limitation connue; elle n’est ni corrigée ni traitée comme une fuite d’autorisation. Aucun élargissement de bêta ni lancement public n’en découle.

## Delta vérifié — 2026-08-19

- Le dernier déploiement Cloudflare Pages Production, ses alias `twoweeks.ai` et `beta.twoweeks.ai`, ainsi que `origin/main` correspondent au SHA `83872148d91263591d4cb9025cd39fbe60acfef4`. Le build Pages et les checks associés aux PR #413/#414 sont réussis.
- Convex Production `prod:giddy-basilisk-88` a été déployé depuis un worktree propre au même SHA avec `convex deploy --yes --typecheck disable --cmd 'npm run build'`; le build et la publication ont réussi. La function-spec post-déploiement expose les fonctions actives de profils, Jobs, propositions, génération et suppression de compte.
- Le seul delta de schéma depuis le backend précédemment prouvé est le champ optionnel `metadata.generationContext`; aucune migration destructive n’a été exécutée.
- Sans cookies, les deux domaines renvoient HTTP 302 vers Cloudflare Access. Le smoke des deux identités autorisées, l’isolation A/B rejouée après ce déploiement et l’appel LLM anonyme ne sont pas validés par ce checkpoint.
- Le déploiement Pages immédiatement précédent correspond au commit `5de4e349fb1565a78ac45f738f79303805b00052`. La source de repli coordonné Edge/Convex avant #411 est `966890d9df580ca2c404faa8e1ed3da87f691ffd`; faute d’historique Convex sur le plan courant, ce repli reste une procédure opérateur à vérifier, pas une restauration instantanée prouvée.
- L’image parser du SHA `83872148` est construite, testée sur les chemins PDF/DOCX et publiée, mais n’est pas promue sur Lightsail. L’image live reste `sha-408e428577704007a5fbafce179b14ef8765a0f2`; cet alignement de maintenance ne bloque pas fonctionnellement la bêta privée.

## Faits confirmés, inférences et non-vérifiable

### Faits confirmés

- Dans Cloudflare Pages Production : `CONVEX_DEPLOYMENT` pointe vers `prod:giddy-basilisk-88`; `VITE_CONVEX_URL` pointe vers l’URL Convex `giddy-basilisk-88`; `VITE_CLERK_PUBLISHABLE_KEY` est de type `pk_live` et lié à `clerk.twoweeks.ai`.
- Dans Convex Production, l’issuer d’authentification est `https://clerk.twoweeks.ai` et le template JWT `convex` est présent dans Clerk Production.
- Cloudflare Access répond anonymement par un blocage sur `twoweeks.ai` et `beta.twoweeks.ai`; la liste d’accès observée contient deux identités sur chaque domaine. Leurs adresses ne sont pas recopiées ici.
- Le dernier déploiement Cloudflare Pages Production correspondant à `main@83872148` est réussi sur les deux alias. Sans cookies, les deux domaines renvoient HTTP 302 vers Cloudflare Access; le smoke des deux identités autorisées n’a pas été rejoué sur ce SHA.
- Clerk Production contient exactement un compte synthétique identifié par son adresse de test; il attend le code email de reconnexion avant le smoke complet.
- Le domaine Clerk personnalisé `twoweeks.ai` a été vérifié côté DNS et SSL.
- Le Google OAuth Clerk Production n’est pas configuré : le bouton Google aboutit à `Missing required parameter: client_id`. Aucun secret OAuth n’a été affiché ni écrit dans le wiki.
- Le parcours email/invitation a créé le compte Clerk Production; le rebuild Pages a ensuite régénéré les bindings contre le backend Action live. Le parcours Google n’est pas une preuve valide pour la Production.
- Les logs Convex montrent le succès de `accountDeletion:request`, des 41 `purgeBatch`, `markClerkDeletionComplete` et `deleteClerkUser`; la requête `proposalsPublic` de l’ancien compte est rejetée par `assertAccountActive`.

### Inférences contrôlées

- La bascule `pk_live` et l’issuer Convex sont maintenant alignés; une session antérieure peut rester invalide jusqu’à reconnexion, d’où le smoke par code email.
- Les anciennes données Dev ne sont pas utilisées comme preuve de Production; aucune migration ni copie de données n’a été réalisée.

### Non vérifiable dans ce checkpoint

- La version précédente exacte du backend Convex et un rollback opérateur sûr restent non vérifiables : l’historique de versions n’est pas exposé par le plan Convex courant. Le SHA déployé est toutefois prouvé par l’archive source, la commande et les artefacts observés.
- La seconde adresse autorisée est confirmée par l’utilisateur, mais son ouverture de session live n’est pas vérifiée dans ce checkpoint.
- Une vérification indépendante de rollback Convex reste non disponible sur le plan courant; le canary prouve la purge applicative et l’absence du sujet synthétique dans `users`, mais pas une procédure de restauration historique.

## Gates restantes

Avant une vraie production :

1. terminer le smoke des deux identités Cloudflare autorisées sur `twoweeks.ai` et `beta.twoweeks.ai`;
2. refaire les tests anonyme/A/B : profils, jobs, historique, suppression, polling et absence d’accès public unclaimed;
3. tester la procédure de repli coordonné Edge/Convex vers la source identifiée `966890d9df580ca2c404faa8e1ed3da87f691ffd`; l’historique Convex instantané reste indisponible;
4. traiter la rotation/révocation des secrets et le contrôle des logs à la gate finale pré-production;
5. conserver le confinement Cloudflare actuel et ne pas élargir la bêta avant ces preuves.

Les travaux ECS/SQS/multi-AZ/IaC, migration de région, extension Chrome et supply-chain avancée restent hors de ce checkpoint et ne sont pas des prérequis ajoutés à cette tâche.

## Actions non effectuées

- aucune modification de code;
- variables d’authentification alignées : Convex `CLERK_JWT_ISSUER_DOMAIN=https://clerk.twoweeks.ai` et Cloudflare `VITE_CLERK_PUBLISHABLE_KEY` de type `pk_live`; aucun secret privé affiché;
- déploiement Convex Production effectué depuis `main@83872148d91263591d4cb9025cd39fbe60acfef4` avec build réussi; historique de rollback précédent non exposé;
- aucune suppression de données réelles; les données du compte synthétique du canary ont été purgées;
- aucun changement d’infrastructure.
