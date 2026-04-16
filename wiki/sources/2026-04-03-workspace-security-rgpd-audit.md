---
title: "Workspace Security & RGPD Audit"
category: source
tags: [security, rgpd, audit, privacy, convex]
created: 2026-04-13
updated: 2026-04-13
status: current
valid_from: 2026-04-03
valid_until:
superseded_by:
horizon: present
version: v1
type: document
sources: [raw/2026-04-03-workspace-security-rgpd-audit.md]
related: [[entities/cv-forge]]
---

# Workspace Security & RGPD Audit

**Type** : Audit statique sécurité / conformité RGPD
**Date source** : 2026-04-03
**Périmètre** : `/Users/aurelienprivileggio/Workspace/Neyssan`

## Résumé

Source d'audit ciblant le code actif `my-app/` (frontend + Convex) et la sécurité opérationnelle du workspace. Le document classe les zones actives vs legacy/obsolètes, identifie 3 constats critiques (secrets exposés, endpoints sensibles sans garde d'identité explicite, stockage durable de PII), 2 constats élevés (effacement RGPD incomplet, logs potentiellement sensibles) et 2 constats moyens (fallbacks sensibles, rétention non appliquée).

Le document propose un plan d'actions priorisé en 4 phases (immédiat, 24-48h, semaine, industrialisation) et relie explicitement les remédiations à des obligations RGPD (minimisation, conservation, confidentialité, droit à l'effacement, accountability).

## Points clés

1. **Critique C1 — Secrets exposés dans le repo** : présence de clés API en clair dans la documentation technique, avec recommandation de suppression du tracking Git, rotation des clés et purge historique.

2. **Critique C2 — Surface d'abus sur actions/mutations** : endpoints Convex sensibles sans vérification d'identité explicite, avec pattern de garde minimal recommandé (`ctx.auth.getUserIdentity()`).

3. **Critique C3 — PII CV stockées en clair** : persistance backend (`raw_text`, `full_response`) et caches navigateur (`localStorage`) incompatibles avec un principe strict de minimisation/rétention.

4. **Élevé H1 — Effacement RGPD non transverse** : suppression utilisateur non cascade vers l'ensemble des tables liées, nécessitant une orchestration dédiée de suppression.

5. **Élevé H2 — Risque de fuite dans les logs** : logs de prompts/variables potentiellement sensibles, recommandation de redaction systématique.

6. **Moyen M1/M2 — Gouvernance de config et rétention** : paramètres sensibles/fallbacks codés en dur et politique de rétention déclarée mais non exécutée.

7. **Roadmap de remédiation** : séquencement opérationnel clair (bloquer les fuites -> sécuriser endpoints -> implémenter purge/effacement -> industrialiser scans CI).

## Implications pour twoweeks

- Prioriser la sécurité applicative et la conformité RGPD comme prérequis de fiabilité produit.
- Introduire une politique formelle de rétention par table et une politique de logs redacted.
- Mettre en place une procédure DSR complète (accès, suppression, export) avec suppression transverse.
- Aligner les flux CV/Proposal sur une stratégie de minimisation des données persistées.
