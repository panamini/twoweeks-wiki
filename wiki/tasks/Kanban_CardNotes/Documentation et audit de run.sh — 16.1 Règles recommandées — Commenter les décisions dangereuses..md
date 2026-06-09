# Documentation et audit de run.sh — 16.1 Règles recommandées — Commenter les décisions dangereuses.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 16.1 Règles recommandées

Amélioration proposée: Commenter les décisions dangereuses.

Les zones à commenter davantage:
	- pourquoi tuer les ports `5173-5215`;
	- pourquoi `reset` supprime certains logs;
	- pourquoi `workspace` n'est pas la validation runtime stable;
	- pourquoi certaines variables Convex sont unset avant démarrage;
	- pourquoi `STRUCTURED_UPLOAD_SKIP_HEALTHCHECK=1` est défini côté Vite;
	- pourquoi le parser démarre même quand le frontend pointe vers l'edge.
