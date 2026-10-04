---
title: "ChatGPT/App SDK Roadmap"
category: product
tags: [chatgpt-app, apps-sdk, mcp, roadmap, safety]
created: 2026-06-23
updated: 2026-10-05
status: current
valid_from: 2026-06-12
type: roadmap
sources: [2026-07-15-mcp-current-head-authenticated-summary-reproof-checkpoint, 2026-07-13-pr322-mcp-public-catalog-url-checkpoint, 2026-06-26-pr87-17c2-mcp-oauth-preauth-ownership-checkpoint, 2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint, 2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint, 2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint, 2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint, 2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint, 2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint, 2026-06-25-pr87-15c-mcp-auth-composition-checkpoint, 2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint, 2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint, 2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint, 2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint, 2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint, 2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint, 2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint, 2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint, 2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint, 2026-06-23-release-orchestration-staging-pr87-8-checkpoint, 2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint, 2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89, 2026-06-12-non-production-apps-sdk-exploration-plan, 2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]
related: [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[product/manual-application-handoff]], [[product/product-roadmap]], [[product/product-vision]], [[product/ai-product-model]]
---

# ChatGPT/App SDK Roadmap

Le transport MCP privé et la lecture utile sur données contrôlées sont désormais prouvés sur `main`, mais la valeur commerciale utilisateur ne l'est pas encore. Le parcours produit Jobs → CV → Proposal est également un candidat de bêta privée locale, sans constituer une preuve de lancement public. La priorité n'est plus de refaire l'OAuth : elle est de connecter ce socle à un parcours utile dans ChatGPT, puis de conduire une petite bêta avant toute publication.

## Current state

Statut : `PRIVATE_BETA_CONTROLLED_DATA_PROVEN` / `COMMERCIAL_USER_VALUE_NOT_YET_PROVEN`. Mise à jour 2026-10-04 : la boucle lettre confirmée est prouvée en bêta privée ; voir la section « October 2026 scope decision ».

V19 reste la preuve historique du transport, des metadata publiques, des deux versions MCP, du client OAuth confidentiel et d'un appel protégé `NO_DATA`.

Le 28 juillet 2026, la PR369 a été mergée sur `main` au commit `a3ea57da6138707fea02a10acbc23583139493b4`. Une preuve locale contrôlée avec deux comptes authentifiés distincts a exécuté 8/8 appels protégés, seed et cleanup 4/4, recovery `RECOVERED`, baseline et delta `ACCEPTED`. Une course entre deux sessions a aussi prouvé qu'un seul rail peut s'exécuter, que l'autre reçoit `409`, puis réussit au retry sans perdre sa session. Le coordinateur partage désormais un lease atomique entre les deux routes de preuve.

Cette preuve qualifie le rail opérationnel et l'isolation contrôlée, pas un parcours commercial dans ChatGPT. La surface actuelle expose exactement quatre tools read-only `summarize`. Elle ne sait pas encore chercher un emploi, ingérer une offre, créer une variante de CV ou générer une lettre.

Le lancement public, les write tools, les provider/model calls déclenchés par le MCP, l'export et le live submit/apply restent bloqués.

## October 2026 scope decision — the letter loop (2026-10-04)

Cette section prime sur la décision V1 read-only ci-dessous, qui reste comme historique.

- **Déjà prouvé (2026-09-27, stack privé local)** : une lettre confirmée de bout en bout depuis un vrai ChatGPT connecté — prepare gratuit, approbation dans l'app, génération via le générateur réel, lettre sauvegardée et relue dans la bibliothèque, exactement un crédit débité. Preuve : `docs/audits/2026-09-27-connected-chatgpt-runtime.md` dans le dépôt code.
- **Principe produit** : ChatGPT demande et lit ; TwoWeeks valide et écrit. Toute action qui coûte un crédit ou modifie un document est approuvée dans TwoWeeks ; chaque résultat renvoie un lien vers l'app (édition, mise en page, export y restent).
- **Point d'arrêt** : « voici une offre » → enregistrée → choix du CV → approbation 1 crédit → lettre dans la bibliothèque → ChatGPT la montre avec un lien.
- **Catalogue retenu (5 outils lettre)** : `fetch(twoweeks.letter_sources)` désormais en lecture seule, `twoweeks.letter.prepare`, `twoweeks.letter.generate` (+ lien app), nouveaux `twoweeks.letter.get` (lecture) et `twoweeks.job.add` (offre collée, même chemin de création que le site, sans appel provider). Même scope `twoweeks:letters:write` et même gate ; aucun nouveau scope, table ni fonction Convex publique.
- **Reporté au backlog (pas abandonné, décision et contrat dédiés à chaque fois)** : suggestions de modification de CV validées dans l'app (jamais d'écriture directe), création de CV, import PDF, recherche d'offres JobsPipe, dossiers de candidature sur `applicationPackages`, export comme outil. L'envoi de candidature reste hors périmètre tant qu'aucun flux confirmé par un fournisseur n'existe.
- **Transition de consentement** : `job.add` et `letter.get` réutilisent le scope lettres ; ils restent masqués et refusés tant que `MCP_LETTER_LOOP_TOOLS_ENABLED` n'est pas à `1`. Activer au moins une heure après la mise en ligne du nouveau texte de consentement (jetons ≤ 1 h, sans refresh).
- **Rejeté** : le prototype à 18 outils (`codex/mcp-public-app-management`, non commité) — écritures CV destructrices, lettres et dossiers dans des tables parallèles, catalogue non filtré par scope.
- **État (2026-10-05)** : branche `codex/mcp-letter-loop` (non poussée, non déployée) **qualifiée de bout en bout** avec un vrai connecteur ChatGPT sur un stack local isolé (tunnel et hostname de test dédiés, production non touchée) : offre ajoutée puis dédupliquée, une lettre générée, exactement un crédit débité, idempotence sans second débit, `letter.get` et `openUrl` OK, approbation expirée refusée. Deux bugs runtime Convex trouvés et corrigés (`3cdd3791`). Détails : `docs/decisions/2026-10-04-mcp-letter-loop-scope.md`.
- **Reste avant production** : `mcp.twoweeks.ai` est servi par un connecteur sur la Lightsail de production, qui n'annonce que `twoweeks:applications:read` (gate lettres éteint ou build plus ancien : non établi) ; son mode de build et de déploiement n'est pas documenté. Un conteneur tunnel `run.sh` resté actif depuis le test du 27/09 sur le Mac était aussi attaché à ce tunnel et renvoyait des 502 ; arrêté le 2026-10-05. Le fusionner sur `main` déploie Convex (fonctions internes, protégées par le gate) mais pas ce serveur. Ordre d'activation : déployer le serveur MCP avec le nouveau consentement, attendre ≥ 1 h, `MCP_LETTER_LOOP_TOOLS_ENABLED=1`, smoke `--letters --letter-loop` sur l'origine de production.

## Commercial V1 product decision

La promesse V1 recommandée est : **dans ChatGPT, comprendre l'état d'un dossier de candidature Twoweeks et savoir quelle action sûre effectuer ensuite**.

Questions utilisateur visées :

- mon dossier de candidature est-il prêt ?
- quelles catégories sont présentes ou manquantes ?
- mon plan de CV ciblé est-il à jour ?
- quels contrôles dois-je terminer avant d'envoyer moi-même la candidature ?

Le V1 reste read-only. Il peut exposer des états, compteurs bornés, catégories sûres et codes de prochaines actions. Il ne doit pas exposer de CV brut, nom, email, texte libre privé, prompt interne, identifiant de stockage, token, action d'écriture, export, envoi ou candidature automatique.

## What is already done

| Surface | État observé |
| --- | --- |
| Endpoint stable | `https://mcp.twoweeks.ai/mcp` décidé par PR322 |
| Protocol | MCP `2025-06-18` et `2025-11-25` prouvés |
| OAuth | client confidentiel et `client_secret_post` prouvés sans exposer de credential |
| Catalog | quatre tools protégés read-only `summarize` et scope `twoweeks:applications:read` |
| Safety | annotations read-only, schémas stricts, résultats minimisés et fail-closed |
| Controlled data | deux sujets distincts, 8/8 appels protégés, seed/cleanup 4/4, recovery et deltas acceptés |
| Coordination | lease atomique partagé, une seule exécution concurrente, session occupée conservée pour retry |
| Operations | doctor, démarrage, tunnel, preuve et recovery canoniques disponibles |
| Public launch | toujours bloqué |

## Functional gap before selling

- Les quatre tools protégés exposent des projections bornées et non sensibles, mais aucun parcours ChatGPT commercial ne les compose encore en résultat utilisateur.
- La preuve data-bearing reste une fixture contrôlée locale ; elle ne démontre ni utilité répétée, ni qualité sur données client réelles.
- Le parcours `ONBOARDING_REQUIRED -> import/creation Twoweeks -> OK` n'est pas prouvé.
- La preuve couvre deux sujets et les quatre tools, pas une cohorte ni une session longue.
- Le serveur n'émet pas de refresh token. Pour un lancement large, il faut soit un cycle de refresh revu séparément, soit une politique de réauthentification explicite et acceptable.
- `search` et `fetch` figuraient dans le catalogue V19 mais ne sont pas dans le registre actif à quatre tools. Le snapshot public final doit être figé avant publication.
- La privacy policy, les conditions/support, les assets de listing, les scénarios de review et le packaging Plugin/App ne sont pas encore enregistrés comme prêts.

## Dependency-first execution roadmap

### 0. Freeze the proven baseline — done

- [x] Conserver le endpoint, le scope, les versions MCP et le client confidentiel déjà prouvés.
- [x] Conserver le contrat fail-closed et l'absence de données privées imbriquées.
- [x] Garder V19 comme preuve de transport, sans le présenter comme preuve de valeur commerciale.

### 1. `COMMERCIAL-MCP-1` — useful bounded read-only projection — done

- [x] Versionner un nouveau contrat public pour les quatre summary tools.
- [x] Ajouter uniquement des champs utiles et non sensibles : état de readiness, compteurs bornés, catégories sûres, fraîcheur et codes de prochaines actions.
- [x] Garder les textes libres privés, PII, identifiants internes et données brutes hors du résultat model-visible.
- [x] Définir les comportements exacts `OK`, `STALE`, `NO_DATA`, `ONBOARDING_REQUIRED`, `TIMEOUT`, `DEPENDENCY_MISSING` et `MALFORMED`.
- [x] Ajouter des tests de projection, de compatibilité et d'absence de fuite.

### 2. `COMMERCIAL-MCP-2` — data and onboarding proof

- [x] `COMMERCIAL-MCP-2A` : prouver deux comptes authentifiés distincts, les quatre tools sur fixture data-bearing contrôlée, l'isolation A/B, le cleanup/recovery et la coordination concurrente atomique.
- [ ] Prouver `ONBOARDING_REQUIRED` sur le compte vide avec une prochaine action sûre et compréhensible.
- [ ] Prouver le parcours complet : connexion, import/création dans Twoweeks, disponibilité MCP, lecture utile.
- [ ] Rejouer l'isolation et la valeur sur une petite cohorte privée, sans données client réelles dans le harness.

### 3. `COMMERCIAL-MCP-3` — operational private beta

- [ ] Lancer une cohorte bornée de 3 à 5 testeurs autorisés.
- [ ] Mesurer connexion OAuth, premier appel utile, taux de statuts `OK`, latence, erreurs, réauthentifications et demandes support.
- [ ] Ajouter rate limits, audit redacted, alertes de santé, révocation et procédure d'incident/rollback.
- [ ] Décider séparément le refresh-token lifecycle. Ce changement touche l'auth et requiert un Change Contract `HIGH` risk.
- [ ] Conserver zéro write tool et zéro provider submission pendant cette bêta.

### 4. `COMMERCIAL-MCP-4` — distribution and commercial readiness

- [ ] Décider le catalogue final avant soumission : conserver six tools ou retirer `search`/`fetch` s'ils n'ajoutent pas de valeur.
- [ ] Préparer privacy policy, conditions, support, domaine vérifié, identité visuelle, description produit et scénarios de review.
- [ ] Vérifier le packaging Apps SDK / Plugin Directory et les plans ChatGPT réellement supportés au moment de soumettre.
- [ ] Recommandation à confirmer : facturer via le compte/abonnement Twoweeks et ne pas bloquer le lancement sur une monétisation native OpenAI encore non stabilisée.
- [ ] Rejouer le test depuis un connecteur/app frais correspondant exactement au snapshot soumis.

### 5. `COMMERCIAL-MCP-5` — controlled launch

- [ ] Ouvrir d'abord un canary commercial borné avec support et rollback immédiat.
- [ ] Étendre seulement après signaux réels de connexion, valeur, fiabilité et absence de fuite.
- [ ] Traiter chaque modification ultérieure de tool/schema comme une nouvelle version revue, pas comme un patch invisible.

## Commercial launch acceptance matrix

| Gate | Preuve requise avant lancement |
| --- | --- |
| Auth | au moins deux sujets distincts, connexion froide et reconnexion contrôlée |
| Useful data | les quatre tools protégés retournent `OK` sur un compte data-bearing contrôlé |
| Empty state | un compte vide retourne `ONBOARDING_REQUIRED` avec une action sûre |
| Isolation | tests négatifs cross-subject et absence de PII/private nested data |
| Reliability | scénarios `OK`, stale, timeout, dependency missing et malformed rejoués sans drift de contrat |
| Operations | health, rate limit, audit redacted, révocation, alerting et rollback documentés |
| OAuth continuity | refresh lifecycle revu ou réauthentification explicite validée par la bêta |
| Distribution | snapshot final, privacy/support/assets et review scenarios prêts |
| Commercial signal | bêta 3-5 utilisateurs avec au moins un usage utile répété et zéro incident privacy |

## Explicitly deferred after V1

- live submit/apply et `provider_verified_submitted` ;
- write tools, export/download/send et mutations Convex ;
- provider/model calls déclenchés par le MCP ;
- génération libre de documents dans le résultat MCP ;
- billing natif ChatGPT, sync, mobile et UI interactive riche ;
- extension publique d'account-link ou automatisation ATS.

## Current OpenAI platform constraints

- OpenAI recommande l'Apps SDK pour packager et publier une expérience app/MCP et exige notamment une privacy policy claire.
- Les tools approuvés par un workspace sont figés dans un snapshot ; les changements demandent une revue/actualisation admin.
- `search` et `fetch` ne sont plus obligatoires pour un serveur MCP personnalisé.
- Sans refresh access, ChatGPT peut perdre l'accès après expiration et demander une nouvelle authentification.
- Depuis juillet 2026, la découverte publique passe principalement par le Plugin Directory, l'app restant la connexion sous-jacente.

Références officielles :

- <https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt>
- <https://help.openai.com/en/articles/12515353-build-with-the-apps-sdk>
- <https://help.openai.com/en/articles/11487775>

## Sources

- [[sources/2026-07-15-mcp-current-head-authenticated-summary-reproof-checkpoint]]
- [[howto/chatgpt-mcp-private-beta-tunnel-connector]]
- [[sources/2026-07-13-pr322-mcp-public-catalog-url-checkpoint]]
- [[sources/2026-06-11-mcp-chatgpt-app-readiness-spec]]
- [[sources/2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint]]
- [[sources/2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89]]
- [[sources/2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]]

## Related

- [[product/manual-application-handoff]]
- [[product/product-roadmap]]
- [[product/product-vision]]
- [[product/ai-product-model]]
