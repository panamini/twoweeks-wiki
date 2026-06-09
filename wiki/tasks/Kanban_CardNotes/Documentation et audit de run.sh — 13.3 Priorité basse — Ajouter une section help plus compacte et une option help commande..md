# Documentation et audit de run.sh — 13.3 Priorité basse — Ajouter une section `help` plus compacte et une option `help <commande>`.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.3 Priorité basse

Amélioration proposée: Ajouter une section `help` plus compacte et une option `help <commande>`.

La commande `help` actuelle est utile mais longue. Une aide par commande serait plus accessible.
	Etapes proposées :
	1. Garder `./run.sh help` comme vue générale.
	2. Ajouter `./run.sh help local-fast`.
	3. Ajouter `./run.sh help prod`.
	4. Ajouter pour chaque commande: objectif, préconditions, effets de bord, exemples, logs à consulter.
	5. Afficher les commandes dangereuses dans une section séparée.
