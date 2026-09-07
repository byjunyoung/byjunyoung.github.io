---
title: "STORAGY"
subtitle: "Nonverbal HRI for an indoor delivery robot"
org: "XYZ Inc."
year: "2025 – Present"
role: "UX Designer"
responsibilities: ["HRI Design", "LED & Sound Feedback", "Expressive Display"]
with: "Robot engineering team"
keywords: ["hri", "delivery robot", "nonverbal interaction"]
link: { label: "STORAGY Website", url: "https://xyzcorp.io/STORAGY" }
tags: ["HRI Design", "LED & Sound Feedback", "Expressive Display"]
kind: case-study
cover: ./cover.png
loop: "/media/works/storagy/loop.mp4"
order: 2
draft: false
---

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/TPq3F_mAeP8?start=28&rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## PROBLEM

STORAGY, an indoor delivery robot, shares hallways, elevators, and offices with people. It has to say without words whether it is waiting, moving, stopped by an obstacle, or done delivering, so that people make way and pick up what it brought. At the start there was no defined list of robot states, and no rules for the face and the light that would show them.


## APPROACH

We defined the robot's states first, then split the channels. System states are shown by LED and sound, driving states by the front display and sound. Display and LED feedback were mapped state by state, with sound added afterward. We put it on the real robot with the engineering team and revised as we went.


## SOLUTION

### Faces

I made the representative face and animation for six states: booting, idle, moving, obstacle, charging, and delivery complete. The position, size, and motion of two eyes are all that separate the states.

<video src="/media/works/storagy/faces.mp4" autoplay muted loop playsinline></video>

### LED and display

The front display carries the face; the LED under the body shows the system state.

![](./01.jpg) ![](./02.jpg)

<video src="/media/works/storagy/led.mp4" autoplay muted loop playsinline></video>

### Multi-floor delivery

STORAGY takes the drinks Barisbrew makes, rides the elevator, and delivers them to the desk. I defined the scenarios and states for this multi-floor delivery and planned the features and screens of MobileON, the console that controls the robot remotely.

<video src="/media/works/storagy/delivery.mp4" autoplay muted loop playsinline></video>


## IMPACT

It runs floor-to-floor delivery with Barisbrew in the Robot Building Solution at the XYZ headquarters in Seongsu, Seoul.


## REFLECTION

**The ideal scenario is easy. The exceptions are the work.**

The hardest part was defining the robot's feedback state by state. I had to understand how the robot actually operates before any feedback could be attached, and this project taught me at what granularity to define it and in what format to hand it to engineering.

The ideal scenario was actually fine. What was hard were the unexpected situations and exception cases, and that work is still going on. It is not something finished in one pass; it needs repeated rounds of improvement. What I would do differently next time, I do not yet know.

For my career, it meant working on a robot that moves, and on the scenario of indoor delivery.
