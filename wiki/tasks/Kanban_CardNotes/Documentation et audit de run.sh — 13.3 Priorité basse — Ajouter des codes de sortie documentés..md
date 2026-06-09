# Documentation et audit de run.sh — 13.3 Priorité basse — Ajouter des codes de sortie documentés.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.3 Priorité basse

Amélioration proposée: Ajouter des codes de sortie documentés.

Exemple:
	- `0`: succès;
	- `1`: erreur runtime;
	- `2`: mauvaise option utilisateur;
	- `130`: interruption utilisateur.
	Etapes proposées:
	1. Définir une table officielle des codes.
	2. Remplacer les `exit 1` génériques par des constantes lisibles.
	3. Documenter les codes dans `help`.
	4. Ajouter ces codes dans les logs d'erreur.
	5. Utiliser ces codes dans les jobs CI/CD.
