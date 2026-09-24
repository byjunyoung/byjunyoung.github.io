# 포트폴리오 사이트 재구축 — 설계

작성 2026-09-04. 프레이머(byjunyoung.framer.website)를 떠나 GitHub Pages에 새로 만든다.
결정은 이 문서, 과정은 세션 기록에 남긴다.

## 1. 배경과 목표

- 현재: 프레이머 무료 플랜, 서브도메인·배지 노출, 플랫폼 귀속. 2026-05에 이미 이탈을 고민했다.
- 목표: 채용 담당자(하드웨어 UX, 글로벌 트랙 포함)가 보는 포트폴리오를 GitHub에 배포하고, 프로젝트 추가·수정을 AI(Claude Code)로 관리한다.
- 원칙: 문구는 담백하고 사실만. 제공하지 않은 사실을 만들거나 부풀리지 않는다 (2026-05 세션에서 정한 기준).

## 2. 확정 사항

| 항목 | 결정 | 이유 |
|---|---|---|
| 디자인 | 전부 새로 설계 | 사용자 결정 |
| 진행 방식 | 레퍼런스 정하고 코드로 직행 (와이어 단계 없음) | 사용자 결정 |
| 1차 레퍼런스 | Special Projects (specialprojects.studio) | 사용자가 프레이머 포폴을 만들 때 참고한 원본. 2열 그리드, 제목·소속·한 줄, 상세는 좌 서술 + 우 메타 카드, 곳곳이 무음 루프 영상 |
| 2차 레퍼런스 | Studio Simo Lahtinen (simolahtinen.com) 톤 / teenage.engineering 요소 | 차분한 제품 사진 그리드 / 연회색 바탕 제품 단독 컷, 치수까지 적는 스펙 리스트, 손으로 조작하는 영상 |
| 제외 | Rino Claessens(디자인 중심), 볼드 타이포·다크 계열 | 사용자 강점이 순수 디자인이 아님 |
| 강조점 | 인터랙티브 하드웨어 케이스 → 카드·본문의 루프 영상 | 영상은 대부분 프로젝트에 보유 |
| 언어 | 한국어만 먼저 → 2026-09-06 영어 추가(§11, /en/ 접두, index.en.md) | 사용자 결정 |
| 스택 | Astro + 콘텐츠 컬렉션 | 정적 전용, 스키마가 콘텐츠 계약, 이미지 최적화 내장 |
| 폰트 | Pretendard 단일 | Inter 기반이라 현재 인상 유지, 한글 품질, 이력서와 통일 |
| 레포 | byjunyoung/byjunyoung.github.io (public) | 루트 도메인. 이력서 레포 `resume`는 /resume 경로로 그대로 공존 |
| 로컬 | ~/Documents/Claude/byjunyoung.github.io | 다른 Claude 레포와 같은 위치 |
| 배포 | GitHub Actions, main 푸시 시 빌드·배포 | |
| About 페이지 | 2026-09-09 추가 (§12). 내비에 넣지 않고 헤더 워드마크로만 진입 | 처음엔 "만들지 않음"이었으나, 어떻게 일하고 자라 왔는지 보일 자리가 필요해 사용자가 추가 결정 |

## 3. 정보 구조

```
/                     홈 = 한 줄 소개 + Works 2열 그리드
/work/{slug}          프로젝트 상세
/activity             활동 목록 — 커뮤니티·발표·강의 (§14)
/activity/{slug}      활동 상세
/play                 사이드 프로젝트 목록 (§14)
/play/{slug}          사이드 프로젝트 상세
/about                소개 — 워드마크 링크로만 (§12)
푸터                  이메일 · LinkedIn · Instagram · 이력서(https://byjunyoung.github.io/resume/)
```

현재 콘텐츠 인벤토리 (공개 사이트 기준, 2026-09-04):

- works 8: birdy, meemo, zibot, dotcanvas, adio, barisbrew, storagy, dotpad
  - 본문 있음: birdy, meemo, zibot, dotcanvas, adio
  - note만 있음: barisbrew, storagy, dotpad
- activities 5: hux(설계자들), uxeed, dino, svip, internview
  - 공개 사이트에서 본문 있음: hux, svip. 나머지 3개는 비어 있음 (프레이머에서 초안인지 확인 필요)
- 이미지 93장 (원본 URL 기준 중복 제거), 영상 0

## 4. 화면 구조

### 홈
- 상단: 이름(좌) / works · activities · resume(우). 현재와 동일한 최소 내비.
- 한 줄 소개 (현재 문구 유지, 수정은 별도 판단).
- Works 그리드: 2열. 카드 = 미디어(루프 영상, 없으면 사진) / 제목 / 소속 · 연도 / 한 줄 설명 / 분야 태그 / `Case study` 또는 `Note` 뱃지.
- 뱃지의 목적: 본문 없는 3개를 본문 있는 것과 같은 무게로 보이지 않게 정직하게 구분.

### 프로젝트 상세
1. 히어로: 전폭 미디어 (영상 있으면 영상, 아니면 cover).
2. 2열: 좌 서술(마크다운 본문), 우 메타 카드 (연한 바탕).
   - 메타 필드: ORGANIZATION · YEAR · ROLE · RESPONSIBILITIES · WITH · KEYWORDS · LINK. 선택: PRESS · AWARDS.
3. 본문 안에 전폭 미디어·2-up 미디어·인용 박스가 섞임.
4. 하단: 다음 프로젝트 링크.
- 본문 헤딩(PROBLEM / APPROACH / IMPLEMENTATION / IMPACT / REFLECTION)은 강제가 아니라 관례. note만 있는 항목은 Note 한 단락.

### 활동
- 목록: 이름 / 한 줄 / 역할 / 기간. 상세는 프로젝트와 같은 레이아웃의 축소판.

### 스타일 방향 (2026-09-05 개정 — 1차 검수에서 "프레이머와 너무 비슷하다"는 피드백 반영)
- 캔버스는 흰색(#ffffff). 카드·히어로·메타 표·본문 이미지·임베드·인용은 모두 흰 바탕에 헤어라인 테두리(#d6d6d2)만 — 회색 패널·줄무늬 없음(2026-09-06, 사용자 요청). 카드 미디어는 16:9(루프 영상이 잘리지 않게, 활동 카드도 동일). 스페셜 프로젝트·TE의 재질감.
- 헤더는 가운데 워드마크(자간 넓은 대문자) 아래 작은 대문자 메뉴. 프레이머식 좌우 배치를 버림.
- 카드는 패널 안 색 띠에 제목·소속·연도·한 줄, 우상단에 01~08 인덱스(카탈로그 느낌), 하단에 뱃지·태그.
- 상세: 메타 카드는 오른쪽 플로트 표 형태(행마다 줄), 본문 첫 문단이 그 옆에서 시작. 섹션 제목은 굵은 소제목 + 28px 밑줄.
- 텍스트는 near-black, 타이포는 작고 조용하게. 색은 미디어가 낸다. 모션은 루프 영상뿐.

## 5. 콘텐츠 모델

```
src/content/works/{slug}/
├─ index.md      frontmatter + 본문
├─ cover.jpg     카드·히어로 정지 이미지 (필수)
└─ 01.jpg …      본문 이미지, 상대경로로 참조
src/content/activities/{slug}/index.md + cover.*
public/media/works/{slug}/loop.mp4   영상 (Astro가 src/content의 비이미지 파일은 서빙하지 않아 public에 둔다)
src/content.config.ts   스키마 (zod)
```

works frontmatter:

| 필드 | 타입 | 필수 | 비고 |
|---|---|---|---|
| title | string | ✓ | |
| subtitle | string | ✓ | 한 줄 설명 |
| org | string | ✓ | |
| year | string | ✓ | "2021 (1y)" 같은 표기 그대로 |
| role | string | ✓ | |
| responsibilities | string[] | ✓ | |
| with | string | | 협업자 |
| keywords | string[] | | |
| link | {label, url} | | |
| tags | string[] | ✓ | 분야 태그 (카드 표시) |
| kind | 'case-study' \| 'note' | ✓ | 뱃지 |
| cover | image | ✓ | |
| loop | string | | `/media/works/{slug}/loop.mp4` 절대경로 |
| order | number | ✓ | 홈 정렬 |
| draft | boolean | | true면 빌드 제외 |
| press, awards | string[] | | 선택 |

activities frontmatter: title, subtitle, role, period, links[], cover, order, draft.

영어 대비: 필드 구조는 그대로 두고, 나중에 `src/content/works-en/` 같은 병렬 컬렉션 또는 locale 필드로 확장. 지금은 만들지 않는다.

## 6. 미디어 규칙

- 이미지: 레포엔 긴 변 2000px 이하 jpg/webp만. 원본은 레포 밖(`~/Documents/Claude/portfolio-import/`)에 보관.
- 영상: ffmpeg로 무음 H.264 mp4, 8초 이내 루프, 파일당 3MB 목표. 포스터는 cover 이미지를 쓴다. 카드는 `autoplay muted loop playsinline`. 위치는 `public/media/works/{slug}/`.
- 한도 근거: GitHub Pages 저장소·사이트 권장 1GB, 월 100GB 대역폭(soft), 시간당 10빌드(soft). 프로젝트당 영상 총량 20MB 이내를 가이드로 둔다.
- Git LFS는 쓰지 않는다 (Pages가 LFS 파일을 서빙하지 않음).

## 7. AI 친화 관리

- 레포 `CLAUDE.md`: 프로젝트 추가 절차, 스키마 요약, 미디어 규칙, 문구 톤 원칙, 하지 말 것.
- 스크립트: `npm run new:work <slug>` (템플릿 생성), `npm run media <slug>` (ffmpeg 변환·포스터 추출).
- 스키마 위반은 빌드 실패 → 잘못된 콘텐츠가 배포되지 않는다.
- 문서: docs/ 아래에 이 설계와 실행 계획. 결정 변경은 이 문서를 고친다.

## 8. 단계 계획과 완료 조건

| 단계 | 내용 | 완료 조건 |
|---|---|---|
| 1 | 추출 마무리 | works 8 + activities 5 마크다운, 이미지 매핑표. 프레이머 MCP는 플러그인이 켜지면 필드·초안 대조 |
| 2 | 레포 스캐폴드 | 빈 Astro 사이트가 https://byjunyoung.github.io/ 에 뜸 (GitHub 레포 생성·푸시는 미리보기 → go) |
| 3 | 콘텐츠 이관 | 13페이지 모두 렌더, 스키마 통과 |
| 4 | 디자인 구현 | 홈·상세 스크린샷을 레퍼런스와 나란히 검토해 승인 |
| 5 | 영상 수집·변환 | 카드에서 루프 재생. 영상 위치는 이 단계에서 확인 |
| 6 | 마무리 | 프레이머 사이트 처리 결정, 메모리 기록 |

## 9. 미결 (TBD)

- (해결 2026-09-06) 커스텀 도메인 없이 byjunyoung.github.io 그대로 쓴다 (사용자 결정)
- 영상 파일 위치 (로컬/드라이브/유튜브)
- (해결 2026-09-06) 활동 5개 본문·기간·링크·사진·영상은 프레이머 CMS 내보내기에서 복원했다.
- 프레이머 사이트를 유지할지, 새 주소로 안내만 남길지 — 2026-09-06 홈 상단에 새 주소 안내 한 줄 추가함(Publish 는 사용자)
- (해결 2026-09-06) 언어: §11

## 10. 환경 사실

- node v25.8.1, npm 11.11.0, git 2.50.1, ffmpeg 8.0.1, gh 로그인 byjunyoung
- 추출물: ~/Documents/Claude/portfolio-import/framer-export (pages/*.md, images/ 93장, manifest.json, raw/*.html)
- 레퍼런스 스크린샷: ~/Documents/Claude/portfolio-import/reference-screenshots

## 11. 언어 (2026-09-06 추가)

- 목적: 한국어·영어 두 언어로 같은 사이트를 낸다. 영문은 프레이머 로케일을 쓰지 않고 한글 콘텐츠를 직접 자연스럽게 번역한다.
- 주소: 한국어는 루트(`/works/birdy/`), 영어는 `/en/` 접두(`/en/works/birdy/`). 페이지마다 `<link rel="alternate" hreflang>`로 서로를 가리키고 `x-default`는 한국어. 사이트맵에 두 언어 모두.
- 콘텐츠 모델: 폴더마다 `index.md`(ko) + `index.en.md`(en). 이미지·영상·`order`·`cover`·`kind`·`tags`·`link`·`links`·`period`·`year`·`org`는 두 파일에 같은 값. 스키마는 하나. 컬렉션 id는 ko `birdy`, en `en/birdy`.
- 영문 파일이 없는 항목은 `/en/`에서 빠진다(목록·상세 모두). 그 항목의 한국어 페이지는 hreflang 없이 토글만 영문 홈으로 보낸다.
- 페이지: 홈·활동 목록·프로젝트 상세·활동 상세 본문은 `src/components/pages/`의 컴포넌트가 `lang`을 받아 렌더하고, `src/pages/`와 `src/pages/en/`에는 얇은 래퍼만 둔다.
- UI 문구(메뉴·메타 라벨·배지·소개문)는 이미 영어라 언어별로 나누지 않는다. `<html lang>`만 언어별. 404는 두 언어 한 줄씩.
- 자동 전환(2026-09-24 추가): 첫 방문은 브라우저 언어(`navigator.languages[0]`가 ko*면 KR, 아니면 EN)로 정해 같은 페이지의 짝으로 `location.replace`. 국가(IP)가 아니라 브라우저 언어 — GitHub Pages엔 서버가 없고, 해외의 한국인·국내의 외국인에게 더 맞다. 배지를 누르면 그 선택을 `localStorage['site-lang']`에 저장하고 이후엔 자동 판정을 하지 않는다. 키는 이력서 사이트(`/resume/`, 같은 도메인)와 공유해 한쪽에서 고르면 다른 쪽도 따라간다. 봇(UA에 bot·crawl·spider)은 제외 — 색인은 hreflang이 담당. 영어 짝이 없는 페이지는 이동하지 않는다. 헤드 맨 앞 인라인 스크립트(`Base.astro`), 이동 시 `window.__langRedirect`를 세워 분석 스니펫이 이동 전 페이지를 세지 않게 한다.
- 전환 UI: 헤더 오른쪽 KR/EN 분할 배지(이력서 사이트와 같은 스타일: 11px 대문자, 헤어라인, 2px 모서리, 선택은 fg 채움). 같은 페이지의 다른 언어로 이동. 이력서 링크는 언어와 무관하게 `/resume/`.
- 번역 원칙: 사실·수치·고유명사 그대로, 수식어 추가 금지, 이력서 영문판 용어를 따른다(tactile display, Dot Canvas tactile-graphics authoring tool, CES 2024 Innovation Award, BarisBrew robot café, AMR, HRI, PUI). 사람 이름은 원문 표기 유지(한글 이름은 한글, 로마자는 로마자), 괄호 안 역할만 번역. 활동 제목 "설계자들"은 고유명사로 유지, "인턴뷰"는 시리즈 표기 "InternView".
- 검수: 영문 초안 → 로컬 빌드 → 스크린샷·대조표로 사용자 검수 → 수정 → go → push.

## 12. About 페이지 (2026-09-09 추가, 2026-09-10 개정)

- 진입: 헤더 워드마크(JUNYOUNG KIM)만. 내비 항목·푸터 링크 없음. 한/영 `/about/`·`/en/about/`.
- 머리: 이름과 소개 두 줄. 사진 없음 — 초상 사진·일러스트 변환 모두 기각(2026-09-09).
- 절 네 개, 이야기 순: 두 번의 탐색(어떻게 왔나) / 하드웨어 UX(생각이 어떻게 바뀌었나, 끝에 2025 발표의 "UX는 관점이자 태도"와 발표 자료 링크) / 만들고 싶은 것(그래서 앞으로) / 그 밖에. 지향을 먼저 꺼내면 근거 없이 들리고 시간이 되감겨, 2026-09-13 이 순서로 바꾸고 "지금의 기준"은 하드웨어 UX에 합쳤다. 절마다 16:9 사진 전폭, 글은 그리드 절반 폭. 활자는 기존 스케일만(큰 글씨 강조 없음). 페이지 라벨은 다른 목록처럼 영문 고정.
- 글의 출처는 본인 글(2018 블로그, 링크드인, 설계자들 북스터디 기록장, 원티드 발표)과 케이스 본문뿐. 해석 문장을 지어 붙이지 않는다. 말투는 다른 페이지보다 캐주얼해도 된다.
- 03 타임라인: 마디 16개, CSS 라디오(JS 없음). 왼쪽 목록은 x 오프셋으로 제 길/헤맨 길을 보이고(채운 점=일어난 일, 점선 점=그때 남긴 의심), 오른쪽 패널에 그 시기 케이스 루프 영상 또는 사진 + 이야기 + 케이스·활동·글 링크. 패널 마크업은 목록 안 각 마디 뒤에 두고, 데스크톱은 그리드 2열로 오른쪽에 고정(sticky), 720px 이하는 누른 마디 바로 아래 펼쳐진다. 영상은 케이스 루프 재사용, 사진은 활동·케이스 폴더와 본인 블로그 원본만(2026-09-10). 자산 없는 마디는 글만 둔다.
- 외부 사진은 라이선스와 저작자를 표기한다(02 Braun T1000CD, CC BY-SA 2.0).

## 13. Blog 페이지 (2026-09-20 Resources로 추가, 같은 날 Writing과 합쳐 Blog로 개정)

- 목적: 하드웨어 UX가 뭔지 설명할 자료가 마땅치 않아 2018년부터 스스로 모아온 책·논문·아티클 목록(원본: 개인 노션 페이지)을 아카이브. 처음엔 WRITING과 나란한 별도 최상위 섹션(`resources`)으로 냈으나, nav가 5개(works/activities/writing/resources/resume)로 늘어난 게 과하다는 지적에 **Writing과 한 페이지로 합쳤다** — 성격은 다르지만(하나는 직접 쓴 글, 하나는 읽은 자료) 굳이 최상위 자리를 따로 줄 정도는 아니라고 판단.
- 진입: 내비 `works / activities / blog / resume` (4개, writing·resources 항목은 blog로 흡수). `/blog/`, `/en/blog/`. 이전 `/writing/`·`/resources/` 라우트는 삭제(내부 링크 없어 안전).
- 페이지 구조: `src/components/pages/Blog.astro` 하나 — 상단 `BLOG` 라벨 아래 CSS 라디오 탭 2개(**Posts** 기본 / **HW UX**, JS 없음, About 타임라인과 같은 라디오 트릭). 탭 버튼은 헤더 KR/EN 배지와 같은 필박스 스타일(선택 시 `fg` 채움) — 새 시각 언어를 만들지 않고 기존 토글 패턴 재사용.
  - **Posts 탭**: 옛 WRITING 그대로 — title·date·source·url·summary, 커버 있으면 16:9 썸네일, 없으면 검정 타이틀카드.
  - **HW UX 탭**: 옛 Resources 그대로 — 소개글(2018년부터 모음, 2022년 북스터디) → 카테고리(Books/Papers/Articles/Blogs/Others) 헤더 + 제목·링크. "너무 시각 이미지가 없다"는 지적에 Books에만 실제 표지(48×72 세로 썸네일)를 붙였다. 표지는 각 항목이 실제로 링크한 판매 페이지의 og:image(구글북스·알라딘·yes24)를 우선 쓰고, 없으면 아마존 링크 ASIN을 ISBN 삼아 Open Library Covers API로 받았다. 14권 중 11권 확보, 3권(Designing Smart Objects in Everyday Life·The Revenge of Analog·Maker Pro)은 tint 배경 빈 박스. 이미지는 `src/assets/resources/`에 로컬 저장 후 정적 import(핫링크 안 함).
- 콘텐츠 모델은 컬렉션 두 개 그대로 유지: `src/content/writing/<slug>/index.md`(폴더당 한 개), `src/content/resources.yaml`(데이터 파일 하나, `{ id·category(Books/Papers/Articles/Blogs/Others)·title·url·order }`, astro `file()` 로더). 탭 UI만 한 페이지로 묶었을 뿐 컬렉션은 합치지 않았다.
- 원본 노션의 "Job Positions & Descriptions"(타사 채용공고 스크랩 425건)는 성격이 다르고 공개 부적절해 전부 제외. Videos 3개는 노션 북마크 임베드라 원본 URL을 못 읽어 제외. 링크 46개 중 `usecon.com`의 아티클 1건은 404 확인돼 제외(45개 게재). 나머지 403 응답은 대부분 봇 차단(Medium, ACM, Fast Company 등)이라 살아있는 것으로 간주.
- 탭 이름 "HW UX"는 사용자 본인의 2022년 링크드인 글 제목("HW UX가 궁금하신 분들께…")을 그대로 따랐다 — 새로 짓지 않고 기존 표현 재사용.
- nav가 5개였을 때 모바일에서 마지막 항목이 잘려 `.nav nav`에 `@media (max-width: 480px)` 줄바꿈을 추가했다(포트폴리오·이력서 둘 다). Blog로 합쳐 4개로 줄었지만 줄바꿈 규칙은 방어적으로 유지.
- 이력서 사이트 헤더(`~/Documents/커리어/웹이력서/index.html` `.site-nav`)의 Writing 링크도 Blog로 교체해 동기화(5-1 규칙).

## 14. Playground 섹션 + 활동 범위 확장 (2026-09-24 추가)

- **Playground**: 회사·학교 밖에서 재미로 만드는 사이드 프로젝트 모음. Works(제품 일)와 성격이 달라 따로 둔다. 사용자가 "메뉴에 추가"를 골랐다 — 내비는 다시 5개 `works / playground / activities / blog / resume`(직접 만든 것끼리 이어지게 works 바로 뒤). §13의 480px 줄바꿈 규칙이 5개에서도 받친다. 이력서 사이트 헤더도 같이 고친다(5-1).
- 형식: 활동과 같은 **16:9 카드 그리드 + 상세 페이지**(사용자 선택). `/playground/`, `/playground/{slug}`, `/en/…` 동일.
- 콘텐츠: `src/content/playground/<slug>/index.md`(+`index.en.md`). 필드는 활동을 따르되 기간 대신 `year`, 역할 대신 `stack`, 진행 단계 `status`, `links`, `cover`(선택), `order`, `draft`.
- 커버가 없는 항목은 Blog Posts와 같은 **검정 제목 카드**로 채운다(빈 tint 카드는 2026-09-06에 기각됨).
- 항목 선정(사용자): 웹앱(weekly-fc), AI 도구(claude-product-skills·clawd-statusline·design-core), 하드웨어 프로토(textrip). youtube-highlight는 제외. **구체화 전 단계(컨셉만 있는 pet-rock)와 보관한 프로젝트(tactics-board)는 넣지 않는다**(2026-09-24 사용자 지시).
- 커버는 프로젝트를 가장 잘 대표하는 장면으로 고른다 — 하드웨어는 손에 쥐고 동작하는 실물(textrip은 사진 앱의 시제품 영상에서 뽑은 8초 루프를 카드·상세 맨 위에 재생 — Works와 같은 `loop` 필드, 정지 커버는 포스터로만), 도구는 실제로 하는 일이 보이는 화면(fig·pm은 화살표 전/후 도식), 로고·소개 이미지는 피한다.
- 비공개 레포(textrip)는 GitHub 링크 없이 설명만. 본문은 각 레포 README·기획서에 적힌 사실만 쓰고 동기·수치를 지어내지 않는다.
- 공개 금지: weekly-fc 화면의 팀원 실명(캡처 시 가명으로 바꿔 찍음)·계좌번호·구장명, 회사명이 섞인 예시 화면.

- **Activities 범위 확장**: 커뮤니티·인턴십에 더해 **발표·강의·심사**도 활동으로 둔다. 원티드 온라인 UX 컨퍼런스 발표(2025-07-09), 한성과학고 특강 두 번(2024-09-09 닷 소속 접근성 특강·닷패드 체험, 2025-10-25 영재교육원 진로 특강 — 한 활동으로 합침), 홍익대 디자인엔지니어링 HRI 수업 심사·융합전공 설명회(2026-06-19). 같은 글의 Blog 링크는 그대로 두고 활동 상세에서 링크로 잇는다(About 타임라인이 원티드 글을 참조).
- 활동 사진은 사진 앱 원본에서 가져오되 EXIF·GPS를 지우고, 학생·청중 얼굴과 이름표가 보이는 컷은 쓰지 않는다. 학생 후기 원문은 옮기지 않는다.

## 15. 메뉴 이름·주소 통일 (2026-09-24)

- 메뉴가 복수(works·activities)와 단수(playground·blog·resume)로 섞여 있다는 지적. 사용자 기준은 "짧은 단어", RESUME은 유지(CV 기각), activities 자리는 "액티비티 같은 느낌"을 원해 단수 **ACTIVITY**(링크드인·GitHub의 Activity 탭 용법)로 확정. TALK·SHARE·EXTRA·ACT·PEOPLE은 기각.
- 최종 내비: `work / activity / play / blog / resume` — activity를 work 옆에 둔다(사용자 지시). 페이지 라벨·탭 제목·돌아가기 링크도 같은 이름.
- 주소도 이름에 맞춰 `/work/{slug}`, `/activity/…`, `/play/…`(영문 `/en/…` 동일). 옛 주소는 `astro.config.mjs` `redirects`로 새 주소로 넘긴다(meta refresh + noindex, 사이트맵에서 제외). 홈 `/`는 그대로 WORK.
- 콘텐츠 컬렉션·폴더 이름(`works`·`activities`·`playground`)과 미디어 경로는 페이지 주소가 아니라서 바꾸지 않았다.
- 이력서 사이트 헤더도 같은 이름·주소로 맞춤(5-1).
