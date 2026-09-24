---
title: "fig · pm"
subtitle: "Claude Code plugins for design and product work"
year: "2026"
stack: "Claude Code skills, Figma Plugin API, Python"
status: "Public, in use"
links: [{ label: "GitHub", url: "https://github.com/byjunyoung/claude-product-skills" }]
cover: ./cover.png
order: 4
draft: false
---

Most Claude Code plugins aim at the codebase. fig and pm aim at the work beside it — the Figma file you draw in, and the spec you write next to it.

fig covers before and after drawing a screen: the to-draw list first, then the audit and sync. It catches settings carried over when a screen is duplicated, a canonical page left stale, broken arrows, and screens nobody drew. pm writes and verifies specs, then drafts, files, and reconciles the tasks.

A few principles hold it together. Only `/fig:lint` decides right from wrong. Team conventions are observed from the file, not asked, and anything uncertain stays empty. fig never writes to Figma; pm writes only after a preview and an explicit go.

I built these one at a time for my own work. I use them every day, and so does my UX team.

![Three problems fig caught in one section](./01.png)

![Screens nobody drew yet, stubbed as placeholder frames](./02.png)

![fig and pm never call each other; they share two objects in config](./03.png)

![A QA defect report written by checking the dev server against the spec](./04.png)
