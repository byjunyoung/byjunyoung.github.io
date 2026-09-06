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
| 언어 | 한국어만 먼저. 영어는 구조만 비워 둠 | 사용자 결정 |
| 스택 | Astro + 콘텐츠 컬렉션 | 정적 전용, 스키마가 콘텐츠 계약, 이미지 최적화 내장 |
| 폰트 | Pretendard 단일 | Inter 기반이라 현재 인상 유지, 한글 품질, 이력서와 통일 |
| 레포 | byjunyoung/byjunyoung.github.io (public) | 루트 도메인. 이력서 레포 `resume`는 /resume 경로로 그대로 공존 |
| 로컬 | ~/Documents/Claude/byjunyoung.github.io | 다른 Claude 레포와 같은 위치 |
| 배포 | GitHub Actions, main 푸시 시 빌드·배포 | |
| About 페이지 | 만들지 않음 | 홈 한 줄 소개 + 푸터 연락처 + 이력서 링크로 충분 |

## 3. 정보 구조

```
/                     홈 = 한 줄 소개 + Works 2열 그리드
/works/{slug}         프로젝트 상세
/activities           활동 목록
/activities/{slug}    활동 상세
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
- 캔버스는 흰색(#ffffff), 카드·히어로·메타 카드는 밝은 패널(#f7f7f5) + 헤어라인 테두리(#d6d6d2), 카드 하단 띠는 #efefec. 스페셜 프로젝트·TE의 재질감.
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

- 커스텀 도메인 보유 여부 (있으면 CNAME 한 줄)
- 영상 파일 위치 (로컬/드라이브/유튜브)
- (해결 2026-09-06) 활동 5개 본문·기간·링크·사진·영상은 프레이머 CMS 내보내기에서 복원했다.
- 프레이머 사이트를 유지할지, 새 주소로 안내만 남길지 — 2026-09-06 홈 상단에 새 주소 안내 한 줄 추가함(Publish 는 사용자)

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
- 전환 UI: 헤더 오른쪽 KR/EN 분할 배지(이력서 사이트와 같은 스타일: 11px 대문자, 헤어라인, 2px 모서리, 선택은 fg 채움). 같은 페이지의 다른 언어로 이동. 이력서 링크는 언어와 무관하게 `/resume/`.
- 번역 원칙: 사실·수치·고유명사 그대로, 수식어 추가 금지, 이력서 영문판 용어를 따른다(tactile display, Dot Canvas tactile-graphics authoring tool, CES 2024 Innovation Award, BarisBrew robot café, AMR, HRI, PUI). 사람 이름은 원문 표기 유지(한글 이름은 한글, 로마자는 로마자), 괄호 안 역할만 번역. 활동 제목 "설계자들"은 고유명사로 유지, "인턴뷰"는 시리즈 표기 "InternView".
- 검수: 영문 초안 → 로컬 빌드 → 스크린샷·대조표로 사용자 검수 → 수정 → go → push.
