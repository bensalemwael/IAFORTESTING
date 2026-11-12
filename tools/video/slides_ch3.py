# Contenu de la vidéo : CT-GenAI v1.1, chapitre 3 (risques de l'IA générative). Synthèse originale des sections 3.1 à 3.4.
# Étapes : "say" = voix principale, "voice": "max" = Max le testeur, "pause" = étape muette, "vars" = variables.

CHAPTER = "CT-GenAI v1.1 · Chapitre 3"


def countdown(**extra):
    return [{"pause": 1.0, "vars": {"count": n, **extra}} for n in ("3", "2", "1")]


SLIDES = [
    {
        "section": "", "title": "",
        "body": """
<div class="hero">
  <p class="kicker">ISTQB® CT-GenAI v1.1 — Chapitre 3</p>
  <h1>Les risques de l'IA générative<br>et comment les maîtriser</h1>
  <p class="lead" data-s="1">Plausible ne veut pas dire correct… ni sûr.</p>
  <div class="chips" data-s="2"><span>160 minutes</span><span>9 objectifs</span><span>1 objectif K3 : repérer les défauts</span></div>
</div>""",
        "steps": [
            {"say": "Bienvenue dans le chapitre trois. Après les super-pouvoirs de l'IA générative, place à ses points faibles."},
            {"say": "Vous vous souvenez ? Plausible ne veut pas dire correct. Et on va voir que ça ne veut pas dire sûr non plus."},
            {"say": "Cent soixante minutes de cours, neuf objectifs, dont un K trois : savoir repérer les défauts dans une réponse d'IA."},
        ],
    },
    {
        "section": "Plan", "title": "Quatre familles de risques",
        "body": """
<div class="cards4">
  <div class="c" data-s="0"><div class="ic">🌀</div><h3>3.1 Fiabilité</h3><p>Hallucinations, erreurs de raisonnement, biais, non-déterminisme</p></div>
  <div class="c" data-s="1"><div class="ic">🔐</div><h3>3.2 Confidentialité et sécurité</h3><p>Données sensibles, attaques, protections</p></div>
  <div class="c" data-s="2"><div class="ic">🌍</div><h3>3.3 Environnement</h3><p>Énergie et émissions de CO₂</p></div>
  <div class="c" data-s="3"><div class="ic">⚖️</div><h3>3.4 Réglementation</h3><p>Lois, normes et cadres de bonnes pratiques</p></div>
</div>""",
        "steps": [
            {"say": "Quatre familles de risques. D'abord la fiabilité : hallucinations, erreurs de raisonnement, biais et non-déterminisme."},
            {"say": "Ensuite, la confidentialité et la sécurité des données."},
            {"say": "Puis l'impact environnemental."},
            {"say": "Et enfin, les lois, normes et cadres de bonnes pratiques."},
        ],
    },
    {
        "section": "3.1.1", "title": "Trois défauts typiques des LLM",
        "body": """
<div class="cards3">
  <div class="c" data-s="0"><div class="ic">👻</div><h3>Hallucination</h3><p>Une sortie <b>factuellement fausse</b> ou <b>hors sujet</b>, qui a pourtant l'air crédible</p></div>
  <div class="c" data-s="1"><div class="ic">🧮</div><h3>Erreur de raisonnement</h3><p>Une <b>logique mal interprétée</b> : cause et effet, conditions, étapes successives</p></div>
  <div class="c" data-s="2"><div class="ic">⚖️</div><h3>Biais</h3><p>Une préférence venue des <b>données d'entraînement</b> pour certaines informations ou hypothèses</p></div>
</div>
<div class="trap" data-s="3"><b>Origine :</b> les données d'entraînement et les limites du transformeur. <b>Difficulté :</b> à cause du non-déterminisme, un défaut corrigé dans une conversation peut <b>réapparaître</b> dans une autre.</div>""",
        "steps": [
            {"say": "Trois défauts typiques. Un : l'hallucination. Le modèle produit quelque chose de faux ou hors sujet, mais qui a l'air tout à fait crédible."},
            {"say": "Deux : l'erreur de raisonnement. Le modèle se trompe dans une logique : une relation de cause à effet, une condition, ou une suite d'étapes."},
            {"say": "Trois : le biais. Le modèle favorise certaines informations ou hypothèses, à cause des données sur lesquelles il a été entraîné."},
            {"say": "Ces défauts viennent des données d'entraînement et des limites du transformeur. Et le non-déterminisme complique tout : un défaut qui semble corrigé peut revenir dans une autre conversation."},
        ],
    },
    {
        "section": "3.1.1", "title": "L'hallucination en action",
        "body": """
<div class="split">
  <div class="box" data-s="0"><h3>📝 User story : 3 critères d'acceptation</h3><ul><li>CA1 : connexion avec e-mail et mot de passe</li><li>CA2 : message d'erreur si mot de passe faux</li><li>CA3 : blocage après 3 échecs</li></ul></div>
  <div class="box" data-s="1"><h3>🤖 Réponse du LLM</h3><ul><li>TC1 → CA1 ✔</li><li>TC2 → CA2 ✔</li><li>TC3 → CA3 ✔</li><li data-s="2" style="color:#b3261e"><b style="color:#b3261e">TC4 → « CA4 : connexion par empreinte digitale »</b> ✘ n'existe pas !</li></ul></div>
</div>
<p class="note" data-s="3">Autres formes : cas de test <b>fictifs</b> ou hors sujet, scripts <b>incorrects ou qui ne fonctionnent pas</b>.</p>""",
        "steps": [
            {"say": "Exemple. Une user story avec trois critères d'acceptation."},
            {"say": "Le modèle propose des cas de test. Les trois premiers correspondent bien aux critères."},
            {"say": "Mais le quatrième vérifie un critère d'empreinte digitale qui n'existe nulle part ! C'est une hallucination : un test qui vérifie un critère d'acceptation inexistant."},
            {"say": "Elle peut aussi prendre la forme de cas de test fictifs, ou de scripts faux qui ne fonctionnent pas."},
        ],
    },
    {
        "section": "3.1.1", "title": "Erreur de raisonnement et biais",
        "body": """
<div class="split">
  <div class="box warn" data-s="0"><h3>🧮 Erreur de raisonnement</h3><p>Le LLM ne raisonne pas vraiment : il <b>reconnaît des motifs</b>.</p><div class="code" data-s="1">TC-B dépend de TC-A
Ordre proposé : TC-B ➜ TC-A   ✘</div><p class="ex">Tâches à risque : planification des tests, priorisation, calculs</p></div>
  <div class="box warn" data-s="2"><h3>⚖️ Biais</h3><p>Hérité des <b>données d'entraînement</b>.</p><div class="code" data-s="3">Données de test générées :
John, Mary, Peter, Susan…</div><p class="ex">Modèle entraîné surtout en anglais : d'autres perspectives sont sous-représentées</p></div>
</div>""",
        "steps": [
            {"say": "Les erreurs de raisonnement viennent de ce que le modèle ne raisonne pas vraiment : il reconnaît des motifs."},
            {"say": "Exemple : le test B dépend du test A, mais le modèle propose d'exécuter B avant A. La planification et la priorisation des tests sont des tâches à risque, tout comme les calculs."},
            {"say": "Les biais, eux, viennent des données d'entraînement. Un modèle entraîné surtout en anglais peut sous-représenter d'autres perspectives."},
            {"say": "Résultat : des données de test où tous les prénoms sont anglo-saxons, par exemple."},
        ],
    },
    {
        "section": "Quiz K3", "title": "Quel défaut ?",
        "body": """
<div class="qa">
  <p class="q" data-s="0">Le script généré appelle <b>login_securise()</b>, une fonction qui n'existe pas.</p>
  <div class="answer" data-s="4">➜ <b>Hallucination</b> : un élément inventé.</div>
  <p class="q" data-s="5">Le LLM calcule l'effort total en additionnant mal les estimations de 5 tâches.</p>
  <div class="answer" data-s="9">➜ <b>Erreur de raisonnement</b> : une logique ou un calcul faux.</div>
  <p class="q" data-s="10">Les tests générés sont tous fonctionnels : aucun test de performance ni de sécurité.</p>
  <div class="answer" data-s="14">➜ <b>Biais</b> sur les types de test : le non-fonctionnel est sous-représenté.</div>
</div>""",
        "steps": [
            {"say": "Quiz K trois ! Le script généré appelle une fonction login sécurisé qui n'existe pas. Quel défaut ?"},
            *countdown(),
            {"say": "Une hallucination : le modèle a inventé un élément."},
            {"say": "Deuxième cas : le modèle calcule l'effort total de test en additionnant mal cinq estimations."},
            *countdown(),
            {"say": "Une erreur de raisonnement."},
            {"say": "Troisième cas : tous les tests générés sont fonctionnels. Aucun test de performance, aucun test de sécurité."},
            *countdown(),
            {"say": "Un biais sur les types de test : le non-fonctionnel est sous-représenté. Le syllabus cite exactement ce cas."},
        ],
    },
    {
        "section": "3.1.2", "title": "Comment les détecter ?",
        "body": """
<div class="cards3">
  <div class="c" data-s="0"><h3>👻 Hallucinations</h3><ul><li><b>Vérification croisée</b> avec la documentation, les exigences, le comportement connu</li><li>Avis d'un <b>expert du domaine</b></li><li><b>Contrôles de cohérence</b> entre les sorties</li></ul></div>
  <div class="c" data-s="1"><h3>🧮 Raisonnement</h3><ul><li><b>Validation logique</b> en revue : cohérence, enchaînement</li><li><b>Tester la sortie</b> : exécuter les tests ou scripts générés sur l'objet de test</li></ul></div>
  <div class="c" data-s="2"><h3>⚖️ Biais</h3><ul><li>Vérifier que le testware respecte la <b>stratégie</b> et la <b>couverture</b></li><li>Chercher les <b>types de test</b> sous-représentés</li></ul></div>
</div>
<div class="trap" data-s="3"><b>Revue humaine</b>, souvent aidée d'outils automatisés. L'effort dépend du <b>niveau de risque</b> de la tâche.</div>""",
        "steps": [
            {"say": "Comment repérer ces défauts ? Pour les hallucinations : la vérification croisée avec la documentation et les exigences, l'avis d'un expert du domaine, et des contrôles de cohérence."},
            {"say": "Pour les erreurs de raisonnement : la validation logique en revue, et surtout, tester la sortie. Par exemple, exécuter les scripts générés sur l'objet de test."},
            {"say": "Pour les biais : vérifier que le testware respecte la stratégie de test et la couverture, et chercher les types de test oubliés."},
            {"say": "Tout cela passe par une revue humaine, souvent aidée d'outils. Et l'effort dépend du niveau de risque."},
        ],
    },
    {
        "section": "3.1.3", "title": "Cinq techniques pour réduire ces défauts",
        "body": """
<div class="caps">
  <div data-s="0"><i class="n">1</i><span>Fournir un <b>contexte complet</b> : toutes les informations utiles dans le prompt</span></div>
  <div data-s="1"><i class="n">2</i><span><b>Découper</b> les prompts complexes (chaînage) et vérifier chaque étape</span></div>
  <div data-s="2"><i class="n">3</i><span>Utiliser des <b>formats de données clairs</b> et structurés</span></div>
  <div data-s="3"><i class="n">4</i><span>Choisir le <b>modèle adapté</b> à la tâche</span></div>
  <div data-s="4"><i class="n">5</i><span><b>Comparer</b> les résultats de plusieurs modèles</span></div>
</div>
<p class="note" data-s="5">Au chapitre 4 : deux techniques complémentaires, le <b>RAG</b> et le <b>fine-tuning</b>.</p>""",
        "steps": [
            {"say": "Ces défauts apparaissent surtout quand le prompt est mal conçu ou que le contexte manque. Première parade : un contexte complet."},
            {"say": "Deux : découper les prompts complexes avec le chaînage, et vérifier chaque étape. On attrape ainsi les erreurs de raisonnement tôt."},
            {"say": "Trois : des formats de données clairs, faciles à interpréter."},
            {"say": "Quatre : choisir le modèle adapté à la tâche."},
            {"say": "Cinq : comparer les réponses de plusieurs modèles."},
            {"say": "Et le chapitre quatre ajoutera deux techniques : le RAG et le fine-tuning."},
        ],
    },
    {
        "section": "3.1.4", "title": "Réduire le non-déterminisme",
        "body": """
<div class="split">
  <div class="box" data-s="0"><h3>🌡️ Baisser la température</h3><p>La distribution de probabilités se <b>resserre</b> : moins de hasard, des réponses plus <b>constantes</b>.</p><p data-s="1">⚠️ Mais aussi moins de <b>créativité</b> et de <b>diversité</b> : réponses plus répétitives.</p></div>
  <div class="box" data-s="2"><h3>🎲 Fixer une graine (seed)</h3><p>Certaines implémentations permettent de fixer la <b>graine aléatoire</b> : même suite pseudo-aléatoire, meilleure <b>reproductibilité</b>.</p></div>
</div>
<div class="trap" data-s="3"><b>À retenir :</b> la reproductibilité totale n'est <b>jamais garantie</b>, et les <b>sorties longues</b> varient davantage.</div>""",
        "steps": [
            {"say": "Objectif trois point un point quatre : le non-déterminisme. Premier levier : baisser la température. Le modèle choisit plus souvent les mots les plus probables, donc les réponses sont plus constantes."},
            {"say": "Le revers : moins de créativité et de diversité. Les réponses deviennent répétitives."},
            {"say": "Deuxième levier : fixer une graine aléatoire, quand l'outil le permet. On rejoue alors la même suite pseudo-aléatoire."},
            {"say": "Mais attention, piège d'examen : la reproductibilité complète n'est jamais garantie. Et plus la sortie est longue, plus elle risque de varier."},
        ],
    },
    {
        "section": "3.2.1", "title": "Confidentialité et sécurité : les risques",
        "body": """
<div class="split">
  <div class="box" data-s="0"><h3>🔏 Confidentialité</h3><ul><li><b>Exposition involontaire</b> de données sensibles dans les sorties</li><li><b>Perte de contrôle</b> : données stockées ou traitées sans consentement</li><li><b>Non-conformité</b> réglementaire, par exemple au <b>RGPD</b></li></ul></div>
  <div class="box" data-s="1"><h3>🛡️ Sécurité</h3><ul><li><b>Attaques</b> contre l'infrastructure de test : fuites, accès non autorisé</li><li><b>Exploitation</b> des vulnérabilités du LLM pour modifier son comportement ou extraire des données</li><li><b>Entrées malveillantes</b> pour tromper le modèle</li></ul></div>
</div>
<div class="bubble" data-s="2"><span class="speaker">Max</span>« J'ai collé la base clients de production dans le chatbot pour générer des tests… c'est grave ? »</div>""",
        "steps": [
            {"say": "Section trois point deux. Côté confidentialité, trois risques : l'exposition involontaire de données sensibles dans les réponses, la perte de contrôle sur l'usage des données, et la non-conformité à des règles comme le RGPD."},
            {"say": "Côté sécurité : des attaques contre l'infrastructure de test, l'exploitation des vulnérabilités du modèle, et des données d'entrée malveillantes destinées à le tromper."},
            {"say": "J'ai collé la base clients de production dans le chatbot pour générer des tests. C'est grave ?", "voice": "max"},
        ],
    },
    {
        "section": "3.2.2", "title": "Quatre vecteurs d'attaque",
        "body": """
<div class="metrics" style="grid-template-columns:repeat(2,1fr)">
  <div class="c" data-s="0"><h3>Manipulation du contexte</h3><p>Des requêtes conçues pour <b>extraire des données d'entraînement confidentielles</b></p><p class="ex">Des prompts très longs saturent la fenêtre de contexte : le modèle révèle des fragments de ses données</p></div>
  <div class="c" data-s="1"><h3>Manipulation de requête</h3><p>Des données qui <b>perturbent la réponse</b></p><p class="ex">Une image entraîne l'IA dans un autre contexte et provoque des hallucinations sur des critères d'acceptation</p></div>
  <div class="c" data-s="2"><h3>Empoisonnement des données</h3><p>Manipuler les <b>données d'entraînement</b></p><p class="ex">De fausses évaluations lors de la notation d'un rapport de test généré</p></div>
  <div class="c" data-s="3"><h3>Génération de code malveillant</h3><p>Pousser le LLM à créer des <b>portes dérobées</b></p><p class="ex">Du code qui ouvre un canal vers une adresse IP malveillante</p></div>
</div>""",
        "steps": [
            {"say": "Oui, Max, c'est un vrai risque. Voyons les quatre vecteurs d'attaque du syllabus. Un : la manipulation du contexte. Le but est d'extraire des données d'entraînement confidentielles, par exemple en saturant la fenêtre de contexte avec des prompts très longs."},
            {"say": "Deux : la manipulation de requête. On introduit des données qui perturbent la réponse, comme une image qui entraîne l'IA dans un autre contexte et la fait halluciner."},
            {"say": "Trois : l'empoisonnement des données. On manipule les données d'entraînement, par exemple avec de fausses évaluations."},
            {"say": "Quatre : la génération de code malveillant. On pousse le modèle à créer une porte dérobée, comme un appel vers une adresse IP malveillante."},
        ],
    },
    {
        "section": "Quiz éclair", "title": "Piège : contexte ou requête ?",
        "body": """
<div class="qa">
  <p class="q" data-s="0">Une capture d'écran piégée pousse l'IA à inventer des critères d'acceptation.</p>
  <div class="opts" data-s="0"><div>Manipulation du contexte</div><div class="{{c1}}">Manipulation de requête</div><div>Empoisonnement</div></div>
  <p class="q" data-s="5">Un attaquant envoie des prompts énormes pour faire « déborder » le modèle et lui soutirer des données d'entraînement.</p>
  <div class="opts" data-s="5"><div class="{{c2}}">Manipulation du contexte</div><div>Manipulation de requête</div><div>Code malveillant</div></div>
</div>""",
        "steps": [
            {"say": "Piège classique ! Une capture d'écran piégée pousse l'IA à inventer des critères d'acceptation. Manipulation du contexte, ou de requête ?"},
            *countdown(),
            {"say": "Manipulation de requête ! Le mot contexte est trompeur : ce sont des données d'entrée qui perturbent la réponse.", "vars": {"c1": "good"}},
            {"say": "Et ici : un attaquant envoie des prompts énormes pour faire déborder le modèle et lui soutirer ses données d'entraînement.", "vars": {"c1": "good"}},
            *countdown(c1="good"),
            {"say": "Manipulation du contexte : le but est d'extraire des données d'entraînement confidentielles.", "vars": {"c1": "good", "c2": "good"}},
        ],
    },
    {
        "section": "3.2.3", "title": "Protéger les données",
        "body": """
<div class="cards4">
  <div class="c" data-s="0"><div class="ic">✂️</div><h3>Minimisation</h3><p>Pas de données sensibles sauf si la loi le permet, et seulement le <b>nécessaire</b></p></div>
  <div class="c" data-s="1"><div class="ic">🎭</div><h3>Anonymisation et pseudonymisation</h3><p><b>Masquer ou remplacer</b> les informations sensibles</p></div>
  <div class="c" data-s="2"><div class="ic">🔒</div><h3>Stockage et transfert sécurisés</h3><p><b>Chiffrement</b> fort et <b>contrôles d'accès</b></p></div>
  <div class="c" data-s="3"><div class="ic">🎓</div><h3>Formation</h3><p>Programmes et règles pour un usage <b>responsable</b></p></div>
</div>
<div class="trap" data-s="4"><b>Nuance RGPD :</b> il n'interdit pas explicitement l'IA générative, mais ses garanties limitent ce qu'on peut faire : licéité, limitation des finalités de collecte, de traitement et de conservation.</div>""",
        "steps": [
            {"say": "Comment se protéger ? Un : la minimisation. On évite les données sensibles, sauf si la loi le permet, et on n'utilise que le strict nécessaire."},
            {"say": "Deux : l'anonymisation et la pseudonymisation, qui masquent ou remplacent les informations sensibles. C'est ce que Max aurait dû faire !"},
            {"say": "Trois : un stockage et une transmission sécurisés, avec du chiffrement et des contrôles d'accès."},
            {"say": "Quatre : la formation et des règles claires pour un usage responsable."},
            {"say": "Et une nuance : le RGPD n'interdit pas explicitement l'IA générative. Mais ses garanties limitent ce qu'on peut faire, par exemple sur la licéité et les finalités du traitement."},
        ],
    },
    {
        "section": "3.2.3", "title": "Autres protections et environnement sécurisé",
        "body": """
<div class="split">
  <div class="box" data-s="0"><h3>Bonnes pratiques</h3><ul><li><b>Revue humaine</b> systématique des sorties</li><li><b>Comparer</b> avec un autre LLM</li><li><b>Audits</b> de sécurité et évaluations de vulnérabilités</li><li>Rester à jour des <b>bonnes pratiques</b></li></ul></div>
  <div class="box" data-s="1"><h3>Environnement, selon la confidentialité</h3><div class="flow" style="flex-direction:column;gap:10px">
    <div class="st">☁️ Offre commerciale <b>sécurisée</b> d'un fournisseur</div>
    <div class="st">🏢 LLM dans un <b>cloud sécurisé</b></div>
    <div class="st">🖥️ LLM installé <b>dans l'infrastructure</b> de l'organisation</div></div></div>
</div>
<p class="note" data-s="2">Combiner les mesures, et impliquer <b>experts sécurité</b>, <b>juristes</b>, <b>CTO</b> ou <b>RSSI (CISO)</b>.</p>""",
        "steps": [
            {"say": "D'autres protections complètent ces mesures : une revue humaine systématique, la comparaison avec un autre modèle, des audits de sécurité réguliers, et une veille sur les bonnes pratiques."},
            {"say": "Selon le niveau de confidentialité, on choisit aussi l'environnement : une offre commerciale sécurisée, un LLM dans un cloud sécurisé, ou un LLM installé dans l'infrastructure de l'organisation."},
            {"say": "Ces mesures se combinent. Et on implique les experts sécurité, les juristes, le directeur technique ou le responsable de la sécurité des systèmes d'information."},
        ],
    },
    {
        "section": "3.3.1", "title": "L'impact environnemental",
        "body": """
<div class="split">
  <div class="box" data-s="0"><h3>⚡ Pourquoi ça consomme</h3><p>Entraîner et utiliser des LLM mobilise beaucoup de <b>ressources de calcul</b> : appareils, réseaux, centres de données.</p><p>La consommation dépend de la <b>complexité de la tâche</b> et des <b>ressources</b> nécessaires.</p></div>
  <div class="box" data-s="1"><h3>📱 Ordre de grandeur</h3><p>🖼️ 1 image avec un modèle puissant ≈ <b>une recharge complète</b> de smartphone</p><p>📝 1 texte ≈ <b>un petit pourcentage</b> de recharge</p></div>
</div>
<div class="trap" data-s="2"><b>Effet cumulé :</b> une requête semble négligeable, mais des millions d'utilisateurs produisent des émissions de CO₂ importantes. Bonne pratique : <b>limiter les interactions inutiles</b>.</div>""",
        "steps": [
            {"say": "Section trois point trois : l'environnement. Les LLM mobilisent énormément de calcul, dans les appareils, les réseaux et les centres de données. La consommation dépend de la complexité de la tâche et des ressources utilisées."},
            {"say": "Un ordre de grandeur cité par le syllabus : générer une image avec un modèle puissant peut consommer autant qu'une recharge complète de smartphone. Un texte, seulement un petit pourcentage."},
            {"say": "Une requête isolée semble négligeable, mais l'effet cumulé de millions d'utilisateurs est considérable. La bonne pratique : limiter les interactions inutiles."},
        ],
    },
    {
        "section": "3.4.1", "title": "Lois, normes et cadres à connaître",
        "body": """
<table class="grid tbl3">
  <tr><th>Nom</th><th>Type</th><th>En une phrase</th></tr>
  <tr data-s="0"><td>ISO/IEC 42001:2023</td><td>Norme</td><td>Exigences pour un <b>système de management</b> de l'IA dans l'organisation</td></tr>
  <tr data-s="1"><td>ISO/IEC 23053:2022</td><td>Norme</td><td>Cadre pour les systèmes d'IA utilisant le <b>machine learning</b> : cycle de vie, sûreté, transparence</td></tr>
  <tr data-s="2"><td>EU AI Act</td><td>Règlement</td><td>Cadre <b>légal</b> européen qui classe les applications d'IA par <b>niveau de risque</b></td></tr>
  <tr data-s="3"><td>NIST AI RMF</td><td>Cadre (États-Unis)</td><td>Lignes directrices de gestion des risques : <b>équité</b>, transparence, sécurité</td></tr>
</table>
<p class="note" data-s="4">Niveau <b>K1</b> : savoir les reconnaître. Et rester à jour, car tout évolue vite.</p>""",
        "steps": [
            {"say": "Section trois point quatre, niveau K un : reconnaître quatre textes. ISO IEC quarante-deux mille un : une norme pour le système de management de l'IA dans une organisation."},
            {"say": "ISO IEC vingt-trois mille cinquante-trois : une norme qui donne un cadre aux systèmes d'IA utilisant le machine learning, avec le cycle de vie, la sûreté et la transparence."},
            {"say": "L'AI Act européen : un règlement, donc une loi, qui classe les applications d'IA par niveau de risque."},
            {"say": "Et le NIST AI RMF : un cadre américain de gestion des risques, centré sur l'équité, la transparence et la sécurité."},
            {"say": "Il suffit de savoir les reconnaître. Et de rester à jour, car ce paysage évolue vite."},
        ],
    },
    {
        "section": "Quiz éclair", "title": "Quel texte ?",
        "body": """
<div class="qa">
  <p class="q" data-s="0">Quel texte est un <b>règlement</b> qui classe les applications d'IA par <b>niveau de risque</b> ?</p>
  <div class="answer" data-s="4">➜ <b>EU AI Act</b></div>
  <p class="q" data-s="5">Quel texte définit les exigences d'un <b>système de management</b> de l'IA ?</p>
  <div class="answer" data-s="9">➜ <b>ISO/IEC 42001:2023</b></div>
</div>""",
        "steps": [
            {"say": "Quiz éclair. Quel texte est un règlement qui classe les applications d'IA par niveau de risque ?"},
            *countdown(),
            {"say": "L'AI Act européen."},
            {"say": "Et lequel définit les exigences d'un système de management de l'IA ?"},
            *countdown(),
            {"say": "La norme ISO IEC quarante-deux mille un."},
        ],
    },
    {
        "section": "Révision", "title": "Les 7 réflexes du chapitre 3",
        "body": """
<ul class="traps">
  <li data-s="0"><b>Hallucination</b> = inventé · <b>Raisonnement</b> = logique fausse · <b>Biais</b> = hérité des données d'entraînement.</li>
  <li data-s="1"><b>Détecter :</b> vérification croisée, expert, cohérence · validation logique, exécuter la sortie · revue de couverture.</li>
  <li data-s="2"><b>Réduire :</b> contexte complet, chaînage, formats clairs, bon modèle, comparer les modèles.</li>
  <li data-s="3"><b>Non-déterminisme :</b> baisser la température, fixer une graine ; reproductibilité jamais garantie.</li>
  <li data-s="4"><b>Attaques :</b> contexte = extraire les données d'entraînement · requête = perturber la sortie.</li>
  <li data-s="5"><b>Protéger :</b> minimiser, anonymiser, chiffrer, former ; RGPD n'interdit pas l'IA mais encadre.</li>
  <li data-s="6"><b>Textes :</b> 42001 = management · 23053 = cadre ML · AI Act = risques · NIST = cadre américain.</li>
</ul>""",
        "steps": [
            {"say": "Récapitulons en sept réflexes. Un : hallucination, erreur de raisonnement, biais."},
            {"say": "Deux : les moyens de détection propres à chaque défaut."},
            {"say": "Trois : les cinq techniques pour les réduire."},
            {"say": "Quatre : température et graine aléatoire contre le non-déterminisme, sans garantie totale."},
            {"say": "Cinq : ne confondez pas manipulation du contexte et manipulation de requête."},
            {"say": "Six : minimiser, anonymiser, chiffrer et former."},
            {"say": "Sept : les quatre textes de référence."},
        ],
    },
    {
        "section": "Fin", "title": "",
        "body": """
<div class="hero">
  <div class="ic big">🛡️</div>
  <h1 style="font-size:84px">Bravo, chapitre 3 terminé !</h1>
  <div class="bubble" data-s="1"><span class="speaker">Max</span>« Promis : je pseudonymise mes données et je vérifie chaque sortie. »</div>
  <p class="lead" data-s="2">À faire : les questions et flashcards du chapitre 3 dans l'application.</p>
</div>""",
        "steps": [
            {"say": "Bravo, vous avez terminé le chapitre trois !"},
            {"say": "Promis : je pseudonymise mes données, et je vérifie chaque sortie de l'IA.", "voice": "max"},
            {"say": "Parfait, Max. Entraînez-vous avec les questions et les flashcards du chapitre trois. Prochaine étape : le chapitre quatre, l'infrastructure de test propulsée par les LLM."},
        ],
    },
]
