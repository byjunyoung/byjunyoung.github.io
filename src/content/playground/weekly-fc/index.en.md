---
title: "WEEKLY FC"
subtitle: "A web portal for my Saturday futsal team"
year: "2026"
stack: "Astro, React, antd, Google Apps Script"
status: "Live"
links: [{ label: "Site", url: "https://byjunyoung.github.io/weekly-fc/" }, { label: "GitHub", url: "https://github.com/byjunyoung/weekly-fc" }]
cover: ./cover.png
order: 3
draft: false
---

A portal for the futsal team that meets every Saturday — roster, lineups, team picks, and house rules in one place.

There is no sign-up or login. You pick your own name from the roster, and admins enter with a PIN. Attendance is read straight from a pasted KakaoTalk poll. Since the team link travels through KakaoTalk, it had to open cleanly in KakaoTalk's in-app browser.

The verdict on the first version: "this looks like an admin dashboard, not a game." So I rebuilt it around football game screens like FM, EA FC, and eFootball. Real player photos went in and came out a day later, replaced by full-body 24 × 32 pixel characters drawn by hand.

![Lineup screen with eleven starters placed automatically](./01.png)

![Home locker room with your own player, and the roster table with ratings](./02.png)

> Player names in the screenshots have been replaced.
