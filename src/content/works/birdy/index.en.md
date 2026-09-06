---
title: "Birdy"
subtitle: "A paper-based messaging device for family communication with older adults"
org: "UNIST"
year: "2021 (1y)"
role: "Lead Researcher"
responsibilities: ["Research", "Product Design", "Prototyping", "Project Management"]
with: "김나눔, 윤혜정 (Research Assistants)"
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

Older adults, low-income households, and people with disabilities — those left on the far side of the digital divide — have a hard time with messengers because of complex UI layouts, small buttons, and multi-level menu navigation. As a result, contact with family and society is cut off, or access to essential information is limited.

![](./01.jpg)


## APPROACH

To make messengers usable for people with low digital literacy, we designed Birdy, a dedicated device used in place of a smartphone. Development went through the following steps.

1. **User research:** Through a literature review, task analysis, and user interviews, we identified the obstacles and needs of users with low digital literacy.
1. **Product design:** Building on the research, we worked out a design that brought together analog elements and physical interaction, and visualized the early concept.
1. **Prototype build and testing:** We built three working mockups and ran a three-week field test with six family pairs.
1. **Data analysis:** Using the qualitative and quantitative data we collected, we analyzed user behavior and experience, evaluated Birdy's effect, and drew out insights.

![](./02.jpg)

![](./03.jpg) ![](./04.jpg)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/YvDX9E_5jvk?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## SOLUTION

**Birdy: a handwriting-based digital messaging device**

Birdy is a desktop messaging device designed for older users. It takes handwriting on paper with a pen as its input and connects digital communication across generations.

**An interface that lowers cognitive load:** Display size, button layout, and LED feedback were designed around how older adults take in information. A message-only display keeps information from piling up, and diffused LED light through the translucent acrylic body signals when a message has been received or sent.

**Handwriting turned digital:** A user writes a message by hand on a 66mm paper card, and Birdy converts it to digital and sends it. The texture and character of the handwriting stay intact, and 20 emoji cards that come with the device make feelings easier to express.

**Simple controls:** Physical buttons for navigation and a simple interface cut down the steps it takes to operate. Received messages appear large on the display, and LED feedback shows the current state.

![](./06.jpg)

![](./05.jpg) ![](./07.jpg)


## IMPLEMENTATION

Birdy was developed along three tracks: hardware, software, and product design.

**Hardware:** Birdy is made up of a display, a scanner, a microcontroller, LED lighting, an IR sensor, a micro linear motor, and a wide-angle camera. When a paper card goes into the 66mm round-cornered slot, the IR sensor and linear motor detect it and align it, and physical buttons browse the conversation history. The translucent acrylic storage box holds paper, pen, and the emoji book, and works with the LED lighting to signal state through color. A wide-angle camera with a ring LED captures the card even in the narrow, dark interior.

**Software development:** The software is built from modules covering message sending and receiving, image processing, and display control. Messages travel through the Telegram API, and scanned images are post-processed with OpenCV. Google Teachable Machine recognizes handwriting and emoji, converts them into digital text, and shows them on the display.

**Product design and mockup fabrication:** Each part was modeled in Autodesk Fusion 360, and the structure was settled through repeated prototyping. The main parts were 3D printed and the exterior was CNC machined, and the whole design is modular, for easier maintenance and fabrication.

![](./12.jpg)

![](./13.jpg)

![](./08.jpg) ![](./09.jpg)

![](./10.jpeg) ![](./11.jpg)


## IMPACT

Over the three-week field test, how much the older participants messaged and what they talked about both changed.

**About a threefold increase in digital communication:** Over the three weeks, the older adults among the six family pairs exchanged an average of 21.5 messages a week — about three times as often as before Birdy. F1-GP went from one or two phone calls a week to 35 messages a week.

**Asynchronous messaging widened what they talked about:** Asynchronous messaging removed the constraints of time and place, moving conversation from simple greetings to everyday stories, health, and family news. For F3-P, the topics moved from "Have you eaten?" to a grandchild's exam results and hobbies.

**What handwriting carried:** 70% of participants said handwriting helped them express emotion, and F2-GP drew flowers in messages and changed letter size to convey feeling.

**Emotional connection through paper:** Paper messages lowered the psychological barrier to digital communication. 83% of participants kept the paper messages they received, and F5-GP held on to a grandchild's notes in a drawer.

![](./14.jpg)

![](./15.jpg)

![](./17.jpeg)


## REFLECTION

**Can a hardware product be more than a device — a tool that connects feelings?**

Birdy was the first time I went through every stage of getting a hardware product into a user's hands. From product design to prototyping, user training, and feedback collection, I had to secure the stability of an IoT device and the user experience at the same time. Through repeated prototype tests and firmware tuning, I saw how much it matters to design hardware and software together.

Going through the full design process taught me user-centered design and how to balance technology with feeling. Birdy was the first project that made me think about what it means to design a solution to a social problem with technology.
