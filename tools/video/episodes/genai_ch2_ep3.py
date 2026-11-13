# CT-GenAI v1.1 · Chapitre 2 · Épisode 3 : automatiser la régression et piloter les tests (sections 2.2.3 à 2.2.5).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import cards, chat, code, flow, quiz, rows, table, title_scene, versus

K = "CT-GenAI · Chapitre 2 · "

META = {
    "file": "genai-chapitre-2-episode-3",
    "title": "CT-GenAI · Chapitre 2 · Épisode 3 : automatiser la régression et piloter les tests",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 2 · Épisode 3 sur 4",
        "Automatiser la régression et piloter les tests",
        "Régression automatisée, pilotage et contrôle, et choix de la bonne technique de prompting",
        ["Sections 2.2.3 à 2.2.5", "3 objectifs K3", "Environ 13 minutes"],
        ["Bonjour, et bienvenue dans le troisième épisode du chapitre deux. {#sub}Au programme : les tests de régression automatisés "
         "avec l'IA générative, puis le pilotage et le contrôle des tests, et enfin une compétence clé pour l'examen : "
         "choisir la bonne technique de prompting selon la situation. {#chips}Trois objectifs de niveau K trois. "
         "Et pour le dernier, on s'entraînera sur plusieurs scénarios. C'est parti."],
    ),
    flow(
        K + "2.2.3", "Pourquoi la régression appelle l'automatisation",
        [("📈", "La suite grossit", "Chaque itération ou version ajoute des tests de régression"),
         ("🔁", "Elle tourne souvent", "En CI/CD, les tests s'exécutent à haute fréquence"),
         ("🤖", "L'IA aide", "Créer, maintenir et optimiser les suites automatisées"),
         ("🎯", "Analyse d'impact", "Cibler les zones les plus touchées par les changements")],
        ["Partons d'un constat. {#s0}À chaque nouvelle itération ou version, le nombre de cas de test de régression à exécuter augmente souvent. "
         "{#s1}Ce sont donc des candidats idéaux pour l'automatisation, surtout dans les pipelines d'intégration et de livraison continues, "
         "où les tests s'exécutent très souvent. {#s2}L'IA générative aide à créer, maintenir et optimiser ces suites de régression automatisées. "
         "{#s3}En s'adaptant dynamiquement aux changements du code, et grâce à l'analyse d'impact, elle identifie les zones du logiciel "
         "les plus susceptibles d'être affectées. On concentre alors l'effort de régression là où il est le plus nécessaire."],
    ),
    cards(
        K + "2.2.3", "Cinq activités soutenues par le prompting",
        [("🔑", "Scripts keyword-driven", "Associer des mots-clés prédéfinis aux cas de test, et générer les scripts."),
         ("🎯", "Analyse d'impact et optimisation", "Analyser les changements de code pour cibler les zones à haut risque."),
         ("🩹", "Tests auto-réparateurs et adaptatifs", "Ajuster les scripts aux petits changements d'IHM ou d'API, sans échec inutile."),
         ("📊", "Rapports et enseignements automatisés", "Rapports détaillés, tableaux de bord de tendances, prédiction des points de défaillance."),
         ("🐞", "Défauts et causes racines", "Rapports de défaut complets : journaux, captures d'écran, données d'environnement.")],
        ["Le syllabus cite cinq activités que l'IA peut soutenir. {#c0}Un : les scripts keyword-driven, dirigés par les mots-clés. "
         "Des mots-clés prédéfinis représentent des étapes courantes ; l'IA les associe aux cas de test et génère les scripts. "
         "{#c1}Deux : l'analyse d'impact et l'optimisation des tests, pour cibler les zones à haut risque. "
         "{#c2}Trois : les tests auto-réparateurs et adaptatifs, qui s'ajustent aux petits changements d'interface ou d'API. "
         "{#c3}Quatre : les rapports de test et les enseignements automatisés, avec des tableaux de bord de tendances et des prédictions sur les points de défaillance. "
         "{#c4}Cinq : des rapports de défaut enrichis, et l'analyse des causes racines. "
         "Ces activités valent pour la régression fonctionnelle comme non fonctionnelle."],
        cols=3,
    ),
    code(
        K + "HO-2.2.3a", "Few-shot : des scripts keyword-driven",
        "# Mots-clés : Ouvrir Page(url) · Saisir(champ, valeur)\n"
        "#             Cliquer(élément) · Vérifier Texte(élément, attendu)\n\n"
        "# Exemple 1 : Connexion valide\n"
        "Ouvrir Page      /connexion\n"
        "Saisir           email          lea@exemple.test\n"
        "Cliquer          btn-connexion\n"
        "Vérifier Texte   bandeau        Bonjour Léa\n\n"
        "# Exemple 2 : Recherche d'un produit\n"
        "Saisir           recherche      casque audio\n"
        "Cliquer          btn-recherche\n"
        "Vérifier Texte   resultats      12 produits\n\n"
        "# À toi : « Ajouter un article au panier »",
        ["Premier exercice de la section, le deux point deux point trois a, sur une application web et un framework d'automatisation d'interface. "
         "{#code}On documente d'abord la bibliothèque de mots-clés : ouvrir page, saisir, cliquer, vérifier texte. "
         "Puis on donne deux exemples complets de scripts, et on demande un nouveau script : ajouter un article au panier. "
         "{#note}Le modèle génère les scripts initiaux. On lui fait ensuite valider ces scripts, puis on étend la couverture "
         "avec des scripts supplémentaires. Des exemples pour un format répétitif et contraint : c'est du few-shot."],
        note=("Few-shot", "Bibliothèque documentée + exemples : le modèle suit le format des exemples.", "ok"),
    ),
    chat(
        K + "HO-2.2.3a", "Un assistant de débogage par system prompt",
        "Vérifie ce script : Ouvrir Page /produit/42 · Cliquer Sur btn-ajout · Vérifier Texte panier-compteur",
        "Ligne 2 : « Cliquer Sur » n'existe pas dans la bibliothèque.\n→ Correction : Cliquer   btn-ajout\n"
        "Ligne 3 : valeur attendue manquante pour « Vérifier Texte ».\n→ Correction : Vérifier Texte   panier-compteur   1\n"
        "Script corrigé ci-dessous, à relire avant exécution.",
        ["Deuxième partie de l'exercice : le débogage. On crée un assistant avec un system prompt, par exemple : "
         "tu vérifies et corriges des scripts keyword-driven, en n'utilisant que les mots-clés de la bibliothèque. "
         "{#type}Ensuite, le testeur lui soumet un script. {#send}"
         "{#answer}L'assistant repère un mot-clé inconnu, « cliquer sur », puis un paramètre manquant, et propose une correction pour chacun. "
         "{#note}Le system prompt reste constant pendant toute la session : chaque script est contrôlé selon les mêmes règles. "
         "On combine ainsi l'automatisation classique et une validation assistée par l'IA."],
        note=("System prompt de l'assistant", "« Vérifie et corrige les scripts. N'utilise que les mots-clés de la bibliothèque. »", "ok"),
    ),
    chat(
        K + "2.2.3", "Démo : l'analyse d'impact",
        "Voici le diff du commit 8c1e (frais de port) et nos 240 tests de régression. Quelles zones sont à risque ? Quels tests lancer en priorité ?",
        "Zones à haut risque : frais de port, récapitulatif de commande, facture.\nTests ciblés : 31 sur 240 (frais, panier, paiement, facturation).\n"
        "À surveiller : la fonction arrondi() sert aussi aux remises.\n→ Ajouter les 6 tests de remise au lot prioritaire.",
        ["Passons à l'analyse d'impact, dans une boutique en ligne. {#type}On fournit le diff d'un commit sur le calcul des frais de port, "
         "avec la liste des deux cent quarante tests de régression. {#send}"
         "{#answer}Le modèle identifie les zones à haut risque, propose trente et un tests ciblés, et repère même une fonction d'arrondi partagée avec les remises. ",
         {"max": "Donc je ne lance plus que ces trente et un tests ?"},
         "Pas si vite, Max. L'analyse d'impact cible la régression là où elle est le plus nécessaire. "
         "{#note}Mais l'IA peut se tromper : sa sortie doit être vérifiée avec soin, en fonction du risque associé. "
         "Le chapitre trois reviendra sur ces risques."],
        note=("L'IA peut se tromper", "On vérifie sa sortie avec un soin proportionné au risque associé.", "warn"),
    ),
    versus(
        K + "2.2.3", "Régression de bout en bout : IHM ou API",
        ("🖥️ Tests par l'IHM", ["Instables : l'interface change souvent", "L'IA adapte les scripts aux localisateurs dynamiques",
                               "… et aux interactions modifiées", "Moins d'interventions manuelles"]),
        ("🔌 Tests d'API", ["Formats de requête et de réponse qui changent", "Endpoints et authentification qui évoluent",
                           "L'IA adapte les scripts aux spécifications d'API", "Elle génère des données de test variées"]),
        ["L'IA aide aussi la régression automatisée de bout en bout, par l'interface graphique ou par les API. Chacune a ses propres difficultés. "
         "{#left}Les tests par l'interface deviennent souvent instables, car l'interface change régulièrement. "
         "L'IA peut adapter automatiquement les scripts aux localisateurs dynamiques et aux interactions modifiées, ce qui réduit les interventions manuelles. "
         "{#right}Les tests d'API, eux, subissent des formats de requête et de réponse, des endpoints et une authentification qui évoluent. "
         "L'IA adapte les scripts aux spécifications d'API, et génère des données de test variées. "
         "La couverture reste complète, avec moins de mises à jour manuelles."],
    ),
    code(
        K + "2.2.3", "Démo : un test auto-réparateur",
        "ÉCHEC  TC-112 « Payer la commande »\n"
        "  Localisateur introuvable : #btn-pay\n\n"
        "DOM actuel :\n"
        "  <button data-testid=\"checkout-pay\" class=\"btn\">Payer</button>\n\n"
        "Proposition de l'IA :\n"
        "  - page.locator('#btn-pay')\n"
        "  + page.getByTestId('checkout-pay')\n"
        "  Raison : même libellé, même position, identifiant renommé.\n\n"
        "Après adaptation : TC-112 ✓ réussi",
        ["Voyons l'auto-réparation en action. {#code}Le test « payer la commande » échoue : le localisateur du bouton est introuvable. "
         "L'IA examine la page actuelle : le bouton existe toujours, avec le même libellé, mais son identifiant a été renommé. "
         "Elle propose un nouveau localisateur, et le test repasse. {#note}C'est le but des tests auto-réparateurs : "
         "éviter les échecs inutiles dus à de petites modifications, et garder une suite stable. "
         "{#trap}Mais ce correctif touche le paiement, une zone à fort risque : on le relit avant de l'accepter."],
        note=("Auto-réparation", "Petit changement d'IHM : le script s'adapte, sans échec inutile.", "ok"),
        trap="L'IA peut se tromper : plus le **risque** est élevé, plus la vérification de sa sortie doit être soigneuse.",
    ),
    quiz(
        K + "Entraînement 2.2.3",
        "Après la mise à jour d'un service de suivi de colis, 40 tests d'API échouent : un champ a été renommé, le comportement est intact. Quelle activité aide le plus ?",
        ["Tests auto-réparateurs et adaptatifs", "Analyse d'impact et optimisation",
         "Rapports de défaut enrichis", "Scripts keyword-driven"], 0,
        "Petit changement d'API, aucun vrai défaut : les tests adaptatifs ajustent les scripts et évitent les échecs inutiles.",
        ["Scénario d'examen, en logistique. Après la mise à jour d'un service de suivi de colis, quarante tests d'API échouent : "
         "un champ de la réponse a été renommé, mais le comportement est intact. Quelle activité aide le plus ?"],
        ["{#rev}Les tests auto-réparateurs et adaptatifs : ils ajustent les scripts aux petits changements d'interface ou d'API. "
         "L'analyse d'impact, elle, sert à choisir quels tests lancer, pas à réparer des scripts."],
    ),
    rows(
        K + "HO-2.2.3b", "Analyser un rapport de régression pas à pas",
        [("Analyser et comparer", "Analyser les résultats de test fournis, et les comparer à la spécification de test."),
         ("Regrouper", "Regrouper les défauts similaires."),
         ("Tenir la liste des anomalies connues", "Mettre à jour la liste des anomalies déjà identifiées."),
         ("Recouper", "Vérifier les constats en les croisant entre eux.")],
        ["Deuxième exercice : le deux point deux point trois b, des prompts structurés pour analyser un rapport de tests de régression. "
         "La démarche est méthodique. {#r0}D'abord, on analyse les résultats fournis, et on les compare à la spécification de test. "
         "{#r1}Ensuite, on regroupe les défauts similaires. {#r2}Puis on tient à jour la liste des anomalies connues. "
         "{#r3}Enfin, on recoupe les constats. {#trap}Chaque étape est reliée à la suivante, dans une seule conversation avec le modèle. "
         "Les résultats et les journaux de test deviennent des informations exploitables."],
        trap="Une **seule conversation** : chaque prompt structuré s'appuie sur la réponse de l'étape précédente.",
    ),
    chat(
        K + "HO-2.2.3b", "Démo : regrouper les échecs",
        "Étape 2. Regroupe les 37 échecs de la régression nocturne par cause probable. Format : groupe | nombre | cause | anomalie connue ?",
        "A | 21 | Délai dépassé, passerelle de paiement | non\nB | 12 | Date affichée MM/JJ au lieu de JJ/MM | non\n"
        "C | 3 | Image produit manquante | oui, AN-112\nD | 1 | Cause indéterminée : analyse manuelle requise | non",
        ["{#type}À l'étape deux, dans la même conversation, on demande de regrouper les trente-sept échecs de la régression nocturne "
         "par cause probable, dans un format précis. {#send}"
         "{#answer}Le modèle forme quatre groupes : vingt et un dépassements de délai sur la passerelle de paiement, douze problèmes de format de date, "
         "trois échecs liés à une anomalie déjà connue, et un échec isolé à analyser. "
         "{#note}Au lieu de trente-sept échecs, l'équipe traite quatre problèmes. Et le groupe C alimente l'étape suivante : "
         "la liste des anomalies connues."],
        note=("37 échecs → 4 problèmes", "Les regroupements alimentent la liste des anomalies connues, puis le recoupement.", "ok"),
    ),
    quiz(
        K + "Entraînement HO-2.2.3b",
        "Le LLM classe 9 échecs d'une version bancaire comme « anomalie connue AN-31 » et propose de les exclure du rapport. Que faire ?",
        ["Recouper ce classement avant de l'accepter", "Les exclure : le LLM connaît l'historique",
         "Relancer toute la régression", "Supprimer AN-31 de la liste"], 0,
        "L'IA peut se tromper. Sur une version bancaire, à risque élevé, on recoupe avant d'accepter.",
        ["Scénario bancaire. Le modèle classe neuf échecs d'une version comme une anomalie déjà connue, "
         "et propose de les exclure du rapport. Que faites-vous ?"],
        ["{#rev}On recoupe ce classement avant de l'accepter. C'est la dernière étape de l'exercice, et c'est la règle du syllabus : "
         "l'IA peut se tromper, et plus le risque est élevé, plus on vérifie soigneusement."],
    ),
    cards(
        K + "2.2.4", "Pilotage et contrôle : quatre tâches",
        [("📡", "Pilotage et analyse des métriques", "Suivi automatisé, tendances, prédiction des risques, alertes en cas d'écart au plan."),
         ("🎛️", "Contrôle des tests", "Pistes pour reprioriser les tests, ajuster le calendrier, réallouer les ressources."),
         ("🎓", "Clôture et apprentissage continu", "Rapports de clôture : succès et leçons apprises, pour affiner la stratégie de test."),
         ("📈", "Visualisation et reporting", "Tableaux de bord dynamiques et résumés en langage naturel pour toutes les parties prenantes.")],
        ["Objectif deux point deux point quatre : le pilotage et le contrôle des tests. Le pilotage demande de récupérer beaucoup de données, "
         "parfois non structurées, souvent déjà présentes dans les outils de gestion des tests. L'IA aide à les analyser et à les synthétiser. "
         "{#c0}Première tâche : automatiser le suivi et analyser les tendances, pour prédire les risques et alerter l'équipe en cas d'écart au plan. "
         "{#c1}Deuxième : le contrôle, avec des pistes pour reprioriser, ajuster le calendrier ou réallouer des ressources. "
         "{#c2}Troisième : des rapports de clôture, avec les succès et les leçons apprises. "
         "{#c3}Quatrième : des tableaux de bord dynamiques et des résumés en langage naturel, pour toutes les parties prenantes."],
        cols=2,
    ),
    chat(
        K + "HO-2.2.4", "Démo : des métriques de pilotage",
        "Export CSV de l'outil de gestion des tests, sprint 14. Calcule avancement, tendance des défauts et couverture, signale les risques, résume pour le comité.",
        "Avancement : 312 tests exécutés sur 400 (78 %), 6 % de retard sur le plan.\nDéfauts : 19 ouverts, dont 7 en facturation, en hausse depuis 3 jours.\n"
        "Couverture : 46 exigences sur 50 ; 4 sans test, dont 2 critiques.\nRisque : la facturation menace la date de livraison.\n"
        "Résumé : « Bonne progression ; la facturation est le point d'attention. »",
        ["Voici la démonstration de l'objectif pratique deux point deux point quatre. {#type}À partir de données extraites des outils de test, "
         "on demande l'avancement, la tendance des défauts et la couverture, les risques, et un résumé pour le comité. {#send}"
         "{#answer}Le modèle produit les métriques clés, repère la hausse des défauts de facturation, et signale quatre exigences sans test. ",
         {"max": "Et le directeur, il va vraiment lire tout ça ?"},
         "Non, Max : il lira le résumé. {#note}Ces métriques peuvent alimenter un tableau de bord, et le résumé en langage naturel "
         "les rend compréhensibles par tous. Les données de test deviennent des informations utiles pour décider vite."],
        note=("Des données aux décisions", "Métriques → tableau de bord + résumé en langage naturel pour toutes les parties prenantes.", "ok"),
    ),
    quiz(
        K + "Entraînement 2.2.4",
        "Mi-sprint, les défauts de facturation augmentent. Le test manager demande au LLM comment reprioriser les tests et réaffecter deux testeurs. Quelle tâche ?",
        ["Contrôle des tests", "Pilotage et analyse des métriques",
         "Clôture et apprentissage continu", "Visualisation et reporting"], 0,
        "Reprioriser, ajuster le calendrier, réallouer les ressources : c'est le contrôle. Le pilotage détecte l'écart.",
        ["Scénario. En milieu de sprint, les défauts de facturation augmentent. Le test manager demande au modèle "
         "comment reprioriser les tests et réaffecter deux testeurs. Quelle tâche est soutenue ?"],
        ["{#rev}Le contrôle des tests. Attention au piège : détecter la hausse des défauts, c'est le pilotage. "
         "Décider comment réagir, en repriorisant et en réallouant les ressources, c'est le contrôle."],
    ),
    table(
        K + "2.2.5", "Quelle technique pour quelle tâche ?",
        ["Technique", "Usage recommandé", "Caractéristiques et applications"],
        [("🔗 Chaînage de prompts", "Tâches complexes exigeant de la précision, avec vérification humaine à chaque étape",
          "Petites étapes contrôlées : analyse de test, conception, automatisation"),
         ("🧩 Few-shot", "Tâches répétitives, ou au format de sortie spécifique et contraint",
          "Des exemples à suivre : Gherkin, keyword-driven, rapports au format imposé"),
         ("🪄 Méta-prompting", "Tâches flexibles et dynamiques ; créer des prompts pour de nouvelles tâches",
          "On décrit objectif et tâche, le LLM crée le prompt : analyse de rapports, anomalies")],
        ["Objectif deux point deux point cinq : choisir la technique de prompting. Le syllabus résume tout dans un tableau. "
         "{#r0}Le chaînage convient aux tâches complexes qui exigent de la précision, avec une vérification humaine à chaque étape. "
         "On découpe en petites étapes, en analyse, en conception ou en automatisation, et chaque étape est vérifiée. "
         "{#r1}Le few-shot convient aux tâches répétitives, ou à format de sortie spécifique : du Gherkin, du keyword-driven, "
         "ou des rapports de test au format imposé. {#r2}Le méta-prompting convient aux tâches flexibles et dynamiques, "
         "et à la création de prompts pour des tâches nouvelles. On décrit l'objectif et la tâche, et le modèle construit le prompt. "
         "Il sert pour des tâches complexes comme l'analyse de rapports de test et la détection d'anomalies."],
    ),
    rows(
        K + "HO-2.2.5", "La méthode : lire la nature de la tâche",
        [("Précision, étapes à valider ?", "Tâche complexe, résultats intermédiaires vérifiés par un humain → chaînage de prompts."),
         ("Structure répétitive ou format imposé ?", "Le même gabarit à reproduire en série → few-shot, avec de bons exemples."),
         ("Tâche nouvelle, prompt à inventer ?", "Objectif connu mais prompt à construire, tâche flexible → méta-prompting."),
         ("Plusieurs besoins à la fois ?", "On combine les techniques.")],
        ["Comment choisir, à l'examen comme au travail ? L'exercice deux point deux point cinq le dit : on évalue la nature de la tâche. "
         "Exige-t-elle de la précision, ou une structure répétitive ? {#r0}Si elle est complexe, et demande précision et vérifications intermédiaires : chaînage. "
         "{#r1}Si elle est répétitive, ou impose un format de sortie : few-shot. "
         "{#r2}Si elle est nouvelle et flexible, et que vous ne savez pas encore quel prompt écrire : méta-prompting. "
         "{#r3}Et si plusieurs besoins se cumulent, on combine. {#trap}Repérez les indices du scénario : ils pointent vers la bonne technique."],
        trap="**Précision + vérification** → chaînage. **Répétitif ou format** → few-shot. **Nouveau, flexible** → méta-prompting.",
    ),
    flow(
        K + "2.2.5", "Combiner les trois techniques",
        [("🪄", "Méta-prompting", "Créer le prompt initial"),
         ("🧩", "Few-shot", "Adapter et enrichir les exemples qu'il contient"),
         ("🔗", "Chaînage", "Découper en sous-tâches pour valider chaque étape")],
        [{"max": "Et si ma tâche coche plusieurs cases à la fois ?"},
         "Alors on combine, Max. Le syllabus le dit : on peut utiliser plusieurs techniques pour un seul cas d'usage. "
         "{#s0}D'abord, le méta-prompting crée un prompt initial. {#s1}Ce prompt peut contenir des exemples, à adapter et à enrichir : "
         "c'est du few-shot. {#s2}Enfin, on divise la tâche en sous-tâches plus petites, pour valider les étapes intermédiaires : c'est le chaînage. "
         "{#check}Les techniques ne s'excluent pas : elles se complètent."],
        check="✔ Un seul cas d'usage peut mobiliser les trois techniques",
    ),
    quiz(
        K + "Entraînement HO-2.2.5",
        "Une équipe hospitalière doit rédiger 150 scénarios Gherkin pour des user stories d'ordonnance, toutes au même gabarit strict. Quelle technique ?",
        ["Chaînage de prompts", "Few-shot", "Méta-prompting", "Zero-shot"], 1,
        "Tâche répétitive et format imposé : quelques exemples de référence guident toute la série. C'est le few-shot.",
        ["Premier scénario. Dans un hôpital, l'équipe doit rédiger cent cinquante scénarios Gherkin pour des user stories "
         "d'ordonnance électronique, toutes au même gabarit strict. Quelle technique choisir ?"],
        ["{#rev}Le few-shot. Deux indices : la tâche est répétitive, et le format de sortie est imposé. "
         "Quelques exemples bien choisis suffisent à guider toute la série."],
    ),
    quiz(
        K + "Entraînement HO-2.2.5",
        "Un testeur analyse une exigence anti-fraude complexe. Chaque résultat intermédiaire doit être validé par un expert conformité. Quelle technique ?",
        ["Few-shot", "Méta-prompting", "Chaînage de prompts", "Un seul prompt très détaillé"], 2,
        "Tâche complexe, précision, validation humaine à chaque étape : c'est exactement le chaînage.",
        ["Deuxième scénario, en banque. Un testeur analyse une exigence anti-fraude complexe, et chaque résultat intermédiaire "
         "doit être validé par un expert conformité. Quelle technique ?"],
        ["{#rev}Le chaînage de prompts. Tâche complexe, besoin de précision, vérification humaine de chaque étape : tous les indices y sont. "
         "Un seul gros prompt ne permettrait pas ces validations intermédiaires."],
    ),
    quiz(
        K + "Entraînement HO-2.2.5",
        "Une équipe logistique doit, pour la première fois, détecter des anomalies dans des journaux de capteurs. Elle ne sait pas quel prompt écrire. Quelle technique ?",
        ["One-shot", "Few-shot", "Chaînage de prompts", "Méta-prompting"], 3,
        "Tâche nouvelle et flexible, prompt à construire : on décrit l'objectif, le LLM aide à créer le prompt.",
        ["Troisième scénario. Une équipe logistique doit, pour la première fois, détecter des anomalies dans des journaux de capteurs. "
         "Elle ne sait pas comment formuler sa demande. Quelle technique ?"],
        ["{#rev}Le méta-prompting. La tâche est nouvelle, et l'équipe ne sait pas encore quel prompt écrire : elle décrit l'objectif, "
         "et le modèle l'aide à construire le prompt. Le syllabus cite d'ailleurs la détection d'anomalies parmi ses usages."],
    ),
    quiz(
        K + "Entraînement HO-2.2.5",
        "Chaque semaine, le rapport de régression doit suivre exactement les 5 rubriques des rapports précédents. Quelle technique ?",
        ["Méta-prompting", "Few-shot", "Chaînage de prompts", "Zero-shot"], 1,
        "Rapport répétitif au format imposé : le few-shot. Le méta-prompting sert quand le prompt reste à inventer.",
        ["Quatrième scénario, plus piégeux. Chaque semaine, le rapport de régression doit suivre exactement les cinq rubriques "
         "des rapports précédents. Quelle technique ?"],
        ["{#rev}Le few-shot, avec d'anciens rapports comme exemples. Le piège : le mot « rapport » fait penser au méta-prompting. "
         "Mais ici, la tâche est répétitive et le format imposé. C'est le few-shot."],
    ),
    quiz(
        K + "Entraînement HO-2.2.5",
        "Une équipe veut générer des scripts keyword-driven : elle ignore comment écrire le prompt, exige un format strict et des étapes validées. Que faire ?",
        ["Méta-prompting seul", "Few-shot seul", "Méta-prompting, puis few-shot, puis chaînage", "Un seul prompt zero-shot"], 2,
        "Plusieurs besoins se cumulent : on combine les techniques, comme le décrit le syllabus.",
        ["Dernier scénario. Une équipe veut générer des scripts keyword-driven. Elle ignore comment écrire le prompt, "
         "elle exige un format strict, et elle veut valider chaque étape. Que faire ?"],
        ["{#rev}On combine. Le méta-prompting crée le prompt initial, le few-shot impose le format par des exemples, "
         "et le chaînage permet de valider chaque étape. Quand les besoins se cumulent, une seule technique ne suffit pas."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes de l'épisode 3",
        [("Régression et CI/CD", "La suite grossit à chaque version : on automatise, et on cible par l'analyse d'impact."),
         ("5 activités", "Keyword-driven, analyse d'impact, auto-réparation, rapports et enseignements, défauts et causes racines."),
         ("IHM et API", "IHM : localisateurs et interactions. API : formats, endpoints, authentification."),
         ("Vérifier selon le risque", "L'IA peut se tromper : plus le risque est élevé, plus on vérifie."),
         ("4 tâches de pilotage", "Métriques, contrôle, clôture et apprentissage, visualisation et reporting."),
         ("Choisir la technique", "Précision → chaînage. Répétitif ou format → few-shot. Nouveau → méta. Ou combiner.")],
        ["Récapitulons. {#r0}Un : la suite de régression grossit à chaque version ; on l'automatise, et on la cible grâce à l'analyse d'impact. "
         "{#r1}Deux : cinq activités soutenues par l'IA, du keyword-driven jusqu'à l'analyse des causes racines. "
         "{#r2}Trois : l'interface et les API ont chacune leurs difficultés. {#r3}Quatre : l'IA peut se tromper, on vérifie selon le risque. "
         "{#r4}Cinq : quatre tâches de pilotage et de contrôle. "
         "{#r5}Et six : précision, chaînage ; répétition ou format, few-shot ; tâche nouvelle, méta-prompting. Et souvent, on combine."],
    ),
    title_scene(
        "À suivre · Épisode 4",
        "Évaluer les résultats et affiner ses prompts",
        "Métriques d'évaluation et techniques pour améliorer ses prompts, pas à pas",
        ["Section 2.3", "2 objectifs K2", "Fin du chapitre 2"],
        ["Bravo, c'est la fin de ce troisième épisode. {#sub}Dans le dernier épisode du chapitre, on apprend à évaluer les résultats "
         "de l'IA générative avec des métriques, et à affiner ses prompts de façon itérative. "
         "{#chips}Deux objectifs K deux, pour boucler le chapitre deux. D'ici là, entraînez-vous sur les scénarios dans l'application. À très vite !"],
    ),
]
