---
title: "Audit historique — état du lancement essais et paiement"
category: output
status: archived
created: 2026-09-16
updated: 2026-09-24
valid_until: 2026-09-24
superseded_by: "[[product/billing-launch-readiness]]"
type: audit
tags: [billing, stripe, convex, infisical, jobspipe, mistral, ocr, production]
related: [[product/billing-launch-readiness]], [[archive/tasks/2026-09-16-billing-launch-qualification]]
---

# Audit historique — état du lancement essais et paiement

Snapshot conservé depuis `docs/audits/2026-09-16-billing-launch-current-state.md`.
Il s’agit d’un audit Git/code et de preuves observables au 16 septembre 2026,
pas d’un état de production actuel. Il a été supersédé par
[[product/billing-launch-readiness]] le 24 septembre 2026.

## Verdict au 16 septembre

`VERIFICATION_BLOCKED` pour une décision de lancement commercial. Ce verdict
signifiait que les preuves externes nécessaires n’étaient pas toutes
observables depuis le contexte d’audit ; il ne déclarait ni JobsPipe ni Stripe
inutilisables.

## Identité Git observée

- `origin/main` observé à `3644e1f6492443a0e2941e3b33287741bb5cb0fc`.
- Le worktree d’audit était sur `codex/fix-parser-release-idempotency` à
  `b1f53a77`, et ne devait pas servir de base d’implémentation.
- Landing, privacy et terms étaient présents dans la référence observée.
- Le rafraîchissement GitHub avait échoué par résolution DNS ; la référence
  distante était donc potentiellement stale.

## JobsPipe

Un test manuel utilisateur concluant prouvait la reachability fonctionnelle.
La qualification billing demandait toutefois une preuve séparée : quota et
plan live, nombre de lignes, limites de recherche/import, signal d’usage et
plafond de coût. `requireQualifiedRoute("search"|"import")` refusait encore
l’activation sans cette preuve économique.

Conclusion : fonctionnel selon le test manuel, mais non qualifié pour le
lancement billing à cette date.

## Garde-fous et routes

`billingLaunchReadiness.ts` exigeait un Price explicite, des routes texte
qualifiées, des capacités OCR signées, des identifiants serveur OpenAI/Clerk,
une preuve d’achat/remboursement sandbox et des décisions de rétention,
fiscalité et coexistence des anciens soldes.

`qualifiedProviderRequest.ts` bloquait les routes Mistral non prouvées avec
`BILLING_INPUT_TOKENIZER_REQUIRED` et les routes d’usage sans preuve avec
`BILLING_USAGE_ROUTE_EVIDENCE_REQUIRED`.

## Stripe et publication

La dernière lecture alors disponible rapportait historiquement :

- `BILLING_LAUNCH_MODE` absent ;
- `STRIPE_LAUNCH_PRICE_ID` absent ;
- clé Stripe en mode test ;
- aucun endpoint webhook ;
- Price test de 7,90 € créé mais non injecté.

Ces éléments ne devaient pas être extrapolés après une nouvelle lecture de la
cible. Le produit visé restait un paiement unique de 7,90 €, sans abonnement.
La présence du code landing/legal dans Git ne prouvait pas sa publication HTTP
ni les exceptions Cloudflare Access.

## Conclusion opérationnelle historique

- Code landing/legal dans Git : PASS.
- JobsPipe manuellement fonctionnel : observé par l’utilisateur.
- Qualification billing JobsPipe : non prouvée.
- Stripe activé : non prouvé à cette date.
- Qualification Mistral/OCR/Jobs complète : non prouvée.
- Smoke Clerk → CV → offre → génération → export → essais → Stripe : non exécuté.

La suite correcte était une relecture fraîche de `origin/main` et des cibles
de production, sans écrire de correctif de code sur la seule base de cet audit.
