// Capture d'une plage d'images [début, fin) d'une scène pilotée par window.render(t), encodée par ffmpeg.
// Usage : node capture.js <episode.html> <sortie.mp4> <fps> <ffmpeg.exe> <image_début> <image_fin>
const { chromium } = require('playwright-core');
const { spawn } = require('child_process');
const path = require('path');

const EDGE = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
const JPEG_QUALITY = 90;

async function main() {
  const [, , scene, output, fpsText, ffmpeg, firstText, lastText] = process.argv;
  const fps = Number(fpsText);
  const first = Number(firstText);
  const last = Number(lastText);
  const browser = await chromium.launch({ executablePath: EDGE, args: ['--disable-gpu', '--force-device-scale-factor=1'] });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  page.on('pageerror', (error) => process.stderr.write(`Erreur de page : ${error.message}\n`));
  await page.goto('file:///' + path.resolve(scene).replace(/\\/g, '/'));
  await page.waitForFunction(() => window.ready === true, null, { timeout: 60000 });
  const encoder = spawn(ffmpeg, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-vf', 'scale=in_range=pc:out_range=tv,format=yuv420p', '-color_range', 'tv',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-r', String(fps), output]);
  const closed = new Promise((resolve, reject) => encoder.on('close', (code) => (code === 0 ? resolve() : reject(new Error(`ffmpeg ${code}`)))));

  let frame = null;
  let previousDirty = true;
  let captured = 0;
  for (let f = first; f < last; f += 1) {
    const dirty = await page.evaluate((t) => window.render(t), f / fps);
    // Une image de plus après la fin d'un mouvement, pour figer son état final.
    if (dirty || previousDirty || frame === null) {
      frame = await page.screenshot({ type: 'jpeg', quality: JPEG_QUALITY });
      captured += 1;
    }
    previousDirty = dirty;
    if (!encoder.stdin.write(frame)) await new Promise((resolve) => encoder.stdin.once('drain', resolve));
  }
  encoder.stdin.end();
  await closed;
  await browser.close();
  process.stdout.write(`plage ${first}-${last} : ${captured} captures sur ${last - first} images\n`);
}

main().catch((error) => {
  process.stderr.write(`${error.stack}\n`);
  process.exit(1);
});
