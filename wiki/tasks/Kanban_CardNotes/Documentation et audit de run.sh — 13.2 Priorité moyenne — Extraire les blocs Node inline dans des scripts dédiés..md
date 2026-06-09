# Documentation et audit de run.sh — 13.2 Priorité moyenne — Extraire les blocs Node inline dans des scripts dédiés.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.2 Priorité moyenne

Amélioration proposée: Extraire les blocs Node inline dans des scripts dédiés.

Des fichiers comme `scripts/spawn-detached.cjs` ou `scripts/read-convex-config.cjs` seraient plus lisibles, testables et commentables.
	Etapes proposées:
	1. Identifier chaque bloc `node -e`.
	2. Donner un nom fonctionnel à chaque responsabilité : spawn détaché, lecture JSON Convex, vérification HTTP.
	3. Créer un fichier script dédié par responsabilité.
	4. Ajouter une aide courte dans chaque script Node.
	5. Remplacer l'appel inline par `node scripts/<nom>.cjs`.
	6. Tester chaque script séparément avant de modifier le flux principal.
	7. Garder une compatibilité des arguments pour éviter de changer le comportement.
