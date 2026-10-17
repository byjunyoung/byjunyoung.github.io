---
title: "clawd-statusline"
subtitle: "Clawd in your status line, reacting to how much room you have left"
year: "2026"
stack: "Python (standard library)"
status: "Public"
links: [{ label: "GitHub", url: "https://github.com/byjunyoung/clawd-statusline" }]
cover: ./cover.png
order: 6
draft: false
---

Clawd, the mascot already inside Claude Code, standing in your status line. Its pose changes with how much context and usage you have left.

It started with `/buddy`, which has since been removed. `/buddy` never grew and behaved the same however you worked. So Clawd reacts to your actual usage.

It wraps whatever status line you already run instead of replacing it, so your original status line still shows. It uses only Anthropic's four original poses. My own faces looked like a knock-off, and a level card, a wardrobe, and three new creatures were built and dropped too. Each run takes 0.027 s.
