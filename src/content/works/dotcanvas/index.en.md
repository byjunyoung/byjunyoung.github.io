---
title: "Dot Pad & Dot Canvas"
subtitle: "UX of a tactile display and its tactile-graphics authoring tool"
org: "Dot Inc."
year: "2022 – 2025"
role: "UX Designer"
responsibilities: ["Hardware UX Design", "UX Research", "Wireframe", "GUI Design"]
with: "김승환 (Service Planner), 주백준 (GUI Designer)"
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

Visually impaired students cannot take in graphic information by sight, so they learn from the tactile graphics in braille textbooks or from separate tactile teaching aids. Those materials are always in short supply. Tactile graphics in braille textbooks are hard to produce and maintain, and they never cover every figure in the original, so only some make it in. Tactile aids are mostly made by teachers themselves. Sit in on a class at a school for the blind and you will find picture materials built from tape and stickers. They take time and money to make, and they do not last.

These constraints narrow what students get to learn and put a load on teachers. Another way of making tactile materials was needed.

![](./01.png) ![](./02.jpg) ![](./03.jpg)


## APPROACH

I joined Dot in July 2022 as a hardware UX designer, but the first job was not hardware. The Dot Pad tactile display is only useful with tactile graphics to show, and there was no tool for making them. Working as one team with a service planner and a GUI designer, the goal was to ship web and app demos of the authoring tool, Dot Canvas, within three months.

**Two users.** The person who makes a tactile graphic and the person who touches it are not the same. The web was aimed at teachers making and managing materials; the app at visually impaired users drawing and touching for themselves. In Korea we ran field studies with special-education teachers and visually impaired students; for users abroad, surveys and diary studies covered the usage environment and its pain points. That data pinned down the problems of the first Canvas version and set the direction for improvements.

**Then the hardware.** Once Canvas had shipped, I moved to Dot Pad itself. I compared more than 20 braille devices to define its tactile notation and the specs and requirements for the next model, and designed the key functions and the haptic and LED feedback that went into the production model.

![](./04.jpg)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/N_L3hR81nik?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## SOLUTION

### Dot Canvas Web

Teachers draw tactile graphics in the browser or import a PDF or image and convert it. The result is stored in Dot Cloud and shared with other teachers through a shared drive. In class, the same graphic can be sent to up to 10 Dot Pads at once, so students touch the same picture and talk about it.

![](./09.jpg)

### Dot Canvas App

Drawing happens with iPad touch and the Apple Pencil. With VoiceOver and live drawing, visually impaired users draw for themselves and feel what they drew on Dot Pad right away. Files sync to the web through Dot Cloud.

![](./10.jpg)

### Dot Pad

Dot Pad is a multi-line tactile area for graphics, a single line of braille beneath it, and physical keys. A visually impaired user cannot pick a key by looking at it. The same key has to do the same thing every time, and keys have to be told apart by touch. So I defined the key functions consistently, added physical markings, and designed the haptic and LED feedback that confirms an input and shows the device's state; all of it went into the production model. A comparative analysis of more than 20 braille devices set the tactile notation and defined the specs and requirements for the next model, and user evaluations gathered the feedback to carry into it.

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/iSmRM2PUBzA?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## IMPLEMENTATION

**Screen design and GUI.** Based on the research, I designed the screens for Dot Canvas Web and App in Figma and did the GUI. Because teachers and visually impaired students share the interface, the UI structure and the placement of functions were organized around those two.

**Documents and collaboration.** I documented screen specs and functional specifications and tracked issues in JIRA, working with the development team to absorb technical changes and keep the schedule for improvements and release.

![](./05.jpg)

![](./06.jpeg) ![](./07.jpeg)

![](./08.jpeg) ![](./13.jpeg)


## IMPACT

Dot Canvas won the CES 2024 Innovation Award and was shown at CSUN 2024. Dot Pad's tactile interface went into the production model. In a science class I observed at a school for the blind in 2024, the picture materials once made from tape and stickers had been replaced by Dot Pad.

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/AHK3VnjvA5Y?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

![](./15.jpg) ![](./14.jpeg)


## REFLECTION

**The price of moving fast comes due later, in maintenance.**

Dot Canvas had to ship web and app demos in a short window. The team had little relevant experience, and we had three months to produce something usable. We filled whiteboards and prototyped quickly, and I handled not only UX design but collaboration with developers and the schedule.

The price of moving fast was just as clear. We hit the short-term goal, but the design had not accounted for scale, so maintenance later required a lot of rework, and parts of it were rough. Hearing feedback directly in user studies showed me how much the balance between speed and quality matters in UX design.

What I learned most was the users. Meeting visually impaired users up close taught me that accessibility is not something added at the last step of a product, but something to work on from the first chapter of the UX.
