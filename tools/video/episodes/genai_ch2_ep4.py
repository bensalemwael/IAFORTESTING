# CT-GenAI v1.1 · Chapitre 2 · Épisode 4 : évaluer les résultats et affiner ses prompts (section 2.3).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import bignum, cards, chat, flow, quiz, rows, table, title_scene, versus

K = "CT-GenAI · Chapitre 2 · "

META = {
    "file": "genai-chapitre-2-episode-4",
    "title": "CT-GenAI · Chapitre 2 · Épisode 4 : évaluer les résultats et affiner ses prompts",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 2 · Épisode 4 sur 4",
        "Évaluer les résultats et affiner ses prompts",
        "Sept métriques, cinq techniques d'amélioration, et une démonstration complète",
        ["Sections 2.3.1 et 2.3.2", "2 objectifs K2", "Environ 12 minutes"],
        ["Bonjour, et bienvenue dans le dernier épisode du chapitre deux. "
         "{#sub}Aujourd'hui, on apprend à mesurer la qualité de ce que produit l'IA générative, puis à améliorer ses prompts, "
         "pas à pas, à partir de ces mesures. {#chips}Deux objectifs de niveau K deux, la section deux point trois, "
         "et une démonstration complète, de la première version d'un prompt jusqu'à sa version finale. C'est parti."],
    ),
    flow(
        K + "2.3", "Générer, mesurer, affiner",
        [("✨", "Générer", "Le LLM produit un résultat pour une tâche de test"),
         ("📏", "Mesurer", "Des métriques claires : qualité, pertinence, efficacité"),
         ("🔧", "Affiner", "Le prompt est amélioré à partir des mesures")],
        ["Dans les épisodes précédents, on a appris à écrire des prompts et à les appliquer aux tâches de test. "
         "Il reste une question essentielle : comment savoir si le résultat est bon ? "
         "{#s0}On génère un résultat. {#s1}On le mesure, avec un ensemble clair de métriques qui évaluent sa qualité, "
         "sa pertinence et son efficacité. {#s2}Puis on affine le prompt. {#loop}Et on recommence. "
         "Le syllabus précise que ces métriques, qu'elles soient générales ou spécifiques à une tâche, servent à optimiser le prompting."],
        loop=True,
    ),
    chat(
        K + "2.3", "Ça a l'air bien… mais est-ce mesuré ?",
        "Génère les cas de test du formulaire d'inscription à la newsletter.",
        "Voici 8 cas de test :\nTC1 · E-mail valide → inscription confirmée\nTC2 · E-mail sans @ → message d'erreur\nTC3 · Champ vide → message d'erreur\nTC4 · E-mail déjà inscrit → message dédié\n…",
        ["Prenons une situation très courante. {#type}On demande au modèle les cas de test d'un formulaire d'inscription à une newsletter. "
         "{#send}{#answer}La réponse est propre, bien présentée, avec huit cas de test. ",
         {"max": "Ça a l'air parfait. On l'adopte pour toute l'équipe ?"},
         "Ça a l'air parfait, Max. {#verdict}Mais une impression n'est pas une mesure. "
         "Ces cas couvrent-ils toutes les exigences ? Les scripts tirés de ces cas s'exécutent-ils ? Combien de temps a-t-on gagné ? "
         "{#note}Sans métriques, impossible de répondre, et impossible de savoir si une nouvelle version du prompt fait mieux ou moins bien."],
        verdict=("NON MESURÉ", "bad"),
        note=("La bonne question", "Pas « est-ce joli ? », mais « est-ce mesurablement bon pour ma tâche de test ? »", "warn"),
    ),
    table(
        K + "2.3.1", "Les sept métriques : les quatre premières",
        ["Métrique", "Ce qu'elle mesure", "Exemple en test"],
        [["Exactitude (accuracy)", "Justesse globale face à une référence : tests d'experts, exigences, normes", "Les cas générés couvrent-ils toutes les exigences spécifiées ?"],
         ["Précision", "Justesse par rapport à un objectif précis", "Les cas générés identifient-ils correctement les anomalies ?"],
         ["Rappel (recall)", "Capacité à trouver toutes les instances pertinentes d'un jeu de données", "Partitions valides et invalides d'une classe de données couvertes ?"],
         ["Pertinence et adéquation au contexte", "Résultat applicable et approprié au contexte donné", "Cohérence avec la base de test et les exigences du domaine"]],
        ["Le syllabus liste sept métriques. Voici les quatre premières. "
         "{#r0}L'exactitude, ou accuracy, mesure la justesse globale du résultat, comparé à des cas de test écrits par des experts, "
         "aux exigences, ou à d'autres normes. Exemple : dans quelle mesure les cas générés couvrent toutes les exigences spécifiées. "
         "{#r1}La précision évalue la justesse par rapport à un objectif précis. Exemple : les cas générés identifient-ils correctement les anomalies ? "
         "{#r2}Le rappel mesure la capacité du modèle à trouver toutes les instances pertinentes d'un jeu de données. "
         "Exemple : les cas générés couvrent-ils les partitions d'équivalence valides et invalides d'une classe de données ? "
         "{#r3}Enfin, la pertinence et l'adéquation au contexte : le résultat est-il applicable et approprié ? "
         "Par exemple, les cas sont-ils cohérents avec la base de test, et intègrent-ils les exigences propres au domaine ?"],
    ),
    versus(
        K + "2.3.1", "Exactitude, précision ou rappel ?",
        ("🎯 Précision", ["La question : ce qui est produit est-il juste pour l'objectif visé ?",
                          "Exemple : les anomalies signalées sont-elles de vraies anomalies ?",
                          "Elle juge la justesse de ce qui est produit"]),
        ("🕸️ Rappel", ["La question : a-t-on trouvé tout ce qu'il fallait trouver ?",
                       "Exemple : toutes les partitions valides et invalides sont-elles couvertes ?",
                       "Il juge l'exhaustivité"]),
        ["Ces trois métriques se confondent facilement à l'examen. Commençons par la paire la plus piégeuse. "
         "{#left}La précision répond à la question : ce que le modèle a produit est-il juste, pour l'objectif visé ? "
         "{#right}Le rappel répond à une autre question : le modèle a-t-il trouvé tout ce qu'il fallait trouver ? "
         "Un jeu de cas peut être très précis, mais oublier la moitié des partitions : précision haute, rappel faible. "
         "{#trap}Et l'exactitude, elle, est la justesse globale, mesurée face à une référence : des tests d'experts, les exigences, ou une norme."],
        trap="**Exactitude** : justesse globale face à une référence. **Précision** : justesse pour un objectif. **Rappel** : tout trouver.",
    ),
    table(
        K + "2.3.1", "Les sept métriques : les trois dernières",
        ["Métrique", "Ce qu'elle mesure", "Exemple en test"],
        [["Diversité", "Un large éventail d'entrées et de scénarios, sans répétition", "Variété des comportements utilisateurs, exploration des cas limites"],
         ["Taux de réussite d'exécution", "Part des artefacts générés exécutables tels quels dans l'environnement de test", "Combien de scripts tournent sans erreur de syntaxe ni de format de sortie ?"],
         ["Efficacité temporelle", "Le temps gagné par rapport à l'effort de test manuel", "Temps de génération par l'IA contre temps d'écriture manuelle de tests équivalents"]],
        ["Passons aux trois dernières. {#r0}La diversité : un large éventail d'entrées et de scénarios est couvert, en évitant les répétitions. "
         "Exemple : les cas générés couvrent différents comportements d'utilisateurs, et explorent les cas limites. "
         "{#r1}Le taux de réussite d'exécution : la proportion des artefacts de test générés qui s'exécutent avec succès, tels quels, "
         "dans l'environnement de test. Exemple : combien de scripts générés tournent sans erreur de syntaxe ni problème de format de sortie. "
         "{#r2}Et l'efficacité temporelle : le temps gagné par rapport à l'effort manuel. "
         "On compare le temps que met l'IA à générer les cas de test, et le temps qu'il faudrait à une personne pour écrire des tests équivalents. "
         "{#trap}Retenez bien le mot clé de l'exécution : tels quels."],
        trap="Taux de réussite d'exécution : le script tourne **tel quel**, sans erreur de syntaxe ni problème de format de sortie.",
    ),
    quiz(
        K + "2.3.1",
        "Sur 50 scripts générés, 43 tournent sans aucune retouche dans l'environnement de test. Quelle métrique ?",
        ["Exactitude", "Taux de réussite d'exécution", "Diversité", "Efficacité temporelle"], 1,
        "Le taux de réussite d'exécution : la part des artefacts générés qui s'exécutent tels quels.",
        ["Premier quiz. Sur cinquante scripts générés, quarante-trois tournent sans aucune retouche dans l'environnement de test. "
         "Quelle métrique mesure-t-on ?"],
        ["{#rev}Le taux de réussite d'exécution. On compte la part des artefacts générés qui s'exécutent avec succès, tels quels."],
    ),
    quiz(
        K + "2.3.1",
        "Un champ « âge » accepte 18 à 65 ans. Les cas générés ne testent que des âges valides. Quelle métrique est faible ?",
        ["Rappel", "Taux de réussite d'exécution", "Efficacité temporelle", "Pertinence et adéquation au contexte"], 0,
        "Le rappel : les partitions invalides, en dessous de 18 et au-dessus de 65, n'ont pas été trouvées.",
        ["Deuxième question. Un champ âge accepte de dix-huit à soixante-cinq ans. "
         "Les cas générés ne testent que des âges valides. Quelle métrique est faible ?"],
        ["{#rev}Le rappel. Le modèle n'a pas trouvé toutes les instances pertinentes : les partitions invalides, "
         "en dessous de dix-huit et au-dessus de soixante-cinq, manquent à l'appel."],
    ),
    cards(
        K + "2.3.1", "Comment mesurer, et sur combien d'essais ?",
        [("🧩", "Métriques spécifiques", "En plus des métriques générales : des métriques taillées pour une activité de test précise."),
         ("👀", "Revue manuelle", "Des testeurs examinent et évaluent eux-mêmes les résultats générés."),
         ("🤖", "Comparaison automatisée", "Le résultat du LLM est comparé automatiquement à une référence définie à l'avance."),
         ("📊", "Données statistiquement pertinentes", "L'IA générative est non déterministe : on mesure sur assez d'exécutions.")],
        ["Ces sept métriques sont générales. {#c0}Le syllabus ajoute qu'on peut définir des métriques spécifiques à une tâche, "
         "pour évaluer comment l'IA soutient une activité de test précise. "
         "Ensuite, comment les mesurer ? {#c1}Soit par une revue manuelle, {#c2}soit de façon automatisée, "
         "par exemple en comparant le résultat du LLM à une référence définie à l'avance. ",
         {"max": "J'ai lancé mon prompt une fois, résultat parfait. Ça suffit, non ?"},
         "{#c3}Justement non, Max. L'IA générative est non déterministe : le même prompt peut donner des résultats différents. "
         "Les métriques doivent donc reposer sur des données statistiquement pertinentes, pas sur un seul essai chanceux."],
        cols=4,
        accent=3,
    ),
    quiz(
        K + "2.3.1",
        "Pourquoi les métriques d'évaluation doivent-elles reposer sur des données statistiquement pertinentes ?",
        ["Parce que l'IA générative est non déterministe", "Parce que la revue manuelle n'est pas autorisée",
         "Parce que le modèle apprend à chaque exécution", "Parce que les métriques générales sont facultatives"], 0,
        "Le même prompt peut produire des résultats différents : une seule exécution ne suffit pas.",
        ["Troisième question. Pourquoi les métriques d'évaluation doivent-elles reposer sur des données statistiquement pertinentes ?"],
        ["{#rev}Parce que l'IA générative est non déterministe. Attention au piège : le modèle n'apprend pas à chaque exécution. "
         "Ses réponses varient, tout simplement."],
    ),
    cards(
        K + "2.3.2", "Cinq techniques pour affiner un prompt",
        [("🔁", "Modification itérative", "Partir d'un prompt de base et l'ajuster selon les résultats : plus de contexte, meilleure terminologie."),
         ("🆎", "Test A/B de prompts", "Créer plusieurs versions et comparer leurs résultats sur des métriques définies à l'avance."),
         ("🔬", "Analyse des résultats", "Chercher erreurs et incohérences, par exemple vis-à-vis de la base de test."),
         ("🗣️", "Retours des utilisateurs", "Recueillir l'avis des testeurs sur l'utilité et la clarté des résultats."),
         ("📏", "Longueur et spécificité", "Expérimenter des prompts plus ou moins longs et plus ou moins détaillés.")],
        ["Une fois qu'on sait mesurer, on peut améliorer. Le syllabus cite cinq techniques. "
         "{#c0}Un : la modification itérative. On part d'un prompt de base, et on le modifie en fonction des résultats réels, "
         "en ajoutant du contexte ou en ajustant la formulation, par exemple la terminologie, pour gagner en spécificité et en pertinence. "
         "{#c1}Deux : le test A B de prompts. On crée plusieurs versions, et on regarde laquelle donne les meilleurs résultats, "
         "selon des métriques définies à l'avance. Cela montre quelle formulation ou quelle structure est la plus exacte et la plus pertinente. "
         "{#c2}Trois : l'analyse des résultats. {#c3}Quatre : l'intégration des retours des utilisateurs. "
         "{#c4}Et cinq : l'ajustement de la longueur et de la spécificité du prompt."],
        cols=3,
    ),
    rows(
        K + "2.3.2", "Analyser, écouter, doser",
        [("Analyse des résultats", "Repérer les inexactitudes et incohérences, comprendre leurs types, et corriger le prompt pour la suite."),
         ("Retours des utilisateurs", "Les testeurs jugent l'utilité et la clarté, par exemple le niveau de détail des tests générés."),
         ("Longueur et spécificité", "Parfois, plus de contexte améliore la réponse. Parfois, un prompt plus court généralise mieux.")],
        ["Détaillons les trois dernières. {#r0}L'analyse des résultats : on examine ce que l'IA a produit, à la recherche d'inexactitudes "
         "ou d'incohérences, par exemple par rapport à la base de test. Comprendre le type d'erreur aide à corriger le prompt, "
         "pour ne pas reproduire les mêmes défauts aux itérations suivantes. "
         "{#r1}Les retours des utilisateurs : on demande aux testeurs si les résultats sont utiles et clairs, par exemple si le niveau de détail "
         "des tests générés leur convient. On analyse leurs remarques, et on affine le prompt pour coller aux vrais besoins du terrain. "
         "{#r2}Enfin, la longueur et la spécificité : on expérimente. {#trap}Parfois, ajouter du contexte améliore la réponse ; "
         "dans d'autres cas, un prompt plus court généralise mieux."],
        trap="Plus long n'est **pas toujours** mieux : selon le cas, un prompt plus court peut mieux généraliser.",
    ),
    chat(
        K + "Démonstration HO-2.3.1", "Démonstration : le prompt de départ",
        "Génère des cas de test pour l'US-7 : « Je réserve un billet de train pour 1 à 9 passagers. »",
        "TC1 · 1 passager → réservation acceptée\nTC2 · 4 passagers → réservation acceptée\nTC3 · 9 passagers → réservation acceptée\nTC4 · Paiement refusé → message d'erreur",
        ["Place à la démonstration. La tâche de test : générer des cas de test pour une user story de réservation, "
         "de un à neuf passagers. Une experte a écrit à l'avance une référence de dix conditions de test : partitions valides et invalides, "
         "et valeurs limites. {#type}Voici le prompt de départ, très simple. {#send}"
         "{#answer}Le modèle propose quatre cas. Trois sont utiles, mais ils ne testent que des valeurs valides. Et le quatrième, sur le paiement, sort du sujet. "
         "{#note}La métrique choisie pour cette tâche, c'est le rappel : la part des dix conditions de référence couvertes, "
         "comparée automatiquement, et calculée en moyenne sur dix exécutions. {#verdict}Résultat : trente pour cent."],
        verdict=("RAPPEL 30 %", "bad"),
        note=("Métrique adaptée à la tâche", "Rappel : part des 10 conditions de référence couvertes, en moyenne sur 10 exécutions.", "warn"),
    ),
    flow(
        K + "Démonstration HO-2.3.2", "Itérer, mesurer, recommencer",
        [("1️⃣", "V1 · prompt de base", "Rappel moyen : 30 %"),
         ("2️⃣", "V2 · + rôle et règles métier", "Rappel moyen : 60 %"),
         ("3️⃣", "V3 · + « partitions valides et invalides »", "Rappel moyen : 80 %")],
        ["{#s0}On part de la version un, à trente pour cent. L'analyse des résultats montre deux problèmes : aucun cas invalide, "
         "et un cas hors sujet. {#s1}Version deux : on ajoute un rôle de testeur et les règles métier de la réservation. "
         "Le rappel monte à soixante pour cent. Mais l'analyse montre que les valeurs invalides, zéro ou dix passagers, manquent encore. "
         "{#s2}Version trois : on ajuste la terminologie, en demandant explicitement les partitions d'équivalence valides et invalides, "
         "et les valeurs limites. Quatre-vingts pour cent. {#check}À chaque version, dix exécutions, et la même comparaison à la référence. ",
         {"max": "Et si j'écrivais le prompt d'une tout autre façon ?"},
         "{#loop}Bonne idée, Max : c'est exactement le principe du test A B."],
        check="✔ Chaque version : 10 exécutions, comparaison automatique à la référence",
        loop=True,
    ),
    versus(
        K + "Démonstration HO-2.3.2", "Le test A/B : deux prompts, une métrique",
        ("🅰️ Prompt A · long et détaillé", ["La V3, plus toutes les règles en paragraphes", "Trois exemples de cas complets",
                                            "10 exécutions", "Rappel moyen : 82 %"]),
        ("🅱️ Prompt B · court et structuré", ["Les règles en liste, consignes ciblées", "Format de sortie : un tableau",
                                             "10 exécutions", "Rappel moyen : 92 %"]),
        ["On prépare deux versions concurrentes. {#left}Le prompt A est long et détaillé : la version trois, plus toutes les règles "
         "rédigées en paragraphes, et trois exemples complets. Sur dix exécutions, son rappel moyen est de quatre-vingt-deux pour cent. "
         "{#right}Le prompt B est plus court et structuré : les règles en liste, des consignes ciblées, et un tableau comme format de sortie. "
         "Sur dix exécutions également, il atteint quatre-vingt-douze pour cent. "
         "Dans ce cas précis, la version la plus courte gagne. C'est l'esprit de la technique sur la longueur et la spécificité : "
         "on ne devine pas, on expérimente et on mesure, avec la même métrique pour les deux versions."],
    ),
    bignum(
        K + "Démonstration HO-2.3.2", "Le prompt retenu",
        92, "% de rappel moyen",
        "Prompt B : 92 % des conditions de référence couvertes, en moyenne sur 10 exécutions",
        ["{#n}Quatre-vingt-douze pour cent. {#cap}C'est le rappel moyen du prompt B, mesuré sur dix exécutions : "
         "il couvre en moyenne neuf conditions de référence sur dix, contre trois au départ. "
         "Mais la démonstration ne s'arrête pas au chiffre. Comme le prévoit l'exercice du syllabus, une vérification humaine complète la mesure : "
         "deux testeurs relisent les cas produits, et confirment que le niveau de détail leur convient. "
         "C'est l'intégration des retours des utilisateurs. Le prompt B peut alors être partagé avec toute l'équipe."],
    ),
    cards(
        K + "2.3.2", "Partager pour progresser ensemble",
        [("🗓️", "Sessions d'optimisation", "L'équipe organise des sessions d'évaluation et d'optimisation des prompts."),
         ("📚", "Bibliothèques de prompts", "Les prompts éprouvés sont partagés et réutilisés dans l'équipe ou l'organisation."),
         ("📐", "Standardiser", "Des techniques de prompting homogènes, et une qualité constante."),
         ("🌱", "Apprendre ensemble", "Une culture d'amélioration itérative : on capitalise et on évite les erreurs répétées.")],
        ["Dernière idée de la section. {#c0}Avec ces techniques, les équipes de test peuvent organiser de vraies sessions d'évaluation "
         "et d'optimisation des prompts, pour une amélioration continue. "
         "{#c1}Le syllabus recommande de partager les pratiques dans l'équipe ou l'organisation, par exemple avec des bibliothèques de prompts. "
         "{#c2}Ce partage aide à standardiser les techniques de prompting et à maintenir une qualité constante. "
         "{#c3}Il favorise aussi une culture d'apprentissage et d'amélioration itérative : chacun s'appuie sur l'expérience collective, "
         "on évite de répéter les mêmes erreurs, et l'usage des outils d'IA s'améliore avec le temps."],
    ),
    quiz(
        K + "2.3.2",
        "Deux formulations d'un même prompt sont lancées 20 fois chacune, puis comparées sur un indicateur fixé d'avance. Quelle technique ?",
        ["Test A/B de prompts", "Analyse des résultats", "Intégration des retours utilisateurs", "Méta-prompting"], 0,
        "Le test A/B : plusieurs versions du prompt, départagées par des métriques définies à l'avance.",
        ["Quatrième question. Deux formulations d'un même prompt sont lancées vingt fois chacune, "
         "puis comparées sur un indicateur fixé d'avance. Quelle technique ?"],
        ["{#rev}Le test A B de prompts. Plusieurs versions, et des métriques définies à l'avance pour les départager. "
         "Le méta-prompting, lui, est une technique du deux point un, où le modèle aide à écrire le prompt."],
    ),
    quiz(
        K + "2.3.2",
        "Les testeurs jugent les cas générés trop détaillés pour leurs revues. L'équipe adapte le prompt. Quelle technique décrit le mieux cela ?",
        ["Test A/B de prompts", "Intégration des retours utilisateurs", "Chaînage de prompts", "Comparaison à une référence"], 1,
        "L'intégration des retours utilisateurs : l'avis des testeurs sur l'utilité et la clarté guide le prompt.",
        ["Dernière question. Les testeurs jugent les cas générés trop détaillés pour leurs revues, et l'équipe adapte le prompt. "
         "Quelle technique décrit le mieux cette démarche ?"],
        ["{#rev}L'intégration des retours des utilisateurs. Le déclencheur, c'est l'avis des testeurs sur l'utilité et la clarté, "
         "ici le niveau de détail. C'est d'ailleurs l'exemple que donne le syllabus."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes de l'épisode 4",
        [("7 métriques", "Exactitude, précision, rappel, pertinence, diversité, réussite d'exécution, efficacité temporelle."),
         ("Précision ≠ rappel", "Précision : justesse pour un objectif. Rappel : trouver toutes les instances pertinentes."),
         ("Comment mesurer", "Revue manuelle ou comparaison automatisée à une référence, et métriques spécifiques à la tâche."),
         ("Statistiques", "Non-déterminisme oblige : des données statistiquement pertinentes, jamais un seul essai."),
         ("5 techniques", "Modification itérative, test A/B, analyse des résultats, retours utilisateurs, longueur et spécificité."),
         ("Partager", "Sessions d'optimisation, pratiques communes et bibliothèques de prompts.")],
        ["Récapitulons l'épisode. {#r0}Un : les sept métriques, de l'exactitude à l'efficacité temporelle. "
         "{#r1}Deux : ne confondez pas précision et rappel. "
         "{#r2}Trois : on mesure par revue manuelle ou par comparaison automatisée à une référence, avec si besoin des métriques propres à la tâche. "
         "{#r3}Quatre : l'IA est non déterministe, donc des données statistiquement pertinentes. "
         "{#r4}Cinq : les cinq techniques pour affiner un prompt. "
         "{#r5}Et six : on partage les bonnes pratiques et les bibliothèques de prompts."],
    ),
    cards(
        K + "Récapitulatif du chapitre", "Tout le chapitre 2 en six cartes",
        [("✍️", "Structurer", "Rôle, contexte, instruction, données d'entrée, contraintes, format. System prompt et user prompt."),
         ("🧰", "Trois techniques", "Chaînage de prompts, few-shot, méta-prompting."),
         ("🔍", "Analyser et concevoir", "2.2.1 et 2.2.2 · Conditions de test, critères d'acceptation, cas, données et scripts."),
         ("🔁", "Automatiser et piloter", "2.2.3 et 2.2.4 · Tests de régression automatisés, suivi et contrôle des tests."),
         ("🧭", "Choisir la technique", "2.2.5 · Chaînage : tâches complexes. Few-shot : sorties répétitives. Méta : tâches nouvelles."),
         ("📏", "Évaluer et affiner", "2.3 · Sept métriques, cinq techniques d'amélioration, partage des prompts.")],
        ["Et maintenant, prenons de la hauteur sur tout le chapitre deux. "
         "{#c0}On a appris à structurer un prompt en six composants, et à distinguer system prompt et user prompt. "
         "{#c1}On a vu trois techniques : le chaînage, le few-shot et le méta-prompting. "
         "{#c2}On les a appliquées à l'analyse de test, puis à la conception et à l'implémentation des tests. "
         "{#c3}Puis à la régression automatisée, et au suivi et au contrôle des tests. "
         "{#c4}On a appris à choisir : le chaînage pour les tâches complexes vérifiées pas à pas, le few-shot pour les sorties répétitives "
         "au format imposé, le méta-prompting pour les tâches nouvelles et flexibles. "
         "{#c5}Et aujourd'hui, à évaluer les résultats et à affiner ses prompts."],
        cols=3,
    ),
    title_scene(
        "À suivre · Chapitre 3",
        "Gérer les risques de l'IA générative",
        "Hallucinations, erreurs de raisonnement, biais, confidentialité, sécurité, énergie et réglementation",
        ["160 minutes au syllabus", "Objectifs K1 à K3", "Démonstrations"],
        ["Bravo, vous avez terminé le chapitre deux, le plus gros morceau du programme ! "
         "{#sub}Dans le chapitre trois, on regarde l'autre face de la médaille : les risques de l'IA générative. "
         "Les hallucinations, les erreurs de raisonnement et les biais, puis la confidentialité des données et la sécurité, "
         "l'impact énergétique, et les réglementations. {#chips}D'ici là, faites les questions et les flashcards du chapitre deux "
         "dans l'application. À très vite !"],
    ),
]
