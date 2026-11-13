// Aperçu : capture quelques instants d'un épisode. Usage : node preview.js <episode.html> <dossier> <t1> <t2> ...
const { chromium } = require('playwright-core');
const path = require('path');

const EDGE = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';

(async () => {
  const [, , scene, dir, ...times] = process.argv;
  const browser = await chromium.launch({ executablePath: EDGE, args: ['--disable-gpu'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  const errors = [];
  page.on('pageerror', (e) => errors.push(e.message));
  await page.goto('file:///' + path.resolve(scene).replace(/\\/g, '/'));
  await page.waitForFunction(() => window.ready === true);
  for (const t of times) {
    await page.evaluate((x) => window.render(x), Number(t));
    await page.screenshot({ path: path.join(dir, `t${String(t).padStart(6, '0')}.png`) });
  }
  const info = await page.evaluate(() => window.EPISODE.scenes.map((s) => [Math.round(s.start), Math.round(s.end)]));
  process.stdout.write(`${JSON.stringify(info)}\nerreurs : ${errors.length ? errors.join(' | ') : 'aucune'}\n`);
  await browser.close();
})();
