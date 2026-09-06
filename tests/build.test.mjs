import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync, readdirSync } from 'node:fs';

const slugs = (dir) =>
  existsSync(dir)
    ? readdirSync(dir, { withFileTypes: true }).filter((d) => d.isDirectory() && !d.name.startsWith('_')).map((d) => d.name)
    : [];
const isDraft = (path) => /^draft:\s*true/m.test(readFileSync(path, 'utf8'));

test('published works each have a page in dist', () => {
  for (const slug of slugs('src/content/works')) {
    const draft = isDraft(`src/content/works/${slug}/index.md`);
    assert.equal(existsSync(`dist/works/${slug}/index.html`), !draft, `works/${slug}`);
  }
});

test('home links every published work', () => {
  const home = readFileSync('dist/index.html', 'utf8');
  for (const slug of slugs('src/content/works')) {
    if (!isDraft(`src/content/works/${slug}/index.md`)) assert.ok(home.includes(`/works/${slug}/`), slug);
  }
});

test('published activities each have a page in dist', () => {
  for (const slug of slugs('src/content/activities')) {
    const draft = isDraft(`src/content/activities/${slug}/index.md`);
    assert.equal(existsSync(`dist/activities/${slug}/index.html`), !draft, `activities/${slug}`);
  }
});

test('loop videos declared in frontmatter exist under public/', () => {
  for (const slug of slugs('src/content/works')) {
    const m = readFileSync(`src/content/works/${slug}/index.md`, 'utf8').match(/^loop:\s*"?(\/media\/[^"\s]+)/m);
    if (m) assert.ok(existsSync(`public${m[1]}`), m[1]);
  }
});

test('index pages render an h1.label', () => {
  for (const path of ['dist/index.html', 'dist/activities/index.html']) {
    const html = existsSync(path) ? readFileSync(path, 'utf8') : '';
    assert.ok(html.includes('<h1 class="label">'), path);
  }
});

test('birdy og:image points at an optimized derivative, not the raw cover', () => {
  const path = 'dist/works/birdy/index.html';
  const html = existsSync(path) ? readFileSync(path, 'utf8') : '';
  const m = html.match(/property="og:image" content="([^"]+)"/);
  assert.ok(m, `${path} missing og:image meta`);
  assert.ok(!m[1].endsWith('cover.jpg'), m && m[1]);
});
