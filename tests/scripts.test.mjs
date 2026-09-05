import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, existsSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { renderTemplate, createWork } from '../scripts/new-work.mjs';
import { parseArgs, ffmpegArgs } from '../scripts/media.mjs';

test('renderTemplate is a draft note with the given order', () => {
  const md = renderTemplate('demo', 9);
  assert.match(md, /^---\n/);
  assert.match(md, /kind: note/);
  assert.match(md, /order: 9/);
  assert.match(md, /draft: true/);
});

test('createWork writes once and refuses to overwrite', () => {
  const root = mkdtempSync(join(tmpdir(), 'works-'));
  const path = createWork('demo', root, 1);
  assert.ok(existsSync(path));
  assert.match(readFileSync(path, 'utf8'), /title: "demo"/);
  assert.throws(() => createWork('demo', root, 1), /exists/);
  assert.throws(() => createWork('Bad Slug', root, 1), /slug/);
});

test('parseArgs applies defaults and validates', () => {
  assert.deepEqual(parseArgs(['birdy', 'in.mov']), { slug: 'birdy', input: 'in.mov', name: 'loop', start: 0, dur: 8, width: 1600 });
  assert.equal(parseArgs(['birdy', 'in.mov', '--start', '3', '--name', 'hero']).name, 'hero');
  assert.throws(() => parseArgs(['Bad', 'in.mov']), /slug/);
  assert.throws(() => parseArgs(['birdy', 'in.mov', '--nope', '1']), /unknown/);
});

test('ffmpegArgs makes a silent h264 clip', () => {
  const a = ffmpegArgs({ input: 'in.mov', start: 2, dur: 6, width: 1600, out: 'o.mp4' });
  assert.ok(a.includes('-an'));
  assert.ok(a.includes('libx264'));
  assert.equal(a[a.indexOf('-ss') + 1], '2');
  assert.equal(a[a.indexOf('-t') + 1], '6');
  assert.equal(a.at(-1), 'o.mp4');
});
