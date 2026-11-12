# Contenu de la vidéo : CT-GenAI v1.1, chapitre 2 (prompt engineering). Synthèse originale des sections 2.1 à 2.3.
# Étapes : "say" = voix principale, "voice": "max" = Max le testeur, "pause" = étape muette, "vars" = variables.

CHAPTER = "CT-GenAI v1.1 · Chapitre 2"

COUNTDOWN = [{"pause": 1.0, "vars": {"count": "3"}}, {"pause": 1.0, "vars": {"count": "2"}}, {"pause": 1.0, "vars": {"count": "1"}}]


def countdown():
    return [dict(step) for step in COUNTDOWN]


SLIDES = [
    {
        "section": "", "title": "",
        "body": """
<div class="hero">
  <p class="kicker">ISTQB® CT-GenAI v1.1 — Chapitre 2</p>
  <h1>Le prompt engineering<br>pour tester mieux</h1>
  <p class="lead" data-s="1">Un prompt flou donne un résultat flou.</p>
  <div class="chips" data-s="2"><span>365 minutes : le plus long chapitre</span><span>10 objectifs</span><span>5 objectifs K3</span></div>
</div>""",
        "steps": [
            {"say": "Bienvenue dans le chapitre deux, le cœur du syllabus : le prompt engineering appliqué au test."},
            {"say": "Une idée à garder en tête pendant toute la vidéo : un prompt flou donne un résultat flou."},
            {"say": "C'est le chapitre le plus long, trois cent soixante-cinq minutes, avec cinq objectifs K trois. On y va !"},
        ],
    },
    {
        "section": "Plan", "title": "Trois blocs à maîtriser",
        "body": """
<div class="cards3">
  <div class="c" data-s="0"><div class="ic">✍️</div><h3>2.1 Écrire de bons prompts</h3><p>Structure en 6 composants, 3 techniques, system prompt et user prompt</p><p><b class="k2">K2</b> comprendre</p></div>
  <div class="c" data-s="1"><div class="ic">🧪</div><h3>2.2 Les appliquer au test</h3><p>Analyse, conception, régression, pilotage, choix de la technique</p><p><b class="k2" style="background:#b3261e">K3</b> appliquer</p></div>
  <div class="c" data-s="2"><div class="ic">📏</div><h3>2.3 Évaluer et améliorer</h3><p>Métriques de qualité et techniques pour affiner les prompts</p><p><b class="k2">K2</b> comprendre</p></div>
</div>
<div class="trap" data-s="3"><b>K3 à l'examen :</b> des scénarios concrets. Il faut savoir quoi faire, pas seulement réciter.</div>""",
        "steps": [
            {"say": "Premier bloc : écrire de bons prompts. Niveau K deux."},
            {"say": "Deuxième bloc : les appliquer aux vraies tâches de test. Là, c'est du K trois : appliquer."},
            {"say": "Troisième bloc : évaluer les résultats et améliorer ses prompts."},
            {"say": "Attention : les questions K trois sont des scénarios. On vous décrit une situation, vous choisissez la bonne action."},
        ],
    },
    {
        "section": "2.1", "title": "Pourquoi structurer son prompt ?",
        "body": """
<div class="vs">
  <div class="box warn" data-s="0"><h3>Prompt flou</h3><div class="code">Écris des tests pour la page de connexion.</div><p data-s="1">➜ Réponse générique : « tester un login valide, un login invalide… »</p></div>
  <div class="mid">VS</div>
  <div class="box ok" data-s="3"><h3>Prompt structuré</h3><div class="code">Rôle, contexte, instruction,
données d'entrée, contraintes,
format de sortie</div><p>➜ Réponse <b>précise</b>, <b>adaptée</b>, <b>exploitable</b></p></div>
</div>
<div class="bubble" data-s="2"><span class="speaker">Max</span>« J'ai demandé des tests à l'IA… et j'ai eu des banalités. »</div>""",
        "steps": [
            {"say": "Regardez ce prompt : écris des tests pour la page de connexion."},
            {"say": "Le modèle ne sait rien de votre application. Il répond donc avec des généralités."},
            {"say": "J'ai demandé des tests à l'IA, et j'ai eu des banalités !", "voice": "max"},
            {"say": "Normal, Max. Le syllabus recommande un prompt structuré. Chaque composant ajoute de la clarté et de la précision."},
        ],
    },
    {
        "section": "2.1.1", "title": "Les 6 composants d'un prompt structuré",
        "body": """
<div class="comp">
  <div class="c" data-s="0"><h3>1. Rôle</h3><p>La <b>persona</b> à adopter : testeur, test manager, ingénieur en automatisation</p></div>
  <div class="c" data-s="1"><h3>2. Contexte</h3><p>Le <b>contexte</b> : l'objet de test, la fonctionnalité à tester</p></div>
  <div class="c" data-s="2"><h3>3. Instruction</h3><p>La <b>tâche</b> : claire, à l'impératif, concise</p></div>
  <div class="c" data-s="3"><h3>4. Données d'entrée</h3><p>User stories, critères d'acceptation, captures, code, cas existants, exemples de sortie</p></div>
  <div class="c" data-s="4"><h3>5. Contraintes</h3><p>Les <b>restrictions</b> : comment appliquer l'instruction aux données</p></div>
  <div class="c" data-s="5"><h3>6. Format de sortie</h3><p>La <b>forme</b> attendue : tableau, Gherkin, JSON, liste…</p></div>
</div>
<p class="note" data-s="6">💡 Comme un brief à un prestataire : qui il est, la situation, la mission, les documents, les règles et le livrable.</p>""",
        "steps": [
            {"say": "Un : le rôle. On dit au modèle quel point de vue adopter, par exemple testeur ou ingénieur en automatisation."},
            {"say": "Deux : le contexte. Les informations de fond : l'objet de test, la fonctionnalité visée."},
            {"say": "Trois : l'instruction. La tâche à faire, formulée clairement, à l'impératif, en peu de mots."},
            {"say": "Quatre : les données d'entrée. Une user story, des critères d'acceptation, une capture d'écran, du code, des cas de test existants ou des exemples de sortie."},
            {"say": "Cinq : les contraintes. Les restrictions à respecter, c'est-à-dire comment appliquer l'instruction aux données."},
            {"say": "Six : le format de sortie. La forme attendue, par exemple un tableau."},
            {"say": "Pour retenir : c'est le brief qu'on donnerait à un prestataire. Qui il est, la situation, la mission, les documents, les règles et le livrable."},
        ],
    },
    {
        "section": "2.1.1", "title": "Un prompt structuré, pièce par pièce",
        "body": """
<div class="prompt-card">
  <div data-s="0"><span class="lbl l1">Rôle</span>Tu es un testeur expert en applications bancaires.</div>
  <div data-s="1"><span class="lbl l2">Contexte</span>Nous testons le virement instantané de l'appli mobile.</div>
  <div data-s="2"><span class="lbl l3">Instruction</span>Rédige les cas de test fonctionnels de la user story ci-dessous.</div>
  <div data-s="3"><span class="lbl l4">Données d'entrée</span>US-42 : « En tant que client, je veux virer jusqu'à 1 000 € … »</div>
  <div data-s="4"><span class="lbl l5">Contraintes</span>Couvre les valeurs limites du montant. Pas plus de 12 cas.</div>
  <div data-s="5"><span class="lbl l6">Format de sortie</span>Tableau : ID | Préconditions | Étapes | Résultat attendu</div>
</div>""",
        "steps": [
            {"say": "Voyons un vrai exemple. Le rôle : tu es un testeur expert en applications bancaires."},
            {"say": "Le contexte : nous testons le virement instantané de l'application mobile."},
            {"say": "L'instruction : rédige les cas de test fonctionnels de la user story."},
            {"say": "Les données d'entrée : la user story elle-même."},
            {"say": "Les contraintes : couvrir les valeurs limites du montant, et pas plus de douze cas."},
            {"say": "Et le format de sortie : un tableau avec identifiant, préconditions, étapes et résultat attendu."},
        ],
    },
    {
        "section": "Quiz éclair", "title": "Quel composant ?",
        "body": """
<div class="qa">
  <p class="q" data-s="0">« Limite-toi aux cas négatifs. »</p>
  <div class="answer" data-s="4">➜ <b>Contraintes</b> : une restriction sur la façon d'appliquer l'instruction.</div>
  <p class="q" data-s="5">« Réponds sous forme de scénarios Given / When / Then. »</p>
  <div class="answer" data-s="9">➜ <b>Format de sortie</b> : la forme du résultat attendu.</div>
</div>""",
        "steps": [
            {"say": "Quiz éclair ! Limite-toi aux cas négatifs : de quel composant s'agit-il ?"},
            *countdown(),
            {"say": "Les contraintes ! C'est une restriction sur la façon d'appliquer l'instruction."},
            {"say": "Et celle-ci : réponds sous forme de scénarios Given, When, Then."},
            *countdown(),
            {"say": "Le format de sortie : on décrit la forme du résultat."},
        ],
    },
    {
        "section": "2.1.2", "title": "Trois techniques de prompting",
        "body": """
<div class="cards3">
  <div class="c" data-s="0"><div class="ic">🔗</div><h3>Chaînage de prompts</h3><p><i>Prompt chaining</i> : découper la tâche en étapes, vérifier chaque résultat</p></div>
  <div class="c" data-s="1"><div class="ic">🧩</div><h3>Few-shot</h3><p>Donner des <b>exemples</b> dans le prompt</p></div>
  <div class="c" data-s="2"><div class="ic">🪄</div><h3>Méta-prompting</h3><p>Le modèle <b>génère ou améliore</b> ses propres prompts</p></div>
</div>
<p class="note" data-s="3">Elles s'utilisent <b>avec</b> la structure en 6 composants… et peuvent se <b>combiner</b>.</p>""",
        "steps": [
            {"say": "Section deux point un point deux : trois techniques de base. La première : le chaînage de prompts."},
            {"say": "La deuxième : le few-shot, avec des exemples."},
            {"say": "La troisième : le méta-prompting."},
            {"say": "On les utilise avec la structure en six composants, et on peut les combiner. Voyons-les une par une."},
        ],
    },
    {
        "section": "2.1.2", "title": "Le chaînage de prompts",
        "body": """
<div class="flow">
  <div class="st" data-s="1"><b>Prompt 1</b>Repérer les ambiguïtés</div><div class="ar">➜</div>
  <div class="st" data-s="2"><b>Prompt 2</b>Évaluer la testabilité</div><div class="ar">➜</div>
  <div class="st" data-s="3"><b>Prompt 3</b>Vérifier la complétude</div>
</div>
<div class="chk" data-s="4" style="font-size:30px;text-align:center;color:#17794a;font-weight:700">✅ Vérification manuelle ou automatique entre chaque étape</div>
<div class="split" data-s="5">
  <div class="box ok"><h3>Avantage</h3><p>Plus de <b>précision</b> : chaque réponse alimente le prompt suivant.</p></div>
  <div class="box"><h3>Idéal pour</h3><p>Les tâches <b>complexes</b>, à découper en sous-tâches, avec <b>contrôle</b> des résultats intermédiaires.</p></div>
</div>""",
        "steps": [
            {"say": "Le chaînage de prompts, c'est découper une tâche en une suite d'étapes, chacune avec son propre prompt."},
            {"say": "Exemple tiré des exercices du syllabus, pour améliorer des critères d'acceptation. Étape un : repérer les ambiguïtés."},
            {"say": "Étape deux : évaluer la testabilité."},
            {"say": "Étape trois : vérifier la complétude."},
            {"say": "Le point clé : entre chaque étape, on vérifie et on corrige le résultat, à la main ou automatiquement, avant de continuer."},
            {"say": "Résultat : plus de précision, car chaque réponse nourrit la suivante. C'est la technique des tâches complexes."},
        ],
    },
    {
        "section": "2.1.2", "title": "Zero-shot, one-shot, few-shot",
        "body": """
<div class="shots">
  <div class="c" data-s="0"><div class="n">0</div><h3>Zero-shot</h3><p>Aucun exemple : le modèle s'appuie sur ses <b>connaissances</b></p></div>
  <div class="c" data-s="1"><div class="n">1</div><h3>One-shot</h3><p><b>Un</b> exemple montre le résultat attendu pour une entrée</p></div>
  <div class="c" data-s="2"><div class="n">2+</div><h3>Few-shot</h3><p><b>Plusieurs</b> exemples consolident le comportement voulu</p></div>
</div>
<div class="code" data-s="3">Exemple 1 : US « ajout au panier »  ➜  Scenario: Given … When … Then …
Exemple 2 : US « suppression »      ➜  Scenario: Given … When … Then …
Nouvelle US : « code promo »        ➜  ?</div>
<p class="note" data-s="4">Résultats <b>cohérents</b> et <b>conformes au modèle</b> : idéal pour les tâches <b>répétitives</b> à format imposé.</p>""",
        "steps": [
            {"say": "Deuxième technique : donner des exemples. Avec zéro exemple, on parle de zero-shot : le modèle se débrouille avec ses connaissances."},
            {"say": "Avec un seul exemple, c'est du one-shot."},
            {"say": "Avec plusieurs exemples, c'est du few-shot."},
            {"say": "Par exemple, on montre deux user stories transformées en scénarios Gherkin, puis on donne une nouvelle user story. Le modèle imite le modèle."},
            {"say": "Les résultats sont cohérents et respectent le format. C'est parfait pour les tâches répétitives."},
        ],
    },
    {
        "section": "2.1.2", "title": "Le méta-prompting",
        "body": """
<div class="bubble" data-s="0"><span class="speaker">Max</span>« Je ne sais même pas comment écrire mon prompt… »</div>
<div class="flow" data-s="1">
  <div class="st"><b>Testeur</b>décrit l'objectif</div><div class="ar">➜</div>
  <div class="st"><b>LLM</b>propose un prompt</div><div class="ar">➜</div>
  <div class="st"><b>Testeur</b>évalue et affine</div><div class="ar">↺</div>
</div>
<div class="split" data-s="2">
  <div class="box ok"><h3>Avantages</h3><p>Moins d'<b>effort manuel</b>, prompts optimisés grâce au savoir du modèle</p></div>
  <div class="box"><h3>Une forme de « pairing »</h3><p>Le testeur et l'IA <b>co-créent</b> le prompt, comme en pair testing</p></div>
</div>""",
        "steps": [
            {"say": "Je ne sais même pas comment écrire mon prompt !", "voice": "max"},
            {"say": "Alors demande au modèle de l'écrire avec toi, Max. C'est le méta-prompting : le modèle génère ou améliore ses propres prompts, et le testeur les évalue et les affine, en boucle."},
            {"say": "Avantages : moins d'effort manuel et des prompts optimisés. Le syllabus parle d'une forme de pairing : le testeur et l'IA travaillent ensemble, comme en pair testing."},
        ],
    },
    {
        "section": "Quiz éclair", "title": "Quelle technique ?",
        "body": """
<div class="qa">
  <p class="q" data-s="0">« Voici 3 exemples de rapports de défaut au format maison. Rédige le rapport du nouveau défaut. »</p>
  <div class="answer" data-s="4">➜ <b>Few-shot</b> : plusieurs exemples guident le format.</div>
  <p class="q" data-s="5">« Aide-moi à écrire le meilleur prompt pour analyser ce rapport de test. »</p>
  <div class="answer" data-s="9">➜ <b>Méta-prompting</b> : le modèle co-crée le prompt.</div>
</div>""",
        "steps": [
            {"say": "Quiz éclair. Voici trois exemples de rapports de défaut au format maison : rédige le rapport du nouveau défaut. Quelle technique ?"},
            *countdown(),
            {"say": "Le few-shot : plusieurs exemples guident le format."},
            {"say": "Et ici : aide-moi à écrire le meilleur prompt pour analyser ce rapport de test."},
            *countdown(),
            {"say": "Le méta-prompting : on co-crée le prompt avec le modèle."},
        ],
    },
    {
        "section": "2.1.3", "title": "System prompt ou user prompt ?",
        "body": """
<div class="split">
  <div class="box" data-s="0"><h3>⚙️ System prompt</h3><ul>
    <li>Défini par le <b>développeur ou le testeur</b></li>
    <li>En général <b>invisible</b> et <b>non modifiable</b> par l'utilisateur du chatbot</li>
    <li><b>Constant</b> pendant toute la session</li>
    <li>Fixe le comportement, la personnalité, les paramètres opérationnels ; peut contenir rôle, contexte, contraintes</li></ul></div>
  <div class="box" data-s="1"><h3>💬 User prompt</h3><ul>
    <li>La <b>demande</b> de l'utilisateur</li>
    <li><b>Change</b> à chaque échange</li>
    <li><b>Visible</b>, c'est le contexte immédiat</li>
    <li>Doit être ciblé : instructions explicites, contexte utile, format de sortie</li></ul></div>
</div>
<div class="trap" data-s="2"><b>Le modèle tient compte des deux à la fois.</b> Image simple : le règlement du restaurant pour le serveur (system) et la commande de chaque client (user).</div>""",
        "steps": [
            {"say": "Objectif deux point un point trois. Le system prompt est défini par le développeur ou le testeur. Il est généralement invisible pour l'utilisateur du chatbot, qui ne peut pas le modifier. Il reste constant pendant toute la session et fixe les règles : le ton, la personnalité, les règles du domaine."},
            {"say": "Le user prompt, lui, c'est la demande de l'utilisateur. Il change à chaque échange et il est visible."},
            {"say": "Le modèle combine les deux pour répondre. Pensez au règlement que le restaurant donne au serveur, et à la commande de chaque client."},
        ],
    },
    {
        "section": "2.2", "title": "Appliquer le prompt engineering au test",
        "body": """
<div class="cards4">
  <div class="c" data-s="0"><div class="ic">🔍</div><h3>Analyse</h3><p>2.2.1</p></div>
  <div class="c" data-s="0"><div class="ic">📐</div><h3>Conception et implémentation</h3><p>2.2.2</p></div>
  <div class="c" data-s="0"><div class="ic">🔁</div><h3>Régression automatisée</h3><p>2.2.3</p></div>
  <div class="c" data-s="0"><div class="ic">📈</div><h3>Pilotage et contrôle</h3><p>2.2.4</p></div>
</div>
<div class="trap" data-s="1"><b>Règle d'or :</b> des entrées de qualité sont indispensables pour obtenir des résultats utiles.</div>""",
        "steps": [
            {"say": "Section deux point deux : place à la pratique. On va appliquer tout cela à quatre familles d'activités de test : l'analyse, la conception et l'implémentation, la régression automatisée, et le pilotage."},
            {"say": "Une règle d'or traverse toute la section : la qualité des entrées détermine la qualité des sorties."},
        ],
    },
    {
        "section": "2.2.1", "title": "L'analyse de test avec l'IA générative",
        "body": """
<div class="caps">
  <div data-s="0"><i class="n">1</i><span>Repérer les <b>défauts dans la base de test</b> : incohérences, ambiguïtés, informations manquantes</span></div>
  <div data-s="1"><i class="n">2</i><span>Générer des <b>conditions de test</b> mesurables et testables</span></div>
  <div data-s="2"><i class="n">3</i><span><b>Prioriser</b> selon le risque : probabilité, impact, conformité réglementaire, fonctions sensibles, historique de défauts</span></div>
  <div data-s="3"><i class="n">4</i><span>Soutenir l'analyse de <b>couverture</b> : relier exigences et conditions de test</span></div>
  <div data-s="4"><i class="n">5</i><span><b>Suggérer des techniques</b> : valeurs limites, partitions d'équivalence…</span></div>
</div>
<p class="note" data-s="5">Entrées : exigences, user stories, spécifications, maquettes · Sorties : conditions de test priorisées, comme des critères d'acceptation</p>""",
        "steps": [
            {"say": "Objectif deux point deux point un : l'analyse de test. Un : l'IA aide à repérer les défauts dans la base de test, comme les incohérences, les ambiguïtés ou les manques."},
            {"say": "Deux : elle génère des conditions de test, en découpant les exigences en énoncés mesurables et testables."},
            {"say": "Trois : elle aide à prioriser selon le risque, si on lui donne la probabilité et l'impact. Elle peut tenir compte de la conformité réglementaire, des fonctions sensibles comme la connexion ou le paiement, et de l'historique des défauts."},
            {"say": "Quatre : elle soutient l'analyse de couverture, en reliant les exigences aux conditions de test."},
            {"say": "Cinq : elle suggère des techniques de test adaptées, comme l'analyse des valeurs limites."},
            {"say": "En entrée : exigences, user stories, spécifications ou maquettes. En sortie : des conditions de test priorisées, par exemple des critères d'acceptation."},
        ],
    },
    {
        "section": "2.2.1", "title": "Scénario : des critères d'acceptation à partir d'une maquette",
        "body": """
<div class="flow">
  <div class="st" data-s="0"><b>🖼️ + 📝</b>Maquette + user story</div><div class="ar">➜</div>
  <div class="st" data-s="1"><b>Prompt structuré</b>multimodal</div><div class="ar">➜</div>
  <div class="st" data-s="2"><b>Critères</b>d'acceptation</div>
</div>
<div class="flow" data-s="3">
  <div class="st">Ambiguïtés</div><div class="chk">✅ humain</div><div class="ar">➜</div>
  <div class="st">Testabilité</div><div class="chk">✅ humain</div><div class="ar">➜</div>
  <div class="st">Complétude</div><div class="chk">✅ humain</div>
</div>
<div class="trap" data-s="4"><b>Réflexe K3 :</b> tâche complexe et précision exigée ➜ chaînage de prompts avec vérification humaine à chaque étape.</div>""",
        "steps": [
            {"say": "Un scénario typique de niveau K trois. Vous avez une maquette d'écran et une user story."},
            {"say": "Vous écrivez un prompt structuré multimodal, avec le texte et l'image en données d'entrée."},
            {"say": "Le modèle propose des critères d'acceptation."},
            {"say": "Ensuite, on les améliore par chaînage : ambiguïtés, puis testabilité, puis complétude. Et à chaque étape, un humain vérifie et corrige."},
            {"say": "Le réflexe à retenir : tâche complexe et besoin de précision, alors chaînage avec vérification humaine."},
        ],
    },
    {
        "section": "2.2.2", "title": "Conception et implémentation des tests",
        "body": """
<div class="cards4">
  <div class="c" data-s="0"><div class="ic">🧪</div><h3>Cas de test</h3><p>Brouillons avec préconditions, entrées, résultats attendus, critères de couverture</p></div>
  <div class="c" data-s="1"><div class="ic">🔢</div><h3>Données synthétiques</h3><p>Réalistes, <b>sans exposer de données sensibles</b>, avec cas extrêmes</p></div>
  <div class="c" data-s="2"><div class="ic">🤖</div><h3>Scripts</h3><p>Procédures manuelles et scripts automatisés pour divers frameworks</p></div>
  <div class="c" data-s="3"><div class="ic">🗓️</div><h3>Planification</h3><p>Ordonnancer et prioriser selon dépendances, risques et ressources</p></div>
</div>
<div class="trap" data-s="4"><b>Exercices types :</b> few-shot pour du Gherkin · chaînage pour prioriser une suite de tests · méta-prompt pour des tests de bout en bout</div>""",
        "steps": [
            {"say": "Objectif deux point deux point deux : conception et implémentation. D'abord, générer des brouillons de cas de test, avec préconditions, entrées, résultats attendus et critères de couverture."},
            {"say": "Ensuite, synthétiser des données de test réalistes, qui ressemblent à la production sans exposer d'informations sensibles, et qui couvrent les cas extrêmes."},
            {"say": "Puis générer des procédures manuelles et des scripts automatisés, compatibles avec différents frameworks."},
            {"say": "Enfin, organiser l'exécution en tenant compte des dépendances, des risques et des ressources disponibles."},
            {"say": "Dans les exercices du syllabus : few-shot pour produire du Gherkin, chaînage pour prioriser une suite de tests, et méta-prompt pour des tests de bout en bout."},
        ],
    },
    {
        "section": "2.2.3", "title": "La régression automatisée",
        "body": """
<p class="lead" data-s="0">À chaque itération, la suite de régression <b>grossit</b> : idéale pour l'automatisation en CI/CD.</p>
<div class="caps">
  <div data-s="1"><i class="n">1</i><span>Scripts <b>keyword-driven</b> : associer des mots-clés aux étapes de test</span></div>
  <div data-s="2"><i class="n">2</i><span><b>Analyse d'impact</b> : cibler les zones à risque après un changement de code</span></div>
  <div data-s="3"><i class="n">3</i><span>Tests <b>auto-réparants</b> : s'adapter aux petits changements d'IHM ou d'API</span></div>
  <div data-s="4"><i class="n">4</i><span><b>Rapports</b>, tendances et rapports de défaut enrichis (logs, captures, environnement)</span></div>
</div>
<div class="trap" data-s="5"><b>Mais :</b> l'IA peut se tromper. Vérifiez ses résultats en fonction du risque associé.</div>""",
        "steps": [
            {"say": "Objectif deux point deux point trois : la régression. À chaque nouvelle itération, la suite de régression grossit. Elle est donc idéale pour l'automatisation, surtout en intégration continue."},
            {"say": "L'IA aide à écrire des scripts keyword-driven, où des mots-clés représentent les étapes de test courantes."},
            {"say": "Elle analyse l'impact des changements de code, pour concentrer la régression là où le risque est le plus fort."},
            {"say": "Elle rend les tests auto-réparants : ils s'adaptent à de petits changements d'interface, comme des localisateurs dynamiques, ou d'API, comme un format de réponse modifié."},
            {"say": "Elle produit aussi des rapports, des tendances, et des rapports de défaut complets avec logs et captures."},
            {"say": "Mais attention : l'IA peut se tromper. On vérifie toujours ses résultats, d'autant plus que le risque est élevé."},
        ],
    },
    {
        "section": "2.2.4", "title": "Pilotage et contrôle des tests",
        "body": """
<div class="cards4">
  <div class="c" data-s="0"><div class="ic">📊</div><h3>Pilotage</h3><p>Analyser les métriques et les <b>tendances</b>, alerter en cas d'<b>écart</b> au plan</p></div>
  <div class="c" data-s="1"><div class="ic">🎛️</div><h3>Contrôle</h3><p><b>Reprioriser</b>, ajuster le planning, réaffecter les ressources</p></div>
  <div class="c" data-s="2"><div class="ic">🏁</div><h3>Clôture</h3><p>Rapports de fin de test, <b>leçons apprises</b></p></div>
  <div class="c" data-s="3"><div class="ic">🗣️</div><h3>Restitution</h3><p>Tableaux de bord et <b>résumés en langage naturel</b> pour toutes les parties prenantes</p></div>
</div>""",
        "steps": [
            {"say": "Objectif deux point deux point quatre : le pilotage et le contrôle. L'IA analyse de grandes quantités de données de test, repère les tendances et alerte en cas d'écart par rapport au plan."},
            {"say": "Pour le contrôle, elle propose de reprioriser des tests, d'ajuster le planning ou de réaffecter des ressources."},
            {"say": "En fin de test, elle aide à rédiger le rapport de clôture et les leçons apprises."},
            {"say": "Et elle crée des tableaux de bord et des résumés en langage naturel, compréhensibles par tous."},
        ],
    },
    {
        "section": "2.2.5", "title": "Choisir la bonne technique",
        "body": """
<table class="grid tbl3">
  <tr><th>Technique</th><th>Quand l'utiliser</th><th>Exemples</th></tr>
  <tr data-s="0"><td>🔗 Chaînage</td><td>Tâche <b>complexe</b>, <b>précision</b>, vérification humaine à chaque étape</td><td>Analyse, conception, automatisation</td></tr>
  <tr data-s="1"><td>🧩 Few-shot</td><td>Tâche <b>répétitive</b>, format <b>imposé</b></td><td>Gherkin, keyword-driven, rapports au format défini</td></tr>
  <tr data-s="2"><td>🪄 Méta-prompting</td><td>Tâche <b>flexible</b>, <b>nouvelle</b> : créer le prompt</td><td>Analyse de rapports, détection d'anomalies</td></tr>
</table>
<div class="flow" data-s="3">
  <div class="st"><b>Méta</b>prompt initial</div><div class="ar">➜</div><div class="st"><b>Few-shot</b>exemples adaptés</div><div class="ar">➜</div><div class="st"><b>Chaînage</b>étapes validées</div>
</div>""",
        "steps": [
            {"say": "Objectif deux point deux point cinq, très important pour l'examen : choisir la technique. Le chaînage pour les tâches complexes qui exigent de la précision et une vérification à chaque étape."},
            {"say": "Le few-shot pour les tâches répétitives avec un format imposé, comme le Gherkin, le keyword-driven ou des rapports au format défini."},
            {"say": "Le méta-prompting pour les tâches flexibles ou nouvelles, quand il faut d'abord créer le prompt."},
            {"say": "Et on peut combiner : un méta-prompt crée le prompt initial, on y ajoute des exemples en few-shot, puis on découpe en étapes validées par chaînage."},
        ],
    },
    {
        "section": "Quiz K3", "title": "À vous de choisir",
        "body": """
<div class="qa">
  <p class="q" data-s="0">Vous devez convertir <b>200 user stories</b> en scénarios Gherkin, toujours au même format.</p>
  <div class="opts" data-s="0"><div>Chaînage</div><div class="{{c1}}">Few-shot</div><div>Méta-prompting</div></div>
  <p class="q" data-s="5">Vous devez prioriser une suite de tests avec des <b>risques et dépendances</b> multiples, en vérifiant le raisonnement.</p>
  <div class="opts" data-s="5"><div class="{{c2}}">Chaînage</div><div>Few-shot</div><div>Méta-prompting</div></div>
</div>""",
        "steps": [
            {"say": "À vous ! Premier scénario : vous devez convertir deux cents user stories en scénarios Gherkin, toujours au même format. Quelle technique ?"},
            *countdown(),
            {"say": "Le few-shot : une tâche répétitive au format imposé.", "vars": {"c1": "good"}},
            {"say": "Deuxième scénario : prioriser une suite de tests avec de nombreux risques et dépendances, en vérifiant le raisonnement du modèle.", "vars": {"c1": "good"}},
            *[dict(step, vars={**step["vars"], "c1": "good"}) for step in countdown()],
            {"say": "Le chaînage : une tâche complexe, découpée, avec vérification à chaque étape.", "vars": {"c1": "good", "c2": "good"}},
        ],
    },
    {
        "section": "2.3.1", "title": "Mesurer la qualité des résultats",
        "body": """
<div class="metrics">
  <div class="c" data-s="0"><h3>Exactitude</h3><p>Justesse globale vs une référence d'expert</p><p class="ex">Les cas couvrent-ils toutes les exigences ?</p></div>
  <div class="c" data-s="0"><h3>Précision</h3><p>Justesse vis-à-vis d'un objectif précis</p><p class="ex">Les cas détectent-ils correctement les anomalies ?</p></div>
  <div class="c" data-s="0"><h3>Rappel</h3><p>Capacité à trouver <b>tous</b> les cas pertinents</p><p class="ex">Partitions valides <b>et</b> invalides couvertes ?</p></div>
  <div class="c" data-s="1"><h3>Pertinence</h3><p>Adapté au contexte et à la base de test</p><p class="ex">Exigences du domaine intégrées ?</p></div>
  <div class="c" data-s="1"><h3>Diversité</h3><p>Variété des scénarios, sans répétition</p><p class="ex">Cas limites explorés ?</p></div>
  <div class="c" data-s="2"><h3>Taux de succès d'exécution</h3><p>Part des scripts exécutables tels quels</p></div>
  <div class="c" data-s="2"><h3>Efficacité en temps</h3><p>Temps gagné vs l'effort manuel</p></div>
  <div class="c hl" data-s="3"><h3>⚠️ À retenir</h3><p>Non-déterminisme ➜ des mesures sur des données <b>statistiquement significatives</b></p></div>
</div>""",
        "steps": [
            {"say": "Section deux point trois : comment savoir si l'IA a bien travaillé ? Avec des métriques. Trois viennent du monde des statistiques : l'exactitude, la précision et le rappel. Exemple pour le rappel : les cas générés couvrent-ils les partitions valides et invalides ?"},
            {"say": "Ensuite, la pertinence et l'adéquation au contexte, et la diversité des scénarios, qui évite les répétitions et explore les cas limites."},
            {"say": "Plus deux métriques très concrètes : le taux de succès d'exécution des scripts générés, et le temps gagné par rapport à un travail manuel."},
            {"say": "Et un piège classique : comme le modèle n'est pas déterministe, les mesures doivent reposer sur des données statistiquement significatives, pas sur un seul essai."},
        ],
    },
    {
        "section": "2.3.2", "title": "Affiner ses prompts : 5 techniques",
        "body": """
<div class="caps">
  <div data-s="0"><i class="n">1</i><span><b>Modification itérative</b> : partir d'un prompt de base, ajouter du contexte, ajuster les termes</span></div>
  <div data-s="1"><i class="n">2</i><span><b>A/B testing</b> : comparer plusieurs versions selon des métriques définies à l'avance</span></div>
  <div data-s="2"><i class="n">3</i><span><b>Analyse des sorties</b> : comprendre les types d'erreurs pour les éviter</span></div>
  <div data-s="3"><i class="n">4</i><span><b>Retours des utilisateurs</b> : utilité, clarté, niveau de détail</span></div>
  <div data-s="4"><i class="n">5</i><span><b>Longueur et précision</b> : plus de contexte aide parfois, un prompt court généralise parfois mieux</span></div>
</div>
<p class="note" data-s="5">Et partagez : <b>bibliothèques de prompts</b> communes à l'équipe.</p>""",
        "steps": [
            {"say": "Dernier objectif : améliorer ses prompts. Un : la modification itérative. On part d'un prompt de base et on l'ajuste selon les résultats."},
            {"say": "Deux : l'A B testing. On compare plusieurs versions du prompt avec des métriques fixées à l'avance."},
            {"say": "Trois : l'analyse des sorties. Comprendre les erreurs du modèle permet de les éviter ensuite."},
            {"say": "Quatre : les retours des testeurs sur l'utilité, la clarté ou le niveau de détail."},
            {"say": "Cinq : jouer sur la longueur et la précision. Parfois, plus de contexte aide. Parfois, un prompt plus court généralise mieux."},
            {"say": "Et partagez vos meilleurs prompts dans une bibliothèque commune à l'équipe."},
        ],
    },
    {
        "section": "Révision", "title": "Les 6 réflexes du chapitre 2",
        "body": """
<ul class="traps">
  <li data-s="0"><b>6 composants :</b> rôle, contexte, instruction, données d'entrée, contraintes, format de sortie.</li>
  <li data-s="1"><b>Contraintes</b> = comment appliquer l'instruction · <b>Format</b> = forme du résultat.</li>
  <li data-s="2"><b>Chaînage</b> = complexe + vérification · <b>Few-shot</b> = répétitif + format · <b>Méta</b> = nouveau + créer le prompt.</li>
  <li data-s="3"><b>System prompt</b> : constant, défini par le développeur ou testeur · <b>User prompt</b> : change à chaque échange.</li>
  <li data-s="4"><b>Toujours vérifier</b> les sorties, selon le risque.</li>
  <li data-s="5"><b>Métriques</b> sur des données statistiquement significatives · <b>A/B testing</b> pour comparer des prompts.</li>
</ul>""",
        "steps": [
            {"say": "Récapitulons en six réflexes. Un : les six composants du prompt."},
            {"say": "Deux : ne confondez pas contraintes et format de sortie."},
            {"say": "Trois : chaînage pour le complexe, few-shot pour le répétitif, méta-prompting pour le nouveau."},
            {"say": "Quatre : le system prompt est constant, le user prompt change à chaque échange."},
            {"say": "Cinq : on vérifie toujours les sorties, selon le risque."},
            {"say": "Six : des métriques fiables, et l'A B testing pour comparer des prompts."},
        ],
    },
    {
        "section": "Fin", "title": "",
        "body": """
<div class="hero">
  <div class="ic big">🚀</div>
  <h1 style="font-size:84px">Bravo, chapitre 2 terminé !</h1>
  <div class="bubble" data-s="1"><span class="speaker">Max</span>« Maintenant, je donne un vrai brief à l'IA. »</div>
  <p class="lead" data-s="2">À faire : les questions et flashcards du chapitre 2 dans l'application.</p>
</div>""",
        "steps": [
            {"say": "Bravo, vous avez terminé le chapitre deux !"},
            {"say": "Maintenant, je donne un vrai brief à l'IA, et ça change tout !", "voice": "max"},
            {"say": "Pour ancrer tout ça, faites les questions et les flashcards du chapitre deux dans l'application. À bientôt pour le chapitre trois, consacré aux risques de l'IA générative."},
        ],
    },
]
