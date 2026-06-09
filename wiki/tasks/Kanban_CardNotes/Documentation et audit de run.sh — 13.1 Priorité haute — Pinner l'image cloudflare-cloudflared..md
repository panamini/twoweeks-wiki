# Documentation et audit de run.sh — 13.1 Priorité haute — Pinner l'image `cloudflare/cloudflared`.

Source: `audit/Documentation et audit de run.sh.md`

Paragraphe: 13.1 Priorité haute

Amélioration proposée: Pinner l'image `cloudflare/cloudflared`.

Remplacer `cloudflare/cloudflared:latest` par une version ou un digest documenté améliore la reproductibilité du mode tunnel.
	Etapes proposées:
	1. Introduire une variable `CLOUDFLARED_IMAGE`.
	2. Définir une valeur par défaut versionnée, par exemple `cloudflare/cloudflared:<version>`.
	3. Documenter la procédure de mise à jour de cette version.
	4. Ajouter la valeur effective dans `status`.
	5. En production, préférer un digest immuable si la politique de déploiement l'exige.
