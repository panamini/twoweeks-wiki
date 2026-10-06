---
title: "Essais et paiement — activation production"
category: product
tags: [billing, stripe, trials, convex, infisical, jobspipe, production]
created: 2026-09-16
updated: 2026-09-29
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
| Prix | 7,90 € TTC (TVA incluse), EUR, paiement unique (`mode=payment`), sans abonnement |
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

- Le Price live courant est `price_1UL3EUFkKSo5QGwIdGDjp4H2` (voir « Décisions du
  2026-09-29 ») ; il remplace `price_1UDtQfFkKSo5QGwIw7WQQSYs`. Paiement
  unique, aucun abonnement récurrent n’est configuré.
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

## Décisions du 2026-09-29

Toutes ces décisions sont prises par le propriétaire et déjà en production.

### Incident TVA Stripe et correctif (PR #531)

- Un achat de pack live du 2026-09-29 a été payé 9,48 €, mais aucun crédit n’a
  été accordé et aucune confirmation n’a été affichée.
- Cause : le snapshot de checkout stocke 790 centimes (Price hors taxe) ; Stripe
  Tax a ajouté 20 % de TVA par-dessus car le Price avait
  `tax_behavior=unspecified`. Le webhook comparait `amount_total` (948) à 790,
  d’où `BILLING_VERIFIED_PAYMENT_MISMATCH`, HTTP 500 et rejeu Stripe sans fin.
- Correctif : le webhook compare `amount_subtotal`. L’événement en attente a été
  renvoyé depuis Stripe ; les crédits de l’acheteur sont apparus (25 lettres,
  52 optimisations).
- PR : [#531](https://github.com/panamini/neyssan/pull/531).

### Prix 7,90 € TTC partout (PR #534)

- Nouveau Price live `price_1UL3EUFkKSo5QGwIdGDjp4H2` (790 EUR, `one_time`,
  `tax_behavior=inclusive`), en remplacement de
  `price_1UDtQfFkKSo5QGwIw7WQQSYs` (`unspecified`). `STRIPE_LAUNCH_PRICE_ID` est
  mis à jour dans Infisical `prod:/twoweeks` et dans l’environnement Convex prod.
- Le code refuse tout Price de lancement dont `tax_behavior` n’est pas
  `inclusive`. L’interface affiche « TTC ».
- Justification : B2C, acheteurs internationaux ; Stripe Tax calcule et reverse
  la TVA de chaque pays, la marge varie légèrement selon le pays (6,58 € HT en
  France à 20 %, 6,53 € en Suède à 25 %).
- PR : [#534](https://github.com/panamini/neyssan/pull/534).

### Économie unitaire (estimations)

- Net par pack en France ≈ 6,17 € (7,90 − 1,32 TVA − ~0,41 Stripe + frais
  Stripe Tax).
- Coût IA typique d’un pack entièrement consommé ≈ 2,4 $ ≈ 2,2 € : lettres sur
  `gpt-5.6-terra` medium ≈ 0,03 $/appel (1 à 2 appels), éditions sur
  `mistral-medium-3-5`, analyse d’adéquation sur `mistral-small-2603`, Jobspipe
  ≈ 0,02 $/recherche, Mistral OCR ≤ 0,01 $/page. Marge ≈ 65 %. Seuil de
  rentabilité : un pack coûtant plus d’environ 6,2 € en IA.
- Suite : confirmer avec les moyennes réelles du ledger fournisseur de prod
  (illisible avec la clé de déploiement ; nécessite un accès en lecture à Convex
  prod).

### Plafonds de coût (PR #534)

- Entrée d’optimisation (édition) bornée à 32 000 octets (128 000 avant).
- Plafond par opération 0,116 $ (0,404 $ avant). Pire cas financé par pack
  10,56 $ (24,96 $ avant) ; par essai 0,92 $ (2,07 $ avant).
- Invariant conservé : chaque crédit annoncé est financé à son plafond de pire
  cas. Risque résiduel : seul un abus délibéré à taille maximale peut dépasser le
  revenu net d’un pack.

### Essais gratuits (PR #534)

- Campagne plafonnée à 50 essais complets (166 avant) car le propriétaire paie
  personnellement les coûts IA ; exposition pire cas ≈ 46 $. Décision : relever
  le plafond à partir d’environ 50 utilisateurs / de vrais clients payants.
- Les domaines d’e-mail jetables sont refusés pour les essais (paquet
  `disposable-email-domains-js@1.26.0`, CC0, suit la liste amont
  disposable-email-domains) ; les achats restent ouverts.
- Garde-fous existants : un essai par propriétaire de facturation, e-mail
  principal vérifié via Clerk.

### Interface (PR #534)

Après un achat, si l’essai est déjà utilisé, la carte gratuite est masquée et
« Continuer » se place à côté de « Ajouter un pack ».

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
