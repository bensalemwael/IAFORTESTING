# CT-GenAI v1.1 · Chapitre 4 · Épisode 1 : architecture d'une infrastructure de test propulsée par LLM et RAG (4.1.1, 4.1.2).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import cards, chat, code, flow, quiz, rows, title_scene, versus

K = "CT-GenAI · Chapitre 4 · "

META = {
    "file": "genai-chapitre-4-episode-1",
    "title": "CT-GenAI · Chapitre 4 · Épisode 1 : architecture et RAG",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 4 · Épisode 1 sur 2",
        "L'infrastructure de test propulsée par LLM",
        "Composants clés, architecture et Retrieval-Augmented Generation",
        ["Sections 4.1.1 et 4.1.2", "2 objectifs K2", "Environ 11 minutes"],
        ["Bonjour, et bienvenue dans le chapitre quatre. On quitte le prompt seul pour regarder ce qu'il y a autour. "
         "{#sub}Dans ce premier épisode : les composants d'une infrastructure de test propulsée par LLM, puis le RAG, "
         "qui permet au modèle de s'appuyer sur vos propres documents. {#chips}Deux objectifs de niveau K deux, "
         "un exercice pratique, et environ onze minutes. C'est parti."],
    ),
    rows(
        K + "Vue d'ensemble", "Le chapitre 4 en deux épisodes",
        [("Épisode 1 · 4.1.1", "Les composants clés d'une infrastructure de test propulsée par LLM. K2."),
         ("Épisode 1 · 4.1.2", "La Retrieval-Augmented Generation, ou RAG, avec un exercice pratique. K2."),
         ("Épisode 2 · 4.1.3", "Les agents propulsés par LLM pour automatiser les processus de test. K2."),
         ("Épisode 2 · 4.2.1", "Le fine-tuning des modèles de langage pour des tâches de test. K2."),
         ("Épisode 2 · 4.2.2", "LLMOps : déployer et gérer les LLM pour les tâches de test. K2.")],
        ["Le chapitre quatre représente cent dix minutes de formation officielle, et cinq objectifs, tous de niveau K deux. "
         "À l'examen, on vous demandera donc d'expliquer, de résumer et de distinguer. "
         "{#r0}Dans cet épisode, l'architecture d'une infrastructure de test propulsée par LLM. "
         "{#r1}Puis le RAG, la génération augmentée par la récupération. "
         "{#r2}Dans l'épisode suivant, les agents, {#r3}le fine-tuning, {#r4}et LLMOps. "
         "Les mots clés du chapitre : infrastructure de test, RAG, base de données vectorielle, agent, fine-tuning et LLMOps."],
    ),
    versus(
        K + "4.1.1", "Chatbot IA ou outil de test propulsé par LLM ?",
        ("💬 Chatbot IA", ["Centré sur les interactions conversationnelles", "Traite des questions, répond en langage naturel",
                          "Communication interactive avec l'utilisateur"]),
        ("🧪 Outil de test propulsé par LLM", ["Conçu pour soutenir le test logiciel", "Traite des requêtes liées au test",
                                             "Analyse les exigences, génère des cas de test", "Évalue des résultats"]),
        ["Le syllabus distingue deux types d'infrastructures de test qui utilisent des LLM, déjà rencontrés au chapitre un. "
         "{#left}Le chatbot IA est d'abord centré sur la conversation : on pose une question, il répond. "
         "{#right}L'outil de test propulsé par LLM, lui, est conçu pour soutenir le test logiciel. Il traite des requêtes liées au test, "
         "analyse les exigences, génère des cas de test et évalue des résultats. "
         "Une infrastructure de test propulsée par LLM, c'est donc un système qui intègre un LLM dans le processus de test, "
         "pour améliorer l'automatisation, le raisonnement et la prise de décision."],
    ),
    cards(
        K + "4.1.1", "Les composants d'une infrastructure de test LLM",
        [("🖥️", "Front-end", "L'interface utilisateur : le testeur y saisit ses requêtes ou ses commandes."),
         ("⚙️", "Back-end", "Traite la saisie : authentification, récupération de données, préparation du prompt, échange avec le LLM."),
         ("🗄️", "Sources de données", "Des sources externes intégrées par le back-end : bases relationnelles et bases vectorielles."),
         ("🧠", "LLM", "Service tiers accessible par API, ou modèle maison. Génère les réponses à partir de prompts structurés.")],
        ["Voyons l'architecture typique. Elle repose sur plusieurs composants, pour une interaction sûre et efficace avec le LLM. "
         "{#c0}Le front-end, c'est l'interface : le testeur y saisit ses requêtes ou ses commandes. "
         "{#c1}Le back-end traite cette saisie, et gère les fonctions critiques : l'authentification, la récupération des données, "
         "la préparation du prompt, et l'interaction avec le LLM. {#c2}Il s'appuie sur des sources de données externes. "
         "{#c3}Et enfin, le LLM génère les réponses à partir de prompts structurés. Il peut être hébergé comme un service tiers, "
         "accessible par API, ou être un modèle maison."],
    ),
    flow(
        K + "4.1.1", "Le trajet d'une requête de test",
        [("🖥️", "Saisie", "Le testeur envoie sa requête depuis le front-end"),
         ("⚙️", "Préparation", "Le back-end authentifie, récupère les données, prépare le prompt"),
         ("🧠", "Génération", "Le LLM répond au prompt structuré"),
         ("🧹", "Post-traitement", "Le back-end améliore la sortie brute du LLM")],
        ["Suivons une requête. {#s0}Le testeur saisit sa demande dans le front-end. "
         "{#s1}Le back-end l'authentifie, va chercher les données utiles dans ses sources, et prépare un prompt structuré. "
         "{#s2}Le LLM génère sa réponse. {#s3}Puis le back-end améliore cette sortie brute, par un post-traitement. "
         "{#check}L'objectif : que la réponse soit alignée sur les conditions de test du processus de test, "
         "avant d'être présentée dans le front-end."],
        check="✔ Réponse alignée sur les conditions de test, puis affichée dans le front-end",
    ),
    rows(
        K + "4.1.1", "Bien plus qu'une architecture client-serveur",
        [("Un composant intelligent", "Le LLM n'est pas un simple serveur : il interprète et raisonne à partir du testware."),
         ("Des analyses dynamiques", "Pas de réponses scriptées : tout est généré à partir du contexte (exigences, code, résultats)."),
         ("Plusieurs sources de données", "Bases relationnelles (données structurées, ex. cas de test) et bases vectorielles (embeddings)."),
         ("Un post-traitement", "Le back-end améliore la sortie brute du LLM pour l'aligner sur les conditions de test.")],
        ["Le syllabus insiste : cette architecture va au-delà d'un modèle client-serveur classique, pour quatre raisons. "
         "{#r0}Un : le LLM n'est pas un simple serveur. C'est un composant intelligent, qui interprète et raisonne à partir du testware. "
         "{#r1}Deux : contrairement aux chatbots à base de règles, qui suivent des réponses scriptées, l'infrastructure génère ses analyses "
         "dynamiquement, à partir du contexte : exigences, code ou résultats de test. "
         "{#r2}Trois : le back-end intègre plusieurs sources. Des bases relationnelles, pour les données structurées comme les cas de test, "
         "et des bases vectorielles, pour retrouver des contenus proches par le sens, grâce aux embeddings. "
         "{#r3}Quatre : le back-end post-traite la sortie brute du LLM. {#trap}Retenez bien le premier point."],
        trap="Le LLM n'est **pas un simple serveur** : c'est un composant intelligent qui raisonne sur le testware.",
    ),
    code(
        K + "4.1.1", "Dans les coulisses du back-end",
        "> Testeur : « Propose les cas de test de l'exigence REQ-118 »\n\n"
        "[1] Authentification ........ compte testeur vérifié\n"
        "[2] Base relationnelle ...... REQ-118 + 6 cas de test existants\n"
        "[3] Base vectorielle ........ 3 passages proches dans les specs\n"
        "[4] Préparation du prompt ... rôle, contexte, données, format\n"
        "[5] Appel au LLM ............ API du fournisseur\n"
        "[6] Post-traitement ......... format vérifié, 2 doublons retirés\n\n"
        "< Front-end : 9 nouveaux cas de test proposés, à relire",
        [{"max": "Concrètement, il se passe quoi entre ma question et la réponse ?"},
         "Regardons les coulisses, Max. {#code}Le testeur demande des cas de test pour l'exigence REQ cent dix-huit. "
         "Le back-end vérifie d'abord son identité. Il lit l'exigence et les cas existants dans la base relationnelle, "
         "puis cherche des passages proches dans la base vectorielle. Il assemble un prompt structuré, appelle le LLM, "
         "et post-traite la réponse : format vérifié, doublons retirés. "
         "{#note}Le testeur ne voit que le résultat final. Et ce résultat, il le relit avant de l'utiliser."],
        note=("Le rôle du back-end", "Authentifier, récupérer les données, préparer le prompt, appeler le LLM, post-traiter.", "ok"),
    ),
    quiz(
        K + "Entraînement 4.1.1",
        "Dans une infrastructure de test propulsée par LLM, à quoi sert le post-traitement réalisé par le back-end ?",
        ["À réentraîner le LLM avec les réponses produites", "À aligner la sortie brute du LLM sur les conditions de test",
         "À authentifier le testeur avant l'appel au LLM", "À recueillir la saisie du testeur"], 1,
        "Avant l'affichage, le back-end améliore la sortie brute du LLM pour l'aligner sur les conditions de test.",
        ["À vous de jouer. Dans une infrastructure de test propulsée par LLM, à quoi sert le post-traitement réalisé par le back-end ?"],
        ["{#rev}À aligner la sortie brute du LLM sur les conditions de test, avant de la présenter dans le front-end. "
         "L'authentification, elle, a lieu avant l'appel au LLM, et la saisie se fait dans le front-end."],
    ),
    quiz(
        K + "Entraînement 4.1.1",
        "Qu'est-ce qui distingue une infrastructure de test propulsée par LLM d'un chatbot à base de règles ?",
        ["Elle suit des réponses scriptées à l'avance", "Elle génère ses analyses dynamiquement, à partir du contexte",
         "Elle n'a besoin d'aucune source de données", "Elle fonctionne sans back-end"], 1,
        "Elle génère dynamiquement ses analyses à partir des exigences, du code ou des résultats de test.",
        ["Deuxième question. Qu'est-ce qui distingue une infrastructure de test propulsée par LLM d'un chatbot à base de règles ?"],
        ["{#rev}Elle génère ses analyses dynamiquement, à partir du contexte. Le chatbot à base de règles, lui, suit des réponses scriptées."],
    ),
    chat(
        K + "4.1.2", "Le modèle ne connaît pas vos documents",
        "Quel est le plafond de retrait hebdomadaire de notre carte Premium ? Donne les valeurs limites à tester.",
        "En général, les cartes premium ont un plafond\nde retrait d'environ 1 000 € par semaine.\nValeurs limites : 999,99 € · 1 000,00 € · 1 000,01 €",
        ["Passons à l'objectif quatre point un point deux, avec une expérience. "
         "{#type}On demande à un LLM : quel est le plafond de retrait hebdomadaire de notre carte Premium, et quelles valeurs limites tester ? "
         "{#send}Envoyé. {#answer}Il répond avec assurance : environ mille euros par semaine. Mais ce chiffre ne vient pas de notre spécification. "
         "{#verdict}La réponse n'est pas ancrée dans nos données. "
         "{#note}Le modèle s'appuie seulement sur ce qu'il a appris pendant son entraînement : il ne connaît pas nos documents internes. "
         "C'est exactement le problème que le RAG vient résoudre."],
        verdict=("NON ANCRÉ", "bad"),
        note=("Le problème", "Le LLM ne s'appuie que sur son entraînement : il ignore vos spécifications internes.", "warn"),
    ),
    versus(
        K + "4.1.2", "LLM seul ou LLM avec RAG ?",
        ("🧠 LLM seul", ["Répond à partir de son entraînement préalable", "Ignore les documents de l'entreprise",
                        "Ses réponses peuvent manquer de précision"]),
        ("📚 LLM avec RAG", ["Intègre des sources de données supplémentaires", "Un retriever récupère les données pertinentes",
                            "Réponses plus pertinentes et plus exactes", "Plus fiables et plus informatives"]),
        ["La Retrieval-Augmented Generation, en français génération augmentée par la récupération, "
         "améliore les LLM en intégrant des sources de données supplémentaires dans leur processus de génération. "
         "{#left}Sans RAG, le modèle ne répond qu'à partir de son entraînement préalable. "
         "{#right}Avec le RAG, on associe le LLM à un système de récupération, un retriever, qui va chercher les données pertinentes. "
         "La réponse n'est plus seulement fondée sur l'entraînement du modèle : elle est enrichie de données précises, liées au prompt. "
         "Résultat : des réponses plus pertinentes, plus exactes, et donc plus fiables pour l'utilisateur."],
    ),
    flow(
        K + "4.1.2", "Étape préalable : préparer les documents",
        [("📚", "Documents", "Spécifications, exigences, guides volumineux"),
         ("✂️", "Découpage", "En chunks de 256 à 512 tokens, par exemple"),
         ("🧮", "Embeddings", "Chaque chunk est nettoyé, traité, puis encodé en vecteur"),
         ("🗄️", "Base vectorielle", "Stockage pour une recherche par similarité")],
        ["Comment ça marche ? Tout commence par un prétraitement. {#s0}On part de documents volumineux. "
         "{#s1}On les découpe en petits morceaux, appelés chunks, par exemple de deux cent cinquante-six à cinq cent douze tokens. "
         "Pourquoi ? Pour une récupération ciblée, et compatible avec la fenêtre de contexte du modèle. "
         "{#s2}Chaque chunk est nettoyé, traité, puis encodé en un vecteur de grande dimension, un embedding, à l'aide de modèles pré-entraînés. "
         "{#s3}Ces embeddings peuvent être stockés dans une base de données vectorielle. Elle permet une recherche efficace par similarité "
         "au moment de l'exécution, qu'on appelle aussi l'inférence."],
    ),
    flow(
        K + "4.1.2", "À chaque prompt : récupérer, puis générer",
        [("❓", "Requête", "La question de l'utilisateur est encodée à son tour"),
         ("🔎", "1 · Récupération", "Les chunks pertinents sont retrouvés par similarité sémantique"),
         ("✍️", "2 · Génération", "Le LLM combine ses connaissances et les chunks récupérés"),
         ("✅", "Réponse ancrée", "Plus exacte et mieux adaptée au contexte")],
        ["Ensuite, à chaque prompt, le système RAG travaille en deux étapes. {#s0}La requête de l'utilisateur est encodée, elle aussi. "
         "{#s1}Première étape, la récupération : le système cherche les informations pertinentes dans la base vectorielle. "
         "En général, il compare l'embedding du prompt à ceux des chunks, par similarité sémantique. "
         "{#s2}Deuxième étape, la génération : les chunks récupérés sont fournis au LLM comme contexte. "
         "Il produit une réponse qui combine ses connaissances existantes et ces nouvelles données. "
         "{#s3}On obtient une réponse ancrée, plus exacte et mieux adaptée au contexte. "
         "{#trap}À l'examen, retenez l'ordre : récupération d'abord, génération ensuite."],
        trap="RAG = **récupération** des chunks par similarité sémantique, **puis génération** par le LLM avec ce contexte.",
    ),
    chat(
        K + "4.1.2", "Même question, avec RAG",
        "Quel est le plafond de retrait hebdomadaire de notre carte Premium ? Donne les valeurs limites à tester.",
        "D'après SPEC-CARTES v3, § 4.2 (passage récupéré) :\nplafond de 1 500 € sur 7 jours glissants.\nValeurs limites : 1 499,99 € · 1 500,00 € · 1 500,01 €\nSource : SPEC-CARTES v3, § 4.2",
        ["Même question, mais cette fois, l'outil de test est relié par RAG à nos spécifications. "
         "{#type}On repose exactement la même question. {#send}Envoyé. "
         "{#answer}Le système a d'abord récupéré le bon passage de la spécification des cartes, puis le LLM a généré sa réponse : "
         "mille cinq cents euros sur sept jours glissants, avec les valeurs limites correspondantes, et la source. "
         "{#verdict}Cette fois, la réponse est ancrée. "
         "{#note}Elle repose sur des informations pertinentes, exactes et adaptées au contexte, et pas seulement sur l'entraînement du modèle. "
         "Le testeur la vérifie quand même, mais il sait d'où elle vient."],
        verdict=("ANCRÉ", "good"),
        note=("Réponse ancrée", "Fondée sur des données précises et récupérées, pas seulement sur l'entraînement du modèle.", "ok"),
    ),
    cards(
        K + "4.1.2", "Le RAG au service du test",
        [("🗃️", "Sources de l'entreprise", "Bases de données, documentation, dépôts : l'infrastructure de test y accède."),
         ("⏱️", "En temps réel", "Les informations contextuelles sont récupérées au moment de la tâche de test."),
         ("🎯", "Toujours à jour", "Analyse et conception alignées sur les dernières spécifications, exigences et données de test.")],
        ["Et dans le test logiciel, concrètement ? {#c0}Le RAG permet à l'infrastructure de test d'accéder aux sources de données "
         "de l'entreprise : bases de données, documentation, dépôts. {#c1}Elle y récupère des informations contextuelles en temps réel. "
         "{#c2}Ainsi, des tâches comme l'analyse de test ou la conception des tests restent alignées sur les dernières spécifications, "
         "les dernières exigences, et les données de test existantes."],
    ),
    rows(
        K + "HO-4.1.2", "Exercice : expérimenter le RAG",
        [("Intégrer", "Alimenter un système RAG avec des documents liés à une tâche de test."),
         ("Comparer", "Confronter la sortie du LLM avec et sans RAG, sur la même tâche."),
         ("Observer", "Les réponses sont plus ou moins exactes selon la complexité de l'information."),
         ("Examiner", "Inspecter les données récupérées et les résultats générés."),
         ("Conclure", "Identifier les forces et les limites du RAG selon les types de tâches de test.")],
        [{"max": "Donc avec le RAG, le modèle a toujours raison ?"},
         "Pas si vite, Max. C'est justement l'objet de l'exercice pratique du syllabus, de niveau H un. "
         "{#r0}On alimente un système RAG avec des documents. {#r1}On compare la sortie du LLM avec et sans RAG, sur la même tâche de test. "
         "{#r2}On observe que les réponses sont plus ou moins exactes, selon la complexité de l'information. "
         "{#r3}On examine les données récupérées, et les résultats générés. "
         "{#r4}Le but : identifier les forces et les limites du RAG, selon les types de tâches de test."],
    ),
    quiz(
        K + "Entraînement 4.1.2",
        "Dans un système RAG, sur quoi repose en général l'étape de récupération ?",
        ["Une correspondance exacte des mots-clés", "La similarité sémantique entre embeddings",
         "Un réentraînement du LLM sur les documents", "L'ordre chronologique des documents"], 1,
        "La similarité sémantique entre l'embedding du prompt et ceux des chunks stockés.",
        ["Passons à l'entraînement sur le RAG. Dans un système RAG, sur quoi repose en général l'étape de récupération ?"],
        ["{#rev}La similarité sémantique entre embeddings. Le prompt est encodé, puis comparé aux chunks. "
         "Attention au piège : le RAG ne réentraîne pas le modèle."],
    ),
    quiz(
        K + "Entraînement 4.1.2",
        "Pourquoi découpe-t-on les documents en chunks lors du prétraitement RAG ?",
        ["Pour réduire le coût de licence du LLM", "Pour une récupération ciblée, compatible avec la fenêtre de contexte",
         "Pour supprimer les données personnelles", "Pour entraîner un nouveau modèle de langage"], 1,
        "Des chunks courts permettent une récupération ciblée et tiennent dans la fenêtre de contexte du modèle.",
        ["Pourquoi découpe-t-on les documents en chunks lors du prétraitement ?"],
        ["{#rev}Pour une récupération ciblée, et compatible avec la fenêtre de contexte du modèle."],
    ),
    quiz(
        K + "Entraînement 4.1.2",
        "Une équipe veut des tests alignés sur la dernière version des exigences, stockées dans son dépôt. Que lui conseiller ?",
        ["Un chatbot à base de règles", "Le RAG, relié au dépôt des exigences",
         "Un prompt zero-shot plus court", "Un LLM sans aucune source externe"], 1,
        "Le RAG récupère en temps réel les données de l'entreprise : les tests suivent les dernières exigences.",
        ["Une situation. Une équipe veut que son outil conçoive des tests alignés sur la dernière version des exigences, "
         "stockées dans son dépôt. Que lui conseiller ?"],
        ["{#rev}Le RAG, relié au dépôt des exigences. Il récupère en temps réel le contexte de l'entreprise, "
         "pour que la conception reste alignée sur les dernières exigences."],
    ),
    quiz(
        K + "Entraînement 4.1.2",
        "Dans un système RAG, que stocke la base de données vectorielle ?",
        ["Les poids du LLM", "Les chunks encodés en embeddings", "Les comptes des utilisateurs", "Les réponses validées par les testeurs"], 1,
        "Les embeddings des chunks, pour une récupération par similarité sémantique.",
        ["Dernière question. Dans un système RAG, que stocke la base de données vectorielle ?"],
        ["{#rev}Les chunks encodés en embeddings. Les données structurées, comme les cas de test, vont plutôt dans une base relationnelle."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes de l'épisode 1",
        [("Quatre composants", "Front-end, back-end, sources de données et LLM (service tiers par API ou modèle maison)."),
         ("Le back-end", "Authentification, récupération de données, préparation du prompt, appel au LLM, post-traitement."),
         ("Pas un client-serveur", "Le LLM raisonne sur le testware et génère ses analyses dynamiquement, à partir du contexte."),
         ("Prétraitement RAG", "Découpage en chunks, encodage en embeddings, stockage dans une base vectorielle."),
         ("Deux étapes", "Récupération par similarité sémantique, puis génération d'une réponse ancrée."),
         ("RAG et test", "Accès en temps réel aux sources de l'entreprise : des tests alignés sur les dernières exigences.")],
        ["Récapitulons. {#r0}Un : une infrastructure de test propulsée par LLM, c'est un front-end, un back-end, des sources de données, et un LLM. "
         "{#r1}Deux : le back-end fait le gros du travail, de l'authentification jusqu'au post-traitement. "
         "{#r2}Trois : ce n'est pas un simple client-serveur, le LLM raisonne sur le testware. "
         "{#r3}Quatre : le RAG prépare les documents en chunks, puis en embeddings, stockés dans une base vectorielle. "
         "{#r4}Cinq : à chaque prompt, récupération par similarité sémantique, puis génération. "
         "{#r5}Et six : en test, le RAG aligne le travail sur les dernières spécifications de l'entreprise."],
    ),
    title_scene(
        "À suivre · Épisode 2",
        "Agents, fine-tuning et LLMOps",
        "Automatiser avec des agents, spécialiser un modèle, l'exploiter en production",
        ["Sections 4.1.3 à 4.2.2", "3 objectifs K2", "Démonstrations"],
        ["Bravo, c'est la fin de ce premier épisode. {#sub}Dans le prochain, on découvre les agents propulsés par LLM, "
         "puis le fine-tuning et LLMOps, pour rendre l'IA générative opérationnelle dans le test. "
         "{#chips}Trois objectifs K deux, avec des démonstrations. D'ici là, révisez l'architecture et le RAG avec les questions "
         "du chapitre quatre dans l'application. À très vite !"],
    ),
]
