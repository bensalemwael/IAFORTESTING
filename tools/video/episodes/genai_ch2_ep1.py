# CT-GenAI v1.1 · Chapitre 2 · Épisode 1 : écrire des prompts efficaces (sections 2.1.1 à 2.1.3).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import cards, chat, code, flow, prompt_build, quiz, rows, title_scene, versus

K = "CT-GenAI · Chapitre 2 · "

META = {
    "file": "genai-chapitre-2-episode-1",
    "title": "CT-GenAI · Chapitre 2 · Épisode 1 : écrire des prompts efficaces",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 2 · Épisode 1 sur 4",
        "Écrire des prompts efficaces",
        "Structure, techniques et system prompt : la base de tout le chapitre",
        ["Sections 2.1.1 à 2.1.3", "3 objectifs K2", "Environ 15 minutes"],
        ["Bonjour, et bienvenue dans le chapitre deux, le plus important du syllabus. "
         "{#sub}Dans ce premier épisode, on apprend à écrire un bon prompt : sa structure, les grandes techniques, "
         "et la différence entre system prompt et user prompt. {#chips}Trois objectifs de niveau K deux, et environ quinze minutes. "
         "Installez-vous, on y va."],
    ),
    cards(
        K + "Vue d'ensemble", "Le chapitre 2 en quatre épisodes",
        [("✍️", "1 · Écrire", "2.1 · Structure d'un prompt, trois techniques, system et user prompt. K2."),
         ("🔍", "2 · Analyser et concevoir", "2.2.1 et 2.2.2 · Analyse de test, conception et implémentation. K3."),
         ("🔁", "3 · Automatiser et piloter", "2.2.3 à 2.2.5 · Régression, pilotage, choix de la technique. K3."),
         ("📏", "4 · Évaluer", "2.3 · Métriques et techniques pour affiner ses prompts. K2.")],
        ["Le chapitre deux représente trois cent soixante-cinq minutes de formation officielle, presque la moitié du programme. "
         "On le découpe donc en quatre épisodes. {#c0}Le premier, celui-ci : écrire de bons prompts. "
         "{#c1}Le deuxième : utiliser l'IA pour l'analyse de test et la conception des tests. "
         "{#c2}Le troisième : la régression automatisée, le pilotage, et le choix de la bonne technique. "
         "Ces deux épisodes couvrent les objectifs K trois, ceux où l'examen vous décrit une situation et vous demande quoi faire. "
         "{#c3}Et le quatrième : mesurer la qualité des résultats, et améliorer ses prompts."],
    ),
    chat(
        K + "2.1", "Pourquoi structurer son prompt ?",
        "Écris des tests pour la page de connexion.",
        "Voici quelques tests :\n• Tester une connexion valide\n• Tester un mot de passe invalide\n• Tester un champ vide",
        ["Commençons par une expérience. Vous ouvrez votre assistant, et vous tapez : {#type}écris des tests pour la page de connexion. "
         "{#send}Vous envoyez. {#answer}La réponse arrive : tester une connexion valide, tester un mot de passe invalide, tester un champ vide. ",
         {"max": "Sérieusement ? J'aurais pu l'écrire moi-même en dix secondes !"},
         "{#verdict}Exactement, Max. C'est générique. Ça pourrait s'appliquer à n'importe quel site. "
         "{#note}Et ce n'est pas la faute du modèle : il ne sait rien de votre application, de vos règles métier, ni de ce que vous attendez. "
         "Le syllabus le dit clairement : un bon prompt augmente les chances d'obtenir des résultats précis et utiles."],
        verdict=("GÉNÉRIQUE", "bad"),
        note=("Le vrai problème", "Le modèle ne connaît ni l'application, ni les règles métier, ni le résultat attendu.", "warn"),
    ),
    cards(
        K + "2.1.1", "Les six composants d'un prompt structuré",
        [("🎭", "Rôle", "La persona à adopter : testeur, test manager, ingénieur en automatisation."),
         ("🗺️", "Contexte", "Le contexte : l'objet de test, la fonctionnalité visée, les informations utiles."),
         ("🎯", "Instruction", "La tâche à réaliser : claire, à l'impératif, concise."),
         ("📎", "Données d'entrée", "Le matériel : user stories, critères d'acceptation, captures, code, cas existants."),
         ("🚧", "Contraintes", "Les restrictions : comment appliquer l'instruction aux données."),
         ("📐", "Format de sortie", "La forme attendue de la réponse : tableau, Gherkin, liste…")],
        ["Le syllabus propose une structure en six composants. {#c0}Un : le rôle. On indique au modèle quel point de vue adopter, "
         "par exemple un testeur ou un ingénieur en automatisation. Cela oriente son ton et sa démarche. "
         "{#c1}Deux : le contexte. Ce sont les informations de fond : l'objet de test, la fonctionnalité à tester. "
         "{#c2}Trois : l'instruction. C'est la tâche elle-même, formulée de façon claire, à l'impératif, et concise. "
         "{#c3}Quatre : les données d'entrée. Tout ce dont le modèle a besoin pour travailler : une user story, des critères "
         "d'acceptation, une capture d'écran, du code, des cas de test existants, ou des exemples de sortie. "
         "{#c4}Cinq : les contraintes. Les restrictions à respecter, autrement dit, la façon d'appliquer l'instruction aux données. "
         "{#c5}Et six : le format de sortie, c'est-à-dire la forme attendue de la réponse."],
        cols=3,
    ),
    prompt_build(
        K + "2.1.1", "Un vrai prompt, pièce par pièce",
        [("Rôle", "Tu es un testeur expert en applications bancaires."),
         ("Contexte", "Nous testons le virement instantané de l'appli mobile."),
         ("Instruction", "Rédige les cas de test fonctionnels de la user story."),
         ("Données d'entrée", "US-42 : « Je veux virer jusqu'à 1 000 € … »"),
         ("Contraintes", "Couvre les valeurs limites du montant. 12 cas maximum."),
         ("Format de sortie", "Tableau : ID | Préconditions | Étapes | Attendu")],
        ["Reprenons notre exemple, mais cette fois avec un vrai brief. {#l0}Le rôle : tu es un testeur expert en applications bancaires. "
         "{#l1}Le contexte : nous testons le virement instantané de l'application mobile. "
         "{#l2}L'instruction : rédige les cas de test fonctionnels de la user story. "
         "{#l3}Les données d'entrée : la user story elle-même, ici l'US quarante-deux. "
         "{#l4}Les contraintes : couvrir les valeurs limites du montant, et pas plus de douze cas. "
         "{#l5}Et le format de sortie : un tableau, avec identifiant, préconditions, étapes et résultat attendu. "
         "{#badge}Six composants. Chacun ajoute de la clarté et de la précision."],
        badge=("6", "composants"),
    ),
    chat(
        K + "2.1.1", "Même modèle, autre prompt",
        "[Rôle] Testeur bancaire · [Contexte] Virement instantané · [Instruction] Cas de test de l'US-42 · [Contraintes] Valeurs limites, 12 cas · [Format] Tableau",
        "TC1 | Solde suffisant | Virer 1 000,00 € | Virement accepté\nTC2 | Solde suffisant | Virer 1 000,01 € | Refus : plafond dépassé\nTC3 | Solde suffisant | Virer 0,01 € | Virement accepté\nTC4 | Solde suffisant | Virer 0,00 € | Refus : montant invalide",
        ["Et voici ce que donne le même modèle avec ce prompt structuré. {#type}On l'envoie… {#send}"
         "{#answer}Cette fois, les cas de test ciblent le vrai plafond de mille euros, avec les valeurs juste en dessous et juste au-dessus, "
         "et ils respectent le format demandé. {#verdict}C'est exploitable. "
         "{#note}Retenez cette idée : le modèle n'a pas changé. C'est la qualité du brief qui fait la qualité de la réponse. "
         "Mais attention : même un bon résultat doit être relu par le testeur."],
        verdict=("PRÉCIS", "good"),
        note=("À retenir", "Le modèle n'a pas changé : c'est le brief qui a changé. Et on relit toujours la réponse.", "ok"),
    ),
    rows(
        K + "2.1.1", "Les trois composants qu'on confond",
        [("Contexte", "L'arrière-plan : l'objet de test et la fonctionnalité concernée."),
         ("Données d'entrée", "Le matériel à traiter : user story, critères, capture, code, cas existants, exemples de sortie."),
         ("Contraintes", "Les règles d'application : « seulement les cas négatifs », « 12 cas maximum »…"),
         ("Format de sortie", "La forme du résultat : « en tableau », « en Gherkin », « en JSON »…")],
        ["À l'examen, quatre composants se confondent facilement. {#r0}Le contexte, c'est l'arrière-plan : de quoi parle-t-on, quel objet de test. "
         "{#r1}Les données d'entrée, c'est le matériel concret que le modèle doit traiter. "
         "{#r2}Les contraintes, ce sont les règles qui disent comment appliquer l'instruction à ces données. "
         "{#r3}Et le format de sortie décrit seulement la forme du résultat. "
         "{#trap}Un indice simple : si la phrase limite ou filtre ce que le modèle produit, c'est une contrainte. Si elle décrit la présentation, c'est le format."],
        trap="Ça limite ou filtre ? **Contrainte**. Ça décrit la présentation ? **Format de sortie**.",
    ),
    quiz(
        K + "Entraînement HO-2.1.1",
        "« Ne propose que des cas de test négatifs. » De quel composant s'agit-il ?",
        ["Contexte", "Instruction", "Contraintes", "Format de sortie"], 2,
        "Une contrainte : elle restreint la façon d'appliquer l'instruction aux données.",
        ["À vous de jouer. Dans un prompt, on lit : ne propose que des cas de test négatifs. De quel composant s'agit-il ?"],
        ["{#rev}Ce sont les contraintes. La phrase ne décrit pas la tâche elle-même, elle restreint la façon de l'appliquer."],
    ),
    quiz(
        K + "Entraînement HO-2.1.1",
        "« Voici la user story US-42 et la capture de l'écran de virement. » De quel composant s'agit-il ?",
        ["Rôle", "Données d'entrée", "Contexte", "Contraintes"], 1,
        "Des données d'entrée : le matériel que le modèle doit traiter, y compris des images.",
        ["Deuxième question. Voici la user story US quarante-deux et la capture de l'écran de virement. Quel composant ?"],
        ["{#rev}Les données d'entrée. Une user story, une capture d'écran, du code ou des cas existants : c'est le matériel de travail du modèle."],
    ),
    cards(
        K + "2.1.2", "Trois techniques de prompting",
        [("🔗", "Chaînage de prompts", "Découper une tâche en étapes, et vérifier chaque résultat avant de continuer."),
         ("🧩", "Few-shot", "Donner des exemples dans le prompt pour montrer le résultat attendu."),
         ("🪄", "Méta-prompting", "Laisser le modèle générer ou améliorer ses propres prompts.")],
        ["Passons à l'objectif deux point un point deux. Le syllabus retient trois techniques de base, à combiner avec la structure en six composants. "
         "{#c0}Le chaînage de prompts, ou prompt chaining. {#c1}Le few-shot, avec des exemples. {#c2}Et le méta-prompting. "
         "Voyons-les une par une, avec une démonstration à chaque fois."],
    ),
    flow(
        K + "2.1.2", "Technique 1 : le chaînage de prompts",
        [("🔍", "Prompt 1", "Repérer les ambiguïtés de la user story"),
         ("🧪", "Prompt 2", "Évaluer la testabilité des critères"),
         ("✅", "Prompt 3", "Vérifier la complétude des critères")],
        ["Le chaînage consiste à découper une tâche en une suite d'étapes intermédiaires, chacune avec son propre prompt. "
         "Prenons l'exemple d'un exercice du syllabus : améliorer les critères d'acceptation d'une user story. "
         "{#s0}Premier prompt : repérer les ambiguïtés. {#s1}Deuxième prompt : évaluer la testabilité. {#s2}Troisième prompt : vérifier la complétude. "
         "{#check}Et voici le point essentiel : entre deux étapes, le résultat est vérifié et corrigé, manuellement ou automatiquement, avant de continuer. "
         "Chaque réponse validée alimente le prompt suivant. {#trap}C'est ce qui rend le chaînage plus précis, et c'est la technique des tâches complexes."],
        check="✔ Vérification manuelle ou automatique entre chaque étape",
        trap="Chaînage = tâche **complexe**, découpée en étapes, avec **vérification** de chaque résultat intermédiaire.",
    ),
    versus(
        K + "2.1.2", "Un gros prompt ou une chaîne de prompts ?",
        ("Un seul gros prompt", ["Tout est demandé d'un coup", "Une erreur au début contamine toute la réponse", "Difficile de savoir où ça a déraillé"]),
        ("Le chaînage", ["Des sous-tâches simples", "Chaque sortie est contrôlée avant de continuer", "Les erreurs sont repérées tôt", "Des échanges dynamiques"]),
        ["Pourquoi ne pas tout demander d'un coup ? {#left}Avec un seul gros prompt, une erreur commise au début contamine toute la réponse, "
         "et on ne sait pas où le raisonnement a déraillé. {#right}Avec le chaînage, chaque sous-tâche est simple, chaque sortie est contrôlée, "
         "et les erreurs sont repérées tôt. Le syllabus ajoute que le chaînage permet des interactions dynamiques dans le processus de test."],
    ),
    cards(
        K + "2.1.2", "Technique 2 : zero-shot, one-shot, few-shot",
        [("0️⃣", "Zero-shot", "Aucun exemple : le modèle s'appuie sur ses connaissances existantes."),
         ("1️⃣", "One-shot", "Un seul exemple montre le résultat attendu pour une entrée donnée."),
         ("🔢", "Few-shot", "Plusieurs exemples consolident le comportement souhaité.")],
        ["Deuxième technique : donner des exemples dans le prompt. {#c0}Sans aucun exemple, on parle de zero-shot : le modèle s'appuie sur ses connaissances. "
         "{#c1}Avec un seul exemple, qui montre le résultat attendu pour une entrée donnée, c'est du one-shot. "
         "{#c2}Et avec plusieurs exemples, c'est du few-shot. Les exemples servent de référence : ils rendent les résultats cohérents et conformes aux attentes. "
         "{#trap}C'est particulièrement efficace quand des exemples peuvent illustrer le comportement voulu, par exemple un format imposé."],
        accent=2,
        trap="Le nombre d'exemples fait la différence : **0** = zero-shot, **1** = one-shot, **plusieurs** = few-shot.",
    ),
    code(
        K + "2.1.2", "Démonstration : few-shot en Gherkin",
        "Exemple 1 · US : « Ajouter un article au panier »\n  Scenario: Ajout d'un article disponible\n    Given un article en stock\n    When je clique sur « Ajouter »\n    Then le panier contient 1 article\n\n"
        "Exemple 2 · US : « Retirer un article du panier »\n  Scenario: Retrait du dernier article\n    Given un panier avec 1 article\n    When je clique sur « Retirer »\n    Then le panier est vide\n\n"
        "Nouvelle US : « Appliquer un code promo »\n  ➜ Rédige les scénarios sur le même modèle.",
        ["Voyons une démonstration, tirée d'un exercice du syllabus. {#code}Le prompt contient deux exemples complets : une user story, puis le scénario "
         "Gherkin correspondant, avec Given, When, Then. Ensuite, on donne une nouvelle user story : appliquer un code promo. "
         "{#note}Le modèle généralise à partir des exemples et produit des scénarios dans exactement le même style. "
         "Si le résultat n'est pas bon, on améliore les exemples ou le prompt."],
        note=("Pourquoi ça marche", "Les exemples servent de modèle : le format est respecté et les résultats restent cohérents.", "ok"),
    ),
    chat(
        K + "2.1.2", "Technique 3 : le méta-prompting",
        "Aide-moi à écrire le meilleur prompt pour analyser un rapport de tests de régression. Pose-moi d'abord les questions utiles.",
        "Avec plaisir. Pour construire le prompt :\n1. Sous quel format est votre rapport ?\n2. Quels indicateurs voulez-vous suivre ?\n3. Faut-il regrouper les échecs similaires ?\nJe vous proposerai ensuite un prompt complet, à ajuster ensemble.",
        [{"max": "Le problème, c'est que je ne sais même pas comment écrire mon prompt."},
         "Alors demandez au modèle de l'écrire avec vous, Max. C'est le méta-prompting : le modèle génère ou améliore ses propres prompts. "
         "{#type}Par exemple : aide-moi à écrire le meilleur prompt pour analyser un rapport de tests de régression. {#send}"
         "{#answer}Le modèle pose des questions, propose un prompt, et le testeur l'évalue et l'affine. On boucle jusqu'à obtenir un bon prompt. "
         "{#note}Deux avantages selon le syllabus : on réduit l'effort manuel, et on profite de ce que le modèle sait des prompts efficaces. "
         "Le syllabus parle d'une forme de pairing : le testeur et l'IA travaillent ensemble, comme en pair testing."],
        note=("Un vrai travail en binôme", "Le testeur et l'IA co-créent le prompt : moins d'effort, prompts optimisés.", "ok"),
    ),
    quiz(
        K + "Entraînement HO-2.1.2b",
        "« Étape 1 sur 3 : liste les ambiguïtés de cette user story. Je t'enverrai l'étape 2 après validation. » Quelle technique ?",
        ["Few-shot", "Chaînage de prompts", "Méta-prompting", "Zero-shot"], 1,
        "Le chaînage : la tâche est découpée en étapes, et chaque résultat est validé avant la suivante.",
        ["Entraînement à reconnaître les techniques. Étape un sur trois : liste les ambiguïtés de cette user story. Je t'enverrai l'étape deux après validation. Quelle technique ?"],
        ["{#rev}Le chaînage de prompts : une tâche découpée en étapes, avec une validation entre chaque étape."],
    ),
    quiz(
        K + "Entraînement HO-2.1.2b",
        "Le prompt contient un seul rapport de défaut complet comme modèle, puis demande d'en rédiger un nouveau. Quelle technique ?",
        ["One-shot", "Few-shot", "Méta-prompting", "Chaînage de prompts"], 0,
        "Un seul exemple : c'est du one-shot. Avec plusieurs exemples, ce serait du few-shot.",
        ["Et celle-ci : le prompt contient un seul rapport de défaut complet comme modèle, puis demande d'en rédiger un nouveau."],
        ["{#rev}Du one-shot ! Il n'y a qu'un seul exemple. Attention à ce piège : few-shot suppose plusieurs exemples."],
    ),
    versus(
        K + "2.1.3", "System prompt et user prompt",
        ("⚙️ System prompt", ["Défini par le développeur ou le testeur", "En général invisible et non modifiable par l'utilisateur du chatbot",
                              "Constant pendant toute la session", "Fixe comportement, personnalité, paramètres opérationnels"]),
        ("💬 User prompt", ["La demande de l'utilisateur", "Change à chaque échange", "Visible : c'est le contexte immédiat",
                            "Ciblé : instructions explicites, contexte utile, format de sortie"]),
        ["Dernier objectif de l'épisode : distinguer system prompt et user prompt. {#left}Le system prompt est défini par le développeur ou le testeur. "
         "Dans la plupart des interfaces, l'utilisateur du chatbot ne le voit pas et ne peut pas le modifier. Il reste constant pendant toute la session, "
         "et il fixe les règles : le comportement, la personnalité, et les paramètres opérationnels, comme un ton formel, des réponses concises, "
         "ou des règles propres au domaine. Il peut contenir le rôle, le contexte et les contraintes. "
         "{#right}Le user prompt, lui, c'est la demande de l'utilisateur. Il change à chaque échange, il est visible, et il forme le contexte immédiat de la réponse."],
    ),
    code(
        K + "2.1.3", "Démonstration : les deux prompts ensemble",
        "[SYSTEM — défini une fois]\nTu es un assistant professionnel de test logiciel. Réponds clairement,\nen langage formel, selon les pratiques ISTQB. Évite les spéculations.\n\n"
        "[USER — échange 1]\nListe les différences entre test boîte noire et test boîte blanche.\n\n"
        "[USER — échange 2]\nDonne un exemple de chaque pour un formulaire de paiement.",
        ["Voici comment cela se passe en pratique. {#code}Le system prompt est défini une seule fois, au début : tu es un assistant professionnel de test, "
         "réponds clairement, en langage formel, selon les pratiques ISTQB. Ensuite, l'utilisateur envoie ses demandes, les unes après les autres. "
         "{#note}Pour chaque réponse, le modèle tient compte des deux à la fois : le system prompt, qui ne change pas, et le user prompt du moment. "
         "Une image pour retenir : le règlement que le restaurant donne à son serveur, et la commande de chaque client."],
        note=("Le modèle combine les deux", "Le system prompt constant + le user prompt du moment = la réponse.", "ok"),
    ),
    quiz(
        K + "2.1.3",
        "Dans la plupart des interfaces de chatbot, qui définit le system prompt ?",
        ["L'utilisateur du chatbot, à chaque question", "Le développeur ou le testeur", "Le modèle lui-même, à chaque échange", "Personne : il n'existe que dans les API"], 1,
        "Le développeur ou le testeur : l'utilisateur du chatbot ne le voit pas et ne le modifie généralement pas.",
        ["Une dernière question avant le récapitulatif. Dans la plupart des interfaces de chatbot, qui définit le system prompt ?"],
        ["{#rev}Le développeur ou le testeur. L'utilisateur du chatbot, lui, ne le voit généralement pas et ne peut pas le modifier."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes de l'épisode 1",
        [("6 composants", "Rôle, contexte, instruction, données d'entrée, contraintes, format de sortie."),
         ("Contraintes ≠ format", "Les contraintes limitent ; le format décrit la présentation."),
         ("Chaînage", "Tâche complexe, découpée, avec vérification de chaque étape."),
         ("Zero, one, few-shot", "Zéro, un, ou plusieurs exemples dans le prompt."),
         ("Méta-prompting", "Le modèle co-crée ou améliore le prompt avec le testeur."),
         ("System vs user", "System : constant, défini par le développeur ou testeur. User : change à chaque échange.")],
        ["Récapitulons. {#r0}Un : les six composants d'un prompt structuré. {#r1}Deux : ne confondez pas contraintes et format de sortie. "
         "{#r2}Trois : le chaînage, pour les tâches complexes, avec une vérification à chaque étape. "
         "{#r3}Quatre : zéro, un ou plusieurs exemples, c'est zero-shot, one-shot ou few-shot. "
         "{#r4}Cinq : le méta-prompting, pour co-créer le prompt avec le modèle. "
         "{#r5}Et six : le system prompt est constant et défini par le développeur ou le testeur, le user prompt change à chaque échange."],
    ),
    title_scene(
        "À suivre · Épisode 2",
        "Analyser et concevoir les tests avec l'IA",
        "Conditions de test, critères d'acceptation, cas de test, données et scripts",
        ["Objectifs K3", "Démonstrations", "Scénarios d'examen"],
        ["Bravo, c'est la fin de ce premier épisode. {#sub}Dans le prochain, on passe à la pratique : l'analyse de test, "
         "puis la conception et l'implémentation des tests avec l'IA générative. {#chips}Ce sont des objectifs K trois, "
         "avec des scénarios comme à l'examen. D'ici là, faites les questions et les flashcards du chapitre deux dans l'application. À très vite !"],
    ),
]
