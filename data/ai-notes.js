// Fiches de révision CT-AI v2.0 : synthèse personnelle en français, à lire avec le syllabus officiel.
(function (root) {
  const notes = {
    1: `
<h3>IA et systèmes conventionnels</h3>
<table><tr><th>Conventionnel</th><th>À base d'IA (ML)</th></tr>
<tr><td>Instructions explicites, comportement prévisible</td><td>Motifs tirés des données, probabiliste</td></tr>
<tr><td>Transparent</td><td>Boîte noire, enjeu d'explicabilité</td></tr>
<tr><td>Mises à jour manuelles</td><td>Peut être auto-apprenant, à surveiller en continu</td></tr></table>
<h3>IA étroite, générale, super IA</h3>
<p>Tous les systèmes déployés sont de l'<b>IA étroite</b>. L'<b>IA frontière</b> en est un sous-ensemble. L'IA générale n'existe pas aujourd'hui. Le passage à la super IA serait la <b>singularité technologique</b>.</p>
<h3>Technologies</h3>
<ul><li>Supervisé, non supervisé, renforcement.</li>
<li>CNN pour l'image, RNN pour les séquences, transformers pour les dépendances longues.</li>
<li>GenAI : <b>GAN</b> (deux réseaux en compétition), <b>diffusion</b> (ajout puis retrait de bruit), <b>transformers</b> (auto-attention).</li>
<li>Agentic AI : agents autonomes qui planifient, raisonnent et agissent.</li></ul>
<h3>Matériel et hébergement</h3>
<p>Le ML bénéficie du parallélisme et de la faible précision (quantization). <b>GPU</b> plus efficaces que CPU malgré une horloge souvent plus lente. ASIC et SoC pour l'edge. Hébergement local, cloud public ou privé, hybride.</p>
<h3>Frameworks</h3>
<p>Gestion des données, construction du modèle, entraînement et optimisation, évaluation, déploiement.</p>
<h3>Réglementation</h3>
<p>EU AI Act : approche par les risques ; le haut risque exige tests rigoureux, gouvernance des données, supervision humaine. Principes OCDE et rapport ONU : droit souple. ISO/IEC TR 29119-11 pour le test des systèmes IA.</p>`,
    2: `
<h3>ISO/IEC 25059 : ce qui s'ajoute à 25010</h3>
<table><tr><th>Caractéristique</th><th>Rattachement</th><th>Idée</th></tr>
<tr><td>Exactitude fonctionnelle IA</td><td>Produit</td><td>Seuils d'erreurs acceptables</td></tr>
<tr><td>Adaptabilité fonctionnelle</td><td>Aptitude fonctionnelle</td><td>S'adapte seul après déploiement</td></tr>
<tr><td>Contrôlabilité utilisateur</td><td>Capacité d'interaction</td><td>Un humain peut intervenir à temps</td></tr>
<tr><td>Transparence</td><td>Capacité d'interaction, satisfaction</td><td>Information aux parties prenantes</td></tr>
<tr><td>Robustesse IA</td><td>Fiabilité</td><td>Exactitude maintenue malgré l'adversité</td></tr>
<tr><td>Intervenabilité</td><td>Sécurité</td><td>Intervenir pour éviter un dommage</td></tr>
<tr><td>Atténuation des risques sociétaux et éthiques</td><td>Absence de risque (qualité d'usage)</td><td>Équité, responsabilité, droits</td></tr></table>
<h3>Défis de sûreté</h3>
<p>Spécifications vagues, non-déterminisme, auto-apprentissage, explicabilité (LIME), réglementation en évolution.</p>
<h3>Critères d'acceptation</h3>
<p>Souvent <b>statistiques, probabilistes ou à seuil</b> plutôt que binaires. Exemple : « rappel de 90 % », « reprise de contrôle en moins de 0,5 s ».</p>`,
    3: `
<h3>Formes de ML</h3>
<table><tr><th>Forme</th><th>Sous-type</th><th>Exemple</th></tr>
<tr><td rowspan="2">Supervisé</td><td>Classification</td><td>Spam ou non</td></tr><tr><td>Régression ML</td><td>Estimer un prix</td></tr>
<tr><td rowspan="2">Non supervisé</td><td>Clustering</td><td>Segmenter des clients</td></tr><tr><td>Association</td><td>Paniers d'achat</td></tr>
<tr><td>Renforcement</td><td>—</td><td>Robotique, récompenses</td></tr></table>
<p class="trap">Piège : « régression ML » n'a aucun rapport avec le test de régression.</p>
<h3>Workflow</h3>
<p>Objectifs → framework → algorithme → préparer et tester les données → <b>entraîner → évaluer → régler</b> (génération du modèle) → tester → déployer → utiliser → surveiller et régler.</p>
<ul><li>Hyperparamètres <b>de modèle</b> : structure (couches, profondeur).</li><li>Hyperparamètres <b>d'algorithme</b> : conduite de l'entraînement (itérations).</li></ul>
<h3>Préparation des données</h3>
<p><b>Acquisition</b> (types, sources, labels) · <b>Prétraitement</b> (nettoyage, imputation, anonymisation, normalisation, augmentation, échantillonnage) · <b>Feature engineering</b> · EDA en parallèle.</p>
<h3>Trois jeux de données</h3>
<p>Entraînement → entraîner. <b>Validation</b> → évaluer et régler. <b>Test (holdout)</b> → tester le modèle réglé. Peu de données : <b>validation croisée en k blocs</b>, moyenne des métriques.</p>
<h3>Métriques (K3, à savoir calculer)</h3>
<ul><li>Exactitude = (VP + VN) / total</li><li>Précision = VP / (VP + FP)</li><li>Rappel = VP / (VP + FN)</li><li>F1 = 2 × P × R / (P + R)</li></ul>
<p>Entraînez-vous dans l'onglet <b>Métriques</b>.</p>
<p class="trap">Piège : la matrice peut être présentée lignes et colonnes inversées. Repérez toujours ce qui est réel et ce qui est prédit.</p>
<h3>Fine-tuning et RAG</h3>
<p>Fine-tuning : entraînement complémentaire, efficace si les tâches sont proches. RAG : <b>aucun changement du modèle</b>. Les biais du modèle préentraîné sont hérités.</p>
<h3>Réseaux de neurones</h3>
<p>Activation = somme pondérée + biais, passée dans une fonction d'activation non linéaire. L'erreur (perte) ajuste poids et biais, époque après époque. Ce biais n'a rien à voir avec le biais d'équité.</p>
<p><b>Couverture</b> : neurones (seuil dépassé), kMNC (k sections), NBC (sortie hors des bornes d'entraînement). La couverture seule ne garantit pas la généralisation.</p>`,
    4: `
<h3>Verrouillé et adaptatif</h3>
<p>Verrouillé : comportement fixe, plus facile à tester, une mise à jour équivaut à un nouveau système. Adaptatif : comportement qui évolue, non anticipable. Les chatbots LLM mis à jour périodiquement se situent entre les deux.</p>
<h3>Pourquoi le statistique</h3>
<p>Non-déterminisme, évaluation sur des distributions, incertitude et biais, contexte réglementaire.</p>
<h3>Problème d'oracle</h3>
<p>Causes : probabiliste, spécifications incomplètes, complexité, subjectivité, auto-apprentissage.</p>
<p>Solutions : bornes de sortie, bornes d'environnement, experts, tests spécialisés (A/B, back-to-back, métamorphique), oracles proxy.</p>
<h3>Tester la GenAI</h3>
<p>Boîte noire, <b>explosion des entrées</b>, revue qualitative ou second système (qui peut reproduire les mêmes biais), non-fonctionnel, benchmarks.</p>
<h3>Red teaming (K3)</h3>
<ol><li>Équipe diverse.</li><li>Accès en environnement sûr.</li><li>Sonder par prompts (exploration ou checklists).</li><li>Analyser les échecs.</li><li>Créer des datasets pour les corrections.</li></ol>
<p>Le plus efficace <b>avant déploiement</b>, après les évaluations internes. Dialogues multi-tours. Sécurité (injection indirecte, documents RAG piégés) ou sûreté (conseils dangereux en usage normal).</p>
<p class="trap">Red team : proactif, avant déploiement. Blue team : défense continue en production.</p>
<h3>Niveaux de test</h3>
<p>Deux niveaux spécifiques : <b>données d'entrée</b> et <b>modèle ML</b>. S'y ajoutent composants, intégration de composants, système, intégration système et acceptation.</p>
<h3>Risques</h3>
<p>Développement (risques projet), données d'entrée et modèle (risques produit).</p>`,
    5: `
<h3>Risques et mitigations</h3>
<table><tr><th>Risque</th><th>Approche</th></tr>
<tr><td>Biais</td><td>Test de biais</td></tr>
<tr><td>Sources douteuses, empoisonnement</td><td>Provenance, EDA, A/B, red teaming</td></tr>
<tr><td>Dataset incohérent, hors plage, mauvais types</td><td>Contraintes de dataset</td></tr>
<tr><td>Déséquilibre, données manquantes</td><td>Représentativité</td></tr>
<tr><td>Annotations médiocres</td><td>Exactitude des labels</td></tr>
<tr><td>Défaillances du pipeline</td><td>Test du pipeline</td></tr></table>
<h3>Biais</h3>
<p>De données ou algorithmique. <b>Analyse d'impact disparate</b> : attributs sensibles → contrefactuels → sorties → analyse statistique. Attention aux contrefactuels irréalistes.</p>
<h3>Pipeline en couches</h3>
<p>Revue de conception · composants · intégration · système (fumée, fonctionnel, non fonctionnel, injection de fautes, back-to-back) · intégration système · production (back-to-back, A/B, monitoring) · gestion de configuration.</p>
<h3>Représentativité</h3>
<p>Définir la population cible → analyser (EDA) → tester (Chi², Kolmogorov-Smirnov). À faire <b>avant l'entraînement</b>, surveiller ensuite.</p>
<h3>Contraintes de dataset (K3)</h3>
<table><tr><th>Catégorie</th><th>Types</th></tr>
<tr><td>Valeur unique</td><td>Missing, Range, Type</td></tr>
<tr><td>Multi-valeurs</td><td>Sum, Count, Duplicate, Useful, Outlier</td></tr>
<tr><td>Comparaison</td><td>Greater Than, Correlate</td></tr></table>
<p class="trap">« Useful » : un attribut où toutes les valeurs sont uniques (identifiant) n'apporte pas de motif.</p>
<h3>Exactitude des labels</h3>
<p>Revue experte, annotation multiple (accord inter-annotateurs, kappa de Cohen), priorisation par le risque, distribution des labels, règles automatisées, analyse de la perte, analyse de la confiance.</p>`,
    6: `
<h3>Documentation du modèle</h3>
<p>Model Cards, Datasheets for Datasets. La revue cherche les manques, incohérences, et vérifie les exigences réglementaires.</p>
<h3>Performance fonctionnelle probabiliste</h3>
<p>Critère statistique : métrique, marge d'erreur (MoE), niveau de confiance (CL). Plus de tests : à CL fixe la MoE baisse, à MoE fixe le CL monte. Jeu de test indépendant et représentatif. Rapport : « 94 % ± 4 % à 95 % CL ». <em>Les formules de calcul statistique ne sont pas demandées à l'examen.</em></p>
<h3>Antagoniste</h3>
<p>Perturbations souvent imperceptibles. Boîte blanche, ou boîte noire via modèle équivalent (<b>transférabilité</b>) ou force brute.</p>
<h3>Métamorphique (K3)</h3>
<p>Cas source → relation métamorphique (MR) → cas de suivi. On vérifie la <b>relation entre les sorties</b>, pas leur valeur absolue.</p>
<ul><li><b>Invariance</b> : sortie stable sous perturbation.</li><li><b>Monotonie</b> : sortie qui évolue dans un sens.</li><li><b>Cohérence</b> : sorties alignées entre entrées liées.</li></ul>
<p>Utile sans oracle. Limite : détecte des défauts relationnels, pas toutes les erreurs absolues. Une MR incorrecte donne une fausse confiance.</p>
<h3>Dérive</h3>
<table><tr><th>Dérive de données</th><th>Dérive de concept</th></tr><tr><td>Les distributions d'entrée changent</td><td>La relation entrée → sortie correcte change</td></tr></table>
<p>Dynamique : retour utilisateur (vérité terrain). Statique : compare les distributions, sans vérité terrain.</p>
<h3>Sur / sous-apprentissage</h3>
<p><b>Surapprentissage</b> : nettement moins bon sur le test que sur la validation. <b>Sous-apprentissage</b> : faible sur entraînement et validation, courbes hautes et proches.</p>
<h3>A/B et back-to-back</h3>
<table><tr><th>A/B</th><th>Back-to-back</th></tr>
<tr><td>Deux variantes, métriques, statistique : laquelle est meilleure ?</td><td>Pseudo-oracle, sorties comparées : détecter des défauts</td></tr>
<tr><td>Ne génère pas de cas de test</td><td>Il suffit de générer des entrées ; éviter les composants communs</td></tr></table>`,
    7: `
<h3>Risques de développement</h3>
<table><tr><th>Risque</th><th>Approche</th></tr>
<tr><td>Mauvais usage des API</td><td>Test d'API</td></tr>
<tr><td>Framework mal choisi</td><td>Revue d'adéquation</td></tr>
<tr><td>Installation défectueuse</td><td>Test de fumée</td></tr>
<tr><td>Mauvaise répartition des jeux</td><td>Revue d'allocation des données</td></tr>
<tr><td>Hyperparamètres sous-optimaux</td><td>Performance fonctionnelle, A/B</td></tr></table>
<h3>Test de déploiement</h3>
<table><tr><th>Type</th><th>Objet</th></tr>
<tr><td>Installabilité</td><td>Installation, dépendances, désinstallation</td></tr>
<tr><td>Rollback</td><td>Retour à un état stable, testé <b>avant</b> déploiement</td></tr>
<tr><td>Canari</td><td>Petite part du trafic réel, métriques surveillées</td></tr>
<tr><td>Shadow</td><td>En parallèle, mêmes requêtes, sans effet sur les réponses</td></tr>
<tr><td>Conversion de modèle</td><td>Exactitude conservée après conversion de format</td></tr>
<tr><td>Multi-appareils</td><td>Mobile, edge, cloud</td></tr>
<tr><td>API</td><td>Entrées, sorties, erreurs, intégrations</td></tr></table>
<p class="trap">Canari : de vrais utilisateurs voient le nouveau modèle. Shadow : personne ne le voit.</p>`,
  };

  root.ISTQB = { ...(root.ISTQB || {}), notes: { ...((root.ISTQB && root.ISTQB.notes) || {}), ai: notes } };
})(globalThis);
