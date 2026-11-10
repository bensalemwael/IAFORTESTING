// Fiches de révision CT-GenAI v1.1 : synthèse personnelle en français, à lire avec le syllabus officiel.
(function (root) {
  const notes = {
    1: `
<h3>Le spectre de l'IA</h3>
<table><tr><th>Type</th><th>Principe</th></tr>
<tr><td>IA symbolique</td><td>Règles et symboles logiques</td></tr>
<tr><td>ML classique</td><td>Données, sélection de features, entraînement</td></tr>
<tr><td>Deep learning</td><td>Réseaux de neurones, features apprises automatiquement</td></tr>
<tr><td>IA générative</td><td>Deep learning créant du contenu nouveau, modèles préentraînés</td></tr></table>
<p>Atout de la GenAI pour le test : des modèles préentraînés utilisables sans phase d'entraînement supplémentaire, avec les risques vus au chapitre 3.</p>
<h3>Bases des LLM</h3>
<ul><li><b>Tokenization</b> : découpe en tokens (caractère, partie de mot, mot).</li>
<li><b>Embeddings</b> : vecteurs ; les sens proches sont proches dans l'espace.</li>
<li><b>Transformer</b> : prédit le token suivant. <em>Plausible n'est pas forcément correct.</em></li>
<li><b>Fenêtre de contexte</b> : mesurée en tokens ; plus grande, elle augmente complexité et temps de calcul.</li>
<li><b>Non-déterminisme</b> : inférence probabiliste et hyperparamètres.</li></ul>
<h3>Trois catégories de LLM</h3>
<ul><li><b>Fondation</b> : généraliste, à adapter.</li>
<li><b>Instruction-tuned</b> : affiné avec des paires prompt / réponse.</li>
<li><b>Raisonnement</b> : inférence logique et problèmes en plusieurs étapes.</li></ul>
<p><b>Multimodal / vision-langage</b> : analyse captures et maquettes avec du texte, pour détecter des écarts entre attendu et visuel.</p>
<h3>Capacités pour le test</h3>
<p>Analyse des exigences, création de cas de test, oracle, données de test, automatisation, analyse des résultats, création de testware.</p>
<table><tr><th>Chatbot IA</th><th>Application de test à base de LLM</th></tr>
<tr><td>Conversationnel, retour immédiat, exploration, onboarding</td><td>Intégration via API, tâches définies et automatisées, personnalisation, passage à l'échelle</td></tr></table>
<p class="trap">Piège : le prompt engineering reste nécessaire dans les deux cas.</p>`,
    2: `
<h3>Les six composants d'un prompt structuré</h3>
<ol><li><b>Rôle</b> : perspective adoptée (testeur, test manager…).</li><li><b>Contexte</b> : objet de test, fonctionnalité.</li><li><b>Instruction</b> : tâche, de façon claire et impérative.</li><li><b>Données d'entrée</b> : stories, critères, captures, code, exemples.</li><li><b>Contraintes</b> : restrictions d'application.</li><li><b>Format de sortie</b> : structure attendue.</li></ol>
<h3>Choisir la technique (§2.2.5)</h3>
<table><tr><th>Technique</th><th>Quand</th><th>Exemples</th></tr>
<tr><td><b>Prompt chaining</b></td><td>Tâche complexe, précision, vérification humaine à chaque étape</td><td>Analyse, conception, automatisation</td></tr>
<tr><td><b>Few-shot</b></td><td>Tâche répétitive, format contraint</td><td>Gherkin, keyword-driven, rapports formatés</td></tr>
<tr><td><b>Meta prompting</b></td><td>Tâche nouvelle, création du prompt</td><td>Analyse de rapports, détection d'anomalies</td></tr></table>
<p>Zero-shot : aucun exemple. One-shot : un exemple. Few-shot : plusieurs. Les techniques se combinent.</p>
<h3>System prompt / user prompt</h3>
<p>Le <b>system prompt</b> reste constant et cadre le comportement ; le <b>user prompt</b> change à chaque interaction. Le modèle considère les deux.</p>
<h3>Application au processus de test</h3>
<ul><li><b>Analyse</b> : défauts du test basis, conditions de test, priorisation par le risque, couverture, suggestion de techniques.</li>
<li><b>Conception et implémentation</b> : cas de test, données synthétiques, scripts, planification d'exécution.</li>
<li><b>Régression</b> : keyword-driven, analyse d'impact, self-healing, rapports, analyse de cause racine.</li>
<li><b>Pilotage et contrôle</b> : tendances et alertes, repriorisation, rapports de clôture, tableaux de bord.</li></ul>
<h3>Métriques d'évaluation</h3>
<p>Exactitude, précision, rappel, pertinence et adéquation au contexte, diversité, taux de succès d'exécution, efficience temporelle.</p>
<p>Non-déterminisme : baser ces métriques sur des données <b>statistiquement pertinentes</b>.</p>
<h3>Raffiner les prompts</h3>
<p>Modification itérative, A/B testing de prompts, analyse des sorties, intégration des retours utilisateurs, ajustement de la longueur et de la spécificité.</p>
<p class="trap">Piège K3 : identifiez d'abord ce que demande le scénario. Vérification à chaque étape → chaining. Format répétitif → few-shot. Ne sait pas comment formuler → meta.</p>`,
    3: `
<h3>Trois défauts, trois détections</h3>
<table><tr><th>Défaut</th><th>Définition</th><th>Détection</th></tr>
<tr><td><b>Hallucination</b></td><td>Faux ou hors sujet (critère inexistant, script non fonctionnel)</td><td>Recoupement, experts métier, contrôles de cohérence</td></tr>
<tr><td><b>Erreur de raisonnement</b></td><td>Logique mal interprétée (calcul, priorisation)</td><td>Validation logique, test des sorties</td></tr>
<tr><td><b>Biais</b></td><td>Issu des données d'entraînement (non-fonctionnel sous-représenté)</td><td>Revue par rapport à la stratégie et à la couverture</td></tr></table>
<h3>Atténuer</h3>
<p>Contexte complet, prompts découpés, formats de données clairs, modèle adapté, comparaison entre modèles. RAG et fine-tuning (chapitre 4) sont complémentaires.</p>
<p><b>Non-déterminisme</b> : baisser la température (moins de créativité), fixer une seed si disponible. La reproductibilité complète n'est pas garantie.</p>
<h3>Vecteurs d'attaque</h3>
<table><tr><th>Vecteur</th><th>Principe</th></tr>
<tr><td>Manipulation de contexte</td><td>Extraire des données d'entraînement confidentielles</td></tr>
<tr><td>Manipulation de requête</td><td>Introduire des données perturbant la sortie (image trompeuse)</td></tr>
<tr><td>Empoisonnement de données</td><td>Manipuler les données d'entraînement (fausses évaluations)</td></tr>
<tr><td>Génération de code malveillant</td><td>Faire produire des portes dérobées</td></tr></table>
<h3>Protection</h3>
<p>Minimisation, anonymisation et pseudonymisation, stockage et transmission sécurisés, formation, revue systématique, comparaison entre LLM, environnement sécurisé, audits, veille.</p>
<h3>Énergie</h3>
<p>La consommation dépend de la complexité de la tâche et des ressources. Générer une image consomme bien plus que du texte. Bonne pratique : limiter les interactions inutiles.</p>
<h3>Cadres à connaître</h3>
<table><tr><th>Référence</th><th>Type</th><th>Objet</th></tr>
<tr><td>ISO/IEC 42001:2023</td><td>Norme</td><td>Système de management de l'IA</td></tr>
<tr><td>ISO/IEC 23053:2022</td><td>Norme</td><td>Cadre pour systèmes IA utilisant le ML</td></tr>
<tr><td>EU AI Act</td><td>Réglementation</td><td>Classement par niveau de risque</td></tr>
<tr><td>NIST AI RMF</td><td>Cadre</td><td>Gestion des risques IA</td></tr></table>`,
    4: `
<h3>Architecture</h3>
<ul><li><b>Front-end</b> : interface du testeur.</li>
<li><b>Back-end</b> : authentification, récupération de données, préparation des prompts, post-traitement.</li>
<li><b>LLM</b> : service tiers via API ou modèle interne.</li>
<li><b>Sources</b> : bases relationnelles et bases vectorielles.</li></ul>
<h3>RAG</h3>
<ol><li>Préparation : découper en fragments (par exemple 256-512 tokens), nettoyer, encoder en embeddings, stocker.</li>
<li><b>Récupération</b> par similarité sémantique avec la requête.</li>
<li><b>Génération</b> à partir des fragments récupérés.</li></ol>
<p class="trap">Piège : le RAG enrichit le prompt, il ne réentraîne pas le modèle. Le fine-tuning, lui, modifie le modèle.</p>
<h3>Agents</h3>
<p>Ils agissent via des <b>outils</b>. Autonomes ou semi-autonomes (supervision périodique). Multi-agents : <b>orchestration</b> de rôles spécialisés. Mêmes défauts que les LLM : vérification automatisée ou semi-autonomie pour les tâches critiques.</p>
<h3>Fine-tuning</h3>
<p>Entraînement complémentaire sur un jeu ciblé. Défis : qualité des données, <b>surapprentissage</b>, <b>opacité</b>, ressources de calcul. S'applique aussi aux SLM, moins coûteux.</p>
<h3>LLMOps : trois approches</h3>
<table><tr><th>Approche</th><th>Points d'attention</th></tr>
<tr><td>Chatbot IA</td><td>Confidentialité, sécurité, coût, garanties du fournisseur</td></tr>
<tr><td>Outil de test avec GenAI</td><td>Idem, plus garanties de l'outil, coût-bénéfice</td></tr>
<tr><td>Développement interne</td><td>Contrôle complet, ressources, expertise, validation</td></tr></table>
<p>Ces approches ne s'excluent pas.</p>`,
    5: `
<h3>Shadow AI</h3>
<p>Usage sans approbation ni supervision. Risques : sécurité et confidentialité, conformité, propriété intellectuelle floue.</p>
<h3>Stratégie</h3>
<p>Objectifs mesurables, choix des LLM, qualité des données d'entrée, formation, métriques, règles de processus (données sensibles, transparence, quality gates avec revue).</p>
<h3>Sélection LLM / SLM</h3>
<p>Performance du modèle, potentiel de fine-tuning, coût récurrent, communauté et support.</p>
<h3>Trois phases d'adoption</h3>
<ol><li><b>Découverte</b> : formation, accès, premiers essais.</li>
<li><b>Initiation et définition des usages</b> : identifier, prioriser, évaluer.</li>
<li><b>Utilisation et itération</b> : intégration, suivi, mesure.</li></ol>
<p>Les phases peuvent se dérouler en parallèle selon les cas d'usage. Tenir compte des craintes pour l'emploi.</p>
<h3>Compétences et évolution</h3>
<ul><li>Testeur : prompt engineering, fenêtres de contexte, revue des sorties, assainissement des données, choix de modèles à la bonne taille.</li>
<li>Équipe : pratique guidée, communautés de pratique, <b>bibliothèques de patterns de prompts</b>.</li>
<li>Test manager : stratégie IA, gestion des risques IA, gouvernance, équipes hybrides humains / agents.</li></ul>`,
  };

  root.ISTQB = { ...(root.ISTQB || {}), notes: { ...((root.ISTQB && root.ISTQB.notes) || {}), genai: notes } };
})(globalThis);
