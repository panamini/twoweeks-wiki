# Documentation et audit de run.sh — 16.1 Règles recommandées — Documenter les effets de bord.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 16.1 Règles recommandées

Amélioration proposée: Documenter les effets de bord.

Chaque fonction qui tue, supprime, reconstruit ou modifie l'état devrait annoncer ses effets principaux en commentaire court.
	Exemple:
	```bash
	# Effets de bord: supprime le fichier d'état, efface les logs temporaires et vide CONVEX_TMPDIR.
	clear_dev_state() { ... }
	```
