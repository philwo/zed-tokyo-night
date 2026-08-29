# zed-tokyo-night

Tokyo Night themes for the Zed editor, with five variants: Night,
Storm, Moon, Day (folke's light palette), and Light (enkia's current
light palette).

This is a fork of
[ssaunderss/zed-tokyo-night](https://github.com/ssaunderss/zed-tokyo-night)
with these changes:

- All variants define the same style keys. Git status colors, indent
  guides, and pane borders no longer fall back to Zed's default theme
  in Storm, Moon, and Light.
- The caret, selection, and all eight collaboration player slots use
  the canonical Tokyo Night palette colors of each variant.
- Terminal foregrounds, dim ANSI colors, whitespace invisibles, and
  focused borders are defined instead of falling back to Zed defaults.
- Parameters use the upstream yellow and comments are italic, as in
  the VS Code theme and tokyonight.nvim.
- Diff and version control hunk backgrounds are tinted with the
  tokyonight.nvim 4.0 overlay colors (enkia's overlays for Light)
  instead of the plain background.
- The Moon editor foreground uses folke's fg `#c8d3f5` instead of the
  dim fg_dark, and Storm comments use `#565f89`.
- Focused pane borders and element hover and selection fills use
  palette colors instead of leftovers from the original port.
- A Day variant derived from the Night variant via folke's Day
  palette, matching the Day theme of the tokyo-night-islands
  JetBrains plugin.
- Types, member fields, delimiters, TODO markers, labels, the text
  selection, search matches, scroll bars, and the ANSI palette use
  the same values as the tokyo-night-islands JetBrains theme, so
  both editors render Tokyo Night identically.
- The Light variant uses enkia's current light palette (#e6e7ed
  background), regenerated from the Night variant.
- `scripts/check_variants.py` verifies that the variants stay in sync.

## Install

Zed installs extensions from its official registry, so a fork needs a
dev install:

1. Clone this repository.
2. In Zed, open the command palette and run `zed: install dev extension`.
3. Select the cloned directory.
4. Pick a variant via `theme selector: toggle`.

## Development

After editing `themes/tokyo-night.json`, run:

```sh
python3 scripts/check_variants.py
```

It fails if the variants diverge in style keys, syntax keys, or player
count, or if any value is null or a malformed color.

## Screenshots

### Tokyo Night

![tokyo-night](./screenshots/Night.png)

### Tokyo Night Storm

![tokyo-night-storm](./screenshots/Storm.png)

### Tokyo Night Moon

![tokyo-night-moon](./screenshots/Moon.png)

### Tokyo Night Light

![tokyo-night-light](./screenshots/Light.png)

## Credits

- [enkia/tokyo-night-vscode-theme](https://github.com/enkia/tokyo-night-vscode-theme):
  the original Tokyo Night theme and the Night, Storm, and Light palettes (MIT).
- [folke/tokyonight.nvim](https://github.com/folke/tokyonight.nvim):
  the Moon and Day palettes (Apache 2.0).
- [ssaunderss](https://github.com/ssaunderss): the original Zed port (MIT).

See NOTICE for details.
