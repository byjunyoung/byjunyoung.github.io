---
title: "DEUX"
subtitle: "양팔 휴머노이드 로봇의 표정·소리·목소리와 운영 콘솔 DEUX ON"
org: "XYZ Inc."
year: "2026 – 현재"
role: "UX 디자이너"
responsibilities: ["HRI Design", "Expression & Sound", "Product Design", "Front-end"]
keywords: ["humanoid", "hri", "expressive display", "teleoperation", "react"]
link: { label: "DEUX 홈페이지", url: "https://xyzcorp.io/DEUX" }
tags: ["HRI Design", "Expression & Sound", "Product Design", "Front-end"]
kind: case-study
cover: ./cover.jpg
loop: "/media/works/deux/loop.mp4"
order: 0
draft: false
---

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/tqhQTiX0NPw?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## PROBLEM

DEUX는 매장에서 사람 옆에서 일하는 양팔 휴머노이드 로봇입니다. 사람 얼굴이 없습니다. 두 팔 사이의 카메라 두 개가 눈이자 표정 디스플레이입니다. 이 두 눈과 소리, 목소리만으로 지금 무엇을 보고 무엇을 하려는지 전해야 사람이 곁을 내주고 말을 겁니다. 그런데 처음에는 어떤 표정과 소리가 있어야 하는지, 그것들을 어떤 단위로 정의해 로봇에 넣을지가 정해져 있지 않았습니다.

로봇을 세우고 움직이는 쪽에도 문제가 있었습니다. 팔 열네 관절과 손, 주행, 리프트를 제어하는 화면은 개발팀이 만든 개발자용 도구였고, 화면을 정의한 문서 없이 코드가 유일한 정본이었습니다. 현장 운영자와 원격 조종자도 쓰는 제품 화면으로 다시 만들어야 했습니다.


## APPROACH

**인터랙션 어휘부터.** 표정·소리·목소리·제스처를 채널로 나누고, 채널마다 어휘를 하나의 데이터베이스로 정의했습니다. 개발팀이 트리거로 부를 수 있는 이름, 언제 쓰는지, 어떤 파일인지가 한 행에 있습니다. 원칙은 하나였습니다. 감정과 의도는 눈과 목소리가 전하고, 소리는 말로 하기 애매한 시스템·상태 신호에만 쓴다.

**DEUX ON은 문서에서 코드까지.** 화면의 기준선이 될 PRD를 세우고, HTML 프로토타입으로 화면을 잡은 뒤 React로 옮겨 직접 구현했습니다. 백엔드는 제어팀이 맡고, 프런트엔드 저장소는 UX 파트가 관리합니다. 구현에는 AI 코딩 도구를 썼습니다.

로봇의 형태는 로봇디자인팀이, 표정을 로봇에 올리고 시연을 준비하는 일은 로봇지능화팀이, 제어와 백엔드는 로봇자동화팀이 맡았습니다. 저는 그 사이에서 인터랙션의 정의와 운영 화면을 맡았습니다.


## SOLUTION

### 표정

두 눈의 위치·크기·움직임과 색만으로 표정을 만듭니다. 기쁨·웃음·하트·반짝·놀람·두려움·슬픔·화남 같은 감정 표현, 사람을 따라가는 시선 네 방향, 깜빡임과 두리번거림, 부팅·로딩·대기·충전·오류 같은 상태 표정까지 20종을 정의했습니다. 부팅은 눈 표정과 소리, 동작을 한 흐름으로 설계했습니다.

<video src="/media/works/deux/faces.mp4" autoplay muted loop playsinline></video>

### 소리와 목소리

소리는 켜짐·꺼짐·알림 같은 전환 순간의 짧은 신호로만 남기고, 감정은 눈이 맡습니다. 시연에서는 버튼 하나로 표정과 소리가 순서대로 나가도록 매핑 표를 만들었습니다. 목소리는 후보를 같은 문장으로 들어 보고 골랐고, 바리스브루의 차분한 목소리와 구분되도록 밝고 호기심 있는 톤의 페르소나 지시문을 썼습니다. 시연 문장마다 어울리는 표정을 붙였습니다.

### DEUX ON

로봇의 자세·이동·표현을 한 화면에서 다루는 운영 콘솔입니다. 왼쪽에는 운전 상태·연결·배터리·리프트 높이와 시스템 로그, 비상 정지가 늘 보이고, 화면 조작·VR·리더암 세 가지 조작 모드를 위에서 고릅니다. 자세 탭은 양팔 열네 관절과 손을 슬라이더로 움직이고, 컴플라이언스와 자세 프리셋을 두며, 로봇 자세를 2D와 3D로 봅니다. 이동 탭은 조이스틱과 휠 조향, 리프트 높이를, 표현 탭은 표정·소리·음량을 다룹니다.

![](./01.jpg)

![](./02.jpg)


## IMPLEMENTATION

**전달과 적용.** 표정 20종은 GIF와 MP4로 만들어 어휘 데이터베이스와 함께 넘겼고, 로봇 디스플레이에서는 MP4로 재생합니다. 표정·소리 매핑과 시연 음성은 로봇지능화팀이 컨트롤러 버튼에 연결했습니다.

**DEUX ON 구현.** React와 TypeScript로 만들고, 3D 자세 뷰는 로봇의 URDF 모델을 three.js로 그립니다. 인터넷이 없는 로봇 현장 단독망에 배포되도록 설정 파일 하나로 백엔드 주소를 바꾸게 했습니다. PRD의 변경 이력이 곧 화면의 이력이고, 저장소의 변경 기록은 세션 단위로 남깁니다.


## IMPACT

2026년 7월 제품 영상과 8월 로봇 빌딩 솔루션 시연·언론 인터뷰에서 DEUX는 이 표정과 소리, 목소리로 사람을 응대했고, 9월 매장 실도입을 앞두고 있습니다. 개발자 도구였던 제어 화면은 UX 파트가 관리하는 제품 화면이 됐습니다.
