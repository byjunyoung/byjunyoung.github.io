---
title: "Birdy"
subtitle: "노년층 가족 소통을 위한 종이 기반 메시징 디바이스"
org: "UNIST"
year: "2021 (1y)"
role: "리드 연구원"
responsibilities: ["Research", "Product Design", "Prototyping", "Project Management"]
with: "김나눔, 윤혜정 (보조 연구원)"
keywords: ["digital divide", "assistive technology", "inclusive design", "IoT"]
link: { label: "Master's Thesis", url: "https://drive.google.com/file/d/1Ys_DDoIZfHbj7Bq9uYravbCF2H8DK-5J/view?usp=sharing" }
tags: ["Research", "Product Design", "Prototyping", "Project Management"]
kind: case-study
cover: ./cover.jpg
loop: "/media/works/birdy/loop.mp4"
order: 5
draft: false
---

## PROBLEM

노년층을 비롯해 디지털 리터러시가 낮은 사용자는 복잡한 UI, 작은 버튼, 여러 단계의 메뉴 탐색 때문에 메신저를 쓰기 어렵습니다. 그래서 가족·사회와의 소통이 끊기거나 꼭 필요한 정보에 닿지 못합니다.

![](./01.jpg)


## APPROACH

스마트폰 대신 쓰는 전용 디바이스 Birdy를 설계했습니다. 리드 연구원으로서 보조 연구원 둘과 함께 다음 과정을 밟았습니다.

1. **유저 리서치:** 문헌 리뷰, 과업 분석, 사용자 인터뷰로 디지털 리터러시가 낮은 사용자가 겪는 장애물과 요구를 도출했습니다.
1. **제품 디자인:** 리서치 결과를 바탕으로 아날로그 요소와 물리적 인터랙션을 결합한 디자인을 구체화하고 초기 컨셉을 시각화했습니다.
1. **프로토타입 제작 및 테스트:** 워킹 목업 3대를 만들고, 6쌍의 가족 사용자와 3주간 필드 테스트를 진행했습니다.
1. **데이터 분석:** 수집한 정성·정량 데이터로 사용자의 행동과 경험을 분석해 Birdy의 효과를 평가했습니다.

![](./02.jpg) ![](./03.jpg) ![](./04.jpg)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/YvDX9E_5jvk?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## SOLUTION

Birdy는 노년층을 위한 탁상형 메시징 디바이스입니다. 종이와 펜으로 쓴 손글씨가 입력이 되고, 그 손글씨가 그대로 가족에게 갑니다. 설계의 축은 셋이었습니다.

**화면은 메시지 하나에만 씁니다.** 노년층의 인지 특성에 맞춰 디스플레이 크기와 버튼 배치를 정했고, 정보가 쌓이지 않도록 메시지 전용 디스플레이를 두었습니다. 수신·발송 상태는 반투명 아크릴 본체를 통해 퍼지는 LED 빛으로 알립니다.

**손글씨는 그대로 남깁니다.** 66mm 종이 카드에 쓴 메시지를 Birdy가 디지털로 바꿔 보내되, 글씨의 질감과 개성은 그대로 전합니다. 함께 주는 20종의 이모지 카드로 감정을 붙입니다.

**조작은 버튼 몇 개로 끝납니다.** 탐색용 물리 버튼과 단순한 인터페이스로 조작 단계를 줄였고, 받은 메시지는 화면에 크게 뜹니다.

![](./06.jpg) ![](./05.jpg) ![](./07.jpg)


## IMPLEMENTATION

하드웨어, 소프트웨어, 제품 디자인 세 갈래로 개발했습니다. 종이 카드를 슬롯에 넣으면 IR 센서와 리니어 모터가 삽입을 감지해 정렬하고, 링 LED를 단 광각 카메라가 좁고 어두운 내부에서 카드를 찍습니다. 메시지는 Telegram API로 주고받고, 스캔한 이미지는 OpenCV로 후처리하며, Google Teachable Machine으로 손글씨와 이모지를 인식합니다.

부품은 Fusion 360으로 모델링해 3D 프린팅과 CNC 가공으로 만들었고, 반복 프로토타이핑으로 구조를 확정했습니다. 유지보수와 제작을 고려해 모듈 구조로 설계했습니다.

![](./12.jpg)

![](./13.jpg)

![](./08.jpg) ![](./09.jpg)

![](./10.jpeg) ![](./11.jpg)


## IMPACT

3주 필드 테스트에서 노년층 참가자의 메시지 사용량과 대화 주제가 달라졌습니다.

**소통 빈도 약 3배.** 6쌍의 가족 중 노년층은 주당 평균 21.5개의 메시지를 주고받아, Birdy 이전보다 약 3배 늘었습니다. 한 조부모는 주 1~2회 전화에서 주당 35개 메시지로 바뀌었습니다.

**넓어진 대화 주제.** 시간과 장소의 제약이 사라지자, 안부에 머물던 대화가 일상과 건강, 가족 소식으로 넓어졌습니다. "밥 먹었니?"가 손자의 시험 결과와 취미 이야기로 옮겨 갔습니다.

**손글씨와 종이가 담은 것.** 참가자의 70%가 손글씨가 감정 표현에 도움이 됐다고 답했고, 꽃을 그리거나 글씨 크기를 바꿔 마음을 전한 참가자도 있었습니다. 83%는 받은 종이 메시지를 보관하고 있었습니다. 손자의 메시지를 서랍에 간직한 조부모도 있었습니다.

![](./18.jpg) ![](./19.jpg) ![](./20.jpg)

![](./21.jpg) ![](./22.jpg) ![](./23.jpg)

![](./15.jpg)

![](./24.jpg)


## REFLECTION

**하드웨어 제품이 단순한 기기가 아니라 감성을 잇는 도구가 될 수 있을까?**

Birdy는 하드웨어 제품이 사용자에게 닿기까지의 모든 단계를 처음 경험한 프로젝트였습니다. 설계와 프로토타이핑, 사용자 교육, 피드백 수집까지, IoT 기기의 안정성과 사용자 경험을 동시에 확보해야 했습니다. 프로토타입 테스트와 펌웨어 최적화를 거듭하며 하드웨어와 소프트웨어를 함께 설계하는 일의 중요성을 확인했습니다. 기술로 사회적 문제를 푸는 디자인이 무엇인지 처음으로 고민하게 된 프로젝트이기도 합니다.
