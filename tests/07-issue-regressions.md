---
title: "Issue Regression Coverage"
subtitle: "H4, callouts, images, math, emoji"
author: "any2pdf"
---

# Issue Regression Coverage

This file covers parser paths that previously regressed: inline math $E = mc^2$, emoji ✅, and image parsing.

#### H4 heading should not loop

Content after an H4 heading must render and the parser must keep moving.

> [!NOTE] Obsidian callout
> Callout body supports **bold text**, inline code `value`, and CJK 混排.
> - A nested list item stays inside the callout block.

![GitHub Light preview](../previews/github-light.png)

The paragraph after the image should still be present.

$$
\frac{a^2 + b^2}{c^2} = 1
$$

Final paragraph after display math.
