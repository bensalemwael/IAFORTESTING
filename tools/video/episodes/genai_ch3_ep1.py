# CT-GenAI v1.1 · Chapitre 3 · Épisode 1 : hallucinations, erreurs de raisonnement et biais (section 3.1).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import cards, chat, code, quiz, rows, title_scene, versus

K = "CT-GenAI · Chapitre 3 · "

META = {
    "file": "genai-chapitre-3-episode-1",
    "title": "CT-GenAI · Chapitre 3 · Épisode 1 : hallucinations, erreurs de raisonnement et biais",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 3 · Épisode 1 sur 2",
        "Hallucinations, erreurs de raisonnement et biais",
        "Reconnaître les défauts des LLM, les détecter et les limiter",
        ["Section 3.1", "Objectifs K1, K2 et K3", "Environ 14 minutes"],
        ["Bonjour, et bienvenue dans le chapitre trois, consacré aux risques de l'IA générative dans les tests. "
         "{#sub}Dans ce premier épisode, on s'attaque aux trois grands défauts des LLM : les hallucinations, les erreurs de raisonnement et les biais. "
         "{#chips}Quatre objectifs, dont un K trois : savoir les repérer dans une vraie sortie de LLM. "
         "Il y aura donc beaucoup de scénarios. On y va."],
    ),
    cards(
        K + "Vue d'ensemble", "Le chapitre 3 en deux épisodes",
        [("🧠", "3.1 · Défauts des LLM", "Hallucinations, erreurs de raisonnement, biais, non-déterminisme. Épisode 1."),
         ("🔒", "3.2 · Confidentialité et sécurité", "Risques, vecteurs d'attaque et mesures de protection. Épisode 2."),
         ("🌱", "3.3 · Énergie", "Consommation d'énergie et émissions de CO2 de l'IA générative. Épisode 2."),
         ("📜", "3.4 · Réglementation", "Normes, réglementations et cadres de bonnes pratiques. Épisode 2.")],
        ["Le chapitre trois représente cent soixante minutes de formation officielle. On le découpe en deux épisodes. "
         "{#c0}Celui-ci couvre la section trois point un : les défauts des LLM et la façon de les maîtriser. "
         "{#c1}Le prochain épisode couvrira la confidentialité des données et la sécurité, "
         "{#c2}l'impact énergétique et environnemental, "
         "{#c3}et enfin les réglementations, normes et cadres de bonnes pratiques."],
    ),
    cards(
        K + "3.1.1", "Trois défauts à connaître par cœur",
        [("🌀", "Hallucination", "Une sortie qui semble factuellement incorrecte, ou sans rapport avec la tâche demandée."),
         ("🧩", "Erreur de raisonnement", "Le LLM interprète mal une structure logique, et arrive à une conclusion incorrecte."),
         ("⚖️", "Biais", "Une sortie qui favorise certaines informations, approches ou hypothèses, héritée des données d'entraînement.")],
        ["Commençons par les définitions, l'objectif trois point un point un, de niveau K un. "
         "Les LLM sont sujets à certains défauts, en particulier ces trois-là. Ils dégradent la qualité des sorties : le testware généré ne répond plus aux attentes des testeurs. "
         "{#c0}Une hallucination, c'est une sortie qui semble factuellement incorrecte, ou sans rapport avec la tâche demandée. "
         "{#c1}Une erreur de raisonnement, c'est quand le modèle interprète mal une structure logique, et arrive à une conclusion incorrecte. "
         "{#c2}Et un biais, c'est une sortie qui favorise certains types d'informations, d'approches ou d'hypothèses. "
         "Le syllabus est clair : le testeur doit les identifier dans les sorties, et prendre des mesures pour réduire ces risques."],
    ),
    rows(
        K + "3.1.1", "Les hallucinations dans les tests",
        [("Cas de test fictifs", "Des cas de test inventés, ou sans rapport avec l'objet de test."),
         ("Scripts défaillants", "Des scripts de test incorrects, ou qui ne fonctionnent pas."),
         ("Critères inexistants", "Des cas de test qui vérifient des critères d'acceptation qui n'existent pas."),
         ("La conséquence", "Le testeur est induit en erreur, et la validité des résultats de test est compromise.")],
        ["À quoi ressemble une hallucination dans le travail du testeur ? Le syllabus donne trois formes. "
         "{#r0}Un : des cas de test fictifs, ou hors sujet. "
         "{#r1}Deux : des scripts de test incorrects, ou qui ne fonctionnent tout simplement pas. "
         "{#r2}Trois : des cas de test qui vérifient des critères d'acceptation qui n'existent pas. "
         "{#r3}Le danger, c'est que tout cela a l'air plausible. Le testeur peut être induit en erreur, et la validité de ses résultats de test est compromise."],
    ),
    chat(
        K + "HO-3.1.2a", "Démo : un critère sorti de nulle part",
        "Voici l'US-17 « Réinitialiser son mot de passe » et ses trois critères d'acceptation, CA1 à CA3. Écris un cas de test par critère.",
        "TC1 · CA1 : lien envoyé à l'adresse e-mail du compte\nTC2 · CA2 : lien expiré au bout de 24 heures\nTC3 · CA3 : nouveau mot de passe de 12 caractères minimum\nTC4 · CA4 : déblocage du compte par SMS après 3 échecs",
        ["Voyons une démonstration, dans l'esprit de l'exercice pratique trois point un point deux a. "
         "{#type}On donne une user story avec trois critères d'acceptation, et on demande un cas de test par critère. {#send}"
         "{#answer}Le modèle répond avec assurance : un, deux, trois… et quatre cas de test. ",
         {"max": "Attends… CA quatre ? La story n'a que trois critères !"},
         "{#verdict}Bien vu, Max. Le critère quatre n'existe nulle part dans les données fournies : c'est une hallucination. "
         "{#note}Dans cet exercice, le syllabus propose de confronter au moins deux LLM à ce genre de situation, "
         "et de varier les prompts pour observer leur influence sur les hallucinations."],
        verdict=("HALLUCINATION", "bad"),
        note=("Exercice HO-3.1.2a", "Confronter au moins deux LLM à ce piège, et varier les prompts pour voir leur influence.", "warn"),
    ),
    rows(
        K + "3.1.1", "Les erreurs de raisonnement",
        [("Ce qui est mal interprété", "Les structures logiques : cause et effet, logique conditionnelle, résolution étape par étape."),
         ("Pourquoi", "Le LLM n'a pas de vrai raisonnement logique : il s'appuie sur la reconnaissance de motifs."),
         ("Un point faible typique", "Le raisonnement mathématique."),
         ("Les tâches de test exposées", "La planification des tests et la priorisation des cas de test.")],
        ["Deuxième défaut : l'erreur de raisonnement. {#r0}Le modèle interprète mal une structure logique : une relation de cause à effet, "
         "une logique conditionnelle, ou un processus de résolution étape par étape. "
         "{#r1}Pourquoi ? Parce que, contrairement à un humain, un LLM n'a pas de véritable raisonnement logique. Il s'appuie sur la reconnaissance de motifs. "
         "{#r2}D'où des erreurs dans des tâches comme le raisonnement mathématique. "
         "{#r3}Côté test, le syllabus cite deux tâches qui exigent un raisonnement logique : la planification des tests, et la priorisation des cas de test. "
         "{#trap}Retenez la nuance : l'hallucination invente du contenu, l'erreur de raisonnement applique une logique fausse."],
        trap="**Hallucination** : contenu inventé ou hors sujet. **Erreur de raisonnement** : logique mal appliquée.",
    ),
    chat(
        K + "HO-3.1.2b", "Démo : un total qui ne tombe pas juste",
        "Estime l'effort d'exécution : 12 cas à 0,5 h, 8 cas à 1,5 h et 4 cas à 3 h. Donne le total.",
        "12 × 0,5 h = 6 h\n8 × 1,5 h = 12 h\n4 × 3 h = 12 h\nEffort total estimé : 28 heures",
        ["Deuxième démonstration, cette fois sur la planification des tests. "
         "{#type}On demande au modèle une estimation de l'effort d'exécution, à partir de trois groupes de cas de test. {#send}"
         "{#answer}Il détaille son calcul, ligne par ligne, et conclut : vingt-huit heures. ",
         {"max": "Vingt-huit heures, parfait. Je le reporte dans le plan de test !"},
         "{#verdict}Pas si vite, Max. Six, plus douze, plus douze, ça fait trente, pas vingt-huit. Chaque ligne est juste, mais la conclusion est fausse. "
         "{#note}C'est l'exercice trois point un point deux b : un problème de planification, comme l'estimation de l'effort ou la priorisation, "
         "avec des données d'entrée assez complexes. On compare la sortie au résultat exact, on essaie trois types de modèles, un LLM, un SLM et un modèle de raisonnement, "
         "et on varie le prompt pour tenter d'améliorer le résultat."],
        verdict=("RAISONNEMENT FAUX", "bad"),
        note=("Exercice HO-3.1.2b", "Comparer au résultat exact. Essayer un LLM, un SLM et un modèle de raisonnement. Varier le prompt.", "warn"),
    ),
    cards(
        K + "3.1.1", "Les biais",
        [("🧬", "Origine", "Les biais proviennent des données sur lesquelles le modèle a été entraîné."),
         ("⚖️", "Effet", "Des sorties qui favorisent certains types d'informations, d'approches ou d'hypothèses."),
         ("🌍", "Exemple", "Un LLM entraîné surtout sur des données en anglais peut sous-représenter les perspectives non anglophones."),
         ("🧪", "En test", "Ils peuvent influencer la génération de données de test, ou l'affinage des critères d'acceptation.")],
        ["Troisième défaut : les biais. {#c0}Ils proviennent des données sur lesquelles le modèle a été entraîné. "
         "{#c1}Résultat : des sorties qui favorisent certains types d'informations, certaines approches, ou certaines hypothèses. "
         "{#c2}L'exemple du syllabus : un LLM entraîné principalement sur des données en anglais peut sous-représenter les perspectives non anglophones. "
         "{#c3}En test, les biais peuvent influencer les réponses du modèle quand il génère des données de test, "
         "ou quand il affine des critères d'acceptation."],
    ),
    cards(
        K + "3.1", "D'où viennent ces défauts, et pourquoi ils persistent",
        [("📚", "Les données d'entraînement", "La nature des données d'entraînement est à l'origine de ces trois défauts."),
         ("🧠", "Les limites du transformer", "Les limites inhérentes à l'architecture transformer, vue au chapitre 1."),
         ("🎲", "Le non-déterminisme", "Il rend ces défauts difficiles à corriger : ils peuvent réapparaître dans une autre conversation.")],
        ["D'où viennent ces trois défauts ? {#c0}D'abord de la nature des données d'entraînement. "
         "{#c1}Ensuite, des limites inhérentes au modèle transformer, vu au chapitre un. "
         "{#c2}Et il y a une difficulté supplémentaire : le comportement non déterministe des LLM. Il rend ces défauts difficiles à corriger. "
         "{#trap}Un défaut peut sembler corrigé dans une réponse, puis réapparaître dans une autre conversation avec le même LLM. "
         "Reconnaître et traiter ces défauts, c'est justement ce qui améliore la qualité des résultats de l'IA dans nos tests."],
        trap="Corrigé une fois ne veut pas dire corrigé : le défaut peut **réapparaître** dans une autre conversation.",
    ),
    quiz(
        K + "3.1.1",
        "Selon le syllabus, d'où proviennent les biais d'un LLM ?",
        ["Des données sur lesquelles il a été entraîné", "D'une température réglée trop haut",
         "D'une graine aléatoire mal choisie", "Du matériel sur lequel il s'exécute"], 0,
        "Les biais proviennent des données d'entraînement : par exemple, des données surtout en anglais.",
        ["Première question, pour fixer les définitions. Selon le syllabus, d'où proviennent les biais d'un LLM ?"],
        ["{#rev}Des données sur lesquelles il a été entraîné. C'est l'origine que le syllabus donne explicitement pour les biais. "
         "Retenez le couple : biais et données d'entraînement. Et souvenez-vous où ils frappent en test : la génération de données de test, "
         "et l'affinage des critères d'acceptation."],
    ),
    rows(
        K + "3.1.2", "Détecter les hallucinations",
        [("Vérification croisée", "Comparer la sortie à la documentation, aux exigences et au comportement connu du système."),
         ("Consultation d'experts du domaine", "Faire valider l'exactitude par des experts, qui captent les nuances que l'automatisation manque."),
         ("Contrôles de cohérence", "Vérifier que les sorties sont cohérentes entre elles, et avec les informations connues.")],
        ["Passons à l'objectif clé du chapitre, trois point un point deux, de niveau K trois : identifier ces défauts dans une sortie de LLM. "
         "On s'appuie sur la revue, ou sur une combinaison de revue et de vérification automatisée. Et l'approche dépend du type de défaut. "
         "Pour les hallucinations, trois approches. {#r0}La vérification croisée : comparer la sortie avec la documentation existante, les exigences, "
         "et le comportement connu du système. Des outils automatisés peuvent aider à signaler les écarts. "
         "{#r1}La consultation d'experts du domaine, pour valider l'exactitude du contenu : ils captent des nuances que l'automatisation peut manquer. "
         "{#r2}Et les contrôles de cohérence : les sorties sont-elles cohérentes entre elles, et avec ce que l'on sait déjà ?"],
    ),
    rows(
        K + "3.1.2", "Détecter les erreurs de raisonnement et les biais",
        [("Raisonnement · Validation logique", "Revoir la cohérence et l'enchaînement du raisonnement. Cas complexes : jugement humain."),
         ("Raisonnement · Test des sorties", "Exécuter les cas ou scripts générés sur les objets de test, en partie ou tout automatisé."),
         ("Biais · Stratégie de test", "Le testware généré, code ou données synthétiques, reflète-t-il la stratégie et la couverture visées ?"),
         ("Biais · Types de test", "Repérer les types de test sous-représentés, comme les tests non fonctionnels.")],
        ["Pour les erreurs de raisonnement, deux approches. {#r0}La validation logique : évaluer, par des cycles de revue, la cohérence et "
         "l'enchaînement du raisonnement. Des outils peuvent aider, mais les cas complexes demandent un jugement humain. "
         "{#r1}Et le test des sorties : par exemple, exécuter les cas de test ou les scripts générés sur les objets de test, et vérifier les résultats. "
         "Selon le testware, c'est automatisable en partie ou totalement. "
         "Pour les biais, deux approches aussi. {#r2}Vérifier que le testware généré, comme du code de test ou des données synthétiques, "
         "représente fidèlement la stratégie de test et les exigences de couverture. "
         "{#r3}Et repérer les biais liés aux types de test, par exemple des tests non fonctionnels sous-représentés. "
         "{#trap}Enfin, l'effort de détection dépend du niveau de risque estimé pour la tâche de test."],
        trap="Le choix et l'effort de détection dépendent du **niveau de risque** estimé de la tâche de test.",
    ),
    chat(
        K + "3.1.2 · Scénario 1", "Scénario 1 : des données de test",
        "Génère 5 profils clients variés pour tester le formulaire d'inscription d'une boutique en ligne qui vend dans toute l'Europe.",
        "1. John Smith · Boston, USA · +1 617…\n2. Emily Brown · Chicago, USA · +1 312…\n3. Michael Davis · Denver, USA · +1 303…\n4. Sarah Wilson · Austin, USA · +1 512…\n5. David Clark · Seattle, USA · +1 206…",
        ["Place à l'entraînement K trois. Trois scénarios, trois sorties de LLM. À vous de repérer le défaut. "
         "{#type}Premier scénario : on demande cinq profils clients variés, pour tester le formulaire d'inscription d'une boutique en ligne "
         "qui vend dans toute l'Europe. {#send}"
         "{#answer}Lisez bien la réponse. Les noms, les villes, les numéros de téléphone. Qu'est-ce qui cloche ?"],
    ),
    quiz(
        K + "3.1.2 · Scénario 1",
        "Profils « variés » pour l'Europe, mais tous américains et anglophones. Quel défaut ?",
        ["Une hallucination", "Une erreur de raisonnement", "Un biais", "Aucun : la sortie est valide"], 2,
        "Un biais : les données générées favorisent un seul profil et ne représentent pas la population visée.",
        ["Les profils demandés devaient couvrir l'Europe, mais ils sont tous américains et anglophones. Quel défaut ?"],
        ["{#rev}Un biais. Rien n'est inventé ni illogique, mais les données favorisent un seul type de profil. "
         "On retrouve l'exemple des données d'entraînement surtout en anglais. Pour le détecter : vérifier que les données reflètent la stratégie et la couverture visées."],
    ),
    code(
        K + "3.1.2 · Scénario 2", "Scénario 2 : un script de test généré",
        "// Script généré pour la user story « Appliquer un code promo »\n"
        "test('code promo valide', async ({ page }) => {\n"
        "  await page.goto('/panier');\n"
        "  await page.fill('#code-promo', 'HIVER10');\n"
        "  await page.click('#appliquer');\n"
        "  await page.verifyDiscountAutomatically('10%');\n"
        "  await expect(page.locator('#total')).toHaveText('90,00 €');\n"
        "});\n\n"
        "// Exécution :\n"
        "// TypeError: page.verifyDiscountAutomatically is not a function",
        ["Deuxième scénario. {#code}On a demandé un script de test automatisé pour une user story de code promo. "
         "Le script a l'air propre : on ouvre le panier, on saisit le code, on clique sur appliquer, on vérifie le total. "
         "Mais à l'exécution, une erreur : la méthode verify discount automatically n'est pas une fonction. "
         "Elle n'existe tout simplement pas dans l'outil. Alors, quel défaut ?"],
    ),
    quiz(
        K + "3.1.2 · Scénario 2",
        "Le script généré appelle une méthode qui n'existe pas, et ne s'exécute pas. Quel défaut ?",
        ["Un biais", "Une hallucination", "Une erreur de raisonnement", "Un simple effet du non-déterminisme"], 1,
        "Une hallucination : le syllabus cite les scripts de test incorrects ou qui ne fonctionnent pas.",
        ["Le script appelle une méthode qui n'existe pas, et il ne s'exécute pas. Quel défaut ?"],
        ["{#rev}Une hallucination. Le modèle a inventé une méthode plausible. "
         "Le syllabus cite précisément les scripts de test incorrects ou non fonctionnels. Une vérification croisée avec la documentation de l'outil l'aurait révélée."],
    ),
    chat(
        K + "3.1.2 · Scénario 3", "Scénario 3 : une priorisation",
        "Règle : risque élevé d'abord ; à risque égal, le cas le plus court d'abord. TC-A moyen 1 h · TC-B élevé 3 h · TC-C élevé 1 h · TC-D faible 2 h",
        "Ordre d'exécution proposé :\n1. TC-B (risque élevé, 3 h)\n2. TC-C (risque élevé, 1 h)\n3. TC-A (risque moyen, 1 h)\n4. TC-D (risque faible, 2 h)",
        ["Troisième et dernier scénario, sur la priorisation des cas de test. {#type}On demande de prioriser quatre cas avec une règle précise : "
         "le risque élevé d'abord, et à risque égal, le cas le plus court d'abord. TC-A est à risque moyen, une heure. "
         "TC-B, risque élevé, trois heures. TC-C, risque élevé, une heure. Et TC-D, risque faible, deux heures. {#send}"
         "{#answer}Voici l'ordre proposé. Regardez attentivement les deux premiers cas, ceux à risque élevé."],
    ),
    quiz(
        K + "3.1.2 · Scénario 3",
        "Dans l'ordre proposé par le LLM, quel défaut repérez-vous ?",
        ["Aucun : l'ordre respecte la règle", "Une hallucination : un cas a été inventé",
         "Une erreur de raisonnement : la règle est mal appliquée", "Un biais : le non fonctionnel est sous-représenté"], 2,
        "TC-C, à risque élevé mais plus court, devait passer avant TC-B : la logique conditionnelle a échoué.",
        ["Dans cet ordre, quel défaut repérez-vous ?"],
        ["{#rev}Une erreur de raisonnement. TC-B et TC-C ont le même risque, donc le plus court, TC-C, devait passer en premier. "
         "Aucun cas n'est inventé : c'est la logique conditionnelle qui a échoué. La priorisation est justement une tâche citée par le syllabus."],
    ),
    cards(
        K + "3.1.3", "Cinq techniques pour limiter ces défauts",
        [("🧾", "Contexte complet", "Le prompt contient toutes les informations utiles (voir 2.1.1) pour guider le modèle."),
         ("🔗", "Découper le prompt", "Chaînage de prompts : petites étapes, chaque sortie vérifiée. Les erreurs de raisonnement sont vues tôt."),
         ("📐", "Formats clairs", "Éviter les formats ambigus : un format structuré et simple aide le modèle à viser l'essentiel."),
         ("🎯", "Modèle adapté", "Utiliser un LLM spécifiquement entraîné pour la tâche (voir 5.1.3)."),
         ("⚖️", "Comparer les modèles", "Soumettre le prompt à plusieurs LLM et comparer : on détecte les erreurs, on garde le plus fiable.")],
        ["Comment réduire ces défauts ? C'est l'objectif trois point un point trois, de niveau K deux. Le syllabus rappelle qu'ils sont plus fréquents "
         "quand le prompt est mal conçu, ou quand il manque des données de contexte pertinentes. Cinq techniques. "
         "{#c0}Un : fournir un contexte complet, avec toutes les informations utiles, comme on l'a vu au chapitre deux. "
         "{#c1}Deux : découper les prompts complexes en étapes, avec le chaînage de prompts, en vérifiant chaque sortie avant la suivante. Cela aide à détecter tôt les erreurs de raisonnement. "
         "{#c2}Trois : utiliser des formats de données clairs et faciles à interpréter, plutôt que des formats ambigus. "
         "{#c3}Quatre : choisir un modèle spécifiquement entraîné pour la tâche. "
         "{#c4}Cinq : quand c'est pertinent, comparer les résultats de plusieurs LLM, pour détecter les erreurs et garder le plus fiable. "
         "{#trap}Et le chapitre quatre présentera deux techniques complémentaires : le RAG et le fine-tuning."],
        cols=3,
        trap="Au chapitre 4 : deux techniques **complémentaires**, le **RAG** et le **fine-tuning**.",
    ),
    quiz(
        K + "3.1.3",
        "Un LLM se trompe souvent dans un calcul d'effort en plusieurs étapes. Que faire pour repérer l'erreur tôt ?",
        ["Augmenter la température", "Chaîner des prompts courts, vérifiés un à un",
         "Demander une réponse plus longue", "Retirer le contexte pour alléger le prompt"], 1,
        "Le chaînage vérifie chaque sortie avant l'étape suivante : les erreurs de raisonnement sont repérées tôt.",
        ["Mise en situation. Un LLM se trompe souvent dans un calcul d'effort en plusieurs étapes. Que faire pour repérer l'erreur au plus tôt ?"],
        ["{#rev}Découper la tâche en prompts chaînés, en vérifiant chaque sortie avant de passer à la suivante. "
         "Retirer le contexte, au contraire, augmenterait le risque."],
    ),
    versus(
        K + "3.1.4", "Même prompt, deux réponses",
        ("Lundi · premier essai", ["12 cas de test générés", "Valeurs limites couvertes", "Format tableau respecté"]),
        ("Mardi · même prompt", ["15 cas de test générés", "Un cas hors sujet apparaît", "Format partiellement respecté"]),
        [{"max": "Hier, même prompt, il m'a donné douze cas. Aujourd'hui, quinze ! Il est cassé ?"},
         "Il n'est pas cassé, Max : il est non déterministe. C'est l'objectif trois point un point quatre, de niveau K un. "
         "{#left}Lundi, une réponse. {#right}Mardi, avec exactement le même prompt, une autre réponse. "
         "Ces variations viennent de l'échantillonnage probabiliste utilisé pendant l'inférence, c'est-à-dire pendant la génération de la réponse. "
         "Obtenir des résultats cohérents et reproductibles est donc difficile, surtout pour les sorties longues, qui augmentent le risque de variabilité."],
    ),
    rows(
        K + "3.1.4", "Maîtriser le non-déterminisme",
        [("Baisser la température", "Pendant l'inférence, la distribution se resserre : moins d'aléa, des sorties plus cohérentes."),
         ("Le revers", "Moins de créativité et de diversité : des sorties répétitives, voire trop déterministes."),
         ("Fixer une graine aléatoire", "Si l'implémentation le permet : même suite pseudo-aléatoire, meilleure reproductibilité."),
         ("Automatiser la vérification", "Automatiser une partie de la vérification des sorties, pour une évaluation structurée et cohérente.")],
        ["Une reproductibilité complète ne peut pas être garantie, mais deux stratégies réduisent la variabilité. "
         "{#r0}D'abord, baisser la température pendant la génération. La distribution de probabilités se resserre : moins d'aléa, et des sorties plus cohérentes. "
         "{#r1}Mais attention au revers : cela limite aussi la créativité et la diversité. Les sorties deviennent répétitives, voire trop déterministes. "
         "{#r2}Ensuite, fixer une graine aléatoire, quand l'implémentation du LLM le permet. On utilise toujours la même suite pseudo-aléatoire, ce qui améliore la reproductibilité. "
         "{#r3}Enfin, pour réduire le risque d'hallucinations et d'erreurs de raisonnement, il faut aussi tenir compte de ce non-déterminisme, "
         "par exemple en automatisant une partie de la vérification des sorties : l'évaluation devient structurée et cohérente. "
         "{#trap}Retenez bien : on réduit la variabilité, on ne la supprime jamais."],
        trap="Température basse et graine fixe **réduisent** la variabilité, mais la reproductibilité complète n'est **jamais garantie**.",
    ),
    code(
        K + "3.1.4", "Démonstration : réglages et contrôle automatique",
        "# Appel à un LLM, réglé pour limiter la variabilité\n"
        "reponse = client.generate(\n"
        "    prompt=prompt_cas_de_test,\n"
        "    temperature=0.1,  # distribution resserrée : moins d'aléa\n"
        "    seed=42,          # même suite pseudo-aléatoire (si supporté)\n"
        ")\n\n"
        "# Vérification automatique, identique pour chaque sortie\n"
        "cas = lire_tableau(reponse)\n"
        "assert all(c.critere in CRITERES_US17 for c in cas)  # rien d'inventé\n"
        "assert len(cas) == len(CRITERES_US17)                # un cas par critère",
        ["Voici à quoi cela ressemble en pratique. {#code}Dans l'appel au modèle, on fixe une température basse, et une graine, si l'outil le permet. "
         "Puis, chaque sortie passe par la même vérification automatique : chaque cas de test doit correspondre à un critère réellement présent dans la user story, "
         "et il doit y avoir un cas par critère. Notre critère quatre inventé de tout à l'heure serait immédiatement signalé. "
         "{#note}On gagne en régularité, et on contrôle chaque sortie de la même façon. Mais sans garantie absolue."],
        note=("Ce que ça apporte", "Moins de variations, et un contrôle identique sur chaque sortie. Sans garantie absolue.", "ok"),
    ),
    quiz(
        K + "3.1.4",
        "Une équipe baisse fortement la température de son LLM. Quel effet faut-il attendre ?",
        ["Des sorties totalement reproductibles", "Des sorties plus cohérentes, mais moins créatives",
         "Des sorties plus variées et plus créatives", "La disparition des hallucinations"], 1,
        "Moins d'aléa, donc plus de cohérence ; en contrepartie, moins de créativité et de diversité.",
        ["Dernière question. Une équipe baisse fortement la température de son LLM. Quel effet faut-il attendre ?"],
        ["{#rev}Des sorties plus cohérentes, mais moins créatives. Attention au piège de la réponse A : la reproductibilité totale n'est jamais garantie."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes de l'épisode 1",
        [("Trois défauts", "Hallucination : inventé ou hors sujet. Raisonnement : logique fausse. Biais : issu des données."),
         ("Non-déterminisme", "Un défaut qui semble corrigé peut réapparaître dans une autre conversation."),
         ("Détecter", "Hallucinations : vérification croisée, experts, cohérence. Raisonnement : validation logique, test de sortie."),
         ("Biais", "Vérifier la fidélité à la stratégie de test, et repérer les types de test sous-représentés."),
         ("Cinq parades", "Contexte complet, chaînage, formats clairs, modèle adapté, comparaison entre modèles."),
         ("Variabilité", "Température basse et graine fixe la réduisent, sans garantie totale. Plus une vérification automatisée.")],
        ["Récapitulons. {#r0}Un : les trois défauts. L'hallucination invente, l'erreur de raisonnement applique une logique fausse, le biais vient des données d'entraînement. "
         "{#r1}Deux : à cause du non-déterminisme, un défaut corrigé peut réapparaître. "
         "{#r2}Trois : pour les hallucinations, vérification croisée, experts du domaine et contrôles de cohérence. Pour le raisonnement, validation logique et test des sorties. "
         "{#r3}Quatre : pour les biais, fidélité à la stratégie de test, et attention aux types de test sous-représentés. "
         "{#r4}Cinq : les cinq techniques pour limiter ces défauts. "
         "{#r5}Et six : la température et la graine réduisent la variabilité, sans jamais la supprimer, et la vérification automatisée rend l'évaluation cohérente."],
    ),
    title_scene(
        "À suivre · Épisode 2",
        "Confidentialité, sécurité, environnement et réglementation",
        "Vecteurs d'attaque, protection des données, énergie, normes et lois",
        ["Sections 3.2 à 3.4", "Pièges d'examen", "Puis le chapitre 4"],
        ["Bravo, c'est la fin de ce premier épisode. {#sub}Dans le prochain, on parle de confidentialité et de sécurité, avec les vecteurs d'attaque, "
         "puis de l'impact énergétique de l'IA, et des réglementations et normes. "
         "{#chips}Ensuite viendra le chapitre quatre, sur l'infrastructure de test propulsée par les LLM. "
         "D'ici là, faites les questions et les flashcards du chapitre trois dans l'application. À très vite !"],
    ),
]
