# Documentation et audit de run.sh — 16.1 Règles recommandées — Commenter l'intention, pas la syntaxe.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 16.1 Règles recommandées

Amélioration proposée: Commenter l'intention, pas la syntaxe.

Mauvais commentaire:
	```bash
	# Set variable to 1
	START_UI=1
	```
	Bon commentaire:
	```bash
	# local-fast doit lancer l'UI pour reproduire le flux complet parser + Convex + frontend.
	START_UI=1
	```
