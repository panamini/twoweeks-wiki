---
title: "ChatGPT/App SDK Roadmap"
category: product
tags: [chatgpt-app, apps-sdk, mcp, roadmap, safety]
created: 2026-06-23
updated: 2026-07-15
status: current
valid_from: 2026-06-12
type: roadmap
sources: [2026-07-15-mcp-current-head-authenticated-summary-reproof-checkpoint, 2026-07-13-pr322-mcp-public-catalog-url-checkpoint, 2026-06-26-pr87-17c2-mcp-oauth-preauth-ownership-checkpoint, 2026-06-26-pr87-17c1-mcp-oauth-login-return-continuation-checkpoint, 2026-06-26-pr87-17c0-mcp-oauth-login-return-convention-checkpoint, 2026-06-26-pr87-17b-mcp-oauth-authorization-intent-checkpoint, 2026-06-26-pr87-17a-mcp-oauth-authorization-request-boundary-checkpoint, 2026-06-25-pr87-16-mcp-account-link-lifecycle-checkpoint, 2026-06-25-pr87-15d-mcp-auth-local-runtime-wiring-checkpoint, 2026-06-25-pr87-15c-mcp-auth-composition-checkpoint, 2026-06-25-pr87-15b1-mcp-account-link-lookup-adapter-checkpoint, 2026-06-25-pr87-15b0-mcp-account-link-canonical-storage-checkpoint, 2026-06-25-pr87-15a-mcp-stytch-bearer-verifier-checkpoint, 2026-06-24-pr87-14b-mcp-auth-dev-endpoint-wiring-checkpoint, 2026-06-24-pr87-14a-mcp-auth-request-orchestrator-checkpoint, 2026-06-24-pr87-13-mcp-auth-policy-boundary-checkpoint, 2026-06-24-pr87-12-mcp-dev-fixture-demo-checkpoint, 2026-06-24-pr87-11-mcp-auth-account-linking-architecture-checkpoint, 2026-06-24-pr87-10-mcp-dev-endpoint-blocked-reachability-checkpoint, 2026-06-23-release-orchestration-staging-pr87-8-checkpoint, 2026-06-23-twoweeks-mcp-chatgpt-app-sdk-roadmap-checkpoint, 2026-06-12-chatgpt-app-sdk-roadmap-pr41-pr89, 2026-06-12-non-production-apps-sdk-exploration-plan, 2026-06-19-pr80b-safe-application-handoff-while-ats-access-pending]
related: [[howto/chatgpt-mcp-private-beta-tunnel-connector]], [[product/manual-application-handoff]], [[product/product-roadmap]], [[product/product-vision]], [[product/ai-product-model]]
---

# ChatGPT/App SDK Roadmap

Le transport MCP privé est désormais prouvé sur le current head, mais la valeur commerciale ne l'est pas encore. La priorité n'est plus de refaire l'OAuth : elle est de transformer la projection read-only actuelle en un produit utile, testable avec de vraies données contrôlées, puis de conduire une petite bêta avant toute publication.

## Current state

Statut : `PRIVATE_BETA_TRANSPORT_PROVEN` / `COMMERCIAL_VALUE_NOT_YET_PROVEN`.

V19 a directement prouvé le HEAD `0503832f5671b995b0095841104afc2e33b065ee`, les metadata publiques, les deux versions MCP supportées, le catalogue ordonné de six tools, le client OAuth confidentiel, un échange token observé sans valeur sensible et exactement un appel protégé à `twoweeks.application_package.summarize`.

Le résultat protégé était `NO_DATA`. Il contenait seulement `kind`, `status`, `toolName`, `version`, sans `summary` ni donnée privée imbriquée. C'est une preuve de transport et de sécurité, pas encore une preuve de valeur utilisateur.

Le runtime current-head de preuve a ensuite été arrêté et l'ancien runtime private-beta a été restauré canoniquement. Le lancement public, la soumission, les write tools, les provider/model calls, l'export et le live submit/apply restent bloqués.

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
| Catalog | six tools ordonnés et scope `twoweeks:applications:read` prouvés |
| Safety | annotations read-only, schémas stricts, résultats minimisés et fail-closed |
| Protected call | un appel `application_package.summarize` exécuté, résultat `NO_DATA` |
| Operations | doctor, démarrage, tunnel, preuve et recovery canoniques disponibles |
| Public launch | toujours bloqué |

## Functional gap before selling

- Les quatre tools protégés sont actuellement des tools de statut. Leur contrat public ne donne au modèle que `kind`, `status`, `toolName`, `version`.
- Aucun compte data-bearing n'a encore produit `OK` en live. Le seul résultat authentifié actuel est `NO_DATA`.
- Le parcours `ONBOARDING_REQUIRED -> import/creation Twoweeks -> OK` n'est pas prouvé.
- La preuve ne couvre qu'un sujet et un appel protégé, pas une cohorte ni une session longue.
- Le serveur n'émet pas de refresh token. Pour un lancement large, il faut soit un cycle de refresh revu séparément, soit une politique de réauthentification explicite et acceptable.
- `search` et `fetch` ne sont plus imposés par OpenAI. Leur maintien doit être décidé avant publication, car les workspaces utilisent un snapshot figé des tools approuvés.
- La privacy policy, les conditions/support, les assets de listing, les scénarios de review et le packaging Plugin/App ne sont pas encore enregistrés comme prêts.

## Dependency-first execution roadmap

### 0. Freeze the proven baseline — done

- [x] Conserver le endpoint, le scope, les versions MCP et le client confidentiel déjà prouvés.
- [x] Conserver le contrat fail-closed et l'absence de données privées imbriquées.
- [x] Garder V19 comme preuve de transport, sans le présenter comme preuve de valeur commerciale.

### 1. `COMMERCIAL-MCP-1` — useful bounded read-only projection — next

- [ ] Versionner un nouveau contrat public pour les quatre summary tools.
- [ ] Ajouter uniquement des champs utiles et non sensibles : état de readiness, compteurs bornés, catégories sûres, fraîcheur et codes de prochaines actions.
- [ ] Garder les textes libres privés, PII, identifiants internes et données brutes hors du résultat model-visible.
- [ ] Définir les comportements exacts `OK`, `STALE`, `NO_DATA`, `ONBOARDING_REQUIRED`, `TIMEOUT`, `DEPENDENCY_MISSING` et `MALFORMED`.
- [ ] Ajouter des tests de projection, de compatibilité, d'absence de fuite et de double `CallToolResult`.

### 2. `COMMERCIAL-MCP-2` — data and onboarding proof

- [ ] Préparer un compte de test data-bearing contrôlé et un compte vide distinct, sans données client réelles.
- [ ] Prouver les quatre tools en `OK` sur le compte data-bearing.
- [ ] Prouver `ONBOARDING_REQUIRED` sur le compte vide avec une prochaine action sûre et compréhensible.
- [ ] Prouver le parcours complet : connexion, import/création dans Twoweeks, disponibilité MCP, lecture utile.
- [ ] Vérifier que la donnée reste propriétaire du bon sujet et qu'aucun compte ne peut lire un autre compte.

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
