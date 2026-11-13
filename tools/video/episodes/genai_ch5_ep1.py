# CT-GenAI v1.1 · Chapitre 5 · Épisode unique : déployer et intégrer l'IA générative dans une organisation de test (5.1, 5.2).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import cards, chat, code, flow, prompt_build, quiz, rows, title_scene

K = "CT-GenAI · Chapitre 5 · "

META = {
    "file": "genai-chapitre-5-episode-1",
    "title": "CT-GenAI · Chapitre 5 · Épisode unique : déployer l'IA générative dans le test",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 5 · Épisode unique",
        "Déployer l'IA générative dans une organisation de test",
        "Shadow AI, stratégie, choix des modèles, adoption et conduite du changement",
        ["Sections 5.1 et 5.2", "7 objectifs K1 et K2", "Environ 12 minutes"],
        ["Bonjour, et bienvenue dans le cinquième et dernier chapitre du syllabus. "
         "{#sub}On prend de la hauteur : comment une organisation de test adopte-t-elle l'IA générative ? "
         "Shadow AI, stratégie, choix des modèles, phases d'adoption, compétences et évolution des rôles. "
         "{#chips}Quatre-vingts minutes de formation officielle, et sept objectifs : quatre de niveau K un, où il faut se souvenir, "
         "et trois de niveau K deux, où il faut expliquer. Plus un exercice d'estimation des coûts. Allons-y."],
    ),
    cards(
        K + "5.1", "D'abord une stratégie, puis une feuille de route",
        [("🎯", "Objectifs de test", "Les objectifs de test à atteindre avec l'IA générative."),
         ("🧠", "Choix des LLM", "Sélectionner les modèles appropriés."),
         ("📥", "Données d'entrée", "Les problèmes posés par les données utilisées dans les prompts."),
         ("⚖️", "Conformité", "Le respect des normes et des réglementations sur l'IA.")],
        ["Section cinq point un. Une stratégie de test avec l'IA générative doit considérer avec soin plusieurs aspects clés : "
         "{#c0}les objectifs de test à atteindre, {#c1}le choix des LLM appropriés, "
         "{#c2}les problèmes liés aux données d'entrée utilisées dans les prompts, "
         "{#c3}et la conformité aux normes et aux réglementations sur l'IA. "
         "À partir de cette stratégie, l'organisation établit une feuille de route, et suit ses progrès dans l'intégration de l'IA générative. "
         "Mais d'abord, voyons ce qui arrive quand il n'y a pas de stratégie."],
    ),
    chat(
        K + "5.1.1", "Le shadow AI",
        "Voici l'export complet de notre base clients de production. Génère-moi 50 jeux de données de test réalistes.",
        "Bien sûr ! Voici 50 jeux de données inspirés\nde vos clients : noms, adresses, IBAN…",
        [{"max": "Moi, j'utilise mon compte perso de chatbot, ça va plus vite !"},
         "Justement, Max, regardons ce que ça donne. {#type}Un testeur colle l'export de la base clients de production "
         "dans son assistant personnel, pour générer des données de test. {#send}Envoyé. {#answer}L'outil s'exécute sans broncher. "
         "{#verdict}C'est du shadow AI. {#note}Le syllabus le définit comme l'usage d'outils ou de systèmes d'IA générative "
         "au sein d'une organisation, sans approbation formelle ni supervision. Ici, personne n'a validé l'outil, ni l'envoi de ces données."],
        verdict=("SHADOW AI", "bad"),
        note=("Définition", "L'usage d'outils d'IA générative dans l'organisation, sans approbation formelle ni supervision.", "warn"),
    ),
    cards(
        K + "5.1.1", "Les trois risques du shadow AI",
        [("🔓", "Sécurité et confidentialité", "Les outils d'IA personnels peuvent manquer de sécurité robuste : risque de fuite de données."),
         ("⚖️", "Conformité réglementaire", "Des outils non approuvés peuvent enfreindre normes et réglementations, avec des suites juridiques."),
         ("©️", "Propriété intellectuelle floue", "Des licences peu claires exposent à des litiges, surtout sur des données protégées traitées sans droit.")],
        ["Le syllabus cite trois risques. {#c0}Un : des faiblesses de sécurité de l'information et de confidentialité des données. "
         "Les outils d'IA personnels peuvent manquer de sécurité robuste, d'où des fuites de données possibles. "
         "{#c1}Deux : des problèmes de conformité réglementaire. Utiliser des outils non approuvés peut conduire à enfreindre "
         "les normes et réglementations du secteur, avec de possibles conséquences juridiques. "
         "{#c2}Trois : une propriété intellectuelle floue. Des outils aux licences peu claires exposent à des litiges, "
         "surtout si des données protégées par le droit d'auteur sont traitées sans autorisation. "
         "{#trap}Le remède : une stratégie, et des étapes claires pour intégrer et déployer l'IA générative."],
        trap="Contre le shadow AI : une **stratégie** et des étapes claires d'intégration et de déploiement de l'IA générative.",
    ),
    quiz(
        K + "Entraînement 5.1.1",
        "Un testeur traite des documents protégés par le droit d'auteur avec un outil d'IA à la licence floue. Quel risque principal ?",
        ["Faiblesse de sécurité des données", "Non-conformité réglementaire",
         "Propriété intellectuelle floue", "Surapprentissage du modèle"], 2,
        "Licence floue et données protégées traitées sans autorisation : risque de litige de propriété intellectuelle.",
        ["À vous. Un testeur traite des documents protégés par le droit d'auteur avec un outil d'IA dont la licence est floue. "
         "Quel risque du shadow AI est le plus directement en jeu ?"],
        ["{#rev}La propriété intellectuelle floue. Le surapprentissage, lui, est un défi du fine-tuning, pas un risque du shadow AI."],
    ),
    rows(
        K + "5.1.2", "Les clés d'une stratégie d'IA générative",
        [("Objectifs mesurables", "Gagner en productivité du test, raccourcir les cycles de test, améliorer la qualité des tests."),
         ("Choix des LLM", "Alignés sur ces objectifs, compatibles avec l'infrastructure de test, capables de monter en charge."),
         ("Qualité des données", "Des données d'entrée exactes et pertinentes, protégées par des procédures de sécurité robustes."),
         ("Formation", "Des programmes complets : les compétences techniques et éthiques des équipes de test."),
         ("Métriques", "Mesurer l'efficacité des résultats de l'IA générative (voir 2.3.1)."),
         ("Lignes directrices", "Données sensibles, obligations de transparence, quality gates avec revue du testware généré.")],
        ["Objectif cinq point un point deux. {#r0}Tout commence par des objectifs de test mesurables : gagner en productivité, "
         "raccourcir les cycles de test, améliorer la qualité des tests. "
         "{#r1}Le choix des LLM doit être aligné sur ces objectifs, compatible avec l'infrastructure de test existante, et capable de monter en charge. "
         "{#r2}La qualité des données est critique : des données d'entrée exactes, pertinentes, et protégées. "
         "C'est la clé pour obtenir des résultats dignes de confiance. "
         "{#r3}Il faut des programmes de formation, pour les compétences techniques et éthiques. "
         "{#r4}Des métriques, pour mesurer l'efficacité des résultats. "
         "{#r5}Et des lignes directrices de processus, pour respecter la réglementation et l'éthique."],
    ),
    code(
        K + "5.1.2", "Démonstration : des lignes directrices concrètes",
        "CHARTE IA GÉNÉRATIVE · ÉQUIPE DE TEST\n\n"
        "1. Données sensibles\n"
        "   Aucune donnée personnelle ou confidentielle non masquée\n"
        "   dans un prompt.\n\n"
        "2. Transparence\n"
        "   Tout testware généré avec l'IA est marqué [IA] dans l'outil\n"
        "   de gestion des tests.\n\n"
        "3. Quality gate\n"
        "   Revue humaine obligatoire du testware généré avant\n"
        "   son intégration au référentiel de test.",
        ["Voici à quoi peuvent ressembler ces lignes directrices. {#code}Une règle sur l'usage des données sensibles : "
         "aucune donnée personnelle ou confidentielle non masquée dans un prompt. Une obligation de transparence : "
         "on indique ce qui a été généré avec l'IA. Et une quality gate : le testware généré est relu avant d'être intégré. "
         "{#note}Ce sont exactement les trois exemples du syllabus : des règles sur les données sensibles, des obligations de transparence, "
         "et des quality gates avec revue du testware généré."],
        note=("Trois types de règles", "Usage des données sensibles, obligations de transparence, quality gates avec revue.", "ok"),
    ),
    quiz(
        K + "Entraînement 5.1.2",
        "« Utilisons l'IA générative dans le test ! » Mais personne ne sait quel résultat est attendu. Que manque-t-il d'abord ?",
        ["Des objectifs de test mesurables", "Des quality gates avec revue",
         "Un programme de formation", "Des règles sur les données sensibles"], 0,
        "La stratégie commence par des objectifs mesurables : productivité, cycles plus courts, qualité.",
        ["Une situation. Une direction lance : utilisons l'IA générative dans le test ! Mais personne ne sait quel résultat est attendu. "
         "Que manque-t-il d'abord ?"],
        ["{#rev}Des objectifs de test mesurables. Le syllabus est clair : la stratégie commence par là. "
         "Par exemple gagner en productivité, raccourcir les cycles, ou améliorer la qualité."],
    ),
    cards(
        K + "5.1.3", "Des modèles très différents",
        [("🖼️", "Capacités fonctionnelles", "Par exemple l'entrée multimodale ou les capacités de raisonnement."),
         ("📏", "Caractéristiques techniques", "Par exemple la taille de la fenêtre de contexte."),
         ("📜", "Types de licence", "Par exemple commerciale ou open source.")],
        ["Objectif cinq point un point trois : choisir ses modèles. Il existe une grande variété de LLM et de SLM. Ils diffèrent par "
         "{#c0}leurs capacités fonctionnelles, comme l'entrée multimodale ou le raisonnement, "
         "{#c1}leurs caractéristiques techniques, comme la taille de la fenêtre de contexte, "
         "{#c2}et leur type de licence, commerciale ou open source. "
         "{#trap}Et attention : de nombreux benchmarks évaluent les modèles sur le langage, le code ou l'analyse d'images, "
         "mais très peu portent spécifiquement sur les tâches de test. D'où l'importance de critères de sélection clairs."],
        trap="Beaucoup de benchmarks existent, mais **très peu** sont centrés sur les tâches de test logiciel.",
    ),
    cards(
        K + "5.1.3", "Quatre critères pour choisir un modèle",
        [("📊", "Performance du modèle", "Sur les tâches de test visées, face aux benchmarks de l'organisation, avec des métriques (2.3.1)."),
         ("🔧", "Potentiel de fine-tuning", "Est-il possible et utile d'affiner le modèle avec des données du domaine ?"),
         ("💶", "Coût récurrent", "Frais de licence et coûts d'exploitation : rester dans le budget prévu pour ces tâches."),
         ("👥", "Communauté et support", "Une communauté active et une documentation détaillée, pour la mise en œuvre et le dépannage.")],
        ["Le syllabus retient quatre critères. {#c0}La performance du modèle : on l'évalue sur les tâches de test visées, "
         "par rapport aux benchmarks de l'organisation, avec des métriques comme celles du chapitre deux. "
         "{#c1}Le potentiel de fine-tuning : est-il possible, et utile, d'affiner le modèle avec des données du domaine, "
         "pour gagner en exactitude et en pertinence ? {#c2}Le coût récurrent : frais de licence et dépenses d'exploitation, "
         "qui doivent tenir dans le budget. {#c3}Et la communauté et le support : une communauté active et une documentation détaillée "
         "aident à la mise en œuvre et au dépannage. Au final, on peut retenir un ou plusieurs modèles."],
        cols=2,
    ),
    quiz(
        K + "Entraînement 5.1.3",
        "Une équipe soumet chaque modèle candidat à ses propres user stories, avec des métriques de qualité. Quel critère ?",
        ["Le potentiel de fine-tuning", "La performance du modèle", "Le coût récurrent", "La communauté et le support"], 1,
        "La performance : sur les tâches visées, face aux benchmarks de l'organisation, avec des métriques.",
        ["Une équipe soumet chaque modèle candidat à ses propres user stories, et mesure les résultats avec des métriques de qualité. "
         "Quel critère de sélection évalue-t-elle ?"],
        ["{#rev}La performance du modèle, mesurée sur ses tâches de test, face à ses propres benchmarks."],
    ),
    code(
        K + "HO-5.1.3", "Exercice : estimer le coût récurrent",
        "Tâche      : générer les cas de test de chaque user story\n"
        "Fréquence  : 400 user stories par mois\n"
        "Prompts    : 1 prompt par user story\n"
        "Entrée     : 3 000 tokens (user story + contexte + instructions)\n"
        "Sortie     : 1 500 tokens\n\n"
        "Volume mensuel : 1,2 M tokens en entrée · 0,6 M tokens en sortie\n\n"
        "Offre A · commerciale (prix fictifs, par million de tokens)\n"
        "  1,2 × 3 €  +  0,6 × 15 €  =  3,60 €  +  9,00 €  =  12,60 € / mois\n"
        "Offre B · modèle open source hébergé en interne\n"
        "  pas de prix au token, mais serveurs, énergie et maintenance",
        ["Place à l'exercice pratique de niveau H un : estimer les coûts récurrents. "
         "{#code}On pose des hypothèses : quatre cents user stories par mois, un prompt par user story, "
         "trois mille tokens en entrée et mille cinq cents en sortie. Avec une offre commerciale aux prix fictifs, "
         "on obtient douze euros soixante par mois. Le modèle open source, lui, n'a pas de prix au token, mais il faut l'héberger.",
         {"max": "Douze euros soixante par mois ? C'est donné !"},
         "{#note}Attention aux hypothèses, Max. Passez à une chaîne de trois prompts par user story, ou lancez la tâche chaque jour, "
         "et la facture change. L'exercice compare plusieurs fournisseurs, dont au moins une solution commerciale "
         "et un modèle sous licence open source."],
        note=("Les hypothèses comptent", "Tokens en entrée et en sortie, prompts utilisés, fréquence de la tâche.", "warn"),
    ),
    flow(
        K + "5.1.4", "Trois phases d'adoption",
        [("🔭", "1 · Découverte", "Former les équipes, donner accès aux LLM et SLM, expérimenter de premiers cas d'usage"),
         ("🧭", "2 · Initiation et définition des usages", "Prioriser les cas d'usage, évaluer l'infrastructure, développer l'expertise"),
         ("🚀", "3 · Utilisation et itération", "Intégration complète, suivi continu, mesure et pilotage de la transformation")],
        ["Objectif cinq point un point quatre. {#s0}Un : la découverte. On sensibilise et on construit les capacités : "
         "former les équipes aux concepts, donner accès à des LLM et des SLM, et expérimenter de premiers cas d'usage pour prendre confiance. "
         "{#s1}Deux : l'initiation et la définition des usages. On identifie et on priorise des cas d'usage concrets, on évalue l'infrastructure "
         "de test propulsée par LLM, et on développe l'expertise, en restant aligné sur les besoins de l'organisation. "
         "{#s2}Trois : l'utilisation et l'itération. L'IA générative est pleinement intégrée, avec un suivi continu, "
         "et une transformation mesurée et pilotée pour durer. {#check}Ces phases peuvent avancer en parallèle selon les cas d'usage. "
         "{#trap}Et il faut traiter tôt les inquiétudes, comme la peur de perdre son emploi."],
        check="✔ Les phases peuvent avancer en parallèle selon les cas d'usage",
        trap="Traiter tôt les inquiétudes, comme la **peur de perdre son emploi** : elles pèsent sur l'adoption et le moral.",
    ),
    quiz(
        K + "Entraînement 5.1.4",
        "Une organisation évalue des outils de test propulsés par LLM pour ses cas d'usage prioritaires. Quelle phase ?",
        ["Découverte", "Initiation et définition des usages", "Utilisation et itération", "Industrialisation"], 1,
        "Évaluer l'infrastructure de test propulsée par LLM pour des cas d'usage priorisés : c'est la phase 2.",
        ["Une organisation évalue des outils de test propulsés par LLM pour ses cas d'usage prioritaires. Dans quelle phase est-elle ?"],
        ["{#rev}L'initiation et la définition des usages, la deuxième phase. Et attention : industrialisation ne fait pas partie des trois phases."],
    ),
    cards(
        K + "5.2.1", "Les compétences du testeur",
        [("✍️", "Prompts et contexte", "Maîtriser le prompt engineering et l'affinage des prompts ; comprendre les fenêtres de contexte."),
         ("🔍", "Évaluer l'IA", "Évaluer les capacités des LLM et le testware généré ; développer des méthodes de revue."),
         ("🧩", "Domaine + test + IA", "Combiner ces expertises pour évaluer l'IA : cas de test, rapports de défaut, données de test."),
         ("⚠️", "Risques", "Connaître les risques inhérents à l'IA générative et les stratégies d'atténuation courantes."),
         ("🔐", "Sécurité des données", "Mesurer ce qu'implique le partage de testware, assainir les données, protéger la vie privée."),
         ("🌱", "Environnement", "Des modèles de bonne taille, moins de calcul : équilibrer bénéfices, coût et énergie.")],
        ["Section cinq point deux : conduire le changement. "
         "Objectif cinq point deux point un : les compétences. {#c0}Maîtriser le prompt engineering et l'affinage des prompts, "
         "et comprendre les fenêtres de contexte. {#c1}Évaluer les capacités des LLM et le testware généré, avec des méthodes de revue. "
         "{#c2}Combiner l'expertise du domaine et du test avec des compétences IA, par exemple pour la génération de cas de test, "
         "l'analyse des rapports de défaut, ou la génération de données de test. {#c3}Connaître les risques de l'IA générative, "
         "et leurs atténuations. {#c4}Comprendre les enjeux de sécurité du partage de testware avec un LLM. "
         "{#c5}Et penser à l'environnement : des modèles de bonne taille, en équilibrant bénéfices, coût et consommation d'énergie."],
        cols=3,
    ),
    chat(
        K + "5.2.1", "Démonstration : assainir avant de partager",
        "Analyse ce rapport de défaut : le client [CLIENT_1], compte [IBAN_MASQUÉ], obtient l'erreur E-502 en validant un virement de 2 000 €.",
        "Analyse du défaut :\n• Erreur E-502 à la validation du virement\n• Montant élevé : vérifier le contrôle du plafond\n"
        "• Les données client ne sont pas utiles à l'analyse\nÉtape suivante : rejouer avec 1 999,99 € et 2 000,01 €",
        [{"max": "Masquer les données avant chaque prompt, c'est vraiment utile ?"},
         "Oui, Max, c'est une compétence attendue. {#type}Ici, le testeur demande l'analyse d'un rapport de défaut, "
         "mais le nom du client et son IBAN ont été remplacés par des étiquettes. {#send}Envoyé. "
         "{#answer}L'analyse reste tout aussi utile : ces données n'étaient pas nécessaires. {#verdict}Les données sont protégées. "
         "{#note}C'est l'assainissement des données : retirer ou masquer les informations sensibles, personnelles ou confidentielles. "
         "Il va de pair avec des pratiques de prompt engineering qui préservent la confidentialité."],
        verdict=("DONNÉES MASQUÉES", "good"),
        note=("Assainissement des données", "Retirer ou masquer les informations sensibles, personnelles ou confidentielles.", "ok"),
    ),
    quiz(
        K + "Entraînement 5.2.1",
        "Pour classer des rapports de défaut, un testeur prend un petit modèle suffisant plutôt que le plus gros LLM. Pourquoi ?",
        ["Par souci d'assainissement des données", "Par considération environnementale",
         "Pour faire du méta-prompting", "Pour réduire l'opacité du modèle"], 1,
        "Un modèle de bonne taille réduit le calcul : bénéfices, coût et énergie sont équilibrés.",
        ["Pour classer des rapports de défaut, un testeur choisit un petit modèle suffisant, plutôt que le plus gros LLM disponible. "
         "Pourquoi ce choix ?"],
        ["{#rev}Les considérations environnementales : choisir un modèle de bonne taille, pour limiter le calcul, le coût et l'énergie."],
    ),
    cards(
        K + "5.2.2", "Développer les compétences de l'équipe",
        [("🛠️", "Une approche pratique", "S'exercer sur plusieurs LLM et SLM, suivre des parcours structurés, partager le savoir-faire."),
         ("👥", "Apprendre ensemble", "Exercices guidés, apprentissage entre pairs, intégration progressive de l'IA au quotidien."),
         ("📈", "Une progression", "Des prompts de base vers des techniques ciblées, comme les prompts spécifiques au test."),
         ("🏛️", "Communautés de pratique", "Réunions régulières, bibliothèques de prompt patterns, leçons apprises documentées.")],
        ["Objectif cinq point deux point deux : comment développer ces compétences. "
         "{#c0}Le syllabus insiste sur une approche pratique : s'exercer avec différents LLM et SLM, suivre des parcours structurés, "
         "et partager progressivement le savoir-faire. {#c1}La formation passe par des exercices guidés, l'apprentissage entre pairs, "
         "et l'intégration progressive de l'IA dans les tâches quotidiennes. "
         "{#c2}On progresse des prompts de base vers des techniques ciblées, comme les prompts spécifiques au test. "
         "{#c3}Enfin, des communautés de pratique internes se réunissent régulièrement pour partager les réussites, les difficultés "
         "et les bonnes pratiques. Elles diffusent des bibliothèques de prompt patterns, et documentent les leçons apprises d'un projet à l'autre."],
        cols=2,
    ),
    prompt_build(
        K + "5.2.2", "Un prompt pattern, prêt à réutiliser",
        [("Rôle", "Tu es un testeur expert du domaine {domaine}."),
         ("Contexte", "Application {application}, fonctionnalité {fonction}."),
         ("Instruction", "Rédige les cas de test de la user story fournie."),
         ("Données d'entrée", "{user story} + {critères d'acceptation}"),
         ("Contraintes", "Technique {technique}, {nombre} cas au maximum."),
         ("Format de sortie", "Tableau : ID | Préconditions | Étapes | Attendu")],
        ["Qu'est-ce qu'un prompt pattern ? C'est un modèle réutilisable pour rédiger des prompts efficaces, "
         "et guider l'IA générative vers des sorties cohérentes et fiables. Voici un exemple, bâti sur la structure du chapitre deux : "
         "{#l0}le rôle, {#l1}le contexte, {#l2}l'instruction, {#l3}les données d'entrée, {#l4}les contraintes, {#l5}et le format de sortie. "
         "Les éléments entre accolades se complètent à chaque usage. "
         "{#badge}Une fois validé, ce patron rejoint la bibliothèque de la communauté de pratique, et toute l'équipe en profite."],
        badge=("{ }", "à compléter"),
    ),
    quiz(
        K + "Entraînement 5.2.2",
        "Qu'est-ce qu'un prompt pattern, selon le syllabus ?",
        ["Un modèle réutilisable pour rédiger des prompts efficaces", "Un défaut récurrent dans les réponses d'un LLM",
         "Un jeu de données pour le fine-tuning", "Une règle de détection du shadow AI"], 0,
        "Un modèle réutilisable qui guide l'IA générative vers des sorties cohérentes et fiables.",
        ["Question de vocabulaire. Qu'est-ce qu'un prompt pattern, selon le syllabus ?"],
        ["{#rev}Un modèle réutilisable pour rédiger des prompts efficaces, et obtenir des sorties cohérentes et fiables."],
    ),
    cards(
        K + "5.2.3", "Le testeur, spécialiste du test assisté par l'IA",
        [("🔄", "Un nouveau profil", "De spécialiste de la conception et de l'exécution des tests à spécialiste du test assisté par l'IA."),
         ("🧭", "Guider et vérifier", "Ses techniques de test, plus la capacité de guider et de vérifier le testware généré par l'IA."),
         ("📚", "Des tâches élargies", "Revue de l'ensemble des sorties de l'IA, affinage des prompts, bibliothèques de prompts de test.")],
        ["Dernier objectif, cinq point deux point trois : l'évolution des processus et des rôles. "
         "{#c0}Le testeur passe de spécialiste de la conception et de l'exécution des tests à spécialiste du test assisté par l'IA. "
         "{#c1}Il combine sa maîtrise des techniques de test avec la capacité de guider et de vérifier le testware généré. "
         "{#c2}Ses tâches s'élargissent : revue de l'ensemble des sorties de l'IA, affinage des prompts, "
         "et maintenance des bibliothèques de prompts spécifiques au test."],
    ),
    cards(
        K + "5.2.3", "Les nouvelles missions du test manager",
        [("🗺️", "Stratégie et risques", "Une stratégie de test et une gestion des risques fondées sur l'IA."),
         ("📡", "Suivi et contrôle", "Le suivi et le contrôle des processus de test fondés sur l'IA."),
         ("⚖️", "Équilibre et gouvernance", "Équilibrer humains et IA ; des cadres de gouvernance de l'IA pour les cas d'usage."),
         ("🎓", "Double compétence", "Des équipes qui gardent leurs compétences de test classiques et développent leur culture IA."),
         ("🤝", "Équipes hybrides", "Diriger des testeurs et coordonner des agents de test propulsés par l'IA générative.")],
        ["Et le test manager ? {#c0}Ses responsabilités incluent désormais une stratégie de test et une gestion des risques fondées sur l'IA, "
         "{#c1}ainsi que le suivi et le contrôle des processus de test fondés sur l'IA. "
         "{#c2}Il équilibre les capacités humaines et celles de l'IA, et met en place des cadres de gouvernance de l'IA pour les cas d'usage. "
         "{#c3}Il veille à ce que son équipe garde ses compétences de test classiques tout en développant sa culture de l'IA. "
         "{#c4}Et il ne dirige plus seulement des testeurs : il coordonne aussi des agents de test propulsés par l'IA générative. "
         "Piloter ces équipes hybrides demande de nouvelles compétences de management."],
        cols=3,
    ),
    quiz(
        K + "Entraînement 5.2.3",
        "Dans une organisation qui adopte l'IA générative, quelle responsabilité revient au test manager ?",
        ["Maintenir les bibliothèques de prompts de test", "Établir une gouvernance de l'IA pour les cas d'usage",
         "Affiner les prompts au quotidien", "Revoir chaque sortie générée par l'IA"], 1,
        "La gouvernance de l'IA revient au test manager ; prompts et revue des sorties, au testeur.",
        ["Dernière question. Dans une organisation qui adopte l'IA générative, quelle responsabilité revient au test manager ?"],
        ["{#rev}Établir une gouvernance de l'IA pour les cas d'usage. Les trois autres tâches font partie du nouveau rôle du testeur."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes du chapitre 5",
        [("Shadow AI", "IA sans approbation : risques de sécurité et confidentialité, de conformité, de propriété intellectuelle."),
         ("Stratégie", "Objectifs mesurables, choix des LLM, qualité des données, formation, métriques, lignes directrices."),
         ("Choix du modèle", "Performance, potentiel de fine-tuning, coût récurrent, communauté et support."),
         ("Trois phases", "Découverte, initiation et définition des usages, utilisation et itération, parfois en parallèle."),
         ("Compétences", "Prompts, contexte, revue, risques, sécurité des données, environnement ; pratique et communautés."),
         ("Rôles", "Testeur : test assisté par l'IA. Test manager : stratégie, risques, gouvernance, équipes hybrides.")],
        ["Récapitulons. {#r0}Un : le shadow AI expose à trois risques, sécurité et confidentialité, conformité, et propriété intellectuelle. "
         "{#r1}Deux : une stratégie part d'objectifs mesurables, et pense aux modèles, aux données, à la formation, aux métriques et aux règles. "
         "{#r2}Trois : quatre critères de choix d'un modèle. {#r3}Quatre : trois phases d'adoption, qui peuvent avancer en parallèle. "
         "{#r4}Cinq : des compétences qui se construisent par la pratique et les communautés. "
         "{#r5}Et six : le testeur devient spécialiste du test assisté par l'IA, et le test manager pilote des équipes hybrides."],
    ),
    title_scene(
        "CT-GenAI v1.1 · Fin du syllabus",
        "Félicitations, vous avez terminé le syllabus !",
        "Prochaine étape : les examens d'exemple officiels, puis les examens blancs de l'application",
        ["5 chapitres terminés", "Examens d'exemple officiels", "Examens blancs de l'application"],
        ["Et voilà : vous venez de terminer le cinquième et dernier chapitre. Félicitations, vous avez parcouru tout le syllabus CT-GenAI ! "
         "{#sub}Place maintenant à l'entraînement en conditions réelles. Faites les examens d'exemple officiels de l'ISTQB, "
         "puis enchaînez les examens blancs de l'application, en vous chronométrant. Revoyez les épisodes des chapitres où vous hésitez. "
         "{#chips}Vous avez toutes les clés en main. Bonne préparation, et bonne chance pour l'examen !"],
    ),
]
