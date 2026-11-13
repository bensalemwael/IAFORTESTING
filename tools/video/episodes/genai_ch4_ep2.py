# CT-GenAI v1.1 · Chapitre 4 · Épisode 2 : agents propulsés par LLM, fine-tuning et LLMOps (4.1.3, 4.2.1, 4.2.2).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import cards, chat, code, flow, quiz, rows, title_scene, versus

K = "CT-GenAI · Chapitre 4 · "

META = {
    "file": "genai-chapitre-4-episode-2",
    "title": "CT-GenAI · Chapitre 4 · Épisode 2 : agents, fine-tuning et LLMOps",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 4 · Épisode 2 sur 2",
        "Agents, fine-tuning et LLMOps",
        "Automatiser avec des agents, spécialiser un modèle, l'exploiter en production",
        ["Sections 4.1.3 à 4.2.2", "3 objectifs K2", "Environ 12 minutes"],
        ["Bienvenue dans le deuxième et dernier épisode du chapitre quatre. "
         "{#sub}Après l'architecture et le RAG, on s'intéresse aux agents propulsés par LLM, puis aux deux pratiques "
         "qui rendent l'IA générative opérationnelle dans le test : le fine-tuning et LLMOps. "
         "{#chips}Trois objectifs de niveau K deux, et deux démonstrations. C'est parti."],
    ),
    versus(
        K + "4.1.3", "Du chatbot à l'agent",
        ("💬 Chatbot IA", ["Centré sur les interactions question-réponse", "Produit des réponses en langage naturel",
                          "Ne fait que répondre"]),
        ("🤖 Agent propulsé par LLM", ["Application d'IA générative spécialisée", "Traite des tâches définies, en semi-autonomie ou en autonomie",
                                      "Agit en appelant des fonctions prédéfinies : les outils", "Interagit avec des systèmes externes"]),
        ["Commençons par l'objectif quatre point un point trois. "
         "{#left}Un chatbot IA traditionnel se concentre uniquement sur les interactions question-réponse. "
         "{#right}Un agent propulsé par LLM est une application d'IA générative spécialisée, conçue pour traiter des tâches définies "
         "de façon semi-autonome ou autonome. Sa grande différence : il peut agir. Il invoque un ensemble prédéfini de fonctions, "
         "qu'on appelle des outils. Cela lui permet d'interagir avec des systèmes externes, et de les manipuler. "
         "C'est ce qui le rend si polyvalent."],
    ),
    cards(
        K + "4.1.3", "Ce qui compose un agent",
        [("🧠", "Un LLM au cœur", "Pour comprendre et générer le langage naturel."),
         ("📋", "Des instructions", "La capacité de traiter les instructions reçues."),
         ("🔎", "Du contexte", "La capacité de récupérer le contexte utile à la tâche."),
         ("🛠️", "Des actions", "Des actions intelligentes, menées en appelant des outils.")],
        ["Que trouve-t-on dans un agent ? {#c0}Au cœur, un LLM, pour comprendre et générer le langage naturel. "
         "{#c1}Autour, la capacité de traiter des instructions, {#c2}de récupérer du contexte, "
         "{#c3}et de mener des actions intelligentes grâce aux outils. "
         "Le glossaire du syllabus le résume ainsi : un agent intègre le raisonnement, la prise de décision et la mémoire d'un LLM, "
         "et utilise des outils pour réaliser des tâches."],
    ),
    versus(
        K + "4.1.3", "Autonome ou semi-autonome ?",
        ("🚀 Agent autonome", ["Travaille de façon indépendante", "Intervention humaine minimale",
                              "Règles prédéfinies et apprentissage par renforcement", "Boucles de rétroaction adaptatives"]),
        ("🤝 Agent semi-autonome", ["Supervision humaine périodique",
                                   "L'humain s'assure que la sortie atteint les objectifs fixés par l'utilisateur"]),
        ["Le degré d'autonomie d'un agent peut varier. {#left}Un agent autonome opère de façon indépendante, avec une intervention humaine minimale. "
         "Il s'appuie sur des règles prédéfinies, l'apprentissage par renforcement, et des boucles de rétroaction adaptatives. "
         "{#right}Un agent semi-autonome, lui, réalise ses tâches sous une supervision humaine périodique, "
         "pour s'assurer que la sortie atteint les objectifs définis par l'utilisateur. "
         "{#trap}Le mot clé à repérer à l'examen : la supervision humaine."],
        trap="Semi-autonome = supervision humaine **périodique**. Autonome = intervention humaine **minimale**.",
    ),
    flow(
        K + "4.1.3", "Plusieurs agents, une orchestration",
        [("🔍", "Agent analyste", "Identifie les conditions de test"),
         ("✏️", "Agent concepteur", "Rédige les cas de test"),
         ("▶️", "Agent exécutant", "Lance les tests"),
         ("📊", "Agent rapporteur", "Synthétise les résultats")],
        ["On peut aussi faire travailler plusieurs agents ensemble : c'est une architecture multi-agents, "
         "un système collaboratif où chaque agent a un rôle spécialisé. Imaginons {#s0}un agent pour l'analyse, "
         "{#s1}un pour la conception, {#s2}un pour l'exécution, {#s3}et un pour le rapport. "
         "{#check}Ils communiquent et se coordonnent pour résoudre des problèmes complexes plus efficacement qu'un agent seul. "
         "Cette coordination s'appelle l'orchestration. Les agents automatisent alors des tâches de test "
         "en imitant le raisonnement et la prise de décision humains."],
        check="✔ Orchestration : des agents spécialisés communiquent et se coordonnent",
    ),
    rows(
        K + "4.1.3", "Les agents dans les outils de test",
        [("Des assistants IA", "Les agents sont souvent proposés via des assistants IA intégrés au flux de travail du test."),
         ("Tout le cycle de vie", "User stories et exigences deviennent du testware : analyse, conception, implémentation, exécution, rapport."),
         ("Moins d'effort", "Une automatisation continue, de bout en bout : moins d'effort manuel, des retours plus rapides."),
         ("Un changement de cap", "De l'exécution de scripts à une automatisation pilotée par les objectifs, à base d'agents.")],
        ["Dans les outils de test modernes, {#r0}les agents sont souvent proposés aux utilisateurs via des assistants IA, "
         "intégrés au flux de travail du test. {#r1}Ces assistants transforment des user stories ou des exigences en artefacts de test, "
         "sur tout le cycle de vie : analyse, conception, implémentation, exécution et rapport de test, de façon semi-autonome. "
         "{#r2}On obtient une automatisation continue, de bout en bout, qui réduit l'effort manuel et raccourcit les cycles de rétroaction. "
         "{#r3}Et l'automatisation des tests change de nature : on passe de l'exécution de scripts à une automatisation pilotée par les objectifs, "
         "à base d'agents. {#trap}Une formulation à bien retenir."],
        trap="Automatisation à base d'agents : pilotée par les **objectifs**, et non plus par l'exécution de **scripts**.",
    ),
    code(
        K + "HO-4.1.3", "Démonstration : un agent et une tâche répétitive",
        "ENTRÉE   Objectif : trier les échecs de la régression nocturne n° 1842\n\n"
        "[outil]  lire_rapport(1842) → 37 tests en échec\n"
        "[outil]  lire_logs(37 tests)\n"
        "[pensée] 29 échecs : même timeout sur le service de paiement\n"
        "[outil]  chercher_defauts(\"timeout paiement\") → DEF-311 ouvert\n"
        "[action] relier les 29 échecs à DEF-311\n"
        "[pensée] 8 échecs restants : causes différentes\n"
        "[action] rédiger 8 brouillons de rapports de défaut\n"
        "[pause]  validation humaine demandée avant création\n\n"
        "SORTIE   1 défaut existant mis à jour · 8 brouillons à relire",
        ["Place à la démonstration prévue par le syllabus : un agent qui aide à automatiser une tâche répétitive. "
         "{#code}En entrée, un objectif : trier les échecs de la régression nocturne. L'agent appelle ses outils : "
         "il lit le rapport, trente-sept tests en échec, puis les journaux d'exécution.Il raisonne : vingt-neuf échecs ont la même cause, "
         "un timeout du service de paiement. Il interroge l'outil de gestion des défauts, trouve un défaut déjà ouvert, et y relie ces échecs. "
         "Pour les huit autres, il rédige des brouillons de rapports, puis il s'arrête : une validation humaine est demandée. "
         "{#note}Voilà les trois aspects à observer : les données d'entrée, le comportement de l'agent, et les résultats de ses actions."],
        note=("Ce qu'on observe", "Les données d'entrée, le comportement de l'agent et le résultat de ses actions.", "ok"),
    ),
    versus(
        K + "4.1.3", "Agents : risques et parades",
        ("⚠️ Les mêmes risques que les LLM", ["Hallucinations", "Erreurs de raisonnement", "Biais",
                                             "Résultats incorrects ou trompeurs : fiabilité affaiblie"]),
        ("🛡️ Les parades", ["Vérification automatisée des résultats de l'agent", "Agents semi-autonomes pour les tâches critiques"]),
        [{"max": "Génial ! Je laisse l'agent tourner seul toutes les nuits, alors ?"},
         "Prudence, Max. {#left}Les agents souffrent des mêmes problèmes que les LLM, vus au chapitre trois : "
         "hallucinations, erreurs de raisonnement et biais. Ils peuvent produire des résultats incorrects ou trompeurs, "
         "et affaiblir la fiabilité des processus de test automatisés. "
         "{#right}Deux parades selon le syllabus : mettre en place des procédures de vérification automatisée des résultats de l'agent, "
         "ou utiliser des agents semi-autonomes pour les tâches critiques. "
         "C'est pour cela que notre agent de démonstration demandait une validation humaine."],
    ),
    quiz(
        K + "Entraînement 4.1.3",
        "Qu'est-ce qui distingue un agent propulsé par LLM d'un chatbot IA traditionnel ?",
        ["Il n'utilise pas de LLM", "Il agit en invoquant des fonctions prédéfinies, les outils",
         "Il ne fait jamais d'erreur de raisonnement", "Il fonctionne toujours sans supervision"], 1,
        "Les outils lui permettent d'agir sur des systèmes externes. Le chatbot se limite aux questions-réponses.",
        ["À vous de jouer. Qu'est-ce qui distingue un agent propulsé par LLM d'un chatbot IA traditionnel ?"],
        ["{#rev}Il agit, en invoquant des fonctions prédéfinies, les outils. Et non : un agent peut se tromper, "
         "et il n'est pas forcément autonome."],
    ),
    quiz(
        K + "Entraînement 4.1.3",
        "Un agent prépare la décision de mise en production d'une appli bancaire. Comment limiter le risque d'erreur ?",
        ["Le rendre entièrement autonome", "Utiliser un agent semi-autonome, supervisé par un humain",
         "Lui donner davantage d'outils", "Supprimer les vérifications pour aller plus vite"], 1,
        "Tâche critique : agent semi-autonome, ou vérification automatisée de ses résultats.",
        ["Une situation. Un agent prépare la décision de mise en production d'une application bancaire. "
         "Comment limiter le risque d'erreur ?"],
        ["{#rev}Avec un agent semi-autonome, supervisé par un humain. C'est la parade prévue pour les tâches critiques, "
         "avec la vérification automatisée des résultats."],
    ),
    flow(
        K + "4.2.1", "Fine-tuning : spécialiser un modèle",
        [("🧠", "Modèle pré-entraîné", "Un LLM, ou un petit modèle de langage, un SLM"),
         ("🏷️", "Données ciblées", "Un jeu d'exemples étiquetés de la tâche ou du domaine"),
         ("🔁", "Entraînement", "L'entraînement se poursuit : les poids sont mis à jour"),
         ("🎯", "Modèle spécialisé", "Il a appris les connaissances et les nuances du domaine")],
        ["Section quatre point deux. Pour rendre opérationnelle une infrastructure de test propulsée par LLM, le syllabus retient deux pratiques : "
         "le fine-tuning, et la gestion du pipeline opérationnel avec LLMOps. Commençons par le fine-tuning, objectif quatre point deux point un. "
         "{#s0}On part d'un modèle de langage pré-entraîné : un LLM, ou un SLM. "
         "{#s1}On lui fournit un jeu de données ciblé, fait d'exemples étiquetés : c'est un apprentissage supervisé. "
         "{#s2}On poursuit son entraînement sur ces données, ce qui met à jour ses poids. "
         "{#s3}Le modèle apprend les connaissances et les nuances du domaine. "
         "{#check}Ses performances s'améliorent pour l'application visée : il devient plus précis et plus pertinent."],
        check="✔ Plus précis et plus pertinent pour l'usage visé",
    ),
    versus(
        K + "4.2.1", "Affiner un LLM ou un SLM ?",
        ("🏔️ Affiner un LLM", ["Doter un LLM générique d'un raisonnement spécialisé", "Lui faire adopter le vocabulaire d'un domaine",
                              "Exige d'importantes ressources de calcul"]),
        ("🪶 Affiner un SLM", ["Modèle plus petit, moins gourmand en ressources", "Hautes performances sur des tâches précises",
                              "Sans le même coût de calcul qu'un LLM"]),
        ["{#left}En pratique, le fine-tuning sert à doter un LLM générique de capacités de raisonnement spécialisées, propres à un domaine, "
         "ou à lui faire adopter le vocabulaire de ce domaine. "
         "{#right}Mais on peut aussi affiner des modèles plus petits, les SLM, qui consomment moins de ressources. "
         "Un SLM affiné peut atteindre de hautes performances sur des tâches précises, sans le coût de calcul d'un LLM. "
         "Le syllabus souligne cette flexibilité : on choisit l'un ou l'autre selon les besoins de la tâche."],
    ),
    code(
        K + "HO-4.2.1", "Démonstration : un fine-tuning pas à pas",
        "# 1. Choisir le modèle de base : un LLM ou un SLM\n"
        "modele = charger(\"slm-open-source\")\n\n"
        "# 2. Un jeu de données adapté : nos user stories → nos cas de test\n"
        "{\"entree\": \"US-301 : En tant que client, je veux exporter mon relevé…\",\n"
        " \"sortie\": \"CT-301-01 | Préconditions | Étapes | Résultat attendu\"}\n"
        "… 1 200 paires relues par l'équipe de test\n\n"
        "# 3. Entraîner avec un framework de machine learning\n"
        "modele_affine = affiner(modele, donnees)\n\n"
        "# 4. Envoyer un prompt au modèle affiné, puis juger la sortie\n"
        "modele_affine.generer(\"Cas de test de l'US-450\")",
        ["Le syllabus prévoit une démonstration du processus, en quatre temps. "
         "{#code}Un : choisir un modèle approprié, un LLM ou un SLM. Deux : présenter un jeu de données adapté à la tâche, "
         "ici, les user stories de l'organisation, avec leurs cas de test au format maison. "
         "Trois : montrer une solution pour l'entraînement, par exemple un framework de machine learning. "
         "Quatre : envoyer un prompt au modèle affiné, et discuter de la qualité de sa sortie. "
         "{#note}Et la démonstration insiste sur un point en particulier : la qualité des données d'entraînement."],
        note=("Le point clé", "La qualité des données d'entraînement, adaptées à la tâche.", "warn"),
    ),
    chat(
        K + "4.2.1", "Résultat : le format de l'organisation",
        "Génère les cas de test de l'US-450 : en tant que client, je veux recevoir mon relevé mensuel par e-mail.",
        "CT-450-01 | Client abonné au relevé | Fin de mois | E-mail reçu, PDF joint\n"
        "CT-450-02 | Client non abonné | Fin de mois | Aucun e-mail envoyé\n"
        "CT-450-03 | Adresse e-mail invalide | Fin de mois | Alerte « contact KO »",
        [{"max": "Je ne pourrais pas juste donner des exemples dans le prompt ?"},
         "Bonne question, Max. Le few-shot guide le modèle le temps d'un prompt. Le fine-tuning, lui, poursuit l'entraînement du modèle. "
         "Prenons l'exemple du syllabus. {#type}On demande les cas de test d'une nouvelle user story. {#send}Envoyé. "
         "{#answer}Le modèle affiné répond directement au format de l'organisation, avec ses identifiants et sa terminologie. "
         "{#verdict}Il a été entraîné sur les user stories et les cas de test de l'organisation. "
         "{#note}Il s'aligne donc sur son processus de test et sur son vocabulaire."],
        verdict=("FORMAT MAISON", "good"),
        note=("Ce qu'apporte le fine-tuning", "Le modèle suit le processus de test et la terminologie de l'organisation.", "ok"),
    ),
    rows(
        K + "4.2.1", "Les quatre défis du fine-tuning",
        [("Qualité des données", "Des données d'entraînement de qualité, propres à la tâche, pour éviter des résultats biaisés ou inexacts."),
         ("Surapprentissage", "Le modèle colle trop à ses données d'entraînement et perd en performance sur des données nouvelles."),
         ("Opacité", "On voit mal comment le modèle décide : le débogage et la validation se compliquent."),
         ("Ressources de calcul", "Le fine-tuning d'un LLM exige d'importantes ressources de calcul.")],
        ["Le fine-tuning présente quatre défis. {#r0}Un : la qualité des données. Pour éviter des résultats biaisés ou inexacts, "
         "il faut des jeux d'entraînement de haute qualité, propres à la tâche. "
         "{#r1}Deux : le surapprentissage, ou overfitting. Le modèle devient trop spécialisé sur ses données d'entraînement, "
         "et ses performances baissent sur des données nouvelles. Il faut préserver sa capacité à généraliser. "
         "{#r2}Trois : l'opacité, c'est-à-dire le manque de transparence sur la façon dont le modèle produit ses sorties. "
         "Cela complique le débogage et la validation. {#r3}Quatre : les importantes ressources de calcul nécessaires, pour les LLM. "
         "{#trap}Le surapprentissage est un grand classique des questions d'examen."],
        trap="Excellent sur ses données d'entraînement, faible sur du neuf ? C'est du **surapprentissage** (overfitting).",
    ),
    quiz(
        K + "Entraînement 4.2.1",
        "Un modèle affiné réussit les user stories de son jeu d'entraînement, mais échoue sur les nouvelles. Quel défi ?",
        ["L'opacité", "Le surapprentissage", "La fenêtre de contexte", "Le coût de calcul"], 1,
        "Le surapprentissage : trop spécialisé sur ses données d'entraînement, le modèle généralise mal.",
        ["Une situation. Un modèle affiné produit d'excellents cas de test pour les user stories de son jeu d'entraînement, "
         "mais de médiocres pour les nouvelles. Quel défi ?"],
        ["{#rev}Le surapprentissage. Le modèle est devenu trop spécialisé sur ses données d'entraînement, et il généralise mal."],
    ),
    quiz(
        K + "Entraînement 4.2.1",
        "Pourquoi une équipe affinerait-elle un SLM plutôt qu'un LLM pour une tâche de test précise ?",
        ["Un SLM n'a besoin d'aucune donnée d'entraînement", "Pour de hautes performances sur la tâche, avec moins de calcul",
         "Un SLM ne présente aucun risque de biais", "Seuls les SLM peuvent être affinés"], 1,
        "Un SLM affiné peut bien performer sur une tâche précise, sans le coût de calcul d'un LLM.",
        ["Pourquoi une équipe affinerait-elle un SLM plutôt qu'un LLM, pour une tâche de test précise ?"],
        ["{#rev}Pour obtenir de hautes performances sur cette tâche, avec moins de ressources de calcul. "
         "Et attention : les LLM aussi peuvent être affinés."],
    ),
    versus(
        K + "4.2.2", "LLMOps : chatbot ou outil de test ?",
        ("💬 Approche 1 : un chatbot IA", ["Confidentialité et sécurité des données, coût optimisé",
                                          "LLM-as-a-Service si les garanties sont données",
                                          "Ou LLM open source déployé en interne",
                                          "Évaluer les garanties du fournisseur ou ses capacités internes"]),
        ("🧪 Approche 2 : un outil de test avec IA", ["Mêmes enjeux : confidentialité, sécurité, coûts",
                                                    "Évaluer les garanties de sécurité et de performance de l'éditeur",
                                                    "Complète les processus existants : analyse coût-bénéfice et des risques"]),
        ["Objectif quatre point deux point deux. LLMOps, ce sont les pratiques, outils et processus qui fluidifient le développement, "
         "le déploiement et la maintenance des LLM en production. Les décisions LLMOps dépendent de l'approche choisie. "
         "{#left}Un : un chatbot IA. L'enjeu : maîtriser confidentialité et sécurité, tout en optimisant le coût. "
         "On passe par une plateforme LLM-as-a-Service si les garanties sont données, ou par un LLM open source en interne, "
         "pour plus de contrôle. On évalue rigoureusement les garanties du fournisseur, ou ses propres capacités. "
         "{#right}Deux : un outil de test doté d'IA générative. Mêmes enjeux, plus les garanties de sécurité et de performance de l'éditeur. "
         "Et comme l'outil complète l'existant : analyse coût-bénéfice et évaluation des risques."],
    ),
    cards(
        K + "4.2.2", "Approche 3 : développer son outil en interne",
        [("🔒", "Contrôle complet", "Une maîtrise totale des risques de confidentialité et de sécurité des données."),
         ("🖥️", "Ressources IA", "Planifier le calcul, le stockage des données et la formation du personnel."),
         ("🔁", "Processus structurés", "Valider et maintenir les développements propres à l'IA générative."),
         ("🎓", "Expertise", "Savoir mettre en œuvre et déployer une infrastructure de test propulsée par LLM.")],
        ["Trois : développer en interne un outil de test fondé sur l'IA générative. "
         "{#c0}Cette approche met l'accent sur le contrôle complet des risques de confidentialité et de sécurité. "
         "{#c1}Elle demande de planifier soigneusement les ressources IA : puissance de calcul, stockage des données, et formation du personnel. "
         "{#c2}Il faut aussi établir des processus structurés pour valider et maintenir ces développements. "
         "{#c3}Et surtout, il faut de l'expertise pour mettre en œuvre et déployer une infrastructure de test propulsée par LLM."],
        cols=2,
    ),
    cards(
        K + "4.2.2", "Des approches combinables",
        [("💬", "Un chatbot pour certaines tâches", "Par exemple pour une partie des activités de test."),
         ("🏗️", "Un outil maison pour d'autres", "Les approches peuvent être mises en œuvre en même temps."),
         ("➕", "Enrichies par RAG et fine-tuning", "Pour une IA générative plus efficace et plus adaptable dans les processus de test.")],
        [{"max": "Donc il faut choisir une seule de ces trois approches ?"},
         "Non, Max, et c'est un piège d'examen. {#c0}Les approches ne s'excluent pas mutuellement. Une organisation peut utiliser "
         "un chatbot IA pour certaines tâches, {#c1}et développer ses propres outils pour d'autres, en même temps, selon les activités de test. "
         "{#c2}Et toutes peuvent intégrer d'autres technologies, comme le RAG et le fine-tuning de LLM ou de SLM, "
         "pour rendre les processus de test plus efficaces et plus adaptables."],
    ),
    quiz(
        K + "Entraînement 4.2.2",
        "Une organisation utilise un chatbot IA et veut aussi développer un outil maison. Que dit le syllabus ?",
        ["Elle doit d'abord abandonner le chatbot", "Les deux approches peuvent coexister",
         "Un outil maison interdit le RAG", "Le fine-tuning est réservé aux chatbots"], 1,
        "Les approches ne s'excluent pas : elles peuvent être mises en œuvre en même temps, selon les tâches.",
        ["Une organisation utilise déjà un chatbot IA, et veut aussi développer un outil de test maison. Que dit le syllabus ?"],
        ["{#rev}Les deux approches peuvent coexister. Elles ne s'excluent pas mutuellement, et peuvent intégrer le RAG ou le fine-tuning."],
    ),
    quiz(
        K + "Entraînement 4.2.2",
        "Quel point est mis en avant pour le développement interne d'un outil de test fondé sur l'IA générative ?",
        ["Se fier aux garanties de l'éditeur de l'outil", "Planifier calcul, stockage et formation du personnel",
         "Aucun besoin d'expertise particulière", "Éviter toute validation des développements"], 1,
        "Développement interne : contrôle complet, ressources IA planifiées, validation, maintenance et expertise.",
        ["Dernière question. Quel point est mis en avant pour le développement interne d'un outil de test fondé sur l'IA générative ?"],
        ["{#rev}La planification des ressources IA : calcul, stockage des données, formation du personnel. "
         "Les garanties de l'éditeur, elles, concernent l'approche avec un outil du marché."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes de l'épisode 2",
        [("Agent", "Application LLM qui agit via des outils, de façon autonome ou semi-autonome."),
         ("Multi-agents", "Des agents spécialisés qui communiquent et se coordonnent : c'est l'orchestration."),
         ("Risques des agents", "Hallucinations, erreurs de raisonnement, biais. Parades : vérification automatisée, semi-autonomie."),
         ("Fine-tuning", "Poursuivre l'entraînement d'un LLM ou d'un SLM sur un jeu de données ciblé."),
         ("Quatre défis", "Qualité des données, surapprentissage, opacité, ressources de calcul."),
         ("LLMOps", "Chatbot, outil du marché ou outil maison : trois approches combinables, avec RAG et fine-tuning.")],
        ["Récapitulons. {#r0}Un : un agent propulsé par LLM agit grâce à des outils, de façon autonome ou semi-autonome. "
         "{#r1}Deux : plusieurs agents spécialisés coordonnés, c'est l'orchestration. "
         "{#r2}Trois : les agents ont les mêmes risques que les LLM ; on vérifie automatiquement leurs résultats, "
         "ou on reste semi-autonome pour les tâches critiques. "
         "{#r3}Quatre : le fine-tuning poursuit l'entraînement d'un modèle sur un jeu de données ciblé. "
         "{#r4}Cinq : ses quatre défis, qualité des données, surapprentissage, opacité et ressources de calcul. "
         "{#r5}Et six : LLMOps dépend de l'approche choisie, et les trois approches se combinent."],
    ),
    title_scene(
        "À suivre · Chapitre 5",
        "Déployer l'IA générative dans une organisation de test",
        "Shadow AI, stratégie, choix des modèles, adoption et conduite du changement",
        ["Dernier chapitre", "Objectifs K1 et K2", "Épisode unique"],
        ["Bravo, vous avez terminé le chapitre quatre ! {#sub}Dans le dernier chapitre, on passe à l'échelle de l'organisation : "
         "les risques du shadow AI, la stratégie, le choix des modèles, les phases d'adoption, et l'évolution des rôles. "
         "{#chips}D'ici là, faites les questions et les flashcards du chapitre quatre dans l'application. À très vite !"],
    ),
]
