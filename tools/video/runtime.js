// Moteur d'animation déterministe : l'image affichée est une fonction pure du temps t.
// Les éléments déclarent leurs animations par attributs data-*, calés sur des repères (cues) issus de la voix.
(function () {
  const ease = {
    out: (x) => 1 - Math.pow(1 - x, 3),
    inOut: (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2),
    back: (x) => 1 + 2.70158 * Math.pow(x - 1, 3) + 1.70158 * Math.pow(x - 1, 2),
  };
  const TRANSITION_S = 0.7;
  let dirty = false;

  function progress(t, start, dur) {
    const x = (t - start) / dur;
    if (x > 0 && x < 1) dirty = true;
    return Math.min(1, Math.max(0, x));
  }

  // "nom" ou "nom+0.4" ou "nom-0.2" : instant absolu du repère dans la scène.
  function cueTime(scene, spec) {
    if (spec === undefined || spec === null || spec === '') return null;
    const match = /^([\w.]+?)([+-]\d+(?:\.\d+)?)?$/.exec(spec.trim());
    if (!match) throw new Error(`Repère illisible : ${spec}`);
    const base = scene.cues[match[1]];
    if (base === undefined) throw new Error(`Repère inconnu « ${match[1]} » dans la scène ${scene.index}`);
    return base + (match[2] ? Number(match[2]) : 0);
  }

  const ANIMS = {
    up: { dy: 50, scale: 1, easing: 'out', dur: 0.6 },
    down: { dy: -50, scale: 1, easing: 'out', dur: 0.6 },
    left: { dx: -90, scale: 1, easing: 'out', dur: 0.7 },
    right: { dx: 90, scale: 1, easing: 'out', dur: 0.7 },
    pop: { scale: 0.4, easing: 'back', dur: 0.55 },
    zoom: { scale: 1.25, easing: 'out', dur: 0.7 },
    fade: { easing: 'out', dur: 0.6 },
    stamp: { scale: 2.6, easing: 'back', dur: 0.45, rotate: -10 },
  };

  function animateIn(el, scene, t) {
    const start = cueTime(scene, el.dataset.in);
    const spec = ANIMS[el.dataset.anim || 'up'];
    const dur = Number(el.dataset.dur || spec.dur);
    const p = ease[spec.easing](progress(t, start, dur));
    const outAt = cueTime(scene, el.dataset.out);
    const q = outAt === null ? 0 : ease.inOut(progress(t, outAt, 0.5));
    const scale = (spec.scale || 1) + (1 - (spec.scale || 1)) * p;
    const x = (spec.dx || 0) * (1 - p) - 60 * q;
    const y = (spec.dy || 0) * (1 - p);
    const rotate = (spec.rotate || 0) * p;
    // Élément « fantôme » : visible en filigrane dès le début, il s'allume sur son repère.
    if (el.dataset.ghost) {
      el.style.opacity = String(Math.max(0, (0.16 + 0.84 * p) * (1 - q)));
      el.style.transform = `scale(${0.97 + 0.03 * p})`;
      return;
    }
    el.style.opacity = String(Math.max(0, Math.min(1, p * (1 - q))));
    el.style.transform = `translate(${x}px, ${y}px) scale(${scale}) rotate(${rotate}deg)`;
  }

  function typewriter(el, scene, t) {
    const text = el.dataset.text;
    const start = cueTime(scene, el.dataset.type);
    const cps = Number(el.dataset.cps || 32);
    const until = cueTime(scene, el.dataset.until);
    const dur = until === null ? text.length / cps : Math.min(text.length / cps, Math.max(0.5, until - start - 0.15));
    const n = Math.round(text.length * progress(t, start, dur));
    const typing = t >= start && t < start + dur + 0.35;
    if (typing) dirty = true;
    el.textContent = text.slice(0, n);
    el.classList.toggle('caret', typing);
  }

  function stream(el, scene, t) {
    const words = el.dataset.text.split(/(\s+)/);
    const total = words.filter((w) => !/^\s+$/.test(w)).length;
    const wps = Number(el.dataset.wps || 7);
    const count = Math.round(total * progress(t, cueTime(scene, el.dataset.stream), total / wps));
    let shown = 0;
    el.textContent = words.filter((w) => (/^\s+$/.test(w) ? true : (shown += 1) <= count)).join('').trimEnd();
  }

  function glow(el, scene, t) {
    const level = el.dataset.glow.split(',').reduce((best, spec) => {
      const x = progress(t, cueTime(scene, spec), 1.3);
      return Math.max(best, Math.sin(Math.PI * x));
    }, 0);
    el.style.boxShadow = level > 0.01 ? `0 0 0 ${4 + 6 * level}px rgba(255,196,90,${0.65 * level}), 0 0 ${60 * level}px rgba(255,196,90,${0.45 * level})` : '';
  }

  function counter(el, scene, t) {
    const to = Number(el.dataset.to);
    const decimals = Number(el.dataset.dec || 0);
    const p = ease.out(progress(t, cueTime(scene, el.dataset.count), Number(el.dataset.cdur || 1.6)));
    el.textContent = (to * p).toLocaleString('fr-FR', { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
  }

  function countdown(el, scene, t) {
    const start = cueTime(scene, el.dataset.countdown);
    const len = Number(el.dataset.len || 3);
    const p = progress(t, start, len);
    const active = t >= start && t < start + len;
    el.style.opacity = active ? '1' : '0';
    if (!active) return;
    dirty = true;
    el.querySelector('b').textContent = String(Math.max(1, Math.ceil(len - (t - start))));
    el.querySelector('circle.fg').style.strokeDashoffset = String(565 * p);
  }

  function toggleClass(el, scene, t, attr, cls) {
    const at = cueTime(scene, el.dataset[attr]);
    const on = t >= at;
    if (on !== el.classList.contains(cls)) el.classList.toggle(cls, on);
  }

  function renderScene(scene, t) {
    const root = scene.el;
    root.querySelectorAll('[data-in]').forEach((el) => animateIn(el, scene, t));
    root.querySelectorAll('[data-type]').forEach((el) => typewriter(el, scene, t));
    root.querySelectorAll('[data-stream]').forEach((el) => stream(el, scene, t));
    root.querySelectorAll('[data-glow]').forEach((el) => glow(el, scene, t));
    root.querySelectorAll('[data-count]').forEach((el) => counter(el, scene, t));
    root.querySelectorAll('[data-countdown]').forEach((el) => countdown(el, scene, t));
    root.querySelectorAll('[data-good]').forEach((el) => toggleClass(el, scene, t, 'good', 'good'));
    root.querySelectorAll('[data-bad]').forEach((el) => toggleClass(el, scene, t, 'bad', 'bad'));
    root.querySelectorAll('[data-dim]').forEach((el) => toggleClass(el, scene, t, 'dim', 'dim'));
  }

  let lastCaption = -1;
  let lastScene = -1;

  window.render = (t) => {
    dirty = false;
    const { scenes, captions } = window.EPISODE;
    let current = 0;
    scenes.forEach((scene, i) => {
      const visible = t >= scene.start - 0.01 && t < scene.end + TRANSITION_S;
      if (t >= scene.start) current = i;
      scene.el.style.display = visible ? 'block' : 'none';
      if (!visible) return;
      const pin = i === 0 ? 1 : ease.out(progress(t, scene.start, TRANSITION_S));
      const pout = i === scenes.length - 1 ? 0 : ease.inOut(progress(t, scene.end, TRANSITION_S));
      scene.el.style.opacity = String(pin * (1 - pout));
      scene.el.style.transform = `translateX(${(1 - pin) * 120 - pout * 120}px)`;
      renderScene(scene, t);
    });
    const caption = captions.findIndex((c) => t >= c.start && t < c.end);
    if (caption !== lastCaption) {
      dirty = true;
      lastCaption = caption;
      document.getElementById('caption').textContent = caption >= 0 ? captions[caption].text : '';
      document.getElementById('caption').style.opacity = caption >= 0 ? '1' : '0';
    }
    if (current !== lastScene) {
      dirty = true;
      lastScene = current;
      document.getElementById('progress').style.width = `${((current + 1) / scenes.length) * 100}%`;
    }
    return dirty;
  };

  window.addEventListener('DOMContentLoaded', () => {
    window.EPISODE.scenes.forEach((scene, i) => {
      scene.index = i;
      scene.el = document.getElementById(`scene-${i}`);
    });
    document.fonts.ready.then(() => { window.ready = true; });
  });
})();
