# Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter un résumé d'échec.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 15.2 Recommandations concrètes

Amélioration proposée: Ajouter un résumé d'échec.

Quand un service échoue, afficher:
	- service concerné;
	- endpoint testé;
	- fichier de log à lire;
	- dernière ligne significative du log si disponible;
	- commande de récupération possible.
	Exemple:
	```text
	[run][ERROR] local Convex did not become reachable
	[run][ERROR] checked: http://127.0.0.1:3210/instance_name
	[run][ERROR] log: tmp/convex-dev.log
	[run][ERROR] try: ./run.sh reset
	```
