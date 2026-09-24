---
title: "design-core"
subtitle: "A design tool where screens are files and the agent draws"
year: "2026"
stack: "Node, YAML, MCP"
status: "Engine and local viewer"
links: [{ label: "GitHub", url: "https://github.com/byjunyoung/design-core" }]
cover: ./cover.png
order: 5
draft: false
---

Every screen of a product is a short text file: what is on it, how it looks when empty, loading, or broken, where each button goes, and which spec it came from. An AI agent writes those files. You look at the drawn result and say "drop that column" — no canvas, no dragging, no design file drifting away from the code.

States don't repeat the whole screen; they say what is different, which is also what a reviewer wants to know. Undecided values are written as `$tbd`, along with who owes the decision. Text-only edits apply at once; structural changes wait for a person to approve.

It doesn't compete with tools that generate screens — it takes their output and keeps it. The lint rules come from [fig](/en/playground/fig-pm/). Today it is an engine and a local viewer, and the name is provisional.
