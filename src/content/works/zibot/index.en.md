---
title: "ZIBOT KK"
subtitle: "Developing a kids' educational robot concept for the U.S. market"
org: "ZIBOT"
year: "2018 (1y)"
role: "Design Engineer"
responsibilities: ["Market Research", "Concept Development", "Prototyping"]
with: "Amy Wang (Project Manager), Frank (Product Designer)"
keywords: ["stem education", "kids robot", "product design", "silicon valley"]
tags: ["Market Research", "Concept Development", "Prototyping"]
kind: case-study
cover: ./cover.png
loop: "/media/works/zibot/loop.mp4"
order: 7
draft: false
---

## PROBLEM

**Which product concept fits an entry into the U.S. market?**

[**ZIBOT Inc.**](https://www.zhibankeji.com/) is a China-based startup that builds educational robots for children using natural language analysis. In 2018, having validated its product in the Chinese market, the company set up a Silicon Valley office to enter the U.S. market, but it had little data or insight about that market at the time. The U.S. product team's task was to gather data and insight on the U.S. market and find the opportunity areas that fit it.

![ZIBOT's existing educational robot](./01.png)


## APPROACH

**Researching the U.S. kids robot market and its products:** I mapped 52 robots on the U.S. market by use, and tested 12 of them hands-on — 8 STEM, 2 Lego-style, 2 best-sellers — comparing their hardware and software. I wrote a report laying out market trends, product characteristics, and opportunity areas.

**A direction that changed three times with HQ feedback:** After the research, headquarters first chose a Lego-style STEM product, then dropped it for lack of STEM experience and people. The August design brief was a small screen that docks on either a watch strap or the robot’s head, with a digital pet, eye expressions, and gesture and voice control. The brief revised on September 20 settled on app coding, maze content, and color-detection coding, for ages 3 to 6.

**Idea workshop:** With the CEO and the PM, I ran a workshop that pulled key words out of the market and product analysis and combined them. From the results we drew early concepts reflecting the features and design elements U.S. customers were likely to prefer.

**Product concept design and development:** We picked one of those ideas and defined the final product's form and functions through early sketches, 3D modeling, and a physical prototype.

![How the product direction changed with HQ feedback, from U.S. market research to CES 2019](./22.jpg)


## SOLUTION

**ZIBOT KK**

**Color coding:** A learning feature in which the robot recognizes colors and performs the matching action. Children pick up coding principles by arranging color patterns.

**A modular handle:** The handle was designed as a module so that a variety of accessories can attach to it. That extends its use beyond education to play and exploration.

**Size:** We set the size so that a child can hold it in one hand, and used prototypes to confirm the smallest dimensions that were feasible.

![Render of the robot on the color-coding board with the companion app](./04.png)

![Render of the yellow cube robot, marking the dot-matrix face and the magnetic attachment point](./05.png) ![Render marking the modular handle that accessories attach to](./06.png)

![Render of two robots moving across the grid of colored tiles](./07.png) ![Render of the robot tracing a Z along a line](./09.png)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/irJ2ge-0ZDw?rel=0&modestbranding=1" title="The ZIBOT KK concept film" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## IMPLEMENTATION

**Validating the design concept through prototyping:** Building a range of sizes and forms showed what product size was feasible and refined the design toward something close to a real product. The prototypes let me check function and usability together.

**Testing the feature with Arduino and MIT App Inventor:** To check whether color coding would actually work, I built a prototype of the core function. The office had nothing to build with, so I started by ordering parts — five orders in all — and put a color sensor, a Bluetooth module, and two continuous-rotation servos on an Arduino Nano. The app was built in MIT App Inventor. The robot reads the color under it and sends it to the app; solve the quiz in the app, press move, and it goes straight on white, turns right on red, and turns left on blue. The early tests identified functional constraints and room for improvement, and became reference material for later product development.

**Getting ready for CES 2019:** The final design was settled by the design team at the Chinese headquarters, led by Frank. I 3D-printed the design file they sent and fitted my parts inside, but time and print quality kept it from becoming the final prototype. For the CES 2019 booth, I made the product concept film using animations from the HQ team.

<video src="/media/works/zibot/proto.mp4" autoplay muted loop playsinline aria-label="Working prototype demo: the app receives the color the robot read, and after the quiz is solved the robot drives across the color tiles"></video>

![Wiring for the Arduino Nano, color sensor, Bluetooth module, and servos, beside the app screens where a correct quiz answer sets the robot moving](./21.jpg)

![A paper mockup made to check size](./10.jpg) ![The prototype testing color recognition on a colored tile](./11.jpg)

![The working prototype with its wiring exposed](./13.jpg) ![The control board and motor inside the mockup](./12.jpg)

![Block code built in MIT App Inventor to validate the function](./20.jpg)


## IMPACT

The final ZIBOT KK mockup was shown at ZIBOT's booth at CES 2019. It was the first project the U.S. product team completed, and the starting point for the company's entry into the U.S. market.

![The ZIBOT booth at CES 2019](./16.jpg) ![The ZIBOT KK concept mockup on show at the CES 2019 booth](./17.jpg) ![Talking with a visitor at the CES 2019 booth](./18.jpeg)


## REFLECTION

**A demanding environment can turn into a chance to learn, once you get through it.**

The internship in Silicon Valley in 2018 was nothing like what I had expected. I started at a small U.S. branch of a Chinese startup where the team was two people, a CTO and a PM, and team building and process were only just beginning. I used visuals and documentation to lower the communication barrier with the Chinese headquarters, and I fixed inefficient processes myself and put the team's workflow in order. The company then started a new project based on my work, and I took on product planning and design. From this I learned that a demanding environment brings bigger lessons, and that the difficulty in front of you can turn out to be an opportunity.
