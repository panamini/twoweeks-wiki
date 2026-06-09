# Documentation et audit de run.sh — 13.2 Priorité moyenne — Renforcer le parsing `.env`.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.2 Priorité moyenne

Amélioration proposée: Renforcer le parsing `.env`.

Idéalement, utiliser une seule stratégie pour charger et inspecter les fichiers d'environnement. Si Bash reste la seule option, documenter clairement que seules les lignes simples `KEY=value` sont supportées dans certains chemins de lecture.
	Etapes proposées:
	1. Choisir un format officiel pour la configuration non sensible.
	2. Pour Bash pur, limiter les properties a `KEY=value` sans expansion complexe.
	3. Refuser ou avertir sur les lignes ambiguës.
	4. Utiliser la même fonction pour lire, valider et hasher la configuration.
	5. Ajouter un mode `config-validate`.
	6. Ajouter des exemples de fichiers dans la documentation.
