---
title: "Meemo"
subtitle: "A memo system for writing creative notes and keeping them for good"
org: "UNIST"
year: "2020 (6m)"
role: "Design Engineer"
responsibilities: ["Product Design", "Prototyping"]
keywords: []
link: { label: "HCI Korea 2021 Journal", url: "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10530368" }
tags: ["Product Design", "Prototyping"]
kind: case-study
cover: ./cover.jpg
loop: "/media/works/meemo/loop.mp4"
order: 2
draft: false
---

## PROBLEM

Analog notes are good at capturing creative ideas: expression is free and access is immediate. When it comes to organizing them and keeping them for the long term, though, the limits are clear. Digital notes, on the other hand, offer vast storage and strong search, but they narrow the freedom of creative expression.

Many people use both at once, which weakens the consistency of how information is kept and makes systematic access and efficient search harder. What is needed is a new solution that can hold the freedom of analog notes and the order of digital ones together.

![](./01.png)


## APPROACH

To get past the limits of the analog system and the digital one, this project set out to design an integrated solution that joins the directness of analog notes to the efficiency of digital ones. The aim was to cover the weaknesses of each so that people could work in a more creative and more efficient note-taking environment.

**Designing a system that links analog and digital :** Analog notes suit creative, intuitive capture, while digital notes are far more efficient for storing and finding things. To combine the strengths of the two systems and cover their weaknesses, we analyzed how people actually use analog and digital notes through user interviews and research. The analysis pointed to the need for a medium that could carry notes made in the physical world into the digital one naturally. From there we designed an integrated approach that connects the two environments without disturbing existing note-taking habits.

**Building Meemo :** On that system design we built a product called Meemo. Meemo connects analog and digital notes efficiently through a straightforward interface and real-time conversion. It keeps the free creative environment of analog notes while making the search and management of digital notes as convenient as possible, offering a note-taking environment distinct from existing tools.

![](./02.jpg)

![](./03.jpg) ![](./04.jpg)

![](./05.png) ![](./06.png) ![](./07.png)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/nXMv4ztNLbA?rel=0&modestbranding=1" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## MEEMO

**Instant cloud upload and digitization** : When a user inserts a handwritten paper note into the device, Meemo converts it to a digital image and uploads it to the cloud (Dropbox, for example) right away. The user keeps writing on paper as freely as before while the note becomes easy to search in the digital environment and usable on other devices.

**An intuitive feedback system** : While an upload runs, the disc on Meemo's front face rotates, giving visual and physical feedback. That movement lets the user read the upload status at a glance, and adds a small pleasure to writing a note.

**A natural link between analog and digital** : Meemo is designed to handle paper notes going in and coming out simply and efficiently. Insert a note and it is digitized automatically; when the work is done the note comes back out to be used again or filed away. The process does not disturb the analog workflow while supporting a smooth move into the digital one. Users keep the intuitive act of writing on paper and still get efficient management and use of their notes in the digital environment.

![](./08.jpg)

![](./09.jpg) ![](./10.jpg) ![](./11.jpg)

![](./12.jpg) ![](./13.jpg)


## IMPLEMENTATION

**Building the physical interaction** : To make the physical interaction feel natural, the system was built on Arduino. When a user inserts paper, an infrared sensor detects it and a servo motor moves it along. A DC motor turns the disc so that upload progress is easy to read. This physical interaction was what carried the analog experience into the digital environment.

**Cloud integration and application development** : To implement cloud storage, the core function, we built a data communication system linking a Raspberry Pi and Arduino. A camera module captures the paper note, and the Dropbox API uploads the image to the cloud in real time. The system digitizes and stores a note the moment the user inserts paper, which is what connects analog and digital efficiently.

**Product design and mockup fabrication** : The exterior and structure were modeled in 3D with Fusion 360, and the outer shell was CNC machined. Internal structural parts were 3D printed so that the device would be easy to assemble and maintain. Meemo came together as a prototype with a user-friendly physical interface and a working structure.

![](./14.jpeg)

![](./15.jpg)


## ACHIEVEMENT

**Excellence Award at the HCI Korea Creative Award** : Meemo received the Excellence Award at the HCI Korea Creative Award, recognized for its user experience design and its inventive physical interaction. The judges rated the original approach of integrating analog and digital note systems highly, and gave particular credit to the intuitive interface for moving between paper and digital notes. One judge mentioned Meemo's potential as a business, viewing its technical originality and commercial promise positively.

**Published in the HCI Korea 2021 conference proceedings** : Meemo was presented at the HCI Korea 2021 conference as a concrete case study in improving user experience, built on the novel approach of integrating analog and digital note systems. The paper covers physical computing techniques (infrared sensors, motor systems, and so on) and the design of a user-centered note management interface, bridging academic discussion and practical design solutions.

![](./16.jpg)


## REFLECTION

**Turning imagination into something real is as tangled and unpredictable as untangling a knot of string.**

Meemo was the first time I took an idea of my own all the way to a product, and building something that simple meant working through problem after problem. Connecting a paper notebook to digital technology ran into technical obstacles I had not expected. Paper thickness, stiffness, and even corner shape all mattered: paper that was too thin would not feed, and square corners caught inside the device. It took a long stretch of trial and error to find the right paper material and shape.

Doing all of it for the first time, I burned a PCB and redid work because of design mistakes, but I kept going on the belief that solving one problem at a time is how you grow. I asked specialists for help when I needed it and improved the technology and the structural design through repeated trial and error. Along the way I handled technical integration with Arduino and Raspberry Pi, internal structural design, and mockup fabrication with 3D printing and CNC machining, which built up solid practical skills. The finished Meemo received the Excellence Award at HCI Korea 2021 Creative Awards.

The project was more than product development; it was a challenge that sharpened both technical skill and creative thinking. And I learned that an idea that looks easy in your head turns, once you build it for real, into a long run of complicated and unpredictable problem-solving — much like untangling a knot of string.
