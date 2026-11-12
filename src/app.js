// Interface de l'application. L'état persistant est conservé dans localStorage.
(function () {
  const { Engine, ISTQB } = globalThis;
  const STORAGE_KEY = 'istqb-ia-prep-v1';
  const BACKUP_KEY = `${STORAGE_KEY}-backup`;
  const SESSION_KEY = `${STORAGE_KEY}-exam`;
  const DEFAULT_CERT = 'genai';
  const LEAVE_EXAM_MESSAGE = "Quitter l'écran d'examen ? Le chrono continue : vous pourrez reprendre depuis l'onglet Examen blanc.";
  const TIME_UP_MESSAGE = 'Temps écoulé : votre copie a été remise automatiquement.';
  const METRIC_TOLERANCE = 0.1;
  const MAX_EXAM_HISTORY = 20;
  const PRACTICE_SESSION_SIZE = 10;
  const MS_PER_SECOND = 1000;

  const view = document.getElementById('view');
  const banks = Object.fromEntries(
    Object.keys(ISTQB.catalog).map((id) => [id, {
      questions: Engine.buildQuestions(ISTQB.rawQuestions[id]),
      cards: Engine.buildFlashcards(id, ISTQB.rawFlashcards[id]),
    }]),
  );

  const certIds = Object.keys(ISTQB.catalog);
  const normalize = (saved) => Engine.normalizeState(saved, certIds, DEFAULT_CERT);

  let notice = '';
  let stopTimer = () => {};
  let activeExam = false;
  let previousHash = location.hash;

  function persist(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (error) {
      notice = "Impossible d'enregistrer la progression dans ce navigateur.";
    }
  }

  function loadState() {
    let raw = null;
    try {
      raw = localStorage.getItem(STORAGE_KEY);
      return normalize(JSON.parse(raw));
    } catch (error) {
      notice = 'La progression enregistrée est illisible : elle a été réinitialisée.';
      if (raw !== null) persist(BACKUP_KEY, raw);
      return normalize(null);
    }
  }

  let state = loadState();

  function save() {
    persist(STORAGE_KEY, JSON.stringify(state));
  }

  // La copie en cours survit à un rechargement de la page.
  function isSession(value) {
    return Boolean(value) && Boolean(ISTQB.catalog[value.cert]) && Number.isFinite(value.deadline)
      && Array.isArray(value.items) && Array.isArray(value.answers)
      && value.items.length === value.answers.length && value.answers.every(Array.isArray)
      && value.items.every((item) => Array.isArray(item.options) && Array.isArray(item.correct))
      && Number.isInteger(value.position) && value.position >= 0 && value.position < value.items.length;
  }

  function loadSession() {
    try {
      const session = JSON.parse(localStorage.getItem(SESSION_KEY));
      return isSession(session) ? session : null;
    } catch (error) {
      return null;
    }
  }

  function clearSession() {
    try {
      localStorage.removeItem(SESSION_KEY);
    } catch (error) {
      notice = "Impossible d'effacer l'examen enregistré dans ce navigateur.";
    }
  }

  const cert = () => ISTQB.catalog[state.cert];
  const bank = () => banks[state.cert];
  const progress = () => state.progress[state.cert];

  function updateProgress(change) {
    state = {
      ...state,
      progress: { ...state.progress, [state.cert]: { ...progress(), ...change(progress()) } },
    };
    save();
  }

  function el(tag, props = {}, ...children) {
    const node = document.createElement(tag);
    Object.entries(props).forEach(([key, value]) => {
      if (key === 'class') node.className = value;
      else if (key === 'html') node.innerHTML = value;
      else if (key.startsWith('on')) node.addEventListener(key.slice(2), value);
      else if (key === 'disabled') node.disabled = value;
      else node.setAttribute(key, value);
    });
    node.append(...children.filter((child) => child !== null && child !== undefined));
    return node;
  }

  const button = (label, onclick, primary = false, disabled = false) =>
    el('button', { class: `btn${primary ? ' primary' : ''}`, onclick, disabled, type: 'button', 'data-key': primary ? 'primary' : label }, label);
  const card = (...children) => el('section', { class: 'card' }, ...children);
  const stat = (value, label) => el('div', { class: 'stat' }, el('b', {}, String(value)), label);
  const percent = (a, b) => (b === 0 ? 0 : Math.round((a / b) * 100));
  const progressBar = (value) => {
    const bar = el('div', { class: 'bar' }, el('span'));
    bar.firstChild.style.width = `${value}%`;
    return bar;
  };

  function draw(nodes) {
    stopTimer();
    stopTimer = () => {};
    view.replaceChildren(
      ...(notice ? [el('p', { class: 'trap', role: 'status' }, notice)] : []),
      ...nodes,
    );
    notice = '';
  }

  // Changement d'écran : retour en haut, focus au début du contenu.
  function render(...nodes) {
    draw(nodes);
    window.scrollTo(0, 0);
    view.focus({ preventScroll: true });
  }

  // Mise à jour d'un même écran : conserve le défilement et le contrôle actif.
  function renderInPlace(...nodes) {
    const key = document.activeElement ? document.activeElement.dataset.key : undefined;
    draw(nodes);
    const target = key ? view.querySelector(`[data-key="${key}"]`) : null;
    if (target) target.focus({ preventScroll: true });
  }

  function reviewOption(item, selected, option, index) {
    const isRight = item.correct.includes(index);
    const isWrong = !isRight && selected.includes(index);
    return el('button', { class: `option${isRight ? ' right' : isWrong ? ' wrong' : ''}`, disabled: true, type: 'button' },
      `${isRight ? '✓ ' : isWrong ? '✗ ' : ''}${option}`);
  }

  // ---------- Accueil ----------
  function homeView() {
    const c = cert();
    const p = progress();
    const cov = Engine.coverage(bank().questions, p.stats);
    const due = Engine.dueCards(bank().cards, p.cards, Date.now()).length;
    const last = p.exams[p.exams.length - 1];
    const days = c.chapters.map((ch, index) =>
      el('tr', {}, el('td', {}, `Étape ${index + 1}`), el('td', {}, `Ch. ${ch.n} — ${ch.title}`), el('td', {}, `${Math.ceil(ch.minutes / 60)} h minimum`)));

    render(
      card(
        el('h2', {}, `${c.code} — ${c.title}`),
        el('p', { class: 'muted' }, `${c.version}. Prérequis officiel : certificat CTFL.`),
        el('div', { class: 'stats' },
          stat(`${c.exam.questions} questions`, `${c.exam.minutes} min (${c.exam.extendedMinutes} min en langue non maternelle)`),
          stat(`${c.exam.pass} / ${c.exam.points}`, 'points pour réussir (65 %)'),
          stat(`${cov.mastered} / ${cov.total}`, 'questions réussies à la dernière tentative'),
          stat(due, 'flashcards à revoir'),
          stat(last ? `${last.earned} / ${last.total}` : '—', 'dernier examen blanc')),
      ),
      card(
        el('h3', {}, 'Parcours conseillé'),
        el('ol', {},
          el('li', {}, 'Pour chaque chapitre : lire la fiche, puis la section correspondante du syllabus officiel.'),
          el('li', {}, "S'entraîner sur le chapitre jusqu'à comprendre chaque explication."),
          el('li', {}, 'Revoir les flashcards chaque jour : les mots-clés sont examinables.'),
          el('li', {}, "Passer un examen blanc, travailler les chapitres faibles, puis faire l'examen d'exemple officiel."),
          el('li', {}, "Viser au moins 80 % de façon répétée avant de s'inscrire.")),
        el('table', {}, el('tbody', {}, ...days)),
      ),
    );
  }

  // ---------- Cours ----------
  // Vidéo narrée du chapitre, avec sous-titres ; chargée seulement à l'ouverture de la fiche.
  function chapterVideo(ch) {
    if (!ch.video) return null;
    return el('figure', { class: 'video' },
      el('video', { controls: 'controls', preload: 'none', src: `${ch.video}.mp4` },
        el('track', { kind: 'subtitles', srclang: 'fr', label: 'Français', src: `${ch.video}.vtt` })),
      el('figcaption', { class: 'muted' }, `Vidéo explicative du chapitre (${ch.videoMinutes} min). Les sous-titres s'activent depuis le lecteur.`));
  }

  function courseView() {
    render(...cert().chapters.map((ch) => {
      const titleOf = () => `${progress().chapters[ch.n] ? '✓ ' : ''}Ch. ${ch.n} — ${ch.title}`;
      const markLabel = () => (progress().chapters[ch.n] ? 'Marquer à revoir' : 'Marquer comme étudié');
      const title = el('h2', {}, titleOf());
      const body = el('div', { hidden: 'hidden' },
        chapterVideo(ch),
        el('div', { html: ISTQB.notes[state.cert][ch.n] }),
        el('h3', {}, "Objectifs d'apprentissage"),
        el('ul', {}, ...ch.los.map(([lo, k, label]) => el('li', {}, el('span', { class: 'tag' }, `K${k}`), ` ${lo} — ${label}`))),
        el('div', { class: 'row' },
          button("S'entraîner sur ce chapitre", () => startPractice((q) => Engine.chapterOf(q.lo) === ch.n, `Chapitre ${ch.n}`), true),
          button(markLabel(), (event) => {
            updateProgress((cur) => ({ chapters: { ...cur.chapters, [ch.n]: !cur.chapters[ch.n] } }));
            title.textContent = titleOf();
            event.target.textContent = markLabel();
          })),
      );
      const toggle = button('Ouvrir', (event) => {
        body.hidden = !body.hidden;
        event.target.textContent = body.hidden ? 'Ouvrir' : 'Fermer';
        event.target.setAttribute('aria-expanded', String(!body.hidden));
      });
      toggle.setAttribute('aria-expanded', 'false');
      return card(
        el('div', { class: 'row spread' },
          title,
          el('span', { class: 'row' }, el('span', { class: 'muted' }, `${ch.minutes} min`), toggle)),
        body,
      );
    }));
  }

  // ---------- Entraînement ----------
  function practiceHomeView() {
    const c = cert();
    const p = progress();
    const weak = Engine.weakQuestions(bank().questions, p.stats);
    render(
      card(
        el('h2', {}, 'Entraînement'),
        el('p', { class: 'muted' }, `Séries de ${PRACTICE_SESSION_SIZE} questions avec correction immédiate. Les questions jamais vues ou les moins réussies passent en premier.`),
        el('div', { class: 'row' },
          button('Tous les chapitres', () => startPractice(() => true, 'Tous les chapitres'), true),
          button(`Mes erreurs (${weak.length})`, () => startPractice((q) => weak.includes(q), 'Mes erreurs'), false, weak.length === 0)),
      ),
      ...c.chapters.map((ch) => {
        const questions = bank().questions.filter((q) => Engine.chapterOf(q.lo) === ch.n);
        const cov = Engine.coverage(questions, p.stats);
        return card(
          el('div', { class: 'row spread' },
            el('strong', {}, `Ch. ${ch.n} — ${ch.title}`),
            button('Commencer', () => startPractice((q) => Engine.chapterOf(q.lo) === ch.n, `Chapitre ${ch.n}`))),
          el('p', { class: 'muted' }, `${cov.mastered} / ${cov.total} réussies à la dernière tentative`),
          progressBar(percent(cov.mastered, cov.total)),
        );
      }),
    );
  }

  function startPractice(filter, label) {
    const pool = Engine.practiceOrder(bank().questions.filter(filter), progress().stats);
    const items = pool.slice(0, PRACTICE_SESSION_SIZE).map((q) => Engine.prepareQuestion(q));
    practiceStep(items, 0, 0, label);
  }

  function questionHeader(item, position, total) {
    const multi = item.correct.length > 1;
    return [
      el('div', { class: 'row spread' },
        el('span', { class: 'muted' }, `Question ${position + 1} / ${total}`),
        el('span', {}, el('span', { class: 'tag' }, `${item.lo} · K${item.k} · ${Engine.pointsFor(item.k)} pt`))),
      el('p', {}, el('strong', {}, item.text)),
      el('p', { class: 'muted' }, multi ? `Sélectionnez ${item.correct.length} réponses.` : 'Sélectionnez une réponse.'),
    ];
  }

  function optionButtons(item, selected, onToggle) {
    return item.options.map((option, index) =>
      el('button', {
        class: `option${selected.includes(index) ? ' selected' : ''}`,
        type: 'button',
        'aria-pressed': String(selected.includes(index)),
        'data-key': `option-${index}`,
        onclick: () => onToggle(index),
      }, option));
  }

  function toggleSelection(selected, index, item) {
    if (selected.includes(index)) return selected.filter((value) => value !== index);
    if (item.correct.length === 1) return [index];
    return selected.length < item.correct.length ? [...selected, index] : selected;
  }

  function practiceStep(items, position, score, label, selected = [], inPlace = false) {
    if (position >= items.length) {
      render(card(
        el('h2', {}, `Série terminée — ${label}`),
        el('p', {}, `${score} / ${items.length} bonnes réponses.`),
        el('div', { class: 'row' }, button("Retour à l'entraînement", practiceHomeView, true)),
      ));
      return;
    }
    const item = items[position];
    const validate = () => {
      const ok = Engine.isCorrect(selected, item.correct);
      updateProgress((cur) => ({ stats: Engine.recordAnswer(cur.stats, item.id, ok, Date.now()) }));
      renderInPlace(card(
        ...questionHeader(item, position, items.length),
        ...item.options.map((option, index) => reviewOption(item, selected, option, index)),
        el('div', { class: `feedback ${ok ? 'right' : 'wrong'}`, role: 'status' },
          el('strong', {}, ok ? 'Correct. ' : 'Incorrect. '), item.explanation),
        el('div', { class: 'row' }, button('Question suivante', () => practiceStep(items, position + 1, score + (ok ? 1 : 0), label), true)),
      ));
    };
    (inPlace ? renderInPlace : render)(card(
      el('p', { class: 'muted' }, label),
      ...questionHeader(item, position, items.length),
      ...optionButtons(item, selected, (index) => practiceStep(items, position, score, label, toggleSelection(selected, index, item), true)),
      el('div', { class: 'row' }, button('Valider', validate, true, selected.length !== item.correct.length)),
    ));
  }

  // ---------- Examen blanc ----------
  function examHomeView() {
    const c = cert();
    const p = progress();
    const session = loadSession();
    render(
      session ? card(
        el('h2', {}, `Examen en cours — ${ISTQB.catalog[session.cert].code}`),
        el('p', {}, `${session.answers.filter((a) => a.length).length} / ${session.items.length} questions répondues. Temps restant : ${formatRemaining(session.deadline - Date.now())}.`),
        el('div', { class: 'row' },
          button('Reprendre', () => resumeExam(session), true),
          button('Abandonner cet examen', () => {
            if (!window.confirm('Abandonner cet examen ? Vos réponses seront perdues.')) return;
            clearSession();
            examHomeView();
          })),
      ) : card(
        el('h2', {}, `Examen blanc ${c.code}`),
        el('p', {}, `${c.exam.questions} questions tirées selon la répartition officielle par chapitre et niveau K. ${c.exam.pass} points sur ${c.exam.points} sont nécessaires. Les questions K3 valent 2 points. Une question à plusieurs réponses n'apporte de points que si toutes les réponses sont exactes.`),
        el('div', { class: 'row' },
          button(`Démarrer (${c.exam.minutes} min)`, () => startExam(c.exam.minutes), true),
          button(`Temps étendu (${c.exam.extendedMinutes} min)`, () => startExam(c.exam.extendedMinutes))),
      ),
      p.exams.length ? card(
        el('h3', {}, 'Historique'),
        el('table', {},
          el('thead', {}, el('tr', {}, el('th', {}, 'Date'), el('th', {}, 'Score'), el('th', {}, 'Résultat'))),
          el('tbody', {}, ...[...p.exams].reverse().map((exam) => el('tr', {},
            el('td', {}, new Date(exam.at).toLocaleString('fr-FR')),
            el('td', {}, `${exam.earned} / ${exam.total}`),
            el('td', {}, exam.passed ? 'Réussi' : 'Échoué'))))),
      ) : null,
    );
  }

  function startExam(minutes) {
    try {
      const items = Engine.drawExam(bank().questions, cert());
      const session = { cert: state.cert, items, answers: items.map(() => []), deadline: Date.now() + minutes * 60 * MS_PER_SECOND };
      activeExam = true;
      examStep(session, 0);
    } catch (error) {
      notice = error.message;
      examHomeView();
    }
  }

  function resumeExam(session) {
    if (session.cert !== state.cert) {
      state = { ...state, cert: session.cert };
      save();
      renderShell();
    }
    activeExam = true;
    examStep(session, session.position);
  }

  function formatRemaining(ms) {
    const total = Math.max(0, Math.ceil(ms / MS_PER_SECOND));
    return `${String(Math.floor(total / 60)).padStart(2, '0')}:${String(total % 60).padStart(2, '0')}`;
  }

  function expireExam(session) {
    notice = TIME_UP_MESSAGE;
    finishExam(session);
  }

  function examStep(session, position, inPlace = false) {
    persist(SESSION_KEY, JSON.stringify({ ...session, position }));
    if (Date.now() >= session.deadline) {
      expireExam(session);
      return;
    }
    const item = session.items[position];
    const selected = session.answers[position];
    const answered = session.answers.filter((answer) => answer.length).length;
    const withAnswer = (answer) => ({
      ...session,
      answers: session.answers.map((current, index) => (index === position ? answer : current)),
    });
    const timer = el('span', { class: 'timer', role: 'timer' }, formatRemaining(session.deadline - Date.now()));

    (inPlace ? renderInPlace : render)(card(
      el('div', { class: 'row spread' }, el('span', { class: 'muted' }, `${answered} / ${session.items.length} répondues`), timer),
      ...questionHeader(item, position, session.items.length),
      ...optionButtons(item, selected, (index) => examStep(withAnswer(toggleSelection(selected, index, item)), position, true)),
      el('div', { class: 'row spread' },
        el('span', { class: 'row' },
          button('Précédente', () => examStep(session, position - 1), false, position === 0),
          button('Suivante', () => examStep(session, position + 1), false, position === session.items.length - 1)),
        button("Terminer l'examen", () => {
          const missing = session.items.length - answered;
          const message = missing ? `Il reste ${missing} question(s) sans réponse. Terminer quand même ?` : "Terminer l'examen ?";
          if (window.confirm(message)) finishExam(session);
        }, true)),
    ));

    const interval = setInterval(() => {
      const remaining = session.deadline - Date.now();
      timer.textContent = formatRemaining(remaining);
      if (remaining <= 0) expireExam(session);
    }, MS_PER_SECOND);
    stopTimer = () => clearInterval(interval);
  }

  function finishExam(session) {
    const c = cert();
    const result = Engine.scoreExam(session.items, session.answers, c.exam.pass);
    const now = Date.now();
    activeExam = false;
    clearSession();
    updateProgress((cur) => ({
      stats: result.results
        .filter((r) => r.selected.length > 0)
        .reduce((stats, r) => Engine.recordAnswer(stats, r.item.id, r.ok, now), cur.stats),
      exams: [...cur.exams, { at: now, earned: result.earned, total: result.total, passed: result.passed }].slice(-MAX_EXAM_HISTORY),
    }));
    render(
      card(
        el('h2', { class: result.passed ? 'result-pass' : 'result-fail' }, result.passed ? 'Réussi' : 'Échoué'),
        el('p', {}, `${result.earned} / ${result.total} points (seuil : ${c.exam.pass}).`),
        el('table', {},
          el('thead', {}, el('tr', {}, el('th', {}, 'Chapitre'), el('th', {}, 'Points'), el('th', {}, '%'))),
          el('tbody', {}, ...c.chapters.map((ch) => {
            const score = result.byChapter[ch.n] || { earned: 0, total: 0 };
            return el('tr', {}, el('td', {}, `${ch.n}. ${ch.title}`), el('td', {}, `${score.earned} / ${score.total}`), el('td', {}, `${percent(score.earned, score.total)} %`));
          }))),
        button("Retour à l'examen blanc", examHomeView, true),
      ),
      ...result.results.filter((r) => !r.ok).map((r) => card(
        el('p', {}, el('span', { class: 'tag' }, `${r.item.lo} · K${r.item.k}`)),
        el('p', {}, el('strong', {}, r.item.text)),
        ...r.item.options.map((option, index) => reviewOption(r.item, r.selected, option, index)),
        el('p', { class: 'feedback wrong' }, r.item.explanation),
      )),
    );
  }

  // ---------- Flashcards ----------
  function flashcardsView() {
    const queue = Engine.shuffle(Engine.dueCards(bank().cards, progress().cards, Date.now()));
    flashStep(queue, 0, false);
  }

  function flashStep(queue, position, revealed, inPlace = false) {
    if (position >= queue.length) {
      render(card(
        el('h2', {}, 'Flashcards'),
        el('p', {}, queue.length ? 'Séance terminée.' : 'Aucune carte à revoir pour le moment.'),
        el('p', { class: 'muted' }, 'Les cartes réussies reviennent après 1, 3, 7, 16 puis 35 jours.'),
      ));
      return;
    }
    const item = queue[position];
    const answer = (ok) => {
      updateProgress((cur) => ({ cards: Engine.reviewCard(cur.cards, item.id, ok, Date.now()) }));
      flashStep(queue, position + 1, false);
    };
    (inPlace ? renderInPlace : render)(card(
      el('p', { class: 'muted' }, `Carte ${position + 1} / ${queue.length}`),
      el('div', { class: 'flash' },
        el('div', { class: 'term' }, item.term),
        revealed ? el('p', {}, item.definition) : el('p', { class: 'muted' }, 'Formulez la définition, puis vérifiez.')),
      revealed
        ? el('div', { class: 'row' }, button('Je savais', () => answer(true), true), button('À revoir', () => answer(false)))
        : el('div', { class: 'row' }, button('Afficher la définition', () => flashStep(queue, position, true, true), true)),
    ));
  }

  // ---------- Métriques ----------
  function metricsView(matrix = Engine.randomConfusion(), feedback = null, values = {}) {
    const fields = [['accuracy', 'Exactitude'], ['precision', 'Précision'], ['recall', 'Rappel'], ['f1', 'F1-score']];
    const expected = Engine.metrics(matrix);
    const inputs = Object.fromEntries(fields.map(([key]) => [key, el('input', { type: 'number', step: '0.1', id: `metric-${key}`, value: values[key] || '' })]));
    const check = () => {
      const lines = fields.map(([key, label]) => {
        const given = Number.parseFloat(inputs[key].value);
        const ok = Math.abs(given - expected[key]) <= METRIC_TOLERANCE;
        return { ok, text: `${label} : ${expected[key].toFixed(1)} ${ok ? '✓' : `(saisi : ${Number.isNaN(given) ? '—' : given})`}` };
      });
      metricsView(matrix, lines, Object.fromEntries(fields.map(([key]) => [key, inputs[key].value])));
    };
    (feedback ? renderInPlace : render)(
      card(
        el('h2', {}, 'Atelier métriques (AI-3.3.1, K3)'),
        el('p', { class: 'muted' }, 'Calculez chaque métrique en pourcentage, à 0,1 près.'),
        el('table', {},
          el('thead', {}, el('tr', {}, el('th', {}, ''), el('th', {}, 'Réel positif'), el('th', {}, 'Réel négatif'))),
          el('tbody', {},
            el('tr', {}, el('th', {}, 'Prédit positif'), el('td', {}, `VP = ${matrix.tp}`), el('td', {}, `FP = ${matrix.fp}`)),
            el('tr', {}, el('th', {}, 'Prédit négatif'), el('td', {}, `FN = ${matrix.fn}`), el('td', {}, `VN = ${matrix.tn}`)))),
        el('div', { class: 'row' }, ...fields.map(([key, label]) => el('label', { class: 'field', for: `metric-${key}` }, label, inputs[key]))),
        feedback ? el('div', { class: `feedback ${feedback.every((l) => l.ok) ? 'right' : 'wrong'}`, role: 'status' }, ...feedback.map((l) => el('div', {}, l.text))) : null,
        el('div', { class: 'row', style: 'margin-top:12px' }, button('Vérifier', check, true), button('Nouvelle matrice', () => metricsView())),
      ),
      card(
        el('h3', {}, 'Formules'),
        el('ul', {},
          el('li', {}, 'Exactitude = (VP + VN) / (VP + VN + FP + FN)'),
          el('li', {}, 'Précision = VP / (VP + FP)'),
          el('li', {}, 'Rappel = VP / (VP + FN)'),
          el('li', {}, 'F1 = 2 × Précision × Rappel / (Précision + Rappel)')),
      ),
    );
  }

  // ---------- Navigation ----------
  const routes = {
    accueil: { label: 'Accueil', view: homeView },
    cours: { label: 'Cours', view: courseView },
    entrainement: { label: 'Entraînement', view: practiceHomeView },
    examen: { label: 'Examen blanc', view: examHomeView },
    flashcards: { label: 'Flashcards', view: flashcardsView },
    metriques: { label: 'Métriques', view: () => metricsView(), only: 'ai' },
  };

  function currentRoute() {
    const name = location.hash.replace('#/', '');
    const known = Object.prototype.hasOwnProperty.call(routes, name);
    return known && (!routes[name].only || routes[name].only === state.cert) ? name : 'accueil';
  }

  function confirmLeaveExam() {
    if (activeExam && !window.confirm(LEAVE_EXAM_MESSAGE)) return false;
    activeExam = false;
    return true;
  }

  function renderShell() {
    const active = currentRoute();
    document.getElementById('cert-switch').replaceChildren(...Object.values(ISTQB.catalog).map((c) =>
      el('button', {
        type: 'button',
        class: c.id === state.cert ? 'active' : '',
        'aria-pressed': String(c.id === state.cert),
        onclick: () => {
          if (!confirmLeaveExam()) return;
          state = { ...state, cert: c.id };
          save();
          route();
        },
      }, c.code)));
    document.getElementById('nav').replaceChildren(...Object.entries(routes)
      .filter(([, r]) => !r.only || r.only === state.cert)
      .map(([name, r]) => el('a', {
        href: `#/${name}`,
        class: name === active ? 'active' : '',
        // Sur l'onglet déjà actif le hash ne change pas : il faut revenir à l'écran d'accueil de la section.
        onclick: () => { if (location.hash === `#/${name}`) route(); },
      }, r.label)));
    return active;
  }

  function route() {
    if (!confirmLeaveExam()) {
      history.replaceState(null, '', previousHash || '#/accueil');
      return;
    }
    previousHash = location.hash;
    routes[renderShell()].view();
  }

  window.addEventListener('hashchange', route);
  // Un autre onglet a enregistré : repartir de sa progression pour ne pas l'écraser.
  window.addEventListener('storage', (event) => {
    if (event.key === STORAGE_KEY) state = { ...loadState(), cert: state.cert };
    // L'examen a été terminé ou abandonné ailleurs : cette copie ne doit ni renaître ni compter deux fois.
    if (event.key === SESSION_KEY && event.newValue === null && activeExam) {
      activeExam = false;
      notice = 'Cet examen a été terminé ou abandonné dans un autre onglet.';
      examHomeView();
    }
  });
  route();
})();
