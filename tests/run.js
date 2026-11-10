// Exécuter avec `npm test`. Aucune dépendance : compatible Node 16.
const assert = require('assert');
const Engine = require('../src/engine.js');
require('../data/catalog.js');
require('../data/genai-questions.js');
require('../data/genai-questions-2a.js');
require('../data/genai-questions-2b.js');
require('../data/ai-questions.js');
require('../data/ai-questions-2a.js');
require('../data/ai-questions-2b.js');
require('../data/flashcards.js');

const { catalog, rawQuestions, rawFlashcards } = globalThis.ISTQB;
const certs = Object.values(catalog);
const seeded = (seed) => () => {
  const x = Math.sin(seed++) * 10000;
  return x - Math.floor(x);
};

const tests = [];
const test = (name, fn) => tests.push({ name, fn });
const bank = (cert) => Engine.buildQuestions(rawQuestions[cert.id]);
const los = (cert) => new Map(cert.chapters.flatMap((c) => c.los.map(([lo, k]) => [lo, k])));

test('metrics calcule les valeurs de la matrice de confusion', () => {
  const m = Engine.metrics({ tp: 80, fp: 20, fn: 10, tn: 90 });
  assert.strictEqual(m.accuracy, 85);
  assert.strictEqual(m.precision, 80);
  assert.ok(Math.abs(m.recall - 88.889) < 0.001);
  assert.ok(Math.abs(m.f1 - 84.211) < 0.001);
});

test('metrics retourne 0 sans division par zéro', () => {
  assert.deepStrictEqual(Engine.metrics({ tp: 0, fp: 0, fn: 0, tn: 0 }), { accuracy: 0, precision: 0, recall: 0, f1: 0 });
});

test('isCorrect exige exactement les bonnes réponses', () => {
  assert.ok(Engine.isCorrect([2, 0], [0, 2]));
  assert.ok(!Engine.isCorrect([0], [0, 2]));
  assert.ok(!Engine.isCorrect([0, 1, 2], [0, 2]));
});

test('prepareQuestion conserve la bonne réponse après mélange', () => {
  const q = { options: ['a', 'b', 'c', 'd'], correct: [1] };
  const prepared = Engine.prepareQuestion(q, seeded(3));
  assert.strictEqual(prepared.options[prepared.correct[0]], 'b');
  assert.deepStrictEqual(q.options, ['a', 'b', 'c', 'd']);
});

test('scoreExam compte 2 points pour un K3 et applique le seuil', () => {
  const items = [{ lo: 'AI-3.3.1', k: 3, correct: [0] }, { lo: 'AI-1.1.1', k: 2, correct: [1] }];
  const result = Engine.scoreExam(items, [[0], [0]], 2);
  assert.strictEqual(result.earned, 2);
  assert.strictEqual(result.total, 3);
  assert.ok(result.passed);
  assert.deepStrictEqual(result.byChapter[1], { earned: 0, total: 1 });
});

test('reviewCard avance en cas de succès et revient à 0 en cas d’échec', () => {
  const up = Engine.reviewCard({}, 'x', true, 1000);
  assert.strictEqual(up.x.box, 1);
  assert.strictEqual(up.x.due, 1000 + 86400000);
  const down = Engine.reviewCard(up, 'x', false, 2000);
  assert.strictEqual(down.x.box, 0);
  assert.strictEqual(up.x.box, 1);
});

test('dueCards inclut les cartes nouvelles et échues uniquement', () => {
  const cards = [{ id: 'a' }, { id: 'b' }, { id: 'c' }];
  const due = Engine.dueCards(cards, { a: { due: 50 }, b: { due: 500 } }, 100);
  assert.deepStrictEqual(due.map((c) => c.id), ['a', 'c']);
});

test('recordAnswer ne modifie pas les statistiques reçues', () => {
  const before = {};
  const after = Engine.recordAnswer(before, 'q', false, 5);
  assert.deepStrictEqual(before, {});
  assert.deepStrictEqual(Engine.weakQuestions([{ id: 'q' }, { id: 'r' }], after), [{ id: 'q' }]);
});

test('normalizeState complète une sauvegarde partielle ou invalide', () => {
  const state = Engine.normalizeState({ cert: 'inconnue', progress: { ai: { stats: { q: 1 }, exams: 'x', cards: [] } } }, ['genai', 'ai'], 'genai');
  assert.strictEqual(state.cert, 'genai');
  assert.deepStrictEqual(state.progress.ai, { stats: { q: 1 }, cards: {}, chapters: {}, exams: [] });
  assert.deepStrictEqual(state.progress.genai, { stats: {}, cards: {}, chapters: {}, exams: [] });
  assert.strictEqual(Engine.normalizeState(null, ['ai'], 'ai').cert, 'ai');
});

test('une carte corrompue reste révisable et se répare', () => {
  assert.deepStrictEqual(Engine.dueCards([{ id: 'a' }], { a: {} }, 100), [{ id: 'a' }]);
  assert.strictEqual(Engine.reviewCard({ a: {} }, 'a', true, 0).a.box, 1);
});

test("l'identifiant d'une question ne dépend pas de sa position", () => {
  const a = ['AI-1.1.1', 2, 'A', ['1', '2', '3', '4'], [0], 'explication'];
  const b = ['AI-1.1.1', 2, 'B', ['1', '2', '3', '4'], [0], 'explication'];
  const idOfB = (rows) => Engine.buildQuestions(rows).find((q) => q.text === 'B').id;
  assert.strictEqual(idOfB([a, b]), idOfB([b, a]));
});

test('drawExam signale une banque insuffisante', () => {
  assert.throws(() => Engine.drawExam([], { quotas: [{ chapter: 1, k: 2, count: 1 }] }), /Banque insuffisante/);
});

certs.forEach((cert) => {
  test(`${cert.code} : le blueprint correspond à la structure officielle`, () => {
    const count = cert.quotas.reduce((sum, q) => sum + q.count, 0);
    const points = cert.quotas.reduce((sum, q) => sum + q.count * Engine.pointsFor(q.k), 0);
    assert.strictEqual(count, cert.exam.questions);
    assert.strictEqual(points, cert.exam.points);
    assert.strictEqual(cert.chapters.reduce((sum, c) => sum + c.minutes, 0), cert.minimumTrainingMinutes);
  });

  test(`${cert.code} : chaque question est valide et rattachée à un objectif`, () => {
    const known = los(cert);
    assert.strictEqual(new Set(bank(cert).map((q) => q.id)).size, bank(cert).length, 'identifiants en double');
    bank(cert).forEach((q) => {
      assert.ok(known.has(q.lo), `${q.id} : objectif inconnu`);
      assert.strictEqual(q.k, known.get(q.lo), `${q.id} : niveau K différent du syllabus`);
      assert.ok(q.options.length >= 4, `${q.id} : options insuffisantes`);
      assert.strictEqual(new Set(q.options).size, q.options.length, `${q.id} : options dupliquées`);
      assert.ok(q.correct.length >= 1 && q.correct.every((i) => i < q.options.length), `${q.id} : réponse invalide`);
      assert.ok(q.explanation.length > 10, `${q.id} : explication manquante`);
      if (q.correct.length > 1) assert.ok(q.text.includes(`(${q.correct.length} réponses)`), `${q.id} : consigne manquante`);
    });
  });

  test(`${cert.code} : chaque objectif a au moins une question`, () => {
    const covered = new Set(bank(cert).map((q) => q.lo));
    [...los(cert).keys()].forEach((lo) => assert.ok(covered.has(lo), `${lo} sans question`));
  });

  test(`${cert.code} : un examen tiré respecte quotas et barème`, () => {
    for (let seed = 1; seed <= 50; seed += 1) {
      const exam = Engine.drawExam(bank(cert), cert, seeded(seed));
      assert.strictEqual(exam.length, cert.exam.questions);
      assert.strictEqual(new Set(exam.map((q) => q.id)).size, exam.length);
      const perfect = Engine.scoreExam(exam, exam.map((q) => q.correct), cert.exam.pass);
      assert.strictEqual(perfect.total, cert.exam.points);
      assert.strictEqual(perfect.earned, cert.exam.points);
    }
  });

  test(`${cert.code} : les flashcards ont des termes uniques`, () => {
    const cards = Engine.buildFlashcards(cert.id, rawFlashcards[cert.id]);
    assert.strictEqual(new Set(cards.map((c) => c.id)).size, cards.length);
  });
});

const failures = tests.reduce((acc, { name, fn }) => {
  try {
    fn();
    process.stdout.write(`ok   ${name}\n`);
    return acc;
  } catch (error) {
    process.stdout.write(`FAIL ${name}\n     ${error.message}\n`);
    return acc + 1;
  }
}, 0);

process.stdout.write(`\n${tests.length - failures}/${tests.length} tests réussis\n`);
process.exitCode = failures ? 1 : 0;
