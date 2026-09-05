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
- 유튜브: `<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/<ID>?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allowfullscreen></iframe></div>` — 전폭 16:9

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
