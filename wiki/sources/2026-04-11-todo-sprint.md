---
title: "Sprint Notes — 2026-04-11"
category: source
tags: [sprint, bugs, parsing, roadmap, paddle, convex, ux, import]
created: 2026-04-11
updated: 2026-04-11
status: current
valid_from: 2026-04-11
valid_until:
superseded_by:
horizon: present
version: v1
type: conversation
sources: []
related: [[concepts/cv-parsing-pipeline]], [[entities/cv-forge]], [[concepts/parsing-poc-progress]]
---

# Sprint Notes — 2026-04-11

## Résumé

Note de sprint mixte : confirmation roadmap parsing (IDENTITY/CONTACT next), bug scroll/zoom preview, Paddle cleanup, feature warning import, vérification Convex.

## Points clés

1. **Roadmap parsing** : (1) finir Experience → (2) IDENTITY/CONTACT POC → (3) EDUCATION → (4) SUMMARY → (5) ACHIEVEMENTS. EXPERIENCE n'est pas la première famille schema-first.
2. **Décision hybrid parser** : heuristiques pour familles stables, extraction structurée famille par famille via POC. Ne pas pivoter tout le parser.
3. **Bug** : scroll bloqué en mode zoom. Pas de pan à 100% fit.
4. **Paddle** : à supprimer. Scope minimal — ne pas toucher au workflow actif.
5. **Feature** : warning navigation pendant import CV (UX 2026 : friction minimale).
6. **Convex** : CVs enregistrés dans `userProfiles.cvDocument` — confirmé. Voir [[entities/cv-forge]].
