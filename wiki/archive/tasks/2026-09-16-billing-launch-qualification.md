---
title: "Plan historique — qualification du lancement essais et paiement"
category: task
status: archived
created: 2026-09-16
updated: 2026-09-24
valid_until: 2026-09-24
superseded_by: "[[product/billing-launch-readiness]]"
type: plan
tags: [billing, stripe, qualification, mistral, ocr, jobspipe, production]
related: [[product/billing-launch-readiness]], [[product/product-roadmap]], [[archive/outputs/2026-09-16-billing-launch-current-state]]
---

# Plan historique — qualification du lancement essais et paiement

Snapshot conservé depuis `docs/plans/2026-09-16-billing-launch-qualification.md`.
Le plan préparait une qualification auditable du checkout de crédits unique et
du parcours d’essai, sans réécrire le moteur de génération, changer les
quantités produit, ajouter un abonnement récurrent ou modifier la production
pendant la phase de revue.

## Invariants

- Checkout fail-closed tant que les critères de readiness n’étaient pas prouvés.
- Paiement Stripe en `mode: payment`, crédité une seule fois par session
  vérifiée ; jamais d’abonnement récurrent.
- Propriété issue de l’identité Clerk authentifiée, jamais d’un owner id fourni
  par le navigateur.
- Webhooks, retries et événements rejoués idempotents.
- Soldes d’essai et soldes achetés séparés du coût fournisseur.

## Qualification requise

1. Repartir d’un worktree propre basé sur le dernier `main` rafraîchi.
2. Relire la production sans exposer de secrets : présence, mode, cible et
   identifiants redigés uniquement.
3. Qualifier les routes Terra, Mistral, OCR v2 et JobsPipe avec bornes de
   tokens, retries, quotas, lignes retournées, usage et plafond de coût.
4. Exécuter le cycle Stripe isolé : Checkout, webhook signé, doublon,
   événement hors ordre, entitlement, remboursement et isolation de compte.
5. Exécuter le smoke authentifié : connexion, import CV, sauvegarde d’offre,
   lettre personnalisée, export PDF/DOCX, solde d’essai, Checkout et mise à
   jour par webhook.
6. Vérifier les routes publiques legal et la frontière Cloudflare Access.
7. Produire un audit frais et obtenir une revue indépendante avant toute
   activation explicite.

## Matrice d’acceptation

| ID | Critère | Preuve attendue |
| --- | --- | --- |
| AC-1 | Candidat = dernier `main` | SHA et worktree propres |
| AC-2 | Readiness d’essai complète | sortie readiness + preuves fournisseurs |
| AC-3 | JobsPipe borné économiquement | quotas, limites, usage et coût |
| AC-4 | Mistral/OCR qualifiés | harness, parser v2, replay |
| AC-5 | Terra réel et borné | CV + job authentifiés, sans fallback |
| AC-6 | Stripe correct | grant unique, replay idempotent, reversal |
| AC-7 | Production alignée | Convex/Infisical/Pages/Clerk sans secret |
| AC-8 | Revue indépendante | Fallow + revue sur le head exact |

## Modes d’échec

- Référence distante stale : arrêter et ne pas cherry-pick sur un worktree
  parser.
- Usage fournisseur non borné : garder readiness et billing désactivés.
- Webhook ou paiement incohérent : ne jamais créditer depuis l’URL de retour.
- Smoke production en échec : préserver les documents et le ledger, puis
  désactiver ou revenir par une modification revue.

## Décision historique

Le plan était à haut risque et nécessitait une approbation explicite avant
implémentation. La configuration et les preuves du 24 septembre sont
désormais documentées dans [[product/billing-launch-readiness]] ; cette page
reste uniquement la trace du plan initial.
