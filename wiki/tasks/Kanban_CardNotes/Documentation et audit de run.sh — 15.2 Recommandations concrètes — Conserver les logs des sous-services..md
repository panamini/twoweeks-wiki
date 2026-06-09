# Documentation et audit de run.sh — 15.2 Recommandations concrètes — Conserver les logs des sous-services.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 15.2 Recommandations concrètes

Amélioration proposée: Conserver les logs des sous-services.

Garder:
	- `tmp/vite-dev.log`;
	- `tmp/convex-dev.log`;
	- `docker logs` pour le parser.
	Mais ajouter dans le log principal les chemins et commandes utiles pour les consulter.
