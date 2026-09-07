# CLAUDE.md — byjunyoung.github.io

Junyoung Kim 포트폴리오. Astro 정적 사이트, GitHub Pages(main 푸시 → 자동 배포).
설계는 `docs/superpowers/specs/2026-09-04-portfolio-site-design.md`. 결정을 바꾸면 그 문서부터 고친다.

## 콘텐츠가 유일한 소스
- 프로젝트: `src/content/works/{slug}/index.md` + `cover.*` + 본문 이미지 `01.jpg …`
- 활동: `src/content/activities/{slug}/index.md` + `cover.*`
- 활동은 프레이머 CMS 내보내기(~/Documents/Claude/portfolio-import/cms/activities.json)에서 임포트했다. 이후 수정은 md에서 직접.
- 스키마: `src/content.config.ts`. 필드가 틀리면 빌드가 실패한다 — 스키마를 바꾸지 말고 콘텐츠를 고친다.
- `draft: true` 는 빌드에서 빠진다. `order` 가 홈 정렬. `kind` 는 `case-study` | `note`(본문 없이 한 단락).
- 영문: 같은 폴더의 index.en.md (있는 항목만 /en/에 나온다). 이미지·order·cover 등 공유 값은 두 파일이 같아야 한다.
- 글(링크 모음): `src/content/writing/<slug>/index.md` — title·date(YYYY-MM-DD)·source·url·summary. 본문 없음, 원문 링크로만 간다. 영문은 index.en.md(제목·요약만).

## 프로젝트 추가 절차
1. `npm run new:work <slug>` → 템플릿 생성 (draft)
2. `cover.jpg` (긴 변 2000px 이하) 를 폴더에 넣고 frontmatter를 채운다 (cover 가 없으면 스키마의 image() 때문에 draft 여도 빌드가 실패한다 — 1번 직후 `npm test` 는 깨진다)
3. 본문은 마크다운. 섹션 제목은 `## PROBLEM` 처럼 대문자 h2 (관례, 강제 아님)
3-1. 영문 index.en.md 를 같이 만든다(용어·톤은 기존 en 파일을 따른다). 없으면 /en/ 목록에서 빠진다.
4. 영상: `npm run media -- <slug> <원본.mov> [--start 초] [--dur 초]` → `public/media/works/<slug>/loop.mp4`, 출력에 찍힌 `loop:` 줄을 frontmatter에 붙인다
5. `npm test` 통과 → 커밋 → push

## 글 추가 절차
1. 폴더 이름은 날짜-키워드(예: 2026-08-barisbrew-v4)
2. index.md 에 title·date·source·url·summary
3. index.en.md 는 title·summary 만 영어로
4. npm test → push

## 본문 관례
- 이미지 한 줄 = 전폭. 같은 줄에 두 개 = 2열, 세 개 = 3열 그리드 (`![](./02.jpg) ![](./03.jpg)`)
- 그리드(2·3열)는 4:3으로 크롭되므로 사진 전용. UI 화면(16:9·폰 화면) 쌍은 흰 간격을 둔 합성 이미지 한 장으로 만들어 전폭에 넣는다(`ffmpeg hstack`, 간격 80px, 긴 변 2000px).
- 사진(4:3·3:2·세로)은 단독 전폭으로 두지 않는다 — 같은 절의 사진끼리 2·3열로 묶는다. 세로 사진은 미리 4:3으로 크롭한 파일을 새 번호로 만들어 쓰고(잘리는 위치를 고른다), 콜라주는 셀로 나눠 그리드에 넣는다. 전폭 단독은 16:9 이상의 화면·도식·합성 이미지뿐이며, 16:9 짝(도식 둘 등)도 hstack 합성 한 장으로.
- 구조·흐름·상태처럼 시각 자료가 도움이 되는데 쓸 자산이 없으면 **직접 그린다**: SVG를 HTML에 넣고 헤드리스 크롬(scale 2)으로 렌더 → 긴 변 2000px JPG. 흰 배경, Pretendard, 글자 #161616·보조 #6b6b6b·선 #d6d6d2·면 #efefec/#f7f7f5만, 사방 40px 패딩, 한/영 병기(두 페이지가 한 파일을 쓴다). 그림의 모든 사실은 본문·PRD에 있는 것만. SVG 원본은 ~/Documents/Claude/portfolio-import/<slug>-*-diagram.html 에 보관.
- 미디어 블록(이미지·그리드·영상·임베드) 사이에 문장을 끼우지 않는다. 절의 글은 앞에 모으고, 미디어는 뒤에 연달아 둔다(2026-09-07 지시).
- 본문 텍스트 블록은 그리드의 절반 폭(`calc(50% - var(--gap)/2)`)이 상한이다. 픽셀 고정 폭으로 바꾸지 않는다.
- 본문 이미지의 alt 는 현재 전부 비어 있다(장식 취급). 채울 때는 사진에 실제로 보이는 것만 한 줄로 — 지어내지 않는다.
- 본문 영상: `<video src="/media/works/<slug>/02.mp4" autoplay muted loop playsinline></video>`
- 인용: `>` 블록 = 연한 배경 박스
- 링크: 마크다운 `[텍스트](url)`. 본문 링크는 밑줄로 표시된다. 사이트 내부는 `/activities/uxeed` 처럼 경로만.
- 이미지는 반드시 마크다운 문법(`![]()`)으로. `<img>` 를 쓰면 최적화되지 않는다
- 유튜브: `<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/<ID>?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>` — 전폭 16:9

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

## 임포터 (일회성, 파괴적)
- `npm run import:framer` 는 `~/Documents/Claude/portfolio-import/` (레포 밖, framer-export + cms/activities.json) 를 읽어 `src/content/works|activities/*/index.md` 를 **전부 다시 생성**한다. macOS `sips` 에 의존.
- 손으로 고친 md 는 덮어써진다. 특히 frontmatter `loop:` 는 임포터가 만들지 않으므로 다시 돌리면 사라진다. 다시 돌릴 일은 거의 없다 — 돌리기 전에 `git status` 가 깨끗한지 확인하고, 돌린 뒤 diff 를 검토한다.
- 임포터 테스트: `npm run test:import` (python unittest, `tests/test_import.py`). `npm test` 에는 포함되지 않는다.

## 검증
- `npm test` = 빌드 + dist 검증. `npm run test:import` = 임포터 단위 테스트. `npm run check` = 타입.
- 화면 확인은 `npm run dev` 후 크롬 스크린샷. 디자인 변경은 스크린샷을 사용자에게 보여주고 승인 후 push.
- 한/영 둘 다 고쳤는지: git diff --name-only 에 index.md 와 index.en.md 가 짝으로 있는지 본다.
