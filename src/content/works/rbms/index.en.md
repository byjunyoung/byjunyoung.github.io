---
title: "RBMS"
subtitle: "One screen for a building's robots and facilities"
org: "XYZ Inc."
year: "2026 – Present"
role: "UX Designer"
responsibilities: ["System UX", "Information Architecture", "Dashboard Design", "Front-end"]
keywords: ["robot fleet", "building management", "dashboard", "signage", "ai agent"]
tags: ["System UX", "Information Architecture", "Dashboard Design", "Front-end"]
kind: case-study
cover: ./cover.jpg
loop: "/media/works/rbms/loop.mp4"
order: 4
draft: false
---

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/TPq3F_mAeP8?rel=0&modestbranding=1" title="The Robot Building Solution film" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## PROBLEM

Inside one building a guide robot, a delivery robot, a patrol robot, a cleaning robot, and a barista robot all work at once. Alongside them run the CCTV cameras, the climate sensors, and the elevators. Each robot had its own control screen, and the facilities were watched somewhere else again. Whoever ran the building had nowhere to see, in one place, what state the building was in.

Visitors had the same gap. To anyone walking through the lobby, nothing showed that the building ran on robots.

## APPROACH

![Diagram of what is managed, the shared state fields, and the two surfaces they go out to](./01.jpg)

My part began with defining what would be managed, what state each thing reports, and what screens were needed. For five robots and three kinds of facility, I set down in a document what gets read, under what name, and where it appears.

State was reduced to four fields. To read eight different things side by side on one screen, the axes have to match: battery, location, operating state, and current task. Facilities have no battery and never move, but the fields stay in place rather than disappear. A list whose rows shift shape is harder to read.

Silence and being switched off are treated separately. If a robot has not refreshed its state for 30 seconds, the server moves it to disconnected. A robot someone turned off and a robot that stopped answering call for different actions.

The screen was split in two. Both surfaces sit on the same state, but the control web is where a building operator acts, and the lobby signage is one that visitors only look at.

## SOLUTION

### Control web

![The control web dashboard and the robot dispatch view. Left, the building section and the alert feed; right, a dispatched cleaning robot's progress and the task queue](./03.jpg)

Robot positions sit on a section of the building, and the status of robots and facilities collects in one panel. Selecting an item opens its battery, location, and current task. Anything abnormal is announced at one of three levels: information, warning, urgent. From an alert you can open the CCTV at that spot or dispatch a robot. A dispatched robot shows its progress as moving, working, and done, and anything waiting stacks up in a task queue. Switching the first-floor lights and air conditioners, connecting robots and IoT devices, renaming them, managing floor information and notices, and issuing accounts all happen in the control web.

### Lobby signage

The same data, rearranged for visitors. A vertical section of the building carries a robot on each floor, so what is moving where reads from across the room. Beside it sit the facility status, the robot roster, and the building's notices. Notices and the floor-by-floor tenant directory used to be uploaded as images and are now typed text. I set the direction; the engineering team built the server side. The building manager can now edit them straight from the control web, and the lettering is sharp now. The standing display in the lobby also cycles through images uploaded from the control web.

### AI agent

<video src="/media/works/rbms/console.mp4" aria-label="The lobby conversation view and the building-section dashboard side by side" autoplay muted loop playsinline></video>

A button at the top of every control web screen opens ROBI, the conversation panel. You ask in plain words, and the answers and the robot event alerts stack up in one timeline.

## IMPLEMENTATION

I wrote the requirements, the information architecture, and the screen specs, and designed the dashboard and the signage. From September 2026 I also took part in building the screens. The engineering team builds the server; I share the front-end code with a developer and check it against the real robots and facilities. Moving every screen onto the company design system was my part.

A simulation mode and a live-data mode share one interface, so the whole flow can be shown where there is no robot and no server to connect to.

## IMPACT

Control that had been scattered across individual robots is now held at the level of the building. The control web shows the robots and facilities of the Seongsu headquarters on one screen and actually switches the first-floor lights and air conditioners. The lobby signage and the standing display take their content from the control web and run in the building.
