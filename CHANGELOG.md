# Changelog

## feat/toc-title-customization

Changes relative to `main`.

### Bug Fixes

- **Cover subtitle overflow**: Added `max_w` constraint to subtitle rendering on the cover page (`_draw_mixed(c, ..., max_w=self.page_w - lx - 20*mm)`), preventing long subtitles from overflowing the page right margin
- **Blank lines silently skipped**: Empty lines between paragraphs were being skipped entirely. They now produce `Spacer(1, 1.5*mm)` vertical space. Inside code blocks, blank lines remain preserved as-is.

### Features

- **Configurable TOC page title**: The TOC page title is no longer hardcoded to Chinese "目  录". It now reads from `self.cfg.get("toc_title", "Contents")`, defaulting to English "Contents". Supported via:
  - CLI argument `--toc-title`
  - Frontmatter keys `toc-title` or `toc_title`
- **TOC header font fix**: TOC page header right-side text now uses "Serif" font and respects `toc_title` config, replacing the previously hardcoded CJK font + "目  录" string

### Documentation

- **SKILL.md**: Configuration reference table now documents `--toc-title` with its frontmatter keys (`toc-title` / `toc_title`) and default value
- **README.md**: Feature list updated from "set title, theme, watermark, cover, TOC" to "set title, theme, watermark, cover, TOC title, TOC"
### Tests

- **New test case**: `tests/09-toc-title-custom.md` tests frontmatter-driven `toc-title` customization across all 3 test themes (warm-academic, nord-frost, tufte)

### Files Changed

| File | Change |
|------|--------|
| `lovstudio-any2pdf/scripts/md2pdf.py` | +15/-7 lines (2 fixes + 2 features) |
| `lovstudio-any2pdf/SKILL.md` | Added `--toc-title` to config table (+1 line) |
| `README.md` | Updated feature list (+1/-1 line) |
| `tests/09-toc-title-custom.md` | New test file for custom TOC title |
