---
title: "STORAGY"
subtitle: "Nonverbal HRI for an indoor delivery robot"
org: "XYZ Inc."
year: "2025 – Present"
role: "UX Designer"
responsibilities: ["HRI Design", "LED & Sound Feedback", "Expressive Display"]
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

**Feedback for a moving robot begins with defining its states and continues with handling the exceptions.**

STORAGY was not a product on a screen but a robot running down hallways. To define feedback state by state, I first had to understand in what order the robot moves and where it stops, what it senses and what it cannot know. Half the work, then, was learning how the robot operates; the other half was translating the states and feedback I had defined into units and formats the engineering team could implement as written. Splitting the channels into face, LED, and sound, and treating the state-by-state mapping table as the source of truth, both came out of that process.

The ideal scenario was not the hard part. Waiting, moving, and arriving are covered by six faces. What is hard is everything else: what the robot should show when it meets an obstacle, when nobody picks up what it delivered, when it has to turn back. None of that was defined in one pass, and it is still being filled in on site. This project taught me that a robot's HRI is not a design that ends at launch but one that is revised repeatedly in operation. So it is too early to say what I would do differently next time.

For my career, it meant working on a robot that moves rather than a device that sits still, and taking on the whole service scenario of indoor delivery.
