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

![ZIBOT's existing educational robot](./01.png)

**Which product concept fits an entry into the U.S. market?**

[ZIBOT Inc.](https://www.zhibankeji.com/) is a China-based startup that builds educational robots for children using natural language analysis. In 2018, having validated its product in the Chinese market, the company set up a Silicon Valley office to enter the U.S. market, but at the time it had little data or insight on that market. The U.S. product team had to gather that data and insight and find the opportunity areas that fit.

## APPROACH

![How the product direction changed with HQ feedback, from U.S. market research to CES 2019](./22.jpg)

**Researching the U.S. kids robot market and products:** I mapped 52 robots on the U.S. market by use, and tested 12 of them hands-on (8 STEM, 2 Lego-style, 2 best-sellers), comparing their hardware and software. I wrote a report laying out market trends, product characteristics, and opportunity areas.

**A direction that changed three times with HQ feedback:** After the research, headquarters first chose a Lego-style STEM product, then dropped it for lack of STEM experience and people. The August design brief was a small screen that docks on either a watch strap or the robot’s head, with a digital pet, eye expressions, and gesture and voice control. The brief revised on September 20 settled on app coding, maze content, and color-detection coding, for ages 3 to 6.

**Idea workshop:** With the CEO and the PM, I pulled key words out of the market and product research and tried combining them. Those combinations became early concepts with the features and design U.S. customers were likely to want.

**Product concept design and development:** We picked one idea and worked out the final form and functions through early sketches, 3D modeling, and a physical prototype.

## SOLUTION

![Render of the robot on the color-coding board with the companion app](./04.png)

![Render of the yellow cube robot, marking the dot-matrix face and the magnetic attachment point](./05.png) ![Render marking the modular handle that accessories attach to](./06.png)

![Render of two robots moving across the grid of colored tiles](./07.png) ![Render of the yellow robot beside a large box on colored tiles marked with X](./08.png) ![Render of the robot tracing a Z along a line](./09.png)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/irJ2ge-0ZDw?rel=0&modestbranding=1" title="The ZIBOT KK concept film" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Color coding:** The robot reads the color on the floor and makes the move set for that color. Children learn coding principles by laying out color tiles.

**A modular handle:** The handle is a module, so different accessories can be swapped onto it. That lets it be used for play and exploration, not only lessons.

**Size:** We set the size so that a child can hold it in one hand, and used prototypes to confirm the smallest dimensions that were feasible.

## IMPLEMENTATION

<video src="/media/works/zibot/proto.mp4" autoplay muted loop playsinline aria-label="Working prototype demo: the app receives the color the robot read, and after the quiz is solved the robot drives across the color tiles"></video>

![Wiring for the Arduino Nano, color sensor, Bluetooth module, and servos, beside the app screens where a correct quiz answer sets the robot moving](./21.jpg)

![A paper mockup made to check size](./10.jpg) ![The prototype testing color recognition on a colored tile](./11.jpg)

![The working prototype with its wiring exposed](./13.jpg) ![The control board and motor inside the mockup](./12.jpg)

![Block code built in MIT App Inventor to validate the function](./20.jpg)

**Testing the concept with prototypes:** I built several sizes and forms to find a size we could actually make, and refined the shape toward a real product. The prototypes also showed whether it worked and whether it was easy to use.

**Testing the feature with Arduino and MIT App Inventor:** To check whether color coding would actually work, I built a prototype of the core function. The office had nothing to build with, so I started by ordering parts, five orders in all, and put a color sensor, a Bluetooth module, and two continuous-rotation servos on an Arduino Nano. The app was built in MIT App Inventor. The robot reads the color under it and sends it to the app; solve the quiz in the app, press move, and it goes straight on white, turns right on red, and turns left on blue. The constraints and fixes the early tests turned up were written up for later product development to review.

**Getting ready for CES 2019:** The final design was settled by the design team at the Chinese headquarters, led by Frank. I 3D-printed the design file they sent and fitted my parts inside, but time and print quality kept it from becoming the final prototype. For the CES 2019 booth, I made the product concept film using animations from the HQ team.

## IMPACT

![The ZIBOT booth at CES 2019](./16.jpg) ![The ZIBOT KK concept mockup on show at the CES 2019 booth](./17.jpg) ![Talking with a visitor at the CES 2019 booth](./18.jpeg)

The final ZIBOT KK mockup was shown at ZIBOT's booth at CES 2019. It was the first project the U.S. product team saw through, and the starting point for the company's move into the U.S. market.

## REFLECTION

![An office desk with a laptop and parts boxes, robot products on the shelves behind](./23.jpg)

**A hard place to work was where I learned the most.**

The internship in Silicon Valley in 2018 was nothing like what I had expected. It was a small U.S. branch of a Chinese startup, and the team was two people, a CTO and a PM. Putting the team together and settling how it worked had only just begun. I used drawings and documents to get past the trouble communicating with the Chinese headquarters, and fixed inefficient steps myself to sort out how the team worked. The company then started a new project based on what I had made, and I took on product planning and design.
