---
title: "Coffee Talk"
category: task
status: current
created: 2026-05-02
updated: 2026-05-02
---

# Coffee Talk

## Note collaborateur — Codex skill

À faire côté collaborateur: mettre à jour sa skill Codex `ingest-wiki` avec la version actuelle du repo.

Étape la plus courte:

```bash
cp skills/ingest-wiki/SKILL.md ~/.codex/skills/ingest-wiki/SKILL.md
```

Pourquoi: la skill doit lire `wiki/hot.md` comme mémoire légère avant `wiki/index.md`, avec les modes `quick`, `standard` et `deep`.


--gros chantier nouveau effectué
-passage a une petite sidebar, avec affichage dynamique template dans proposal et cv
-page today avec choix des derniers chantiers
-page documents avec preview des de la librairie
-page settings (manque paiement et ingest profile linkedin)
-selecteur temporaire de llm dans proposal, gpt/mistral, (soit a creer dans preference soit a supprimer) en fonction du resultat des test

----------------
renommer styles : BRAND KIT, comme ca l'user peut appliquer sa marque pour creer video ou lettres/cv

ajouter un module de creation d'avatar ia. 

--trucs a affiner

-un point de bullet list en trop dans le cv , a supprimer
-les generation de proposal font plus d'une page , inclure une limite de longueur.
-passer le bouton share dans le header, ansin que undo redo 
-mettre en dynamique affichage une toolbar de style qd le texte est sleectionné
-arriver a moyen terme a avoir a simplifier le panneau de droite, dans cv forge, pour qu'il soit plus que dédier a des taches ai . et passer les choses obligatoire a gauche dans la sidebar.