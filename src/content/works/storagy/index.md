---
title: "STORAGY"
subtitle: "실내 배송 로봇의 비언어적 HRI"
org: "XYZ Inc."
year: "2025 – 현재"
role: "UX 디자이너"
responsibilities: ["HRI Design", "LED & Sound Feedback", "Expressive Display"]
keywords: ["hri", "delivery robot", "nonverbal interaction"]
link: { label: "스토리지 홈페이지", url: "https://xyzcorp.io/STORAGY" }
tags: ["HRI Design", "LED & Sound Feedback", "Expressive Display"]
kind: case-study
cover: ./cover.png
loop: "/media/works/storagy/loop.mp4"
order: 3
draft: false
---

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/TPq3F_mAeP8?start=28&rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## PROBLEM

실내 배송 로봇 STORAGY는 복도와 엘리베이터, 사무실을 사람과 같이 씁니다. 지금 대기 중인지, 이동 중인지, 앞에 장애물이 있어 멈춘 건지, 배송이 끝났는지를 말없이 알려야 사람이 길을 내주고 물건을 찾아갑니다. 처음에는 로봇의 상태를 정의한 목록도, 그것을 드러낼 표정과 빛의 규칙도 없었습니다.


## APPROACH

로봇 상태를 먼저 정의하고 채널을 나눴습니다. 로봇이 보고하는 상태는 두 갈래입니다. 부팅·정상·경고·오류와 배터리 같은 시스템 상태, 그리고 대기·주행·도킹과 지금 하는 일 같은 운영 상태입니다. 시스템 상태는 운영자가 어디서든 한눈에 확인해야 하니 몸체 아래 LED와 사운드로, 주행 상태는 로봇 앞에 선 사람이 읽어야 하니 전면 디스플레이의 표정과 사운드로 알리기로 했습니다. 디스플레이와 LED의 피드백 목록을 상태별로 매핑해 정본으로 삼고, 사운드는 그 뒤에 붙였습니다. 정의한 상태를 기준으로 개발팀이 구현하고, 실제 로봇에 올려 보며 고쳤습니다.


## SOLUTION

### 표정

부팅·대기·이동·장애물·충전·배송 완료 여섯 상태의 대표 표정과 애니메이션을 만들었습니다. 눈 두 개의 위치와 크기, 움직임만으로 상태를 구분합니다.

<video src="/media/works/storagy/faces.mp4" autoplay muted loop playsinline></video>

### LED와 디스플레이

전면 디스플레이가 표정을, 몸체 아래 LED가 시스템 상태를 보여 줍니다. 표정은 로봇 앞에 선 사람에게 지금 무엇을 하는지 말하고, LED는 부팅·정상·경고·오류와 충전을 빛의 색과 패턴으로 알립니다. 같은 상태가 두 채널에서 다른 말을 하지 않도록 매핑 표 하나로 관리합니다.

![](./01.jpg) ![](./02.jpg)

<video src="/media/works/storagy/led.mp4" autoplay muted loop playsinline></video>

### 다층 배송

바리스브루가 만든 음료를 STORAGY가 받아 엘리베이터로 층을 옮겨 자리까지 배송합니다. 이 다층 배송의 시나리오와 상태를 정의하고, 로봇을 원격으로 제어하는 운영 콘솔 MobileON의 기능과 화면을 기획했습니다. 엘리베이터를 호출하고, 타고, 목적층을 고르고, 내리는 단계마다 표정을 더했고, 경로가 막혔을 때와 오류·비상정지 표정도 추가했습니다.

<video src="/media/works/storagy/delivery.mp4" autoplay muted loop playsinline></video>


## IMPACT

서울 성수 XYZ 사옥의 로봇 빌딩 솔루션에서 바리스브루와 연동해 층간 배송을 운영 중입니다.


## REFLECTION

**움직이는 로봇의 피드백은 상태를 정의하는 데서 시작하고, 예외를 다루는 데서 계속된다.**

STORAGY는 화면 속 제품이 아니라 복도를 달리는 로봇이었습니다. 상태별 피드백을 정의하려면 로봇이 어떤 순서로 움직이고 어디서 멈추는지, 무엇을 감지하고 무엇은 모르는지를 먼저 이해해야 했습니다. 그래서 일의 절반은 로봇의 동작 방식을 배우는 것이었고, 나머지 절반은 그렇게 정의한 상태와 피드백을 개발팀이 그대로 구현할 수 있는 단위와 포맷으로 옮기는 것이었습니다. 표정·LED·사운드로 채널을 나눈 것도, 상태별 매핑 표를 정본으로 삼은 것도 그 과정에서 나왔습니다.

이상적인 시나리오는 오히려 어렵지 않았습니다. 대기하고, 이동하고, 도착하는 흐름은 표정 여섯 개로 설명됩니다. 어려운 건 그 밖의 상황입니다. 장애물을 만났을 때, 배송한 물건을 아무도 찾아가지 않을 때, 그래서 되돌아와야 할 때 로봇이 무엇을 보여 줘야 하는지는 한 번에 정의되지 않았고, 지금도 현장에서 하나씩 채우고 있습니다. 로봇의 HRI는 출시로 끝나는 설계가 아니라 운영하면서 반복해서 고치는 설계라는 것을 이 프로젝트에서 배웠습니다. 그래서 다시 한다면 무엇을 바꿀지는 아직 답하기 이릅니다.

커리어로 보면, 정지한 기기가 아니라 움직이는 로봇을 다루고, 실내 배송이라는 서비스 시나리오를 통째로 다뤄 봤다는 데 의미가 있습니다.
