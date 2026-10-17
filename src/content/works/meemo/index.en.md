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

Paper notes are good for ideas because you can write any way you like. They are hard to organize and keep, though. Digital notes are easy to store and search, but you can express less with them.

So many people use both. Then notes end up scattered and hard to find. I wanted a way to write as freely as on paper and keep things as tidy as digital.

## APPROACH

![A Venn diagram overlapping the advantages of paper notes and digital notes](./01.png)

I designed a system that leaves the way people write paper notes alone and moves only storage and search to digital.

First I looked, through user interviews and research, at how people use paper and digital notes. Something had to carry notes written on paper into the digital world, and it could not change anyone's note-taking habits.

That something became Meemo. Turning paper notes into digital ones right away sits at its center. Writing happens on paper; finding and organizing happen digitally.

## SOLUTION

![Meemo on a desk with round notes in several colors](./02.jpg)

![A yellow round note with handwriting on it, held in a hand](./05.png) ![The Meemo body with the input slot on top](./03.jpg) ![Close-up of a round note being ejected from the device](./04.jpg)

![Checking the digitized note on a phone](./06.png) ![The paper note going back onto a calendar after being digitized](./07.png)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/nXMv4ztNLbA?rel=0&modestbranding=1" title="Film showing Meemo in operation" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

Put a paper note into the device and Meemo turns it into an image and uploads it to Dropbox right away. The writing still happens on paper, but the note can be searched digitally and opened on other devices.

While it scans, the disc on the front turns slowly, and it stops when the scan is done. The turning disc tells you the scan is in progress, and it adds a little fun to taking notes.

When the scan is done, the note comes back out to be used again or filed away. The paper workflow is not interrupted. Only the note moves into the digital world.

## IMPLEMENTATION

![Meemo system diagram: camera, image processing, and Dropbox on the Raspberry Pi side; proximity sensor, servo motor, NeoPixel ring, and stepper motor on the Arduino side](./13.jpg)

![The six steps one note passes through: insertion, IR detection, servo feed, camera capture, cloud upload, and ejection](./18.jpg)

![The raw photo from inside the device, the image cropped to a circle, and the handwritten memo as uploaded to the cloud](./19.jpg)

The hands-on part runs on Arduino. When you insert paper, an infrared sensor detects it and a servo motor moves it inside. A stepper motor turns the disc to show progress. For the capture, a 12-LED NeoPixel ring around the camera lights up white to brighten the dark interior.

Cloud storage comes from linking a Raspberry Pi to the Arduino. When the Arduino reports a sheet, the Raspberry Pi takes a 1024×768 photo, crops the center to a square, and applies a round mask in the shape of the memo. The file is named with the capture time and uploaded to Dropbox.

## PROTOTYPING

![Meemo's internal structure: gears, Neopixel ring, camera, proximity sensor, step motor, and servo motor](./12.jpg)

![Meemo on a desk beside a monitor](./08.jpg) ![The camera and sensor seated inside the mockup](./09.jpg)

![The wiring inside, with a blue note fed in](./10.jpg) ![A machined exterior part held in hand](./11.jpg)

I modeled the exterior and the internal structure in Fusion 360. The shell was CNC-machined, and the internal parts that hold the camera, sensor, and gears were 3D-printed. The stepper motor drives the disc through two spur gears.

Paper took the most time. Paper that was too thin would not feed, and square corners caught inside the device. After trying different thicknesses, materials, and shapes, I settled on the round memo, and recessed the slot so paper slides in easily.

The camera didn’t work the first time either. I started by trying to find the four corners of the sheet, the way document-scanning examples do, but the wide-angle lens I needed for the cramped interior distorted the image too much to find them. The repository still has separate test code for the camera, cropping, the Dropbox upload, and serial communication. Along the way I burned a PCB and redid work after design mistakes.

## IMPACT

![The HCI Korea 2021 Creative Award certificate](./14.jpeg) ![Cover of the HCI Korea 2021 conference proceedings](./15.jpg)

Meemo received the Excellence Award at the HCI Korea Creative Award.

It was presented at the HCI Korea 2021 conference and published in the proceedings. The paper covers physical computing techniques such as infrared sensors and motor systems, along with the design of a user-centered note management interface.

## REFLECTION

![Meemo on a display shelf](./20.jpg)

Meemo was the first time I took an idea of my own all the way to a product. Wiring Arduino and Raspberry Pi together, designing the internal structure, 3D printing, and CNC machining were all new to me, and when I got stuck I asked specialists and fixed things one at a time.

Ideas that looked easy in my head threw up one unexpected problem after another once I built them. It was a lot like untangling a knot of string.
