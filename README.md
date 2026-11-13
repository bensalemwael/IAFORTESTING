# Préparation ISTQB IA

Application hors ligne, en français, pour préparer deux certifications ISTQB :

| | **CT-GenAI v1.1** | **CT-AI v2.0** |
|---|---|---|
| Sujet | Utiliser l'IA générative **pour tester** | **Tester** des systèmes à base d'IA |
| Prérequis | Certificat CTFL | Certificat CTFL |
| Examen | 40 questions, 60 min (75 min en langue non maternelle) | 40 questions, 60 min (75 min en langue non maternelle) |
| Seuil | 30 / 46 points | 29 / 44 points |
| Formation minimale de référence | 13,6 h | 19,5 h |

**Quelle certification choisir ?** Si votre objectif est d'utiliser des LLM dans votre travail de testeur, commencez par CT-GenAI.
Si vous testez des modèles de ML ou des produits contenant de l'IA, choisissez CT-AI. La v2.0 ne traite plus de l'usage de l'IA pour tester.

L'examen CT-AI v1.0 reste proposé jusqu'au 21 avril 2027 en anglais et au 21 octobre 2027 dans les autres langues.
Ce projet couvre uniquement la v2.0. Beaucoup de ressources en ligne portent encore sur la v1.0 (11 chapitres).

## Démarrer

Double-cliquez sur `index.html`. Aucune installation ni connexion n'est nécessaire.
La progression est enregistrée dans le navigateur (localStorage) : elle disparaît si vous videz ses données ou si vous changez de navigateur.

| Onglet | Rôle |
|---|---|
| Cours | Fiches par chapitre, objectifs d'apprentissage et pièges d'examen |
| Entraînement | Séries de 10 questions corrigées, par chapitre ou sur vos erreurs |
| Examen blanc | 40 questions chronométrées, avec la répartition officielle par chapitre et niveau K |
| Flashcards | Mots-clés examinables, en répétition espacée |
| Métriques | Matrices de confusion à calculer à l'infini (CT-AI uniquement) |

La banque contient 143 questions originales pour CT-GenAI et 156 pour CT-AI, soit plus de trois examens blancs différents par certification.
Un examen en cours reprend après un rechargement de la page ; le chrono continue pendant votre absence.

## Vidéos

Les cinq chapitres de CT-GenAI sont expliqués en vidéo, en français : 10 épisodes animés de 10 à 14 minutes, soit un peu plus de deux heures.

| Chapitre | Épisodes |
|---|---|
| 1. Introduction à la GenAI pour le test | 1 |
| 2. Prompt engineering pour le test | 4 |
| 3. Gérer les risques de la GenAI | 2 |
| 4. Infrastructure de test à base de LLM | 2 |
| 5. Déployer la GenAI dans l'organisation de test | 1 |

Chaque épisode s'ouvre dans la fiche de son chapitre, onglet Cours, avec un sélecteur d'épisode ; les fichiers sont aussi dans `videos/`.
Les éléments apparaissent au mot près avec la voix, un second narrateur pose les questions que l'on se pose, et chaque épisode se termine par des quiz à compte à rebours. Les sous-titres sont incrustés.

Le générateur est dans `tools/video/` : un épisode est un module Python de `episodes/`, décrit dans `AUTHORING.md`.

```text
cd tools/video
npm install
pip install edge-tts imageio-ffmpeg
python build.py genai_ch2_ep1
```

Il demande Python, Node.js et Microsoft Edge ; la voix est synthétisée par le service en ligne de Microsoft.

## Ateliers pratiques

```text
python labs/perceptron.py
python labs/contraintes_dataset.py
python labs/metamorphique.py
```

Les exercices de prompting sont dans [labs/PROMPTS-GENAI.md](labs/PROMPTS-GENAI.md).

## Méthode conseillée

1. Lire la fiche d'un chapitre, puis la section correspondante du syllabus officiel.
2. S'entraîner sur ce chapitre et lire chaque explication.
3. Faire les flashcards dues chaque jour.
4. Passer un examen blanc une fois tous les chapitres couverts, puis retravailler les plus faibles.
5. Terminer par les examens d'exemple officiels, qui donnent le style réel des questions.

Au rythme d'une heure par jour, comptez environ 3 semaines pour CT-GenAI et 4 pour CT-AI. Ce sont des estimations.
Le chapitre 2 de CT-GenAI et le chapitre 3 de CT-AI sont les plus longs.

## Préparer sans budget de formation

Aucune formation n'est obligatoire pour ces deux examens : seul le certificat CTFL est exigé.
Les syllabus et les examens d'exemple officiels ci-dessous sont gratuits. Avec cette application, ils suffisent pour se préparer seul.
Les frais d'inscription à l'examen restent à payer à l'organisme de certification.

Les questions de ce projet sont originales et leur difficulté n'est pas calibrée sur l'examen réel : gardez les examens d'exemple officiels pour la fin, comme test final.

## Documents officiels

Le syllabus fait foi : le contenu de ce projet est une synthèse personnelle et non un support accrédité.

- CT-GenAI : [page officielle](https://istqb.org/certifications/gen-ai/), [syllabus v1.1](https://istqb.org/?sdm_process_download=1&download_id=6295), [examen d'exemple A](https://istqb.org/?sdm_process_download=1&download_id=6309), [réponses](https://istqb.org/?sdm_process_download=1&download_id=6301)
- CT-AI : [page officielle](https://istqb.org/certifications/certified-tester-ai-testing-ct-ai/), [syllabus v2.0](https://istqb.org/?sdm_process_download=1&download_id=9558), [examen d'exemple A](https://istqb.org/?sdm_process_download=1&download_id=9561), [réponses](https://istqb.org/?sdm_process_download=1&download_id=9564), [notes sur la v2.0](https://istqb.org/help/ct-ai-v2)
- [Tables de structure des examens](https://istqb.org/wp-content/uploads/2026/05/ISTQB_Exam-Structure-and-Rules-Tables_v1.18.pdf)

Avant de vous inscrire, vérifiez auprès de votre organisme la langue proposée et la version d'examen disponible.

## Modifier le contenu

- Questions : `data/genai-questions*.js` et `data/ai-questions*.js`. La bonne réponse est listée par indice ; les options sont mélangées à l'affichage.
- Fiches : `data/genai-notes.js` et `data/ai-notes.js`.
- Après une modification : `npm test` vérifie les quotas, les barèmes et la validité des questions.

ISTQB® est une marque déposée de l'International Software Testing Qualifications Board. Ce projet n'est ni affilié à l'ISTQB ni approuvé par lui.
Les questions sont originales. Les syllabus restent la propriété de l'ISTQB et de leurs auteurs.
