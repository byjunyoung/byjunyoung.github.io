---
title: "fig · pm"
subtitle: "디자인·기획 일을 위한 Claude Code 플러그인"
year: "2026"
stack: "Claude Code 스킬, Figma Plugin API, Python"
status: "공개·사용 중"
links: [{ label: "GitHub", url: "https://github.com/byjunyoung/claude-product-skills" }]
cover: ./cover.png
order: 4
draft: false
---

Claude Code 플러그인은 대부분 코드베이스를 향합니다. fig와 pm은 그 옆의 일을 향합니다. 화면을 그리는 피그마 파일, 그리고 그 옆에 쓰는 기획서입니다.

fig는 화면을 그리기 전후를 맡습니다. 그려야 할 목록을 뽑고, 다 그린 뒤엔 검수하고 맞춥니다. 복제하면서 따라온 설정, 갱신 안 된 원본 페이지, 끊긴 화살표, 아무도 안 그린 화면 같은 것을 잡습니다. pm은 기획서를 쓰고 검증한 뒤 일감으로 쪼개 올리고 맞춥니다.

원칙은 몇 가지로 정했습니다. 옳고 그름은 `/fig:lint` 한 곳에서만 판단합니다. 팀의 관례는 묻지 않고 파일에서 관찰해 뽑고, 확실하지 않으면 값을 비워 둡니다. fig는 피그마에 쓰지 않고, pm은 미리보기와 명시적인 승인 뒤에만 씁니다.

실무에서 하나씩 만든 스킬이라 매일 쓰고 있고, UX 파트원들도 함께 씁니다.

![fig가 한 섹션에서 잡아낸 세 가지 문제](./01.png)

![아무도 안 그린 화면을 자리표시 프레임으로 먼저 채워 둔 모습](./02.png)

![fig와 pm이 서로를 부르지 않고 설정 두 가지만 공유하는 구조](./03.png)

![개발 서버 화면을 기획서와 대조해 쓴 QA 결함 보고서](./04.png)
