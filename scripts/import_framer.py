#!/usr/bin/env python3
"""프레이머 공개 HTML(portfolio-import/framer-export/raw)을 콘텐츠 컬렉션으로 변환한다. 일회성.
사용: python3 scripts/import_framer.py [--dry]
"""
import json, re, shutil, subprocess, sys, urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORT = Path.home() / 'Documents/Claude/portfolio-import/framer-export'
ACTS_CMS = Path.home() / 'Documents/Claude/portfolio-import/cms/activities.json'
WORKS_OUT = ROOT / 'src/content/works'
ACTS_OUT = ROOT / 'src/content/activities'

WORK_ORDER = ['birdy', 'meemo', 'zibot', 'dotcanvas', 'adio', 'barisbrew', 'storagy', 'dotpad']
NOTE_ONLY = {'barisbrew', 'storagy', 'dotpad'}
ACT_ORDER = ['hux', 'uxeed', 'dino', 'svip', 'internview']   # activities 목록 페이지의 표시 순서
# 프레이머 CMS activities 컬렉션(id E_ju10rBl) 필드 id
ACT_FIELD = {'cover': 'A4TAvjUiL', 'title': 'xQgMccVzV', 'subtitle': 'NG0B_paBD', 'period': 'VXuQBHODd',
             'role': 'r654WdnKz', 'body': 'FGtWtwN8l', 'links': 'hYCcXEbYm'}
ACT_VIDEO_FIELDS = ['qVOdHx9fc', 'vrpP0BfX9', 'vWo1Vl6ep']
ACT_IMAGE_FIELDS = ['kC9O0vHO8', 'VUNIVtyBq', 'ytOV0971V', 'HlVBwh2Z6', 'IwhondQmL']
META = {'ORGANIZATION': 'org', 'YEAR': 'year', 'ROLE': 'role', 'RESPONSIBILITIES': 'responsibilities',
        'WITH': 'with', 'KEYWORDS': 'keywords', 'LINK': 'link', 'LINKS': 'links'}
STOP = ('junyoung735@gmail.com', 'Select Language', 'Create a free website')
RULE = re.compile(r'^[—–-]{1,3}$')
HEADING = re.compile(r'^[A-Z0-9][A-Z0-9 :&/\-]{1,40}$')


def is_link_href(href):
    """마크다운 링크로 옮길 대상: 외부 http(s) 링크와 사이트 내부 /works/·/activities/ 링크."""
    return bool(href) and (href.startswith('http') or href.startswith('/works/') or href.startswith('/activities/'))


def cols_from_sizes(sizes):
    """Framer <img sizes>의 데스크톱(≥1200px) 값으로 원본 그리드 열 수를 읽는다.
    항목 구분 콤마는 최상위(다음 항목이 '(min-width:'/'(max-width:'로 시작하는 지점)만 보고,
    calc()/max()/min() 안에 중첩된 콤마(예: min(100vw, 1200px))는 값의 일부로 취급한다."""
    m = re.search(r'\(min-width:\s*1200px\)\s*(.+?)(?:,\s*\((?:min|max)-width|\Z)', sizes or '')
    v = m.group(1) if m else ''
    # 코퍼스 전체에 `/ 2`(2열)뿐 아니라 `/ 3`(3열) 나눗셈 공식도 동일한 빈도로 쓰인다(원본 그리드).
    div = re.search(r'/\s*(\d+)\b', v)
    if div:
        return int(div.group(1))
    if re.fullmatch(r'\s*(3[0-9]{2}|4[0-4][0-9])px\s*', v):
        return 3
    return 1


def fix_bold_spacing(text):
    """`**` 안쪽 앞뒤 공백을 마커 밖으로 옮긴다. 원문 저작 시 <strong> 경계에 공백이 들쭉날쭉 들어가 있어
    (예: '<strong>레이블 </strong>본문' 처럼 여는/닫는 태그 안쪽에 공백이 남는 경우), 그대로 옮기면
    CommonMark의 여닫힘 규칙(마커 바로 안쪽에 공백이 있으면 무효)을 어겨 굵게 표시가 깨진다.
    문구·단어는 그대로 두고 공백 위치만 마커 밖으로 옮긴다."""
    parts = text.split('**')
    if len(parts) < 3 or len(parts) % 2 == 0:
        return text  # 마커 개수가 안 맞으면(홀수 쌍이 아니면) 손대지 않는다
    for i in range(1, len(parts), 2):
        inner = parts[i]
        lstripped = inner.lstrip()
        leading = inner[:len(inner) - len(lstripped)]
        stripped = lstripped.rstrip()
        trailing = lstripped[len(stripped):]
        parts[i] = stripped
        if leading:
            parts[i - 1] += leading
        if trailing:
            parts[i + 1] = trailing + parts[i + 1]
    return '**'.join(parts)


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
        if tag == 'iframe' and 'youtube' in (a.get('src') or ''):
            m = re.search(r'/embed/([A-Za-z0-9_-]{6,})', a['src'])
            if m:
                self._flush('p')
                self.blocks.append(('embed', m.group(1), ''))
            return
        if tag == 'img' and 'framerusercontent.com/images/' in (a.get('src') or ''):
            self._flush('p')
            self.blocks.append(('img', a['src'].split('?')[0], cols_from_sizes(a.get('sizes'))))
        elif tag == 'a' and is_link_href(a.get('href')):
            self._href = a['href']
            self._buf.append('[')
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
            self._buf.append(f']({self._href})')
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
        text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', '', text)
        text = fix_bold_spacing(text)
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
    """LINK/LINKS 메타 값에서 (라벨, url) 목록을 뽑는다. Walker가 앵커를 마크다운 링크
    `[label](url)`로 만들므로 그 형식을 먼저 보고, 옛 ` <url>` 마커 형식도 계속 인식한다."""
    md = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text)
    if md:
        return [(lab.strip(' /'), url) for lab, url in md]
    return [(lab.strip(' /'), url) for lab, url in re.findall(r'([^<>]+?)\s*<(https?://[^>]+)>', text)]


class _MdParser(HTMLParser):
    """CMS formattedText(HTML) → 마크다운 문단. <p>는 빈 줄로 구분되는 문단,
    <br>는 공백, <strong>는 **, <a href>는 [text](href). 그 외 태그는 벗기고 텍스트만 남긴다."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.paras, self._buf, self._href = [], [], None

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = dict(attrs).get('href')
            if href:
                self._href = href
                self._buf.append('[')
        elif tag in ('strong', 'b'):
            self._buf.append('**')
        elif tag == 'br':
            self._buf.append(' ')

    def handle_endtag(self, tag):
        if tag == 'a' and self._href:
            self._buf.append(f']({self._href})')
            self._href = None
        elif tag in ('strong', 'b'):
            self._buf.append('**')
        elif tag == 'p':
            self._flush()

    def handle_data(self, data):
        if data:
            self._buf.append(data)

    def _flush(self):
        text = re.sub(r'\s+', ' ', ''.join(self._buf)).strip()
        self._buf = []
        if text:
            self.paras.append(text)


def html_to_md(html):
    p = _MdParser()
    p.feed(html)
    p._flush()  # <p>로 닫히지 않은 꼬리 텍스트도 담는다
    return '\n\n'.join(p.paras).strip()


class _LinkParser(HTMLParser):
    """HTML 안의 <a href> 목록을 (라벨, url) 순서대로 뽑는다."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self._buf, self._href = [], [], None

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self._href = dict(attrs).get('href')
            self._buf = []

    def handle_data(self, data):
        if self._href is not None:
            self._buf.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self._href is not None:
            self.links.append((''.join(self._buf).strip(), self._href))
            self._href = None


def links_from_html(html):
    p = _LinkParser()
    p.feed(html or '')
    return p.links


def youtube_id(url):
    """youtu.be/<ID>?si=…, watch?v=<ID>, /embed/<ID> 모두에서 유튜브 ID를 뽑는다."""
    m = re.search(r'(?:youtu\.be/|[?&]v=|/embed/)([A-Za-z0-9_-]{6,})', url or '')
    return m.group(1) if m else None


def split_csv(text):
    return [t.strip() for t in re.split(r'[,/]', text) if t.strip()]


def blocks_of(raw, chrome):
    w = Walker(); w.feed(raw)
    blocks = [b for b in w.blocks if not (b[0] == 'img' and b[1] in chrome)]
    # .svg는 이 코퍼스 전체(93개 원본)에서 실제 사진이 아니라 갤러리 화살표 등 UI 아이콘에만 쓰인다.
    blocks = [b for b in blocks if not (b[0] == 'img' and b[1].lower().endswith('.svg'))]
    # 마퀴/캐러셀 컴포넌트는 같은 이미지를 무한 스크롤용으로 여러 번 반복 렌더링한다.
    # 페이지 안에서는 이미지가 항상 유일해야 하므로, 같은 URL의 두 번째 이후 등장은 버린다.
    seen, deduped = set(), []
    for b in blocks:
        if b[0] == 'img':
            if b[1] in seen:
                continue
            seen.add(b[1])
        deduped.append(b)
    blocks = deduped
    end = next((i for i, b in enumerate(blocks) if b[0] != 'img' and b[1].startswith(STOP)), len(blocks))
    blocks = blocks[:end]
    # STOP 마커(이메일) 바로 앞에 오는 푸터 서명("Junyoung Kim" 링크)도 함께 잘라낸다.
    while blocks and blocks[-1][0] != 'img' and blocks[-1][1] == 'Junyoung Kim':
        blocks.pop()
    return blocks


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
        val = texts[n + 1][1]
        # 값이 비어 있으면 프레이머는 값 문단 자체를 렌더링하지 않아, 다음에 오는 것은
        # 다른 메타 라벨이거나(라벨 연속) 본문 섹션 제목(라벨 뒤에 '——' 구분선)이 된다.
        empty = val in META or (HEADING.match(val) and n + 2 < len(texts) and RULE.match(texts[n + 2][1]))
        if empty:
            meta[META[texts[n][1]]] = ''
            n += 1
        else:
            meta[META[texts[n][1]]] = val
            n += 2
    body_start = texts[n][0] if n < len(texts) else len(blocks)
    # 메타와 본문 사이에 낀 이미지·임베드(히어로)도 본문 앞에 붙인다
    hero = [b for b in blocks[texts[first][0]:body_start] if b[0] in ('img', 'embed')]
    return {'title': title, 'subtitle': subtitle, 'meta': meta, 'body': hero + blocks[body_start:]}


def render_body(blocks, skip_url=None):
    """블록 → 마크다운 본문, [(원본URL, 파일명)]. skip_url(=cover)과 같은 이미지는 본문에서 뺀다.
    연속된 이미지는 <img sizes>로 읽은 원본 열 수(cols)만큼 한 줄에 묶는다(원본 그리드 복원)."""
    lines, imgs, n, pending, prev_li = [], [], 0, [], False

    def flush_imgs():
        nonlocal pending
        if not pending:
            return
        cols = pending[0][1]
        for i in range(0, len(pending), cols):
            lines.append(' '.join(f'![](./{name})' for name, _ in pending[i:i + cols]) + '\n')
        pending = []

    for kind, text, extra in blocks:
        # 리스트 항목은 줄 끝에 개행이 없어(리스트 안에서는 한 줄바꿈만 필요), 리스트 다음에
        # 바로 다른 블록(특히 이미지)이 오면 빈 줄 없이 이어져 CommonMark가 그 블록을 리스트 항목의
        # lazy continuation으로 읽어버린다. 리스트 다음 비-li 블록 앞엔 빈 줄을 끼워 리스트를 닫는다.
        if kind != 'li' and prev_li:
            lines.append('')
        prev_li = kind == 'li'
        if kind == 'img':
            if text == skip_url:
                continue
            n += 1
            name = f'{n:02d}{Path(text).suffix.lower() or ".jpg"}'
            imgs.append((text, name))
            if pending and pending[0][1] != extra:
                flush_imgs()
            pending.append((name, extra))
            continue
        flush_imgs()
        if kind == 'embed':
            lines.append(f'<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/{text}?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>\n')
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
    flush_imgs()
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


MAX_LONG_EDGE = 2000  # 설계 문서 §6: 레포엔 긴 변 2000px 이하 이미지만


def long_edge(path):
    """sips로 픽셀 크기를 읽어 긴 변을 반환한다."""
    out = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', str(path)],
                          capture_output=True, text=True).stdout
    dims = {}
    for line in out.splitlines():
        k, _, v = line.strip().partition(':')
        if k in ('pixelWidth', 'pixelHeight'):
            dims[k] = int(v.strip())
    return max(dims.get('pixelWidth', 0), dims.get('pixelHeight', 0))


def downscale_if_needed(path):
    """긴 변이 MAX_LONG_EDGE를 넘으면만 sips -Z로 줄인다. sips -Z는 작은 이미지를 큰 쪽으로
    늘리기도 해서(확인함) 무조건 돌리면 안 되고, 넘을 때만 호출해야 한다. svg는 호출하는 쪽에서
    이미 제외된다(코퍼스 전체에서 실제 사진이 아니라 UI 아이콘에만 쓰임 — chrome/svg 필터 참고).
    """
    ext = path.suffix.lower()
    if ext not in ('.jpg', '.jpeg', '.png'):
        return False
    if long_edge(path) <= MAX_LONG_EDGE:
        return False
    if ext in ('.jpg', '.jpeg'):
        subprocess.run(['sips', '-Z', str(MAX_LONG_EDGE), '-s', 'formatOptions', '90', str(path)],
                        capture_output=True)
    else:
        subprocess.run(['sips', '-Z', str(MAX_LONG_EDGE), str(path)], capture_output=True)
    return True


def copy_image(url, dest, dry):
    src = IMPORT / 'images' / Path(url).name
    if not src.exists():
        return f'missing image {src.name}'
    if dry:
        return None
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return 'resized' if downscale_if_needed(dest) else None


def copy_images(pairs, dry):
    """(url, dest) 쌍을 모두 복사하고, missing/resized 요약을 warn 줄 목록으로 돌려준다."""
    warn, resized = [], 0
    for url, dest in pairs:
        w = copy_image(url, dest, dry)
        if w == 'resized':
            resized += 1
        elif w:
            warn.append(w)
    if resized:
        warn.append(f'resized {resized}')
    return warn


def download_image(url, dest, dry):
    """framerusercontent.com 원본 이미지를(쿼리 제거 후) 내려받는다. 같은 파일명이 이미 있으면
    다시 받지 않는다."""
    if dest.exists():
        return None
    if dry:
        return None
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(url.split('?')[0], dest)
    except OSError as e:
        return f'download failed {dest.name}: {e}'
    return 'resized' if downscale_if_needed(dest) else None


def download_images(pairs, dry):
    warn, resized = [], 0
    for url, dest in pairs:
        w = download_image(url, dest, dry)
        if w == 'resized':
            resized += 1
        elif w:
            warn.append(w)
    if resized:
        warn.append(f'resized {resized}')
    return warn


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
        pairs = [(cover, out / f'cover{Path(cover).suffix.lower()}')] + [(u, out / n) for u, n in imgs]
        warn += copy_images(pairs, dry)
        write(out / 'index.md', '---\n' + '\n'.join(fm) + '\n---\n\n' + body, dry)
        print(f'works/{slug:10s} imgs={len(imgs) + 1:2d} body_lines={body.count(chr(10)):3d} {" | ".join(warn)}')


def import_activities(dry):
    """activities는 더 이상 공개 HTML(raw/activities__*.html)을 파싱하지 않는다 — 공개 페이지가
    비어 있던 템플릿 문제 때문에 본문·기간·링크·영상이 담긴 프레이머 CMS(activities.json)에서 바로 읽는다."""
    items = {i['slug']: i for i in json.loads(ACTS_CMS.read_text(encoding='utf-8'))['items']}
    missing = [s for s in ACT_ORDER if s not in items]
    assert not missing, f'activities.json에 없는 slug: {missing}'
    for order, slug in enumerate(ACT_ORDER, 1):
        item = items[slug]
        fd = item['fieldData']
        fv = lambda fid: (fd.get(fid) or {}).get('value')  # noqa: E731

        title, subtitle = fv(ACT_FIELD['title']), fv(ACT_FIELD['subtitle'])
        role, period = fv(ACT_FIELD['role']), fv(ACT_FIELD['period'])
        links = links_from_html(fv(ACT_FIELD['links']) or '')
        cover_url, out, warn, pairs = fv(ACT_FIELD['cover']), ACTS_OUT / slug, [], []

        fm_cover = ''
        if cover_url:
            cover_ext = Path(cover_url.split('?')[0]).suffix.lower()
            pairs.append((cover_url, out / f'cover{cover_ext}'))
            fm_cover = f'cover: ./cover{cover_ext}'

        body = html_to_md(fv(ACT_FIELD['body']) or '')

        names = []
        for fid in ACT_IMAGE_FIELDS:
            url = fv(fid)
            if not url:
                continue
            name = f'{len(names) + 1:02d}{Path(url.split("?")[0]).suffix.lower()}'
            pairs.append((url, out / name))
            names.append(name)
        gallery = '\n\n'.join(' '.join(f'![](./{n})' for n in names[i:i + 3]) for i in range(0, len(names), 3))

        embeds = []
        for fid in ACT_VIDEO_FIELDS:
            vid = youtube_id(fv(fid))
            if vid:
                embeds.append(f'<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/{vid}?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>')

        body_full = '\n\n'.join(part for part in (body, gallery, '\n\n'.join(embeds)) if part).strip() + '\n'

        fm = [f'title: {ys(title)}', f'subtitle: {ys(subtitle)}', f'role: {ys(role)}', f'period: {ys(period)}',
              'links: [' + ', '.join(f'{{ label: {ys(l)}, url: {ys(u)} }}' for l, u in links) + ']']
        if fm_cover:
            fm.append(fm_cover)
        fm += [f'order: {order}', f'draft: {"true" if item.get("draft") else "false"}']

        warn += download_images(pairs, dry)
        write(out / 'index.md', '---\n' + '\n'.join(fm) + '\n---\n\n' + body_full, dry)
        print(f'activities/{slug:10s} imgs={len(pairs):2d} {" | ".join(warn)}')


if __name__ == '__main__':
    dry = '--dry' in sys.argv
    manifest = json.loads((IMPORT / 'manifest.json').read_text(encoding='utf-8'))
    chrome = chrome_images(manifest)
    print(f'chrome images skipped: {len(chrome)}')
    import_works(chrome, dry)
    import_activities(dry)
