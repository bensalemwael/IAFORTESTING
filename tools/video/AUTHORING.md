# Écrire un épisode vidéo

Un épisode est un module Python dans `episodes/` qui définit `META` et `SCENES`, construits avec les modèles de `scenes.py`.
Lisez `scenes.py` (docstrings) et l'épisode de référence `episodes/genai_ch2_ep1.py` avant d'écrire : copiez son ton, son rythme et sa densité.

## Règles de narration (voix Vivienne, sous-titres incrustés)

- Français oral, chaleureux et clair, phrases courtes. On parle à l'apprenant (« vous »). Pas de jargon non expliqué.
- Les nombres et sigles s'écrivent comme ils se prononcent : « K trois », « deux point un point trois », « quarante-deux mille un », « RAG ».
- Apostrophes droites `'`. Pas de balises, pas d'émojis dans la narration.
- Chaque scène dure entre 20 et 50 secondes de parole. Un épisode fait 10 à 15 minutes (environ 1 500 à 2 200 mots), 18 à 26 scènes.
- Max (voix masculine) intervient 2 ou 3 fois par épisode, avec une réplique courte et naturelle : `{"max": "..."}`. La vedette répond ensuite.
- Tout doit être exact selon le syllabus officiel. Citez la logique de l'examen : pièges, distinctions, niveaux K.
- Toutes les questions et exemples sont originaux : ne copiez ni ne paraphrasez les examens d'exemple officiels.

## Repères

Dans la narration, `{#nom}` déclenche l'animation `nom` au début du mot suivant. Chaque modèle attend ses repères :

| Modèle | Repères à placer |
|---|---|
| `title_scene` | `sub`, `chips` |
| `cards` | `c0`, `c1`… (une par carte) ; `trap` si `trap=` |
| `rows` | `r0`, `r1`… ; `trap` si `trap=` |
| `chat` | `type`, `send`, `answer` ; `verdict` si `verdict=` ; `note` si `note=` |
| `prompt_build` | `l0`, `l1`… ; `badge` si `badge=` |
| `flow` | `s0`, `s1`… ; `check` si `check=` ; `loop` si `loop=True` |
| `versus` | `left`, `right` |
| `table` | `r0`, `r1`… |
| `bignum` | `n`, `cap` |
| `code` | `code` ; `note` si `note=` |
| `quiz` | `rev` au début de `reveal` (les options et le compte à rebours sont automatiques) |

Un repère manquant fait échouer la génération avec un message clair. Placez les repères au moment où la voix parle de l'élément.

## Contraintes de mise en page (1920 × 1080)

- Titres de scène : 60 caractères maximum (45 si Max intervient).
- `cards` : 3 à 6 cartes ; textes de carte de 120 caractères maximum. `rows` : 6 lignes maximum, 110 caractères par ligne.
- `chat` : prompt de 160 caractères maximum, réponse de 6 lignes maximum (`\n`).
- `prompt_build` : 8 lignes maximum, 60 caractères par ligne. `code` : 16 lignes maximum, 75 caractères par ligne.
- `table` : 5 lignes maximum, 3 colonnes. `quiz` : 4 options courtes (70 caractères maximum) ; explication de 120 caractères maximum.
- `trap=` : une phrase de 130 caractères maximum, avec `**gras**` pour le mot clé.

## Vérifier

```text
python build.py <module> --page-only
```

Cette commande synthétise les voix (mises en cache), vérifie tous les repères et affiche la durée. Elle ne génère pas la vidéo.
