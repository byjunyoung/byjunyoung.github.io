---
title: "Birdy"
subtitle: "A paper-based messaging device for family communication with older adults"
org: "UNIST"
year: "2021 (1y)"
role: "Lead Researcher"
responsibilities: ["Research", "Product Design", "Prototyping", "Project Management"]
with: "김나눔, 윤혜정 (Research Assistants)"
keywords: ["digital divide", "assistive technology", "inclusive design", "IoT"]
link: { label: "Master's Thesis", url: "https://drive.google.com/file/d/1Ys_DDoIZfHbj7Bq9uYravbCF2H8DK-5J/view?usp=sharing" }
tags: ["Research", "Product Design", "Prototyping", "Project Management"]
kind: case-study
cover: ./cover.jpg
loop: "/media/works/birdy/loop.mp4"
order: 5
draft: false
---

## PROBLEM

Older adults and other users with low digital literacy struggle with messengers because of complex UI layouts, small buttons, and multi-level menus. Contact with family and society thins out, or they miss information they need.

![Diagram of how Birdy links older adults and grandchildren: a handwritten card travels through a messenger to a smartphone](./01.jpg)


## APPROACH

We designed Birdy, a dedicated device used in place of a smartphone. As lead researcher, I worked with two assistant researchers through the following steps.

1. **User research:** Through a literature review, task analysis, and user interviews, we identified the obstacles and needs of users with low digital literacy.
1. **Product design:** Building on the research, we worked out a design that brought together analog elements and physical interaction, and visualized the early concept.
1. **Prototype build and testing:** We built three working mockups and ran a three-week field test with six family pairs.
1. **Data analysis:** Using the qualitative and quantitative data, we analyzed user behavior and experience and evaluated Birdy's effect.

![A hand writing a message on a round paper card](./02.jpg) ![Inserting the written card into the slot on top of Birdy, with the emoji card box beside it](./03.jpg) ![Pushing a card into the Birdy body](./04.jpg)

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/YvDX9E_5jvk?rel=0&modestbranding=1" title="Film showing how Birdy is used" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>


## SOLUTION

Birdy is a desktop messaging device for older adults. Handwriting on paper with a pen is the input, and that handwriting is what the family receives. The design rested on three decisions.

**The screen shows one message and nothing else.** Display size and button layout follow how older adults take in information, and a message-only display keeps information from piling up. Received and sent states are shown by LED light diffused through the translucent acrylic body.

**The handwriting stays as it is.** A message written on a 66mm paper card is converted and sent by Birdy, with the texture and character of the writing intact. Twenty emoji cards that come with the device add feeling.

**A few buttons do everything.** Physical buttons for navigation and a simple interface cut the steps down, and received messages appear large on the display.

![Close-up of the round-cornered slot the card goes into](./06.jpg) ![Hands leafing through emoji cards printed with a heart and faces](./05.jpg) ![The grandchild's phone thread, where the handwritten message arrives as an image](./07.jpg)


## IMPLEMENTATION

Development ran along three tracks: hardware, software, and product design. When a paper card goes into the slot, an IR sensor and a linear motor detect and align it, and a wide-angle camera with a ring LED captures it in the narrow, dark interior. Messages travel through the Telegram API, scanned images are post-processed with OpenCV, and Google Teachable Machine recognizes the handwriting and emoji.

Parts were modeled in Fusion 360 and made by 3D printing and CNC machining, with the structure settled through repeated prototyping. The design is modular for maintenance and fabrication.

![Birdy's internal parts and exploded drawing: high-luminance LED, camera with a ring LED, IR sensor, linear stepping motor, and the control boards](./12.jpg)

![Birdy's system diagram: motors and sensors on the Arduino, camera and display on the Raspberry Pi, connected through the messenger server and the recognition model](./13.jpg)

![An early foam-board mockup with a message on the display](./08.jpg) ![Testing the prototype at a monitor, the recognized handwriting showing on the device](./09.jpg)

![Parts laid out on the workbench: ring LED, boards, housings, and tools](./10.jpeg) ![Housing and handle parts made in several colors](./11.jpg)


## IMPACT

Over the three-week field test, how much the older participants messaged and what they talked about both changed.

**About three times the contact.** The older adults in the six family pairs exchanged an average of 21.5 messages a week, about three times as often as before Birdy. One grandparent went from one or two phone calls a week to 35 messages.

**Wider conversations.** With the constraints of time and place gone, conversation moved from greetings to everyday life, health, and family news. "Have you eaten?" gave way to a grandchild's exam results and hobbies.

**What handwriting and paper carried.** 70% of participants said handwriting helped them express feeling, and some drew flowers or changed the size of their letters to do it. 83% kept the paper messages they received; one grandparent kept a grandchild's notes in a drawer.

![A field-test participant writing a message on a card at a desk](./18.jpg) ![Birdy on a table by the living-room window](./19.jpg) ![Birdy and its card box installed on a shelf in a participant's home](./20.jpg)

![Birdy and the emoji box on a chest of drawers](./21.jpg) ![A participant using Birdy on a wooden porch](./22.jpg) ![Birdy on a bedroom dresser](./23.jpg)

![Messages per week over the three-week field test, one line per family](./15.jpg)

![Presenting the study results](./24.jpg)


## REFLECTION

**Can a hardware product be more than a device, a tool that connects feelings?**

Birdy was the first time I went through every stage of getting a hardware product into a user's hands. From design to prototyping, user training, and feedback collection, I had to secure the stability of an IoT device and the user experience at the same time. Repeated prototype tests and firmware tuning showed me how much it matters to design hardware and software together. It was also the first project that made me think about what it means to design a solution to a social problem with technology.
