---
aliases:
  - Twoweeks — Workbench Tool List
---

Document pour collaborateur  
Objectif : comprendre **à quoi sert chaque outil / skill**, **dans quel cas l’utiliser**, et **quel problème concret de Twoweeks il aide à résoudre**.



---

## 1. Vue rapide

| Outil / Skill | Adresse | Ce que ça fait | Problème Twoweeks ciblé | Quand l’utiliser |
|---|---|---|---|---|
| **Fallow** | https://github.com/fallow-rs/fallow-skills | Codebase intelligence pour JavaScript / TypeScript : unused code, duplication, circular deps, complexity hotspots, architecture drift. Avec Fallow Runtime : hot-path / cold-path evidence. | Très utile pour CvLibraryContext, ProposalDisplay, toolbar/drawer, templates, persistence : détecter où le code est trop couplé, répété, mort ou dangereux à modifier. | Avant un refactor, avant suppression de code, avant cleanup gros fichier, ou quand Codex se perd dans l’architecture. |
| **Fallow Agent Skills** | https://docs.fallow.tools/integrations/agent-skills | Skills permettant à Codex/Claude/Cursor d’utiliser Fallow comme méthode de diagnostic. | Donne à l’agent une procédure pour lire les rapports Fallow et décider quoi modifier sans deviner. | À installer dans l’environnement agent pour que les audits Fallow deviennent répétables. |
| **Agentic Engineering Workflow Skill** | https://github.com/pawel-cell/micky-podcast-agentic-engineering/blob/main/skills/agentic-engineering-workflow/SKILL.md | Workflow complet : harness, contexte, scope, structure, revue, launch, sécurité. | Évite le “vibe coding”, les grosses PR incontrôlables, les bugs en cascade sur CV Forge / Proposal Forge. | Au début d’une feature ou d’un fix important. |
| **Michael Shimeles' Skills Repo** | https://github.com/michaelshimeles/skills/tree/main | Collection publique de skills / workflows à étudier ou adapter. | Sert de bibliothèque d’inspiration pour créer nos propres skills Twoweeks. | Quand on veut enrichir notre setup Codex/Claude avec des workflows réutilisables. |
| **Source Code as Agent Context** | https://github.com/pawel-cell/micky-podcast-agentic-engineering/blob/main/skills/source-code-context/SKILL.md | Force l’agent à lire le vrai code source d’un repo/package au lieu d’inventer depuis la doc ou sa mémoire. | Très utile pour Convex, Clerk, Vite, ProseMirror, exporters PDF, Chrome extension, Daytona/OpenSrc. | Dès qu’un bug dépend d’une lib, d’un SDK, d’un repo open source ou d’une API externe. |
| **Code Structure Cleanup** | https://github.com/pawel-cell/micky-podcast-agentic-engineering/blob/main/skills/code-structure-cleanup/SKILL.md | Refactor léger après que la feature marche : extraire duplications dans services/modules réutilisables. | Réduit les répétitions dans CvLibraryContext, rendu templates, persistence style/layout/image, toolbar logic. | Après un fix validé, jamais avant d’avoir une version fonctionnelle. |
| **Grep Loop Review Workflow** | https://github.com/pawel-cell/micky-podcast-agentic-engineering/blob/main/skills/grep-loop-review-workflow/SKILL.md | Boucle courte : review PR, corriger feedback, relancer tests, répéter jusqu’à merge-ready. | Évite les “fixes” partiels : template persiste mais font casse, image OK mais layout perdu, toolbar OK mais mobile cassé. | Avant merge, après chaque PR Codex, surtout sur persistence / UI complexe. |

---

## 2. Pourquoi Fallow est important pour Twoweeks

Fallow n’est pas juste un prompt. C’est un **outil de lecture de santé du codebase JS/TS**.

Il aide à répondre à des questions que Codex devine souvent mal :

- Quel fichier est devenu un hotspot dangereux ?
- Quelle logique est dupliquée dans plusieurs zones ?
- Quels imports / composants / helpers sont morts ?
- Est-ce qu’on a des dépendances circulaires ?
- Quelle partie du code est vraiment exécutée souvent, et quelle partie est froide ?
- Est-ce qu’un refactor proposé touche un chemin critique ?

### Problèmes Twoweeks que Fallow peut aider à traiter

| Problème Twoweeks | Ce que Fallow apporte |
|---|---|
| `CvLibraryContext.tsx` énorme et fragile | Détecter hotspots, duplication, complexité, fonctions candidates à extraction. |
| Persistence CV : template/font/color/image/layout | Repérer les chemins couplés et les duplications entre save, hydrate, cache local, remote refresh. |
| ProposalDisplay / editor riche | Trouver les zones où DOM-only logic, model update et persistence divergent. |
| Toolbar / drawer / Ask AI / preview click | Identifier les flows parallèles et les composants qui devraient partager un même état. |
| Nettoyage de vieux code | Éviter de supprimer au hasard : Fallow peut signaler unused code, mais il faut confirmer par tests/runtime. |
| Refactor après bugfix | Prioriser les extractions qui réduisent vraiment le risque au lieu de “faire propre” partout. |

### Quand utiliser Fallow

Utiliser Fallow **avant** :

1. gros refactor ;
2. suppression de code ;
3. extraction depuis `CvLibraryContext` ;
4. réparation d’un bug qui revient souvent ;
5. intégration d’un workflow agentique Codex/Claude ;
6. audit avant merge sur une PR risquée.

### Quand ne pas utiliser Fallow

Ne pas l’utiliser comme excuse pour :

- refactorer tout le projet ;
- supprimer du code sans preuve runtime ;
- mélanger cleanup + feature + bugfix ;
- remplacer l’audit fonctionnel navigateur ;
- ignorer les tests manuels CV/Proposal.

Fallow donne une **carte de risque**, pas une validation produit.

---

## 3. Lecture par problème Twoweeks

### A. Bugs de persistence Convex / CV Forge

**Symptômes vus dans Twoweeks :**

- Template/layout qui ne persiste pas après refresh.
- Image uploadée qui existe mais ne s’affiche pas.
- Font/color OK mais template perdu.
- Metadata patch qui ne contient pas tous les champs visuels.
- Local cache qui peut écraser un remote plus récent.

**Outils utiles :**

1. **Agentic Engineering Workflow**  
   Pour forcer un audit avant patch : preuve du boundary, logs, payload, remote read, hard refresh.
2. **Source Code as Agent Context**  
   Pour lire le vrai code Convex + notre code adapter au lieu de deviner comment `db.patch`, `ctx.storage.getUrl`, hydration ou metadata fonctionnent.
3. **Fallow**  
   Pour repérer si la logique save/hydrate/merge/cache est dupliquée ou dispersée dans plusieurs hotspots.
4. **Grep Loop Review Workflow**  
   Pour vérifier qu’un fix ne casse pas autre chose : image, template, font, color, hard refresh, authenticated runtime.

**Prompt court recommandé :**

```text
Use Agentic Engineering Workflow + Source Code as Agent Context.
Run Fallow diagnostics first if available: complexity hotspots, duplication, circular deps, unused code around CV persistence/hydration.
Audit the live persistence boundary before editing.
Trace setter → saveCurrentCvStyleOnly → adapter.saveMetadataPatch → Convex mutation → getByProfileId hydration → hard refresh render.
Patch only the smallest boundary proven broken.
Then run Grep Loop Review Workflow with tests/typecheck and a regression matrix for image, color, font, template, and layout.
```

---

### B. Gros fichiers trop fragiles : CvLibraryContext, ProposalDisplay, toolbar, renderer

**Symptômes vus dans Twoweeks :**

- Une correction locale provoque une régression ailleurs.
- Beaucoup de logique dupliquée : save, hydrate, merge metadata, render decoration, layout state.
- Les agents se perdent dans un fichier énorme et modifient trop large.

**Outils utiles :**

1. **Fallow**  
   Premier diagnostic : hotspots, complexité, duplication, dépendances circulaires.
2. **Agentic Engineering Workflow**  
   Pour limiter la tâche à une unité reviewable.
3. **Code Structure Cleanup**  
   Pour extraire après validation : service metadata, service hydration, service decoration URL, helpers toolbar.
4. **Grep Loop Review Workflow**  
   Pour reviewer les diff et interdire les refactors opportunistes.

**Quand l’utiliser :**

- Après un bugfix fonctionnel.
- Quand Fallow montre une vraie duplication.
- Quand on voit 2–3 blocs identiques dans plusieurs composants.
- Quand Codex veut “simplify architecture” alors qu’on veut juste sécuriser une mécanique répétée.

**Ne pas utiliser :**

- Pendant un bug critique non compris.
- Avant d’avoir une preuve claire du problème.
- Pour réécrire tout CV Forge d’un coup.

---

### C. Intégration d’outils externes : Daytona, OpenSrc Vercel, MCP, GitHub, libraries

**Symptômes vus dans Twoweeks :**

- On ne sait pas si l’agent comprend vraiment Daytona vs local Mac.
- Risque que Codex invente des commandes MCP ou Vercel/OpenSrc.
- Repo cloné dans sandbox mais workflow Git pas clair.

**Outils utiles :**

1. **Source Code as Agent Context**  
   L’agent doit lire les repos / docs / sources réels avant de proposer une intégration.
2. **Agentic Engineering Workflow**  
   Pour découper : installer, connecter, vérifier, documenter, puis seulement automatiser.
3. **Grep Loop Review Workflow**  
   Pour valider les scripts, env vars, README, commandes de lancement.
4. **Fallow**  
   Après intégration, pour voir si l’outil a créé duplication, code mort, dépendances circulaires ou hotspots.

**Prompt court recommandé :**

```text
Use Source Code as Agent Context.
Clone/read the relevant upstream repo or official docs before proposing commands.
Do not invent MCP config keys.
Produce a minimal integration plan for Twoweeks, then implement only the smallest verified step.
Validate with actual commands and document exact setup instructions for collaborator.
After implementation, run Fallow diagnostics if available to check for unused code, circular dependencies, duplication, and complexity hotspots.
```

---

### D. UI/UX premium : toolbar fluide, drawers, templates, drag & drop skills

**Symptômes vus dans Twoweeks :**

- Codex peut changer le style mais casser l’interaction.
- Animation trop visible, trop “demo”, pas intégrée au système réel.
- Drawer de section / Ask AI / click preview doivent ouvrir le même panneau, pas trois flows différents.

**Outils utiles :**

1. **Source Code as Agent Context**  
   Lire les composants existants avant d’ajouter une UI parallèle.
2. **Fallow**  
   Repérer si toolbar/drawer ont déjà des flows dupliqués ou composants morts.
3. **Agentic Engineering Workflow**  
   Définir un scope ultra précis : un seul composant, un seul état, une seule interaction.
4. **Grep Loop Review Workflow**  
   Vérifier les états : collapsed, expanded, hover, preview click, mobile, reduced motion.
5. **Code Structure Cleanup**  
   Après coup, si plusieurs drawers partagent la même mécanique.

**Prompt court recommandé :**

```text
Use Agentic Engineering Workflow + Source Code as Agent Context.
Do not create a parallel drawer system.
Find the existing section drawer opened by toolbar / Ask AI / preview click.
If Fallow is available, inspect duplication/hotspots around drawer and toolbar state before editing.
Wire the Skills DnD module into that existing drawer only.
Keep animation minimal and CSS-driven.
Run a regression checklist for toolbar, drawer open/close, preview click, mobile, and reduced motion.
```

---

## 4. Ordre d’utilisation recommandé

### Pour un bug critique

1. **Agentic Engineering Workflow** : cadrer le problème, scope petit.
2. **Source Code as Agent Context** : lire le vrai code et les libs concernées.
3. **Fallow** : regarder hotspots / duplication si le bug touche une zone large.
4. Patch minimal.
5. **Grep Loop Review Workflow** : review, tests, régressions.
6. **Code Structure Cleanup** seulement si le fix a créé ou révélé une duplication claire.

### Pour une nouvelle feature

1. **Agentic Engineering Workflow** : feature en tranche PR-sized.
2. **Source Code as Agent Context** : trouver le vrai point d’intégration.
3. Build minimal.
4. Test manuel + typecheck.
5. **Fallow** : vérifier qu’on n’a pas ajouté un flow parallèle ou du code mort.
6. **Code Structure Cleanup** : seulement après que ça marche.
7. **Grep Loop Review Workflow** avant merge.

### Pour intégrer un outil externe

1. **Source Code as Agent Context** : lire repo/docs source.
2. Mini POC.
3. Documentation de setup.
4. **Fallow** si le POC ajoute du code TS/JS au projet.
5. Review loop.

---

## 5. Ce que chaque outil empêche

| Risque | Outil qui aide | Pourquoi |
|---|---|---|
| Agent qui devine l’API Convex / Clerk / Vercel | Source Code as Agent Context | Il doit lire le vrai code source / doc officielle. |
| PR trop grosse et impossible à reviewer | Agentic Engineering Workflow | Il impose une unité petite et reviewable. |
| Fix qui marche localement mais casse au refresh | Grep Loop Review Workflow | Il force la matrice de régression + tests. |
| Duplications qui rendent les prochains bugs pires | Code Structure Cleanup + Fallow | Fallow détecte, Cleanup extrait proprement après validation. |
| Refactor prématuré qui casse la feature | Agentic Engineering Workflow | Il dit : feature minimale d’abord, cleanup après. |
| Agent qui invente une UI parallèle | Source Code as Agent Context + Fallow | Il doit trouver le composant existant et voir les flows dupliqués. |
| Suppression dangereuse de code | Fallow + Grep Loop Review | Fallow signale unused/cold code, la review valide avec tests/runtime. |
| Sécurité / packages trop jeunes / secrets exposés | Agentic Engineering Workflow | Il inclut des garde-fous sécurité de base. |

---

## 6. Recommandation pour Twoweeks

À installer / copier dans le repo comme skills projet :

```text
my-app/.agents/skills/
  fallow/
  agentic-engineering-workflow/SKILL.md
  source-code-context/SKILL.md
  code-structure-cleanup/SKILL.md
  grep-loop-review-workflow/SKILL.md
```

Installation Fallow skills possible via :

```bash
npx add-skill fallow-rs/fallow-skills
```

Ensuite, dans les prompts Codex, mentionner explicitement le skill voulu :

```text
Use $fallow and $agentic-engineering-workflow.
```

ou :

```text
Use $grep-loop-review-workflow before final output.
```

---

## 7. Règle simple pour le collaborateur

- **Tu ne comprends pas encore le bug ?**  
  Agentic Engineering Workflow + Source Code as Agent Context.

- **Le bug touche un gros fichier ou une zone fragile ?**  
  Ajoute Fallow avant de patcher.

- **Tu veux supprimer ou déplacer du code ?**  
  Fallow obligatoire, puis Grep Loop Review.

- **Tu as déjà un patch ?**  
  Grep Loop Review Workflow.

- **Le patch marche mais le code devient sale / répété ?**  
  Code Structure Cleanup.

- **Tu intègres une lib / repo externe ?**  
  Source Code as Agent Context obligatoire.

- **Tu veux juste changer une ligne évidente ?**  
  Pas besoin de skill lourd.

---

## 8. Liens sources

- Fallow Skills  
  https://github.com/fallow-rs/fallow-skills

- Fallow Agent Skills integration  
  https://docs.fallow.tools/integrations/agent-skills

- Agentic Engineering Workflow Skill  
  https://github.com/pawel-cell/micky-podcast-agentic-engineering/blob/main/skills/agentic-engineering-workflow/SKILL.md

- Michael Shimeles' Skills Repo  
  https://github.com/michaelshimeles/skills/tree/main

- Source Code as Agent Context  
  https://github.com/pawel-cell/micky-podcast-agentic-engineering/blob/main/skills/source-code-context/SKILL.md

- Code Structure Cleanup  
  https://github.com/pawel-cell/micky-podcast-agentic-engineering/blob/main/skills/code-structure-cleanup/SKILL.md

- Grep Loop Review Workflow  
  https://github.com/pawel-cell/micky-podcast-agentic-engineering/blob/main/skills/grep-loop-review-workflow/SKILL.md

- Codex Agent Skills documentation  
  https://developers.openai.com/codex/skills


### Daytona + MCP

**Site :** [Daytona](https://www.daytona.io?utm_source=chatgpt.com)  
**GitHub :** [Daytona GitHub](https://github.com/daytonaio/daytona?utm_source=chatgpt.com)

**Daytona** fournit des environnements de développement cloud isolés où les agents IA peuvent exécuter du code, lancer des serveurs, tester des branches Git et reproduire des bugs sans toucher à la machine du développeur.

Pour Twoweeks, cela permet à Codex ou Claude de :

- cloner le repo
- installer les dépendances
- lancer Vite / Convex
- reproduire un bug réel
- tester un correctif
- valider une PR

Avec **MCP (Model Context Protocol)**, l'agent peut contrôler Daytona directement : créer une sandbox, exécuter des commandes, modifier des fichiers et lancer des tests.

**En résumé :**

|Outil|Rôle|
|---|---|
|Fallow|Trouve les problèmes d'architecture|
|Skills|Expliquent comment les résoudre|
|Daytona + MCP|Permet à l'agent de les reproduire et les tester réellement|

Pour Twoweeks, Daytona est surtout utile pour les bugs complexes, audits, refactors et validations avant merge. Pas nécessaire pour de petites modifications UI ou CSS.

Oui — version courte pour ajouter au fichier.

---

## Pi Tooling

**Repo :** `https://github.com/panamini/pi-tooling`  
**Install :**

```bash
pi install git:github.com/panamini/pi-tooling
```

**Pi Tooling** est ton hub central de skills et extensions Pi. Il regroupe des workflows pour auditer, debugger, documenter, reviewer, sécuriser et améliorer un projet sans repartir de zéro à chaque session.

Pour **Twoweeks**, il sert surtout à transformer les problèmes répétitifs en workflows réutilisables.

### Cas utiles pour Twoweeks

|Skill / extension|À quoi ça sert|Quand l’utiliser|
|---|---|---|
|`repo-scan`|Audit global du codebase|Avant gros refactor ou quand le projet devient confus|
|`debug-live-boundary`|Trouver où une donnée est perdue dans le runtime|Bugs Convex, hydration, template, autosave|
|`verification-loop`|Tester, corriger, retester|Avant merge ou après fix fragile|
|`pi-review-loop`|Boucle review → fix → tests|Pour rendre une PR merge-ready|
|`security-review`|Checklist sécurité|Avant release, auth, storage, permissions|
|`project-checklist`|Checklist projet|Pour cadrer une tâche Codex/Claude|
|`blueprint`|Plan avant exécution|Pour refactor complexe|
|`visual-explainer`|Diagrammes / plans visuels|Pour expliquer l’architecture à un collaborateur|
|`pi-mcp-adapter`|Connecter Pi à des outils MCP|Pour brancher Pi avec Daytona, GitHub, outils externes|
|`self-generating-skills`|Créer de nouveaux skills|Quand un problème Twoweeks revient souvent|

### Résumé

**Pi Tooling = bibliothèque de workflows agentiques.**

Pour Twoweeks :

- **Fallow** trouve les zones sales du code.
    
- **Pi Tooling** donne les méthodes pour corriger proprement.
    
- **Daytona + MCP** donne un environnement réel pour tester.
    
- **Grep / Review Loop** empêche de merger trop vite.
    

À utiliser surtout pour les bugs récurrents, refactors, audits, validations PR et documentation technique.  
Pas nécessaire pour une micro-modif UI ou une simple phrase de copy.

1. Fallow
   → trouve duplication, complexité, circular deps, dead code.

2. Code Structure skill
   → transforme les duplications réelles en services propres.

3. Grep Loop / Review Loop
   → vérifie que le refactor n’a rien cassé.

4. Daytona
   → lance le projet et teste le bug en runtime.