// scripts/media.mjs
import { spawnSync } from 'node:child_process';
import { mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const SLUG = /^[a-z0-9-]+$/;
const LIMIT = 3 * 1024 * 1024;

export function parseArgs(argv) {
  const [slug, input, ...rest] = argv;
  if (!slug || !input) throw new Error('usage: npm run media -- <slug> <input> [--name loop] [--start 0] [--dur 8] [--width 1600]');
  if (!SLUG.test(slug)) throw new Error(`bad slug: ${slug}`);
  const opts = { name: 'loop', start: 0, dur: 8, width: 1600 };
  for (let i = 0; i < rest.length; i += 2) {
    const key = rest[i].replace(/^--/, '');
    if (!(key in opts)) throw new Error(`unknown option --${key}`);
    opts[key] = key === 'name' ? rest[i + 1] : Number(rest[i + 1]);
  }
  if (!SLUG.test(opts.name)) throw new Error(`bad name: ${opts.name}`);
  return { slug, input, ...opts };
}

export function ffmpegArgs({ input, start, dur, width, out }) {
  return ['-y', '-ss', String(start), '-t', String(dur), '-i', input, '-an',
    '-vf', `scale='min(${width},iw)':-2,fps=30`,
    '-c:v', 'libx264', '-crf', '28', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out];
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const a = parseArgs(process.argv.slice(2));
  const dir = join('public/media/works', a.slug);
  mkdirSync(dir, { recursive: true });
  const out = join(dir, `${a.name}.mp4`);
  const r = spawnSync('ffmpeg', ffmpegArgs({ ...a, out }), { stdio: 'inherit' });
  if (r.status !== 0) process.exit(r.status ?? 1);
  const size = statSync(out).size;
  console.log(`${out}  ${(size / 1024 / 1024).toFixed(2)} MB${size > LIMIT ? '  ⚠ 3MB 초과 — --dur 를 줄이거나 --width 1280' : ''}`);
  console.log(`frontmatter: loop: "/media/works/${a.slug}/${a.name}.mp4"`);
}
