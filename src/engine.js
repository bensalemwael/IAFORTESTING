// Logique pure de l'application : aucun accès au DOM ni au stockage.
// Toutes les fonctions retournent de nouveaux objets et n'altèrent pas leurs arguments.
(function (root) {
  const DAY_MS = 86400000;
  const LEITNER_INTERVALS_DAYS = [0, 1, 3, 7, 16, 35];
  const K3_POINTS = 2;
  const DEFAULT_POINTS = 1;

  function shuffle(items, rng = Math.random) {
    const copy = [...items];
    for (let i = copy.length - 1; i > 0; i -= 1) {
      const j = Math.floor(rng() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  function chapterOf(lo) {
    const match = /-(\d+)\./.exec(lo);
    if (!match) throw new Error(`Objectif d'apprentissage invalide : ${lo}`);
    return Number(match[1]);
  }

  // Les banques sont saisies en tableaux compacts : [lo, k, texte, options, indices corrects, explication].
  // L'identifiant dépend de l'énoncé : ajouter ou réordonner des questions ne décale pas la progression.
  function textHash(text) {
    let hash = 5381;
    for (const char of text) hash = ((hash * 33) ^ char.codePointAt(0)) >>> 0;
    return hash.toString(36);
  }

  function buildQuestions(rows) {
    return rows.map(([lo, k, text, options, correct, explanation]) => (
      { id: `${lo}#${textHash(text)}`, lo, k, text, options, correct, explanation }
    ));
  }

  function isRecord(value) {
    return typeof value === 'object' && value !== null && !Array.isArray(value);
  }

  function normalizeProgress(saved) {
    const source = isRecord(saved) ? saved : {};
    const record = (key) => (isRecord(source[key]) ? source[key] : {});
    return {
      stats: record('stats'),
      cards: record('cards'),
      chapters: record('chapters'),
      exams: Array.isArray(source.exams) ? source.exams : [],
    };
  }

  // Reconstruit un état complet à partir d'une sauvegarde absente, partielle ou ancienne.
  function normalizeState(saved, certIds, defaultCert) {
    const source = isRecord(saved) ? saved : {};
    const progress = isRecord(source.progress) ? source.progress : {};
    return {
      cert: certIds.includes(source.cert) ? source.cert : defaultCert,
      progress: Object.fromEntries(certIds.map((id) => [id, normalizeProgress(progress[id])])),
    };
  }

  function buildFlashcards(prefix, rows) {
    return rows.map(([term, definition]) => ({ id: `${prefix}:${term}`, term, definition }));
  }

  function pointsFor(k) {
    return k === 3 ? K3_POINTS : DEFAULT_POINTS;
  }

  function prepareQuestion(question, rng = Math.random) {
    const order = shuffle(question.options.map((_, index) => index), rng);
    return {
      ...question,
      options: order.map((index) => question.options[index]),
      correct: order.flatMap((index, position) => (question.correct.includes(index) ? [position] : [])),
    };
  }

  function isCorrect(selected, correct) {
    const chosen = new Set(selected);
    return chosen.size === correct.length && correct.every((index) => chosen.has(index));
  }

  function drawExam(questions, blueprint, rng = Math.random) {
    const drawn = blueprint.quotas.flatMap(({ chapter, k, count }) => {
      const pool = questions.filter((q) => chapterOf(q.lo) === chapter && q.k === k);
      if (pool.length < count) {
        throw new Error(`Banque insuffisante : chapitre ${chapter}, K${k} (${pool.length}/${count})`);
      }
      return shuffle(pool, rng).slice(0, count);
    });
    return drawn
      .sort((a, b) => chapterOf(a.lo) - chapterOf(b.lo))
      .map((question) => prepareQuestion(question, rng));
  }

  function scoreExam(items, answers, passMark) {
    const results = items.map((item, index) => ({
      item,
      selected: answers[index] || [],
      ok: isCorrect(answers[index] || [], item.correct),
      points: pointsFor(item.k),
    }));
    const earned = results.reduce((sum, r) => sum + (r.ok ? r.points : 0), 0);
    const total = results.reduce((sum, r) => sum + r.points, 0);
    const byChapter = results.reduce((acc, r) => {
      const chapter = chapterOf(r.item.lo);
      const current = acc[chapter] || { earned: 0, total: 0 };
      return {
        ...acc,
        [chapter]: { earned: current.earned + (r.ok ? r.points : 0), total: current.total + r.points },
      };
    }, {});
    return { results, earned, total, passed: earned >= passMark, byChapter };
  }

  function recordAnswer(stats, id, ok, now) {
    const current = stats[id] || { seen: 0, correct: 0, lastOk: null, at: 0 };
    return {
      ...stats,
      [id]: { seen: current.seen + 1, correct: current.correct + (ok ? 1 : 0), lastOk: ok, at: now },
    };
  }

  function weakQuestions(questions, stats) {
    return questions.filter((q) => stats[q.id] && stats[q.id].lastOk === false);
  }

  // Ordonne les questions pour présenter d'abord les jamais vues, puis les moins bien réussies.
  function practiceOrder(questions, stats, rng = Math.random) {
    const rate = (q) => {
      const s = stats[q.id];
      return s && s.seen > 0 ? s.correct / s.seen : -1;
    };
    return shuffle(questions, rng).sort((a, b) => rate(a) - rate(b));
  }

  function reviewCard(cards, id, ok, now) {
    const previousBox = cards[id] && Number.isFinite(cards[id].box) ? cards[id].box : 0;
    const box = ok ? Math.min(previousBox + 1, LEITNER_INTERVALS_DAYS.length - 1) : 0;
    return { ...cards, [id]: { box, due: now + LEITNER_INTERVALS_DAYS[box] * DAY_MS } };
  }

  function dueCards(flashcards, cards, now) {
    return flashcards.filter((card) => !cards[card.id] || !(cards[card.id].due > now));
  }

  function metrics({ tp, fp, fn, tn }) {
    const ratio = (num, den) => (den === 0 ? 0 : (num / den) * 100);
    const accuracy = ratio(tp + tn, tp + tn + fp + fn);
    const precision = ratio(tp, tp + fp);
    const recall = ratio(tp, tp + fn);
    const f1 = precision + recall === 0 ? 0 : (2 * precision * recall) / (precision + recall);
    return { accuracy, precision, recall, f1 };
  }

  function randomConfusion(rng = Math.random) {
    const pick = (min, max) => min + Math.floor(rng() * (max - min + 1));
    return { tp: pick(20, 120), fp: pick(2, 40), fn: pick(2, 40), tn: pick(20, 120) };
  }

  function coverage(questions, stats) {
    const seen = questions.filter((q) => stats[q.id]);
    const mastered = questions.filter((q) => stats[q.id] && stats[q.id].lastOk === true);
    return { total: questions.length, seen: seen.length, mastered: mastered.length };
  }

  const Engine = {
    shuffle,
    chapterOf,
    buildQuestions,
    buildFlashcards,
    normalizeState,
    pointsFor,
    prepareQuestion,
    isCorrect,
    drawExam,
    scoreExam,
    recordAnswer,
    weakQuestions,
    practiceOrder,
    reviewCard,
    dueCards,
    metrics,
    randomConfusion,
    coverage,
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = Engine;
  root.Engine = Engine;
})(globalThis);
