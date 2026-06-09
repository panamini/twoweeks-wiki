# Documentation et audit de run.sh — 15.2 Recommandations concrètes — Ajouter une commande `logs <service>`.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 15.2 Recommandations concrètes

Amélioration proposée: Ajouter une commande `logs <service>`.

Exemples:
	```bash
	./run.sh logs parser
	./run.sh logs vite
	./run.sh logs convex
	./run.sh logs all
	```
	La commande actuelle `logs` ne couvre que le parser Docker.
