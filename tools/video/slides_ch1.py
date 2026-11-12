# Contenu de la vidéo : CT-GenAI v1.1, chapitre 1. Chaque diapositive = (titre, section, corps HTML, narration).
# Le texte est une synthèse originale du syllabus v1.1 (sections 1.1 et 1.2).

CHAPTER = "CT-GenAI v1.1 · Chapitre 1"

SLIDES = [
    {
        "section": "",
        "title": "Introduction à l'IA générative pour le test",
        "body": """
<div class="hero">
  <p class="kicker">ISTQB® CT-GenAI v1.1 — Chapitre 1</p>
  <h1>L'IA générative<br>expliquée simplement</h1>
  <p class="lead">Les bases à connaître pour l'examen, avec des exemples de testeur</p>
  <div class="chips"><span>100 minutes de cours</span><span>6 objectifs d'apprentissage</span><span>Niveaux K1 et K2</span></div>
</div>""",
        "narration": (
            "Bonjour et bienvenue. Dans cette vidéo, nous allons parcourir le chapitre un du syllabus ISTQB "
            "Testing with Generative AI, version un point un. Ce chapitre pose les fondations : ce qu'est l'IA "
            "générative, comment fonctionne un grand modèle de langage, et comment un testeur peut s'en servir. "
            "Pas de panique : nous allons utiliser des images simples, comme des briques de Lego, une carte "
            "ou l'autocomplétion de votre téléphone. Et à chaque étape, je vous signalerai les pièges classiques de l'examen."
        ),
    },
    {
        "section": "Plan",
        "title": "Ce que vous devez savoir faire",
        "body": """
<table class="grid">
  <tr><th>Objectif</th><th>Niveau</th><th>En clair</th></tr>
  <tr><td>1.1.1</td><td><b class="k1">K1</b></td><td>Citer les types d'IA : symbolique, ML classique, deep learning, IA générative</td></tr>
  <tr><td>1.1.2</td><td><b class="k2">K2</b></td><td>Expliquer les bases de l'IA générative et des LLM</td></tr>
  <tr><td>1.1.3</td><td><b class="k2">K2</b></td><td>Distinguer LLM de fondation, ajustés aux instructions et de raisonnement</td></tr>
  <tr><td>1.1.4</td><td><b class="k2">K2</b></td><td>Utiliser un LLM multimodal (texte + image) pour une tâche de test</td></tr>
  <tr><td>1.2.1</td><td><b class="k2">K2</b></td><td>Donner des exemples de capacités des LLM pour le test</td></tr>
  <tr><td>1.2.2</td><td><b class="k2">K2</b></td><td>Comparer chatbot et application intégrant un LLM</td></tr>
</table>
<p class="note"><b>K1</b> = se souvenir · <b>K2</b> = comprendre et expliquer</p>""",
        "narration": (
            "Voici les six objectifs du chapitre. Le premier est de niveau K un : il suffit de se souvenir des "
            "types d'intelligence artificielle. Les cinq autres sont de niveau K deux : il faut comprendre et "
            "savoir expliquer, par exemple la différence entre deux familles de modèles. Concrètement, à "
            "l'examen, une question K deux vous demandera souvent de choisir le bon exemple, ou la bonne "
            "explication, parmi quatre propositions qui se ressemblent."
        ),
    },
    {
        "section": "1.1.1",
        "title": "Le spectre de l'IA : quatre familles",
        "body": """
<div class="cards4">
  <div class="c"><div class="ic">📘</div><h3>IA symbolique</h3><p>Des <b>règles</b> et des <b>symboles</b> écrits par des humains : « si… alors… »</p><p class="ex">Comme un livre de recettes à suivre à la lettre</p></div>
  <div class="c"><div class="ic">📊</div><h3>ML classique</h3><p>Apprend à partir des <b>données</b>. Il faut préparer les données, <b>choisir les features</b> et entraîner</p><p class="ex">Ex. : classer des défauts, prédire des problèmes</p></div>
  <div class="c"><div class="ic">🧠</div><h3>Deep learning</h3><p>Des <b>réseaux de neurones</b> trouvent <b>seuls</b> les features dans de grandes données : images, son, texte</p><p class="ex">L'humain reste utile : annotation, réglage, validation</p></div>
  <div class="c hl"><div class="ic">✨</div><h3>IA générative</h3><p>Utilise le deep learning pour <b>créer du contenu nouveau</b> : texte, images, code</p><p class="ex">Ex. : les LLM</p></div>
</div>""",
        "narration": (
            "Commençons par le paysage de l'intelligence artificielle. Le syllabus cite quatre familles. "
            "Un : l'IA symbolique. Elle représente le savoir avec des symboles et des règles logiques, du type "
            "si ceci, alors cela. Pensez à un livre de recettes que la machine suit à la lettre. "
            "Deux : le machine learning classique. Ici, la machine apprend à partir de données, mais il faut "
            "préparer ces données, choisir soi-même les caractéristiques importantes, qu'on appelle les features, "
            "puis entraîner le modèle. Exemple de testeur : classer automatiquement des défauts. "
            "Trois : le deep learning. Il utilise des réseaux de neurones qui trouvent tout seuls les features "
            "dans de très grandes données, comme des images ou du son. Attention : en pratique, des humains "
            "restent nécessaires pour annoter les données, régler le modèle ou valider les résultats. "
            "Quatre : l'IA générative. Elle s'appuie sur le deep learning pour créer du contenu nouveau, "
            "du texte, des images ou du code, en imitant ce qu'elle a appris."
        ),
    },
    {
        "section": "1.1.1",
        "title": "Pourquoi l'IA générative change la donne pour le test",
        "body": """
<div class="split">
  <div class="box ok"><h3>✅ L'avantage clé</h3><p>Les modèles sont <b>déjà pré-entraînés</b>.</p><p>On peut les appliquer <b>directement</b> à une tâche de test, <b>sans phase d'entraînement supplémentaire</b>.</p></div>
  <div class="box warn"><h3>⚠️ Mais…</h3><p>Cet avantage s'accompagne de <b>risques</b> : hallucinations, biais, sécurité…</p><p>Ils sont traités au <b>chapitre 3</b>.</p></div>
</div>
<div class="trap"><b>Piège d'examen :</b> le ML classique demande de préparer des données et d'entraîner un modèle. L'IA générative, elle, s'utilise sans entraîner un nouveau modèle.</div>""",
        "narration": (
            "Retenez bien ce point, car c'est l'avantage principal selon le syllabus. Avec le machine learning "
            "classique, il faut collecter des données, les préparer et entraîner un modèle avant de pouvoir "
            "l'utiliser. Avec l'IA générative, le modèle est déjà pré-entraîné : vous pouvez l'appliquer "
            "directement à une tâche de test, sans phase d'entraînement supplémentaire. C'est comme engager "
            "quelqu'un qui a déjà lu une bibliothèque entière, plutôt que de former un débutant. "
            "Mais cet avantage a un prix : des risques comme les hallucinations ou les biais, que vous verrez "
            "au chapitre trois."
        ),
    },
    {
        "section": "1.1.2",
        "title": "Qu'est-ce qu'un LLM ?",
        "body": """
<div class="split">
  <div class="box"><h3>LLM = Large Language Model</h3><ul>
    <li>Basé sur le modèle <b>GPT</b> : <i>Generative Pre-trained Transformer</i></li>
    <li>Entraîné sur d'<b>immenses jeux de données</b> : livres, articles, sites web</li>
    <li>Comprend les <b>nuances</b> du langage et produit un texte <b>cohérent</b></li></ul></div>
  <div class="box"><h3>Et les SLM ?</h3><ul>
    <li><b>Small Language Models</b> : modèles compacts</li>
    <li><b>Moins de paramètres</b></li>
    <li>Solutions <b>légères</b> et <b>ciblées</b></li></ul>
    <p class="ex">Un camion polyvalent face à un scooter rapide pour un trajet précis</p></div>
</div>""",
        "narration": (
            "Passons aux grands modèles de langage, les LLM, pour Large Language Models. Ils reposent sur le "
            "modèle GPT, ce qui signifie transformeur génératif pré-entraîné. Ils ont été entraînés sur "
            "d'énormes quantités de textes : des livres, des articles, des sites web. Résultat : ils saisissent "
            "les nuances du langage et produisent des réponses cohérentes. "
            "Le syllabus mentionne aussi les SLM, les petits modèles de langage. Ils ont moins de paramètres "
            "et offrent des solutions plus légères et plus ciblées. Imaginez un gros camion polyvalent face à "
            "un scooter, parfait pour un trajet précis."
        ),
    },
    {
        "section": "1.1.2",
        "title": "Tokenisation : découper le texte en briques",
        "body": """
<p class="lead">Le modèle ne lit pas des mots : il lit des <b>tokens</b>.</p>
<div class="tokens"><span>Le</span><span> bouton</span><span> Val</span><span>ider</span><span> ne</span><span> rép</span><span>ond</span><span> pas</span><span>.</span></div>
<p class="small center">Découpage illustratif : chaque modèle a son propre tokenizer.</p>
<ul class="big">
  <li>Un token peut être <b>un caractère</b>, <b>un morceau de mot</b> ou <b>un mot entier</b></li>
  <li>Le modèle découpe d'abord l'entrée, puis traite chaque token <b>sans perdre le contexte global</b></li>
  <li>Exercice pratique HO-1.1.2 : découper un texte et <b>compter les tokens</b></li>
</ul>""",
        "narration": (
            "Deux mécanismes permettent au modèle de traiter le langage : la tokenisation et les embeddings. "
            "Ensemble, ils transforment le texte en nombres. Commençons par la tokenisation. "
            "Le modèle ne lit pas vraiment des mots. Il découpe d'abord le texte en petites briques, comme des "
            "Lego, qu'on appelle des tokens. Un token peut être un seul caractère, un morceau de mot, ou un mot "
            "entier. Par exemple, la phrase « Le bouton Valider ne répond pas » peut être découpée en neuf tokens. "
            "Le modèle traite ensuite chaque token, tout en gardant le sens général de la phrase. "
            "Le syllabus propose d'ailleurs un exercice pratique : découper un texte et compter ses tokens, "
            "pour voir l'effet de la longueur sur l'utilisation du modèle."
        ),
    },
    {
        "section": "1.1.2",
        "title": "Embeddings : une carte du sens",
        "body": """
<div class="split">
  <div class="map">
    <div class="dot" style="left:16%;top:22%">défaut</div>
    <div class="dot" style="left:30%;top:34%">bug</div>
    <div class="dot" style="left:14%;top:46%">anomalie</div>
    <div class="dot b" style="left:62%;top:20%">connexion</div>
    <div class="dot b" style="left:74%;top:34%">login</div>
    <div class="dot c" style="left:58%;top:74%">banane</div>
    <div class="ring" style="left:6%;top:12%;width:36%;height:46%"></div>
  </div>
  <div class="box"><h3>Chaque token devient un vecteur</h3><ul>
    <li>Une liste de nombres = une <b>position</b> dans un espace à très grand nombre de dimensions</li>
    <li>Sens <b>proches</b> → positions <b>proches</b></li>
    <li>Le modèle comprend ainsi les <b>relations entre les mots</b> et garde le <b>contexte</b></li></ul></div>
</div>""",
        "narration": (
            "Deuxième mécanisme : les embeddings. Chaque token est transformé en une liste de nombres, un "
            "vecteur. Imaginez une immense carte où chaque mot a une adresse. Les mots qui ont un sens ou un "
            "rôle proche sont placés près les uns des autres : bug, défaut et anomalie sont voisins, tandis "
            "que banane est très loin. En réalité, cette carte n'a pas deux dimensions mais des centaines, voire "
            "des milliers. Grâce à cette proximité, le modèle comprend les relations entre les mots, garde le "
            "contexte et produit des réponses cohérentes."
        ),
    },
    {
        "section": "1.1.2",
        "title": "Le transformeur prédit le token suivant",
        "body": """
<div class="predict">
  <div class="prompt">« Le test de connexion a échoué parce que le mot de passe était… »</div>
  <div class="bars">
    <div><span>incorrect</span><i style="width:62%"></i><em>62 %</em></div>
    <div><span>expiré</span><i style="width:21%"></i><em>21 %</em></div>
    <div><span>vide</span><i style="width:11%"></i><em>11 %</em></div>
    <div><span>bleu</span><i style="width:1%"></i><em>≈ 0 %</em></div>
  </div>
  <p class="small center">Probabilités inventées pour l'exemple</p>
</div>
<div class="trap"><b>À retenir :</b> le texte produit est <b>statistiquement plausible</b>… mais <b>plausible ne veut pas dire correct</b>.</div>""",
        "narration": (
            "Comment le modèle écrit-il ? Les LLM utilisent une architecture de réseau de neurones appelée "
            "transformeur. Elle apprend comment les tokens sont liés entre eux, même dans de longs textes. "
            "Au moment de répondre, ce qu'on appelle l'inférence, le modèle prédit simplement le token "
            "suivant, puis le suivant, et ainsi de suite. C'est l'autocomplétion de votre téléphone, en "
            "beaucoup plus puissant. Par exemple, après « le mot de passe était », le mot incorrect est très "
            "probable, le mot bleu presque impossible. "
            "Voici une phrase clé du syllabus : le texte généré est statistiquement plausible, mais plausible "
            "ne veut pas dire correct. En tant que testeur, vous devez donc toujours vérifier ce que produit le modèle."
        ),
    },
    {
        "section": "1.1.2",
        "title": "Même question, réponses différentes",
        "body": """
<div class="split">
  <div class="box"><h3>Le non-déterminisme</h3><p>Le même prompt, envoyé plusieurs fois, peut donner des <b>réponses différentes</b>.</p>
    <h3>Deux causes</h3><ul><li>la nature <b>probabiliste</b> de l'inférence</li><li>les réglages des <b>hyperparamètres</b> (ex. : la température)</li></ul></div>
  <div class="box"><h3>🎲 Image simple</h3><p>Le modèle tire le mot suivant avec un dé <b>pipé</b> : les mots probables sortent souvent, mais pas toujours.</p>
    <h3>Pour le testeur</h3><p>Ne pas compter sur une réponse <b>identique</b> d'une exécution à l'autre.</p></div>
</div>""",
        "narration": (
            "Autre caractéristique importante : les LLM ne sont pas déterministes. Si vous envoyez exactement "
            "le même prompt plusieurs fois, vous pouvez obtenir des réponses différentes. Le syllabus donne "
            "deux causes : la nature probabiliste de l'inférence, et le réglage des hyperparamètres, comme la "
            "température. Imaginez que le modèle choisit le mot suivant en lançant un dé pipé : les mots "
            "probables sortent le plus souvent, mais pas à chaque fois. Pour un testeur, cela compte : on ne "
            "peut pas supposer qu'une sortie sera identique d'une exécution à l'autre."
        ),
    },
    {
        "section": "1.1.2",
        "title": "La fenêtre de contexte : la mémoire de travail",
        "body": """
<div class="window">
  <div class="tape"><span class="out">…début d'un très long log…</span><span class="in">[ ce que le modèle « voit » : N tokens ]</span><span class="next">→ réponse</span></div>
</div>
<div class="split">
  <div class="box ok"><h3>Plus grande fenêtre</h3><p>Le modèle reste <b>cohérent</b> sur de longs textes, par exemple pour analyser de <b>gros logs de test</b>.</p></div>
  <div class="box warn"><h3>Mais</h3><p>Plus de tokens = plus de <b>calcul</b> et un <b>temps de traitement</b> plus long.</p></div>
</div>
<p class="note">Elle se mesure en <b>tokens</b>, pas en mots ni en pages.</p>""",
        "narration": (
            "Parlons maintenant de la fenêtre de contexte. C'est la quantité de texte précédent que le modèle "
            "peut prendre en compte pour répondre. Elle se mesure en tokens, pas en mots ni en pages. "
            "Pensez à la surface d'un bureau : ce qui tient sur le bureau est visible, le reste est hors de "
            "vue. Une fenêtre plus grande permet de rester cohérent sur de longs passages, par exemple pour "
            "analyser de gros fichiers de logs de test. Mais attention au revers : plus il y a de tokens, plus "
            "le calcul est complexe et plus le traitement est long. Voilà pourquoi compter les tokens, comme "
            "dans l'exercice pratique, est utile."
        ),
    },
    {
        "section": "1.1.3",
        "title": "Trois familles de LLM",
        "body": """
<div class="steps">
  <div class="s"><h3>1. Fondation</h3><p><b>Généraliste</b>, pré-entraîné sur des données massives et variées : texte, code, images…</p><p class="ex">L'étudiant qui a tout lu, mais qu'il faut encore <b>adapter</b> à une tâche précise</p></div>
  <div class="arrow">➜</div>
  <div class="s"><h3>2. Ajusté aux instructions</h3><p><i>Instruction-tuned</i> : affiné avec des paires <b>prompt → réponse attendue</b></p><p class="ex">L'assistant qui <b>suit bien les consignes</b></p></div>
  <div class="arrow">➜</div>
  <div class="s"><h3>3. Raisonnement</h3><p>Entraîné en plus au <b>raisonnement en plusieurs étapes</b>, à l'inférence logique, à la <i>chain-of-thought</i></p><p class="ex">L'expert pour les <b>tâches complexes</b></p></div>
</div>
<p class="note">Pour le test, on utilise les modèles ajustés aux instructions <b>et</b> de raisonnement : le choix dépend de la <b>complexité de la tâche</b>.</p>""",
        "narration": (
            "Objectif un point un point trois : les trois familles de LLM. Elles correspondent à des étapes "
            "d'entraînement de plus en plus spécialisées. "
            "Première famille : le modèle de fondation. C'est un généraliste, pré-entraîné sur des données "
            "massives et variées. Il est puissant et flexible, mais il faut généralement l'adapter à une tâche "
            "précise. Pensez à un étudiant qui a tout lu mais qui n'a pas encore de métier. "
            "Deuxième famille : le modèle ajusté aux instructions, instruction-tuned en anglais. On part d'un "
            "modèle de fondation et on l'affine avec des paires associant un prompt et la réponse attendue. Il "
            "suit alors beaucoup mieux les consignes. On l'appelle parfois modèle sans raisonnement. "
            "Troisième famille : le modèle de raisonnement. Il prolonge le précédent et est entraîné au "
            "raisonnement logique en plusieurs étapes. Il convient aux tâches exigeantes. "
            "Pour le test, on utilise les deux dernières familles : le choix dépend de la complexité de la tâche."
        ),
    },
    {
        "section": "1.1.4",
        "title": "LLM multimodaux et modèles vision-langage",
        "body": """
<div class="split">
  <div class="box"><h3>Multimodal</h3><p>Traite <b>plusieurs types de données</b> : texte, images, son, vidéo.</p><p>La tokenisation est <b>adaptée à chaque type</b> : une image est convertie en embeddings par un modèle vision-langage.</p></div>
  <div class="box"><h3>Vision-langage (VLM)</h3><p>Un <b>sous-ensemble</b> des multimodaux, qui combine <b>image et texte</b> :</p><ul><li>décrire une image</li><li>répondre à une question sur une image</li><li>vérifier la <b>cohérence</b> entre un texte et une image</li></ul></div>
</div>
<div class="usecase">🖼️ Capture d'écran + 📝 user story → « Le bouton “Payer” attendu est-il visible et correctement libellé ? »</div>""",
        "narration": (
            "Objectif un point un point quatre : les modèles multimodaux. Un LLM multimodal sait traiter "
            "plusieurs types de données : du texte, des images, du son, de la vidéo. Pour cela, la "
            "tokenisation est adaptée à chaque type. Par exemple, une image est convertie en embeddings grâce "
            "à un modèle vision-langage, avant d'être traitée par le transformeur. "
            "Les modèles vision-langage sont un sous-ensemble des modèles multimodaux. Ils combinent l'image "
            "et le texte pour décrire une image, répondre à une question sur une image, ou vérifier qu'un "
            "texte et une image sont cohérents."
        ),
    },
    {
        "section": "1.1.4",
        "title": "Le multimodal au service du testeur",
        "body": """
<div class="cards3">
  <div class="c"><div class="ic">🔍</div><h3>Comparer</h3><p>Une <b>capture d'écran</b> ou une <b>maquette</b> avec une user story ou un rapport de défaut, pour repérer les <b>écarts</b> entre attendu et affiché</p></div>
  <div class="c"><div class="ic">🧪</div><h3>Générer</h3><p>Des <b>cas de test réalistes</b> qui combinent données textuelles et <b>indices visuels</b>, pour augmenter la <b>couverture</b></p></div>
  <div class="c"><div class="ic">🛠️</div><h3>Pratiquer</h3><p>Exercice HO-1.1.4 : relire le prompt et les entrées, puis exécuter avec <b>texte + image</b> et <b>vérifier</b> la réponse</p></div>
</div>""",
        "narration": (
            "Pourquoi est-ce utile pour un testeur ? Un modèle multimodal peut analyser les éléments visuels "
            "d'une application, comme une capture d'écran ou une maquette d'interface, en même temps qu'un "
            "texte, comme une user story ou un rapport de défaut. Il peut ainsi repérer les écarts entre le "
            "résultat attendu et ce qui est réellement affiché à l'écran. Il peut aussi générer des cas de test "
            "réalistes qui combinent texte et indices visuels, ce qui augmente la couverture. "
            "Le syllabus prévoit un exercice pratique : relire le prompt et les entrées, puis envoyer le texte "
            "et l'image au modèle, et vérifier sa réponse."
        ),
    },
    {
        "section": "1.2.1",
        "title": "Sept capacités des LLM pour le test",
        "body": """
<div class="caps">
  <div><i class="n">1</i><span>Analyser et améliorer les <b>exigences</b> : ambiguïtés, incohérences, manques, questions à poser</span></div>
  <div><i class="n">2</i><span>Aider à créer des <b>cas de test</b> et proposer des objectifs de test</span></div>
  <div><i class="n">3</i><span>Générer des <b>oracles de test</b> : les résultats attendus</span></div>
  <div><i class="n">4</i><span>Générer des <b>données de test</b> : jeux de données, valeurs limites, combinaisons</span></div>
  <div><i class="n">5</i><span>Soutenir l'<b>automatisation</b> : écrire et améliorer des scripts de test</span></div>
  <div><i class="n">6</i><span>Analyser les <b>résultats</b> : résumés, classement des anomalies par sévérité et priorité</span></div>
  <div><i class="n">7</i><span>Créer le <b>testware</b> : plans de test, rapports de test, rapports de défaut… et les tenir à jour</span></div>
</div>""",
        "narration": (
            "Section un point deux : comment exploiter ces modèles dans le test. Les LLM excellent pour traiter "
            "le langage naturel et le code, résumer, traduire, répondre à des questions, et analyser des images. "
            "Le syllabus cite sept capacités clés. Un : analyser les exigences pour trouver des ambiguïtés, des "
            "incohérences ou des informations manquantes, et proposer des questions à poser aux parties "
            "prenantes. Deux : aider à créer des cas de test. Trois : générer des oracles de test, c'est-à-dire "
            "les résultats attendus. Quatre : générer des données de test, y compris des valeurs limites. "
            "Cinq : soutenir l'automatisation, en écrivant ou en améliorant des scripts. Six : analyser les "
            "résultats de test, en les résumant et en classant les anomalies. Sept : créer le testware, comme "
            "les plans et rapports de test, et le tenir à jour."
        ),
    },
    {
        "section": "1.2.1",
        "title": "Exemple : une user story de connexion",
        "body": """
<div class="story">« En tant que client, je veux me connecter avec mon e-mail et un mot de passe <b>sécurisé</b>. »</div>
<div class="cards3">
  <div class="c"><h3>❓ Exigences</h3><p>« Que signifie <b>sécurisé</b> ? Combien de caractères au minimum ? Que se passe-t-il après 3 échecs ? »</p></div>
  <div class="c"><h3>🧪 Cas de test</h3><p>Connexion valide, mot de passe faux, e-mail inconnu, compte bloqué…</p></div>
  <div class="c"><h3>🔢 Données</h3><p>Si le minimum est 8 caractères : tester <b>7</b>, <b>8</b> et une valeur juste au-dessus</p></div>
</div>
<div class="trap"><b>Toujours :</b> relire et valider ce que propose le modèle. Il assiste le testeur, il ne le remplace pas.</div>""",
        "narration": (
            "Prenons un exemple concret. Une user story dit : en tant que client, je veux me connecter avec mon "
            "e-mail et un mot de passe sécurisé. Un LLM peut d'abord repérer l'ambiguïté : que veut dire "
            "sécurisé ? Combien de caractères au minimum ? Que se passe-t-il après trois échecs ? Ce sont de "
            "bonnes questions à poser au métier. Ensuite, il peut proposer des cas de test : une connexion "
            "valide, un mauvais mot de passe, un e-mail inconnu, un compte bloqué. Enfin, si on lui précise que "
            "le minimum est de huit caractères, il peut proposer des valeurs limites, comme sept et huit. "
            "Mais rappelez-vous : plausible ne veut pas dire correct. Le testeur relit et valide toujours."
        ),
    },
    {
        "section": "1.2.2",
        "title": "Chatbot ou application intégrant un LLM ?",
        "body": """
<table class="grid cmp">
  <tr><th></th><th>💬 Chatbot d'IA</th><th>⚙️ Application de test intégrant un LLM</th></tr>
  <tr><td>Accès</td><td>Interface de <b>conversation</b></td><td>Intégration par <b>API</b> dans les outils de test</td></tr>
  <tr><td>Points forts</td><td>Réponse <b>immédiate</b>, affinage par <b>enchaînement de prompts</b>, accessible aux <b>non-techniciens</b></td><td><b>Personnalisation</b>, <b>passage à l'échelle</b>, <b>automatisation</b> de tâches répétitives ou complexes</td></tr>
  <tr><td>Usages typiques</td><td>Tâches courantes, test exploratoire, intégration des nouveaux testeurs, clarifier une exigence</td><td>Génération de cas de test, analyse de défauts, synthèse de données de test, <b>agents d'IA</b> (chapitre 4)</td></tr>
</table>""",
        "narration": (
            "Dernier objectif : comparer les deux façons d'utiliser l'IA générative. "
            "Première façon : le chatbot. C'est une interface de conversation. Vous posez une question, vous "
            "obtenez une réponse immédiate, et vous l'améliorez par étapes en enchaînant les prompts. C'est "
            "idéal pour les tâches courantes, le test exploratoire, la clarification d'exigences, ou pour aider "
            "un nouveau testeur. Et comme c'est intuitif, même des personnes non techniques peuvent l'utiliser. "
            "Deuxième façon : l'application de test qui intègre un LLM par une API. Elle réalise des tâches "
            "bien définies, souvent automatisées, comme générer des cas de test ou analyser des défauts. Elle "
            "est plus personnalisable et passe mieux à l'échelle. Dans les cas avancés, on crée même des agents "
            "d'IA, que vous verrez au chapitre quatre. Image simple : le chatbot, c'est discuter avec un expert ; "
            "l'application, c'est une machine intégrée à votre chaîne de production."
        ),
    },
    {
        "section": "1.2.2",
        "title": "Le point commun : le prompt engineering",
        "body": """
<div class="hero compact">
  <div class="ic big">🎯</div>
  <p class="lead">Chatbot ou application : dans les deux cas, la réussite dépend de <b>prompts bien conçus</b>.</p>
  <p>Des instructions <b>claires et précises</b> augmentent la probabilité d'obtenir des réponses <b>exactes</b>, <b>pertinentes</b> et <b>alignées</b> sur les objectifs de test.</p>
  <p class="note">C'est tout le sujet du <b>chapitre 2</b>, le plus long du syllabus.</p>
</div>""",
        "narration": (
            "Quelle que soit la façon d'utiliser le modèle, chatbot ou application, un point commun décide de "
            "la réussite : la qualité des prompts. Des instructions claires et précises augmentent les chances "
            "d'obtenir des réponses exactes, pertinentes et alignées sur vos objectifs de test. C'est ce qu'on "
            "appelle le prompt engineering, et c'est tout le sujet du chapitre deux, le plus long du syllabus."
        ),
    },
    {
        "section": "Révision",
        "title": "Les pièges classiques de l'examen",
        "body": """
<ul class="traps">
  <li><b>Features :</b> choisies à la main en <b>ML classique</b>, apprises automatiquement en <b>deep learning</b>.</li>
  <li><b>Avantage de l'IA générative :</b> modèles <b>pré-entraînés</b>, utilisables <b>sans phase d'entraînement supplémentaire</b>.</li>
  <li><b>Plausible ≠ correct :</b> le modèle prédit le token suivant le plus probable, pas la vérité.</li>
  <li><b>Fenêtre de contexte :</b> mesurée en <b>tokens</b> ; plus grande = plus cohérent, mais plus de calcul et de temps.</li>
  <li><b>Non-déterminisme :</b> inférence <b>probabiliste</b> + <b>hyperparamètres</b>.</li>
  <li><b>Instruction-tuned :</b> affiné avec des paires <b>prompt / réponse attendue</b>.</li>
  <li><b>Vision-langage :</b> un <b>sous-ensemble</b> des modèles multimodaux.</li>
</ul>""",
        "narration": (
            "Avant de terminer, voici les pièges les plus fréquents. "
            "Les features sont choisies à la main en machine learning classique, mais apprises automatiquement "
            "en deep learning. "
            "L'avantage clé de l'IA générative est d'utiliser des modèles pré-entraînés, sans phase "
            "d'entraînement supplémentaire. "
            "Plausible ne veut pas dire correct. "
            "La fenêtre de contexte se mesure en tokens : plus grande, elle améliore la cohérence, mais coûte "
            "plus de calcul et de temps. "
            "Le non-déterminisme vient de l'inférence probabiliste et des hyperparamètres. "
            "Un modèle ajusté aux instructions est affiné avec des paires prompt et réponse attendue. "
            "Et les modèles vision-langage sont un sous-ensemble des modèles multimodaux."
        ),
    },
    {
        "section": "Quiz",
        "title": "À vous de jouer",
        "body": """
<div class="quiz">
  <div class="q"><b>Question 1.</b> Le même prompt donne deux réponses différentes. Pourquoi ?<ol type="A"><li>Le modèle a été réentraîné entre les deux</li><li>L'inférence est probabiliste et dépend des hyperparamètres</li><li>La fenêtre de contexte a été vidée</li></ol></div>
  <div class="q"><b>Question 2.</b> Vous voulez générer des cas de test chaque nuit, automatiquement, dans votre outil de test. Que choisir ?<ol type="A"><li>Un chatbot d'IA</li><li>Une application intégrant un LLM par API</li><li>Un système d'IA symbolique</li></ol></div>
</div>
<p class="note">Mettez la vidéo en pause et répondez.</p>""",
        "narration": (
            "À vous de jouer avec deux questions. Mettez la vidéo en pause si vous voulez réfléchir. "
            "Question un : le même prompt donne deux réponses différentes. Pourquoi ? "
            "A : le modèle a été réentraîné entre les deux. B : l'inférence est probabiliste et dépend des "
            "hyperparamètres. C : la fenêtre de contexte a été vidée. "
            "Question deux : vous voulez générer des cas de test chaque nuit, automatiquement, dans votre "
            "outil de test. Que choisir ? A : un chatbot. B : une application qui intègre un LLM par une API. "
            "C : un système d'IA symbolique."
        ),
    },
    {
        "section": "Quiz",
        "title": "Les réponses",
        "body": """
<div class="quiz">
  <div class="q ok"><b>Question 1 → B.</b> Le non-déterminisme vient de la nature <b>probabiliste</b> de l'inférence et des <b>hyperparamètres</b>. Le modèle n'est pas réentraîné à chaque requête.</div>
  <div class="q ok"><b>Question 2 → B.</b> Une tâche <b>bien définie</b>, <b>automatisée</b> et intégrée aux outils correspond à une <b>application intégrant un LLM par API</b>. Le chatbot convient plutôt aux échanges ponctuels.</div>
</div>
<div class="hero compact"><p class="lead">Prochaine étape : le <b>chapitre 2</b>, le prompt engineering.</p><p class="note">Entraînez-vous ensuite dans l'application : cours, questions et flashcards du chapitre 1.</p></div>""",
        "narration": (
            "Voici les réponses. Question un : la bonne réponse est B. Le non-déterminisme vient de la nature "
            "probabiliste de l'inférence et du réglage des hyperparamètres. Le modèle n'est pas réentraîné à "
            "chaque requête. Question deux : la réponse est B. Une tâche bien définie, automatisée et intégrée "
            "aux outils correspond à une application qui intègre un LLM par une API. Le chatbot convient "
            "plutôt aux échanges ponctuels. "
            "Bravo, vous avez fait le tour du chapitre un ! Pour ancrer ces notions, entraînez-vous avec les "
            "questions et les flashcards du chapitre un dans l'application. Rendez-vous ensuite au chapitre "
            "deux, consacré au prompt engineering."
        ),
    },
]
