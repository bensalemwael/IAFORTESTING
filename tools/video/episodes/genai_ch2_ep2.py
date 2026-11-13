# CT-GenAI v1.1 · Chapitre 2 · Épisode 2 : analyser et concevoir les tests avec l'IA (sections 2.2, 2.2.1 et 2.2.2).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import cards, chat, code, flow, prompt_build, quiz, rows, table, title_scene

K = "CT-GenAI · Chapitre 2 · "

META = {
    "file": "genai-chapitre-2-episode-2",
    "title": "CT-GenAI · Chapitre 2 · Épisode 2 : analyser et concevoir les tests avec l'IA",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 2 · Épisode 2 sur 4",
        "Analyser et concevoir les tests avec l'IA",
        "Analyse de test, conception et implémentation : le prompting appliqué aux vraies tâches de test",
        ["Sections 2.2.1 et 2.2.2", "2 objectifs K3", "Environ 13 minutes"],
        ["Bonjour, et bienvenue dans ce deuxième épisode du chapitre deux. Dans le premier, on a appris à écrire un bon prompt. "
         "{#sub}Aujourd'hui, on l'applique à de vraies tâches de test : l'analyse de test, puis la conception et l'implémentation des tests. "
         "{#chips}Deux objectifs de niveau K trois : à l'examen, on vous décrira une situation, et vous devrez choisir quoi faire. "
         "Alors on va pratiquer, avec beaucoup d'exemples."],
    ),
    cards(
        K + "2.2", "Le prompting au service des tâches de test",
        [("🧰", "Des tâches de test", "Analyse, conception, automatisation, priorisation, détection de défauts, couverture, pilotage et contrôle."),
         ("🔗", "Des techniques combinées", "Chaînage, few-shot et méta-prompting, adaptés aux objectifs de test."),
         ("🎯", "Des résultats plus utiles", "Des sorties plus précises, plus pertinentes et plus efficaces."),
         ("💎", "Des entrées de qualité", "Une entrée de haute qualité est indispensable pour obtenir des résultats utiles.")],
        ["La section deux point deux part d'une idée simple. {#c0}L'IA générative peut soutenir de nombreuses tâches de test : "
         "l'analyse, la conception, l'automatisation, la priorisation des cas de test, la détection de défauts, l'analyse de couverture, "
         "et le pilotage et le contrôle des tests. {#c1}Pour cela, on utilise et on combine les techniques de l'épisode un : "
         "le chaînage, le few-shot et le méta-prompting, en les adaptant aux objectifs de test. "
         "{#c2}Résultat : des sorties plus précises, plus pertinentes et plus efficaces. "
         "{#c3}Mais une condition reste essentielle : des entrées de qualité."],
        cols=2,
    ),
    flow(
        K + "2.2.1", "Analyse de test : ce qui entre, ce qui sort",
        [("📥", "Entrées", "Exigences, user stories, spécifications techniques, wireframes d'IHM, autres informations utiles"),
         ("🤖", "Le LLM assiste", "Conditions de test générées et priorisées, défauts de la base de test, couverture"),
         ("📤", "Sorties", "Produits de l'analyse : conditions de test priorisées, par exemple des critères d'acceptation")],
        ["Commençons par l'analyse de test, objectif deux point deux point un. {#s0}En entrée, on donne au modèle la base de test : "
         "des exigences, des user stories, des spécifications techniques, des wireframes de l'interface graphique, et toute autre information utile. "
         "{#s1}Le modèle aide alors à générer et à prioriser des conditions de test, à repérer des défauts dans la base de test, et à analyser la couverture. "
         "{#s2}En sortie, on obtient les produits habituels de l'analyse : des conditions de test priorisées, par exemple des critères d'acceptation. "
         "{#check}Et retenez cette phrase du syllabus : la qualité et la pertinence des entrées, par rapport à la tâche, "
         "ont un impact direct sur l'exactitude et la précision du résultat."],
        check="✔ Qualité et pertinence des entrées = exactitude et précision des sorties",
    ),
    cards(
        K + "2.2.1", "Cinq tâches d'analyse soutenues par l'IA",
        [("🐞", "Défauts de la base de test", "Incohérences, ambiguïtés, informations incomplètes : le LLM les signale et suggère des améliorations."),
         ("🧾", "Conditions de test", "Décomposer exigences et user stories en énoncés mesurables et testables."),
         ("⚖️", "Priorisation par le risque", "Selon la probabilité et l'impact du risque de chaque condition de test."),
         ("🗺️", "Analyse de couverture", "Relier exigences et conditions de test pour trouver ce qui n'est pas couvert."),
         ("🛠️", "Techniques de test", "Suggérer valeurs limites, partitions d'équivalence… selon le type d'exigence.")],
        ["Le syllabus cite cinq tâches typiques. {#c0}Un : identifier des défauts potentiels dans la base de test, c'est-à-dire "
         "des incohérences, des ambiguïtés ou des informations incomplètes. Le modèle peut comparer des exigences de forme similaire, "
         "ou s'appuyer sur des rapports de défauts passés, pour signaler des anomalies et proposer des améliorations. "
         "{#c1}Deux : générer des conditions de test, en décomposant les exigences en énoncés mesurables et testables. "
         "{#c2}Trois : prioriser ces conditions selon le niveau de risque. {#c3}Quatre : soutenir l'analyse de couverture. "
         "{#c4}Et cinq : suggérer des techniques de test adaptées, comme l'analyse des valeurs limites ou les partitions d'équivalence."],
        cols=3,
    ),
    chat(
        K + "2.2.1", "Démo : les défauts de la base de test",
        "Tu es analyste de test. Repère ambiguïtés, incohérences et manques dans cette US : « Le patient peut annuler un rendez-vous rapidement, sauf exceptions. »",
        "1. Ambiguïté : « rapidement » n'est pas mesurable.\n2. Manque : quelles sont les « exceptions » ?\n3. Manque : jusqu'à quel délai avant le rendez-vous ?\n"
        "4. Manque : que voit le patient après l'annulation ?\nSuggestion : préciser le délai, lister les exceptions, décrire la confirmation.",
        ["Passons à la pratique, dans le domaine de la santé. {#type}On demande au modèle, dans le rôle d'un analyste de test, de repérer les ambiguïtés, "
         "les incohérences et les manques de cette user story : le patient peut annuler un rendez-vous rapidement, sauf exceptions. "
         "{#send}On envoie. {#answer}Le modèle relève que « rapidement » n'est pas mesurable, que les exceptions ne sont pas définies, "
         "et que le délai d'annulation manque. Puis il propose des améliorations. ",
         {"max": "Pratique ! Ces trous, je les découvrais d'habitude en pleine exécution."},
         "{#verdict}Exactement, Max : trouvés dès l'analyse, ces défauts coûtent bien moins cher. "
         "{#note}Mais le modèle signale des défauts potentiels. C'est au testeur de les confirmer, avec l'équipe et le métier."],
        verdict=("4 DÉFAUTS POTENTIELS", "good"),
        note=("Défauts potentiels", "Le LLM signale, le testeur confirme avec l'équipe et le métier.", "warn"),
    ),
    table(
        K + "2.2.1", "Prioriser les conditions de test par le risque",
        ["Condition de test", "Probabilité · Impact", "Priorité recommandée"],
        [("Paiement par carte refusé", "Élevée · Élevé", "Haute (fonction exposée)"),
         ("Consentement aux données enregistré", "Moyenne · Élevé", "Haute (conformité)"),
         ("Blocage après 3 connexions ratées", "Élevée · Moyen", "Haute (défauts passés)"),
         ("Tri des avis clients", "Faible · Faible", "Basse")],
        ["Troisième tâche : la priorisation. Pour aider à prioriser l'effort de test, le modèle a besoin d'informations "
         "sur la probabilité et sur l'impact d'une défaillance, pour chaque condition de test. "
         "{#r0}Le paiement par carte est une fonction exposée à l'utilisateur : priorité haute. "
         "{#r1}Le consentement aux données personnelles relève de la conformité réglementaire : haute aussi. "
         "{#r2}Le blocage de la connexion a un historique de défauts : on le remonte. "
         "{#r3}Et le tri des avis clients, à faible risque, reste en priorité basse. "
         "{#trap}Conformité réglementaire, fonctions exposées, historique des défauts : ce sont les aspects cités par le syllabus."],
        trap="Le LLM **recommande** des priorités à partir de la probabilité et de l'impact fournis pour chaque condition.",
    ),
    chat(
        K + "2.2.1", "Couverture et choix des techniques de test",
        "Voici 4 exigences (EX-1 à EX-4) et 6 conditions de test. Fais la matrice de couverture, signale les trous et suggère une technique de test par exigence.",
        "EX-1 Montant du virement → CT-1, CT-2 ✓ · Valeurs limites\nEX-2 Type de compte → CT-3 ✓ · Partitions d'équivalence\n"
        "EX-3 Double authentification → CT-4, CT-5, CT-6 ✓ · Table de décision\nEX-4 Historique des virements → aucune condition ✗\n"
        "À compléter : EX-4 n'est couverte par aucune condition de test.",
        ["Direction la banque, maintenant. {#type}On donne au modèle quatre exigences et six conditions de test, et on lui demande "
         "la matrice de couverture, les trous, et une technique de test par exigence. {#send}On envoie. "
         "{#answer}Il relie chaque exigence à ses conditions, propose les valeurs limites pour le montant, les partitions d'équivalence "
         "pour le type de compte, et signale que l'exigence quatre n'est couverte par aucune condition. {#verdict}Trou détecté. "
         "{#note}C'est précieux sur les projets aux exigences complexes, où un trou de couverture peut laisser s'échapper des défauts."],
        verdict=("1 TROU DÉTECTÉ", "good"),
        note=("Pourquoi c'est utile", "Sur des exigences complexes, un trou de couverture peut laisser s'échapper des défauts.", "ok"),
    ),
    quiz(
        K + "Entraînement 2.2.1",
        "Un LLM compare de nouvelles exigences aux rapports de défauts des projets passés pour signaler des anomalies. Quelle tâche ?",
        ["Identifier des défauts potentiels dans la base de test", "Prioriser les conditions de test par le risque",
         "Soutenir l'analyse de couverture", "Suggérer des techniques de test"], 0,
        "On analyse les exigences elles-mêmes pour y signaler des anomalies : ce sont des défauts de la base de test.",
        ["À vous. Une équipe d'assurance fournit au modèle ses nouvelles exigences, avec les rapports de défauts des projets précédents, "
         "pour signaler des anomalies avant la conception. Quelle tâche d'analyse est soutenue ?"],
        ["{#rev}Identifier des défauts potentiels dans la base de test. Attention au piège : l'historique des défauts sert aussi à prioriser. "
         "Mais ici, le but est de signaler des anomalies dans les exigences elles-mêmes."],
    ),
    prompt_build(
        K + "HO-2.2.1a", "Un prompt multimodal : texte et maquette",
        [("Rôle", "Tu es analyste de test pour un transporteur."),
         ("Contexte", "Appli web de prise de rendez-vous de livraison."),
         ("Instruction", "Rédige les critères d'acceptation de la user story."),
         ("Données : texte", "US-17 : « Je veux choisir mon créneau de livraison. »"),
         ("Données : image", "[maquette jointe : ecran_creneau.png]"),
         ("Contraintes", "Code postal : 5 chiffres. Créneaux de 2 h, J+1 à J+14."),
         ("Format de sortie", "Liste numérotée de critères clairs et vérifiables.")],
        ["Premier exercice pratique, le deux point deux point un a. Objectif : produire des critères d'acceptation de haute qualité, "
         "c'est-à-dire bien formés, clairs et complets, à partir d'une user story et d'une maquette d'écran. "
         "{#l0}Le rôle. {#l1}Le contexte : une application de prise de rendez-vous de livraison. {#l2}L'instruction. "
         "{#l3}Les données d'entrée textuelles : la user story. {#l4}Et des données d'entrée en image : le wireframe de l'écran. "
         "{#l5}On peut ajouter d'autres éléments de texte, comme des contraintes sur les champs de saisie ou des règles métier. "
         "{#l6}Enfin, le format de sortie. {#badge}Du texte et une image ensemble : c'est un prompt multimodal."],
        badge=("2", "types d'entrée : texte et image"),
    ),
    chat(
        K + "HO-2.2.1a", "Avec ou sans la maquette ?",
        "[Prompt structuré complet + maquette ecran_creneau.png] Rédige les critères d'acceptation de l'US-17.",
        "CA1 Le code postal accepte exactement 5 chiffres.\nCA2 Seuls les créneaux de J+1 à J+14 sont proposés.\nCA3 Un créneau complet apparaît grisé et non cliquable.\n"
        "CA4 « Confirmer » reste inactif tant qu'aucun créneau n'est choisi.\nCA5 Un récapitulatif s'affiche après la confirmation.",
        ["{#type}On envoie le prompt complet, avec la maquette jointe. {#send}"
         "{#answer}Les critères reprennent les contraintes du texte, comme les cinq chiffres du code postal, mais aussi des éléments "
         "visibles seulement sur la maquette : le créneau grisé, le bouton Confirmer inactif, le récapitulatif. ",
         {"max": "Et sans l'image, j'aurais obtenu quoi ?"},
         "C'est justement l'exercice, Max. {#note}On compare les résultats de plusieurs formulations du prompt structuré : avec ou sans image, "
         "avec ou sans contraintes, avec une instruction plus ou moins précise. On mesure ainsi l'apport de chaque composant, "
         "et l'importance des données de contexte, textuelles comme visuelles."],
        note=("Ce que montre l'exercice", "Structure, instruction précise, texte et image : chaque élément améliore le résultat.", "ok"),
    ),
    quiz(
        K + "Entraînement HO-2.2.1a",
        "Les critères générés pour un écran de paiement ignorent le champ « cryptogramme » visible sur la maquette, non jointe au prompt. Que faire d'abord ?",
        ["Joindre la maquette au prompt comme donnée d'entrée", "Demander au LLM d'être plus créatif",
         "Ajouter « sois exhaustif » à l'instruction", "Passer au méta-prompting"], 0,
        "L'information manque dans les entrées : on joint l'image. La qualité des entrées fait celle de la sortie.",
        ["Scénario d'examen. Les critères d'acceptation générés pour un écran de paiement ignorent le champ cryptogramme, "
         "pourtant visible sur la maquette. Mais la maquette n'a pas été jointe au prompt. Que faites-vous d'abord ?"],
        ["{#rev}On joint la maquette comme donnée d'entrée. Le modèle ne peut pas deviner ce qu'il n'a pas vu. "
         "Demander plus d'exhaustivité ne remplace pas une information manquante."],
    ),
    flow(
        K + "HO-2.2.1b", "Chaîner l'analyse d'une user story",
        [("🔍", "Étape 1 · Ambiguïtés", "Repérer les formulations floues ou interprétables"),
         ("🧪", "Étape 2 · Testabilité", "Chaque critère peut-il être vérifié par un test ?"),
         ("✅", "Étape 3 · Complétude", "Rien ne manque pour atteindre les objectifs de test ?")],
        ["Deuxième exercice, le deux point deux point un b : le chaînage de prompts, avec vérification humaine. "
         "On analyse une user story, et on affine ses critères d'acceptation, pas à pas. "
         "{#s0}Étape un : identifier les ambiguïtés. {#s1}Étape deux : évaluer la testabilité. {#s2}Étape trois : évaluer la complétude. "
         "{#check}À chaque étape, le testeur vérifie le résultat du modèle et le corrige si nécessaire, soit en ajustant lui-même la sortie, "
         "soit en poursuivant la chaîne avec le modèle. {#trap}Ainsi, chaque étape part d'un résultat propre."],
        check="👤 À chaque étape : vérification humaine, correction, puis résultat propre transmis",
        trap="L'ordre de l'exercice : **ambiguïtés**, puis **testabilité**, puis **complétude**, avec vérification humaine entre les étapes.",
    ),
    chat(
        K + "HO-2.2.1b", "Étape 2 : évaluer la testabilité",
        "Étape 2. Voici les critères corrigés après l'étape 1. Pour chacun : est-il testable ? Sinon, explique pourquoi et propose une reformulation.",
        "CA1 Annulation possible jusqu'à 24 h avant le rendez-vous : testable ✓\nCA2 « L'interface est agréable » : non testable ✗\n"
        "→ Proposition : « l'annulation se fait en 2 clics maximum »\nCA3 Un SMS de confirmation est envoyé : testable ✓\n"
        "CA4 « Le système reste fiable » : non testable ✗ → à préciser",
        ["Voici l'étape deux, dans notre application de rendez-vous médicaux. {#type}On envoie les critères corrigés après l'étape un, "
         "et on demande, pour chacun, s'il est testable. {#send}On envoie. "
         "{#answer}Le modèle valide deux critères, signale deux critères non testables, et propose une reformulation mesurable. "
         "{#note}Mais cette reformulation convient-elle au métier ? C'est au testeur d'en juger, et de la corriger avant l'étape trois. "
         "C'est tout l'intérêt de l'exercice : découper une tâche complexe en sous-tâches, avec une vérification humaine à chaque étape."],
        note=("Avant l'étape 3", "Le testeur valide ou corrige chaque reformulation : l'étape suivante part d'un résultat propre.", "ok"),
    ),
    quiz(
        K + "Entraînement HO-2.2.1b",
        "À l'étape 2 d'une chaîne, le LLM juge testable le critère « le virement est sécurisé ». Que faire avant l'étape 3 ?",
        ["Corriger ce résultat, puis lancer l'étape 3", "Lancer l'étape 3, qui corrigera l'erreur",
         "Tout refaire en un seul prompt", "Garder ce critère tel quel"], 0,
        "Chaque résultat intermédiaire est vérifié et corrigé : l'étape suivante doit partir d'un résultat propre.",
        ["Nouveau scénario. À l'étape deux d'une chaîne, le modèle juge testable le critère : le virement est sécurisé. "
         "Que faites-vous avant l'étape trois ?"],
        ["{#rev}On corrige ce résultat d'abord, soi-même ou en relançant le modèle. "
         "Si on le laisse passer, l'erreur se propage dans toute la suite de la chaîne."],
    ),
    cards(
        K + "2.2.2", "Conception et implémentation : quatre tâches",
        [("🧪", "Génération de cas de test", "Préconditions, entrées, résultats attendus, critères de couverture : du fonctionnel simple au bout en bout."),
         ("🧬", "Données de test synthétiques", "Représentatives, proches de la production, sans exposer de données sensibles."),
         ("📜", "Génération de scripts", "Procédures manuelles et scripts automatisés, compatibles avec divers frameworks."),
         ("📅", "Planification de l'exécution", "Ordonnancement selon priorité, risques, ressources disponibles et objectifs de test.")],
        ["Objectif deux point deux point deux : la conception et l'implémentation des tests. La conception transforme les conditions de test "
         "en cas de test et en d'autres éléments du testware ; l'implémentation crée ou acquiert le testware nécessaire. "
         "L'IA aide à créer et à évaluer ce testware : cas de test, données, scripts et environnements de test. "
         "{#c0}Première tâche : générer des brouillons de cas de test, à partir d'exigences fonctionnelles et non fonctionnelles. "
         "{#c1}Deuxième : synthétiser des données de test. {#c2}Troisième : générer des scripts de test. "
         "{#c3}Quatrième : planifier et prioriser l'exécution. Le modèle analyse les cas de test et leurs interdépendances, "
         "et optimise le calendrier selon la priorité, les risques, les ressources disponibles et les objectifs de test."],
        cols=2,
    ),
    code(
        K + "2.2.2", "Démo : des données de test synthétiques",
        "Prompt : génère 5 clients fictifs pour tester le virement instantané.\n"
        "Contraintes : aucune donnée réelle, couvre les situations extrêmes.\n\n"
        "id | nom                    | solde (€)  | plafond | remarque\n"
        "C1 | Léa Martin             |   2 450,00 |   1 000 | cas nominal\n"
        "C2 | Yanis Fabre            |       0,00 |   1 000 | solde nul\n"
        "C3 | Zoé Ndiaye-Lopez-Garcia| 999 999,99 |   1 000 | nom long, solde max\n"
        "C4 | Hugo Petit             |    -150,00 |     500 | découvert\n"
        "C5 | Inès Roy               |   1 000,00 |   1 000 | solde = plafond\n\n"
        "IBAN : format valide, comptes fictifs uniquement.",
        ["Démonstration, toujours en banque. {#code}On demande cinq clients fictifs pour tester le virement instantané, "
         "sans aucune donnée réelle, en couvrant les situations extrêmes. Le modèle produit un cas nominal, un solde nul, "
         "un nom très long avec un solde maximal, un découvert, et un solde exactement égal au plafond. "
         "{#note}C'est la synthèse de données de test : des données représentatives, qui ressemblent à la production, "
         "mais qui protègent la vie privée. Elles s'adaptent aux exigences de l'application, et servent aux tests fonctionnels comme non fonctionnels."],
        note=("Synthèse de données", "Réalistes, variées, sans exposer d'informations sensibles. Fonctionnel et non fonctionnel.", "ok"),
    ),
    code(
        K + "2.2.2", "Du cas de test structuré au script",
        "# Cas de test TC-08 : code promo dans le panier\n"
        "# Préconditions : client connecté, panier de 80,00 €\n"
        "# Étapes : saisir PROMO10, puis valider\n"
        "# Résultat attendu : total = 72,00 €\n\n"
        "test('TC-08 code promo valide', async ({ page }) => {\n"
        "  await page.goto('/panier');\n"
        "  await page.getByLabel('Code promo').fill('PROMO10');\n"
        "  await page.getByRole('button', { name: 'Valider' }).click();\n"
        "  await expect(page.getByTestId('total')).toHaveText('72,00 €');\n"
        "});",
        ["Troisième tâche : la génération de scripts. {#code}On part d'un cas de test structuré : un code promo de dix pour cent, "
         "dans un panier de quatre-vingts euros. Le modèle interprète les étapes, et les traduit en code compatible "
         "avec le framework d'automatisation de l'équipe. {#note}Il peut aussi produire des procédures de test manuelles. "
         "Et quand une nouvelle exigence arrive, le script peut être mis à jour ou étendu. "
         "Bien sûr, un script généré se relit et s'exécute avant d'être adopté."],
        note=("Procédures et scripts", "Manuels ou automatisés, mis à jour ou étendus quand les exigences évoluent.", "ok"),
    ),
    flow(
        K + "HO-2.2.2a", "Trois techniques pour générer des cas de test",
        [("📐", "1 · Prompt structuré", "Cas de test fonctionnels issus des critères d'acceptation, dans un format imposé"),
         ("📊", "2 · Vérifier la complétude", "Le LLM produit un tableau : chaque critère est-il couvert ?"),
         ("🪄", "3 · Méta-prompt", "Construire et affiner le prompt des tests de bout en bout")],
        ["Exercice deux point deux point deux a : générer des cas de test fonctionnels à partir de user stories, "
         "en combinant chaînage, prompts structurés et méta-prompting. {#s0}Première étape : un prompt demande des cas de test fonctionnels, "
         "à partir des critères d'acceptation, dans un format de sortie précis. {#s1}Deuxième étape : vérifier la complétude. "
         "Le modèle produit un tableau qui montre, pour chaque critère d'acceptation, s'il est couvert. "
         "{#s2}Troisième étape : un méta-prompt, pour aider à créer des procédures de test de bout en bout. "
         "{#loop}On affine ce prompt par itérations successives, pour des tests de bout en bout complets."],
        loop=True,
    ),
    chat(
        K + "HO-2.2.2a", "Démo : le méta-prompt de bout en bout",
        "Je veux un prompt qui génère des procédures de test de bout en bout pour le parcours commande, paiement, livraison. Pose-moi d'abord tes questions.",
        "Pour construire ce prompt, j'ai besoin de savoir :\n1. Quels moyens de paiement et quels transporteurs inclure ?\n"
        "2. Faut-il couvrir les retours et les remboursements ?\n3. Quel format : étapes numérotées ou tableau ?\n"
        "Proposition : « Tu es testeur e-commerce. Rédige des procédures… »",
        ["Troisième étape, en e-commerce. {#type}Je veux un prompt qui génère des procédures de test de bout en bout pour le parcours "
         "commande, paiement, livraison. Pose-moi d'abord tes questions. {#send}"
         "{#answer}Le modèle demande quels moyens de paiement inclure, s'il faut couvrir les retours, quel format adopter, puis propose un premier prompt. "
         "{#note}Le testeur l'utilise, examine les cas produits, et revient vers le modèle pour l'améliorer. "
         "On itère ainsi jusqu'à obtenir des tests de bout en bout vraiment complets."],
        note=("Itérer", "Le testeur évalue chaque version du prompt, et l'affine avec le modèle.", "ok"),
    ),
    prompt_build(
        K + "HO-2.2.2b", "Few-shot : des scénarios Gherkin en série",
        [("Ex. 1 · User story", "Je veux suivre mon colis en temps réel."),
         ("Ex. 1 · Conditions", "Colis en transit ; colis livré ; numéro inconnu."),
         ("Ex. 1 · Gherkin", "Given un colis en transit When je saisis… Then…"),
         ("Ex. 2 · User story", "Je veux changer l'adresse de livraison."),
         ("Ex. 2 · Conditions", "Colis pas encore expédié ; colis déjà expédié."),
         ("Ex. 2 · Gherkin", "Given un colis non expédié When je modifie… Then…"),
         ("Nouvelle US", "Je veux choisir un point relais."),
         ("Instruction", "Écris conditions et scénarios Gherkin sur ce modèle.")],
        ["Exercice deux point deux point deux b : le few-shot, pour produire des conditions de test et des cas de test en style Gherkin. "
         "On commence par revoir des exemples prédéfinis et la syntaxe Gherkin, puis on choisit n exemples à inclure dans le prompt. "
         "{#l0}Chaque exemple contient une user story, {#l1}ses conditions de test, {#l2}et les cas de test attendus, en Given, When, Then. "
         "{#l3}Deuxième exemple, {#l4}avec ses conditions {#l5}et ses scénarios. {#l6}Puis on applique le prompt à une nouvelle user story : "
         "choisir un point relais. {#l7}Le modèle produit des scénarios Gherkin qui reprennent la logique des exemples. "
         "{#badge}Et si le résultat est inexact, on affine le prompt, ou les exemples."],
        badge=("n = 2", "exemples complets"),
    ),
    quiz(
        K + "Entraînement HO-2.2.2b",
        "Avec 3 exemples few-shot, les scénarios Gherkin générés oublient les cas d'erreur. Aucun exemple n'en contient. Que faire ?",
        ["Ajouter des cas d'erreur dans les exemples", "Passer en zero-shot",
         "Retirer les conditions de test des exemples", "Corriger à la main chaque sortie"], 0,
        "Le modèle imite ses exemples : s'ils n'ont pas de cas d'erreur, la sortie non plus. On affine les exemples.",
        ["Scénario. Avec trois exemples few-shot, les scénarios Gherkin générés pour une nouvelle user story oublient les cas d'erreur. "
         "En relisant, vous constatez qu'aucun exemple n'en contient. Que faites-vous ?"],
        ["{#rev}On affine les exemples, en y ajoutant des cas d'erreur. Le modèle généralise à partir de ce qu'on lui montre : "
         "la qualité des exemples fait la qualité du résultat."],
    ),
    chat(
        K + "HO-2.2.2c", "Prioriser une suite de tests",
        "Étape 2. Selon les risques et les dépendances validés à l'étape 1, propose l'ordre d'exécution des 6 cas de test (approche basée sur les risques).",
        "1. TC-5 Paiement 3-D Secure (risque élevé)\n2. TC-2 Création du compte client\n3. TC-6 Remboursement (risque élevé)\n"
        "4. TC-1 Connexion\n5. TC-3 Ajout au panier\n6. TC-4 Recherche de produit",
        ["Dernier exercice, le deux point deux point deux c : prioriser une suite de tests par chaînage. On revoit d'abord plusieurs approches, "
         "basées sur les risques, sur la couverture ou sur les exigences, puis on fait générer des plans de priorisation exploitables. "
         "{#type}Ici, à l'étape deux, on demande l'ordre d'exécution. {#send}"
         "{#answer}Le modèle place le paiement en premier, car son risque est élevé. ",
         {"max": "Attends… le paiement passe avant la création du compte ?"},
         "{#verdict}Bien vu, Max. Le paiement dépend du compte et de la connexion : le modèle a ignoré une dépendance. "
         "{#note}Voilà pourquoi on vérifie manuellement son raisonnement : risques et dépendances à la fois, c'est un raisonnement multicritère."],
        verdict=("DÉPENDANCE IGNORÉE", "bad"),
        note=("Vérification manuelle", "Risques + dépendances = raisonnement multicritère : on contrôle la logique du LLM.", "warn"),
    ),
    quiz(
        K + "Entraînement HO-2.2.2c",
        "Un LLM ordonne une suite bancaire par risque, mais place la clôture de compte avant l'ouverture de compte. Que faire ?",
        ["Corriger l'ordre et expliciter les dépendances", "Accepter : le risque prime toujours",
         "Supprimer le test d'ouverture de compte", "Relancer le prompt jusqu'à un autre ordre"], 0,
        "La vérification manuelle révèle l'erreur de raisonnement : on corrige et on précise les dépendances.",
        ["Dernier scénario. Un modèle ordonne une suite de tests bancaires par niveau de risque, mais place la clôture de compte "
         "avant l'ouverture de compte. Que faites-vous ?"],
        ["{#rev}On corrige l'ordre, et on explicite les dépendances dans les entrées de la chaîne. "
         "Relancer au hasard ne garantit rien : c'est la vérification humaine qui détecte l'erreur de raisonnement."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes de l'épisode 2",
        [("Entrées de qualité", "Exigences, user stories, maquettes : leur qualité fait celle des sorties."),
         ("5 tâches d'analyse", "Défauts de la base de test, conditions, priorisation par le risque, couverture, techniques."),
         ("Multimodal", "User story + maquette + contraintes : des critères d'acceptation plus complets."),
         ("Chaînage vérifié", "Ambiguïtés, testabilité, complétude : chaque étape validée par un humain."),
         ("4 tâches de conception", "Cas de test, données synthétiques, scripts, planification de l'exécution."),
         ("Few-shot et priorisation", "Gherkin par l'exemple ; priorités et dépendances toujours vérifiées.")],
        ["Récapitulons. {#r0}Un : la qualité des entrées fait la qualité des sorties. "
         "{#r1}Deux : cinq tâches d'analyse, des défauts de la base de test jusqu'au choix des techniques. "
         "{#r2}Trois : un prompt multimodal, avec la maquette, donne des critères d'acceptation plus complets. "
         "{#r3}Quatre : le chaînage, ambiguïtés, testabilité, complétude, avec une vérification humaine à chaque étape. "
         "{#r4}Cinq : quatre tâches de conception et d'implémentation. "
         "{#r5}Et six : le few-shot pour le Gherkin, et une priorisation dont on vérifie toujours le raisonnement."],
    ),
    title_scene(
        "À suivre · Épisode 3",
        "Automatiser la régression et piloter les tests",
        "Régression automatisée, pilotage et contrôle, et choix de la bonne technique de prompting",
        ["Objectifs K3", "Démonstrations", "Scénarios d'examen"],
        ["Bravo, c'est la fin de ce deuxième épisode. {#sub}Dans le prochain, on automatise la régression avec l'IA générative, "
         "on pilote et on contrôle les tests, et surtout, on apprend à choisir la bonne technique de prompting pour chaque situation. "
         "{#chips}Encore des objectifs K trois, avec des scénarios comme à l'examen. D'ici là, entraînez-vous dans l'application. À très vite !"],
    ),
]
