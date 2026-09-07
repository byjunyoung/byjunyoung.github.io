---
title: "Dot Pad & Dot Canvas"
subtitle: "촉각 디스플레이와 촉각 그래픽 저작 툴의 UX"
org: "Dot Inc."
year: "2022 – 2025"
role: "UX 디자이너"
responsibilities: ["Hardware UX Design", "UX Research", "Wireframe", "GUI Design"]
with: "김승환 (서비스 기획자), 주백준 (GUI 디자이너)"
keywords: ["tactile display", "braille", "haptic", "tactile graphic", "design tool", "accessibility"]
awards: ["CES 2024 Innovation Award"]
link: { label: "Dot Canvas Web", url: "https://apps.dotincorp.com/" }
tags: ["Hardware UX Design", "UX Research", "Wireframe", "GUI Design"]
kind: case-study
cover: ./cover.jpg
loop: "/media/works/dotcanvas/loop.mp4"
order: 2
draft: false
---

## PROBLEM

시각장애 학생은 그래픽 정보를 눈으로 확인할 수 없어, 점자 교과서의 촉각 그래픽이나 별도의 촉각 교구로 배웁니다. 그런데 이 촉각 자료가 늘 부족합니다. 점자 교과서의 촉각 그래픽은 만들고 관리하기 어렵고, 원본 교과서의 그림을 다 담지 못해 일부만 실립니다. 촉각 교구는 대부분 교사가 직접 만듭니다. 맹학교 수업을 참관하면 테이프와 스티커를 붙여 만든 그림 자료가 나옵니다. 시간과 비용이 많이 들고, 내구성이 약해 유지 관리도 어렵습니다.

이 제약은 학생의 학습 기회를 좁히고 교사에게 부담을 지웁니다. 촉각 자료를 만드는 다른 방법이 필요했습니다.

![촉각 그래픽 학습 자료와 분자 모형을 손으로 만지는 학생](./01.png) ![닷패드 위에 색색의 블록을 놓고 촉각 그래픽을 만지는 손](./02.jpg) ![촉각 그래픽이 올라온 닷패드 실물과 그 옆에 놓인 손](./03.jpg)


## APPROACH

2022년 7월 닷에 하드웨어 UX 디자이너로 합류했지만, 첫 일은 하드웨어가 아니었습니다. 촉각 디스플레이 닷패드는 올릴 촉각 그래픽이 있어야 쓸모가 있는데, 그것을 만드는 도구가 없었습니다. 서비스 기획자, GUI 디자이너와 한 팀으로 3개월 안에 저작 도구 닷 캔버스의 웹과 앱 데모를 내는 것이 목표였습니다.

**사용자가 둘.** 촉각 그래픽은 만드는 사람과 만지는 사람이 다릅니다. 웹은 교사가 자료를 만들고 관리하는 쪽에, 앱은 시각장애 사용자가 직접 그리고 만지는 쪽에 맞췄습니다. 국내에서는 특수학교 교사와 시각장애 학생을 대상으로 필드 스터디를, 해외 사용자는 설문과 다이어리 스터디로 사용 환경과 페인포인트를 조사했습니다. 이 데이터가 초기 캔버스 버전의 문제를 짚고 개선 방향을 정하는 근거가 됐습니다.

**그다음 하드웨어.** 캔버스를 내보낸 뒤에는 닷패드 자체로 갔습니다. 점자 디바이스 20종 이상을 비교해 촉각 표기 방식과 차기 모델의 스펙·요구사항을 정의하고, 키 기능과 햅틱·LED 피드백을 설계해 양산 모델에 반영했습니다.

![닷패드와 아이패드, 노트북에서 닷 캔버스를 함께 쓰는 제품 구성](./04.jpg)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/N_L3hR81nik?rel=0&modestbranding=1" title="닷 캔버스 소개 영상" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## SOLUTION

### Dot Canvas 웹

교사가 브라우저에서 촉각 그래픽을 그리거나 PDF·이미지를 불러와 변환합니다. 만든 자료는 닷 클라우드에 저장되고 공용 드라이브로 다른 교사와 나눕니다. 수업에서는 닷패드 최대 10대에 같은 그래픽을 동시에 띄워, 학생들이 같은 그림을 만지며 이야기할 수 있습니다.

![닷 캔버스 웹 편집 화면. 왼쪽 도구 막대, 가운데 격자 캔버스, 오른쪽 페이지 설명 칸](./09.jpg)

### Dot Canvas 앱

아이패드의 터치와 애플 펜슬로 그립니다. 보이스오버와 라이브 드로잉을 지원해 시각장애 사용자도 직접 그리고, 그린 것을 바로 닷패드로 만져 봅니다. 파일은 닷 클라우드로 웹과 공유됩니다.

![아이패드에서 연 닷 캔버스 앱의 편집 화면](./10.jpg)

### Dot Pad

닷패드는 그래픽을 띄우는 여러 줄 촉각 영역과 그 아래 한 줄 점자 영역, 그리고 물리 키로 이뤄져 있습니다. 시각장애 사용자는 키를 보고 고를 수 없습니다. 같은 키는 언제나 같은 일을 해야 하고, 손끝으로 구분돼야 합니다. 그래서 키 기능을 일관되게 정의하고 물리적 표기를 더했으며, 입력이 들어갔는지와 기기의 상태를 알리는 햅틱·LED 피드백을 설계해 양산 모델에 적용했습니다. 점자 디바이스 20종 이상의 비교 분석으로 촉각 표기 방식을 정하고 차기 모델의 스펙·요구사항을 정의했으며, 사용자 평가로 차기 모델에 반영할 피드백을 모았습니다.

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/iSmRM2PUBzA?rel=0&modestbranding=1" title="닷패드 소개 영상" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## IMPLEMENTATION

**화면 설계와 GUI.** 리서치 결과를 바탕으로 닷 캔버스 웹과 앱의 화면을 Figma로 설계하고 GUI를 디자인했습니다. 교사와 시각장애 학생이 함께 쓰는 인터페이스라, UI 구조와 기능 배치를 그 둘에 맞춰 정리했습니다.

**문서와 협업.** 화면 설계서와 기능 명세서를 문서화하고 JIRA로 이슈를 관리했습니다. 개발팀과 기술적 변경을 맞추며 기능 개선과 출시 일정을 조율했습니다.

![화이트보드에 화면 설계 출력물을 붙여 흐름을 이어 놓은 작업 벽](./05.jpg)

![전시장에서 노트북과 닷패드를 놓고 시연을 준비하는 팀](./06.jpeg) ![교실에서 학생들이 책상마다 닷패드를 놓고 수업하는 모습](./07.jpeg)

![해외 사용자 워크숍. 참가자들이 노트북으로 닷 캔버스를 사용하는 모습](./08.jpeg) ![교실 모니터에 띄운 닷 캔버스 화면과 그 안의 촉각 그래픽](./13.jpeg)


## IMPACT

닷 캔버스는 CES 2024 Innovation Award를 받고 CSUN 2024에 출품했습니다. 닷패드의 촉각 인터페이스는 양산 모델에 들어갔습니다. 2024년 참관한 맹학교 과학 수업에서는 테이프와 스티커로 만들던 그림 자료가 닷패드로 대체돼 있었습니다.

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/AHK3VnjvA5Y?rel=0&modestbranding=1" title="CES 2024에서 소개된 닷 캔버스 영상" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

![CSUN 2024 부스에서 방문자가 닷패드의 촉각 그래픽을 만져 보는 모습](./15.jpg) ![전시 준비 중인 닷 부스](./14.jpeg)


## REFLECTION

**빠른 실행의 대가는 나중에 유지보수로 돌아온다.**

닷 캔버스는 짧은 기간 안에 웹과 앱의 데모를 내야 하는 프로젝트였습니다. 팀에 관련 경험이 있는 사람이 부족했고, 3개월 안에 쓸 수 있는 결과물을 만들어야 했습니다. 화이트보드를 채워 가며 빠르게 프로토타입을 만들었고, UX 설계뿐 아니라 개발팀과의 협업과 일정 관리까지 함께 다뤘습니다.

빠른 실행의 대가도 분명했습니다. 단기 목표는 달성했지만 확장성을 고려하지 못한 설계 탓에 이후 유지보수에서 수정이 많았고, 완성도가 부족한 부분도 있었습니다. 사용자 스터디로 직접 피드백을 받으면서 속도와 완성도 사이의 균형이 UX 설계에서 얼마나 중요한지 확인했습니다.

가장 많이 배운 것은 사용자였습니다. 시각장애인 사용자를 가까이에서 만나며, 접근성은 제품의 마지막 단계에서 덧붙이는 것이 아니라 UX의 첫 챕터에서부터 다뤄야 한다는 것을 배웠습니다.
