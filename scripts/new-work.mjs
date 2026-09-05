// scripts/new-work.mjs
import { existsSync, mkdirSync, readdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const SLUG = /^[a-z0-9-]+$/;

export function renderTemplate(slug, order) {
  return `---
title: "${slug}"
subtitle: "한 줄 설명"
org: "소속"
year: "${new Date().getFullYear()}"
role: "역할"
responsibilities: ["Research"]
keywords: []
tags: ["Hardware UX"]
kind: note
cover: ./cover.jpg
order: ${order}
draft: true
---

## NOTE

여기에 한 단락. 사실만, 담백하게.
`;
}

export function createWork(slug, root = 'src/content/works', order) {
  if (!SLUG.test(slug)) throw new Error(`bad slug: ${slug} (a-z, 0-9, - 만)`);
  const dir = join(root, slug);
  if (existsSync(dir)) throw new Error(`${dir} exists`);
  mkdirSync(dir, { recursive: true });
  const path = join(dir, 'index.md');
  writeFileSync(path, renderTemplate(slug, order));
  return path;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const slug = process.argv[2];
  if (!slug) { console.error('usage: npm run new:work <slug>'); process.exit(1); }
  const root = 'src/content/works';
  const order = readdirSync(root, { withFileTypes: true }).filter((d) => d.isDirectory()).length + 1;
  const path = createWork(slug, root, order);
  console.log(`created ${path}\n다음: cover.jpg 를 같은 폴더에 넣고 frontmatter를 채운 뒤 draft: false`);
}
