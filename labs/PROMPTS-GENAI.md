# Ateliers CT-GenAI

Ces exercices reprennent les objectifs pratiques du syllabus v1.1. Faites-les avec un chatbot autorisé.
N'y mettez aucune donnée réelle ou confidentielle : la user story ci-dessous est fictive.

## Matériau commun

> En tant que client, je veux transférer de l'argent entre mes comptes afin de gérer mon budget.
> Critères : montant de 1 à 5 000 € ; le compte source doit être approvisionné ; une confirmation est envoyée.

## 1. Prompt structuré (HO-2.1.1)

```text
Rôle : Tu es test analyst pour une banque en ligne.
Contexte : Fonction de transfert entre comptes d'un même client.
Instruction : Dérive les conditions de test de la user story.
Données d'entrée : <user story et critères>
Contraintes : N'utilise que les critères fournis. Signale toute ambiguïté au lieu de l'interpréter.
Format de sortie : Tableau ID | Condition | Critère source | Priorité.
```

Retirez un composant à la fois et comparez les sorties.

## 2. Prompt chaining avec vérification (HO-2.2.1b)

1. « Liste les ambiguïtés de ces critères. » Corrigez vous-même la liste.
2. « Avec ces corrections, évalue la testabilité de chaque critère. » Vérifiez.
3. « Évalue la complétude et propose les critères manquants. » Vérifiez.

## 3. Few-shot en Gherkin (HO-2.2.2b)

Écrivez deux exemples story → scénarios, ajoutez la story de transfert, et observez le respect du format.
Comparez avec le même prompt en zero-shot.

## 4. Meta prompting (HO-2.2.2a)

```text
Je veux un prompt qui transforme des cas de test en procédures de bout en bout.
Pose-moi les questions nécessaires, propose le prompt, puis critique-le.
```

## 5. Provoquer et détecter (HO-3.1.2a et b)

- **Hallucination** : demandez des tests « pour tous les critères » d'une story sans critères. Repérez ce qui est inventé.
- **Erreur de raisonnement** : donnez dix tests avec dépendances, durées et risques, demandez un ordre optimal, puis vérifiez à la main.
- **Non-déterminisme** : lancez le même prompt cinq fois et comptez les différences.

## 6. Évaluer un prompt (HO-2.3.2)

Faites un A/B entre deux versions. Notez sur plusieurs exécutions la couverture des critères (rappel),
les tests hors sujet (pertinence) et le temps de revue.

## 7. Estimer le coût (HO-5.1.3)

Coût mensuel = exécutions par mois × (tokens d'entrée × prix d'entrée + tokens de sortie × prix de sortie).
Comparez deux fournisseurs à partir de leurs tarifs publics du moment.

## 8. Red teaming pour CT-AI (AI-4.2.2)

Sur un système que vous êtes autorisé à tester, en environnement sûr, préparez une feuille de session :
objectif, comportement interdit, stratégies sur plusieurs tours, sorties observées, gravité, jeu de données de correction.
