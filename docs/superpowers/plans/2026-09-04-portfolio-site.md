# 포트폴리오 사이트 재구축 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 프레이머 포트폴리오를 Astro 정적 사이트로 다시 만들어 https://byjunyoung.github.io/ 에 배포하고, 프로젝트 추가·수정을 마크다운 파일과 스크립트로 관리한다.

**Architecture:** Astro 콘텐츠 컬렉션(`src/content/works/{slug}/index.md`, `src/content/activities/{slug}/index.md`)이 유일한 콘텐츠 소스다. zod 스키마가 필드를 검증하고, 빌드가 통과해야 GitHub Actions가 Pages에 배포한다. 영상은 `public/media/works/{slug}/`에 두고 frontmatter·본문에서 절대경로로 참조한다.

**Tech Stack:** Astro 7.3 (content collections, astro:assets), @astrojs/sitemap, Node 25 내장 `node --test`, Python 3 stdlib(일회성 임포터), ffmpeg 8, GitHub Actions(withastro/action@v6, actions/deploy-pages@v5), Pretendard Variable(jsDelivr CDN)

**Spec:** `docs/superpowers/specs/2026-09-04-portfolio-site-design.md`

## Global Constraints

- 레포: `byjunyoung/byjunyoung.github.io` (public). 로컬 `~/Documents/Claude/byjunyoung.github.io`. `base` 설정 없음, `site: 'https://byjunyoung.github.io'`.
- 언어: 한국어만. `<html lang="ko">`. 영어 컬렉션은 만들지 않는다.
- 문구: 담백하고 사실만. 프레이머에 없던 사실·수치를 추가하지 않는다. 임포터가 만든 문장을 "개선"하지 않는다.
- 스타일: 색·크기·간격은 `src/styles/global.css`의 토큰만 쓴다. 컴포넌트에 hex·px 하드코딩 금지. 폰트는 Pretendard Variable 하나.
- 모션: 루프 영상만. 스크롤 애니메이션·트랜지션 라이브러리 금지.
- 미디어: 이미지는 긴 변 2000px 이하, 콘텐츠 폴더에 둔다. 영상은 무음 H.264 mp4, 8초 이내, 3MB 목표, `public/media/works/{slug}/`에만 둔다. Git LFS 금지.
- 의존성: astro, @astrojs/sitemap, sharp 외 추가 금지 (필요하면 계획을 고친다).
- 외부 쓰기(GitHub 레포 생성·push, Pages 설정)는 **사용자 미리보기 → "go" 후에만** 실행한다. 로컬 커밋은 자유.
- 원본 자료: `~/Documents/Claude/portfolio-import/framer-export/` (raw/*.html, images/ 93장, manifest.json). 읽기만 한다.

## File Structure

```
byjunyoung.github.io/
├─ .github/workflows/deploy.yml     Pages 배포
├─ astro.config.mjs                 site + sitemap
├─ package.json / tsconfig.json
├─ CLAUDE.md                        AI 작업 규칙 (Task 9)
├─ README.md
├─ public/
│  ├─ favicon.svg, robots.txt
│  └─ media/works/{slug}/*.mp4      영상 (Task 11)
├─ scripts/
│  ├─ import_framer.py              일회성 임포터 (Task 3)
│  ├─ new-work.mjs                  프로젝트 템플릿 생성 (Task 9)
│  └─ media.mjs                     ffmpeg 변환 (Task 9)
├─ src/
│  ├─ content.config.ts             스키마 (Task 1)
│  ├─ content/works/{slug}/index.md + cover.* + NN.*
│  ├─ content/activities/{slug}/index.md + cover.*
│  ├─ layouts/Base.astro            head·nav·footer (Task 5)
│  ├─ components/WorkCard.astro     홈 카드 (Task 5)
│  ├─ components/MetaCard.astro     상세 메타 (Task 6)
│  ├─ styles/global.css             토큰·전역 (Task 5)
│  └─ pages/
│     ├─ index.astro                홈 (Task 5)
│     ├─ 404.astro                  (Task 10)
│     ├─ works/[slug].astro         (Task 6)
│     └─ activities/index.astro, activities/[slug].astro  (Task 7)
└─ tests/
   ├─ build.test.mjs                dist 검증 (Task 1)
   ├─ scripts.test.mjs              스크립트 단위 (Task 9)
   └─ test_import.py                임포터 단위 (Task 3)
```

---

### Task 1: Astro 스캐폴드 + 콘텐츠 스키마 + 테스트 러너

**Files:**
- Create: `package.json`, `astro.config.mjs`, `tsconfig.json`, `.gitignore`, `src/content.config.ts`, `src/pages/index.astro`(임시), `tests/build.test.mjs`
- Create(임시): `src/content/works/_fixture/index.md`, `src/content/works/_fixture/cover.jpg`

**Interfaces:**
- Produces: 컬렉션 `works`(id = 폴더명, 필드는 아래 스키마), 컬렉션 `activities`. `npm test` = `astro build` + `node --test tests/`. 이후 모든 Task는 이 스키마의 필드명을 그대로 쓴다.

- [ ] **Step 1: Astro 최소 템플릿 생성**

레포 루트(`~/Documents/Claude/byjunyoung.github.io`, 이미 `git init` 됨)에서:

```bash
cd ~/Documents/Claude/byjunyoung.github.io
npm create astro@latest -- _scaffold --template minimal --no-install --no-git --yes
rsync -a _scaffold/ ./ && rm -rf _scaffold
npm install
npm install @astrojs/sitemap sharp
npm install -D @astrojs/check typescript
```

(현재 폴더에 docs/·.git이 있어 "비어 있지 않음" 프롬프트를 피하려고 임시 폴더에 만든 뒤 합친다.)

Expected: `package.json`에 `astro` ^7 의존성, `src/pages/index.astro` 생성, `npm run build` 통과.

- [ ] **Step 2: astro.config.mjs**

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://byjunyoung.github.io',
  integrations: [sitemap()],
});
```

- [ ] **Step 3: package.json 스크립트**

`package.json`의 `scripts`를 아래로 교체한다 (다른 필드는 유지):

```json
"scripts": {
  "dev": "astro dev",
  "build": "astro build",
  "preview": "astro preview",
  "check": "astro check",
  "test": "npm run build && node --test tests/",
  "new:work": "node scripts/new-work.mjs",
  "media": "node scripts/media.mjs",
  "import:framer": "python3 scripts/import_framer.py"
}
```

`.gitignore`에 아래가 있는지 확인하고 없으면 추가: `node_modules/`, `dist/`, `.astro/`, `.DS_Store`.

- [ ] **Step 4: 콘텐츠 스키마**

```ts
// src/content.config.ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const link = z.object({ label: z.string().min(1), url: z.string().url() });
const folderId = ({ entry }: { entry: string }) => entry.split('/')[0];

const works = defineCollection({
  loader: glob({ pattern: '*/index.md', base: './src/content/works', generateId: folderId }),
  schema: ({ image }) =>
    z.object({
      title: z.string().min(1),
      subtitle: z.string().min(1),
      org: z.string().min(1),
      year: z.string().min(1),
      role: z.string().min(1),
      responsibilities: z.array(z.string()).min(1),
      with: z.string().optional(),
      keywords: z.array(z.string()).default([]),
      link: link.optional(),
      tags: z.array(z.string()).min(1),
      kind: z.enum(['case-study', 'note']),
      cover: image(),
      loop: z.string().regex(/^\/media\/works\/[a-z0-9-]+\/[a-z0-9-]+\.mp4$/).optional(),
      order: z.number().int(),
      draft: z.boolean().default(false),
      press: z.array(link).default([]),
      awards: z.array(z.string()).default([]),
    }),
});

const activities = defineCollection({
  loader: glob({ pattern: '*/index.md', base: './src/content/activities', generateId: folderId }),
  schema: ({ image }) =>
    z.object({
      title: z.string().min(1),
      subtitle: z.string().min(1),
      role: z.string().min(1),
      period: z.string().min(1),
      links: z.array(link).default([]),
      cover: image().optional(),
      order: z.number().int(),
      draft: z.boolean().default(false),
    }),
});

export const collections = { works, activities };
```

- [ ] **Step 5: 실패하는 빌드 테스트 작성 (픽스처로 스키마 검증 확인)**

`tests/build.test.mjs`:

```js
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
```

- [ ] **Step 6: 스키마가 잘못된 픽스처를 거부하는지 확인**

`src/content/works/_fixture/index.md` (title 누락):

```md
---
subtitle: "x"
org: "x"
year: "x"
role: "x"
responsibilities: ["x"]
tags: ["x"]
kind: note
cover: ./cover.jpg
order: 1
---
본문
```

`cover.jpg`는 임포트 폴더에서 아무 jpg 하나 복사: `cp ~/Documents/Claude/portfolio-import/framer-export/images/$(ls ~/Documents/Claude/portfolio-import/framer-export/images | grep -m1 jpg) src/content/works/_fixture/cover.jpg`

Run: `npm run build`
Expected: FAIL. 에러 메시지에 `title` 가 required 라는 zod 메시지 포함. (glob 패턴 `*/index.md`는 `_fixture`도 잡는다 — 그래서 실패해야 정상.)

- [ ] **Step 7: 픽스처를 올바르게 고쳐 빌드 통과**

`_fixture/index.md` frontmatter에 `title: "Fixture"` 추가.

Run: `npm run build && node --test tests/`
Expected: build 성공, `dist/works/_fixture/index.html` 생성. 테스트는 `_fixture`를 `_` 접두어로 건너뛰므로 통과. (홈 페이지는 아직 기본 템플릿이라 "home links" 테스트는 works가 0개로 통과.)

- [ ] **Step 8: 픽스처 제거 후 커밋**

```bash
rm -rf src/content/works/_fixture
mkdir -p src/content/works src/content/activities && touch src/content/works/.gitkeep src/content/activities/.gitkeep
npm run build
git add -A
git commit -m "chore: astro scaffold with works/activities schema and build tests"
```

---

### Task 2: GitHub 레포·Actions·첫 배포 (외부 쓰기 — go 게이트)

**Files:**
- Create: `.github/workflows/deploy.yml`, `README.md`

**Interfaces:**
- Produces: `main` 푸시 → https://byjunyoung.github.io/ 자동 배포.

- [ ] **Step 1: 워크플로 작성**

```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: withastro/action@v6

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v5
```

`README.md`:

```md
# byjunyoung.github.io

Junyoung Kim 포트폴리오. Astro 정적 사이트, GitHub Pages 배포.

- 콘텐츠: `src/content/works/{slug}/index.md`, `src/content/activities/{slug}/index.md`
- 작업 규칙: `CLAUDE.md`
- 설계·계획: `docs/superpowers/`
- 로컬: `npm run dev` / 검증: `npm test`
```

```bash
git add -A && git commit -m "ci: github pages deploy workflow"
```

- [ ] **Step 2: 사용자에게 미리보기 → go**

아래를 그대로 보여주고 "go"를 받는다. 받기 전엔 실행하지 않는다.

```
대상: GitHub 계정 byjunyoung
1. public 레포 byjunyoung.github.io 생성, 로컬 main 푸시 (커밋 2개)
2. Pages 소스를 GitHub Actions로 설정
3. 첫 배포 → https://byjunyoung.github.io/ 에 빈 홈이 뜸
되돌리기: gh repo delete byjunyoung/byjunyoung.github.io
이대로 진행할까요? (go / 수정사항)
```

- [ ] **Step 3: 레포 생성·푸시·Pages 설정**

```bash
cd ~/Documents/Claude/byjunyoung.github.io
gh repo create byjunyoung/byjunyoung.github.io --public --source . --remote origin --push
gh api -X POST repos/byjunyoung/byjunyoung.github.io/pages -f build_type=workflow
gh run watch --exit-status $(gh run list --workflow deploy.yml --limit 1 --json databaseId -q '.[0].databaseId')
```

Expected: 워크플로 성공. (Pages API가 409를 내면 이미 설정된 것이므로 무시.)

- [ ] **Step 4: 배포 확인**

Run: `curl -s -o /dev/null -w "%{http_code}\n" https://byjunyoung.github.io/`
Expected: `200`. `curl -s https://byjunyoung.github.io/resume/ -o /dev/null -w "%{http_code}\n"` 도 `200` (이력서 공존 확인).

---

### Task 3: 프레이머 임포터 — 공개 HTML → 콘텐츠 컬렉션

**Files:**
- Create: `scripts/import_framer.py`, `tests/test_import.py`
- Create(생성물): `src/content/works/{8 slugs}/index.md` + 이미지, `src/content/activities/{5 slugs}/index.md` + cover

**Interfaces:**
- Consumes: Task 1 스키마. 원본 `~/Documents/Claude/portfolio-import/framer-export/{raw,images,manifest.json}`.
- Produces: 스키마를 통과하는 13개 엔트리. `kind: note`는 barisbrew·storagy·dotpad. 활동 uxeed·dino·internview는 `draft: true`.

프레이머 마크업 사실(확인됨): 메타 라벨은 `<h6>` 텍스트(ORGANIZATION·YEAR·ROLE·RESPONSIBILITIES·WITH·KEYWORDS·LINK / 활동은 ROLE·YEAR·LINKS), 섹션 제목은 대문자 `<p>`(PROBLEM·APPROACH·IMPLEMENTATION·IMPACT·REFLECTION·CHALLENGE·ACHIEVEMENT·프로젝트별 대문자 제목), 구분선은 `——`, 볼드는 `<strong>`, 목록은 `<ol><li><p>`, 이미지는 `<img src="https://framerusercontent.com/images/...?scale-down-to=...">`, 링크는 `<a href="http...">`. 사이트 공통 이미지(로고·아이콘)는 거의 모든 페이지에 나온다.

- [ ] **Step 1: 실패하는 단위 테스트**

`tests/test_import.py`:

```python
import importlib.util, sys, unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('imp', Path(__file__).resolve().parents[1] / 'scripts/import_framer.py')
imp = importlib.util.module_from_spec(spec); spec.loader.exec_module(imp)

HTML = '''<html><body><div><p>works</p><p>Junyoung Kim</p><p>activities</p>
<a href="https://byjunyoung.github.io/resume/">resume</a></div>
<h1>Birdy</h1><p>부제입니다</p>
<h6>ORGANIZATION</h6><p>UNIST</p><h6>YEAR</h6><p>2021 (1y)</p><h6>ROLE</h6><p>리드 연구원</p>
<h6>RESPONSIBILITIES</h6><p>Research, Product Design</p>
<h6>LINK</h6><p><a href="https://x.y/z">Master's Thesis</a></p>
<img src="https://framerusercontent.com/images/logo.png?scale-down-to=512" alt="">
<img src="https://framerusercontent.com/images/hero.jpg?scale-down-to=1024" alt="">
<p>PROBLEM</p><p>——</p><p>문제 문단</p>
<img src="https://framerusercontent.com/images/a.jpg?scale-down-to=1024" alt="">
<p>APPROACH</p><ol><li><p><strong>첫째</strong>: 설명</p></li><li><p>둘째</p></li></ol>
<p>junyoung735@gmail.com</p><p>Select LanguageKorean</p></body></html>'''
CHROME = {'https://framerusercontent.com/images/logo.png'}

class ImportTest(unittest.TestCase):
    def test_parse_page_title_meta_body(self):
        page = imp.parse_page(HTML, CHROME)
        self.assertEqual(page['title'], 'Birdy')
        self.assertEqual(page['subtitle'], '부제입니다')
        self.assertEqual(page['meta']['org'], 'UNIST')
        self.assertEqual(page['meta']['responsibilities'], 'Research, Product Design')
        self.assertEqual(imp.split_links(page['meta']['link']), [("Master's Thesis", 'https://x.y/z')])
        self.assertEqual(page['body'][0], ('img', 'https://framerusercontent.com/images/hero.jpg', ''))

    def test_render_body(self):
        page = imp.parse_page(HTML, CHROME)
        body, imgs = imp.render_body(page['body'], skip_url='https://framerusercontent.com/images/hero.jpg')
        self.assertIn('## PROBLEM', body)
        self.assertNotIn('——', body)
        note, _ = imp.render_body([('p', 'Note', False), ('p', '——', False), ('p', '한 단락', False)])
        self.assertIn('## NOTE', note)
        self.assertIn('![](./01.jpg)', body)
        self.assertIn('1. **첫째**: 설명', body)
        self.assertEqual(imgs, [('https://framerusercontent.com/images/a.jpg', '01.jpg')])

    def test_chrome_images(self):
        man = {f'p{i}': {'images': ['https://f/logo.png'] + (['https://f/only.png'] if i == 0 else [])} for i in range(4)}
        self.assertEqual(imp.chrome_images(man), {'https://f/logo.png'})

    def test_split_csv(self):
        self.assertEqual(imp.split_csv('Research, Product Design / UX'), ['Research', 'Product Design', 'UX'])

if __name__ == '__main__':
    unittest.main()
```

Run: `python3 -m unittest tests/test_import.py -v`
Expected: FAIL (`FileNotFoundError` — 스크립트 없음).

- [ ] **Step 2: 임포터 구현**

`scripts/import_framer.py`:

```python
#!/usr/bin/env python3
"""프레이머 공개 HTML(portfolio-import/framer-export/raw)을 콘텐츠 컬렉션으로 변환한다. 일회성.
사용: python3 scripts/import_framer.py [--dry]
"""
import json, re, shutil, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORT = Path.home() / 'Documents/Claude/portfolio-import/framer-export'
WORKS_OUT = ROOT / 'src/content/works'
ACTS_OUT = ROOT / 'src/content/activities'

WORK_ORDER = ['birdy', 'meemo', 'zibot', 'dotcanvas', 'adio', 'barisbrew', 'storagy', 'dotpad']
NOTE_ONLY = {'barisbrew', 'storagy', 'dotpad'}
ACT_ORDER = ['hux', 'uxeed', 'dino', 'svip', 'internview']   # activities 목록 페이지의 표시 순서
META = {'ORGANIZATION': 'org', 'YEAR': 'year', 'ROLE': 'role', 'RESPONSIBILITIES': 'responsibilities',
        'WITH': 'with', 'KEYWORDS': 'keywords', 'LINK': 'link', 'LINKS': 'links'}
STOP = ('junyoung735@gmail.com', 'Select Language', 'Create a free website')
RULE = re.compile(r'^[—–-]{1,3}$')
HEADING = re.compile(r'^[A-Z0-9][A-Z0-9 :&/\-]{1,40}$')


class Walker(HTMLParser):
    """문서 순서대로 ('p'|'h'|'li'|'img', text|src, extra) 블록을 뽑는다."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.blocks, self._buf, self._skip, self._ol, self._li, self._href = [], [], 0, 0, 0, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('script', 'style', 'noscript', 'svg'):
            self._skip += 1
        if self._skip:
            return
        if tag == 'img' and 'framerusercontent.com/images/' in (a.get('src') or ''):
            self._flush('p')
            self.blocks.append(('img', a['src'].split('?')[0], a.get('alt', '')))
        elif tag == 'a' and (a.get('href') or '').startswith('http'):
            self._href = a['href']
        elif tag == 'strong':
            self._buf.append('**')
        elif tag == 'ol':
            self._ol += 1
        elif tag == 'li':
            self._li += 1
        elif tag == 'br':
            self._buf.append(' ')

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript', 'svg'):
            self._skip = max(0, self._skip - 1)
            return
        if self._skip:
            return
        if tag == 'a' and self._href:
            self._buf.append(f' <{self._href}>')
            self._href = None
        elif tag == 'strong':
            self._buf.append('**')
        elif tag in ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'div'):
            self._flush(tag)
        if tag == 'ol':
            self._ol -= 1
        if tag == 'li':
            self._li -= 1

    def handle_data(self, data):
        if not self._skip and data.strip():
            self._buf.append(data)

    def _flush(self, tag):
        text = re.sub(r'\s+', ' ', ''.join(self._buf)).strip()
        self._buf = []
        if not text:
            return
        kind = 'li' if self._li > 0 else ('h' if tag[0] == 'h' and tag[1:].isdigit() else 'p')
        self.blocks.append((kind, text, self._ol > 0))


def chrome_images(manifest):
    """페이지 절반 넘게 등장하는 이미지 = 사이트 공통(로고·아이콘)."""
    count = {}
    for m in manifest.values():
        for u in m['images']:
            count[u] = count.get(u, 0) + 1
    return {u for u, n in count.items() if n > len(manifest) / 2}


def split_links(text):
    return [(lab.strip(' /'), url) for lab, url in re.findall(r'([^<>]+?)\s*<(https?://[^>]+)>', text)]


def split_csv(text):
    return [t.strip() for t in re.split(r'[,/]', text) if t.strip()]


def blocks_of(raw, chrome):
    w = Walker(); w.feed(raw)
    blocks = [b for b in w.blocks if not (b[0] == 'img' and b[1] in chrome)]
    end = next((i for i, b in enumerate(blocks) if b[0] != 'img' and b[1].startswith(STOP)), len(blocks))
    return blocks[:end]


def parse_page(raw, chrome):
    """상세 페이지 → {title, subtitle, meta{...}, body[blocks]}. 메타 블록이 없으면 None."""
    blocks = blocks_of(raw, chrome)
    texts = [(i, b[1]) for i, b in enumerate(blocks) if b[0] != 'img']
    first = next((n for n, (_, t) in enumerate(texts) if t in META), None)
    if first is None or first < 2:
        return None
    title, subtitle = texts[first - 2][1], texts[first - 1][1]
    meta, n = {}, first
    while n + 1 < len(texts) and texts[n][1] in META:
        meta[META[texts[n][1]]] = texts[n + 1][1]
        n += 2
    body_start = texts[n][0] if n < len(texts) else len(blocks)
    # 메타와 본문 사이에 낀 이미지(히어로)도 본문 앞에 붙인다
    hero = [b for b in blocks[texts[first][0]:body_start] if b[0] == 'img']
    return {'title': title, 'subtitle': subtitle, 'meta': meta, 'body': hero + blocks[body_start:]}


def render_body(blocks, skip_url=None):
    """블록 → 마크다운 본문, [(원본URL, 파일명)]. skip_url(=cover)과 같은 이미지는 본문에서 뺀다."""
    lines, imgs, n = [], [], 0
    for kind, text, extra in blocks:
        if kind == 'img':
            if text == skip_url:
                continue
            n += 1
            name = f'{n:02d}{Path(text).suffix.lower() or ".jpg"}'
            imgs.append((text, name))
            lines.append(f'![](./{name})\n')
        elif RULE.match(text):
            continue
        elif text.upper() == 'NOTE':
            lines.append('\n## NOTE\n')
        elif HEADING.match(text) and text not in META:
            lines.append(f'\n## {text}\n')
        elif kind == 'h':
            lines.append(f'\n### {text}\n')
        elif kind == 'li':
            lines.append(('1. ' if extra else '- ') + text)
        else:
            lines.append(text + '\n')
    return '\n'.join(lines).strip() + '\n', imgs


def parse_cards(raw, chrome, label):
    """목록 페이지 → (카드 이미지 URL 순서, 텍스트 순서). label 다음 소개문 1개는 건너뛴다."""
    blocks = blocks_of(raw, chrome)
    start = next(i for i, b in enumerate(blocks) if b[0] != 'img' and b[1] == label) + 2
    tail = blocks[start:]
    return [b[1] for b in tail if b[0] == 'img'], [b[1] for b in tail if b[0] != 'img']


def ys(s):
    return json.dumps(s, ensure_ascii=False)


def yl(items):
    return '[' + ', '.join(ys(i) for i in items) + ']'


def copy_image(url, dest, dry):
    src = IMPORT / 'images' / Path(url).name
    if not src.exists():
        return f'missing image {src.name}'
    if not dry:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    return None


def write(path, text, dry):
    if dry:
        print(f'--- would write {path.relative_to(ROOT)}')
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def import_works(chrome, dry):
    covers, _ = parse_cards((IMPORT / 'raw/home.html').read_text(encoding='utf-8'), chrome, 'WORKS')
    assert len(covers) == len(WORK_ORDER), f'home cards {len(covers)} != {len(WORK_ORDER)}'
    for order, slug in enumerate(WORK_ORDER, 1):
        raw = (IMPORT / f'raw/works__{slug}.html').read_text(encoding='utf-8')
        page = parse_page(raw, chrome)
        assert page, f'{slug}: no meta block'
        m, warn = page['meta'], []
        cover = covers[order - 1]
        body, imgs = render_body(page['body'], skip_url=cover)
        out = WORKS_OUT / slug
        links = split_links(m.get('link', ''))
        fm = [f'title: {ys(page["title"])}', f'subtitle: {ys(page["subtitle"])}',
              f'org: {ys(m.get("org", ""))}', f'year: {ys(m.get("year", ""))}', f'role: {ys(m.get("role", ""))}',
              f'responsibilities: {yl(split_csv(m.get("responsibilities", "")))}']
        if m.get('with'):
            fm.append(f'with: {ys(m["with"])}')
        fm.append(f'keywords: {yl(split_csv(m.get("keywords", "")))}')
        if links:
            fm.append(f'link: {{ label: {ys(links[0][0])}, url: {ys(links[0][1])} }}')
        elif m.get('link'):
            warn.append(f'link without url: {m["link"]}')
        fm += [f'tags: {yl(split_csv(m.get("responsibilities", "")) or ["Hardware UX"])}',
               f'kind: {"note" if slug in NOTE_ONLY else "case-study"}',
               f'cover: ./cover{Path(cover).suffix.lower()}', f'order: {order}', 'draft: false']
        for url, name in [(cover, f'cover{Path(cover).suffix.lower()}')] + imgs:
            w = copy_image(url, out / name, dry)
            if w:
                warn.append(w)
        write(out / 'index.md', '---\n' + '\n'.join(fm) + '\n---\n\n' + body, dry)
        print(f'works/{slug:10s} imgs={len(imgs) + 1:2d} body_lines={body.count(chr(10)):3d} {" | ".join(warn)}')


def import_activities(chrome, dry):
    covers, texts = parse_cards((IMPORT / 'raw/activities.html').read_text(encoding='utf-8'), chrome, 'ACTIVITIES')
    cards = [texts[i:i + 3] for i in range(0, len(ACT_ORDER) * 3, 3)]
    assert len(cards) == len(ACT_ORDER) and len(covers) == len(ACT_ORDER), f'activity cards {len(cards)}/{len(covers)}'
    for order, slug in enumerate(ACT_ORDER, 1):
        title, subtitle, role = cards[order - 1]
        raw = (IMPORT / f'raw/activities__{slug}.html').read_text(encoding='utf-8')
        page = parse_page(raw, chrome)
        cover, out, warn = covers[order - 1], ACTS_OUT / slug, []
        if page:
            m = page['meta']
            body, imgs = render_body(page['body'], skip_url=cover)
            links = split_links(m.get('links', ''))
            period, draft = m.get('year', ''), False
        else:
            body, imgs, links, period, draft = '', [], [], 'TBD', True
            warn.append('empty page → draft')
        fm = [f'title: {ys(title)}', f'subtitle: {ys(subtitle)}', f'role: {ys(role)}', f'period: {ys(period)}',
              'links: [' + ', '.join(f'{{ label: {ys(l)}, url: {ys(u)} }}' for l, u in links) + ']',
              f'cover: ./cover{Path(cover).suffix.lower()}', f'order: {order}', f'draft: {"true" if draft else "false"}']
        for url, name in [(cover, f'cover{Path(cover).suffix.lower()}')] + imgs:
            w = copy_image(url, out / name, dry)
            if w:
                warn.append(w)
        write(out / 'index.md', '---\n' + '\n'.join(fm) + '\n---\n\n' + body, dry)
        print(f'activities/{slug:10s} imgs={len(imgs) + 1:2d} {" | ".join(warn)}')


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    manifest = json.loads((IMPORT / 'manifest.json').read_text(encoding='utf-8'))
    chrome = chrome_images(manifest)
    print(f'chrome images skipped: {len(chrome)}')
    import_works(chrome, dry)
    import_activities(chrome, dry)
```

- [ ] **Step 3: 단위 테스트 통과**

Run: `python3 -m unittest tests/test_import.py -v`
Expected: 4 tests OK.

- [ ] **Step 4: 드라이런으로 원본 전체에 대해 파싱 확인**

Run: `npm run import:framer -- --dry`
Expected: `works/*` 8줄, `activities/*` 5줄, assert 없이 끝남. uxeed·dino·internview는 `empty page → draft`. `missing image` 경고가 있으면 manifest의 이미지 목록과 대조해 원인을 적는다(그 페이지에만 있는 `srcset` 변형 URL이면 `Walker`에서 `src` 대신 `srcset` 첫 항목을 쓰도록 고친다).

- [ ] **Step 5: 실제 생성 + 빌드**

```bash
npm run import:framer
npm run build
```

Expected: 빌드 통과, `dist/works/*` 8개, `dist/activities/*` 2개(hux, svip). 스키마 에러가 나면 해당 슬러그의 frontmatter를 확인한다 — `year`나 `role`이 비면 원본 페이지에 라벨이 없는 것이므로 프레이머 화면을 보고 값을 채우고 사유를 커밋 메시지에 적는다.

- [ ] **Step 6: 사람 검토 (문구 왜곡 여부)**

아래 두 파일을 열어 https://byjunyoung.framer.website/works/birdy , /works/barisbrew 와 나란히 비교한다:
- `src/content/works/birdy/index.md` — 섹션 5개(PROBLEM/APPROACH/IMPLEMENTATION/IMPACT/REFLECTION), 볼드 리드, 번호 목록, 이미지 위치
- `src/content/works/barisbrew/index.md` — `## NOTE` 아래 한 단락, `kind: note`

틀린 곳은 임포터가 아니라 **생성된 md를 직접 고친다** (일회성 도구를 완벽하게 만들 이유 없음). 단, 여러 페이지에 같은 패턴으로 틀리면 임포터를 고치고 재실행.

- [ ] **Step 7: 커밋**

```bash
node --test tests/
git add -A
git commit -m "content: import 8 works and 5 activities from framer export"
```

---

### Task 4: 프레이머 MCP로 CMS 필드·초안 대조 (플러그인이 켜져 있을 때만)

**Files:**
- Modify: `src/content/works/*/index.md`, `src/content/activities/*/index.md` (값 보정만)

**Interfaces:**
- Consumes: MCP 도구 `mcp__framer__getCMSCollections`, `mcp__framer__getCMSItems`. 연결 조건: 프레이머에서 Portfolio 프로젝트를 열고 Cmd+K → MCP 플러그인 실행. 안 켜져 있으면 "Framer plugin not connected" 에러 — 그 경우 이 Task는 건너뛰고 미결로 남긴다.

- [ ] **Step 1: 연결 확인**

`mcp__framer__getProjectWebsiteUrl` 호출. 에러면 사용자에게 플러그인을 켜 달라고 한 번 요청하고, 그래도 안 되면 Task 종료(미결 기록).

- [ ] **Step 2: 컬렉션·아이템 읽기**

`getCMSCollections` → works/activities 컬렉션 id와 필드 목록. 각각 `getCMSItems`로 전 항목을 받는다. 확인할 것:
1. 필드 목록이 스키마(org·year·role·responsibilities·with·keywords·link)와 대응하는지. CMS에만 있는 필드(예: 태그, 회사 enum)는 `tags`에 반영.
2. `draft` 상태 항목 — 공개 사이트에 없던 초안이 있으면 `draft: true`로 추가 생성.
3. uxeed·dino·internview 본문이 CMS에 있는지 → 있으면 md 본문 채우고 `draft: false`.

- [ ] **Step 3: 차이를 표로 사용자에게 보여주고, 확인 후 md 반영**

형식: `| slug | 필드 | 사이트(md) | CMS | 조치 |`. 반영 후 `npm test` 통과, 커밋 `content: reconcile with framer cms`.

---

### Task 5: 전역 스타일·레이아웃·홈 그리드·카드

**Files:**
- Create: `src/styles/global.css`, `src/layouts/Base.astro`, `src/components/WorkCard.astro`
- Modify: `src/pages/index.astro`

**Interfaces:**
- Produces: `Base` props `{ title?: string; description?: string; ogImage?: string }`. CSS 클래스 `.wrap .label .intro .grid .card .badge .tags .hero .detail .detail-head .metacard .prose .next .rows` (뒤 Task가 그대로 쓴다).

- [ ] **Step 1: 토큰과 전역 스타일**

```css
/* src/styles/global.css */
:root {
  --bg: #f6f6f4;
  --fg: #141414;
  --muted: #707070;
  --line: #e2e2df;
  --tint: #ececea;
  --max: 1120px;
  --pad: 24px;
  --gap: 24px;
  --fs-xs: 11px;
  --fs-sm: 13px;
  --fs-md: 15px;
  --fs-lg: 18px;
  --font: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto,
    "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
}
* { box-sizing: border-box; }
html { background: var(--bg); color: var(--fg); font-family: var(--font); font-size: var(--fs-md); line-height: 1.65; -webkit-font-smoothing: antialiased; word-break: keep-all; }
body { margin: 0; }
a { color: inherit; text-decoration: none; }
img, video { display: block; max-width: 100%; height: auto; }
.wrap { max-width: var(--max); margin: 0 auto; padding: 0 var(--pad); }

.nav { position: sticky; top: 0; z-index: 10; display: flex; justify-content: space-between; align-items: center; max-width: var(--max); margin: 0 auto; padding: 16px var(--pad); background: color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter: blur(8px); font-size: var(--fs-sm); }
.nav nav { display: flex; gap: 16px; }
.nav a:hover { color: var(--muted); }

.label { font-size: var(--fs-xs); letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); margin: 32px 0 8px; }
.intro { max-width: 560px; margin: 0 0 48px; color: var(--muted); font-size: var(--fs-sm); }

.grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 40px var(--gap); margin-bottom: 96px; }
@media (max-width: 720px) { .grid { grid-template-columns: 1fr; } }
.card .media { aspect-ratio: 4 / 3; overflow: hidden; background: var(--tint); }
.card .media img, .card .media video { width: 100%; height: 100%; object-fit: cover; }
.card h2 { font-size: var(--fs-md); font-weight: 600; margin: 14px 0 2px; }
.card .sub { margin: 0; }
.card .meta { display: flex; gap: 8px; align-items: center; margin-top: 6px; font-size: var(--fs-sm); color: var(--muted); }
.badge { font-size: var(--fs-xs); letter-spacing: 0.04em; padding: 1px 6px; border: 1px solid var(--line); border-radius: 3px; color: var(--muted); }
.tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; font-size: var(--fs-xs); color: var(--muted); }

.hero { margin: 8px 0 32px; background: var(--tint); }
.hero img, .hero video { width: 100%; }
.detail { display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 48px; align-items: start; margin-bottom: 48px; }
@media (max-width: 860px) { .detail { grid-template-columns: 1fr; } }
.detail-head h1 { font-size: var(--fs-lg); font-weight: 600; margin: 0 0 4px; }
.detail-head p { margin: 0; color: var(--muted); }
.metacard { background: var(--tint); padding: 20px; font-size: var(--fs-sm); display: grid; gap: 14px; margin: 0; }
.metacard dl { margin: 0; }
.metacard dt { font-size: var(--fs-xs); letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); }
.metacard dd { margin: 2px 0 0; }
.metacard a { text-decoration: underline; }

.prose > :not(img):not(video):not(p:has(> img)) { max-width: 640px; }
.prose h2 { font-size: var(--fs-xs); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin: 56px 0 12px; padding-top: 12px; border-top: 1px solid var(--line); }
.prose h3 { font-size: var(--fs-md); font-weight: 600; margin: 28px 0 8px; }
.prose p { margin: 0 0 14px; }
.prose li { margin: 0 0 8px; }
.prose img, .prose video { width: 100%; margin: 24px 0; background: var(--tint); }
.prose p:has(> img + img) { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.prose p:has(> img + img) img { margin: 0; }
.prose blockquote { margin: 24px 0; padding: 16px 20px; background: var(--tint); }
.prose blockquote p { margin: 0; }

.next { margin: 96px 0; padding-top: 24px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; font-size: var(--fs-sm); }

.rows { margin: 0 0 96px; padding: 0; list-style: none; border-top: 1px solid var(--line); }
.rows li { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr; gap: 16px; padding: 18px 0; border-bottom: 1px solid var(--line); font-size: var(--fs-sm); }
.rows li .t { font-weight: 600; }
.rows li .m { color: var(--muted); }
@media (max-width: 720px) { .rows li { grid-template-columns: 1fr; gap: 2px; } }

.footer { display: flex; justify-content: space-between; padding-top: 24px; padding-bottom: 48px; border-top: 1px solid var(--line); font-size: var(--fs-sm); color: var(--muted); }
.footer .n { color: var(--fg); }
.footer-links { display: flex; gap: 16px; }
```

- [ ] **Step 2: 기본 레이아웃**

```astro
---
// src/layouts/Base.astro
import '../styles/global.css';
interface Props { title?: string; description?: string; ogImage?: string }
const {
  title,
  description = 'Hardware UX designer. I design the part of products that lives beyond the screen — form, touch, space, feedback.',
  ogImage,
} = Astro.props;
const fullTitle = title ? `${title} — Junyoung Kim` : 'Junyoung Kim';
const canonical = new URL(Astro.url.pathname, Astro.site);
---
<!doctype html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{fullTitle}</title>
    <meta name="description" content={description} />
    <link rel="canonical" href={canonical} />
    <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
    <link rel="sitemap" href="/sitemap-index.xml" />
    <meta property="og:title" content={fullTitle} />
    <meta property="og:description" content={description} />
    {ogImage && <meta property="og:image" content={new URL(ogImage, Astro.site)} />}
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" />
  </head>
  <body>
    <header class="nav">
      <a href="/">Junyoung Kim</a>
      <nav>
        <a href="/">works</a>
        <a href="/activities/">activities</a>
        <a href="https://byjunyoung.github.io/resume/">resume</a>
      </nav>
    </header>
    <main class="wrap"><slot /></main>
    <footer class="footer wrap">
      <div>
        <div class="n">Junyoung Kim</div>
        <a href="mailto:junyoung735@gmail.com">junyoung735@gmail.com</a>
      </div>
      <div class="footer-links">
        <a href="https://www.linkedin.com/in/byjunyoung/">LinkedIn</a>
        <a href="https://www.instagram.com/byjunyoung/">Instagram</a>
      </div>
    </footer>
  </body>
</html>
```

- [ ] **Step 3: 카드 컴포넌트**

```astro
---
// src/components/WorkCard.astro
import { Image } from 'astro:assets';
import type { CollectionEntry } from 'astro:content';
interface Props { entry: CollectionEntry<'works'> }
const { entry } = Astro.props;
const d = entry.data;
---
<a class="card" href={`/works/${entry.id}/`}>
  <div class="media">
    {d.loop
      ? <video src={d.loop} poster={d.cover.src} autoplay muted loop playsinline preload="metadata"></video>
      : <Image src={d.cover} alt={d.title} widths={[640, 960, 1280]} sizes="(max-width: 720px) 100vw, 560px" />}
  </div>
  <h2>{d.title}</h2>
  <p class="sub">{d.subtitle}</p>
  <div class="meta">
    <span>{d.org}</span><span>·</span><span>{d.year}</span>
    <span class="badge">{d.kind === 'case-study' ? 'Case study' : 'Note'}</span>
  </div>
  <div class="tags">{d.tags.map((t) => <span>{t}</span>)}</div>
</a>
```

- [ ] **Step 4: 홈**

```astro
---
// src/pages/index.astro
import Base from '../layouts/Base.astro';
import WorkCard from '../components/WorkCard.astro';
import { getCollection } from 'astro:content';
const works = (await getCollection('works', ({ data }) => !data.draft)).sort((a, b) => a.data.order - b.data.order);
---
<Base>
  <p class="label">Works</p>
  <p class="intro">Hardware UX designer. I design the part of products that lives beyond the screen — form, touch, space, feedback. Currently shipping BarisBrew at XYZ Inc., previously the Dot Pad tactile display.</p>
  <section class="grid">{works.map((w) => <WorkCard entry={w} />)}</section>
</Base>
```

- [ ] **Step 5: 확인**

Run: `npm test`
Expected: 통과. `home links every published work` 테스트가 이제 실제로 8개 링크를 검사한다.
Run: `npm run dev` 후 http://localhost:4321/ 을 크롬으로 열어 스크린샷 1장. 2열 그리드, 카드마다 뱃지, 폰트가 Pretendard(콘솔에 CDN 404 없음).

- [ ] **Step 6: 커밋**

```bash
git add -A && git commit -m "feat: base layout, tokens, home grid with work cards"
```

---

### Task 6: 프로젝트 상세 페이지

**Files:**
- Create: `src/components/MetaCard.astro`, `src/pages/works/[slug].astro`

**Interfaces:**
- Consumes: Task 5의 `.hero .detail .detail-head .metacard .prose .next`, `Base`.
- Produces: `MetaCard` props `{ rows: Array<{ label: string; value?: string; href?: string }> }` (Task 7이 재사용).

- [ ] **Step 1: 메타 카드**

```astro
---
// src/components/MetaCard.astro
interface Props { rows: Array<{ label: string; value?: string; href?: string }> }
const { rows } = Astro.props;
---
<aside class="metacard">
  {rows.filter((r) => r.value).map((r) => (
    <dl>
      <dt>{r.label}</dt>
      <dd>{r.href ? <a href={r.href} target="_blank" rel="noopener">{r.value}</a> : r.value}</dd>
    </dl>
  ))}
</aside>
```

- [ ] **Step 2: 상세 페이지**

```astro
---
// src/pages/works/[slug].astro
import Base from '../../layouts/Base.astro';
import MetaCard from '../../components/MetaCard.astro';
import { Image } from 'astro:assets';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const works = (await getCollection('works', ({ data }) => !data.draft)).sort((a, b) => a.data.order - b.data.order);
  return works.map((entry, i) => ({ params: { slug: entry.id }, props: { entry, next: works[(i + 1) % works.length] } }));
}
const { entry, next } = Astro.props;
const d = entry.data;
const { Content } = await render(entry);
const rows = [
  { label: 'Organization', value: d.org },
  { label: 'Year', value: d.year },
  { label: 'Role', value: d.role },
  { label: 'Responsibilities', value: d.responsibilities.join(', ') },
  { label: 'With', value: d.with },
  { label: 'Keywords', value: d.keywords.join(', ') || undefined },
  { label: 'Link', value: d.link?.label, href: d.link?.url },
  { label: 'Press', value: d.press.map((p) => p.label).join(', ') || undefined },
  { label: 'Awards', value: d.awards.join(', ') || undefined },
];
---
<Base title={d.title} description={d.subtitle} ogImage={d.cover.src}>
  <div class="hero">
    {d.loop
      ? <video src={d.loop} poster={d.cover.src} autoplay muted loop playsinline></video>
      : <Image src={d.cover} alt={d.title} widths={[960, 1440, 2000]} sizes="(max-width: 1120px) 100vw, 1120px" />}
  </div>
  <div class="detail">
    <div class="detail-head"><h1>{d.title}</h1><p>{d.subtitle}</p></div>
    <MetaCard rows={rows} />
  </div>
  <article class="prose"><Content /></article>
  <nav class="next"><a href="/">← Works</a><a href={`/works/${next.id}/`}>{next.data.title} →</a></nav>
</Base>
```

- [ ] **Step 3: 확인**

Run: `npm test`
Expected: 통과, `dist/works/{8}/index.html`.
크롬으로 http://localhost:4321/works/birdy/ 와 /works/barisbrew/ 스크린샷 각 1장(상단 + 스크롤 1회). 확인: 히어로 → 제목/부제 + 메타 카드 2열 → 본문 텍스트 640px, 이미지는 전폭, `## PROBLEM` 이 작은 대문자 라벨로. barisbrew는 `Note` 한 단락. 다음 프로젝트 링크가 순환.

- [ ] **Step 4: 커밋**

```bash
git add -A && git commit -m "feat: work detail page with meta card and prose media"
```

---

### Task 7: 활동 목록·상세

**Files:**
- Create: `src/pages/activities/index.astro`, `src/pages/activities/[slug].astro`

**Interfaces:**
- Consumes: 컬렉션 `activities`, `.rows`, `MetaCard`, `.prose`.

- [ ] **Step 1: 목록**

```astro
---
// src/pages/activities/index.astro
import Base from '../../layouts/Base.astro';
import { getCollection } from 'astro:content';
const acts = (await getCollection('activities', ({ data }) => !data.draft)).sort((a, b) => a.data.order - b.data.order);
---
<Base title="Activities">
  <p class="label">Activities</p>
  <p class="intro">Discover my journey beyond design projects, where community events, interviews, and hands-on projects come together. Each activity reflects my drive to connect, share knowledge, and contribute to a thriving, collaborative design community.</p>
  <ul class="rows">
    {acts.map((a) => (
      <li>
        <a class="t" href={`/activities/${a.id}/`}>{a.data.title}</a>
        <span>{a.data.subtitle}</span>
        <span class="m">{a.data.role}</span>
        <span class="m">{a.data.period}</span>
      </li>
    ))}
  </ul>
</Base>
```

- [ ] **Step 2: 상세**

```astro
---
// src/pages/activities/[slug].astro
import Base from '../../layouts/Base.astro';
import MetaCard from '../../components/MetaCard.astro';
import { Image } from 'astro:assets';
import { getCollection, render } from 'astro:content';

export async function getStaticPaths() {
  const acts = await getCollection('activities', ({ data }) => !data.draft);
  return acts.map((entry) => ({ params: { slug: entry.id }, props: { entry } }));
}
const { entry } = Astro.props;
const d = entry.data;
const { Content } = await render(entry);
const rows = [
  { label: 'Role', value: d.role },
  { label: 'Period', value: d.period },
  ...d.links.map((l) => ({ label: 'Link', value: l.label, href: l.url })),
];
---
<Base title={d.title} description={d.subtitle} ogImage={d.cover?.src}>
  {d.cover && <div class="hero"><Image src={d.cover} alt={d.title} widths={[960, 1440, 2000]} sizes="(max-width: 1120px) 100vw, 1120px" /></div>}
  <div class="detail">
    <div class="detail-head"><h1>{d.title}</h1><p>{d.subtitle}</p></div>
    <MetaCard rows={rows} />
  </div>
  <article class="prose"><Content /></article>
  <nav class="next"><a href="/activities/">← Activities</a><span></span></nav>
</Base>
```

- [ ] **Step 3: 확인·커밋**

Run: `npm test` → 통과, `dist/activities/index.html`, `dist/activities/{hux,svip}/index.html`. 크롬 스크린샷 /activities/ 1장.

```bash
git add -A && git commit -m "feat: activities list and detail pages"
```

---

### Task 8: 시각 검수 게이트 (레퍼런스 대조 + 반응형)

**Files:** 없음 (검수 결과에 따라 `global.css` 값만 조정)

- [ ] **Step 1: 스크린샷 세트 만들기**

`npm run preview` 후 크롬으로 1280px 폭과 390px 폭에서 각각: 홈, /works/birdy/, /works/barisbrew/, /activities/. 파일로 저장해 사용자에게 보낸다(SendUserFile). 레퍼런스 비교용으로 `~/Documents/Claude/portfolio-import/reference-screenshots/`의 Special Projects·Simo Lahtinen 스크린샷도 함께.

- [ ] **Step 2: 사용자 검토 → 조정**

체크리스트를 사용자에게 제시하고 답을 받는다: (1) 카드 비율 4:3이 사진에 맞는가 (2) 텍스트 크기·회색 톤 (3) 메타 카드 배경 톤 (4) 섹션 라벨 스타일 (5) 모바일에서 카드 1열·메타 카드가 본문 앞에 오는 순서. 조정은 `global.css` 토큰·값만 바꾼다. 승인 전까지 다음 Task로 가지 않는다.

- [ ] **Step 3: 커밋 + 배포 푸시 (go 게이트)**

승인되면 "지금까지 커밋을 main에 푸시해 배포합니다 — go?" 를 받고:

```bash
git add -A && git commit -m "style: tune tokens after visual review" && git push origin main
```

Expected: Actions 성공, https://byjunyoung.github.io/ 에 새 디자인.

---

### Task 9: 관리 스크립트 + CLAUDE.md

**Files:**
- Create: `scripts/new-work.mjs`, `scripts/media.mjs`, `tests/scripts.test.mjs`, `CLAUDE.md`

**Interfaces:**
- Produces: `npm run new:work <slug>` → `src/content/works/<slug>/index.md`(draft). `npm run media -- <slug> <input> [--name loop] [--start 0] [--dur 8] [--width 1600]` → `public/media/works/<slug>/<name>.mp4`.
- 내보내는 순수 함수: `renderTemplate(slug, order)`, `createWork(slug, root, order)`, `parseArgs(argv)`, `ffmpegArgs({input,start,dur,width,out})`.

- [ ] **Step 1: 실패하는 테스트**

`tests/scripts.test.mjs`:

```js
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
```

Run: `node --test tests/scripts.test.mjs`
Expected: FAIL (모듈 없음).

- [ ] **Step 2: new-work.mjs**

```js
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
```

- [ ] **Step 3: media.mjs**

```js
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
```

- [ ] **Step 4: 테스트 통과**

Run: `node --test tests/scripts.test.mjs`
Expected: 4 tests OK.

- [ ] **Step 5: CLAUDE.md**

```md
# CLAUDE.md — byjunyoung.github.io

Junyoung Kim 포트폴리오. Astro 정적 사이트, GitHub Pages(main 푸시 → 자동 배포).
설계는 `docs/superpowers/specs/2026-09-04-portfolio-site-design.md`. 결정을 바꾸면 그 문서부터 고친다.

## 콘텐츠가 유일한 소스
- 프로젝트: `src/content/works/{slug}/index.md` + `cover.*` + 본문 이미지 `01.jpg …`
- 활동: `src/content/activities/{slug}/index.md` + `cover.*`
- 스키마: `src/content.config.ts`. 필드가 틀리면 빌드가 실패한다 — 스키마를 바꾸지 말고 콘텐츠를 고친다.
- `draft: true` 는 빌드에서 빠진다. `order` 가 홈 정렬. `kind` 는 `case-study` | `note`(본문 없이 한 단락).

## 프로젝트 추가 절차
1. `npm run new:work <slug>` → 템플릿 생성 (draft)
2. `cover.jpg` (긴 변 2000px 이하) 를 폴더에 넣고 frontmatter를 채운다
3. 본문은 마크다운. 섹션 제목은 `## PROBLEM` 처럼 대문자 h2 (관례, 강제 아님)
4. 영상: `npm run media -- <slug> <원본.mov> [--start 초] [--dur 초]` → `public/media/works/<slug>/loop.mp4`, 출력에 찍힌 `loop:` 줄을 frontmatter에 붙인다
5. `npm test` 통과 → 커밋 → push

## 본문 관례
- 이미지 한 줄 = 전폭. 같은 줄에 이미지 두 개(`![](./02.jpg) ![](./03.jpg)`) = 2-up 그리드
- 본문 영상: `<video src="/media/works/<slug>/02.mp4" autoplay muted loop playsinline></video>`
- 인용: `>` 블록 = 연한 배경 박스
- 이미지는 반드시 마크다운 문법(`![]()`)으로. `<img>` 를 쓰면 최적화되지 않는다

## 문구 원칙
- 담백하고 사실만. 제공되지 않은 사실·수치·효과를 만들거나 부풀리지 않는다.
- 어려운 용어·장황한 수식 자제. 삭제로 문단 구성이 바뀌면 앞뒤를 자연스럽게 다듬는다.
- 영어 카피(홈·활동 소개문)는 현재 문구 유지. 바꾸려면 사용자 확인.

## 스타일
- 색·크기·간격은 `src/styles/global.css` 토큰만. 컴포넌트에 hex·px 하드코딩 금지.
- 폰트 Pretendard Variable 하나. 모션은 루프 영상뿐 — 스크롤 애니메이션·트랜지션 라이브러리 금지.
- 의존성 추가 금지(astro, @astrojs/sitemap, sharp 외). 필요하면 이유를 적고 사용자 확인.

## 미디어 한도
- 영상: 무음 H.264 mp4, 8초 이내, 파일당 3MB 목표, 프로젝트당 20MB 이내. `public/media/works/<slug>/` 에만.
- Git LFS 금지 (Pages가 서빙 못 함). 원본은 레포 밖 `~/Documents/Claude/portfolio-import/`.
- 저장소 1GB 권장 한도 — `du -sh public src/content` 로 가끔 확인.

## 검증
- `npm test` = 빌드 + dist 검증. `npm run check` = 타입.
- 화면 확인은 `npm run dev` 후 크롬 스크린샷. 디자인 변경은 스크린샷을 사용자에게 보여주고 승인 후 push.
```

- [ ] **Step 6: 커밋**

```bash
npm test
git add -A && git commit -m "chore: new:work and media scripts, CLAUDE.md"
```

---

### Task 10: SEO·404·파비콘·robots

**Files:**
- Create: `src/pages/404.astro`, `public/favicon.svg`, `public/robots.txt`

- [ ] **Step 1: 파일 작성**

```astro
---
// src/pages/404.astro
import Base from '../layouts/Base.astro';
---
<Base title="Not found">
  <p class="label">404</p>
  <p class="intro">페이지가 없습니다. <a href="/" style="text-decoration: underline">홈으로</a></p>
</Base>
```

`public/favicon.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#141414"/><text x="16" y="21" text-anchor="middle" font-family="Pretendard, Inter, system-ui, sans-serif" font-size="16" font-weight="600" fill="#f6f6f4">J</text></svg>
```

`public/robots.txt`:

```
User-agent: *
Allow: /
Sitemap: https://byjunyoung.github.io/sitemap-index.xml
```

- [ ] **Step 2: 확인·커밋**

Run: `npm test && ls dist/sitemap-index.xml dist/404.html dist/favicon.svg dist/robots.txt`
Expected: 네 파일 존재. `grep -c '<url>' dist/sitemap-0.xml` ≥ 11.

```bash
git add -A && git commit -m "feat: 404, favicon, robots, sitemap check"
```

---

### Task 11: 영상 수집·변환·연결 (사용자 자료 필요)

**Files:**
- Create: `public/media/works/{slug}/loop.mp4`
- Modify: `src/content/works/{slug}/index.md` (`loop:` 추가)

- [ ] **Step 1: 영상 위치 확인**

사용자에게 한 번 묻는다: 프로젝트별 영상이 어디 있는지(로컬 경로 / 드라이브 / 유튜브). 드라이브·유튜브면 다운로드를 사용자가 직접 해서 `~/Documents/Claude/portfolio-import/video/<slug>/` 에 넣도록 안내한다(다운로드는 대행하지 않는다).

- [ ] **Step 2: 변환**

프로젝트마다 가장 "손이 조작하고 제품이 반응하는" 구간을 고른다. 원본을 QuickTime으로 열어 시작 초를 확인하고:

```bash
npm run media -- birdy ~/Documents/Claude/portfolio-import/video/birdy/원본.mov --start 12 --dur 6
```

출력의 `loop:` 줄을 해당 `index.md` frontmatter에 붙인다. 3MB 초과 경고가 나면 `--dur` 를 줄인다.

- [ ] **Step 3: 확인**

Run: `npm test` (loop 파일 존재 테스트 포함). `npm run dev` 후 크롬에서 홈 스크린샷 2장(2초 간격) — 카드 프레임이 달라져 있으면 자동 재생 중. 사용자에게 스크린샷을 보낸다.

- [ ] **Step 4: 커밋·푸시 (go 게이트)**

`du -sh public/media` 를 함께 보여주고 go 후:

```bash
git add -A && git commit -m "content: loop videos for works" && git push origin main
```

---

### Task 12: 마무리

**Files:**
- Modify: `docs/superpowers/specs/2026-09-04-portfolio-site-design.md` (9. 미결 갱신), 메모리 `~/.claude/projects/-Users-junyoungkim/memory/portfolio-site-framer.md`

- [ ] **Step 1: 프레이머 사이트 처리 — 사용자 결정**

선택지를 AskUserQuestion으로: (a) 프레이머 사이트 유지하되 홈 상단에 새 주소 안내 한 줄 (b) 프레이머 언퍼블리시 (c) 그대로 둠. 프레이머 쓰기는 미리보기 → go.

- [ ] **Step 2: 커스텀 도메인 (있을 때만)**

도메인이 있으면 `public/CNAME` 에 도메인 한 줄, `astro.config.mjs`의 `site`를 그 도메인으로, DNS는 사용자가 GitHub 안내대로 설정. 없으면 건너뛴다.

- [ ] **Step 3: 문서·메모리 갱신**

- 설계 문서 9장 미결 항목을 결과로 바꾼다(도메인·영상 위치·활동 3개·프레이머 처리).
- 메모리 파일에 새 주소·레포·"콘텐츠는 md, 스크립트 두 개, CLAUDE.md 참조" 를 적고 MEMORY.md 한 줄 갱신.

```bash
git add -A && git commit -m "docs: close out spec open items" && git push origin main
```

---

### Task 13: 디자인 패스 — 프레이머와 거리 두기 (Task 8 검수 결과)

사용자 피드백(2026-09-05): "디자인이 너무 프레이머 따라한 것 같다." 검수에서 발견한 결함 2개(상세 페이지 좌측 빈 공간, 히어로 지연 로딩)와 함께 한 번에 고친다. 방향은 설계 §2의 레퍼런스에서 가져온다: 스페셜 프로젝트(연회색 캔버스 위 밝은 패널, 가운데 워드마크, 표 형태 메타 카드, 굵은 소제목 + 짧은 밑줄, 플로트 메타 카드 옆에서 본문 시작), TE(카탈로그식 인덱스 번호).

**Files:**
- Modify: `src/styles/global.css` (전체 교체), `src/layouts/Base.astro` (header만), `src/components/WorkCard.astro` (전체 교체), `src/pages/index.astro` (카드 호출), `src/pages/works/[slug].astro` (히어로 loading), `src/pages/activities/[slug].astro` (히어로 loading)

**Interfaces:**
- `WorkCard` props become `{ entry: CollectionEntry<'works'>; index: number; eager?: boolean }`.
- `MetaCard` unchanged (dl/dt/dd). CSS class names unchanged except new `.mark`, `.card .body/.row/.idx/.org`.

- [ ] **Step 1: global.css 전체 교체**

```css
/* src/styles/global.css */
:root {
  --bg: #e9e9e6;
  --surface: #f7f7f5;
  --tint: #efefec;
  --fg: #161616;
  --muted: #6f6f6f;
  --line: #d6d6d2;
  --max: 1120px;
  --pad: 24px;
  --gap: 24px;
  --fs-xs: 11px;
  --fs-sm: 13px;
  --fs-md: 15px;
  --fs-lg: 20px;
  --font: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont, system-ui, Roboto,
    "Helvetica Neue", "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
}
* { box-sizing: border-box; }
html { background: var(--bg); color: var(--fg); font-family: var(--font); font-size: var(--fs-md); line-height: 1.65; -webkit-font-smoothing: antialiased; word-break: keep-all; }
body { margin: 0; }
a { color: inherit; text-decoration: none; }
img, video { display: block; max-width: 100%; height: auto; }
.wrap { max-width: var(--max); margin: 0 auto; padding: 0 var(--pad); }

.nav { display: flex; flex-direction: column; align-items: center; gap: 10px; max-width: var(--max); margin: 0 auto; padding: 28px var(--pad) 20px; border-bottom: 1px solid var(--line); }
.nav .mark { font-size: var(--fs-md); font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; }
.nav nav { display: flex; gap: 20px; font-size: var(--fs-xs); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }
.nav nav a:hover { color: var(--fg); }

.label { font-size: var(--fs-xs); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); text-align: center; margin: 40px 0 8px; }
.intro { max-width: 620px; margin: 0 auto 48px; text-align: center; color: var(--muted); font-size: var(--fs-sm); }

.grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--gap); margin-bottom: 96px; }
@media (max-width: 720px) { .grid { grid-template-columns: 1fr; } }
.card { display: block; background: var(--surface); border: 1px solid var(--line); }
.card .media { aspect-ratio: 4 / 3; overflow: hidden; background: var(--tint); border-bottom: 1px solid var(--line); }
.card .media img, .card .media video { width: 100%; height: 100%; object-fit: cover; }
.card .body { padding: 16px 18px 18px; background: var(--tint); }
.card .row { display: flex; justify-content: space-between; align-items: baseline; gap: 12px; }
.card h2 { font-size: var(--fs-md); font-weight: 600; margin: 0; }
.card .idx { font-size: var(--fs-xs); letter-spacing: 0.08em; color: var(--muted); }
.card .org { margin: 10px 0 2px; font-size: var(--fs-sm); font-weight: 600; }
.card .sub { margin: 0; font-size: var(--fs-sm); }
.card .meta { display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: center; margin-top: 12px; font-size: var(--fs-xs); letter-spacing: 0.04em; text-transform: uppercase; color: var(--muted); }
.badge { padding: 2px 6px; border: 1px solid var(--line); border-radius: 2px; }

.hero { margin: 24px 0 32px; background: var(--surface); border: 1px solid var(--line); }
.hero img, .hero video { width: 100%; }
.detail { margin-bottom: 8px; }
.detail-head h1 { font-size: var(--fs-lg); font-weight: 600; margin: 0 0 4px; }
.detail-head p { margin: 0 0 24px; color: var(--muted); }
.metacard { float: right; width: 360px; margin: 0 0 32px 48px; background: var(--surface); border: 1px solid var(--line); font-size: var(--fs-sm); }
.metacard dl { margin: 0; padding: 12px 16px; border-bottom: 1px solid var(--line); }
.metacard dl:last-child { border-bottom: 0; }
.metacard dl:nth-child(odd) { background: var(--tint); }
.metacard dt { font-size: var(--fs-xs); letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin-bottom: 2px; }
.metacard dd { margin: 0; }
.metacard a { text-decoration: underline; }
@media (max-width: 860px) { .metacard { float: none; width: auto; margin: 0 0 32px; } }

.prose > :not(img):not(video):not(p:has(> img)) { max-width: 640px; }
.prose h2 { font-size: var(--fs-sm); font-weight: 600; letter-spacing: 0.06em; margin: 48px 0 16px; }
.prose h2::after { content: ""; display: block; width: 28px; height: 2px; background: var(--fg); margin-top: 8px; }
.prose h3 { font-size: var(--fs-md); font-weight: 600; margin: 28px 0 8px; }
.prose p { margin: 0 0 14px; }
.prose li { margin: 0 0 8px; }
.prose img, .prose video { width: 100%; margin: 28px 0; background: var(--surface); border: 1px solid var(--line); clear: both; }
.prose p:has(> img) { max-width: none; clear: both; }
.prose p:has(> img + img) { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.prose p:has(> img + img) img { margin: 0; }
.prose blockquote { margin: 24px 0; padding: 16px 20px; background: var(--surface); border: 1px solid var(--line); }
.prose blockquote p { margin: 0; }

.next { clear: both; margin: 96px 0; padding-top: 24px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; font-size: var(--fs-sm); }

.rows { margin: 0 0 96px; padding: 0; list-style: none; background: var(--surface); border: 1px solid var(--line); }
.rows li { display: grid; grid-template-columns: 2fr 3fr 1fr 1fr; gap: 16px; padding: 18px 20px; border-bottom: 1px solid var(--line); font-size: var(--fs-sm); }
.rows li:last-child { border-bottom: 0; }
.rows li .t { font-weight: 600; }
.rows li .m { color: var(--muted); }
@media (max-width: 720px) { .rows li { grid-template-columns: 1fr; gap: 2px; } }

.footer { display: flex; justify-content: space-between; padding-top: 24px; padding-bottom: 48px; border-top: 1px solid var(--line); font-size: var(--fs-sm); color: var(--muted); }
.footer .n { color: var(--fg); }
.footer-links { display: flex; gap: 16px; }
```

- [ ] **Step 2: Base.astro 헤더만 교체**

`<header class="nav">…</header>` 블록을 아래로 바꾼다 (나머지는 그대로):

```astro
    <header class="nav">
      <a class="mark" href="/">Junyoung Kim</a>
      <nav>
        <a href="/">works</a>
        <a href="/activities/">activities</a>
        <a href="https://byjunyoung.github.io/resume/">resume</a>
      </nav>
    </header>
```

- [ ] **Step 3: WorkCard.astro 전체 교체**

```astro
---
// src/components/WorkCard.astro
import { Image } from 'astro:assets';
import type { CollectionEntry } from 'astro:content';
interface Props { entry: CollectionEntry<'works'>; index: number; eager?: boolean }
const { entry, index, eager = false } = Astro.props;
const d = entry.data;
const idx = String(index).padStart(2, '0');
---
<a class="card" href={`/works/${entry.id}/`}>
  <div class="media">
    {d.loop
      ? <video src={d.loop} poster={d.cover.src} autoplay muted loop playsinline preload="metadata"></video>
      : <Image src={d.cover} alt={d.title} widths={[640, 960, 1280]} sizes="(max-width: 720px) 100vw, 560px" loading={eager ? 'eager' : 'lazy'} />}
  </div>
  <div class="body">
    <div class="row"><h2>{d.title}</h2><span class="idx">{idx}</span></div>
    <p class="org">{d.org} · {d.year}</p>
    <p class="sub">{d.subtitle}</p>
    <div class="meta">
      <span class="badge">{d.kind === 'case-study' ? 'Case study' : 'Note'}</span>
      {d.tags.map((t) => <span>{t}</span>)}
    </div>
  </div>
</a>
```

- [ ] **Step 4: index.astro 카드 호출**

`{works.map((w) => <WorkCard entry={w} />)}` → `{works.map((w, i) => <WorkCard entry={w} index={i + 1} eager={i < 2} />)}`

- [ ] **Step 5: 히어로 즉시 로딩**

`src/pages/works/[slug].astro` 와 `src/pages/activities/[slug].astro` 의 히어로 `<Image … />` 에 `loading="eager"` 속성을 추가한다 (video 분기는 그대로).

- [ ] **Step 6: 정적 확인·커밋**

`grep -nE '#[0-9a-fA-F]{3,6}\b' src/layouts src/components src/pages` → 없음. `grep -c 'loading="eager"' 'src/pages/works/[slug].astro' 'src/pages/activities/[slug].astro'` → 각 1.

```bash
git add -A && git commit -m "style: design pass — gray canvas, framed panels, centered wordmark, floated meta table, eager hero"
```

---

### Task 14: 유튜브 임베드 복원 · 활동 5개 노출 · 소셜 링크 · 흰 배경 (2차 검수 피드백)

사용자 피드백(2026-09-05): (1) 원본 프로젝트 페이지의 유튜브 영상이 모두 빠짐 (2) 활동이 많이 빠짐 (3) GitHub 등 소셜 링크 추가 (4) 디자인은 좋은데 배경은 흰색.

사실(확인됨): 원본 raw HTML에 `<iframe … src="https://www.youtube.com/embed/<ID>?…">` 가 works 7개 페이지에 있다 — adio 7O4_Z_1cJk8, barisbrew GnPiB19v5kQ, birdy YvDX9E_5jvk, dotcanvas AHK3VnjvA5Y·N_L3hR81nik, dotpad iSmRM2PUBzA, meemo nXMv4ztNLbA, zibot irJ2ge-0ZDw (storagy 없음, 총 8개 iframe). 활동 uxeed·dino·internview는 원본 상세가 비어 있어 `draft: true`였음. 이력서 기준 UXeed 기간 2022 – 2024. DINO·인턴뷰 기간은 사용자 확인 전까지 `—`.

**Files:**
- Modify: `scripts/import_framer.py`, `tests/test_import.py`, `src/styles/global.css`, `src/layouts/Base.astro`(footer), `AGENTS.md`(=CLAUDE.md 심링크)
- Regenerate: `src/content/works/*/index.md`(임베드 삽입), `src/content/activities/*/index.md`(draft/period)

- [ ] **Step 1: 실패하는 테스트 추가** (`tests/test_import.py`의 `ImportTest`에 메서드 추가)

```python
    def test_youtube_embed_block_in_order(self):
        html = ('<h1>T</h1><p>부제</p><h6>ORGANIZATION</h6><p>X</p><h6>YEAR</h6><p>2020</p><h6>ROLE</h6><p>R</p>'
                '<p>PROBLEM</p><p>첫 문단</p>'
                '<div><iframe title="Youtube Video" src="https://www.youtube.com/embed/YvDX9E_5jvk?rel=0&amp;x=1"></iframe></div>'
                '<p>둘째 문단</p><p>junyoung735@gmail.com</p>')
        page = imp.parse_page(html, set())
        body, imgs = imp.render_body(page['body'])
        i_first, i_embed, i_second = body.index('첫 문단'), body.index('class="embed"'), body.index('둘째 문단')
        self.assertTrue(i_first < i_embed < i_second)
        self.assertIn('https://www.youtube-nocookie.com/embed/YvDX9E_5jvk?rel=0&modestbranding=1', body)
        self.assertEqual(imgs, [])

    def test_control_chars_stripped(self):
        html = '<h1>T</h1><p>부제</p><h6>ROLE</h6><p>R</p><p>Note</p><p>가\x08나</p><p>junyoung735@gmail.com</p>'
        body, _ = imp.render_body(imp.parse_page(html, set())['body'])
        self.assertIn('가나', body)
        self.assertNotIn('\x08', body)
```

Run: `python3 -m unittest tests/test_import.py -v` → 두 테스트 FAIL.

- [ ] **Step 2: 임포터 수정** (기존 코드 구조를 유지하고 아래만 추가·변경)

1. `Walker.handle_starttag`: `img` 분기 앞에 iframe 처리 —
```python
        if tag == 'iframe' and 'youtube' in (a.get('src') or ''):
            m = re.search(r'/embed/([A-Za-z0-9_-]{6,})', a['src'])
            if m:
                self._flush('p')
                self.blocks.append(('embed', m.group(1), ''))
            return
```
2. `Walker._flush`: 텍스트 정규화 직후 제어문자 제거 — `text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)`.
3. `render_body`: `kind == 'img'` 분기 다음에 —
```python
        elif kind == 'embed':
            lines.append(f'<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/{text}?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>\n')
```
4. `blocks_of`의 이미지 dedup/필터 로직이 `embed` 블록을 버리지 않는지 확인(`b[0] == 'img'` 조건만 건드리도록).
5. `import_activities`: 빈 페이지 처리를 `draft = False`, `period = PERIODS.get(slug, '—')` 로 바꾸고 모듈 상단에 `PERIODS = {'uxeed': '2022 – 2024', 'dino': '—', 'internview': '—'}` 추가. 경고 문구는 `'empty page → meta only'`.

Run: `python3 -m unittest tests/test_import.py -v` → 전부 OK (기존 4 + 새 2).

- [ ] **Step 3: 임포터 재실행** (`npm run import:framer`). 제어문자 제거가 임포터에 들어갔으므로 dotcanvas 수동 수정은 재현된다. 확인:
- `grep -c 'class="embed"' src/content/works/*/index.md` → adio 1, barisbrew 1, birdy 1, dotcanvas 2, dotpad 1, meemo 1, storagy 0, zibot 1.
- `grep -l 'draft: true' src/content/activities/*/index.md` → 없음. `grep -h '^period' src/content/activities/*/index.md` → uxeed `"2022 – 2024"`, dino·internview `"—"`.
- `git diff --stat -- src/content` 에서 이미지 파일이 바뀌지 않았는지 (리사이즈는 결정적이라 바이트 동일해야 함; 다르면 보고).
- `git diff -- 'src/content/works/*/index.md' | grep '^[-+]' | grep -v '^[-+][-+]' | grep -v 'class="embed"'` → 빈 줄 외 출력 없음(임베드 삽입 외 본문 변화 없음).

- [ ] **Step 4: CSS** (`src/styles/global.css`)
- `:root`의 `--bg: #e9e9e6;` → `--bg: #ffffff;`. `--surface`·`--tint`·`--line` 유지(패널 구조 유지).
- `.prose > :not(img):not(video):not(p:has(> img))` → `.prose > :not(img):not(video):not(.embed):not(p:has(> img))`.
- `.prose blockquote` 규칙 뒤에 추가:
```css
.prose .embed { aspect-ratio: 16 / 9; width: 100%; margin: 28px 0; background: var(--surface); border: 1px solid var(--line); clear: both; }
.prose .embed iframe { width: 100%; height: 100%; border: 0; display: block; }
```

- [ ] **Step 5: 푸터 GitHub 링크** (`src/layouts/Base.astro`) — `.footer-links` 안 LinkedIn 앞에 `<a href="https://github.com/byjunyoung">GitHub</a>` 추가.

- [ ] **Step 6: CLAUDE.md 관례 추가** (`AGENTS.md`의 "## 본문 관례" 목록 끝에)
```
- 유튜브: `<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/<ID>?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allowfullscreen></iframe></div>` — 전폭 16:9
```

- [ ] **Step 7: 확인·커밋**
`node --test tests/scripts.test.mjs` 통과, `grep -c '<a href="https://github.com/byjunyoung">' src/layouts/Base.astro` → 1, `grep -n -- '--bg' src/styles/global.css` → `#ffffff`.
```bash
git add -A && git commit -m "content: restore youtube embeds, list all activities; style: white canvas, embed frame; footer github link"
```

---

### Task 15: 원본 이미지 그리드 복원 · 활동 목록 카드화 (3차 검수 피드백)

사용자 피드백(2026-09-05): (1) 활동 페이지가 너무 간소화됨 — 원본은 사진 카드 목록 (2) 상세 페이지에서 사진을 전부 전폭으로 나열하니 가독성이 떨어짐 — 원본의 그리드를 참고.

사실(확인됨, 원본 `<img sizes>`의 `(min-width: 1200px)` 값): `calc(min(100vw, 1200px) - 80px)` · `max(min(100vw, 1200px) - 80px, 1px)` · `1120px` · `100vw` = 전폭(1열); `max((min(100vw, 1200px) - 82px) / 2, 1px)` = 2열; `400px` = 3열. 예: birdy는 PROBLEM 전폭1 / APPROACH 전폭1 + 2열5 / 영상 / 전폭1 + 2열5 / IMPLEMENTATION 전폭3 / IMPACT 전폭1. 활동 상세 사진 5장은 3열(마키). 활동 목록 원본 = 사진 + 이름/한 줄/역할 카드.

**Files:**
- Modify: `scripts/import_framer.py`, `tests/test_import.py`, `src/styles/global.css`, `src/pages/activities/index.astro`, `AGENTS.md`
- Create: `src/components/ActivityCard.astro`
- Regenerate: `src/content/works/*/index.md`, `src/content/activities/*/index.md` (이미지 줄 묶음만 달라짐)

- [ ] **Step 1: 실패하는 테스트** — `tests/test_import.py`에 추가하고, 기존 `test_parse_page_title_meta_body`의 `page['body'][0]` 기대값을 `('img', 'https://framerusercontent.com/images/hero.jpg', 1)` 로 바꾼다 (블록 3번째 값이 alt → 열 수).

```python
    def test_cols_from_sizes(self):
        self.assertEqual(imp.cols_from_sizes('(min-width: 1200px) calc(min(100vw, 1200px) - 80px), (max-width: 809px) 100vw'), 1)
        self.assertEqual(imp.cols_from_sizes('(min-width: 1200px) max((min(100vw, 1200px) - 82px) / 2, 1px), (max-width: 809px) 100vw'), 2)
        self.assertEqual(imp.cols_from_sizes('(min-width: 1200px) 400px, (min-width: 810px) and (max-width: 1199px) 33vw'), 3)
        self.assertEqual(imp.cols_from_sizes('(min-width: 1200px) 1120px, (max-width: 809px) 100vw'), 1)
        self.assertEqual(imp.cols_from_sizes(''), 1)

    def test_render_groups_consecutive_images_by_cols(self):
        blocks = [('p', 'PROBLEM', False), ('p', '문단', False),
                  ('img', 'https://f/a.jpg', 2), ('img', 'https://f/b.jpg', 2), ('img', 'https://f/c.jpg', 2),
                  ('img', 'https://f/d.jpg', 1),
                  ('img', 'https://f/e.jpg', 3), ('img', 'https://f/f.jpg', 3), ('img', 'https://f/g.jpg', 3)]
        body, imgs = imp.render_body(blocks)
        lines = [l for l in body.splitlines() if l.startswith('![](')]
        self.assertEqual(lines, ['![](./01.jpg) ![](./02.jpg)', '![](./03.jpg)', '![](./04.jpg)',
                                 '![](./05.jpg) ![](./06.jpg) ![](./07.jpg)'])
        self.assertEqual([n for _, n in imgs], ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg'])
```

Run: `python3 -m unittest tests/test_import.py -v` → 새 테스트 2개 FAIL(+ 수정한 기존 테스트 1개 FAIL).

- [ ] **Step 2: 임포터**

1. 모듈 함수 추가:
```python
def cols_from_sizes(sizes):
    """Framer <img sizes>의 데스크톱(≥1200px) 값으로 원본 그리드 열 수를 읽는다."""
    m = re.search(r'\(min-width:\s*1200px\)\s*([^,]+)', sizes or '')
    v = m.group(1) if m else ''
    if '/ 2' in v:
        return 2
    if re.fullmatch(r'\s*(3[0-9]{2}|4[0-4][0-9])px\s*', v):
        return 3
    return 1
```
2. `Walker.handle_starttag`의 img 분기: `self.blocks.append(('img', a['src'].split('?')[0], cols_from_sizes(a.get('sizes'))))` (alt 대신 열 수).
3. `render_body`: 연속된 img 블록을 모아 열 수별로 줄을 만든다 — 같은 열 수의 연속 이미지를 `cols`개씩 끊어 한 줄에 공백으로 이어 붙인다(`![](./01.jpg) ![](./02.jpg)`), 열 수가 바뀌거나 텍스트/embed가 오면 묶음을 끝낸다. 각 이미지 줄 뒤엔 빈 줄. 파일명 번호는 등장 순서 그대로. 구현 예:
```python
    def flush_imgs():
        nonlocal pending
        if not pending:
            return
        cols = pending[0][1]
        for i in range(0, len(pending), cols):
            lines.append(' '.join(f'![](./{name})' for name, _ in pending[i:i + cols]) + '\n')
        pending = []
```
img 블록마다 `n += 1; name = …; imgs.append((url, name))` 후 `if pending and pending[0][1] != cols: flush_imgs()` 다음 `pending.append((name, cols))`; 다른 블록을 만나면 먼저 `flush_imgs()`; 루프 끝에도 `flush_imgs()`. `skip_url` 처리는 그대로.
4. `parse_page`의 hero 판별에서 `b[0] == 'img'` 조건은 그대로(튜플 3번째 값 변경 무관). `blocks_of`의 dedup/svg 필터도 그대로.

Run: `python3 -m unittest tests/test_import.py -v` → 전부 OK.

- [ ] **Step 3: 임포터 재실행** (`npm run import:framer`, sips 때문에 수 분). 확인:
- `grep -c '^!\[\](./[0-9]*\.[a-z]*) !\[\]' src/content/works/birdy/index.md` → 2열 줄이 4개 이상(APPROACH 5장 → 2+2+1 이 두 번).
- `grep -cE '^(!\[\]\([^)]*\) ){2}!\[\]' src/content/activities/svip/index.md` → 3열 줄 1개 이상.
- `git diff -- 'src/content/**/index.md' | grep '^[-+]' | grep -v '^[-+][-+]' | grep -vE '^\+?-?\s*$' | grep -v '!\[\]'` → 출력 없음(이미지 줄 외 본문 변화 없음). 활동 md의 `period`·`draft`는 유지돼야 한다(임포터 PERIODS가 이미 반영됨).
- `git diff --stat -- src/content | grep -vE 'index\.md'` → 이미지 파일 변화 없음.

- [ ] **Step 4: CSS** (`src/styles/global.css`, `.prose p:has(> img + img) img { margin: 0; }` 뒤에 추가)
```css
.prose p:has(> img + img + img) { grid-template-columns: repeat(3, 1fr); }
@media (max-width: 720px) { .prose p:has(> img + img) { grid-template-columns: 1fr; } }
```

- [ ] **Step 5: 활동 카드**

```astro
---
// src/components/ActivityCard.astro
import { Image } from 'astro:assets';
import type { CollectionEntry } from 'astro:content';
interface Props { entry: CollectionEntry<'activities'>; eager?: boolean }
const { entry, eager = false } = Astro.props;
const d = entry.data;
---
<a class="card" href={`/activities/${entry.id}/`}>
  <div class="media">
    {d.cover && <Image src={d.cover} alt={d.title} widths={[640, 960, 1280]} sizes="(max-width: 720px) 100vw, 560px" loading={eager ? 'eager' : 'lazy'} />}
  </div>
  <div class="body">
    <div class="row"><h2>{d.title}</h2></div>
    <p class="org">{d.role} · {d.period}</p>
    <p class="sub">{d.subtitle}</p>
  </div>
</a>
```

`src/pages/activities/index.astro`의 `<ul class="rows">…</ul>` 블록을 아래로 교체하고 상단 import에 `import ActivityCard from '../../components/ActivityCard.astro';` 추가:
```astro
  <section class="grid">{acts.map((a, i) => <ActivityCard entry={a} eager={i < 2} />)}</section>
```
(`.rows` CSS는 남겨 둔다 — 다른 곳에서 안 쓰지만 제거는 이 Task 범위 밖.)

- [ ] **Step 6: AGENTS.md 관례** — "## 본문 관례"의 2-up 줄을 아래로 바꾼다:
```
- 이미지 한 줄 = 전폭. 같은 줄에 두 개 = 2열, 세 개 = 3열 그리드 (`![](./02.jpg) ![](./03.jpg)`)
```

- [ ] **Step 7: 확인·커밋**
`python3 -m unittest tests/test_import.py` OK, `node --test tests/scripts.test.mjs` OK, `grep -c 'ActivityCard' src/pages/activities/index.astro` → 2.
```bash
git add -A && git commit -m "content: restore original image grids from framer sizes; activities as photo cards"
```
