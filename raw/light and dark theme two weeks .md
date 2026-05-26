---
css: " "
ui: " "
light mode: " "
dark mode: " "
---
Choix solide. Voici la palette finale consolidée — light validé (Bone Deeper) + dark Onyx Crisp.

```css
:root, [data-theme="light"] {
  --bg:     #F1EEE7;
  --sf1:    #F6F4EF;
  --sf2:    #E9E5DC;
  --sf3:    #F8F6F2;
  --sfr:    #FFFDF8;
  --paper:  #FAF9F5;
  --paper-ink: #15120F;
  --border:  rgba(15,12,8,0.07);
  --border2: rgba(15,12,8,0.12);
  --text:    #2D2A26;
  --strong:  #1A1815;
  --muted:   #76726B;
  --dim:     #A8A39A;
  --accent:  #D47554;
  --accent-soft: rgba(212,117,84,0.12);

  --w-regular: 400;
  --w-medium:  500;
  --w-semibold: 600;
  --w-bold:    700;
}

[data-theme="dark"] {
  --bg:     #16130F;
  --sf1:    #1C1814;
  --sf2:    #251F19;
  --sf3:    #211C17;
  --sfr:    #2A2620;
  --paper:  #EFEADC;
  --paper-ink: #1E1A17;
  --border:  rgba(255,240,220,0.075);
  --border2: rgba(255,240,220,0.135);
  --text:    #D8D0C2;
  --strong:  #F1EBDD;
  --muted:   #918677;
  --dim:     #62584C;
  --accent:  #D8805F;
  --accent-soft: rgba(216,128,95,0.14);

  /* Anti-blooming : weights −50/−100 vs light */
  --w-regular: 380;
  --w-medium:  480;
  --w-semibold: 580;
  --w-bold:    640;

  --paper-shadow:
    inset 0 1px 0 rgba(255,250,240,0.04),
    0 0 0 1px rgba(255,240,220,0.08),
    0 18px 40px -22px rgba(0,0,0,0.50);
}

/* Micro-interactions partagées */
:where(button, input, select, a):focus-visible {
  outline: 1px solid color-mix(in oklab, var(--accent) 50%, transparent);
  outline-offset: 2px;
}
.card { background: var(--sfr); border: 1px solid var(--border); border-radius: 6px;
        transition: border-color 120ms ease; }
.card:hover { border-color: var(--border2); }
.card.is-active { box-shadow: inset 2px 0 0 var(--accent); background: var(--sf2); }
```

## Prochaine étape

Pour appliquer dans ton app, il faut mapper ces tokens sur les noms existants :

- `--bg` → existe ? Probablement déjà mappé dans `foundation.css`
- `--ac` (accent actuel) → `--accent`
- `--am` (accent-mid actuel) → soit on le supprime, soit on lui donne une variante claire de l'accent

Dis-moi quand tu veux que je fasse l'inventaire de mapping `themes.css` / `foundation.css` → tokens cibles, et je te donne le diff minimal pour tout swap d'un coup. Pas avant que tu valides.