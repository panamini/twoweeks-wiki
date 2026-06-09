# Documentation et audit de run.sh — 13.1 Priorité haute — Ajouter des préchecks bloquants pour la production.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.1 Priorité haute

Amélioration proposée: Ajouter des préchecks bloquants pour la production.

Etapes proposées:
	1. Vérifier que Docker est disponible.
	2. Vérifier que l'image runtime attendue existe ou que la stratégie de build est autorisée.
	3. Vérifier que les ports requis sont libres ou déjà détenus par le bon service.
	4. Vérifier que les variables obligatoires sont présentes.
	5. Vérifier que les secrets ne sont pas vides.
	6. Vérifier que `cloudflared` est pinné si le tunnel est utilise.
	7. Refuser de continuer si une précondition critique échoue.
