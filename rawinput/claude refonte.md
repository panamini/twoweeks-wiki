prompt
Compris — `neyssan` (l'app actuelle) est la ref pour les noms de tokens. Je vérifie ce qui existe déjà dont `FloatingAiToolbar.tsx` (24.5K, déjà là !) et le dossier `ui/`.

[Mode: Plan → Execute (doc only)]

Tout est aligné : les tokens du kit DS = ceux de `my-app/src/styles/foundation.css`. Je peux référencer les noms exacts (`--ac`, `--am`, `--sfr`, `--ti`, `--tm2`, `--tg2`, `--border-soft`, `--border-strong`, `--radius-2/3`, `--hs/hm/hb`, `--ts/tb`, `--ez`, `--dur-1..5`, `--motion-press-scale`, etc.) sans risque de divergence.

Composants déjà présents à **refactorer** (pas créer) :

- `components/ui/{button,card,dialog,input,toast,skeleton}.tsx`
- `components/FloatingAiToolbar.tsx` (24.5K, à scinder)

J'écris le doc maintenant.

[Mode: Review]

Doc livré : [docs/UI/CODEX-DS-V2-PLAN.md](https://claude.ai/epitaxy/docs/UI/CODEX-DS-V2-PLAN.md)

## Ce que tu as

Un cahier des charges **autosuffisant** pour Codex, qu'il peut suivre à la lettre :

- **§1 Token contract** — table exhaustive (couleur/spacing/radius/heights/type/motion/z) avec les noms exacts de `foundation.css` neyssan. Aucune valeur littérale tolérée.
- **§2 File map** — chemins précis, ce qui est NEW vs REFACTOR vs DELETE.
- **§3 CSS layer `ds-v2.css`** — tout le CSS prêt à coller (Button, IconButton, Input, Card, Pill, Status, Toast, Dialog, Skeleton, AiStageList, AiSuggestionCard, DiffBlock, FloatingAiToolbar, AskAiInput).
- **§4 Component contracts TS** — interfaces exactes, props, defaults, règles de rendu pour chaque primitive UI.
- **§5 AI primitives** — `AiStageList` (matrice d'états), `AiSuggestionCard` (3 modes × 3 états), `DiffBlock`, `FloatingAiToolbar` (refactor explicite : max 4 actions, no auto-apply, position above/below selection), `AskAiInput`, `UndoToast`.
- **§6 `lib/motion.ts`** — tokens motion typés pour usage TS.
- **§7 Voice/copy** — chaînes verbatim à utiliser (`Saved.`, `Couldn't finish.`, `Change applied.`, etc.).
- **§8 Storybook (Ladle)** — entrée par primitive, dark mode + reduced motion stories obligatoires.
- **§10 Acceptance criteria** — checklist par PR, pas de "ça a l'air OK".
- **§11 Stylelint** — config qui **bloque** tout hex/rgb/px hors tokens.
- **§13 PR sequence** — 7 PRs avec titres de commit littéraux et dépendances.
- **§14 Hard rules** — 12 interdictions explicites (no spinner, no auto-apply Rewrite, max 4 actions toolbar, no Title Case, no emoji, etc.).
- **§15 Pre-commit check** — commandes exactes à passer en vert.

## Points clés que Codex ne pourra pas rater

- Refonte AI alignée : `FloatingAiToolbar` émet des actions, **n'applique rien** ; `AiSuggestionCard` est l'unique surface d'acceptation, avec `Accept`/`Discard`/`Try again` et `Undo` toast après acceptation.
- Une seule animation idle dans tout le système : la "période brand" (header `AiStageList`, button-loading). Pas de spinners, pas de sparkles.
- Diff bloc-level uniquement (pas de per-char).
- Stylelint en porte-fou-sortie : tout hex/rgb hors `foundation.css`/`themes.css` casse le build.

## Si tu veux aller plus loin

Je peux, sur ta demande :

- Ajouter une annexe avec les **tests Playwright** détaillés (sélecteurs, assertions) pour DS-7.
- Générer les **stubs Storybook** (un fichier par primitive) prêts à coller, pour que Codex n'ait qu'à remplir.
- Pré-écrire le PR DS-1 (stylelint config + import motion-tokens) puisque mécanique pure.

Dis-moi.![[CODEX-DS-V2-PLAN]]