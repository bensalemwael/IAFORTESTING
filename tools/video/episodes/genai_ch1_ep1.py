# CT-GenAI v1.1 · Chapitre 1 · Épisode unique : l'IA générative expliquée simplement (sections 1.1 et 1.2).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import bignum, cards, chat, code, quiz, rows, title_scene, versus

K = "CT-GenAI · Chapitre 1 · "

META = {
    "file": "genai-chapitre-1-episode-1",
    "title": "CT-GenAI · Chapitre 1 · Épisode unique : l'IA générative expliquée simplement",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 1 · Épisode unique",
        "L'IA générative expliquée simplement",
        "Des familles d'IA aux LLM, et ce qu'ils apportent au test logiciel",
        ["Sections 1.1 et 1.2", "1 objectif K1, 5 objectifs K2", "Environ 14 minutes"],
        ["Bonjour, et bienvenue dans le chapitre un. {#sub}Ici, on pose les fondations : d'où vient l'IA générative, "
         "comment fonctionne un grand modèle de langage, quels types de modèles existent, et ce qu'ils peuvent faire pour les testeurs. "
         "{#chips}Un objectif K un, cinq objectifs K deux, et aucune connaissance préalable n'est nécessaire. "
         "On avance pas à pas, avec des images simples."],
    ),
    cards(
        K + "1.1", "IA générative et LLM : deux définitions",
        [("✨", "IA générative", "Branche de l'IA qui utilise de grands modèles pré-entraînés pour produire du texte, des images ou du code."),
         ("📚", "LLM", "Modèles d'IA générative pré-entraînés sur d'immenses textes : ils saisissent le contexte et répondent aux prompts."),
         ("🧪", "Pour le testeur", "Critères d'acceptation, cas et scripts de test, défauts, données synthétiques, documentation…")],
        ["Commençons par deux définitions. {#c0}L'IA générative est une branche de l'intelligence artificielle qui utilise de grands modèles "
         "pré-entraînés pour produire un résultat qui ressemble à celui d'un humain : du texte, des images, ou du code. "
         "{#c1}Les grands modèles de langage, les LLM, sont des modèles d'IA générative pré-entraînés sur de très grands ensembles de textes. "
         "Ils peuvent saisir le contexte, et produire des réponses pertinentes à partir des prompts de l'utilisateur. "
         "{#c2}En test, ils aident tout au long du processus : revoir et améliorer des critères d'acceptation, générer des cas ou des scripts de test, "
         "repérer des défauts potentiels, analyser des tendances de défauts, générer des données de test synthétiques, ou produire de la documentation."],
    ),
    cards(
        K + "1.1.1", "Le spectre de l'IA en quatre familles",
        [("📜", "IA symbolique", "Un système à base de règles : la connaissance est représentée par des symboles et des règles logiques."),
         ("📊", "Machine learning classique", "Piloté par les données : préparation, sélection des features, entraînement. Ex. : classer des défauts."),
         ("🧠", "Deep learning", "Des réseaux de neurones apprennent seuls les features dans de très grands jeux de données."),
         ("✨", "IA générative", "S'appuie sur le deep learning pour créer du contenu nouveau : texte, images, code.")],
        ["L'IA est un vaste domaine. Le syllabus en retient quatre familles. "
         "{#c0}L'IA symbolique imite la prise de décision humaine avec des règles : la connaissance y est représentée par des symboles "
         "et des règles logiques. {#c1}Le machine learning classique est piloté par les données. Il demande de préparer les données, "
         "de sélectionner les features, c'est-à-dire les caractéristiques utiles, puis d'entraîner le modèle. On s'en sert par exemple "
         "pour catégoriser des défauts ou prédire des problèmes logiciels. "
         "{#c2}Le deep learning utilise des réseaux de neurones qui apprennent les features tout seuls, dans des données très volumineuses "
         "et complexes : images, vidéo, audio ou texte. Même si, en pratique, l'humain intervient encore, pour annoter les données, "
         "régler le modèle ou valider les résultats. "
         "{#c3}Enfin, l'IA générative utilise le deep learning pour créer du contenu nouveau, en imitant les motifs de ses données d'entraînement. "
         "{#trap}Retenez la distinction clé : features choisies à la main, ou apprises automatiquement."],
        trap="Machine learning classique : features **choisies à la main**. Deep learning : features **apprises automatiquement**.",
    ),
    versus(
        K + "1.1.1", "L'avantage clé : un modèle déjà entraîné",
        ("📊 Approche classique", ["Collecter et préparer les données", "Sélectionner les features",
                                   "Entraîner le modèle", "Seulement ensuite : l'utiliser"]),
        ("✨ IA générative", ["Le modèle est déjà pré-entraîné", "Il s'applique directement aux tâches de test",
                              "Pas de phase d'entraînement supplémentaire", "Mais des risques : voir le chapitre 3"]),
        ["Quel est l'intérêt pour nous, testeurs ? {#left}Avec une approche classique, il faut collecter et préparer des données, "
         "choisir des features et entraîner un modèle avant de pouvoir s'en servir. "
         "{#right}Avec l'IA générative, le modèle est déjà pré-entraîné : on l'applique directement aux tâches de test, "
         "sans phase d'entraînement supplémentaire. Le syllabus en fait l'avantage clé. ",
         {"max": "Génial, donc on branche et ça marche tout seul ?"},
         "Pas si vite, Max. Le syllabus précise aussitôt que cet avantage s'accompagne de risques. "
         "On les étudiera en détail au chapitre trois."],
    ),
    quiz(
        K + "1.1.1",
        "Un outil classe les défauts grâce à des caractéristiques choisies par l'équipe et à un modèle entraîné sur l'historique. Quel type d'IA ?",
        ["IA symbolique", "Machine learning classique", "Deep learning", "IA générative"], 1,
        "Machine learning classique : préparation des données, sélection des features, puis entraînement.",
        ["Premier quiz. Un outil classe les défauts grâce à des caractéristiques choisies par l'équipe, "
         "et à un modèle entraîné sur l'historique des défauts. De quel type d'IA s'agit-il ?"],
        ["{#rev}Du machine learning classique. L'indice décisif : les features sont sélectionnées par des humains. "
         "En deep learning, le réseau les apprendrait tout seul."],
    ),
    cards(
        K + "1.1.2", "Qu'est-ce qu'un LLM ?",
        [("🏗️", "GPT", "Generative Pre-trained Transformer : le modèle de deep learning sur lequel reposent les LLM."),
         ("📖", "Données d'entraînement", "De très grands ensembles de données : livres, articles, sites web."),
         ("🪶", "SLM", "Petits modèles de langage : moins de paramètres, pour des solutions légères et ciblées.")],
        ["Entrons dans la machine. {#c0}Les LLM reposent sur le modèle GPT : generative pre-trained transformer. "
         "Génératif : il produit du contenu. Pré-entraîné : il a appris avant qu'on s'en serve. "
         "Transformer : c'est son architecture. "
         "{#c1}Les LLM sont entraînés sur de très grands ensembles de données : des livres, des articles, des sites web. "
         "Cela leur permet de gérer les nuances du langage et de produire un contenu cohérent. "
         "{#c2}À côté, il existe des petits modèles de langage, les SLM. Ils sont compacts, avec moins de paramètres, "
         "et conçus pour offrir des solutions d'IA générative légères et ciblées."],
    ),
    code(
        K + "Démonstration HO-1.1.2", "La tokenisation : des briques de Lego",
        "Texte : Le bouton « Valider » reste grisé après la saisie.\n\n"
        "Tokens (découpage illustratif) :\n"
        "[Le] [ bouton] [ «] [ Val] [ider] [ »] [ reste]\n"
        "[ gr] [isé] [ après] [ la] [ sa] [isie] [.]\n\n"
        "→ 8 mots, mais 14 tokens\n"
        "→ « Valider », « grisé », « saisie » : coupés en morceaux",
        ["Pour traiter du texte, un LLM doit d'abord le convertir en nombres. Première étape : la tokenisation. "
         "Imaginez une construction en Lego : le modèle démonte la phrase en petites briques, les tokens. "
         "{#code}Prenons une phrase de rapport de défaut. Un tokenizer la découpe : certains mots restent entiers, "
         "d'autres sont coupés en morceaux, et la ponctuation devient un token à part. Huit mots, mais quatorze tokens. "
         "{#note}Un token peut être aussi petit qu'un caractère, ou aussi grand qu'un morceau de mot ou qu'un mot entier. "
         "Le modèle traite chaque token individuellement, tout en gardant le contexte global de la phrase. "
         "C'est le premier volet de l'exercice du syllabus."],
        note=("Briques de Lego", "Un token peut être un caractère, un morceau de mot ou un mot entier.", "ok"),
    ),
    cards(
        K + "1.1.2", "Les embeddings : une carte du sens",
        [("🔢", "Des vecteurs", "Chaque token devient un vecteur, un point dans un espace à très nombreuses dimensions."),
         ("🗺️", "Une carte", "Sens ou rôle proche = positions proches : « défaut » se place près de « bug »."),
         ("🧭", "À quoi ça sert", "Saisir les relations entre les mots, garder le contexte, produire des réponses cohérentes.")],
        ["Deuxième étape : les embeddings. {#c0}Chaque token est transformé en vecteur, c'est-à-dire une liste de nombres, "
         "qui le place dans un espace à très nombreuses dimensions. Ces nombres encodent les relations sémantiques, syntaxiques et contextuelles du token. "
         "{#c1}Pensez à une carte : les tokens dont le sens ou le rôle se ressemblent sont placés tout près les uns des autres, "
         "comme deux villages voisins. Défaut, par exemple, se retrouve près de bug. "
         "{#c2}Cette proximité permet au modèle de comprendre les relations entre les mots, de garder le contexte, "
         "et de produire des réponses cohérentes et adaptées. Retenez : tokenisation et embeddings convertissent le langage en nombres."],
    ),
    chat(
        K + "1.1.2", "Prédire le token suivant",
        "Complète la phrase : « Le test de connexion a échoué parce que… »",
        "… le mot de passe de l'utilisateur de test avait expiré.",
        ["Comment le modèle écrit-il ? Les LLM utilisent une architecture de réseau de neurones appelée transformer. "
         "Elle excelle à traiter le contexte de longues séquences de texte, et apprend comment les tokens sont liés entre eux. "
         "Quand il génère, le modèle prédit le token suivant, puis le suivant, comme l'autocomplétion de votre téléphone, en beaucoup plus puissant. "
         "{#type}Demandons-lui de compléter une phrase de rapport de test. {#send}{#answer}La réponse coule de source. ",
         {"max": "Il a l'air tellement sûr de lui. C'est forcément la bonne cause, non ?"},
         "{#verdict}Non, Max. Le texte est statistiquement plausible, d'après les données d'entraînement et le prompt. "
         "{#note}Mais le syllabus insiste : plausible ne veut pas forcément dire correct. Le modèle n'a jamais vu vos journaux d'exécution."],
        verdict=("PLAUSIBLE ≠ CORRECT", "bad"),
        note=("Plausible n'est pas correct", "Le modèle prédit une suite plausible, pas la vérité : le testeur vérifie.", "warn"),
    ),
    rows(
        K + "1.1.2", "Même prompt, réponses différentes",
        [("Essai 1", "« … parce que le mot de passe de l'utilisateur de test avait expiré. »"),
         ("Essai 2", "« … parce que le serveur d'authentification n'a pas répondu à temps. »"),
         ("Essai 3", "« … parce que le jeton de session n'était plus valide. »")],
        ["Envoyons maintenant exactement le même prompt trois fois. {#r0}Premier essai : le mot de passe avait expiré. "
         "{#r1}Deuxième essai : le serveur n'a pas répondu à temps. {#r2}Troisième essai : le jeton de session n'était plus valide. "
         "Imaginez un dé pipé : certaines faces sortent plus souvent que d'autres, mais jamais avec certitude. "
         "{#trap}C'est le non-déterminisme. Il vient surtout de la nature probabiliste de l'inférence, et du réglage des hyperparamètres. "
         "Résultat : la même entrée peut produire des sorties différentes. Pour un testeur, c'est une donnée essentielle."],
        trap="Même entrée, sorties différentes : c'est le **non-déterminisme**, dû à l'inférence probabiliste et aux hyperparamètres.",
    ),
    bignum(
        K + "Démonstration HO-1.1.2", "La fenêtre de contexte : la taille du bureau",
        150000, "tokens",
        "Exemple : le journal de tests de la nuit, à comparer à la fenêtre de contexte du modèle",
        ["Dernière notion clé : la fenêtre de contexte. C'est la quantité de texte précédent, mesurée en tokens, "
         "que le modèle peut prendre en compte pour générer sa réponse. Voyez-la comme un bureau : le modèle ne travaille "
         "qu'avec les documents qui tiennent dessus. {#n}Prenons un journal de tests de cent cinquante mille tokens. "
         "{#cap}C'est le second volet de l'exercice du syllabus : compter les tokens de différents textes, et comparer à la fenêtre du modèle. "
         "Une grande fenêtre garde la cohérence sur de longs passages, par exemple pour analyser de gros journaux de tests. "
         "Mais plus il y a de tokens, plus la complexité de calcul et le temps de traitement augmentent."],
    ),
    quiz(
        K + "1.1.2",
        "Qu'est-ce que la fenêtre de contexte d'un LLM ?",
        ["Le nombre de paramètres du modèle", "La quantité de texte, en tokens, que le modèle peut prendre en compte",
         "La période couverte par les données d'entraînement", "Le nombre de prompts envoyés dans une session"], 1,
        "La quantité de texte précédent, mesurée en tokens, que le modèle considère pour générer sa réponse.",
        ["Deuxième quiz. Qu'est-ce que la fenêtre de contexte d'un LLM ?"],
        ["{#rev}La quantité de texte précédent, mesurée en tokens, que le modèle peut prendre en compte. "
         "Plus elle est grande, plus le modèle reste cohérent sur de longs textes, mais plus le traitement est coûteux."],
    ),
    cards(
        K + "1.1.3", "Trois étapes de spécialisation",
        [("🏛️", "LLM de fondation", "Généraliste, pré-entraîné sur des données vastes et variées. Demande en général une adaptation."),
         ("🎯", "LLM ajusté aux instructions", "Dérivé d'un modèle de fondation, affiné sur des paires prompt et réponse attendue."),
         ("🧩", "LLM de raisonnement", "Prolonge le précédent : inférence logique, problèmes en plusieurs étapes, chaîne de pensée.")],
        ["Les LLM sont construits par étapes de plus en plus spécialisées. {#c0}Le LLM de fondation est généraliste. "
         "Il est pré-entraîné sur des données vastes et variées : texte, code, images, et d'autres modalités. "
         "Il demande en général une adaptation pour une tâche précise. "
         "{#c1}Le LLM ajusté aux instructions, ou instruction-tuned, dérive d'un modèle de fondation. Il est affiné avec des paires "
         "associant un prompt et la réponse attendue, pour mieux suivre les consignes, respecter la tâche, et répondre de façon cohérente. "
         "{#c2}Le LLM de raisonnement prolonge le précédent : il met l'accent sur l'inférence logique, la résolution de problèmes en plusieurs étapes "
         "et la chaîne de pensée. Il convient aux tâches à forte charge cognitive. "
         "{#trap}En test, on utilise les deux derniers : le choix dépend de la complexité de la tâche."],
        trap="En test : LLM **ajustés aux instructions** (dits non-raisonnants) ou **de raisonnement**, selon la complexité de la tâche.",
    ),
    quiz(
        K + "1.1.3",
        "Il faut déduire, étape par étape, les cas limites de règles de tarification imbriquées. Quel type de LLM convient le mieux ?",
        ["LLM de fondation non adapté", "LLM ajusté aux instructions", "LLM de raisonnement", "Petit modèle de langage (SLM)"], 2,
        "Un LLM de raisonnement : il est conçu pour l'inférence logique et les problèmes en plusieurs étapes.",
        ["Troisième quiz. Il faut déduire, étape par étape, les cas limites de règles de tarification imbriquées. "
         "Quel type de LLM convient le mieux ?"],
        ["{#rev}Un LLM de raisonnement. La tâche demande plusieurs étapes de raisonnement logique : c'est exactement sa spécialité."],
    ),
    cards(
        K + "1.1.4", "Multimodal et vision-langage",
        [("🎛️", "LLM multimodal", "Traite plusieurs modalités : texte, images, son et vidéo. La tokenisation est adaptée à chacune."),
         ("👁️", "Modèle vision-langage", "Un sous-ensemble des multimodaux, qui relie l'information visuelle et le texte."),
         ("🖼️", "Ses tâches", "Légender une image, répondre à une question sur une image, vérifier la cohérence texte-image."),
         ("🧪", "En test", "Croiser captures ou wireframes et textes, repérer les écarts, générer des cas plus riches.")],
        ["{#c0}Les LLM multimodaux étendent le transformer à plusieurs modalités : texte, images, son et vidéo. "
         "Pour chaque type de données, la tokenisation est adaptée. Par exemple, les images sont converties en embeddings par des modèles vision-langage, "
         "avant d'être traitées par le transformer. {#c1}Les modèles vision-langage sont justement un sous-ensemble des multimodaux, "
         "qui intègrent information visuelle et texte. {#c2}Ils savent légender une image, répondre à une question sur une image, "
         "et analyser la cohérence entre un texte et un visuel. "
         "{#c3}En test, ils analysent des captures d'écran ou des wireframes, avec une user story ou un rapport de défaut. "
         "On repère ainsi les écarts entre le résultat attendu et l'écran réel. Et ils peuvent générer des cas de test riches, "
         "mêlant texte et indices visuels, ce qui augmente la couverture."],
        cols=4,
    ),
    chat(
        K + "Démonstration HO-1.1.4", "Démonstration : un prompt texte et image",
        "[Image : capture de l'écran de paiement] Compare cette capture à l'US-12 : « Le bouton Payer affiche le total TTC. » Liste les écarts.",
        "Écart 1 : le bouton affiche « Payer » sans aucun montant.\nÉcart 2 : le total visible porte la mention HT, pas TTC.\nÀ confirmer : le libellé sous le total est illisible sur la capture.",
        ["Passons à l'exercice du syllabus, en deux étapes. Étape un : revoir les entrées, c'est-à-dire le prompt, le texte et l'image. "
         "Ici, une capture de l'écran de paiement, et une user story : le bouton Payer affiche le total TTC. "
         "{#type}On envoie les deux ensemble au modèle multimodal. {#send}"
         "{#answer}Étape deux : exécuter, puis vérifier le résultat réel. Le modèle signale deux écarts, et une zone illisible. ",
         {"max": "Il a vraiment lu l'image ? Je peux lui faire confiance ?"},
         "{#note}C'est tout l'enjeu de l'étape deux, Max : on contrôle chaque écart sur la vraie capture. "
         "L'exercice montre les bénéfices de l'approche, mais aussi ses difficultés potentielles."],
        note=("Étape 2 : vérifier", "Chaque écart signalé est contrôlé sur la vraie capture avant d'ouvrir un défaut.", "warn"),
    ),
    cards(
        K + "1.2.1", "Sept capacités clés : les quatre premières",
        [("📋", "Analyse des exigences", "Repérer ambiguïtés, incohérences, manques ; proposer des questions pour clarifier."),
         ("🧪", "Création de cas de test", "Générer des cas et suggérer des objectifs de test à partir de la base de test."),
         ("🔮", "Oracle de test", "Aider à générer les résultats attendus."),
         ("🎲", "Données de test", "Générer des jeux de données, fixer des valeurs limites, créer des combinaisons.")],
        ["Section un point deux. Les LLM savent interpréter des exigences, des spécifications, des captures d'écran, du code, "
         "des cas de test et des rapports de défauts. Le syllabus en tire sept capacités clés pour le test. "
         "{#c0}Un : l'analyse et l'amélioration des exigences. Le modèle repère les ambiguïtés, les incohérences ou les informations manquantes, "
         "et propose des questions à poser aux parties prenantes. "
         "{#c1}Deux : l'aide à la création de cas de test, et la suggestion d'objectifs de test, à partir de la base de test. "
         "{#c2}Trois : la génération d'oracles de test, c'est-à-dire des résultats attendus. "
         "{#c3}Quatre : la génération de données de test : des jeux de données, des valeurs limites, des combinaisons."],
    ),
    cards(
        K + "1.2.1", "Sept capacités clés : les trois dernières",
        [("🤖", "Automatisation", "Générer des scripts depuis les cas de test, améliorer les scripts, suggérer des techniques de test."),
         ("📈", "Analyse des résultats", "Résumer les résultats, classer les anomalies par sévérité et par priorité."),
         ("📄", "Création du testware", "Plans de test, rapports de test et de défauts, tenus à jour au fil du projet.")],
        ["{#c0}Cinq : l'aide à l'automatisation. Le modèle génère des scripts à partir des descriptions de cas de test, "
         "améliore les scripts existants en suggérant des modifications, et identifie les techniques de test appropriées. "
         "{#c1}Six : l'analyse des résultats de test, en produisant des résumés, et en classant les anomalies par sévérité et par priorité. "
         "{#c2}Et sept : la création du testware, comme les plans de test, les rapports de test et les rapports de défauts, "
         "tenus à jour au fil du projet. Ensemble, ces capacités couvrent tout le processus de test."],
    ),
    quiz(
        K + "1.2.1",
        "Un LLM propose le résultat attendu de chacun des 20 cas de test déjà rédigés. Quelle capacité est utilisée ?",
        ["Génération d'oracles de test", "Génération de données de test", "Analyse des exigences", "Analyse des résultats de test"], 0,
        "La génération d'oracles de test : le LLM aide à produire les résultats attendus.",
        ["Quatrième quiz. Un LLM propose le résultat attendu de chacun des vingt cas de test déjà rédigés. Quelle capacité est utilisée ?"],
        ["{#rev}La génération d'oracles de test. Un oracle, c'est ce qui donne le résultat attendu. "
         "Ne confondez pas avec l'analyse des résultats, qui porte sur des tests déjà exécutés."],
    ),
    versus(
        K + "1.2.2", "Chatbot IA ou application de test à base de LLM ?",
        ("💬 Chatbot IA", ["Interface conversationnelle, réponses immédiates", "Affinage itératif, par exemple par chaînage",
                           "Tâches courantes, test exploratoire, intégration des nouveaux", "Accessible aux non-techniciens"]),
        ("🔌 Application à base de LLM", ["Intégration via API dans les outils de test", "Tâches bien définies, souvent automatisées",
                                         "Plus de personnalisation et de passage à l'échelle", "Jusqu'aux agents IA : chapitre 4"]),
        ["Dernier objectif : comparer deux façons d'utiliser l'IA générative. {#left}Le chatbot IA offre une interface conversationnelle : "
         "on pose une question, on obtient une réponse immédiate et adaptée au contexte. Avec le chaînage de prompts, on affine le résultat pas à pas. "
         "Il est idéal pour les tâches courantes, le test exploratoire, l'intégration des nouveaux testeurs, le retour rapide, "
         "la clarification de concepts, ou l'exploration des exigences. Et il est accessible même aux non-techniciens. "
         "{#right}L'application de test à base de LLM intègre le modèle via des API, pour des tâches bien définies et souvent automatisées : "
         "génération de cas de test, analyse de défauts, synthèse de données de test. Elle offre plus de personnalisation et de passage à l'échelle, "
         "et peut aller jusqu'à des agents IA dédiés à un rôle de test, vus au chapitre quatre."],
    ),
    quiz(
        K + "1.2.2",
        "Une équipe veut générer chaque nuit des données de test synthétiques au sein de son framework de test. Quelle approche convient ?",
        ["Un chatbot IA utilisé à la main", "Une application à base de LLM, intégrée via API",
         "Un système d'IA symbolique à base de règles", "Un LLM de fondation sans aucun prompt"], 1,
        "Une application à base de LLM : intégrée via API, elle automatise des tâches répétitives et passe à l'échelle.",
        ["Cinquième quiz. Une équipe veut générer chaque nuit des données de test synthétiques, au sein de son framework de test. "
         "Quelle approche convient le mieux ?"],
        ["{#rev}Une application de test à base de LLM, intégrée via API. Tâche bien définie, automatisée et répétitive : "
         "c'est son terrain. Le chatbot, lui, brille dans l'échange interactif."],
    ),
    cards(
        K + "1.2.2", "Le point commun : le prompt engineering",
        [("✍️", "Des prompts soignés", "Chatbot ou application intégrée : sans prompt engineering solide, pas de bons résultats."),
         ("🎯", "Des consignes claires", "Des instructions claires et spécifiques, conçues avec soin."),
         ("✅", "Des résultats utiles", "Plus de chances d'obtenir des résultats exacts, pertinents et alignés sur les objectifs de test.")],
        ["{#c0}Quelle que soit la façon d'interagir avec un LLM, "
         "réussir avec l'IA générative en test demande un prompt engineering solide. C'est tout le sujet du chapitre deux. "
         "{#c1}Des prompts conçus avec soin, avec des instructions claires et spécifiques, "
         "{#c2}augmentent les chances d'obtenir des résultats exacts, pertinents et alignés sur les objectifs de test. "
         "C'est ainsi qu'on tire le meilleur de l'IA générative, avec une aide plus cohérente et plus fiable sur toutes les activités de test."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes du chapitre 1",
        [("4 familles d'IA", "Symbolique, machine learning classique, deep learning, IA générative. Atout : le pré-entraînement."),
         ("Du texte aux nombres", "Tokenisation en briques, embeddings sur une carte du sens, transformer qui prédit le token suivant."),
         ("Plausible ≠ correct", "Le résultat est statistiquement plausible, et non déterministe : on vérifie toujours."),
         ("Fenêtre de contexte", "Mesurée en tokens. Plus grande : plus de cohérence, mais plus de calcul et de temps."),
         ("3 types de LLM", "Fondation, ajusté aux instructions, raisonnement. Multimodal et vision-langage pour les images."),
         ("7 capacités, 2 usages", "De l'analyse des exigences au testware ; chatbot ou application, toujours du prompt engineering.")],
        ["Récapitulons ce chapitre. {#r0}Un : quatre familles d'IA, et l'avantage clé de l'IA générative, des modèles déjà pré-entraînés. "
         "{#r1}Deux : tokenisation et embeddings convertissent le langage en nombres, et le transformer prédit le token suivant. "
         "{#r2}Trois : plausible ne veut pas dire correct, et le même prompt peut donner des réponses différentes. "
         "{#r3}Quatre : la fenêtre de contexte se mesure en tokens, et elle a un coût. "
         "{#r4}Cinq : modèles de fondation, ajustés aux instructions ou de raisonnement, et modèles multimodaux pour les images. "
         "{#r5}Et six : sept capacités clés pour le test, deux façons de les utiliser, et toujours le même besoin de bons prompts."],
    ),
    title_scene(
        "À suivre · Chapitre 2",
        "Le prompt engineering pour le test logiciel",
        "Structurer ses prompts, les appliquer aux tâches de test, puis évaluer les résultats",
        ["Le plus gros chapitre", "Objectifs K2 et K3", "Quatre épisodes"],
        ["Bravo, vous avez terminé le chapitre un ! {#sub}Vous savez maintenant ce qu'est un LLM et ce qu'il peut faire. "
         "Dans le chapitre deux, on apprend à bien lui parler : structurer ses prompts, les appliquer aux tâches de test, "
         "puis évaluer et améliorer les résultats. {#chips}C'est le plus gros chapitre du programme, en quatre épisodes. "
         "D'ici là, faites les questions et les flashcards du chapitre un dans l'application. À très vite !"],
    ),
]
