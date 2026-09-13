---
title: "Meemo"
subtitle: "A memo system that saves handwritten paper notes to the cloud automatically"
org: "UNIST"
year: "2020 (6m)"
role: "Design Engineer"
responsibilities: ["Product Design", "Prototyping"]
keywords: ["analog memo", "digital memo", "physical computing", "cloud"]
awards: ["HCI Korea Creative Award, Excellence Award (2021)"]
link: { label: "HCI Korea 2021 Journal", url: "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10530368" }
tags: ["Product Design", "Prototyping"]
kind: case-study
cover: ./cover.jpg
loop: "/media/works/meemo/loop.mp4"
order: 6
draft: false
---

## PROBLEM

![A Venn diagram overlapping the advantages of paper notes and digital notes](./01.png)

Analog notes are good for capturing ideas because you can write without being tied to a format, but they are hard to organize and to keep for the long term. Digital notes, on the other hand, give you storage and search but narrow the range of expression.

Many people use both at once, which weakens the consistency of how information is kept and makes search harder. What is needed is a way to have the freedom of analog notes and the order of digital ones together.

## APPROACH

To get past the limits of the analog system and the digital one, I designed an integrated system that joins the way analog notes are written to the storage and search of digital ones.

**Designing a system that links analog and digital:** Through user interviews and research, I analyzed how people use analog and digital notes. That confirmed the need for a medium to carry notes made in the physical world into the digital one, so I designed a way to connect the two environments without changing existing note-taking habits.

**Building Meemo:** On that design I built Meemo. Real-time conversion of paper notes into digital sits at the center, so the writing environment of paper stays as it is while the search and management convenience of digital notes comes with it.

## SOLUTION

![Meemo on a desk with round notes in several colors](./02.jpg)

![A yellow round note with handwriting on it, held in a hand](./05.png) ![The Meemo body with the input slot on top](./03.jpg) ![Close-up of a round note being ejected from the device](./04.jpg)

![Checking the digitized note on a phone](./06.png) ![The paper note going back onto a calendar after being digitized](./07.png) ![Meemo on a desk beside a monitor](./08.jpg)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/nXMv4ztNLbA?rel=0&modestbranding=1" title="Film showing Meemo in operation" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Meemo**

**Instant cloud upload and digitization:** When a user puts a handwritten paper note into the device, Meemo converts it to a digital image and uploads it to the cloud (Dropbox) right away. Writing stays on paper, while the note becomes searchable in the digital environment and usable on other devices.

**Rotating-disc feedback:** While a note is being scanned, the disc on the front face turns slowly, and it stops when the scan is done. The movement lets the user know the scan is in progress, and adds a small pleasure to writing a note.

**Input and output that bridge analog and digital:** Insert a note and it is digitized; when the work is done the note comes back out to be used again or filed away. The process moves a note into the digital environment without breaking the analog workflow.

## IMPLEMENTATION

![The six steps one note passes through: insertion, IR detection, servo feed, camera capture, cloud upload, and ejection](./18.jpg)

![The raw photo from inside the device, the image cropped to a circle, and the handwritten memo as uploaded to the cloud](./19.jpg)

**Building the physical interaction:** To realize the physical interaction, I built the system on Arduino. When a user inserts paper, an infrared sensor detects it, a servo motor moves it inside, and a stepper motor turns the disc to show progress. For the capture, a 12-LED NeoPixel ring around the camera lights up white to brighten the dark interior. This physical interaction was what carried the analog experience into the digital environment.

**Cloud integration and application development:** To implement cloud storage, I built a data communication system linking a Raspberry Pi and Arduino. When the Arduino reports a detected sheet, the Raspberry Pi takes a 1024×768 photo, crops the center to a square, and applies a round mask in the shape of the memo. The file is named with the capture time and uploaded to Dropbox.

## PROTOTYPING

![Meemo's internal structure: gears, Neopixel ring, camera, proximity sensor, step motor, and servo motor](./12.jpg)

![The camera and sensor seated inside the mockup](./09.jpg) ![The wiring inside, with a blue note fed in](./10.jpg) ![A machined exterior part held in hand](./11.jpg)

**Product design and mockup fabrication:** The exterior and structure were modeled in 3D with Fusion 360. The outer shell was CNC machined and the internal structural parts were 3D printed, designed for easy assembly and maintenance. Meemo came together as a prototype with a physical interface and a working structure.

## IMPACT

![The HCI Korea 2021 Creative Award certificate](./14.jpeg) ![Meemo on a display shelf](./16.jpg)

Meemo received the Excellence Award at the HCI Korea Creative Award.

It was presented at the HCI Korea 2021 conference and published in the proceedings. The paper covers physical computing techniques such as infrared sensors and motor systems, along with the design of a user-centered note management interface.

## REFLECTION

**Turning imagination into something real is as tangled and unpredictable as untangling a knot of string.**

Meemo was the first time I took an idea of my own all the way to a product. Connecting a paper notebook to digital technology ran into technical obstacles I had not expected. Paper thickness, stiffness, and even corner shape all mattered: paper that was too thin would not feed, and square corners caught inside the device. I burned a PCB and redid the same work because of design mistakes, and it took trial and error to settle the paper's material and shape. I asked specialists for help when I needed it and improved the technology and the structural design, and I handled technical integration with Arduino and Raspberry Pi, internal structural design, and mockup fabrication with 3D printing and CNC machining myself.

I learned that an idea that looks easy in your head turns, once you build it for real, into a long run of complicated and unpredictable problem-solving — much like untangling a knot of string.
