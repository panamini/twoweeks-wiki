---
title: "Essais et paiement — activation production"
category: product
tags: [billing, stripe, trials, convex, infisical, jobspipe, production]
created: 2026-09-16
updated: 2026-09-24
status: current
valid_from: 2026-09-24
version: v1
type: runbook
related: [[product/product-roadmap]], [[tech/import-ocr-pipeline]], [[howto/local-parser-operations]], [[entities/twoweeks]]
---

# Essais et paiement — activation production

État courant de l’activation des essais gratuits et du paiement Twoweeks,
vérifié le 24 septembre 2026 après fusion et déploiement de la PR #481. La
configuration et les preuves ci-dessous ne contiennent aucune valeur secrète ni
identité utilisateur.

## État actuel

L’activation de production est en place : `BILLING_LAUNCH_MODE=enforced` dans
Convex Production `prod:giddy-basilisk-88` et Infisical EU `prod /twoweeks`.
La requête directe de production confirme `enabled=true`; la readiness renvoie
`ready=true` et `trialReady=true`, avec 23/23 contrôles réussis et aucun
contrôle en échec.

Le smoke authentifié sur `/settings?tab=billing`, avec un utilisateur Clerk
vérifié dont l’identité n’est pas consignée, a réussi : la réclamation d’essai
a affiché 2 lettres et 4 optimisations IA, et Checkout Stripe live s’est ouvert
pour 7,90 €. Aucun achat n’a été soumis par l’agent. Une preuve d’achat payant
effectuée manuellement par l’utilisateur reste le seul élément de preuve
utilisateur en attente.

## Offre et quotas

| Surface | Allocation |
| --- | --- |
| Essai gratuit | 2 lettres, 4 optimisations IA, 5 pages OCR |
| Pack payant | 25 lettres, 50 optimisations IA, 10 pages OCR, 5 recherches, 25 imports |
| Prix | 7,90 € EUR, paiement unique (`mode=payment`), sans abonnement |
| Version d’offre | `twoweeks_letters_25_optimizations_50_v1` |

## Déploiement et revue

- La PR [#481](https://github.com/panamini/neyssan/pull/481) a été fusionnée
  le 2026-09-24 à 20:56:39 UTC au commit
  `8513c35f234b11dc0f0cc00d11c36709ba08cbce`; tous les contrôles GitHub sont
  verts.
- Codex Review s’est terminé sans nouveau finding sur le head
  `1dea6dd964be32282a0a54752b6675dfc56240b5`.
- Cloudflare Pages a déployé avec succès le commit de fusion. Le code fusionné
  a aussi été déployé avec succès sur Convex Production.
- L’image parser immuable
  `ghcr.io/panamini/neyssan/cv-parser:sha-8513c35f234b11dc0f0cc00d11c36709ba08cbce`
  (`sha256:8a1ab27de73903d9f31a2e7b04a2e542479cc47bb8cb088c89bc44f9dfc5799c`)
  est déployée et saine derrière cloudflared ; aucun port applicatif public
  n’est exposé.
- Aucun nouveau code n’a été écrit pendant le checkpoint d’activation après la
  fusion.

## Configuration et qualification

Convex Production et Infisical EU `prod /twoweeks` sont alignés sur le mode de
lancement `enforced`, le mode Stripe live, le fournisseur/modèle de matching
sémantique, le modèle de toolbar Mistral et les champs de preuve webhook. Les
valeurs secrètes ne sont pas consignées.

`BILLING_METER_UNIT=off` reste aligné dans Convex Production et Infisical EU :
il concerne le trajet Checkout legacy basé sur le meter. La branche
`enforced` de `stripe.ts` utilise le flux d’entitlement/wallet V2
(`billingPurchaseV2`) sans appeler `requireCheckoutMeterUnit`; le smoke
Checkout live réussi confirme que `off` ne bloque pas ce lancement.

Les routes et configurations comprises dans la readiness qualifiée couvrent
Terra pour la génération de lettres, Mistral pour l’édition/le matching/
l’extraction, le contrat de facturation OCR v2 signé, JobsPipe pour la
recherche et l’import, l’identité Clerk vérifiée et le déploiement du parser.
La décision Terra existante `gpt-5.6-terra` est conservée ; aucun autre nom de
modèle n’est inféré ici.

## Stripe live

- Le Price `price_1UDtQfFkKSo5QGwIw7WQQSYs` reste à 7,90 € en paiement unique ;
  aucun abonnement récurrent n’est configuré.
- L’endpoint live `we_1UDu0QFkKSo5QGwITijUNltK` est activé vers
  `https://giddy-basilisk-88.convex.site/stripe/webhook`.
- La preuve de transport signée sans frais a utilisé une Checkout Session live
  expirée immédiatement. L’événement
  `evt_1UJJqsFkKSo5QGwICqLvcgKS` est
  `checkout.session.expired`, `livemode=true`, avec
  `pending_webhooks=0` au 2026-09-24T21:06:50.725Z. L’identifiant de session
  n’est pas conservé.
- Cette preuve ne correspond pas à un achat payant : aucun paiement n’a été
  soumis pendant le smoke.

## Preuves et suite

La [PR #481](https://github.com/panamini/neyssan/pull/481) regroupe les
checkpoints d’activation et de revue :
[checkpoint d’activation](https://github.com/panamini/neyssan/pull/481#issuecomment-5813645723),
[audit Luna](https://github.com/panamini/neyssan/pull/481#issuecomment-5813785120),
[checkpoint pré-fusion](https://github.com/panamini/neyssan/pull/481#issuecomment-5813887408)
et [activation finale](https://github.com/panamini/neyssan/pull/481#issuecomment-5822506871).

La seule preuve utilisateur encore attendue est un achat payant effectué
manuellement. Aucun secret, identifiant de session Checkout ou renseignement
personnel n’est enregistré dans cette page.
