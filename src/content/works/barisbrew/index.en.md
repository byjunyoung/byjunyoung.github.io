---
title: "Baris Brew"
subtitle: "Unified customer and operator UX for a barista robot system"
org: "XYZ Inc."
year: "2025 – Present"
role: "UX Designer"
responsibilities: ["System UX", "Voice UX", "UX Design Ops"]
keywords: ["barista robot", "kiosk", "voice order", "llm"]
link: { label: "Baris Brew Website", url: "https://xyzcorp.io/baris" }
tags: ["System UX", "Voice UX", "UX Design Ops"]
kind: case-study
cover: ./cover.jpg
loop: "/media/works/barisbrew/loop.mp4"
order: 1
draft: false
---

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/GnPiB19v5kQ?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## PROBLEM

Baris Brew, a barista robot café, meets its customers at several touchpoints. They order at a kiosk or in the mobile app, follow the brewing status on the front display, and collect their drink at the pickup zone. Operators manage menus, stock, and device status in the back office, BarisON. Each touchpoint had been built with its own screens and rules, so a single order did not always read as one continuous flow.

The problems found on site were concrete. Coupons were hard to find, and the coupon confirmation covered the pay button. When orders queued up, order numbers rotated on screen, so customers could not judge their wait. The QR reader was not obviously placed, and some customers had to look for it. In the back office, screen drafts and part of the development had run ahead of planning, leaving gaps in the information architecture and the permission model.

![](./01.jpg) ![](./02.jpg)


## APPROACH

When I joined in August 2025, I took on the role of tying the customer channels and the operator back office together as one system UX.

**Start from the field:** I gathered problems from an operations debrief after a trade show and from an interview with the retail operations lead. In the summer of 2026 I ran field observations across stores and shared a report of usage patterns and insights by store with the whole company.

**Design the flow across touchpoints:** I defined the states of a single order from ordering and payment through brewing status, pickup, and retrieval, and aligned the app, kiosk, and displays to show the same state in the same words.

**Run the UX track:** I kept the specs and the Figma files separately managed, and used phased handoff milestones and weekly meetings to stay in step with the development and AI teams. From October 2025 the UX part also took on the PM role.


## SOLUTION

### Customer channels

**Kiosk:** I shortened the coupon flow to QR scan, items added automatically, edit the menu, pay, and merged the payment method selection and guidance screens. For the barrier-free kiosk I kept the existing form factor and added a speaker, microphone, and keypad, then reviewed TTS timing, focus order, and screen reader behavior.

**Mobile app:** I managed app updates centered on pre-ordering and pickup notifications, and added a temperature-based price option.

**Pickup zone and front display:** I designed the brewing status guidance and the feedback right after pickup, and unified the wording for retrieval and disposal situations across the app and the displays. The pickup zone screen stays simple, with motion and labels kept to a minimum.

![](./03.jpg) ![](./04.jpg)

![](./05.jpg)

### Operator back office, BarisON

I defined a three-tier permission model for headquarters, purchasing partners, and store operators, and turned the operations interview into requirements for product, stock, payment, and sales analysis features. I also designed the functions an unmanned store needs, such as device power management (restart, shutdown, One-Stop On/Off) and pickup zone background video management.

![](./06.jpg)

### VoiceOrder

I designed the prompts and conversation flow for an LLM-based voice ordering service: a prompt defining personality, environment, tone, goals, guardrails, and tools; the wake words ("Baris", "Hi, Baris"); barge-in; and the session-end rules and completion screen. Issues found in the store pilot, such as the TTS audio feeding back into the microphone and triggering false barge-ins, were tracked in a checklist and fixed in updates.


## IMPLEMENTATION

**Documentation and handoff:** I managed screen specs and functional specs separately from Figma and handed them to development in phases. I chaired the BarisON project meetings to set priorities with the development team.

**Validation:** I validated the designs with a store pilot checklist, barrier-free kiosk QA, and analysis of voice order logs. The logs showed people using it like a voice assistant, which I reframed as a UI problem rather than an AI capability problem.


## IMPACT

- Shipped a mobile app update timed to a new store opening.
- Put the VoiceOrder MVP into a store pilot in December 2025 and released an update that improved wake word recognition and TTS.
- Applied the stock and payment management improvements in BarisON and finalized the barrier-free kiosk spec.
- Shared the field observation research results with the whole company.
