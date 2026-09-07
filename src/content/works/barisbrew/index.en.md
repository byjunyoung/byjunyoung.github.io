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

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/Y1_9bq1jhkE?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## PROBLEM

At Baris Brew, a barista robot café, a single order passes through five screens. Customers order at a kiosk or in the app, follow the brewing status on the store display (DID), and collect their drink at the pickup zone. Operators run the store remotely from the back office, BarisON. Each screen had been built at a different time by a different team, so the same state went by different names and an order never read as one flow.

The problems found on site were concrete. Coupons were hard to find, and the coupon confirmation covered the pay button. When orders queued up, order numbers rotated on screen and customers could not judge their wait. In the back office, screen drafts and development had run ahead of planning, leaving the information architecture and permission model undefined.

![](./01.jpg) ![](./02.jpg)


## APPROACH

I joined in August 2025 to tie the customer channels and the operations console together as one system UX, working from three principles.

**Field first.** I gathered problems from a trade show operations debrief and an interview with the retail operations lead. In the summer of 2026 I ran field observations across stores and shared a report of usage patterns by store with the whole company.

**One order, one flow.** I defined the states of an order first, from ordering and payment through brewing, pickup, and retrieval, then aligned the kiosk, app, and displays to show the same state in the same words.

**The document is the source of truth.** Each product got a PRD whose features and policies map one-to-one to the Figma screen pages. When a screen and a rule disagree, the document is fixed first.


## SOLUTION

### Kiosk

I organized the flow from the start screen through menu browsing, item detail, order review, and payment. Coupons are applied on the order review screen by scanning a QR code or entering a code, and payment finishes in two screens: choosing a method and following the terminal guidance. To meet the accessibility standard for unattended terminals, the kiosk gained a physical keypad, voice guidance, high contrast, and magnification, and the start screen carries the entry point for voice ordering.

![](./03.jpg)

![](./04.jpg)

### Mobile app

Customers order before they arrive and see their queue position and expected completion time in the app. The brewing status screen uses one structure for the waiting, brewing, done, and error states, and guides them to pickup when the drink is ready. The [expected wait time](https://www.venturesquare.net/1102926) follows a single rule and is shown the same way on the kiosk and in the app.

![](./05.jpg)

### Store display and pickup zone

In a store with no staff, the display does the calling. It splits orders being brewed from orders waiting for pickup, by order number, and announces completion on screen. The pickup zone shows each order as a card and clears cards as a camera detects pickups. The wording for retrieval and disposal situations was aligned across the app and the displays.

![](./06.jpg)

<video src="/media/works/barisbrew/did.mp4" autoplay muted loop playsinline></video>

### Operations console, BarisON

BarisON is the console from which headquarters runs unmanned stores remotely. I planned store and robot control (power, status, cameras), unified management of the headquarters master catalog and each store's products and stock, an alarm system organized by operational severity, and a three-tier account model for headquarters admins, operations staff, and store owners. I also set common policies such as input form validation and button label conventions.

![](./07.jpg)

### Voice ordering, VoiceOrder

I designed the prompts and conversation flow for LLM-based voice ordering: a prompt defining personality, environment, tone, goals, guardrails, and tools; the wake word ("Baris"); barge-in; and the session-end rules and completion screen. The conversation was validated against twelve scenarios, from a basic order to multi-item commands, small-talk interruptions, and budget-based recommendations, and the TTS voice was chosen by listening to the candidates side by side. The kiosk carries the entry point and distinguishes the listening, thinking, responding, and error states with an animation along the screen edge. It was [first demonstrated](https://www.linkedin.com/posts/xyzcorporation_ai-robotcafe-agenticai-activity-7378711064454205440-h9Wl) at the Seoul AI Robot Show in September 2025, [unveiled at RoboWorld 2025](https://www.mt.co.kr/future/2025/11/03/2025110314103736602) in November, and then went into a store pilot; issues from the logs, such as TTS audio feeding back into the microphone, were tracked in a checklist and fixed in updates.

<video src="/media/works/barisbrew/voice.mp4" autoplay muted loop playsinline></video>


## IMPLEMENTATION

**Documents and handoff.** PRDs for the kiosk, app, DID, pickup zone, and BarisON link every feature and policy to its Figma screen and keep a change log. Work goes to development in phases, and I chair the BarisON project meetings to set priorities.

**Validation.** I validated the designs with a store pilot checklist, barrier-free kiosk QA, and analysis of voice order logs. The logs showed people using it like a voice assistant, which I reframed as a UI problem rather than an AI capability problem.


## IMPACT

- Shipped a mobile app update timed to a new store opening.
- Put the VoiceOrder MVP into a store pilot in December 2025 and released an update that improved wake word recognition and TTS.
- Applied the stock and payment management improvements in BarisON and finalized the barrier-free kiosk spec.
- Shared the field observation research results with the whole company.
- The system runs in stores of many kinds, including public cultural spaces, apartment community centers, corporate retreats, and unmanned laundromats.

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/tAH6xt0qpqk?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
