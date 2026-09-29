---
title: "WEEKLY FC"
subtitle: "A web portal for my Saturday futsal team"
year: "2026"
stack: "Astro, React, antd, Supabase"
status: "Live"
links: [{ label: "Site", url: "https://byjunyoung.github.io/weekly-fc/" }, { label: "GitHub", url: "https://github.com/byjunyoung/weekly-fc" }]
cover: ./cover.png
order: 3
draft: false
---

A portal for the futsal team that meets every Saturday — roster, lineups, match records, tactics, and house rules in one place.

The verdict on the first version: "this looks like an admin dashboard, not a game." So I rebuilt it around football game screens like FM, EA FC, and eFootball. Real player photos went in and came out a day later, replaced by full-body 24 × 32 pixel characters drawn by hand. Honestly, once it turned into pixel art, building it got a lot more fun for me too.

Ratings aren't set by me — the team sets them. In the tier game you pick one of two players for a question like "Who's faster?", the numbers shift on the spot, and the ranking splits everyone into tiers from S to D. Player cards follow the FIFA card layout, and when one stat clearly stands out within the team, the player earns a title like Winger or Poacher.

![Player page with the rating card and title](./01.png)

![Tier game, picking one of two players](./02.png)

Each day gets one match, and the players who played that day vote for POTM on match day. The winner gets +1 on every stat the next day. Upload the match video to YouTube and it attaches itself to that day's match.

![Match records with POTM and the match video](./03.png)

The good news is that the team actually uses it. In the six days since the tier game opened on September 24, 361 duels were played and ratings moved 987 times. The rough numbers I first put in were re-ranked by teammates in under a week. From day one it ran at 40–90 duels a day, stopping only on Saturdays when we play. That said, six people still do most of it, and one of them played 150. With a few people carrying the load, widening participation looks like the next challenge. So far 9 of 31 players have linked an account.

Since the team link travels mostly through KakaoTalk, it had to open cleanly in KakaoTalk's in-app browser. Sign-in is a single code sent by email, and you link your account by picking your name from the roster.

> Player names in the screenshots have been replaced.
